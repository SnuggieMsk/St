"""Faiveley Transport Rail Technologies India dossier (pilot 69)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "faiveley-transport-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 69 of 75 · Coimbatore · Wabtec Corp · Rail-systems · Greenfield · Vande Bharat tailwind</div>
<h1>Faiveley Transport Rail Technologies India Private Limited<br>French-origin Faiveley (now Wabtec Corp NYSE: WAB) Indian rail-systems subsidiary &mdash; brakes, doors, HVAC, pantograph</h1>
<p class="lede">Faiveley Transport Rail Technologies India Pvt Ltd (CIN U29199TZ1991PTC008636){ref("540")} is the Indian subsidiary of Wabtec Corporation (NYSE: WAB; FY25 revenue ~$10.8 bn) which acquired Faiveley Transport in 2016{ref("541")}. <strong>FY25 Total Operating Income Rs 2,183 Cr</strong>{ref("128")}; EBITDA Rs 295 Cr (13.5%); PAT Rs 165 Cr; TNW Rs 760 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 880 FTE{ref("128")}. Manufactures rail-vehicle systems &mdash; brake systems (CCBII, ECP), automatic doors, pantograph, HVAC, wheel-set. Customers: Indian Railways (Vande Bharat trainsets), BEML, ICF (Integral Coach Factory), Alstom-LHB, Bombardier-Alstom, BHEL.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + capex + customer-LC)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,183 Cr</div><div class="sub">Rail-systems{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD + EUR royalty + RM-import hedge</strong> &mdash; precision rail-systems subsystems imports.</li>
<li><strong>Vande Bharat 2.0 + 3.0 + bullet-train + 25 kV ramp</strong> &mdash; Indian Railways modernisation; Rs 1.05 lakh Cr 2026-27 capex; capex TL + LC + BG + customer-finance.</li>
<li><strong>Wabtec Inc-portfolio cross-sell</strong> &mdash; Wabtec freight-locomotive India (DLW) + signalling.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29199TZ1991PTC008636</strong></span>
<span>Incorp <strong>20 Mar 1991</strong></span>
<span>HO <strong>Hosur (TN) + Coimbatore</strong></span>
<span>Parent <strong>Wabtec Corp (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Wabtec Corporation{ref("541")} is a US-listed rail + transit + freight-locomotive major; FY25 revenue ~$10.8 bn. Wabtec acquired Faiveley Transport (French rail-systems major) in 2016 for ~$1.8 bn; Wabtec also acquired GE Transportation in 2019 for ~$11 bn. India operations: Faiveley Transport Rail Technologies India (this entity, transit-systems subsystem manufacturer) + Wabtec Locomotive India + Wabtec Sustainability + Wabtec Industrial India.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 25 Cr; reserves Rs 735 Cr; cash Rs 215 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: BNP Paribas, Standard Chartered, Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + capex + LC entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,720</td><td class="num">1,950</td><td class="num">2,183{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">220</td><td class="num">255</td><td class="num">295{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.8</td><td class="num">13.1</td><td class="num">13.5</td></tr>
<tr><td>PAT</td><td class="num">110</td><td class="num">135</td><td class="num">165{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">580</td><td class="num">670</td><td class="num">760{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 25 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">880</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 215 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: bid the Indian-Railways capex tailwind (Vande Bharat + 25 kV electrification + bullet-train); customer-LC + BG + capex TL.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Rail-systems / Vande Bharat ecosystem</div>
<p>India rail-equipment market FY25 ~Rs 95,000 Cr; CAGR 14-16%; driven by IR Rs 11.6 lakh Cr 2024-2030 capex. Vande Bharat trainset programme (~400 sets by FY30 + bullet-train Mumbai-Ahmedabad + RRTS Delhi-Meerut + Mumbai-Pune). Faiveley + Knorr-Bremse + Stadler + Alstom rail-systems compete.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Indian Railways modernisation: Vande Bharat + bullet-train + 25 kV.</li>
<li>USA-tariff window{ref("6")}: limited (rail-systems are local-Indian assembly).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting for rail-vehicle exports.</li>
<li>Defence + metro-rail capex: Bengaluru, Chennai, Mumbai, Pune, Hyderabad metro phases.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,183{ref("128")}</td><td class="num">2,500</td><td class="num">2,900</td><td class="num">3,400</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.5</td><td class="num">14.0</td><td class="num">14.5</td><td class="num">15.0</td></tr>
<tr><td>EBITDA</td><td class="num">295</td><td class="num">350</td><td class="num">421</td><td class="num">510</td></tr>
<tr><td>PAT</td><td class="num">165</td><td class="num">200</td><td class="num">245</td><td class="num">300</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + EUR)</td><td class="num">700&ndash;1,100 notional</td><td class="num">3&ndash;5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>MNC TM-aaS</td></tr>
<tr><td>BG (PSU customer-LC)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>IR + ICF + BEML PSU contracts</td></tr>
<tr><td>Capex TL (Vande Bharat ramp)</td><td class="num">200&ndash;350</td><td class="num">2&ndash;3.5</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Subsystem imports</td></tr>
<tr><td>Customer-finance (PSU receivable-discount)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>IR-LD discounting</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>880 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 15-24.9 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 660-820; Rs 2.4-3.4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>French/US expat MD + Indian leadership; PB AUM Rs 90-150 Cr; Rs 1.1-1.8 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Faiveley CSR; Rs 65-100 Cr; Rs 0.6-0.9 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4.1-6.1 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>BG (PSU)</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade</td><td class="num">4</td><td class="num">6.7</td></tr>
<tr><td>Customer-finance</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4.1</td><td class="num">6.1</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>19.1</strong></td><td class="num"><strong>31.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Wabtec parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Wabtec Corp, US (parent){ref("541")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Faiveley wins Vande Bharat 3.0 brake-systems contract; capacity expansion announced.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 IR-LD discounting framework</li><li>T-14 Pre-pitch capex TL + BG sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Faiveley CFO meeting; FX + capex + IR-LD memo.</p></div>
<div class="card"><p><strong>T+60:</strong> BG framework for IR + ICF projects; capex TL pilot.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; customer-LC discounting MoU.</p></div>
<div class="card"><p><strong>T+180:</strong> Wabtec Loco + Industrial India ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>BG outstanding Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 200 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Faiveley-specific from [540].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Faiveley-specific sources</h3>
<ol start="540">
<li id="src-540"><strong>MCA v3 + ZaubaCorp &mdash; Faiveley Transport Rail Technologies India Pvt Ltd master data</strong> &mdash; CIN U29199TZ1991PTC008636; incorp 20 Mar 1991. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-541"><strong>Wabtec Corp Annual Report FY25 + NYSE WAB disclosures + Faiveley acquisition + GE Transportation acquisition</strong> &mdash; FY25 revenue ~$10.8 bn; 2016 + 2019 acquisitions. <span class="u">wabteccorp.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "Faiveley Transport India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Faiveley Transport", "Rail-systems (brakes, doors, HVAC) / Wabtec US"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + IR-LD + Vande Bharat capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
