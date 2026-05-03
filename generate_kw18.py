import os
from generate_html_from_analysis import create_html

# ── Daten ──────────────────────────────────────────────────────────────────────
KW = "18"
DATE = "03.05.2026"

SUMMARY = (
    "In KW 18 sehen wir einen klaren Trend zur tiefen Integration von KI-Agenten in bestehende Workflows. "
    "Genspark for Word bringt leistungsstarke KI direkt in Microsoft 365, während Buda eine komplette "
    "Plattform für den Aufbau eines KI-Unternehmens bietet. TrafficClaw revolutioniert die Web-Analyse "
    "mit einem KI-Chat-Interface, und Bitgrain positioniert sich als leichtgewichtige, flexible Design-Alternative. "
    "Zudem erweitert Anthropic mit neuen Connectors die kreativen Möglichkeiten von Claude massiv."
)

STARS = (
    "Genspark for Word (9/10) & Buda (9/10): KI-Agenten werden nahtlos in den Arbeitsalltag integriert "
    "und übernehmen komplexe, mehrstufige Aufgaben."
)

TREND = (
    "Agentic Workflows in Standard-Tools — KI verlässt die isolierten Chat-Interfaces und "
    "wird direkt in Microsoft Office, Design-Software und Analytics-Dashboards eingebettet."
)

TOOLS = [
    {
        'name': 'Genspark for Word',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 9.0,
        'tagline': 'KI-Agenten nativ in Microsoft 365 — Draften, Editieren und Recherchieren direkt in Word',
        'description': (
            'Genspark for Word ist ein leistungsstarkes Add-in, das die KI-Agenten von Genspark direkt in '
            'Microsoft Word integriert. Durch eine neue strategische Partnerschaft mit Microsoft ermöglicht '
            'das Tool das Erstellen, Formatieren und Überarbeiten von Dokumenten ohne den Workflow zu verlassen. '
            'Es nutzt fortschrittliche Modelle (inkl. OpenAI und Anthropic), um tiefgehende Recherchen durchzuführen '
            'und kontextbezogene Bearbeitungen vorzunehmen.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free Tier: Grosszügiger kostenloser Plan mit 100-200 Credits/Tag. '
                           'Plus Plan: ca. $20/Monat für erweiterte Features und unlimitierte Chats. '
                           'Pro Plan: ca. $200/Monat für Power-User.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Nahtlose Integration in Microsoft 365. Nutzt "Agentic AI", um nicht nur Text zu generieren, '
                           'sondern Dokumente basierend auf tiefgehender Recherche intelligent zu strukturieren und zu formatieren.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Serverstandort: Microsoft Azure. Enterprise-Grade Security. '
                           'DSGVO-konform mit Standardvertragsklauseln. Spezielle Datenschutzrichtlinien für Enterprise-Kunden.'
            }
        ],
        'verdict': (
            'Ein Game-Changer für alle, die intensiv mit Microsoft Word arbeiten. Die nahtlose Integration '
            'und die starken Recherche-Fähigkeiten sparen enorm viel Zeit. Der grosszügige Free-Tier macht '
            'den Einstieg sehr attraktiv.'
        ),
        'url': 'https://www.genspark.ai/genspark-for-word'
    },
    {
        'name': 'Bitgrain',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 8.0,
        'tagline': 'Leichtgewichtiges Design-Studio im Browser — Fokus auf Texturen und Dithering',
        'description': (
            'Bitgrain startete als Dithering-Tool und hat sich zu einem vollwertigen, browserbasierten Design-Studio '
            'entwickelt. Es positioniert sich als leichtere, flexiblere Alternative zu Figma, speziell für die Erstellung '
            'von texturierten, auffälligen Visuals und Postern. Es bietet High-Fidelity Image Dithering und eine '
            'Vektor-SVG-Engine.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Aktuell komplett kostenlos nutzbar im Browser. Keine versteckten Kosten für die Grundfunktionen.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Spezialisiert auf Dithering und texturierte Designs. Läuft komplett im Browser ohne Installation. '
                           'Sehr schnelle und intuitive Bedienung für spezifische Design-Ästhetiken.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Verarbeitet Bilder lokal im Browser. Keine Speicherung von Nutzerdaten auf externen Servern '
                           'für die Grundfunktionen ersichtlich.'
            }
        ],
        'verdict': (
            'Eine erfrischende, spezialisierte Alternative zu den überladenen Standard-Design-Tools. '
            'Perfekt für schnelle, stylische Social-Media-Grafiken oder Poster mit einem einzigartigen Look.'
        ),
        'url': 'https://bitgrain.diptanshumahish.in/'
    },
    {
        'name': 'TrafficClaw',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA',
        'rating': 8.0,
        'tagline': 'Google Analytics Alternative mit KI-Chat und Echtzeit-3D-Globus',
        'description': (
            'TrafficClaw revolutioniert die Web-Analyse, indem es komplexe Dashboards durch ein natürliches '
            'KI-Chat-Interface ersetzt. Nutzer können einfach in plain English Fragen zu ihrem Traffic stellen. '
            'Zusätzlich bietet es einen beeindruckenden Echtzeit-3D-Globus für Besucher und integriert '
            'Social-Media-Mentions (X, Reddit) direkt als Social Proof.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: 10 KI-Credits zum Start. '
                           'Starter: $9/Monat (50 Credits). '
                           'Growth: $19/Monat (150 Credits). '
                           'Pro: $29/Monat (300 Credits, Telegram Bot).'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'KI-Chat für Analytics-Daten (powered by Google Gemini). Autonomer SEO-Bot für Keyword-Research '
                           'und Content-Decay-Warnungen. Einbettbarer Echtzeit-Globus.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Sichere Authentifizierung via OAuth 2.0. Strikte Datenisolation. '
                           'Daten werden nicht für KI-Training Dritter verwendet. DSGVO-konform.'
            }
        ],
        'verdict': (
            'Eine sehr innovative Herangehensweise an Web-Analytics. Der KI-Chat macht Daten für Nicht-Analysten '
            'zugänglich, und die visuellen Features (Globus) eignen sich hervorragend für Präsentationen.'
        ),
        'url': 'https://trafficclaw.com/'
    },
    {
        'name': 'Claude Creative Connectors',
        'category': 'recherche',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 9.0,
        'tagline': 'Anthropic integriert Claude direkt in professionelle Kreativ-Software',
        'description': (
            'Anthropic hat eine Reihe neuer MCP-Connectors veröffentlicht, die Claude direkt mit professionellen '
            'Kreativ-Tools verbinden. Dazu gehören Integrationen für Adobe Creative Cloud, Blender, Autodesk Fusion, '
            'Ableton und SketchUp. Claude kann nun als Tutor fungieren, Skripte schreiben oder Assets zwischen '
            'verschiedenen Programmen synchronisieren.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Teil der Claude-Abonnements. Pro Plan: $20/Monat. Max Plan: ab $100/Monat für Power-User.'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Ermöglicht die Steuerung komplexer Software via natürlicher Sprache. In Blender kann Claude '
                           'z.B. Szenen debuggen oder Batch-Änderungen via Python-API vornehmen.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Enterprise-Grade Security von Anthropic. SOC 2 Type II. Keine Verwendung von Kundendaten '
                           'für das Training der Basismodelle (bei API/Enterprise).'
            }
        ],
        'verdict': (
            'Ein massiver Schritt für kreative Workflows. Die Möglichkeit, komplexe Software wie Blender oder '
            'Adobe-Tools mit natürlicher Sprache zu steuern oder zu erweitern, senkt die Einstiegshürde und '
            'beschleunigt Produktionsprozesse enorm.'
        ),
        'url': 'https://www.anthropic.com/news/claude-for-creative-work'
    },
    {
        'name': 'Buda',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 9.0,
        'tagline': 'Cloud-native Plattform zum Aufbau und Management einer KI-Belegschaft',
        'description': (
            'Buda ist eine innovative Plattform, die es ermöglicht, ein komplettes Unternehmen mit KI-Agenten '
            'zu betreiben. Nutzer können spezialisierte Agenten für HR, Sales, Marketing oder Coding rekrutieren '
            'und orchestrieren. Im Gegensatz zu lokalen Lösungen wie OpenClaw läuft Buda komplett in der Cloud '
            'mit isolierten Sandboxes und geteilten Dateisystemen.'
        ),
        'features': [
            {
                'icon': '💰',
                'label': 'Pricing',
                'content': 'Free: $0 (2 Agenten, 300 Credits/Tag). '
                           'Plus: $20/Monat/Agent (Browser, Terminal, Git). '
                           'Pro: $100/Monat/Agent (mehr Power, Automatisierungen). '
                           'Enterprise: Custom (Self-Hosted Option).'
            },
            {
                'icon': '✨',
                'label': 'Besonderheit',
                'content': 'Jeder Agent hat Zugriff auf Drive, Browser, Terminal und Git in einer Ansicht. '
                           'Agenten erinnern sich an vergangene Sessions. Parallele Ausführung möglich.'
            },
            {
                'icon': '🔒',
                'label': 'Datenschutz',
                'content': 'Isolierte Dateisysteme pro Agent. Enterprise-Plan bietet BYOK (Bring Your Own Key) '
                           'und Self-Hosting-Optionen für maximale Datenkontrolle.'
            }
        ],
        'verdict': (
            'Buda macht die Vision von "Agents as a Company" greifbar. Die Cloud-native Architektur löst '
            'viele Probleme lokaler Agenten-Setups. Besonders spannend für Startups und Solo-Entwickler, '
            'die ihre Produktivität skalieren wollen.'
        ),
        'url': 'https://buda.im/'
    }
]

# ── Generierung ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    html_content = create_html(KW, DATE, SUMMARY, TREND, STARS, TOOLS)
    
    output_file = "index.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Erfolgreich generiert: {output_file}")
