#!/usr/bin/env python3
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from boxoffice.db import connect
from boxoffice.train import FEATURE_COLUMNS, load_model


def parse_args():
    p = argparse.ArgumentParser(description="Evaluate saved baseline models against current training table")
    p.add_argument("--db", default="data/processed/boxoffice.sqlite")
    p.add_argument("--model-dir", default="data/models")
    p.add_argument("--top-errors", type=int, default=5)
    return p.parse_args()


def metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    denom = np.maximum(np.abs(y_true), 1.0)
    err = y_pred - y_true
    return {
        "count": int(len(y_true)),
        "mae": float(np.mean(np.abs(err))),
        "rmse": float(math.sqrt(np.mean(err * err))),
        "mape_pct": float(np.mean(np.abs(err) / denom) * 100.0),
    }


def fetch_eval_frame(conn) -> pd.DataFrame:
    return pd.read_sql_query(
        """
        SELECT
            movie_id,
            title,
            release_date,
            opening_weekend_usd,
            day3_total_usd,
            day7_total_usd,
            fri_sat_change_pct,
            sat_sun_change_pct,
            sun_mon_change_pct,
            theaters_day1,
            theaters_day7,
            release_month,
            is_holiday_window,
            domestic_total_usd,
            international_total_usd,
            worldwide_total_usd,
            domestic_multiplier,
            intl_dom_ratio
        FROM training_examples
        """,
        conn,
    )


def main() -> int:
    args = parse_args()
    conn = connect(args.db)

    frame = fetch_eval_frame(conn)
    summary = {
        "rows": {
            "training_examples": int(len(frame)),
            "with_domestic_multiplier": int(frame["domestic_multiplier"].notna().sum()),
            "with_intl_dom_ratio": int(frame["intl_dom_ratio"].notna().sum()),
        },
        "models": {},
        "notes": [
            "Metrics are computed on current table rows using saved models (not strict out-of-sample backtest)."
        ],
    }

    model_multiplier_path = Path(args.model_dir) / "domestic_multiplier_rf.joblib"
    model_ratio_path = Path(args.model_dir) / "intl_dom_ratio_rf.joblib"

    if model_multiplier_path.exists():
        model_multiplier = load_model(str(model_multiplier_path))
        dom_df = frame.dropna(subset=["domestic_multiplier"]).copy()
        if not dom_df.empty:
            dom_pred = model_multiplier.predict(dom_df[FEATURE_COLUMNS])
            summary["models"]["domestic_multiplier"] = metrics(
                dom_df["domestic_multiplier"].to_numpy(dtype=float),
                dom_pred,
            )

            dom_df["pred_domestic_multiplier"] = dom_pred
            dom_df["pred_domestic_total"] = dom_df["opening_weekend_usd"] * dom_df["pred_domestic_multiplier"]
            if dom_df["domestic_total_usd"].notna().any():
                dom_total_df = dom_df.dropna(subset=["domestic_total_usd", "pred_domestic_total"])
                summary["models"]["domestic_total_from_multiplier"] = metrics(
                    dom_total_df["domestic_total_usd"].to_numpy(dtype=float),
                    dom_total_df["pred_domestic_total"].to_numpy(dtype=float),
                )

            dom_df["abs_pct_error"] = (
                np.abs(dom_df["pred_domestic_multiplier"] - dom_df["domestic_multiplier"]) /
                np.maximum(np.abs(dom_df["domestic_multiplier"]), 1.0)
            )
            worst = dom_df.sort_values("abs_pct_error", ascending=False).head(args.top_errors)
            summary["models"]["domestic_multiplier"]["worst_examples"] = [
                {
                    "title": r.title,
                    "release_date": r.release_date,
                    "actual": float(r.domestic_multiplier),
                    "predicted": float(r.pred_domestic_multiplier),
                    "abs_pct_error": float(r.abs_pct_error * 100.0),
                }
                for r in worst.itertuples(index=False)
            ]

    if model_ratio_path.exists():
        model_ratio = load_model(str(model_ratio_path))
        ratio_df = frame.dropna(subset=["intl_dom_ratio"]).copy()
        if not ratio_df.empty:
            ratio_pred = model_ratio.predict(ratio_df[FEATURE_COLUMNS])
            summary["models"]["intl_dom_ratio"] = metrics(
                ratio_df["intl_dom_ratio"].to_numpy(dtype=float),
                ratio_pred,
            )

    if model_multiplier_path.exists() and model_ratio_path.exists():
        both = frame.dropna(subset=["opening_weekend_usd", "domestic_total_usd", "international_total_usd"]).copy()
        if not both.empty:
            model_multiplier = load_model(str(model_multiplier_path))
            model_ratio = load_model(str(model_ratio_path))
            both["pred_multiplier"] = model_multiplier.predict(both[FEATURE_COLUMNS])
            both["pred_ratio"] = model_ratio.predict(both[FEATURE_COLUMNS])
            both["pred_domestic"] = both["opening_weekend_usd"] * both["pred_multiplier"]
            both["pred_international"] = both["pred_domestic"] * both["pred_ratio"]
            both["pred_worldwide"] = both["pred_domestic"] + both["pred_international"]

            summary["models"]["combined_totals"] = {
                "domestic": metrics(both["domestic_total_usd"].to_numpy(dtype=float), both["pred_domestic"].to_numpy(dtype=float)),
                "international": metrics(
                    both["international_total_usd"].to_numpy(dtype=float),
                    both["pred_international"].to_numpy(dtype=float),
                ),
            }
            ww = both.dropna(subset=["worldwide_total_usd"])
            if not ww.empty:
                summary["models"]["combined_totals"]["worldwide"] = metrics(
                    ww["worldwide_total_usd"].to_numpy(dtype=float),
                    ww["pred_worldwide"].to_numpy(dtype=float),
                )

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
