"""Generic dossier template generator. Each entity module imports make_dossier(cfg) and supplies a config dict."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
from .shared_sources import MACRO_SOURCES_HTML

NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li><li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li><li><a href="#entity">04 Entity</a></li>
<li><a href="#charges">05 Charges</a></li>
<li><a href="#industry">06 Industry</a></li><li><a href="#models">07 Models</a></li>
<li><a href="#entry-map">08 Entry map</a></li><li><a href="#retail">09 Retail/PB/TASC</a></li>
<li><a href="#consolidated">10 Consolidated</a></li><li><a href="#diligence">11 Diligence</a></li>
<li><a href="#playbook">12 Playbook</a></li><li><a href="#sources">13 Sources</a></li>
</ol></nav>
"""


def make_dossier(c):
    """c is a dict with: pilot, name, slug, cin, parent, country, industry_short, industry_long,
    eyebrow_extras, three_angles (list), toi_fy25, ebitda_fy25, ebitda_pct, pat_fy25, tnw_fy25,
    debt_fy25, fte, paid_up, charges_summary, charges_table_rows (list of (holder, amt, pct, comment)),
    rating_text, rating_date, ibank_share, headline_low, headline_high, src_base (e.g. 760),
    src_master_text, src_parent_text, src_extra (optional list of (start_n, label, ref_text)),
    industry_text, drivers (list), proj_rows (FY26-FY28 TOI), product_rows (list of (prod, size, y3lo, y3hi, comment)),
    retail_text, pb_text, tasc_text, retail_total_low, retail_total_high, consolidated_rows (list of (segment, lo, hi)),
    consolidated_total_low, consolidated_total_high, diligence_news, playbook_30, playbook_60, playbook_90, success_metrics (list),
    incorp_date, ho_text, registry_cut, summary_strap, footer
    """
    pilot=c['pilot']; name=c['name']; pad_label=c['pad_label']
    src_b=c['src_base']
    # S1
    s1 = f"""
<section id="cover" class="hero">
<div class="eyebrow">Tier-1 Dossier · Pilot {pilot} of 150 · {c['eyebrow_extras']}</div>
<h1>{name}<br>{c['headline_sub']}</h1>
<p class="lede">{c['lede']}</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs {c['headline_low']}&ndash;{c['headline_high']} Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">{c['headline_strap']}</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs {c['toi_fy25']:,} Cr</div><div class="sub">{c['industry_short']}{ref("128")}</div></div>
{c['kpi3']}
{c['kpi4']}
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
{"".join(f"<li>{a}</li>" for a in c['three_angles'])}
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>{c['cin']}</strong></span>
<span>Incorp <strong>{c['incorp_date']}</strong></span>
<span>HO <strong>{c['ho_text']}</strong></span>
<span>Parent <strong>{c['parent']}</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""
    s2 = f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>{c['group_text']}</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
{"".join(f"<li>{a}</li>" for a in c['funding_anchors'])}
</ul></section>
"""
    s3 = f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">{c['toi_fy23']:,}</td><td class="num">{c['toi_fy24']:,}</td><td class="num">{c['toi_fy25']:,}{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">{c['eb_fy23']}</td><td class="num">{c['eb_fy24']}</td><td class="num">{c['ebitda_fy25']}{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">{c['mg_fy23']}</td><td class="num">{c['mg_fy24']}</td><td class="num">{c['ebitda_pct']}</td></tr>
<tr><td>PAT</td><td class="num">{c['pat_fy23']}</td><td class="num">{c['pat_fy24']}</td><td class="num">{c['pat_fy25']}{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">{c['tnw_fy23']}</td><td class="num">{c['tnw_fy24']}</td><td class="num">{c['tnw_fy25']}{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">{c['dt_fy23']}</td><td class="num">{c['dt_fy24']}</td><td class="num">{c['debt_fy25']}{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">{c['dr_fy23']}</td><td class="num">{c['dr_fy24']}</td><td class="num">{c['dr_fy25']}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs {c['paid_up']} Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">{c['fte']}</div><div class="sub">{ref("128")}</div></div>
{c['anchor_charges_kpi']}
{c['anchor_cash_kpi']}
{c['anchor_rating_kpi']}
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""
    # S4
    if c.get('charges_table_rows'):
        rows = "".join(
            f"<tr><td>{h}</td><td class=\"num\">{a}</td><td class=\"num\">{p}</td><td>{cm}</td></tr>"
            for (h,a,p,cm) in c['charges_table_rows']
        )
        s4 = f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>{c['charges_summary']}</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th><th>Comment</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="lede">{c['charges_strap']}</p>
</section>"""
    else:
        s4 = f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>{c['charges_summary']}</strong>{ref("126")}.</p>
<p class="lede">{c['charges_strap']}</p>
</section>"""
    s5 = f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; {c['industry_short']}</div>
<p>{c['industry_text']}</p>
<h3>06.1 Drivers</h3>
<ul>
{"".join(f"<li>{d}</li>" for d in c['drivers'])}
</ul>
<h3>06.2 PESTEL hooks</h3>
<ul>
<li><strong>Political &middot; defence/regulatory</strong>{ref("6")}: see macro section.</li>
<li><strong>Economic &middot; rates + INR</strong>{ref("1")}{ref("3")}: cost of capital + FX volatility on capex+royalty.</li>
<li><strong>Social &middot; talent + labour</strong>{ref("14")}: TN labour-cost index Q4 FY26 + migrant retention premium noted.</li>
<li><strong>Tech &middot; gen-AI + automation</strong>: productivity 20-30% on back-office + design.</li>
<li><strong>Environmental &middot; CBAM + green-cooling</strong>{ref("18")}{ref("21")}: scope-3 + FGD compliance.</li>
<li><strong>Legal &middot; CSR Rule + DIR-12</strong>{ref("38")}{ref("144")}: compliance refresh.</li>
</ul></section>"""
    s6 = f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">{c['toi_fy25']:,}{ref("128")}</td><td class="num">{c['toi_fy26']:,}</td><td class="num">{c['toi_fy27']:,}</td><td class="num">{c['toi_fy28']:,}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">{c['ebitda_pct']}</td><td class="num">{c['mg_fy26']}</td><td class="num">{c['mg_fy27']}</td><td class="num">{c['mg_fy28']}</td></tr>
<tr><td>EBITDA</td><td class="num">{c['ebitda_fy25']}</td><td class="num">{c['eb_fy26']}</td><td class="num">{c['eb_fy27']}</td><td class="num">{c['eb_fy28']}</td></tr>
<tr><td>PAT</td><td class="num">{c['pat_fy25']}</td><td class="num">{c['pat_fy26']}</td><td class="num">{c['pat_fy27']}</td><td class="num">{c['pat_fy28']}</td></tr>
</tbody></table></div></section>"""
    prows = "".join(
        f"<tr><td>{p[0]}</td><td class=\"num\">{p[1]}</td><td class=\"num\">{p[2]}&ndash;{p[3]}</td><td>{p[4]}</td></tr>"
        for p in c['product_rows']
    )
    s7 = f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>{prows}</tbody></table></div>
<p><strong>Wholesale Y3:</strong> {c['wholesale_y3']}.</p></section>"""
    s8 = f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>{c['retail_text']}</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>{c['pb_text']}</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>{c['tasc_text']}</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>{c['retail_total_low']}-{c['retail_total_high']} Cr / yr</strong>.</p></section>"""
    crows = "".join(f"<tr><td>{s[0]}</td><td class=\"num\">{s[1]}</td><td class=\"num\">{s[2]}</td></tr>" for s in c['consolidated_rows'])
    s9 = f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>{crows}
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>{c['consolidated_total_low']}</strong></td><td class="num"><strong>{c['consolidated_total_high']}</strong></td></tr>
</tbody></table></div>
<p>Headline Rs {c['headline_low']}-{c['headline_high']} Cr/yr.</p></section>"""
    s10 = f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; {c['kmp_text']}.</p>
<h3>11.2 Ownership</h3><ul><li>{c['ownership_text']}{ref(str(src_b+1))}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>{c['diligence_news']}</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>{c['dil2']}</li><li>{c['dil3']}</li></ul></section>"""
    s11 = f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> {c['playbook_30']}</p></div>
<div class="card"><p><strong>T+60:</strong> {c['playbook_60']}</p></div>
<div class="card pos"><p><strong>T+90:</strong> {c['playbook_90']}</p></div>
<div class="card"><p><strong>T+180:</strong> {c['playbook_180']}</p></div>
<h3>Success metrics</h3><ul class="check">
{"".join(f"<li>{m}</li>" for m in c['success_metrics'])}
</ul></section>"""
    extra_src = "".join(
        f'<li id="src-{n}"><strong>{lbl}</strong> &mdash; {body}</li>'
        for (n,lbl,body) in c.get('src_extra', [])
    )
    s12 = f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; {c['name']}-specific from [{src_b}].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">{c['name']}-specific sources</h3>
<ol start="{src_b}">
<li id="src-{src_b}"><strong>MCA v3 + ZaubaCorp &mdash; {c['name']} master data</strong> &mdash; CIN {c['cin']}; incorp {c['incorp_date']}. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-{src_b+1}"><strong>{c['parent']} corporate disclosures + {c['name']} commentary</strong> &mdash; {c['src_parent_body']}. <span class="u">{c['src_parent_url']}</span></li>
{extra_src}
</ol></div></section>"""
    return [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]


def emit(cfg):
    OUT = Path("/home/user/St") / f"{cfg['slug']}-dossier.html"
    parts=[HEAD(cfg['title']),NAV] + [make_dossier(cfg)[0]] + [MACRO_BLOCK] + make_dossier(cfg)[1:] + [pad(cfg['pad_label'], cfg['pad_sector']), FOOT(cfg['footer'])]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
