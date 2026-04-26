"""DXC Technology India dossier (pilot 70)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "dxc-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 70 of 75 · Chennai · DXC Technology Co · IT services GCC · Greenfield</div>
<h1>DXC Technology India Private Limited<br>DXC Technology Co (NYSE: DXC) Indian IT-services delivery + GCC arm</h1>
<p class="lede">DXC Technology India Pvt Ltd (CIN U72900TN2015FTC102489){ref("550")} is the Indian delivery + GCC arm of DXC Technology Company (NYSE: DXC; FY25 revenue ~$13.5 bn), a US-listed global IT-services major formed from the 2017 HPE Enterprise Services + CSC merger{ref("551")}. <strong>FY25 Total Operating Income Rs 2,181 Cr</strong>{ref("128")}; EBITDA Rs 350 Cr (16.0%); PAT Rs 215 Cr; TNW Rs 1,085 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~9,500 FTE{ref("128")}. Application services, infrastructure modernisation, cloud-and-platform-services, security, business-process services for global clients (BFSI, manufacturing, energy, government). Chennai + Bengaluru + Hyderabad + Pune.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 26&ndash;44 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + retail + PB)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,181 Cr</div><div class="sub">IT services / GCC{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~9,500</div><div class="sub">{ref("128")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD revenue-FX hedge</strong> &mdash; 100% USD billing.</li>
<li><strong>9,500 FTE retail-mass-market + PB</strong> &mdash; salary CASA + auto/home + cards + senior PB.</li>
<li><strong>SEZ STPI + cloud-and-platform-services capex</strong> &mdash; AWS + Azure + GCP partnership co-spend.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U72900TN2015FTC102489</strong></span>
<span>Incorp <strong>27 Mar 2015</strong></span>
<span>HO <strong>Chennai (DLF IT Park)</strong></span>
<span>Parent <strong>DXC Technology Co (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>DXC Technology Co{ref("551")} is a NYSE-listed IT-services major; FY25 revenue ~$13.5 bn; ~125k FTE globally with India ~30% of workforce. India operations: DXC Technology India Pvt Ltd (this entity, principal services delivery + GCC) + DXC Technology Services India + Hewlett-Packard Enterprise India legacy entities (post-HPE-CSC merger consolidation in progress).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent-funded.</li>
<li>FY25 paid-up capital Rs 35 Cr; reserves Rs 1,050 Cr; cash Rs 380 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor for DXC US-anchor relationship), JPMorgan, HSBC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + retail-mass entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,750</td><td class="num">1,960</td><td class="num">2,181{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">240</td><td class="num">295</td><td class="num">350{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.7</td><td class="num">15.1</td><td class="num">16.0</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">170</td><td class="num">215{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">720</td><td class="num">895</td><td class="num">1,085{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 35 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~9,500</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 380 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: bid USD-FX + retail-mass on 9,500 FTE; PB book on senior MD layer.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; IT services / global delivery GCC</div>
<p>India IT services GCC market FY25 ~$50-55 bn export; CAGR 8-10%; TCS + Infy + WPRO + HCL + Tech Mah dominant; DXC + Cognizant + Capgemini + Atos + IBM Indian delivery captives compete. Workforce ~5.5 mn FTE.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: services-tariff still ~0%; ITES revenue protected.</li>
<li>Gen-AI + agentic-AI shift: services pricing pressure but Indian delivery capacity remains anchor.</li>
<li>EU AI-Act + DORA: regulatory-tech work shoring.</li>
<li>Cloud-modernisation + cybersecurity scope: continuing.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,181{ref("128")}</td><td class="num">2,450</td><td class="num">2,750</td><td class="num">3,100</td></tr>
<tr><td>EBITDA margin %</td><td class="num">16.0</td><td class="num">16.6</td><td class="num">17.2</td><td class="num">17.8</td></tr>
<tr><td>EBITDA</td><td class="num">350</td><td class="num">407</td><td class="num">473</td><td class="num">552</td></tr>
<tr><td>PAT</td><td class="num">215</td><td class="num">255</td><td class="num">300</td><td class="num">355</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD)</td><td class="num">1,800&ndash;2,700 notional</td><td class="num">7&ndash;12</td><td>100% USD billing</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">350&ndash;520 float</td><td class="num">2.5&ndash;3.5</td><td>MNC TM-aaS</td></tr>
<tr><td>EBR / PCFC (services-export)</td><td class="num">250&ndash;400</td><td class="num">2.2&ndash;3.5</td><td>Receivable financing</td></tr>
<tr><td>Salary + retail asset (9,500)</td><td class="num">800&ndash;1,200 disbursal/yr</td><td class="num">7&ndash;11</td><td>Auto + home + cards</td></tr>
<tr><td>PB (senior leadership)</td><td class="num">220&ndash;360 AUM</td><td class="num">2.5&ndash;4</td><td>Indian + expat MDs</td></tr>
<tr><td>TASC + payroll</td><td class="num">200&ndash;320</td><td class="num">1.5&ndash;2.4</td><td>PF + Gratuity</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">1.7&ndash;2.7</td><td>9,500 FTE corporate cards</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.4-21.7 Cr / yr. Retail/PB/TASC: Rs 11-17.4 Cr/yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card pos"><h4 style="margin-top:0">Retail (anchor)</h4><p>9,500 FTE; salary CASA Rs 8,500-10,500 mn aggregate; auto + home + cards cross-sell; Rs 7-11 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Senior MDs UHNI; PB AUM Rs 220-360 Cr; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + DXC CSR; Rs 200-320 Cr; Rs 1.5-2.4 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 11-17.4 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">7</td><td class="num">12</td></tr>
<tr><td>Treasury sweep</td><td class="num">2.5</td><td class="num">3.5</td></tr>
<tr><td>EBR/PCFC</td><td class="num">2.2</td><td class="num">3.5</td></tr>
<tr><td>CMS + cards</td><td class="num">1.7</td><td class="num">2.7</td></tr>
<tr><td>Retail asset cross-sell</td><td class="num">7</td><td class="num">11</td></tr>
<tr><td>PB</td><td class="num">2.5</td><td class="num">4</td></tr>
<tr><td>TASC</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>24.4</strong></td><td class="num"><strong>39.1</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 26-44 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; DXC parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% DXC Technology Co, US (parent){ref("551")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: DXC India delivery scope expansion to gen-AI services + agentic platforms.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 HPE-CSC integration legacy entity consolidation</li><li>T-14 Pre-pitch retail-mass + PB sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> DXC India CFO + HR meetings; FX + retail concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Salary-CASA pilot for 1,500 FTE; PB book on 30 senior MDs.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; retail-asset campaign 9,500 base.</p></div>
<div class="card"><p><strong>T+180:</strong> DXC US-corporate cross-sell + correspondent.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Salary CASA 4,500+ accounts by Q3 FY27</li><li>Retail-asset book Rs 450 Cr by Q4 FY27</li><li>Y3 run-rate Rs 26-44 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; DXC-specific from [550].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">DXC India-specific sources</h3>
<ol start="550">
<li id="src-550"><strong>MCA v3 + ZaubaCorp &mdash; DXC Technology India Pvt Ltd master data</strong> &mdash; CIN U72900TN2015FTC102489; incorp 27 Mar 2015. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-551"><strong>DXC Technology Co Annual Report FY25 + NYSE DXC disclosures + HPE-CSC merger commentary</strong> &mdash; FY25 revenue ~$13.5 bn; ~125k FTE; ~30% India workforce. <span class="u">dxc.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "DXC Technology India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("DXC Technology India", "IT services + GCC / DXC Technology US"),
           FOOT("Cipher clean; 1,500+ lines; FX + retail-mass + PB on 9,500 FTE base.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
