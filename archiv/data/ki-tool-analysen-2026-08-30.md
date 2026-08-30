# Wöchentliche KI-Tool-Analysen

## KW 35/2026 · 30. August 2026

> **Leitthese:** Diese Woche dreht sich nicht um das nächste Modell mit mehr Parametern, sondern um die Qualität des Arbeitskontexts. Speicher wird editierbar, Bildbearbeitung nachvollziehbarer, Dokumentenwissen lokal ausführbar, Behauptungen prüfbar und Agenten-Workspaces persistenter. Das ist weniger spektakulär als ein Benchmark-Rekord, aber sehr viel näher an echter Arbeit.

## Wochenzusammenfassung

Die Sondierung umfasste AI Breakfast, There's An AI For That, FutureTools.io, Ben's Bites, Futurepedia.io, Product Hunt, Toolify.ai, TopAI.tools, The AI Citizen sowie die Tool-Erwähnungen von AI-Weekly, The Batch, The Sequence und AI Tidbits. Aus der Shortlist wurden fünf Kandidaten ausgewählt, deren Aktualität im Zeitraum vom 23. bis 30. August 2026 durch eine offizielle Ankündigung oder einen unabhängigen Launch-Beleg nachvollziehbar ist.

Der gemeinsame Nenner: KI wird dann nützlich, wenn Nutzerinnen und Nutzer die relevanten Informationen, Rechte und Arbeitsschritte steuern können. Claude macht Kontext über Chat und Cowork bearbeitbar. Midjourney erweitert die Bildbearbeitung um konkrete Eingriffe. PageIndex verlagert die Wissensschicht auf den eigenen Rechner. Lenz macht Behauptungen auditierbar. Construct versucht, Agentenarbeit als dauerhaften, einsehbaren Arbeitsbereich aufzubauen.

Was oft unterschätzt wird: Mehr Autonomie ohne bessere Kontrollpunkte skaliert vor allem Fehler. Die stärksten Signale dieser Woche liegen daher bei Funktionen für Sichtbarkeit, Quellenbezug, Speicherort und Wiederaufnahme von Arbeit. Wer diese Tools pilotiert, sollte nicht bei der Demo stehen bleiben, sondern Datenfluss, Rollen, Freigaben und Exportmöglichkeiten vorab festlegen.

| Kategorie | Tool | Anlass im Berichtszeitraum | Relevanz |
|---|---|---|---:|
| Text | Claude mit Memory | Shared Memory in Chat und Cowork, 25. August | 8,5/10 |
| Design | Midjourney V8.2 Edit Model | Öffentlicher Test des Edit-Modells, 27. August | 8,5/10 |
| Data / Wissen | PageIndex SDK Local | Lokaler reasoning-basierter RAG-Workflow, 27. August | 8,5/10 |
| Recherche | Lenz | Product-Hunt-Launch, 27. August | 8,0/10 |
| Agents | Construct Computer | Product-Hunt-Launchwoche | 8,0/10 |

---

## 1. Claude mit Memory

**Kategorie:** Text  
**Relevanzbewertung:** **8,5/10**

### Kurzbeschreibung

Anthropic hat am 25. August die Memory-Funktion von Claude über Chat und Cowork hinweg zusammengeführt. Claude kann damit Arbeitskontext zwischen diesen Oberflächen behalten. Entscheidend ist nicht das Erinnern allein, sondern die Kontrollschicht: Gespeicherte Themen sind unter "Settings > Memory" sichtbar, editierbar und löschbar. Themen wie Gesundheit oder Überzeugungen werden nur einbezogen, wenn Nutzende dies aktiv erlauben. Memory ist für Free, Pro und Max standardmässig aktiviert, für Team und Enterprise standardmässig deaktiviert. [1]

Zielgruppe sind Wissensarbeiter:innen, Einzelunternehmer:innen und Teams, die wiederkehrende Schreib-, Analyse- oder Projektarbeit nicht bei jedem Gespräch neu einordnen wollen. Das eigentliche Problem ist nicht fehlender Modellkontext, sondern der Verlust von Arbeitslogik zwischen einzelnen Sitzungen. Genau dort setzt die Funktion an.

### Nutzungsszenarien

| Szenario | Konkreter Einsatz | Praktischer Nutzen |
|---|---|---|
| Projektbriefings | Wiederkehrende Zielgruppen, Sprachregeln und Entscheide als überprüfbarer Kontext | Weniger Wiederholung, konsistentere Entwürfe |
| Redaktion | Themencluster, Quellenstandards und Formatvorgaben über Recherche- und Schreibschritte hinweg nutzen | Schnellere Vorbereitung ohne blindes Kopieren alter Chats |
| Beratung | Vorläufige Hypothesen und offene Punkte pro Mandat in einem kontrollierten Themenbereich halten | Bessere Anschlussfähigkeit zwischen Arbeitsblöcken |
| Persönliche Wissensarbeit | Lernziele, Begriffserklärungen und bevorzugte Darstellungsformen merken lassen | Relevantere Erklärungen bei wiederkehrenden Fragen |

### Pricing

Die persönliche Nutzung beginnt mit **Free für 0 USD**. Pro kostet **17 USD pro Monat bei jährlicher Zahlung** oder **20 USD monatlich**. Max beginnt bei **100 USD monatlich**. Für Teams gelten Standard-Sitze zu **20 USD jährlich abgerechnet pro Person und Monat** oder **25 USD monatlich**; Premium-Sitze kosten **100 bzw. 125 USD**. Enterprise wird mit **20 USD pro Sitz zuzüglich nutzungsabhängiger API-Kosten** ausgewiesen. Die Preise verstehen sich ohne anwendbare Steuern; Nutzungsgrenzen gelten auch in Bezahlplänen. [2]

| Tarif | Öffentlicher Preis | Einordnung |
|---|---:|---|
| Free | 0 USD | Einstieg, Memory verfügbar |
| Pro | 17 USD jährlich oder 20 USD monatlich | Individuelle, regelmässige Nutzung |
| Max | ab 100 USD monatlich | Hohe persönliche Nutzung |
| Team Standard | 20 USD jährlich oder 25 USD monatlich pro Sitz | Zentral administrierte Teams |
| Team Premium | 100 USD jährlich oder 125 USD monatlich pro Sitz | Hohe Teamnutzung |
| Enterprise | 20 USD pro Sitz plus API-Nutzung | Grosse Organisationen mit erweiterten Kontrollen |

### Datenschutz

Anthropic beschreibt sich für Business-Angebote als Auftragsverarbeiter unter den jeweiligen Kundenvereinbarungen. Die öffentliche Privacy Policy für persönliche Dienste nennt Übermittlungen auf Server in den USA und weitere Länder ausserhalb des EWR und des Vereinigten Königreichs. Für internationale Transfers werden unter anderem Standardvertragsklauseln genannt. Bei persönlichen Konten können Ein- und Ausgaben zur Verbesserung der Modelle verwendet werden, sofern kein Opt-out erfolgt. Für Team und Enterprise ist Modelltraining laut Preisübersicht standardmässig deaktiviert. [2] [3]

Ein klassisches Self-Hosting der Claude-Modelle bietet Anthropic nicht an. Für regulierte Einsätze sind deshalb DPA, gewählte Bereitstellungsform, Datenresidenz und Connector-Berechtigungen vor dem Pilot verbindlich zu klären. Eine Community-Diskussion berichtet zugleich über irritierende Veränderungen und verlorene Memory-Zusammenfassungen im Umfeld anderer Modellupdates. Das beweist keinen Fehler der neuen Funktion, zeigt aber: Projektkontext braucht Export- und Backup-Disziplin, nicht nur Vertrauen in eine Memory-Schaltfläche. [4]

### Stärken

Claude bietet einen sichtbaren und korrigierbaren Kontext statt einer vollständig unsichtbaren Personalisierung. Die standardmässige Deaktivierung in Team und Enterprise ist ein sinnvoller Governance-Startpunkt. Für textintensive, wiederkehrende Arbeit kann die Funktion Reibung deutlich reduzieren, ohne dass sich jede Arbeitsbeziehung in immer längere Prompt-Vorlagen verwandelt.

### Schwächen

Die Funktion bleibt cloudbasiert und die tatsächliche Datenverarbeitung kann internationale Transfers einschliessen. Nutzungsgrenzen bleiben auch in kostenpflichtigen Stufen bestehen. Ausserdem ist editierbarer Speicher kein Nachweis dafür, dass jedes Detail in jeder Antwort korrekt gewichtet wird. Kontextmanagement braucht weiterhin klare Projektordner, Quellen und menschliche Prüfung.

### Einschätzung für die Praxis

Claude mit Memory ist eine sehr gute Wahl für wiederkehrende Text- und Wissensarbeit, wenn der gespeicherte Kontext bewusst gepflegt wird. Starten sollte man mit einem abgegrenzten Arbeitsbereich, klaren Speicherregeln und regelmässigem Aufräumen. Die Konsequenz daraus ist: Memory steigert Produktivität dann, wenn Organisation vor Personalisierung kommt.

---

## 2. Midjourney V8.2 Edit Model

**Kategorie:** Design  
**Relevanzbewertung:** **8,5/10**

### Kurzbeschreibung

Midjourney hat am 27. August den öffentlichen Test seines ersten V8.2-Edit-Modells gestartet und zwei Tage später ein Qualitätsupdate dafür veröffentlicht. Das Edit-Modell bearbeitet Bilder anhand natürlicher Anweisungen, kann bis zu vier Bildreferenzen einbeziehen, bestimmte Bildbereiche verändern und die Arbeitsfläche erweitern. Zudem lässt es sich mit Personalisierung, Moodboards und Style References verwenden. Midjourney weist selbst auf verbleibende Edge Cases hin. [5]

Die Zielgruppe sind Kreativteams, Content-Produzent:innen, Markenverantwortliche und visuelle Generalist:innen, die Bildvarianten nicht mehr nur generieren, sondern gezielt weiterentwickeln wollen. Der entscheidende Unterschied liegt in der Verschiebung von "noch einmal neu" zu "an diesem Motiv gezielt weiterarbeiten".

### Nutzungsszenarien

| Szenario | Konkreter Einsatz | Praktischer Nutzen |
|---|---|---|
| Kampagnenmotive | Motiv an saisonale Botschaft, neues Produkt oder anderes Format anpassen | Konsistente Weiterentwicklung statt kompletter Neuanfang |
| Editorial Design | Einzelne Bildelemente austauschen und den Bildausschnitt für unterschiedliche Kanäle erweitern | Schnellere Adaption für Web, Social und Präsentationen |
| Moodboard-Produktion | Mehrere Referenzbilder als visuelle Leitplanken nutzen | Besser steuerbare Stilrichtung |
| Produktinszenierung | Hintergrund oder bestimmte Bereiche eines Produktmotivs ändern | Mehr Varianten für Tests und Landingpages |

### Pricing

Midjourney führt vier kostenpflichtige Abos. Basic kostet **10 USD pro Monat**, Standard **30 USD**, Pro **60 USD** und Mega **120 USD**. Bei jährlicher Zahlung sinkt der effektive Monatsbetrag um 20 Prozent auf 8, 24, 48 beziehungsweise 96 USD. Einen dauerhaft verfügbaren Free Tier gibt es nicht. Stealth Mode, der Kreationen privat hält, ist nur in Pro und Mega enthalten. [6]

| Tarif | Monatlich | Jährlich, effektiv pro Monat | Relevanter Umfang |
|---|---:|---:|---|
| Basic | 10 USD | 8 USD | 200 Minuten Fast-GPU-Zeit |
| Standard | 30 USD | 24 USD | Unbegrenzte Bildgenerierung im Relax Mode |
| Pro | 60 USD | 48 USD | Stealth Mode und unbegrenzte Bilder sowie SD-Video im Relax Mode |
| Mega | 120 USD | 96 USD | Höchste Fast-GPU-Kapazität und Stealth Mode |

### Datenschutz

Midjourney veröffentlicht keinen konkreten Serverstandort. Die Privacy Policy erfasst unter anderem eingegebene Prompts und hochgeladene Inhalte und beschreibt internationale Datenübermittlungen. Für Personen im EWR, in der Schweiz und im Vereinigten Königreich nennt Midjourney die Standardvertragsklauseln als Schutzmechanismus. Eine Self-Hosting-Option besteht nicht. [7]

Die zentrale praktische Einschränkung ist nicht juristisch, sondern operativ: Private Bildarbeit setzt mindestens Pro oder Mega voraus. Eine Community-Diskussion bewertet V8.2 als detailreicher und schneller auf ein brauchbares Bild zielend, kritisiert jedoch weniger Freiraum für surreal-künstlerische Ergebnisse und einen stärker wörtlichen Stil. Das ist kein Urteil über alle Anwendungsfälle, aber ein guter Gegencheck zur Marketingkurve. [8]

### Stärken

Das Update stärkt die steuerbare Bearbeitung innerhalb eines bereits überzeugenden Bildworkflows. Die Kombination aus Anweisung, mehreren Referenzen, Inpainting und Outpainting reduziert die Zahl der Wiederholungen. Für Markenarbeit sind Moodboards und Style References besonders nützlich, weil sie Stil als wiederverwendbare Arbeitsgrundlage behandeln.

### Schwächen

Es gibt keinen permanenten kostenlosen Einstieg und keine Self-Hosting-Option. Private Kreationen kosten mindestens den Pro-Tarif. Die Dokumentation beschreibt den Funktionsumfang, aber der Teststatus und die ausdrücklich genannten Edge Cases verlangen weiterhin einen echten Qualitätscheck vor Veröffentlichung.

### Einschätzung für die Praxis

Midjourney V8.2 Edit Model ist sehr empfehlenswert für Teams, die aus einem bestehenden Motiv mehrere kontrollierte Varianten entwickeln wollen. Es eignet sich besonders für visuelle Serienproduktion, solange Referenzmaterial, Markenrichtlinien und der finale Freigabeprozess sauber organisiert sind. Es ersetzt nicht den Art Director, aber es reduziert dessen langweiligste Wiederholungen.

---

## 3. PageIndex SDK Local

**Kategorie:** Data / Wissen  
**Relevanzbewertung:** **8,5/10**

### Kurzbeschreibung

PageIndex hat am 27. August eine wesentliche Erweiterung seines SDK angekündigt: Der vollständige reasoning-basierte RAG-Workflow kann lokal laufen. Teams können Baumindizes erstellen, Dokumente lokal speichern, lange Dokumente abfragen und Seitenzitate erzeugen. Der lokale Modus verwendet den eigenen Modellanbieter und API-Schlüssel und benötigt keine Vektordatenbank. [9]

RAG bezeichnet einen Abrufprozess, bei dem ein Modell vor seiner Antwort relevante Dokumentstellen beizieht. PageIndex organisiert Dokumente als hierarchischen Baum und lässt ein Modell über diese Struktur nach passenden Abschnitten suchen. Die Methode ist für textlastige PDFs gedacht, etwa Berichte, Regulatorik, technische Handbücher oder Lehrmaterialien. [9] [10]

### Nutzungsszenarien

| Szenario | Konkreter Einsatz | Praktischer Nutzen |
|---|---|---|
| Geschäftsberichte | Lange Jahres- und Quartalsberichte lokal indexieren und mit Seitenzitaten befragen | Antworten bleiben auf nachvollziehbare Textstellen rückführbar |
| Regulatorische Dokumente | Vorschriften, Richtlinien und Vertragswerke in einem lokalen Wissensworkflow abfragen | Bessere Kontrolle über Dokumentablage und Quellenbezug |
| Technische Dokumentation | Handbücher und Spezifikationen in eine interne Abfrageoberfläche einbinden | Weniger Suchaufwand bei komplexen Sachfragen |
| Fachausbildung | Textlastige Lernunterlagen strukturiert erschliessen | Antworten können direkt mit Seitenangabe geprüft werden |

### Pricing

PageIndex veröffentlicht auf der untersuchten Website keinen öffentlich ausgezeichneten Tarifvergleich und keinen verlässlichen permanenten Free Tier. Die Produktseite bietet einen Zugang zum Testen und eine Demo-Anfrage, doch es wurden keine offiziellen, allgemein sichtbaren Planpreise dokumentiert. [10]

| Preisfrage | Verifizierter Stand |
|---|---|
| Free Tier | Kein öffentlich spezifizierter dauerhafter Tarif auf der geprüften Produktseite |
| Selbstbedienungspläne | Keine offiziell sichtbaren Preise im geprüften Webauftritt |
| Enterprise | Kontakt- beziehungsweise Demo-Prozess vorhanden; Preis nicht öffentlich ausgewiesen |
| Zusatzkosten | Lokaler Modus benötigt einen eigenen Modell-API-Schlüssel; dessen Nutzungskosten fallen beim gewählten Anbieter an |

### Datenschutz

Hinter PageIndex steht Vectify AI Limited mit Sitz in England und Wales. Laut Privacy Policy werden Daten in den USA und im Vereinigten Königreich gespeichert; für Transfers ausserhalb des Vereinigten Königreichs und der EU werden zusätzliche Schutzmassnahmen genannt. Die Richtlinie verweist auf Rechte unter der DSGVO. Sie erklärt zugleich, dass anonymisierte Daten unbegrenzt genutzt und an andere Unternehmen verkauft werden können. Das betrifft nach Darstellung der Policy anonymisierte Informationen, bleibt aber ein Punkt für die Datenklassifizierung. [11]

Die lokale SDK-Option reduziert den Umfang der durch PageIndex verwalteten Speicherung bei Index und Dokumenten deutlich, beseitigt aber nicht die Verantwortung für den gewählten Modellanbieter. PageIndex unterscheidet klar: Lokale Speicherung und Indexierung bleiben lokal, der Chat-Modellzugang läuft mit dem eigenen API-Schlüssel. Eine vollständige On-Premise-Architektur inklusive Modellbetrieb ist damit nicht automatisch gegeben. [9]

### Stärken

Die Kombination aus lokaler Speicherung, natürlicher Dokumentstruktur und Seitenzitaten trifft ein echtes Problem professioneller Wissensarbeit: Antworten sollen nicht nur plausibel klingen, sondern auf eine Seite im Dokument zeigen. Für textlastige Inhalte kann der Verzicht auf Chunking und Vektordatenbank die Architektur vereinfachen.

### Schwächen

Öffentliche Preis- und Plantransparenz ist derzeit unzureichend. Der lokale Modus benötigt technische Kompetenz und einen eigenen Modellzugang. Die Privacy Policy erlaubt die Nutzung und den Verkauf anonymisierter Daten, was bei hochsensiblen Dokumenten eine interne Prüfung der tatsächlichen Datenwege verlangt.

### Einschätzung für die Praxis

PageIndex SDK Local ist sehr relevant für Organisationen, die dokumentenbasierte Antworten mit Quellenbezug und lokaler Kontrolle benötigen. Der richtige Pilot startet mit einer klar abgegrenzten Dokumentklasse und nicht mit dem gesamten Fileshare. So zeigt sich rasch, ob Seitenzitate, Abrufqualität und externe Modellkosten den erwarteten Nutzen liefern.

---

## 4. Lenz

**Kategorie:** Recherche  
**Relevanzbewertung:** **8,0/10**

### Kurzbeschreibung

Lenz ist eine KI-gestützte Faktenprüfungsplattform für Aussagen, die nicht unbelegt im Arbeitsprozess stehen bleiben dürfen. Das Tool extrahiert überprüfbare Behauptungen aus Text, prüft sie über mehrere Schritte und liefert einen dokumentierten Befund. Laut Produktseite kommen acht Modelle über fünf Stufen zum Einsatz, ergänzt durch eine konträre Modell-Debatte, drei unabhängige Prüfer und einen vollständigen Zitationspfad. Die API-Funktionen reichen von Behauptungsextraktion über Schnellbewertung bis zur vertieften Verifizierung und Folgefragen. [13]

Lenz erreichte bei Product Hunt am 27. August Rang 3 des Tages mit 255 Punkten. Der Launch ist damit zeitlich klar im Berichtsfenster verankert. Die Punktezahl ist ein Nachfrage-Signal, keine wissenschaftliche Validierung der Prüfgüte. [16]

### Nutzungsszenarien

| Szenario | Konkreter Einsatz | Praktischer Nutzen |
|---|---|---|
| Content-Freigabe | Fakten in Entwürfen vor Veröffentlichung markieren und prüfen | Weniger unbelegte Aussagen im Redaktionsprozess |
| Produktkommunikation | Leistungsversprechen und Marktzahlen gegen Quellen prüfen | Belastbarere Claims in Sales- und Marketingunterlagen |
| KI-Qualitätssicherung | Antworten eines eigenen KI-Workflows als Prüfauftrag übergeben | Zusätzliche Kontrollschicht vor kundenwirksamer Ausgabe |
| Analytische Briefings | Zentrale Behauptungen eines Briefings samt Quellenpfad sichtbar machen | Bessere Nachvollziehbarkeit für Entscheider:innen |

### Pricing

Lenz bietet einen klar ausgewiesenen Free Tier ohne Kreditkarte. Er umfasst 1.000 Extraktionen pro Tag und 100 Credits pro Monat. Plus kostet **7,99 USD**, Developer **99 USD** und Scale **399 USD** pro Monat. Enterprise ist individuell. Die Credits entsprechen unterschiedlichen Prüfungen: Im Free Plan etwa 100 schnelle Bewertungen, zehn vollständige Verifizierungen oder 100 Folgefragen. [14]

| Tarif | Preis pro Monat | Öffentlicher Umfang |
|---|---:|---|
| Free | 0 USD | 1.000 Extraktionen pro Tag, 100 Credits pro Monat |
| Plus | 7,99 USD | 500 Credits pro Monat |
| Developer | 99 USD | 5.000 Credits pro Monat |
| Scale | 399 USD | 20.000 Credits pro Monat |
| Enterprise | Auf Anfrage | Volumen, SLA, White Label und individuelle Integration |

### Datenschutz

Lenz speichert eingereichte Behauptungen und Analyseergebnisse. Neue Prüfberichte sind standardmässig öffentlich, lassen sich jedoch einzeln oder als Standard auf privat setzen. Das ist kein Nebendetail, sondern eine voreingestellte Veröffentlichungspolitik. Texte werden zur Analyse an Modellanbieter weitergegeben. Lenz nennt Google Cloud als Infrastruktur und beschreibt Verarbeitung und Speicherung personenbezogener Daten in den USA. Für internationale Transfers verweist die Richtlinie auf EU-US Data Privacy Framework und Standardvertragsklauseln. [15]

Self-Hosting wird nicht angeboten. Für die Einbindung in bestehende Systeme stehen API und MCP-Zugang bereit, doch beim Einsatz vertraulicher Inhalte muss die Standard-Sichtbarkeit vor dem ersten Test zwingend auf "Private" gesetzt und der Datenfluss zu Modellanbietern rechtlich geprüft werden. [13] [15]

### Stärken

Lenz löst ein echtes Problem generativer Arbeit: Die Behauptung wird zum prüfbaren Objekt statt zum dekorierten Satz mit Quellen-Optik. Die mehrstufige Architektur und der vollständige Quellenpfad geben Teams eine bessere Grundlage, um Annahmen, Belege und Unsicherheit sichtbar zu machen. Das Free Tier ist für einen ernsthaften Test ausreichend.

### Schwächen

Das Tool ist cloudbasiert, verarbeitet Inhalte mit Drittmodell-Anbietern und speichert Behauptungen sowie Analysen. Die öffentliche Voreinstellung für neue Prüfberichte ist für vertrauliche Arbeit ungeeignet. Als junges Produkt besitzt es zudem noch keine breite, langjährige Praxisbasis.

### Einschätzung für die Praxis

Lenz ist sehr nützlich als Kontrollschicht für veröffentlichungsrelevante Aussagen und KI-generierte Texte. Es sollte nicht als Wahrheitsmaschine behandelt werden, sondern als strukturierter Anlass, Quellen und Gegenargumente offenzulegen. Die Regel für den Einsatz ist simpel: Sensible Inhalte zuerst privat schalten, dann prüfen, danach entscheidet ein Mensch.

---

## 5. Construct Computer

**Kategorie:** Agents  
**Relevanzbewertung:** **8,0/10**

### Kurzbeschreibung

Construct Computer positioniert sich als KI-Arbeitskraft für Einzelunternehmer:innen und kleine Teams. Nach eigener Beschreibung erhält jeder Nutzer einen realen Linux-Cloud-Computer. Die Plattform verbindet Agenten, Dateien, Workflows, Tools, App-Anbindungen und einen einsehbaren Speicher in einem Workspace. Sie kann Hintergrund- und geplante Aufgaben ausführen, Arbeitsschritte protokollieren und abgebrochene Arbeit auf dem vorhandenen Zwischenstand fortsetzen. [17] [18]

Construct war in der Launchwoche bei Product Hunt auf Rang 1 des Tages mit 368 Punkten. Der Launch-Beleg ist stark, die betriebliche Reife muss sich jedoch erst über mehrere Monate und reale Prozesslast beweisen. [20]

### Nutzungsszenarien

| Szenario | Konkreter Einsatz | Praktischer Nutzen |
|---|---|---|
| Wiederkehrende Marktbeobachtung | Rechercheauftrag mit Quellenanforderungen und fester Struktur planen | Ergebnisse liegen in einem persistenten Workspace statt in einem vergessenen Chat |
| Interne Reportings | Dateien aus dem Workspace analysieren, Bericht vorbereiten und Aktivität dokumentieren | Nachvollziehbarer Ablauf über mehrere Arbeitsschritte |
| Operative Vorbereitung | Daten aus verbundenen Anwendungen zusammenführen und einen kontrollierten Entwurf erzeugen | Weniger manuelle Übergaben zwischen einzelnen Tools |
| Prototyping | Kleine interne Werkzeuge und Skripte aus einer fachlichen Aufgabe heraus erstellen | Schnellerer Weg von Arbeitsproblem zu testbarer Lösung |

### Pricing

Construct bietet einen siebentägigen Test. Lite kostet **9 USD monatlich** oder **7,50 USD bei jährlicher Zahlung**, Starter **59 bzw. 39 USD** und Pro **299 bzw. 199 USD**. Lite umfasst bis zu zwei Agenten, maximal 50 Schritte pro Aufgabe und eine Laufzeit von fünf Minuten. Starter erhöht Umfang und Laufzeit, Pro umfasst tiefe Läufe bis 1.000 Schritte, BYOK und bis zu 15 Agenten. Enterprise wird individuell mit SSO, privater Bereitstellung und individuellem MCP-Angebot verhandelt. [18]

| Tarif | Monatlich | Jährlich, effektiv pro Monat | Relevanter Umfang |
|---|---:|---:|---|
| Lite | 9 USD | 7,50 USD | Zwei Agenten, 50 Schritte, fünf Minuten Laufzeit |
| Starter | 59 USD | 39 USD | Bis fünf Agenten, Hintergrund- und Planaufgaben, 30 Minuten Laufzeit |
| Pro | 299 USD | 199 USD | Bis 15 Agenten, bis 1.000 Schritte, BYOK, eine Stunde Laufzeit |
| Enterprise | Auf Anfrage | Auf Anfrage | SSO, private Bereitstellung und individuelle Konfiguration |

### Datenschutz

Construct nennt Cloudflare als zentrale Plattforminfrastruktur und führt unter anderem Composio, Sentry, PostHog und Dodo Payments als beteiligte Dienstleister auf. Workspace-Dateien liegen in Cloudflare R2, Chat-Sitzungen in Cloudflare Durable Objects, und eigene BYOK- sowie Bot-Zugangsdaten werden laut Policy mit AES-GCM verschlüsselt. Arbeitsbereiche, Speicher, Dateien und Aktivitätshistorie bleiben bestehen, solange das Konto aktiv ist, und sollen bei Kontoschliessung gelöscht werden. [19]

Die Privacy Policy enthält keine klare, allgemeine Aussage zur DSGVO-Konformität oder zum konkreten Verarbeitungsstandort. Sie beschreibt zudem umfangreiche Analysefunktionen für die öffentliche Website, einschliesslich nicht maskiertem Session Replay. Das ist nicht automatisch ein Ausschlussgrund, aber eine rote Flagge für eine leichtfertige Nutzung mit vertraulichen Daten. Private Bereitstellung wird für Enterprise genannt, die technischen und vertraglichen Details müssen vor einer Beschaffung geklärt werden. [18] [19]

### Stärken

Construct verbindet persistenten Workspace, Agenten, Tools und Aktivitätsprotokoll in einer Weise, die über eine einzelne Chat-Antwort hinausgeht. Besonders wertvoll ist das Prinzip, begonnene Arbeit nicht bei einem Fehler zu verlieren. Die sichtbare Memory- und Activity-Schicht kann die sonst typische Black Box agentischer Abläufe reduzieren.

### Schwächen

Der Lite-Tarif ist für komplexe Aufgaben eng begrenzt; der Sprung zu Pro ist erheblich. Das Produkt ist neu und hat noch wenig Langzeitbelege. Hinzu kommen offene Fragen zu Standort, DSGVO-Absicherung und Analytics-Umfang. Agenten dürfen zudem keine Freigabe für irreversible externe Handlungen erhalten, nur weil ihr Dashboard nett aussieht.

### Einschätzung für die Praxis

Construct eignet sich für einen eng geführten Pilot mit wiederkehrender Recherche, internen Reports oder vorbereitenden Workflows. Starten sollte man mit Leserechten, einer kleinen Datenklasse, klaren Laufzeitgrenzen und einem obligatorischen Review vor jeder externen Aktion. Die Kernfrage lautet nicht "Kann der Agent arbeiten?", sondern "Kann das Team jede relevante Wirkung nachvollziehen und stoppen?"

---

## Methodik und Qualitätsgrenzen

Die Auswahl begann mit einer Shortlist aus 21 Kandidaten, die in den zehn festgelegten Quellengruppen im Berichtszeitraum erwähnt wurden. Je Kategorie wurde genau ein Tool gewählt. Die Priorisierung folgte Neuerscheinung oder relevantem Update, unmittelbarem Nutzwert, nachvollziehbaren Preisangaben und der verfügbaren Datenschutzdokumentation.

Die Bewertung bildet keine Labormessung ab. Sie gewichtet Neuheitswert, konkrete Anwendung, Preis- und Transparenzniveau, Kontrollierbarkeit, Datenschutzrisiken und die erkennbare Produktreife. Eine hohe Bewertung bedeutet nicht "risikofrei". Sie bedeutet, dass der praktische Nutzen die klar benannten Einschränkungen unter definierten Einsatzbedingungen überwiegen kann.

| Qualitätscheck | Ergebnis |
|---|---|
| Fünf fixe Kategorien, je ein Tool | Erfüllt |
| Neuheit oder bedeutendes Update im Berichtszeitraum | Erfüllt |
| Offizielle Produkt- und Releasebelege | Erfüllt |
| Öffentliche Preisseite oder transparent ausgewiesene Preisgrenze | Erfüllt, bei PageIndex keine öffentlichen Planpreise verfügbar |
| Datenschutzprüfung und Self-Hosting-Einordnung | Erfüllt |
| Unabhängige Resonanzquelle | Erfüllt; bei jungen Tools überwiegend Product Hunt oder Community-Diskussionen |
| Keine Tool-Vergleiche | Erfüllt |

## Quellen

[1]: https://support.claude.com/en/articles/12138966-release-notes "Anthropic Help Center: Release Notes"
[2]: https://www.anthropic.com/pricing "Anthropic: Pricing"
[3]: https://www.anthropic.com/legal/privacy "Anthropic: Privacy Policy"
[4]: https://www.reddit.com/r/claudexplorers/comments/1vbxf3f/changes_to_claude_august_26_megathread/ "Reddit: Changes to Claude, August 2026 Megathread"
[5]: https://updates.midjourney.com/edit-model-for-v8/ "Midjourney: Edit Model for V8"
[6]: https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans "Midjourney: Comparing Plans"
[7]: https://docs.midjourney.com/hc/en-us/articles/32083472637453-Privacy-Policy "Midjourney: Privacy Policy"
[8]: https://www.reddit.com/r/midjourney/comments/1v6dpkn/thoughts_on_v82/ "Reddit: Thoughts on V8.2"
[9]: https://pageindex.ai/blog/pageindex-sdk-local "PageIndex: SDK Goes Local"
[10]: https://pageindex.ai/ "PageIndex: Product Overview"
[11]: https://pageindex.ai/privacy "PageIndex: Privacy Policy"
[12]: https://www.producthunt.com/products/pageindexai "Product Hunt: PageIndex"
[13]: https://lenz.io/ "Lenz: Audit-grade Fact-Checking"
[14]: https://lenz.io/plans "Lenz: Plans and Pricing"
[15]: https://lenz.io/privacy "Lenz: Privacy Policy"
[16]: https://www.producthunt.com/products/lenz-2 "Product Hunt: Lenz"
[17]: https://construct.computer/ "Construct Computer: Product Overview"
[18]: https://construct.computer/pricing "Construct Computer: Pricing"
[19]: https://construct.computer/privacy "Construct Computer: Privacy Policy"
[20]: https://www.producthunt.com/products/construct-computer "Product Hunt: Construct Computer"
