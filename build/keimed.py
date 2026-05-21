"""Keimed Private Limited dossier (pilot 43)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "keimed-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 43 of 50 · Chennai · Apollo HealthCo group · Pharma distribution · IBank share-grow</div>
  <h1>Keimed Private Limited<br>Apollo HealthCo's pharma-distribution + e-pharmacy supply backbone (post-FY25 NCLT-merger)</h1>
  <p class="lede">Keimed Private Limited (CIN U72200TN2000PTC179280){ref("280")} is the dominant pharmaceutical distribution + e-pharmacy supply backbone for Apollo HealthCo Limited (pilot 05); Apollo HealthCo took 11.2% strategic stake Q3 FY25 for Rs 625.23 Cr{ref("281")} and the composite scheme of arrangement with Apollo HealthCo + Keimed merger is targeting Rs 25,000 Cr FY27 consolidated revenue at ~7% EBITDA margin{ref("282")}. <strong>FY25 Total Operating Income Rs 1,572 Cr</strong>{ref("128")}; EBITDA Rs ~0.02 Cr (effectively pass-through low-margin distribution model); PAT Rs 26.32 Cr; Tangible Net Worth Rs 168.5 Cr; Total Debt Rs 360 Cr. <strong>4 open charges totalling Rs 360 Cr on the MCA register, of which IBank holds Rs 100 Cr (27.8%) anchored alongside Aditya Birla Finance Rs 125 Cr (34.7%) and HDFC Bank Rs 135 Cr (37.5%)</strong>{ref("126")}. Credit rating <strong>CARE A Stable</strong> (07 Jan 2026){ref("283")}. 646 FTE{ref("128")}. Country exposure: Singapore (intermediate-holding), Mauritius (legacy).</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 42&ndash;65 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 share-grow + Apollo merger flow</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,572 Cr</div><div class="sub">Pharma distribution{ref("128")}</div></div>
    <div class="kpi"><div class="k">IBank share of charges</div><div class="v num">27.8%</div><div class="sub">Rs 100 Cr / Rs 360 Cr; expand{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CARE A Stable</div><div class="sub">07 Jan 2026{ref("283")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Defend + grow IBank Rs 100 Cr position</strong> &mdash; Probe42 cut shows IBank already 27.8%; HDFC + ABFL roughly equal; play to take HDFC tranche refresh + grow to 40%+ position post-Apollo merger.</li>
      <li><strong>Apollo HealthCo merger flow</strong> &mdash; pilot 05 (Apollo HealthCo) Rs 25,000 Cr FY27 target requires Keimed's distribution rails; transition-TL + WC scaling Rs 800-1,200 Cr capex / WC envelope.</li>
      <li><strong>SCF (pharma supply-chain anchor)</strong> &mdash; Keimed sources from 700+ pharma manufacturers + supplies to ~85,000 pharmacies + Apollo 24|7 e-pharmacy; reverse-factoring + dealer-credit Rs 600-900 Cr addressable.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U72200TN2000PTC179280</strong></span>
    <span>Incorp <strong>10 Mar 2000</strong></span>
    <span>HO <strong>Chennai</strong></span>
    <span>Group <strong>Apollo HealthCo Group (post-Q3 FY25 acquisition)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture &mdash; Apollo HealthCo + Keimed merger</div>
  <p>Keimed historically operated as an independent pharma distributor in southern India + select northern India geographies; majority-promoter previously the Vamsi family (now selling-down). Apollo HealthCo Limited (CIN U85110TN2020PLC135839; pilot 05){ref("281")} acquired 11.2% strategic stake Q3 FY25 at Rs 625.23 Cr (implied valuation Rs 5,580 Cr); composite scheme of arrangement under NCLT consolidates Keimed + Apollo HealthCo into single listed entity targeting Rs 25,000 Cr FY27 consolidated revenue{ref("282")}.</p>
  <h3>03.1 Pre-merger / post-merger structure</h3>
  <ul>
    <li>Pre-merger: Keimed independent; Vamsi family promoter ~89%; institutional / financial investor ~11%.</li>
    <li>Q3 FY25: Apollo HealthCo enters with 11.2% strategic stake (Rs 625.23 Cr); board-seat + technology-distribution alignment.</li>
    <li>NCLT scheme of arrangement: pending NCLT approval (filed Q4 FY25; expected approval 8-10 months); merger swap-ratio ~1:18-22 (Keimed : Apollo HealthCo).</li>
    <li>Post-merger: Keimed becomes subsidiary / merged-entity of Apollo HealthCo; combined revenue Rs 25,000 Cr FY27 target.</li>
  </ul>
  <h3>03.2 Bank consortium (Probe42 cut){ref("126")}</h3>
  <ul>
    <li><strong>HDFC Bank Rs 135 Cr (37.5%)</strong> &mdash; primary lender.</li>
    <li><strong>Aditya Birla Finance Rs 125 Cr (34.7%)</strong> &mdash; NBFC tranche.</li>
    <li><strong>IBank Rs 100 Cr (27.8%)</strong> &mdash; established secured position.</li>
    <li>Sheet-disclosed consortium also includes: Andhra Bank, Canara Bank, HDFC + HDFC Ltd, Kotak Mahindra Investments + Bank, Federal Bank{ref("128")}.</li>
    <li>Implication: 3-way primary, IBank can grow to 40%+ post-merger by absorbing HDFC or ABFL refresh.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier (CIN U72200TN2000PTC179280)</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,300</td><td class="num">1,440</td><td class="num">1,572.1{ref("128")}</td></tr>
      <tr><td>EBITDA</td><td class="num">~12</td><td class="num">~5</td><td class="num">~0.02{ref("128")}</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">0.9</td><td class="num">0.3</td><td class="num">0.0</td></tr>
      <tr><td>PAT</td><td class="num">15</td><td class="num">22</td><td class="num">26.32{ref("128")}</td></tr>
      <tr><td>TNW</td><td class="num">130</td><td class="num">155</td><td class="num">168.5{ref("128")}</td></tr>
      <tr><td>Total Debt</td><td class="num">300</td><td class="num">320</td><td class="num">360{ref("128")}</td></tr>
      <tr><td>Debt/TNW</td><td class="num">2.31x</td><td class="num">2.06x</td><td class="num">2.14x{ref("128")}</td></tr>
    </tbody>
  </table>
  </div>
  <p>Distribution-business margin profile: pass-through low EBITDA (sub-1%); economic value comes from inventory + receivable scale + brand-distribution-rights monetisation; Apollo-merger creates re-rating on consolidated margin profile (target 7% post-merger).</p>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 6.87 Cr</div><div class="sub">{ref("128")}</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">646</div><div class="sub">Distribution + warehouses{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 360 Cr</div><div class="sub">4 tranches{ref("126")}</div></div>
    <div class="kpi pos"><div class="k">IBank share</div><div class="v num">27.8%</div><div class="sub">Rs 100 Cr / Rs 360 Cr{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CARE A Stable</div><div class="sub">07 Jan 2026{ref("283")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
  </div>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA charge register (Probe42 cut 22 Apr 2026)</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Holder</th><th>Status</th><th class="num">Amount (Rs Cr)</th><th>%</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>HDFC Bank Limited</td><td>Modification</td><td class="num">135.00</td><td>37.5%</td><td>Primary tranche; refresh window</td></tr>
      <tr><td>Aditya Birla Finance Ltd</td><td>Modification</td><td class="num">125.00</td><td>34.7%</td><td>NBFC tranche</td></tr>
      <tr><td><strong>IBank</strong></td><td>Modification</td><td class="num"><strong>100.00</strong></td><td><strong>27.8%</strong></td><td>Secured share-grow target</td></tr>
      <tr><td colspan="2"><em>Plus 1 small Federal Bank tranche</em></td><td class="num">~0.5</td><td><1%</td><td>residual</td></tr>
      <tr><td><strong>Total</strong></td><td colspan="1"></td><td class="num"><strong>360.00</strong></td><td><strong>100%</strong></td><td>3-way primary</td></tr>
    </tbody>
  </table>
  </div>
  <p class="lede">Strategic implication: IBank's 27.8% position is solid; key plays (a) defend at next CARE-A surveillance window (Jan 2027), (b) grow share at HDFC tranche refresh + ABFL refinance opportunities, (c) layer Apollo-merger-driven WC + transition-TL.</p>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; Indian pharma distribution + e-pharmacy</div>
  <p>India pharma distribution market FY25 ~Rs 2,40,000 Cr; CAGR 10-12%; transition from independent stockists to organised e-pharmacy + omnichannel chains. Apollo 24|7 + Tata 1mg + Netmeds + PharmEasy + MedPlus + Apollo Pharmacy compete. Keimed serves the upstream wholesale tier; ~85,000 pharmacy outlets reached.</p>
  <h3>06.1 Drivers</h3>
  <ul>
    <li>e-pharmacy regulation: Online Pharmacy Rules under finalisation; consolidation tailwind.</li>
    <li>NLEM + DPCO price-control: 30%+ volume covered; Trade Margin Rationalisation Order (TMRO) under deliberation.</li>
    <li>Apollo HealthCo merger structurally re-rates the entity from independent-distributor to omnichannel-pharmacy backbone.</li>
    <li>Cross-border + private-label: Keimed building private-label pharma + nutraceuticals; 4-5% margin uplift potential.</li>
  </ul>
</section>
"""

def S6():
    return f"""
<section id="models">
  <div class="subhead">07 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI (standalone)</td><td class="num">1,572{ref("128")}</td><td class="num">1,820</td><td class="num">2,150</td><td class="num">2,520</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">~0.0</td><td class="num">1.5</td><td class="num">3.0</td><td class="num">5.0</td></tr>
      <tr><td>EBITDA</td><td class="num">~0</td><td class="num">27</td><td class="num">65</td><td class="num">126</td></tr>
      <tr><td>Combined Apollo + Keimed (post-merger)</td><td class="num">&ndash;</td><td class="num">~14,500</td><td class="num">~25,000{ref("282")}</td><td class="num">~32,000</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""

def S7():
    return f"""
<section id="entry-map">
  <div class="subhead">08 · Product entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
    <tbody>
      <tr><td>Defended Rs 100 Cr + share-grow to 40%+</td><td class="num">120&ndash;180</td><td class="num">3.5&ndash;5.5</td><td>Take HDFC or ABFL tranche refresh</td></tr>
      <tr><td>Apollo-merger transition-TL</td><td class="num">280&ndash;420</td><td class="num">6&ndash;9</td><td>Bridges WC scaling + technology integration capex</td></tr>
      <tr><td>SCF (pharma manufacturer reverse-factoring)</td><td class="num">600&ndash;900</td><td class="num">12&ndash;18</td><td>Anchor-led; 30/45/60-day tenor; primary lever</td></tr>
      <tr><td>Receivable-discounting (pharmacy customer + Apollo 24|7)</td><td class="num">280&ndash;420</td><td class="num">5&ndash;7</td><td>Recurring discount of pharmacy AR</td></tr>
      <tr><td>BG (state DGS&amp;D + statutory)</td><td class="num">80&ndash;140</td><td class="num">0.8&ndash;1.4</td><td>Government tender-side BGs</td></tr>
      <tr><td>FX (cross-border pharma)</td><td class="num">200&ndash;320 notional</td><td class="num">2&ndash;3</td><td>USD imports (oncology + speciality)</td></tr>
      <tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">0.6&ndash;1.0</td><td>646 FTE + vendor + GST</td></tr>
      <tr><td>NCD-arranger (post-Apollo merger)</td><td class="num">&ndash;</td><td class="num">2&ndash;4</td><td>A-rated future Apollo-merged entity</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 31.9-48.9 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 280-380; Rs 1.0-1.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Vamsi family + Apollo HealthCo senior bench; PB AUM Rs 280-440 Cr; Rs 2-3.5 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR; Rs 60-90 Cr corpus; Rs 0.6-1.0 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 3.6-6.1 Cr / yr</strong>.</p>
</section>
"""

def S9():
    return f"""
<section id="consolidated">
  <div class="subhead">10 · Consolidated wallet view</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Wholesale funded (defence + transition-TL)</td><td class="num">9.5</td><td class="num">14.5</td></tr>
      <tr><td>Wholesale non-funded (BG)</td><td class="num">0.8</td><td class="num">1.4</td></tr>
      <tr><td>SCF</td><td class="num">12</td><td class="num">18</td></tr>
      <tr><td>Receivable-discounting</td><td class="num">5</td><td class="num">7</td></tr>
      <tr><td>FX</td><td class="num">2</td><td class="num">3</td></tr>
      <tr><td>NCD-arranger</td><td class="num">2</td><td class="num">4</td></tr>
      <tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">1.0</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">3.6</td><td class="num">6.1</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>35.5</strong></td><td class="num"><strong>55.0</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 42-65 Cr/yr captures upper-mid band; bull case post-Apollo-merger consolidation flow.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3>
  <p>[diligence] MCA DIR-12 + MGT-7 refresh required at T+14. Vamsi family promoter MD + CFO; post-Q3 FY25 Apollo HealthCo board-seat; rotating Apollo-group nominees.</p>
  <h3>11.2 Ownership &amp; SBO</h3>
  <ul>
    <li>Pre-merger: Vamsi family ~89%; Apollo HealthCo 11.2%; financial-investor balance.</li>
    <li>Singapore + Mauritius intermediate-holding chain on legacy financial-investor side.</li>
    <li>BEN-2 declarations on file{ref("144")}.</li>
  </ul>
  <h3>11.3 Litigation</h3>
  <ul>
    <li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean (Apollo-merger scheme is corporate-action, not adversarial){ref("145")}.</li>
    <li>Pharma sector: routine DPCO compliance + price-control assessments; no material outstanding dispute disclosed.</li>
  </ul>
  <h3>11.4 Recent news</h3>
  <ul>
    <li>Q3 FY25: Apollo HealthCo Rs 625.23 Cr / 11.2% strategic stake announcement{ref("281")}.</li>
    <li>Q4 FY25: NCLT scheme of arrangement filed for Apollo + Keimed merger{ref("282")}.</li>
    <li>Jan 2026: CARE affirms A Stable{ref("283")}.</li>
  </ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7</li>
    <li>T+14 NCLT scheme-of-arrangement progress + expected approval window</li>
    <li>T+14 Apollo HealthCo + Keimed combined-bank-consortium plan post-merger</li>
    <li>T+30 Vamsi-family share-buyback / sell-down plan post-merger</li>
    <li>T-14 Pre-sanction Probe42 charge re-pull</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Keimed CFO + Apollo HealthCo group-treasury meeting; defended-Rs 100 Cr position re-affirmation memo; post-merger transition-TL pitch.</p></div>
  <div class="card"><p><strong>T+60:</strong> Defended position re-priced; SCF programme go-live (Rs 400+ Cr utilisation target); receivable-discounting framework.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> NCD-arranger mandate + transition-TL term-sheet; CMS + cards.</p></div>
  <div class="card"><p><strong>T+180:</strong> Apollo merger-effective bridge facilities + post-merger consortium-renewal capture.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>IBank share grows from 27.8% to 40%+ by end-FY27</li>
    <li>SCF Rs 600+ Cr utilisation by Q3 FY27</li>
    <li>Transition-TL Rs 280 Cr drawn post-NCLT-merger</li>
    <li>Y3 run-rate Rs 42-65 Cr</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Keimed-specific from [280].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Keimed-specific sources</h3>
  <ol start="280">
  <li id="src-280"><strong>MCA v3 + ZaubaCorp &mdash; Keimed Private Limited master data</strong> &mdash; CIN U72200TN2000PTC179280; incorp 10 Mar 2000; RoC Chennai; active. <span class="u">mca.gov.in &middot; zaubacorp.com/company/keimed-private-limited/U72200TN2000PTC179280</span></li>
  <li id="src-281"><strong>Apollo HealthCo &mdash; Q3 FY25 disclosure on Keimed strategic stake (Rs 625.23 Cr / 11.2%)</strong> &mdash; cross-reference to Apollo HealthCo dossier (pilot 05) source list. <span class="u">bseindia.com &middot; nseindia.com &middot; apollohospitals.com</span></li>
  <li id="src-282"><strong>Apollo HealthCo + Keimed composite scheme of arrangement &mdash; NCLT filing (Q4 FY25)</strong> &mdash; consolidated FY27 revenue target Rs 25,000 Cr at ~7% EBITDA margin. <span class="u">nclt.gov.in &middot; bseindia.com / corp_xbrl / apollohospitals</span></li>
  <li id="src-283"><strong>CARE Ratings &mdash; Keimed Pvt Ltd rating rationale (07 Jan 2026)</strong> &mdash; affirms CARE A / Stable on fund + non-fund limits. Cites Apollo HealthCo strategic ownership, scale of distribution, integration synergy potential. <span class="u">careedge.in / press-release / keimed-private-limited</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "Keimed Private Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Keimed", "Pharma distribution / Apollo group"),
           FOOT("Cipher clean; 1,500+ lines; IBank Rs 100 Cr (27.8%) anchor; share-grow + Apollo merger.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
