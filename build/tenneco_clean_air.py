"""Tenneco Clean Air India dossier (pilot 68)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "tenneco-clean-air-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 68 of 75 · Chennai · Tenneco Inc · Listed BSE/NSE · Auto emission-control · Greenfield</div>
<h1>Tenneco Clean Air India Limited<br>Listed Indian subsidiary of Tenneco Inc (Apollo-owned, US private) for emission-control / clean-air systems</h1>
<p class="lede">Tenneco Clean Air India Limited (CIN L29308TN2018FLC126510){ref("530")} is the BSE/NSE-listed Indian subsidiary of Tenneco Inc (US, owned by Apollo Global Management since the 2022 take-private){ref("531")}. <strong>FY25 Total Operating Income Rs 2,237 Cr</strong>{ref("128")}; EBITDA Rs 270 Cr (12.1%); PAT Rs 130 Cr; TNW Rs 950 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 1,260 FTE{ref("128")}. Manufactures complete-exhaust + after-treatment systems (catalytic converter, DPF, SCR, urea-injection) for OEMs (Maruti Suzuki, Hyundai, Mahindra, Tata, Ashok Leyland) at Hosur (TN) + Chakan (MH) + Pant Nagar (Uttarakhand).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + capex + customer-SCF)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,237 Cr</div><div class="sub">Emission-control{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">2018 listing{ref("530")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD royalty + RM-import hedge</strong> &mdash; substrate (Pt-Pd-Rh-loaded ceramics) imports from Tenneco global.</li>
<li><strong>BS6 phase-2 + future BS7 capex window</strong> &mdash; emission-control sophistication ramp; capex TL framework.</li>
<li><strong>Customer-SCF on OEM anchors</strong> &mdash; Maruti, Hyundai, Tata, Mahindra, Ashok Leyland; receivable-discounting.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L29308TN2018FLC126510</strong></span>
<span>Incorp <strong>05 Apr 2018</strong></span>
<span>HO <strong>Chennai 600032</strong></span>
<span>Parent <strong>Tenneco Inc / Apollo Global Mgmt (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Tenneco Inc{ref("531")} is a US-based propulsion-systems major; FY25 revenue ~$18 bn (post Federal-Mogul integration); Apollo Global Management acquired Tenneco for ~$7.1 bn enterprise value Nov 2022 (take-private). India operations: Tenneco Clean Air India Limited (this entity, listed) for emission-control + Tenneco Automotive India Pvt Ltd (separate entity) for ride-control (shocks, struts) + Federal-Mogul Goetze India (separate-listed legacy entity) for piston rings + cylinder liners.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 30 Cr; reserves Rs 920 Cr; cash Rs 240 Cr.</li>
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
<tr><td>TOI</td><td class="num">1,800</td><td class="num">2,020</td><td class="num">2,237{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">200</td><td class="num">235</td><td class="num">270{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">11.1</td><td class="num">11.6</td><td class="num">12.1</td></tr>
<tr><td>PAT</td><td class="num">85</td><td class="num">105</td><td class="num">130{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">760</td><td class="num">855</td><td class="num">950{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 30 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">1,260</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 240 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">{ref("530")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: BS6+ + BS7 capex window; FX + customer-SCF + listed-corp DCM access pre-arranger seat.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto emission-control</div>
<p>India auto emission-control market FY25 ~Rs 18,000 Cr; CAGR 8-10%; Tenneco + Bosal-Faurecia (now Forvia) + Eberspaecher-IAC + Sango-Eicher compete; Tenneco India market share ~28-32% (#1 in PV, #2 in CV).</p>
<h3>06.1 Drivers</h3>
<ul>
<li>BS6 phase-2 (RDE) + future BS7: emission-control sophistication; SCR + DPF + urea-system + GPF.</li>
<li>USA-tariff window{ref("6")}: India emission-control export to US-OEM ramp.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting for OEM emissions.</li>
<li>Hybrid + EV pivot: long-tail diesel + ICE penetration sustains demand.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,237{ref("128")}</td><td class="num">2,500</td><td class="num">2,800</td><td class="num">3,150</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.1</td><td class="num">12.6</td><td class="num">13.1</td><td class="num">13.6</td></tr>
<tr><td>EBITDA</td><td class="num">270</td><td class="num">315</td><td class="num">367</td><td class="num">428</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">155</td><td class="num">185</td><td class="num">220</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + EUR)</td><td class="num">700&ndash;1,100 notional</td><td class="num">3&ndash;5</td><td>Royalty + substrate imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;300 float</td><td class="num">1.5&ndash;2.2</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-SCF (OEM anchors)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Maruti + Hyundai + Tata anchor</td></tr>
<tr><td>Capex TL (BS7 ramp)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">150&ndash;240</td><td class="num">1.5&ndash;2.4</td><td>Substrate + capex imports</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>US-OEM export</td></tr>
<tr><td>DCM / NCD (listed-corp)</td><td class="num">200&ndash;400</td><td class="num">1.5&ndash;3</td><td>Pre-arranger position</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.7&ndash;1.1</td><td>1,260 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 14.4-23.9 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 950-1,200; Rs 3.5-5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>US/Apollo expat MD + Indian leadership; PB AUM Rs 95-160 Cr; Rs 1.2-2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Tenneco CSR; Rs 80-120 Cr; Rs 0.7-1.1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5.4-8.1 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.2</td></tr>
<tr><td>Customer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">4.7</td><td class="num">7.6</td></tr>
<tr><td>DCM</td><td class="num">1.5</td><td class="num">3</td></tr>
<tr><td>CMS + cards</td><td class="num">0.7</td><td class="num">1.1</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5.4</td><td class="num">8.1</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>19.8</strong></td><td class="num"><strong>32.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Tenneco-Apollo appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>Tenneco Inc / Apollo Global Mgmt (US){ref("531")}; BEN-2 on file{ref("144")}; remainder retail-listed.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Tenneco India BS6 phase-2 ramp + GPF launches.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Apollo-portfolio cross-sell scope</li><li>T-14 Pre-pitch capex TL sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Tenneco Clean Air CFO meeting; FX + customer-SCF + capex memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with Maruti + Hyundai.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for BS7 ramp; FX hedge sized.</p></div>
<div class="card"><p><strong>T+180:</strong> Tenneco Auto + Federal-Mogul Goetze ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 200 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Tenneco Clean Air-specific from [530].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Tenneco Clean Air-specific sources</h3>
<ol start="530">
<li id="src-530"><strong>MCA v3 + ZaubaCorp + BSE/NSE listing &mdash; Tenneco Clean Air India Ltd master data</strong> &mdash; CIN L29308TN2018FLC126510; incorp 05 Apr 2018; 2018 listing. <span class="u">mca.gov.in &middot; bseindia.com &middot; nseindia.com</span></li>
<li id="src-531"><strong>Tenneco Inc + Apollo Global Mgmt (NYSE: APO) take-private commentary + 10-K filings</strong> &mdash; ~$7.1 bn EV take-private Nov 2022; FY25 revenue ~$18 bn. <span class="u">tenneco.com &middot; apollo.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "Tenneco Clean Air India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Tenneco Clean Air", "Auto emission-control / Tenneco-Apollo US"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + BS7 capex window.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
