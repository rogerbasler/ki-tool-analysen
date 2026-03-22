#!/usr/bin/env python3
"""
Generiert die index.html für KW 12/2026
"""
import sys
sys.path.insert(0, '/home/ubuntu/ki-tool-website')
from generate_html_from_analysis import create_html

tools = [
    {
        'name': 'Fathom Commentary Writer',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 8.5,
        'tagline': 'KI-Finanzkommentar mit symbolischer Attribution — jede Zahl bis zur Quelle nachverfolgbar',
        'description': 'Fathom Commentary Writer richtet sich an Buchhalter, CFOs und Finance-Teams, die Finanzberichte mit kontextbewussten und nachvollziehbaren KI-Kommentaren anreichern wollen. Das Besondere: Jede von der KI generierte Aussage ist durch "symbolische Attribution" bis zur Rohdatenquelle zurückverfolgbar — ein Durchbruch für den Einsatz von KI in regulierten Finanzumgebungen. Das Tool berücksichtigt strategische Unternehmensziele und saisonale Effekte und integriert sich nahtlos in bestehende Fathom-Workflows.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Starter: $53/Monat (1 Unternehmen). Silver: $280/Monat (10 Unternehmen). Gold: $400/Monat (25 Unternehmen). 14-tägige kostenlose Testversion verfügbar, kein dauerhafter Free Tier.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Symbolische Attribution: Jede KI-generierte Zahl kann angeklickt und bis zur Rohdatenquelle zurückverfolgt werden. Löst das Halluzinations-Problem in Finanzberichten. Business Context: KI berücksichtigt strategische Unternehmensziele und saisonale Effekte.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'DSGVO-konform. Serverstandort: AWS in den USA und Kanada; für EU-Kunden ist eine EU-Isolation-Option mit Servern in Deutschland/Finnland verfügbar. Data Processing Agreement (DPA) für europäische Kunden vorhanden. (8.0/10)'
            }
        ],
        'verdict': 'Für Finanzabteilungen und Steuerberater ist der Commentary Writer ein massiver Produktivitätsgewinn. Die Nachvollziehbarkeit der KI-Aussagen (Attribution) ist genau das Feature, das bisherigen KI-Textgeneratoren im Finanzbereich fehlte, um Vertrauen bei Geschäftsführern aufzubauen. Für Einzelunternehmer ist der Einstiegspreis hoch, für Finance-Teams ab 3 Personen jedoch klar gerechtfertigt.',
        'url': 'https://www.fathomhq.com/'
    },
    {
        'name': 'Gamma Imagine',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 9.5,
        'tagline': 'KI-natives Design-Canvas für Infografiken, Logos und Marketing-Assets via Texteingabe',
        'description': 'Am 17. März 2026 lancierte Gamma sein bisher grösstes Update: Gamma Imagine, eine KI-native Design-Plattform, die Logos, Infografiken, Social-Media-Grafiken und Poster aus einfachen Textbeschreibungen generiert. Gamma hat bereits fast 100 Millionen Nutzer und eine Bewertung von $2.1 Milliarden (Series B, a16z). Das Update positioniert Gamma als direkte Konkurrenz zu Canva und Adobe — mit einem entscheidenden Vorteil: Gamma Imagine übernimmt automatisch die Brand-Guidelines des Teams und integriert sich nahtlos in ChatGPT, Claude, Zapier und Atlassian.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (400 Credits bei Anmeldung). Plus: $10/Monat ($8/Monat jährlich) — erweiterte KI-Modelle, kein Wasserzeichen. Pro: $20/Monat ($15/Monat jährlich) — Premium-Modelle, API-Zugang, Custom Fonts.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Automatische Brand-Konsistenz über alle generierten Assets. Smart Charts: Interaktive Datenvisualisierungen mit automatischer Corporate-Identity-Übernahme. Integrationen in ChatGPT, Claude, Zapier, Make, n8n und Atlassian. Über 100 remixbare Templates.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'DSGVO-konform. EU-Repräsentanz in Dresden, Deutschland. DPA standardmässig verfügbar. SOC 2 Type II zertifiziert. Für DACH-Teams eine der stärksten Datenschutzpositionen unter Design-KI-Tools. (9.0/10)'
            }
        ],
        'verdict': 'Gamma Imagine ist das Tool der Woche — und eines der bedeutendsten KI-Design-Launches des Jahres. Für Marketing-Teams, Gründer und Berater ohne eigene Designer ist es ein Game-Changer: professionelle, markenkonforme Visualisierungen in Sekunden. Canva bleibt stärker bei Print und manueller Pixel-Kontrolle, aber im B2B-Knowledge-Worker-Segment übernimmt Gamma die Führung.',
        'url': 'https://gamma.app/'
    },
    {
        'name': 'Genie by Databox',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA/WISSEN',
        'rating': 8.8,
        'tagline': 'KI-Analyst für Business-Daten — Natural Language Queries über eigene Metriken und KPIs',
        'description': 'Genie ist der integrierte KI-Analyst von Databox, der natürliche Sprachabfragen zu Unternehmensdaten ermöglicht. Statt auf den Data-Analysten zu warten, können Führungskräfte direkt mit ihren KPIs "chatten": "Warum sind die Leads diese Woche um 20% gesunken?" oder "Erstelle ein Dashboard für CAC nach Akquisitionskanal." Genie verbindet Daten aus HubSpot, Google Analytics, Stripe und über 100 weiteren Quellen und erklärt nicht nur was passiert ist, sondern analysiert Trends, um das Warum zu beantworten.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Professional: ab $159/Monat. Growth: ab $499/Monat. Premium: ab $799/Monat. Genie ist aktuell als Early-Access-Feature kostenlos in allen Paid-Plans (ausser Starter Agency) integriert. 14-tägige kostenlose Testversion.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Demokratisiert den Datenzugang: Keine SQL-Kenntnisse für komplexe Abfragen nötig. Multi-Channel-Fähigkeit: Verbindet Daten aus 100+ Quellen. Erklärt Anomalien und Trends in natürlicher Sprache. Shareable AI-Reports für Kunden und Team.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'DSGVO-konform. Serverstandort: Hauptsächlich USA (AWS). Databox bietet Standardvertragsklauseln (SCCs) und ein DPA für europäische Kunden an. Etablierter Anbieter mit dokumentierten Compliance-Prozessen. (7.5/10)'
            }
        ],
        'verdict': 'Genie löst ein massives Problem im Management: Den Flaschenhals bei der Datenanalyse. Für datengetriebene Unternehmen, die bereits Databox nutzen oder evaluieren, ist es ein extrem wertvolles Feature. Der hohe Einstiegspreis ($159/Monat) macht es für kleine Startups schwer zugänglich, für wachsende Teams mit mehreren Datenquellen ist der ROI jedoch schnell erreicht.',
        'url': 'https://databox.com/genie'
    },
    {
        'name': 'Perplexity Comet für iOS',
        'category': 'research',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 9.2,
        'tagline': 'KI-nativer Browser jetzt auf iPhone — Deep Research, Voice Mode und Agentic Browsing',
        'description': 'Am 18. März 2026 lancierte Perplexity den Comet-Browser für iOS. Comet kombiniert traditionelle Websuche mit KI-nativer Recherche: Statt blauer Links erhält man zitierte Antworten, Deep-Research-Reports und einen Agenten, der Formulare ausfüllt und Termine bucht. Die iOS-Version bringt Voice Mode (Fragen einsprechen), Hybrid-Suche (traditionell für lokale Anfragen, KI für komplexe Recherchen) und nahtlose Session-Synchronisation zwischen Desktop und iPhone. Optional: Integration mit Apple Health für personalisierte Gesundheitsrecherchen.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (mit Rate-Limits für Pro-Suchen). Pro: $17/Monat — Premium-Modelle (GPT-4.5, Claude 3.5 Opus), unlimitierte Pro-Suchen. Max: $34/Monat — höchste Limits und Performance. Studentenrabatt verfügbar.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Nahtlose Session-Synchronisation zwischen Desktop und iPhone. Deep Research Engine direkt in der Hosentasche. Voice Mode für freihändige Recherche. Agentic Browsing: KI füllt Formulare aus und bucht Termine. Hybrid-Suche für optimale mobile UX.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'DSGVO-konform. Server in USA und EU verfügbar. Opt-out für KI-Training mit Nutzerdaten. Im "Strict Mode" werden sensible Daten lokal verarbeitet. DPA vorhanden. Hinweis: Die Apple Health Integration ist optional und erfordert explizite Zustimmung. (8.0/10)'
            }
        ],
        'verdict': 'Comet für iOS bringt die beste KI-Suchmaschine nativ auf das iPhone und verändert die Art mobiler Recherche grundlegend — weg von blauen Links hin zu fertigen, zitierten Antworten. Ein absolutes Must-have für Wissensarbeiter. Die Apple Health Integration ist ein interessantes Feature, das jedoch aus Datenschutzperspektive sorgfältig abgewogen werden sollte.',
        'url': 'https://www.perplexity.ai/comet'
    },
    {
        'name': 'Skyvern',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 9.0,
        'tagline': 'Open-Source Browser-Automatisierung mit LLMs und Computer Vision — selbst hostbar',
        'description': 'Skyvern ist eine Open-Source-Plattform für KI-gestützte Browser-Automatisierung, die LLMs mit Computer Vision kombiniert. Im Gegensatz zu traditionellen RPA-Tools wie Playwright oder Selenium, die auf fragile DOM-Selektoren angewiesen sind, "sieht" Skyvern Websites wie ein Mensch und navigiert sie entsprechend. Das bedeutet: Wenn sich ein Button verschiebt oder eine Website ihr Design ändert, bricht das Script nicht. Skyvern löst auch komplexe Authentifizierungen (Logins, 2FA, CAPTCHAs, Cloudflare) nativ und ist vollständig selbst hostbar.',
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (1.000 Credits/Monat). Hobby: $29/Monat (30.000 Credits). Pro: $149/Monat (150.000 Credits, Team-Workspaces, 2FA-Management). Enterprise: Custom (unlimitiert, Self-Hosted, HIPAA, SOC2). Open Source: Kostenlos bei Self-Hosting via Docker.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Computer Vision statt DOM-Selektoren: Resistent gegen UI-Änderungen. Löst CAPTCHAs, Cloudflare und 2FA nativ. Open Source und vollständig selbst hostbar (Docker). MCP-ready für Integration in KI-Agenten-Workflows. Y Combinator-backed.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Durch Open-Source-Self-Hosting: 100% Datenkontrolle und DSGVO-Konformität möglich. Cloud-Version in den USA. Enterprise-Cloud: SOC 2 und HIPAA zertifiziert. Für DACH-Unternehmen mit hohen Datenschutzanforderungen ist Self-Hosting die empfohlene Option. (9.0/10 für Self-Hosted)'
            }
        ],
        'verdict': 'Skyvern ist ein Game-Changer für die Prozessautomatisierung und löst das grösste Problem traditioneller RPA-Tools: die Anfälligkeit für kleinste Website-Änderungen. Für Ops-Teams, die manuelle Copy-Paste-Arbeit eliminieren wollen, ist dies das Tool der Wahl. Die Open-Source-Option macht es besonders attraktiv für datenschutzbewusste Unternehmen und Entwickler, die volle Kontrolle behalten wollen.',
        'url': 'https://www.skyvern.com/'
    }
]

summary = """KW 12/2026 markiert den Übergang von allgemeinen KI-Assistenten zu tief integrierten, kontextbewussten Workflow-Tools. Gamma Imagine demonstriert, wie ein Design-Tool mit fast 100 Millionen Nutzern die Branche neu definiert: Nicht mehr Templates und manuelle Bearbeitung, sondern Prompt-to-Design in Sekunden mit automatischer Brand-Konsistenz. Skyvern zeigt, dass Browser-Automatisierung endlich zuverlässig wird — dank Computer Vision statt fragiler DOM-Selektoren. Genie by Databox demokratisiert den Datenzugang im Management, Perplexity Comet bringt Deep Research auf das iPhone, und Fathom Commentary Writer löst das Halluzinations-Problem im Finanzreporting durch symbolische Attribution."""

trend = "Agentic Workflows und kontextbewusste KI-Tools ersetzen allgemeine Chatbots — Gewinner sind Produkte, die tief in bestehende Workflows integriert sind und klare ROI-Logik haben"

stars = "Gamma Imagine (9.5/10): Grösster Design-KI-Launch des Jahres — 100M Nutzer, $2.1B Bewertung, und jetzt ein vollständiges Design-Canvas via Texteingabe"

html = create_html(
    kw="12",
    date="22.03.2026",
    summary=summary,
    trend=trend,
    stars=stars,
    tools=tools
)

with open('/home/ubuntu/ki-tool-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html für KW 12/2026 erfolgreich erstellt!")
