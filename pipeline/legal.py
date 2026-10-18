"""Texte für Methode, Impressum und Datenschutz (HTML-Fragmente)."""

OWNER = {
    "name": "Roger Basler de Roca",
    "company": "Analytics Agentur",
    "street": "The Circle 6",
    "city": "8058 Zürich",
    "country": "Schweiz",
    "email": "mail@rogerbasler.ch",
    "web": "https://fragroger.ai",
}

METHOD = """
<h2>Warum diese Übersicht</h2>
<p>Jede Woche erscheinen Hunderte neue KI-Tools. Die meisten verschwinden wieder, einige verändern Arbeitsabläufe. Für Entscheider:innen zählt nicht die Menge, sondern die Frage, welches Werkzeug ein reales Problem löst, was es kostet und wohin die Daten fliessen. Diese Seite beantwortet das einmal pro Woche für fünf Tools.</p>

<h2>Fünf feste Kategorien</h2>
<ul>
<li><strong>Text:</strong> Schreiben, Kommunikation, Übersetzung, Content.</li>
<li><strong>Design:</strong> Bild, Video, Audio, Präsentationen, UI.</li>
<li><strong>Data / Wissen:</strong> Analyse, Wissensmanagement, Datenaufbereitung.</li>
<li><strong>Recherche:</strong> Suche, Reasoning, Quellenarbeit.</li>
<li><strong>Agents:</strong> Automatisierung, Workflows, autonome Ausführung.</li>
</ul>
<p>Pro Kategorie wird genau ein Tool gewählt. Gibt es in einer Kategorie keine relevante Neuerscheinung, rückt ein bestehendes Tool mit einem wichtigen Update nach. Die Auswahl wechselt von Woche zu Woche; Vergleiche zwischen Tools gibt es bewusst nicht.</p>

<h2>Quellen der Recherche</h2>
<p>AI Breakfast, There's An AI For That, FutureTools.io, Ben's Bites, Futurepedia.io, Product Hunt (Kategorie AI), Toolify.ai, TopAI.tools, The AI Citizen (Weekly Tool Roundup) sowie AI-Weekly, The Batch, The Sequence und AI Tidbits für Tool-Erwähnungen. Preis-, Funktions- und Datenschutzangaben werden anschliessend in den offiziellen Unterlagen der Anbieter geprüft.</p>

<h2>Was jede Analyse enthält</h2>
<ul>
<li>Kurzbeschreibung mit Funktion und Zielgruppe</li>
<li>Drei bis fünf praxisnahe Nutzungsszenarien</li>
<li>Pricing in CHF oder USD, inklusive Free Tier</li>
<li>Datenschutz: Serverstandort, Policies, DSGVO und DSG, Self-Hosting</li>
<li>Stärken und Schwächen</li>
<li>Einschätzung für die Praxis</li>
<li>Relevanzbewertung von 1 bis 10</li>
</ul>

<h2>Wie die Relevanz bewertet wird</h2>
<p>Die Zahl beschreibt den erwarteten Nutzen für Unternehmen im deutschsprachigen Raum, nicht die technische Brillanz. Sie verbindet vier Fragen: Löst das Tool ein häufiges Problem? Ist es heute produktiv einsetzbar? Sind Kosten und Datenwege nachvollziehbar? Wie stark ist die Abhängigkeit von einem einzelnen Anbieter? Werte ab 9 sind selten und markieren Werkzeuge, die Arbeitsweisen spürbar verschieben.</p>

<h2>Rhythmus und Herstellung</h2>
<p>Eine neue Ausgabe erscheint jeden Sonntagmorgen. Recherche, Auswahl und Texte entstehen mit Unterstützung von KI und werden automatisiert veröffentlicht. Bis Oktober 2026 lief die Produktion über Manus, seit KW 43/2026 über Claude. Alle früheren Ausgaben bleiben im <a href="archiv.html">Archiv</a> erhalten.</p>
"""

IMPRINT = """
<h2>Verantwortlich für den Inhalt</h2>
<p>{name}<br>{company}<br>{street}<br>{city}<br>{country}</p>
<p>E-Mail: <a href="mailto:{email}">{email}</a><br>Web: <a href="{web}">{web}</a></p>
<h2>Was diese Seite ist</h2>
<p>Die KI-Tool-Analysen sind eine wöchentliche, redaktionell kuratierte Übersicht über neue und aktualisierte KI-Werkzeuge. Jeden Sonntag erscheinen fünf Analysen in den Kategorien Text, Design, Data / Wissen, Recherche und Agents.</p>
<h2>Haftungsausschluss</h2>
<p>Die Inhalte werden mit Sorgfalt erstellt. Recherche, Auswahl und Texte entstehen jedoch mit Unterstützung von KI-Systemen und werden automatisiert veröffentlicht. Für Richtigkeit, Vollständigkeit und Aktualität wird keine Gewähr übernommen. Preise, Funktionen und Datenschutzangaben der Anbieter ändern sich laufend; massgebend sind deren aktuelle Unterlagen. Haftungsansprüche wegen Schäden materieller oder immaterieller Art, die aus der Nutzung oder Nichtnutzung der Informationen entstehen, sind ausgeschlossen, soweit gesetzlich zulässig. Die Inhalte sind keine Rechts-, Kauf- oder sonstige Beratung.</p>
<h2>Links auf Drittseiten</h2>
<p>Die Analysen verlinken auf die Websites der Anbieter und auf Quellen. Für Inhalte verlinkter Seiten sind ausschliesslich deren Betreiber verantwortlich. Marken- und Produktnamen gehören den jeweiligen Inhaber:innen.</p>
<h2>Urheberrecht</h2>
<p>Die Analysen dürfen mit Quellenangabe ("KI-Tool-Analysen, Roger Basler de Roca") geteilt und zitiert werden.</p>
"""

PRIVACY = """
<p>Diese Seite kommt ohne Cookies, ohne Tracking und ohne externe Schriftarten oder Skripte von Drittanbietern aus. Es gibt keine Nutzerkonten und keine Formulare.</p>
<h2>Verantwortliche Stelle</h2>
<p>{name}, {company}, {street}, {city}, {country}, <a href="mailto:{email}">{email}</a></p>
<h2>Hosting</h2>
<p>Die Seite wird über GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA) ausgeliefert. Beim Aufruf verarbeitet GitHub technisch notwendige Verbindungsdaten wie IP-Adresse, Zeitpunkt des Zugriffs, aufgerufene Seite, Browsertyp und Referrer in Server-Logs, um die Seite bereitzustellen und die Sicherheit des Dienstes zu gewährleisten. Grundlage ist das berechtigte Interesse am sicheren Betrieb der Website. Details: <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<h2>Suche im Archiv</h2>
<p>Die Archivsuche läuft vollständig im Browser. Suchbegriffe werden weder übertragen noch gespeichert.</p>
<h2>Externe Links</h2>
<p>Beim Klick auf die Website eines Anbieters oder eine Quelle gelten die Datenschutzbestimmungen der jeweiligen Seite.</p>
<h2>Ihre Rechte</h2>
<p>Sie haben nach dem Schweizer Datenschutzgesetz (DSG) und, soweit anwendbar, der DSGVO das Recht auf Auskunft, Berichtigung, Löschung und Einschränkung der Bearbeitung Ihrer Personendaten. Wenden Sie sich dazu an <a href="mailto:{email}">{email}</a>.</p>
<p>Stand: Oktober 2026</p>
"""
