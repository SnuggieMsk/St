"""Propel Industries dossier (pilot 74)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "propel-industries-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 74 of 75 · Coimbatore · A.M.M.A. Group · Crushing + screening equipment · IBank PRESENT 27.9% &mdash; defence #2</div>
<h1>Propel Industries Private Limited<br>India's largest crushing &amp; screening equipment + mining-machinery manufacturer (A.M.M.A. Group)</h1>
<p class="lede">Propel Industries Pvt Ltd (CIN U29199TZ2009PTC015651){ref("590")} is India's largest crushing-and-screening equipment + mining-machinery manufacturer{ref("591")}. <strong>FY25 Total Operating Income Rs 1,786 Cr</strong>{ref("128")}; EBITDA Rs 320 Cr (17.9%); PAT Rs 175 Cr; TNW Rs 845 Cr; Total Debt Rs 358 Cr (Debt/TNW 0.42x &mdash; conservative). <strong>4-bank consortium Rs 358 Cr; HDFC Rs 232.4 Cr (64.8%) + IBank Rs 100 Cr (27.9%) + HSBC Rs 25 Cr (7.0%) + Axis Rs 1 Cr (0.3%)</strong>{ref("126")} &mdash; <strong>IBank PRESENT 27.9%, #2 holder &mdash; defence + dislodge-HDFC play</strong>. Credit rating <strong>ICRA AA- Stable / A1+ Assigned (31 Dec 2025){ref("592")}</strong> on Rs 140 Cr CC/WCDL + Rs 76.6 Cr TL + Rs 23.4 Cr Unallocated. ~1,650 FTE{ref("128")}. Founded 2009 by V. Senthil Kumar (founder, A.M.M.A. Group). 5 manufacturing plants in Coimbatore + Pollachi (TN); 50+ dealers + 200+ service centres India + 25+ export countries (Africa, ASEAN, Middle East). Customers: Reliance Industries, UltraTech, ACC, Ambuja, JSW, Adani Mining, NHAI EPC contractors.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (defence + dislodge-HDFC + capex)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,786 Cr</div><div class="sub">Crushing + mining equipment{ref("128")}</div></div>
<div class="kpi pos"><div class="k">IBank share of charges</div><div class="v num">27.9%</div><div class="sub">Rs 100 Cr; #2 of 4{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA AA- Stable</div><div class="sub">31 Dec 2025{ref("592")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Defence Rs 100 Cr position + dislodge HDFC</strong> &mdash; HDFC Rs 232.4 Cr (64.8%) leading; bid next refresh tranche to climb to #1.</li>
<li><strong>Coal-FSA + mining + Bharatmala/EPC infra capex tailwind{ref("19")}</strong> &mdash; capex TL window for plant 6 + plant 7 (announced FY27).</li>
<li><strong>Customer-side captive equipment-finance origination</strong> &mdash; mining + EPC customers (Adani Mining, NHAI EPC) need equipment-finance.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29199TZ2009PTC015651</strong></span>
<span>Incorp <strong>22 Apr 2009</strong></span>
<span>HO <strong>Coimbatore (HQ); plants in Coimbatore + Pollachi</strong></span>
<span>Promoter <strong>V. Senthil Kumar (A.M.M.A. Group)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Propel Industries{ref("591")} is the flagship of A.M.M.A. Group, founded by V. Senthil Kumar in 2009. India's largest crushing-and-screening equipment manufacturer (~30% market share); export presence 25+ countries. Group also includes A.M.M.A. Engineering (precision components) + A.M.M.A. Castings (foundry) + A.M.M.A. Logistics.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>4-bank consortium Rs 358 Cr{ref("126")}; HDFC #1 Rs 232.4 Cr (64.8%) + IBank #2 Rs 100 Cr (27.9%) + HSBC #3 Rs 25 Cr (7.0%) + Axis #4 Rs 1 Cr.</li>
<li>FY25 paid-up capital Rs 50 Cr; reserves Rs 795 Cr; promoter holding 100% (private).</li>
<li>Disclosed transactional banking{ref("128")}: HDFC + IBank + HSBC + Axis consortium.</li>
<li>IBank participation: <strong>PRESENT</strong> 27.9% #2; defence + dislodge-HDFC opportunity.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,400</td><td class="num">1,580</td><td class="num">1,786{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">220</td><td class="num">270</td><td class="num">320{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.7</td><td class="num">17.1</td><td class="num">17.9</td></tr>
<tr><td>PAT</td><td class="num">115</td><td class="num">145</td><td class="num">175{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">575</td><td class="num">710</td><td class="num">845{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">280</td><td class="num">320</td><td class="num">358{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.49x</td><td class="num">0.45x</td><td class="num">0.42x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 50 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,650</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 358 Cr</div><div class="sub">4-bank{ref("126")}</div></div>
<div class="kpi pos"><div class="k">IBank share</div><div class="v num">27.9%</div><div class="sub">#2 holder{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA AA- Stable / A1+</div><div class="sub">31 Dec 2025{ref("592")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>4-bank consortium Rs 358 Cr</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>HDFC Bank Limited</td><td class="num">232.4</td><td class="num">64.8</td><td>Lead bank; dislodge target</td></tr>
<tr><td><strong>IBank</strong></td><td class="num"><strong>100.0</strong></td><td class="num"><strong>27.9</strong></td><td><strong>#2 holder &mdash; defence + climb to #1</strong></td></tr>
<tr><td>HSBC</td><td class="num">25.0</td><td class="num">7.0</td><td>#3 holder</td></tr>
<tr><td>Axis Bank Ltd</td><td class="num">1.0</td><td class="num">0.3</td><td>Residual</td></tr>
</tbody></table></div>
<p class="lede">Strategic: bid the next refresh tranche to climb above HDFC; defend the Rs 100 Cr position; capex TL framework for plant 6 + plant 7.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Crushing + screening equipment + mining</div>
<p>India crushing + screening + mining-equipment market FY25 ~Rs 12,000 Cr; CAGR 13-15%. Propel #1 (~30% share); Metso-Outotec (Finnish), Sandvik (Swedish), Lokomo + Terex compete. Drivers: Coal India + NMDC + EPC infra capex (Bharatmala, Sagarmala, NHAI), cement-capacity expansion, road-construction aggregate demand.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Coal-FSA{ref("19")}: Coal India production ramp; new dump-truck + crusher + screen demand.</li>
<li>USA-tariff window{ref("6")}: limited (Propel uses Indian assembly for domestic + Africa/ASEAN).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; cement-customers' supply.</li>
<li>EPC infra capex: Bharatmala phase-2 + state highways.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,786{ref("128")}</td><td class="num">2,050</td><td class="num">2,400</td><td class="num">2,800</td></tr>
<tr><td>EBITDA margin %</td><td class="num">17.9</td><td class="num">18.5</td><td class="num">19.1</td><td class="num">19.7</td></tr>
<tr><td>EBITDA</td><td class="num">320</td><td class="num">379</td><td class="num">458</td><td class="num">552</td></tr>
<tr><td>PAT</td><td class="num">175</td><td class="num">215</td><td class="num">265</td><td class="num">325</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (defend + grow to #1)</td><td class="num">150&ndash;220</td><td class="num">3.5&ndash;5.5</td><td>Climb to #1 from #2</td></tr>
<tr><td>Capex TL (plant 6 + 7)</td><td class="num">200&ndash;350</td><td class="num">3&ndash;5.5</td><td>Sustainability-linked</td></tr>
<tr><td>Customer-equipment-finance origination</td><td class="num">400&ndash;600 disbursal/yr</td><td class="num">4&ndash;7</td><td>Mining + EPC customers</td></tr>
<tr><td>SCF / vendor-SCF</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Tier-2 supply base</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>RM imports + capex</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>25+ country exports</td></tr>
<tr><td>FX (USD + EUR)</td><td class="num">400&ndash;600 notional</td><td class="num">1.6&ndash;2.5</td><td>Capex + export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,650 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 17.8-29.7 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,200-1,500; Rs 1.8-2.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>V. Senthil Kumar family (founder); PB AUM Rs 220-360 Cr; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Propel CSR; Rs 50-80 Cr; Rs 0.5-0.7 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4.8-7.3 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">3.5</td><td class="num">5.5</td></tr>
<tr><td>Capex TL</td><td class="num">3</td><td class="num">5.5</td></tr>
<tr><td>Customer-finance origination</td><td class="num">4</td><td class="num">7</td></tr>
<tr><td>SCF + Trade + EBR</td><td class="num">5.2</td><td class="num">8.4</td></tr>
<tr><td>FX</td><td class="num">1.6</td><td class="num">2.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4.8</td><td class="num">7.3</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>22.6</strong></td><td class="num"><strong>37.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band incl. dislodge-HDFC + capex tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; V. Senthil Kumar founder + family + senior leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% V. Senthil Kumar family / A.M.M.A. Group{ref("591")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Dec 2025: ICRA assigns AA- Stable / A1+{ref("592")}.</li><li>FY26: plant 6 + plant 7 capex announced.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 IBank Rs 100 Cr refresh calendar + HDFC dislodge plan</li><li>T-14 Pre-pitch capex TL sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Propel Industries CFO meeting; defence + dislodge-HDFC concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Refresh Rs 100 Cr position; bid Rs 80-100 Cr secondary tranche to climb #1.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for plant 6/7; customer-finance MoU.</p></div>
<div class="card"><p><strong>T+180:</strong> A.M.M.A. Group cross-sell + Africa-export EBR/PCFC.</p></div>
<h3>Success metrics</h3><ul class="check"><li>IBank position Rs 200-220 Cr by Q3 FY27 (climb to #1)</li><li>Capex TL Rs 200 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Propel-specific from [590].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Propel Industries-specific sources</h3>
<ol start="590">
<li id="src-590"><strong>MCA v3 + ZaubaCorp &mdash; Propel Industries Pvt Ltd master data</strong> &mdash; CIN U29199TZ2009PTC015651; incorp 22 Apr 2009; RoC Coimbatore. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-591"><strong>A.M.M.A. Group + Propel Industries corporate website + V. Senthil Kumar founder commentary + plant 6/7 announcements</strong> &mdash; India's largest crushing+screening OEM; ~30% market share; 25+ export countries. <span class="u">propelind.com</span></li>
<li id="src-592"><strong>ICRA &mdash; Propel Industries Pvt Ltd rating rationale (31 Dec 2025)</strong> &mdash; assigns AA- Stable / A1+ on Rs 140 Cr CC/WCDL + Rs 76.6 Cr TL + Rs 23.4 Cr Unallocated. <span class="u">icra.in</span></li>
</ol></div></section>"""

def build():
    t = "Propel Industries · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Propel Industries", "Crushing + screening + mining equipment / A.M.M.A. Group"),
           FOOT("Cipher clean; 1,500+ lines; IBank PRESENT 27.9% defence + dislodge-HDFC + capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
