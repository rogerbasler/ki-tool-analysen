# KI-Tool-Analysen: Wochenlauf

Dieses Repo ist die Website https://tools.fragroger.ai (Deutsch) und https://tools.fragroger.ai/en/ (Englisch),
ausgeliefert über GitHub Pages (Branch `master`, Datei `CNAME`).
Jeden Sonntagmorgen erscheint eine neue Ausgabe mit fünf KI-Tools. Herausgeber ist Roger Basler de Roca (#fragRoger).
Die Website wird ausschliesslich aus `data/weeks/*.json` (DE) und `data/weeks/en/*.json` (EN) gebaut. Generierte HTML-Dateien nie von Hand bearbeiten.

## Ablauf eines Wochenlaufs

1. **Vorbereiten**
   - `pip install --break-system-packages -r pipeline/requirements.txt` (falls Jinja2/Markdown fehlen)
   - Datum = heutiger Sonntag (Europe/Zurich), `DATUM=YYYY-MM-DD`, KW = ISO-Kalenderwoche dieses Datums.
   - Existiert `data/weeks/$DATUM.json` bereits, ist die Woche erledigt: nichts tun, kurz melden, Ende.
   - Letzte Ausgaben ansehen, damit sich keine Tools wiederholen: `ls data/weeks | tail -6` und die Tool-Namen darin.

2. **Recherche (Zeitraum: die sieben Tage bis heute)**
   Mit WebSearch und WebFetch systematisch durchgehen:
   AI Breakfast, There's An AI For That, FutureTools.io, Ben's Bites, Futurepedia.io, Product Hunt (AI),
   Toolify.ai, TopAI.tools, The AI Citizen (Weekly Tool Roundup), sowie AI-Weekly, The Batch, The Sequence,
   AI Tidbits (nur für Tool-Erwähnungen). Ziel sind 15 bis 30 Kandidaten mit Quelle und Datum.
   Rechercheprotokoll speichern unter `research/kwNN-YYYY-source-scan.md` (Kandidat, Kategorie, Quelle, Datum, Signal).

3. **Auswahl**
   - Pro Kategorie genau ein Tool: Text, Design, Data / Wissen, Recherche, Agents.
   - Nur Tools, die in der Woche neu erschienen, signifikant aktualisiert oder stark erwähnt wurden.
     Gibt es keine relevante Neuerscheinung, ein bestehendes Tool mit wichtigem Update wählen und das Update im Feld `signal` benennen.
   - Kein Tool aus den letzten sechs Ausgaben wiederholen (der Validator prüft das).
   - Relevanz für Unternehmer:innen und Entscheider:innen im DACH-Raum vor Neuheitswert.

4. **Tiefenanalyse pro Tool**
   Offizielle Website, Preisseite, Datenschutzerklärung, AGB/DPA, Trust Center oder Security-Seite lesen.
   Preise in USD oder CHF so angeben, wie sie publiziert sind; Free Tier ausdrücklich nennen oder ausschliessen.
   Datenschutz immer mit: Serverstandort/Region, relevante Policies, Einordnung DSGVO und Schweizer DSG, Self-Hosting ja/nein.
   Was nicht dokumentiert ist, als "nicht dokumentiert" benennen, nie raten. Keine Fakten erfinden.

5. **Wochendatei schreiben**: `data/weeks/$DATUM.json` nach dem Schema unten.

5b. **Englische Fassung schreiben**: `data/weeks/en/$DATUM.json` nach dem EN-Schema unten. Vollständige,
   sinngetreue Übersetzung aller Textfelder in britischem Englisch, gleiche Tool-Namen, gleiche Anzahl Listeneinträge.
   Preise, Zahlen und Namen unverändert übernehmen, Dezimalpunkt statt Komma ("8.4/10").

6. **Prüfen**: `python3 pipeline/validate_week.py data/weeks/$DATUM.json` (prüft DE und EN) so lange korrigieren, bis `OK` erscheint.
   Warnungen ernst nehmen und wo möglich beheben.

7. **Bauen**: `python3 pipeline/build_site.py`. Das erzeugt Startseite, Wochenseite, Archiv, Feed, Sitemap und
   die vollständigen Markdown-Analysen unter `archiv/data/ki-tool-analysen-$DATUM.md` und `...-$DATUM.en.md`. Die Vorwoche bleibt automatisch im Archiv.

8. **Veröffentlichen**
   ```bash
   git add -A
   git commit -m "Weekly update: KW $KW - $DATUM"
   git push origin master    # bei Konflikt: git pull --rebase origin master, neu bauen, erneut pushen
   ```

9. **Abschluss**: kurze Meldung mit KW, den fünf Tools samt Bewertung und den Links https://tools.fragroger.ai und https://tools.fragroger.ai/en/.

## Schema `data/weeks/YYYY-MM-DD.json`

```json
{
  "kw": 43,
  "jahr": 2026,
  "datum": "2026-10-25",
  "zeitraum": "18. bis 25. Oktober 2026",
  "zusammenfassung": "3 bis 5 Sätze. These, Mechanismus, Evidenz, Konsequenz; letzter Satz als verdichtete Kernaussage.",
  "highlights": [
    "Toolname (8,6/10): warum es diese Woche heraussticht, ein Satz.",
    "Praxisregel: eine konkrete Handlungsregel für Entscheider:innen."
  ],
  "trend": "Ein Satz zum Muster der Woche.",
  "quelle": "Claude",
  "tools": [
    {
      "kategorie": "Text",
      "name": "Toolname",
      "url": "https://offizielle-website",
      "bewertung": 8.4,
      "signal": "Was diese Woche passiert ist, mit Datum (Launch, Update, Erwähnung).",
      "kurzbeschreibung": "Ein Satz: konkrete Funktion und Zielgruppe.",
      "beschreibung": "Ein bis zwei Absätze (Leerzeile trennt Absätze). Fachbegriffe einfach erklären.",
      "nutzungsszenarien": ["Kurzlabel: konkretes Praxisbeispiel.", "... (3 bis 5)"],
      "pricing": "Pläne mit Preisen in USD oder CHF, inklusive Free Tier.",
      "datenschutz": "Serverstandort, Policies, DSGVO/DSG, Self-Hosting.",
      "staerken": ["...", "..."],
      "schwaechen": ["...", "..."],
      "einschaetzung": "Einschätzung für die Praxis: für wen, unter welchen Bedingungen, wie testen.",
      "quellen": [
        "Anbieter. (2026, 22. Oktober). Titel der Seite. https://...",
        "Anbieter. (o. D.). Datenschutzerklärung. https://..."
      ]
    }
  ]
}
```

## Schema `data/weeks/en/YYYY-MM-DD.json`

Nur die Textfelder, Struktur (Kategorie, Bewertung, URL, Quellen) kommt aus der deutschen Datei:

```json
{
  "umfang": "voll",
  "zeitraum": "18 to 25 October 2026",
  "zusammenfassung": "3 to 5 sentences ...",
  "highlights": ["Toolname (8.6/10): ...", "Rule of thumb: ..."],
  "trend": "...",
  "tools": [
    {
      "name": "Toolname (identisch zur DE-Datei)",
      "signal": "...", "kurzbeschreibung": "...", "beschreibung": "...",
      "nutzungsszenarien": ["Label: ..."], "pricing": "...", "datenschutz": "...",
      "staerken": ["..."], "schwaechen": ["..."], "einschaetzung": "..."
    }
  ]
}
```

Englische Schreibregeln: gleicher Ton (analytisch, ruhig, ohne Buzzwords), keine Gedankenstriche, gerade Anführungszeichen,
kein "according to", kein "[1]", keine Konstruktion "not only ..., but", keine deutschen Umlaute im Text.
Archivwochen vor KW 43/2026 haben `"umfang": "uebersicht"`: nur Zusammenfassung und Kurzbeschreibungen sind übersetzt,
die englische Seite verweist für die Details auf die deutsche Fassung.

Reihenfolge der Tools: Text, Design, Data / Wissen, Recherche, Agents. `bewertung` ist eine Zahl von 1 bis 10 (eine Nachkommastelle erlaubt).
In Listen wird ein Präfix bis zum ersten Doppelpunkt fett dargestellt ("Vertrieb: ...").

## Schreibregeln (verbindlich)

- Sprache Deutsch, Schweizer Orthografie: ä, ö, ü, immer "ss" statt "ß", Gender mit Doppelpunkt (Nutzer:innen).
- Keine Gedankenstriche (— oder –), keine typografischen Anführungszeichen, nur gerade "".
- Ton: analytisch, ruhig, präzise, ohne Pathos. Keine Buzzwords (Game Changer, revolutionär, bahnbrechend, disruptiv), keine Marketing-Sprache, keine unnötigen Adjektive.
- Keine Floskeln wie "Das eigentliche Problem ist nicht ..., sondern ...", "Was oft unterschätzt wird", "Der entscheidende Unterschied liegt in", "hier zeigt sich", "dieses Muster".
- Keine Quellenangaben im Fliesstext (kein "[1]", kein "laut X"). Quellen nur im Feld `quellen`, im APA-7-Format mit URL.
- Keine Vergleiche zwischen Tools. Jedes Tool steht für sich.
- Kurze bis mittellange Sätze. Jeder Satz liefert einen Erkenntnisgewinn.
- Die Wochenzusammenfassung beginnt mit einer Beobachtung oder These, nie mit einer Definition, und endet mit einer verdichteten Kernaussage statt einem Appell.

## Aufbau des Repos

```
data/weeks/YYYY-MM-DD.json     eine Datei pro Ausgabe (Quelle der deutschen Seite und der Struktur)
data/weeks/en/YYYY-MM-DD.json  englische Texte zur selben Ausgabe
data/legacy-redirects.json     alte, unregelmässig benannte Archiv-URLs -> neue Wochenseiten
pipeline/build_site.py         baut die statische Website (DE im Wurzelverzeichnis, EN unter en/)
pipeline/i18n.py               Pfade und Oberflächentexte DE/EN
pipeline/validate_week.py      prüft Pflichtfelder, Kategorien, Stil und Wiederholungen
pipeline/legal.py              Texte für Methode, Impressum, Datenschutz
templates/, assets/            Vorlagen und CSS im fragRoger-CI
research/                      Rechercheprotokolle
archiv/data/*.md               Markdown-Analysen je Woche
```

Wochen mit `"quelle": "Manus-Archiv (migriert)"` stammen aus der Zeit vor Oktober 2026; ihre Markdown-Fassungen
werden unverändert als Vollanalyse-Seite angezeigt und nicht neu erzeugt.
