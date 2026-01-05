# Playbook: Wöchentliche KI-Tool-Analyse

**Version:** 2.0 (Updated 04.01.2026)  
**Autor:** Manus AI  
**Zweck:** Systematische wöchentliche Analyse der Top 5 neuen KI-Tools mit Website-Update

---

## 🎯 Ziel

Erstelle jede Woche eine fundierte Analyse der 5 interessantesten neuen KI-Tools aus den Kategorien:
- 📝 **Text** (Copywriting, Content, NLP)
- 🎨 **Design** (Bildgenerierung, Video, UI/UX)
- 📊 **Data/Wissen** (Datenanalyse, Knowledge Management)
- 🔍 **Recherche** (Search, Information Retrieval)
- 🤖 **Agents** (Autonome Systeme, Workflows)

---

## 📋 Prozess-Übersicht

### Phase 1: Recherche (10 Quellen)
### Phase 2: Tool-Auswahl (Top 5)
### Phase 3: Tiefenanalyse
### Phase 4: Markdown-Analyse erstellen
### Phase 5: **HTML-Generierung mit Template** ⚠️ KRITISCH
### Phase 6: Website archivieren und aktualisieren
### Phase 7: Git Commit & Push

---

## 🔍 Phase 1: Systematische Recherche

### Primäre Quellen (MUST)
1. **AI Breakfast** (https://aibreakfast.beehiiv.com/) - Newsletter mit Tool-Launches
2. **There's An AI For That** (https://theresanaiforthat.com/just-released/) - Neu veröffentlichte Tools
3. **FutureTools.io** (https://www.futuretools.io/newly-added) - Neu hinzugefügte Tools
4. **Ben's Bites** (https://news.bensbites.com/) - Aktuelle KI-Tool-Launches
5. **Futurepedia** (https://www.futurepedia.io/ai-innovations) - AI Innovations

### Sekundäre Quellen (SHOULD)
6. **Product Hunt** (https://www.producthunt.com/leaderboard/daily) - Best of Day (letzte 7 Tage)
7. **Toolify.ai** (https://www.toolify.ai/new) - Neue Tools
8. **TopAI.tools** (https://topai.tools/browse?sort=newest) - Neueste Tools

### Newsletter-Quellen (OPTIONAL)
9. **AI-Weekly** - Tool-Erwähnungen
10. **The Batch** - Tool-Erwähnungen

### Recherche-Prozess
1. Besuche alle Primärquellen systematisch
2. Notiere Tools der letzten 7 Tage in `/home/ubuntu/ki-tool-recherche-notizen.md`
3. Erfasse: Name, Kategorie, URL, Kurzbeschreibung, Quelle, Datum

---

## 🎯 Phase 2: Tool-Auswahl

### Auswahlkriterien
1. **Innovationsgrad:** Löst das Tool ein Problem auf neue Weise?
2. **Praxisrelevanz:** Hat es echten Nutzen für professionelle Anwender?
3. **Timing:** Wurde es in den letzten 7 Tagen gelauncht/erwähnt?
4. **Kategorie-Diversität:** Je 1 Tool pro Kategorie (Text, Design, Data, Recherche, Agents)

### Shortlist erstellen
- Erstelle `/home/ubuntu/ki-tool-shortlist.md`
- Kategorisiere alle gefundenen Tools
- Wähle Top 5 aus (je 1 pro Kategorie)
- Begründe Auswahl kurz

---

## 🔬 Phase 3: Tiefenanalyse

Für jedes der 5 ausgewählten Tools:

### 3.1 Website-Analyse
- Besuche die offizielle Website
- Erfasse: Features, USPs, Use Cases, Testimonials
- Screenshots/Notizen von wichtigen Infos

### 3.2 Pricing-Analyse
- Free Tier? Trial?
- Paid Plans: Preise, Features, Limits
- Enterprise-Optionen?
- Vergleich mit Wettbewerb

### 3.3 Datenschutz-Check
- Serverstandort (EU/US/etc.)
- DSGVO-Konformität erwähnt?
- Privacy Policy vorhanden?
- Self-Hosting möglich?

### 3.4 Praktische Bewertung
- **Stärken:** Was macht das Tool besonders gut?
- **Schwächen:** Wo gibt es Limitationen?
- **Zielgruppe:** Für wen ist es geeignet?
- **Relevanzbewertung:** 1-10 Punkte mit Begründung

### Analyse speichern
- Erstelle `/home/ubuntu/tool-analysen/{toolname}-analyse.md` für jedes Tool
- Strukturiert nach: Grunddaten, Beschreibung, Use Cases, Pricing, Datenschutz, Stärken, Schwächen, Fazit, Bewertung

---

## 📝 Phase 4: Markdown-Analyse erstellen

Erstelle `/home/ubuntu/wochenanalyse-kw{XX}-{YYYY}.md` mit:

### Struktur
```markdown
# Wöchentliche KI-Tool-Analyse: Die Top 5 Neuentdeckungen der KW XX/YYYY

**Datum:** DD.MM.YYYY | **Autor:** Manus AI

## Einleitung
[Kontext, Trends, Überblick]

---

## 1. [Tool-Name]: [Tagline]

**Kategorie: [Kategorie]** | **Relevanz: X/10**

[Beschreibung]

### Praxis-Analyse
[Detaillierte Analyse]

| Feature | Details |
|---------|---------|
| **Pricing-Modell** | ... |
| **Besonderheit** | ... |
| **Datenschutz** | ... |

**Fazit:** [Zusammenfassung]

---

[Wiederhole für Tools 2-5]

---

## Zusammenfassung und Ausblick
[Trends, Learnings, Ausblick]

## Referenzen
[1] Tool 1. [URL]
[2] Tool 2. [URL]
...
```

---

## 🚨 Phase 5: HTML-Generierung mit Template (KRITISCH!)

### ⚠️ WICHTIG: NIEMALS Markdown direkt in HTML konvertieren!

Das führt zu fehlendem Styling. **IMMER** das vollständige HTML-Template verwenden.

### Korrekte Vorgehensweise

#### Option A: Python-Skript verwenden (EMPFOHLEN)

```python
# Verwende generate_html_from_analysis.py
from generate_html_from_analysis import create_html

tools = [
    {
        'name': 'Tool-Name',
        'category': 'text',  # text/design/data/research/agents
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 8.0,
        'tagline': 'Kurzbeschreibung',
        'description': 'Ausführliche Beschreibung...',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Details'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Details'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'Details'}
        ],
        'verdict': 'Fazit-Text',
        'url': 'https://...'
    },
    # ... weitere Tools
]

html = create_html(
    kw="01",
    date="04.01.2026",
    summary="Zusammenfassung...",
    trend="Trend-Text",
    stars="Stars der Woche: Tool X & Tool Y (9/10)",
    tools=tools
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
```

#### Option B: Manuell aus Template erstellen

1. Kopiere die vorherige `index.html` als Basis
2. Aktualisiere:
   - KW-Nummer im Header
   - Datum
   - Summary-Text
   - Trend & Stars
   - Alle 5 Tool-Cards mit korrekten Daten
3. Speichere als neue `index.html`

### Template-Struktur (Referenz)

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KI-Tool-Analysen | Wöchentliche Reviews KW XX/YYYY</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Cyberpunk Background Effects -->
    <div class="cyber-grid"></div>
    <div class="cyber-scanline"></div>
    
    <!-- Header mit Logo, KW-Nummer, Archiv-Link -->
    <header class="header">...</header>

    <!-- Main Content -->
    <main class="main">
        <div class="container">
            <!-- Summary Card -->
            <div class="summary-card">...</div>

            <!-- Tools Grid -->
            <div class="tools-grid">
                <!-- Tool Card 1-5 -->
                <div class="tool-card" data-category="...">...</div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">...</footer>
</body>
</html>
```

### ✅ Checkliste vor Git Push

- [ ] HTML hat vollständiges Cyber-Design (Header, Grid, Footer)
- [ ] Alle 5 Tool-Cards sind vorhanden
- [ ] KW-Nummer ist korrekt
- [ ] Datum ist aktuell
- [ ] Alle Links funktionieren
- [ ] style.css wird korrekt geladen
- [ ] Mobile-responsive (viewport meta tag vorhanden)

---

## 📦 Phase 6: Website archivieren und aktualisieren

### 6.1 Repository klonen (falls noch nicht geschehen)
```bash
gh repo clone rogerbasler/ki-tool-analysen
cd ki-tool-analysen
```

### 6.2 Vorherige Version archivieren
```bash
# Archiviere aktuelle index.html
mv index.html archiv/kw{XX}_{YYYY-MM-DD}.html
```

### 6.3 Neue Version deployen
```bash
# Kopiere neue HTML
cp /home/ubuntu/wochenanalyse-kw{XX}-{YYYY}.html index.html

# Kopiere Markdown-Analyse
cp /home/ubuntu/wochenanalyse-kw{XX}-{YYYY}.md .
```

### 6.4 Archiv-Index aktualisieren
Bearbeite `archiv/data/archive-index.json`:

```json
{
  "analysen": [
    {
      "kw": 1,
      "jahr": 2026,
      "datum": "2026-01-04",
      "url": "index.html",
      "tools": [
        {
          "name": "Tool-Name",
          "kategorie": "Text",
          "bewertung": 8,
          "kurzbeschreibung": "..."
        }
      ],
      "highlights": "Stars der Woche: ...",
      "trend": "Trend-Beschreibung"
    },
    // ... vorherige Analysen
  ]
}
```

---

## 🚀 Phase 7: Git Commit & Push

```bash
cd ki-tool-analysen

# Stage alle Änderungen
git add .

# Commit mit aussagekräftiger Message
git commit -m "Update: Wöchentliche KI-Tool-Analyse KW XX/YYYY"

# Push zu GitHub
git push
```

### Verifizierung
- Besuche https://rogerbasler.github.io/ki-tool-analysen/
- Prüfe: Layout, Styling, Links, Mobile-Ansicht
- Teste Archiv-Seite

---

## 🎨 Design-Richtlinien

### Cyber-Design-Elemente (MUST HAVE)
- ✅ Cyber-Grid Background (`<div class="cyber-grid"></div>`)
- ✅ Scanline-Effekt (`<div class="cyber-scanline"></div>`)
- ✅ Neon-Green Primary Color (#00ff9d)
- ✅ Orbitron Font für Headlines
- ✅ Roboto Mono für Body
- ✅ Tool-Cards mit Hover-Effekten
- ✅ Rating-Display (X.0/10)
- ✅ Category-Icons (📝🎨📊🔍🤖)

### Responsive Design
- Mobile-first approach
- Breakpoints: 768px, 1024px
- Touch-friendly buttons
- Readable font sizes

---

## 📊 Qualitätskriterien

### Inhalt
- ✅ 5 Tools analysiert (je 1 pro Kategorie)
- ✅ Jedes Tool: Beschreibung, Pricing, Datenschutz, Fazit, Bewertung
- ✅ Zusammenfassung mit Trends
- ✅ Referenzen mit URLs

### Technisch
- ✅ HTML validiert (W3C)
- ✅ Alle Links funktionieren
- ✅ Mobile-responsive
- ✅ Ladezeit < 3 Sekunden
- ✅ Cyber-Design vollständig

### SEO
- ✅ Meta-Description
- ✅ Semantic HTML
- ✅ Alt-Texte (falls Bilder)
- ✅ Strukturierte Überschriften (H1-H3)

---

## 🐛 Troubleshooting

### Problem: HTML ohne Styling
**Ursache:** Markdown wurde direkt in HTML konvertiert ohne Template  
**Lösung:** Verwende `generate_html_from_analysis.py` oder kopiere Template manuell

### Problem: style.css wird nicht geladen
**Ursache:** Falscher Pfad im `<link>`-Tag  
**Lösung:** Prüfe: `<link rel="stylesheet" href="style.css">`

### Problem: Archiv-Seite zeigt neue Analyse nicht
**Ursache:** `archive-index.json` nicht aktualisiert  
**Lösung:** Füge neuen Eintrag in JSON hinzu und pushe

### Problem: Mobile-Ansicht kaputt
**Ursache:** Viewport-Meta-Tag fehlt  
**Lösung:** Füge hinzu: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

---

## 📚 Ressourcen

### Dateien
- `generate_html_from_analysis.py` - HTML-Generator-Skript
- `style.css` - Cyber-Design-Stylesheet
- `archiv/data/archive-index.json` - Archiv-Datenbank
- `PLAYBOOK-UPDATED.md` - Dieses Dokument

### Links
- GitHub Repo: https://github.com/rogerbasler/ki-tool-analysen
- Live Website: https://rogerbasler.github.io/ki-tool-analysen/
- Archiv: https://rogerbasler.github.io/ki-tool-analysen/archiv.html

---

## ✅ Checkliste für jede Woche

- [ ] Phase 1: Alle 10 Quellen durchsucht
- [ ] Phase 2: Top 5 Tools ausgewählt (je 1 pro Kategorie)
- [ ] Phase 3: Tiefenanalyse für alle 5 Tools
- [ ] Phase 4: Markdown-Analyse erstellt
- [ ] Phase 5: **HTML mit vollständigem Template generiert** ⚠️
- [ ] Phase 6: Website archiviert und aktualisiert
- [ ] Phase 7: Git committed und gepusht
- [ ] Verifizierung: Live-Website geprüft

---

**Version History:**
- v1.0 (28.12.2025): Initial Playbook
- v2.0 (04.01.2026): Hinzugefügt: HTML-Template-Prozess, Troubleshooting, Python-Skript

**Nächste Review:** Nach 4 Wochen (Ende Januar 2026)
