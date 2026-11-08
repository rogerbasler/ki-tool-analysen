# KI-Tool-Analysen KW 45/2026

**Datum:** 8. November 2026  
**Recherchezeitraum:** 1. bis 8. November 2026

## Wochenzusammenfassung

KI-Werkzeuge arbeiten in dieser Woche zunehmend ohne Aufsicht weiter, nachdem der Auftrag einmal erteilt ist. Der Mechanismus ist überall ähnlich: Ein Agent behält Ziel, Verlauf und Zugriffe, zerlegt die Arbeit selbst und meldet sich erst, wenn eine Entscheidung ansteht, sei es ein Perplexity Teammate in Slack, ChatGPT mit vereinter Arbeitsansicht oder eine Elicit-Routine. Damit wandert die Kontrolle vom einzelnen Prompt zur Frage, welche Rechte ein Agent dauerhaft besitzt und wo seine Daten liegen. Gleichzeitig gelten die strengeren Zusagen zu Training, Aufbewahrung und Datenregion fast überall nur in Enterprise-Verträgen, während die neuen Funktionen zuerst in Einzelplänen erscheinen. Wer Agenten arbeiten lässt, delegiert mit jeder Aufgabe auch Zugriffsrechte, und diese brauchen ein Ablaufdatum.

- Google Forms mit Gemini (7,7/10): Umfrageauswertung mit nachvollziehbaren Zahlen aus ausgeführtem Code, in Workspace-Plänen ab Business Standard ohne Zusatzkosten.
- Perplexity Teammates (7,6/10): Dauerhafte Agenten mit eigenem Rechner und Slack-Anbindung, vorerst nur im Einzelplan Max und als Research Preview.
- ElevenLabs Scribe v2 Realtime (7,2/10): Personen-, Gesundheits- und Kartendaten werden schon während der Echtzeit-Transkription geschwärzt.
- Praxisregel: Jedem Agenten, der im Hintergrund arbeitet, vorab drei Dinge mitgeben: welche Konten er nutzen darf, bis wann der Auftrag gilt und wer die Ergebnisse freigibt.

**Trend:** Aus Assistenten werden Mitarbeitende auf Zeit, und mit jedem dauerhaft laufenden Agenten wird die Rechtevergabe zur eigentlichen Führungsaufgabe.

| Kategorie | Tool | Relevanz |
|---|---|---:|
| Text | ChatGPT Chat und Work | 7,4/10 |
| Design | Google Vids mit Omni 1.2 Flash | 7/10 |
| Data / Wissen | Google Forms mit Gemini | 7,7/10 |
| Recherche | Elicit Research Agent | 7,5/10 |
| Agents | Perplexity Teammates | 7,6/10 |
| Transkription | ElevenLabs Scribe v2 Realtime | 7,2/10 |

---

## 1. ChatGPT Chat und Work

**Kategorie:** Text  
**Relevanzbewertung:** 7,4/10  
**Website:** https://chatgpt.com/  
**Aktualitätssignal:** Am 2. November 2026 hat OpenAI angekündigt, die Bereiche Chat und Work in der ChatGPT-Desktop-App zu einer Ansicht zusammenzulegen, zunächst für ausgewählte Nutzer:innen; ab Dezember teilen sich ChatGPT und Codex in Plus, Pro und Business ein gemeinsames Nutzungskontingent.

### Kurzbeschreibung

ChatGPT-Desktop-App, in der ein Gespräch ohne Moduswechsel zu einer mehrstufigen Arbeitsaufgabe wird, für Wissensarbeitende in Unternehmen.

Work ist seit Juli 2026 ein eigener Modus der Desktop-App. Dort arbeitet ein Agent längere Aufgaben ab: Recherche, Datenanalyse sowie das Erstellen von Dokumenten, Tabellen, Präsentationen und Websites, auch über verbundene Apps und Dateien. Neu verschmilzt dieser Modus mit dem normalen Chat. Eine Frage kann so direkt in eine Aufgabe übergehen, Dateien und Plugins lassen sich einbinden, Zwischenergebnisse prüfen und mehrere Projekte an einem Ort verfolgen. Codex, die Programmierumgebung, bleibt ein eigener Bereich.

Für die Kostenplanung ist die zweite Änderung wichtiger. Ab Dezember zählen Work und Codex gegen ein gemeinsames Kontingent, gemessen in Tokens, also in Textbausteinen, die ein Modell verarbeitet. Normale Instant-Chats sind davon ausgenommen. Wer viel agentisch arbeiten lässt, verbraucht das Kontingent entsprechend schneller.

### Nutzungsszenarien

- Geschäftsleitung: Aus einer Frage zur Quartalsentwicklung direkt eine Präsentation mit Tabellen aus hochgeladenen Dateien erstellen lassen.
- Marketing: Einen Wettbewerbsüberblick recherchieren und als Dokument mit Quellenliste ausgeben lassen.
- Projektleitung: Mehrere laufende Aufgaben wie Berichtsentwürfe und Datenauswertungen an einem Ort verfolgen.
- Controlling: Eine Excel-Datei analysieren lassen und die Zwischenschritte vor der Weiterverwendung prüfen.

### Pricing

Free: USD 0. Go: USD 8 pro Monat. Plus: USD 20 pro Monat. Pro: USD 100, 200 oder 500 pro Monat. Business: USD 20 pro Person und Monat bei Jahreszahlung, USD 25 bei Monatszahlung, ab zwei Personen. Enterprise und Edu: Preis auf Anfrage. Work und Codex sind in allen Plänen aufgeführt, das Kontingent wächst mit dem Plan; Business, Edu und Enterprise können zusätzliche Credits kaufen. Ein Termin für die breite Verfügbarkeit der vereinten Ansicht ist nicht dokumentiert.

### Datenschutz

Training: In Free, Go, Plus und Pro dürfen Inhalte standardmässig zum Training genutzt werden, ein Opt-out ist in den Data Controls möglich; in Business, Enterprise, Edu und API gibt es kein Training ohne aktive Zustimmung. Serverstandort: Datenresidenz in Europa gibt es für neue Workspaces in Enterprise und Edu sowie für API-Projekte, seit Januar 2026 auch mit Verarbeitung auf GPUs in der EU; für Business und Einzelpläne ist eine Datenresidenz nicht dokumentiert. Aufbewahrungsfristen für Einzelpläne sind nicht dokumentiert. OpenAI nennt SOC 2 Type 2, AES-256-Verschlüsselung und bietet einen Auftragsverarbeitungsvertrag (DPA) an. Für DSGVO und DSG ist Business mit DPA eine vertretbare Grundlage für interne Dokumente, für Personaldaten oder Berufsgeheimnisse erst Enterprise mit EU-Datenresidenz. Das Schweizer DSG wird nicht eigens erwähnt. Self-Hosting ist nicht dokumentiert.

### Stärken

- Arbeitsfluss: Frage und Ausführung in einer Ansicht, ohne Moduswechsel.
- Ausgabeformate: Dokumente, Tabellen, Präsentationen und Websites direkt aus dem Gespräch.
- Kontrolle: Zwischenergebnisse lassen sich prüfen und steuern, bevor die Aufgabe abgeschlossen ist.
- Unternehmenspläne: Kein Training in Business und Enterprise, EU-Datenresidenz für Enterprise.

### Schwächen

- Verfügbarkeit: Zunächst nur für ausgewählte Nutzer:innen, ohne publizierten Zeitplan.
- Kosten: Gemeinsames Kontingent mit Codex macht den Verbrauch agentischer Aufgaben schwerer planbar.
- Dokumentation: Keine offizielle Release Note, Details stammen aus einer E-Mail an Abonnent:innen.
- Einzelpläne: Training standardmässig aktiv, keine Datenresidenz.

### Einschätzung für die Praxis

Die vereinte Ansicht lohnt sich für Teams, die ChatGPT bereits für Recherche und Dokumente nutzen und den Wechsel zwischen Modi als Bruch erleben. Für den Unternehmenseinsatz sollte mindestens Business mit DPA gelten, für sensible Daten Enterprise. Ein sinnvoller Test: drei wiederkehrende Aufgaben, etwa Monatsbericht, Wettbewerbsnotiz und Datenauswertung, je einmal im Chat und einmal als Work-Aufgabe ausführen und Zeitaufwand, Korrekturbedarf und Kontingentverbrauch notieren, bevor im Dezember die geteilten Limits gelten.

**Relevanzbewertung:** 7,4/10

---

## 2. Google Vids mit Omni 1.2 Flash

**Kategorie:** Design  
**Relevanzbewertung:** 7/10  
**Website:** https://workspace.google.com/products/vids/  
**Aktualitätssignal:** Seit 5. November 2026 erzeugt Google Vids Clips bis 15 Sekunden mit dem Videomodell Gemini Omni 1.2 Flash; jedes Google-Konto kann drei solche Videos pro Monat kostenlos erstellen.

### Kurzbeschreibung

Videoeditor in Google Workspace, der kurze KI-Clips aus Text und Referenzbildern erzeugt und eigene Aufnahmen per Anweisung bearbeitet, für interne Kommunikation und Marketing.

Google Vids ist ein Werkzeug für Erklär-, Schulungs- und Präsentationsvideos im Browser. Mit Omni 1.2 Flash entstehen Clips bis 15 Sekunden in einer Einstellung, bisher waren es 10. Referenzbilder halten Figuren und Szenen über mehrere Clips konsistent, die Sprachausgabe klingt natürlicher. Entwürfe entstehen in 360p oder 720p und lassen sich auf 1080p oder 4K hochrechnen.

Seit Juli 2026 können bezahlte Konten zudem eigene Handy- oder Kameraaufnahmen per Textanweisung verändern, etwa Licht, Hintergrund oder Kamerawinkel. Persönliche Avatare aus eigenem Gesicht und eigener Stimme sind nur für Erwachsene mit Englisch als Hauptsprache verfügbar. Jedes Ergebnis trägt ein unsichtbares SynthID-Wasserzeichen, das maschinell als KI-generiert erkannt werden kann.

### Nutzungsszenarien

- HR: Kurze Begrüssungsclips für das Onboarding neuer Mitarbeitender erstellen.
- Marketing: Produktideen als 15-Sekunden-Entwurf visualisieren, bevor eine Agentur beauftragt wird.
- Schulung: Erklärvideos zu internen Abläufen mit konsistenten Figuren über mehrere Szenen bauen.
- Kommunikation: Eigene Handyaufnahmen per Anweisung nachbearbeiten, etwa Hintergrund oder Licht.

### Pricing

Free Tier: Jedes Google-Konto und jedes Workspace-Abo erhält drei 15-Sekunden-Videos pro Monat kostenlos. Google AI Plus: USD 4.99 pro Monat, AI Pro: USD 19.99, AI Ultra: USD 99.99 oder 199.99 pro Monat (US-Preise); die Vids-Kontingente je Plan sind nicht dokumentiert. Workspace: Business Starter USD 7, Standard USD 14, Plus USD 22 pro Person und Monat ohne Steuern, Enterprise auf Anfrage; Vids ist in allen Plänen enthalten. Entwickler:innen zahlen für das Modell USD 0.07 pro Sekunde in 720p. CHF-Preise sind nicht dokumentiert.

### Datenschutz

In Workspace gilt das Cloud Data Processing Addendum: Prompts und Inhalte sind Kundendaten, werden ohne Erlaubnis nicht zum Training genutzt und nicht von Menschen ausserhalb der Organisation geprüft. Google nennt ISO 27001, 27701, 42001 sowie SOC 1, 2 und 3. Serverstandort: Datenregionen für die KI-Funktionen in Vids sind nicht dokumentiert. Für private Konten, auch Google AI Pro und Ultra, gelten die Consumer-Bedingungen; ob Vids-Inhalte dort zum Training dienen, ist nicht dokumentiert. Für DSGVO und DSG ist der Workspace-Vertrag eine tragfähige Grundlage, bei Avataren aus Gesicht und Stimme kommen biometrische Daten hinzu, die eine eigene Abklärung brauchen. Das Schweizer DSG wird nicht eigens erwähnt. Self-Hosting ist nicht möglich, Vids läuft nur in der Google-Cloud.

### Stärken

- Einstieg: Drei Videos pro Monat kostenlos, ohne Zusatzabo.
- Konsistenz: Referenzbilder halten Figuren und Szenen über Clips hinweg gleich.
- Kennzeichnung: SynthID-Wasserzeichen erleichtert die Offenlegung als KI-Inhalt.
- Integration: Teil von Workspace, Freigaben und Verwaltung laufen über die bestehende Admin-Konsole.

### Schwächen

- Länge: 15 Sekunden pro Clip reichen für Entwürfe, nicht für fertige Filme.
- Kontingente: Für bezahlte Pläne sind die Vids-Limits nicht publiziert.
- Avatare: Nur für Englisch als Hauptsprache, für den DACH-Raum vorerst eingeschränkt.
- Datenregion: Keine Angabe, wo die Videogenerierung verarbeitet wird.

### Einschätzung für die Praxis

Vids passt für Organisationen, die bereits mit Google Workspace arbeiten und interne Videos ohne Agentur oder Schnittprogramm erstellen wollen. Für Kampagnen mit Markenanspruch bleibt es ein Werkzeug für Entwürfe. Ein sinnvoller Test: mit den drei Gratis-Clips ein Onboarding-Video mit gleichbleibender Figur bauen und prüfen, ob Qualität und Kennzeichnung den internen Richtlinien genügen. Avatare mit echten Gesichtern erst nach Klärung der Einwilligung und der biometrischen Daten einsetzen.

**Relevanzbewertung:** 7/10

---

## 3. Google Forms mit Gemini

**Kategorie:** Data / Wissen  
**Relevanzbewertung:** 7,7/10  
**Website:** https://workspace.google.com/products/forms/  
**Aktualitätssignal:** Ab 2. November 2026 rollt Google in Forms die Gemini-Funktion Actionable Insights aus: Analyse aller Antworttypen mit Trends, Zusammenhängen und Handlungsvorschlägen; Rapid Release ab 2. November, Scheduled Release ab 19. November.

### Kurzbeschreibung

Auswertungsfunktion im Antworten-Tab von Google Forms, die Umfrageergebnisse mit ausgeführtem Python-Code analysiert und nächste Schritte vorschlägt, für alle, die Kunden- oder Mitarbeitendenbefragungen durchführen.

Gemini liest die Antworten auf alle Fragetypen, erkennt Trends und Zusammenhänge zwischen Fragen und schlägt nächste Schritte vor. Zahlen wie Anzahl und Prozent entstehen nicht aus Schätzung des Sprachmodells, sondern aus Python-Code, den Gemini schreibt und auf den echten Daten ausführt. Die Ausgabe gliedert sich in eine Kurzsynthese, eine vertiefte Analyse mit Korrelationen und empfohlene nächste Schritte. Die Analyseschritte lassen sich einsehen, Vorschläge bewerten und neu erzeugen.

Die Funktion braucht mindestens 12 Antworten und 3 Fragen, ist Teil des Gemini-Beta-Programms und bei aktivierten Quiz-Einstellungen nicht verfügbar. Erzeugte Auswertungen werden nicht gespeichert. Korrelation heisst dabei nur, dass zwei Antworten gemeinsam auftreten; ob das eine das andere verursacht, kann die Auswertung nicht belegen.

### Nutzungsszenarien

- HR: Mitarbeitendenbefragung auswerten und erkennen, welche Teams bei Führung und Arbeitslast auffällig antworten.
- Kundendienst: Zufriedenheitsumfragen nach Produkt und Kanal aufschlüsseln und die häufigsten Kritikpunkte sammeln.
- Veranstaltungen: Feedback nach einem Anlass auswerten und konkrete Verbesserungen für das nächste Mal ableiten.
- Geschäftsleitung: Ergebnisse einer internen Strategieumfrage als Kurzsynthese für die nächste Sitzung erhalten.

### Pricing

Kein Free Tier für diese Funktion. Enthalten in Workspace Business Standard (USD 14 pro Person und Monat), Business Plus (USD 22), Enterprise Standard und Plus (Preis auf Anfrage), Education Plus sowie in den privaten Abos Google AI Pro und Ultra. Business Starter (USD 7) ist nicht berechtigt. Preise ohne Steuern bei monatlicher Abrechnung, CHF-Preise sind nicht dokumentiert. Voraussetzung: Smart Features und Personalisierung sind aktiviert.

### Datenschutz

In Workspace gilt das Cloud Data Processing Addendum: Kundendaten werden ohne Erlaubnis nicht zum Training genutzt, Interaktionen mit Gemini bleiben innerhalb der Organisation. Google nennt SOC 1, 2 und 3, ISO 27001, 27701, 27017, 27018 und 42001. Serverstandort: Seit Juni 2025 lässt sich die Gemini-Verarbeitung in Enterprise Plus oder mit Assured Controls auf die EU oder die USA beschränken; ob Forms darunter fällt, ist nicht dokumentiert, ein Standort Schweiz ebenfalls nicht. Ob die Beta-Funktion unter denselben Zusagen läuft, ist nicht dokumentiert. Für private AI-Pro- und Ultra-Konten gelten Consumer-Bedingungen. Für DSGVO und DSG ist der Workspace-Vertrag eine tragfähige Grundlage, bei Befragungen mit Gesundheits- oder Personaldaten sollten Antworten anonymisiert erhoben werden. Das Schweizer DSG wird nicht eigens erwähnt. Self-Hosting ist nicht möglich.

### Stärken

- Nachvollziehbarkeit: Zahlen stammen aus ausgeführtem Code, die Analyseschritte sind einsehbar.
- Kosten: Ohne Zusatzabo in den gängigen Workspace-Plänen ab Business Standard enthalten.
- Breite: Analysiert alle Fragetypen, nicht nur Freitext.
- Vertrag: Kein Training auf Kundendaten in Workspace, umfangreiche Zertifizierungen.

### Schwächen

- Status: Beta, mit unklarer Geltung der Datenschutzzusagen für Beta-Funktionen.
- Mindestmenge: Erst ab 12 Antworten und 3 Fragen nutzbar, keine Quiz-Formulare.
- Datenregion: Keine Angabe, ob die EU-Beschränkung für Forms greift.
- Kausalität: Gefundene Zusammenhänge verleiten zu Schlüssen, die die Daten nicht tragen.

### Einschätzung für die Praxis

Die Funktion lohnt sich für KMU und Abteilungen, die regelmässig mit Google Forms befragen und die Auswertung bisher in Tabellen von Hand erledigen. Sie ersetzt keine statistische Analyse, verkürzt aber den Weg zur ersten Interpretation deutlich. Ein sinnvoller Test: eine abgeschlossene Umfrage, die bereits manuell ausgewertet wurde, erneut mit Gemini analysieren und Zahlen sowie Empfehlungen vergleichen. Erst danach auf neue Befragungen anwenden, und Handlungsvorschläge immer als Hypothese behandeln.

**Relevanzbewertung:** 7,7/10

---

## 4. Elicit Research Agent

**Kategorie:** Recherche  
**Relevanzbewertung:** 7,5/10  
**Website:** https://elicit.com/  
**Aktualitätssignal:** Am 2. November 2026 hat Elicit dokumentiert, dass der Research Agent neben Fachartikeln auch Patente (USPTO, EPO, WIPO), FDA-Sicherheitsmeldungen, Open Targets, DepMap und ChEMBL durchsucht, jeweils über einen eigenen Skill; Ende Oktober wurden die alten Alerts durch planbare Routines ersetzt.

### Kurzbeschreibung

Rechercheagent für wissenschaftliche und regulatorische Evidenz, der Fachartikel, Patente und Behördendaten systematisch durchsucht und als Tabelle oder Bericht ausgibt, für Forschung, Innovation und Regulatory Affairs.

Der Research Agent stellt zuerst Rückfragen zu Quellen, Format und Abgrenzung. Danach zerlegt er die Frage in ein Suchprogramm, durchsucht über 138 Millionen Fachartikel, Web, klinische Studien und Regulierungsdokumente, bewertet die Treffer und fasst sie zusammen. Die konsultierten Quellen sind während der Arbeit sichtbar, die Ergebnisse lassen sich als Tabelle oder Text weiterbearbeiten.

Neu sind fünf Quelltypen ausserhalb der Fachliteratur. Patentdaten beantworten Fragen zu Inhaber:innen, Anmeldedaten und Ansprüchen. Die FDA-Meldesysteme FAERS und MAUDE zeigen Sicherheitssignale zu Medikamenten und Medizinprodukten; Ereignisraten lassen sich daraus nicht ableiten, weil Spontanmeldungen keine Bezugsgrösse haben. Hinzu kommen biomedizinische Datenbanken zu Genen, Krebszellen und Wirkstoffen. Mit Routines laufen solche Recherchen wiederkehrend und melden neue Evidenz per E-Mail.

### Nutzungsszenarien

- Innovation: Vor einer Produktentwicklung prüfen, welche Patente in einem Technologiefeld angemeldet sind und wem sie gehören.
- Medtech: Sicherheitsmeldungen zu vergleichbaren Medizinprodukten sammeln, bevor ein Zulassungsdossier entsteht.
- Pharma und Biotech: Evidenz zu einem Wirkstoffziel aus Literatur und Datenbanken in einer Tabelle zusammenführen.
- Strategie: Eine Routine einrichten, die monatlich neue Studien zu einem Marktthema meldet.

### Pricing

Basic: kostenlos, mit unbegrenzter Suche in Fachartikeln und begrenzter Agentennutzung. Plus: USD 11 pro Person und Monat. Pro: USD 39 (alternativ ausgewiesen USD 49) mit Routines und API-Zugang. Scale: USD 89 (alternativ USD 229) mit Admin-Panel. Enterprise: auf Anfrage, mit SSO und Single-Tenancy. Alle Preise bei jährlicher Zahlung; die Seite zeigt zwei Preissätze, vermutlich Standard und Industry, ohne das ausdrücklich zu benennen. Monatspreise sind nicht dokumentiert, ebenso welche Pläne die neuen Quelltypen nutzen dürfen.

### Datenschutz

Anbieter ist Elicit Research, PBC, in Kalifornien. Serverstandort: USA auf AWS, eine Region oder EU-Datenresidenz ist nicht dokumentiert; Enterprise erhält logisch isolierte Cluster. Training: Für Enterprise ausgeschlossen, auch vertraglich gegenüber den Modellanbietern; für Basic, Plus, Pro und Scale ist das nicht dokumentiert. SOC 2 Type II liegt seit Oktober 2025 vor. Der Auftragsverarbeitungsvertrag enthält EU-Standardvertragsklauseln, eine Schweizer Anpassung und den UK-Zusatz, Meldung von Verletzungen innert 72 Stunden. Die Datenschutzerklärung stammt von 2023. Für DSGVO und DSG ist Enterprise mit DPA eine solide Basis; in den kleineren Plänen sollten keine vertraulichen Projektdokumente hochgeladen werden. Self-Hosting ist nicht dokumentiert.

### Stärken

- Quellenbreite: Fachartikel, Patente und Behördendaten in einem Recherchelauf.
- Transparenz: Konsultierte Quellen sind sichtbar, Zahlen aus Datenbanken werden direkt zitiert.
- Methodik: Hinweise auf Grenzen der Daten, etwa fehlende Bezugsgrössen bei Spontanmeldungen.
- Vertrag: DPA mit Schweizer Anpassung und SOC 2 Type II.

### Schwächen

- Fokus: Stark biomedizinisch, für andere Branchen sind die neuen Quellen weniger ergiebig.
- Preise: Zwei Preissätze ohne klare Erklärung, Monatspreise fehlen.
- Datenstandort: Nur USA, keine EU-Region.
- Training: Für Nicht-Enterprise-Pläne nicht geregelt.

### Einschätzung für die Praxis

Elicit lohnt sich für Unternehmen in Life Sciences, Medtech und technologieintensiven Branchen, die Evidenz aus Literatur, Patenten und Behördendaten regelmässig zusammentragen. Für allgemeine Marktrecherche ist der Nutzen kleiner. Ein sinnvoller Test: im Gratisplan eine abgeschlossene Patent- oder Literaturrecherche wiederholen und prüfen, welche Treffer fehlen oder neu dazukommen. Bei positivem Ergebnis eine Routine im Pro-Plan für ein laufendes Projekt einrichten und die Meldungen einen Monat lang auswerten.

**Relevanzbewertung:** 7,5/10

---

## 5. Perplexity Teammates

**Kategorie:** Agents  
**Relevanzbewertung:** 7,6/10  
**Website:** https://www.perplexity.ai/hub/products/teammate  
**Aktualitätssignal:** Am 4. November 2026 hat Perplexity Teammates als Research Preview lanciert: dauerhafte Agenten mit eigenem Rechner, Gedächtnis und Slack-Anbindung, vorerst nur für Abonnent:innen des Einzelplans Max.

### Kurzbeschreibung

Dauerhaft laufende KI-Agenten, die eine feste Rolle übernehmen, Aufgaben nach Zeitplan oder Auslöser erledigen und sich in Slack ansprechen lassen, für Teams mit wiederkehrender Wissens- und Routinearbeit.

Jeder Teammate hat einen eigenen, dauerhaft offenen Arbeitsbereich und behält seine Rolle, bis sie geändert wird. Er merkt sich Projektziele, Aufgabenverlauf und geteilte Dateien und übernimmt Feedback in künftige Aufgaben. Ein Ziel zerlegt er selbst in Teilaufgaben, lässt parallele Agenten auf je eigenem Rechner arbeiten und liefert Berichte, Code-Änderungen oder Konfigurationen. Aufgaben laufen nach Zeitplan, etwa jeden Montag, oder auf ein Ereignis hin, etwa eine neue Nachricht.

In Slack lässt sich ein Teammate einem Kanal hinzufügen, Kolleg:innen geben ihm dort Aufträge oder fragen nach dem Stand. Anbindungen bestehen unter anderem zu Slack, GitHub, Gmail und Linear; wo es keine gibt, bedient der Agent Browser und Desktop selbst. Gespeicherte Zugangsdaten sind verschlüsselt und für den Agenten nicht einsehbar, die Nutzer:in kann den Desktop jederzeit übernehmen. Das Modell ist je Teammate wählbar.

### Nutzungsszenarien

- Vertrieb: Jeden Montag die Pipeline prüfen und auffällige Deals im Slack-Kanal melden lassen.
- Kundenbindung: Wöchentlich Hinweise auf Abwanderung bei Bestandskund:innen zusammentragen.
- Marktbeobachtung: Eine fortlaufende Wettbewerbsrecherche führen, die auf neue Meldungen reagiert.
- Website: Gemeldete Fehler auf der Website prüfen und Korrekturvorschläge zur Freigabe vorbereiten.

### Pricing

Kein Free Tier; Teammates sind nur im Einzelplan Max enthalten, der in der Presse mit USD 200 pro Monat oder USD 2000 pro Jahr angegeben wird, auf einer offiziellen Preisseite aber nicht bestätigt ist. Während einer Aktionsphase ist die Nutzung für Max gratis, danach zählt sie gegen die monatlichen Credits, zusätzliche Credits sind kaufbar. Enterprise Max kostet USD 325 pro Platz und Monat oder USD 3250 pro Jahr, enthält Teammates zum Start aber nicht standardmässig.

### Datenschutz

Serverstandort: Die Datenschutzerklärung vom 23. Oktober 2026 nennt keine Rechenzentren, Daten können unter anderem in den USA verarbeitet werden; EU-Datenresidenz ist nicht dokumentiert. Als EU- und UK-Vertretung sowie Datenschutzbeauftragte ist VeraSafe benannt, Standardvertragsklauseln gibt es auf Anfrage. Training: In Consumer-Plänen, auch Max, ist die Datennutzung standardmässig aktiv und abschaltbar; in Enterprise wird nicht trainiert. Aufbewahrungsfristen für Teammates sind nicht dokumentiert. SOC 2 Type II liegt vor, ein DPA besteht, ob er für Max-Einzelkonten gilt, ist nicht dokumentiert. Für DSGVO und DSG ist die Kombination aus Consumer-Plan, dauerhaften Zugriffen auf Slack, Gmail und GitHub und fehlender Datenregion heikel. Self-Hosting ist nicht dokumentiert.

### Stärken

- Dauerhaftigkeit: Rolle, Gedächtnis und Aufgabenverlauf bleiben über Sitzungen hinweg erhalten.
- Teamarbeit: Aufträge und Statusabfragen direkt in Slack.
- Isolation: Jeder Agent arbeitet auf eigenem Rechner, Zugangsdaten bleiben für ihn unsichtbar.
- Steuerung: Zeitpläne und Auslöser, Übernahme des Desktops jederzeit möglich.

### Schwächen

- Zugang: Nur Einzelplan Max, Enterprise vorerst ausgeschlossen.
- Reifegrad: Research Preview, Verhalten kann sich ändern.
- Datenschutz: Training im Max-Plan standardmässig aktiv, keine EU-Datenregion.
- Kosten: Credit-Verbrauch nach der Aktionsphase schwer abschätzbar.

### Einschätzung für die Praxis

Teammates zeigen, wie Agenten als ständige Mitarbeitende funktionieren können, sind aber derzeit eher ein Lernfeld als ein Produktivsystem für Unternehmen. Wer testen will, sollte das mit einem Max-Konto ohne Zugriff auf Kundendaten tun, das Training abschalten und einem Teammate eine eng umrissene Aufgabe geben, etwa eine wöchentliche Marktbeobachtung aus öffentlichen Quellen. Nach vier Wochen bewerten: Wie oft war das Ergebnis brauchbar, wie viele Credits wurden verbraucht, und welche Zugriffe brauchte der Agent tatsächlich.

**Relevanzbewertung:** 7,6/10

---

## 6. ElevenLabs Scribe v2 Realtime

**Kategorie:** Transkription  
**Relevanzbewertung:** 7,2/10  
**Website:** https://elevenlabs.io/realtime-speech-to-text-api  
**Aktualitätssignal:** Am 2. November 2026 hat ElevenLabs die Echtzeit-Spracherkennung Scribe v2 Realtime um eine Schwärzung von Entitäten erweitert: Namen, Adressen, Gesundheits- und Kartendaten werden noch während des Transkribierens ersetzt.

### Kurzbeschreibung

Spracherkennungsdienst für Echtzeit- und Dateitranskription per API mit über 90 Sprachen, für Unternehmen, die Transkription in eigene Anwendungen wie Callcenter, Meeting- oder Diktatlösungen einbauen.

Scribe gibt es als Modell für Dateien (Scribe v2), für Live-Audio (Scribe v2 Realtime) und als medizinische Variante. Die Echtzeitversion liefert Text mit etwa 150 Millisekunden Verzögerung, erkennt über 90 Sprachen und lässt sich mit bis zu 50 Fachbegriffen auf Namen und Produktbezeichnungen trimmen. Die Dateiversion unterscheidet bis zu 32 Sprecher:innen und verarbeitet Dateien bis 10 Stunden.

Neu ist die Schwärzung in Echtzeit. Ein Parameter legt fest, ob alle erkannten Entitäten oder nur Kategorien ersetzt werden: personenbezogene Daten wie Namen, Adressen, Telefonnummern und Kontonummern, Gesundheitsdaten wie Diagnosen und Medikamente sowie Kartendaten. Nach jedem Abschnitt kommen ursprünglicher und geschwärzter Text zurück, Platzhalter wie {NAME_0} halten erkennbar, dass es sich um dieselbe Person handelt. Die Funktion richtet sich an Entwickler:innen, eine fertige Meeting-App mit Bot bietet ElevenLabs nicht an.

### Nutzungsszenarien

- Kundendienst: Telefonate live transkribieren und Kartennummern sowie Adressen vor der Speicherung schwärzen.
- Gesundheitswesen: Gespräche dokumentieren, ohne dass Diagnosen und Namen im Klartext in Analysesysteme gelangen.
- Softwareanbieter: Eine eigene Meeting- oder Diktatfunktion mit Schwärzung in die Unternehmenssoftware einbauen.
- Compliance: Transkripte für Schulung und Qualitätssicherung nutzen, in denen Personendaten bereits ersetzt sind.

### Pricing

Free Tier: Gratisplan mit rund 2.5 Stunden Echtzeit-Transkription pro Monat. Starter: USD 6, Creator: USD 22, Pro: USD 99, Scale: USD 299, Business: USD 990 pro Monat, mit wachsenden Stundenkontingenten. API-Preis: Scribe v2 USD 0.22 pro Stunde, Scribe v2 Realtime USD 0.39 pro Stunde, Fachbegriffe plus USD 0.05 pro Stunde. Ob die Schwärzung einen Aufpreis kostet, ist nicht dokumentiert. Die Stunden je Plan sind aus den Preistabellen abgeleitet und sollten vor dem Kauf geprüft werden.

### Datenschutz

Audio gespeichert: Ja, Audio und Text werden standardmässig aufbewahrt, gelöschte Daten bleiben bis zu 30 Tage in Backups; nur der Zero Retention Mode für ausgewählte Enterprise-Kund:innen verhindert die Speicherung. Sichtbarer Bot: Nicht zutreffend, Scribe ist eine API; die Information und Einwilligung aller Gesprächsteilnehmenden liegt bei der einbauenden Organisation. Spracherkennung: in der Cloud von ElevenLabs, eine Verarbeitung auf dem Gerät ist nicht dokumentiert. Serverstandort: standardmässig USA, isolierte Umgebungen in der EU nur für Enterprise. Training: Für Nicht-Enterprise-Konten standardmässig aktiv, abschaltbar. ElevenLabs nennt SOC 2 Type II, ISO 27001, 27701 und 42001 und bietet einen DPA an. Für DSGVO und DSG reicht erst Enterprise mit EU-Umgebung und Zero Retention für Personendaten; die Schwärzung senkt das Risiko in nachgelagerten Systemen, nicht beim Anbieter selbst. Self-Hosting ist nicht dokumentiert.

### Stärken

- Datenschutz in der Anwendung: Schwärzung von Personen-, Gesundheits- und Kartendaten schon im Live-Transkript.
- Geschwindigkeit: Rund 150 Millisekunden Verzögerung bei Echtzeit-Transkription.
- Sprachen: Über 90 Sprachen, Fachbegriffe lassen sich vorgeben.
- Zertifizierungen: SOC 2 Type II, ISO 27001, 27701 und 42001.

### Schwächen

- Speicherung: Audio und Text werden ohne Enterprise-Vertrag aufbewahrt.
- Datenstandort: Standardmässig USA, EU nur in Enterprise.
- Training: Für Nicht-Enterprise-Konten standardmässig aktiv.
- Zielgruppe: Reine API, ohne Entwicklungsaufwand nicht nutzbar.

### Einschätzung für die Praxis

Scribe v2 Realtime ist für Unternehmen interessant, die Transkription selbst in Callcenter-, Meeting- oder Branchenlösungen einbauen und Personendaten früh aus dem Datenstrom entfernen müssen. Für den produktiven Einsatz mit Kund:innen- oder Gesundheitsdaten führt kein Weg an Enterprise mit EU-Umgebung und Zero Retention vorbei. Ein sinnvoller Test: im Gratisplan mit dem Training ausgeschaltet zehn nachgestellte Gespräche auf Deutsch und Schweizerdeutsch transkribieren und zählen, wie viele Namen, Adressen und Nummern die Schwärzung übersieht. Vor jedem Einsatz alle Gesprächsteilnehmenden informieren und einwilligen lassen.

**Relevanzbewertung:** 7,2/10

---

## Quellen

- Annamalai, K. (2025, 9. Dezember). New in Elicit: Research Agents. https://elicit.com/blog/introducing-research-agent-workflows
- CXOToday. (2026, 3. November). OpenAI follows Anthropic example, merges ChatGPT's Chat and Work tabs. https://cxotoday.com/ai/openai-follows-anthropic-example-merges-chatgpts-chat-and-work-tabs/
- Data Studios. (2026, 3. November). ChatGPT merges Chat and Work tabs in desktop app, Codex stays separate. https://www.datastudios.org/post/chatgpt-merges-chat-and-work-tabs-desktop-app-codex-stays-separate
- Dataconomy. (2026, 6. November). Perplexity launches always-on AI agents for work. https://dataconomy.com/2026/11/06/perplexity-launches-always-on-ai-agents-for-work/
- Digital Trends. (2026, 2. November). OpenAI merges Chat and Work in ChatGPT. https://www.digitaltrends.com/computing/openai-merges-chat-and-work-in-chatgpt/
- ElevenLabs. (2026, 16. Oktober). Certification renewals. https://elevenlabs.io/blog/certification-renewals
- ElevenLabs. (2026, 2. November). Changelog: November 2, 2026. https://elevenlabs.io/docs/changelog/2026/11/2
- ElevenLabs. (o. D.). API pricing. https://elevenlabs.io/pricing/api
- ElevenLabs. (o. D.). Data residency. https://elevenlabs.io/docs/overview/administration/data-residency
- ElevenLabs. (o. D.). Entity detection. https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection
- ElevenLabs. (o. D.). Is my data used to improve ElevenLabs' AI models? https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models
- ElevenLabs. (o. D.). Realtime Speech to Text API. https://elevenlabs.io/realtime-speech-to-text-api
- ElevenLabs. (o. D.). Zero Retention Mode. https://elevenlabs.io/docs/resources/zero-retention-mode
- Elicit. (2023, 12. September). Privacy Policy. https://elicit.com/operations/privacy
- Elicit. (2025, 1. April). Data Processing Addendum. https://elicit.com/operations/dpa
- Elicit. (2025, 30. Oktober). Elicit achieves SOC 2. https://elicit.com/blog/elicit-achieves-soc-2
- Elicit. (2026, 2. November). Where Elicit looks beyond research papers. https://elicit.com/blog/sources-of-elicit
- Elicit. (o. D.). Changelog. https://support.elicit.com/en/articles/14823097-changelog
- Elicit. (o. D.). Pricing. https://elicit.com/pricing
- Google. (2025, 9. Juni). Data regions support for Gemini features in Google Workspace. https://workspaceupdates.googleblog.com/2025/06/data-regions-support-for-gemini-features-in-google-workspace.html
- Google. (2026, 2. November). Get actionable insights with Gemini in Google Forms. Google Workspace Updates. https://workspaceupdates.googleblog.com/2026/11/get-actionable-insights-with-gemini-in-Google-Forms.html
- Google. (2026, 23. September). Gemini Omni 1.1 Flash now in Vids with improved extension quality, 1080p, and duration control. https://workspaceupdates.googleblog.com/2026/09/gemini-omni-11-flash-now-in-vids-with-improved-extension-quality-1080p-and-duration-control.html
- Google. (2026, 5. November). Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost. https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Compare Google Workspace pricing plans. https://workspace.google.com/pricing?hl=en
- Google. (o. D.). Google AI Pro & Ultra subscriptions. https://gemini.google/subscriptions/
- Google. (o. D.). Google Workspace pricing. https://workspace.google.com/pricing?hl=en_ch
- Google. (o. D.). Summarize & analyze responses with Gemini in Google Forms. https://support.google.com/docs/answer/16231981
- Luk, J. (2026, 16. Juli). Gemini Omni Flash now available in Google Vids. Google Workspace Blog. https://workspace.google.com/blog/product-announcements/introducing-gemini-omni-flash-in-google-vids
- Nack, J. (2026, 6. November). Gemini Omni 1.2 Flash: Fast, cost-effective, and reliable video generation and editing now generally available. Google Cloud Blog. https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available
- OpenAI. (2025, 5. Februar). Introducing data residency in Europe. https://openai.com/blog/introducing-data-residency-in-europe
- OpenAI. (o. D.). Enterprise privacy at OpenAI. https://openai.com/enterprise-privacy/
- OpenAI. (o. D.). How your data is used to improve model performance. https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
- OpenAI. (o. D.). Pricing. https://learn.chatgpt.com/docs/pricing
- Perplexity. (2026, 23. Oktober). Perplexity Privacy Notice. https://www.perplexity.ai/hub/legal/privacy-notice
- Perplexity. (2026, 4. November). Teammates are agents for complex, ongoing work. https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work
- Perplexity. (o. D.). Data collection at Perplexity. https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity
- Perplexity. (o. D.). Get started with Perplexity teammates. https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates
- Perplexity. (o. D.). Perplexity Teammates. https://www.perplexity.ai/hub/products/teammate
- Perplexity. (o. D.). What is Enterprise Max? https://www.perplexity.ai/help-center/en/articles/12310544-what-is-enterprise-max
- Releasebot. (2026, 5. November). Google Forms release notes. https://releasebot.io/updates/google/google-forms
