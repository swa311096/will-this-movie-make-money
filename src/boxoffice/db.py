import sqlite3
from pathlib import Path


def connect(db_path: str) -> sqlite3.Connection:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS movies_raw (
            movie_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            studio TEXT NOT NULL,
            release_date TEXT,
            numbers_url TEXT NOT NULL,
            budget_numbers_usd REAL,
            opening_weekend_numbers_usd REAL,
            domestic_numbers_usd REAL,
            worldwide_numbers_usd REAL,
            ingested_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS daily_gross (
            movie_id TEXT NOT NULL,
            gross_date TEXT NOT NULL,
            day_number INTEGER,
            rank_text TEXT,
            gross_usd REAL,
            percent_change REAL,
            theaters INTEGER,
            per_theater_usd REAL,
            total_gross_usd REAL,
            PRIMARY KEY (movie_id, gross_date),
            FOREIGN KEY (movie_id) REFERENCES movies_raw(movie_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS training_examples (
            movie_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            release_date TEXT,
            as_of_day INTEGER NOT NULL,
            opening_weekend_usd REAL,
            day3_total_usd REAL,
            day7_total_usd REAL,
            fri_sat_change_pct REAL,
            sat_sun_change_pct REAL,
            sun_mon_change_pct REAL,
            theaters_day1 INTEGER,
            theaters_day7 INTEGER,
            release_month INTEGER,
            is_holiday_window INTEGER,
            domestic_total_usd REAL,
            international_total_usd REAL,
            worldwide_total_usd REAL,
            domestic_multiplier REAL,
            intl_dom_ratio REAL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (movie_id) REFERENCES movies_raw(movie_id) ON DELETE CASCADE
        );
        """
    )
    conn.commit()
