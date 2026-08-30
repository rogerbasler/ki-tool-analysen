#!/usr/bin/env python3
"""Archiviert die bestehende Homepage und ergänzt den Wochenindex für KW 35/2026."""
from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path("/home/ubuntu/ki-tool-website")
CURRENT_DATE = date(2026, 8, 30)
CURRENT_KW = 35
CURRENT_YEAR = 2026
ARCHIVE_DIR = ROOT / "archiv" / str(CURRENT_YEAR)
ARCHIVE_FILE = ARCHIVE_DIR / f"kw{CURRENT_KW}-{CURRENT_DATE.isoformat()}.html"
INDEX_FILE = ROOT / "archiv" / "data" / "archive-index.json"

ENTRY = {
    "kw": CURRENT_KW,
    "jahr": CURRENT_YEAR,
    "datum": CURRENT_DATE.isoformat(),
    "url": f"archiv/{CURRENT_YEAR}/kw{CURRENT_KW}-{CURRENT_DATE.isoformat()}.html",
    "tools": [
        {
            "name": "Claude mit Memory",
            "kategorie": "Text",
            "bewertung": 8.5,
            "kurzbeschreibung": "Kontrollierbarer, geteilter Arbeitskontext über Claude Chat und Cowork hinweg",
        },
        {
            "name": "Midjourney V8.2 Edit Model",
            "kategorie": "Design",
            "bewertung": 8.5,
            "kurzbeschreibung": "Instruktionsbasierte Bildbearbeitung mit bis zu vier Referenzbildern",
        },
        {
            "name": "PageIndex SDK Local",
            "kategorie": "Data / Wissen",
            "bewertung": 8.5,
            "kurzbeschreibung": "Lokal ausführbares, reasoning-basiertes Dokumentenretrieval mit Seitenzitaten",
        },
        {
            "name": "Lenz",
            "kategorie": "Recherche",
            "bewertung": 8.0,
            "kurzbeschreibung": "Mehrstufige, quellenbasierte Faktenprüfung für KI-generierte Behauptungen",
        },
        {
            "name": "Construct Computer",
            "kategorie": "Agents",
            "bewertung": 8.0,
            "kurzbeschreibung": "Agentischer Arbeitsbereich mit persistentem Cloud-Computer und nachvollziehbaren Abläufen",
        },
    ],
    "highlights": "PageIndex SDK Local (8.5/10): Private Dokumentenarbeit wird durch lokalen Index, eigene Modellschlüssel und Seitenzitate deutlich steuerbarer.",
    "trend": "KI-Tools verlagern ihren Wert von der einzelnen Antwort in den kontrollierbaren Arbeitskontext: editierbarer Speicher, nachvollziehbare Quellen, lokale Datenhaltung und persistente Workspaces.",
}

ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
shutil.copy2(ROOT / "index.html", ARCHIVE_FILE)

with INDEX_FILE.open("r", encoding="utf-8") as handle:
    data = json.load(handle)

analysen = [item for item in data.get("analysen", []) if not (
    item.get("kw") == CURRENT_KW
    and item.get("jahr") == CURRENT_YEAR
    and item.get("datum") == CURRENT_DATE.isoformat()
)]
data["analysen"] = [ENTRY, *analysen]

with INDEX_FILE.open("w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=2)
    handle.write("\n")

print(f"Archiv erstellt: {ARCHIVE_FILE}")
print(f"Archivindex ergänzt: KW {CURRENT_KW}/{CURRENT_YEAR}")
