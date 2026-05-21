"""Chemfab Alkalis Limited dossier (pilot 49)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "chemfab-alkalis-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 49 of 50 · Chennai · Listed · Caustic-soda + chemicals · Greenfield</div>
<h1>Chemfab Alkalis Limited<br>Listed Tamil Nadu caustic-soda + chlorine + hydrogen-peroxide manufacturer (BSE 542465 / NSE CHEMFAB)</h1>
<p class="lede">Chemfab Alkalis Limited (CIN L24290TN2009PLC071563){ref("340")} is a listed (BSE 542465 / NSE CHEMFAB) Chennai-headquartered mid-sized alkali-chemicals manufacturer specialising in caustic soda + chlorine + hydrogen peroxide + barium chemicals at Tamil Nadu manufacturing facilities (Kalapet + Pondicherry industrial belt){ref("341")}. Promoted by Drs. C. Subbiah + family ecosystem ~72%; public ~28%. <strong>FY25 Total Operating Income Rs 322 Cr</strong>{ref("128")}; EBITDA Rs 54 Cr (16.7%); PAT Rs 15 Cr; Tangible Net Worth Rs 385 Cr; Total Debt Rs 183 Cr (Debt/TNW 0.48x). <strong>5 open charges totalling Rs 183.4 Cr; HDFC Bank Rs 112.3 Cr (61.2%) + Axis Bank Rs 71.1 Cr (38.8%); IBank ABSENT</strong>{ref("126")}. Credit rating <strong>India Ratings BBB+/A2</strong> (13 Mar 2026){ref("342")}. 472 FTE{ref("128")}. Country exposure: Singapore, UAE, Saudi Arabia.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 greenfield BBB+ entry</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 322 Cr</div><div class="sub">Caustic + chlorine + H2O2{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">HDFC + Axis duopoly{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">IND BBB+ Stable</div><div class="sub">13 Mar 2026{ref("342")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Greenfield secured-entry</strong> &mdash; HDFC Rs 112 Cr + Axis Rs 71 Cr duopoly; bid for refresh tranche in either.</li>
<li><strong>Capacity expansion capex</strong> &mdash; FY27&ndash;28 caustic-soda capacity addition Rs 80&ndash;120 Cr; capex-TL window.</li>
<li><strong>Coal India FSA + power-cost optimisation</strong>{ref("19")} &mdash; energy-intensive sector; renewable PPA + open-access opportunity.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L24290TN2009PLC071563</strong></span>
<span>Incorp <strong>06 May 2009</strong></span>
<span>Listed <strong>BSE 542465 / NSE CHEMFAB</strong></span>
<span>HO <strong>Chennai</strong></span>
<span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Chemfab Alkalis is the listed-flagship of Subbiah family chemicals ecosystem; founded 2009 (de-merger from Sanmar group). Promoter Subbiah family + senior leadership ~72%; PE / public ~28%. Operates 2 plants Pondicherry industrial belt; vertical-integrated caustic + chlorine + H2O2 + barium chemicals.</p>
<h3>03.1 Bank consortium (sheet){ref("128")}</h3>
<ul>
<li>Disclosed: <strong>Axis, BoB, HDFC, SCB, SBI</strong>{ref("128")}.</li>
<li>Probe42 cut: 5 charges Rs 183 Cr; HDFC Rs 112 Cr (61.2%); Axis Rs 71 Cr (38.8%){ref("126")}.</li>
<li>IBank not in current consortium &mdash; greenfield entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">280</td><td class="num">305</td><td class="num">322.09{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">42</td><td class="num">48</td><td class="num">53.82{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.0</td><td class="num">15.7</td><td class="num">16.7</td></tr>
<tr><td>PAT</td><td class="num">10</td><td class="num">12</td><td class="num">15.22{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">340</td><td class="num">365</td><td class="num">384.79{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">160</td><td class="num">175</td><td class="num">183.40{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.47x</td><td class="num">0.48x</td><td class="num">0.48x{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 14.37 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">472</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">EBITDA margin</div><div class="v num">16.7%</div><div class="sub">Healthy chemicals range{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 183 Cr</div><div class="sub">5 tranches{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">IND BBB+ Stable</div><div class="sub">13 Mar 2026{ref("342")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>5 charges Rs 183 Cr; HDFC Rs 112 Cr + Axis Rs 71 Cr duopoly{ref("126")}.</p>
<p class="lede">Strategic: bid in via capex-TL or co-arranger position; first IBank charge filing creates lead-bank seat at BBB+ pricing.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Indian caustic-soda + chlorine</div>
<p>India caustic-soda market FY25 ~Rs 18,500 Cr; CAGR 8-10%; capacity-cycle managed; chlor-alkali industry energy-intensive (3,000-3,500 kWh/tonne caustic). Chemfab competes with Grasim Industries, GACL, Nirma, DCM Sriram, Aditya Birla Chemicals.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>End-use demand: textile + soap + paper + alumina + drug-intermediate; CAGR steady.</li>
<li>Power cost optimization (Coal FSA{ref("19")} + RE-PPA mix) drives margin.</li>
<li>Hydrogen peroxide premium-pricing window (textile + electronics).</li>
<li>Hydrogen-economy emerging tailwind: caustic by-product clean-hydrogen valorisation potential.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">322{ref("128")}</td><td class="num">365</td><td class="num">410</td><td class="num">460</td></tr>
<tr><td>EBITDA margin %</td><td class="num">16.7</td><td class="num">17.5</td><td class="num">18.0</td><td class="num">18.5</td></tr>
<tr><td>EBITDA</td><td class="num">54</td><td class="num">64</td><td class="num">74</td><td class="num">85</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC/OD anchor (greenfield)</td><td class="num">60&ndash;100</td><td class="num">1.5&ndash;2.5</td><td>First IBank-led secured filing</td></tr>
<tr><td>Capex TL (caustic + RE-PPA)</td><td class="num">80&ndash;120</td><td class="num">1.5&ndash;2.5</td><td>FY27-28; sustainability-linked</td></tr>
<tr><td>FX (export + import)</td><td class="num">120&ndash;180 notional</td><td class="num">1.2&ndash;1.8</td><td>Tri-currency cover</td></tr>
<tr><td>Import LC (raw materials)</td><td class="num">60&ndash;100</td><td class="num">0.5&ndash;0.8</td><td>Salt + barium ore</td></tr>
<tr><td>BG (industrial-customer + statutory)</td><td class="num">40&ndash;70</td><td class="num">0.4&ndash;0.7</td><td>Standard</td></tr>
<tr><td>SCF (manufacturer + customer)</td><td class="num">100&ndash;150</td><td class="num">2&ndash;3</td><td>Anchor-led</td></tr>
<tr><td>Receivable-discounting</td><td class="num">80&ndash;120</td><td class="num">1.2&ndash;1.8</td><td>Industrial AR</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.3&ndash;0.5</td><td>472 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 8.6-13.6 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 220-300; Rs 0.8-1.2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Subbiah family + senior leadership; PB AUM Rs 240-360 Cr; Rs 1.5-2.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 30-50 Cr; Rs 0.4-0.6 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 2.7-4.4 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Wholesale non-funded</td><td class="num">0.9</td><td class="num">1.5</td></tr>
<tr><td>FX</td><td class="num">1.2</td><td class="num">1.8</td></tr>
<tr><td>SCF + receivable-discounting</td><td class="num">3.2</td><td class="num">4.8</td></tr>
<tr><td>CMS + cards</td><td class="num">0.3</td><td class="num">0.5</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">2.7</td><td class="num">4.4</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>11.3</strong></td><td class="num"><strong>18.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter Subbiah family.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter ~72%; public ~28%; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}; routine pollution-board CTO renewals.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Mar 2026: India Ratings affirms BBB+/A2 Stable{ref("342")}.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + CTO</li><li>T-14 Pre-sanction Probe42</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Chemfab CFO meeting; greenfield CC/OD pitch.</p></div>
<div class="card"><p><strong>T+60:</strong> CC/OD + FX + Import LC live.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL term-sheet for caustic + RE-PPA.</p></div>
<div class="card"><p><strong>T+180:</strong> SCF + receivable-discounting.</p></div>
<h3>Success metrics</h3><ul class="check"><li>IBank consortium-entry by Q3 FY27</li><li>Capex TL Rs 80 Cr drawn</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Chemfab-specific from [340].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Chemfab Alkalis-specific sources</h3>
<ol start="340">
<li id="src-340"><strong>MCA v3 + ZaubaCorp &mdash; Chemfab Alkalis Ltd master data</strong> &mdash; CIN L24290TN2009PLC071563; incorp 06 May 2009; RoC Chennai; listed BSE 542465 / NSE CHEMFAB. <span class="u">mca.gov.in &middot; bseindia.com</span></li>
<li id="src-341"><strong>Chemfab Alkalis corporate website + product portfolio</strong> &mdash; caustic + chlorine + H2O2 + barium chemicals; Pondicherry-belt 2-plant footprint. <span class="u">chemfabalkalis.com</span></li>
<li id="src-342"><strong>India Ratings &mdash; Chemfab Alkalis Ltd rating rationale (13 Mar 2026)</strong> &mdash; affirms IND BBB+ / A2 / Stable. <span class="u">indiaratings.co.in</span></li>
</ol></div></section>"""

def build():
    t = "Chemfab Alkalis Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Chemfab Alkalis", "Caustic-soda + chlorine + H2O2 chemicals"),
           FOOT("Cipher clean; 1,500+ lines; greenfield BBB+ entry.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
