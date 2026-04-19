# Wöchentliche KI-Tool-Analyse – KW 16 (14. bis 19. April 2026)

Diese Woche stand ganz im Zeichen von Agentic Workflows und der Integration von KI in bestehende Systeme. Anthropic hat mit Claude Opus 4.7 sein stärkstes Modell für autonome Aufgaben veröffentlicht, während Figma mit seinem neuen MCP-Server die Lücke zwischen KI-generiertem Code und Design-Systemen schliesst. Perplexity erweitert seinen Computer-Agenten zum "Personal CFO" und Google bringt mit Gemma 4 ein extrem leistungsfähiges, lokales Open-Source-Modell. Fathom 3.0 zeigt derweil, wie Meeting-KI ohne störende Bots funktionieren kann.

---

## 1. Fathom 3.0
**Kategorie:** Text

**Kurzbeschreibung:**
Fathom 3.0 ist ein KI-gestützter Meeting-Assistent, der Gespräche aufzeichnet, transkribiert und zusammenfasst. Das Major-Update vom 15. April 2026 führt eine "bot-freie" Aufzeichnungsoption ein, die Meetings ohne sichtbaren Teilnehmer-Bot dokumentiert, und integriert sich tief in LLMs wie Claude und ChatGPT.

**Nutzungsszenarien:**
- **Vertriebsgespräche:** Automatische Erstellung von Deal-Zusammenfassungen und Synchronisation der Notizen direkt in CRM-Felder (Salesforce, HubSpot).
- **Interne Team-Meetings:** Bot-freie Aufzeichnung von Strategie-Meetings, bei denen ein sichtbarer Bot als störend empfunden würde.
- **Coaching & Onboarding:** Analyse von Sprechanteilen und Gesprächsdynamiken zur Schulung neuer Mitarbeitenden.

**Pricing:**
- **Free Tier:** Kostenlos für Einzelnutzer (unlimitierte Aufzeichnungen, Transkriptionen und Basis-Zusammenfassungen).
- **Team:** $15 pro Nutzer/Monat (globale Suche, Team-Playlists, SSO).
- **Business:** $25 pro Nutzer/Monat (CRM-Sync, Deal-Views, Coaching-Metriken).

**Datenschutz:**
Fathom legt grossen Wert auf Datenschutz. Die Server befinden sich primär in den USA, das Unternehmen ist jedoch nach dem Data Privacy Framework (DPF) zertifiziert und bietet Standardvertragsklauseln (SCCs) für europäische Kunden an. Im Business-Plan können zudem individuelle Datenaufbewahrungsrichtlinien (Data Retention Policies) definiert werden.

**Stärken:**
- Die neue bot-freie Aufzeichnung löst das weit verbreitete Problem der "Bot-Müdigkeit" in Video-Calls.
- Sehr grosszügiger Free-Tier für Einzelpersonen.
- Starke CRM-Integrationen und neue "Ask Fathom"-Funktion über alle Team-Calls hinweg.

**Schwächen:**
- Die bot-freie Aufzeichnung ist aktuell noch im Beta-Stadium und primär für Mac-Nutzer optimiert.
- Volle DSGVO-Konformität mit europäischem Serverstandort wird nicht explizit als Standard angeboten (US-Hosting mit DPF).

**Einschätzung für die Praxis:**
Fathom 3.0 ist ein exzellentes Tool für Teams, die ihre Meeting-Kultur professionalisieren wollen, ohne die Teilnehmer mit Bots zu irritieren. Besonders für Sales- und Customer-Success-Teams bietet die CRM-Integration einen massiven Effizienzgewinn.

**Relevanzbewertung:** 9/10

---

## 2. Figma for Agents
**Kategorie:** Design

**Kurzbeschreibung:**
Figma for Agents ist ein neues Model Context Protocol (MCP) Tool, das es KI-Agenten (wie Claude Code oder Cursor) ermöglicht, direkt in Figma-Dateien zu arbeiten. Es verbindet KI-generierten Code mit dem tatsächlichen Design-System eines Unternehmens.

**Nutzungsszenarien:**
- **Design-to-Code:** Ein Frontend-Entwickler nutzt einen KI-Agenten, um React-Komponenten zu generieren, die exakt auf den Figma-Tokens und -Variablen basieren.
- **Code-to-Design:** Ein Entwickler pusht eine im Code erstellte UI zurück auf das Figma-Canvas, damit Designer sie mit echten Komponenten verfeinern können.
- **Accessibility-Audits:** Automatische Generierung von Screen-Reader-Spezifikationen (ARIA) direkt aus den Figma-Komponenten durch einen KI-Agenten.

**Pricing:**
Das MCP-Tool selbst ist kostenlos nutzbar, erfordert jedoch einen entsprechenden Figma-Plan (Professional ab $12/Monat oder Organization/Enterprise) sowie API-Kosten für die genutzten LLMs (z.B. Claude Opus).

**Datenschutz:**
Da es sich um ein Protokoll (MCP) handelt, das lokal oder über die Figma-API läuft, gelten die allgemeinen Datenschutzbestimmungen von Figma. Figma hostet Daten primär in den USA, bietet für Enterprise-Kunden aber erweiterte Compliance-Optionen. Die Datenverarbeitung durch die KI-Agenten hängt vom gewählten LLM-Anbieter ab.

**Stärken:**
- Löst das fundamentale Problem, dass KI-generierte UIs oft nicht den Markenrichtlinien entsprechen ("Looks AI-generated").
- Ermöglicht echte bidirektionale Workflows zwischen Designern und Entwicklern.
- Nutzt das standardisierte Model Context Protocol (MCP).

**Schwächen:**
- Setzt ein sehr gut gepflegtes und strukturiertes Design-System in Figma voraus (saubere Benennung, Auto-Layout, Tokens).
- Die Einrichtung des MCP-Servers und die Verknüpfung mit Coding-Agenten erfordert technisches Know-how.

**Einschätzung für die Praxis:**
Für Produktteams, die bereits stark auf Figma und KI-Coding-Assistenten setzen, ist dieses Tool ein absoluter Game-Changer. Es schliesst die Lücke zwischen Design-Intention und KI-generiertem Code und verhindert das "Ausfransen" von Design-Systemen.

**Relevanzbewertung:** 10/10

---

## 3. Google Gemma 4
**Kategorie:** Data / Wissen

**Kurzbeschreibung:**
Gemma 4 ist Googles neueste Familie von offenen, multimodalen KI-Modellen. Sie bieten eine Kontextlänge von bis zu 256K Tokens und sind in verschiedenen Grössen (von 2B bis 31B Parametern) verfügbar, optimiert für den lokalen Einsatz auf Laptops bis hin zu Servern.

**Nutzungsszenarien:**
- **Lokale Datenanalyse:** Auswertung sensibler Unternehmensdaten (z.B. Finanzberichte, HR-Daten) komplett offline auf einem Firmen-Laptop.
- **Multimodale Verarbeitung:** Analyse von Diagrammen, Dokumenten und sogar Audio/Video-Dateien direkt auf dem Endgerät (E2B/E4B Modelle).
- **Edge-Computing:** Integration von leistungsfähiger KI in mobile Apps oder IoT-Geräte ohne Cloud-Abhängigkeit.

**Pricing:**
Kostenlos. Die Modelle werden unter der offenen Gemma-Lizenz (ähnlich Apache 2.0) bereitgestellt und können frei heruntergeladen und kommerziell genutzt werden.

**Datenschutz:**
Da die Modelle lokal (z.B. via Ollama oder LM Studio) ausgeführt werden können, bieten sie maximalen Datenschutz. Es fliessen keine Daten an externe Server ab. Dies macht Gemma 4 zur perfekten Wahl für strikte DSGVO-Anforderungen und hochsensible Daten.

**Stärken:**
- Hervorragendes Verhältnis von Modellgrösse zu Leistung, besonders bei den kleinen E2B und E4B Modellen.
- Native multimodale Fähigkeiten (Text, Bild, Audio, Video) auch bei den kleinsten Varianten.
- 100% Datenkontrolle durch lokales Deployment.

**Schwächen:**
- Erreicht bei extrem komplexen Logik-Aufgaben nicht ganz das Niveau der grossen proprietären Modelle (wie GPT-5.4 oder Claude Opus 4.7).
- Erfordert entsprechende Hardware (RAM/VRAM) für die Ausführung der grösseren 26B/31B Modelle.

**Einschätzung für die Praxis:**
Gemma 4 ist ein Meilenstein für Open-Source-KI. Für Unternehmen, die aus Compliance- oder Sicherheitsgründen keine Cloud-LLMs nutzen dürfen, bietet Gemma 4 nun multimodale Fähigkeiten auf einem Niveau, das lokales Arbeiten extrem produktiv macht.

**Relevanzbewertung:** 9/10

---

## 4. Perplexity Computer (Personal CFO)
**Kategorie:** Recherche

**Kurzbeschreibung:**
Perplexity hat seinen Desktop-Agenten "Computer" um eine "Personal CFO"-Funktion erweitert. Durch eine tiefe Integration mit Plaid kann die KI nun sicher auf Bankkonten, Kreditkarten und Kredite zugreifen, um personalisierte Finanzanalysen und Recherchen durchzuführen.

**Nutzungsszenarien:**
- **Ausgabenanalyse:** Automatische Kategorisierung und Visualisierung (z.B. Heatmaps) der monatlichen Ausgaben über alle Konten hinweg.
- **Budget-Planung:** Erstellung massgeschneiderter Budgetpläne basierend auf dem tatsächlichen, historischen Ausgabeverhalten.
- **Net-Worth-Tracking:** Konsolidierte Übersicht über Vermögenswerte und Verbindlichkeiten in Echtzeit.

**Pricing:**
Das "Computer"-Feature und die Personal CFO-Funktion erfordern ein Perplexity Pro Abonnement ($20/Monat) oder den Max Plan ($200/Monat).

**Datenschutz:**
Die Finanzdaten-Anbindung erfolgt über Plaid, einen etablierten und stark regulierten Finanzdaten-Provider. Perplexity betont die Sicherheit der Verbindung, dennoch erfordert die Übergabe von Live-Transaktionsdaten an einen KI-Agenten ein hohes Mass an Vertrauen. Die Funktion ist aktuell auf die USA und Kanada beschränkt.

**Stärken:**
- Verbindet die exzellenten Recherche- und Analysefähigkeiten von Perplexity mit echten, persönlichen Echtzeit-Daten.
- Ersetzt potenziell teure Finanz-Tracking-Apps durch eine flexible, dialogbasierte Schnittstelle.

**Schwächen:**
- Aktuell nur in den USA und Kanada verfügbar (Plaid-Restriktionen).
- Datenschutzbedenken: Viele Nutzer zögern, einer generativen KI direkten Zugriff auf ihre Bankdaten zu gewähren.

**Einschätzung für die Praxis:**
Ein faszinierender Blick in die Zukunft von KI-Agenten, die nicht nur das Web durchsuchen, sondern als persönliche Analysten auf private Daten-Silos zugreifen. Für europäische Nutzer aufgrund der regionalen Beschränkung aktuell noch nicht nutzbar, aber konzeptionell wegweisend.

**Relevanzbewertung:** 8/10

---

## 5. Claude Opus 4.7
**Kategorie:** Agents

**Kurzbeschreibung:**
Claude Opus 4.7 ist das neueste und stärkste Modell von Anthropic, das speziell für "Agentic Coding", komplexe Systemarchitekturen und langlaufende, autonome Aufgaben entwickelt wurde. Es bietet ein 1-Million-Token-Kontextfenster und verbesserte visuelle Fähigkeiten.

**Nutzungsszenarien:**
- **Autonome Softwareentwicklung:** Einbindung in Tools wie Claude Code oder Cursor zur eigenständigen Lösung komplexer GitHub-Issues über mehrere Dateien hinweg.
- **Tiefenanalyse von Dokumenten:** Auswertung hunderter Seiten von Finanzberichten oder juristischen Verträgen in einem einzigen Prompt (dank 1M Kontext).
- **Visuelle Verifikation:** Analyse von hochauflösenden Screenshots (bis zu 3.75 Megapixel) zur Überprüfung von UI-Implementierungen gegen Design-Vorgaben.

**Pricing:**
Die API-Preise bleiben identisch zum Vorgänger Opus 4.6: $5 pro 1 Million Input-Tokens und $25 pro 1 Million Output-Tokens. Es gibt keinen Preisaufschlag für die Nutzung des vollen 1M-Kontextfensters.

**Datenschutz:**
Anthropic bietet für Enterprise-Kunden Zero-Data-Retention-Agreements an (Daten werden nicht für das Modelltraining verwendet). Für europäische Kunden ist die Nutzung über Cloud-Provider wie AWS (Amazon Bedrock) oder Google Cloud (Vertex AI) mit Serverstandorten in der EU (z.B. Frankfurt, Paris) möglich, was die DSGVO-Konformität sicherstellt.

**Stärken:**
- Führend bei Coding-Benchmarks (87.6% auf SWE-bench Verified).
- Keine versteckten Kosten für extrem lange Kontexte (1M Tokens).
- Deutlich verbesserte Bilderkennung (3.3x höhere Auflösung als der Vorgänger).

**Schwächen:**
- Die API-Kosten sind im Vergleich zu Modellen wie Claude 4.6 Sonnet oder Gemini 3.1 Pro weiterhin sehr hoch.
- Ein neuer Tokenizer kann dazu führen, dass derselbe Text bis zu 35% mehr Tokens verbraucht als bei Opus 4.6, was die effektiven Kosten leicht erhöht.

**Einschätzung für die Praxis:**
Claude Opus 4.7 ist kein Modell für einfache Chat-Anfragen, sondern eine "Heavy-Duty"-Engine für Entwickler und Unternehmen, die komplexe, autonome Agenten-Workflows bauen. Wer höchste Zuverlässigkeit bei Code-Generierung und Systemarchitektur sucht, kommt an diesem Modell aktuell nicht vorbei.

**Relevanzbewertung:** 10/10
