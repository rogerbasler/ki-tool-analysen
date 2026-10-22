"""Texte für Methode, Impressum und Datenschutz (HTML-Fragmente)."""

OWNER = {
    "name": "Roger Basler de Roca",
    "company": "Analytics Agentur",
    "street": "The Circle 6",
    "city": "8058 Zürich",
    "country": {"de": "Schweiz", "en": "Switzerland"},
    "email": "mail@rogerbasler.ch",
    "web": "https://fragroger.ai",
}

METHOD = """
<h2>Warum diese Übersicht</h2>
<p>Jede Woche erscheinen Hunderte neue KI-Tools. Die meisten verschwinden wieder, einige verändern Arbeitsabläufe. Für Entscheider:innen zählt nicht die Menge, sondern die Frage, welches Werkzeug ein reales Problem löst, was es kostet und wohin die Daten fliessen. Diese Seite beantwortet das einmal pro Woche für sechs Tools.</p>

<h2>Sechs feste Kategorien</h2>
<ul>
<li><strong>Text:</strong> Schreiben, Kommunikation, Übersetzung, Content.</li>
<li><strong>Design:</strong> Bild, Video, Audio, Präsentationen, UI.</li>
<li><strong>Data / Wissen:</strong> Analyse, Wissensmanagement, Datenaufbereitung.</li>
<li><strong>Recherche:</strong> Suche, Reasoning, Quellenarbeit.</li>
<li><strong>Agents:</strong> Automatisierung, Workflows, autonome Ausführung.</li>
<li><strong>Transkription:</strong> Meetings, Interviews und Sprachaufnahmen in Text überführen, zusammenfassen und übersetzen. Seit Oktober 2026. Der rechtliche Rahmen für Aufnahmen in der Schweiz und der EU steht im <a href="https://transcribe.fragroger.ai/" rel="noopener">Datenschutz-Guide zur KI-Transkription</a>.</li>
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
<p>Eine neue Ausgabe erscheint jeden Sonntagmorgen auf Deutsch und Englisch. Recherche, Auswahl und Texte entstehen mit Unterstützung von KI und werden automatisiert veröffentlicht. Bis Oktober 2026 lief die Produktion über Manus, seit KW 43/2026 über Claude. Alle früheren Ausgaben bleiben im <a href="archiv.html">Archiv</a> erhalten.</p>
"""

IMPRINT = """
<h2>Verantwortlich für den Inhalt</h2>
<p>{name}<br>{company}<br>{street}<br>{city}<br>{country_l}</p>
<p>E-Mail: <a href="mailto:{email}">{email}</a><br>Web: <a href="{web}">{web}</a></p>
<h2>Was diese Seite ist</h2>
<p>Die KI-Tool-Analysen sind eine wöchentliche, redaktionell kuratierte Übersicht über neue und aktualisierte KI-Werkzeuge. Jeden Sonntag erscheinen sechs Analysen in den Kategorien Text, Design, Data / Wissen, Recherche, Agents und Transkription.</p>
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
<p>{name}, {company}, {street}, {city}, {country_l}, <a href="mailto:{email}">{email}</a></p>
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

METHOD_EN = """
<h2>Why this overview exists</h2>
<p>Hundreds of new AI tools appear every week. Most disappear again; a few change how work gets done. For decision-makers the volume does not matter. What matters is which tool solves a real problem, what it costs and where the data goes. This page answers that once a week for six tools.</p>

<h2>Six fixed categories</h2>
<ul>
<li><strong>Text:</strong> writing, communication, translation, content.</li>
<li><strong>Design:</strong> image, video, audio, presentations, UI.</li>
<li><strong>Data / Knowledge:</strong> analysis, knowledge management, data preparation.</li>
<li><strong>Research:</strong> search, reasoning, working with sources.</li>
<li><strong>Agents:</strong> automation, workflows, autonomous execution.</li>
<li><strong>Transcription:</strong> turning meetings, interviews and voice recordings into text, summaries and translations. Since October 2026. The legal framework for recordings in Switzerland and the EU is covered in the <a href="https://transcribe.fragroger.ai/" rel="noopener">data protection guide to AI transcription</a> (German, French, Italian).</li>
</ul>
<p>Exactly one tool is chosen per category. If a category has no relevant new release, an existing tool with an important update takes its place. The selection changes every week; tools are deliberately not compared with each other.</p>

<h2>Research sources</h2>
<p>AI Breakfast, There's An AI For That, FutureTools.io, Ben's Bites, Futurepedia.io, Product Hunt (AI category), Toolify.ai, TopAI.tools, The AI Citizen (Weekly Tool Roundup), plus AI-Weekly, The Batch, The Sequence and AI Tidbits for tool mentions. Pricing, feature and privacy details are then checked against the providers' official documentation.</p>

<h2>What every review contains</h2>
<ul>
<li>Short description of function and target group</li>
<li>Three to five practical use cases</li>
<li>Pricing in CHF or USD, including any free tier</li>
<li>Data protection: server location, policies, GDPR and Swiss FADP, self-hosting</li>
<li>Strengths and weaknesses</li>
<li>Practical assessment</li>
<li>Relevance rating from 1 to 10</li>
</ul>

<h2>How relevance is rated</h2>
<p>The number describes the expected value for organisations in Switzerland, Germany and Austria, not technical brilliance. It combines four questions: Does the tool solve a common problem? Can it be used productively today? Are costs and data flows transparent? How strong is the dependency on a single provider? Scores of 9 and above are rare and mark tools that noticeably shift ways of working.</p>

<h2>Rhythm and production</h2>
<p>A new issue appears every Sunday morning in German and English. Research, selection and texts are produced with the help of AI and published automatically. Until October 2026 production ran on Manus, since week 43/2026 on Claude. All earlier issues remain in the <a href="archive.html">archive</a>; issues from before the English edition are available in English as summaries, with the detailed reviews in German.</p>
"""

IMPRINT_EN = """
<h2>Responsible for the content</h2>
<p>{name}<br>{company}<br>{street}<br>{city}<br>{country_l}</p>
<p>Email: <a href="mailto:{email}">{email}</a><br>Web: <a href="{web}">{web}</a></p>
<h2>What this site is</h2>
<p>AI Tool Reviews is a weekly, editorially curated overview of new and updated AI tools. Every Sunday six reviews appear in the categories text, design, data / knowledge, research, agents and transcription.</p>
<h2>Disclaimer</h2>
<p>The content is prepared with care. Research, selection and texts are, however, produced with the help of AI systems and published automatically. No guarantee is given for accuracy, completeness or timeliness. Providers' prices, features and privacy terms change constantly; their current documentation is authoritative. Liability claims for material or immaterial damage arising from the use or non-use of the information are excluded to the extent permitted by law. The content is not legal, purchasing or other advice.</p>
<h2>Links to third-party sites</h2>
<p>The reviews link to providers' websites and to sources. The operators of linked pages are solely responsible for their content. Brand and product names belong to their respective owners.</p>
<h2>Copyright</h2>
<p>The reviews may be shared and quoted with attribution ("AI Tool Reviews, Roger Basler de Roca").</p>
"""

PRIVACY_EN = """
<p>This site uses no cookies, no tracking and no external fonts or third-party scripts. There are no user accounts and no forms.</p>
<h2>Controller</h2>
<p>{name}, {company}, {street}, {city}, {country_l}, <a href="mailto:{email}">{email}</a></p>
<h2>Hosting</h2>
<p>The site is delivered via GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). When you visit, GitHub processes technically necessary connection data such as IP address, time of access, page requested, browser type and referrer in server logs in order to deliver the site and keep the service secure. The legal basis is the legitimate interest in operating the website securely. Details: <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<h2>Archive search</h2>
<p>The archive search runs entirely in your browser. Search terms are neither transmitted nor stored.</p>
<h2>External links</h2>
<p>When you follow a link to a provider or a source, that site's privacy policy applies.</p>
<h2>Your rights</h2>
<p>Under the Swiss Federal Act on Data Protection (FADP) and, where applicable, the GDPR, you have the right to access, rectify, erase and restrict the processing of your personal data. Please contact <a href="mailto:{email}">{email}</a>.</p>
<p>Last updated: October 2026</p>
"""

NOT_FOUND = """
<p>Diese Adresse führt ins Leere. Die aktuelle Woche liegt auf der <a href="/">Startseite</a>, alle früheren Wochen im <a href="/archiv.html">Archiv</a>.</p>
<p lang="en">This page does not exist. The current week is on the <a href="/en/">home page</a>, all earlier weeks are in the <a href="/en/archive.html">archive</a>.</p>
"""

TEXTS = {
    "de": {"method": METHOD, "imprint": IMPRINT, "privacy": PRIVACY},
    "en": {"method": METHOD_EN, "imprint": IMPRINT_EN, "privacy": PRIVACY_EN},
}
