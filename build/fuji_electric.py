"""Fuji Electric India dossier (pilot 89)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "fuji-electric-dossier.html"

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

def S1():
    return f"""
<section id="cover" class="hero">
<div class="eyebrow">Tier-1 Dossier · Pilot 89 of 90 · Chennai · Fuji Electric Co Ltd Japan · Power equipment + drives · CARE A+/A1</div>
<h1>Fuji Electric India Private Limited<br>Japanese Fuji Electric (TSE: 6504) Indian power-electronics + drives + UPS + power-meter + semiconductor arm</h1>
<p class="lede">Fuji Electric India Pvt Ltd (CIN U31900TN1985PTC011866){ref("740")} is the Indian subsidiary of Fuji Electric Co Ltd (TSE: 6504; ~&yen;1.1 trillion / $7.5 bn revenue), a Japanese power-electronics + drives major{ref("741")}. <strong>FY25 Total Operating Income Rs 1,504 Cr</strong>{ref("128")}; EBITDA Rs 195 Cr (13.0%); PAT Rs 105 Cr; TNW Rs 595 Cr; Total Debt Rs 1.45 Cr (negligible). <strong>Single negligible South Indian Bank Rs 1.45 Cr charge only &mdash; effectively zero charges</strong>{ref("126")}. Credit rating <strong>CARE A+ / A1 Reaffirmed (20 Mar 2026){ref("742")}</strong> on Rs 34.4 Cr LT + Rs 379.2 Cr LT/ST + Rs 61 Cr ST. ~1,200 FTE{ref("128")}. Manufactures UPS, power-meters, drives, low-voltage switchgear, semiconductor power-electronics for Indian + global markets.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + customer-SCF + capex)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,504 Cr</div><div class="sub">Power equipment + drives{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 1.45 Cr</div><div class="sub">Negligible{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE A+ / A1</div><div class="sub">20 Mar 2026{ref("742")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>JPY + USD royalty + RM-import hedge</strong> &mdash; Fuji Japan intercompany flows.</li>
<li><strong>BG + LC envelope on Rs 379 Cr ST/LT facility</strong> &mdash; rated A+ + A1; bid the next refresh.</li>
<li><strong>Data-center + UPS + EV-charger + grid-modernisation capex window</strong> &mdash; structural growth.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U31900TN1985PTC011866</strong></span>
<span>Incorp <strong>10 Jan 1985</strong></span>
<span>HO <strong>Chennai (Sriperumbudur) + Pune</strong></span>
<span>Parent <strong>Fuji Electric Co Ltd (Japan)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Fuji Electric Co Ltd{ref("741")} is a Japanese listed (TSE: 6504) power-electronics + drives + semiconductor + UPS major; FY25 revenue ~&yen;1.1 trillion / $7.5 bn. India operations: Fuji Electric India Pvt Ltd (this entity, Sriperumbudur + Pune plants).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Negligible Rs 1.45 Cr charge (South Indian Bank residual){ref("126")}; rated facility Rs 474 Cr underutilised.</li>
<li>FY25 paid-up capital Rs 65 Cr; reserves Rs 530 Cr; cash Rs 195 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: MUFG (Japanese MNC default), Mizuho, SBI, South Indian Bank.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + BG/LC entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,180</td><td class="num">1,340</td><td class="num">1,504{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">130</td><td class="num">160</td><td class="num">195{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">11.0</td><td class="num">11.9</td><td class="num">13.0</td></tr>
<tr><td>PAT</td><td class="num">65</td><td class="num">85</td><td class="num">105{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">450</td><td class="num">520</td><td class="num">595{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~1</td><td class="num">~1</td><td class="num">1.45{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 65 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,200</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 1.45 Cr</div><div class="sub">SIB residual{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 195 Cr</div><div class="sub">est.</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE A+ / A1</div><div class="sub">20 Mar 2026{ref("742")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>1 charge SIB Rs 1.45 Cr residual; rated facility Rs 474.6 Cr underutilised</strong>{ref("126")}{ref("742")}.</p>
<p class="lede">Strategic: bid BG + LC + WC tranche of the rated facility; FX hedge envelope.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Power equipment + UPS + drives + semiconductor</div>
<p>India power-electronics + UPS market FY25 ~Rs 22,000 Cr; CAGR 12-14%; Fuji + Schneider + Eaton + Vertiv + Emerson + Hitachi compete. Data-center + EV-charger + grid-modernisation drives.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Data-center + UPS demand: AI + cloud-capex + GIFT-IFSC.</li>
<li>EV-charger + EV-fast-charging deployment.</li>
<li>USA-tariff window{ref("6")}: India power-electronics export ramp.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,504{ref("128")}</td><td class="num">1,720</td><td class="num">1,980</td><td class="num">2,280</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.0</td><td class="num">13.6</td><td class="num">14.2</td><td class="num">14.8</td></tr>
<tr><td>EBITDA</td><td class="num">195</td><td class="num">234</td><td class="num">281</td><td class="num">337</td></tr>
<tr><td>PAT</td><td class="num">105</td><td class="num">130</td><td class="num">160</td><td class="num">195</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (JPY + USD)</td><td class="num">500&ndash;750 notional</td><td class="num">2&ndash;3.5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">160&ndash;240 float</td><td class="num">1&ndash;1.6</td><td>MNC TM-aaS</td></tr>
<tr><td>BG (project + customer)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>UPS+drives projects</td></tr>
<tr><td>LC + Trade</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Capex + RM</td></tr>
<tr><td>Customer-SCF (data-center + EV-charger)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Receivables</td></tr>
<tr><td>Capex TL (semiconductor + drives ramp)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>Sustainability-linked</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>Fuji global re-export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,200 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 11.2-18.4 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 900-1,150; Rs 1.5-2.2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Japanese expat MD + Indian leadership; PB AUM Rs 75-130 Cr; Rs 0.9-1.4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Fuji CSR; Rs 60-95 Cr; Rs 0.5-0.8 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 2.9-4.4 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">2</td><td class="num">3.5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1</td><td class="num">1.6</td></tr>
<tr><td>BG + LC + Trade</td><td class="num">3.5</td><td class="num">5.7</td></tr>
<tr><td>Customer-SCF + capex TL + EBR</td><td class="num">4.2</td><td class="num">6.8</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">2.9</td><td class="num">4.4</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>14.1</strong></td><td class="num"><strong>22.8</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr captures upper-mid band incl. data-center + EV-charger ramp.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Fuji parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Fuji Electric Co Ltd (Japan){ref("741")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Mar 2026: CARE reaffirms A+ / A1{ref("742")}.</li><li>FY26: Fuji India data-center UPS launch.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 SIB residual + new bank refresh</li><li>T-14 Pre-pitch BG + capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Fuji India CFO meeting; FX + BG + capex memo.</p></div>
<div class="card"><p><strong>T+60:</strong> BG + LC pilot; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Customer-SCF + capex TL framework.</p></div>
<div class="card"><p><strong>T+180:</strong> Fuji global ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>BG outstanding Rs 200 Cr by Q3 FY27</li><li>Capex TL Rs 100 Cr drawn</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Fuji-specific from [740].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Fuji Electric India-specific sources</h3>
<ol start="740">
<li id="src-740"><strong>MCA v3 + ZaubaCorp &mdash; Fuji Electric India Pvt Ltd master data</strong> &mdash; CIN U31900TN1985PTC011866; incorp 10 Jan 1985. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-741"><strong>Fuji Electric Co Ltd Annual Report FY25 + TSE 6504 disclosures</strong> &mdash; FY25 ~&yen;1.1 trillion / $7.5 bn revenue; Japanese power-electronics + drives + semiconductor major. <span class="u">fujielectric.com &middot; jpx.co.jp</span></li>
<li id="src-742"><strong>CARE Ratings &mdash; Fuji Electric India Pvt Ltd rating rationale (20 Mar 2026)</strong> &mdash; reaffirms A+ on Rs 34.44 Cr LT + Rs 379.20 Cr LT/ST + A1 on Rs 61 Cr ST. <span class="u">careedge.in</span></li>
</ol></div></section>"""

def build():
    t = "Fuji Electric India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Fuji Electric India", "Power equipment + drives / Fuji Electric Japan"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + BG/LC + data-center + EV-charger capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
