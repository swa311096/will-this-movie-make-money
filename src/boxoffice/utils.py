import datetime as dt
import re
from typing import Optional


def parse_date(text: str) -> Optional[dt.date]:
    text = (text or "").strip()
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return dt.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def parse_money(value: str) -> Optional[float]:
    value = (value or "").replace(",", "").strip()
    if not value or value in {"-", "N/A", "n/a"}:
        return None

    negative = value.startswith("(") and value.endswith(")")
    value = value.strip("()")
    value = value.replace("$", "")

    m = re.match(r"^(\d+(?:\.\d+)?)(?:\s*(million|billion|m|bn))?$", value, re.I)
    if m:
        number = float(m.group(1))
        unit = (m.group(2) or "").lower()
        if unit in {"million", "m"}:
            number *= 1_000_000
        elif unit in {"billion", "bn"}:
            number *= 1_000_000_000
        return -number if negative else number

    digits = re.sub(r"[^\d.]", "", value)
    if not digits:
        return None

    number = float(digits)
    return -number if negative else number


def parse_percent(value: str) -> Optional[float]:
    value = (value or "").strip().replace("%", "")
    if not value or value == "-":
        return None
    try:
        return float(value) / 100.0
    except ValueError:
        return None
