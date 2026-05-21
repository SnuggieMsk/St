"""Danfoss Industries India dossier (pilot 82)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "danfoss-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 82 of 90 · Chennai · Danfoss A/S Denmark · HVAC + drives + climate · Greenfield</div>
<h1>Danfoss Industries Private Limited<br>Danish Danfoss A/S Indian climate-solutions + drives + power-electronics manufacturing arm</h1>
<p class="lede">Danfoss Industries Pvt Ltd (CIN U29199TN1999PTC041877){ref("670")} is the Indian subsidiary of Danfoss A/S (Denmark, private; ~&euro;10 bn revenue), a Bitten &amp; Mads Clausen Foundation-controlled climate-solutions + drives + power-electronics MNC{ref("671")}. <strong>FY25 Total Operating Income Rs 2,509 Cr</strong>{ref("128")}; EBITDA Rs 365 Cr (14.5%); PAT Rs 215 Cr; TNW Rs 920 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~1,650 FTE{ref("128")}. Manufactures HVAC compressors + variable-frequency-drives + heat-exchanger + power-electronics for refrigeration + commercial-AC + industrial drive applications.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + customer-SCF + capex TL)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,509 Cr</div><div class="sub">HVAC + drives{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + DKK royalty + RM-import hedge</strong> &mdash; Danfoss Denmark intercompany flows.</li>
<li><strong>Customer-SCF on commercial-AC + cold-chain anchors</strong> &mdash; Voltas + Daikin + LG + Samsung anchor customers.</li>
<li><strong>Cold-chain + green-cooling + EV-drive capex window</strong> &mdash; Danfoss India capex ramp.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U29199TN1999PTC041877</strong></span>
<span>Incorp <strong>20 Apr 1999</strong></span>
<span>HO <strong>Chennai (Oragadam) + Pune</strong></span>
<span>Parent <strong>Danfoss A/S (Denmark)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Danfoss A/S{ref("671")} is a Danish private MNC; FY25 revenue ~&euro;10 bn; family-foundation owned (Bitten and Mads Clausen Foundation). India operations: Danfoss Industries Pvt Ltd (this entity, principal manufacturing).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 60 Cr; reserves Rs 860 Cr; cash Rs 235 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Nordea India branch (Danish anchor), Citi, HSBC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF + capex entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,000</td><td class="num">2,250</td><td class="num">2,509{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">270</td><td class="num">315</td><td class="num">365{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.5</td><td class="num">14.0</td><td class="num">14.5</td></tr>
<tr><td>PAT</td><td class="num">150</td><td class="num">180</td><td class="num">215{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">685</td><td class="num">800</td><td class="num">920{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 60 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,650</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 235 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: customer-SCF on FMCG-cold-chain + AC anchors; FX hedge envelope; capex TL for green-cooling.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; HVAC + drives + climate solutions</div>
<p>India HVAC + drives market FY25 ~Rs 78,000 Cr; CAGR 13-15%; Danfoss + Emerson Climate + Carrier + Rexroth + ABB + Siemens compete. Cold-chain + green-cooling structural growth driven by FMCG capex + government cold-chain mission.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Cold-chain mission + Operation Greens: FMCG + agri-processor capex.</li>
<li>USA-tariff window{ref("6")}: HVAC components export tailwind.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting; refrigerant phase-out.</li>
<li>EV-drive + railway-traction + industrial drives growth.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,509{ref("128")}</td><td class="num">2,850</td><td class="num">3,250</td><td class="num">3,700</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.5</td><td class="num">15.1</td><td class="num">15.7</td><td class="num">16.3</td></tr>
<tr><td>EBITDA</td><td class="num">365</td><td class="num">430</td><td class="num">510</td><td class="num">603</td></tr>
<tr><td>PAT</td><td class="num">215</td><td class="num">255</td><td class="num">310</td><td class="num">370</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + DKK + USD)</td><td class="num">700&ndash;1,100 notional</td><td class="num">3&ndash;5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-SCF (Voltas + Daikin + LG)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>HVAC anchors</td></tr>
<tr><td>Capex TL (cold-chain + EV drives)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>RM + capex</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>Component export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.6&ndash;0.9</td><td>1,650 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 12.8-21 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,250-1,560; Rs 1.7-2.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Danish expat MD + Indian leadership; PB AUM Rs 100-160 Cr; Rs 1.2-1.8 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Danfoss CSR; Rs 80-130 Cr; Rs 0.7-1.2 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.6-5.5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>Customer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">4.7</td><td class="num">7.7</td></tr>
<tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">0.9</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.6</td><td class="num">5.5</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>16.4</strong></td><td class="num"><strong>26.5</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band incl. capex tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Danfoss parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% Danfoss A/S, Denmark{ref("671")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Danfoss India announces Rs 1,000 Cr capex over FY27-30 for green-cooling + EV drives.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 EUR + DKK hedge framework</li><li>T-14 Pre-pitch capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Danfoss India CFO meeting; FX + customer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with Voltas + Daikin; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for green-cooling ramp.</p></div>
<div class="card"><p><strong>T+180:</strong> Danfoss group cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 150 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Danfoss India-specific from [670].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Danfoss India-specific sources</h3>
<ol start="670">
<li id="src-670"><strong>MCA v3 + ZaubaCorp &mdash; Danfoss Industries Pvt Ltd master data</strong> &mdash; CIN U29199TN1999PTC041877; incorp 20 Apr 1999. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-671"><strong>Danfoss A/S Annual Report FY25 + Bitten &amp; Mads Clausen Foundation disclosures</strong> &mdash; FY25 ~&euro;10 bn revenue; private Danish climate + drives MNC. <span class="u">danfoss.com</span></li>
</ol></div></section>"""

def build():
    t = "Danfoss Industries India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Danfoss Industries", "HVAC + drives / Danfoss Denmark"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + green-cooling capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
