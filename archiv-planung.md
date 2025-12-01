# KI-Tool-Analysen - Archiv-Struktur & Workflow

## Archiv-Struktur

### Repository-Organisation

```
ki-tool-analysen/
├── index.html                    # Homepage (aktuelle Woche)
├── style.css                     # Haupt-Stylesheet
├── script.js                     # Haupt-JavaScript
├── archiv.html                   # Archiv-Übersichtsseite
├── archiv/                       # Archiv-Verzeichnis
│   ├── 2025/                     # Jahr
│   │   ├── kw49-2025-12-01.html # Woche 49
│   │   ├── kw50-2025-12-08.html # Woche 50
│   │   ├── kw51-2025-12-15.html # Woche 51
│   │   └── ...
│   └── data/                     # JSON-Daten für dynamisches Laden
│       ├── 2025-kw49.json
│       ├── 2025-kw50.json
│       └── archive-index.json   # Index aller Analysen
└── README.md
```

### Datenformat: archive-index.json

```json
{
  "analysen": [
    {
      "kw": 49,
      "jahr": 2025,
      "datum": "2025-12-01",
      "url": "archiv/2025/kw49-2025-12-01.html",
      "tools": [
        {
          "name": "Contenov",
          "kategorie": "Text",
          "bewertung": 7
        },
        {
          "name": "Alai",
          "kategorie": "Design",
          "bewertung": 8
        },
        {
          "name": "TwelveLabs Marengo 3.0",
          "kategorie": "Data",
          "bewertung": 9
        },
        {
          "name": "DeepSeek v3.2",
          "kategorie": "Recherche",
          "bewertung": 10
        },
        {
          "name": "Taskade Genesis",
          "kategorie": "Agents",
          "bewertung": 9
        }
      ],
      "highlights": "DeepSeek v3.2 (10/10) - Star der Woche"
    }
  ]
}
```

## Wöchentlicher Update-Workflow

### Schritt 1: Recherche & Analyse (Samstag/Sonntag)
1. Manus AI recherchiert über 10 Quellen
2. Identifiziert Top 5 Tools
3. Erstellt detaillierte Analysen

### Schritt 2: Archivierung der aktuellen Woche (Sonntag früh)
1. Kopiere aktuelles `index.html` nach `archiv/YYYY/kwXX-YYYY-MM-DD.html`
2. Aktualisiere `archive-index.json` mit neuer Woche
3. Commit & Push Archiv-Dateien

### Schritt 3: Update der Homepage (Sonntag 6:00)
1. Generiere neues `index.html` mit aktuellen Tools
2. Aktualisiere Datum und KW-Nummer
3. Commit & Push neue Homepage

### Schritt 4: Automatisches Deployment
1. GitHub Pages deployed automatisch
2. Website ist live aktualisiert
3. Archiv bleibt zugänglich

## Archiv-Seite Features

### Übersichtsseite (archiv.html)
- **Timeline-Ansicht** - Chronologische Liste aller Wochen
- **Filter nach Jahr** - 2025, 2026, etc.
- **Filter nach Kategorie** - Zeige nur Wochen mit bestimmten Kategorien
- **Suchfunktion** - Suche nach Tool-Namen
- **Statistiken** - Anzahl analysierter Tools, Durchschnittsbewertung

### Einzelne Archiv-Seiten
- Identisches Design wie aktuelle Homepage
- "Archiv"-Badge oben rechts
- Link zurück zur Archiv-Übersicht
- Link zur aktuellen Woche

## Automatisierungs-Script (für wöchentliche Task)

```bash
#!/bin/bash
# weekly-update.sh

# 1. Archiviere aktuelle Woche
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_YEAR=$(date +%Y)
CURRENT_KW=$(date +%V)

mkdir -p archiv/$CURRENT_YEAR
cp index.html archiv/$CURRENT_YEAR/kw$CURRENT_KW-$CURRENT_DATE.html

# 2. Aktualisiere archive-index.json
# (wird von Manus AI generiert)

# 3. Generiere neue Homepage
# (wird von Manus AI generiert)

# 4. Commit & Push
git add .
git commit -m "Weekly update: KW $CURRENT_KW - $CURRENT_DATE"
git push origin master
```

## Vorteile dieser Struktur

✅ **Vollständige Historie** - Alle Analysen bleiben verfügbar  
✅ **SEO-freundlich** - Jede Woche hat eigene URL  
✅ **Schnelles Laden** - Statische HTML-Dateien  
✅ **Einfache Navigation** - Timeline und Filter  
✅ **Automatisiert** - Kein manueller Eingriff nötig  
✅ **Skalierbar** - Funktioniert für Jahre von Analysen
