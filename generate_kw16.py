#!/usr/bin/env python3
"""
KW 16/2026 - Homepage Generator
Datum: 19. April 2026
Tools: Fathom 3.0, Figma for Agents, Google Gemma 4, Perplexity Computer (Personal CFO), Claude Opus 4.7
"""

import json
import sys
sys.path.insert(0, '/home/ubuntu/ki-tool-website')
from generate_html_from_analysis import create_html

# ── Daten ──────────────────────────────────────────────────────────────────────

KW = "16"
DATE = "19.04.2026"

SUMMARY = (
    "KW 16/2026 stand ganz im Zeichen von Agentic Workflows und der tiefen Integration von KI "
    "in bestehende Systeme. Anthropic veröffentlichte mit Claude Opus 4.7 sein stärkstes Modell "
    "für autonome Aufgaben: 87.6% auf SWE-bench Verified, ein 1-Million-Token-Kontextfenster ohne "
    "Preisaufschlag und 3.3x höhere Bildauflösung. Figma schliesst mit seinem neuen MCP-Server die "
    "fundamentale Lücke zwischen KI-generiertem Code und Design-Systemen und ermöglicht erstmals "
    "echte bidirektionale Workflows. Perplexity erweitert seinen Desktop-Agenten um eine "
    "'Personal CFO'-Funktion mit Echtzeit-Bankdaten-Anbindung via Plaid. Fathom 3.0 löst das "
    "weit verbreitete Problem der 'Bot-Müdigkeit' in Video-Calls mit bot-freier Aufzeichnung. "
    "Google Gemma 4 bleibt mit seiner Kombination aus multimodalen Fähigkeiten und vollständiger "
    "Datensouveränität die beste Wahl für DSGVO-kritische Deployments."
)

STARS = (
    "Figma for Agents (10/10) & Claude Opus 4.7 (10/10): Figma schliesst die Design-Code-Lücke, "
    "Anthropic setzt den neuen Massstab für Agentic Coding"
)

TREND = (
    "Agentic Workflows werden produktionsreif — KI-Agenten greifen auf Design-Systeme, Bankkonten "
    "und Codebases zu und liefern Ergebnisse, die ohne menschliche Nachkorrektur deploybar sind"
)

TOOLS = [
    {
        'name': 'Fathom 3.0',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 9.0,
        'tagline': 'Bot-freie Meeting-KI — Aufzeichnung ohne sichtbaren Teilnehmer, CRM-Sync, Account-weite Insights',
        'description': (
            'Fathom 3.0 ist ein KI-gestützter Meeting-Assistent, der Gespräche aufzeichnet, '
            'transkribiert und zusammenfasst. Das Major-Update vom 15. April 2026 führt eine '
            '"bot-freie" Aufzeichnungsoption ein, die Meetings ohne sichtbaren Teilnehmer-Bot '
            'dokumentiert. Die neue "Ask Fathom"-Funktion ermöglicht es, über alle Team-Calls '
            'hinweg zu suchen und zu analysieren. Starke CRM-Integrationen (Salesforce, HubSpot) '
            'mit automatischer Deal-Zusammenfassung runden das Update ab.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': (
                    'Free: $0 (unlimitierte Aufzeichnungen, Transkriptionen, Basis-Zusammenfassungen). '
                    'Team: $15/Nutzer/Monat (globale Suche, Team-Playlists, SSO). '
                    'Business: $25/Nutzer/Monat (CRM-Sync, Deal-Views, Coaching-Metriken).'
                )
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': (
                    'Bot-freie Aufzeichnung löst das "Bot-Müdigkeits"-Problem in Video-Calls. '
                    'Ask Fathom: Suche und Analyse über alle Team-Meetings hinweg. '
                    'Automatische CRM-Befüllung (Salesforce, HubSpot). '
                    'Erweiterte LLM-Integrationen: Claude, ChatGPT, Gemini wählbar. '
                    'Sehr grosszügiger Free-Tier für Einzelpersonen.'
                )
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': (
                    'Serverstandort: USA. DSGVO: DPF-zertifiziert, SCCs für EU-Kunden verfügbar. '
                    'Business-Plan: Individuelle Data Retention Policies konfigurierbar. '
                    'Kein EU-Serverstandort als Standard. Für hochsensible Daten zu berücksichtigen. (6.5/10)'
                )
            }
        ],
        'verdict': (
            'Fathom 3.0 ist ein exzellentes Tool für Teams, die ihre Meeting-Kultur professionalisieren '
            'wollen, ohne die Teilnehmer mit Bots zu irritieren. Die bot-freie Aufzeichnung löst ein '
            'echtes Problem. Besonders für Sales- und Customer-Success-Teams bietet die CRM-Integration '
            'einen massiven Effizienzgewinn. Der grosszügige Free-Tier macht den Einstieg risikolos.'
        ),
        'url': 'https://fathom.video'
    },
    {
        'name': 'Figma for Agents',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 10.0,
        'tagline': 'MCP-Server verbindet KI-Agenten mit Design-Systemen — bidirektionale Code-Canvas-Workflows',
        'description': (
            'Figma for Agents ist ein neues Model Context Protocol (MCP) Tool, das es KI-Agenten '
            '(wie Claude Code oder Cursor) ermöglicht, direkt in Figma-Dateien zu arbeiten. '
            'Zwei Kerntools: generate_figma_design (HTML zu editierbaren Figma-Layern) und '
            'use_figma (KI-Agenten erstellen/bearbeiten Designs mit echten Komponenten und Variablen). '
            'Das Tool schliesst die fundamentale Lücke zwischen KI-generiertem Code und dem '
            'tatsächlichen Design-System eines Unternehmens.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': (
                    'MCP-Tool kostenlos. Erfordert Figma Professional ($12/Monat) oder höher. '
                    'API-Kosten für genutztes LLM (z.B. Claude Opus 4.7: $5/MTok Input). '
                    'Code Connect (Figma-zu-Codebase-Mapping): Im Professional Plan inklusive.'
                )
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': (
                    'Löst das "Looks AI-generated"-Problem: KI nutzt echte Tokens, Variablen und Komponenten. '
                    'Bidirektionaler Workflow: Design-to-Code UND Code-to-Design. '
                    'Skills (Markdown-Dateien) steuern das Agenten-Verhalten kontextbezogen. '
                    'Code Connect mappt Figma-Komponenten zu exakten Codebase-Entsprechungen. '
                    'Standardisiertes MCP-Protokoll: funktioniert mit Claude, Cursor, Codex.'
                )
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': (
                    'Serverstandort: USA (Figma-Infrastruktur). DSGVO: Enterprise-Compliance-Optionen verfügbar. '
                    'MCP läuft lokal (http://127.0.0.1:3845/sse) — Designdaten verlassen den Rechner nicht direkt. '
                    'Datenverarbeitung durch LLM-Anbieter abhängig vom gewählten Modell. (7.0/10)'
                )
            }
        ],
        'verdict': (
            'Für Produktteams, die bereits stark auf Figma und KI-Coding-Assistenten setzen, ist dieses '
            'Tool ein absoluter Game-Changer. Es verhindert das "Ausfransen" von Design-Systemen durch '
            'KI-generierte UIs und ermöglicht echte Zusammenarbeit zwischen Designern und Entwicklern '
            'auf einem neuen Niveau. Voraussetzung: ein gut gepflegtes, strukturiertes Design-System.'
        ),
        'url': 'https://www.figma.com/blog/the-tldr-on-mcp/'
    },
    {
        'name': 'Google Gemma 4',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA/WISSEN',
        'rating': 9.0,
        'tagline': 'Multimodales Open-Source-Modell lokal — 256K Kontext, Text/Bild/Audio/Video, 100% DSGVO-konform',
        'description': (
            'Gemma 4 ist Googles neueste Familie offener, multimodaler KI-Modelle mit bis zu 256K '
            'Token Kontext. Verfügbar in Grössen von 2B bis 31B Parametern, optimiert für lokales '
            'Deployment von Laptops bis Servern. Die E2B/E4B-Varianten unterstützen nativ Text, '
            'Bild, Audio und Video. Unter der offenen Gemma-Lizenz (ähnlich Apache 2.0) kostenlos '
            'nutzbar und kommerziell einsetzbar via Ollama, LM Studio oder Hugging Face.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': (
                    'Kostenlos. Gemma-Lizenz (ähnlich Apache 2.0) — freie kommerzielle Nutzung. '
                    'Deployment via Ollama, LM Studio, Hugging Face (kostenlos). '
                    'Google AI Studio API: Kostenloser Tier verfügbar, danach Pay-as-you-go.'
                )
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': (
                    'Native Multimodalität (Text, Bild, Audio, Video) auch bei kleinen Modellen (E2B/E4B). '
                    '256K Token Kontextfenster — ideal für lange Dokumente. '
                    'Exzellentes Leistungs-/Grössen-Verhältnis: 27B-Modell schlägt viele 70B-Modelle. '
                    'Vollständig lokales Deployment möglich — null Cloud-Abhängigkeit. '
                    'Optimiert für Quantisierung (4-bit, 8-bit) für Consumer-Hardware.'
                )
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': (
                    'Lokales Deployment: Maximaler Datenschutz — keine Daten verlassen das Gerät. '
                    'DSGVO: Vollständig konform bei lokalem Betrieb (kein externer Datentransfer). '
                    'Self-Hosting: Vollständig unterstützt (Ollama, vLLM, llama.cpp). '
                    'Ideal für hochsensible Daten (Medizin, Recht, Finanzen). (10/10 bei lokalem Betrieb)'
                )
            }
        ],
        'verdict': (
            'Gemma 4 ist ein Meilenstein für Open-Source-KI und die erste Wahl für Unternehmen, '
            'die aus Compliance- oder Sicherheitsgründen keine Cloud-LLMs nutzen dürfen. '
            'Die Kombination aus multimodalen Fähigkeiten, 256K Kontext und vollständiger '
            'Datensouveränität ist einzigartig. Für DSGVO-kritische Deployments gibt es aktuell '
            'keine bessere Option.'
        ),
        'url': 'https://ai.google.dev/gemma'
    },
    {
        'name': 'Perplexity Computer (Personal CFO)',
        'category': 'research',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 8.0,
        'tagline': 'KI-Agent mit Echtzeit-Bankdaten — Ausgabenanalyse, Budget-Planung, Net-Worth-Tracking via Plaid',
        'description': (
            'Perplexity hat seinen Desktop-Agenten "Computer" um eine "Personal CFO"-Funktion '
            'erweitert. Durch tiefe Integration mit Plaid greift die KI sicher auf Bankkonten, '
            'Kreditkarten und Kredite zu und liefert personalisierte Finanzanalysen. '
            'Der Agent kategorisiert Ausgaben automatisch, erstellt Heatmaps, generiert '
            'massgeschneiderte Budgetpläne und konsolidiert alle Vermögenswerte in einer '
            'Echtzeit-Übersicht. Rollout: 17. April 2026, aktuell USA/Kanada.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': (
                    'Perplexity Pro: $20/Monat (Computer-Feature inklusive). '
                    'Perplexity Max: $200/Monat (unlimitierte Computer-Nutzung, alle Frontier-Modelle). '
                    'Plaid-Anbindung: Kostenlos im Abonnement inklusive.'
                )
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': (
                    'Erste KI, die Recherche-Intelligenz mit persönlichen Echtzeit-Finanzdaten verbindet. '
                    'Automatische Ausgaben-Kategorisierung und Heatmap-Visualisierung. '
                    'Konsolidiertes Net-Worth-Tracking über alle Konten. '
                    'Dialogbasierte Finanzanalyse — ersetzt spezialisierte Finanz-Apps. '
                    'Plaid-Integration: Sicherer, regulierter Datenzugang zu 12.000+ Banken.'
                )
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': (
                    'Finanzdaten via Plaid (stark regulierter, SOC2-zertifizierter Provider). '
                    'Serverstandort: USA. Aktuell nur USA/Kanada verfügbar (Plaid-Restriktionen). '
                    'DSGVO: Nicht anwendbar (EU-Rollout noch nicht angekündigt). '
                    'Hohes Vertrauen in KI-Zugriff auf Bankdaten erforderlich. (5.0/10 für EU)'
                )
            }
        ],
        'verdict': (
            'Ein faszinierender Blick in die Zukunft von KI-Agenten, die nicht nur das Web durchsuchen, '
            'sondern als persönliche Analysten auf private Daten-Silos zugreifen. Konzeptionell '
            'wegweisend. Für europäische Nutzer aufgrund der regionalen Beschränkung aktuell nicht '
            'nutzbar. Wer in den USA ist und Perplexity Pro bereits nutzt, sollte es testen.'
        ),
        'url': 'https://www.perplexity.ai'
    },
    {
        'name': 'Claude Opus 4.7',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 10.0,
        'tagline': '87.6% SWE-bench Verified, 1M Token Kontext ohne Aufpreis, 3.3x bessere Vision — der neue Massstab',
        'description': (
            'Claude Opus 4.7 ist das neueste und stärkste Modell von Anthropic, veröffentlicht am '
            '16. April 2026. Es ist speziell für Agentic Coding, komplexe Systemarchitekturen und '
            'langlaufende, autonome Aufgaben entwickelt. Das 1-Million-Token-Kontextfenster ist ohne '
            'Preisaufschlag verfügbar. Die neue adaptive Thinking-Engine ersetzt manuelle '
            'Budget-Parameter. Hochauflösende Bildverarbeitung bis 3.75 Megapixel (3.3x mehr als '
            'Opus 4.6) macht es zum stärksten Modell für visuelle Verifikation und Dokumentenanalyse.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': (
                    'API: $5/MTok Input, $25/MTok Output (identisch zu Opus 4.6). '
                    '1M Token Kontext: Kein Preisaufschlag. '
                    'Prompt Caching: $6.25/MTok Write, $0.50/MTok Read. '
                    'Batch Processing: 50% Rabatt auf normale Preise. '
                    'Hinweis: Neuer Tokenizer kann effektive Kosten um bis zu 35% erhöhen.'
                )
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': (
                    '87.6% auf SWE-bench Verified — neuer State-of-the-Art für Agentic Coding. '
                    '1M Token Kontext ohne Preisaufschlag (einzigartig am Markt). '
                    'Hochauflösende Vision: bis 3.75MP / 2576px (3.3x mehr als Opus 4.6). '
                    'Adaptive Thinking Engine: xhigh-Modus für maximale Reasoning-Tiefe. '
                    'Task Budget Feature: Modell plant Token-Verbrauch über gesamten Agenten-Loop.'
                )
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': (
                    'Enterprise: Zero-Data-Retention-Agreements verfügbar (kein Modell-Training). '
                    'EU-Deployment: Via AWS Bedrock (Frankfurt) oder Google Vertex AI (EU-Regionen). '
                    'DSGVO: Vollständig konform bei EU-Serverstandort-Konfiguration. '
                    'Self-Hosting: Nicht verfügbar (Cloud-only). (8.5/10 mit EU-Konfiguration)'
                )
            }
        ],
        'verdict': (
            'Claude Opus 4.7 ist kein Modell für einfache Chat-Anfragen, sondern eine Heavy-Duty-Engine '
            'für Entwickler und Unternehmen, die komplexe, autonome Agenten-Workflows bauen. '
            'Wer höchste Zuverlässigkeit bei Code-Generierung, Dokumentenanalyse und visueller '
            'Verifikation sucht, kommt an diesem Modell aktuell nicht vorbei. Der fehlende '
            'Preisaufschlag für 1M-Token-Kontext ist ein echter Wettbewerbsvorteil.'
        ),
        'url': 'https://www.anthropic.com/claude'
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

output_path = '/home/ubuntu/ki-tool-website/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ index.html für KW {KW}/2026 erfolgreich generiert!")

# ── Archiv-HTML (KW 15 archivieren) ───────────────────────────────────────────

archive_html_path = '/home/ubuntu/ki-tool-website/archiv/2026/kw15-2026-04-12.html'

# Lese die bisherige index.html (vor dem Überschreiben) — sie ist jetzt KW15
# Wir erstellen eine Kopie aus dem Git-Stand
import subprocess
result = subprocess.run(
    ['git', 'show', 'HEAD:index.html'],
    capture_output=True, text=True,
    cwd='/home/ubuntu/ki-tool-website'
)
if result.returncode == 0:
    with open(archive_html_path, 'w', encoding='utf-8') as f:
        f.write(result.stdout)
    print(f"✅ KW 15 archiviert als: {archive_html_path}")
else:
    print(f"⚠️  Archivierung KW15 fehlgeschlagen: {result.stderr}")

# ── Archive-Index aktualisieren ────────────────────────────────────────────────

archive_index_path = '/home/ubuntu/ki-tool-website/archiv/data/archive-index.json'

with open(archive_index_path, 'r', encoding='utf-8') as f:
    archive = json.load(f)

# Vorherige aktuelle Woche (KW 15) auf permanente URL umschreiben
for entry in archive['analysen']:
    if entry.get('url') == 'index.html':
        entry['url'] = 'archiv/2026/kw15-2026-04-12.html'
        print(f"✅ KW {entry['kw']} URL auf Archiv-Pfad umgeschrieben")
        break

# Neuen Eintrag für KW 16 vorne einfügen
new_entry = {
    "kw": 16,
    "jahr": 2026,
    "datum": "2026-04-19",
    "url": "index.html",
    "tools": [
        {
            "name": "Fathom 3.0",
            "kategorie": "Text",
            "bewertung": 9.0,
            "kurzbeschreibung": "Bot-freie Meeting-KI — Aufzeichnung ohne sichtbaren Teilnehmer, CRM-Sync, Account-weite Insights"
        },
        {
            "name": "Figma for Agents",
            "kategorie": "Design",
            "bewertung": 10.0,
            "kurzbeschreibung": "MCP-Server verbindet KI-Agenten mit Design-Systemen — bidirektionale Code-Canvas-Workflows"
        },
        {
            "name": "Google Gemma 4",
            "kategorie": "Data",
            "bewertung": 9.0,
            "kurzbeschreibung": "Multimodales Open-Source-Modell lokal — 256K Kontext, Text/Bild/Audio/Video, 100% DSGVO-konform"
        },
        {
            "name": "Perplexity Computer (Personal CFO)",
            "kategorie": "Recherche",
            "bewertung": 8.0,
            "kurzbeschreibung": "KI-Agent mit Echtzeit-Bankdaten — Ausgabenanalyse, Budget-Planung, Net-Worth-Tracking via Plaid"
        },
        {
            "name": "Claude Opus 4.7",
            "kategorie": "Agents",
            "bewertung": 10.0,
            "kurzbeschreibung": "87.6% SWE-bench Verified, 1M Token Kontext ohne Aufpreis, 3.3x bessere Vision — der neue Massstab"
        }
    ],
    "highlights": "Figma for Agents (10/10) & Claude Opus 4.7 (10/10): Figma schliesst die Design-Code-Lücke, Anthropic setzt den neuen Massstab für Agentic Coding",
    "trend": "Agentic Workflows werden produktionsreif — KI-Agenten greifen auf Design-Systeme, Bankkonten und Codebases zu und liefern deploybare Ergebnisse"
}

archive['analysen'].insert(0, new_entry)

with open(archive_index_path, 'w', encoding='utf-8') as f:
    json.dump(archive, f, ensure_ascii=False, indent=2)

print(f"✅ archive-index.json mit KW 16 aktualisiert ({len(archive['analysen'])} Einträge total)")
