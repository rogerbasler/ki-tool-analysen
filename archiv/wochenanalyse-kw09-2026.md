# KI-Tool-Analysen — KW 09/2026
**Datum:** 1. März 2026 | **Analysiert von:** KI-Tool-Research-Agent

---

## Wöchentliche Zusammenfassung

KW 09/2026 markiert eine Zäsur in der KI-Entwicklung: Geschwindigkeit, Zugänglichkeit und Orchestrierung stehen im Mittelpunkt. Das herausragendste Ereignis war der Launch von **Mercury 2** durch Inception Labs — das erste Diffusion-basierte Reasoning-Modell der Welt, das mit über 1.000 Token pro Sekunde eine völlig neue Geschwindigkeitsdimension eröffnet. Gleichzeitig betrat **QuiverAI** mit Arrow-1 die Bühne: das erste dedizierte KI-Modell für Vektorgrafiken, das sofort die Spitze des SVG Arena-Leaderboards erklomm und $8,3 Millionen von a16z einsammelte. **Perplexity Computer** redefiniert den Begriff des KI-Agenten, indem es 19 verschiedene Modelle zu einem einzigen, autonomen Workflow-System orchestriert. **Notion Custom Agents** bringt 24/7-KI-Automatisierung direkt in den meistgenutzten Workspace der Welt — ohne Programmierkenntnisse. Und **Supaboard** beweist, dass Datenanalyse kein Expertenwissen mehr erfordert, wenn man einfach auf Englisch fragen kann.

---

## Tool 1: Mercury 2 (Inception Labs)

### Kategorie: TEXT

### Kurzbeschreibung
Mercury 2 ist das weltweit schnellste Reasoning-Sprachmodell, entwickelt von Inception Labs (Stanford-Ausgründung). Im Gegensatz zu herkömmlichen autogressiven Modellen, die Text Token für Token generieren, nutzt Mercury 2 eine **Diffusion-basierte Architektur**: Es verfeinert ganze Textpassagen parallel — ähnlich wie ein Lektor, der einen vollständigen Entwurf auf einmal überarbeitet. Das Ergebnis ist eine Generierungsgeschwindigkeit von über **1.009 Token pro Sekunde** auf NVIDIA Blackwell GPUs — mehr als 5x schneller als vergleichbare Speed-optimierte Modelle. Zielgruppe sind Entwickler, Unternehmen und alle, die KI in latenzempfindlichen Produktionsumgebungen einsetzen: Agenten-Loops, Echtzeit-Voice-Interfaces, Code-Autocomplete und RAG-Pipelines.

### Nutzungsszenarien
1. **Echtzeit-Code-Autocomplete:** Entwickler erhalten Vorschläge, die schnell genug sind, um den eigenen Denkfluss nicht zu unterbrechen — Mercury 2 fühlt sich an wie eine Erweiterung des eigenen Denkens, nicht wie ein Warteprozess.
2. **Agentenbasierte Workflows:** In mehrstufigen Agenten-Loops, wo Dutzende von Inferenz-Aufrufen pro Aufgabe anfallen, reduziert Mercury 2 die Gesamtlatenz dramatisch und ermöglicht komplexere, qualitativ bessere Ergebnisse.
3. **Voice-AI-Interfaces:** Sprachassistenten haben das engste Latenz-Budget aller KI-Anwendungen. Mercury 2 macht Reasoning-Qualität innerhalb natürlicher Sprachkadenz möglich.
4. **Echtzeit-Transkription und -Bereinigung:** Für Tools wie Wispr Flow, die Live-Transkripte bereinigen müssen, ist die Geschwindigkeit ein entscheidender Faktor.
5. **Multi-Hop-RAG-Pipelines:** Retrieval, Reranking und Zusammenfassung stapeln sich schnell — Mercury 2 erlaubt es, Reasoning in den Suchloop einzubauen, ohne das Latenz-Budget zu sprengen.

### Pricing
| Plan | Preis | Details |
|------|-------|---------|
| API (Input) | $0.25 / 1M Token | 4x günstiger als Claude Haiku |
| API (Output) | $0.75 / 1M Token | 4x günstiger als Claude Haiku |
| Chat (Mercury Chat) | Kostenlos | Zugang über mercury.inception.ai |
| Enterprise | Auf Anfrage | Dedizierte Kapazität, SLA, Workload-Optimierung |

**Vergleich:** GPT-5.2 kostet ca. $0.50/$1.50 pro 1M Token bei deutlich niedrigerer Geschwindigkeit. Gemini 3 Flash liegt bei $0.50/$1.50. Mercury 2 ist damit das günstigste und schnellste Reasoning-Modell auf dem Markt.

### Datenschutz
- **Unternehmensstandort:** USA (Inception Labs, Inc., Stanford-Ausgründung)
- **Serverstandort:** USA (primär NVIDIA Blackwell GPU-Cluster)
- **DSGVO:** Keine explizite DSGVO-Zertifizierung oder EU-Serverstandort kommuniziert. Privacy Policy vorhanden, aber keine SCCs oder DPA öffentlich dokumentiert.
- **Datenverwendung:** Keine öffentliche Aussage zu Training auf Nutzerdaten
- **Self-Hosting:** Nicht verfügbar (Cloud-only API)
- **Datenschutz-Bewertung: 5/10** — US-Unternehmen ohne klare DSGVO-Dokumentation; für europäische Unternehmen mit Compliance-Anforderungen kritisch zu prüfen

### Stärken
- Revolutionäre Diffusion-Architektur: erste ihrer Art für Reasoning-Modelle
- Überlegene Geschwindigkeit: 1.009 Token/Sek vs. <200 bei Konkurrenten
- Sehr günstige API-Preise: 4x günstiger als Claude Haiku
- OpenAI API-kompatibel: Drop-in-Replacement ohne Code-Änderungen
- 128K Kontextfenster, native Tool-Use, JSON-Schema-Output
- Tunable Reasoning: Qualitäts-Geschwindigkeits-Tradeoff steuerbar

### Schwächen
- Noch kein EU-Serverstandort oder DSGVO-Dokumentation
- Qualität bei komplexen Reasoning-Aufgaben noch hinter GPT-5.2 und Claude Sonnet 4.6
- Kein Self-Hosting oder On-Premise-Option
- Noch keine breite Community oder Ökosystem-Integration
- Early Access für Mercury 2 — noch nicht für alle verfügbar

### Einschätzung für die Praxis
Mercury 2 ist ein technologischer Durchbruch, der die Grundannahme des KI-Feldes — sequentielle Token-Generierung — in Frage stellt. Für Entwickler, die latenzempfindliche Anwendungen bauen (Voice-AI, Code-Tools, Agenten-Loops), ist Mercury 2 bereits heute ein ernstzunehmender Kandidat. Die API-Preise sind unschlagbar. Der Hauptvorbehalt für europäische Nutzer ist die fehlende DSGVO-Dokumentation. Für Nicht-Compliance-kritische Anwendungen: sofort ausprobieren.

### Relevanzbewertung: **9/10**
*Technologischer Durchbruch mit sofortiger Praxisrelevanz. Einziger Abzug: fehlende DSGVO-Dokumentation und noch nicht GA für alle.*

---

## Tool 2: QuiverAI (Arrow-1)

### Kategorie: DESIGN

### Kurzbeschreibung
QuiverAI ist ein neues KI-Labor und Produktunternehmen, das sich auf **Vektorgrafik-Design** spezialisiert hat. Ihr erstes Modell, **Arrow-1**, ist das weltweit erste dedizierte KI-Modell für die Generierung von SVG-Vektorgrafiken aus Text-Prompts und Referenzbildern. Anders als Bildgeneratoren wie Midjourney oder DALL-E, die Pixel-Bilder erzeugen, generiert Arrow-1 echte, editierbare SVG-Dateien — strukturierten Code, der sich verlustfrei skalieren, in jedem Vektorprogramm bearbeiten und direkt in Produktionscode integrieren lässt. Das Unternehmen wurde von Pascal Wichmann (PhD-Arbeit zu Vektorgrafiken) gegründet und hat $8,3 Millionen Seed-Kapital von Andreessen Horowitz (a16z) erhalten. Arrow-1 belegt bereits **Platz 1 auf dem SVG Arena Leaderboard** mit einem Elo von 1583 — das erste Modell, das je die 1500-Marke überschritten hat.

### Nutzungsszenarien
1. **Logo-Generierung:** Marken und Designer können skalierbare, editierbare Logos aus Text-Beschreibungen oder Referenzbildern generieren — ohne Illustrator-Kenntnisse.
2. **Icon-Sets:** Entwickler und Produktteams erstellen konsistente Icon-Bibliotheken für Apps und Websites direkt aus Prompts.
3. **Illustrationen für Marketing:** Vollständig vektorielle Illustrationen für Landing Pages, Präsentationen oder Social Media — editierbar in Figma, Illustrator oder direkt im Code.
4. **UI-Komponenten:** Frontend-Entwickler generieren SVG-Elemente wie Buttons, Badges oder Dekorationselemente direkt als produktionsreifen Code.
5. **Brand-Asset-Erstellung:** Startups und KMUs erstellen ihre gesamte visuelle Identität (Logo, Icons, Illustrationen) ohne Designagentur.

### Pricing
| Plan | Preis | Details |
|------|-------|---------|
| Public Beta | Kostenlos | Vollzugang zu Arrow-1 während der Beta-Phase |
| API | Auf Anfrage | Für Entwickler und Enterprise-Kunden |
| Zukünftige Pläne | Noch nicht kommuniziert | Preismodell nach Beta noch offen |

**Hinweis:** QuiverAI befindet sich in der öffentlichen Beta-Phase. Die Nutzung ist derzeit kostenlos. Ein Preismodell nach der Beta-Phase wurde noch nicht kommuniziert.

### Datenschutz
- **Unternehmensstandort:** USA (QuiverAI, Inc.)
- **Serverstandort:** USA
- **DSGVO:** Privacy Policy vorhanden (app.quiver.ai), aber keine spezifischen DSGVO-Zertifizierungen oder EU-Serverstandorte kommuniziert
- **Datenverwendung:** Beta-Phase — Nutzungsdaten werden wahrscheinlich für Modell-Verbesserungen verwendet
- **Self-Hosting:** Nicht verfügbar
- **Datenschutz-Bewertung: 5/10** — Junges US-Startup in Beta-Phase; Datenschutz-Dokumentation noch minimal

### Stärken
- Erstes dediziertes KI-Modell für Vektorgrafiken weltweit
- Platz 1 auf SVG Arena Leaderboard (Elo 1583, erstmals über 1500)
- Generiert echte, editierbare SVG-Dateien — kein Pixel-Raster
- Direkte Integration in Figma, Illustrator, Code-Workflows
- Starke Investoren-Unterstützung (a16z, $8,3M Seed)
- Kostenlos in der Public Beta

### Schwächen
- Noch in der Beta-Phase — Qualität und Konsistenz variieren
- Kein Support für fotorealistische Bilder (SVG-Limitation)
- Pricing nach Beta noch unklar
- Keine DSGVO-Dokumentation oder EU-Serverstandort
- Noch keine Animations- und Typografie-Features (angekündigt)
- Kleines Team, noch kein etabliertes Ökosystem

### Einschätzung für die Praxis
QuiverAI löst ein echtes Problem: KI-Bildgeneratoren erzeugen Pixel, aber Designer und Entwickler brauchen Vektoren. Arrow-1 ist der erste ernstzunehmende Ansatz, dieses Problem zu lösen. Für Logos, Icons und einfache Illustrationen ist es bereits heute beeindruckend. Wer regelmäßig SVG-Assets erstellt, sollte die kostenlose Beta unbedingt testen. Das a16z-Investment signalisiert hohes Vertrauen in die Technologie.

### Relevanzbewertung: **8.5/10**
*Pionierleistung in einer wichtigen Nische. Beta-Status und fehlende Datenschutz-Dokumentation sind die einzigen Vorbehalte.*

---

## Tool 3: Supaboard

### Kategorie: DATA / WISSEN

### Kurzbeschreibung
Supaboard ist eine **KI-gestützte Echtzeit-Analyseplattform**, die es ermöglicht, Geschäftsdaten auf Englisch zu befragen und sofort präzise Antworten, Dashboards und Berichte zu erhalten — ohne SQL-Kenntnisse oder Data-Science-Hintergrund. Die Plattform verbindet sich mit über 600 Datenquellen (Google Analytics, Stripe, PostgreSQL, Salesforce u.v.m.) und setzt KI-Agenten ein, um natürlichsprachliche Fragen in präzise Datenbankabfragen zu übersetzen. Supaboard wurde im Februar 2026 auf Product Hunt gelauncht und erreichte dort **Platz 1** für den Monat Februar 2026 mit 728 Upvotes. Zielgruppe sind Gründer, Marketing-Teams, Product Manager und Revenue-Teams, die schnell Daten-Insights brauchen, ohne auf Data Engineers warten zu müssen.

### Nutzungsszenarien
1. **Marketing-Performance:** Ein Marketing-Manager fragt: "Welcher Kanal hat im letzten Quartal die meisten qualifizierten Leads gebracht?" — Supaboard analysiert Google Analytics, CRM und Ad-Daten und liefert eine klare Antwort mit Visualisierung.
2. **Revenue-Analyse:** Ein Gründer fragt: "Wie entwickelt sich unser MRR nach Kundensegment?" — Supaboard verbindet Stripe-Daten mit dem CRM und erstellt automatisch ein Dashboard.
3. **Risiko-Monitoring:** Ein Produktteam fragt: "Welche Risiken sehen wir für das nächste Quartal?" — Supaboard analysiert historische Trends und identifiziert Anomalien.
4. **Automatisierte Reports:** Wöchentliche KPI-Reports werden automatisch generiert und per Slack oder E-Mail versendet (Feature in Entwicklung).
5. **Ad-hoc-Datenexploration:** Statt auf einen Data Analyst zu warten, können Business-Nutzer selbst Fragen stellen und Zusammenhänge erkunden.

### Pricing
| Plan | Preis (monatlich) | Preis (jährlich) | Details |
|------|-------------------|------------------|---------|
| Individual | $85/Monat | $71/Monat | 1 Nutzer, Default Agent, Advanced AI, Unlimited Dashboards |
| Business (Popular) | $229/Monat | $191/Monat | Mehrere Nutzer, Custom Agents, Slack/Teams-Integration |
| Enterprise | Auf Anfrage | Auf Anfrage | Unlimited Nutzer, White-Labelling, Dedicated Support |

**Kein Free Tier** — nur kostenlose Testphase (Dauer nicht kommuniziert). Für Einzelnutzer und kleine Teams ist der Einstiegspreis von $71-85/Monat vergleichsweise hoch.

### Datenschutz
- **Unternehmensstandort:** USA (Supaboard, Inc.)
- **Serverstandort:** USA (primär), Deployment-Region wählbar im Enterprise-Plan
- **DSGVO:** SOC2-Report verfügbar (im Enterprise-Plan), HIPAA BAA verfügbar. Keine explizite DSGVO-Zertifizierung kommuniziert.
- **Datenverwendung:** Daten werden für die Analyse verwendet, nicht für Modell-Training (laut Privacy Policy)
- **Self-Hosting:** Nicht verfügbar in Standard-Plänen; Enterprise-Plan mit Custom Deployment Region
- **Datenschutz-Bewertung: 6/10** — SOC2 und HIPAA sind positiv, aber kein EU-Serverstandort und keine explizite DSGVO-Zertifizierung

### Stärken
- Platz 1 auf Product Hunt Februar 2026 — starke Community-Validierung
- 600+ Datenquellen-Integrationen
- Keine SQL- oder Programmierkenntnisse erforderlich
- KI-Agenten für spezifische Business-Rollen (Marketing, Revenue, Product)
- Saubere, intuitive Benutzeroberfläche
- SOC2 und HIPAA verfügbar (Enterprise)

### Schwächen
- Kein Free Tier — hohe Einstiegshürde für Einzelnutzer
- US-Unternehmen ohne klare DSGVO-Dokumentation
- Kein Self-Hosting in Standard-Plänen
- Scheduled Reports und Alerting noch "Coming in Feb" (nicht live)
- Junges Unternehmen — Langzeit-Stabilität noch nicht bewiesen
- Konkurrenz von etablierten Tools wie Tableau, Power BI und Metabase

### Einschätzung für die Praxis
Supaboard adressiert einen realen Schmerz: Business-Teams warten zu lange auf Daten-Insights, weil sie von Data Engineers abhängig sind. Die natürlichsprachliche Schnittstelle ist intuitiv und die 600+ Integrationen sind beeindruckend. Für Teams, die bereit sind, $71-229/Monat zu investieren, und deren Daten in US-Cloud-Diensten liegen, ist Supaboard ein starker Kandidat. Für DSGVO-kritische europäische Unternehmen ist Vorsicht geboten.

### Relevanzbewertung: **8.0/10**
*Starkes Produkt mit klarer Marktvalidierung. Fehlender Free Tier und DSGVO-Lücken sind die Hauptschwächen.*

---

## Tool 4: Perplexity Computer

### Kategorie: RECHERCHE

### Kurzbeschreibung
Perplexity Computer ist ein **autonomes Multi-Modell-Orchestrierungssystem**, das am 25. Februar 2026 lanciert wurde. Es ist mehr als ein Recherche-Tool — es ist ein vollständiger digitaler Mitarbeiter, der komplexe, mehrstufige Workflows selbstständig plant und ausführt. Perplexity Computer koordiniert **19 verschiedene KI-Modelle** (darunter Claude Opus 4.6, Gemini für Deep Research, Nano Banana für Bilder, Veo 3.1 für Video, Grok für schnelle Aufgaben und ChatGPT 5.2 für Long-Context) und setzt sie intelligent für spezifische Teilaufgaben ein. Ein Nutzer beschreibt ein Ziel — Perplexity Computer zerlegt es in Aufgaben, erstellt Sub-Agenten, führt parallele Workflows aus und liefert ein Ergebnis. Das System kann stunden- oder sogar monatelang autonom laufen. Zielgruppe sind Power-User, Researcher, Unternehmen und alle, die komplexe Informationsarbeit automatisieren wollen.

### Nutzungsszenarien
1. **Marktforschung:** "Erstelle einen vollständigen Wettbewerbsanalysebericht für unser SaaS-Produkt im DACH-Markt" — Perplexity Computer recherchiert, analysiert, strukturiert und schreibt den Bericht autonom.
2. **Content-Produktion:** "Erstelle 10 LinkedIn-Posts für den nächsten Monat basierend auf unseren letzten Blogartikeln" — das System liest die Artikel, generiert Posts und passt Ton und Format an.
3. **Code-und-Deploy-Workflows:** "Baue eine Landing Page für unser neues Produkt" — Computer recherchiert Best Practices, schreibt Code, testet und deployt.
4. **Datenerhebung und -analyse:** "Sammle alle öffentlich verfügbaren Preise unserer Top-10-Konkurrenten und erstelle eine Vergleichstabelle" — vollständig automatisiert.
5. **Komplexe Recherche-Aufgaben:** Wissenschaftliche Literaturrecherche, Due Diligence, Policy-Analyse — Aufgaben, die normalerweise Stunden dauern, werden in Minuten erledigt.

### Pricing
| Plan | Preis | Details |
|------|-------|---------|
| Free | $0 | Kein Zugang zu Computer |
| Pro | $20/Monat | Kein Zugang zu Computer |
| Max (Individual) | $200/Monat ($2.000/Jahr) | Vollzugang zu Computer, 10.000 Credits/Monat, Priority Execution |
| Enterprise Pro | $40/Nutzer/Monat | Computer-Zugang kommt bald |

**Perplexity Computer Credits:** Max-Abonnenten erhalten 10.000 Credits/Monat + 20.000 Bonus-Credits (Limited-Time). Jede Computer-Aufgabe verbraucht Credits basierend auf Komplexität. Normale Perplexity-Suchen bleiben unberührt.

### Datenschutz
- **Unternehmensstandort:** USA (Perplexity AI, Inc., San Francisco)
- **Serverstandort:** USA (primär)
- **DSGVO:** DSGVO-Datenschutzanfragen werden unterstützt (eigener Bereich im Help Center). Keine EU-Serverstandorte kommuniziert. Enterprise-Plan mit erweiterten Datenschutz-Features.
- **Datenverwendung:** Laut Privacy Policy werden Daten nicht für Modell-Training verwendet (opt-out möglich)
- **Self-Hosting:** Nicht verfügbar
- **Datenschutz-Bewertung: 6/10** — DSGVO-Anfragen werden unterstützt, aber keine EU-Server; für Enterprise-Kunden mit Compliance-Anforderungen kritisch

### Stärken
- Einzigartiger Ansatz: 19 Modelle intelligent orchestriert
- Vollständig autonome, asynchrone Workflow-Ausführung
- Parallele Sub-Agenten für maximale Effizienz
- Modell-agnostisch: wechselt automatisch zu den besten Modellen je Aufgabe
- Echte Filesystem- und Browser-Integration
- Basiert auf Perplexitys bewährter Deep-Research-Infrastruktur

### Schwächen
- Sehr hoher Preis: $200/Monat (nur für Max-Abonnenten)
- Noch in früher Phase — Zuverlässigkeit bei komplexen Aufgaben variiert
- Kein EU-Serverstandort
- Kein Self-Hosting
- Erste User-Reviews berichten von Credit-Verbrauch bei fehlgeschlagenen Aufgaben
- Keine Transparenz über welche Modelle für welche Aufgaben eingesetzt werden

### Einschätzung für die Praxis
Perplexity Computer ist das ambitionierteste Produkt der Woche — und möglicherweise das wichtigste. Die Idee, 19 spezialisierte KI-Modelle zu einem einzigen, autonomen System zu orchestrieren, ist der logische nächste Schritt nach Chatbots und einfachen Agenten. Für Power-User und Unternehmen, die bereit sind, $200/Monat zu investieren, und komplexe Informationsarbeit automatisieren wollen, ist es ein Game-Changer. Die ersten Reviews sind gemischt — die Technologie ist beeindruckend, aber noch nicht perfekt zuverlässig.

### Relevanzbewertung: **8.5/10**
*Paradigmenwechsel in der KI-Orchestrierung. Hoher Preis und frühe Reife sind die Hauptvorbehalte.*

---

## Tool 5: Notion Custom Agents

### Kategorie: AGENTS

### Kurzbeschreibung
Notion Custom Agents, lanciert am 24. Februar 2026 als Teil von **Notion 3.3**, sind autonome KI-Bots, die direkt im Notion-Workspace laufen und komplette Workflows 24/7 selbstständig ausführen — ohne dass der Nutzer anwesend sein muss. Sie können Aufgaben triagieren, Fragen beantworten, Berichte erstellen, Slack-Nachrichten senden, E-Mails verschicken und auf Datenbanken zugreifen. Das Besondere: Notion hat ein **"Build-from-Nothing"-Sicherheitsmodell** entwickelt, bei dem Agenten ohne jegliche Berechtigungen starten und nur explizit freigegebene Ressourcen nutzen können — ein fundamentaler Unterschied zu anderen Agenten-Systemen. Während der Alpha-Phase haben interne Notion-Teams über 3.000 Custom Agents erstellt, externe Alpha-Kunden über 25.000. Zielgruppe sind alle Notion Business- und Enterprise-Nutzer, die repetitive Workflows automatisieren wollen.

### Nutzungsszenarien
1. **Aufgaben-Triage:** Ein Agent überwacht den Notion-Inbox, priorisiert neue Aufgaben nach definierten Kriterien und weist sie automatisch den richtigen Teammitgliedern zu.
2. **Wöchentliche Status-Reports:** Jeden Freitagabend erstellt ein Agent automatisch einen Projektbericht aus allen Notion-Datenbanken und postet ihn in den Team-Slack-Channel.
3. **Kundensupport-Vorbereitung:** Ein Agent überwacht eingehende Support-Anfragen, recherchiert relevante Informationen in der Wissensdatenbank und erstellt Antwort-Entwürfe für das Support-Team.
4. **Content-Kalender-Management:** Ein Agent überwacht den Content-Kalender, erinnert Autoren an Deadlines und erstellt automatisch Briefings für neue Artikel.
5. **Security-Monitoring:** Notions eigenes Security-Team nutzt einen Agenten ("Scruff Bot"), um Security-Alerts zu triagieren, anzureichern und Code-Fixes zu generieren.

### Pricing
| Plan | Preis | Custom Agents |
|------|-------|---------------|
| Free | $0 | Kein Zugang |
| Plus | $10/Nutzer/Monat | Kein Zugang |
| Business | $20/Nutzer/Monat | Kostenlos bis 3. Mai 2026 |
| Enterprise | Custom | Kostenlos bis 3. Mai 2026 |

**Ab 4. Mai 2026:** Custom Agents laufen auf **Notion Credits** ($10 pro 1.000 Credits, Add-on für Business/Enterprise). Credits werden basierend auf Aufgaben-Komplexität verbraucht und monatlich zurückgesetzt. Bis zum 3. Mai 2026 ist die Nutzung für alle Business- und Enterprise-Nutzer **vollständig kostenlos und unbegrenzt**.

### Datenschutz
- **Unternehmensstandort:** USA (Notion Labs, Inc., San Francisco)
- **Serverstandort:** USA (primär), EU-Serverstandort für Enterprise verfügbar
- **DSGVO:** DSGVO-konform, SCCs verfügbar, EU-Datenschutzanfragen werden unterstützt. Enterprise-Plan mit Zero Data Retention bei LLM-Providern.
- **Datenverwendung:** Notion AI trainiert nicht auf Nutzerdaten (opt-out standard). Vertragliche Vereinbarungen mit AI-Subprozessoren verbieten Modell-Training auf Kundendaten.
- **Self-Hosting:** Nicht verfügbar
- **Datenschutz-Bewertung: 7/10** — Gute DSGVO-Dokumentation, EU-Server für Enterprise, Zero Data Retention im Enterprise-Plan. Kein Self-Hosting.

### Stärken
- Direkt in Notion integriert — kein separates Tool nötig
- "Build-from-Nothing"-Sicherheitsmodell: sicherster Agenten-Ansatz im Vergleich
- Kostenlos bis Mai 2026 für alle Business/Enterprise-Nutzer
- Granulare Berechtigungen auf Seiten-Ebene
- Prompt-Injection-Schutz eingebaut
- Erste-Party-Slack-Integration mit granularen Berechtigungen
- Bewährt: 25.000+ Agenten in Alpha-Phase erstellt

### Schwächen
- Nur für Business- und Enterprise-Nutzer ($20+/Monat)
- Noch in der Beta-Phase — Zuverlässigkeit noch nicht für alle Use Cases bewiesen
- Kein Self-Hosting
- Pricing ab Mai 2026 noch unklar (Credits-Modell)
- Begrenzt auf Notion-Ökosystem — externe Integrationen über MCP (noch eingeschränkt)
- US-Unternehmen ohne EU-Server in Standard-Plänen

### Einschätzung für die Praxis
Notion Custom Agents ist das zugänglichste Agenten-System, das je lanciert wurde. Wer bereits Notion Business nutzt, kann sofort und kostenlos starten — ohne Programmierkenntnisse, ohne Server-Setup, ohne komplexe Konfiguration. Das Sicherheitsmodell ist durchdacht und der Ansatz, Agenten direkt in den bestehenden Workspace zu integrieren, ist der richtige. Für europäische Unternehmen ist der Enterprise-Plan mit EU-Servern und Zero Data Retention empfehlenswert.

### Relevanzbewertung: **8.5/10**
*Demokratisierung von KI-Agenten auf höchstem Niveau. Kostenlos bis Mai 2026 — jetzt ausprobieren.*

---

## Quellen dieser Analyse

- Ben's Bites Newsletter (26. Feb 2026)
- Product Hunt Leaderboard Februar 2026
- Inception Labs Blog (Mercury 2 Launch, 24. Feb 2026)
- Perplexity Blog (Introducing Perplexity Computer, 25. Feb 2026)
- Notion Blog (Introducing Custom Agents, 24. Feb 2026)
- Kilo.ai Blog (KiloClaw GA, 24. Feb 2026)
- a16z Announcement (Investing in QuiverAI, 26. Feb 2026)
- VentureBeat, TechCrunch, The Decoder (Berichterstattung KW 09/2026)
- Reddit r/perplexity_ai, r/singularity (Community-Reviews)
- Supaboard.ai Pricing Page
- Notion Pricing & Help Center
