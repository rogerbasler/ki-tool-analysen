#!/usr/bin/env python3
"""
Generiert die index.html für KW 14/2026
"""
import sys
sys.path.insert(0, '/home/ubuntu/ki-tool-website')
from generate_html_from_analysis import create_html

tools = [
    {
        'name': 'Atomic Chat',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 8.5,
        'tagline': 'Open-Source ChatGPT-Alternative — 1.000+ KI-Modelle vollständig offline auf dem Mac, zero data exfiltration',
        'description': 'Atomic Chat ist eine Open-Source-Desktop-App für macOS (und Linux/Windows via Build-from-Source), die es ermöglicht, über 1.000 KI-Modelle vollständig offline zu betreiben. Die App basiert auf dem Fork des bekannten Jan-Projekts (janhq/jan) und wurde in dieser Woche stark in The Neuron Daily und Ben\'s Bites erwähnt. Zielgruppe sind datenschutzbewusste Einzelpersonen, Unternehmen mit sensiblen Daten sowie Entwicklerinnen und Entwickler, die Cloud-Kosten eliminieren möchten. Unterstützt Llama, Gemma, Qwen, Mistral und viele weitere Modelle von HuggingFace. Mit MCP-Integration für agentenbasierte Workflows und einem OpenAI-kompatiblen lokalen API-Server (localhost:1337).',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Kostenlos (Apache 2.0 Open Source). Atomic Chat selbst ist dauerhaft gratis. Wer Cloud-Modelle via API einbinden möchte, zahlt die jeweiligen API-Kosten der Anbieter (OpenAI, Anthropic, Mistral, Groq). Lokale Modelle sind komplett kostenlos. Keine versteckten Kosten, kein Abo.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Zero-Data-Exfiltration by Design: Kein Byte verlässt das Gerät. Unterstützt 1.000+ Modelle von HuggingFace. MCP-Integration für agentenbasierte Workflows. OpenAI-kompatibler lokaler API-Server (localhost:1337). Aktive Entwicklung: 57 Tags, 7.976 Commits, wöchentliche Releases. Systemanforderungen: macOS 13.6+, 8 GB RAM für 3B-Modelle, 16 GB für 7B, 32 GB für 13B+.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: Keiner — alle Daten verbleiben lokal. DSGVO: Vollständig konform, da keine Datenübermittlung an Dritte stattfindet. Lizenz: Apache 2.0. Eliminiert die gesamte Komplexität von Datenverarbeitungsverträgen, Drittlandtransfers und Datenschutz-Folgeabschätzungen. Für Schweizer und EU-Unternehmen unter DSGVO und DSG ideal. (10/10)'
            }
        ],
        'verdict': 'Atomic Chat ist die konsequenteste Antwort auf die Datenschutzproblematik von Cloud-KI. Für Schweizer und europäische Unternehmen unter DSGVO und dem revidierten DSG ist dieses Tool besonders relevant: Es eliminiert die gesamte Komplexität von DPAs, Drittlandtransfers und Datenschutz-Folgeabschätzungen. Die Kombination mit Gemma 4 (Apache 2.0, läuft auf Consumer-Hardware) macht 2026 zum Jahr, in dem lokale KI erstmals wirklich praxistauglich wird.',
        'url': 'https://atomic.chat'
    },
    {
        'name': 'Noon',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 7.5,
        'tagline': 'Das erste KI-native Design-Tool auf Production-Code — $44M Funding, aus dem Stealth-Modus',
        'description': 'Noon ist das erste KI-native Produktdesign-Tool, das direkt auf dem Production-Code des Teams arbeitet — nicht auf statischen Mockups. Gegründet 2024 von Aditya Bandi (ex-Bookpad CEO) und Kushagra Sinha (ex-Leap Co-Founder), trat Noon in dieser Woche aus dem Stealth-Modus heraus und veröffentlichte gleichzeitig seine $44-Millionen-Finanzierungsrunde (Chemistry, First Round Capital, Scribble Ventures, Elevation Capital). Das Tool richtet sich an Produktdesigner und Entwicklungsteams, die den Gap zwischen Design und Code schliessen wollen. Designer arbeiten direkt auf der laufenden Codebasis, nicht auf einem separaten Figma-Mockup, das anschliessend manuell implementiert werden muss.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Noch in der Early-Access-Phase; öffentliche Preispläne wurden noch nicht kommuniziert. Aktuell: Waitlist / Early Access auf Anfrage. Basierend auf der Positionierung ist ein SaaS-Modell im Bereich $20–50/Monat/Nutzer zu erwarten (Q2/Q3 2026).'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Revolutionärer Ansatz: Design direkt auf Production-Code statt auf statischen Mockups. Eliminiert den klassischen "Handoff"-Prozess zwischen Design und Entwicklung. Dual-Canvas: Visueller Editor und Code-View in einem. KI-nativ von Grund auf gebaut — kein nachträgliches KI-Feature-Bolting. Starkes Investoren-Backing ($44M von Top-VCs).'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: USA (San Francisco; Vercel-Hosting). DSGVO-Konformität: Noch keine öffentliche DSGVO-Erklärung; Terms of Service vorhanden. Self-Hosting: Nicht verfügbar (Cloud-only). Da das Tool auf dem Produktionscode des Unternehmens arbeitet, ist eine sorgfältige Prüfung vor dem Einsatz mit sensiblem Code empfehlenswert. (5.5/10)'
            }
        ],
        'verdict': 'Noon adressiert einen echten Pain Point: Der Bruch zwischen Design-Tools (Figma, Sketch) und der tatsächlichen Codebasis kostet Teams täglich Stunden. Wenn Noon hält, was es verspricht, könnte es den Design-Workflow fundamental verändern. Für den sofortigen Einsatz ist es noch zu früh — kein öffentliches Pricing, keine DSGVO-Klarheit, keine unabhängigen Reviews. In 6–12 Monaten könnte Noon jedoch eines der wichtigsten Tools für Produktteams werden.',
        'url': 'https://noon.design'
    },
    {
        'name': 'Google Gemma 4',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA/WISSEN',
        'rating': 9.5,
        'tagline': 'Frontier Open-Source-KI unter Apache 2.0 — von Raspberry Pi bis H100, DSGVO-konform on-premise',
        'description': 'Google DeepMind veröffentlichte am 2. April 2026 Gemma 4 — die bisher fähigste Open-Source-Modellfamilie von Google, erstmals unter der kommerziell permissiven Apache-2.0-Lizenz. Die Familie umfasst vier Modelle (E2B, E4B, 26B MoE, 31B Dense) für unterschiedliche Hardware-Anforderungen, von Raspberry Pi bis zum Rechenzentrum. Gemma 4 unterstützt nativ Text, Bild und Audio und ist für agentenbasierte Workflows optimiert. Auf der Google AI Studio API sind 1.500 kostenlose Anfragen pro Tag für Gemma 4 31B verfügbar. Läuft auf Ollama, LM Studio, MLX, NVIDIA NIM, LiteRT und mehr.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Modell-Weights (lokal): Kostenlos (Apache 2.0, HuggingFace, Ollama, Kaggle). Google AI Studio API: Kostenlos (1.500 Anfragen/Tag für Gemma 4 31B). Gemini API (Pay-as-you-go): ab $0,03/1M Token für höhere Volumina. Vertex AI: Auf Anfrage für Enterprise. Cloudflare Workers AI: Kostenlos im Free Tier.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Erstmals Apache 2.0 — vollständige kommerzielle Freiheit ohne Nutzungsbeschränkungen. Vier Modellgrössen für jede Hardware (Raspberry Pi bis H100). Nativ multimodal (Text, Bild, Audio) in einem Modell. 128K–256K Kontext. 400M+ Downloads auf HuggingFace (historischer Wert der Gemma-Familie). Läuft auf Ollama, LM Studio, MLX, NVIDIA NIM und mehr.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Bei lokalem Betrieb: Vollständig DSGVO-konform, keine Datenübermittlung. Bei Cloud-API: Standard-Contractual-Clauses mit Google erforderlich; EU-Region via Vertex AI Sovereign Cloud verfügbar. Self-Hosting vollständig unterstützt (Ollama, LM Studio, llama.cpp, Docker). Lizenz: Apache 2.0 — keine Nutzungsbeschränkungen. (10/10 für On-Premise)'
            }
        ],
        'verdict': 'Gemma 4 unter Apache 2.0 ist das wichtigste Open-Source-KI-Ereignis des Jahres 2026 bis dato. Für europäische Unternehmen unter DSGVO öffnet sich damit eine neue Tür: Frontier-nahe KI-Qualität, vollständig on-premise, ohne Drittlandtransfer, ohne Lizenzrisiko. Die Kombination mit Atomic Chat oder Ollama macht den Einstieg denkbar einfach. Besonders die E2B/E4B-Modelle für Edge-Geräte sind ein Gamechanger für mobile Anwendungen.',
        'url': 'https://deepmind.google/models/gemma/gemma-4'
    },
    {
        'name': 'Perplexity Computer for Taxes',
        'category': 'research',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 7.8,
        'tagline': 'Erster agentischer Steuer-Assistent — IRS-Formulare ausfüllen, Erklärungen prüfen, Abzüge optimieren',
        'description': 'Perplexity Computer ist ein agentischer KI-Dienst, der seit Februar 2026 End-to-End-Aufgaben für Nutzer ausführen kann. In dieser Woche erweiterte Perplexity die Plattform um ein umfassendes Steuer-Modul ("Navigate My Taxes"), das auf dem Agent-Skills-Protokoll basiert. Das System kann US-Bundessteuererklärungen auf offiziellen IRS-Formularen ausfüllen, professionell erstellte Steuererklärungen prüfen, Dashboards und Tools für komplexe Steuerszenarien bauen und beliebige Steuer-Workflows automatisieren. Im Test fand das System in einer anwaltlich erstellten Erklärung nicht geltend gemachte Abzüge von mehreren Tausend Dollar (No Tax on Overtime 2025 — 67% unterbewertet).',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (kein Zugang zu Computer). Pro: $17/Monat — Perplexity Computer inkl. Tax-Modul. Max: $200/Monat — erweiterte Nutzung, Priority Access. Das Tax-Feature ist ab sofort für alle Pro-Abonnenten verfügbar; Mobile-Rollout in den kommenden Wochen.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Erster vollständig agentischer Steuer-Assistent auf dem Markt. Basiert auf dem Agent-Skills-Protokoll — erweiterbar für eigene Workflows. Kennt aktuelle Gesetzesänderungen (No Tax on Overtime 2025). Kann nicht nur Formulare ausfüllen, sondern auch Software, Dashboards und Tracking-Tools bauen. Nachweislich bessere Ergebnisse als manche professionellen Steuerberater in Tests.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: USA (Perplexity AI, San Francisco). DSGVO: Eingeschränkt — Steuerdaten sind hochsensibel und werden auf US-Servern verarbeitet. Für EU-Nutzer mit sensiblen Finanzdaten problematisch. Kein Self-Hosting. Hinweis: Das Tax-Feature ist primär auf US-Steuerrecht (IRS) ausgerichtet; für Schweizer/EU-Steuern nicht direkt anwendbar. (5.0/10 für EU-Nutzer)'
            }
        ],
        'verdict': 'Für US-amerikanische Nutzer ist Perplexity Computer for Taxes ein echter Gamechanger — $17/Monat für einen KI-Steuerberater, der aktuelle Gesetzesänderungen kennt und professionell erstellte Erklärungen prüfen kann. Für Schweizer und EU-Nutzer ist das Tool aufgrund des US-Fokus und der Datenschutzbedenken weniger relevant. Die zugrundeliegende Technologie (Agent Skills für komplexe Fachdomänen) ist jedoch wegweisend.',
        'url': 'https://www.perplexity.ai/computer'
    },
    {
        'name': 'Holo3 by H Company',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 9.2,
        'tagline': 'State-of-the-Art Computer-Use-Agent — 78,85% OSWorld, Open Source Apache 2.0, europäisches Unternehmen',
        'description': 'Holo3 ist die neueste Generation der Computer-Use-Agenten von H Company (Paris, Frankreich) und setzt mit 78,85% auf dem OSWorld-Verified-Benchmark einen neuen State-of-the-Art für Desktop-Computer-Use. Das Modell übertrifft GPT-5.4 und Claude Opus 4.6 bei Desktop-Aufgaben und erreicht dies mit nur 10 Milliarden aktiven Parametern (122B total, Mixture-of-Experts-Architektur). Die Gewichte des 35B-A3B-Modells sind unter Apache 2.0 frei verfügbar. Holo3 kann mehrstufige Enterprise-Workflows ausführen: z.B. Preise aus einem PDF extrahieren, mit Mitarbeiterbudgets abgleichen und personalisierte Genehmigungs-E-Mails versenden — alles autonom.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Inference API (Free Tier): Kostenlos über HuggingFace (limitierte Anfragen). Holo3-35B-A3B Weights: Kostenlos (Apache 2.0, Self-Hosting möglich). H Company API (Open-Source): $0,25/1M Input-Token, $1,80/1M Output-Token. Enterprise: Auf Anfrage (Dedicated Deployment, SLA).'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': '78,85% auf OSWorld-Verified — neuer State-of-the-Art, übertrifft GPT-5.4 und Opus 4.6. Nur 10B aktive Parameter bei 122B total — extrem kosteneffizient. Apache 2.0 Lizenz. Europäisches Unternehmen (Paris) — starker DSGVO-Vorteil. Speziell für Enterprise-Workflows trainiert (Synthetic Environment Factory). Unterstützt komplexe Multi-App-Workflows mit Zustandserhaltung.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: Frankreich/EU (H Company, Paris) — starker DSGVO-Vorteil gegenüber US-Anbietern. DSGVO: Sehr gut — europäisches Unternehmen, EU-Serverstandort, kein Drittlandtransfer bei API-Nutzung. Self-Hosting: Vollständig unterstützt (Apache 2.0 Weights). Bei Self-Hosting: vollständige Datensouveränität. (9.5/10)'
            }
        ],
        'verdict': 'Holo3 ist der überzeugendste Computer-Use-Agent, der bisher veröffentlicht wurde — und das von einem europäischen Unternehmen unter Apache 2.0. Für Schweizer und EU-Unternehmen, die Desktop-Automatisierung ohne US-Cloud-Abhängigkeit suchen, ist dies ein ausserordentlich relevantes Tool. Die Kombination aus SOTA-Performance, Open-Source-Lizenz, EU-Serverstandort und kostenlosem Einstieg macht Holo3 zur ersten ernsthaften Alternative zu proprietären Computer-Use-Lösungen.',
        'url': 'https://hcompany.ai'
    }
]

summary = """KW 14/2026 markiert eine historische Woche für Open-Source-KI: Google veröffentlichte Gemma 4 erstmals unter der Apache-2.0-Lizenz — ein Paradigmenwechsel, der proprietäre Cloud-Modelle direkt herausfordert. Gleichzeitig setzt H Companys Holo3 mit 78,85% auf dem OSWorld-Benchmark einen neuen Massstab für Computer-Use-Agenten und übertrifft GPT-5.4 und Claude Opus 4.6 — als europäisches Unternehmen unter Apache 2.0. Im Bereich Datenschutz sticht Atomic Chat hervor: Das Open-Source-Tool läuft vollständig offline auf dem Mac, ohne dass auch nur ein Byte das Gerät verlässt. Abgerundet wird die Woche durch Noons Stealth-Exit mit $44 Millionen für das erste KI-native Design-Tool auf Production-Code sowie Perplexity Computers neues Tax-Modul für US-Steuererklärungen."""

trend = "Open-Source überholt Cloud-KI: Gemma 4 (Apache 2.0) und Holo3 (Apache 2.0, EU) zeigen, dass frontier-nahe KI-Qualität jetzt on-premise, kostenlos und ohne Lizenzrisiko verfügbar ist — historischer Moment für DSGVO-konforme Unternehmen"

stars = "Google Gemma 4 (9.5/10): Historischer Meilenstein — Frontier Open-Source-KI unter Apache 2.0, von Raspberry Pi bis H100, vollständig DSGVO-konform on-premise betreibbar"

html = create_html(
    kw="14",
    date="05.04.2026",
    summary=summary,
    trend=trend,
    stars=stars,
    tools=tools
)

with open('/home/ubuntu/ki-tool-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html für KW 14/2026 erfolgreich erstellt!")
