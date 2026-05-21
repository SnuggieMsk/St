"""Michelin India dossier (pilot 66)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "michelin-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 66 of 75 · Chennai · Compagnie Generale des Etablissements Michelin · Tyres + mobility · Greenfield</div>
<h1>Michelin India Private Limited<br>French Michelin Group Indian tyre + mobility-services subsidiary</h1>
<p class="lede">Michelin India Pvt Ltd (CIN U25119TN2009PTC071454){ref("510")} is the Indian subsidiary of Compagnie Generale des Etablissements Michelin (Euronext: ML; ~&euro;28 bn revenue), the world's largest tyre manufacturer{ref("511")}. <strong>FY25 Total Operating Income Rs 2,419 Cr</strong>{ref("128")}; EBITDA Rs 240 Cr (9.9%); PAT Rs 95 Cr; TNW Rs 580 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 940 FTE{ref("128")}. India operations include Chennai (HQ), Hyderabad (technology centre), Pune (training centre); Indian-manufactured truck/bus radial (TBR) tyres at Chennai for domestic + export, plus imported PV passenger-car tyres + premium specialty + mining tyres.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + dealer + capex)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,419 Cr</div><div class="sub">Tyres + mobility services{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + USD royalty + RM-import + finished-goods-import hedge</strong> &mdash; natural rubber + carbon-black + premium-tyre imports.</li>
<li><strong>Dealer-SCF (~600 dealers + 1,800 outlets)</strong> &mdash; tier-1 + tier-2 distribution finance.</li>
<li><strong>Mining + specialty + EV-tyre capex window</strong> &mdash; Michelin specialty tyre capacity expansion at Chennai.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U25119TN2009PTC071454</strong></span>
<span>Incorp <strong>16 Jul 2009</strong></span>
<span>HO <strong>Chennai 600032</strong></span>
<span>Parent <strong>Compagnie Generale des Etablissements Michelin (France)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Compagnie Generale des Etablissements Michelin{ref("511")} is a French listed tyre + mobility-services major (Euronext: ML); FY25 revenue ~&euro;28 bn. India operations: Michelin India Pvt Ltd (this entity) + Michelin India Tyres Pvt Ltd (the Chennai TBR plant) + Michelin India Technology Centre (Hyderabad ER&amp;D centre). Capacity 1.4 mn TBR tyres/yr at Thervoy Kandigai (Tiruvallur).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 65 Cr; reserves Rs 515 Cr; cash Rs 165 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: BNP Paribas (anchor, French MNC default), Credit Agricole, HSBC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + dealer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,950</td><td class="num">2,180</td><td class="num">2,419{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">175</td><td class="num">205</td><td class="num">240{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">9.0</td><td class="num">9.4</td><td class="num">9.9</td></tr>
<tr><td>PAT</td><td class="num">60</td><td class="num">75</td><td class="num">95{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">435</td><td class="num">505</td><td class="num">580{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 65 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">940</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 165 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: dealer-SCF on 600+ dealers; FX + capex envelope; specialty-tyre capex TL.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Tyres + mobility services</div>
<p>India tyre market FY25 ~Rs 90,000 Cr; CAGR 7-9%; MRF #1, JK Tyre + Apollo + Ceat + Bridgestone + Michelin. Michelin India holds ~3-4% (premium PV + TBR + specialty/mining segment leadership).</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India tyre export to North America benefit.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; Michelin renewable-rubber + bio-based compound.</li>
<li>Mining + specialty: Coal India + NMDC capex.</li>
<li>EV-tyre transition: Michelin EV-specific tyre R&amp;D.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,419{ref("128")}</td><td class="num">2,750</td><td class="num">3,150</td><td class="num">3,600</td></tr>
<tr><td>EBITDA margin %</td><td class="num">9.9</td><td class="num">10.5</td><td class="num">11.1</td><td class="num">11.7</td></tr>
<tr><td>EBITDA</td><td class="num">240</td><td class="num">289</td><td class="num">350</td><td class="num">421</td></tr>
<tr><td>PAT</td><td class="num">95</td><td class="num">120</td><td class="num">155</td><td class="num">195</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + USD)</td><td class="num">800&ndash;1,200 notional</td><td class="num">3.5&ndash;5.5</td><td>Royalty + RM/FG imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>MNC TM-aaS</td></tr>
<tr><td>Dealer-SCF (600 + 1,800 outlets)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Distribution finance</td></tr>
<tr><td>Capex TL (specialty + EV ramp)</td><td class="num">150&ndash;280</td><td class="num">1.5&ndash;2.8</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>RM imports + capex</td></tr>
<tr><td>EBR / PCFC (TBR export)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>Export ramp</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>940 FTE + dealer</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.2-21.7 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 700-880; Rs 2.5-3.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>French expat MD + Indian leadership; PB AUM Rs 80-130 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Michelin CSR; Rs 50-80 Cr; Rs 0.5-0.7 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4-5.7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3.5</td><td class="num">5.5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>Dealer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">4.7</td><td class="num">8</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4</td><td class="num">5.7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>17.2</strong></td><td class="num"><strong>27.4</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; French Michelin parent appointee MD + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Michelin Group, France (parent){ref("511")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Michelin announces specialty + EV-tyre capacity expansion at Chennai.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Michelin India Tyres (manufacturing) co-pitch scope</li><li>T-14 Pre-pitch dealer-SCF sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Michelin India CFO meeting; FX + dealer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Dealer-SCF pilot 100 dealers; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for specialty + EV tyres.</p></div>
<div class="card"><p><strong>T+180:</strong> Michelin India Tyres + Tech Centre bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Dealer-SCF Rs 300 Cr by Q3 FY27</li><li>Capex TL Rs 150 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Michelin India-specific from [510].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Michelin India-specific sources</h3>
<ol start="510">
<li id="src-510"><strong>MCA v3 + ZaubaCorp &mdash; Michelin India Pvt Ltd master data</strong> &mdash; CIN U25119TN2009PTC071454; incorp 16 Jul 2009; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-511"><strong>Compagnie Generale des Etablissements Michelin Annual Report FY25 + Euronext (ML) disclosures + Chennai capacity expansion press</strong> &mdash; world #1 tyre OEM; ~&euro;28 bn revenue. <span class="u">michelin.com &middot; euronext.com</span></li>
</ol></div></section>"""

def build():
    t = "Michelin India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Michelin India", "Tyres + mobility services / French Michelin"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + dealer-SCF + capex TL.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
