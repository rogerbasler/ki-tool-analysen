"""Prüft eine Wochendatei vor dem Build.

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
