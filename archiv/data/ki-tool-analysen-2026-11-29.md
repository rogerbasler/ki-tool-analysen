# KI-Tool-Analysen KW 48/2026

**Datum:** 29. November 2026  
**Recherchezeitraum:** 21. bis 28. November 2026

## Wochenzusammenfassung

KI-Werkzeuge erhalten diese Woche Schreibrechte in Systemen, in denen bisher Menschen das letzte Wort hatten: Sie genehmigen Codeänderungen, erzeugen Designs im Markenauftritt und stellen Personenlisten zusammen. Damit verlagert sich die Kontrolle vom einzelnen Ergebnis auf die Regel, die vorab festlegt, was ein Werkzeug darf, und auf den Ort, an dem die Daten liegen. Anthropic liest die Freigaberegeln von Claude Ship aus einer YAML-Datei im Repository, Canva kennt für angebundene Assistenten nur einen Schalter für das ganze Team, und Exa verarbeitet Websets in den USA ohne Option auf Nullspeicherung. Carry und MacWhisper gehen den umgekehrten Weg und halten Chatverläufe, Transkripte und Stimmprofile auf dem eigenen Rechner. Steuerbar bleibt ein Werkzeug dort, wo Regeln und Daten als prüfbare Dateien im eigenen Zugriff liegen.

- Gemini 4 Neon (8,3/10): Ein Modell für lange Dokumente mit einem Kontextfenster von gut einer Million Tokens, auf Google Cloud mit EU-Verarbeitung, für USD 3 und USD 15 pro Million Tokens.
- MacWhisper 16.0 (8,0/10): Transkription und Sprechererkennung laufen auf dem Mac, benannte Stimmen werden in späteren Aufnahmen wiedererkannt, ein Bot tritt keinem Meeting bei.
- Canva MCP (7,8/10): KI-Assistenten erzeugen bearbeitbare Designs direkt im Canva-Konto, die Kernfunktionen stehen auch im kostenlosen Plan bereit.
- Praxisregel: Bevor ein KI-Werkzeug etwas genehmigen, veröffentlichen oder versenden darf, die Regel dafür als Datei ablegen, zwei Wochen im Beobachtungsmodus prüfen und erst dann scharf schalten.

**Trend:** KI-Werkzeuge erhalten Schreibrechte, und die Kontrolle wandert in Regeldateien und auf den eigenen Rechner.

| Kategorie | Tool | Relevanz |
|---|---|---:|
| Text | Gemini 4 Neon | 8,3/10 |
| Design | Canva MCP | 7,8/10 |
| Data / Wissen | Carry | 7/10 |
| Recherche | Exa Websets V2 | 6,8/10 |
| Agents | Claude Ship | 7,4/10 |
| Transkription | MacWhisper 16.0 | 8/10 |

---

## 1. Gemini 4 Neon

**Kategorie:** Text  
**Relevanzbewertung:** 8,3/10  
**Website:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/  
**Aktualitätssignal:** Google hat Gemini 4 Neon am 18. November 2026 veröffentlicht, also kurz vor dem Recherchezeitraum. In dieser Woche war es das meistbesprochene Modell in den Newslettern, Google hat die Cloud-Dokumentation am 24. November aktualisiert, und ab dem 1. Dezember 2026 steigen die Preise der Schwestermodelle Carbon und Argon auf USD 4 und USD 20 pro Million Tokens.

### Kurzbeschreibung

Sprachmodell von Google für anspruchsvolle Text-, Analyse- und Dokumentenarbeit, verfügbar in der Gemini-App ab Google AI Pro, über die Gemini API und auf Google Cloud.

Neon steht in der Gemini-4-Familie zwischen Hydrogen für schnelle Alltagsaufgaben und Carbon für die schwierigsten, lang laufenden Aufgaben. Das Modell verarbeitet Text, Bilder, Audio und Video und gibt Text aus. Das Kontextfenster umfasst 1'048'576 Tokens, die sich Eingabe und Ausgabe teilen. Ein Kontextfenster ist die Menge an Material, die ein Modell in einem Durchgang berücksichtigen kann. Pro Anfrage lassen sich bis zu 3'000 Dokumente oder Bilder mit je bis zu 3'000 Seiten übergeben, neu auch Microsoft-Office- und OpenDocument-Dateien.

In der Gemini-App liest Neon hochgeladene Tabellen, PDFs und Fotos genauer aus und verdichtet umfangreiches Material zu Berichten und Zusammenfassungen. Für die API gibt es vier Denkstufen von Low bis Extra High. Sampling-Parameter wie die Temperatur sind fest eingestellt, Feintuning und die Live-API werden nicht unterstützt. Die Benchmark-Angaben stammen von Google selbst, eine unabhängige Prüfung der Auswahl liegt nicht vor. Der Wissensstand des Modells endet im März 2026.

### Nutzungsszenarien

- Geschäftsleitung: Mehrere Jahresberichte und Verträge in einer Anfrage laden und die Abweichungen zwischen den Dokumenten als Tabelle ausgeben lassen.
- Kommunikation: Aus Sitzungsunterlagen, Tabellen und Notizen einen Bericht im eigenen Aufbau erstellen.
- Recht und Compliance: Lange Regelwerke nach bestimmten Pflichten durchsuchen und die Fundstellen mit Seitenangabe prüfen.
- IT: Über das EU-Multi-Region-Angebot von Google Cloud interne Assistenten bauen, deren Verarbeitung in der EU bleibt.

### Pricing

Free Tier: In der kostenlosen Gemini-App und in Google AI Plus (USD 4.99 pro Monat) ist Neon nicht enthalten, dort steht nur Hydrogen bereit. Google AI Pro: USD 19.99 pro Monat, mit Neon. Google AI Ultra: USD 99.99 oder USD 199.99 pro Monat, mit Neon und Carbon. API: USD 3 pro Million Eingabe-Tokens, USD 0.15 für zwischengespeicherte Eingaben, USD 15 pro Million Ausgabe-Tokens einschliesslich Denk-Tokens; ein kostenloses API-Kontingent für Neon ist nicht dokumentiert. Workspace mit Gemini ab USD 14 und Gemini Enterprise ab USD 30 pro Person und Monat; ob Neon dort enthalten ist, ist nicht dokumentiert. Numerische Nutzungslimits der App sind nicht veröffentlicht, CHF-Preise nicht dokumentiert.

### Datenschutz

Serverstandort: Auf Google Cloud stehen die Standorte global, Multi-Region us und Multi-Region eu zur Wahl. Im Multi-Region eu bleiben Verarbeitung und gespeicherte Daten in der EU, der globale Endpunkt gibt keine Zusage. Die Schweiz gehört nicht zum Multi-Region eu, eine Region Zürich ist für Neon nicht gelistet. Für die Gemini-App ist der Speicherort nicht dokumentiert, Anbieter für EWR und Schweiz ist Google Ireland Limited. Training: In der Gemini-App für Privatkonten können Chats zum Training verwendet werden, solange der Verlauf aktiv ist; die Standardlöschfrist beträgt 18 Monate, von Menschen geprüfte Chats bleiben bis zu drei Jahre gespeichert. In Workspace werden Kundeninhalte nicht für das Training verwendet. Für die API ist die Regelung zu Neon nicht dokumentiert. Policies: Cloud Data Processing Addendum, auf Cloud zusätzlich kundenverwaltete Schlüssel, VPC Service Controls und Access Transparency; für Workspace unter anderem ISO/IEC 27001, 27701 und 42001 sowie SOC 2. DSGVO und DSG: Für personenbezogene oder vertrauliche Inhalte kommen Workspace oder Google Cloud mit Multi-Region eu und Auftragsverarbeitungsvertrag in Frage, die App mit Privatkonto nicht. Eine Aussage speziell zum Schweizer DSG fehlt auf den geprüften Seiten. Self-Hosting ist nicht möglich, es gibt weder offene Gewichte noch eine lokale Variante.

### Stärken

- Dokumentenarbeit: Sehr grosses Kontextfenster und direkte Verarbeitung von Office-Dateien.
- Datenhaltung: Multi-Region eu auf Google Cloud mit kundenverwalteten Schlüsseln.
- Kosten: Ab dem 1. Dezember günstiger als die Schwestermodelle Carbon und Argon.
- Verfügbarkeit: Auf Google Cloud allgemein verfügbar, in der App ab Google AI Pro.

### Schwächen

- Zugang: Nicht in der kostenlosen App und nicht in Google AI Plus.
- Transparenz: Nutzungslimits der App ohne Zahlen, Workspace-Verfügbarkeit nicht dokumentiert.
- Schweiz: Keine Schweizer Region, kein Hinweis zum DSG.
- Steuerung: Feste Sampling-Parameter, kein Feintuning, Ausgabe nur als Text.
- Belege: Leistungsangaben stammen vom Anbieter.

### Einschätzung für die Praxis

Neon eignet sich für Organisationen, die bereits mit Google Workspace oder Google Cloud arbeiten und lange Dokumente auswerten. Für vertrauliche Inhalte ist der Weg über Google Cloud mit Multi-Region eu oder über Workspace vorzuziehen, weil dort die Verarbeitung vertraglich geregelt ist. Das Abo Google AI Pro mit Privatkonto passt für öffentliche oder unkritische Inhalte. Ein sinnvoller Test: drei eigene Dokumente von je über 100 Seiten laden, zehn Fragen mit bekannter Antwort stellen und prüfen, ob Fundstellen und Zahlen stimmen. Wer über die API arbeitet, sollte die Kosten pro Aufgabe auf der Stufe High messen, da Denk-Tokens als Ausgabe verrechnet werden.

**Relevanzbewertung:** 8,3/10

---

## 2. Canva MCP

**Kategorie:** Design  
**Relevanzbewertung:** 7,8/10  
**Website:** https://www.canva.com/newsroom/news/canva-mcp-update/  
**Aktualitätssignal:** Am 24. November 2026 hat Canva den MCP-Server öffentlich als allgemein verfügbar angekündigt und um REST-APIs, Kommandozeilenwerkzeuge und Dienstkonten ergänzt. Entwickler:innen konnten sich bereits seit dem 7. Oktober 2026 ohne Warteliste anmelden.

### Kurzbeschreibung

Schnittstelle, über die KI-Assistenten wie Claude, ChatGPT, Gemini oder Copilot im Canva-Konto der Nutzer:innen bearbeitbare Designs erstellen, anpassen und exportieren.

MCP steht für Model Context Protocol, einen offenen Standard, über den KI-Assistenten Funktionen fremder Dienste aufrufen. Der Canva-Server stellt 46 solcher Funktionen bereit: Designs suchen und lesen, neue Designs und Bilder erzeugen, Hintergründe entfernen, ein flaches Bild in bearbeitbare Ebenen zerlegen, Grössen anpassen, Vorlagen mit Daten befüllen und als PDF, PNG, JPG, PPTX oder MP4 exportieren. Das Ergebnis ist ein Canva-Design mit Bearbeitungslink. Änderungen an bestehenden Designs laufen als Transaktion, die bestätigt oder verworfen wird.

Die Anmeldung erfolgt pro Person über OAuth. Der Assistent kann nur, was die angemeldete Person in Canva darf. Eine Anmeldung auf Ebene der Organisation gibt es für MCP nicht, Dienstkonten gelten nur für die REST-APIs. Pro Person sind 300 Anfragen pro Minute erlaubt, die Bildgenerierung ist auf 10 pro Minute begrenzt. Die Ankündigung nennt auch Videogenerierung; in der offiziellen Funktionsliste ist dafür nur der MP4-Export dokumentiert.

### Nutzungsszenarien

- Marketing: Im Assistenten aus einem Briefing mehrere Social-Media-Varianten anlegen und in Canva fertigstellen.
- Vertrieb: Eine Markenvorlage per Autofill mit Kundendaten befüllen und als PDF exportieren, ab Canva Pro.
- Kommunikation: Ein bestehendes Design für weitere Formate anpassen lassen, ohne die Vorlage neu zu bauen.
- Wissensarbeit: Präsentationen im Konto durchsuchen und Inhalte samt Sprechernotizen zusammenfassen lassen.

### Pricing

Free Tier: Ja, USD 0. Im kostenlosen Plan stehen über MCP Erzeugung, Bearbeitung, Suche, Export, Kommentare und Upload bereit, mit bis zu 20 KI-Nutzungen. Canva Pro: USD 144 pro Jahr für eine Person, zusätzlich Grössenanpassung, Autofill, Markenkits und Markenvorlagen. Canva Business: USD 250 pro Person und Jahr. Enterprise: Preis auf Anfrage. Für MCP selbst fällt kein eigener Preis an, KI-Funktionen zehren vom KI-Kontingent des jeweiligen Plans. Die REST-APIs werden über vorausbezahlte API-Credits abgerechnet, etwa 10 Credits pro Autofill-Seite; der Preis pro Credit ist nicht dokumentiert. Eine ältere Canva-Seite zeigt abweichende Pro-Preise. CHF-Preise wurden nicht geprüft.

### Datenschutz

Serverstandort: Canva speichert Daten standardmässig in den USA auf AWS. Die Wahl zwischen USA und EU als Speicherort gibt es nur in Enterprise und in Bildungsplänen; ob auch KI-Verarbeitung und MCP-Verkehr in der EU bleiben, ist nicht dokumentiert. Drittanbieter: Der angebundene Assistent kann Designinhalte, Sprechernotizen, Kommentare, Dateien und Markenkits im Rahmen der Rechte der angemeldeten Person lesen. Diese Inhalte fallen danach unter die Bedingungen des Assistenten-Anbieters. Canva untersagt MCP-Partnern vertraglich, mit Canva-Daten Modelle zu trainieren oder Daten nutzerübergreifend zu speichern; technisch erzwungen ist das nicht. Training durch Canva: In Business, Teams und Enterprise werden Inhalte nicht zur Verbesserung der KI verwendet. Die Standardeinstellung für Free- und Pro-Einzelkonten ist nicht dokumentiert. Policies: Data Processing Addendum mit EU-Standardvertragsklauseln und Schweizer Anpassungen, für Business und Enterprise automatisch Vertragsbestandteil; SOC 2 Type 2, ISO/IEC 27001, EU-US Data Privacy Framework. Admins können den KI-Connector nur für das ganze Team ein- oder ausschalten, einzelne Assistenten lassen sich nicht zulassen oder sperren. DSGVO und DSG: Zwei Übermittlungen sind zu regeln, jene an Canva und jene an den Anbieter des Assistenten. Für Werbematerial ist das vertretbar, für Designs mit Personendaten oder vertraulichen Inhalten nur mit geklärten Verträgen auf beiden Seiten. Self-Hosting ist nicht möglich, der Server läuft bei Canva.

### Stärken

- Ergebnis: Bearbeitbare Canva-Designs statt flacher Bilder.
- Einstieg: Kernfunktionen im kostenlosen Plan, kein eigener Preis für MCP.
- Reichweite: Canva listet 21 unterstützte Assistenten und Plattformen.
- Rechte: Anmeldung pro Person, der Assistent überschreitet deren Berechtigungen nicht.
- Dokumentation: Veröffentlichte Limits und Nutzungsrichtlinie mit Trainingsverbot für Partner.

### Schwächen

- Admin-Kontrolle: Nur ein Schalter für das ganze Team, keine Auswahl einzelner Assistenten.
- Datenstandort: Standard USA, EU-Speicherung nur in Enterprise.
- Markenfunktionen: Markenkits, Vorlagen und Autofill erst ab Pro.
- Dokumentation: Videogenerierung angekündigt, in der Funktionsliste nicht beschrieben; Datum der allgemeinen Verfügbarkeit uneinheitlich.
- Kosten der API: Preis pro Credit nicht veröffentlicht.

### Einschätzung für die Praxis

Für Teams, die Canva bereits nutzen, verkürzt der Connector den Weg vom Briefing zum ersten Entwurf, und das Ergebnis bleibt im gewohnten Werkzeug bearbeitbar. Der Nutzen entsteht vor allem mit Markenkits und Vorlagen, also ab Canva Pro. Vor der Freigabe im Team sollte feststehen, welcher Assistent angebunden wird und welche Designs im Konto liegen, denn der Assistent liest alles, was die Person sehen darf. Ein sinnvoller Test: mit einem Konto ohne vertrauliche Designs fünf wiederkehrende Formate über den Assistenten erzeugen und die Nacharbeit in Canva messen.

**Relevanzbewertung:** 7,8/10

---

## 3. Carry

**Kategorie:** Data / Wissen  
**Relevanzbewertung:** 7/10  
**Website:** https://carry.md/  
**Aktualitätssignal:** Am 25. November 2026 erschien Version 2.1.4 im Chrome Web Store, am selben Tag wurde die Datenschutzerklärung aktualisiert. Am 26. November 2026 hat The Neuron das Werkzeug unter seinen Empfehlungen aufgeführt. Bis zum 1. Dezember 2026 gilt ein Aktionspreis.

### Kurzbeschreibung

Browser-Erweiterung, die Chats, Projekte und Dateien aus ChatGPT, Claude, Gemini und Grok als Markdown-Dateien in einem lokalen Ordner sichert und durchsuchbar macht.

Carry liest die Unterhaltungen über die angemeldete Sitzung im Browser und schreibt pro Chat eine Markdown-Datei in einen frei gewählten Ordner, etwa einen Obsidian-Vault. Markdown ist ein einfaches Textformat, das sich mit jedem Editor öffnen lässt. Die Sicherung läuft etwa alle zwei Stunden, solange der Browser geöffnet ist. Ein erneutes Sichern aktualisiert dieselbe Datei, Anhänge und erzeugte Dateien werden mitgeladen. Ein API-Schlüssel oder ein Konto bei Carry ist nicht nötig.

Im Fenster der Erweiterung lassen sich alle vier Dienste gemeinsam nach Stichwort, App, Datum und Projekt durchsuchen. Die Funktion Continue in öffnet einen gesicherten Chat in einem der anderen Dienste und hängt den Verlauf an; der Inhalt geht damit an diesen Anbieter. Unterstützt werden Chrome, Edge und weitere Chromium-Browser auf dem Desktop. Firefox, Safari und Mobilgeräte fehlen, ebenso Arbeitsbereiche von ChatGPT Business und Enterprise. Wer hinter Carry steht, ist auf den offiziellen Seiten nicht dokumentiert.

### Nutzungsszenarien

- Wissenssicherung: Recherchen und Entwürfe aus mehreren KI-Diensten in einem Ordner ablegen, der auch nach einer Kündigung bestehen bleibt.
- Suche: Eine frühere Antwort finden, ohne zu wissen, in welchem Dienst sie entstanden ist.
- Anbieterwechsel: Einen laufenden Arbeitsstand mit dem bisherigen Verlauf in einem anderen Dienst fortsetzen.
- Nachvollziehbarkeit: Als Einzelperson festhalten, welche Eingaben zu welchem Ergebnis geführt haben.

### Pricing

Free Tier: Nein. Kostenloser Test: 14 Tage ohne Kreditkarte, mit den neuesten 25 Chats pro Dienst und neuen Chats; danach endet die Sicherung, bereits gespeicherte Dateien bleiben. Lizenz auf Lebenszeit: regulär USD 79, einmalig, für bis zu fünf eigene Browser, Updates inbegriffen. Vom 15. November bis 1. Dezember 2026 USD 59 mit Aktionscode, zuzüglich Steuern. Teams mit einer Zahlung: USD 59 pro Person bei 3 bis 4 Personen, USD 54 bei 5 bis 9, USD 50 ab 10. Volle Rückerstattung innerhalb von 14 Tagen. CHF-Preise sind nicht dokumentiert.

### Datenschutz

Serverstandort: Für die Inhalte entfällt die Frage, Chats und Dateien bleiben lokal im gewählten Ordner und werden nicht auf Server von Carry geladen. Nach aussen gehen eine signierte Kompatibilitätsdatei von carry.md, die Lizenzprüfung über den Zahlungsanbieter Polar und Nutzungszähler. Die Zähler sind standardmässig aktiv und abschaltbar; sie enthalten Ereignisnamen, Dienst, Anzahl, Version, Betriebssystem, Browser, Sprache und eine zufällige Installationskennung, aber keine Inhalte, Titel oder Dateinamen. Die Serverregion dafür ist nicht dokumentiert. Policies: Datenschutzerklärung vom 25. November 2026 mit einer Liste aller Netzwerkzugriffe, Nutzungsbedingungen vom 15. November 2026. Nicht dokumentiert sind Rechtsträger, Sitz, Auftragsverarbeitungsvertrag, Zertifizierungen und ein Abschnitt zu Betroffenenrechten. DSGVO und DSG: Für die Chatinhalte entsteht kein Auftragsverarbeiter und keine Übermittlung ins Ausland durch Carry. Die exportierten Dateien liegen danach in der Verantwortung des Unternehmens, mit eigenen Regeln für Zugriff, Aufbewahrung und Löschung. Ob das automatische Auslesen mit den Nutzungsbedingungen der KI-Anbieter vereinbar ist, lässt Carry offen. Self-Hosting: nicht anwendbar, das Werkzeug arbeitet vollständig lokal im Browser.

### Stärken

- Datenhaltung: Inhalte bleiben als offene Markdown-Dateien auf dem eigenen Rechner, auch nach der Deinstallation.
- Überblick: Eine Suche über vier KI-Dienste.
- Preis: Einmalzahlung, Test ohne Kreditkarte.
- Transparenz: Jeder Netzwerkzugriff ist in der Datenschutzerklärung aufgeführt.
- Berechtigungen: Kein Zugriff auf alle Websites, Cookies oder Verlauf.

### Schwächen

- Anbieter: Rechtsträger und Sitz nicht dokumentiert, 152 Nutzer:innen im Chrome Web Store.
- Abdeckung: ChatGPT Business und Enterprise nicht unterstützt, nur Chromium-Browser auf dem Desktop.
- Abhängigkeit: Die Anbieter können ihre Oberflächen ändern, eine Unterstützung ist nicht zugesichert.
- Teams: Kein gemeinsames Archiv, keine Admin-Sicht.
- Betrieb: Sicherung nur bei geöffnetem Browser.

### Einschätzung für die Praxis

Carry löst ein konkretes Problem von Einzelpersonen und kleinen Teams: Arbeitswissen liegt verstreut in den Verläufen mehrerer KI-Dienste und ist dort an ein Abo gebunden. Die lokale Ablage ist aus Sicht des Datenschutzes günstig, verlagert aber die Pflichten für Zugriff und Löschung auf den eigenen Ordner. Gegen einen breiten Einsatz im Unternehmen sprechen der nicht dokumentierte Anbieter und die fehlende Unterstützung für ChatGPT Business und Enterprise. Ein sinnvoller Test: 14 Tage mit einem Konto ohne Kundendaten nutzen, die Nutzungszähler abschalten und prüfen, ob die Dateien im eigenen Ablagesystem auffindbar sind.

**Relevanzbewertung:** 7/10

---

## 4. Exa Websets V2

**Kategorie:** Recherche  
**Relevanzbewertung:** 6,8/10  
**Website:** https://exa.ai/websets  
**Aktualitätssignal:** Exa hat Websets V2 am 17. November 2026 im eigenen Blog angekündigt und am 21. November 2026 auf Product Hunt vorgestellt. Neu sind eine nutzungsbasierte Abrechnung ohne Abo und der API-Zugang für alle.

### Kurzbeschreibung

Recherchewerkzeug, das aus einer Beschreibung in Alltagssprache geprüfte Listen von Unternehmen, Personen, Produkten oder Fachartikeln aus dem offenen Web erstellt.

Ein Webset beginnt mit einer Beschreibung der gesuchten Liste. Das System schlägt daraus bis zu fünf Kriterien und eine Kategorie vor, die bestätigt werden. Danach prüft ein KI-Agent jeden Kandidaten gegen jedes Kriterium und zeigt pro Zeile, welche Kriterien erfüllt sind, mit Begründung und Quellen. Zusätzliche Spalten, sogenannte Enrichments, werden als Frage formuliert, etwa nach Umsatz, Ansprechperson, E-Mail oder Telefonnummer.

Ergebnisse lassen sich als CSV exportieren, per Link teilen oder an Salesforce, HubSpot, Clay und mehrere Versandwerkzeuge übergeben. Monitore wiederholen eine Suche höchstens einmal täglich. Die gewünschte Trefferzahl ist ein Zielwert, bei strengen Kriterien fallen die Listen kürzer aus. Die Angaben zu Tempo, Kosten und Genauigkeit von V2 stammen aus eigenen Tests von Exa mit je 20 Abfragen, eine unabhängige Messung liegt nicht vor. Die Dokumentation beschreibt an mehreren Stellen noch den Stand vor V2.

### Nutzungsszenarien

- Marktanalyse: Alle Anbieter einer Nische in einer Region mit Gründungsjahr und Finanzierung auflisten.
- Einkauf: Hersteller mit bestimmten Zertifikaten finden und die Belege pro Zeile prüfen.
- Vertrieb: Zielunternehmen nach überprüfbaren Kriterien zusammenstellen und an das CRM übergeben.
- Beobachtung: Mit einem Monitor täglich neue Treffer zu einem Thema erhalten.

### Pricing

Free Tier: Ja. Der Plan Starter gibt bei der Anmeldung USD 10 Guthaben ohne Zahlungsmittel, das jeden Monat auf USD 10 zurückgesetzt wird, dazu einmalig USD 10 Bonus. Dass dieses Guthaben auch für Websets gilt, ist nicht ausdrücklich bestätigt. Websets: USD 0.10 pro Agent Compute Unit plus USD 5 pro 1'000 Suchen; die Produktseite nennt USD 0.01 bis über USD 1 pro Anfrage. Was eine Compute Unit leistet, ist nicht veröffentlicht. Enrichments: USD 0.02 pro E-Mail, USD 0.07 pro Telefonnummer. Developer: Guthaben im Voraus, ohne Abo und Mindestumsatz. Growth: Jahresvertrag mit Auftragsverarbeitungsvertrag, Preis nicht erfasst. Enterprise: Preis auf Anfrage. Abgerechnet wird der Rechenaufwand, nicht der Treffer; sehr schwierige Suchen können pro Treffer teurer sein als zuvor.

### Datenschutz

Serverstandort: USA. Die seit dem 13. November 2026 angebotene EU-Datenhaltung in Stockholm gilt nur für die Endpunkte Search und Contents, noch nicht für Websets. Aufbewahrung: Eine Frist für Abfragen ist nicht dokumentiert, die Option Zero Data Retention steht für Websets nicht zur Verfügung. Training: Abfragedaten werden standardmässig zum Training und zur Verbesserung der Modelle verwendet. Policies: SOC 2 Type II, HIPAA nur in Enterprise; ein Auftragsverarbeitungsvertrag ist ab dem Plan Growth aufgeführt, ob Starter und Developer einen erhalten, ist nicht dokumentiert. Die Datenschutzerklärung vom 29. Juni 2026 enthält keine Abschnitte zur DSGVO oder zur Schweiz, keine Rechtsgrundlagen und kein Verfahren, mit dem Personen ihre Einträge entfernen lassen können. DSGVO und DSG: Wer mit Websets Personenlisten erstellt, ist für diese Listen selbst verantwortlich. Öffentlich zugängliche Daten bleiben Personendaten. Nötig sind eine Rechtsgrundlage, die Information der Betroffenen und ein Umgang mit Widersprüchen; für Werbemails gelten zusätzlich die nationalen Regeln gegen unlauteren Wettbewerb. Listen von Unternehmen ohne Personenangaben sind deutlich weniger heikel. Self-Hosting ist nicht dokumentiert und wird nicht angeboten.

### Stärken

- Nachvollziehbarkeit: Jede Zeile zeigt, welche Kriterien erfüllt sind, mit Begründung und Quellen.
- Einstieg: Kein Abo, monatliches Gratisguthaben, API ohne bezahlten Plan.
- Weiterverarbeitung: CSV, Webhooks, MCP und direkte Anbindung an CRM-Systeme.
- Aktualität: Monitore für wiederkehrende Suchen.

### Schwächen

- Datenschutz: Verarbeitung in den USA, Training mit Abfragedaten als Standard, keine Nullspeicherung für Websets.
- Personendaten: Keine Regelung für Betroffene im EWR und in der Schweiz.
- Kosten: Pro Treffer nicht vorhersehbar, Recheneinheit nicht definiert.
- Belege: Genauigkeit nur vom Anbieter gemessen, Listen sind nicht vollständig.
- Dokumentation: FAQ widerspricht den neuen Preisen.

### Einschätzung für die Praxis

Websets V2 ist ein brauchbares Werkzeug für Markt-, Anbieter- und Wettbewerbsrecherchen, bei denen es um Unternehmen geht und jede Zeile gegen ihre Quelle geprüft werden kann. Für Personenlisten mit E-Mail und Telefonnummer ist im DACH-Raum Zurückhaltung angebracht: Die Verantwortung liegt bei der Organisation, die die Liste erstellt, und der Anbieter bietet dafür keine Unterstützung. Suchbegriffe sollten keine vertraulichen Angaben enthalten, weil Abfragen ins Training einfliessen. Ein sinnvoller Test: mit dem Gratisguthaben eine Unternehmensliste erstellen, deren Umfang bekannt ist, und Vollständigkeit, Fehlerquote und Kosten pro Treffer festhalten.

**Relevanzbewertung:** 6,8/10

---

## 5. Claude Ship

**Kategorie:** Agents  
**Relevanzbewertung:** 7,4/10  
**Website:** https://claude.com/product/claude-ship  
**Aktualitätssignal:** Am 23. November 2026 hat Anthropic Claude Ship vorgestellt: drei Agenten, die Pull Requests auf GitHub prüfen, nachbessern und nach einer Richtliniendatei genehmigen. Code Review ist allgemein verfügbar, PR Steward und Claude Approvals sind in öffentlicher Beta.

### Kurzbeschreibung

Agenten von Anthropic für Softwareteams auf den Plänen Claude Team und Enterprise, die Codeänderungen auf GitHub prüfen, Fehler in der Pipeline beheben und Routineänderungen nach festgelegten Regeln freigeben.

Ein Pull Request ist ein Änderungsvorschlag am Code, der vor der Übernahme geprüft wird. Code Review lässt mehrere Agenten die Änderung parallel lesen, filtert Fehlalarme in einem Prüfschritt und schreibt Befunde als Kommentare. Der Zugriff ist dabei nur lesend, genehmigt oder blockiert wird nichts. PR Steward arbeitet in einer Cloud-Sitzung an fehlgeschlagenen Tests, Merge-Konflikten und Review-Kommentaren und schreibt nach jedem Push, was geändert wurde und wie es sich rückgängig machen lässt.

Claude Approvals liest die Datei .claude/approvals.yml aus dem Hauptzweig des Repositorys. Jede Regel legt für bestimmte Pfade fest, ob Claude genehmigt, kommentiert oder blockiert und wie viele Personen zusätzlich zustimmen müssen. Ein Beobachtungsmodus zeigt die Entscheide an, ohne sie durchzusetzen. Die Dokumentation benennt selbst Wege, auf denen eine Änderung ohne zweite Person übernommen wird: Die Autorin oder der Autor kann den verlangten Platz selbst besetzen, null verlangte Personen sind zulässig, und eine Genehmigung löst nicht von sich aus ein Code Review aus. Ein eigenes Audit-Log für die Entscheide ist nicht dokumentiert. Unterstützt wird nur GitHub.

### Nutzungsszenarien

- Softwareentwicklung: Jede Änderung vor der menschlichen Prüfung auf Fehler durchsehen lassen.
- Routineänderungen: Aktualisierungen von Abhängigkeiten oder Dokumentation nach einer Regel freigeben, sicherheitsrelevante Pfade weiterhin durch zwei Personen.
- Governance: Im Beobachtungsmodus messen, wie oft die Regeln zum selben Urteil kommen wie das Team.
- Betrieb: Fehlgeschlagene Tests und Merge-Konflikte vom Agenten beheben lassen, mit Kostenobergrenze pro Pull Request.

### Pricing

Free Tier: Nein, Claude Ship ist in Free, Pro und Max nicht enthalten. Claude Team Standard: USD 20 pro Person und Monat bei Jahreszahlung, USD 25 monatlich. Team Premium: USD 100 bei Jahreszahlung, USD 125 monatlich. Enterprise: USD 20 pro Person und Monat bei Jahresabrechnung, mindestens 20 Plätze, Nutzung zusätzlich zu API-Preisen. Claude Ship wird nach Tokens über Nutzungsguthaben abgerechnet, getrennt vom Kontingent des Plans; ein Preis pro Review ist nicht veröffentlicht. Auch der Beobachtungsmodus kostet. Neue Repositorys prüfen standardmässig nach jedem Push, PR Steward hat ohne gesetzte Grenze kein Ausgabenlimit. Enterprise-Organisationen können bis 15. Januar 2027 einmalig Guthaben von USD 10'000 bis USD 50'000 beziehen, gültig 30 Tage.

### Datenschutz

Serverstandort: Code Review läuft auf Infrastruktur von Anthropic, PR Steward klont das Repository in eine von Anthropic verwaltete virtuelle Maschine. Daten werden in den USA gespeichert, die Verarbeitung kann über die USA, Europa, Asien und Australien laufen. Eine EU-Datenhaltung ist für Claude Ship und für die Pläne Team und Enterprise nicht dokumentiert. Über Amazon Bedrock oder Google Vertex ist Claude Ship nicht verfügbar. Training: Unter den kommerziellen Bedingungen trainiert Anthropic nicht mit Kundencode, sofern die Organisation nicht zustimmt. Aufbewahrung: 30 Tage als Standard; für Organisationen mit Zero Data Retention, HIPAA-Konfiguration oder eigenen Schlüsseln steht Claude Ship nicht zur Verfügung. Policies: Auftragsverarbeitungsvertrag als Teil der kommerziellen Bedingungen, SOC 2 Type II, ISO 27001, ISO/IEC 42001. DSGVO und DSG: Quellcode, Commit-Daten und Kommentare mit Namen der Beteiligten werden in den USA verarbeitet, nötig sind der Auftragsverarbeitungsvertrag und eine Grundlage für die Übermittlung. Ein Hinweis zum Schweizer DSG fehlt auf den geprüften Seiten. Self-Hosting: Für Code Review nein. PR Steward kann auf einem eigenen Runner laufen, die Modellanfragen gehen auch dann an Anthropic.

### Stärken

- Einführung: Drei Agenten, einzeln und pro Repository zuschaltbar, mit Beobachtungsmodus.
- Regeln: Richtlinie als versionierte Datei im Repository, aus dem Hauptzweig gelesen.
- Trennung: Code Review nur lesend, PR Steward kann in gehosteten Sitzungen nicht genehmigen.
- Kostenkontrolle: Monatliche Limits und Obergrenze pro Pull Request einstellbar.
- Daten: Kein Training mit Kundencode unter kommerziellen Bedingungen.

### Schwächen

- Freigaben: Mehrere dokumentierte Wege zu einer Übernahme ohne unabhängige menschliche Prüfung.
- Reife: Zwei von drei Agenten in Beta, die Sperren gegen Merge und Force-Push sind umgehbar.
- Kosten: Abrechnung nach Tokens ohne Richtpreis, teure Standardeinstellungen.
- Datenstandort: Keine EU-Datenhaltung, keine Nullspeicherung.
- Plattform: Nur GitHub, kein dediziertes Audit-Log.

### Einschätzung für die Praxis

Für Unternehmen mit eigenen Entwicklungsteams auf GitHub ist Code Review der risikoarme Einstieg, weil der Agent nur liest und kommentiert. Die Genehmigung durch den Agenten berührt dagegen das Vier-Augen-Prinzip und gehört in die Hand der Geschäfts- oder IT-Leitung, nicht in eine Einstellung nebenbei. Die Schutzregeln für Zweige in GitHub bleiben die eigentliche Sperre und sollten vor dem Start geprüft sein. Ein sinnvoller Test: ein unkritisches Repository wählen, ein Ausgabenlimit setzen, Approvals zwei Wochen im Beobachtungsmodus laufen lassen und jede Abweichung vom Urteil des Teams auswerten.

**Relevanzbewertung:** 7,4/10

---

## 6. MacWhisper 16.0

**Kategorie:** Transkription  
**Relevanzbewertung:** 8/10  
**Website:** https://www.macwhisper.com/  
**Aktualitätssignal:** Version 16.0 wurde am 26. November 2026 erstmals erfasst, Version 16.0.1 am 27. November 2026; die offiziellen Release Notes tragen kein Datum. Neu ist eine Stimmerkennung auf dem Gerät: Einmal benannte Sprecher:innen werden in späteren Transkripten und Live-Meetings wiedererkannt.

### Kurzbeschreibung

Mac-App, die Audio- und Videodateien transkribiert, Online-Meetings ohne Bot aufzeichnet und systemweites Diktat bietet, mit Spracherkennung auf dem eigenen Gerät.

MacWhisper verarbeitet Aufnahmen standardmässig lokal mit Whisper, Parakeet und weiteren Modellen. Meetings aus Zoom, Teams, Webex, Slack und aus dem Browser werden auf dem Mac mitgeschnitten, FaceTime ist ausgenommen. Zusammenfassungen und Fragen an ein Transkript laufen über eigene API-Schlüssel bei einem KI-Anbieter oder lokal über Ollama und LM Studio. Die Website nennt über 100 Sprachen, darunter Deutsch. Schweizerdeutsch ist nicht dokumentiert.

Mit Version 16.0 merkt sich die App Stimmen. Wird eine Person einmal benannt, ordnet MacWhisper ihr spätere Aufnahmen zu und markiert die Treffer zur Bestätigung oder Korrektur. In Live-Meetings erscheinen die Namen nach dem Ende des Gesprächs. In den Einstellungen lässt sich die Funktion abschalten und die Stimme einer Person löschen. Voraussetzung sind ein Mac mit Apple-Chip und die lokale Transkription mit Sprechererkennung. Die Neuerung gilt für die Direktversion von der Website, die App-Store-Ausgabe steht noch bei Version 15.7.1.

### Nutzungsszenarien

- Geschäftsleitung: Vertrauliche Sitzungen protokollieren, ohne dass Audio das Gerät verlässt.
- Beratung und Recht: Mandantengespräche transkribieren und wiederkehrende Beteiligte automatisch zuordnen lassen.
- Kommunikation: Interviews und Podcasts in Text umwandeln und als Untertitel exportieren.
- IT: Über MDM Cloud-Transkription und externe KI-Dienste für alle Geräte sperren.

### Pricing

Free Tier: Ja, EUR 0, ohne zeitliche Begrenzung; die genauen Grenzen der Gratisversion sind nicht klar dokumentiert. Pro: EUR 64 pro Lizenz als Einmalzahlung mit Updates auf Lebenszeit, so in Euro publiziert; Preise in USD oder CHF sind nicht veröffentlicht. Zum Black Friday 2026 gibt es 25 % Rabatt, derselbe Rabatt gilt dauerhaft auf Anfrage für Journalist:innen, Studierende und gemeinnützige Organisationen. Volumenpakete mit 5, 10, 20 oder 50 Lizenzen, Preise nicht dokumentiert. Rückgabe innerhalb von sieben Tagen. Die Stimmerkennung setzt nach Presseberichten eine Pro-Lizenz voraus.

### Datenschutz

Audio gespeichert: Ja, lokal auf dem Mac im Ordner der Anwendung. Eine automatische Löschung oder eine Aufbewahrungsfrist ist nicht dokumentiert, entfernt wird von Hand. Wo die Stimmprofile liegen, steht nicht in der offiziellen Dokumentation; Presseberichte nennen das Gerät. Sichtbarer Bot: Nein, es tritt kein Bot bei. Andere Teilnehmende erhalten keinen Hinweis, eine Einwilligungsfunktion ist nicht dokumentiert; die Einwilligung aller Beteiligten müssen die Nutzer:innen selbst einholen. Spracherkennung: standardmässig auf dem Gerät, einschliesslich Sprechererkennung. Daten verlassen den Mac nur bei zugeschalteten Funktionen: Cloud-Transkription über OpenAI, Groq, ElevenLabs oder Deepgram, Übersetzung mit DeepL, Zusammenfassungen über externe KI-Anbieter. Serverstandort: Bei lokaler Nutzung entfällt er, für die optionalen Dienste gilt der Standort des gewählten Anbieters. Anbieter ist Good Snooze von Jordi Bruin in Amsterdam. Policies: Die Datenschutzerklärung vom 14. Februar 2024 ist knapp, nennt weder Verantwortlichen noch Fristen und erwähnt die Cloud-Optionen nicht; Auftragsverarbeitungsvertrag und Zertifizierungen sind nicht dokumentiert. Per MDM lassen sich Cloud-Transkription, externe KI-Dienste, Übersetzung, Integrationen und Analysedaten abschalten. DSGVO und DSG: Bei rein lokaler Nutzung entsteht keine Auftragsverarbeitung und keine Übermittlung ins Ausland. Stimmprofile können als biometrische Daten gelten und brauchen dann eine ausdrückliche Einwilligung der betroffenen Personen. Self-Hosting: nicht anwendbar, die App läuft vollständig lokal und offline.

### Stärken

- Lokale Verarbeitung: Transkription, Sprecher- und Stimmerkennung auf dem Gerät, auch offline.
- Kein Bot: Aufnahme ohne zusätzlichen Teilnehmer im Meeting.
- Preis: Einmalzahlung und dauerhafte Gratisversion.
- Verwaltung: MDM-Schlüssel zum Sperren aller Cloud-Funktionen.
- Kontrolle: Stimmerkennung abschaltbar, einzelne Stimmen löschbar.

### Schwächen

- Plattform: Nur Mac, Stimmerkennung nur mit Apple-Chip.
- Einwilligung: Kein Hinweis an Teilnehmende, keine Einwilligungsfunktion.
- Rechtliche Unterlagen: Datenschutzerklärung von 2024, kein Auftragsverarbeitungsvertrag, keine Zertifizierung.
- Dokumentation: Release Notes ohne Datum, einzelne Hilfeartikel veraltet.
- Ausgaben: App-Store-Version ohne Diktat, Meeting-Erkennung und MDM.

### Einschätzung für die Praxis

MacWhisper passt für Personen und Teams auf dem Mac, die Gespräche protokollieren wollen, ohne Audio an einen Cloud-Dienst zu geben. Die Stimmerkennung spart Zuordnungsarbeit bei wiederkehrenden Runden, legt aber Stimmprofile an. Dafür braucht es die Einwilligung der betroffenen Personen und eine Regel, wann Profile gelöscht werden. Weil kein Bot sichtbar ist, muss die Aufnahme angesagt werden. Ein sinnvoller Test: drei interne Sitzungen auf Hochdeutsch und in Mundart mit angekündigter Aufnahme transkribieren, Cloud-Funktionen abgeschaltet lassen und Fehlerquote sowie Sprecherzuordnung prüfen.

**Relevanzbewertung:** 8/10

---

## Quellen

- 9to5Google. (2026, 18. November). Gemini 4 Neon announcement. https://9to5google.com/2026/11/18/gemini-4-neon-announcement/
- AlphaSignal. (2026, 18. November). Exa's Websets V2 runs 4x faster at half the cost for web research. https://alphasignal.ai/news/exa-s-websets-v2-runs-4x-faster-at-half-the-cost-for-web-research
- Anthropic. (2026, 23. November). Free Code Review promotional credits for Claude Enterprise. https://support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise
- Anthropic. (2026, 23. November). Introducing Claude Ship. https://claude.com/resources/articles/introducing-claude-ship
- Anthropic. (o. D.). Claude Approvals policy file reference. Claude Code Docs. https://code.claude.com/docs/en/approvals-policy
- Anthropic. (o. D.). Claude Ship. Claude Code Docs. https://code.claude.com/docs/en/claude-ship
- Anthropic. (o. D.). Data usage. Claude Code Docs. https://code.claude.com/docs/en/data-usage
- Anthropic. (o. D.). Pricing. https://claude.com/pricing
- Anthropic. (o. D.). What PR Steward can access. Claude Code Docs. https://code.claude.com/docs/en/pr-steward-security
- Canva Developers. (2026, 27. Oktober). How to use Canva MCP in your AI application. https://www.canva.dev/blog/developers/canva-mcp-ga/
- Canva Developers. (o. D.). Canva MCP usage policy. https://www.canva.dev/docs/mcp/usage-policy/
- Canva Developers. (o. D.). MCP tools and rate limits. https://www.canva.dev/docs/mcp/tools/
- Canva. (2025, 30. Oktober). Data Processing Addendum. https://www.canva.com/policies/data-processing-addendum/
- Canva. (2026, 24. November). Building the design layer of the internet: opening Canva to every agent and developer. https://www.canva.com/newsroom/news/canva-mcp-update/
- Canva. (o. D.). Connect AI assistants and tools to Canva. https://www.canva.com/help/ai-connectors-canva/
- Canva. (o. D.). Trust Center: Privacy. https://www.canva.com/trust/privacy/
- Carry. (2026, 15. November). Terms. https://carry.md/terms/
- Carry. (2026, 25. November). Privacy policy. https://carry.md/privacy/
- Carry. (o. D.). Carry for teams. https://carry.md/teams/
- Carry. (o. D.). Carry: save ChatGPT, Claude, Gemini and Grok chats as Markdown. https://carry.md/
- Carry. (o. D.). FAQ. https://carry.md/faq/
- Dataconomy. (2026, 25. November). Canva opens design tools to AI agents and developers. https://dataconomy.com/2026/11/25/canva-opens-design-tools-to-ai-agents-and-developers/
- Exa. (2026, 13. November). Exa Search, now in the EU. https://exa.ai/blog/eu-data-residency
- Exa. (2026, 17. November). Websets V2. https://exa.ai/blog/websets-v2
- Exa. (2026, 29. Juni). Exa privacy policy. https://exa.ai/privacy-policy
- Exa. (o. D.). Exa API pricing. https://exa.ai/pricing
- Exa. (o. D.). Exa Websets. https://exa.ai/websets
- Exa. (o. D.). Trust Center. https://trust.exa.ai
- Exa. (o. D.). Zero Data Retention. https://exa.ai/docs/admin/security/zero-data-retention
- Good Snooze. (2024, 14. Februar). Privacy policy. https://www.macwhisper.com/legal/privacy-policy
- Good Snooze. (2025, 27. Juli). Keeping transcriptions private. https://docs.macwhisper.com/article/52-keeping-transcriptions-private
- Good Snooze. (2026, 27. November). Deploying MacWhisper with MDM. https://docs.macwhisper.com/article/27-deploying-macwhisper-with-mdm
- Good Snooze. (2026, 29. September). Local files and data locations. https://docs.macwhisper.com/article/54-file-locations
- Good Snooze. (o. D.). MacWhisper release notes. https://macwhisper-site.vercel.app/release_notes.html
- Good Snooze. (o. D.). MacWhisper. https://www.macwhisper.com/
- Google Chrome Web Store. (2026, 25. November). Carry: AI chat exporter for ChatGPT, Claude, Gemini & Grok to Obsidian. https://chromewebstore.google.com/detail/carry-%E2%80%94-save-chatgpt-clau/mlligjaffhiphbpkjejefoibcclbdfll
- Google Cloud. (2026, 24. November). Gemini 4 Neon. https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-neon
- Google Cloud. (2026, 24. November). Where your data lives and is processed. https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency
- Google DeepMind. (2026, 18. November). Gemini 4 Neon model card. https://deepmind.google/models/model-cards/gemini-4-neon/
- Google. (2026, 17. November). Gemini Apps Privacy Hub. https://support.google.com/gemini/answer/13594961
- Google. (2026, 18. November). Introducing Gemini 4 Neon. https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
- Google. (2026, 6. Oktober). Generative AI in Google Workspace Privacy Hub. https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub
- Google. (o. D.). Google AI Pro & Ultra. https://gemini.google/subscriptions/
- Mendes, M. (2026, 27. November). MacWhisper now remembers speakers' voices across recordings. 9to5Mac. https://9to5mac.com/2026/11/27/macwhisper-now-remembers-speakers-voices-across-recordings/
- Perez, S. (2026, 23. November). Anthropic launches Claude Ship, letting AI agents review, fix and approve code changes. TechCrunch. https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
- Product Hunt. (2026, 21. November). Exa Websets V2. https://www.producthunt.com/products/exa-ai
- Releasebot. (2026, 27. November). MacWhisper release notes. https://releasebot.io/updates/macwhisper
- The Neuron. (2026, 26. November). Amodei says AI shouldn't govern us. https://www.theneuron.ai/newsletter/november-26-thursday/
