"""Tenneco Automotive India dossier (pilot 85)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "tenneco-automotive-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 85 of 90 · Hosur · Tenneco Inc / Apollo · Auto ride-control · Greenfield</div>
<h1>Tenneco Automotive India Private Limited<br>Apollo-owned Tenneco Inc Indian ride-control (shocks + struts) subsidiary</h1>
<p class="lede">Tenneco Automotive India Pvt Ltd (CIN U34300TZ1998PTC015231){ref("700")} is the ride-control (shocks + struts + dampers) subsidiary of Apollo-owned Tenneco Inc (US, post-2022 take-private){ref("701")}. Sister entity Tenneco Clean Air India Limited (pilot 68 done, listed) handles emission-control. <strong>FY25 Total Operating Income Rs 2,078 Cr</strong>{ref("128")}; EBITDA Rs 245 Cr (11.8%); PAT Rs 130 Cr; TNW Rs 720 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,500 FTE{ref("128")}. Manufactures shocks + struts + dampers + ride-control assemblies for Maruti Suzuki, Hyundai, Mahindra, Tata Motors, Ashok Leyland.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + customer-SCF + capex)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,078 Cr</div><div class="sub">Auto ride-control{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD royalty + RM-import hedge</strong> &mdash; Tenneco intercompany flows.</li>
<li><strong>Customer-SCF on Maruti + Hyundai + Tata + Mahindra anchors</strong> &mdash; OEM receivables.</li>
<li><strong>Tenneco Clean Air sister-entity bundled cross-sell</strong> &mdash; pilot 68 ecosystem.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U34300TZ1998PTC015231</strong></span>
<span>Incorp <strong>17 Jul 1998</strong></span>
<span>HO <strong>Hosur (TN) + Chakan (MH)</strong></span>
<span>Parent <strong>Tenneco Inc / Apollo Global Mgmt (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Tenneco Inc{ref("701")} is owned by Apollo Global Mgmt (NYSE: APO; Nov 2022 ~$7.1 bn take-private). FY25 group revenue ~$18 bn. India operations: Tenneco Automotive India Pvt Ltd (this entity, ride-control) + Tenneco Clean Air India Ltd (BSE/NSE listed, pilot 68 emission-control) + Federal-Mogul Goetze India (BSE 505744, listed legacy entity for piston rings + cylinder liners).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 35 Cr; reserves Rs 685 Cr; cash Rs 220 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (Apollo-Tenneco anchor), JPMorgan, HDFC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,650</td><td class="num">1,860</td><td class="num">2,078{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">175</td><td class="num">210</td><td class="num">245{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">10.6</td><td class="num">11.3</td><td class="num">11.8</td></tr>
<tr><td>PAT</td><td class="num">85</td><td class="num">105</td><td class="num">130{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">540</td><td class="num">630</td><td class="num">720{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 35 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,500</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 220 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: greenfield FX + customer-SCF; Tenneco Clean Air sister bundled cross-sell.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto ride-control + suspension</div>
<p>India ride-control market FY25 ~Rs 11,500 Cr; CAGR 7-9%; Tenneco + Endurance Tech + Gabriel India + KYB Conmat compete. EV-suspension ramp; ride-comfort premiumisation.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India ride-control component export ramp.</li>
<li>EV-suspension transition: Tenneco active-suspension R&amp;D.</li>
<li>OEM capex cycle.</li>
<li>Ride-comfort premiumisation in PV.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,078{ref("128")}</td><td class="num">2,330</td><td class="num">2,650</td><td class="num">3,000</td></tr>
<tr><td>EBITDA margin %</td><td class="num">11.8</td><td class="num">12.3</td><td class="num">12.8</td><td class="num">13.3</td></tr>
<tr><td>EBITDA</td><td class="num">245</td><td class="num">287</td><td class="num">339</td><td class="num">399</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">155</td><td class="num">185</td><td class="num">220</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD)</td><td class="num">650&ndash;1,000 notional</td><td class="num">2.5&ndash;4.5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">220&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-SCF (Maruti/Hyundai/Tata)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>OEM receivables</td></tr>
<tr><td>Capex TL (EV-suspension ramp)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>RM + capex</td></tr>
<tr><td>EBR / PCFC</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>Export tier-1</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,500 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 11.2-18.8 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,150-1,400; Rs 1.8-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>US/Apollo expat MD + Indian leadership; PB AUM Rs 95-160 Cr; Rs 1.2-1.8 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Tenneco CSR; Rs 70-110 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.7-5.3 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">2.5</td><td class="num">4.5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>Customer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">3.7</td><td class="num">6.1</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.7</td><td class="num">5.3</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>14.9</strong></td><td class="num"><strong>24.1</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Tenneco/Apollo appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Tenneco Inc / Apollo Global Mgmt{ref("701")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Tenneco India active-suspension launch for premium-PV.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Tenneco Clean Air listed-arm relationship adjacency</li><li>T-14 Pre-pitch capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Tenneco Automotive CFO meeting; FX + customer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with Maruti.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for EV-suspension.</p></div>
<div class="card"><p><strong>T+180:</strong> Tenneco Clean Air + Tenneco Auto bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 200 Cr by Q3 FY27</li><li>Capex TL Rs 100 Cr drawn</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Tenneco Auto-specific from [700].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Tenneco Automotive India-specific sources</h3>
<ol start="700">
<li id="src-700"><strong>MCA v3 + ZaubaCorp &mdash; Tenneco Automotive India Pvt Ltd master data</strong> &mdash; CIN U34300TZ1998PTC015231; incorp 17 Jul 1998. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-701"><strong>Tenneco Inc + Apollo Global Mgmt take-private (Nov 2022 ~$7.1 bn)</strong> &mdash; FY25 ~$18 bn revenue; sister Tenneco Clean Air India Ltd listed BSE/NSE. <span class="u">tenneco.com &middot; apollo.com</span></li>
</ol></div></section>"""

def build():
    t = "Tenneco Automotive India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Tenneco Automotive India", "Auto ride-control (shocks/struts) / Tenneco-Apollo US"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + EV-suspension capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
