# KI-Tool-Analysen

Jeden Sonntag sechs KI-Tools, eingeordnet nach Nutzen, Kosten und Datenschutz. Eine Publikation von
Roger Basler de Roca (#fragRoger).

- Website: https://tools.fragroger.ai (Deutsch) und https://tools.fragroger.ai/en/ (English)
- Archiv: https://tools.fragroger.ai/archiv.html und https://tools.fragroger.ai/en/archive.html
- RSS: https://tools.fragroger.ai/feed.xml und https://tools.fragroger.ai/en/feed.xml

## Domain

`CNAME` enthält `tools.fragroger.ai`. Im DNS von fragroger.ai braucht es einen CNAME-Record `tools` auf
`rogerbasler.github.io`. Danach leitet GitHub die alte Adresse rogerbasler.github.io/ki-tool-analysen/ automatisch
um. In den Pages-Einstellungen "Enforce HTTPS" aktivieren, sobald das Zertifikat ausgestellt ist.

## Inhalt

Pro Woche genau ein Tool in jeder der sechs Kategorien Text, Design, Data / Wissen, Recherche, Agents und Transkription (seit Oktober 2026; zuvor fünf Kategorien).
Jede Analyse enthält Kurzbeschreibung, Nutzungsszenarien, Pricing, Datenschutz (Serverstandort, DSGVO/DSG,
Self-Hosting), Stärken, Schwächen, Einschätzung für die Praxis und eine Relevanzbewertung von 1 bis 10.
Jede Ausgabe erscheint auf Deutsch und Englisch. Das Archiv reicht zurück bis KW 48/2025 und ist nach Tool, Kategorie, Jahr und Bewertung durchsuchbar.

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
