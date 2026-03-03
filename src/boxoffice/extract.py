import datetime as dt
import hashlib
import time
from urllib.parse import urldefrag
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from .utils import parse_date, parse_money, parse_percent


BASE_URL = "https://www.the-numbers.com"
UNIVERSAL_URL = f"{BASE_URL}/movies/production-company/Universal-Pictures"


@dataclass
class MovieSeed:
    movie_id: str
    title: str
    studio: str
    release_date: Optional[dt.date]
    numbers_url: str
    budget_numbers_usd: Optional[float]
    opening_weekend_numbers_usd: Optional[float]
    domestic_numbers_usd: Optional[float]
    worldwide_numbers_usd: Optional[float]


@dataclass
class DailyGrossPoint:
    movie_id: str
    gross_date: dt.date
    day_number: Optional[int]
    rank_text: str
    gross_usd: Optional[float]
    percent_change: Optional[float]
    theaters: Optional[int]
    per_theater_usd: Optional[float]
    total_gross_usd: Optional[float]


class NumbersClient:
    def __init__(self, timeout_s: int = 30, use_playwright: bool = False):
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": "wtmmm/0.1"})
        self.timeout_s = timeout_s
        self.use_playwright = use_playwright

    def _get(self, url: str) -> str:
        resp = self._session.get(url, timeout=self.timeout_s)
        resp.raise_for_status()
        return resp.text

    def _get_page(self, url: str) -> str:
        html = self._get(url)
        if self.use_playwright and ("<title></title>" in html or "Access denied" in html[:600]):
            rendered = self._get_playwright(url)
            if rendered:
                return rendered
        return html

    def _get_playwright(self, url: str) -> Optional[str]:
        try:
            from playwright.sync_api import sync_playwright
        except Exception:
            return None

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=self.timeout_s * 1000)
            html = page.content()
            browser.close()
            return html

    @staticmethod
    def _extract_daily_table(soup: BeautifulSoup):
        for table in soup.find_all("table"):
            headers = [th.get_text(" ", strip=True) for th in table.find_all("th")]
            header_set = set(headers)
            if {"Date", "Gross", "Total Gross"}.issubset(header_set):
                return table
        return None

    def _find_daily_table_and_link(self, soup: BeautifulSoup) -> Tuple[Optional[Tag], Optional[str]]:
        target = self._extract_daily_table(soup)
        domestic_link = None
        if target is None:
            for a in soup.find_all("a"):
                text = a.get_text(" ", strip=True).lower()
                href = a.get("href") or ""
                if "domestic performance" in text and href:
                    domestic_link = href if href.startswith("http") else f"{BASE_URL}{href}"
                    break
        return target, domestic_link

    @staticmethod
    def _movie_id(title: str, release_date: Optional[dt.date]) -> str:
        basis = f"{title}|{release_date.isoformat() if release_date else 'na'}"
        return hashlib.sha1(basis.encode("utf-8")).hexdigest()[:16]

    def fetch_universal_titles(self, start_date: dt.date, end_date: dt.date) -> List[MovieSeed]:
        html = self._get_page(UNIVERSAL_URL)
        soup = BeautifulSoup(html, "html.parser")

        target = None
        for table in soup.find_all("table"):
            headers = [th.get_text(" ", strip=True) for th in table.find_all("th")]
            if "Release Date" in headers and "Worldwide Box Office" in headers:
                target = table
                break

        if target is None:
            raise RuntimeError("Could not find Universal table on The Numbers page")

        output: List[MovieSeed] = []
        for tr in target.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 6:
                continue

            release_date = parse_date(tds[0].get_text(" ", strip=True))
            if not release_date:
                continue
            if release_date < start_date or release_date > end_date:
                continue

            title_cell = tds[1]
            title = title_cell.get_text(" ", strip=True)
            if title.lower().startswith("untitled"):
                continue

            anchor = title_cell.find("a")
            if not anchor or not anchor.get("href"):
                continue

            numbers_url = f"{BASE_URL}{anchor['href']}"
            movie_id = self._movie_id(title, release_date)

            output.append(
                MovieSeed(
                    movie_id=movie_id,
                    title=title,
                    studio="Universal Pictures",
                    release_date=release_date,
                    numbers_url=numbers_url,
                    budget_numbers_usd=parse_money(tds[2].get_text(" ", strip=True)),
                    opening_weekend_numbers_usd=parse_money(tds[3].get_text(" ", strip=True)),
                    domestic_numbers_usd=parse_money(tds[4].get_text(" ", strip=True)),
                    worldwide_numbers_usd=parse_money(tds[5].get_text(" ", strip=True)),
                )
            )

        return output

    def fetch_daily_domestic(self, movie: MovieSeed) -> List[DailyGrossPoint]:
        base_url, _ = urldefrag(movie.numbers_url)
        html = self._get_page(base_url)
        soup = BeautifulSoup(html, "html.parser")

        target, domestic_link = self._find_daily_table_and_link(soup)
        if target is None and domestic_link:
            detail_html = self._get_page(domestic_link)
            detail_soup = BeautifulSoup(detail_html, "html.parser")
            target = self._extract_daily_table(detail_soup)

        if target is None:
            box_office_url = f"{base_url}#tab=box-office"
            fallback_html = self._get_page(box_office_url)
            fallback_soup = BeautifulSoup(fallback_html, "html.parser")
            target = self._extract_daily_table(fallback_soup)

        if target is None:
            return []

        rows: List[DailyGrossPoint] = []
        for tr in target.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 8:
                continue

            date_value = parse_date(tds[0].get_text(" ", strip=True))
            if not date_value:
                continue

            day_number_raw = tds[7].get_text(" ", strip=True)
            day_number = int(day_number_raw) if day_number_raw.isdigit() else None

            theaters_txt = tds[4].get_text(" ", strip=True).replace(",", "")
            theaters = int(theaters_txt) if theaters_txt.isdigit() else None

            rows.append(
                DailyGrossPoint(
                    movie_id=movie.movie_id,
                    gross_date=date_value,
                    day_number=day_number,
                    rank_text=tds[1].get_text(" ", strip=True),
                    gross_usd=parse_money(tds[2].get_text(" ", strip=True)),
                    percent_change=parse_percent(tds[3].get_text(" ", strip=True)),
                    theaters=theaters,
                    per_theater_usd=parse_money(tds[5].get_text(" ", strip=True)),
                    total_gross_usd=parse_money(tds[6].get_text(" ", strip=True)),
                )
            )

        rows.sort(key=lambda r: r.gross_date)
        return rows

    def fetch_daily_for_many(self, movies: Iterable[MovieSeed], sleep_s: float = 0.25) -> List[DailyGrossPoint]:
        all_rows: List[DailyGrossPoint] = []
        for movie in movies:
            rows = self.fetch_daily_domestic(movie)
            all_rows.extend(rows)
            time.sleep(sleep_s)
        return all_rows
