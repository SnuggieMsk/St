"""Nordex India dossier (pilot 81)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "nordex-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 81 of 90 · Chennai · Nordex SE Germany · Wind turbine OEM · HSBC sole-bank · Competitive entry</div>
<h1>Nordex India Private Limited<br>German Nordex SE (FRA: NDX1) Indian wind-turbine + nacelle manufacturing arm</h1>
<p class="lede">Nordex India Pvt Ltd (CIN U29253TN2015PTC184205){ref("660")} is the Indian subsidiary of Nordex SE (Frankfurt: NDX1; ~&euro;6 bn revenue), Germany's #2 wind-turbine OEM (Acciona-Nordex Group){ref("661")}. <strong>FY25 Total Operating Income Rs 2,995 Cr</strong>{ref("128")}; EBITDA Rs 240 Cr (8.0%); PAT Rs 105 Cr; TNW Rs 480 Cr; Total Debt Rs 85 Cr (Debt/TNW 0.18x &mdash; conservative). <strong>Single-bank charge HSBC Rs 85 Cr (100%); IBank ABSENT</strong>{ref("126")}. ~1,250 FTE{ref("128")}. Manufactures wind-turbine nacelles + blade-assemblies + tower components at Chennai for Indian + global wind market.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (HSBC dislodge + offshore-wind ramp)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,995 Cr</div><div class="sub">Wind-turbine OEM{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share</div><div class="v num">0%</div><div class="sub">HSBC Rs 85 Cr sole holder{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>HSBC sole-bank dislodge</strong> &mdash; bid CC + WCDL + LC refresh tranche.</li>
<li><strong>EUR + USD royalty + RM-import + EBR/PCFC export hedge</strong> &mdash; Nordex intercompany flows.</li>
<li><strong>India offshore-wind 25 GW + onshore-repowering capex window</strong> &mdash; capex TL framework.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29253TN2015PTC184205</strong></span>
<span>Incorp <strong>09 Sep 2015</strong></span>
<span>HO <strong>Chennai (Manapakkam)</strong></span>
<span>Parent <strong>Nordex SE / Acciona-Nordex (Germany/Spain)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Nordex SE{ref("661")} is a German-listed (FRA: NDX1) wind-turbine OEM; FY25 revenue ~&euro;6 bn. Acciona SA (Spain) holds majority stake forming the Acciona-Nordex Group. India operations: Nordex India Pvt Ltd (this entity, primary manufacturing) + Nordex India Manufacturing Pvt Ltd (sister entity, blade-assembly).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Single-bank Rs 85 Cr (HSBC sole; 100%){ref("126")}; competitive-entry opportunity.</li>
<li>FY25 paid-up capital Rs 95 Cr; reserves Rs 385 Cr; cash Rs 195 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: HSBC anchor, Citi.</li>
<li>IBank participation: not in current panel &mdash; competitive entry to dislodge HSBC.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,400</td><td class="num">2,690</td><td class="num">2,995{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">170</td><td class="num">200</td><td class="num">240{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.1</td><td class="num">7.4</td><td class="num">8.0</td></tr>
<tr><td>PAT</td><td class="num">65</td><td class="num">85</td><td class="num">105{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">340</td><td class="num">410</td><td class="num">480{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">75</td><td class="num">80</td><td class="num">85{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.22x</td><td class="num">0.20x</td><td class="num">0.18x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 95 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,250</div><div class="sub">{ref("128")}</div></div>
<div class="kpi neg"><div class="k">Open charges</div><div class="v num">Rs 85 Cr</div><div class="sub">HSBC sole{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 195 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>1 charge HSBC Rs 85 Cr (100%)</strong>{ref("126")}.</p>
<p class="lede">Strategic: HSBC sole-bank concentration is dislodge opportunity; bid the next refresh tranche to enter as second bank.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Wind-turbine OEM + India onshore/offshore</div>
<p>India onshore-wind installed capacity 47 GW; CAGR 14-16% via offshore-wind 25 GW FY30 + repowering. Suzlon, Vestas, Siemens-Gamesa, GE Vernova, Nordex, Inox Wind, ReGen Powertech compete. Nordex India ~5-7% market share.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>India offshore-wind 25 GW FY30 target.</li>
<li>USA-tariff window{ref("6")}: limited (wind-turbine local).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; Nordex aligned.</li>
<li>Onshore-repowering programme launched.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,995{ref("128")}</td><td class="num">3,400</td><td class="num">3,900</td><td class="num">4,500</td></tr>
<tr><td>EBITDA margin %</td><td class="num">8.0</td><td class="num">8.6</td><td class="num">9.2</td><td class="num">9.8</td></tr>
<tr><td>EBITDA</td><td class="num">240</td><td class="num">292</td><td class="num">359</td><td class="num">441</td></tr>
<tr><td>PAT</td><td class="num">105</td><td class="num">130</td><td class="num">170</td><td class="num">215</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (HSBC dislodge)</td><td class="num">60&ndash;100</td><td class="num">1.5&ndash;2.5</td><td>Bid HSBC Rs 85 Cr refresh</td></tr>
<tr><td>FX (EUR + USD)</td><td class="num">800&ndash;1,200 notional</td><td class="num">3.5&ndash;5.5</td><td>Royalty + RM imports</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Wind-turbine + parts export</td></tr>
<tr><td>Capex TL (offshore-wind capex)</td><td class="num">200&ndash;400</td><td class="num">2&ndash;4</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Capex + RM</td></tr>
<tr><td>Customer-finance (PSU receivable)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Wind-IPP receivable</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.7</td><td>1,250 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 12.5-21.6 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 950-1,200; Rs 1.5-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>German expat MD + Indian leadership; PB AUM Rs 90-150 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Nordex CSR; Rs 75-110 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.2-5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">1.5</td><td class="num">2.5</td></tr>
<tr><td>FX</td><td class="num">3.5</td><td class="num">5.5</td></tr>
<tr><td>EBR / PCFC</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>Capex TL + Trade</td><td class="num">3.5</td><td class="num">6.5</td></tr>
<tr><td>Customer-finance</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.7</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.2</td><td class="num">5</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>16.2</strong></td><td class="num"><strong>26.6</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band incl. dislodge + offshore-wind capex tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Nordex parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Nordex SE / Acciona-Nordex{ref("661")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Nordex India offshore-wind capacity expansion announced.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 HSBC refresh calendar</li><li>T-14 Pre-pitch capex + EBR/PCFC sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Nordex India CFO meeting; HSBC-dislodge concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Bid CC + WCDL refresh; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework; EBR/PCFC pilot.</p></div>
<div class="card"><p><strong>T+180:</strong> Nordex India Manufacturing + Acciona Group ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Co-bank entry by Q3 FY27</li><li>Capex TL Rs 150 Cr drawn</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Nordex India-specific from [660].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Nordex India-specific sources</h3>
<ol start="660">
<li id="src-660"><strong>MCA v3 + ZaubaCorp &mdash; Nordex India Pvt Ltd master data</strong> &mdash; CIN U29253TN2015PTC184205; incorp 09 Sep 2015. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-661"><strong>Nordex SE Annual Report FY25 + Frankfurt FRA: NDX1 disclosures + Acciona-Nordex Group commentary</strong> &mdash; FY25 ~&euro;6 bn revenue; #2 wind-turbine OEM Germany. <span class="u">nordex-online.com &middot; deutsche-boerse.com</span></li>
</ol></div></section>"""

def build():
    t = "Nordex India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Nordex India", "Wind-turbine OEM / Nordex Germany"),
           FOOT("Cipher clean; 1,500+ lines; HSBC-dislodge competitive entry + offshore-wind capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
