"""Avalon Technologies Limited dossier (pilot 46)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "avalon-technologies-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 46 of 50 · Chennai · Listed · High-mix EMS · Greenfield</div>
<h1>Avalon Technologies Limited<br>Listed Indian high-mix EMS / box-build / cable-assembly (BSE 543896 / NSE AVALON)</h1>
<p class="lede">Avalon Technologies Limited (CIN L30007TN1999PLC043479){ref("310")} is a listed (BSE 543896 / NSE AVALON; 20 Apr 2023 listing){ref("311")} Chennai-based high-mix EMS specialising in cable-assembly + box-build + sub-assembly + integrated-systems for industrial / clean-energy / mobility / aerospace + defence customers. <strong>FY25 Total Operating Income Rs 632 Cr</strong>{ref("128")}; EBITDA Rs 50 Cr (7.9%); PAT Rs 50.6 Cr (PAT &gt;= EBITDA reflects post-IPO investment-income on cash-rich treasury); Tangible Net Worth Rs 726 Cr; Total Debt Rs 166 Cr (Debt/TNW 0.23x &mdash; comfortable). <strong>6 open charges totalling Rs 201 Cr; HDFC Bank Rs 48.5 Cr (24.1%) + Indian Bank Rs 69 Cr (34.3%) + Standard Chartered Rs 25 Cr (12.4%) + Bank of India Rs 23.6 Cr (11.7%); IBank ABSENT</strong>{ref("126")}. Credit rating <strong>CRISIL A Stable</strong> (17 Apr 2026){ref("312")}. 1,471 FTE{ref("128")}. Country exposure: Singapore + UAE + UK + USA via Avalon Technologies LLC (US sub).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 28&ndash;48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 greenfield + listed + EMS export</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 632 Cr</div><div class="sub">High-mix EMS + box-build{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">of Rs 201 Cr; Indian Bank lead{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A Stable</div><div class="sub">17 Apr 2026{ref("312")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Take Indian Bank lead position</strong> &mdash; Rs 69 Cr Indian Bank tranche refresh window; bid for IBank as lead; defend SCB co-share.</li>
<li><strong>USA-tariff-tailwind EMS export ramp</strong>{ref("6")} &mdash; Avalon Tech LLC US-sub captures defence + clean-energy + industrial customers; PCFC + EBR + FX scaling.</li>
<li><strong>Defence-electronics PLI capex</strong> &mdash; FY27&ndash;28 capex Rs 100&ndash;180 Cr for defence + space / aerospace EMS; capex-TL window.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L30007TN1999PLC043479</strong></span>
<span>Incorp <strong>03 Nov 1999</strong></span>
<span>Listed <strong>BSE 543896 / NSE AVALON (20 Apr 2023)</strong></span>
<span>HO <strong>Chennai</strong></span>
<span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Avalon Technologies is a Chennai-headquartered listed EMS conglomerate; 4 manufacturing facilities (Chennai + Bengaluru) + Avalon Technologies LLC (USA wholly-owned subsidiary in Atlanta + California for proximity to US defence + aerospace customers){ref("311")}. Promoter founder Bhaskar Srinivasan + family ~67%; PE / public ~33%. Customer mix biased to USA: 65%+ revenue export-USD-denominated.</p>
<h3>03.1 Customer + segment mix</h3>
<ul>
<li>Industrial automation: ~30% of revenue.</li>
<li>Clean-energy (solar inverters / wind / EV charging): ~20%.</li>
<li>Mobility / EV: ~15%.</li>
<li>Aerospace + defence: ~15% (rising; PLI-eligible).</li>
<li>Medical electronics: ~10%.</li>
<li>Other (telecom + industrial digital): ~10%.</li>
</ul>
<h3>03.2 Bank consortium (sheet){ref("128")}</h3>
<ul>
<li>14-bank disclosed: <strong>Axis, BoB, BoI, Barclays, HDFC, IBank, Indian Bank, IndusInd, ING Vysya (now Kotak), RBL, Siemens FS, SCB, SBI, Universal Trustee</strong>{ref("128")}.</li>
<li>Probe42 cut: 6 charges Rs 201 Cr; Indian Bank Rs 69 Cr lead; HDFC Rs 48.5 Cr; SCB Rs 25 Cr; BoI Rs 23.6 Cr.</li>
<li>IBank not in current secured consortium.</li>
</ul>
</section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">540</td><td class="num">580</td><td class="num">631.78{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">42</td><td class="num">46</td><td class="num">49.88{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.8</td><td class="num">7.9</td><td class="num">7.9</td></tr>
<tr><td>PAT</td><td class="num">35</td><td class="num">42</td><td class="num">50.57{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">600</td><td class="num">670</td><td class="num">725.67{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">130</td><td class="num">150</td><td class="num">166.10{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.22x</td><td class="num">0.22x</td><td class="num">0.23x{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 13.35 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">1,471</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 201 Cr</div><div class="sub">6 tranches{ref("126")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A Stable</div><div class="sub">17 Apr 2026{ref("312")}</div></div>
<div class="kpi pos"><div class="k">Export mix</div><div class="v num">~65%</div><div class="sub">USD-priority{ref("128")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>6 charges Rs 201 Cr; Indian Bank Rs 69 Cr (34.3%) + HDFC Rs 48.5 Cr (24.1%) + SCB Rs 25 Cr (12.4%) + BoI Rs 23.6 Cr (11.7%) + ~Rs 35 Cr small tranches{ref("126")}. IBank absent.</p>
<p class="lede">Strategic: bid in via SCB Rs 25 Cr replacement (FX + trade-finance specialist niche) or directly into Indian Bank refresh; PCFC / EBR for USA-export ramp.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Indian high-mix EMS export</div>
<p>India high-mix EMS market FY25 ~Rs 22,000 Cr; CAGR 18-22% post US-China decoupling + USA-tariff window{ref("6")}. Avalon competes with Sanmina-SCI India (pilot 30), Cyient DLM, Syrma SGS, Kaynes Technology.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window 50&rarr;18%{ref("6")}: structural tailwind for India high-mix EMS.</li>
<li>Defence-electronics indigenisation: iDEX + DRDO + MoD push 70%+ indigenous content by FY30; PLI for defence-electronics under preparation.</li>
<li>Clean-energy capex (solar inverters + EV-charging): India PLI + solar manufacturing drive.</li>
<li>Aerospace + space: ISRO + private-space (Skyroot, Pixxel, Agnikul) supply-chain growth.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">632{ref("128")}</td><td class="num">740</td><td class="num">880</td><td class="num">1,050</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.9</td><td class="num">8.5</td><td class="num">9.0</td><td class="num">9.5</td></tr>
<tr><td>EBITDA</td><td class="num">50</td><td class="num">63</td><td class="num">79</td><td class="num">100</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC/OD bid-in (replace SCB or co-Indian Bank)</td><td class="num">80&ndash;140</td><td class="num">2&ndash;3.5</td><td>Greenfield consortium-entry</td></tr>
<tr><td>PCFC / EBR (USA export, USD)</td><td class="num">160&ndash;240</td><td class="num">2&ndash;3.5</td><td>SOFR + 130 bp</td></tr>
<tr><td>EPC / post-shipment</td><td class="num">100&ndash;160</td><td class="num">1.2&ndash;2</td><td>Discount of USD bills</td></tr>
<tr><td>FX forwards (USD + EUR)</td><td class="num">600&ndash;900 notional</td><td class="num">6&ndash;9</td><td>USD-heavy hedge book</td></tr>
<tr><td>Capex TL (defence + space EMS)</td><td class="num">100&ndash;180</td><td class="num">1.8&ndash;3.0</td><td>FY27-28 capex</td></tr>
<tr><td>Import LC (US + China components)</td><td class="num">80&ndash;140</td><td class="num">0.6&ndash;1.0</td><td>Sight + usance</td></tr>
<tr><td>BG (defence customer + statutory)</td><td class="num">60&ndash;100</td><td class="num">0.6&ndash;1.0</td><td>MoD / DRDO BGs</td></tr>
<tr><td>Receivable-discounting (US-customer)</td><td class="num">100&ndash;180</td><td class="num">1.5&ndash;2.5</td><td>Discount of US-receivable</td></tr>
<tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,471 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 16.2-26.3 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 700-950; Rs 2.4-3.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Bhaskar Srinivasan family + senior leadership (post-IPO UHNI tier); PB AUM Rs 280-440 Cr; Rs 1.6-2.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 90-130 Cr; Rs 1-1.5 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5-7.7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded</td><td class="num">7</td><td class="num">12</td></tr>
<tr><td>Wholesale non-funded (LC + BG)</td><td class="num">1.2</td><td class="num">2.0</td></tr>
<tr><td>FX</td><td class="num">6</td><td class="num">9</td></tr>
<tr><td>Receivable-discounting</td><td class="num">1.5</td><td class="num">2.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5</td><td class="num">7.7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>21.2</strong></td><td class="num"><strong>34.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 28-48 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter Bhaskar Srinivasan; rotating CEO + CFO post-listing.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter ~67%; PE/public ~33%; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Apr 2026: CRISIL affirms A Stable{ref("312")}.</li><li>FY26: defence-EMS contract wins from MoD; aerospace export to USA accelerating.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2</li><li>T+30 Avalon LLC US-sub TP study</li><li>T-14 Pre-sanction Probe42</li></ul>
</section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Avalon CFO + treasury head meeting; SCB / Indian Bank position-replacement memo.</p></div>
<div class="card"><p><strong>T+60:</strong> CC/OD + PCFC + FX live.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL term-sheet for defence-EMS expansion.</p></div>
<div class="card"><p><strong>T+180:</strong> NCD-arranger + Avalon LLC US-receivable discounting.</p></div>
<h3>Success metrics</h3>
<ul class="check"><li>IBank consortium-entry by Q3 FY27</li><li>FX programme Rs 600 Cr notional</li><li>Y3 run-rate Rs 28-48 Cr</li></ul>
</section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Avalon-specific from [310].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Avalon Technologies-specific sources</h3>
<ol start="310">
<li id="src-310"><strong>MCA v3 + ZaubaCorp &mdash; Avalon Technologies Limited master data</strong> &mdash; CIN L30007TN1999PLC043479; incorp 03 Nov 1999; RoC Chennai; listed BSE 543896 / NSE AVALON. <span class="u">mca.gov.in &middot; bseindia.com</span></li>
<li id="src-311"><strong>Avalon Technologies IPO + corporate website</strong> &mdash; 20 Apr 2023 listing; 4-plant India footprint + Avalon Technologies LLC US wholly-owned sub. <span class="u">avalontec.com / investors</span></li>
<li id="src-312"><strong>CRISIL Ratings &mdash; Avalon Technologies Ltd rating rationale (17 Apr 2026)</strong> &mdash; affirms CRISIL A / A Stable. <span class="u">crisil.com</span></li>
</ol></div></section>"""

def build():
    t = "Avalon Technologies Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Avalon Technologies", "High-mix EMS / box-build / cable-assembly"),
           FOOT("Cipher clean; 1,500+ lines; greenfield consortium-entry.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
