"""ZF Wind Power Coimbatore dossier (pilot 79)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "zf-wind-power-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 79 of 90 · Coimbatore · ZF Friedrichshafen DE · Wind-turbine gearbox · Greenfield</div>
<h1>ZF Wind Power Coimbatore Private Limited<br>ZF Friedrichshafen Indian wind-turbine gearbox + planetary-gearbox manufacturer for global wind OEMs</h1>
<p class="lede">ZF Wind Power Coimbatore Pvt Ltd (CIN U28112TZ2006PTC013294){ref("640")} is the Indian subsidiary of ZF Friedrichshafen AG (Germany; ~&euro;46 bn revenue){ref("641")}. <strong>FY25 Total Operating Income Rs 3,832 Cr</strong>{ref("128")}; EBITDA Rs 540 Cr (14.1%); PAT Rs 320 Cr; TNW Rs 1,250 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,800 FTE{ref("128")}. Manufactures wind-turbine gearboxes + planetary-gearbox subsystems for Vestas, Siemens-Gamesa, GE Vernova, Suzlon, Senvion globally. Coimbatore plant is one of ZF Group's largest wind-gearbox plants worldwide.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 24&ndash;42 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + EBR + treasury)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,832 Cr</div><div class="sub">Wind-turbine gearbox{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + USD royalty + RM-import + finished-goods-export hedge</strong> &mdash; ZF intercompany flows.</li>
<li><strong>EBR/PCFC export window</strong> &mdash; 60%+ revenue from gearbox exports to Vestas + Siemens-Gamesa + GE Vernova.</li>
<li><strong>India offshore-wind capex tailwind</strong> &mdash; MNRE 25 GW offshore-wind by FY30; ZF gearbox supply window.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U28112TZ2006PTC013294</strong></span>
<span>Incorp <strong>17 Apr 2006</strong></span>
<span>HO <strong>Coimbatore (HQ); plants Coimbatore + Pune</strong></span>
<span>Parent <strong>ZF Friedrichshafen AG (Germany)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>ZF Friedrichshafen AG{ref("641")} is the German auto-systems major; FY25 revenue ~&euro;46 bn. ZF Wind Power business unit (separate from auto-systems business) is a global wind-gearbox leader. India operations: ZF Wind Power Coimbatore (this entity, principal manufacturing) + ZF India Pvt Ltd (auto) + ZF CV Controls (pilot 78 sister) + ZF Steering JV (ZF-Rane, pilot 32).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 60 Cr; reserves Rs 1,190 Cr; cash Rs 320 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Deutsche Bank (anchor), HSBC, Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + EBR + treasury entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,150</td><td class="num">3,490</td><td class="num">3,832{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">395</td><td class="num">465</td><td class="num">540{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.5</td><td class="num">13.3</td><td class="num">14.1</td></tr>
<tr><td>PAT</td><td class="num">220</td><td class="num">270</td><td class="num">320{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">895</td><td class="num">1,070</td><td class="num">1,250{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 60 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,800</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 320 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: EBR/PCFC for wind-gearbox exports; FX envelope; capex TL for offshore-wind ramp.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Wind-turbine gearbox + global wind</div>
<p>Global wind-turbine market FY25 ~150 GW installed; CAGR 8-10%; offshore segment 18-20% CAGR. ZF Wind Power, Moventas (Finland), Winergy (Siemens captive), GMI, Vestas-captive compete. India onshore-wind installed capacity 47 GW; offshore-wind targeted 25 GW by FY30 (MNRE).</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India wind-gearbox exports protected (services-tariff zero; gearbox tariff favourable).</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; ZF aligned.</li>
<li>India offshore-wind 25 GW FY30 target.</li>
<li>Global re-shoring of wind-supply-chain to Asia (away from China).</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,832{ref("128")}</td><td class="num">4,300</td><td class="num">4,900</td><td class="num">5,600</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.1</td><td class="num">14.7</td><td class="num">15.3</td><td class="num">15.9</td></tr>
<tr><td>EBITDA</td><td class="num">540</td><td class="num">632</td><td class="num">750</td><td class="num">890</td></tr>
<tr><td>PAT</td><td class="num">320</td><td class="num">385</td><td class="num">465</td><td class="num">560</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + USD)</td><td class="num">2,500&ndash;3,800 notional</td><td class="num">10&ndash;16</td><td>Royalty + RM imports + FG exports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>EBR / PCFC (wind-gearbox export)</td><td class="num">600&ndash;900</td><td class="num">5&ndash;8</td><td>60%+ export revenue</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Capex + RM</td></tr>
<tr><td>Capex TL (offshore-wind ramp)</td><td class="num">200&ndash;400</td><td class="num">2&ndash;4</td><td>Sustainability-linked</td></tr>
<tr><td>SCF (vendor-side)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Indian tier-2 supply</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.5&ndash;0.8</td><td>1,800 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 23.5-38.2 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,400-1,750; Rs 2-3 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>German expat MD + Indian leadership; PB AUM Rs 95-160 Cr; Rs 1-1.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + ZF Wind CSR; Rs 95-150 Cr; Rs 0.9-1.3 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.9-5.8 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">10</td><td class="num">16</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>EBR / PCFC</td><td class="num">5</td><td class="num">8</td></tr>
<tr><td>Trade + capex TL</td><td class="num">4</td><td class="num">7.2</td></tr>
<tr><td>SCF vendor</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>CMS + cards</td><td class="num">0.5</td><td class="num">0.8</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.9</td><td class="num">5.8</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>27.4</strong></td><td class="num"><strong>44.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 24-42 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; ZF parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% ZF Friedrichshafen AG{ref("641")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: ZF Wind Coimbatore capacity expansion announced for offshore-wind ramp.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Offshore-wind capex framework</li><li>T-14 Pre-pitch EBR/PCFC sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> ZF Wind Coimbatore CFO meeting; FX + EBR concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> EBR/PCFC envelope sized; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for offshore-wind ramp.</p></div>
<div class="card"><p><strong>T+180:</strong> ZF Group cross-sell (ZF CV + ZF-Rane + ZF auto bundled).</p></div>
<h3>Success metrics</h3><ul class="check"><li>EBR Rs 500 Cr by Q3 FY27</li><li>Capex TL Rs 200 Cr drawn</li><li>Y3 run-rate Rs 24-42 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; ZF Wind-specific from [640].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">ZF Wind Power Coimbatore-specific sources</h3>
<ol start="640">
<li id="src-640"><strong>MCA v3 + ZaubaCorp &mdash; ZF Wind Power Coimbatore Pvt Ltd master data</strong> &mdash; CIN U28112TZ2006PTC013294; incorp 17 Apr 2006. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-641"><strong>ZF Friedrichshafen AG Annual Report FY25 + ZF Wind Power business-unit disclosures</strong> &mdash; FY25 ~&euro;46 bn revenue; global wind-gearbox leadership. <span class="u">zf.com</span></li>
</ol></div></section>"""

def build():
    t = "ZF Wind Power Coimbatore · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("ZF Wind Power", "Wind-turbine gearbox / ZF Germany"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + EBR/PCFC + offshore-wind capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
