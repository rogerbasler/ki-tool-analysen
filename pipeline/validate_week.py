"""Prüft eine Wochendatei (DE) und ihre englische Fassung (data/weeks/en/) vor dem Build.

Aufruf: python3 pipeline/validate_week.py data/weeks/YYYY-MM-DD.json
Exit-Code 0 = in Ordnung, 1 = Fehler. Warnungen brechen nicht ab.
"""
import datetime as dt
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = ["Text", "Design", "Data / Wissen", "Recherche", "Agents"]

# Stilregeln (Schweizer Orthografie, keine Floskeln, keine Inline-Quellen)
FORBIDDEN = [
    (r"ß", "ß statt ss"),
    (r"[—–]", "Gedankenstrich (— oder –); Komma, Doppelpunkt oder 'bis' verwenden"),
    (r"[„“”«»‚‘’]", "typografische Anführungszeichen; gerade \" verwenden"),
    (r"\[\d+\]", "Inline-Quellenverweis wie [1]; Quellen nur in 'quellen'"),
    (r"(?i)\blaut\s+[A-ZÄÖÜa-zäöü]", "Inline-Quellenangabe 'laut ...'; Aussage direkt formulieren, Quelle in 'quellen'"),
    (r"(?i)das eigentliche problem", "Floskel 'Das eigentliche Problem'"),
    (r"(?i)was oft unterschätzt wird", "Floskel 'Was oft unterschätzt wird'"),
    (r"(?i)der entscheidende unterschied", "Floskel 'Der entscheidende Unterschied'"),
    (r"(?i)hier zeigt sich", "Floskel 'hier zeigt sich'"),
    (r"(?i)dieses muster", "Floskel 'dieses Muster'"),
    (r"(?i)am wenigsten sichtbare", "Floskel 'am wenigsten sichtbare ...'"),
    (r"(?i)game[- ]?changer", "Buzzword 'Game Changer'"),
    (r"(?i)revolution", "Buzzword 'revolutionär'"),
    (r"(?i)bahnbrechend", "Buzzword 'bahnbrechend'"),
    (r"(?i)disruptiv", "Buzzword 'disruptiv'"),
    (r"(?i)\bnicht nur\b.{0,80}\bsondern\b", "Konstruktion 'nicht nur ..., sondern'"),
]


FORBIDDEN_EN = [
    (r"[\u2014\u2013]", "dash (— or –); use a comma, colon or 'to'"),
    (r"[„“”«»‚‘’]", "typographic quotes; use straight quotes"),
    (r"\[\d+\]", "inline citation such as [1]; sources only in 'quellen'"),
    (r"(?i)\baccording to\b", "inline attribution 'according to'; state it directly, source in 'quellen'"),
    (r"(?i)game[- ]?changer", "buzzword 'game changer'"),
    (r"(?i)revolution", "buzzword 'revolutionary'"),
    (r"(?i)groundbreaking", "buzzword 'groundbreaking'"),
    (r"(?i)disruptive", "buzzword 'disruptive'"),
    (r"(?i)the real problem (is|isn)", "phrase 'the real problem is'"),
    (r"(?i)often underestimated", "phrase 'often underestimated'"),
    (r"(?i)\bnot (just|only)\b.{0,80}\bbut\b", "construction 'not only ..., but'"),
    (r"[äöüÄÖÜß]", "German characters in the English text"),
]
EN_TOOL_FIELDS = ["kurzbeschreibung", "signal", "beschreibung", "nutzungsszenarien", "pricing", "datenschutz",
                  "staerken", "schwaechen", "einschaetzung"]


def validate_en(de, path, E, W):
    en_path = os.path.join(os.path.dirname(path), "en", os.path.basename(path))
    if not os.path.exists(en_path):
        E(f"Englische Fassung fehlt: {en_path}")
        return
    en = json.load(open(en_path, encoding="utf-8"))
    if en.get("umfang", "voll") != "voll":
        E("EN: neue Wochen brauchen eine vollständige Übersetzung (umfang: voll)")
    for k in ("zusammenfassung", "highlights", "trend"):
        if not en.get(k):
            E(f"EN: Feld fehlt: {k}")
    n = len(sentences(en.get("zusammenfassung", "")))
    if not 3 <= n <= 5:
        E(f"EN: summary has {n} sentences, 3 to 5 required")
    names = [t.get("name") for t in en.get("tools", [])]
    for t in de.get("tools", []):
        if t.get("name") not in names:
            E(f"EN: Tool {t.get('name')!r} fehlt (Name muss identisch zur DE-Fassung sein)")
    for t in en.get("tools", []):
        for k in EN_TOOL_FIELDS:
            if not t.get(k):
                E(f"EN {t.get('name')}: Feld fehlt: {k}")
        de_t = next((x for x in de.get("tools", []) if x.get("name") == t.get("name")), {})
        for k in ("nutzungsszenarien", "staerken", "schwaechen"):
            if len(t.get(k) or []) != len(de_t.get(k) or []):
                W(f"EN {t.get('name')}: {k} hat eine andere Anzahl Einträge als DE")
    for p, txt in texts(en, "en"):
        if p.endswith(".name"):
            continue
        for pat, msg in FORBIDDEN_EN:
            m = re.search(pat, txt)
            if m:
                E(f"{p}: {msg} -> \"...{txt[max(0, m.start() - 30):m.end() + 30]}...\"")


def texts(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            yield from texts(x, f"{path}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("url", "quellen", "datum", "markdown"):
                continue
            yield from texts(v, f"{path}.{k}" if path else k)


def sentences(s):
    return [x for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9\"])", s.strip()) if x]


def main(path):
    errors, warnings = [], []
    w = json.load(open(path, encoding="utf-8"))
    E, W = errors.append, warnings.append

    for k in ("kw", "jahr", "datum", "zusammenfassung", "highlights", "trend", "tools"):
        if k not in w or w[k] in ("", None, []):
            E(f"Feld fehlt: {k}")
    try:
        d = dt.date.fromisoformat(w["datum"])
        iso = d.isocalendar()
        if w.get("kw") != iso[1] or w.get("jahr") != iso[0]:
            E(f"KW/Jahr passen nicht zum Datum {w['datum']} (ISO: KW {iso[1]}/{iso[0]})")
        if os.path.basename(path) != f"{w['datum']}.json":
            E("Dateiname muss <datum>.json sein")
    except Exception as e:  # noqa: BLE001
        E(f"Datum ungültig: {e}")

    n = len(sentences(w.get("zusammenfassung", "")))
    if not 3 <= n <= 5:
        E(f"Zusammenfassung hat {n} Sätze, verlangt sind 3 bis 5")

    tools = w.get("tools", [])
    if len(tools) != 5:
        E(f"{len(tools)} Tools statt 5")
    cats = [t.get("kategorie") for t in tools]
    if sorted(cats, key=lambda c: CATEGORIES.index(c) if c in CATEGORIES else 9) != CATEGORIES:
        E(f"Kategorien müssen genau einmal vorkommen: {cats}")

    for t in tools:
        name = t.get("name", "?")
        for k in ("name", "url", "bewertung", "signal", "kurzbeschreibung", "beschreibung", "nutzungsszenarien",
                  "pricing", "datenschutz", "staerken", "schwaechen", "einschaetzung", "quellen"):
            if not t.get(k) and t.get(k) != 0:
                E(f"{name}: Feld fehlt: {k}")
        if t.get("url") and not str(t["url"]).startswith("https://"):
            E(f"{name}: url muss mit https:// beginnen")
        b = t.get("bewertung")
        if not isinstance(b, (int, float)) or not 1 <= b <= 10:
            E(f"{name}: bewertung muss eine Zahl von 1 bis 10 sein")
        ns = t.get("nutzungsszenarien") or []
        if not 3 <= len(ns) <= 5:
            E(f"{name}: {len(ns)} Nutzungsszenarien, verlangt sind 3 bis 5")
        for k in ("staerken", "schwaechen"):
            if len(t.get(k) or []) < 2:
                E(f"{name}: mindestens 2 Einträge in {k}")
        q = t.get("quellen") or []
        if len(q) < 2:
            E(f"{name}: mindestens 2 Quellen (APA 7) angeben")
        for s in q:
            if not re.search(r"https?://", s) or not re.search(r"\(\d{4}|\(o\. ?D\.\)|\(n\.d\.\)", s):
                W(f"{name}: Quelle sieht nicht nach APA 7 mit URL aus: {s[:90]}")
        if t.get("pricing") and not re.search(r"(?i)\b(CHF|USD|EUR|\$|kostenlos|free|gratis|open source)", t["pricing"]):
            W(f"{name}: Pricing nennt weder Währung noch Free Tier")
        if t.get("datenschutz") and not re.search(r"(?i)(DSGVO|GDPR|DSG)", t["datenschutz"]):
            E(f"{name}: Datenschutz muss DSGVO/DSG einordnen")
        if t.get("datenschutz") and not re.search(r"(?i)(self-host|selbst hosten|on-prem|lokal|eigene[nr]? (server|infrastruktur))", t["datenschutz"]):
            W(f"{name}: Datenschutz sagt nichts zu Self-Hosting")

    for p, s in texts(w):
        for pat, msg in FORBIDDEN:
            m = re.search(pat, s)
            if m:
                E(f"{p}: {msg} -> \"...{s[max(0, m.start() - 30):m.end() + 30]}...\"")

    # Wöchentliche Variation: kein Tool aus den letzten 6 Ausgaben erneut (ausser klar benanntes Update)
    others = sorted(f for f in glob.glob(os.path.join(ROOT, "data/weeks/*.json")) if os.path.basename(f) < os.path.basename(path))[-6:]
    recent = {}
    for f in others:
        for t in json.load(open(f, encoding="utf-8"))["tools"]:
            recent[re.sub(r"[^a-z0-9]", "", t["name"].lower())] = os.path.basename(f)[:-5]
    for t in tools:
        k = re.sub(r"[^a-z0-9]", "", t.get("name", "").lower())
        if k in recent:
            E(f"{t['name']} war bereits am {recent[k]} dabei; anderes Tool wählen")
        elif any(k[:6] and r.startswith(k[:6]) for r in recent):
            W(f"{t['name']}: ähnlicher Name in den letzten Wochen; nur zulässig, wenn es ein signifikantes Update ist (im Feld 'signal' benennen)")

    validate_en(w, path, E, W)

    for x in warnings:
        print("WARNUNG:", x)
    for x in errors:
        print("FEHLER:", x)
    print("OK" if not errors else f"{len(errors)} Fehler")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
