# Wöchentliche KI-Tool-Analyse – KW 40/2026

**Recherchezeitraum:** 28. September bis 4. Oktober 2026  
**Stand:** 4. Oktober 2026  
**Methodik:** Die Auswahl beruht auf einem systematischen Scan der im Playbook festgelegten Quellen. Für jedes ausgewählte Tool wurden Release, offizielle Produktseite, Pricing, Privacy Policy und verfügbare unabhängige Signale geprüft. Wo ein Hands-on-Test einen Account, eine Kreditkarte oder kostenpflichtigen Zugang voraussetzt, wird dies transparent vermerkt.

## Wochenzusammenfassung

Die auffälligste Bewegung dieser Woche liegt nicht bei noch mehr generierter Prosa, sondern bei **kontrollierbarer Ausführung**. Claude Sonnet 5.5 und Strands Decider 2B zielen auf unterschiedliche Teile derselben Wertschöpfung: Das eine System erledigt klar abgegrenzte Wissensarbeit schneller, das andere trifft günstige, lokale Routineentscheidungen mit Konfidenzwert. Für Unternehmen ist das wichtiger als der übliche Benchmark-Zirkus, weil daraus überprüfbare Workflows entstehen können.

Auf der kreativen Seite wird Audio zur zusammenhängenden Produktionseinheit. Suno Speech generiert Sprechstimme und Musikbett gemeinsam, ist aber klar als Beta zu behandeln. Das senkt den Produktionsaufwand für einfache Formate, ersetzt jedoch weder Rechteklärung noch Qualitätsabnahme. Kreativität ohne Governance ist nur schnelleres Risiko mit hübscherem Soundtrack.

Slashspace 3.3 und OpenAI Dots zeigen zwei gegensätzliche Betriebsmodelle für agentische Arbeit. Slashspace legt Canvas, Chats und Dateien grundsätzlich lokal ab, verlagert je nach gewählter Funktion aber Daten an diverse Modell- und Analyseanbieter. Dots bietet eine stark integrierte, dauerhaft arbeitende Cloud-Agenten-Erfahrung, ist zum Analysezeitpunkt jedoch für Pro-Nutzer:innen in der Schweiz nicht verfügbar. Das eigentliche Problem ist nicht die Anzahl von Funktionen, sondern die Frage, **wer die Datenwege, Berechtigungen und Freigaben tatsächlich kontrolliert**.

| Kategorie | Ausgewähltes Tool | Release-Signal | Relevanz | Kurzurteil |
|---|---|---:|---:|---|
| Text | Claude Sonnet 5.5 | 29.09.2026 | **8,8/10** | Stark für klar abgegrenzte Wissens- und Umsetzungsarbeit, mit Governance-Aufwand im Consumer-Plan. |
| Design | Suno Speech Beta | 01.10.2026 | **7,4/10** | Schneller kreativer Audio-Prototyp, aber Beta-Qualität und US-Cloud begrenzen professionelle Einsätze. |
| Data / Wissen | Strands Decider 2B | 01.10.2026 | **8,2/10** | Transparente, lokal betreibbare Entscheidungsinfrastruktur für technische Teams. |
| Recherche | Slashspace 3.3 | aktuelle Version im Wochenfenster | **7,8/10** | Überzeugender Recherche-Canvas mit ungewöhnlich klarer Local-first-Dokumentation. |
| Agents | Dots by OpenAI | 29.09.2026 | **7,0/10** | Konzeptionell stark, für die Schweiz derzeit aber nicht zugänglich und deshalb praktisch eingeschränkt. |

> **Bewertungslogik:** Die Bewertung misst den gegenwärtigen Praxiswert, nicht Marketinglautstärke. Datenschutz, Verfügbarkeit, Kontrollmöglichkeiten und dokumentierte Grenzen beeinflussen die Note direkt.

---

## 1. Claude Sonnet 5.5

| Pflichtfeld | Einordnung |
|---|---|
| **Kategorie** | Text |
| **Status** | Neues Modellrelease vom 29. September 2026. |
| **Kurzbeschreibung** | Schnelleres Claude-Modell für klar abgegrenzte Wissensarbeit, Dokumente, Tabellen, Slides und technische Umsetzungsaufgaben. |
| **Zielgruppe** | Wissensarbeiter:innen, Produkt- und Operations-Teams sowie Entwickler:innen mit wiederkehrenden, klar spezifizierten Aufgaben. |
| **Relevanzbewertung** | **8,8/10** |
| **Teststatus** | Kein Account-Test durchgeführt. Zugriff, Nutzungsgrenzen und Datenpfade hängen vom gewählten Claude-Plan bzw. Cloud-Provider ab. |

Claude Sonnet 5.5 ist kein neues Textwerkzeug im engeren Sinn, sondern die aktuelle Modellschicht hinter Claude. Anthropic positioniert es für gut definierte Alltagsaufgaben, Fehlerkorrekturen und die Erstellung von Dokumenten, Tabellen sowie Präsentationen. Gegenüber Sonnet 5 nennt der Anbieter mehr als 30 Prozent höhere Geschwindigkeit und bis zu 30 Prozent niedrigere Kosten pro Aufgabe. Diese Werte sind Herstellerangaben und sollten im eigenen Aufgabenportfolio validiert werden. Für die Praxis ist relevanter, dass der Nutzen bei präzisen Aufgabenbeschreibungen entsteht, nicht bei offenen Strategiefragen ohne Qualitätskriterien. [1]

Die Stärke liegt in der Kombination aus Geschwindigkeit, langem Kontext und einer breiten Arbeitsoberfläche. Sinnvolle Szenarien sind erstens das Überführen geprüfter Stichpunkte in einen strukturierten Management-Entwurf, zweitens das Bereinigen und Dokumentieren von Code-Änderungen, drittens die Aufbereitung von Tabellen in nachvollziehbare Entscheidungsvorlagen, viertens die Erstellung erster Präsentationsentwürfe auf Basis einer verbindlichen Vorlage und fünftens die Extraktion klar definierter Felder aus nicht vertraulichen Dokumenten. Die Konsequenz daraus ist: Sonnet 5.5 eignet sich als Produktionsschicht, sobald Inputs, gewünschte Ausgabe und fachliche Abnahme sauber definiert sind. [1]

**Pricing:** Im Claude-Webprodukt gibt es einen kostenlosen Plan mit Sonnet-Zugang, allerdings mit Nutzungsgrenzen. Claude Pro kostet in den USA 20 USD monatlich beziehungsweise 17 USD pro Monat bei jährlicher Zahlung. Die Max-Stufen liegen bei 100 USD und 200 USD monatlich. Für die API kostet Sonnet 5.5 2 USD je eine Million Input-Tokens und 10 USD je eine Million Output-Tokens; Cache Reads werden mit 0,20 USD je Million Tokens ausgewiesen. Preise verstehen sich zuzüglich allfälliger Steuern und können sich ändern. Für kleine Teams ist der Free Plan sinnvoll für Funktionsverständnis, nicht als belastbare Produktionsgrundlage. [1] [2] [3]

**Datenschutz:** Anthropic erklärt für persönliche Claude-Konten, Inputs und Outputs könnten zur Modellverbesserung verwendet werden, sofern Nutzer:innen nicht widersprechen. Die Privacy Policy nennt Datenübermittlungen in die USA und weitere Länder sowie Standardvertragsklauseln für Transfers aus EWR, UK und Schweiz. Für Team- und Enterprise-Angebote erfolgt Modelltraining laut Pricing standardmässig nicht; zusätzlich existieren Enterprise-Kontrollen und eine US-only-Inference-Option. Eine Self-Hosting-Option gibt es nicht. Eine pauschale DSGVO-Konformität lässt sich deshalb nicht seriös behaupten: Für personenbezogene oder vertrauliche Inhalte braucht es je nach Einsatz ein DPA, eine Transfer Impact Assessment, definierte Connector-Rechte und einen dokumentierten Opt-out beziehungsweise Business-Vertrag. [2] [4]

**Stärken:** Sonnet 5.5 verbindet eine breite Aufgabenabdeckung mit hoher Geschwindigkeit und transparenten API-Preisen. Anthropic dokumentiert zudem die Grenzen und Sicherheitsvorkehrungen des Releases vergleichsweise ausführlich. **Schwächen:** Die Leistungs- und Kostenbehauptungen stammen überwiegend aus Anbieter- und Benchmarkdaten. Im Consumer-Kontext ist die Trainingsnutzung nicht standardmässig ausgeschlossen, und externe Connectoren erweitern den Datenpfad zusätzlich. Für hochgradig offene, folgenreiche Entscheidungen bleibt fachliche Prüfung zwingend.

**Einschätzung für die Praxis:** Starten Sie mit einem abgegrenzten Workflow, etwa einer wiederkehrenden Präsentations- oder Dokumentaufbereitung. Messen Sie Durchlaufzeit, Nachbearbeitungsaufwand, Fehlerrate und die Qualität der Quellenprüfung gegen einen manuellen Referenzprozess. Erst wenn diese Kennzahlen besser werden, lohnt sich eine Ausweitung. Der entscheidende Unterschied liegt nicht im besseren Prompt, sondern in einem wiederholbaren Qualitäts- und Freigabeprozess.

---

## 2. Suno Speech Beta

| Pflichtfeld | Einordnung |
|---|---|
| **Kategorie** | Design |
| **Status** | Öffentliche Beta seit 1. Oktober 2026. |
| **Kurzbeschreibung** | Generiert gesprochene Audios mit passendem, originärem Musikbett als zusammenhängenden Track. |
| **Zielgruppe** | Creator, Marketing- und Kommunikationsteams sowie Bildungsanbieter mit Bedarf an schnellen Audio-Prototypen. |
| **Relevanzbewertung** | **7,4/10** |
| **Teststatus** | Kein Account-Test durchgeführt. Die Analyse basiert auf der offiziellen Beta-Ankündigung, Produkt- und Privacy-Dokumentation sowie externen Launch-Signalen. |

Suno Speech Beta erweitert die Musikplattform um ein Modell, das Sprechstimme und Hintergrundmusik gemeinsam erzeugt. Nutzer:innen geben eine Idee, einen Text oder ein Gedicht sowie gewünschte Stimm- und Musikmerkmale ein. Suno beschreibt die Funktion ausdrücklich als Beta und weist selbst auf noch unzuverlässige Akzente und übertriebene Pausen hin. Genau das ist der wichtige Realitätscheck: Das Tool ist ein schneller Generator für eine kohärente Audio-Skizze, nicht automatisch eine sendefähige Audio-Produktion. [5]

Sinnvolle Nutzungsszenarien sind erstens ein Mood-Prototyp für einen Audio-Teaser, zweitens ein Entwurf für eine geführte Meditation, drittens eine Vorversion für eine Lernsequenz, viertens ein kreativer Test von Erzählrhythmus und Musikdramaturgie sowie fünftens ein schnelles internes Konzept für Social- oder Event-Kommunikation. Für diese Anwendungen spart Speech Produktionsschritte, weil Stimme und Musik nicht separat synchronisiert werden müssen. Was oft unterschätzt wird: Die kreative Idee wird dadurch nicht automatisch rechtlich, sprachlich oder markentechnisch freigegeben.

**Pricing:** Suno bietet einen Free Plan für 0 USD mit 50 Credits pro Tag, kostenlosen Modellen und ohne kommerzielle Rechte. Pro kostet 8 USD pro Monat bei jährlicher Abrechnung und umfasst 2'500 Credits, kommerzielle Nutzungsrechte, frühen Zugriff auf Funktionen sowie zusätzliche Editing-Funktionen. Premier kostet 24 USD pro Monat bei jährlicher Abrechnung und enthält 10'000 Credits, mehr Downloads und Suno Studio. Die Pricing-Seite nennt Speech Beta nicht als separat verrechenbare Funktion; die tatsächliche Credit-Belastung sollte vor einem Produktionsentscheid im Konto geprüft werden. [6]

**Datenschutz:** Suno ist in den USA ansässig und speichert Informationen laut Privacy Notice grundsätzlich auf Servern in den USA. Die Richtlinie erfasst Prompts, Uploads, Stimmaufnahmen, erzeugte Inhalte und Nutzungsdaten; sie erlaubt zudem, bestimmte Inhalte zur Verbesserung der Produkte und der Modelle zu verwenden. Für EWR- und UK-Transfers nennt Suno angemessene Garantien, veröffentlicht aber keine EU-Residenz oder Self-Hosting-Option für Speech. Die Policy beschreibt DSGVO-Rechte, ist aber kein Ersatz für eine unternehmensspezifische Datenschutzprüfung. Vertrauliche Skripte, personenbezogene Stimmen oder unveröffentlichte Kampagnen sollten deshalb nicht in der Beta verarbeitet werden. [7]

**Stärken:** Speech reduziert den Medienbruch zwischen Voiceover und Musikbett und kann Kreativ-Teams sehr schnell zu einer diskutierbaren Richtung bringen. Der kostenlose Einstieg erlaubt risikofreie Erkundung mit nicht kritischen Inhalten. **Schwächen:** Beta-Status, unklare Produktionskontrolle auf Wort- und Satzebene, fehlende lokale Ausführung und US-Datenverarbeitung. Die hörbare Qualität einer Demo ist kein Beweis für belastbare Marken- oder Voice-Governance.

**Einschätzung für die Praxis:** Nutzen Sie Speech als Ideations- und Prototyping-Tool. Arbeiten Sie mit fiktiven Texten, einem Freigabeprozess für Aussagen und einer menschlichen Nachbearbeitung vor Veröffentlichung. Für externe Kommunikation braucht es zusätzlich Rechteklärung, Tonalitätsabnahme und einen Test mit der tatsächlichen Zielgruppe. Die Stärke ist Geschwindigkeit beim Entwurf, nicht autonome Endproduktion.

---

## 3. Strands Decider 2B

| Pflichtfeld | Einordnung |
|---|---|
| **Kategorie** | Data / Wissen |
| **Status** | Open-Source-Release vom 1. Oktober 2026. |
| **Kurzbeschreibung** | Kleines Entscheidungsmodell, das zwischen vorgegebenen Optionen auswählt oder Skalenwerte und Konfidenzen ausgibt. |
| **Zielgruppe** | Engineering-, Data- und Plattformteams, die Agenten-Workflows, Triage oder Guardrails selbst betreiben wollen. |
| **Relevanzbewertung** | **8,2/10** |
| **Teststatus** | Kein lokaler Modelltest. Der veröffentlichte Checkpoint, Code und die Trainingsartefakte wurden auf Lizenz, Betriebsmodell und dokumentierte Grenzen geprüft. |

Strands Decider 2B ist kein Chatbot. Das Modell generiert keine freie Prosa, sondern beantwortet Auswahl-, Ja/Nein- und Skalenfragen mit Konfidenzwert. Der Anbieter beschreibt es als "System-One"-Modell für schnelle Routineentscheidungen in Agenten-Workflows. Beispiele sind Tool-Auswahl, Routing, Argumentprüfung vor einem Tool-Aufruf, Triage und einfache Policy-Checks. Diese Spezialisierung ist keine Schwäche, sondern der Kern des Nutzens: Nicht jede Entscheidung braucht ein teures, generatives Modell, und nicht jede Konfidenz darf aus einem hübschen Satz herausinterpretiert werden. [8]

Für die Praxis bieten sich fünf Szenarien an: Erstens die Klassifizierung eingehender Service-Anfragen nach Team oder Priorität. Zweitens die Prüfung, ob Angaben für einen Tool-Aufruf tatsächlich aus dem Nutzerinput ableitbar sind. Drittens das Routing einer Aufgabe an das passende Modell oder den passenden Workflow. Viertens die Bewertung, ob ein generierter Entwurf eine definierte Mindestanforderung erfüllt. Fünftens die Eskalation unsicherer Fälle an Menschen ab einem selbst kalibrierten Schwellenwert. Das Modell kann lokal auf CPU, GPU oder Apple Silicon laufen; laut Anbieter liegt die mittlere Latenz auf einer RTX 3090 bei rund 115 Millisekunden. [8] [9]

**Pricing:** Der Code und die Modellgewichte stehen unter Apache-2.0-Lizenz. Damit fallen keine Lizenzkosten für den Decider selbst an. Ein kostenloser SaaS-Free-Tier ist nicht nötig, weil die Software selbst lokal oder in eigener Infrastruktur betrieben wird. Reale Kosten entstehen durch Hardware, Betrieb, Monitoring, Modell-Downloads, allfällige Basis- oder Begleitmodelle sowie die Engineering-Zeit. Wer Daten aus dem eigenen Unternehmen verarbeitet, muss diese Kosten gegen den Gewinn an Kontrolle rechnen, nicht gegen "gratis" auf einer Landingpage. [9] [10]

**Datenschutz:** Im Self-Hosting-Betrieb kann der Datenfluss auf eigener Infrastruktur verbleiben. Die Hugging-Face-Dokumentation weist darauf hin, dass der lokale Server standardmässig auf `127.0.0.1` bindet und keine Authentisierung enthält. Daraus folgt nicht automatisch Sicherheit, sondern eine klare Betriebsaufgabe: Netzwerkzugriff, Authentisierung, Logging, Patch-Management und Datenklassifizierung liegen beim betreibenden Team. Strands veröffentlicht keinen Managed-Cloud-Dienst für diesen Checkpoint, keine eigene EU-Residenz und keine pauschale DSGVO-Zusage. Datenschutzkonformität ist hier technisch gut erreichbar, aber nur durch korrekte Implementierung und Governance. [10]

**Stärken:** Apache-2.0-Lizenz, offen dokumentierte Trainings- und Evaluationselemente, lokale Ausführung und explizite Konfidenzwerte machen das Modell ungewöhnlich gut prüfbar. Die Dokumentation benennt auch Grenzen bei langen, mehrstufigen Dokumenten und empfiehlt, Schwellenwerte auf eigener Verkehrslage zu messen. **Schwächen:** Es ist ein Entwicklerwerkzeug, kein Klickprodukt. Seine Konfidenzwerte sind kein Freipass für autonome Entscheide, und die Benchmark-Ergebnisse enthalten Selbstangaben des Projekts. [9] [10]

**Einschätzung für die Praxis:** Beginnen Sie mit einem risikoarmen Routing- oder Triage-Fall und einem gelabelten historischen Datensatz. Kalibrieren Sie Konfidenzschwellen gegen echte Fehlerraten und erzwingen Sie bei Unsicherheit eine menschliche Freigabe. Der entscheidende Unterschied liegt in der Messbarkeit: Statt ein grosses Modell nach seiner "Sicherheit" zu fragen, lässt sich hier eine konkrete Entscheidung, Schwelle und Eskalation operativ testen.

---

## 4. Slashspace 3.3

| Pflichtfeld | Einordnung |
|---|---|
| **Kategorie** | Recherche |
| **Status** | Umbenennung von RabbitHoles AI zu Slashspace und aktuelle Version 3.3.0 im untersuchten Wochenfenster. |
| **Kurzbeschreibung** | Desktop-Canvas für Multi-Modell-Recherche, verknüpfte Quellen, Social-Transkripte, lokale Dateien und orchestrierte Hilfsagenten. |
| **Zielgruppe** | Research-intensive Einzelpersonen, Studios und kleine Teams mit mehreren Modellabos oder lokalen Modellen. |
| **Relevanzbewertung** | **7,8/10** |
| **Teststatus** | Kein Trial gestartet, da die dreitägige Testphase eine Karte verlangt. Funktions- und Datenflussanalyse basiert auf Website, Changelog und Privacy Policy. |

Slashspace 3.3 ist eine räumliche Arbeitsoberfläche für Recherche. Die aktuelle Version verbindet ein unendliches Canvas mit mehreren Modellzugängen, lokalen Modellen via Ollama, Claude Code und Codex, einem Orchestrator-Modus mit Hilfsagenten sowie dem Import von TikTok-, Instagram-, X- und YouTube-Inhalten inklusive Transkripten. Der Nutzen ist nicht das Canvas als Dekoration, sondern die Möglichkeit, Quellen, Teilfragen, Notizen und Modellantworten sichtbar zu verknüpfen. Für anspruchsvolle Recherche kann das die Qualität der Fragestellung verbessern, sofern Quellen und Schlüsse getrennt dokumentiert werden. [11] [12]

Praktisch eignet sich Slashspace erstens für die Zerlegung einer Marktfrage in überprüfbare Teilhypothesen. Zweitens für die Auswertung mehrerer Social- und Videoquellen zu wiederkehrenden Themen. Drittens für einen Research-Sprint, bei dem unterschiedliche Modelle nur für klar abgegrenzte Rollen eingesetzt werden. Viertens für ein evidenzbasiertes Content-Briefing mit Quellenknoten, Gegenargumenten und Entwurfsknoten. Fünftens für ein lokales Wissenscanvas mit Ollama, sofern keine Cloud-Funktionen verwendet werden. Die Grenzen müssen sichtbar bleiben: Ein Canvas speichert Zusammenhänge, es ersetzt nicht die Quellenprüfung.

**Pricing:** Slashspace bietet keinen dauerhaften kostenlosen Plan. Der Test dauert drei Tage und erfordert eine Kreditkarte. Danach kostet die Jahreslizenz 89 USD pro Jahr, laut Anbieter ungefähr 7,40 USD pro Monat; alternativ wird eine zeitlich begrenzte Lifetime-Lizenz für 249 USD angeboten. Beide Optionen umfassen zwei Geräte und 500 Bonus-Credits für den optionalen gehosteten Anbieter. Eigene API-Schlüssel, lokale Modelle und die jeweiligen Drittanbieter können zusätzliche Kosten verursachen. [12]

**Datenschutz:** Slashspace beschreibt sich als Local-first: Canvases, Chats und Dateien liegen grundsätzlich im lokalen Ordner auf dem Computer. Bei eigenen API-Schlüsseln gehen Chats direkt an den gewählten Provider; bei gehosteten Modellen, dem Orchestrator oder bestimmten Medienfunktionen werden Inhalte, Canvas-Kontext oder Job-Daten an Server und Unterauftragnehmer übermittelt. Die Policy nennt unter anderem Vercel AI Gateway, Anthropic, OpenAI, Amazon Bedrock, Trigger.dev, PostHog und Sentry. Lokale API-Schlüssel werden in der sicheren Betriebssystemablage gespeichert; Umgebungsvariablen für lokale MCP-Server können hingegen unverschlüsselt in den App-Einstellungen liegen. Eine EU-Residenz, Self-Hosting des gesamten Produkts oder eine pauschale DSGVO-Zusage wird nicht angeboten. Die Transparenz der Policy ist positiv, entbindet aber nicht von einer Datentrennung nach Sensitivität. [13]

**Stärken:** Das lokale Datenmodell, der Support für eigene Provider und die ungewöhnlich konkrete Privacy Policy sind für Recherchearbeit wertvoll. Das Pricing ist für Einzelpersonen nachvollziehbar. **Schwächen:** Die Orchestrierung verlagert im gehosteten Modus Content und Job-Historie an mehrere Dienstleister. Der Trial ist nicht ohne Zahlungsmittel verfügbar, und frei zugängliche unabhängige Tests zum 3.3-Release sind noch dünn. Die bisher sichtbaren Ratings im Verzeichnis There's An AI For That sind ein Signal, aber kein Ersatz für einen kontrollierten Praxistest. [11] [13]

**Einschätzung für die Praxis:** Testen Sie Slashspace mit einer unkritischen, bekannten Recherchefrage. Definieren Sie vorab: Welche Quellen sind zulässig? Welche Behauptungen brauchen Primärquellen? Welche Modelle dürfen welche Daten sehen? Messen Sie nicht nur Geschwindigkeit, sondern auch die Anzahl korrekt belegter Aussagen und die Nachbearbeitungszeit. Das eigentliche Problem ist nicht fehlender KI-Output, sondern unklare Provenienz in einem sehr bequemen Canvas.

---

## 5. Dots by OpenAI

| Pflichtfeld | Einordnung |
|---|---|
| **Kategorie** | Agents |
| **Status** | Rollout seit 29. September 2026. |
| **Kurzbeschreibung** | Dauerhaft arbeitende Cloud-Agenten in ChatGPT mit eigener Cloud-Umgebung, App-Verbindungen, Regeln und Aktivitätsansicht. |
| **Zielgruppe** | Pro- und Business-Premium-Nutzer:innen in unterstützten Regionen sowie Enterprise-Teams im Beta-Zugang. |
| **Relevanzbewertung** | **7,0/10** |
| **Teststatus** | Kein Test möglich: Zum Stichtag sind Dots für Pro-Nutzer:innen in EWR, Schweiz und UK nicht verfügbar. |

Dots sind immer aktive Agenten in ChatGPT, die Kontext zwischen Gesprächen behalten und Aufgaben im Hintergrund bearbeiten können. Jeder Dot erhält laut OpenAI einen eigenen Cloud-Computer und Browser; über Plugins lassen sich mehr als 4'000 Apps anbinden. Die Produktidee ist operativ relevant, weil sie Agenten von einmaligen Chat-Sitzungen in dauerhafte Verantwortungsbereiche verschiebt. Das erhöht potenziell den Nutzen, aber auch die Angriffsfläche. Ein Agent mit mehr Kontext, mehr Laufzeit und mehr App-Zugriff braucht mehr Governance, nicht weniger. [14]

Geeignete Szenarien sind erstens ein regelmässiger, rein lesender Markt- oder Kalendercheck. Zweitens die Vorbereitung von Entwürfen aus wiederkehrendem Feedback. Drittens das Nachhalten offener Punkte in einem klar begrenzten Projekt. Viertens die Voranalyse neuer Daten mit Eskalation bei Abweichungen. Fünftens die Erstellung von Entwürfen für Content- oder Sales-Material mit zwingender Freigabe. OpenAI dokumentiert, dass proaktive Recherche zunächst nur mit read-only Berechtigungen auf verbundene Apps zugreift und dass bestimmte Handlungen eine Auto-Review- oder Nutzerfreigabe benötigen. Trotzdem gilt: Vor jeder Freigabe ist das Ergebnis zu prüfen, denn die Hilfe weist ausdrücklich auf mögliche Fehler hin. [14] [15]

**Pricing:** Dots haben keinen separaten Preis. Der erste Dot ist laut OpenAI in ChatGPT Pro oder Business Premium ohne Aufpreis enthalten; Free und Plus haben keinen Zugriff. Für ChatGPT Pro wird öffentlich ein Einstieg ab 100 USD pro Monat berichtet, während Business-Premium-Preise regional und vertragsabhängig sein können. Die offizielle Pricing-Seite zeigt Dot als Bestandteil von Pro, nennt im extrahierbaren öffentlichen Preisvergleich aber keinen festen Betrag. Für eine Beschaffung gilt deshalb: Preis, Nutzungsgrenzen, Region und Add-ons im konkreten Angebot verifizieren, bevor ein Budget freigegeben wird. [14] [16] [17]

**Datenschutz:** Jede Instanz arbeitet in einer OpenAI-Cloud-Umgebung, eine Selbsthost-Option wird nicht angeboten. Persönliche ChatGPT-Inhalte können, abhängig von den Datenkontrollen, zur Modellverbesserung verwendet werden. Für Business-, Enterprise- und Edu-Workspaces gilt laut OpenAI standardmässig keine Nutzung zur Modellverbesserung. OpenAI verarbeitet personenbezogene Daten in verschiedenen Jurisdiktionen, einschliesslich USA. Dots erlauben eigene Regeln, App-Berechtigungen und Einsicht in ihre Aktivität; beim Verbinden eigener Apps können sie Informationen daraus dauerhaft in ihren Speicher aufnehmen. Das ist ein brauchbarer Kontrollansatz, aber keine pauschale DSGVO-Freigabe. [14] [15] [18]

Die grösste praktische Einschränkung ist die Verfügbarkeit. Die offizielle Hilfe schliesst Pro-Nutzer:innen in EWR, Schweiz und UK beim Start aus; Business Premium soll in unterstützten ChatGPT-Regionen verfügbar sein, Enterprise ist Beta und standardmässig deaktiviert. Damit ist Dots für eine Schweizer Einzelperson in KW 40/2026 nicht test- und nicht produktiv nutzbar. Diese regionale Lücke drückt die Praxisnote bewusst: Ein beeindruckendes Produktversprechen ist kein Nutzen, wenn es im relevanten Rechts- und Vertriebsraum nicht zugänglich ist. [15]

**Stärken:** Durchgängige Kontextarbeit, Aktivitätsansicht, integrierte Freigaberegeln und der eigene Cloud-Computer sind eine starke Agentenbasis. Product Hunt listete Dots in der Startwoche als bezahlten Launch, was das öffentliche Launch-Signal bestätigt. **Schwächen:** Kein Self-Hosting, erhebliche Abhängigkeit von Cloud, Apps und Berechtigungen, unklare regionale Verfügbarkeit sowie persönliche Datenkontrollen, die aktiv konfiguriert werden müssen. [17] [18]

**Einschätzung für die Praxis:** Für berechtigte Business-Teams lohnt sich ein read-only Pilot mit Testdaten, maximal zwei Connectoren, klaren Freigabegrenzen und einem dokumentierten Kill-Switch. Für Schweizer Pro-Nutzer:innen lautet die korrekte Entscheidung derzeit schlicht: beobachten, nicht planen. Das ist weniger spektakulär als ein Agenten-Hype, aber deutlich nützlicher.

---

## Querschnitt: Datenschutz- und Einführungsentscheid

| Tool | Datenmodell | Öffentliche Residenzangabe | Self-Hosting | Einführungsentscheidung |
|---|---|---|---|---|
| Claude Sonnet 5.5 | Cloud; persönliche Inputs opt-out für Training | US und weitere Länder; US-only-Inference für bestimmte Workloads | Nein | Mit Business-/Enterprise-Vertrag und klaren Datenklassen pilotieren. |
| Suno Speech Beta | Cloud; Prompts, Uploads und Content werden verarbeitet | Grundsätzlich USA | Nein | Nur mit nicht vertraulichen Inhalten und menschlicher Endabnahme testen. |
| Strands Decider 2B | Lokal oder eigene Infrastruktur möglich | Betreiberabhängig | Ja | Für technische Teams mit MLOps- und Security-Basis empfehlen. |
| Slashspace 3.3 | Local-first, aber featureabhängige Cloud-Datenwege | Keine EU-Residenz publiziert | Nicht für das Gesamtprodukt | Mit lokalen Modellen und nicht vertraulichen Research-Piloten beginnen. |
| Dots by OpenAI | Cloud-Agent mit verbundenen Apps | Mehrere Jurisdiktionen inkl. USA | Nein | Schweizer Einzelzugang abwarten; Business-Pilot nur in unterstützter Region. |

## Qualitäts- und Quellenhinweis

Die Recherche deckte die im Playbook genannten kuratierten Quellen ab. AI Breakfast, Futurepedia, Ben's Bites, FutureTools, There's An AI For That, Product Hunt, Toolify, TopAI.tools, The AI Citizen, AI Weekly, The Batch und The Sequence wurden auf aktuelle Erwähnungen geprüft. Nicht jede Quelle veröffentlichte im Wochenfenster einen frei zugänglichen Tool-Roundup. Deshalb stützt sich die Endauswahl auf nachprüfbare aktuelle Signale und wird pro Tool durch offizielle Anbieterquellen abgesichert. Verzeichnisse und Nutzerbewertungen dienen als Entdeckungssignal, nicht als alleiniger Beleg.

---

## Quellen

[1]: https://www.anthropic.com/claude-sonnet-5-5 "Anthropic: Introducing Claude Sonnet 5.5"
[2]: https://www.anthropic.com/pricing "Anthropic: Claude Pricing"
[3]: https://support.claude.com/en/articles/8325606-what-is-the-pro-plan "Claude Help Center: Pro Plan"
[4]: https://www.anthropic.com/privacy "Anthropic: Privacy Policy"
[5]: https://suno.com/blog/introducing-speech-beta "Suno: Introducing Speech (beta)"
[6]: https://suno.com/pricing "Suno: Pricing"
[7]: https://suno.com/privacy "Suno: Privacy Notice"
[8]: https://strandsagents.com/blog/introducing-strands-decider/ "Strands: Introducing Strands Decider 2B"
[9]: https://github.com/strands-labs/strands-decider "Strands Decider: offizielles GitHub-Repository"
[10]: https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19 "Strands Decider 2B: offizieller Modell-Checkpoint"
[11]: https://theresanaiforthat.com/ai/rabbitholes-ai/ "There's An AI For That: Slashspace 3.3"
[12]: https://www.slashspace.ai/ "Slashspace: Produkt- und Pricing-Seite"
[13]: https://www.slashspace.ai/privacy "Slashspace: Privacy Policy"
[14]: https://openai.com/index/introducing-dots/ "OpenAI: Introducing dots"
[15]: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot "OpenAI Help: Getting started with your dot"
[16]: https://openai.com/chatgpt/pricing/ "OpenAI: ChatGPT Pricing"
[17]: https://www.producthunt.com/products/dots-by-openai "Product Hunt: Dots by OpenAI"
[18]: https://openai.com/policies/privacy-policy/ "OpenAI: Privacy Policy"
[19]: https://www.eesel.ai/blog/openai-dots-pricing "Eesel: OpenAI Dots Pricing"
[20]: https://futuretools.io/ "FutureTools: aktuelle Tool- und Release-Signale"
[21]: https://aibreakfast.beehiiv.com/ "AI Breakfast: aktuelle Ausgaben"
[22]: https://www.bensbites.com/ "Ben's Bites: aktuelle Ausgaben"
[23]: https://newsletter.futurepedia.io/ "Futurepedia Newsletter: aktuelle Ausgaben"
[24]: https://www.producthunt.com/leaderboard/weekly/2026/40 "Product Hunt: Wochenrangliste KW 40"
[25]: https://www.toolify.ai/ "Toolify: aktuelle KI-Tools"
[26]: https://topai.tools/ "TopAI.tools: aktuelle Tool-Übersicht"
[27]: https://theaicitizen.com/ "The AI Citizen: öffentlicher Newsletter-Feed"
[28]: https://www.aiweekly.co/ "AI Weekly: aktuelle Ausgaben"
[29]: https://www.deeplearning.ai/the-batch/ "The Batch: aktuelle Ausgaben"
[30]: https://thesequence.substack.com/ "The Sequence: Newsletter"
