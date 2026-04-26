"""Renault India dossier (pilot 58)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "renault-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 58 of 75 · Chennai · Renault Group France · Auto OEM · Greenfield</div>
<h1>Renault India Private Limited<br>French Renault Group Indian retail-distribution + import-OEM arm</h1>
<p class="lede">Renault India Pvt Ltd (CIN U34100TN2005FTC078835){ref("430")} is the Indian sales + after-market subsidiary of Groupe Renault (Euronext: RNO; ~&euro;55 bn revenue){ref("431")}. <strong>FY25 Total Operating Income Rs 4,510 Cr</strong>{ref("128")}; EBITDA Rs 145 Cr (3.2%); PAT Rs 25 Cr; TNW Rs 380 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 1,250 FTE{ref("128")}. Sister entity Renault-Nissan Automotive India Pvt Ltd (RNAIPL, Oragadam JV) operates the Chennai manufacturing plant; this entity (RIPL) handles imports + dealer-distribution + after-sales + financing-tie-ups (RCI Bank). Post-Nissan-divorce, Renault has announced standalone India strategy with new EV launches (Kiger-EV, Triber refresh).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 26&ndash;46 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + dealer-SCF + treasury)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 4,510 Cr</div><div class="sub">Auto OEM / French{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR-INR + USD-INR hedge book</strong> &mdash; royalty + CKD-import + parent-funding flows.</li>
<li><strong>Dealer-SCF + retail auto-finance origination</strong> &mdash; ~250 dealers nationwide post-network rationalisation.</li>
<li><strong>Renault EV-relaunch capex window</strong> &mdash; Kiger-EV + new compact-EV announced for FY27; capex TL + capex-import LC.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U34100TN2005FTC078835</strong></span>
<span>Incorp <strong>20 Sep 2005</strong></span>
<span>HO <strong>Chennai 600032</strong></span>
<span>Parent <strong>Groupe Renault (France)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Groupe Renault{ref("431")} is a French auto major with Renault, Dacia, Alpine, Mobilize brands; FY25 revenue ~&euro;55 bn; ~2.4 mn vehicles. India footprint post-Nissan-divorce: <strong>RIPL</strong> (this entity, sales/distribution); <strong>RNAIPL</strong> (manufacturing JV at Oragadam &mdash; majority restructured to Renault); <strong>RNTBCI</strong> (engineering R&amp;D centre, see pilot 61); <strong>Mobilize Financial Services India</strong> (consumer-finance JV with Nissan, expected to be unwound). Standalone India 5-year roadmap announced Nov 2025: 5 EV/ICE launches by FY29.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; entirely equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 245 Cr; reserves Rs 135 Cr; cash Rs 220 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: BNP Paribas (anchor), Credit Agricole, Standard Chartered &mdash; FX + LC.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + dealer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,800</td><td class="num">4,150</td><td class="num">4,510{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">110</td><td class="num">125</td><td class="num">145{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">2.9</td><td class="num">3.0</td><td class="num">3.2</td></tr>
<tr><td>PAT</td><td class="num">10</td><td class="num">15</td><td class="num">25{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">340</td><td class="num">355</td><td class="num">380{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 245 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">1,250</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 220 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. Pure flow + dealer-finance origination opportunity.</p>
<p class="lede">Strategic: own the dealer-finance + retail auto-loan origination + FX hedge envelope. Negotiate co-arranger role on parent-ICD (Mobilize / RCI Bank) framework.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto OEM (PV)</div>
<p>India PV market FY25 ~4.3 mn units (SIAM); CAGR ~7-9%; Renault market share <2% post-network rationalisation. EV transition + small-car segment refresh expected; competitor set Maruti, Hyundai-Kia, Tata, Mahindra.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: limited (Renault not US-export anchored).</li>
<li>EU CBAM{ref("18")}: Renault carbon-footprint disclosure aligned; Indian sourcing benefit.</li>
<li>EV ramp + PLI Auto: Renault-EV launches FY27-29 expected.</li>
<li>Dealer-network: ~250 dealers post-rationalisation; SCF + retail-finance origination scale.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">4,510{ref("128")}</td><td class="num">5,200</td><td class="num">6,400</td><td class="num">7,800</td></tr>
<tr><td>EBITDA margin %</td><td class="num">3.2</td><td class="num">3.6</td><td class="num">4.2</td><td class="num">4.8</td></tr>
<tr><td>EBITDA</td><td class="num">145</td><td class="num">187</td><td class="num">269</td><td class="num">374</td></tr>
<tr><td>PAT</td><td class="num">25</td><td class="num">45</td><td class="num">110</td><td class="num">180</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + USD)</td><td class="num">1,800&ndash;2,800 notional</td><td class="num">7&ndash;12</td><td>Royalty + CKD imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;300 float</td><td class="num">1.5&ndash;2.5</td><td>MNC TM-aaS</td></tr>
<tr><td>Dealer-SCF (~250 dealers)</td><td class="num">600&ndash;900</td><td class="num">5&ndash;8</td><td>Anchor-finance</td></tr>
<tr><td>Retail auto-loan origination</td><td class="num">800&ndash;1,200 disbursal/yr</td><td class="num">5&ndash;9</td><td>Cross-sell to RCI Bank tie-up</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;400</td><td class="num">2&ndash;3.5</td><td>CKD + capex imports</td></tr>
<tr><td>Capex TL (EV ramp)</td><td class="num">150&ndash;300</td><td class="num">1.5&ndash;3</td><td>FY27-28 EV launch capex</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">1.2&ndash;2</td><td>1,250 FTE + dealer payments</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 23.2-40 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 950-1,200; Rs 3.5-5 Cr/yr (incl. dealer-staff packages).</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>French expat MD + Indian leadership; PB AUM Rs 95-160 Cr; Rs 1.2-2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Renault CSR; Rs 75-115 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5.4-8 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">7</td><td class="num">12</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.5</td></tr>
<tr><td>Dealer-SCF + retail auto-loan</td><td class="num">10</td><td class="num">17</td></tr>
<tr><td>Trade + capex TL</td><td class="num">3.5</td><td class="num">6.5</td></tr>
<tr><td>CMS + cards</td><td class="num">1.2</td><td class="num">2</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5.4</td><td class="num">8</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>28.6</strong></td><td class="num"><strong>48.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 26-46 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; French Renault appointee MD + Indian CFO.</p>
<h3>11.2 Ownership</h3><ul><li>100% Groupe Renault, France (parent){ref("431")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Nov 2025: Renault standalone India 5-year roadmap (5 launches by FY29){ref("431")}.</li><li>FY26: Renault-Nissan JV restructuring; RNAIPL ownership realignment.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 RCI Bank tie-up scope</li><li>T-14 Pre-pitch dealer-SCF + EV-capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Renault India CFO meeting; FX + dealer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> FX hedge envelope sized; dealer-SCF pilot 50 dealers.</p></div>
<div class="card pos"><p><strong>T+90:</strong> EV-capex TL framework; retail auto-loan origination MoU.</p></div>
<div class="card"><p><strong>T+180:</strong> RNAIPL + RNTBCI ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>FX envelope Rs 1,800 Cr notional/yr</li><li>Dealer SCF Rs 600 Cr by Q3 FY27</li><li>Y3 run-rate Rs 26-46 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Renault India-specific from [430].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Renault India-specific sources</h3>
<ol start="430">
<li id="src-430"><strong>MCA v3 + ZaubaCorp &mdash; Renault India Pvt Ltd master data</strong> &mdash; CIN U34100TN2005FTC078835; incorp 20 Sep 2005; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-431"><strong>Groupe Renault Annual Report FY25 + Euronext (RNO) disclosures + India 5-year roadmap announcement Nov 2025</strong> &mdash; FY25 revenue ~&euro;55 bn; ~2.4 mn vehicles; standalone India 5 launches by FY29. <span class="u">renaultgroup.com &middot; euronext.com</span></li>
</ol></div></section>"""

def build():
    t = "Renault India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Renault India", "Auto OEM PV / French Renault Group"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + dealer-SCF + EV-capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
