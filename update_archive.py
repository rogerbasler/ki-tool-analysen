#!/usr/bin/env python3
"""
Update archive-index.json with new KW 05/2026 entry
"""

import json

# Load existing archive
with open('archiv/data/archive-index.json', 'r', encoding='utf-8') as f:
    archive = json.load(f)

# New entry for KW 05/2026
new_entry = {
    "kw": 5,
    "jahr": 2026,
    "datum": "2026-02-01",
    "url": "index.html",
    "tools": [
        {
            "name": "OpenAI Prism",
            "kategorie": "Text",
            "bewertung": 9.0,
            "kurzbeschreibung": "KI-nativer Workspace für wissenschaftliches Schreiben mit GPT-5.2"
        },
        {
            "name": "AirMusic v1.1",
            "kategorie": "Design",
            "bewertung": 7.5,
            "kurzbeschreibung": "KI-Musikgenerator mit royalty-free Lizenzierung"
        },
        {
            "name": "Pandada AI",
            "kategorie": "Data",
            "bewertung": 8.5,
            "kurzbeschreibung": "KI-gestützte Datenanalyse ohne Programmierkenntnisse"
        },
        {
            "name": "The Prompting Company",
            "kategorie": "Recherche",
            "bewertung": 8.0,
            "kurzbeschreibung": "SEO für das KI-Zeitalter - Optimierung für ChatGPT-Zitate"
        },
        {
            "name": "Agentic Vision in Gemini",
            "kategorie": "Agents",
            "bewertung": 9.0,
            "kurzbeschreibung": "Google Major Update für agentenähnliche visuelle Interaktion"
        }
    ],
    "highlights": "OpenAI Prism & Agentic Vision in Gemini (9/10)",
    "trend": "KI-native Arbeitsumgebungen und agentenähnliche Systeme"
}

# Add new entry at the beginning (newest first)
archive['analysen'].insert(0, new_entry)

# Save updated archive
with open('archiv/data/archive-index.json', 'w', encoding='utf-8') as f:
    json.dump(archive, f, ensure_ascii=False, indent=2)

print("✅ Archiv erfolgreich aktualisiert!")
print(f"   Neue Einträge: {len(archive['analysen'])}")
