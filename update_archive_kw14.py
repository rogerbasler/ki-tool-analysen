#!/usr/bin/env python3
"""
Aktualisiert archive-index.json für KW 14/2026 und archiviert die KW 13 HTML.
"""
import json
import shutil
import os

# Schritt 1: Aktuelle index.html (KW 14) als Archiv-Kopie speichern
# (wird nach dem nächsten Update benötigt — jetzt speichern wir KW 13 Archiv)
# KW 13 ist bereits archiviert als archiv/2026/kw13-2026-03-29.html

# Schritt 2: Archive-Index aktualisieren
archive_path = '/home/ubuntu/ki-tool-website/archiv/data/archive-index.json'

with open(archive_path, 'r', encoding='utf-8') as f:
    archive = json.load(f)

# Neuer Eintrag für KW 14
new_entry = {
    "kw": 14,
    "jahr": 2026,
    "datum": "2026-04-05",
    "url": "index.html",
    "tools": [
        {
            "name": "Atomic Chat",
            "kategorie": "Text",
            "bewertung": 8.5,
            "kurzbeschreibung": "Open-Source ChatGPT-Alternative — 1.000+ KI-Modelle vollständig offline auf dem Mac, zero data exfiltration"
        },
        {
            "name": "Noon",
            "kategorie": "Design",
            "bewertung": 7.5,
            "kurzbeschreibung": "Das erste KI-native Design-Tool auf Production-Code — $44M Funding, aus dem Stealth-Modus"
        },
        {
            "name": "Google Gemma 4",
            "kategorie": "Data",
            "bewertung": 9.5,
            "kurzbeschreibung": "Frontier Open-Source-KI unter Apache 2.0 — von Raspberry Pi bis H100, DSGVO-konform on-premise"
        },
        {
            "name": "Perplexity Computer for Taxes",
            "kategorie": "Recherche",
            "bewertung": 7.8,
            "kurzbeschreibung": "Erster agentischer Steuer-Assistent — IRS-Formulare ausfüllen, Erklärungen prüfen, Abzüge optimieren"
        },
        {
            "name": "Holo3 by H Company",
            "kategorie": "Agents",
            "bewertung": 9.2,
            "kurzbeschreibung": "State-of-the-Art Computer-Use-Agent — 78,85% OSWorld, Open Source Apache 2.0, europäisches Unternehmen"
        }
    ],
    "highlights": "Google Gemma 4 (9.5/10): Historischer Meilenstein — Frontier Open-Source-KI unter Apache 2.0, vollständig DSGVO-konform on-premise betreibbar",
    "trend": "Open-Source überholt Cloud-KI: Gemma 4 und Holo3 zeigen, dass frontier-nahe KI-Qualität jetzt on-premise, kostenlos und ohne Lizenzrisiko verfügbar ist"
}

# Alten KW 13 Eintrag auf Archiv-URL umstellen
for entry in archive['analysen']:
    if entry['kw'] == 13 and entry['jahr'] == 2026:
        entry['url'] = 'archiv/2026/kw13-2026-03-29.html'
        print(f"✅ KW 13 URL auf Archiv umgestellt")
        break

# Neuen KW 14 Eintrag vorne einfügen
archive['analysen'].insert(0, new_entry)

# JSON speichern
with open(archive_path, 'w', encoding='utf-8') as f:
    json.dump(archive, f, ensure_ascii=False, indent=2)

print(f"✅ archive-index.json aktualisiert: {len(archive['analysen'])} Einträge")
print(f"✅ Neuester Eintrag: KW {archive['analysen'][0]['kw']}/{archive['analysen'][0]['jahr']}")
