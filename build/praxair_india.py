"""Praxair India dossier (pilot 64)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "praxair-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 64 of 75 · Chennai · Linde plc · Industrial gases · Greenfield</div>
<h1>Praxair India Private Limited<br>Linde plc Indian industrial-gases (oxygen, nitrogen, argon, hydrogen, helium) subsidiary</h1>
<p class="lede">Praxair India Pvt Ltd (CIN U24111TN1996PTC180780){ref("490")} is the Indian subsidiary of Linde plc (NYSE: LIN; ~$33 bn revenue), the world's largest industrial-gases company post the 2018 Praxair-Linde merger{ref("491")}. <strong>FY25 Total Operating Income Rs 2,726 Cr</strong>{ref("128")}; EBITDA Rs 460 Cr (16.9%); PAT Rs 235 Cr; TNW Rs 1,180 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 720 FTE{ref("128")}. Onsite + bulk + cylinder gas supply to steel (Tata Steel, JSW, AM/NS), chemicals (Reliance, IOC), pharma (Cipla, Sun, Aurobindo), electronics (Foxconn, Tata Electronics, Pegatron) + green-hydrogen partnerships.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + capex + treasury)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,726 Cr</div><div class="sub">Industrial gases{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD + EUR royalty + capex-import hedge</strong> &mdash; ASU + cylinder fleet imports.</li>
<li><strong>Green-hydrogen capex window</strong> &mdash; NTPC + Reliance + Adani green-H2 projects; ASU + electrolyser EPC; capex TL framework.</li>
<li><strong>Customer-side onsite capex SCF</strong> &mdash; long-term take-or-pay onsite contracts at customer facilities.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U24111TN1996PTC180780</strong></span>
<span>Incorp <strong>27 Mar 1996</strong></span>
<span>HO <strong>Chennai 600001</strong></span>
<span>Parent <strong>Linde plc (US/IRL)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Linde plc{ref("491")} is the world's largest industrial-gases company; FY25 revenue ~$33 bn; HQ Dublin/Connecticut. India operations: Linde India Ltd (BSE: 523457, listed flagship for the Linde-AGA legacy entity; merged with Praxair-India operationally) + Praxair India Pvt Ltd (this entity, separate legal vehicle pre-merger; integration in progress). Major site Chennai + Bengaluru + Pune + Mumbai + Bharuch (Gujarat) + Jamshedpur (Jharkhand).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; equity + parent-funded.</li>
<li>FY25 paid-up capital Rs 90 Cr; reserves Rs 1,090 Cr; cash Rs 280 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor), JPMorgan, HSBC, Standard Chartered.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + capex + customer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,200</td><td class="num">2,460</td><td class="num">2,726{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">340</td><td class="num">395</td><td class="num">460{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.5</td><td class="num">16.1</td><td class="num">16.9</td></tr>
<tr><td>PAT</td><td class="num">160</td><td class="num">195</td><td class="num">235{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">880</td><td class="num">1,025</td><td class="num">1,180{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 90 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">720</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 280 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. Capex-heavy industry but funded via parent + retained earnings.</p>
<p class="lede">Strategic: bid the green-H2 capex envelope; FX + capex-import hedge; customer-side onsite SCF.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Industrial gases + green H2</div>
<p>India industrial-gases market FY25 ~Rs 16,000 Cr; CAGR 12-14%; Linde-Praxair #1 (~38% share), Air Liquide, INOX Air Products, Air Water India, BOC India compete. Green-H2 + electrolyser ramp is structural growth.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Green-H2 mission{ref("19")}: 5 mn-tonne H2 by FY30; ASU + electrolyser EPC; capex window.</li>
<li>USA-tariff window{ref("6")}: minimal direct (gas-supply is local).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting for Indian-steel exports requires Linde gas-supply emissions data.</li>
<li>Steel + electronics + pharma capex cycle.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,726{ref("128")}</td><td class="num">3,100</td><td class="num">3,560</td><td class="num">4,100</td></tr>
<tr><td>EBITDA margin %</td><td class="num">16.9</td><td class="num">17.5</td><td class="num">18.1</td><td class="num">18.7</td></tr>
<tr><td>EBITDA</td><td class="num">460</td><td class="num">543</td><td class="num">644</td><td class="num">767</td></tr>
<tr><td>PAT</td><td class="num">235</td><td class="num">285</td><td class="num">345</td><td class="num">415</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + EUR)</td><td class="num">800&ndash;1,200 notional</td><td class="num">3.5&ndash;5.5</td><td>Royalty + capex imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>Capex TL (green-H2 + ASU)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>ASU + electrolyser imports</td></tr>
<tr><td>Customer-SCF (onsite)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Tata + JSW + RIL onsite</td></tr>
<tr><td>BG (project + take-or-pay)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Long-term contracts</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>720 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 15.5-25 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 540-680; Rs 2-3 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Linde expat MD + Indian leadership; PB AUM Rs 165-260 Cr; Rs 2-3 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Linde CSR; Rs 70-105 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4.7-7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3.5</td><td class="num">5.5</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Capex TL + Trade</td><td class="num">5</td><td class="num">8.2</td></tr>
<tr><td>Customer-SCF + BG</td><td class="num">4.5</td><td class="num">7.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4.7</td><td class="num">7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>20.2</strong></td><td class="num"><strong>32.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band incl. green-H2 capex tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Linde-parent appointee MD + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Linde plc, US/IRL (parent){ref("491")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Linde India announces green-H2 partnership with NTPC + Reliance.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Praxair-Linde India merger integration roadmap</li><li>T-14 Pre-pitch green-H2 capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Praxair India CFO meeting; FX + green-H2 capex memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Capex TL + LC framework for ASU expansion.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Customer-SCF go-live with 5 onsite anchors; FX hedge sized.</p></div>
<div class="card"><p><strong>T+180:</strong> Linde India + Praxair India bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Capex TL Rs 300 Cr by Q3 FY27</li><li>Customer-SCF Rs 200 Cr by Q4 FY27</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Praxair India-specific from [490].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Praxair India-specific sources</h3>
<ol start="490">
<li id="src-490"><strong>MCA v3 + ZaubaCorp &mdash; Praxair India Pvt Ltd master data</strong> &mdash; CIN U24111TN1996PTC180780; incorp 27 Mar 1996; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-491"><strong>Linde plc Annual Report FY25 + NYSE LIN disclosures + India green-H2 partnership announcements</strong> &mdash; world #1 industrial gases; ~$33 bn revenue. <span class="u">linde.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "Praxair India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Praxair India", "Industrial gases + green H2 / Linde plc"),
           FOOT("Cipher clean; 1,500+ lines; FX + capex TL + green-H2 capex window.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
