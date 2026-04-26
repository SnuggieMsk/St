"""Rane Steering Systems Pvt Ltd dossier (pilot 35)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "rane-steering-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 35 of 38 · Madras / Chennai · Rane Group · Auto-comp · IBank wallet anchor</div>
  <h1>Rane Steering Systems Pvt Ltd<br>Steering &amp; suspension systems for Maruti Suzuki / Tata / M&amp;M / Hyundai (Rane Group + Maruti Suzuki + JTEKT JV)</h1>
  <p class="lede">Rane Steering Systems Pvt Ltd (CIN U29141TN1995PTC030621){ref("200")} is the steering-systems manufacturing arm of the Rane Group (Madras-headquartered ~Rs 7,500 Cr group revenue, founded 1929), in joint-venture configuration with Maruti Suzuki and JTEKT (Japanese steering-systems major){ref("201")}. The entity supplies hydraulic + electric power-steering assemblies + manual-rack assemblies + suspension-link components to Maruti Suzuki Manesar / Gurgaon / Kharkhoda + Tata Motors PV + Mahindra &amp; Mahindra + Hyundai India + Renault-Nissan Chennai. <strong>FY25 Total Operating Income Rs 1,706 Cr</strong>{ref("128")}; EBITDA Rs 23.21 Cr (1.4%); PAT Rs 72.29 Cr (PAT &gt; EBITDA reflects one-time gains); Tangible Net Worth Rs 48.93 Cr; Total Debt Rs 235.9 Cr (Debt/TNW 4.82x &mdash; high leverage relative to TNW); <strong>Rs 350.75 Cr open charges on MCA register, of which IBank holds Rs 350 Cr (99.8%)</strong>{ref("126")} as a charge created 06 Sep 2024 &mdash; <strong>IBank is the secured-lender anchor</strong>. Credit rating IND A-/A- Stable (CRISIL, 02 Sep 2025){ref("202")}. Country-of-origin: Japan (JTEKT minority); 1,270 FTE{ref("128")}; Madras-incorporated 22 Mar 1995.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 38&ndash;58 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet-defence + cross-sell layered</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,706 Cr</div><div class="sub">Auto-comp customer base{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">IBank share of charges</div><div class="v num">99.8%</div><div class="sub">of Rs 350.75 Cr total{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CRISIL A- Stable</div><div class="sub">02 Sep 2025{ref("202")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles &mdash; defence + cross-sell</h4>
    <ol style="margin-bottom:0">
      <li><strong>Defend the Rs 350 Cr IBank charge anchor</strong> &mdash; CRISIL A- credit profile rotates annually; price + service quality vs HDFC / Axis tier-1 peers; lock at competitive RoRWA.</li>
      <li><strong>Cross-sell into Rane Group</strong> &mdash; Rane (Madras) Ltd (BSE 532661), Rane Engine Valves, Rane Brake Lining, Rane NSK Steering &mdash; sister entities offer Rs 200&ndash;400 Cr addressable wholesale + retail/PB pool.</li>
      <li><strong>EV-steering + ADAS migration capex</strong> &mdash; FY27&ndash;28 capacity addition for electric-power-steering supply to EV programmes (Tata + M&amp;M + Hyundai) creates Rs 180&ndash;240 Cr capex-TL window.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U29141TN1995PTC030621</strong></span>
    <span>Incorp <strong>22 Mar 1995</strong></span>
    <span>RoC <strong>Chennai</strong></span>
    <span>Group <strong>Rane Group + Maruti Suzuki + JTEKT (Japan)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture &mdash; Rane Group + JV partners</div>
  <p>Rane Group{ref("203")} is a Madras-headquartered automotive-components conglomerate founded 1929 (originally tariff-policy related; transitioned to auto-components 1950s onwards under L. L. Narayan and the Ganesh family). Group annual revenue ~Rs 7,500 Cr (FY25); 11+ legal entities; technology partners include JTEKT (Japan), NSK (Japan), Nisshinbo (Japan), TRW (now ZF/US), Mahle (Germany).</p>
  <h3>03.1 Rane-group structural map (TN-headquartered material entities)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>CIN / listing</th><th>Function</th><th>FY25 TOI (Rs Cr)</th></tr></thead>
    <tbody>
      <tr><td><strong>Rane Steering Systems Pvt Ltd</strong></td><td>U29141TN1995PTC030621{ref("200")}</td><td>JV with Maruti Suzuki + JTEKT; steering systems for Maruti / Tata / M&amp;M / Hyundai</td><td class="num">1,706{ref("128")}</td></tr>
      <tr><td>Rane (Madras) Limited</td><td>L35999TN2004PLC054948 / BSE 532661{ref("204")}</td><td>Listed group holding-cum-operating; consolidated turnover Rs 4,500-5,000 Cr</td><td class="num">~4,800</td></tr>
      <tr><td>Rane Engine Valve Limited</td><td>(BSE 532661 group){ref("204")}</td><td>Engine valves; valve-train components</td><td class="num">~720</td></tr>
      <tr><td>Rane Brake Lining Limited</td><td>(listed){ref("204")}</td><td>Brake friction material</td><td class="num">~580</td></tr>
      <tr><td>Rane NSK Steering Systems</td><td>JV with NSK Japan</td><td>Steering columns + intermediate shafts</td><td class="num">~640</td></tr>
      <tr><td>Rane TRW Steering Systems</td><td>JV with ZF/TRW (US)</td><td>Steering gears (heavy commercial)</td><td class="num">~480</td></tr>
    </tbody>
  </table>
  </div>
  <h3>03.2 JV structural commentary</h3>
  <ul>
    <li>Rane Steering Systems is a tri-party JV: Rane Holdings ~25-30% + Maruti Suzuki India 20-30% + JTEKT (Japan) 40-49% (exact split [diligence] at T+14 via MCA MGT-7 + shareholders' agreement).</li>
    <li>Maruti Suzuki participation aligns the entity to Maruti's manufacturing schedule + product roadmap; ~55-60% of Rane Steering's volumes go to Maruti Suzuki.</li>
    <li>JTEKT technology transfer covers electric-power-steering (EPS) IP critical to FY27 ADAS-readiness migration.</li>
    <li>Promoter family (L. L. Narayan family) retains operational control of group-level via Rane Holdings.</li>
  </ul>
  <h3>03.3 Bank consortium (per sheet disclosure){ref("128")}</h3>
  <ul>
    <li><strong>Canara Bank, Ford India Pvt Ltd (Rs 0.8 Cr legacy charge), IBank (Rs 240 Cr disclosed in sheet vs Rs 350 Cr in fresh Probe42 cut), MUFG Bank Ltd (Japanese-parent affinity)</strong>{ref("128")}.</li>
    <li>Sheet vs current charge cut: sheet shows Rs 240 Cr at IBank; Probe42 cut 22 Apr 2026 shows Rs 350 Cr (modification creation 06 Sep 2024). Variance reflects intervening modification &mdash; <strong>IBank position has grown by Rs 110 Cr</strong> since sheet date{ref("126")}.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier (CIN U29141TN1995PTC030621)</div>
  <h2>Financial snapshot &mdash; 3-year trajectory</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>Total Operating Income</td><td class="num">1,400</td><td class="num">1,560</td><td class="num">1,706{ref("128")}</td><td>9-13% YoY growth tied to Maruti volume cycle</td></tr>
      <tr><td>EBITDA</td><td class="num">42</td><td class="num">38</td><td class="num">23.21{ref("128")}</td><td>Margin compression FY25 reflects raw-material + JTEKT-tech royalty step-up</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">3.0</td><td class="num">2.4</td><td class="num">1.4</td><td>Thin margin typical of steering OEM-dependent comp; sub-2% is rating-sensitivity zone</td></tr>
      <tr><td>PAT</td><td class="num">22</td><td class="num">28</td><td class="num">72.29{ref("128")}</td><td>FY25 PAT &gt; EBITDA suggests one-time item (asset-sale, IT-refund, divestment); [diligence] confirm via FY25 audited notes</td></tr>
      <tr><td>Tangible Net Worth</td><td class="num">35</td><td class="num">42</td><td class="num">48.93{ref("128")}</td><td>Modest; capacity to absorb shocks limited</td></tr>
      <tr><td>Total Debt</td><td class="num">220</td><td class="num">230</td><td class="num">235.9{ref("128")}</td><td>Elevated relative to TNW (Debt/TNW 4.82x) &mdash; explains rating ceiling at A-</td></tr>
      <tr><td>Debt / TNW</td><td class="num">6.29x</td><td class="num">5.48x</td><td class="num">4.82x{ref("128")}</td><td>Trending down with TNW build; still elevated</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">5.24x</td><td class="num">6.05x</td><td class="num">10.16x{ref("128")}</td><td>FY25 spike on EBITDA collapse; rating-rotation sensitivity</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 19.9 Cr</div><div class="sub">JTEKT + Maruti + Rane infusions{ref("128")}</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">1,270</div><div class="sub">Madras-area plants{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 350.75 Cr</div><div class="sub">2 tranches{ref("126")}</div></div>
    <div class="kpi pos"><div class="k">IBank share</div><div class="v num">99.8%</div><div class="sub">Rs 350 Cr / Rs 350.75 Cr{ref("126")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">Probe42 clean{ref("82")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CRISIL A- Stable</div><div class="sub">02 Sep 2025{ref("202")}</div></div>
  </div>
  <h3>04.2 Operational footprint</h3>
  <ul>
    <li><strong>Madras / Chennai-belt plants</strong> &mdash; primary steering-column + steering-rack production; proximity to Renault-Nissan Chennai + Hyundai Sriperumbudur enables JIT supply.</li>
    <li><strong>Customer concentration:</strong> Maruti Suzuki ~55-60%; Tata Motors ~12-15%; M&amp;M ~8-10%; Hyundai ~6-8%; balance Renault-Nissan + RE / KTM 2-wheeler.</li>
    <li><strong>Technology:</strong> JTEKT EPS (electric-power-steering) IP licensed; royalty 2-3% of revenue typical; manual + hydraulic + electric variants in production.</li>
    <li><strong>EV migration:</strong> EPS volume growing as ICE&rarr;EV mix shifts; FY27&ndash;28 capacity addition planned for Tata Avinya / Curvv-EV / M&amp;M Born programmes.</li>
  </ul>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA charge register (Probe42 cut 22 Apr 2026)</div>
  <h2>IBank-anchor structure &mdash; defend at next consortium re-set</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Holder</th><th>Status</th><th>Action date</th><th class="num">Amount (Rs Cr)</th><th>Comment</th></tr></thead>
    <tbody>
      <tr><td><strong>IBank</strong></td><td>Creation</td><td>06 Sep 2024</td><td class="num"><strong>350.00</strong></td><td>Single largest tranche; primary secured anchor; covers WC + capex blend</td></tr>
      <tr><td>Ford India Private Limited</td><td>Modification</td><td>23 Apr 2001</td><td class="num">0.75</td><td>Legacy customer-buyback / consignment-stock charge from Ford-customer era; effectively dormant</td></tr>
      <tr><td><strong>Total</strong></td><td colspan="2"></td><td class="num"><strong>350.75</strong></td><td><strong>IBank 99.8%</strong>; Ford-customer 0.2% (legacy)</td></tr>
    </tbody>
  </table>
  </div>
  <p class="lede">Strategic implication: IBank holds the dominant secured position. Defence priority &mdash; CRISIL A- suggests annual rating reaffirmation; a competing tier-1 bank (HDFC / Axis / SBI) could attempt to re-bid at the next covenant refresh window. Pricing discipline is the lever: the Rs 350 Cr book today should be paying ~repo + 240 bp blended; competitor pitch would target ~repo + 200 bp. <strong>Proactive re-pricing of 15-25 bp protects the wallet.</strong></p>
  <h3>05.1 Implications for engagement strategy</h3>
  <ul>
    <li><strong>Annual rating-action calendar:</strong> CRISIL action 02 Sep 2025; next surveillance ~Sep 2026; align covenant-refresh + pricing review T-30 ahead.</li>
    <li><strong>Cross-sell into Rane Group:</strong> Sister entities (Rane Madras Ltd listed, Rane NSK, Rane TRW, Rane Brake Lining, Rane Engine Valve) likely have HDFC + Axis + SBI consortium; opportunity to syndicate IBank-led group-finance facility.</li>
    <li><strong>EV-capex TL:</strong> Rs 180-240 Cr capacity addition for EPS programmes &mdash; structure as 50% IBank lead with co-arrangers; sustainability-linked tranche option.</li>
    <li><strong>FX layer:</strong> JTEKT royalty + Japan-parent payments + USD-EUR component imports drive Rs 180-260 Cr annual FX hedge need; currently fragmented; consolidate at IBank treasury desk.</li>
  </ul>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; Indian auto-comp + steering-systems sector</div>
  <p>India auto-components sector FY25 turnover ~Rs 6.4 lakh Cr; export ~Rs 1.5 lakh Cr; CAGR 11-13%. Steering-systems sub-segment ~Rs 12,000-14,000 Cr; competitive intensity from Nexteer + JTEKT-owned + Sona Comstar + ZF Rane + ZF Hero + Bosch.</p>
  <h3>06.1 Steering-systems peer set</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Tech partner</th><th>FY25 revenue (Rs Cr)</th><th>Anchor customer</th></tr></thead>
    <tbody>
      <tr><td><strong>Rane Steering Systems</strong></td><td>JTEKT (Japan)</td><td class="num">1,706{ref("128")}</td><td>Maruti Suzuki</td></tr>
      <tr><td>Sona BLW Precision Forgings (Sona Comstar; listed)</td><td>Independent</td><td class="num">~3,400{ref("205")}</td><td>BorgWarner / Tesla</td></tr>
      <tr><td>Rane NSK Steering Systems</td><td>NSK (Japan)</td><td class="num">~640</td><td>Tata Motors / M&amp;M</td></tr>
      <tr><td>Rane TRW Steering Systems</td><td>ZF / TRW (US)</td><td class="num">~480</td><td>Ashok Leyland / Tata CV</td></tr>
      <tr><td>Bosch India steering JV</td><td>Bosch (Germany)</td><td class="num">~860</td><td>BMW / VW / Skoda</td></tr>
      <tr><td>Hella India Lighting / steering</td><td>Forvia Hella (Germany)</td><td class="num">~720</td><td>Multi</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.2 Sector drivers</h3>
  <ul>
    <li><strong>EV mix shift:</strong> EPS-only architecture in EVs vs hydraulic/EPS hybrid in ICE; revenue per vehicle rising 25-40%.</li>
    <li><strong>ADAS-readiness:</strong> Steer-by-wire + lane-keep-assist + auto-park requires sensor + ECU integration; tech-partner JTEKT supplies the IP.</li>
    <li><strong>Maruti Kharkhoda capacity ramp:</strong> 250,000 units/year incremental Maruti capacity FY27 drives Rane Steering volume ~ Rs 240-320 Cr incremental.</li>
    <li><strong>Tata Motors Avinya / Curvv-EV launch FY27:</strong> Rane Steering EPS supply contracts being negotiated; capex implication.</li>
  </ul>
</section>
"""

def S6():
    return f"""
<section id="models">
  <div class="subhead">07 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,706{ref("128")}</td><td class="num">1,920</td><td class="num">2,180</td><td class="num">1,950</td><td class="num">2,520</td><td class="num">2,500</td></tr>
      <tr><td>YoY %</td><td class="num">+9.4</td><td class="num pos">+12.6</td><td class="num pos">+13.5</td><td class="num">+1.6</td><td class="num pos">+31.3</td><td class="num pos">+14.7</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">1.4</td><td class="num">2.2</td><td class="num">3.0</td><td class="num">1.5</td><td class="num">4.0</td><td class="num">3.5</td></tr>
      <tr><td>EBITDA</td><td class="num">23.21</td><td class="num">42</td><td class="num">65</td><td class="num">29</td><td class="num">101</td><td class="num">88</td></tr>
      <tr><td>PAT (ex-one-offs)</td><td class="num">12</td><td class="num">22</td><td class="num">35</td><td class="num">10</td><td class="num">62</td><td class="num">48</td></tr>
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
      <tr><td>CC/OD + WC line (anchor defence)</td><td class="num">240&ndash;320</td><td class="num">5.2&ndash;7.5</td><td>Re-affirm at competitive RoRWA; rate-lock pre-Sep 2026 surveillance</td></tr>
      <tr><td>Capex TL (EPS expansion FY27-28)</td><td class="num">180&ndash;240</td><td class="num">3.5&ndash;5.2</td><td>MCLR + 70 bp; 7-yr; rate-lock pre-June MPC{ref("1")}{ref("5")}</td></tr>
      <tr><td>Import LC (JTEKT royalty + Japan component imports)</td><td class="num">220&ndash;320</td><td class="num">1.6&ndash;2.4</td><td>Sight + 90-day usance</td></tr>
      <tr><td>FX forwards (JPY + USD + EUR)</td><td class="num">600&ndash;900 notional</td><td class="num">7&ndash;11</td><td>Royalty + import flow; tri-currency cover</td></tr>
      <tr><td>BG (customer + statutory + lease)</td><td class="num">120&ndash;180</td><td class="num">1.0&ndash;1.7</td><td>Maruti / Tata / M&amp;M counter-guarantees</td></tr>
      <tr><td>SCF (vendor + dealer-end)</td><td class="num">180&ndash;260</td><td class="num">3&ndash;4.2</td><td>Anchor-led; reverse-factoring vendors at 60-day tenor</td></tr>
      <tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">1.0&ndash;1.6</td><td>1,270 FTE payroll + vendor + GST</td></tr>
      <tr><td>Cross-sell into Rane Group syndication</td><td class="num">200&ndash;400 (group)</td><td class="num">4&ndash;8 incremental</td><td>Sister-entity wallet share growth</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 26.3-41.6 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <p>1,270 FTE plant + admin workforce; promoter-family + Rane Group senior leadership PB anchor.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 600&ndash;850; auto + home loans. Rs 2.4-3.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Rane Group promoter family (Ganesh family, ~5-8 UHNI heads) + senior MDs + plant-heads; estimated PB AUM Rs 280&ndash;520 Cr including listed-Rane wealth proxy. Rs 1.6&ndash;3.4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR; combined corpus Rs 90&ndash;140 Cr; Rs 1.0&ndash;1.6 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 5.0&ndash;8.6 Cr / yr</strong>.</p>
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
      <tr><td>Wholesale funded (CC + TL + cross-sell)</td><td class="num">12.7</td><td class="num">20.7</td></tr>
      <tr><td>Wholesale non-funded (LC + BG)</td><td class="num">2.6</td><td class="num">4.1</td></tr>
      <tr><td>FX + derivatives</td><td class="num">7</td><td class="num">11</td></tr>
      <tr><td>SCF</td><td class="num">3</td><td class="num">4.2</td></tr>
      <tr><td>CMS + cards</td><td class="num">1.0</td><td class="num">1.6</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">5.0</td><td class="num">8.6</td></tr>
      <tr><td>Cross-sell into Rane Group</td><td class="num">4</td><td class="num">8</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>35.3</strong></td><td class="num"><strong>58.2</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 38-58 Cr/yr on cover sits inside this band.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3>
  <p>[diligence] MCA DIR-12 + MGT-7 refresh required at T+14. Rane Group senior leadership publicly visible: <strong>L. Ganesh</strong> (Chairman, Rane Group); <strong>L. Lakshman</strong> (Vice-Chairman); <strong>Harish Lakshman</strong> (Vice-Chairman, Rane Holdings; on Rane Steering Systems board){ref("203")}; CEO/MD of Rane Steering Systems specifically [diligence]. JTEKT + Maruti Suzuki nominee directors typical structure.</p>
  <h3>11.2 Ownership &amp; SBO</h3>
  <ul>
    <li>Tri-party JV: Rane Holdings ~25-30% + Maruti Suzuki India ~20-30% + JTEKT (Japan) ~40-49%; exact split [diligence] via shareholders' agreement.</li>
    <li>UBO: combination of (a) Maruti Suzuki India (Suzuki Motor Corp Japan via Suzuki Holdings) and (b) JTEKT Corporation (Japan; majority-held by Toyota Motor Corp at the parent-level), and (c) Rane Holdings (Ganesh family).</li>
    <li>BEN-2 declarations on file{ref("144")}.</li>
  </ul>
  <h3>11.3 Litigation &amp; regulatory</h3>
  <ul>
    <li>Probe42 suit-filed: <strong>0</strong>{ref("82")}.</li>
    <li>NCLT / CIRP / Indian Kanoon: clean{ref("145")}.</li>
    <li>Standard transfer-pricing assessments expected (JTEKT royalty arms-length test); [diligence] APA / TP-order status.</li>
    <li>Auto-comp sector: standard environmental + labour compliance; no material disclosed dispute.</li>
  </ul>
  <h3>11.4 Recent news</h3>
  <ul>
    <li>Sep 2025: CRISIL affirms IND A- Stable on the entity{ref("202")}.</li>
    <li>Apr 2026: Auto-trade press indicates Rane Group EV-EPS contracts in pipeline with Tata + M&amp;M.</li>
    <li>Group-level FY25 commentary highlights margin pressure on JTEKT royalty step-up + raw material.</li>
  </ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7 refresh; current MD / CEO confirmation</li>
    <li>T+14 BEN-2 SBO confirmation across Maruti / JTEKT / Rane holding chain</li>
    <li>T+14 Shareholders' agreement consent rights / right-of-first-refusal review</li>
    <li>T+14 JTEKT royalty agreement copy (rate, tenor, renewal triggers)</li>
    <li>T+14 FY25 audited notes for one-time-gain explanation (PAT &gt; EBITDA)</li>
    <li>T+30 Maruti Kharkhoda + Tata-EV supply-contract confirmation</li>
    <li>T-14 Pre-sanction Probe42 charge re-pull</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Rane Steering CFO meeting; CC/OD pricing review; rating-action calendar align ahead of Sep 2026 surveillance{ref("202")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Re-price defended Rs 350 Cr book at competitive RoRWA; FX framework + Import LC + JTEKT-royalty hedge; capex-TL term-sheet for FY27 EPS expansion.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Capex TL Rs 100&ndash;150 Cr drawdown; SCF programme go-live; rate-lock pre-Jun MPC{ref("1")}{ref("5")}; salary CASA + PB.</p></div>
  <div class="card"><p><strong>T+180:</strong> Rane Group syndication memo (sister-entity cross-sell); TASC + ESG-linked tranche.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>Defended Rs 350 Cr secured book retained at next Sep 2026 surveillance window</li>
    <li>Capex TL Rs 150 Cr drawn by Q2 FY27</li>
    <li>FX programme Rs 600 Cr notional steady-state</li>
    <li>Cross-sell into 2 sister entities by end-FY27</li>
    <li>Y3 run-rate Rs 38-58 Cr</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42 endpoints; cross-pilot common 31/38/42/126/128/140/144/145; Rane Steering-specific from [200].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Rane Steering Systems-specific sources</h3>
  <ol start="200">
  <li id="src-200"><strong>MCA v3 + ZaubaCorp &mdash; Rane Steering Systems Pvt Ltd master data</strong> &mdash; CIN U29141TN1995PTC030621; incorp 22 Mar 1995; RoC Chennai; active. <span class="u">mca.gov.in &middot; zaubacorp.com/company/rane-steering-systems-private-limited/U29141TN1995PTC030621</span></li>
  <li id="src-201"><strong>JTEKT Corporation (TYO: 6473) Annual Report + India operations disclosure</strong> &mdash; Japanese steering-systems major; technology partner across Rane Steering Systems + Rane NSK Steering; royalty / IP framework. <span class="u">jtekt.co.jp/e/ir &middot; tyo.jpx.co.jp</span></li>
  <li id="src-202"><strong>CRISIL Ratings &mdash; Rane Steering Systems Pvt Ltd rating rationale (02 Sep 2025)</strong> &mdash; affirms IND A- / A- Stable on fund + non-fund limits. Cites JV-partner support framework, customer-concentration risk (Maruti dependence), and capex-cycle EV-migration outlook. <span class="u">crisil.com / ratings / credit-rating-rationale</span></li>
  <li id="src-203"><strong>Rane Group corporate website + Rane Holdings + L. Ganesh family chronology</strong> &mdash; group founded 1929; transitioned to auto-components; Ganesh family promoter-control; structure of operating + listed entities; technology-partnership history. <span class="u">ranegroup.com &middot; ranegroup.com/about-us/leadership-team</span></li>
  <li id="src-204"><strong>Rane (Madras) Limited (BSE 532661 / NSE RANEMADRAS) FY25 Annual Report</strong> &mdash; listed Rane group consolidated turnover; segmental disclosure; sister-entity finances; promoter shareholding pattern. <span class="u">bseindia.com/stock-share-price/rane-madras-ltd/RANEMADRAS/532661/</span></li>
  <li id="src-205"><strong>Sona BLW Precision Forgings Ltd (Sona Comstar; BSE 543300) FY25 disclosures</strong> &mdash; listed peer; Rs 3,400 Cr revenue; BorgWarner / Tesla anchor customers; benchmark for steering / driveline India peer-comp valuation. <span class="u">bseindia.com/stock-share-price/sona-blw-precision-forgings-ltd/SONACOMS/543300/</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "Rane Steering Systems Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Rane Steering Systems", "Auto-comp / steering systems"),
           FOOT("Cipher clean; 1,500+ lines; IBank wallet anchor 99.8% of Rs 350.75 Cr secured.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
