"""Sprachen, Pfade und Oberflächentexte für DE und EN."""
import datetime as dt

LANGS = ["de", "en"]

CATEGORIES = ["Text", "Design", "Data / Wissen", "Recherche", "Agents"]
CAT_LABEL = {
    "de": {c: c for c in CATEGORIES},
    "en": {"Text": "Text", "Design": "Design", "Data / Wissen": "Data / Knowledge", "Recherche": "Research", "Agents": "Agents"},
}

MONTHS = {
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
}

PATHS = {
    "de": {"home": "index.html", "archive": "archiv.html", "method": "methode.html", "imprint": "impressum.html",
           "privacy": "datenschutz.html", "feed": "feed.xml"},
    "en": {"home": "en/index.html", "archive": "en/archive.html", "method": "en/method.html", "imprint": "en/imprint.html",
           "privacy": "en/privacy.html", "feed": "en/feed.xml"},
}


def week_page(lang, w):
    if lang == "de":
        return f"archiv/{w['jahr']}/kw{w['kw']:02d}-{w['datum']}.html"
    return f"en/archive/{w['jahr']}/week{w['kw']:02d}-{w['datum']}.html"


def date_text(iso, lang):
    d = dt.date.fromisoformat(iso)
    if lang == "en":
        return f"{d.day} {MONTHS['en'][d.month - 1]} {d.year}"
    return f"{d.day}. {MONTHS['de'][d.month - 1]} {d.year}"


def score(v, lang="de"):
    if v is None or v == "":
        return ""
    v = float(v)
    s = str(int(v)) if v == int(v) else f"{v:.1f}"
    return s.replace(".", ",") if lang == "de" else s


T = {
    "de": {
        "html_lang": "de-CH", "locale": "de_CH", "site": "KI-Tool-Analysen",
        "skip": "Zum Inhalt", "nav_current": "Diese Woche", "nav_archive": "Archiv", "nav_method": "Methode",
        "home_label": "KI-Tool-Analysen, Startseite",
        "footer_line": "Jeden Sonntag fünf KI-Tools, eingeordnet nach Nutzen, Kosten und Datenschutz.",
        "footer_by": "Eine Publikation von", "footer_more": "Weitere wöchentliche Einordnung:",
        "news_url": "https://news.fragroger.ai/",
        "disclaimer_title": "Hinweis",
        "disclaimer": "Recherche, Auswahl und Texte entstehen mit Unterstützung von KI-Systemen und werden automatisiert veröffentlicht. Preise, Funktionen und Datenschutzangaben ändern sich laufend; massgebend sind die aktuellen Unterlagen der Anbieter. Die Analysen sind keine Rechts- oder Kaufberatung.",
        "imprint": "Impressum", "privacy": "Datenschutz", "more_pages": "Weitere Seiten",
        "week": "KW", "badge_new": "Neu", "badge_archive": "Archiv",
        "hero_1": "5 KI-Tools", "hero_2": "der Woche",
        "hero_sub": "Text, Design, Data / Wissen, Recherche und Agents: je ein Tool, geprüft auf Nutzen, Kosten und Datenschutz.",
        "to_current": "Zur aktuellen Woche →", "all_weeks": "Alle Wochen",
        "summary": "Die Woche in Kürze", "trend": "Trend", "jump": "Zu den Tools springen",
        "relevance": "Relevanz", "relevance_of": "von 10", "this_week": "Diese Woche:",
        "scenarios": "Nutzungsszenarien", "pricing": "Pricing", "data_protection": "Datenschutz",
        "strengths": "Stärken", "weaknesses": "Schwächen", "verdict": "Einschätzung für die Praxis",
        "open_pre": "", "open_post": "öffnen →", "read_full": "In der Vollanalyse lesen", "sources": "Quellen",
        "full_text_legacy": "Die ausführliche Fassung mit allen Recherchenotizen.",
        "full_text_new": "Die komplette Analyse dieser Woche als Markdown, inklusive Quellen nach APA 7.",
        "read_full_btn": "Vollanalyse lesen", "download_md": "Markdown herunterladen", "more_weeks": "Weitere Wochen",
        "partial_note": "", "partial_link": "",
        "archive_kicker": "Archiv", "archive_title": "Alle Wochen, alle Tools",
        "archive_sub": "Seit Dezember 2025 jede Woche fünf Tools. Suche nach Namen, Einsatzzweck oder Stichwort, filtere nach Kategorie und Jahr.",
        "stat_weeks": "Wochen", "stat_tools": "Tool-Analysen", "stat_avg": "Ø Relevanz",
        "search": "Suche", "search_ph": "Tool oder Stichwort suchen, z. B. Agent, lokal, Präsentation",
        "filter": "Filter", "all": "Alle", "all_years": "Alle Jahre", "year": "Jahr", "min_score": "Mindestbewertung",
        "any_score": "Jede Bewertung", "from_8": "ab 8/10", "from_9": "ab 9/10",
        "count_filtered": "{t} Tools in {w} Wochen", "count_all": "{w} Wochen im Archiv",
        "archive_page_title": "Archiv | KI-Tool-Analysen",
        "archive_desc": "Alle wöchentlichen KI-Tool-Analysen seit Dezember 2025, durchsuchbar nach Tool, Kategorie und Jahr.",
        "week_desc": "Die fünf KI-Tools der KW {kw}/{jahr}: {names}.",
        "analysis_title": "Vollanalyse KW {kw}/{jahr} | KI-Tool-Analysen", "analysis_desc": "Ausführliche Analyse der KI-Tools der KW {kw}/{jahr}.",
        "analysis_kicker": "Vollanalyse", "analysis_heading": "Die ausführliche Fassung", "to_week": "Zur Wochenübersicht",
        "analysis_note": "Diese Fassung stammt aus dem Archiv und wird unverändert wiedergegeben.",
        "method_title": "Methode | KI-Tool-Analysen", "method_desc": "Wie die wöchentlichen KI-Tool-Analysen entstehen: Quellen, Kategorien, Bewertung.",
        "method_heading": "So entstehen die Analysen", "method_kicker": "Methode",
        "method_lead": "Jede Woche ein Tool pro Kategorie, ausgewählt aus zehn Quellen und nach festen Kriterien geprüft.",
        "legal_kicker": "Rechtliches", "imprint_title": "Impressum | KI-Tool-Analysen", "privacy_title": "Datenschutz | KI-Tool-Analysen",
        "feed_title": "KI-Tool-Analysen (#fragRoger)", "feed_lang": "de-ch", "lang_name": "Deutsch",
    },
    "en": {
        "html_lang": "en", "locale": "en_GB", "site": "AI Tool Reviews",
        "skip": "Skip to content", "nav_current": "This week", "nav_archive": "Archive", "nav_method": "Method",
        "home_label": "AI Tool Reviews, home",
        "footer_line": "Every Sunday, five AI tools assessed for value, cost and data protection.",
        "footer_by": "Published by", "footer_more": "Weekly AI news in context:",
        "news_url": "https://news.fragroger.ai/en/",
        "disclaimer_title": "Note",
        "disclaimer": "Research, selection and texts are produced with the help of AI systems and published automatically. Prices, features and privacy terms change constantly; the providers' current documentation is authoritative. The reviews are not legal or purchasing advice.",
        "imprint": "Imprint", "privacy": "Privacy", "more_pages": "More pages",
        "week": "Week", "badge_new": "New", "badge_archive": "Archive",
        "hero_1": "5 AI tools", "hero_2": "of the week",
        "hero_sub": "Text, design, data / knowledge, research and agents: one tool each, checked for value, cost and data protection.",
        "to_current": "To the current week →", "all_weeks": "All weeks",
        "summary": "The week in brief", "trend": "Trend", "jump": "Jump to the tools",
        "relevance": "Relevance", "relevance_of": "out of 10", "this_week": "This week:",
        "scenarios": "Use cases", "pricing": "Pricing", "data_protection": "Data protection",
        "strengths": "Strengths", "weaknesses": "Weaknesses", "verdict": "Practical assessment",
        "open_pre": "Visit ", "open_post": "→", "read_full": "Read the full analysis (German)", "sources": "Sources",
        "full_text_legacy": "The detailed version with all research notes is available in German.",
        "full_text_new": "The complete analysis of this week as Markdown, including APA 7 sources.",
        "read_full_btn": "Full analysis (German)", "download_md": "Download Markdown", "more_weeks": "More weeks",
        "partial_note": "This issue dates from before the English edition launched in October 2026. Summaries and short descriptions are translated; the detailed reviews are available in German.",
        "partial_link": "Detailed review in German",
        "archive_kicker": "Archive", "archive_title": "All weeks, all tools",
        "archive_sub": "Five tools every week since December 2025. Search by name, use case or keyword, filter by category and year.",
        "stat_weeks": "Weeks", "stat_tools": "Tool reviews", "stat_avg": "Avg. relevance",
        "search": "Search", "search_ph": "Search tools or keywords, e.g. agent, local, presentation",
        "filter": "Filter", "all": "All", "all_years": "All years", "year": "Year", "min_score": "Minimum rating",
        "any_score": "Any rating", "from_8": "8/10 and up", "from_9": "9/10 and up",
        "count_filtered": "{t} tools in {w} weeks", "count_all": "{w} weeks in the archive",
        "archive_page_title": "Archive | AI Tool Reviews",
        "archive_desc": "All weekly AI tool reviews since December 2025, searchable by tool, category and year.",
        "week_desc": "The five AI tools of week {kw}/{jahr}: {names}.",
        "analysis_title": "", "analysis_desc": "", "analysis_kicker": "", "analysis_heading": "", "to_week": "", "analysis_note": "",
        "method_title": "Method | AI Tool Reviews", "method_desc": "How the weekly AI tool reviews are produced: sources, categories, rating.",
        "method_heading": "How the reviews are made", "method_kicker": "Method",
        "method_lead": "One tool per category every week, selected from ten sources and checked against fixed criteria.",
        "legal_kicker": "Legal", "imprint_title": "Imprint | AI Tool Reviews", "privacy_title": "Privacy | AI Tool Reviews",
        "feed_title": "AI Tool Reviews (#fragRoger)", "feed_lang": "en", "lang_name": "English",
    },
}
