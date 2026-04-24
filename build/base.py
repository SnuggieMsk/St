"""Shared CSS, fonts, header/footer, and HTML table helpers for Tier-1 dossiers.

Follows the `jhaver-dossier.html` idiom (PR #1):
- Literata (headings) / DM Sans (body) / JetBrains Mono (numbers)
- IBank cipher for ICICI Bank proper-noun; ICICI Securities / Prudential / Lombard allowed
- Self-contained HTML (CSS embedded), portable for email / Drive
- Evidence tags [n] anchored to Section 15 sources
"""
from __future__ import annotations
from html import escape

CSS = r"""
:root{
  --bg:#f7f5f0;--paper:#ffffff;--ink:#1a1a1a;--muted:#5a5a5a;--line:#e3dfd6;
  --accent:#7a1f2b;--accent-soft:#f5e6e8;--pos:#2e7d4f;--neg:#b42318;
  --amber:#b86a00;--cool:#1c4e80;--indigo:#3730a3;
  --mono:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;
  --sans:'DM Sans',-apple-system,Segoe UI,Roboto,sans-serif;
  --serif:'Literata','Iowan Old Style','Source Serif Pro',Georgia,serif;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:var(--sans);background:var(--bg);color:var(--ink);line-height:1.55;font-size:15px}
.wrap{max-width:1180px;margin:0 auto;padding:40px 48px 80px}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;letter-spacing:-0.01em;color:var(--ink);margin:0 0 .4em}
h1{font-size:2.6rem;line-height:1.15}
h2{font-size:1.85rem;line-height:1.2;border-bottom:2px solid var(--ink);padding-bottom:.35em;margin-top:2.2em}
h3{font-size:1.3rem;margin-top:1.6em;color:var(--accent)}
h4{font-size:1.05rem;margin-top:1.2em}
p{margin:.6em 0}
a{color:var(--accent);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
code,.mono{font-family:var(--mono);font-size:.92em}
.num{font-family:var(--mono);font-variant-numeric:tabular-nums}
.lede{font-size:1.12rem;color:var(--muted);max-width:72ch;margin:0 0 1.2em}
.subhead{font-family:var(--mono);text-transform:uppercase;letter-spacing:.12em;font-size:.8rem;color:var(--muted);margin:0 0 .4em}
.card{background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:22px 26px;margin:14px 0;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.card.accent{border-left:4px solid var(--accent);background:var(--accent-soft)}
.card.warn{border-left:4px solid var(--amber);background:#fbf2e3}
.card.pos{border-left:4px solid var(--pos);background:#e8f2ec}
.card.neg{border-left:4px solid var(--neg);background:#fbe8e6}
.grid{display:grid;gap:14px;margin:14px 0}
.grid.c2{grid-template-columns:repeat(2,1fr)}
.grid.c3{grid-template-columns:repeat(3,1fr)}
.grid.c4{grid-template-columns:repeat(4,1fr)}
@media (max-width:780px){.grid.c2,.grid.c3,.grid.c4{grid-template-columns:1fr}}
.kpi{background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:14px 16px}
.kpi .k{font-family:var(--mono);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.kpi .v{font-family:var(--serif);font-size:1.65rem;line-height:1.1;margin-top:4px}
.kpi .sub{font-size:.82rem;color:var(--muted);margin-top:3px}
.kpi.pos .v{color:var(--pos)} .kpi.neg .v{color:var(--neg)} .kpi.accent .v{color:var(--accent)}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:.92rem;background:var(--paper)}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--mono);font-size:.74rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);background:#faf7f1;font-weight:600}
td.num,th.num{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums}
tr:hover td{background:#fdfbf5}
.tag{display:inline-block;font-family:var(--mono);font-size:.7rem;letter-spacing:.05em;padding:2px 7px;border-radius:3px;background:var(--line);color:var(--ink);margin-right:4px;text-transform:uppercase}
.tag.pos{background:var(--pos);color:#fff}
.tag.neg{background:var(--neg);color:#fff}
.tag.amber{background:var(--amber);color:#fff}
.tag.cool{background:var(--cool);color:#fff}
.tag.indigo{background:var(--indigo);color:#fff}
.tag.accent{background:var(--accent);color:#fff}
sup.ref{font-family:var(--mono);font-size:.7rem;color:var(--accent);text-decoration:none;padding-left:2px}
sup.ref a{color:var(--accent);text-decoration:none}
.hero{border-top:6px solid var(--accent);padding-top:28px}
.hero .eyebrow{font-family:var(--mono);font-size:.8rem;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);font-weight:600}
.hero h1{font-size:3.1rem;margin:.15em 0 .3em}
.hero .meta{display:flex;gap:28px;flex-wrap:wrap;margin-top:14px;color:var(--muted);font-size:.92rem}
.hero .meta span{font-family:var(--mono);font-size:.82rem}
.nav{position:sticky;top:0;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:28px;z-index:10;font-size:.8rem}
.nav ol{list-style:none;margin:0;padding:0;display:flex;gap:14px;flex-wrap:wrap;font-family:var(--mono);text-transform:uppercase;letter-spacing:.05em}
.nav ol li a{color:var(--muted);text-decoration:none}
.nav ol li a:hover{color:var(--accent)}
ul.check{list-style:none;padding-left:0}
ul.check li{padding:4px 0 4px 22px;position:relative}
ul.check li::before{content:"✓";position:absolute;left:0;color:var(--pos);font-weight:700}
ul.x{list-style:none;padding-left:0}
ul.x li{padding:4px 0 4px 22px;position:relative}
ul.x li::before{content:"✗";position:absolute;left:0;color:var(--neg);font-weight:700}
.src-list{font-size:.85rem;columns:1;column-gap:32px}
.src-list ol{padding-left:24px;margin:0}
.src-list li{padding:4px 0;break-inside:avoid}
.src-list .u{font-family:var(--mono);font-size:.78rem;color:var(--cool);word-break:break-all}
.waterfall{font-family:var(--mono);font-size:.82rem;white-space:pre}
footer.foot{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);font-size:.82rem;text-align:center}
.pestel-cell{font-size:.82rem}
.pestel-cell .tt{font-weight:600;display:block;margin-bottom:2px}
.playbook .phase{font-family:var(--mono);text-transform:uppercase;letter-spacing:.08em;background:var(--ink);color:#fff;padding:3px 8px;border-radius:3px;font-size:.72rem;margin-right:6px}
"""

NAV_TEMPLATE = """\
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li>
<li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li>
{entity_nav}
<li><a href="#pestel">{sec_pestel} PESTEL</a></li>
<li><a href="#industry">{sec_industry} Industry</a></li>
<li><a href="#models">{sec_models} Models</a></li>
<li><a href="#consolidated">{sec_cons} Consolidated</a></li>
<li><a href="#retail">{sec_retail} Retail/PB/TASC</a></li>
<li><a href="#playbook">{sec_play} Playbook</a></li>
<li><a href="#sources">{sec_src} Sources</a></li>
</ol></nav>
"""

HEAD = lambda title: f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;0,7..72,700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body><div class="wrap">
"""

FOOT = lambda verify: f"""
<footer class="foot">
  <div class="mono">Dossier prepared 24 April 2026 &middot; macro block sourced same day &middot; registry cut-off per Probe42 metadata timestamps embedded in Section 04.</div>
  <div class="mono" style="margin-top:6px">{escape(verify)}</div>
</footer>
</div></body></html>"""

# --------- Helpers ---------

def ref(ids):
    """Render an evidence superscript. `ids` is e.g. "1" or "1,3-5"."""
    return f'<sup class="ref">[<a href="#src-{ids.split(",")[0].split("-")[0]}">{ids}</a>]</sup>'

def kpi(label, value, sub="", cls=""):
    c = f" {cls}" if cls else ""
    sub_h = f'<div class="sub">{escape(sub)}</div>' if sub else ""
    return f'<div class="kpi{c}"><div class="k">{escape(label)}</div><div class="v">{value}</div>{sub_h}</div>'

def card(title, body, cls=""):
    c = f" {cls}" if cls else ""
    t = f'<h4 style="margin-top:0">{escape(title)}</h4>' if title else ""
    return f'<div class="card{c}">{t}{body}</div>'

def table(headers, rows, classes=None):
    """rows is a list of lists; classes is an optional parallel list of cell classes."""
    hh = "".join(f"<th{(' class=num' if h.startswith('#') else '')}>{escape(h.lstrip('#'))}</th>" for h in headers)
    out = [f"<table><thead><tr>{hh}</tr></thead><tbody>"]
    for i, row in enumerate(rows):
        cells = []
        for j, cell in enumerate(row):
            cls = (classes[i][j] if classes else "") or ""
            is_num = headers[j].startswith("#")
            klass = f'class="{"num " + cls if is_num else cls}".strip()' if (is_num or cls) else ""
            cls_attr = f' class="{"num " + cls if is_num else cls}".strip()' if is_num or cls else ""
            # simpler: if num column, always num class
            if is_num and cls:
                cls_attr = f' class="num {cls}"'
            elif is_num:
                cls_attr = ' class="num"'
            elif cls:
                cls_attr = f' class="{cls}"'
            else:
                cls_attr = ""
            cells.append(f"<td{cls_attr}>{cell}</td>")
        out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)

def inr_cr(x, decimals=0):
    if x is None or x == "":
        return "—"
    try:
        v = float(x)
    except ValueError:
        return escape(str(x))
    if decimals == 0:
        return f"{v:,.0f}"
    return f"{v:,.{decimals}f}"
