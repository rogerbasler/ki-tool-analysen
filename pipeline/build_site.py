"""Baut die statische Website aus data/weeks/*.json.

Aufruf (aus dem Repo-Root): python3 pipeline/build_site.py
Erzeugt: index.html, archiv.html, archiv/<jahr>/kwNN-<datum>.html (+ -analyse.html),
methode.html, impressum.html, datenschutz.html, 404.html, feed.xml, sitemap.xml,
robots.txt, archiv/data/archive-index.json und Weiterleitungen für alte URLs.
"""
import datetime as dt
import glob
import html
import json
import os
import re
import shutil
import sys

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
import legal  # noqa: E402

SITE_URL = "https://rogerbasler.github.io/ki-tool-analysen"
CATEGORIES = ["Text", "Design", "Data / Wissen", "Recherche", "Agents"]
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
          "September", "Oktober", "November", "Dezember"]
BUILD_ID = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M")


# ------------------------------------------------------------------ Helfer
def date_text(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.day}. {MONTHS[d.month - 1]} {d.year}"


def score(v):
    if v is None or v == "":
        return ""
    v = float(v)
    return str(int(v)) if v == int(v) else f"{v:.1f}".replace(".", ",")


def slug(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "tool"


URL_RE = re.compile(r"(https?://[^\s<>\"]+[^\s<>\".,;:)\]])")


def linkify(escaped_text):
    return URL_RE.sub(lambda m: f'<a href="{m.group(1)}" rel="noopener" target="_blank">{m.group(1)}</a>', str(escaped_text))


def rich(text):
    """Absätze (Leerzeile) und Aufzählungen ("• " oder "- ") als HTML."""
    if not text:
        return Markup("")
    if isinstance(text, list):
        text = "\n".join("• " + x for x in text)
    out, items = [], []

    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{lead_bold(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if lines and all(re.match(r"^(?:•|-|\*)\s+", l) for l in lines):
            items.extend(re.sub(r"^(?:•|-|\*)\s+", "", l) for l in lines)
            continue
        flush()
        out.append(f"<p>{linkify(escape(' '.join(lines)))}</p>")
    flush()
    return Markup("".join(out))


def lead_bold(s):
    s = str(s)
    m = re.match(r"^([^:]{2,45}):\s+(.+)$", s, re.S)
    if m and not m.group(1).startswith("http"):
        return Markup(f"<strong>{escape(m.group(1))}:</strong> {linkify(escape(m.group(2)))}")
    return Markup(linkify(escape(s)))


def source(q):
    if isinstance(q, dict):
        title = q.get("titel") or q.get("title") or q.get("url", "")
        parts = [escape(title)]
        if q.get("url"):
            parts = [Markup(f'<a href="{escape(q["url"])}" rel="noopener" target="_blank">{escape(title)}</a>')]
        return Markup("".join(str(p) for p in parts))
    return Markup(linkify(escape(q)))


env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")),
                  autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True)
env.filters.update(score=score, rich=rich, lead_bold=lead_bold, source=source)


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def root_for(rel):
    depth = rel.count("/")
    return "../" * depth


def base_ctx(rel, section, title, description, **extra):
    ctx = dict(root=root_for(rel), section=section, page_title=title, page_description=description,
               canonical=f"{SITE_URL}/{'' if rel == 'index.html' else rel}", site_url=SITE_URL,
               build_id=BUILD_ID, year=dt.date.today().year, categories=CATEGORIES)
    ctx.update(extra)
    return ctx


# ------------------------------------------------------------------ Markdown-Export
def is_legacy(w):
    return "Manus" in (w.get("quelle") or "")


def export_markdown(w):
    """Schreibt die vollständige Markdown-Analyse einer neuen Woche aus dem JSON."""
    L = [f"# KI-Tool-Analysen KW {w['kw']:02d}/{w['jahr']}", ""]
    meta = [f"**Datum:** {date_text(w['datum'])}"]
    if w.get("zeitraum"):
        meta.append(f"**Recherchezeitraum:** {w['zeitraum']}")
    L += ["  \n".join(meta), "", "## Wochenzusammenfassung", "", w["zusammenfassung"], ""]
    for h in w.get("highlights") or []:
        L.append(f"- {h}")
    if w.get("trend"):
        L += ["", f"**Trend:** {w['trend']}"]
    L += ["", "| Kategorie | Tool | Relevanz |", "|---|---|---:|"]
    for t in w["tools"]:
        L.append(f"| {t['kategorie']} | {t['name']} | {score(t.get('bewertung'))}/10 |")
    sources = []
    for i, t in enumerate(w["tools"], 1):
        L += ["", "---", "", f"## {i}. {t['name']}", "",
              f"**Kategorie:** {t['kategorie']}  ", f"**Relevanzbewertung:** {score(t.get('bewertung'))}/10  "]
        if t.get("url"):
            L.append(f"**Website:** {t['url']}  ")
        if t.get("signal"):
            L.append(f"**Aktualitätssignal:** {t['signal']}")
        L += ["", "### Kurzbeschreibung", "", t.get("kurzbeschreibung", "")]
        if t.get("beschreibung"):
            L += ["", t["beschreibung"]]
        L += ["", "### Nutzungsszenarien", ""] + [f"- {x}" for x in t.get("nutzungsszenarien", [])]
        L += ["", "### Pricing", "", t.get("pricing", ""), "", "### Datenschutz", "", t.get("datenschutz", "")]
        L += ["", "### Stärken", ""] + [f"- {x}" for x in t.get("staerken", [])]
        L += ["", "### Schwächen", ""] + [f"- {x}" for x in t.get("schwaechen", [])]
        L += ["", "### Einschätzung für die Praxis", "", t.get("einschaetzung", ""), "",
              f"**Relevanzbewertung:** {score(t.get('bewertung'))}/10"]
        for q in t.get("quellen") or []:
            if q not in sources:
                sources.append(q)
    if sources:
        L += ["", "---", "", "## Quellen", ""] + [f"- {q}" for q in sorted(sources, key=str.lower)]
    rel = f"archiv/data/ki-tool-analysen-{w['datum']}.md"
    write(rel, "\n".join(L).rstrip() + "\n")
    return rel


# ------------------------------------------------------------------ Daten
def load_weeks():
    weeks = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data/weeks/*.json"))):
        w = json.load(open(f, encoding="utf-8"))
        w["page"] = f"archiv/{w['jahr']}/kw{w['kw']:02d}-{w['datum']}.html"
        if not is_legacy(w):
            w["markdown"] = export_markdown(w)
        # Eigene Vollanalyse-Seite nur für migrierte Wochen; neue Wochen stehen vollständig auf der Wochenseite
        w["analysis_page"] = w["page"].replace(".html", "-analyse.html") if is_legacy(w) and w.get("markdown") and os.path.exists(os.path.join(ROOT, w["markdown"])) else None
        w["date_text"] = date_text(w["datum"])
        w["tools"].sort(key=lambda t: CATEGORIES.index(t["kategorie"]) if t.get("kategorie") in CATEGORIES else 9)
        used = set()
        for t in w["tools"]:
            a = slug(t["name"])
            while a in used:
                a += "-2"
            used.add(a)
            t["anchor"] = a
            t["search"] = " ".join(filter(None, [t.get("name"), t.get("kategorie"), t.get("kurzbeschreibung"), t.get("beschreibung", "")[:400]]))
        hl = " ".join(w.get("highlights") or [])
        w["show_trend"] = bool(w.get("trend")) and w["trend"] not in hl and not any(h.lower().startswith("trend") for h in w.get("highlights") or [])
        rated = [t["bewertung"] for t in w["tools"] if t.get("bewertung") is not None]
        w["avg"] = round(sum(rated) / len(rated), 1) if rated else None
        weeks.append(w)
    weeks.sort(key=lambda w: w["datum"])
    return weeks


# ------------------------------------------------------------------ Seiten
def jsonld(w, rel):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"KI-Tool-Analysen KW {w['kw']:02d}/{w['jahr']}",
        "datePublished": w["datum"],
        "inLanguage": "de-CH",
        "author": {"@type": "Person", "name": "Roger Basler de Roca", "url": "https://fragroger.ai"},
        "url": f"{SITE_URL}/{rel}",
        "about": [{"@type": "SoftwareApplication", "name": t["name"], "applicationCategory": t.get("kategorie"),
                   **({"url": t["url"]} if t.get("url") else {})} for t in w["tools"]],
    }, ensure_ascii=False)


def render_week(w, rel, is_latest, prev_w, next_w):
    names = ", ".join(t["name"] for t in w["tools"])
    title = f"KW {w['kw']:02d}/{w['jahr']}: {names} | KI-Tool-Analysen"
    desc = (w.get("zusammenfassung") or f"Die fünf KI-Tools der KW {w['kw']}/{w['jahr']}: {names}.")[:300]
    rated = [t["bewertung"] for t in w["tools"] if t.get("bewertung") is not None]
    ctx = base_ctx(rel, "current" if is_latest else "archive", title, desc,
                   week=w, is_latest=is_latest, date_text=w["date_text"], jsonld=jsonld(w, rel),
                   top_score=max(rated) if rated else None,
                   analysis_href=(root_for(rel) + w["analysis_page"]) if w["analysis_page"] else None,
                   prev_week=prev_w, next_week=next_w)
    write(rel, env.get_template("week.html").render(**ctx))


def render_analysis(w):
    rel = w["analysis_page"]
    text = open(os.path.join(ROOT, w["markdown"]), encoding="utf-8").read()
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)          # Front Matter
    text = re.sub(r"\A\s*#\s+[^\n]*\n", "", text)                        # erste H1
    body = markdown.markdown(text, extensions=["tables", "sane_lists", "attr_list"])
    body = body.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
    body = re.sub(r"<h1>", "<h2>", body).replace("</h1>", "</h2>")
    # Sprunganker je Tool (voller Name, sonst die ersten zwei Wörter, sonst das erste Wort)
    w["analysis_anchors"] = set()
    for t in w["tools"]:
        base = re.split(r"\s[(+&]", t["name"])[0].strip()
        words = base.split()
        for cand in [base[:25], " ".join(words[:2]), words[0] if words and len(words[0]) > 3 else None]:
            if not cand:
                continue
            body, n = re.subn(rf"<(h[234])>((?:(?!</h[234]>).)*?{re.escape(cand)})", rf'<\1 id="{t["anchor"]}">\2', body, count=1, flags=re.I | re.S)
            if n:
                w["analysis_anchors"].add(t["anchor"])
                break
    week_href = root_for(rel) + w["page"]
    ctx = base_ctx(rel, "archive", f"Vollanalyse KW {w['kw']:02d}/{w['jahr']} | KI-Tool-Analysen",
                   f"Ausführliche Analyse der KI-Tools der KW {w['kw']}/{w['jahr']}.",
                   kicker=f"Vollanalyse · KW {w['kw']:02d}/{w['jahr']} · {w['date_text']}",
                   heading="Die ausführliche Fassung",
                   lead=", ".join(t["name"] for t in w["tools"]),
                   actions=[{"href": week_href, "label": "Zur Wochenübersicht"},
                            {"href": root_for(rel) + w["markdown"], "label": "Markdown herunterladen"}],
                   note=("Diese Fassung stammt aus dem Archiv und wird unverändert wiedergegeben." if "Manus" in w.get("quelle", "") else None),
                   body=Markup(body))
    write(rel, env.get_template("page.html").render(**ctx))


def render_archive(weeks):
    rel = "archiv.html"
    rated = [t["bewertung"] for w in weeks for t in w["tools"] if t.get("bewertung") is not None]
    stats = {"weeks": len(weeks), "tools": sum(len(w["tools"]) for w in weeks),
             "avg": round(sum(rated) / len(rated), 1) if rated else None}
    years = sorted({w["jahr"] for w in weeks}, reverse=True)
    ctx = base_ctx(rel, "archive", "Archiv | KI-Tool-Analysen",
                   "Alle wöchentlichen KI-Tool-Analysen seit Dezember 2025, durchsuchbar nach Tool, Kategorie und Jahr.",
                   weeks=list(reversed(weeks)), stats=stats, years=years)
    write(rel, env.get_template("archive.html").render(**ctx))


def render_page(rel, section, title, desc, heading, body, kicker=None, lead=None, noindex=False):
    ctx = base_ctx(rel, section, title, desc, heading=heading, body=Markup(body), kicker=kicker, lead=lead, noindex=noindex)
    write(rel, env.get_template("page.html").render(**ctx))


def render_redirect(rel, target_rel, label):
    root = root_for(rel)
    url = root + target_rel
    write(rel, f"""<!DOCTYPE html>
<html lang="de-CH"><head><meta charset="utf-8"><title>{html.escape(label)}</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{SITE_URL}/{target_rel}">
<meta http-equiv="refresh" content="0; url={url}"></head>
<body style="background:#000;color:#fff;font-family:system-ui,sans-serif;padding:2rem">
<p>Diese Seite ist umgezogen: <a style="color:#fff" href="{url}">{html.escape(label)}</a></p>
<script>location.replace({json.dumps(url)} + location.hash);</script>
</body></html>
""")


def render_feed(weeks):
    items = []
    for w in reversed(weeks[-30:]):
        link = f"{SITE_URL}/{w['page']}"
        pub = dt.datetime.combine(dt.date.fromisoformat(w["datum"]), dt.time(6, 0), dt.timezone.utc)
        tools = "".join(f"<li><strong>{html.escape(t['kategorie'])}: {html.escape(t['name'])}</strong> ({score(t.get('bewertung'))}/10). {html.escape(t.get('kurzbeschreibung', ''))}</li>" for t in w["tools"])
        desc = f"<p>{html.escape(w.get('zusammenfassung', ''))}</p><ul>{tools}</ul>"
        items.append(f"""  <item>
    <title>KW {w['kw']:02d}/{w['jahr']}: {html.escape(', '.join(t['name'] for t in w['tools']))}</title>
    <link>{link}</link>
    <guid isPermaLink="true">{link}</guid>
    <pubDate>{pub.strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
    <description><![CDATA[{desc}]]></description>
  </item>""")
    write("feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>KI-Tool-Analysen (#fragRoger)</title>
  <link>{SITE_URL}/</link>
  <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Jeden Sonntag fünf KI-Tools, eingeordnet nach Nutzen, Kosten und Datenschutz.</description>
  <language>de-ch</language>
{chr(10).join(items)}
</channel>
</rss>
""")


def render_sitemap(weeks, extra):
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{p}" for p in extra]
    for w in weeks:
        urls.append(f"{SITE_URL}/{w['page']}")
        if w["analysis_page"]:
            urls.append(f"{SITE_URL}/{w['analysis_page']}")
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


def render_compat_index(weeks):
    """archiv/data/archive-index.json im bisherigen Format, für bestehende Verweise."""
    data = {"analysen": [{
        "kw": w["kw"], "jahr": w["jahr"], "datum": w["datum"], "url": w["page"],
        "tools": [{"name": t["name"], "kategorie": t["kategorie"], "bewertung": t.get("bewertung"),
                   "kurzbeschreibung": t.get("kurzbeschreibung", "")} for t in w["tools"]],
        "highlights": (w.get("highlights") or [""])[0], "trend": w.get("trend", ""),
    } for w in reversed(weeks)]}
    write("archiv/data/archive-index.json", json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def clean_generated():
    for f in glob.glob(os.path.join(ROOT, "archiv/20*/*.html")):
        os.remove(f)


def main():
    weeks = load_weeks()
    if not weeks:
        sys.exit("Keine Wochen in data/weeks gefunden.")
    clean_generated()
    for i, w in enumerate(weeks):
        prev_w = weeks[i - 1] if i > 0 else None
        next_w = weeks[i + 1] if i + 1 < len(weeks) else None
        if w["analysis_page"]:
            render_analysis(w)
        render_week(w, w["page"], False, prev_w, next_w)
    latest = weeks[-1]
    render_week(latest, "index.html", True, weeks[-2] if len(weeks) > 1 else None, None)
    render_archive(weeks)

    o = legal.OWNER
    render_page("methode.html", "method", "Methode | KI-Tool-Analysen",
                "Wie die wöchentlichen KI-Tool-Analysen entstehen: Quellen, Kategorien, Bewertung.",
                "So entstehen die Analysen", legal.METHOD, kicker="Methode",
                lead="Jede Woche ein Tool pro Kategorie, ausgewählt aus zehn Quellen und nach festen Kriterien geprüft.")
    render_page("impressum.html", "legal", "Impressum | KI-Tool-Analysen", "Impressum der KI-Tool-Analysen.",
                "Impressum", legal.IMPRINT.format(**o), kicker="Rechtliches")
    render_page("datenschutz.html", "legal", "Datenschutz | KI-Tool-Analysen", "Datenschutzerklärung der KI-Tool-Analysen.",
                "Datenschutz", legal.PRIVACY.format(**o), kicker="Rechtliches")
    render_page("404.html", "none", "Seite nicht gefunden | KI-Tool-Analysen", "Diese Seite gibt es nicht.",
                "Seite nicht gefunden",
                '<p>Diese Adresse führt ins Leere. Die aktuelle Woche liegt auf der <a href="/ki-tool-analysen/">Startseite</a>, alle früheren Wochen im <a href="/ki-tool-analysen/archiv.html">Archiv</a>.</p>',
                kicker="404", noindex=True)

    # Weiterleitungen für alte, unregelmässig benannte Archivdateien
    by_date = {w["datum"]: w for w in weeks}
    redirects = json.load(open(os.path.join(ROOT, "data/legacy-redirects.json"), encoding="utf-8"))
    for old, datum in redirects.items():
        w = by_date.get(datum)
        if w:
            render_redirect(old, w["page"], f"KW {w['kw']:02d}/{w['jahr']}")

    render_feed(weeks)
    render_sitemap(weeks, ["archiv.html", "methode.html", "impressum.html", "datenschutz.html"])
    render_compat_index(weeks)
    open(os.path.join(ROOT, ".nojekyll"), "a").close()
    print(f"Gebaut: {len(weeks)} Wochen, aktuell KW {latest['kw']:02d}/{latest['jahr']} ({latest['datum']}).")


if __name__ == "__main__":
    main()
