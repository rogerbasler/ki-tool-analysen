"""Baut die statische Website (DE und EN) aus data/weeks/*.json und data/weeks/en/*.json.

Aufruf (aus dem Repo-Root): python3 pipeline/build_site.py
DE liegt im Wurzelverzeichnis (index.html, archiv.html, archiv/<jahr>/kwNN-<datum>.html, ...),
EN unter en/ (en/index.html, en/archive.html, en/archive/<jahr>/weekNN-<datum>.html, ...).
"""
import copy
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
from i18n import CAT_LABEL, CATEGORIES, LANGS, PATHS, T, date_text, score, week_page  # noqa: E402

SITE_URL = "https://tools.fragroger.ai"
BUILD_ID = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M")

# Felder, die in der englischen Fassung übersetzt werden
TEXT_FIELDS_WEEK = ["zeitraum", "zusammenfassung", "highlights", "trend"]
TEXT_FIELDS_TOOL = ["signal", "kurzbeschreibung", "beschreibung", "nutzungsszenarien", "pricing", "datenschutz",
                    "staerken", "schwaechen", "einschaetzung", "felder"]


# ------------------------------------------------------------------ Helfer
def slug(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "tool"


URL_RE = re.compile(r"(https?://[^\s<>\"]+[^\s<>\".,;:)\]])")


def linkify(escaped_text):
    return URL_RE.sub(lambda m: f'<a href="{m.group(1)}" rel="noopener" target="_blank">{m.group(1)}</a>', str(escaped_text))


def lead_bold(s):
    s = str(s)
    m = re.match(r"^([^:]{2,45}):\s+(.+)$", s, re.S)
    if m and not m.group(1).startswith("http"):
        return Markup(f"<strong>{escape(m.group(1))}:</strong> {linkify(escape(m.group(2)))}")
    return Markup(linkify(escape(s)))


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


def source(q):
    if isinstance(q, dict):
        title = q.get("titel") or q.get("title") or q.get("url", "")
        if q.get("url"):
            return Markup(f'<a href="{escape(q["url"])}" rel="noopener" target="_blank">{escape(title)}</a>')
        return escape(title)
    return Markup(linkify(escape(q)))


env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")),
                  autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True)
env.filters.update(rich=rich, lead_bold=lead_bold, source=source)


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def root_for(rel):
    return "../" * rel.count("/")


def url_for(rel):
    if rel.endswith("index.html"):
        rel = rel[: -len("index.html")]
    return f"{SITE_URL}/{rel}"


def href(root, rel):
    """Relativer Link; index.html wird zum Verzeichnis."""
    if rel.endswith("index.html"):
        rel = rel[: -len("index.html")]
    return (root + rel) or "./"


def base_ctx(lang, rel, section, title, description, alternates=None, **extra):
    root = root_for(rel)
    alts = alternates or {l: PATHS[l]["home"] for l in LANGS}
    nav = {k: href(root, v) for k, v in PATHS[lang].items()}
    ctx = dict(
        T=T[lang], lang=lang, root=root, section=section, page_title=title, page_description=description,
        canonical=url_for(rel), site_url=SITE_URL, build_id=BUILD_ID, year=dt.date.today().year,
        nav=nav, alt_links={l: href(root, p) for l, p in alts.items()}, alt_urls={l: url_for(p) for l, p in alts.items()},
        categories=[(c, CAT_LABEL[lang][c]) for c in CATEGORIES],
        cat=lambda c: CAT_LABEL[lang].get(c, c), fmt=lambda v: score(v, lang),
    )
    ctx.update(extra)
    return ctx


def is_legacy(w):
    return "Manus" in (w.get("quelle") or "")


# ------------------------------------------------------------------ Markdown-Export
MD_LABELS = {
    "de": dict(title="KI-Tool-Analysen KW {kw}/{jahr}", date="Datum", period="Recherchezeitraum", summary="Wochenzusammenfassung",
               trend="Trend", cat="Kategorie", rel="Relevanz", relfull="Relevanzbewertung", web="Website", signal="Aktualitätssignal",
               short="Kurzbeschreibung", scen="Nutzungsszenarien", price="Pricing", priv="Datenschutz", pro="Stärken",
               con="Schwächen", verdict="Einschätzung für die Praxis", sources="Quellen", suffix=""),
    "en": dict(title="AI Tool Reviews, week {kw}/{jahr}", date="Date", period="Research period", summary="Weekly summary",
               trend="Trend", cat="Category", rel="Relevance", relfull="Relevance rating", web="Website", signal="Signal this week",
               short="Short description", scen="Use cases", price="Pricing", priv="Data protection", pro="Strengths",
               con="Weaknesses", verdict="Practical assessment", sources="Sources", suffix=".en"),
}


def export_markdown(w, lang):
    m = MD_LABELS[lang]
    L = ["# " + m["title"].format(kw=f"{w['kw']:02d}", jahr=w["jahr"]), ""]
    meta = [f"**{m['date']}:** {date_text(w['datum'], lang)}"]
    if w.get("zeitraum"):
        meta.append(f"**{m['period']}:** {w['zeitraum']}")
    L += ["  \n".join(meta), "", f"## {m['summary']}", "", w["zusammenfassung"], ""]
    L += [f"- {h}" for h in w.get("highlights") or []]
    if w.get("trend"):
        L += ["", f"**{m['trend']}:** {w['trend']}"]
    L += ["", f"| {m['cat']} | Tool | {m['rel']} |", "|---|---|---:|"]
    L += [f"| {CAT_LABEL[lang][t['kategorie']]} | {t['name']} | {score(t.get('bewertung'), lang)}/10 |" for t in w["tools"]]
    sources = []
    for i, t in enumerate(w["tools"], 1):
        L += ["", "---", "", f"## {i}. {t['name']}", "", f"**{m['cat']}:** {CAT_LABEL[lang][t['kategorie']]}  ",
              f"**{m['relfull']}:** {score(t.get('bewertung'), lang)}/10  "]
        if t.get("url"):
            L.append(f"**{m['web']}:** {t['url']}  ")
        if t.get("signal"):
            L.append(f"**{m['signal']}:** {t['signal']}")
        L += ["", f"### {m['short']}", "", t.get("kurzbeschreibung", "")]
        if t.get("beschreibung"):
            L += ["", t["beschreibung"]]
        L += ["", f"### {m['scen']}", ""] + [f"- {x}" for x in t.get("nutzungsszenarien", [])]
        L += ["", f"### {m['price']}", "", t.get("pricing", ""), "", f"### {m['priv']}", "", t.get("datenschutz", "")]
        L += ["", f"### {m['pro']}", ""] + [f"- {x}" for x in t.get("staerken", [])]
        L += ["", f"### {m['con']}", ""] + [f"- {x}" for x in t.get("schwaechen", [])]
        L += ["", f"### {m['verdict']}", "", t.get("einschaetzung", ""), "", f"**{m['relfull']}:** {score(t.get('bewertung'), lang)}/10"]
        for q in t.get("quellen") or []:
            if q not in sources:
                sources.append(q)
    if sources:
        L += ["", "---", "", f"## {m['sources']}", ""] + [f"- {q}" for q in sorted(sources, key=str.lower)]
    rel = f"archiv/data/ki-tool-analysen-{w['datum']}{m['suffix']}.md"
    write(rel, "\n".join(L).rstrip() + "\n")
    return rel


# ------------------------------------------------------------------ Daten
def prepare(w, lang):
    w["lang"] = lang
    w["page"] = week_page(lang, w)
    w["date_text"] = date_text(w["datum"], lang)
    w["tools"].sort(key=lambda t: CATEGORIES.index(t["kategorie"]) if t.get("kategorie") in CATEGORIES else 9)
    used = set()
    for t in w["tools"]:
        a = slug(t["name"])
        while a in used:
            a += "-2"
        used.add(a)
        t["anchor"] = a
        t["search"] = " ".join(filter(None, [t.get("name"), CAT_LABEL[lang].get(t.get("kategorie"), ""),
                                             t.get("kurzbeschreibung"), (t.get("beschreibung") or "")[:400]]))
    hl = w.get("highlights") or []
    w["show_trend"] = bool(w.get("trend")) and w["trend"] not in " ".join(hl) and not any(h.lower().startswith("trend") for h in hl)
    rated = [t["bewertung"] for t in w["tools"] if t.get("bewertung") is not None]
    w["avg"] = round(sum(rated) / len(rated), 1) if rated else None
    w["top_score"] = max(rated) if rated else None
    return w


def localize_en(de, overlay):
    """Englische Fassung: Struktur (Kategorie, Bewertung, URL, Quellen) aus DE, Texte aus dem Overlay."""
    w = copy.deepcopy(de)
    for k in ["markdown", "analysis_page", "analysis_anchors"]:
        w.pop(k, None)
    for k in TEXT_FIELDS_WEEK:
        w[k] = overlay.get(k, "" if k != "highlights" else [])
    full = overlay.get("umfang", "voll") == "voll"
    w["partial"] = not full
    ov_tools = {t["name"]: t for t in overlay.get("tools", [])}
    for t in w["tools"]:
        o = ov_tools.get(t["name"])
        if o is None:
            raise SystemExit(f"EN-Overlay {de['datum']}: Tool {t['name']!r} fehlt")
        for k in TEXT_FIELDS_TOOL:
            t.pop(k, None)
            if o.get(k):
                t[k] = o[k]
    return w


def load_weeks():
    weeks = {"de": [], "en": []}
    for f in sorted(glob.glob(os.path.join(ROOT, "data/weeks/*.json"))):
        de = json.load(open(f, encoding="utf-8"))
        prepare(de, "de")
        if not is_legacy(de):
            de["markdown"] = export_markdown(de, "de")
        de["analysis_page"] = de["page"].replace(".html", "-analyse.html") if is_legacy(de) and de.get("markdown") and os.path.exists(os.path.join(ROOT, de["markdown"])) else None
        weeks["de"].append(de)
        en_file = os.path.join(ROOT, "data/weeks/en", os.path.basename(f))
        if os.path.exists(en_file):
            en = localize_en(de, json.load(open(en_file, encoding="utf-8")))
            prepare(en, "en")
            if not en["partial"]:
                en["markdown"] = export_markdown(en, "en")
            en["de_page"] = de["page"]
            en["de_analysis_page"] = de["analysis_page"]
            weeks["en"].append(en)
        else:
            print(f"Hinweis: keine englische Fassung für {de['datum']}")
    for l in LANGS:
        weeks[l].sort(key=lambda w: w["datum"])
    return weeks


# ------------------------------------------------------------------ Seiten
def jsonld(w, rel, lang):
    return json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": f"{T[lang]['site']} {T[lang]['week']} {w['kw']:02d}/{w['jahr']}",
        "datePublished": w["datum"], "inLanguage": T[lang]["html_lang"],
        "author": {"@type": "Person", "name": "Roger Basler de Roca", "url": "https://fragroger.ai"},
        "url": url_for(rel),
        "about": [{"@type": "SoftwareApplication", "name": t["name"], "applicationCategory": CAT_LABEL[lang][t["kategorie"]],
                   **({"url": t["url"]} if t.get("url") else {})} for t in w["tools"]],
    }, ensure_ascii=False)


def render_week(w, rel, is_latest, prev_w, next_w, alternates):
    lang, tt = w["lang"], T[w["lang"]]
    names = ", ".join(t["name"] for t in w["tools"])
    title = f"{tt['week']} {w['kw']:02d}/{w['jahr']}: {names} | {tt['site']}"
    desc = (w.get("zusammenfassung") or tt["week_desc"].format(kw=w["kw"], jahr=w["jahr"], names=names))[:300]
    root = root_for(rel)
    if lang == "de":
        analysis = w.get("analysis_page")
        partial_href = None
    else:
        analysis = w.get("de_analysis_page")
        partial_href = href(root, w["de_page"]) if w.get("partial") else None
    ctx = base_ctx(lang, rel, "current" if is_latest else "archive", title, desc, alternates,
                   week=w, is_latest=is_latest, jsonld=jsonld(w, rel, lang),
                   analysis_href=href(root, analysis) if analysis else None,
                   analysis_anchors=w.get("analysis_anchors") or (de_anchor_lookup.get(w["datum"]) if lang == "en" else set()) or set(),
                   partial_href=partial_href,
                   prev_week=prev_w, next_week=next_w)
    write(rel, env.get_template("week.html").render(**ctx))


de_anchor_lookup = {}


def render_analysis(w):
    rel = w["analysis_page"]
    text = open(os.path.join(ROOT, w["markdown"]), encoding="utf-8").read()
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\A\s*#\s+[^\n]*\n", "", text)
    body = markdown.markdown(text, extensions=["tables", "sane_lists", "attr_list"])
    body = body.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
    body = body.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
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
    de_anchor_lookup[w["datum"]] = w["analysis_anchors"]
    tt, root = T["de"], root_for(rel)
    ctx = base_ctx("de", rel, "archive", tt["analysis_title"].format(kw=f"{w['kw']:02d}", jahr=w["jahr"]),
                   tt["analysis_desc"].format(kw=w["kw"], jahr=w["jahr"]),
                   {"de": rel, "en": week_page("en", w)},
                   kicker=f"{tt['analysis_kicker']} · KW {w['kw']:02d}/{w['jahr']} · {w['date_text']}",
                   heading=tt["analysis_heading"], lead=", ".join(t["name"] for t in w["tools"]),
                   actions=[{"href": href(root, w["page"]), "label": tt["to_week"]},
                            {"href": href(root, w["markdown"]), "label": tt["download_md"]}],
                   note=tt["analysis_note"], body=Markup(body))
    write(rel, env.get_template("page.html").render(**ctx))


def render_archive(weeks, lang, alternates):
    rel = PATHS[lang]["archive"]
    tt = T[lang]
    rated = [t["bewertung"] for w in weeks for t in w["tools"] if t.get("bewertung") is not None]
    stats = {"weeks": len(weeks), "tools": sum(len(w["tools"]) for w in weeks),
             "avg": round(sum(rated) / len(rated), 1) if rated else None}
    years = sorted({w["jahr"] for w in weeks}, reverse=True)
    ctx = base_ctx(lang, rel, "archive", tt["archive_page_title"], tt["archive_desc"], alternates,
                   weeks=list(reversed(weeks)), stats=stats, years=years)
    write(rel, env.get_template("archive.html").render(**ctx))


def render_page(lang, key, section, title, desc, heading, body, alternates, kicker=None, lead=None, noindex=False, rel=None):
    rel = rel or PATHS[lang][key]
    ctx = base_ctx(lang, rel, section, title, desc, alternates, heading=heading, body=Markup(body),
                   kicker=kicker, lead=lead, noindex=noindex)
    write(rel, env.get_template("page.html").render(**ctx))


def load_topic(name):
    """Themenseite: DE-Datei liefert Struktur, URLs, Bewertungen, Quellen; EN-Datei die Texte."""
    de = json.load(open(os.path.join(ROOT, f"data/themen/{name}.json"), encoding="utf-8"))
    out = {"de": de}
    en_path = os.path.join(ROOT, f"data/themen/{name}.en.json")
    if os.path.exists(en_path):
        ov = json.load(open(en_path, encoding="utf-8"))
        en = copy.deepcopy(de)
        for k, v in ov.items():
            if k not in ("fokus", "gruppen", "guide"):
                en[k] = v
        en["guide"] = {**de["guide"], **ov.get("guide", {})}
        ovf = {f["name"]: f for f in ov.get("fokus", [])}
        for t in en["fokus"]:
            t.update({k: v for k, v in ovf.get(t["name"], {}).items() if k != "name"})
        ovg = {g["id"]: g for g in ov.get("gruppen", [])}
        for g in en["gruppen"]:
            o = ovg.get(g["id"], {})
            for k in ("titel", "badge", "intro", "hinweis"):
                if k in o:
                    g[k] = o[k]
            for x in g["tools"]:
                x.update(o.get("tools", {}).get(x["name"], {}))
        out["en"] = en
    for t in out["de"]["fokus"] + (out["en"]["fokus"] if "en" in out else []):
        t["anchor"] = slug(t["name"])
    return out


def render_topic(name):
    topics = load_topic(name)
    alt = {l: PATHS[l]["transcription"] for l in topics}
    for lang, topic in topics.items():
        rel = PATHS[lang]["transcription"]
        tt = T[lang]
        ctx = base_ctx(lang, rel, "transcription", tt["topic_page_title"], tt["topic_desc"], alt,
                       topic=topic, stand_text=date_text(topic["stand"], lang), guide_url=topic["guide"]["url"])
        write(rel, env.get_template("topic.html").render(**ctx))
    return list(alt.values())


def render_redirect(rel, target_rel, label):
    url = href(root_for(rel), target_rel)
    write(rel, f"""<!DOCTYPE html>
<html lang="de-CH"><head><meta charset="utf-8"><title>{html.escape(label)}</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{url_for(target_rel)}">
<meta http-equiv="refresh" content="0; url={url}"></head>
<body style="background:#000;color:#fff;font-family:system-ui,sans-serif;padding:2rem">
<p>Diese Seite ist umgezogen: <a style="color:#fff" href="{url}">{html.escape(label)}</a></p>
<script>location.replace({json.dumps(url)} + location.hash);</script>
</body></html>
""")


def render_feed(weeks, lang):
    tt = T[lang]
    items = []
    for w in reversed(weeks[-30:]):
        link = url_for(w["page"])
        pub = dt.datetime.combine(dt.date.fromisoformat(w["datum"]), dt.time(6, 0), dt.timezone.utc)
        tools = "".join(f"<li><strong>{html.escape(CAT_LABEL[lang][t['kategorie']])}: {html.escape(t['name'])}</strong> ({score(t.get('bewertung'), lang)}/10). {html.escape(t.get('kurzbeschreibung', ''))}</li>" for t in w["tools"])
        desc = f"<p>{html.escape(w.get('zusammenfassung', ''))}</p><ul>{tools}</ul>"
        items.append(f"""  <item>
    <title>{tt['week']} {w['kw']:02d}/{w['jahr']}: {html.escape(', '.join(t['name'] for t in w['tools']))}</title>
    <link>{link}</link>
    <guid isPermaLink="true">{link}</guid>
    <pubDate>{pub.strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
    <description><![CDATA[{desc}]]></description>
  </item>""")
    feed = PATHS[lang]["feed"]
    write(feed, f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{tt['feed_title']}</title>
  <link>{url_for(PATHS[lang]['home'])}</link>
  <atom:link href="{url_for(feed)}" rel="self" type="application/rss+xml"/>
  <description>{html.escape(tt['footer_line'])}</description>
  <language>{tt['feed_lang']}</language>
{chr(10).join(items)}
</channel>
</rss>
""")


def render_sitemap(pages):
    body = "\n".join(f"  <url><loc>{url_for(p)}</loc></url>" for p in pages)
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
    shutil.rmtree(os.path.join(ROOT, "en"), ignore_errors=True)


def main():
    weeks = load_weeks()
    de_weeks, en_weeks = weeks["de"], weeks["en"]
    if not de_weeks:
        sys.exit("Keine Wochen in data/weeks gefunden.")
    clean_generated()
    en_by_date = {w["datum"]: w for w in en_weeks}
    de_by_date = {w["datum"]: w for w in de_weeks}
    sitemap = []

    # Deutsch
    for i, w in enumerate(de_weeks):
        if w["analysis_page"]:
            render_analysis(w)
            sitemap.append(w["analysis_page"])
        alt = {"de": w["page"], "en": en_by_date[w["datum"]]["page"] if w["datum"] in en_by_date else PATHS["en"]["archive"]}
        render_week(w, w["page"], False, de_weeks[i - 1] if i else None, de_weeks[i + 1] if i + 1 < len(de_weeks) else None, alt)
        sitemap.append(w["page"])
    # Englisch
    for i, w in enumerate(en_weeks):
        alt = {"de": de_by_date[w["datum"]]["page"], "en": w["page"]}
        render_week(w, w["page"], False, en_weeks[i - 1] if i else None, en_weeks[i + 1] if i + 1 < len(en_weeks) else None, alt)
        sitemap.append(w["page"])

    home_alt = {l: PATHS[l]["home"] for l in LANGS}
    render_week(de_weeks[-1], "index.html", True, de_weeks[-2] if len(de_weeks) > 1 else None, None, home_alt)
    if en_weeks:
        render_week(en_weeks[-1], "en/index.html", True, en_weeks[-2] if len(en_weeks) > 1 else None, None, home_alt)
    for l, ws in (("de", de_weeks), ("en", en_weeks)):
        alt = {x: PATHS[x]["archive"] for x in LANGS}
        render_archive(ws, l, alt)
        render_feed(ws, l)

    o = legal.OWNER
    for l in LANGS:
        tt = T[l]
        L = legal.TEXTS[l]
        render_page(l, "method", "method", tt["method_title"], tt["method_desc"], tt["method_heading"], L["method"],
                    {x: PATHS[x]["method"] for x in LANGS}, kicker=tt["method_kicker"], lead=tt["method_lead"])
        render_page(l, "imprint", "legal", tt["imprint_title"], tt["imprint"], tt["imprint"], L["imprint"].format(**o, country_l=o["country"][l]),
                    {x: PATHS[x]["imprint"] for x in LANGS}, kicker=tt["legal_kicker"])
        render_page(l, "privacy", "legal", tt["privacy_title"], tt["privacy"], tt["privacy"], L["privacy"].format(**o, country_l=o["country"][l]),
                    {x: PATHS[x]["privacy"] for x in LANGS}, kicker=tt["legal_kicker"])
        sitemap += [PATHS[l][k] for k in ("home", "archive", "method", "imprint", "privacy")]
    render_page("de", None, "none", "Seite nicht gefunden | KI-Tool-Analysen", "Diese Seite gibt es nicht.",
                "Seite nicht gefunden", legal.NOT_FOUND, {x: PATHS[x]["home"] for x in LANGS}, kicker="404", noindex=True, rel="404.html")

    sitemap += render_topic("transkription")

    by_date = {w["datum"]: w for w in de_weeks}
    redirects = json.load(open(os.path.join(ROOT, "data/legacy-redirects.json"), encoding="utf-8"))
    for old, datum in redirects.items():
        w = by_date.get(datum)
        if w:
            render_redirect(old, w["page"], f"KW {w['kw']:02d}/{w['jahr']}")

    render_sitemap(sitemap)
    render_compat_index(de_weeks)
    write("CNAME", SITE_URL.split("://")[1] + "\n")
    open(os.path.join(ROOT, ".nojekyll"), "a").close()
    latest = de_weeks[-1]
    print(f"Gebaut: {len(de_weeks)} Wochen DE, {len(en_weeks)} Wochen EN, aktuell KW {latest['kw']:02d}/{latest['jahr']} ({latest['datum']}).")


if __name__ == "__main__":
    main()
