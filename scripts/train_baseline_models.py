#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from boxoffice.db import connect
from boxoffice.train import train_two_baselines
from boxoffice.transform import fetch_training_frame


def parse_args():
    p = argparse.ArgumentParser(description="Train baseline multiplier + intl/dom models")
    p.add_argument("--db", default="data/processed/boxoffice.sqlite")
    p.add_argument("--model-dir", default="data/models")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    conn = connect(args.db)
    df = fetch_training_frame(conn)
    metrics = train_two_baselines(df, model_dir=args.model_dir)
    print(json.dumps(metrics, indent=2))
    print(f"Saved models to: {args.model_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
