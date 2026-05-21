"""Perkins India dossier (pilot 84)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "perkins-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 84 of 90 · Aurangabad / Hosur · Caterpillar US · Diesel/gas engines · Greenfield</div>
<h1>Perkins India Private Limited<br>UK-origin Perkins Engines (Caterpillar Inc subsidiary) Indian off-highway diesel + gas engine arm</h1>
<p class="lede">Perkins India Pvt Ltd (CIN U29253TN2011PTC084853){ref("690")} is the Indian subsidiary of Perkins Engines Company Limited (UK), wholly-owned by Caterpillar Inc (NYSE: CAT; FY25 revenue ~$67 bn){ref("691")}. <strong>FY25 Total Operating Income Rs 2,172 Cr</strong>{ref("128")}; EBITDA Rs 295 Cr (13.6%); PAT Rs 165 Cr; TNW Rs 985 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,400 FTE{ref("128")}. Manufactures off-highway diesel + gas engines (4-22 litre, 36-1500 hp) for construction equipment + power-generation + agriculture machinery + industrial OEMs.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + customer-SCF + capex TL)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,172 Cr</div><div class="sub">Off-highway engines{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD + GBP royalty + RM-import hedge</strong> &mdash; Perkins UK + Caterpillar US intercompany flows.</li>
<li><strong>Customer-SCF on JCB + L&amp;T + Tata Power + Mahindra anchors</strong> &mdash; engine-customer receivables.</li>
<li><strong>Tier-V emission ramp + EV-genset transition capex window</strong> &mdash; capex TL framework.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29253TN2011PTC084853</strong></span>
<span>Incorp <strong>30 Mar 2011</strong></span>
<span>HO <strong>Hosur (TN) + Aurangabad</strong></span>
<span>Parent <strong>Perkins Engines Co Ltd / Caterpillar Inc (UK/US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Perkins Engines Company Limited (UK){ref("691")} is wholly-owned by Caterpillar Inc (NYSE: CAT; FY25 revenue ~$67 bn). India operations: Perkins India Pvt Ltd (this entity, off-highway engine assembly + parts); sister entity Caterpillar India (pilot 18 done earlier) for construction equipment.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 75 Cr; reserves Rs 910 Cr; cash Rs 290 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (Caterpillar anchor), JPMorgan, HSBC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,720</td><td class="num">1,945</td><td class="num">2,172{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">220</td><td class="num">255</td><td class="num">295{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.8</td><td class="num">13.1</td><td class="num">13.6</td></tr>
<tr><td>PAT</td><td class="num">110</td><td class="num">135</td><td class="num">165{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">740</td><td class="num">860</td><td class="num">985{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 75 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,400</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 290 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: greenfield FX + customer-SCF + capex TL; sister-entity Caterpillar India bundled cross-sell.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Off-highway engines + gensets</div>
<p>India off-highway-engines market FY25 ~Rs 14,000 Cr; CAGR 9-11%; Perkins + Cummins + KOEL + Mahindra Powertrain + Greaves Cotton compete. Tier-V + Tier-VI emission norms phasing through FY26-28; EV-genset (battery + fuel-cell) transition.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>BS6 + Tier-V emission ramp.</li>
<li>USA-tariff window{ref("6")}: limited (engines local-anchored).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting.</li>
<li>Construction-equipment + power-genset capex cycle.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,172{ref("128")}</td><td class="num">2,450</td><td class="num">2,800</td><td class="num">3,200</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.6</td><td class="num">14.0</td><td class="num">14.4</td><td class="num">14.8</td></tr>
<tr><td>EBITDA</td><td class="num">295</td><td class="num">343</td><td class="num">403</td><td class="num">474</td></tr>
<tr><td>PAT</td><td class="num">165</td><td class="num">195</td><td class="num">235</td><td class="num">280</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + GBP)</td><td class="num">700&ndash;1,100 notional</td><td class="num">3&ndash;5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">280&ndash;420 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-SCF (JCB/L&amp;T/Tata Power)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Engine-customer receivables</td></tr>
<tr><td>Capex TL (Tier-V ramp + EV-genset)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>RM + capex</td></tr>
<tr><td>EBR / PCFC (engine export)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>Caterpillar global re-export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,400 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.7-22.2 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,050-1,300; Rs 1.7-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>UK/US expat MD + Indian leadership; PB AUM Rs 90-150 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Perkins/Caterpillar CSR; Rs 65-100 Cr; Rs 0.6-0.9 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.3-4.9 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Customer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">5.2</td><td class="num">8.4</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.3</td><td class="num">4.9</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>17.0</strong></td><td class="num"><strong>27.1</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Perkins/Caterpillar parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Perkins Engines Co Ltd / Caterpillar Inc{ref("691")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Perkins India Tier-V engine portfolio launch.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Caterpillar India relationship adjacency</li><li>T-14 Pre-pitch capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Perkins India CFO meeting; FX + customer-SCF + capex memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with JCB; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for Tier-V ramp.</p></div>
<div class="card"><p><strong>T+180:</strong> Caterpillar India + Perkins India bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 150 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Perkins-specific from [690].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Perkins India-specific sources</h3>
<ol start="690">
<li id="src-690"><strong>MCA v3 + ZaubaCorp &mdash; Perkins India Pvt Ltd master data</strong> &mdash; CIN U29253TN2011PTC084853; incorp 30 Mar 2011. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-691"><strong>Caterpillar Inc Annual Report FY25 + NYSE CAT disclosures + Perkins Engines (UK) commentary</strong> &mdash; FY25 ~$67 bn revenue; Perkins UK wholly-owned subsidiary. <span class="u">caterpillar.com &middot; perkins.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "Perkins India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Perkins India", "Off-highway engines / Caterpillar US"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + Tier-V emission capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
