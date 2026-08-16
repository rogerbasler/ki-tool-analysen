#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path
from generate_html_from_analysis import create_html

ROOT = Path(__file__).resolve().parent
DATE_ISO = "2026-08-16"
DATE_DISPLAY = "16.08.2026"
KW = "33"
YEAR = 2026

# 1. Bestehende Homepage archivieren, bevor sie überschrieben wird.
archive_dir = ROOT / "archiv" / str(YEAR)
archive_dir.mkdir(parents=True, exist_ok=True)
archive_html = archive_dir / f"kw{KW}-{DATE_ISO}.html"
shutil.copy2(ROOT / "index.html", archive_html)

# 2. Neue Homepage mit dem bewährten Generator erzeugen.
tools = [
    {
        "name": "Writer Agent + effizientes Harness",
        "category": "text",
        "category_icon": "📝",
        "category_label": "TEXT",
        "rating": 8.0,
        "tagline": "Agentische Textarbeit mit Fokus auf Kostenkontrolle, Kontext und Governance.",
        "description": "Writer optimiert die technische Schicht rund um Modelle. Laut eigener Forschung senkt ein effizientes Harness Kosten und Laufzeit um mehr als 40 Prozent bei vergleichbarer Qualität. Relevant für Teams mit wiederkehrenden, freigabepflichtigen Textprozessen.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "14 Tage gratis ohne Kreditkarte; Starter bis 5 User. Öffentliche Dollar-Listenpreise fehlen, Enterprise auf Anfrage."},
            {"icon": "🔒", "label": "Datenschutz", "content": "DPA für DSGVO/CCPA, SOC 2 Type II; laut Anbieter kein Training auf Kundendaten. US-Transfers möglich, kein Self-Hosting."},
            {"icon": "✨", "label": "Praxis", "content": "Stark für wiederholte Fachartikel, Sales-Follow-ups, Briefings und mehrsprachige Kommunikationspakete."}
        ],
        "verdict": "8/10. Sehr stark, wenn messbare Textprozesse und Governance bereits vorhanden sind. Ohne Baseline wird ein Kostenversprechen schnell zum PowerPoint-Accessoire.",
        "url": "https://writer.com/engineering/harness-research-tokens-efficiency-cost-spend-ai/"
    },
    {
        "name": "Grok Imagine Image 2.0",
        "category": "design",
        "category_icon": "🎨",
        "category_label": "DESIGN",
        "rating": 8.0,
        "tagline": "Bildgenerierung und präzise Editierung für produktionsnahe Kreativarbeit.",
        "description": "Image 2.0 verbindet Bildgenerierung mit selektiver Bereichsbearbeitung, Hintergrundentfernung, Smart Resize und bis zu fünf Referenzbildern. Der Mehrwert liegt in der Iteration und nicht nur im ersten schönen Zufallstreffer.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Über Grok Quality Mode und API erhältlich. Kein separater, verbindlicher Preis auf der Release-Seite veröffentlicht."},
            {"icon": "🔒", "label": "Datenschutz", "content": "Cloud-Service; keine veröffentlichte EU-Datenresidenz oder Self-Hosting-Option. Nur rechtegeprüfte Referenzassets nutzen."},
            {"icon": "✨", "label": "Praxis", "content": "Geeignet für Kampagnenadaptionen, Produktbilder, Social Assets und visuelle Konzeptvalidierung."}
        ],
        "verdict": "8/10. Besonders wertvoll für Teams, die kontrolliert editieren statt ewig neu prompten wollen. Marken- und Rechtsreview bleiben Pflicht.",
        "url": "https://x.ai/news/grok-imagine-image-2"
    },
    {
        "name": "Muse Glimmer",
        "category": "data",
        "category_icon": "📊",
        "category_label": "DATA / WISSEN",
        "rating": 9.0,
        "tagline": "Open-Weights-Modell für lokale Wissensassistenten, Tool Use und agentische Workflows.",
        "description": "Meta veröffentlicht Muse Glimmer unter Apache 2.0. Das 30B-Modell ist auf lokale agentische Abläufe, multimodale Dokumentarbeit und Tool Use ausgelegt. Lokal betrieben entsteht eine kontrollierbare Wissensschicht statt einer weiteren Black Box.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Gewichte unter Apache 2.0 kostenlos. Kosten entstehen über Hardware, Betrieb, Monitoring und optionales Hosting."},
            {"icon": "🔒", "label": "Datenschutz", "content": "Self-Hosting möglich. Bei vollständig lokaler Ausführung bleiben Daten in der eigenen Infrastruktur; DSGVO-Verantwortung bleibt beim Betreiber."},
            {"icon": "✨", "label": "Praxis", "content": "Ideal für lokale RAG-Workflows, Dokumentenassistenten, Codeexploration und offline-fähige Fachanwendungen."}
        ],
        "verdict": "9/10. Der Datenschutz- und Souveränitätshebel der Woche. Kein Plug-and-Play-Tool, sondern ein strategischer Baustein für Teams mit Plattformkompetenz.",
        "url": "https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model"
    },
    {
        "name": "Perplexity Computer for Builders",
        "category": "research",
        "category_icon": "🔍",
        "category_label": "RECHERCHE",
        "rating": 8.0,
        "tagline": "Recherche- und Ausführungsworkflow über Code, Produktdaten, Zahlungen und Telemetrie.",
        "description": "Computer for Builders verbindet GitHub, Datadog, Stripe, Supabase, Slack und weitere Connectoren. Es kann Ursachen recherchieren, Daten auswerten, Pull Requests vorbereiten und regelmässige Wachstumsberichte erzeugen.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Für Pro- und Max-Abos verfügbar, Computer-Einstieg gratis erwähnt. Orientierung: Pro ab 20 USD/Monat, Max ab 200 USD/Monat; Checkout prüfen."},
            {"icon": "🔒", "label": "Datenschutz", "content": "DPA vorhanden, kein Self-Hosting. Entscheidend sind minimale Connector-Rechte, getrennte Servicekonten und PR-Reviews."},
            {"icon": "✨", "label": "Praxis", "content": "Nützlich für technische Ursachenanalysen, Churn-Reports, Release-Reviews und wöchentliche Gründerbriefings."}
        ],
        "verdict": "8/10. Ein starker Research-Copilot für kleine Teams. Start nur mit Leserechten, denn der Kontext ist wertvoll und die Rechtekette potenziell heikel.",
        "url": "https://www.perplexity.ai/hub/blog/computer-for-builders"
    },
    {
        "name": "Claude Code Auto Mode",
        "category": "agents",
        "category_icon": "🤖",
        "category_label": "AGENTS",
        "rating": 9.0,
        "tagline": "Länger laufende Coding-Agents mit risikobasierter Sicherheitsprüfung statt Klick-Marathon.",
        "description": "Seit 14. August läuft Auto Mode für neue Pro-, Max- und Team-Sessions standardmässig. Ein Klassifikator prüft Tool-Aufrufe auf irreversible, destruktive oder externe Aktionen und fordert bei Bedarf Freigabe an.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Enthalten für Pro, Max und Team; kein zusätzlicher Klassifikator-Overhead. Kein Free Tier für diese Funktion kommuniziert."},
            {"icon": "🔒", "label": "Datenschutz", "content": "Cloud-Service ohne reguläres Self-Hosting. Harte Sperren, Regeln und menschliche Reviews für Produktionsumgebungen notwendig."},
            {"icon": "✨", "label": "Praxis", "content": "Für Refactoring, Tests, PR-Vorbereitung und längere Engineering-Aufgaben mit klaren Git- und CI-Regeln."}
        ],
        "verdict": "9/10. Ein echter Fortschritt bei kontrollierter Autonomie. Der Agent wird nützlicher, aber keineswegs zum Ersatz für saubere Berechtigungen und Reviews.",
        "url": "https://claude.com/blog/auto-mode-default-in-claude-code"
    }
]

summary = (
    "Diese Woche verschiebt sich KI vom einzelnen Output zur steuerbaren Ausführung. "
    "Writer optimiert die Kostenstruktur agentischer Textarbeit, Claude Code verbindet Autonomie mit einem zusätzlichen Sicherheitsmechanismus. "
    "Für visuelle Teams wird präzises Editieren wichtiger als ein weiterer Prompt-Lottoschein. "
    "Muse Glimmer zeigt zugleich, wie lokale Open Weights Datenschutz und Kontrolle wieder stärker in die eigene Hand legen."
)
html = create_html(
    kw=KW,
    date=DATE_DISPLAY,
    summary=summary,
    trend="Von generierten Einzelergebnissen zu kontrollierbaren, kontextfähigen Workflows",
    stars="Muse Glimmer & Claude Code Auto Mode (9/10)",
    tools=tools,
)
(ROOT / "index.html").write_text(html, encoding="utf-8")

# 3. Archivindex aktualisieren, neuester Eintrag zuerst.
index_path = ROOT / "archiv" / "data" / "archive-index.json"
archive = json.loads(index_path.read_text(encoding="utf-8"))
new_entry = {
    "kw": 33,
    "jahr": YEAR,
    "datum": DATE_ISO,
    "url": f"archiv/{YEAR}/kw{KW}-{DATE_ISO}.html",
    "tools": [
        {"name": "Writer Agent + effizientes Harness", "kategorie": "Text", "bewertung": 8.0, "kurzbeschreibung": "Agentische Textarbeit mit Fokus auf Kostenkontrolle, Kontext und Governance"},
        {"name": "Grok Imagine Image 2.0", "kategorie": "Design", "bewertung": 8.0, "kurzbeschreibung": "Bildgenerierung und präzise Editierung für produktionsnahe Kreativarbeit"},
        {"name": "Muse Glimmer", "kategorie": "Data / Wissen", "bewertung": 9.0, "kurzbeschreibung": "Open-Weights-Modell für lokale Wissensassistenten, Tool Use und agentische Workflows"},
        {"name": "Perplexity Computer for Builders", "kategorie": "Recherche", "bewertung": 8.0, "kurzbeschreibung": "Recherche- und Ausführungsworkflow über Code, Produktdaten, Zahlungen und Telemetrie"},
        {"name": "Claude Code Auto Mode", "kategorie": "Agents", "bewertung": 9.0, "kurzbeschreibung": "Länger laufende Coding-Agents mit risikobasierter Sicherheitsprüfung"}
    ],
    "highlights": "Muse Glimmer & Claude Code Auto Mode (9/10): Lokale Souveränität und kontrollierte Agentenautonomie werden produktionsreif.",
    "trend": "Von Einzelausgaben zu kontrollierbaren Workflows: Kosten, Rechte, Kontext und Sicherheitsmechanismen werden zur eigentlichen Produktqualität."
}
archive["analysen"] = [entry for entry in archive["analysen"] if not (entry.get("kw") == 33 and entry.get("jahr") == YEAR)]
archive["analysen"].insert(0, new_entry)
index_path.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# 4. Quellen- und Hauptanalyse auch im Projekt verfügbar machen.
analysis_source = Path("/home/ubuntu/ki-tool-analysen") / f"ki-tool-analysen-{DATE_ISO}.md"
shutil.copy2(analysis_source, ROOT / "archiv" / "data" / analysis_source.name)

print(f"Archiv erstellt: {archive_html.relative_to(ROOT)}")
print("Homepage aktualisiert: index.html")
print("Archivindex aktualisiert: archiv/data/archive-index.json")
print(f"Analyse kopiert: archiv/data/{analysis_source.name}")
