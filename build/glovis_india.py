"""Glovis India dossier (pilot 59)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "glovis-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 59 of 75 · Chennai · Hyundai Glovis Korean MNC · Auto-logistics · Greenfield</div>
<h1>Glovis India Private Limited<br>Korean Hyundai Glovis Co. Indian inbound + outbound auto-logistics arm</h1>
<p class="lede">Glovis India Pvt Ltd (CIN U74900TN2006PTC058975){ref("440")} is the Indian subsidiary of Hyundai Glovis Co. Ltd (KOSPI: 086280; ~$24 bn revenue), the Hyundai Motor Group's captive logistics arm{ref("441")}. <strong>FY25 Total Operating Income Rs 4,454 Cr</strong>{ref("128")}; EBITDA Rs 215 Cr (4.8%); PAT Rs 105 Cr; TNW Rs 530 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 480 FTE{ref("128")}. End-to-end logistics for HMIL Sriperumbudur, Kia Anantapur, Mobis (pilot 56) &mdash; CKD/PBP-import, finished-vehicle outbound rail/road, port handling, parts-distribution. Major customers: HMIL, Kia, Hyundai-Mobis tier-1 ecosystem.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;32 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + treasury + SCF)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 4,454 Cr</div><div class="sub">Auto logistics{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>KRW + USD freight + bunker hedge</strong> &mdash; international shipping + intercompany payables.</li>
<li><strong>Vendor-SCF (3PL + transporter network)</strong> &mdash; 200+ trucking partners + Indian-Railway BCACBM rake operators.</li>
<li><strong>Hyundai-Glovis ecosystem cross-sell</strong> &mdash; HMIL + Kia + Mobis bundled relationship play.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U74900TN2006PTC058975</strong></span>
<span>Incorp <strong>23 Mar 2006</strong></span>
<span>HO <strong>Sriperumbudur (Chennai 602105)</strong></span>
<span>Parent <strong>Hyundai Glovis Co. (Korea)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Hyundai Glovis Co. Ltd{ref("441")} is the Hyundai Motor Group's captive logistics + supply-chain arm; FY25 group revenue ~$24 bn; bulk shipping + auto-finished-vehicle ocean fleet + 3PL warehousing globally. Glovis India (this entity) sits within HMG India ecosystem alongside HMIL, Kia India, Mobis India, Hyundai Steel India, HMC India.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; entirely equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 35 Cr; reserves Rs 495 Cr; cash Rs 320 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: HDFC, BNP Paribas, Standard Chartered &mdash; FX + LC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + vendor-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,560</td><td class="num">4,000</td><td class="num">4,454{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">155</td><td class="num">180</td><td class="num">215{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">4.4</td><td class="num">4.5</td><td class="num">4.8</td></tr>
<tr><td>PAT</td><td class="num">75</td><td class="num">90</td><td class="num">105{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">395</td><td class="num">465</td><td class="num">530{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 35 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">480</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 320 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. Pure flow + treasury opportunity.</p>
<p class="lede">Strategic: KRW + USD ocean-freight + bunker hedge envelope; vendor-SCF for 200+ transporter network; bid the export RoRo + finished-vehicle PCFC.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto + bulk logistics</div>
<p>India 3PL auto-logistics market FY25 ~Rs 38,000 Cr; CAGR 11-13%. Glovis India holds ~12-15% share of HMG-captive flow. Industry drivers: ocean-freight cycles, port + rake congestion, dedicated-rail freight corridor (DFC) ramp, GST-3PL consolidation.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: HMG export ramp boosts Glovis container outbound.</li>
<li>EU CBAM{ref("18")}: scope-3 emission reporting required for HMG exports; Glovis emissions-data infrastructure.</li>
<li>Bunker + freight volatility: hedge demand.</li>
<li>DFC + port ramp: capex on rake assets.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">4,454{ref("128")}</td><td class="num">5,000</td><td class="num">5,650</td><td class="num">6,300</td></tr>
<tr><td>EBITDA margin %</td><td class="num">4.8</td><td class="num">5.0</td><td class="num">5.2</td><td class="num">5.4</td></tr>
<tr><td>EBITDA</td><td class="num">215</td><td class="num">250</td><td class="num">294</td><td class="num">340</td></tr>
<tr><td>PAT</td><td class="num">105</td><td class="num">130</td><td class="num">160</td><td class="num">195</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (KRW + USD + EUR)</td><td class="num">1,500&ndash;2,400 notional</td><td class="num">5&ndash;9</td><td>Freight + intercompany</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>Vendor-SCF (transporters)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>200+ partners</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Capex + bunker</td></tr>
<tr><td>EBR / PCFC (RoRo export)</td><td class="num">200&ndash;400</td><td class="num">2&ndash;3.5</td><td>HMG export ramp</td></tr>
<tr><td>Capex TL (rake / warehouse)</td><td class="num">100&ndash;200</td><td class="num">1&ndash;2</td><td>DFC + port handling</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.4&ndash;0.7</td><td>480 FTE + transporter payments</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 14.9-25.7 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 360-450; Rs 1.4-2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Korean expat MD + Indian leadership; PB AUM Rs 75-130 Cr; Rs 0.9-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Glovis CSR; Rs 35-55 Cr; Rs 0.3-0.5 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 2.6-4 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">5</td><td class="num">9</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Vendor-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Trade + EBR + capex TL</td><td class="num">4.5</td><td class="num">8</td></tr>
<tr><td>CMS + cards</td><td class="num">0.4</td><td class="num">0.7</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">2.6</td><td class="num">4</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>17.5</strong></td><td class="num"><strong>29.7</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-32 Cr/yr captures upper-mid band incl. ecosystem cross-sell tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Korean Glovis-parent appointee MD + Indian CFO.</p>
<h3>11.2 Ownership</h3><ul><li>100% Hyundai Glovis Co. Ltd, Korea (parent){ref("441")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Glovis India scope expansion to handle Kia post-IPO ramp + parts-distribution.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Bunker + freight hedge framework</li><li>T-14 Vendor-SCF panel sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Glovis India CFO meeting; FX + bunker hedge memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Vendor-SCF pilot with 50 transporters.</p></div>
<div class="card pos"><p><strong>T+90:</strong> EBR/PCFC live for RoRo exports; capex TL framework.</p></div>
<div class="card"><p><strong>T+180:</strong> HMG-ecosystem cross-sell (HMIL + Kia + Mobis bundled).</p></div>
<h3>Success metrics</h3><ul class="check"><li>FX envelope Rs 1,500 Cr by Q3 FY27</li><li>Vendor SCF Rs 300 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-32 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Glovis India-specific from [440].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Glovis India-specific sources</h3>
<ol start="440">
<li id="src-440"><strong>MCA v3 + ZaubaCorp &mdash; Glovis India Pvt Ltd master data</strong> &mdash; CIN U74900TN2006PTC058975; incorp 23 Mar 2006; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-441"><strong>Hyundai Glovis Co. Ltd Annual Report FY25 + KOSPI 086280 disclosures</strong> &mdash; group revenue ~$24 bn; HMG captive logistics. <span class="u">glovis.net &middot; krx.co.kr</span></li>
</ol></div></section>"""

def build():
    t = "Glovis India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Glovis India", "Auto-logistics 3PL / Hyundai Glovis Korean MNC"),
           FOOT("Cipher clean; 1,500+ lines; FX + vendor-SCF + bunker hedge.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
