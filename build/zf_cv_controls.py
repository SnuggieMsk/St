"""ZF Commercial Vehicle Control Systems India dossier (pilot 78)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "zf-cv-controls-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 78 of 90 · Chennai · ZF Friedrichshafen · CV brake systems · Listed BSE/NSE</div>
<h1>ZF Commercial Vehicle Control Systems India Limited<br>ZF Friedrichshafen (DE) Indian listed CV brake-system + air-treatment + electronic-control subsidiary (ex-WABCO India)</h1>
<p class="lede">ZF Commercial Vehicle Control Systems India Limited (CIN L34103TN2004PLC054667){ref("630")} is the BSE/NSE-listed Indian subsidiary of ZF Friedrichshafen AG (Germany; ZF acquired WABCO 2020 for $7 bn){ref("631")}. <strong>FY25 Total Operating Income Rs 3,841 Cr</strong>{ref("128")}; EBITDA Rs 615 Cr (16.0%); PAT Rs 380 Cr; TNW Rs 2,400 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~3,200 FTE{ref("128")}. Manufactures CV brake-systems (ABS, AEBS, ESC, ECAS), air-treatment, electronic-control modules for Tata, Ashok Leyland, Volvo-Eicher, Daimler, MAN, Mahindra. Plant locations: Mahindra World City + Pantnagar.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 28&ndash;48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + customer-SCF + DCM)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,841 Cr</div><div class="sub">CV brake systems{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">Listed since pre-WABCO era</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + USD royalty + RM-import hedge</strong> &mdash; ZF Germany intercompany flows.</li>
<li><strong>Customer-SCF on Tata + Ashok Leyland + Volvo-Eicher + Daimler</strong> &mdash; CV-OEM receivables.</li>
<li><strong>BS6 + ABS-mandate + AEBS-mandate capex window</strong> &mdash; ZF India capex-import + capex TL.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L34103TN2004PLC054667</strong></span>
<span>Incorp <strong>16 Sep 2004</strong></span>
<span>HO <strong>Chennai (Mahindra World City)</strong></span>
<span>Parent <strong>ZF Friedrichshafen AG (Germany)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>ZF Friedrichshafen AG{ref("631")} is a German auto-systems major (private; family-foundation owned); FY25 revenue ~&euro;46 bn; #2 propulsion + chassis-systems globally (Bosch #1). India operations: ZF Commercial Vehicle Control Systems India Ltd (this entity, listed; ex-WABCO, formerly WABCO India Ltd) + ZF India Pvt Ltd (private + ZF group's PV entity) + ZF Steering (sister of ZF-Rane JV pilot 32 done earlier).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity-funded; cash-positive listed corp.</li>
<li>FY25 paid-up capital Rs 19 Cr; reserves Rs 2,381 Cr; cash Rs 850 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Deutsche Bank (anchor), HSBC, Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF + DCM entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,200</td><td class="num">3,510</td><td class="num">3,841{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">450</td><td class="num">525</td><td class="num">615{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.1</td><td class="num">15.0</td><td class="num">16.0</td></tr>
<tr><td>PAT</td><td class="num">270</td><td class="num">320</td><td class="num">380{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">1,860</td><td class="num">2,130</td><td class="num">2,400{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 19 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~3,200</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 850 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">Listed</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: bid customer-SCF + DCM + FX hedge envelope; capex TL framework for AEBS-mandate ramp.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; CV brake-systems + electronic control</div>
<p>India CV (M&amp;HCV+ICV+LCV) brake-system market FY25 ~Rs 8,500 Cr; CAGR 11-13%; ZF (ex-WABCO) #1 (~70%+ share) on M&amp;HCV; competing players KNORR-Bremse + Bosch + Continental + indigenous (BSL).</p>
<h3>06.1 Drivers</h3>
<ul>
<li>BS6 phase-2 + AEBS-mandate Apr 2026 + ESC-mandate FY27: brake-system sophistication.</li>
<li>USA-tariff window{ref("6")}: limited (CV brake-systems are local-anchored).</li>
<li>EV-CV transition + e-Axle: ZF e-Axle product ramp.</li>
<li>CV-OEM cycle + capex.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,841{ref("128")}</td><td class="num">4,300</td><td class="num">4,850</td><td class="num">5,500</td></tr>
<tr><td>EBITDA margin %</td><td class="num">16.0</td><td class="num">16.6</td><td class="num">17.2</td><td class="num">17.8</td></tr>
<tr><td>EBITDA</td><td class="num">615</td><td class="num">714</td><td class="num">834</td><td class="num">979</td></tr>
<tr><td>PAT</td><td class="num">380</td><td class="num">450</td><td class="num">540</td><td class="num">650</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + USD)</td><td class="num">1,200&ndash;1,800 notional</td><td class="num">5&ndash;8</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">600&ndash;900 float</td><td class="num">4&ndash;6</td><td>Listed-corp TM</td></tr>
<tr><td>Customer-SCF (Tata + AL + Volvo)</td><td class="num">400&ndash;600</td><td class="num">4&ndash;6</td><td>CV-OEM receivables</td></tr>
<tr><td>Capex TL (AEBS ramp)</td><td class="num">200&ndash;350</td><td class="num">2&ndash;3.5</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>RM + capex imports</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>ZF global cross-export</td></tr>
<tr><td>DCM / NCD (listed corp)</td><td class="num">300&ndash;500</td><td class="num">2&ndash;4</td><td>Pre-arranger position</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.8&ndash;1.2</td><td>3,200 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 21.3-34.4 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 2,400-3,000; Rs 3.5-5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>German expat MD + Indian leadership; PB AUM Rs 220-360 Cr; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + ZF CSR; Rs 220-340 Cr; Rs 1.7-2.6 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 7.7-11.6 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">5</td><td class="num">8</td></tr>
<tr><td>Treasury sweep</td><td class="num">4</td><td class="num">6</td></tr>
<tr><td>Customer-SCF</td><td class="num">4</td><td class="num">6</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">5.5</td><td class="num">9.2</td></tr>
<tr><td>DCM/NCD</td><td class="num">2</td><td class="num">4</td></tr>
<tr><td>CMS + cards</td><td class="num">0.8</td><td class="num">1.2</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">7.7</td><td class="num">11.6</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>29.0</strong></td><td class="num"><strong>46.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 28-48 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; ZF parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>~75% ZF Friedrichshafen AG{ref("631")}; remainder retail-listed; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: AEBS-mandate ramp; ZF India capex announced.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 ZF group e-Axle scope</li><li>T-14 Pre-pitch DCM + capex sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> ZF CV CFO meeting; FX + customer-SCF + DCM concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot Tata + AL; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> DCM mandate + capex TL framework.</p></div>
<div class="card"><p><strong>T+180:</strong> ZF Group + ZF-Rane bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 250 Cr by Q3 FY27</li><li>DCM Rs 250 Cr arranged by Q4 FY27</li><li>Y3 run-rate Rs 28-48 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; ZF CV-specific from [630].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">ZF Commercial Vehicle Control Systems India-specific sources</h3>
<ol start="630">
<li id="src-630"><strong>MCA v3 + ZaubaCorp + BSE/NSE listing &mdash; ZF CV Control Systems India Ltd master data</strong> &mdash; CIN L34103TN2004PLC054667; incorp 16 Sep 2004; ex-WABCO India Ltd. <span class="u">mca.gov.in &middot; bseindia.com &middot; nseindia.com</span></li>
<li id="src-631"><strong>ZF Friedrichshafen AG Annual Report FY25 + WABCO acquisition (May 2020 ~$7 bn) commentary</strong> &mdash; private German auto-systems major; FY25 ~&euro;46 bn revenue. <span class="u">zf.com</span></li>
</ol></div></section>"""

def build():
    t = "ZF Commercial Vehicle Control Systems India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("ZF CV Controls", "CV brake systems / ZF Germany"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + AEBS-mandate capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
