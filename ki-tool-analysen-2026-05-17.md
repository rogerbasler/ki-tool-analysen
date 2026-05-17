# Wöchentliche KI-Tool-Analyse, KW 20 / 2026

**Datum:** 17. Mai 2026  
**Autor:** Manus AI  
**Fokus:** Neue oder signifikant aktualisierte KI-Tools aus der letzten Woche  
**Kategorien:** Text, Design, Data / Wissen, Recherche, Agents

## Wochenzusammenfassung

Die interessanteste Entwicklung dieser Woche ist nicht, dass KI-Tools „mehr können“. Das eigentliche Problem ist nicht Funktionsfülle, sondern **Kontextfähigkeit**. Drei der fünf ausgewählten Tools versuchen, aus isolierten Prompts operative Systeme zu machen: Shadow während Meetings, Kanwas im Produktwissen und Mindra in agentischen Workflows. Was oft unterschätzt wird: Datenschutz wird zum Differenzierungsmerkmal. Aaavatar zeigt sehr sauber, wie local-first Design-Software aussehen kann, während AnySearch die Recherche-Infrastruktur für Agenten adressiert, aber noch mit offenen Fragen bei Pricing und Governance lebt.

| Kategorie | Tool | Kurzurteil | Relevanz |
|---|---|---|---:|
| Text | Shadow | Starker Schritt von Meeting-Notizen zu Echtzeit-Ausführung. | 8 |
| Design | Aaavatar | Local-first Headshot-Tool mit klarer Datenschutzlogik. | 8 |
| Data / Wissen | Kanwas | Kontext-Workspace für Teams und Agenten, besonders für Produktarbeit. | 8 |
| Recherche | AnySearch | API-Suchinfrastruktur für Agenten statt klassischer Websuche. | 7 |
| Agents | Mindra | Ambitionierte Multi-Agent-Orchestrierung für operative Workflows. | 8 |

## 1. Shadow

**Kategorie:** Text  
**URL:** [https://shadowlabs.ai](https://shadowlabs.ai)

### Kurzbeschreibung

Shadow ist ein Echtzeit-Assistent für Meetings und Sales-Calls. Das Tool positioniert sich nicht als weiterer Notizbot, sondern als System, das **während des Gesprächs** Aufgaben erkennt und erledigt. Die offizielle Website nennt Beispiele wie Dokumente erstellen, Daten abrufen, Follow-ups planen und sogar Slides bauen, während die Unterhaltung noch läuft.[1] Product Hunt beschreibt Shadow als „real-time AI wingman“ für High-Stakes-Calls und bestätigt Shadow 2.0 als #2 Product of the Day sowie #4 Product of the Week für den 6. Mai 2026.[2]

> „Shadow completes your to-dos before you finish the call.“  
> Quelle: Shadow Website[1]

### Nutzungsszenarien

| Szenario | Praktischer Nutzen |
|---|---|
| Sales-Calls | Shadow erkennt Zusagen, erstellt Follow-up-Entwürfe und kann CRM-Aktualisierungen vorbereiten. |
| Kundenmeetings | Recaps, nächste Schritte und Kalendereinladungen entstehen direkt aus dem Gespräch. |
| Gründer- und Investorencalls | Kritische Fragen, Faktenchecks und Gesprächsnotizen werden live unterstützt. |
| Interne Projektmeetings | Action Items werden während des Calls dokumentiert und anschlussfähig gemacht. |
| Mehrsprachige Teams | Shadow unterstützt laut Website über 60 Sprachen.[1] |

### Pricing

Die öffentliche Website bietet einen direkten Download der Mac-App und verweist in den FAQs auf eine Testmöglichkeit, zeigt aber keine vollständige Pricing-Seite mit Planvergleich.[1] Futurepedia klassifiziert Shadow als **Freemium**.[6] Für die Praxis bedeutet das: Es gibt offenbar einen niedrigen Einstieg, aber Budgetsicherheit für Teams ist erst nach direkter Prüfung im Produkt oder beim Anbieter möglich.

| Plan / Modell | Preis | Einschätzung |
|---|---:|---|
| Test / Freemium | Nicht öffentlich exakt ausgewiesen | Niedrige Einstiegshürde, aber unklarer Umfang. |
| Bezahlpläne | Nicht öffentlich ausgewiesen | Für Teamrollout vorab verifizieren. |

### Datenschutz

Die Privacy Policy wurde am 30. März 2026 aktualisiert. Shadow sammelt Google-Account-Daten, Calendar Events mit read-only Zugriff, Meeting-Transkripte, AI-generierte Inhalte und anonyme Nutzungsdaten.[3] Google User Data wird laut Policy nicht für Werbung, Verkauf an Dritte oder Training von AI-Modellen verwendet.[3] Daten werden verschlüsselt gespeichert und per HTTPS übertragen. Eine Löschung kann per E-Mail verlangt werden und soll innerhalb von 30 Tagen erfolgen.[3]

| Datenschutzpunkt | Befund |
|---|---|
| Serverstandort | Nicht öffentlich klar ausgewiesen. |
| DSGVO | Keine explizite DSGVO-Erklärung gefunden. |
| Training auf Nutzerdaten | Für Google User Data laut Policy ausgeschlossen. |
| Subprozessoren | Genannt, aber nicht im Detail aufgelistet. |
| Self-Hosting | Nicht gefunden. |

### Stärken

Shadow trifft einen wunden Punkt: Meeting-Tools haben jahrelang Zusammenfassungen geliefert, aber die operative Arbeit blieb bei Menschen hängen. Der entscheidende Unterschied liegt in der **Echtzeit-Ausführung**. Wenn Shadow zuverlässig To-dos, Kalender, CRM und Dokumente bedient, reduziert es nicht nur Schreibarbeit, sondern auch Kontextverlust nach Meetings.

### Schwächen

Die grösste Schwäche ist die noch dünne öffentliche Transparenz bei Pricing und Infrastruktur. Für Unternehmen ist ausserdem relevant, dass Meeting-Transkripte und AI-generierte Inhalte verarbeitet werden. Ohne klaren Serverstandort, Subprozessorenliste und DPA-Prüfung bleibt Shadow für regulierte Branchen ein Tool mit Prüfbedarf.

### Einschätzung für die Praxis

Für Sales, Recruiting, Beratung und Gründerteams ist Shadow sehr interessant. Besonders dort, wo Gesprächsqualität und Anschlussgeschwindigkeit über Umsatz entscheiden, kann das Tool echten Hebel haben. Für Enterprise-Setups gilt: Erst Datenschutz und Integrationen prüfen, dann Pilot starten. Wildes Installieren im Vertrieb wäre wieder einmal die schnellste Route zur Schatten-IT. Der Name wäre dann wenigstens ehrlich.

**Relevanzbewertung:** 8 / 10

## 2. Aaavatar

**Kategorie:** Design  
**URL:** [https://aaavatar.nl](https://aaavatar.nl)

### Kurzbeschreibung

Aaavatar ist eine macOS-App für konsistente Team-Portraits. Das Tool entfernt Hintergründe automatisch, erlaubt Brand-Farben oder eigene Hintergründe, retuschiert Portraits in einem Klick, richtet Gesichter aus und exportiert Bilder für LinkedIn, Slack, E-Mail und weitere Kanäle.[4] Die App wird von Square One aus den Niederlanden veröffentlicht.[5]

### Nutzungsszenarien

| Szenario | Praktischer Nutzen |
|---|---|
| Teamseite | Uneinheitliche Mitarbeitendenfotos werden in eine konsistente visuelle Sprache gebracht. |
| LinkedIn-Profile | Portraits lassen sich markenkonform und schnell für Social Profiles aufbereiten. |
| Pitch Decks | Gründer- und Teamfotos wirken professioneller, ohne Fotoshooting. |
| Onboarding | Neue Mitarbeitende können schnell in ein bestehendes Portraitsystem integriert werden. |
| Agentur- und Beratungsteams | Einheitlicher Auftritt über Website, Signaturen und Plattformen. |

### Pricing

Die Website zeigt einen direkten Mac-Download über GitHub und keine sichtbare Pricing-Seite.[4] Futurepedia nennt Aaavatar als Freemium.[6] Für die aktuelle Praxis ist relevant: Das Tool wirkt derzeit wie ein kostenloser oder sehr niedrigschwelliger Mac-Download. Ein verbindlicher Planvergleich wurde nicht gefunden.

| Plan / Modell | Preis | Einschätzung |
|---|---:|---|
| Mac-App Download | Öffentlich ohne Preisbarriere sichtbar | Für Tests sehr zugänglich. |
| Bezahlpläne | Nicht öffentlich ausgewiesen | Noch keine Budgettransparenz. |

### Datenschutz

Aaavatar ist datenschutzseitig das sauberste Tool dieser Woche. Laut Privacy Policy ist die App **local-first**, betreibt kein Backend und sammelt keine Daten auf Servern von Square One.[5] Portraits und Hintergründe bleiben lokal auf dem Mac, ausser Nutzer aktivieren freiwillig einen geteilten Workspace in Google Drive.[5] In diesem Fall liegen Dateien im eigenen Google Drive der Nutzer und werden über Google APIs synchronisiert. OAuth-Tokens bleiben in der macOS Keychain.[5]

| Datenschutzpunkt | Befund |
|---|---|
| Anbieterstandort | Square One, Niederlande.[5] |
| Serverstandort | Kein eigenes Backend laut Policy. |
| DSGVO | Starke EU-Nähe durch Anbieterstandort und local-first Ansatz, aber keine explizite vollständige DSGVO-Zertifizierung. |
| Self-Hosting | Nicht nötig, da local-first, kein Backend. |
| Drittanbieter | Optional Google Drive, Sparkle-Update-Framework über GitHub.[5] |

### Stärken

Aaavatar löst ein sehr konkretes Problem: Corporate Portraits sind oft eine wilde Ausstellung persönlicher Lichtverhältnisse, Kamerawinkel und Hintergrundentscheidungen. Aaavatar standardisiert dieses Chaos schnell und ohne schwere Designprozesse. Was oft unterschätzt wird: Der local-first Ansatz reduziert Risiko, weil biometrisch sensible Bilddaten nicht automatisch an einen Headshot-Cloudanbieter gehen.

### Schwächen

Die App ist aktuell auf macOS beschränkt. Pricing ist nicht transparent, und der optionale Google-Drive-Scope ist technisch breit, auch wenn die Policy die Nutzung klar auf Avatar-Workspaces begrenzt. Für grössere Unternehmen fehlen sichtbare Admin-, Audit- und Rollout-Funktionen.

### Einschätzung für die Praxis

Für kleine Teams, Agenturen, HR und Personal Brands ist Aaavatar sehr empfehlenswert. Es ist kein „AI Magic“-Spielzeug, sondern ein konkretes Design-Werkzeug mit guter Datenschutzarchitektur. Besonders für europäische Teams ist das ein Vorteil. Die Konsequenz daraus ist: Für standardisierte Teamkommunikation kann Aaavatar mehr bringen als der nächste grosse generative Bildgenerator mit dramatischem Namen und Datenschutznebelmaschine.

**Relevanzbewertung:** 8 / 10

## 3. Kanwas

**Kategorie:** Data / Wissen  
**URL:** [https://kanwas.ai](https://kanwas.ai)

### Kurzbeschreibung

Kanwas ist ein gemeinsamer Kontext-Workspace für Teams und Agenten. Die Plattform bündelt Produktwissen, Research, Entscheidungen und Daten in einem bearbeitbaren Arbeitsraum, der sowohl Menschen als auch AI-Agenten zugänglich ist.[7] Die Website positioniert Kanwas als Alternative zum Zerfasern von Kontext über Claude-Chats, lokale Ordner, Obsidian, VS Code, Git und Docs.[7]

Product Hunt beschreibt Kanwas als „open-source brain for your team“, nennt 1.7K Follower, ein Free-Label, ein 5.0 Rating bei 1 Review, #1 Day Rank und 506 Punkte.[8] Das GitHub-Repository wurde am 22. April 2026 erstellt, hatte zum Prüfzeitpunkt 655 Stars und wurde am 16. Mai 2026 aktualisiert.[9]

### Nutzungsszenarien

| Szenario | Praktischer Nutzen |
|---|---|
| Produktstrategie | Entscheidungen, Annahmen, PRDs und Research bleiben verbunden statt verstreut. |
| Wettbewerbsanalyse | Agenten können auf historisches Research und neue Inputs zugreifen. |
| Roadmap-Arbeit | Trade-offs und technische Constraints werden nachvollziehbarer. |
| GTM-Planung | Positionierung, Kundensegmente und Marktdaten können in einem Kontextgraphen verdichtet werden. |
| Teamübergaben | Wissen bleibt im Workspace und verschwindet nicht in Chatverläufen. |

### Pricing

Product Hunt markiert Kanwas als **Free**.[8] Futurepedia nennt Freemium.[6] Die Homepage zeigt keinen vollständigen Planvergleich. Für Teams ist deshalb unklar, welche Limits, Hostingmodelle oder Enterprise-Funktionen später kostenpflichtig werden.

| Plan / Modell | Preis | Einschätzung |
|---|---:|---|
| Free | Auf Product Hunt sichtbar | Sehr attraktiv für Tests und kleine Teams. |
| Freemium / spätere Pläne | Nicht öffentlich klar ausgewiesen | Für produktive Teamnutzung prüfen. |

### Datenschutz

Auf der Homepage war keine Privacy Policy prominent auffindbar. Das GitHub-Repository ist öffentlich, die Lizenz wird von GitHub jedoch als „Other“ angezeigt.[9] Das ist wichtig: „Open-source brain“ im Marketing heisst nicht automatisch klassische Open-Source-Lizenz mit klaren Nutzungsrechten. Serverstandort, DPA, Subprozessoren und DSGVO-Status konnten öffentlich nicht vollständig verifiziert werden.

| Datenschutzpunkt | Befund |
|---|---|
| Serverstandort | Nicht gefunden. |
| DSGVO | Nicht verifiziert. |
| Self-Hosting | Durch GitHub-Nähe möglich zu prüfen, aber nicht sauber bestätigt. |
| Lizenz | GitHub zeigt „Other“, daher Vorsicht bei Open-Source-Interpretation.[9] |
| Datenrisiko | Hochrelevanter Produktkontext, deshalb Governance nötig. |

### Stärken

Kanwas greift ein Kernproblem moderner KI-Arbeit auf: Modelle können vieles erzeugen, aber sie scheitern oft an **organisiertem Kontext**. Der Workspace-Ansatz ist stark, weil produktbezogene Entscheidungen, Research und Trade-offs nicht in Chatfenstern sterben. Für Produktteams ist das relevant, weil gute Strategie selten aus einem Prompt entsteht, sondern aus akkumuliertem Kontext plus Urteilsvermögen.

### Schwächen

Die Schwäche liegt in der Reife und Transparenz. Datenschutz, Hosting, Lizenz und Pricing sind noch nicht ausreichend klar. Für Teams mit sensiblen Produkt-, Kunden- oder Marktdaten ist das kein Detail, sondern die Eintrittskarte. Ohne klare Governance wird aus dem „Team Brain“ schnell eine sehr hübsche Blackbox für interne Strategieinformationen.

### Einschätzung für die Praxis

Kanwas ist ein sehr spannendes Werkzeug für Produktteams, Founder und kleine Growth-Teams. Es eignet sich besonders für Teams, die bereits intensiv mit AI-Agenten, Research und Produktdokumentation arbeiten. Für Enterprise-Kontexte würde ich Kanwas zuerst mit nicht-sensiblen Projektdaten testen und parallel Datenschutz, Lizenz und Exportfähigkeit prüfen.

**Relevanzbewertung:** 8 / 10

## 4. AnySearch

**Kategorie:** Recherche  
**URL:** [https://www.anysearch.com/home](https://www.anysearch.com/home)

### Kurzbeschreibung

AnySearch ist eine Suchinfrastruktur für KI-Agenten und Enterprise-Systeme. Laut Dokumentation stellt AnySearch eine Search API unter `https://api.anysearch.com` bereit und unterstützt sowohl anonyme Requests mit täglichem Free-Kontingent als auch authentifizierte Requests mit API Key und bezahltem Kontingent.[10] Eine unabhängige Quelle beschreibt AnySearch als einheitliche API für vertikale und authentifizierte Datenquellen, darunter Finance, Legal, akademische Repositories, Code-Hosts und strukturierte APIs.[11]

### Nutzungsszenarien

| Szenario | Praktischer Nutzen |
|---|---|
| Agenten-Recherche | AI-Agenten erhalten strukturiertere Suchergebnisse statt nur Public-Web-Snippets. |
| Entwicklerprodukte | Eine API kann verschiedene Such- und Datenquellen abstrahieren. |
| Fachrecherche | Legal-, Finance- oder Academic-Quellen lassen sich perspektivisch integrieren. |
| Knowledge-Workflows | Rechercheergebnisse können in Agentenketten oder interne Tools eingebunden werden. |
| Prototyping | Das anonyme Free-Kontingent erleichtert schnelle Tests ohne sofortige API-Key-Pflicht. |

### Pricing

Die Dokumentation bestätigt zwei Modi: anonym ohne Authorization Header, limitiert pro Client-IP und gegen ein tägliches Free-Kontingent, sowie authentifiziert mit Bearer API Key, bezahltem Kontingent und höheren Concurrency Limits.[10] Eine externe Quelle nennt 1'000 kostenlose API-Calls pro Tag.[11] Ein vollständiger öffentlicher Planvergleich wurde nicht gefunden.

| Plan / Modell | Preis | Einschätzung |
|---|---:|---|
| Anonymous Free Quota | Laut externer Quelle 1'000 API-Calls pro Tag | Gut für Tests und Prototyping. |
| Authenticated / Paid Quota | Preis nicht öffentlich klar ausgewiesen | Für produktive Nutzung muss Pricing geprüft werden. |

### Datenschutz

Die externe Quelle verweist auf Privacy-Claims wie „no tracking, no telemetry, no logging“.[11] Die Dokumentation verlinkt Privacy, Terms und Cookie Policy, aber im extrahierten Inhalt waren keine vollständigen Datenschutzdetails sichtbar.[10] Serverstandort, Subprozessoren, DSGVO-Status und Löschkonzept sind daher nicht ausreichend verifiziert.

| Datenschutzpunkt | Befund |
|---|---|
| Serverstandort | Nicht verifiziert. |
| DSGVO | Nicht verifiziert. |
| Logging | Claim: no tracking, no telemetry, no logging.[11] |
| Self-Hosting | Nicht gefunden. |
| Hauptrisiko | Suchanfragen können sensible Absichten, Quellen und Geschäftskontexte enthalten. |

### Stärken

AnySearch adressiert ein unterschätztes Infrastrukturproblem: Agenten sind nur so gut wie ihre Informationszugänge. Klassische Websuche liefert oft unvollständige oder schlecht strukturierte Resultate. Eine API, die Quellen aggregiert, dedupliziert und in agententaugliche Form bringt, kann Recherche-Workflows massiv verbessern.

### Schwächen

Der Anspruch ist gross, die öffentliche Transparenz noch begrenzt. Pricing, Datenschutzdetails und reale Provider-Abdeckung müssen vor produktiver Nutzung geprüft werden. Auch Benchmarks aus Anbieterumfeld sind nützlich, aber kein Ersatz für eigene Tests mit relevanten Suchaufgaben.

### Einschätzung für die Praxis

AnySearch ist für Entwickler, AI-Produktteams und Research-Agenten interessant. Für klassische Endnutzer ist es eher Infrastruktur als fertiges Tool. Für Roger-relevante Workflows liegt der Nutzen dort, wo eigene Agenten bessere Quellenarbeit leisten sollen. Die Konsequenz daraus ist: AnySearch ist kein hübsches Interface, sondern eher ein Rohrsystem. Und bei Rohrsystemen merkt man erst beim Wasserschaden, ob jemand Governance ernst genommen hat.

**Relevanzbewertung:** 7 / 10

## 5. Mindra

**Kategorie:** Agents  
**URL:** [https://mindra.co](https://mindra.co)

### Kurzbeschreibung

Mindra ist ein Orchestrator für spezialisierte Agententeams. Nutzer beschreiben eine Aufgabe in natürlicher Sprache, Mindra erstellt daraus ein Team spezialisierter Agenten, das rund um die Uhr arbeitet, intern kommuniziert und Aktionen über bestehende Tools ausführt.[12] Die Website nennt Use Cases in Performance Marketing, Supply Chain Ops, GTM / Sales Ops und Product Intelligence.[12] Product Hunt bestätigt #1 Day Rank und 369 Punkte.[13]

### Nutzungsszenarien

| Szenario | Praktischer Nutzen |
|---|---|
| Performance Marketing | Google- und Meta-Ads-Ausgaben auditieren und verschwendetes Budget markieren. |
| Support Ops | Eingehende Support-E-Mails nach Dringlichkeit triagieren und routen. |
| Sales Ops | Inbound-Leads mit Unternehmenskontext anreichern, bevor sie in den Vertrieb gehen. |
| Supply Chain | Operative Signale überwachen und Workflows anstossen. |
| Product Intelligence | Markt- und Produktinformationen in wiederkehrende Agentenprozesse einbinden. |

### Pricing

Mindra setzt sichtbar auf **Book a Demo** und Contact-for-pricing.[12] Eine öffentliche Preisliste oder ein Free Tier wurden nicht gefunden. Product Hunt markiert „Payment Required“.[13]

| Plan / Modell | Preis | Einschätzung |
|---|---:|---|
| Demo / Sales-led | Nicht öffentlich | Für mittlere und grössere Teams. |
| Free Tier | Nicht gefunden | Einstiegshürde höher als bei Self-serve-Tools. |
| Enterprise | Vermutlich Custom Pricing | Vor allem für operative Teams mit klaren Workflows. |

### Datenschutz

Die Privacy Policy wurde am 14. Mai 2026 aktualisiert. Mindra sammelt Account-Informationen, Zahlungsinformationen über Drittanbieter, API-Nutzungsdaten, Agent-Konfigurationen, Transaction Logs und Performance Metrics.[14] Daten werden laut Policy in transit und at rest verschlüsselt, mit Access Controls und regelmässigen Security Audits geschützt.[14] Die Website zeigt GDPR-Compliant-, ZDR-Enterprise-Security- und SOC-2-Type-II-in-Progress-Badges.[12]

| Datenschutzpunkt | Befund |
|---|---|
| Serverstandort | Nicht öffentlich klar ausgewiesen. |
| DSGVO | GDPR-Compliant-Badge sichtbar, Details nicht vollständig in Policy ausgeführt.[12] |
| SOC 2 | Type II Compliance in Progress.[12] |
| Self-Hosting | Nicht gefunden. |
| Datenrisiko | Hoch, weil Agenten operative Systeme und Logs berühren. |

### Stärken

Mindra macht den nächsten logischen Schritt: Weg vom einzelnen Agenten, hin zu **koordinierten Agententeams**. Der Ansatz ist plausibel, weil operative Arbeit selten eindimensional ist. Ein Marketing-Audit braucht Datenzugriff, Analyse, Priorisierung, Kommunikation und manchmal Ausführung. Genau hier kann Multi-Agent-Orchestrierung sinnvoll sein.

### Schwächen

Das Tool ist eindeutig anspruchsvoller als ein klassisches SaaS-Produkt. Je mehr ein Agent ausführt, desto wichtiger werden Rechte, Audit Logs, Freigaben, Rollbacks und Verantwortlichkeiten. Die Privacy Policy ist vergleichsweise kurz und lässt Fragen zu Subprozessoren, Datenresidenz und internationalen Transfers offen. Ausgerechnet bei Agenten ist das kein Nebenschauplatz, sondern Betriebshaftung mit schöner UI.

### Einschätzung für die Praxis

Mindra ist für Teams spannend, die wiederkehrende operative Prozesse mit klar messbaren Outputs haben. Für KMU ist der Nutzen hoch, wenn die Daten sauber angebunden sind und Freigaben gut geregelt werden. Für unstrukturierte „macht mal alles automatisch“-Fantasien ist Mindra ungeeignet. Agents sind keine Praktikanten mit WLAN, sondern Systeme, die Führung, Grenzen und Messgrössen brauchen.

**Relevanzbewertung:** 8 / 10

## Quellenlage und Auswahlbegründung

Die Shortlist wurde aus aktuellen Tool-Roundups und Verzeichnissen abgeleitet. Futurepedia nannte Shadow, Kanwas, Mindra, Aaavatar und Gyro Autopilot als neue Tools der Woche.[6] Ben's Bites und There's An AI For That zeigten zusätzliche Signale für Agenten, Notion als Agent-Hub, Daybreak und Browser-Agenten, lieferten aber für die finalen fünf Kategorien nicht immer sauber prüfbare Endnutzer-Tools.[15] [16] PLANADVISER bestätigte den breiteren Trend zu agentischen Enterprise-Workflows, etwa bei Broadridge, Allvue/RSM und EmotionShield AI.[17]

| Qualitätskriterium | Status |
|---|---|
| Preise verifiziert | Teilweise. Vollständig bei keinem Tool, da mehrere Anbieter keine öffentliche Planseite zeigen. |
| Datenschutz vollständig | Gut bei Aaavatar und Shadow, mittel bei Mindra, schwach bis mittel bei Kanwas und AnySearch. |
| Links geprüft | Ja, alle Hauptlinks wurden geöffnet oder über Quellen validiert. |
| Reviews geprüft | Product Hunt für Shadow, Kanwas und Mindra; kaum formale Reviews bei neuen Tools. |
| Schweizer Schreibweise | Ja, inklusive „ss“ statt „ß“ und Umlauten. |

## References

[1]: https://shadowlabs.ai/ "Shadow, offizielle Website"  
[2]: https://www.producthunt.com/products/shadow-6 "Shadow auf Product Hunt"  
[3]: https://shadowlabs.ai/privacy "Shadow Privacy Policy"  
[4]: https://aaavatar.nl/ "Aaavatar, offizielle Website"  
[5]: https://aaavatar.nl/privacy-policy "Aaavatar Privacy Policy"  
[6]: https://www.linkedin.com/posts/futurepedia_5-ai-tools-released-over-the-past-week-worth-activity-7460449060404006912-4xQT "Futurepedia: 5 AI Tools released over the past week"  
[7]: https://kanwas.ai/ "Kanwas, offizielle Website"  
[8]: https://www.producthunt.com/products/kanwas "Kanwas auf Product Hunt"  
[9]: https://github.com/kanwas-ai/kanwas "Kanwas GitHub Repository"  
[10]: https://www.anysearch.com/docs "AnySearch API Documentation"  
[11]: https://letsdatascience.com/news/anysearch-launches-search-infrastructure-for-ai-agents-a94ba119 "AnySearch Launches Search Infrastructure for AI Agents"  
[12]: https://mindra.co/ "Mindra, offizielle Website"  
[13]: https://www.producthunt.com/products/mindra "Mindra auf Product Hunt"  
[14]: https://mindra.co/legal/privacy "Mindra Privacy Policy"  
[15]: https://www.bensbites.com/p/agents-feedback-tip "Ben's Bites: Agents feedback tip"  
[16]: https://newsletter.theresanaiforthat.com/archive "There's An AI For That Newsletter Archive"  
[17]: https://www.planadviser.com/ai-product-service-launches-5-11-2026/ "PLANADVISER: AI Product & Service Launches, 5/11/2026"
