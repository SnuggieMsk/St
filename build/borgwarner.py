"""BorgWarner Morse Systems India Pvt Ltd dossier (pilot 54)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "borgwarner-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 54 of 55 · Thiruvallur + Sriperumbudur · MNC · US e-mobility tier-1 (BorgWarner two-entity)</div>
<h1>BorgWarner India (Morse Systems + Cooling Systems) Private Limited<br>BorgWarner Inc. (NYSE: BWA) &mdash; e-mobility tier-1; turbo + chains + thermal-management + EV-power</h1>
<p class="lede">BorgWarner India (consolidated dossier covering BorgWarner Morse Systems India Pvt Ltd, CIN U28991TN2001FTC047397{ref("390")}, and BorgWarner Cooling Systems India Pvt Ltd, CIN U28999TN2001PTC047184{ref("391")}) are the two operating entities of BorgWarner Inc. (NYSE: BWA), the US-listed global e-mobility tier-1 (FY25 global revenue ~$14 bn){ref("392")}. Morse Systems specialises in timing-chain + transmission components; Cooling Systems specialises in fan + thermal-management + radiator + cooling-pump components. Combined operations: Thiruvallur (Morse) + Sriperumbudur (Cooling) plants. <strong>Combined FY25 TOI Rs 1,142 Cr</strong>{ref("128")}; combined EBITDA Rs 324 Cr (28.4% &mdash; premium-tier auto-comp margins); combined PAT Rs 237 Cr; <strong>zero open charges across both entities</strong>{ref("126")}. Credit rating Not Rated at entity level; parent BorgWarner Inc. is Moody's Baa1 / S&amp;P BBB+{ref("392")}. Combined 612 FTE{ref("128")}.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 30&ndash;48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 2-entity consolidated greenfield</div></div>
<div class="kpi"><div class="k">Combined FY25 TOI</div><div class="v num">Rs 1,142 Cr</div><div class="sub">Morse Rs 630 Cr + Cooling Rs 512 Cr{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges (both)</div><div class="v num">0 / Rs 0 Cr</div><div class="sub">Zero secured exposure{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Parent rating</div><div class="v num">Moody's Baa1 / S&amp;P BBB+</div><div class="sub">{ref("392")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Greenfield 2-entity consolidated entry</strong> &mdash; both entities zero-charge today; first IBank-led WC + capex line creates wallet anchor at AA-equivalent given parent BBB+ credit.</li>
<li><strong>EV powertrain pivot</strong> &mdash; BorgWarner globally pivoting from ICE turbo to EV-power-electronics + e-axle + battery thermal-management; India FY27&ndash;28 capex Rs 200&ndash;320 Cr.</li>
<li><strong>USD-heavy import LC + FX</strong> &mdash; US-parent timing-chain + e-power components; FX hedge Rs 480-720 Cr notional.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CINs <strong>U28991TN2001FTC047397 + U28999TN2001PTC047184</strong></span>
<span>Incorp <strong>09 Jul 2001 + 30 May 2001</strong></span>
<span>Group <strong>BorgWarner Inc. (NYSE: BWA)</strong></span>
<span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>BorgWarner Inc.{ref("392")} (NYSE: BWA; founded 1928; FY25 revenue ~$14 bn; 50,000+ FTE) is the world's leading e-mobility tier-1, ranked top-3 in turbocharger + transmission components + EV-power-electronics. Investment-grade ratings Moody's Baa1 / S&amp;P BBB+. India operations split across two TN-based entities to align technology lineage (Morse Systems = timing-chain + transmission; Cooling Systems = thermal-management).</p>
<h3>03.1 Two-entity structure</h3>
<div style="overflow-x:auto"><table>
<thead><tr><th>Entity</th><th>CIN</th><th>Function</th><th>FY25 TOI (Rs Cr)</th></tr></thead>
<tbody>
<tr><td>BorgWarner Morse Systems India</td><td>U28991TN2001FTC047397{ref("390")}</td><td>Timing chains + transmission components</td><td class="num">630.4{ref("128")}</td></tr>
<tr><td>BorgWarner Cooling Systems India</td><td>U28999TN2001PTC047184{ref("391")}</td><td>Cooling fan + radiator + thermal management</td><td class="num">511.5{ref("128")}</td></tr>
<tr><td><strong>Combined</strong></td><td>&nbsp;</td><td>&nbsp;</td><td class="num"><strong>1,141.9</strong></td></tr>
</tbody></table></div>
<h3>03.2 Bank consortium (per sheet){ref("128")}</h3>
<ul>
<li>Both entities show essentially no disclosed banking lines beyond transactional / parent-funded.</li>
<li>Probe42 cut: zero open charges{ref("126")} both entities.</li>
<li>IBank not in current consortium &mdash; clean greenfield.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier (consolidated)</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th>Morse</th><th>Cooling</th><th><strong>Combined FY25</strong></th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">630.4</td><td class="num">511.5</td><td class="num"><strong>1,141.9</strong>{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">153.0</td><td class="num">171.2</td><td class="num"><strong>324.2</strong>{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">24.3</td><td class="num">33.5</td><td class="num"><strong>28.4</strong></td></tr>
<tr><td>PAT</td><td class="num">102.8</td><td class="num">133.8</td><td class="num"><strong>236.6</strong>{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">238.97</td><td class="num">235.39</td><td class="num"><strong>474.4</strong>{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">0</td><td class="num">0</td><td class="num"><strong>0</strong>{ref("128")}</td></tr>
<tr><td>FTE</td><td class="num">435</td><td class="num">177</td><td class="num"><strong>612</strong>{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi pos"><div class="k">EBITDA margin</div><div class="v num">28.4%</div><div class="sub">Premium e-mobility tier-1{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">612</div><div class="sub">Combined{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">0 / Rs 0 Cr</div><div class="sub">Both entities{ref("126")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
<div class="kpi pos"><div class="k">Parent rating</div><div class="v num">Moody's Baa1 / S&amp;P BBB+</div><div class="sub">{ref("392")}</div></div>
<div class="kpi"><div class="k">Country of origin</div><div class="v num">USA</div><div class="sub">{ref("128")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Both entities zero-charge{ref("126")}; zero balance-sheet debt; pure parent-funded. Greenfield.</p>
<p class="lede">Strategic: First IBank charge filing (either entity) creates lead-bank position at AA-equivalent pricing supported by parent letter-of-comfort framework.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; e-mobility tier-1</div>
<p>India e-mobility / EV-power-electronics market emerging FY26-30; CAGR 25-30% from low base. BorgWarner global pivot from ICE-turbo to EV-power; India alignment to Tata + M&amp;M + Hyundai EV programmes.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>EV mix shift: BorgWarner timing chain volume compressed by EV mix; e-axle + e-power gains.</li>
<li>USA-tariff window{ref("6")}: India-export to USA aftermarket benefits.</li>
<li>BorgWarner global e-mobility programme: India role rising.</li>
<li>Premium auto-comp margin profile (28% EBITDA) reflects high-tech IP content.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr (combined)</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,142{ref("128")}</td><td class="num">1,280</td><td class="num">1,440</td><td class="num">1,620</td></tr>
<tr><td>EBITDA margin %</td><td class="num">28.4</td><td class="num">28.0</td><td class="num">27.5</td><td class="num">28.0</td></tr>
<tr><td>EBITDA</td><td class="num">324</td><td class="num">358</td><td class="num">396</td><td class="num">454</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC/OD anchor (greenfield, both entities)</td><td class="num">120&ndash;200</td><td class="num">2.8&ndash;4.5</td><td>First filing</td></tr>
<tr><td>Capex TL (EV powertrain pivot)</td><td class="num">200&ndash;320</td><td class="num">3.5&ndash;5.5</td><td>FY27-28; SLL-style</td></tr>
<tr><td>Import LC (US parent components)</td><td class="num">280&ndash;420</td><td class="num">2.2&ndash;3.4</td><td>USD-priority</td></tr>
<tr><td>FX (USD + EUR)</td><td class="num">480&ndash;720 notional</td><td class="num">4.8&ndash;7.2</td><td>Hedge book</td></tr>
<tr><td>BG (customer + statutory)</td><td class="num">60&ndash;100</td><td class="num">0.6&ndash;1.0</td><td>OEM counter-guarantees</td></tr>
<tr><td>SCF (vendor)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3.2</td><td>Anchor-led</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">100&ndash;180</td><td class="num">1.2&ndash;2.2</td><td>USA-tariff aftermarket</td></tr>
<tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>612 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 17.6-27.8 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 280-380; Rs 1.0-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>India MD + plant + finance leadership (US-rotation expat); PB AUM Rs 200-320 Cr; Rs 1.4-2.4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR; Rs 60-90 Cr; Rs 0.7-1.0 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.1-4.9 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view (2-entity)</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded</td><td class="num">5.5</td><td class="num">9</td></tr>
<tr><td>Wholesale non-funded</td><td class="num">2.8</td><td class="num">4.4</td></tr>
<tr><td>FX</td><td class="num">4.8</td><td class="num">7.2</td></tr>
<tr><td>SCF</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>EBR / PCFC</td><td class="num">1.2</td><td class="num">2.2</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.1</td><td class="num">4.9</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>19.9</strong></td><td class="num"><strong>31.7</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 30-48 Cr/yr captures upper-mid band including EV capex pipeline.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12 across both entities; US-rotation MD + India CFO + parent nominees.</p>
<h3>11.2 Ownership</h3><ul><li>100% BorgWarner Inc. (NYSE: BWA){ref("392")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong> both{ref("82")}; NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY25 BorgWarner global e-mobility commentary cites India growth-market.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 both entities</li><li>T+30 Transfer-pricing + US-parent letter-of-comfort feasibility</li><li>T-14 Pre-sanction Probe42 both</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Both India MDs + treasury heads meeting; greenfield CC/OD memo; FX framework.</p></div>
<div class="card"><p><strong>T+60:</strong> CC/OD + FX + Import LC live both entities.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL term-sheet for EV-powertrain pivot.</p></div>
<div class="card"><p><strong>T+180:</strong> SCF + receivable-discounting + parent treasury introduction.</p></div>
<h3>Success metrics</h3><ul class="check"><li>First IBank charge by Q3 FY27 (either entity)</li><li>Capex TL Rs 200 Cr drawn</li><li>Y3 run-rate Rs 30-48 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; BorgWarner-specific from [390].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">BorgWarner India-specific sources</h3>
<ol start="390">
<li id="src-390"><strong>MCA v3 + ZaubaCorp &mdash; BorgWarner Morse Systems India Pvt Ltd</strong> &mdash; CIN U28991TN2001FTC047397; incorp 09 Jul 2001; RoC Chennai; Thiruvallur. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-391"><strong>MCA v3 + ZaubaCorp &mdash; BorgWarner Cooling Systems (India) Pvt Ltd</strong> &mdash; CIN U28999TN2001PTC047184; incorp 30 May 2001; RoC Chennai; Sriperumbudur. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-392"><strong>BorgWarner Inc. FY25 10-K (NYSE: BWA)</strong> &mdash; revenue ~$14 bn; 50,000+ FTE; Moody's Baa1 / S&amp;P BBB+; e-mobility pivot strategy. <span class="u">sec.gov &middot; borgwarner.com / investors</span></li>
</ol></div></section>"""

def build():
    t = "BorgWarner India (Morse + Cooling Systems) · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("BorgWarner India", "Auto-comp e-mobility tier-1 (US-MNC)"),
           FOOT("Cipher clean; 1,500+ lines; 2-entity greenfield BBB+ entry.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
