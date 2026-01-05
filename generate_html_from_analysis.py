#!/usr/bin/env python3
"""
HTML Generator für KI-Tool-Analysen
Erstellt eine vollständige HTML-Seite mit Cyber-Design aus strukturierten Tool-Daten
"""

def create_html(kw, date, summary, trend, stars, tools):
    """
    Erstellt eine vollständige HTML-Seite mit Cyber-Design
    
    Args:
        kw: Kalenderwoche (z.B. "01")
        date: Datum (z.B. "04.01.2026")
        summary: Zusammenfassungstext
        trend: Trend-Text
        stars: Stars der Woche (z.B. "Nano Banana & Mnexium AI (9/10)")
        tools: Liste von Tool-Dictionaries mit:
            - name: Tool-Name
            - category: Kategorie (text/design/data/research/agents)
            - category_icon: Emoji für Kategorie
            - category_label: Label für Kategorie
            - rating: Bewertung (z.B. 8.0)
            - tagline: Kurzbeschreibung
            - description: Ausführliche Beschreibung
            - features: Liste von Feature-Dictionaries mit icon und content
            - verdict: Fazit-Text
            - url: Website-URL
    """
    
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KI-Tool-Analysen | Wöchentliche Reviews KW {kw}/2026</title>
    <meta name="description" content="Wöchentliche Analysen der Top 5 KI-Tools mit detaillierten Reviews, Pricing und Datenschutz-Bewertungen.">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Cyberpunk Background Effects -->
    <div class="cyber-grid"></div>
    <div class="cyber-scanline"></div>
    
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo-section">
                    <div class="logo-icon">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 5L35 12.5V27.5L20 35L5 27.5V12.5L20 5Z" stroke="#00ff9d" stroke-width="2" fill="none"/>
                            <circle cx="20" cy="20" r="8" fill="#00ff9d"/>
                            <path d="M20 12V28M12 20H28" stroke="#ffffff" stroke-width="2"/>
                        </svg>
                    </div>
                    <div class="logo-text">
                        <h1>KI-TOOL-ANALYSEN</h1>
                        <p class="tagline">Weekly Deep Dive Reviews</p>
                    </div>
                </div>
                <div class="header-stats">
                    <div class="stat">
                        <span class="stat-value">KW {kw}</span>
                        <span class="stat-label">Kalenderwoche</span>
                    </div>
                    <div class="stat">
                        <span class="stat-value">{len(tools)}</span>
                        <span class="stat-label">Tools/Woche</span>
                    </div>
                    <a href="archiv.html" class="stat" style="text-decoration: none; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 15px rgba(0,255,157,0.3)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
                        <span class="stat-value">📚</span>
                        <span class="stat-label">Archiv</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="main">
        <div class="container">
            <!-- Latest Analysis Section -->
            <section class="latest-section">
                <div class="section-header">
                    <h2 class="section-title">
                        <span class="title-icon">▶</span>
                        Aktuelle Analyse
                    </h2>
                    <div class="section-meta">
                        <span class="date">{date}</span>
                        <span class="badge badge-live">LIVE</span>
                    </div>
                </div>

                <!-- Summary Card -->
                <div class="summary-card">
                    <h3 class="summary-title">Wöchentliche Zusammenfassung</h3>
                    <p class="summary-text">
                        {summary}
                    </p>
                    <div class="summary-highlights">
                        <div class="highlight">
                            <span class="highlight-icon">⭐</span>
                            <span class="highlight-text">{stars}</span>
                        </div>
                        <div class="highlight">
                            <span class="highlight-icon">🚀</span>
                            <span class="highlight-text">Trend: {trend}</span>
                        </div>
                        <div class="highlight">
                            <span class="highlight-icon">💡</span>
                            <span class="highlight-text">Paradigmenwechsel: Von All-in-One zu spezialisierten Lösungen</span>
                        </div>
                    </div>
                </div>

                <!-- Tools Grid -->
                <div class="tools-grid">
"""
    
    # Generiere Tool-Cards
    for tool in tools:
        features_html = ""
        for feature in tool['features']:
            features_html += f"""
                            <div class="feature">
                                <span class="feature-icon">{feature['icon']}</span>
                                <div class="feature-content">
                                    <strong>{feature['label']}:</strong> {feature['content']}
                                </div>
                            </div>"""
        
        html += f"""
                    <!-- Tool: {tool['name']} -->
                    <div class="tool-card" data-category="{tool['category']}">
                        <div class="tool-header">
                            <div class="tool-category">
                                <span class="category-icon">{tool['category_icon']}</span>
                                <span class="category-label">{tool['category_label']}</span>
                            </div>
                            <div class="tool-rating">
                                <span class="rating-value">{tool['rating']}</span>
                                <span class="rating-label">/10</span>
                            </div>
                        </div>
                        
                        <h3 class="tool-name">{tool['name']}</h3>
                        <p class="tool-tagline">{tool['tagline']}</p>
                        
                        <div class="tool-description">
                            <p>{tool['description']}</p>
                        </div>
                        
                        <div class="tool-features">{features_html}
                        </div>
                        
                        <div class="tool-verdict">
                            <strong>Fazit:</strong> {tool['verdict']}
                        </div>
                        
                        <div class="tool-links">
                            <a href="{tool['url']}" class="tool-link" target="_blank">
                                <span>Website besuchen</span>
                                <span class="link-icon">→</span>
                            </a>
                        </div>
                    </div>
"""
    
    html += """
                </div>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>KI-Tool-Analysen</h3>
                <p>Wöchentliche Deep-Dive-Reviews der interessantesten KI-Tools mit detaillierten Analysen zu Pricing, Features und Datenschutz.</p>
            </div>
            
            <div class="footer-section">
                <h3>Updates</h3>
                <p>Jeden Samstag neue Analysen</p>
                <p>5 Tools pro Woche</p>
            </div>
            
            <div class="footer-section">
                <h3>Kategorien</h3>
                <p>📝 Text • 🎨 Design • 📊 Data • 🔍 Recherche • 🤖 Agents</p>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>&copy; 2026 KI-Tool-Analysen | Erstellt von Roger Basler de Roca</p>
        </div>
    </footer>
</body>
</html>
"""
    
    return html


# Beispiel-Verwendung:
if __name__ == "__main__":
    # Beispiel-Daten
    tools = [
        {
            'name': 'Beispiel Tool',
            'category': 'text',
            'category_icon': '📝',
            'category_label': 'TEXT',
            'rating': 8.0,
            'tagline': 'Kurzbeschreibung',
            'description': 'Ausführliche Beschreibung des Tools...',
            'features': [
                {'icon': '💰', 'label': 'Pricing', 'content': 'Ab $10/Monat'},
                {'icon': '✨', 'label': 'Besonderheit', 'content': 'Einzigartiges Feature'},
                {'icon': '🔒', 'label': 'Datenschutz', 'content': 'DSGVO-konform'}
            ],
            'verdict': 'Fazit-Text...',
            'url': 'https://example.com'
        }
    ]
    
    html = create_html(
        kw="01",
        date="04.01.2026",
        summary="Zusammenfassung...",
        trend="Trend-Text",
        stars="Stars der Woche",
        tools=tools
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ HTML-Datei erfolgreich erstellt!")
