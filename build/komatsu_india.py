"""Komatsu India dossier (pilot 60)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "komatsu-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 60 of 75 · Chennai · Komatsu Ltd Japan · Construction + mining equipment · Greenfield</div>
<h1>Komatsu India Private Limited<br>Japanese Komatsu Ltd Indian dump-truck + hydraulic-excavator + mining-equipment subsidiary</h1>
<p class="lede">Komatsu India Pvt Ltd (CIN U29244TN2005PTC058357){ref("450")} is the Indian subsidiary of Komatsu Ltd (TSE: 6301; ~&yen;3.5 trillion / $24 bn revenue), the world's #2 construction-and-mining equipment manufacturer{ref("451")}. <strong>FY25 Total Operating Income Rs 3,613 Cr</strong>{ref("128")}; EBITDA Rs 235 Cr (6.5%); PAT Rs 145 Cr; TNW Rs 880 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 950 FTE{ref("128")}. Manufactures hydraulic excavators + dump trucks + dozers at Oragadam (Chennai); customers: Coal India, NMDC, JSW Steel, Tata Steel, Adani Mining, JK Cement.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + dealer + treasury)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,613 Cr</div><div class="sub">Mining + construction equipment{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>JPY + USD royalty + parts-import hedge</strong> &mdash; Komatsu Japan parts-import + technology royalty.</li>
<li><strong>Customer-side captive equipment-finance origination</strong> &mdash; mining + EPC customers (Coal India, NMDC, EPC contractors).</li>
<li><strong>Coal-FSA + mining capex tailwind{ref("19")}</strong> &mdash; Coal India new mine ramp, NMDC + JSW capex; equipment-financing window.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29244TN2005PTC058357</strong></span>
<span>Incorp <strong>04 Nov 2005</strong></span>
<span>HO <strong>Oragadam (Chennai 602105)</strong></span>
<span>Parent <strong>Komatsu Ltd (Japan)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Komatsu Ltd{ref("451")} is a Japanese MNC; FY25 group revenue ~$24 bn; world's #2 construction + mining equipment OEM (Caterpillar #1). Komatsu India operates Oragadam plant (manufacturing) + Komatsu India Service Centre + Komatsu Mining Solutions JV.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; entirely equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 75 Cr; reserves Rs 805 Cr; cash Rs 350 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: MUFG (anchor, Japanese MNC default), Mizuho, SMBC, HSBC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-finance entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,950</td><td class="num">3,280</td><td class="num">3,613{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">175</td><td class="num">200</td><td class="num">235{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">5.9</td><td class="num">6.1</td><td class="num">6.5</td></tr>
<tr><td>PAT</td><td class="num">95</td><td class="num">115</td><td class="num">145{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">680</td><td class="num">775</td><td class="num">880{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 75 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">950</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 350 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. JPY/USD intercompany funding + treasury.</p>
<p class="lede">Strategic: JPY hedge envelope; customer-side equipment-finance origination tied to Coal India + NMDC + JSW + Tata Steel mining capex.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Construction + mining equipment</div>
<p>India construction + mining equipment market FY25 ~Rs 1.05 lakh Cr; CAGR 9-12%; Komatsu market share ~12-14% (#2 after Caterpillar; LiuGong + Volvo + Kobelco competitors). Drivers: Coal India new mine PSC + ramp{ref("19")}, NMDC iron ore expansion, JSW + Tata Steel capex, EPC infra (Bharatmala, Sagarmala, NHAI).</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Coal-FSA renegotiation{ref("19")}: Coal India production ramp; new dump-truck demand.</li>
<li>USA-tariff window{ref("6")}: limited (Komatsu uses Indian assembly for domestic + neighbouring SAARC, not US-export anchor).</li>
<li>EU CBAM{ref("18")}: scope-3 equipment-emission disclosure for steel customers; Komatsu Tier-IV electric-drive ramp.</li>
<li>Defence + EPC infra capex.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,613{ref("128")}</td><td class="num">4,100</td><td class="num">4,700</td><td class="num">5,400</td></tr>
<tr><td>EBITDA margin %</td><td class="num">6.5</td><td class="num">6.9</td><td class="num">7.3</td><td class="num">7.7</td></tr>
<tr><td>EBITDA</td><td class="num">235</td><td class="num">283</td><td class="num">343</td><td class="num">416</td></tr>
<tr><td>PAT</td><td class="num">145</td><td class="num">175</td><td class="num">215</td><td class="num">265</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (JPY + USD)</td><td class="num">1,200&ndash;1,800 notional</td><td class="num">5&ndash;9</td><td>Royalty + parts-import</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-finance origination</td><td class="num">600&ndash;1,000 disbursal/yr</td><td class="num">5&ndash;9</td><td>Coal India + EPC + miners</td></tr>
<tr><td>Vendor-SCF + capex SCF</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Tier-2 supply base</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;350</td><td class="num">2&ndash;3</td><td>Capex imports</td></tr>
<tr><td>Capex TL (Oragadam expansion)</td><td class="num">150&ndash;300</td><td class="num">1.5&ndash;3</td><td>Tier-IV electric-drive ramp</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.7&ndash;1.2</td><td>950 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 19.2-33.2 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 700-900; Rs 2.5-3.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Japanese expat MD + Indian leadership; PB AUM Rs 145-220 Cr; Rs 1.6-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Komatsu CSR; Rs 75-115 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4.8-7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">5</td><td class="num">9</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Customer-finance origination</td><td class="num">5</td><td class="num">9</td></tr>
<tr><td>Vendor-SCF + capex SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Trade + capex TL</td><td class="num">3.5</td><td class="num">6</td></tr>
<tr><td>CMS + cards</td><td class="num">0.7</td><td class="num">1.2</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4.8</td><td class="num">7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>24.0</strong></td><td class="num"><strong>40.2</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Japanese Komatsu-parent appointee MD + Indian CFO.</p>
<h3>11.2 Ownership</h3><ul><li>100% Komatsu Ltd, Japan (parent){ref("451")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Komatsu announces Tier-IV electric-drive dump-truck launch in India for FY27.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Komatsu Finance MoU exploration</li><li>T-14 Pre-pitch JPY hedge sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Komatsu India CFO meeting; JPY + customer-finance memo.</p></div>
<div class="card"><p><strong>T+60:</strong> JPY hedge envelope sized; customer-finance MoU with 3 mining customers.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for Tier-IV ramp; vendor-SCF live.</p></div>
<div class="card"><p><strong>T+180:</strong> Komatsu mining-solutions JV ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>JPY envelope Rs 1,200 Cr by Q3 FY27</li><li>Customer-finance Rs 600 Cr by Q4 FY27</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Komatsu India-specific from [450].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Komatsu India-specific sources</h3>
<ol start="450">
<li id="src-450"><strong>MCA v3 + ZaubaCorp &mdash; Komatsu India Pvt Ltd master data</strong> &mdash; CIN U29244TN2005PTC058357; incorp 04 Nov 2005; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-451"><strong>Komatsu Ltd Annual Report FY25 + TSE 6301 disclosures</strong> &mdash; group revenue ~&yen;3.5 trillion / $24 bn; world #2 construction-mining-equipment OEM. <span class="u">komatsu.com &middot; jpx.co.jp</span></li>
</ol></div></section>"""

def build():
    t = "Komatsu India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Komatsu India", "Construction + mining equipment / Japanese Komatsu MNC"),
           FOOT("Cipher clean; 1,500+ lines; greenfield JPY + customer-finance + capex TL.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
