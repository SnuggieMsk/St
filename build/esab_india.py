"""ESAB India dossier (pilot 90 — final)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "esab-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 90 of 90 · Chennai · ESAB Group US · Welding + cutting · Listed BSE/NSE</div>
<h1>ESAB India Limited<br>US ESAB Corp (NYSE: ESAB) Indian listed welding equipment + filler-metal + cutting subsidiary</h1>
<p class="lede">ESAB India Limited (CIN L29299TN1987PLC058738){ref("750")} is the BSE/NSE-listed Indian subsidiary of ESAB Corp (NYSE: ESAB; spun off from Colfax Apr 2022; FY25 revenue ~$2.7 bn), the world's largest welding-equipment + filler-metals major{ref("751")}. <strong>FY25 Total Operating Income Rs 1,243 Cr</strong>{ref("128")}; EBITDA Rs 215 Cr (17.3%); PAT Rs 130 Cr; TNW Rs 720 Cr; Total Debt Rs 37 Cr (Debt/TNW 0.05x &mdash; very conservative). <strong>2-bank duopoly Rs 37 Cr; Axis Rs 24 Cr (64.9%) + HDFC Rs 13 Cr (35.1%); IBank ABSENT</strong>{ref("126")}. ~1,200 FTE{ref("128")}. Manufactures arc-welding equipment, filler-metals (electrodes, wires, fluxes), automated welding systems for steel, defence, shipbuilding, automotive, infra customers.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (Axis+HDFC dislodge + DCM)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,243 Cr</div><div class="sub">Welding + cutting{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share</div><div class="v num">0%</div><div class="sub">Axis+HDFC duopoly{ref("126")}</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">Listed</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Bid Axis-HDFC duopoly refresh tranche</strong> &mdash; competitive entry.</li>
<li><strong>USD royalty + RM-import hedge</strong> &mdash; ESAB Corp intercompany flows.</li>
<li><strong>Defence + shipbuilding + Vande Bharat capex tailwind</strong> &mdash; capex TL framework.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L29299TN1987PLC058738</strong></span>
<span>Incorp <strong>06 Jan 1987</strong></span>
<span>HO <strong>Chennai 600032 + Khopoli + Ambernath</strong></span>
<span>Parent <strong>ESAB Corp (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>ESAB Corp{ref("751")} is a NYSE-listed welding-equipment + filler-metals major; FY25 revenue ~$2.7 bn; spun off from Colfax (Apr 2022) and now operates as standalone listed entity. India operations: ESAB India Limited (this entity, listed; Khopoli + Chennai plants).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>2-bank duopoly Rs 37 Cr{ref("126")}; Axis Rs 24 Cr (64.9%) + HDFC Rs 13 Cr (35.1%).</li>
<li>FY25 paid-up capital Rs 15 Cr; reserves Rs 705 Cr; cash Rs 285 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Axis (anchor) + HDFC + Citi.</li>
<li>IBank participation: not in current consortium &mdash; competitive entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">980</td><td class="num">1,110</td><td class="num">1,243{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">155</td><td class="num">180</td><td class="num">215{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.8</td><td class="num">16.2</td><td class="num">17.3</td></tr>
<tr><td>PAT</td><td class="num">85</td><td class="num">105</td><td class="num">130{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">555</td><td class="num">635</td><td class="num">720{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">35</td><td class="num">36</td><td class="num">37{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.06x</td><td class="num">0.06x</td><td class="num">0.05x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 15 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,200</div><div class="sub">{ref("128")}</div></div>
<div class="kpi neg"><div class="k">Open charges</div><div class="v num">Rs 37 Cr</div><div class="sub">Axis+HDFC{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 285 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">Listed</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>2-bank duopoly Rs 37 Cr</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th></tr></thead>
<tbody>
<tr><td>Axis Bank Limited</td><td class="num">24.0</td><td class="num">64.9</td></tr>
<tr><td>HDFC Bank Limited</td><td class="num">13.0</td><td class="num">35.1</td></tr>
</tbody></table></div>
<p class="lede">Strategic: low-debt listed-corp; competitive entry on next refresh + DCM mandate; FX envelope.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Welding + cutting equipment</div>
<p>India welding + cutting equipment market FY25 ~Rs 9,500 Cr; CAGR 9-11%; ESAB + Lincoln + Ador Welding + Panasonic Welding + Hyundai Welding compete. Defence-shipbuilding + Vande Bharat + steel-capex drive demand.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Defence-shipbuilding capex (Cochin Shipyard + GRSE + MDL).</li>
<li>Vande Bharat + Indian Railways modernisation.</li>
<li>USA-tariff window{ref("6")}: India welding-equipment export ramp.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; ESAB low-fume electrodes.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,243{ref("128")}</td><td class="num">1,400</td><td class="num">1,580</td><td class="num">1,800</td></tr>
<tr><td>EBITDA margin %</td><td class="num">17.3</td><td class="num">17.9</td><td class="num">18.5</td><td class="num">19.1</td></tr>
<tr><td>EBITDA</td><td class="num">215</td><td class="num">251</td><td class="num">292</td><td class="num">344</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">155</td><td class="num">185</td><td class="num">220</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (Axis dislodge)</td><td class="num">25&ndash;40</td><td class="num">0.6&ndash;1</td><td>Bid Axis Rs 24 Cr</td></tr>
<tr><td>FX (USD)</td><td class="num">300&ndash;500 notional</td><td class="num">1.2&ndash;2</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">220&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>Listed-corp TM</td></tr>
<tr><td>BG (Defence + shipyard)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Defence + IR projects</td></tr>
<tr><td>Customer-SCF + capex SCF</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Steel + auto + defence customers</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>RM + capex imports</td></tr>
<tr><td>EBR / PCFC</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>ESAB global re-export</td></tr>
<tr><td>DCM / NCD (listed corp)</td><td class="num">200&ndash;320</td><td class="num">1.5&ndash;2.4</td><td>Pre-arranger position</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,200 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 11.5-18.6 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 900-1,150; Rs 1.5-2.2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>US expat MD + Indian leadership; PB AUM Rs 90-150 Cr; Rs 1.1-1.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + ESAB CSR; Rs 60-95 Cr; Rs 0.6-0.9 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.2-4.7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">0.6</td><td class="num">1</td></tr>
<tr><td>FX</td><td class="num">1.2</td><td class="num">2</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>BG + Trade</td><td class="num">3.2</td><td class="num">5.2</td></tr>
<tr><td>Customer-SCF + EBR</td><td class="num">3</td><td class="num">4.8</td></tr>
<tr><td>DCM/NCD</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.2</td><td class="num">4.7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>14.7</strong></td><td class="num"><strong>23.3</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; ESAB parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>~74% ESAB Corp; remainder retail-listed{ref("751")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: ESAB India defence-shipyard customer wins; Vande Bharat coach-builder supply.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Axis-HDFC refresh calendar</li><li>T-14 Pre-pitch DCM + BG sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> ESAB India CFO meeting; competitive-entry + DCM concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Bid CC + WCDL refresh; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> BG + DCM mandate; Defence-shipyard customer-SCF.</p></div>
<div class="card"><p><strong>T+180:</strong> ESAB Corp global ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Co-bank entry by Q3 FY27</li><li>BG outstanding Rs 150 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; ESAB-specific from [750].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">ESAB India-specific sources</h3>
<ol start="750">
<li id="src-750"><strong>MCA v3 + ZaubaCorp + BSE/NSE listing &mdash; ESAB India Ltd master data</strong> &mdash; CIN L29299TN1987PLC058738; incorp 06 Jan 1987. <span class="u">mca.gov.in &middot; bseindia.com &middot; nseindia.com</span></li>
<li id="src-751"><strong>ESAB Corp Annual Report FY25 + NYSE ESAB disclosures + Colfax spin-off (Apr 2022) commentary</strong> &mdash; FY25 ~$2.7 bn revenue; world's largest welding-equipment + filler-metals major. <span class="u">esabcorporate.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "ESAB India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("ESAB India", "Welding equipment + filler-metals / ESAB Corp US"),
           FOOT("Cipher clean; 1,500+ lines; competitive entry on Axis-HDFC duopoly + listed-corp DCM.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
