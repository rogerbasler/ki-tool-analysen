from __future__ import annotations

import json
import shutil
from pathlib import Path

from generate_html_from_analysis import create_html

ROOT = Path(__file__).resolve().parent
DATE_ISO = "2026-08-23"
DATE_DISPLAY = "23.08.2026"
KW = "34"
YEAR = 2026
ANALYSIS_SOURCE = Path("/home/ubuntu/ki-tool-analysen") / f"ki-tool-analysen-{DATE_ISO}.md"

# 1. Bestehende Homepage vor dem Überschreiben archivieren.
archive_dir = ROOT / "archiv" / str(YEAR)
archive_dir.mkdir(parents=True, exist_ok=True)
archive_html = archive_dir / f"kw{KW}-{DATE_ISO}.html"
shutil.copy2(ROOT / "index.html", archive_html)

# 2. Neue Homepage im bewährten Cyber-Design erzeugen.
tools = [
    {
        "name": "ChatGPT for Teens",
        "category": "text",
        "category_icon": "📝",
        "category_label": "TEXT",
        "rating": 8.0,
        "tagline": "Lernorientierte Text-KI mit zusätzlichen Schutzmechanismen für Jugendliche.",
        "description": "OpenAI bündelt Study Mode, Quizze, Lernvisualisierungen und Elternfunktionen in einer automatisch zugewiesenen Erfahrung für 13- bis 17-Jährige. Der Wert liegt nicht in der schnellen Antwort, sondern im schrittweisen Lernen und kritischen Prüfen.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Kein separater Teen-Preis. Zugang über ChatGPT Free; höhere Limits über allgemeine Bezahlpläne, regional prüfen."},
            {"icon": "🔒", "label": "Datenschutz", "content": "US-Cloud mit europäischer Privacy Policy. Keine Self-Hosting-Option; Datenkontrollen bei persönlichen Konten aktiv prüfen."},
            {"icon": "✨", "label": "Praxis", "content": "Für Prüfungsvorbereitung, Verständnischecks, Entwürfe und KI-Literacy, immer mit Quellenprüfung und klaren Schulregeln."}
        ],
        "verdict": "8/10. Ein sinnvoller Lernbegleiter mit besseren Leitplanken als ein Standard-Chat. Er ersetzt weder Fachperson noch Quellenkritik.",
        "url": "https://openai.com/index/chatgpt-for-teens/"
    },
    {
        "name": "ElevenLabs AI Caption Generator",
        "category": "design",
        "category_icon": "🎨",
        "category_label": "DESIGN",
        "rating": 9.0,
        "tagline": "Zeitlich synchronisierte Untertitel als schneller, editierbarer Produktionsschritt.",
        "description": "ElevenLabs erstellt aus MP4, MOV und MKV präzise Untertitel mit Wort-Timing, Sprecherzuordnung und Unterstützung für mehr als 90 Sprachen. Für Content-Teams wird aus einem mühsamen Nachgang ein kontrollierbarer Workflow.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Free mit 10'000 Credits; Starter 6 USD, Creator 22 USD, Pro 99 USD. Abrechnung über Credits und Videominuten."},
            {"icon": "🔒", "label": "Datenschutz", "content": "US-Anbieter mit Privacy Policy und DPA. Reguläres Self-Hosting fehlt; private Deployments nennt ElevenLabs nur für Enterprise."},
            {"icon": "✨", "label": "Praxis", "content": "Stark für Reels, Podcasts, Bildungs- und Eventvideos. Namen, Fachbegriffe und Sprecherwechsel vor Veröffentlichung prüfen."}
        ],
        "verdict": "9/10. Praktische Entlastung mit hoher Produktionsreife. Die KI spart Tipparbeit, nicht den finalen Qualitätsentscheid.",
        "url": "https://elevenlabs.io/caption-generator"
    },
    {
        "name": "Databricks Genie One",
        "category": "data",
        "category_icon": "📊",
        "category_label": "DATA / WISSEN",
        "rating": 8.0,
        "tagline": "Governte Antworten und Folgeaktionen auf Unternehmensdaten in natürlicher Sprache.",
        "description": "Genie One verbindet Fragen, Daten- und Wissenszugriff sowie agentische Folgeaktionen. Über Unity Catalog sollen bestehende Berechtigungen bis auf Zeilen- und Spaltenebene respektiert werden. Das ist für Unternehmen relevanter als ein weiterer hübscher Prompt.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Nutzungsbasiert statt fixer Monatspauschale. Kostenloser Einstieg laut Produktseite, Compute- und Plattformkosten vorab budgetieren."},
            {"icon": "🔒", "label": "Datenschutz", "content": "Cloud-native auf AWS, Azure und Google Cloud. Governance über Unity Catalog; Datenresidenz und Modellendpunkte vor dem Pilot festlegen."},
            {"icon": "✨", "label": "Praxis", "content": "Für Self-Service-Analysen, governte Wissensabfragen, Briefings und Datenfragen in Slack oder Teams."}
        ],
        "verdict": "8/10. Stark für Organisationen mit reifer Datenbasis. Ohne Begriffsmodell, saubere Zugriffsrechte und Kostenkontrolle automatisiert es vor allem Missverständnisse.",
        "url": "https://www.databricks.com/product/genie"
    },
    {
        "name": "ChatPlayground AI",
        "category": "research",
        "category_icon": "🔍",
        "category_label": "RECHERCHE",
        "rating": 7.0,
        "tagline": "Mehrere KI-Modelle vergleichen, Widersprüche sehen und Recherchefragen besser stellen.",
        "description": "ChatPlayground sendet einen Prompt parallel an ausgewählte Modelle und stellt die Antworten nebeneinander. Diese Perspektivvielfalt hilft, Gegenargumente und offene Punkte sichtbar zu machen. Modellmehrheit ist keine Wahrheit, aber sie ist ein brauchbarer Warnhinweis.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Begrenzter Testzugang; Pro ab 15 USD und Unlimited ab 25 USD pro Monat bei Jahreszahlung. Checkout bleibt verbindlich."},
            {"icon": "🔒", "label": "Datenschutz", "content": "US-Betreiber, keine klar auffindbare DPA oder Self-Hosting-Option. Keine vertraulichen Inputs ohne dokumentierte Datenflussprüfung."},
            {"icon": "✨", "label": "Praxis", "content": "Für Recherche, Argumentenchecks, Dokumentensichtung und Prompt-Qualität. Jede auffällige Antwort braucht eine Primärquelle."}
        ],
        "verdict": "7/10. Stark als Werkzeug gegen vorschnelle Sicherheit. Für regulierte Inhalte ist die Compliance-Dokumentation zu dünn.",
        "url": "https://www.chatplayground.ai/"
    },
    {
        "name": "Berd",
        "category": "agents",
        "category_icon": "🤖",
        "category_label": "AGENTS",
        "rating": 8.0,
        "tagline": "Quelloffener Desktop-Workspace für lokale Projekte, Skills und spezialisierte Agenten.",
        "description": "Berd von Block organisiert Projekte, Chats, Agenten und Skills in einem lokalen Workspace. Eigene Ordner, Repositories und Modellanbieter lassen sich anbinden. Damit rückt die Datensouveränität wieder näher an den Rechner, vorausgesetzt die Rechte sind sauber gesetzt.",
        "features": [
            {"icon": "💰", "label": "Pricing", "content": "Die Open-Source-App ist kostenlos. Kosten entstehen über angebundene Modellanbieter, API-Schlüssel, Infrastruktur und Betrieb."},
            {"icon": "🔒", "label": "Datenschutz", "content": "Lokaler Fokus und offener Quellcode ermöglichen eigene Betriebsformen. Externe Provider und Tools können trotzdem Daten abziehen."},
            {"icon": "✨", "label": "Praxis", "content": "Für technische Teams mit abgegrenzten Projektordnern, wiederkehrenden Skills und einem vorsichtigen Start mit Leserechten."}
        ],
        "verdict": "8/10. Ein guter Gegenentwurf zum beliebigen Chatfenster. Einrichtung und Berechtigungskonzept verlangen allerdings technische Reife.",
        "url": "https://berd.xyz/"
    }
]

summary = (
    "Diese Woche geht es weniger um den nächsten Modell-Showcase als um kontrollierbare Arbeitskontexte. "
    "ChatGPT for Teens zeigt, wie Text-KI Lernpfade statt Abkürzungen fördern kann. "
    "ElevenLabs reduziert die Untertitelung auf einen editierbaren Produktionsschritt, während Genie One Antworten an Governance und Unternehmensdaten bindet. "
    "ChatPlayground macht Widersprüche sichtbar, Berd bringt Agenten wieder näher an lokale Projekte und eigene Regeln."
)

html = create_html(
    kw=KW,
    date=DATE_DISPLAY,
    summary=summary,
    trend="Von einzelnen KI-Antworten zu begrenzten Kontexten, überprüfbaren Datenflüssen und klaren Berechtigungen",
    stars="ElevenLabs AI Caption Generator (9/10) & kontrollierbare KI-Kontexte",
    tools=tools,
)
(ROOT / "index.html").write_text(html, encoding="utf-8")

# 3. Archivindex aktualisieren, neue Woche an erster Stelle.
index_path = ROOT / "archiv" / "data" / "archive-index.json"
archive = json.loads(index_path.read_text(encoding="utf-8"))
new_entry = {
    "kw": int(KW),
    "jahr": YEAR,
    "datum": DATE_ISO,
    "url": f"archiv/{YEAR}/kw{KW}-{DATE_ISO}.html",
    "tools": [
        {"name": "ChatGPT for Teens", "kategorie": "Text", "bewertung": 8.0, "kurzbeschreibung": "Lernorientierte Text-KI mit zusätzlichen Schutzmechanismen für Jugendliche"},
        {"name": "ElevenLabs AI Caption Generator", "kategorie": "Design", "bewertung": 9.0, "kurzbeschreibung": "Zeitlich synchronisierte Untertitel als schneller, editierbarer Produktionsschritt"},
        {"name": "Databricks Genie One", "kategorie": "Data / Wissen", "bewertung": 8.0, "kurzbeschreibung": "Governte Antworten und Folgeaktionen auf Unternehmensdaten in natürlicher Sprache"},
        {"name": "ChatPlayground AI", "kategorie": "Recherche", "bewertung": 7.0, "kurzbeschreibung": "Mehrere KI-Modelle vergleichen, Widersprüche sehen und Recherchefragen besser stellen"},
        {"name": "Berd", "kategorie": "Agents", "bewertung": 8.0, "kurzbeschreibung": "Quelloffener Desktop-Workspace für lokale Projekte, Skills und spezialisierte Agenten"}
    ],
    "highlights": "ElevenLabs AI Caption Generator (9/10): Produktionsreife Untertitelung trifft auf den Wochenfokus kontrollierbarer KI-Kontexte.",
    "trend": "Kontext, Rechte, Datenflüsse und Review-Schleifen werden zum eigentlichen Qualitätsmerkmal von KI-Tools."
}
archive["analysen"] = [entry for entry in archive["analysen"] if not (entry.get("kw") == int(KW) and entry.get("jahr") == YEAR)]
archive["analysen"].insert(0, new_entry)
index_path.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# 4. Vollständige Analyse im Projekt und im Archiv ablegen.
shutil.copy2(ANALYSIS_SOURCE, ROOT / ANALYSIS_SOURCE.name)
shutil.copy2(ANALYSIS_SOURCE, ROOT / "archiv" / "data" / ANALYSIS_SOURCE.name)

print(f"Archiv erstellt: {archive_html.relative_to(ROOT)}")
print("Homepage aktualisiert: index.html")
print("Archivindex aktualisiert: archiv/data/archive-index.json")
print(f"Analyse kopiert: {ANALYSIS_SOURCE.name}")
