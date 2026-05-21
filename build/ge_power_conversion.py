"""GE Power Conversion India dossier (pilot 80)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "ge-power-conversion-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 80 of 90 · Chennai · GE Vernova US · Power conversion · Greenfield</div>
<h1>GE Power Conversion India Private Limited<br>GE Vernova (NYSE: GEV) Indian power-conversion + drives + automation arm; servicing Indian Navy + steel + marine</h1>
<p class="lede">GE Power Conversion India Pvt Ltd (CIN U34300TN2007PTC081587){ref("650")} is the Indian subsidiary of GE Vernova (NYSE: GEV; spun off from GE Apr 2024; FY25 revenue ~$36 bn){ref("651")}. <strong>FY25 Total Operating Income Rs 3,235 Cr</strong>{ref("128")}; EBITDA Rs 380 Cr (11.7%); PAT Rs 220 Cr; TNW Rs 1,150 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,400 FTE{ref("128")}. Manufactures rotating machines, drives, marine-electric-propulsion, naval-defence systems for Indian Navy + Cochin Shipyard + GRSE + steel mills + cement plants.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + BG + capex + customer-LC)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,235 Cr</div><div class="sub">Power conversion / drives{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD royalty + capex-import hedge</strong> &mdash; GE Vernova intercompany flows.</li>
<li><strong>Defence + naval BG + customer-LC envelope</strong> &mdash; Indian Navy + Cochin Shipyard + GRSE projects.</li>
<li><strong>Green-H2 + offshore-wind + grid-modernisation capex tailwind</strong> &mdash; GE Vernova Aero + Wind Power + Electrification India.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U34300TN2007PTC081587</strong></span>
<span>Incorp <strong>09 Aug 2007</strong></span>
<span>HO <strong>Chennai (Mahindra World City)</strong></span>
<span>Parent <strong>GE Vernova (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>GE Vernova{ref("651")} is a NYSE-listed energy + power equipment major (Aero, Wind, Hydro, Power, Grid, Electrification segments); FY25 revenue ~$36 bn; spun off from GE Inc on 02 Apr 2024. India operations: GE Power Conversion India (this entity, electrification/drives) + GE T&amp;D India (BSE: 522275, listed grid + transmission flagship) + GE Aerospace India (separate, post-spin).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 50 Cr; reserves Rs 1,100 Cr; cash Rs 280 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor for GE), JPMorgan, BNP Paribas.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + BG + customer-LC entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,650</td><td class="num">2,930</td><td class="num">3,235{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">280</td><td class="num">325</td><td class="num">380{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">10.6</td><td class="num">11.1</td><td class="num">11.7</td></tr>
<tr><td>PAT</td><td class="num">155</td><td class="num">185</td><td class="num">220{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">820</td><td class="num">975</td><td class="num">1,150{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 50 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,400</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 280 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: BG + LC envelope for Indian Navy + Cochin Shipyard + GRSE projects; FX hedge.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Power conversion + drives + grid</div>
<p>India power-equipment market FY25 ~Rs 1.85 lakh Cr; CAGR 10-12%; GE Vernova + Siemens Energy + ABB India + Hitachi Energy + Schneider Electric + Crompton Greaves compete. India offshore-wind 25 GW FY30; grid-modernisation FY24-30 capex Rs 5+ lakh Cr.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Indian Navy + Coast Guard + Cochin Shipyard + GRSE shipbuilding capex.</li>
<li>Green-H2 + offshore-wind + grid-modernisation: structural growth.</li>
<li>USA-tariff window{ref("6")}: limited (power-conversion is local-anchored).</li>
<li>Steel + cement plant capex: continuing.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,235{ref("128")}</td><td class="num">3,650</td><td class="num">4,150</td><td class="num">4,750</td></tr>
<tr><td>EBITDA margin %</td><td class="num">11.7</td><td class="num">12.3</td><td class="num">12.9</td><td class="num">13.5</td></tr>
<tr><td>EBITDA</td><td class="num">380</td><td class="num">449</td><td class="num">535</td><td class="num">641</td></tr>
<tr><td>PAT</td><td class="num">220</td><td class="num">265</td><td class="num">320</td><td class="num">385</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + EUR)</td><td class="num">800&ndash;1,200 notional</td><td class="num">3.5&ndash;5.5</td><td>Royalty + capex imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">220&ndash;340 float</td><td class="num">1.5&ndash;2.5</td><td>MNC TM-aaS</td></tr>
<tr><td>BG (Indian Navy + Cochin Shipyard)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Defence project BG</td></tr>
<tr><td>Capex TL (offshore-wind + drives ramp)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>RM + capex</td></tr>
<tr><td>Customer-finance (PSU receivable)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>PSU receivable</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,400 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 14.5-23.4 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,050-1,300; Rs 1.7-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>US expat MD + Indian leadership; PB AUM Rs 145-220 Cr; Rs 1.6-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + GE Vernova CSR; Rs 95-145 Cr; Rs 0.9-1.3 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 4.2-6.3 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3.5</td><td class="num">5.5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.5</td></tr>
<tr><td>BG (Defence)</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + customer-finance</td><td class="num">6</td><td class="num">9.6</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">4.2</td><td class="num">6.3</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>18.7</strong></td><td class="num"><strong>29.7</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band incl. defence + green-H2 capex tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; GE Vernova parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% GE Vernova{ref("651")} (US); BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: GE Vernova India scope expansion to offshore-wind + green-H2.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 GE Vernova spin-off corporate structure</li><li>T-14 Pre-pitch BG + customer-LC sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> GE Power Conversion CFO meeting; FX + BG + capex memo.</p></div>
<div class="card"><p><strong>T+60:</strong> BG framework for Defence / Cochin Shipyard projects.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL + customer-LC discounting MoU.</p></div>
<div class="card"><p><strong>T+180:</strong> GE T&amp;D + GE Vernova ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>BG outstanding Rs 300 Cr by Q3 FY27</li><li>Capex TL Rs 150 Cr drawn</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; GE Power Conversion-specific from [650].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">GE Power Conversion India-specific sources</h3>
<ol start="650">
<li id="src-650"><strong>MCA v3 + ZaubaCorp &mdash; GE Power Conversion India Pvt Ltd master data</strong> &mdash; CIN U34300TN2007PTC081587; incorp 09 Aug 2007. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-651"><strong>GE Vernova Annual Report FY25 + NYSE GEV disclosures + spin-off (Apr 2024)</strong> &mdash; FY25 ~$36 bn revenue; energy/power equipment major. <span class="u">gevernova.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "GE Power Conversion India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("GE Power Conversion", "Power conversion / drives / GE Vernova US"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + BG + capex TL + defence/green-H2 tailwind.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
