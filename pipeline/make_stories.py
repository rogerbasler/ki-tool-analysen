#!/usr/bin/env python3
"""Erzeugt drei Instagram-Stories (1080 x 1920, PNG) aus einer Wochendatei.

Aufruf: python3 pipeline/make_stories.py data/weeks/YYYY-MM-DD.json [Ausgabeordner]
Standard-Ausgabe: /home/claude/stories/YYYY-MM-DD/ (ausserhalb des Repos, wird nicht committet).

Story 1: Titel mit KW, Zeitraum und Trend der Woche.
Story 2: Übersicht der sechs Tools mit Kategorie und Bewertung.
Story 3: Praxisregel der Woche und Link auf tools.fragroger.ai.
Texte oben und unten halten 250 px Abstand (Instagram-Bedienelemente).
"""
import html
import json
import os
import sys
import zipfile

from playwright.sync_api import sync_playwright

W, H = 1080, 1920

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,800;9..40,900&display=block');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1080px; height: 1920px; }
body {
  font-family: 'DM Sans', 'Avenir Next', 'Nunito', 'Inter', system-ui, sans-serif;
  color: #e8ecf3; background: #000;
  background-image:
    radial-gradient(900px 700px at 90% 0%, rgba(74,127,161,0.38), transparent 62%),
    radial-gradient(800px 600px at 0% 100%, rgba(255,20,144,0.20), transparent 60%);
  position: relative; overflow: hidden;
}
.safe { position: absolute; left: 80px; right: 80px; top: 260px; bottom: 260px; display: flex; flex-direction: column; }
.brand { font-weight: 900; font-size: 44px; letter-spacing: -0.02em; color: #fff; }
.brand .h { color: #ff1490; }
.brand .b { color: #4a7fa1; }
.kicker { margin-top: 18px; color: #4a7fa1; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; font-size: 30px; }
.big { font-weight: 900; line-height: 0.95; letter-spacing: -0.035em; color: #fff; }
.pink { color: #ff1490; }
.muted { color: #9aa7bd; }
.bar { width: 120px; height: 10px; background: #ff1490; border-radius: 6px; }
.footer { margin-top: auto; font-size: 30px; font-weight: 700; color: #9aa7bd; }
.footer b { color: #fff; }
.row { display: flex; align-items: center; gap: 28px; padding: 18px 0; border-bottom: 2px solid rgba(255,255,255,0.10); }
.row:last-child { border-bottom: 0; }
.cat { font-size: 24px; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: #4a7fa1; }
.name { font-size: 44px; font-weight: 800; color: #fff; line-height: 1.08; letter-spacing: -0.015em; }
.score { margin-left: auto; flex: none; width: 118px; height: 118px; border-radius: 50%;
  border: 6px solid #ff1490; display: flex; align-items: center; justify-content: center;
  font-size: 44px; font-weight: 900; color: #fff; }
.score.top { background: #ff1490; color: #000; }
.cta { margin-top: 48px; display: inline-block; background: #ff1490; color: #000; font-weight: 900;
  font-size: 46px; padding: 26px 40px; border-radius: 999px; letter-spacing: -0.01em; }
.sticker { margin-top: 40px; border: 4px dashed rgba(255,255,255,0.35); border-radius: 28px; height: 200px;
  display: flex; align-items: center; justify-content: center; font-size: 28px; color: #9aa7bd; font-weight: 700; }
"""

T = {
    "de": {
        "sub": "KI-Tool-Analysen",
        "kw": "KW {kw} · {zeitraum}",
        "intro": "Eingeordnet für Unternehmer:innen und Entscheider:innen",
        "trend": "Trend der Woche",
        "overview": "Die sechs Tools der Woche",
        "rule": "Praxisregel",
        "more": "Pricing, Datenschutz und Einschätzung zu jedem Tool:",
        "sticker": "Platz für den Link-Sticker",
        "swipe": "Weiter tippen",
        "dec": ",",
    },
}


def esc(s):
    return html.escape(s or "", quote=False)


def fmt_score(v, dec):
    return f"{float(v):.1f}".replace(".", dec)


def fit(text, small, mid, large, n1, n2):
    n = len(text)
    return large if n <= n1 else mid if n <= n2 else small


def page(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def brand(t):
    return (f"<div class='brand'><span class='h'>#</span>frag<span class='b'>Roger</span></div>"
            f"<div class='kicker'>{t['sub']}</div>")


def story_title(w, t):
    trend = w.get("trend", "")
    size = fit(trend, 50, 58, 66, 110, 160)
    return page(f"""
<div class='safe'>
  {brand(t)}
  <div style='margin-top:90px' class='kicker'>{esc(t['kw'].format(kw=w['kw'], zeitraum=w['zeitraum']))}</div>
  <div class='big' style='font-size:118px;margin-top:28px'>6 Tools.<br><span class='pink'>1 Muster.</span></div>
  <div style='margin-top:40px;font-size:38px;line-height:1.3;font-weight:600' class='muted'>{esc(t['intro'])}</div>
  <div style='margin-top:90px' class='bar'></div>
  <div class='kicker' style='margin-top:30px'>{t['trend']}</div>
  <div style='margin-top:20px;font-size:{size}px;line-height:1.18;font-weight:800;color:#fff;letter-spacing:-0.015em'>{esc(trend)}</div>
  <div class='footer'>{t['swipe']} →</div>
</div>""")


def story_overview(w, t):
    best = max(x["bewertung"] for x in w["tools"])
    rows = []
    for x in w["tools"]:
        name = x["name"]
        size = 44 if len(name) <= 26 else 38 if len(name) <= 34 else 33
        top = " top" if x["bewertung"] == best else ""
        rows.append(f"""<div class='row'><div><div class='cat'>{esc(x['kategorie'])}</div>
<div class='name' style='font-size:{size}px'>{esc(name)}</div></div>
<div class='score{top}'>{fmt_score(x['bewertung'], t['dec'])}</div></div>""")
    return page(f"""
<div class='safe'>
  {brand(t)}
  <div class='big' style='font-size:76px;margin-top:50px'>{esc(t['overview'])}</div>
  <div class='kicker' style='margin-top:14px'>{esc(t['kw'].format(kw=w['kw'], zeitraum=w['zeitraum']))}</div>
  <div style='margin-top:24px'>{''.join(rows)}</div>
</div>""")


def story_rule(w, t):
    rule = next((h for h in w.get("highlights", []) if h.lower().startswith("praxisregel")), "")
    rule = rule.split(":", 1)[1].strip() if ":" in rule else rule
    size = fit(rule, 48, 56, 64, 140, 200)
    return page(f"""
<div class='safe'>
  {brand(t)}
  <div style='margin-top:110px' class='bar'></div>
  <div class='kicker' style='margin-top:30px'>{t['rule']}</div>
  <div style='margin-top:24px;font-size:{size}px;line-height:1.2;font-weight:800;color:#fff;letter-spacing:-0.015em'>{esc(rule)}</div>
  <div style='margin-top:80px;font-size:36px;line-height:1.3;font-weight:600' class='muted'>{t['more']}</div>
  <div><span class='cta'>tools.fragroger.ai</span></div>
  <div class='sticker'>{t['sticker']}</div>
</div>""")


def main(path, out=None):
    w = json.load(open(path, encoding="utf-8"))
    t = T["de"]
    out = out or os.path.join("/home/claude/stories", w["datum"])
    os.makedirs(out, exist_ok=True)
    pages = [("1_titel", story_title(w, t)), ("2_tools", story_overview(w, t)), ("3_praxisregel", story_rule(w, t))]
    files = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for name, content in pages:
            pg.set_content(content, wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            # Kein Inhalt darf in die unteren 250 px laufen.
            overflow = pg.evaluate("(() => { const s = document.querySelector('.safe'); return s.scrollHeight > s.clientHeight + 2; })()")
            if overflow:
                print(f"WARNUNG: {name} läuft über den sicheren Bereich hinaus")
            f = os.path.join(out, f"fragroger-tools-kw{w['kw']:02d}-{w['datum']}_{name}.png")
            pg.screenshot(path=f, full_page=False)
            files.append(f)
        b.close()
    z = os.path.join(out, f"fragroger-tools-kw{w['kw']:02d}-{w['datum']}_stories.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, os.path.basename(f))
    for f in files + [z]:
        print(f)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
