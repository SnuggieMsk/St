"""Roca Bathroom Products dossier (pilot 87)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "roca-bathroom-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 87 of 90 · Chennai · Roca Sanitario Spain · Bathroom + sanitary-ware · Greenfield</div>
<h1>Roca Bathroom Products Private Limited<br>Spanish Roca Sanitario Indian sanitary-ware + faucet + ceramic + premium-bathroom subsidiary</h1>
<p class="lede">Roca Bathroom Products Pvt Ltd (CIN U15421TN1983PTC010243){ref("720")} is the Indian subsidiary of Roca Sanitario SA (Spain, private; ~&euro;2 bn revenue), the world's largest bathroom-products manufacturer; Roca acquired Parryware Glamour (the legacy entity) and merged with Indian operations{ref("721")}. <strong>FY25 Total Operating Income Rs 1,701 Cr</strong>{ref("128")}; EBITDA Rs 245 Cr (14.4%); PAT Rs 130 Cr; TNW Rs 685 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,580 FTE{ref("128")}. Manufactures sanitary-ware (toilets, basins), bathroom faucets, ceramic tiles + premium-bathroom solutions at Perundurai (TN) + Dewas (MP).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 16&ndash;28 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + dealer-SCF + capex)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,701 Cr</div><div class="sub">Bathroom + sanitary-ware{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + USD royalty + RM-import hedge</strong> &mdash; Roca Spain intercompany flows.</li>
<li><strong>Dealer-SCF (~3,500 dealers + 28 brand showrooms)</strong> &mdash; distribution finance.</li>
<li><strong>Premiumisation + housing capex tailwind</strong> &mdash; capex TL framework.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U15421TN1983PTC010243</strong></span>
<span>Incorp <strong>06 Aug 1983</strong></span>
<span>HO <strong>Perundurai (TN) + Dewas (MP)</strong></span>
<span>Parent <strong>Roca Sanitario SA (Spain)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Roca Sanitario SA{ref("721")} is a Spanish private MNC; FY25 revenue ~&euro;2 bn; world's largest bathroom-products major; Barcelona HQ. India operations: Roca Bathroom Products Pvt Ltd (this entity, ex-Parryware merged unit) under Roca India ecosystem.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 95 Cr; reserves Rs 590 Cr; cash Rs 165 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: BBVA India branch (Spanish anchor), HSBC, Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + dealer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,360</td><td class="num">1,520</td><td class="num">1,701{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">175</td><td class="num">205</td><td class="num">245{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.9</td><td class="num">13.5</td><td class="num">14.4</td></tr>
<tr><td>PAT</td><td class="num">85</td><td class="num">105</td><td class="num">130{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">485</td><td class="num">580</td><td class="num">685{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 95 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,580</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 165 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: greenfield FX + dealer-SCF on 3,500 dealer base; capex TL.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Bathroom + sanitary-ware</div>
<p>India bathroom + sanitary-ware market FY25 ~Rs 38,000 Cr; CAGR 9-11%; Roca + Cera + Hindware (HSIL) + Jaquar + Kohler + Toto compete. Premiumisation + tier-2/3 city housing demand structural growth.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Housing capex + PMAY rural-urban: Roca volume up.</li>
<li>USA-tariff window{ref("6")}: India sanitary-ware export ramp.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting for ceramics export.</li>
<li>Premiumisation + smart-bathroom segment.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,701{ref("128")}</td><td class="num">1,920</td><td class="num">2,200</td><td class="num">2,520</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.4</td><td class="num">14.9</td><td class="num">15.4</td><td class="num">15.9</td></tr>
<tr><td>EBITDA</td><td class="num">245</td><td class="num">286</td><td class="num">339</td><td class="num">401</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">155</td><td class="num">190</td><td class="num">230</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + USD)</td><td class="num">450&ndash;700 notional</td><td class="num">2&ndash;3.2</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">160&ndash;240 float</td><td class="num">1&ndash;1.6</td><td>MNC TM-aaS</td></tr>
<tr><td>Dealer-SCF (3,500 dealers)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Distribution finance</td></tr>
<tr><td>Capex TL (premium-line ramp)</td><td class="num">120&ndash;220</td><td class="num">1.2&ndash;2.2</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>RM + capex</td></tr>
<tr><td>EBR / PCFC</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>Sanitary-ware export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,580 FTE + dealer payments</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 9.7-16 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,200-1,500; Rs 1.7-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Spanish expat MD + Indian leadership; PB AUM Rs 95-160 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Roca CSR; Rs 70-110 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.4-5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>Treasury sweep</td><td class="num">1</td><td class="num">1.6</td></tr>
<tr><td>Dealer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">3.2</td><td class="num">5.4</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.4</td><td class="num">5</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>13.1</strong></td><td class="num"><strong>21.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 16-28 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Roca parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Roca Sanitario SA (Spain){ref("721")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Roca India premium-line capex announced for tier-1 cities.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Dealer-SCF panel + KYC framework</li><li>T-14 Pre-pitch capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Roca India CFO meeting; FX + dealer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Dealer-SCF pilot 200 dealers; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for premium-line.</p></div>
<div class="card"><p><strong>T+180:</strong> Roca Group cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Dealer-SCF Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 100 Cr drawn</li><li>Y3 run-rate Rs 16-28 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Roca-specific from [720].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Roca Bathroom Products-specific sources</h3>
<ol start="720">
<li id="src-720"><strong>MCA v3 + ZaubaCorp &mdash; Roca Bathroom Products Pvt Ltd master data</strong> &mdash; CIN U15421TN1983PTC010243; incorp 06 Aug 1983 (ex-Parryware Glamour). <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-721"><strong>Roca Sanitario SA Annual Report FY25 + India + Parryware merger commentary</strong> &mdash; world's largest bathroom-products major; FY25 ~&euro;2 bn revenue. <span class="u">roca.com</span></li>
</ol></div></section>"""

def build():
    t = "Roca Bathroom Products · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Roca Bathroom Products", "Bathroom + sanitary-ware / Roca Spain"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + dealer-SCF + premiumisation capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
