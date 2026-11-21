# KI-Tool-Analysen KW 47/2026

**Datum:** 22. November 2026  
**Recherchezeitraum:** 15. bis 22. November 2026

## Wochenzusammenfassung

Die Werkzeuge dieser Woche verlassen das Chatfenster und arbeiten dort, wo Dateien, Gespräche und Gesichter liegen: auf dem Desktop, im Telefon, im eigenen Rechenzentrum. Je näher ein Werkzeug an diesen Rohstoffen arbeitet, desto weniger entscheidet die Modellleistung über den Nutzen und desto mehr die Frage, welche Rechte es erhält und wer eingewilligt hat. Proton lässt in Lumo jede Aktion einzeln freigeben, sperren oder automatisch ausführen, Cloudflare stellt Clairic als offenes Modell für eigene Server bereit, HeyGen verlangt vor jedem Avatar eine Einwilligungsaufnahme mit Einmalcode, und Wispr nimmt Gespräche am Tisch ohne Bot auf, speichert aber in den USA. Die Steuerung verschiebt sich damit von der Auswahl eines Tools zur Vergabe von Zugriffsrechten. Wer einem Werkzeug Zugriff gibt, delegiert Verantwortung, und diese bleibt bei der Person, die den Zugriff erteilt hat.

- Proton Lumo Desktop (8,4/10): Ein Assistent mit Zugriff auf Dateien, Mail und Drittdienste, bei dem jede Aktion einzeln erlaubt, freigabepflichtig oder gesperrt ist, betrieben unter Schweizer Recht.
- GPT-6.2 Astra und Sol (8,2/10): Dokumente, Folien und Tabellen, die sich enger an vorhandene Vorlagen halten, dazu EU-Datenhaltung für API-Projekte mit Datenresidenz.
- Cloudflare Clairic (7,6/10): Strukturierte Werte mit Konfidenzangabe aus Texten, Bildern und PDFs, als offenes Modell unter Apache-2.0 auch auf eigener Hardware.
- Praxisregel: Bevor ein Werkzeug Zugriff auf Dateien, Postfach oder Gespräche erhält, schriftlich festhalten, welche Aktionen es ohne Rückfrage ausführen darf, welche eine Freigabe brauchen und welche gesperrt sind.

**Trend:** KI-Werkzeuge rücken an Dateien, Gespräche und Personen heran, und die Rechtevergabe wird zur wichtigsten Führungsaufgabe beim Einsatz.

| Kategorie | Tool | Relevanz |
|---|---|---:|
| Text | GPT-6.2 Astra und Sol | 8,2/10 |
| Design | HeyGen Avatar 6 | 7/10 |
| Data / Wissen | Cloudflare Clairic | 7,6/10 |
| Recherche | Gemini Notebook interaktive Seiten | 7,3/10 |
| Agents | Proton Lumo Desktop | 8,4/10 |
| Transkription | Wispr Flow Notetaker | 7,1/10 |

---

## 1. GPT-6.2 Astra und Sol

**Kategorie:** Text  
**Relevanzbewertung:** 8,2/10  
**Website:** https://openai.com/index/introducing-gpt-6-2-astra-sol/  
**Aktualitätssignal:** Am 17. November 2026 hat OpenAI GPT-6.2 Astra und GPT-6.2 Sol veröffentlicht, in ChatGPT Work, Codex und in der API. Der API-Preis von Astra sinkt gegenüber GPT-6 Astra um 20 Prozent.

### Kurzbeschreibung

Zwei neue Sprachmodelle in ChatGPT: Astra für anspruchsvolle Fach- und Analyseaufgaben, Sol für die tägliche Arbeit, für Wissensarbeiter:innen und Teams, die Dokumente, Folien und Tabellen erstellen.

Astra ist das leistungsfähigste Modell von OpenAI für lange, komplexe Aufgaben. Sol ist auf Effizienz ausgelegt und in neuen Work-Chats der Standard. Neu ist vor allem der Umgang mit Büroformaten: Folien, Tabellen und Dokumente sollen sich enger an mitgelieferte Vorlagen und an die Konventionen des jeweiligen Fachgebiets halten. Eine Folienvorlage kann als Originaldatei oder als Bildschirmfoto übergeben werden.

Die Modelle laufen in ChatGPT Work, dem Arbeitsbereich für mehrstufige Aufgaben, und in Codex, dem Programmierassistenten. Beide teilen sich das Nutzungskontingent. OpenAI stuft beide Modelle im eigenen Sicherheitsrahmen bei Cyberfähigkeiten in die höchste Stufe ein und schränkt deshalb einzelne Sicherheitsanwendungen ein, was auch legitime Schwachstellenforschung betreffen kann. Die Grösse des Kontextfensters in ChatGPT ist in der Ankündigung nicht dokumentiert.

### Nutzungsszenarien

- Geschäftsleitung: Quartalsbericht aus Rohdaten in die bestehende Firmenvorlage für Folien überführen.
- Finanzen: Bewertungs- oder Budgetmodell als Tabelle mit nachvollziehbaren Formeln aufbauen lassen.
- Beratung: Offerten und Konzepte im Stil früherer Dokumente erstellen, ohne Vorlage neu zu formatieren.
- Recht und Compliance: Lange Vertragsentwürfe strukturieren und auf fehlende Klauseln prüfen lassen.
- Entwicklung: In Codex Fehler über mehrere Dienste hinweg nachverfolgen und beheben.

### Pricing

In ChatGPT für Plus, Pro, Business, Enterprise und Edu verfügbar, bei Enterprise und Edu nach Freischaltung durch die Administration. Für den Free-Plan ist der Zugang nicht angekündigt. Die aktuellen Monatspreise der ChatGPT-Pläne waren auf der offiziellen Preisseite nicht abrufbar und werden hier nicht genannt. API: Astra USD 8 pro Million Eingabe-Tokens, USD 0.40 für zwischengespeicherte Eingaben, USD 40 pro Million Ausgabe-Tokens. Sol: USD 2, USD 0.10 und USD 10. Ab 272 000 Eingabe-Tokens verdoppeln sich Eingabe- und Cache-Preise.

### Datenschutz

Serverstandort: Für API-Projekte mit Datenresidenz unterstützen beide Modelle die Regionen USA und EU für Standard-, Fast- und Batch-Verarbeitung; der Ultrafast-Modus läuft nur in den USA. Neue ChatGPT-Enterprise- und Edu-Arbeitsbereiche können mit Datenhaltung in Europa eingerichtet werden, für Business ist das nicht dokumentiert. Eine Schweizer Region ist nicht dokumentiert. Policies: In Business, Enterprise, Edu und der API werden Geschäftsdaten standardmässig nicht für Training genutzt, gelöschte Chats werden innerhalb von 30 Tagen entfernt, SOC 2 Type 2, Verschlüsselung mit AES-256 und TLS 1.2. In Plus und Pro können Inhalte für Training genutzt werden, sofern man nicht widerspricht. Für Nutzer:innen in EWR und Schweiz ist OpenAI Ireland Limited verantwortlich. DSGVO und DSG: Mit Business- oder Enterprise-Vertrag und DPA vertretbar, für Plus und Pro nur ohne Personendaten und mit deaktiviertem Training. Self-Hosting ist nicht möglich.

### Stärken

- Büroformate: Vorlagentreue bei Folien, Tabellen und Dokumenten als ausdrücklicher Entwicklungsschwerpunkt.
- Zwei Stufen: Sol für Routine, Astra für schwierige Aufgaben im selben Arbeitsbereich.
- Kosten: API-Preis von Astra um 20 Prozent gesenkt.
- Datenresidenz: EU-Region für API-Projekte und neue Enterprise-Arbeitsbereiche.

### Schwächen

- Zugang: Kein Free-Plan, Enterprise und Edu erst nach Freischaltung.
- Transparenz: Kontextfenster in ChatGPT und aktuelle Planpreise nicht dokumentiert.
- Einschränkungen: Strengere Schutzmechanismen können legitime Sicherheitsarbeit blockieren.
- Datenschutz: Training mit Inhalten in Plus und Pro, solange nicht widersprochen wird.

### Einschätzung für die Praxis

Für Unternehmen, die bereits ChatGPT Business oder Enterprise nutzen, ist GPT-6.2 ein Update, das sich im Alltag bemerkbar machen dürfte, weil es auf das häufigste Ärgernis zielt: Ergebnisse, die nach dem Erstellen neu formatiert werden müssen. Ein sinnvoller Test: drei wiederkehrende Dokumente mit Firmenvorlage, etwa Monatsreport, Offerte und Präsentation, einmal mit Sol und einmal mit Astra erstellen und den Nacharbeitsaufwand in Minuten messen. Für sensible Inhalte gilt weiterhin: nur im Geschäftsplan mit DPA, nicht im privaten Plus-Konto.

**Relevanzbewertung:** 8,2/10

---

## 2. HeyGen Avatar 6

**Kategorie:** Design  
**Relevanzbewertung:** 7/10  
**Website:** https://www.heygen.com/models/heygen-avatar-6  
**Aktualitätssignal:** Am 17. November 2026 hat HeyGen das Avatar-Modell Avatar 6 mit technischem Bericht vorgestellt: sprechende Videoavatare aus einem einzigen Foto, nativ in 2K und ohne Längenbegrenzung pro Generierung.

### Kurzbeschreibung

Videomodell, das aus einem Foto oder einer kurzen Aufnahme einen sprechenden Avatar erzeugt, für Kommunikation, Schulung und Marketing ohne Filmdreh.

Avatar 6 erzeugt aus einem Foto und optional einer kurzen Videoaufnahme als Identitätsreferenz ein sprechendes Video. Jedes Bild wird nativ in 2880 x 1620 Pixeln erzeugt. HeyGen zeigt Beispiele von 25 bis 28 Minuten, die in einem Durchgang aus einer Tonspur entstanden sind. Gesten lassen sich per Textanweisung an einzelne Wörter koppeln, etwa ein Daumen hoch bei der Begrüssung. Zwei Sprecher:innen können im selben Bild auftreten.

Neu ist auch die Bearbeitung bestehender Sprechvideos: Ändert man einzelne Wörter im Skript, werden nur diese Stellen neu erzeugt, in der Stimme der Person. Für Avatare aus Videomaterial muss die abgebildete Person vorab eine Einwilligung vor der Kamera aufnehmen, die einen einmaligen Code enthält. Erst wenn HeyGen diese Aufnahme mit dem Material abgeglichen hat, lässt sich der Avatar verwenden. Welche Sprachen Avatar 6 selbst unterstützt, ist im Bericht nicht dokumentiert; die Pläne nennen 30 bis 175 Sprachen und Dialekte.

### Nutzungsszenarien

- Interne Kommunikation: Wöchentliche Updates der Geschäftsleitung als kurzes Video, ohne jedes Mal zu filmen.
- Schulung: Lernvideos aktualisieren, indem nur geänderte Sätze im Skript neu erzeugt werden.
- Vertrieb: Produkterklärungen in mehreren Sprachen mit derselben Person produzieren.
- Marketing: Podcast-Ausschnitte oder Interviews mit zwei Avataren im selben Bild umsetzen.

### Pricing

Free Tier: USD 0 pro Monat, drei Videos pro Monat mit Wasserzeichen, je höchstens eine Minute, Zugang zu Avatar 6. Creator: USD 29 pro Monat oder USD 24 bei Jahreszahlung, 600 Credits, Avatar 6 Turbo, Export in 1080p, Videos bis 30 Minuten. Pro: USD 49 pro Monat, 1000 Credits, Avatar 6 Pro, eine professionelle Stimmkopie, 4K-Export; höhere Stufen bis USD 4300 für 100 000 Credits. Business: USD 149 pro Monat, 1500 Credits, plus USD 20 pro weiterem Teammitglied, SSO. Enterprise: Preis auf Anfrage. Der Credit-Verbrauch hängt von Modell, Dauer und Komplexität ab, ein fester Preis pro Credit ist nicht ausgewiesen.

### Datenschutz

Serverstandort: Alle Kundendaten liegen in den USA auf AWS, eine EU-Region ist nicht dokumentiert. Übermittlungen aus EU und Schweiz stützen sich auf das EU-US- und das Swiss-US Data Privacy Framework sowie Standardvertragsklauseln. Policies: SOC 2 Type II, Verschlüsselung mit AES-256 und TLS 1.2, jährliche Penetrationstests. Training: Inhalte von Nicht-Enterprise-Kund:innen werden für das Training genutzt, ein Widerspruch per E-Mail ist möglich; bei biometrischen Daten spricht der Biometrie-Hinweis von Einwilligung. Enterprise-Daten sind standardmässig vom Training ausgenommen. Ein DPA gibt es nur für Enterprise-Kund:innen. Biometrische Daten eines Avatars werden innerhalb von 60 Tagen nach dessen Löschung vernichtet. Eine C2PA-Kennzeichnung ist nicht dokumentiert. DSGVO und DSG: Gesichts- und Stimmdaten sind besonders schützenswert; ohne DPA, mit Training und US-Speicherung für Mitarbeitende nur mit ausdrücklicher, freiwilliger Einwilligung vertretbar. Self-Hosting ist nicht möglich.

### Stärken

- Qualität: Natives 2K und lange Videos aus einer Generierung.
- Bearbeitung: Einzelne Wörter ändern, ohne das ganze Video neu zu erzeugen.
- Einwilligung: Verifizierte Kameraaufnahme mit Einmalcode vor jedem Avatar aus Videomaterial.
- Einstieg: Gratisplan mit Zugang zu Avatar 6.

### Schwächen

- Datenstandort: Ausschliesslich USA.
- Training: Standardmässig Nutzung von Inhalten ausserhalb von Enterprise, Widerspruch nur per E-Mail.
- Vertrag: DPA nur im Enterprise-Plan.
- Kennzeichnung: Keine dokumentierte maschinenlesbare Herkunftskennzeichnung, Pflichten aus Art. 50 AI Act liegen bei den Anwender:innen.

### Einschätzung für die Praxis

Avatar 6 macht Videokommunikation ohne Dreh praktikabel, verschiebt die Verantwortung aber auf die Organisation, die das Gesicht einer Person einsetzt. Sinnvoll ist ein Einsatz für Schulungs- und Erklärvideos mit einer Person, die freiwillig und schriftlich eingewilligt hat und den Avatar jederzeit löschen lassen kann. Videos sollten sichtbar als KI-generiert gekennzeichnet werden. Ein Test im Gratisplan mit einem Foto der verantwortlichen Person und einem Skript von einer Minute zeigt, ob Lippenbewegung und Aussprache auf Deutsch genügen.

**Relevanzbewertung:** 7/10

---

## 3. Cloudflare Clairic

**Kategorie:** Data / Wissen  
**Relevanzbewertung:** 7,6/10  
**Website:** https://developers.cloudflare.com/workers-ai/models/clairic/  
**Aktualitätssignal:** Am 18. November 2026 hat Cloudflare die überarbeiteten Extraktionsmodelle Clairic und Clairic-flash als offene Gewichte unter Apache-2.0 veröffentlicht. Beide sind zusätzlich über Workers AI nutzbar.

### Kurzbeschreibung

Spezialisiertes Modell, das aus Texten, Bildern und PDFs typisierte Werte wie Beträge, Daten oder Kategorien mit Konfidenzangabe ausliest, für Teams, die Belege, Verträge oder Formulare automatisiert verarbeiten.

Clairic ist kein Chatmodell, sondern ein Extraktionsmodell. Man übergibt einen Text oder ein Dokument und eine Liste von Feldern mit Datentyp, etwa Rechnungsbetrag als Zahl, Fälligkeitsdatum als Datum oder Vertragsart als Auswahlliste. Das Modell liefert für jedes Feld einen Wert, eine Konfidenzangabe und die Wahrscheinlichkeit, dass die Antwort im Dokument gar nicht enthalten ist. Bei Textfeldern zeigt es die Fundstelle im Original. Neben Extraktion kann es Werte berechnen, schätzen und prognostizieren, jeweils mit Bandbreite.

Pro Anfrage verarbeitet Clairic bis zu vier Bilder oder PDF-Seiten. Es gibt zwei Grössen: Clairic mit rund 27 Milliarden Parametern und Clairic-flash mit rund 9 Milliarden Parametern, beide auf Basis offener Qwen-Modelle. Clairic ist auf Workers AI als Preview markiert, Clairic-flash als frühe Research-Preview. Cloudflare bezeichnet die publizierten Genauigkeitswerte als interne Messungen, öffentliche Benchmarks fehlen noch. Welche Sprachen unterstützt werden, insbesondere Deutsch, ist nicht dokumentiert.

### Nutzungsszenarien

- Buchhaltung: Betrag, Mehrwertsteuer, Lieferant und Fälligkeit aus eingehenden Rechnungen auslesen und nur unsichere Fälle manuell prüfen.
- Vertragsmanagement: Laufzeit, Kündigungsfrist und Verlängerungsklauseln aus Mietverträgen als Tabelle erfassen.
- Versicherung und Schadenfall: Angaben aus fotografierten Formularen strukturiert übernehmen.
- Kundendienst: Anliegen aus E-Mails in feste Kategorien und Dringlichkeitsstufen einordnen.

### Pricing

Open Source: Gewichte kostenlos unter Apache-2.0 auf Hugging Face, Betriebskosten für eigene GPU-Server tragen die Nutzer:innen. Workers AI: Free Tier mit 10 000 Neurons pro Tag, danach USD 0.011 pro 1000 Neurons. Clairic kostet bis 1. Dezember 2026 USD 0.10 pro Million Eingabe-Tokens, danach USD 0.24. Clairic-flash kostet USD 0.10 pro Million Eingabe-Tokens. Ausgabe-Tokens werden nicht verrechnet, Bilder und PDFs werden in Tokens umgerechnet.

### Datenschutz

Self-Hosting: Ja, die Gewichte lassen sich mit vLLM, SGLang oder Docker auf eigenen Servern betreiben; dann verlassen die Dokumente die eigene Infrastruktur nicht. Konkrete Hardwareanforderungen sind nicht dokumentiert. Workers AI: Cloudflare nutzt Kundeninhalte nicht für Training und speichert Ein- und Ausgaben bei Standardanfragen nicht über die Verarbeitung hinaus, ausgenommen bei Logging über AI Gateway, Speicherdiensten oder Batch-Funktionen. Betriebsmetadaten wie Zeitstempel und Tokenzahlen werden aufbewahrt. Serverstandort: Eine EU-Verarbeitung für Clairic ist auf den gelesenen Seiten nicht dokumentiert. Das Modell wird ohne Gewährleistung bereitgestellt und kann eingestellt werden. DSGVO und DSG: Im Self-Hosting gut umsetzbar, bei Workers AI mit Cloudflare-DPA und ohne Logging vertretbar.

### Stärken

- Kontrolle: Offene Gewichte unter Apache-2.0, Betrieb im eigenen Rechenzentrum möglich.
- Nachvollziehbarkeit: Konfidenz, Wahrscheinlichkeit für fehlende Angaben und Fundstelle pro Feld.
- Kosten: Ausgaben werden nicht verrechnet, tiefer Preis pro Eingabe.
- Typisierung: Ausgaben folgen einem festen Schema statt freiem Text.

### Schwächen

- Reifegrad: Beide Modelle im Preview-Status, ohne Gewährleistung.
- Belege: Genauigkeit nur aus internen Messungen, keine öffentlichen Benchmarks.
- Sprachen: Unterstützung für Deutsch nicht dokumentiert.
- Aufwand: Einbindung erfordert Entwicklungskenntnisse, keine Oberfläche für Fachanwender:innen.

### Einschätzung für die Praxis

Clairic ist für Unternehmen interessant, die Dokumente in grossen Mengen verarbeiten und die Daten nicht an einen externen Dienst geben wollen. Die Konfidenzangabe pro Feld erlaubt einen Ablauf, in dem Menschen nur noch die unsicheren Fälle prüfen. Ein sinnvoller Test: 100 bereits manuell erfasste deutschsprachige Rechnungen oder Verträge durch Clairic-flash auf Workers AI laufen lassen, die Treffer mit den bekannten Werten vergleichen und festlegen, ab welcher Konfidenz ein Wert ohne Prüfung übernommen wird. Erst danach lohnt sich der Aufbau eines eigenen Servers.

**Relevanzbewertung:** 7,6/10

---

## 4. Gemini Notebook interaktive Seiten

**Kategorie:** Recherche  
**Relevanzbewertung:** 7,3/10  
**Website:** https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites/  
**Aktualitätssignal:** Am 16. November 2026 hat Google in Gemini Notebook, dem früheren NotebookLM, interaktive Seiten eingeführt. Die Funktion wird weltweit im Web ausgerollt, auch für Google-Workspace-Kund:innen; die Mobile-App folgt.

### Kurzbeschreibung

Funktion im Recherche- und Schreibassistenten Gemini Notebook, die aus hochgeladenen Quellen und Notizen interaktive Webseiten wie Zeitachsen, Dashboards oder Tracker erzeugt, für Teams, die Rechercheergebnisse weitergeben.

Gemini Notebook arbeitet mit Quellen, die man selbst hochlädt, und beantwortet Fragen auf deren Grundlage. Neu kann man im Chat eine Seite anfordern und beschreiben, was sie zeigen soll. Google nennt als Beispiele eine interaktive Zeitachse, ein Dashboard mit Quartalsumsätzen oder einen Projekttracker mit Aufgaben und Terminen. Die fertige Seite öffnet sich in einem neuen Tab und lässt sich mit anderen teilen.

Damit wird aus einer Recherche ein Ergebnis, das andere ohne Zugriff auf das Notizbuch erkunden können. Welche Quelltypen für Seiten unterstützt werden, wie geteilte Seiten geschützt sind und ob sie nachträglich bearbeitet werden können, ist in der Ankündigung nicht dokumentiert. Die Funktion steht Personen ab 18 Jahren zur Verfügung.

### Nutzungsszenarien

- Marktanalyse: Studien und Berichte hochladen und daraus ein klickbares Dashboard für die Geschäftsleitung erzeugen.
- Projektleitung: Protokolle und Pläne in einen Tracker mit Aufgaben und Terminen überführen.
- Weiterbildung: Fachliteratur als interaktive Zeitachse oder Lernseite für Mitarbeitende aufbereiten.
- Verwaltungsrat: Hintergrundmaterial zu einer Entscheidung als navigierbare Übersicht bereitstellen.

### Pricing

Free Tier: Gemini Notebook ist im kostenlosen Google-Konto enthalten. Google AI Plus: USD 4.99 pro Monat mit mehr Notizbüchern und Audio-Übersichten. Google AI Pro: USD 19.99 pro Monat mit fünfmal höheren Limits. Google AI Ultra: ab USD 99.99 pro Monat. Gemini with Google Workspace: ab USD 14 pro Lizenz und Monat; Gemini Enterprise ab USD 30. Konkrete Limits für Quellen und Seiten sowie CHF-Preise sind nicht dokumentiert.

### Datenschutz

Privatkonten: In der EWR und der Schweiz ist Google Ireland Limited Anbieterin. Chats mit Notizbüchern werden gemäss Gemini-Verlauf gespeichert und können von menschlichen Prüfer:innen gelesen und zur Verbesserung genutzt werden; geprüfte Chats werden bis zu drei Jahre aufbewahrt. Hochgeladene Quelldateien werden nicht direkt für das Training genutzt. Workspace: Kundendaten werden ohne Erlaubnis nicht für Training genutzt und nicht von Menschen geprüft, Prompts und Antworten in Gemini Notebook werden nach der Sitzung nicht aufbewahrt. Zertifizierungen: SOC 1 bis 3, ISO 27001, 27701 und 42001. Serverstandort: Datenregionen für Gemini Notebook sind nicht verbindlich dokumentiert; die Datenregion-Einstellungen von Workspace gelten nach Google-Hilfe nicht für Gemini Notebook. Freigaberegeln für geteilte Seiten sind nicht dokumentiert. DSGVO und DSG: Mit Workspace-Vertrag für interne Unterlagen vertretbar, im Privatkonto nur ohne vertrauliche Inhalte. Self-Hosting ist nicht möglich.

### Stärken

- Quellenbindung: Antworten und Seiten beruhen auf selbst hochgeladenen Unterlagen.
- Weitergabe: Rechercheergebnisse als interaktive Seite statt als langer Text.
- Verfügbarkeit: Weltweit, im Gratiskonto und in Workspace.
- Workspace-Schutz: Kein Training und keine menschliche Prüfung bei Geschäftskonten.

### Schwächen

- Dokumentation: Quelltypen, Bearbeitung und Freigabe geteilter Seiten nicht beschrieben.
- Datenregion: Workspace-Regionseinstellungen gelten nicht für Gemini Notebook.
- Privatkonten: Menschliche Prüfung und Aufbewahrung bis drei Jahre.
- Plattform: Zum Start nur im Web.

### Einschätzung für die Praxis

Interaktive Seiten schliessen eine Lücke zwischen Recherche und Entscheidung: Wer eine Analyse vorbereitet, kann sie als navigierbare Übersicht weitergeben statt als Dokument von zwanzig Seiten. Für Unternehmen ist der Einsatz nur über ein Workspace-Konto sinnvoll, weil dort Training und menschliche Prüfung ausgeschlossen sind. Ein sinnvoller Test: fünf öffentliche Marktstudien hochladen, ein Dashboard anfordern und jede dargestellte Zahl gegen die Quelle prüfen, bevor die Seite geteilt wird. Vor dem Teilen sollte geklärt sein, wer die Seite sehen kann.

**Relevanzbewertung:** 7,3/10

---

## 5. Proton Lumo Desktop

**Kategorie:** Agents  
**Relevanzbewertung:** 8,4/10  
**Website:** https://proton.me/lumo  
**Aktualitätssignal:** Am 17. November 2026 hat Proton Lumo Desktop für Windows, macOS und Linux veröffentlicht, zusammen mit Connectors, zeitgesteuerten Aufgaben und Skills.

### Kurzbeschreibung

Datenschutzorientierter KI-Assistent des Genfer Anbieters Proton als Desktop-App, der auf Dateien, Proton Mail und Drittdienste zugreift und Aufgaben zeitgesteuert ausführt, für Unternehmer:innen und Teams mit hohen Vertraulichkeitsanforderungen.

Lumo Desktop erweitert den Assistenten um Connectors, also Verbindungen zu Werkzeugen und Diensten. Dazu gehören lokale Dateien, die Kommandozeile, das Abrufen von Webseiten, Proton Mail über die Mail Bridge, Google Drive, Jira, Confluence sowie eigene MCP-Server. MCP ist ein offener Standard, über den KI-Assistenten an fremde Anwendungen angebunden werden. Für jede Aktion eines Connectors legt man fest, ob sie automatisch läuft, eine Freigabe braucht oder gesperrt ist, etwa Posteingang durchsuchen erlaubt, E-Mail senden nur nach Rückfrage, Löschen gesperrt.

Mit Schedules lassen sich Aufgaben einmalig oder wiederkehrend ausführen, in Alltagssprache beschrieben und vor dem Start zur Prüfung vorgelegt. Jede Aufgabe hat eigene Berechtigungen. Skills sind wiederverwendbare Anweisungen mit Referenzdateien. Connectors und Schedules gibt es nur in der Desktop-App. Lumo nutzt nach Angaben von Proton ausschliesslich offene Sprachmodelle, welche genau, ist nicht dokumentiert.

### Nutzungsszenarien

- Geschäftsführung: Jeden Montag eingegangene Offertanfragen aus Proton Mail zusammenfassen lassen, ohne dass Lumo antworten darf.
- Projektleitung: Offene Jira-Tickets und Confluence-Seiten zu einem Wochenstatus verdichten.
- Administration: Lokale Ordner nach Verträgen mit bald ablaufender Kündigungsfrist durchsuchen.
- Beratung: Wiederkehrende Rechercheaufträge als Skill mit festen Quellen und Formatvorgaben hinterlegen.

### Pricing

Free Tier: USD 0, ohne Kreditkarte, mit begrenzter Nutzung, begrenztem Verlauf und einem Projekt; Limits nicht als Zahlen ausgewiesen. Lumo Plus: USD 9.99 pro Monat bei Jahreszahlung (USD 119.88 pro Jahr, Listenpreis USD 12.99). Lumo Professional für Unternehmen: USD 11.99 pro Person und Monat bei Jahreszahlung (USD 143.88), mit Administrationswerkzeugen und 14 Tagen Testphase. Proton Workspace Premium mit Lumo, Mail, Drive und VPN: USD 14.99 pro Person und Monat im ersten Jahr. CHF-Preise werden auf der Preisseite angeboten, wurden hier aber nicht ausgelesen.

### Datenschutz

Serverstandort: Europäische Infrastruktur ausserhalb des US CLOUD Act, unter Schweizer Datenschutzrecht; der erste eigene GPU-Cluster entsteht in der Schweiz. Ein genauer Rechenzentrumsstandort ist nicht dokumentiert. Policies: Der gespeicherte Chatverlauf ist mit Zero-Access-Verschlüsselung geschützt, Proton selbst kann ihn nicht lesen. Während der Verarbeitung entschlüsselt der Inferenzserver die Anfrage jedoch und verarbeitet sie im Klartext, danach wird sie verworfen. Proton führt keine Logs der Gespräche und nutzt weder Chats noch Inhalte verbundener Dienste für Training oder Werbung. Der Code ist quelloffen. Für das Business-Angebot nennt Proton ISO 27001 und SOC 2. DSGVO und DSG: Proton bezeichnet Lumo als DSGVO-konform; für Unternehmen im DACH-Raum ist es gut vertretbar, sofern die Rechte der Connectors restriktiv gesetzt sind. Self-Hosting ist nicht vorgesehen.

### Stärken

- Rechtevergabe: Für jede Aktion einzeln erlauben, freigeben lassen oder sperren.
- Datenschutz: Schweizer Anbieter, europäische Server, kein Training, kein Logging.
- Offenheit: Quelloffener Code, offene Modelle und MCP für eigene Anbindungen.
- Plattformen: Windows, macOS und Linux.

### Schwächen

- Verschlüsselung: Inferenz nicht Ende-zu-Ende verschlüsselt, nur der gespeicherte Verlauf.
- Voreinstellung: Connectors sind in Gesprächen standardmässig aktiv.
- Risiko: Kommandozeilen- und Dateizugriff ohne dokumentierte Sandbox.
- Transparenz: Eingesetzte Modelle und Free-Tier-Limits nicht konkret benannt.

### Einschätzung für die Praxis

Lumo Desktop ist für Unternehmen im DACH-Raum der derzeit naheliegendste Weg, einen Agenten mit Zugriff auf Mail und Dateien zu testen, ohne Daten in die USA zu geben. Das Rechtemodell pro Aktion ist dafür die Voraussetzung, wirkt aber nur, wenn es bewusst gesetzt wird. Empfehlung: Kommandozeile und Löschfunktionen zu Beginn sperren, Senden nur mit Freigabe erlauben und die erste zeitgesteuerte Aufgabe auf reines Lesen beschränken, etwa eine wöchentliche Zusammenfassung des Posteingangs. Nach zwei Wochen prüfen, welche Freigaben tatsächlich nötig waren.

**Relevanzbewertung:** 8,4/10

---

## 6. Wispr Flow Notetaker

**Kategorie:** Transkription  
**Relevanzbewertung:** 7,1/10  
**Website:** https://wisprflow.ai/post/notetaker-on-iphone  
**Aktualitätssignal:** Am 18. November 2026 hat Wispr den Notetaker auf das iPhone gebracht. Damit lassen sich Gespräche vor Ort aufnehmen, transkribieren und zusammenfassen; die Funktion ist für alle Nutzer:innen kostenlos.

### Kurzbeschreibung

Meeting-Assistent der Diktat-App Wispr Flow, der auf Mac und Windows Online-Meetings und neu auf dem iPhone Gespräche vor Ort aufnimmt, transkribiert und zusammenfasst, ohne einen Bot in das Meeting zu schicken.

Der Notetaker zeichnet über das Mikrofon des Geräts auf. Auf dem Desktop erfasst er Online-Meetings aus jeder Anwendung, auf dem iPhone Gespräche im Raum. Telefonate und Videoanrufe auf dem iPhone werden nicht aufgenommen. Die Aufnahme startet nur, wenn jemand sie auslöst, etwa über ein Widget, das Kontrollzentrum oder die Aktionstaste, und läuft bei gesperrtem Bildschirm weiter. Ohne Verbindung wird weiter aufgezeichnet und später verarbeitet.

Danach liefert Wispr ein vollständiges Transkript mit Sprecherkennzeichnung und eine Zusammenfassung mit Entscheiden, Terminen und Aufgaben. Fragen lassen sich zu einem oder zu allen Meetings stellen. Notizen werden mit dem Desktop synchronisiert und können per Link oder über MCP an andere KI-Werkzeuge weitergegeben werden. Jeder Aufnahmebildschirm erinnert an die Einwilligung. Welche Sprachen der Notetaker unterstützt, insbesondere Deutsch und Schweizerdeutsch, ist nicht dokumentiert.

### Nutzungsszenarien

- Geschäftsführung: Gespräch mit einem Lieferanten vor Ort aufnehmen und die Zusagen beider Seiten als Aufgabenliste erhalten.
- Beratung: Workshops im Kundenraum dokumentieren, ohne einen Laptop aufzustellen.
- Personalgespräche: Nur nach ausdrücklicher Einwilligung, Entscheide und nächste Schritte festhalten.
- Wissensmanagement: Über alle Meetings fragen, wann eine bestimmte Entscheidung gefallen ist.

### Pricing

Free Tier: USD 0, Notetaker mit Sprechererkennung, Fragen an Meetings und MCP-Zugang; auf dem iPhone kostenlos für alle. Die Seite nennt gleichzeitig unbegrenzte Meetings und ein wöchentliches Limit, Aufnahmen unter fünf Minuten zählen nicht. Pro: USD 15 pro Person und Monat oder USD 12 bei Jahreszahlung, mit unbegrenztem Verlauf und Team-Arbeitsbereich. Growth: Preis auf der Seite uneinheitlich ausgewiesen, zwischen USD 18 und USD 33 pro Person und Monat je nach Zahlungsweise und Notetaker-Umfang, mit SSO und HIPAA. Enterprise: Preis auf Anfrage.

### Datenschutz

Audio gespeichert: Ja, Meeting-Audio wird verschlüsselt auf dem Gerät und in der Cloud für eine begrenzte Zeit aufbewahrt und danach automatisch gelöscht; eine konkrete Frist ist nicht dokumentiert. Transkripte liegen zur Synchronisation in der Cloud von Wispr, die Aufbewahrung ist einstellbar. Sichtbarer Bot: Nein, es tritt kein Bot bei, die Aufnahme läuft lokal auf dem Gerät. Andere Teilnehmende sehen damit nicht, dass aufgezeichnet wird; die Einwilligung aller Teilnehmenden liegt vollständig bei den Nutzer:innen. Spracherkennung: in der Cloud, nicht auf dem Gerät. Serverstandort: USA auf AWS, Nord-Virginia und Nordkalifornien, eine Datenhaltung ausserhalb der USA wird nicht angeboten. Drittanbieter für KI verarbeiten Inhalte mit Vereinbarungen ohne Datenspeicherung, bei einzelnen Funktionen gilt das nicht. Training: Einstellung Improve the model for everyone, abschaltbar, in Growth und Enterprise standardmässig aus. Policies: SOC 2 Type II, ISO 27001 je nach Seite erteilt oder ausstehend, HIPAA mit BAA ab Growth, DPA mit Standardvertragsklauseln. DSGVO und DSG: Nur mit DPA, deaktiviertem Training und dokumentierter Einwilligung aller Anwesenden vertretbar. Self-Hosting ist nicht möglich.

### Stärken

- Kein Bot: Aufnahme ohne fremden Teilnehmer im Meeting, auch für Gespräche vor Ort.
- Einstieg: Notetaker auf dem iPhone kostenlos.
- Kontrolle: Aufnahme startet nie automatisch, Admins können eine Einwilligungsbestätigung erzwingen.
- Weiterverwendung: Synchronisation mit dem Desktop und Anbindung per MCP.

### Schwächen

- Transparenz gegenüber Teilnehmenden: Ohne Bot ist die Aufnahme für andere nicht erkennbar.
- Datenstandort: Ausschliesslich USA, Spracherkennung in der Cloud.
- Sprachen: Unterstützung für Deutsch nicht dokumentiert.
- Angaben: Widersprüche bei Free-Limits, Growth-Preis und ISO-Zertifizierung.

### Einschätzung für die Praxis

Der iPhone-Notetaker macht Protokolle von Gesprächen am Tisch so einfach wie eine Sprachnotiz, und genau darin liegt das Risiko: Ohne Bot weiss niemand im Raum, dass aufgezeichnet wird, solange es nicht gesagt wird. Für den DACH-Raum ist der Einsatz nur mit einer klaren Regel sinnvoll: Aufnahme ansagen, Einwilligung aller Anwesenden einholen und festhalten. Für vertrauliche Gespräche spricht der reine US-Standort dagegen. Ein sinnvoller Test: drei interne Besprechungen auf Hochdeutsch mit angekündigter Aufnahme protokollieren, Training in den Einstellungen deaktivieren und die Qualität der Aufgabenliste mit einem manuellen Protokoll vergleichen.

**Relevanzbewertung:** 7,1/10

---

## Quellen

- Aranguren, M. I. (2026, 16. November). Turn Gemini Notebook sources into interactive sites. Google. https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites/
- Cloudflare. (2026, 16. Oktober). Your data and Workers AI. https://developers.cloudflare.com/workers-ai/platform/data-usage/
- Cloudflare. (2026, 18. November). An updated Clairic and Clairic-flash are now open-weight, from the new Workers AI Superintelligence team. https://blog.cloudflare.com/open-clairic/
- Cloudflare. (2026, 18. November). Pricing. Cloudflare Workers AI docs. https://developers.cloudflare.com/workers-ai/platform/pricing/
- Cloudflare. (o. D.). clairic-flash. Cloudflare AI docs. https://developers.cloudflare.com/workers-ai/models/clairic-flash/
- Cloudflare. (o. D.). clairic. Cloudflare AI docs. https://developers.cloudflare.com/workers-ai/models/clairic/
- Cloudflare. (o. D.). Cloudflare/clairic. Hugging Face. https://huggingface.co/Cloudflare/clairic
- Google. (2026, 19. November). Gemini Apps Privacy Hub. https://support.google.com/gemini/answer/13594961
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Google AI Pro und Ultra: Abonnements. https://gemini.google/subscriptions/
- HeyGen Research. (2026, 17. November). HeyGen Avatar 6 technical report. https://www.heygen.com/research/avatar-6-model
- HeyGen. (2026, 15. Oktober). Privacy policy. https://www.heygen.com/privacy
- HeyGen. (2026, 5. Mai). Biometric information privacy notice. https://www.heygen.com/biometric-privacy-notice
- HeyGen. (o. D.). HeyGen Avatar 6: AI avatar model that looks like you. https://www.heygen.com/models/heygen-avatar-6
- HeyGen. (o. D.). Pricing plans for creators and marketers. https://www.heygen.com/pricing
- HeyGen. (o. D.). Security practices. https://www.heygen.com/security
- Maguire, E. (2026, 17. November). Proton launches Lumo Desktop, bringing connectivity and automation to privacy-first AI. Proton. https://proton.me/blog/lumo-desktop-features
- OpenAI. (2025, 5. Februar). Introducing data residency in Europe. https://openai.com/index/introducing-data-residency-in-europe/
- OpenAI. (2026, 17. November). GPT-6.2 Astra and Sol. https://learn.chatgpt.com/docs/whats-new/gpt-62-astra-sol.md
- OpenAI. (2026, 17. November). Introducing GPT-6.2 Astra and Sol. https://openai.com/index/introducing-gpt-6-2-astra-sol/
- OpenAI. (2026, 24. August). Europe privacy policy. https://openai.com/policies/eu-privacy-policy/
- OpenAI. (2026, 8. Januar). Enterprise privacy at OpenAI. https://openai.com/enterprise-privacy/
- Perez, S. (2026, 17. November). Proton's Lumo, a privacy-focused alternative to ChatGPT and Claude, arrives on desktop. TechCrunch. https://techcrunch.com/2026/11/17/protons-lumo-a-privacy-focused-alternative-to-chatgpt-and-claude-arrives-on-desktop/
- PricingSaaS. (2026, 19. November). Wispr Flow brought Notetaker meeting notes to iPhone. https://pricingsaas.com/news/article/wisprflow-brought-notetaker-meeting-notes-to-iphone
- Proton. (2025, 4. August). Lumo security model: How Proton makes AI private. https://proton.me/blog/lumo-security-model
- Proton. (o. D.). About Lumo, the privacy-first AI assistant. https://proton.me/lumo
- Proton. (o. D.). Lumo pricing and plans. https://proton.me/lumo/pricing
- Proton. (o. D.). Private AI for business plans and pricing. https://proton.me/business/lumo/pricing
- TestingCatalog. (2026, 17. November). OpenAI launches GPT-6.2 Astra and Sol on ChatGPT and APIs. https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis.md
- Unite.AI. (2026, 18. November). Wispr Flow brings AI meeting notes to iPhone. https://www.unite.ai/wispr-flow-notetaker-iphone-meeting-notes/
- Wispr. (2026, 18. August). Data controls. https://wisprflow.ai/data-controls
- Wispr. (2026, 18. November). Wispr Flow Notetaker now goes with you. https://wisprflow.ai/post/notetaker-on-iphone
- Wispr. (2026, 19. August). Privacy policy. https://wisprflow.ai/privacy-policy
- Wispr. (o. D.). Enterprise privacy and security. https://wisprflow.ai/enterprise-privacy
- Wispr. (o. D.). Pricing. https://wisprflow.ai/pricing
