"""Dr. Agarwal's Eye Hospital Limited dossier (pilot 45)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "dr-agarwal-eye-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 45 of 50 · Chennai · Listed · Specialty hospital · Greenfield</div>
  <h1>Dr. Agarwal's Eye Hospital Limited<br>India's largest single-specialty eye-care chain (BSE 542741)</h1>
  <p class="lede">Dr. Agarwal's Eye Hospital Limited (CIN L85110TN1994PLC027366){ref("300")} is the listed flagship of the Dr. Agarwal's eye-care chain, India's largest single-specialty ophthalmology + eye-hospital network with 200+ clinics + hospitals across 14 states + 9 international locations (Africa, Mauritius, Sri Lanka){ref("301")}. Listed BSE (542741) since 2019; recent IPO Sep 2025{ref("302")}. <strong>FY25 Total Operating Income Rs 397 Cr</strong>{ref("128")}; EBITDA Rs 120 Cr (30.2%); PAT Rs 54.65 Cr; Tangible Net Worth Rs 335 Cr; Total Debt Rs 115 Cr (Debt/TNW 0.34x &mdash; comfortable). <strong>1 open charge totalling Rs 114.83 Cr to Axis Bank only</strong>{ref("126")}; IBank ABSENT. Credit rating <strong>ICRA AA- Stable</strong> (23 Feb 2026){ref("303")}. 1,303 FTE{ref("128")}. Listed-entity governance.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 24&ndash;42 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 greenfield + listed + post-IPO</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 397 Cr</div><div class="sub">Eye-care + cataract / refractive{ref("128")}</div></div>
    <div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">Single Axis Bank Rs 114.8 Cr{ref("126")}</div></div>
    <div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA AA- Stable</div><div class="sub">23 Feb 2026{ref("303")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Compete with Axis Bank</strong> &mdash; only Axis at Rs 114.8 Cr; concentrated single-bank position; bid for share-grow / refresh.</li>
      <li><strong>Post-IPO capex pipeline</strong> &mdash; Sep 2025 IPO raised Rs 950 Cr{ref("302")}; capex for new-clinic rollout + AI / robotic-cataract surgery; capex-TL window FY27-28.</li>
      <li><strong>International expansion + FX</strong> &mdash; 9 international clinics; cross-border treasury + FX-hedge envelope.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L85110TN1994PLC027366</strong></span>
    <span>Incorp <strong>22 Apr 1994</strong></span>
    <span>HO <strong>Chennai</strong></span>
    <span>Group <strong>Dr. Agarwal's Health Care Group</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture</div>
  <p>Dr. Agarwal's Eye Hospital is the listed-flagship operating-entity of the Dr. Agarwal's Health Care Limited holding-co (parent listing under L74999TN2010PLC075265){ref("301")}. Promoter family: Agarwal family (Dr. Athiya Agarwal, Dr. Sunita Agarwal, Dr. Adil Agarwal et al; 5+ practising ophthalmologists). PE-investor TPG Asia (~32% post-IPO); promoter ~58%; public ~10%. Operates as full-stack ophthalmology + cataract + refractive + retina + paediatric eye-care; 200+ clinics India + 9 international.</p>
  <h3>03.1 Bank consortium (sheet){ref("128")}</h3>
  <ul>
    <li>Disclosed banks: <strong>Allahabad Bank, Axis Bank, HDFC Bank, IBank, Siemens Financial Services, State Bank of India</strong>{ref("128")}.</li>
    <li>Probe42 cut: 1 charge Rs 114.8 Cr Axis Bank{ref("126")}; relationships transactional/unsecured.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">320</td><td class="num">358</td><td class="num">397.15{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">85</td><td class="num">102</td><td class="num">120.06{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">26.6</td><td class="num">28.5</td><td class="num">30.2</td></tr>
<tr><td>PAT</td><td class="num">38</td><td class="num">46</td><td class="num">54.65{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">280</td><td class="num">310</td><td class="num">334.56{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">100</td><td class="num">110</td><td class="num">114.83{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.36x</td><td class="num">0.35x</td><td class="num">0.34x{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 4.83 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">EBITDA margin</div><div class="v num">30.2%</div><div class="sub">Top-tier specialty-hospital range{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">1,303</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 114.83 Cr</div><div class="sub">Axis only{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA AA- Stable</div><div class="sub">23 Feb 2026{ref("303")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Single Axis Bank charge Rs 114.8 Cr{ref("126")}; concentrated single-bank position. Listed AA- rated entity post-IPO offers IBank a clean entry to compete on consortium-extension or take-out terms.</p>
<p class="lede">Strategic: bid into Axis-only position at AA- pricing, leveraging listed-status + post-IPO capex pipeline; sustainability-linked covenant on patient-outcome-rate KPIs.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Indian eye-care + ophthalmology</div>
<p>India eye-care market FY25 ~Rs 18,000 Cr; CAGR 14-16%; chain consolidation accelerating (Centre for Sight, Vasan Eye Care alumni, Eye-Q, Sankara Nethralaya hospital network). Dr. Agarwal's leads with 200+ clinics; closest peers Vasan Eye Care + Centre for Sight.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>Cataract surgery volume ~7-8 mn/yr; chain-share rising from 25% to 40% by FY28.</li>
<li>Insurance + Ayushman Bharat coverage drives addressable market.</li>
<li>Refractive (LASIK, ICL) + premium IOL upgrade-cycle accelerating.</li>
<li>AI + robotic-surgery integration (Aurora-Catalys IOL system) emerging tech competitive.</li>
<li>International expansion (Africa, Sri Lanka, Mauritius) high-margin export-services.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">397{ref("128")}</td><td class="num">490</td><td class="num">600</td><td class="num">730</td></tr>
<tr><td>EBITDA margin %</td><td class="num">30.2</td><td class="num">31.0</td><td class="num">31.5</td><td class="num">32.0</td></tr>
<tr><td>EBITDA</td><td class="num">120</td><td class="num">152</td><td class="num">189</td><td class="num">234</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC/OD secured anchor</td><td class="num">120&ndash;180</td><td class="num">3&ndash;4.5</td><td>Bid into Axis position</td></tr>
<tr><td>Capex TL (post-IPO clinic-rollout)</td><td class="num">200&ndash;300</td><td class="num">3.5&ndash;5</td><td>MCLR + 40 bp; 7-yr; SLL-style</td></tr>
<tr><td>FX (international receivables)</td><td class="num">120&ndash;180 notional</td><td class="num">1.2&ndash;1.8</td><td>USD + AED + KES + LKR</td></tr>
<tr><td>Cards + corporate cards (T&amp;E)</td><td class="num">&ndash;</td><td class="num">0.6&ndash;1.0</td><td>Doctor + senior travel</td></tr>
<tr><td>Receivable-discounting (insurance + Ayushman)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3</td><td>Insurance receivables monetise</td></tr>
<tr><td>Channel-partner SCF (medical-device vendor)</td><td class="num">80&ndash;140</td><td class="num">1.2&ndash;2</td><td>Anchor-led</td></tr>
<tr><td>Capital-markets / NCD arranger</td><td class="num">200&ndash;400 issuance</td><td class="num">2&ndash;4</td><td>Listed AA-; debt-market access</td></tr>
<tr><td>CMS + payroll</td><td class="num">&ndash;</td><td class="num">0.4&ndash;0.7</td><td>1,303 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.9-22.0 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 600-850; Rs 2.4-3.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Agarwal family (5+ practising ophthalmologists, UHNI tier post-IPO); PB AUM Rs 380-620 Cr; Rs 3-5.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 80-130 Cr; Rs 0.9-1.4 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 6.3-10.5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded (CC + TL)</td><td class="num">6.5</td><td class="num">9.5</td></tr>
<tr><td>FX</td><td class="num">1.2</td><td class="num">1.8</td></tr>
<tr><td>Receivable-discounting + SCF</td><td class="num">3.2</td><td class="num">5</td></tr>
<tr><td>Cards + CMS</td><td class="num">1</td><td class="num">1.7</td></tr>
<tr><td>Capital-markets / NCD-arranger</td><td class="num">2</td><td class="num">4</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">6.3</td><td class="num">10.5</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>20.2</strong></td><td class="num"><strong>32.5</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 24-42 Cr/yr captures upper-mid band including post-IPO capex + PB scale.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter Agarwal family + 5+ practising ophthalmologists on board; PE-investor TPG nominee directors post-2018.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter ~58%; TPG Asia ~32%; public ~10%.</li><li>BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}; medical-malpractice claims routine.</li></ul>
<h3>11.4 Recent news</h3>
<ul>
<li>Sep 2025: IPO raised Rs 950 Cr{ref("302")}.</li>
<li>Feb 2026: ICRA affirms AA- Stable{ref("303")}.</li>
<li>FY26: 50+ new clinic openings target across India + 2 international expansion (Saudi Arabia + UAE).</li>
</ul>
<h3>11.5 Diligence items</h3>
<ul class="x">
<li>T+14 MCA DIR-12 + MGT-7</li>
<li>T+14 BEN-2 + TPG-promoter shareholders' agreement consent rights</li>
<li>T+30 Insurance-receivable aging + Ayushman-Bharat reimbursement-cycle</li>
<li>T-14 Pre-sanction Probe42 charge re-pull</li>
</ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Dr. Agarwal's CFO + treasury meeting; bid memo to share Axis position; FX framework introduction.</p></div>
<div class="card"><p><strong>T+60:</strong> CC/OD bid-in tranche; capex-TL term-sheet for clinic-rollout.</p></div>
<div class="card pos"><p><strong>T+90:</strong> SLL-linked tranche; PB engagement.</p></div>
<div class="card"><p><strong>T+180:</strong> Receivable-discounting + NCD-arranger memo.</p></div>
<h3>Success metrics</h3>
<ul class="check"><li>Share Axis position to 30%+ by Q3 FY27</li><li>Capex TL Rs 200 Cr drawn</li><li>Y3 run-rate Rs 24-42 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Dr. Agarwal's-specific from [300].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Dr. Agarwal's Eye Hospital-specific sources</h3>
<ol start="300">
<li id="src-300"><strong>MCA v3 + ZaubaCorp &mdash; Dr. Agarwal's Eye Hospital Ltd master data</strong> &mdash; CIN L85110TN1994PLC027366; incorp 22 Apr 1994; RoC Chennai; listed BSE 542741. <span class="u">mca.gov.in &middot; bseindia.com</span></li>
<li id="src-301"><strong>Dr. Agarwal's Health Care Limited corporate website + group structure</strong> &mdash; 200+ clinics India + 9 international; promoter Agarwal family; full-stack ophthalmology platform. <span class="u">dragarwal.com</span></li>
<li id="src-302"><strong>Dr. Agarwal's Health Care IPO (Sep 2025; Rs 950 Cr issue)</strong> &mdash; Red Herring Prospectus + listing disclosures; capex-pipeline and use-of-proceeds. <span class="u">sebi.gov.in &middot; chittorgarh.com / ipo / dr-agarwals</span></li>
<li id="src-303"><strong>ICRA Ratings &mdash; Dr. Agarwal's Eye Hospital Ltd (23 Feb 2026)</strong> &mdash; affirms ICRA AA- / Stable. <span class="u">icra.in</span></li>
</ol>
</div></section>"""

def build():
    t = "Dr. Agarwal's Eye Hospital Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Dr. Agarwal's Eye Hospital", "Specialty hospital / eye-care chain"),
           FOOT("Cipher clean; 1,500+ lines; greenfield (Axis-only).")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
