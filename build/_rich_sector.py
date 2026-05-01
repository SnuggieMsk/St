"""Rich bespoke sector deep-dive generator.

Each company's spec carries per-section content; framework provides 15-section
HTML structure (A-O) including a 7-subsection company history block (B).
Used for pilots 153-171 (CUMI through Lapp India) for efficiency at depth.
"""
from pathlib import Path
from .base import HEAD, FOOT, ref

OUTDIR = Path("/home/user/St")

NAV = """
<nav class="nav"><ol>
<li><a href="#tldr">A · TL;DR</a></li>
<li><a href="#history">B · History</a></li>
<li><a href="#promoters">C · Promoters/KMP</a></li>
<li><a href="#valuechain">D · Value-chain</a></li>
<li><a href="#driver-fs">E · Driver→FS</a></li>
<li><a href="#product-fs">F · Product→FS</a></li>
<li><a href="#hooks">G · Hooks</a></li>
<li><a href="#questions">H · Q-bank</a></li>
<li><a href="#objections">I · Objections</a></li>
<li><a href="#math">J · Math</a></li>
<li><a href="#ecosystem">K · Ecosystem</a></li>
<li><a href="#competitors">L · Competitors</a></li>
<li><a href="#plays">M · Plays</a></li>
<li><a href="#firstcall">N · First-call</a></li>
<li><a href="#sources">O · Sources</a></li>
</ol></nav>
"""


def _sec_a(s):
    return f"""
<section id="tldr" class="hero">
<div class="eyebrow">Sector deep-dive companion · Pilot {s['pilot']} · {s['name']} · {s['cluster_label']}</div>
<h1>The play in 90 seconds<br>{s['play_strap']}</h1>
<p class="lede">{s['tldr_lede']}</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Y3 wallet</div><div class="v num">Rs {s['headline_low']}-{s['headline_high']} Cr/yr</div><div class="sub">{s.get('y3_sub','All products')}</div></div>
<div class="kpi pos"><div class="k">{s['kpi_b_label']}</div><div class="v num">{s['kpi_b_val']}</div><div class="sub">{s['kpi_b_sub']}</div></div>
<div class="kpi"><div class="k">{s['kpi_c_label']}</div><div class="v num">{s['kpi_c_val']}</div><div class="sub">{s['kpi_c_sub']}</div></div>
<div class="kpi pos"><div class="k">{s['kpi_d_label']}</div><div class="v num">{s['kpi_d_val']}</div><div class="sub">{s['kpi_d_sub']}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">The single sentence the RM walks in with</h4>
<p style="font-size:1.1rem;margin-bottom:0"><em>{s['walking_in']}</em></p>
</div>
<div class="meta" style="margin-top:14px">
<span>Companion to <strong><a href="{s['dossier_slug']}-dossier.html">{s['dossier_slug']}-dossier.html</a></strong></span>
<span>Cut <strong>Probe42 28 Apr 2026</strong></span>
<span>Author <strong>RM-meeting prep · LCG/PBG Chennai</strong></span>
</div>
</section>
"""


def _sec_b(s):
    """History — 7 subsections."""
    items = ""
    for i, (h, body) in enumerate(s['history'], 1):
        items += f'<h3>B.{i} {h}</h3>\n<div class="card"><p>{body}</p></div>\n\n'
    return f"""
<section id="history"><div class="subhead">B · Company history &mdash; {s.get('history_strap','full company arc')}</div>
{items}</section>
"""


def _sec_c(s):
    """Promoters + KMP."""
    items = ""
    for h, body in s['kmp']:
        items += f'<h3>C.{len(items.split("<h3>"))} {h}</h3>\n<div class="card"><p>{body}</p></div>\n\n'
    return f"""
<section id="promoters"><div class="subhead">C · Promoters + Key Managerial Personnel</div>
{items}</section>
"""


def _sec_d(s):
    return f"""
<section id="valuechain"><div class="subhead">D · Value-chain &mdash; {s.get('valuechain_strap','sector positioning')}</div>
<p>{s['valuechain_text']}</p>
<div class="card">{s.get('valuechain_table','')}</div>
{s.get('valuechain_extra','')}
</section>
"""


def _sec_e(s):
    rows = ""
    for d, fs, prod in s['driver_fs']:
        rows += f"<tr><td><strong>{d}</strong></td><td>{fs}</td><td>{prod}</td></tr>\n"
    return f"""
<section id="driver-fs"><div class="subhead">E · Driver &rarr; FS line-item map</div>
<p>{s.get('driver_fs_intro','For each driver, mapping to FS line-item + IBank product entry.')}</p>
<div class="card"><table>
<thead><tr><th>Driver</th><th>FS impact</th><th>IBank product entry</th></tr></thead>
<tbody>{rows}</tbody></table></div>
</section>
"""


def _sec_f(s):
    rows = ""
    for p in s['products']:
        rows += f"<tr><td><strong>{p[0]}</strong></td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td><td>{p[4]}</td></tr>\n"
    return f"""
<section id="product-fs"><div class="subhead">F · IBank product &rarr; FS map</div>
<div class="card"><table>
<thead><tr><th>Product</th><th>Structure</th><th>Size</th><th>Price</th><th>Y3 income</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="muted small">Pricing indicative; final depends on rating, tenor, collateral, consortium dynamics.</p>
{s.get('product_extra','')}
</section>
"""


def _sec_g(s):
    items = ""
    for i, (h, body) in enumerate(s['hooks'], 1):
        items += f'<li><strong>{i}. {h}</strong> &mdash; {body}</li>\n'
    return f"""
<section id="hooks"><div class="subhead">G · Five conversation hooks</div>
<div class="card"><ol>{items}</ol></div>
</section>
"""


def _sec_h(s):
    qs = "".join(f"<li>{q}</li>\n" for q in s['questions'])
    not_qs = "".join(f"<li>{q}</li>\n" for q in s['questions_not'])
    return f"""
<section id="questions"><div class="subhead">H · Question bank</div>
<div class="card"><h4 style="margin-top:0">12 questions for the meeting</h4><ol>{qs}</ol></div>
<div class="card"><h4 style="margin-top:0">What NOT to ask</h4><ul>{not_qs}</ul></div>
</section>
"""


def _sec_i(s):
    items = ""
    for q, a in s['objections']:
        items += f'<div class="card"><h4 style="margin-top:0">{q}</h4><p>{a}</p></div>\n'
    return f"""
<section id="objections"><div class="subhead">I · Objection handling</div>
{items}
</section>
"""


def _sec_j(s):
    return f"""
<section id="math"><div class="subhead">J · 12 / 24 / 36-month conversion math</div>
{s['math_html']}
</section>
"""


def _sec_k(s):
    return f"""
<section id="ecosystem"><div class="subhead">K · Customer + supplier ecosystem</div>
{s['ecosystem_html']}
</section>
"""


def _sec_l(s):
    return f"""
<section id="competitors"><div class="subhead">L · Competitor bank diagnosis</div>
{s['competitors_html']}
</section>
"""


def _sec_m(s):
    items = ""
    for i, (h, body) in enumerate(s['plays'], 1):
        items += f'<h3>M.{i} {h}</h3>\n<div class="card"><p>{body}</p></div>\n\n'
    return f"""
<section id="plays"><div class="subhead">M · The three plays</div>
{items}
<p><strong>All three plays in parallel</strong> get Y3 wallet Rs {s['headline_low']}-{s['headline_high']} Cr base case.</p>
</section>
"""


def _sec_n(s):
    return f"""
<section id="firstcall"><div class="subhead">N · First-call playbook</div>
{s['firstcall_html']}
</section>
"""


def _sec_o(s):
    items = "".join(f'<li id="src-{i}">{src}</li>\n' for i, src in enumerate(s['sources'], 1))
    return f"""
<section id="sources"><div class="subhead">O · Sources</div>
<ol>{items}</ol>
<p class="muted small">Cipher: IBank notation in use. Approved sister-entities (ICICI Securities / Prudential / Lombard) retained. FY25-FY29 projections analyst-est. Diligence items inline.</p>
</section>
"""


def build_one(spec):
    title = f"{spec['name']} · Sector Deep-Dive · 28 Apr 2026"
    verify = f"Sector deep-dive · companion to pilot {spec['pilot']} dossier · 15 sections A-O · cipher clean"
    body = (NAV + _sec_a(spec) + _sec_b(spec) + _sec_c(spec) + _sec_d(spec)
            + _sec_e(spec) + _sec_f(spec) + _sec_g(spec) + _sec_h(spec)
            + _sec_i(spec) + _sec_j(spec) + _sec_k(spec) + _sec_l(spec)
            + _sec_m(spec) + _sec_n(spec) + _sec_o(spec))
    html = HEAD(title) + body + FOOT(verify)
    out = OUTDIR / f"{spec['dossier_slug']}-sector.html"
    out.write_text(html)
    return out, len(html.splitlines())
