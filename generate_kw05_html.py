#!/usr/bin/env python3
"""
HTML Generator für KI-Tool-Analysen KW 05/2026
"""

from generate_html_from_analysis import create_html

# Tool-Daten für KW 05/2026
tools = [
    {
        'name': 'OpenAI Prism',
        'category': 'text',
        'category_icon': '📝',
        'category_label': 'TEXT',
        'rating': 9.0,
        'tagline': 'KI-nativer Workspace für wissenschaftliches Schreiben mit GPT-5.2',
        'description': 'OpenAI Prism ist eine kostenlose, cloud-basierte LaTeX-Umgebung für wissenschaftliche Forschungsarbeiten. Die Plattform integriert GPT-5.2 direkt in den Schreibprozess und ermöglicht Echtzeit-Kollaboration, automatische Literaturrecherche und die Konvertierung von handgeschriebenen Notizen in LaTeX-Code.',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Vollständig kostenlos für persönliche Accounts, erweiterte Funktionen über ChatGPT Business/Enterprise geplant'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Native Integration von GPT-5.2, arXiv-Suche und Echtzeit-Kollaboration in einer LaTeX-Umgebung'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'Standardmäßig privat, opt-in für KI-Training, DSGVO-konform (8/10)'}
        ],
        'verdict': 'OpenAI Prism könnte die wissenschaftliche Zusammenarbeit revolutionieren, indem es die Barrieren von LaTeX senkt und KI-Unterstützung nahtlos integriert. Die kostenlose Verfügbarkeit macht es besonders attraktiv für Studierende und Forscher.',
        'url': 'https://openai.com/index/introducing-prism/'
    },
    {
        'name': 'AirMusic v1.1',
        'category': 'design',
        'category_icon': '🎨',
        'category_label': 'DESIGN',
        'rating': 7.5,
        'tagline': 'KI-Musikgenerator mit royalty-free Lizenzierung',
        'description': 'AirMusic ist ein KI-gestützter Musikgenerator, der es Nutzern ermöglicht, hochwertige, lizenzfreie Musik für Videos, Podcasts und andere Projekte zu erstellen. Die Plattform bietet verschiedene Stile und Stimmungen und ermöglicht die Anpassung von Tempo, Instrumentierung und Struktur.',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Freemium: Kostenlos für 3 Songs/Monat, Pro ab $9.99/Monat für unbegrenzte Generierung'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Royalty-free Lizenzierung für kommerzielle Nutzung, auch im kostenlosen Plan'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'Keine Angaben zu Trainingsdaten oder Datenschutz auf der Website (5/10)'}
        ],
        'verdict': 'AirMusic bietet eine praktische Lösung für Content Creator, die schnell lizenzfreie Musik benötigen. Die Qualität ist solide, aber noch nicht auf dem Niveau menschlicher Komponisten. Der kostenlose Plan ist großzügig genug für gelegentliche Nutzung.',
        'url': 'https://airmusic.ai/'
    },
    {
        'name': 'Pandada AI',
        'category': 'data',
        'category_icon': '📊',
        'category_label': 'DATA',
        'rating': 8.5,
        'tagline': 'KI-gestützte Datenanalyse ohne Programmierkenntnisse',
        'description': 'Pandada AI ist eine Datenanalyse-Plattform, die es Benutzern ermöglicht, strukturierte und unstrukturierte Daten zu analysieren und zu visualisieren, ohne Code schreiben zu müssen. Die Plattform bietet eine intuitive Drag-and-Drop-Oberfläche und automatisierte Dashboard-Erstellung.',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Freemium: Kostenloser Basis-Plan, Pro ab $29/Monat für erweiterte Funktionen und mehr Datenquellen'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Verarbeitung unstrukturierter Daten (PDFs, Bilder) und automatische Insight-Generierung'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'DSGVO-konform, Daten werden verschlüsselt gespeichert, keine Weitergabe an Dritte (8/10)'}
        ],
        'verdict': 'Pandada AI ist ein starkes Tool für Unternehmen und Einzelpersonen, die Daten analysieren müssen, aber nicht über die technischen Ressourcen verfügen. Die Fähigkeit, unstrukturierte Daten zu verarbeiten, hebt es von der Konkurrenz ab.',
        'url': 'https://pandada.ai/'
    },
    {
        'name': 'The Prompting Company',
        'category': 'research',
        'category_icon': '🔍',
        'category_label': 'RECHERCHE',
        'rating': 8.0,
        'tagline': 'SEO für das KI-Zeitalter - Optimierung für ChatGPT-Zitate',
        'description': 'The Prompting Company bietet Tools zur Optimierung der Sichtbarkeit von Inhalten in KI-Chatbot-Antworten. Die Plattform analysiert, wie und warum bestimmte Quellen in KI-Antworten zitiert werden, und bietet Strategien zur Verbesserung der Präsenz.',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Noch in geschlossener Beta, Preisgestaltung nicht veröffentlicht'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Pionier im Bereich "AI Search Optimization" - eine völlig neue Disziplin'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'Keine Informationen verfügbar (N/A)'}
        ],
        'verdict': 'The Prompting Company könnte eine neue Ära des digitalen Marketings einläuten. Wenn KI-Chatbots zunehmend als Informationsquelle genutzt werden, wird die Optimierung für diese Plattformen genauso wichtig wie traditionelles SEO.',
        'url': 'https://www.producthunt.com/products/the-prompting-company'
    },
    {
        'name': 'Agentic Vision in Gemini',
        'category': 'agents',
        'category_icon': '🤖',
        'category_label': 'AGENTS',
        'rating': 9.0,
        'tagline': 'Google Major Update für agentenähnliche visuelle Interaktion',
        'description': 'Agentic Vision ist ein bedeutendes Update für die Gemini-Modellfamilie von Google, das erweiterte "agentenähnliche" Fähigkeiten zur visuellen Erfassung und Interaktion ermöglicht. Gemini kann nun wie ein menschlicher Agent agieren, der nicht nur sieht, was auf einem Bildschirm passiert, sondern auch Aktionen ausführt.',
        'features': [
            {'icon': '💰', 'label': 'Pricing', 'content': 'Teil der Google Gemini API, Kosten abhängig von der Nutzung (Pay-as-you-go)'},
            {'icon': '✨', 'label': 'Besonderheit', 'content': 'Ermöglicht KI-Agenten, komplexe Aufgaben in Web-Interfaces zu automatisieren'},
            {'icon': '🔒', 'label': 'Datenschutz', 'content': 'Google Cloud-Datenschutzrichtlinien, DSGVO-konform (7/10)'}
        ],
        'verdict': 'Agentic Vision ist ein fundamentaler Fortschritt in der KI-Agenten-Technologie. Es könnte die Art und Weise, wie wir mit Software interagieren, grundlegend verändern und neue Möglichkeiten für Automatisierung und Produktivität eröffnen.',
        'url': 'https://blog.google/technology/ai/google-gemini-ai-update-january-2026/'
    }
]

# Generiere HTML
html = create_html(
    kw="05",
    date="01.02.2026",
    summary="In dieser Woche standen vor allem fundamentale Weiterentwicklungen und neue Plattformen im Fokus, die weniger auf einzelne Features als auf die Schaffung neuer Arbeitsweisen abzielen. OpenAI startete mit Prism eine kostenlose, KI-gestützte Plattform für wissenschaftliches Schreiben, die das Potenzial hat, die akademische Zusammenarbeit zu revolutionieren. Gleichzeitig treibt Google mit Agentic Vision in Gemini die Evolution von reiner Bilderkennung zu einem agentischen, interaktiven Prozess voran. Im Bereich der Datenanalyse überzeugte Pandada AI auf Product Hunt durch seinen Ansatz, auch unstrukturierte Daten für professionelle Reports zugänglich zu machen.",
    trend="KI-native Arbeitsumgebungen und agentenähnliche Systeme",
    stars="OpenAI Prism & Agentic Vision in Gemini (9/10)",
    tools=tools
)

# Speichere HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML-Datei für KW 05/2026 erfolgreich erstellt!")
