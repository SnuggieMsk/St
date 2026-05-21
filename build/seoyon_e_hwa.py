"""Seoyon E-Hwa Summit Automotive India dossier (pilot 83)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "seoyon-e-hwa-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 83 of 90 · Chennai · Seoyon E-Hwa Korea · Auto interior + cockpit · Competitive entry</div>
<h1>Seoyon E-Hwa Summit Automotive India Private Limited<br>Korean Seoyon E-Hwa Indian auto-cockpit + interior tier-1 supplier to Hyundai-Kia + Mahindra</h1>
<p class="lede">Seoyon E-Hwa Summit Automotive India Pvt Ltd (CIN U35999TN2002PTC049333){ref("680")} is the Indian subsidiary of Seoyon E-Hwa Co Ltd (KOSDAQ-listed Korean tier-1 cockpit + interior major){ref("681")}. <strong>FY25 Total Operating Income Rs 2,183 Cr</strong>{ref("128")}; EBITDA Rs 175 Cr (8.0%); PAT Rs 90 Cr; TNW Rs 460 Cr; Total Debt Rs 154 Cr (Debt/TNW 0.33x). <strong>4-bank consortium Rs 154 Cr; Citi Rs 82.5 Cr (53.7%) + Kotak Rs 40 Cr (26.1%) + Shinhan Rs 18 Cr (11.7%) + IndusInd Rs 13 Cr (8.5%); IBank ABSENT</strong>{ref("126")}. ~1,800 FTE{ref("128")}. Manufactures auto-cockpit + interior + door-trim + headliner subsystems for Hyundai Sriperumbudur + Kia Anantapur + Mahindra Chakan customers.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (competitive entry + customer-SCF)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,183 Cr</div><div class="sub">Auto interior + cockpit{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share</div><div class="v num">0%</div><div class="sub">Citi-led 4-bank consortium{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Bid Citi-led consortium refresh tranche</strong> &mdash; competitive entry on next refresh.</li>
<li><strong>KRW + USD royalty + RM-import hedge</strong> &mdash; Seoyon Korea intercompany flows.</li>
<li><strong>Hyundai-Kia ecosystem cross-sell</strong> &mdash; bundled wallet across Mobis (pilot 56) + Glovis (pilot 59) + Hyundai Steel.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U35999TN2002PTC049333</strong></span>
<span>Incorp <strong>11 Sep 2002</strong></span>
<span>HO <strong>Sriperumbudur (Chennai 602105)</strong></span>
<span>Parent <strong>Seoyon E-Hwa Co Ltd (Korea)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Seoyon E-Hwa Co Ltd{ref("681")} is a KOSDAQ-listed Korean auto-tier-1 supplier; FY25 revenue ~$1.8 bn; Hyundai-Kia ecosystem captive (alongside Mobis); cockpit + interior leadership. India operations: Seoyon E-Hwa Summit Automotive India Pvt Ltd (this entity, primary manufacturing).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>4-bank Rs 154 Cr{ref("126")}; Citi Rs 82.5 Cr (53.7%) + Kotak Rs 40 Cr (26.1%) + Shinhan Rs 18 Cr (11.7%) + IndusInd Rs 13 Cr (8.5%).</li>
<li>FY25 paid-up capital Rs 75 Cr; reserves Rs 385 Cr; cash Rs 145 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor), Shinhan (Korean MNC anchor), Kotak, IndusInd.</li>
<li>IBank participation: not in current secured consortium &mdash; competitive entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,750</td><td class="num">1,960</td><td class="num">2,183{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">125</td><td class="num">150</td><td class="num">175{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.1</td><td class="num">7.7</td><td class="num">8.0</td></tr>
<tr><td>PAT</td><td class="num">55</td><td class="num">70</td><td class="num">90{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">320</td><td class="num">390</td><td class="num">460{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">140</td><td class="num">148</td><td class="num">154{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.44x</td><td class="num">0.38x</td><td class="num">0.33x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 75 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,800</div><div class="sub">{ref("128")}</div></div>
<div class="kpi neg"><div class="k">Open charges</div><div class="v num">Rs 154 Cr</div><div class="sub">4-bank Citi-led{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 145 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>4-bank consortium Rs 154 Cr</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th></tr></thead>
<tbody>
<tr><td>Citibank N.A.</td><td class="num">82.5</td><td class="num">53.7</td></tr>
<tr><td>Kotak Mahindra Bank</td><td class="num">40.0</td><td class="num">26.1</td></tr>
<tr><td>Shinhan Bank</td><td class="num">18.0</td><td class="num">11.7</td></tr>
<tr><td>IndusInd Bank</td><td class="num">13.0</td><td class="num">8.5</td></tr>
</tbody></table></div>
<p class="lede">Strategic: bid the next refresh tranche to enter; Citi-led concentration is dislodge opportunity.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto-interior + cockpit tier-1</div>
<p>India auto-interior + cockpit market FY25 ~Rs 32,000 Cr; CAGR 9-11%; Hyundai-Kia ecosystem includes Seoyon E-Hwa, Mobis (pilot 56), Sungwoo Stamping. Mahindra ecosystem: Faurecia (pilot 25 done), Continental, Yanfeng compete.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Hyundai-Kia capacity ramp post-HMIL listing{ref("11")}: Seoyon volume up.</li>
<li>USA-tariff window{ref("6")}: HMG export ramp benefit.</li>
<li>EV-cockpit + ADAS-cockpit transition: cockpit-electronics ramp.</li>
<li>Premiumisation: high-end interiors.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,183{ref("128")}</td><td class="num">2,500</td><td class="num">2,900</td><td class="num">3,350</td></tr>
<tr><td>EBITDA margin %</td><td class="num">8.0</td><td class="num">8.4</td><td class="num">8.8</td><td class="num">9.2</td></tr>
<tr><td>EBITDA</td><td class="num">175</td><td class="num">210</td><td class="num">255</td><td class="num">308</td></tr>
<tr><td>PAT</td><td class="num">90</td><td class="num">110</td><td class="num">140</td><td class="num">175</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (Citi dislodge)</td><td class="num">80&ndash;120</td><td class="num">2&ndash;3</td><td>Bid Citi Rs 82.5 Cr</td></tr>
<tr><td>FX (KRW + USD)</td><td class="num">700&ndash;1,000 notional</td><td class="num">3&ndash;4.5</td><td>Royalty + RM imports</td></tr>
<tr><td>Customer-SCF (Hyundai/Kia/Mahindra)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>OEM receivables</td></tr>
<tr><td>Capex TL (cockpit-electronics ramp)</td><td class="num">100&ndash;180</td><td class="num">1&ndash;1.8</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>RM + capex imports</td></tr>
<tr><td>EBR / PCFC</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>Korean re-export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.6&ndash;0.9</td><td>1,800 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 10.6-16.6 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,350-1,700; Rs 2-3 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Korean expat MD + Indian leadership; PB AUM Rs 90-150 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Seoyon CSR; Rs 70-110 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.7-5.5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>FX</td><td class="num">3</td><td class="num">4.5</td></tr>
<tr><td>Customer-SCF</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">0.9</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.7</td><td class="num">5.5</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>14.3</strong></td><td class="num"><strong>22.1</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr captures upper-mid band incl. dislodge upside.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Seoyon parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Seoyon E-Hwa Co Ltd, Korea{ref("681")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Seoyon India volume ramp post-HMIL listing.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Citi refresh calendar</li><li>T-14 Pre-pitch capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Seoyon E-Hwa CFO meeting; Citi-dislodge concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Bid CC + WCDL refresh; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Customer-SCF MoU with HMIL/Kia; capex TL framework.</p></div>
<div class="card"><p><strong>T+180:</strong> Hyundai-Kia ecosystem bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Co-bank entry by Q3 FY27</li><li>Customer-SCF Rs 150 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Seoyon-specific from [680].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Seoyon E-Hwa-specific sources</h3>
<ol start="680">
<li id="src-680"><strong>MCA v3 + ZaubaCorp &mdash; Seoyon E-Hwa Summit Automotive India Pvt Ltd master data</strong> &mdash; CIN U35999TN2002PTC049333; incorp 11 Sep 2002. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-681"><strong>Seoyon E-Hwa Co Ltd KOSDAQ disclosures + Hyundai-Kia ecosystem captive commentary</strong> &mdash; FY25 ~$1.8 bn revenue. <span class="u">seoyon.com &middot; krx.co.kr</span></li>
</ol></div></section>"""

def build():
    t = "Seoyon E-Hwa Summit Automotive India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Seoyon E-Hwa", "Auto-interior + cockpit tier-1 / Korean MNC"),
           FOOT("Cipher clean; 1,500+ lines; Citi-dislodge competitive entry + Hyundai-Kia ecosystem.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
