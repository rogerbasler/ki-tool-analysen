#!/usr/bin/env python3
"""
KW 17/2026 - Homepage Generator
Datum: 26. April 2026
Tools: Chronicle, ChatGPT Images 2.0, DeepSeek V4, Gemini Deep Research Max, OpenAI Workspace Agents
"""
import json
import sys
sys.path.insert(0, '/home/ubuntu/ki-tool-website')
from generate_html_from_analysis import create_html

# ── Daten ──────────────────────────────────────────────────────────────────────
KW = "17"
DATE = "26.04.2026"
SUMMARY = (
    "KW 17 markiert eine Verdichtung im Bereich autonomer Workflows: OpenAI, Google und DeepSeek "
    "liefern gleichzeitig Produkte, die den Übergang von Einzelprompts zu dauerhaft laufenden "
    "Agenten vollziehen. ChatGPT Images 2.0 setzt mit Thinking-Bildgenerierung einen neuen "
    "Massstab im Design-Bereich. DeepSeek V4 schockt erneut mit Open-Source-Qualität auf "
    "Frontier-Niveau zu Bruchteilspreisen. Chronicle etabliert sich als ernsthafter "
    "PowerPoint-Konkurrent für Teams. Die eigentliche Botschaft der Woche: KI-Agenten werden "
    "zur Teaminfrastruktur, nicht mehr nur zum Einzelwerkzeug."
)
STARS = (
    "ChatGPT Images 2.0 (9/10) & DeepSeek V4 (9/10): Thinking-Bildgenerierung trifft "
    "Open-Source-Frontier — zwei Releases, die den Markt neu kalibrieren"
)
TREND = (
    "KI-Agenten werden Teaminfrastruktur — OpenAI Workspace Agents, Gemini Deep Research Max "
    "und DeepSeek V4 zeigen: Autonome Systeme laufen jetzt dauerhaft, nicht nur auf Abruf"
)

TOOLS = [
    {
        'name': 'Chronicle',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 8.0,
        'tagline': 'Cursor für Slides — KI-Präsentationen auf Enterprise-Niveau mit Agentic Workflows',
        'description': (
            'Chronicle ist ein KI-gestützter Präsentations-Maker, der sich explizit als "Cursor für Slides" '
            'positioniert. Das Tool generiert hochwertige, on-brand Präsentationen aus Texteingaben, URLs, '
            'PDFs oder bestehenden PowerPoint-Dateien. Im Gegensatz zu Gamma fokussiert Chronicle auf '
            'Qualität und Markenkonsistenz für Teams. Vertraut von 5.000+ Teams bei OpenAI, Apple, Vercel, '
            'Notion und Meta. Der Plus-Plan bringt Agentic Workflows, die echte Automatisierung ermöglichen.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (300 Tokens/Monat, unlimitierte Dokumente, PDF-Export). '
                           'Pro: $15/Nutzer/Monat (750 Tokens, alle KI-Modelle, kein Wasserzeichen). '
                           'Plus: $30/Nutzer/Monat (Agentic Workflows, PPT-Export, Custom Themes). '
                           'Max: $59/Nutzer/Monat (5.000 Tokens, Advanced Branding). '
                           'Jahresabrechnung spart 20%. Enterprise auf Anfrage.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Agentic Workflows (Plus) ermöglichen automatisierte Report-Generierung. '
                           'Breite Integrationslandschaft: Notion, Salesforce, HubSpot. '
                           'Ausgabequalität übertrifft Gamma deutlich — wirkt nicht KI-generiert. '
                           'PPT-Export, Custom Fonts und Themes ab Plus-Plan.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: USA (San Francisco). SOC 2 Type II zertifiziert. '
                           'Standardvertragsklauseln (SCCs) für EU-Kunden verfügbar. '
                           'Kein EU-Serverstandort als Standard. Self-Hosting nicht verfügbar. '
                           'Für DSGVO-kritische Branchen: Enterprise-Plan mit individuellem AVV empfohlen.'
            }
        ],
        'verdict': (
            'Chronicle ist der überzeugendste Anwärter auf den Platz als Standard-Präsentationstool '
            'für KI-affine Teams. Die Qualität übertrifft Gamma deutlich, der Preis ist fair. '
            'Für Schweizer und europäische Unternehmen mit strengen Datenschutzanforderungen bleibt '
            'der US-Serverstandort ein Hindernis. Für alle anderen: Sofort testen.'
        ),
        'url': 'https://chroniclehq.com'
    },
    {
        'name': 'ChatGPT Images 2.0',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 9.0,
        'tagline': 'Erstes Bildgenerierungsmodell mit Thinking — fehlerfreier Text, Web-Browsing, präzise Kontrolle',
        'description': (
            'ChatGPT Images 2.0 (gpt-image-2) ist OpenAIs neues Bildgenerierungsmodell vom 21. April 2026. '
            'Es ist das erste Bildgenerierungsmodell mit integrierter Thinking-Fähigkeit: Das Modell '
            'reflektiert vor der Generierung, kann Code ausführen, Websuchen durchführen und Logos '
            'aus dem Web abrufen. Das Ergebnis: drastisch verbesserte Text-in-Bild-Genauigkeit '
            '(keine Tippfehler, auch bei hunderten Wörtern), multilinguale Unterstützung und eine '
            'deutlich geringere "KI-Ästhetik" in professionellen Outputs.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'ChatGPT Plus/Pro: Im Abonnement enthalten ($20/$200/Monat). '
                           'API (gpt-image-2): $5/1M Input-Tokens, $30/1M Output-Tokens (Standard). '
                           '$10/1M Output-Tokens (Low Quality). '
                           'Codex App (mit Thinking): Codex-Credits ab $20/Monat. '
                           'Preise in USD.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Thinking-Modus: Modell plant vor der Generierung, nutzt Code und Web-Suche. '
                           'Fehlerfreier Text in Bildern, auch bei hunderten Wörtern und mehreren Sprachen. '
                           'Aktives Web-Browsing für Logos und Referenzbilder. '
                           'Nahtlose Integration in ChatGPT-Workflows und Codex. '
                           'Deutlich weniger "KI-Ästhetik" bei professionellen Outputs.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: USA. Enterprise/Business: Daten nicht für Training genutzt. '
                           'EU-US Data Privacy Framework (DPF) zertifiziert. SCCs verfügbar. '
                           'Kein EU-Serverstandort. Parallel lanciert: OpenAI Privacy Filter '
                           '(Open-Source-Modell zur lokalen PII-Erkennung). (6.5/10)'
            }
        ],
        'verdict': (
            'ChatGPT Images 2.0 ist der bedeutendste Sprung in der KI-Bildgenerierung seit Midjourney V6. '
            'Die Kombination aus Reasoning und Generierung löst das fundamentale Problem der "KI-Ästhetik" '
            'bei professionellen Anwendungsfällen. Für Marketing-Teams, die präzise, textreiche Visuals '
            'benötigen, ist dieses Tool ein Game-Changer. Der US-Serverstandort bleibt für DSGVO-kritische '
            'Workflows ein Einschränkungsfaktor.'
        ),
        'url': 'https://openai.com/index/introducing-chatgpt-images-2-0/'
    },
    {
        'name': 'DeepSeek V4',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA',
        'rating': 9.0,
        'tagline': '1,6T Open-Source-Parameter, 1M Kontext als Standard — Frontier-Qualität zu Bruchteilspreisen',
        'description': (
            'DeepSeek V4 ist das neueste Open-Source-Sprachmodell von DeepSeek, veröffentlicht am '
            '24. April 2026. Zwei Varianten: V4-Pro (1,6T Parameter total, 49B aktiv) und V4-Flash '
            '(284B total, 13B aktiv). Beide unterstützen standardmässig 1 Million Token Kontext und '
            'kombinieren Thinking- und Non-Thinking-Modus. Laut Benchmarks übertrifft V4-Pro alle '
            'Open-Source-Modelle in Coding, Mathematik und Reasoning. Vollständig open-sourced '
            'auf HuggingFace unter Modified MIT License — self-hostbar für vollständige DSGVO-Konformität.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'V4-Flash API: $0.028/1M Input (Cache Hit), $0.14/1M (Cache Miss), $0.28/1M Output. '
                           'V4-Pro API: $0.036/1M Input (75% Rabatt bis 05.05.2026, danach $0.145/1M). '
                           '$0.435/1M Cache Miss, $0.87/1M Output. '
                           'Open-Source-Gewichte: Kostenlos auf HuggingFace. Self-Hosting möglich.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Open-Source SOTA: Übertrifft alle anderen Open-Source-Modelle in Agentic Coding. '
                           '1M Token Kontext als Standard (nicht als Aufpreis). '
                           'Novel Attention: Token-wise Compression + DeepSeek Sparse Attention. '
                           'Dual-Mode (Thinking/Non-Thinking) für flexible Nutzung. '
                           'Nahtlose Integration mit Claude Code, OpenClaw und OpenCode.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'API-Server: China (Hangzhou) — für EU-Unternehmen datenschutzrechtlich problematisch. '
                           'Keine SCCs, kein DPF, kein EU-Serverstandort für die API. '
                           'ABER: Open-Source-Gewichte ermöglichen vollständiges Self-Hosting auf EU-Servern. '
                           'V4-Flash self-hosted via vLLM/SGLang = vollständige DSGVO-Konformität. '
                           'Politisches Risiko: US-Exportbeschränkungen möglich.'
            }
        ],
        'verdict': (
            'DeepSeek V4 ist der wichtigste Open-Source-Release des Jahres. Für Unternehmen, die '
            'Datensouveränität benötigen, ist V4-Flash self-hosted die überzeugendste Option: '
            'Frontier-nahe Qualität, vollständige Kontrolle, minimale Kosten. Die direkte API-Nutzung '
            'bleibt für europäische Unternehmen ein Compliance-Problem. Das eigentliche Problem ist '
            'nicht die Qualität — sondern die Frage, ob man die Infrastruktur für Self-Hosting aufbauen will.'
        ),
        'url': 'https://api-docs.deepseek.com/news/news260424'
    },
    {
        'name': 'Gemini Deep Research Max',
        'category': 'recherche',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 9.0,
        'tagline': 'MCP-Support + native Charts + Gemini 3.1 Pro — autonome Recherche auf Enterprise-Niveau',
        'description': (
            'Google hat am 21. April 2026 zwei neue Versionen seines autonomen Recherche-Agenten lanciert: '
            'Deep Research (für interaktive Oberflächen, optimiert auf Geschwindigkeit) und Deep Research Max '
            '(für asynchrone, maximale Tiefe). Beide basieren auf Gemini 3.1 Pro. Drei entscheidende '
            'Neuerungen: MCP-Support (Anbindung an beliebige Datenquellen wie FactSet, S&P Global, PitchBook), '
            'native Chart-Generierung und kollaborative Planung. Das Modell kann gleichzeitig das offene Web, '
            'proprietäre Datenbanken via MCP, hochgeladene Dateien und Google-Dienste durchsuchen.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free Tier: Gemini 3.1 Flash (limitiert). '
                           'Paid API Deep Research: Gemini 3.1 Pro-Preise (~$1.25/1M Input, $5/1M Output). '
                           'Deep Research Max: Höhere Kosten durch Extended Compute (dynamisch berechnet). '
                           'Google Cloud Enterprise: Unternehmensvertrag mit EU-Datenresidenz-Option.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'MCP-Support: Anbindung an beliebige Datenquellen macht es zum universellen Recherche-Hub. '
                           'Native Charts und Infografiken direkt im Bericht (HTML oder Nano Banana). '
                           'Kollaborative Planung: Nutzer prüfen und verfeinern den Recherche-Plan vor Ausführung. '
                           'Multimodale Eingaben: PDFs, CSVs, Bilder, Audio, Video. '
                           'Real-time Streaming der Zwischenschritte. Partnerschaften mit FactSet, S&P Global, PitchBook.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Google Cloud: ISO 27001, SOC 2/3, DSGVO-konform. '
                           'EU-Rechenzentren verfügbar (Frankfurt, Eemshaven). '
                           'API-Nutzer: Daten standardmässig nicht für Training genutzt. '
                           'SCCs und AVV für europäische Kunden. '
                           'EU-Datenresidenz via Google Cloud Enterprise. (8.0/10)'
            }
        ],
        'verdict': (
            'Gemini Deep Research Max ist das leistungsfähigste Recherche-Tool, das aktuell als API '
            'verfügbar ist. Die Kombination aus MCP-Support, nativen Visualisierungen und dem Zugang '
            'zu Google-Partnerdaten macht es besonders für Finanz-, Beratungs- und Forschungsorganisationen '
            'attraktiv. Die EU-Serveroptionen lösen das DSGVO-Problem. Der entscheidende Unterschied zu '
            'Perplexity: nicht nur Suche, sondern vollständige Analyse-Pipelines.'
        ),
        'url': 'https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/'
    },
    {
        'name': 'OpenAI Workspace Agents',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 9.0,
        'tagline': 'Codex-Agenten für Teams — dauerhaft laufend, Slack-integriert, Enterprise-Controls',
        'description': (
            'OpenAI hat am 22. April 2026 Workspace Agents in ChatGPT lanciert, die Nachfolger der '
            'Custom GPTs für Teams und Unternehmen. Workspace Agents sind Codex-gestützte Agenten, '
            'die dauerhaft in der Cloud laufen, auf externe Tools zugreifen, Workflows automatisieren '
            'und in Slack integriert werden können. Einmal konfiguriert, von allen genutzt, kontinuierlich '
            'verbessert. Verfügbar für ChatGPT Business, Enterprise, Edu und Teachers-Pläne. '
            'Bis 06. Mai 2026 kostenlos, danach Credit-basiertes Pricing.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'ChatGPT Business: $30/Nutzer/Monat (Workspace Agents in Research Preview). '
                           'ChatGPT Enterprise: ~$60/Nutzer/Monat (mit Admin-Controls und Compliance API). '
                           'Workspace Agents kostenlos bis 06. Mai 2026. '
                           'Danach: Credit-basiertes Pricing (Preise noch nicht final kommuniziert).'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Codex-Backbone: Agenten schreiben und führen Code aus, erledigen mehrstufige Tasks. '
                           'Slack-Integration: Agenten arbeiten dort, wo Teams bereits kommunizieren. '
                           'Schedule-Funktion: Agenten laufen auch ohne menschliche Interaktion. '
                           'Compliance API: Vollständige Sichtbarkeit über alle Agenten-Konfigurationen. '
                           'Eingebauter Prompt-Injection-Schutz. Nahtloser Übergang von Custom GPTs.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: USA. Enterprise: Daten nicht für Training genutzt, 30 Tage Retention. '
                           'SOC 2 Type II zertifiziert. EU-US Data Privacy Framework (DPF). SCCs verfügbar. '
                           'Compliance API: Admins sehen alle Agenten-Konfigurationen, Updates und Runs. '
                           'Kein EU-Serverstandort. (6.5/10)'
            }
        ],
        'verdict': (
            'Workspace Agents sind der bisher überzeugendste Versuch, KI-Agenten als Teaminfrastruktur '
            'zu etablieren. Die Kombination aus Codex-Intelligenz, Slack-Integration und Enterprise-Controls '
            'macht sie für mittelgrosse bis grosse Unternehmen sofort relevant. Das Credit-Pricing ab Mai '
            'wird der entscheidende Faktor für die Adoption sein. Was oft unterschätzt wird: Die Compliance '
            'API ist für Enterprise-Kunden ein echtes Differenzierungsmerkmal.'
        ),
        'url': 'https://openai.com/index/introducing-workspace-agents-in-chatgpt/'
    }
]

# ── HTML generieren ────────────────────────────────────────────────────────────
html = create_html(
    kw=KW,
    date=DATE,
    summary=SUMMARY,
    trend=TREND,
    stars=STARS,
    tools=TOOLS
)

# ── Speichern ──────────────────────────────────────────────────────────────────
with open('/home/ubuntu/ki-tool-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ KW {KW} Homepage erfolgreich generiert!")
print(f"   Datei: /home/ubuntu/ki-tool-website/index.html")
print(f"   Tools: {', '.join(t['name'] for t in TOOLS)}")
