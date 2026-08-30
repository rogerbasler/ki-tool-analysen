#!/usr/bin/env python3
"""Prüft die konsistente Wochenaktualisierung für KW 35/2026."""
from __future__ import annotations

import json
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path("/home/ubuntu/ki-tool-website")
html_path = ROOT / "index.html"
archive_index_path = ROOT / "archiv" / "data" / "archive-index.json"
analysis_path = ROOT / "archiv" / "data" / "ki-tool-analysen-2026-08-30.md"
archive_path = ROOT / "archiv" / "2026" / "kw35-2026-08-30.html"

html = html_path.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
assert soup.title and "KW 35/2026" in soup.title.text
assert "30.08.2026" in soup.get_text(" ")
cards = soup.select(".tool-card")
assert len(cards) == 5, f"Erwartet 5 Tool-Karten, erhalten: {len(cards)}"
expected_categories = ["TEXT", "DESIGN", "DATA / WISSEN", "RECHERCHE", "AGENTS"]
actual_categories = [card.select_one(".category-label").get_text(strip=True) for card in cards]
assert actual_categories == expected_categories, actual_categories
expected_tools = ["Claude mit Memory", "Midjourney V8.2 Edit Model", "PageIndex SDK Local", "Lenz", "Construct Computer"]
actual_tools = [card.select_one(".tool-name").get_text(strip=True) for card in cards]
assert actual_tools == expected_tools, actual_tools
assert soup.select_one('a[href="archiv/data/ki-tool-analysen-2026-08-30.md"]')
assert archive_path.exists(), "Archivkopie der vorherigen Homepage fehlt"
assert analysis_path.exists(), "Archivierte Markdown-Analyse fehlt"
analysis = analysis_path.read_text(encoding="utf-8")
for heading in expected_tools:
    assert heading in analysis, f"Abschnitt fehlt: {heading}"
assert "## Quellen" in analysis
with archive_index_path.open(encoding="utf-8") as handle:
    archive_index = json.load(handle)
first = archive_index["analysen"][0]
assert first["kw"] == 35 and first["jahr"] == 2026 and first["datum"] == "2026-08-30"
assert first["url"] == "archiv/2026/kw35-2026-08-30.html"
assert len(first["tools"]) == 5
print("OK: Homepage, Analyse, Archivkopie und Archivindex sind für KW 35/2026 konsistent.")
