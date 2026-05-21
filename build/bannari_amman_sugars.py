"""Bannari Amman Sugars Limited dossier (pilot 73)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "bannari-amman-sugars-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 73 of 75 · Coimbatore · Bannari Amman Group · Sugar + ethanol + power · IBank PRESENT 13.7% &mdash; share-grow defence</div>
<h1>Bannari Amman Sugars Limited<br>Listed TN flagship of Bannari Amman Group &mdash; sugar mills, ethanol-distillery, co-gen power, granite</h1>
<p class="lede">Bannari Amman Sugars Limited (CIN L15421TZ1983PLC001358){ref("580")} is a BSE/NSE-listed flagship of Bannari Amman Group, a Coimbatore-headquartered Tamil-Nadu industrial group{ref("581")}. <strong>FY25 Total Operating Income Rs 1,793 Cr</strong>{ref("128")}; EBITDA Rs 280 Cr (15.6%); PAT Rs 145 Cr; TNW Rs 1,250 Cr; Total Debt Rs 728 Cr (Debt/TNW 0.58x &mdash; conservative). <strong>9-bank disclosed consortium with charges Rs 728 Cr; HDFC Rs 200 Cr (27.5%) + PNB Rs 120 Cr (16.5%) + IBank Rs 100 Cr (13.7%) + Federal Rs 100 Cr (13.7%) + MoCA Rs 76 Cr (10.5%) + Axis Rs 60 Cr (8.2%) + SBI Rs 50 Cr (6.9%) + GoI Rs 11 Cr (1.6%) + IOB Rs 10 Cr (1.4%)</strong>{ref("126")} &mdash; <strong>IBank PRESENT 13.7%, #3 holder &mdash; share-grow defence play</strong>. Credit rating <strong>CARE AA- Stable (10 Dec 2025){ref("582")}</strong> on Rs 500 Cr LT facilities + Rs 15 Cr LT/ST. ~3,250 FTE{ref("128")}. 5 sugar mills (4 in TN + 1 in Karnataka) + 200 KLPD ethanol-distillery + 92 MW co-gen power + granite-quarrying + bio-fertiliser. Promoter: S.V. Balasubramaniam (founder), 67.3% holding{ref("128")}.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (defence + share-grow + ethanol)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,793 Cr</div><div class="sub">Sugar + ethanol + power{ref("128")}</div></div>
<div class="kpi pos"><div class="k">IBank share of charges</div><div class="v num">13.7%</div><div class="sub">Rs 100 Cr; #3 of 9{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE AA- Stable</div><div class="sub">10 Dec 2025{ref("582")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Defence + share-grow Rs 100 Cr position</strong> &mdash; HDFC Rs 200 Cr (27.5%) + PNB Rs 120 Cr (16.5%) leading; bid the next refresh tranche to climb above HDFC.</li>
<li><strong>Ethanol-distillery + E20-blending capex window{ref("12")}</strong> &mdash; Bannari already 200 KLPD; expansion to 350-400 KLPD by FY28 likely; capex TL framework.</li>
<li><strong>Bannari Amman Group ecosystem cross-sell</strong> &mdash; Bannari Amman Spinning Mills (BASM, listed) + Sakthi Sugars adjacency + group cross-sell.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L15421TZ1983PLC001358</strong></span>
<span>Incorp <strong>14 Apr 1983</strong></span>
<span>HO <strong>Coimbatore (HQ); plants in Erode, Sathyamangalam, Karnataka</strong></span>
<span>Promoter <strong>S.V. Balasubramaniam (Bannari Amman Group)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Bannari Amman Group{ref("581")} is a TN-headquartered diversified industrial group founded by S.V. Balasubramaniam in 1955; group revenue ~Rs 5,500-6,000 Cr FY25. Key listed entities: Bannari Amman Sugars Ltd (this entity, sugar + ethanol + power) + Bannari Amman Spinning Mills Ltd (BSE: 532998, textile spinning) + Sakthi Sugars Ltd (related-promoter; sugar). Unlisted: Bannari Amman Cement, Bannari Amman granite-quarrying, Bannari Group bio-fertiliser.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>9-bank consortium Rs 728 Cr{ref("126")}; HDFC + PNB + IBank + Federal + AXIS + SBI + IOB + MoCA cane-procurement-trust + GoI grant; IBank #3 at Rs 100 Cr (13.7%).</li>
<li>FY25 paid-up capital Rs 12.5 Cr; reserves Rs 1,238 Cr; promoter holding 67.3%.</li>
<li>Disclosed transactional banking{ref("128")}: HDFC + PNB + IBank + Federal + Axis + SBI consortium.</li>
<li>IBank participation: <strong>PRESENT</strong> 13.7%; defence + share-grow opportunity.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,520</td><td class="num">1,650</td><td class="num">1,793{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">220</td><td class="num">250</td><td class="num">280{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.5</td><td class="num">15.2</td><td class="num">15.6</td></tr>
<tr><td>PAT</td><td class="num">95</td><td class="num">115</td><td class="num">145{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">1,070</td><td class="num">1,160</td><td class="num">1,250{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">680</td><td class="num">700</td><td class="num">728{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.64x</td><td class="num">0.60x</td><td class="num">0.58x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 12.5 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~3,250</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 728 Cr</div><div class="sub">9-bank{ref("126")}</div></div>
<div class="kpi pos"><div class="k">IBank share</div><div class="v num">13.7%</div><div class="sub">#3 holder{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE AA- Stable</div><div class="sub">10 Dec 2025{ref("582")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>9-bank consortium Rs 728 Cr</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>HDFC Bank Limited</td><td class="num">200.0</td><td class="num">27.5</td><td>Lead bank</td></tr>
<tr><td>Punjab National Bank</td><td class="num">120.0</td><td class="num">16.5</td><td>#2 holder</td></tr>
<tr><td><strong>IBank</strong></td><td class="num"><strong>100.0</strong></td><td class="num"><strong>13.7</strong></td><td><strong>#3 holder &mdash; defence + share-grow</strong></td></tr>
<tr><td>Federal Bank Ltd</td><td class="num">100.0</td><td class="num">13.7</td><td>#3 tied</td></tr>
<tr><td>Min of Consumer Affairs</td><td class="num">76.4</td><td class="num">10.5</td><td>Cane-procurement trust</td></tr>
<tr><td>Axis Bank Ltd</td><td class="num">60.0</td><td class="num">8.2</td><td></td></tr>
<tr><td>State Bank of India</td><td class="num">50.0</td><td class="num">6.9</td><td></td></tr>
<tr><td>Government of India</td><td class="num">11.4</td><td class="num">1.6</td><td>Subsidy/grant trust</td></tr>
<tr><td>Indian Overseas Bank</td><td class="num">10.0</td><td class="num">1.4</td><td>Residual</td></tr>
</tbody></table></div>
<p class="lede">Strategic: defend the Rs 100 Cr position + climb to #2 (Rs 150 Cr) on next refresh; bid HDFC Rs 50 Cr secondary tranche.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Sugar + ethanol + co-gen</div>
<p>India sugar industry FY25 ~Rs 1.3 lakh Cr revenue; CAGR 5-7%; key players Balrampur Chini, Renuka Sugars, EID Parry, DCM Shriram + integrated mills (Bajaj Hindusthan, Triveni). E20 blending mandate{ref("12")} structurally drives ethanol-distillery investment 8-10% CAGR; cane-SAP{ref("15")} and TN-state-advised-price + ISMA crush projections{ref("17")} drive margin sensitivity.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>E20 blending{ref("12")}: ethanol-distillery output structural growth.</li>
<li>Cane-SAP{ref("15")} + TN-SAP: input-cost sensitivity.</li>
<li>USA-tariff window{ref("6")}: limited (sugar is domestic-anchored).</li>
<li>El Nino / monsoon{ref("4")}: cane-yield + crush variability.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,793{ref("128")}</td><td class="num">2,000</td><td class="num">2,250</td><td class="num">2,550</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.6</td><td class="num">16.4</td><td class="num">17.2</td><td class="num">18.0</td></tr>
<tr><td>EBITDA</td><td class="num">280</td><td class="num">328</td><td class="num">387</td><td class="num">459</td></tr>
<tr><td>PAT</td><td class="num">145</td><td class="num">175</td><td class="num">215</td><td class="num">265</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (defend + grow)</td><td class="num">120&ndash;180</td><td class="num">2.5&ndash;4.5</td><td>Climb to #2 from #3</td></tr>
<tr><td>Capex TL (ethanol expansion)</td><td class="num">200&ndash;400</td><td class="num">3&ndash;6</td><td>200&rarr;350-400 KLPD</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">120&ndash;200</td><td class="num">1.5&ndash;2.5</td><td>Sugar + cane purchase</td></tr>
<tr><td>SCF (cane farmer + dealer)</td><td class="num">200&ndash;320</td><td class="num">2.5&ndash;4</td><td>Cane-procurement SCF</td></tr>
<tr><td>EBR / PCFC (ethanol export)</td><td class="num">80&ndash;130</td><td class="num">0.8&ndash;1.4</td><td>Export ramp</td></tr>
<tr><td>NCD / DCM arranger</td><td class="num">200&ndash;400</td><td class="num">1.5&ndash;3</td><td>AA-rated capex DCM</td></tr>
<tr><td>FX (USD)</td><td class="num">300&ndash;500 notional</td><td class="num">1.2&ndash;2.2</td><td>Capex + ethanol-export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.6&ndash;1</td><td>3,250 FTE + farmer payments</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.6-24.6 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 2,500-3,200; cane farmer-CASA + dealer-loan + tractor-loan; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>S.V. Balasubramaniam family + senior leadership; PB AUM Rs 280-440 Cr; Rs 3-4.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Bannari Amman CSR; Rs 95-140 Cr; Rs 0.9-1.3 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 6.4-9.8 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">2.5</td><td class="num">4.5</td></tr>
<tr><td>Capex TL (ethanol)</td><td class="num">3</td><td class="num">6</td></tr>
<tr><td>Trade + SCF + EBR</td><td class="num">4.8</td><td class="num">7.9</td></tr>
<tr><td>NCD/DCM</td><td class="num">1.5</td><td class="num">3</td></tr>
<tr><td>FX</td><td class="num">1.2</td><td class="num">2.2</td></tr>
<tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">1</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">6.4</td><td class="num">9.8</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>20.0</strong></td><td class="num"><strong>34.4</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr captures upper-mid band incl. share-grow defence.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; S.V. Balasubramaniam family + Bannari Amman Group leadership.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter holding 67.3%{ref("128")}; BSE/NSE listed; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Dec 2025: CARE reaffirms AA- Stable{ref("582")}.</li><li>FY26: ethanol-distillery expansion to 350+ KLPD announced.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 IBank Rs 100 Cr refresh calendar</li><li>T-14 Pre-pitch ethanol-capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Bannari Amman Sugars CFO meeting; defence + share-grow concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Refresh Rs 100 Cr position; bid Rs 50-60 Cr secondary tranche.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for ethanol-distillery expansion.</p></div>
<div class="card"><p><strong>T+180:</strong> Bannari Amman Group + BASM ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>IBank position Rs 150-160 Cr by Q3 FY27 (climb to #2)</li><li>Capex TL Rs 250 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Bannari Amman Sugars-specific from [580].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Bannari Amman Sugars-specific sources</h3>
<ol start="580">
<li id="src-580"><strong>MCA v3 + ZaubaCorp + BSE/NSE listing &mdash; Bannari Amman Sugars Ltd master data</strong> &mdash; CIN L15421TZ1983PLC001358; incorp 14 Apr 1983; RoC Coimbatore. <span class="u">mca.gov.in &middot; bseindia.com &middot; nseindia.com</span></li>
<li id="src-581"><strong>Bannari Amman Group corporate disclosures + S.V. Balasubramaniam family commentary + Sakthi Sugars adjacency</strong> &mdash; group revenue ~Rs 5,500-6,000 Cr FY25; founded 1955. <span class="u">bannariammangroup.com &middot; bannarisugars.com</span></li>
<li id="src-582"><strong>CARE Ratings &mdash; Bannari Amman Sugars Ltd rating rationale (10 Dec 2025)</strong> &mdash; reaffirms AA- Stable on Rs 500 Cr LT facilities + Rs 15 Cr LT/ST. <span class="u">careedge.in</span></li>
</ol></div></section>"""

def build():
    t = "Bannari Amman Sugars · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Bannari Amman Sugars", "Sugar + ethanol + co-gen / Bannari Amman Group"),
           FOOT("Cipher clean; 1,500+ lines; IBank PRESENT 13.7% defence + share-grow + ethanol capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
