# KI-Tool-Analysen

Jeden Sonntag fünf KI-Tools, eingeordnet nach Nutzen, Kosten und Datenschutz. Eine Publikation von
Roger Basler de Roca (#fragRoger).

- Website: https://rogerbasler.github.io/ki-tool-analysen/
- Archiv: https://rogerbasler.github.io/ki-tool-analysen/archiv.html
- RSS: https://rogerbasler.github.io/ki-tool-analysen/feed.xml

## Inhalt

Pro Woche genau ein Tool in jeder der fünf Kategorien Text, Design, Data / Wissen, Recherche und Agents.
Jede Analyse enthält Kurzbeschreibung, Nutzungsszenarien, Pricing, Datenschutz (Serverstandort, DSGVO/DSG,
Self-Hosting), Stärken, Schwächen, Einschätzung für die Praxis und eine Relevanzbewertung von 1 bis 10.
Das Archiv reicht zurück bis KW 48/2025 und ist nach Tool, Kategorie, Jahr und Bewertung durchsuchbar.

## Betrieb

Die Ausgabe entsteht jeden Sonntagmorgen in einem geplanten Claude-Lauf. Der komplette Ablauf, das Datenschema
und die Schreibregeln stehen in [`CLAUDE.md`](CLAUDE.md). Bis Oktober 2026 lief die Produktion über Manus;
alle Ausgaben aus dieser Zeit wurden in das neue Datenformat übernommen.

## Lokal bauen

```bash
pip install -r pipeline/requirements.txt
python3 pipeline/validate_week.py data/weeks/2026-10-18.json
python3 pipeline/build_site.py
python3 -m http.server 8000   # dann http://localhost:8000
```

Generierte Dateien (`index.html`, `archiv.html`, `archiv/20*/`, `feed.xml`, `sitemap.xml`, `methode.html`,
`impressum.html`, `datenschutz.html`, `404.html`) nicht von Hand bearbeiten.
