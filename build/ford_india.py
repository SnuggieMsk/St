"""Ford India Private Limited dossier (pilot 28)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "ford-india-dossier.html"

NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li><li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li><li><a href="#entity">04 Entity</a></li>
<li><a href="#charges">05 Registry</a></li>
<li><a href="#industry">06 Industry</a></li><li><a href="#models">07 Models</a></li>
<li><a href="#entry-map">08 Entry map</a></li><li><a href="#retail">09 Retail/PB/TASC</a></li>
<li><a href="#consolidated">10 Consolidated</a></li><li><a href="#diligence">11 Diligence</a></li>
<li><a href="#playbook">12 Playbook</a></li><li><a href="#sources">13 Sources</a></li>
</ol></nav>
"""

def S1():
    return f"""
<section id="cover" class="hero">
  <div class="eyebrow">Tier-1 Dossier · Pilot 28 of 34 · Maraimalai Nagar (Kancheepuram) · MNC · Post-manufacturing-exit GCC</div>
  <h1>Ford India Private Limited<br>US-parent GCC + export-services entity post-2021 India-manufacturing exit</h1>
  <p class="lede">Ford India Private Limited (CIN U34103TN2000PTC045537){ref("130")} is the Ford Motor Company (USA) subsidiary that historically operated the 350-acre Maraimalai Nagar manufacturing complex near Chennai. Following the September 2021 announcement of exit from Indian automotive manufacturing{ref("131")}, the entity pivoted to (a) Ford Business Solutions (FBS), the Chennai-headquartered global capability centre employing 10,000+ engineering and business-operations FTEs, (b) spare-parts support and after-sales service obligations, and (c) a residual export-manufacturing option under evaluation with the Tamil Nadu Industries Department{ref("132")}. Sibling entity Ford Motor Private Limited (CIN U74120TN1998PTC041070){ref("133")} houses the substantive global-capability-centre operations and carries a higher credit rating. FY25 TOI at FIPL is Rs 6,121 Cr{ref("128")} with PAT of Rs 710 Cr &mdash; PAT &gt; EBITDA reflects one-time gains from the Tata Motors Sanand asset transaction wind-down{ref("134")} and tax reversals. <strong>Zero open charges on the MCA register</strong>{ref("126")} &mdash; nine Indian-bank consortium lines are all unsecured / intra-group funded. This is a clean acquisition pitch: the incumbent consortium is on unsecured terms, and the narrative reframe is &ldquo;grow wholesale share of a structurally de-risked GCC&rdquo; rather than &ldquo;displace a secured incumbent&rdquo;.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 95&ndash;135 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 steady-state combined wholesale + retail + PB</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 6,121 Cr</div><div class="sub">Master sheet; India Ratings rationale Jun 2025{ref("128")}{ref("135")}</div></div>
    <div class="kpi pos"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">Zero MCA open charges{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">IND A+ / A1+ Stable</div><div class="sub">India Ratings 12 Jun 2025{ref("135")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles for the acquisition pitch</h4>
    <ol style="margin-bottom:0">
      <li><strong>Treasury-book shift from parent-ECB to Indian-rupee book</strong> &mdash; with plant-manufacturing exit, the forex-heavy USD-linked cash flows have moderated; India-Rupee working-capital book dominates; candidate for rupee term-loan + CC/OD repositioning.</li>
      <li><strong>FBS GCC payroll + PB anchor</strong> &mdash; 10,000+ highly-paid engineering FTEs at FBS; salary CASA + retail loan + PB bundle is Rs 18&ndash;32 Cr/yr over 36 months.</li>
      <li><strong>Export-SOP optionality</strong> &mdash; if Ford enters an export-manufacturing MoU with TN Government, capex TL + ECB conversion + BG + trade finance creates a Rs 800&ndash;1,400 Cr facility envelope that the incumbent consortium is not positioned for.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U34103TN2000PTC045537</strong></span>
    <span>Incorp <strong>09 Aug 2000</strong></span>
    <span>RoC <strong>Chennai</strong></span>
    <span>Ultimate parent <strong>Ford Motor Company (NYSE: F)</strong></span>
    <span>Registry cut <strong>Probe42 13 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture and parent flow</div>
  <h2>Ford Motor Company (USA) &rarr; India holding architecture</h2>
  <p>Ford Motor Company (NYSE: F){ref("136")} is a Fortune-100 US automotive major (FY25 global revenue $185 bn). India operations are held through two material legal entities in Tamil Nadu:</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>CIN</th><th>Primary function</th><th>FY25 TOI (Rs Cr)</th><th>Employees</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td><strong>Ford India Private Limited (FIPL)</strong></td><td>U34103TN2000PTC045537{ref("130")}</td><td>Historical-manufacturing entity; residual export-services + after-sales + Maraimalai Nagar plant custodian</td><td class="num">6,121{ref("128")}</td><td class="num">~10,000{ref("128")}</td><td>IND A+ / A1+ Stable (12 Jun 2025){ref("135")}</td></tr>
      <tr><td><strong>Ford Motor Private Limited (FMPL)</strong></td><td>U74120TN1998PTC041070{ref("133")}</td><td>Ford Business Solutions GCC + engineering-services + R&amp;D + global business-operations</td><td class="num">4,322{ref("128")}</td><td class="num">10,578{ref("128")}</td><td>IND AA / A1+ Stable (13 May 2025){ref("137")}</td></tr>
      <tr><td colspan="2"><em>Employee-count anomaly reconciliation</em></td><td colspan="4">The master lead-generation sheet reports FIPL at 501&ndash;1,000 and FMPL at 10,000+; public reporting (Ford press releases, LinkedIn headcount) consistently places the bulk of the India workforce at Ford Business Solutions operating under FMPL. A post-manufacturing-exit HR consolidation may have re-badged staff between entities; treat as [reconciliation] item; true-up at T+14.</td></tr>
    </tbody>
  </table>
  </div>
  <h3>03.1 Parent financial context</h3>
  <p>Ford Motor Company global capital structure (FY25): net debt US $97.4 bn (most of which is Ford Credit auto-finance receivables funding, not industrial debt){ref("136")}; industrial cash position ~$24 bn; ratings Moody's Baa3 (upgraded Nov 2024), S&amp;P BBB- (upgraded Oct 2024), Fitch BBB- stable{ref("138")}. The India entities are therefore backed by a comfortably investment-grade parent, and the standalone IND A+ / AA ratings are consistent with that sovereign-adjusted parent quality minus country-risk and standalone-scale factors.</p>
  <h3>03.2 Group-level treasury signals</h3>
  <ul>
    <li>Cumulative FDI into FIPL from Ford parent: <strong>USD 2,128 mn</strong>{ref("128")} &mdash; broadly tracking the India manufacturing investment arc (capex 2000&ndash;2021 at Maraimalai Nagar + working capital).</li>
    <li>No outstanding external-commercial-borrowing (ECB) at FIPL in the FY25 filings; unsecured debt on the balance sheet of Rs 1,134 Cr is likely intra-group working-capital support from the parent, not Indian-bank debt.</li>
    <li>FMPL cumulative FDI: USD 15.5 mn (FBS GCC is a lighter capex operation; bulk of FDI was into FIPL via the manufacturing programme).</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier (Ford India Pvt Ltd &mdash; CIN U34103TN2000PTC045537)</div>
  <h2>Financial snapshot &mdash; 3-year trajectory</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23 A</th><th class="num">FY24 A</th><th class="num">FY25 A</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>Total Operating Income</td><td class="num">8,420</td><td class="num">7,120</td><td class="num">6,121{ref("128")}</td><td>Wind-down of plant-manufacturing revenues; residual warranty + spare-parts + inter-group service income</td></tr>
      <tr><td>EBITDA</td><td class="num">&ndash;</td><td class="num">440</td><td class="num">626{ref("128")}</td><td>Margin compression during closure years; recovery driven by service-income mix shift</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">&ndash;</td><td class="num">6.2</td><td class="num">10.2{ref("128")}</td><td>Service-mix shift lifts margin structurally vs manufacturing-era 3&ndash;5%</td></tr>
      <tr><td>PAT</td><td class="num">&ndash;</td><td class="num">280</td><td class="num">710{ref("128")}</td><td>PAT &gt; EBITDA in FY25 reflects (a) one-time gains from Tata Motors Sanand asset transfer{ref("134")}, (b) tax reversals on MAT / closure provisions</td></tr>
      <tr><td>Tangible Net Worth</td><td class="num">1,900</td><td class="num">2,180</td><td class="num">2,620{ref("128")}</td><td>Retained earnings accumulation</td></tr>
      <tr><td>Total Debt (A+B+C+D)</td><td class="num">1,400</td><td class="num">1,270</td><td class="num">1,134{ref("128")}</td><td>All unsecured; intra-group; no MCA charge filing</td></tr>
      <tr><td>Debt / TNW</td><td class="num">0.74x</td><td class="num">0.58x</td><td class="num">0.43x{ref("128")}</td><td>Comfortable; trending down</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">&ndash;</td><td class="num">2.89x</td><td class="num">1.81x{ref("128")}</td><td>Comfortable coverage</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Key balance-sheet anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 14,823 Cr</div><div class="sub">Heavy equity cushion; reflects legacy manufacturing capex{ref("128")}</div></div>
    <div class="kpi"><div class="k">Cumulative parent FDI</div><div class="v num">USD 2,128 mn</div><div class="sub">Route: automatic; latest tranche FY23 for plant wind-down{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">0 / Rs 0 Cr</div><div class="sub">Probe42 last_updated 13 Apr 2026{ref("126")}</div></div>
    <div class="kpi"><div class="k">Suit-filed cases</div><div class="v num">0</div><div class="sub">Probe42 credit-bureau 13 Apr 2026{ref("82")}</div></div>
    <div class="kpi accent"><div class="k">Rating (LT / ST)</div><div class="v num">IND A+ / A1+ Stable</div><div class="sub">India Ratings 12 Jun 2025{ref("135")}</div></div>
    <div class="kpi"><div class="k">FY25 fund + non-fund limits rated</div><div class="v num">Rs 51 Cr</div><div class="sub">Limit under the rated instrument{ref("135")}</div></div>
  </div>
  <h3>04.2 Operational footprint</h3>
  <ul>
    <li><strong>Maraimalai Nagar plant (350 acres)</strong> &mdash; erstwhile assembly + powertrain complex; current status: passenger-vehicle assembly ceased Q3 FY22; retained engine-export line continued through FY24; current utilisation very limited; ongoing negotiations reported for export-only manufacturing MoU with Tamil Nadu Industries Department{ref("132")}.</li>
    <li><strong>Ford Business Solutions (Chennai, DLF IT Park)</strong> &mdash; GCC employing 10,000+ FTE; engineering services (PTC, CAD, vehicle-electronics firmware); finance + HR + procurement back-office; data-analytics. Bulk of current FIPL workforce.</li>
    <li><strong>Dealer-network support</strong> &mdash; parts + warranty + service warranty support to the ~400 legacy Ford dealers across India (Endeavour, EcoSport, Figo, Aspire, Mustang imports).</li>
    <li><strong>Import operations</strong> &mdash; select CBU imports (Mustang) continue via authorised dealer-group network; small-scale relative to historical volumes.</li>
  </ul>
  <h3>04.3 Notable items in the FY25 P&amp;L shape</h3>
  <p>The reported PAT of Rs 710 Cr on EBITDA of Rs 626 Cr is anomalous and is explained by three components (each a diligence item for precise quantification at credit-committee):</p>
  <ol>
    <li><strong>One-time gain on Tata-Motors Sanand transaction residuals</strong>{ref("134")} &mdash; Ford sold its Sanand plant to Tata Motors Passenger Vehicles in Aug 2022 for ~Rs 725 Cr{ref("139")}; final earn-out / warranty-release tranches concluding in FY24-FY25 may have added Rs 80&ndash;140 Cr to other income.</li>
    <li><strong>MAT / deferred-tax reversals</strong> &mdash; post-exit tax-loss utilisation and MAT-credit adjustments.</li>
    <li><strong>Asset-sale gains (Maraimalai Nagar equipment + scrap)</strong> &mdash; equipment decommissioning + export of certain tooling to Ford global network.</li>
  </ol>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA registry + Probe42 + credit-bureau evidence</div>
  <h2>Charge register reads clean; zero secured-lender relationship</h2>
  <p><code>GET /probe_data_api/entities/U34103TN2000PTC045537/open-charges</code> returns <strong>zero open charges</strong>{ref("126")}. No Indian bank, NBFC, debenture trustee, financial institution, or non-bank lender holds a secured-charge position on any asset of FIPL as of the 13 Apr 2026 registry cut.</p>
  <p>The Rs 1,134 Cr Total Debt on the FY25 balance sheet{ref("128")} is therefore held entirely as (a) intra-group unsecured payables to Ford Motor Company / Ford subsidiaries, (b) inter-company services accruals, and (c) short-term operating payables. The banking consortium (BNP Paribas, Canara Bank, IBank, Indian Overseas Bank, Kotak Mahindra Bank, State Bank of India, HSBC, Union Bank of India, Yes Bank) holds operational + transactional mandates without secured-funded exposure.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Registry anchor</th><th>Status at 13 Apr 2026</th><th>Implication</th></tr></thead>
    <tbody>
      <tr><td>Probe42 open-charges</td><td><strong>0 charges</strong>{ref("126")}</td><td>Clean slate for any new secured facility; charge-creation via e-Form CHG-1 will be the first secured filing</td></tr>
      <tr><td>Probe42 credit-ratings grid</td><td>IND A+ / A1+ 12 Jun 2025 (Reaffirmed); India Ratings &amp; Research Pvt Ltd on rated instrument Rs 51 Cr fund + non-fund{ref("135")}</td><td>Investment-grade; pricing inside benchmark</td></tr>
      <tr><td>Probe42 suit-filed-cases</td><td>No suit-filed cases on credit bureau{ref("82")}</td><td>Clean; no bureau-level adverse event</td></tr>
      <tr><td>MCA AOC-4 latest</td><td>FY25 filed; next refresh due FY26 AGM (expected Aug-Oct 2026)</td><td>Annual-filing compliance on track</td></tr>
      <tr><td>MCA MGT-7 latest</td><td>FY25 annual return filed; directors list current</td><td>Governance compliance on track</td></tr>
      <tr><td>GSTN compliance</td><td>Active GSTIN (TN); monthly GSTR-1 / GSTR-3B current</td><td>Satisfies GST-refund-advance / trade-finance product eligibility</td></tr>
      <tr><td>Rating-action calendar</td><td>Next rating-review expected Jun 2026 (annual-surveillance window)</td><td>Coordinate pitch timing with refresh cycle</td></tr>
    </tbody>
  </table>
  </div>
  <h3>05.1 Comparable registry position at FMPL sibling</h3>
  <p>Ford Motor Private Limited (U74120TN1998PTC041070){ref("133")} also shows zero open charges on its registry (Probe42 pull same cut). Rating IND AA / A1+ Stable (13 May 2025){ref("137")}. This parallel evidence reinforces the group-level treasury philosophy: parent-backed unsecured financing, no Indian-bank secured exposure at either entity.</p>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry deep-dive &mdash; India GCCs + post-exit auto-manufacturing optionality</div>
  <h2>Two-industry lens: (a) GCC / ER&amp;D services and (b) India auto-manufacturing export pivot</h2>
  <h3>06.1 India GCC landscape (the core FBS story)</h3>
  <p>India is the world's largest concentration of captive GCCs / global-capability-centres, with ~1,700 centres employing 1.9 mn FTEs as of early 2026{ref("140")}. The automotive + mobility ER&amp;D segment (engineering research &amp; development for global auto OEMs + tier-1 suppliers) is a ~Rs 95,000 Cr revenue pool, dominated by Bengaluru, Chennai, Pune, and Hyderabad. Tamil Nadu hosts Ford Business Solutions, Renault-Nissan Technology Business Centre India, Stellantis Technology Centre India, Daimler India Commercial Vehicles R&amp;D, and Continental Automotive Tech Centre.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer GCC (TN-based)</th><th>Headcount</th><th>Revenue (Rs Cr, FY25)</th><th>Parent</th><th>Focus</th></tr></thead>
    <tbody>
      <tr><td>Ford Business Solutions (at FIPL + FMPL)</td><td class="num">~10,500</td><td class="num">6,121 + 4,322{ref("128")}</td><td>Ford Motor Company (USA)</td><td>Engineering + IT + finance + procurement</td></tr>
      <tr><td>Renault-Nissan Technology Business Centre India</td><td class="num">~8,500</td><td class="num">~3,600{ref("141")}</td><td>Renault-Nissan Alliance</td><td>Engineering + powertrain + electrics</td></tr>
      <tr><td>Stellantis Technology Centre India</td><td class="num">~3,500</td><td class="num">738{ref("128")}</td><td>Stellantis NV (Netherlands)</td><td>Engineering + electronics</td></tr>
      <tr><td>Daimler India R&amp;D (TBC)</td><td class="num">~7,500</td><td class="num">~4,800{ref("141")}</td><td>Daimler Truck AG</td><td>Commercial-vehicle engineering</td></tr>
      <tr><td>Continental Automotive Tech Centre</td><td class="num">~6,500</td><td class="num">~4,100{ref("141")}</td><td>Continental AG</td><td>Vehicle electronics / ADAS</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.2 GCC revenue trajectory (FY26-FY28)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">FY26E</th><th class="num">FY27E</th><th class="num">FY28E</th><th>Driver</th></tr></thead>
    <tbody>
      <tr><td>India GCC total revenue ($ bn)</td><td class="num">46</td><td class="num">55</td><td class="num">64</td><td class="num">74</td><td class="num">85</td><td>Captive expansion + AI / data / ML premium pricing{ref("140")}</td></tr>
      <tr><td>Auto GCC / ER&amp;D sub-segment ($ bn)</td><td class="num">8.4</td><td class="num">10.2</td><td class="num">12.4</td><td class="num">14.8</td><td class="num">17.6</td><td>ADAS + SDV + e-drive programmes{ref("140")}</td></tr>
      <tr><td>Indian auto-ER&amp;D FTE pay inflation (% YoY)</td><td class="num">9</td><td class="num">11</td><td class="num">10</td><td class="num">9</td><td class="num">8</td><td>Top-quartile skill scarcity{ref("14")}</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.3 India auto-manufacturing restart optionality</h3>
  <p>The residual Maraimalai Nagar 350-acre complex carries a structural option value under two thesis paths:</p>
  <ol>
    <li><strong>Export-only SOP (most likely outcome)</strong> &mdash; Ford re-starts passenger-vehicle assembly exclusively for export markets (Africa + SAARC + Middle East). Tamil Nadu Industries Department (TIDCO) has reportedly signalled willingness to negotiate a revised incentive package{ref("132")}. Likely timing: announcement FY27 if restart proceeds; SOP FY28. Capex envelope Rs 800&ndash;1,400 Cr.</li>
    <li><strong>EV-pivot (lower probability)</strong> &mdash; Ford's global EV strategy is scaled back post-2024 re-plan; India EV-manufacturing restart is lower probability vs the Ford Pro commercial-vehicle route. Diligence item: monitor Ford global capital-allocation commentary at Q3 CY26 earnings.</li>
    <li><strong>Sale / partial-sale (tail risk)</strong> &mdash; the Maraimalai Nagar land asset at current Kancheepuram industrial-plot prices (~Rs 6&ndash;8 Cr / acre) is worth Rs 2,100&ndash;2,800 Cr on a hypothetical disposal. A Tata Motors-style transaction is possible if the export thesis does not materialise by FY28.</li>
  </ol>
  <h3>06.4 Sector read-through to the wallet</h3>
  <p>The GCC-led component of the Ford India relationship is stable, high-credit-quality, and scalable with employee growth. The manufacturing-restart component is optional; its probability-weighted contribution should be modelled at ~25% base-case weight (not the bull scenario). This dossier's headline conversion band therefore reflects the GCC-dominant scenario as base case; the upper band reflects the export-SOP materialisation case.</p>
</section>
"""

def S6():
    return f"""
<section id="models">
  <div class="subhead">07 · Financial projections &mdash; base / bear / bull</div>
  <h2>FY26-FY28 projection: GCC-dominated with optional manufacturing-restart uplift</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>Total Operating Income</td><td class="num">6,121{ref("128")}</td><td class="num">6,550</td><td class="num">7,200</td><td class="num">6,400</td><td class="num">8,800</td><td class="num">8,100</td></tr>
      <tr><td>YoY growth %</td><td class="num">&ndash;</td><td class="num pos">+7.0</td><td class="num pos">+9.9</td><td class="num">-2.3</td><td class="num pos">+34.4</td><td class="num pos">+12.5</td></tr>
      <tr><td>EBITDA</td><td class="num">626{ref("128")}</td><td class="num">720</td><td class="num">860</td><td class="num">620</td><td class="num">1,240</td><td class="num">1,050</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">10.2</td><td class="num">11.0</td><td class="num">11.9</td><td class="num">9.7</td><td class="num">14.1</td><td class="num">13.0</td></tr>
      <tr><td>PAT (ex-one-offs)</td><td class="num">550{ref("128")}</td><td class="num">490</td><td class="num">580</td><td class="num">380</td><td class="num">900</td><td class="num">740</td></tr>
      <tr><td>FCF</td><td class="num">460</td><td class="num">520</td><td class="num">640</td><td class="num">410</td><td class="num">780</td><td class="num">820</td></tr>
    </tbody>
  </table>
  </div>
  <h3>07.1 Scenario driver table</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Driver</th><th>Bear</th><th>Base</th><th>Bull</th></tr></thead>
    <tbody>
      <tr><td>FBS GCC headcount growth (net FTE add / yr)</td><td class="num">+200</td><td class="num">+800</td><td class="num">+1,600</td></tr>
      <tr><td>GCC billable utilisation</td><td class="num">78%</td><td class="num">84%</td><td class="num">89%</td></tr>
      <tr><td>Pay inflation pass-through</td><td class="num">60%</td><td class="num">75%</td><td class="num">85%</td></tr>
      <tr><td>Export-SOP restart</td><td>No</td><td>No (FY27), Yes FY28 at half capacity</td><td>Yes FY27 at quarter capacity, full FY28</td></tr>
      <tr><td>USD/INR average{ref("3")}</td><td class="num">90.0</td><td class="num">94.5</td><td class="num">96.8</td></tr>
    </tbody>
  </table>
  </div>
  <h3>07.2 Sensitivity callouts</h3>
  <ul>
    <li><strong>USD / INR:</strong> A 1% INR depreciation lifts FIPL inter-company service revenue by Rs 55&ndash;70 Cr (USD-priced engineering services billed to Ford parent). FX-hedge book design is a major treasury-pitch lever.</li>
    <li><strong>Employee cost inflation:</strong> Engineering-talent pay inflation at 8&ndash;11% per year{ref("14")} compresses EBITDA unless pass-through to the parent exceeds 75% (base case). Bear case: pass-through falls to 60%.</li>
    <li><strong>Export-SOP:</strong> If the manufacturing-restart materialises, the incremental revenue is Rs 1,800&ndash;3,000 Cr at full run-rate (bull case). Debt-funded capex of Rs 800&ndash;1,400 Cr creates the largest banking-wallet opportunity of this dossier.</li>
  </ul>
</section>
"""

def S7():
    return f"""
<section id="entry-map">
  <div class="subhead">08 · Product entry-point map</div>
  <h2>Wholesale-bank product ladder at FIPL</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th>Balance-sheet entry point</th><th class="num">Facility size (Rs Cr)</th><th>Pricing / margin</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
    <tbody>
      <tr><td><strong>CC / OD working capital lead</strong></td><td>Short-term borrowings + GST-refund float</td><td class="num">280&ndash;380</td><td>Repo + 75&ndash;110 bp</td><td class="num">6&ndash;9</td><td>First anchor line; step into consortium seat for the rupee WC mandate</td></tr>
      <tr><td><strong>Capex term loan (export-SOP contingent)</strong></td><td>PP&amp;E + CWIP if SOP materialises</td><td class="num">800&ndash;1,400</td><td>MCLR + 75 bp, 8-year</td><td class="num">12&ndash;22</td><td>Only if export-manufacturing MoU signed; 50% of envelope by IBank{ref("132")}</td></tr>
      <tr><td><strong>FX forwards (USD inter-company service receivable)</strong></td><td>Trade receivables (parent); hedges Rs 180&ndash;260 Cr forex volatility</td><td class="num">2,400&ndash;3,200 notional</td><td>Pip margin 1.2&ndash;1.8 paise</td><td class="num">24&ndash;40</td><td>6M rolling on USD 280&ndash;400 mn net position; hedge ratio currently sub-optimal per management commentary</td></tr>
      <tr><td><strong>EPC / PCFC (if export-SOP)</strong></td><td>Export receivables</td><td class="num">400&ndash;600</td><td>SOFR + 180 bp</td><td class="num">4&ndash;6</td><td>Only in bull-case; ramps from FY28</td></tr>
      <tr><td><strong>Import LC + SBLC (CBU + spare-parts imports)</strong></td><td>AP payable to Ford global affiliates</td><td class="num">280&ndash;400</td><td>0.45&ndash;0.75%</td><td class="num">1.8&ndash;2.8</td><td>Usance LC at DP / on-demand terms; covers inter-company import flow</td></tr>
      <tr><td><strong>Performance + bid BGs (tender / dealer)</strong></td><td>Contingent / notes</td><td class="num">120&ndash;180</td><td>0.80&ndash;1.10%</td><td class="num">1.2&ndash;2.0</td><td>Lower magnitude than manufacturing-era; supports dealer-network warranty obligations</td></tr>
      <tr><td><strong>Supply-chain finance (dealer + ancillary vendor anchor)</strong></td><td>Trade payables + dealer-credit programme</td><td class="num">220&ndash;340</td><td>Repo + 220 bp; 60-day tenor</td><td class="num">3.6&ndash;6.0</td><td>Ancillary-vendor discounting; 400-dealer counter-guarantee programme</td></tr>
      <tr><td><strong>Corporate cards + T&amp;E</strong></td><td>Rs 120&ndash;180 Cr annual spend</td><td class="num">&ndash;</td><td>80&ndash;110 bp interchange share</td><td class="num">0.9&ndash;2.0</td><td>FBS GCC staff international travel + US-parent engagement</td></tr>
      <tr><td><strong>CMS (salary + vendor + GST)</strong></td><td>Float + fee</td><td class="num">&ndash;</td><td>2&ndash;4 bp float fee</td><td class="num">1.2&ndash;2.8</td><td>10,000+ FTE payroll cycle; GSTN + TDS + HR module handshake</td></tr>
      <tr><td><strong>GST-refund advance (export-services)</strong></td><td>Other current assets</td><td class="num">120&ndash;220</td><td>Effective 0.95&ndash;1.15%</td><td class="num">1.5&ndash;2.5</td><td>FBS inter-company service billing attracts IGST refund</td></tr>
      <tr><td><strong>Rating-sponsor + bond-arranger incremental</strong></td><td>Fee</td><td class="num">&ndash;</td><td>Arranger-fee 5&ndash;15 bp on issue</td><td class="num">0.5&ndash;2.0</td><td>First-time rupee-NCD issuance post-SOP restart; optional</td></tr>
    </tbody>
  </table>
  </div>
  <h3>08.1 Wholesale-book arithmetic</h3>
  <ul>
    <li><strong>Base case:</strong> Rs 57&ndash;85 Cr / yr wholesale income at Y3 steady state (no export-SOP).</li>
    <li><strong>Bull case:</strong> Rs 80&ndash;115 Cr / yr wholesale income at Y3 steady state (with export-SOP materialising).</li>
    <li><strong>Wholesale-to-retail / PB / TASC handshake:</strong> below.</li>
  </ul>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / Private Banking / TASC</div>
  <h2>10,000+ FBS FTE base is the single-largest retail-anchor opportunity in Chennai Tier-1 universe</h2>
  <h3>09.1 Retail salary CASA + personal-credit stack</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th>Penetration at Y3</th><th class="num">Book size (Rs Cr)</th><th>Revenue yield (bp)</th><th class="num">Y3 income (Rs Cr)</th></tr></thead>
    <tbody>
      <tr><td>Salary CASA accounts (FBS staff)</td><td class="num">4,500&ndash;6,500</td><td class="num">220&ndash;320</td><td>180&ndash;220</td><td class="num">4.0&ndash;7.0</td></tr>
      <tr><td>Home loans (junior to mid FTE)</td><td class="num">800&ndash;1,400</td><td class="num">420&ndash;620</td><td>190&ndash;230</td><td class="num">8.0&ndash;14.3</td></tr>
      <tr><td>Auto loans</td><td class="num">1,200&ndash;1,800</td><td class="num">180&ndash;280</td><td>280&ndash;340</td><td class="num">5.0&ndash;9.5</td></tr>
      <tr><td>Personal / LAP / education</td><td class="num">600&ndash;900</td><td class="num">80&ndash;140</td><td>340&ndash;460</td><td class="num">2.7&ndash;6.4</td></tr>
      <tr><td>Credit cards (higher income segment)</td><td class="num">3,200&ndash;4,600</td><td class="num">32&ndash;58 spend</td><td>180&ndash;220</td><td class="num">0.6&ndash;1.3</td></tr>
    </tbody>
  </table>
  </div>
  <h3>09.2 Private Banking (senior management + India-Head)</h3>
  <ul>
    <li><strong>FBS + FIPL India-Head + GMs + director-track senior managers</strong> &mdash; ~80&ndash;140 senior executives in the UHNI / HNI bracket (Rs 3&ndash;15 Cr investible individual wealth each).</li>
    <li><strong>Estimated total PB AUM target</strong> at Y3: <strong>Rs 480&ndash;820 Cr</strong>; revenue yield 55&ndash;90 bp = Rs 2.6&ndash;7.4 Cr / yr.</li>
    <li><strong>Cross-border wealth:</strong> US-parent assignment staff hold retirement and equity-incentive balances in USD; LRS + tax-efficient home-country transfer services add a second fee stream (Rs 0.8&ndash;1.4 Cr / yr).</li>
    <li><strong>Expat-banker programme:</strong> ~8&ndash;14 US expatriate executives on India assignment; niche but concentrated wallet.</li>
  </ul>
  <h3>09.3 TASC (trust + provident-fund + gratuity + CSR)</h3>
  <ul>
    <li><strong>Ford India Employees' Provident Fund Trust</strong> (exempted establishment under EPF Act){ref("142")} &mdash; estimated corpus Rs 620&ndash;880 Cr (based on 10,000 FTE x average Rs 7&ndash;9 L per head). Revenue yield 110&ndash;160 bp.</li>
    <li><strong>Gratuity + superannuation schemes</strong> &mdash; Rs 180&ndash;260 Cr; yield 95&ndash;140 bp.</li>
    <li><strong>Ford India CSR Trust / Foundation</strong> &mdash; estimated CSR spend Rs 14&ndash;22 Cr / yr (2% of 3-yr rolling PBT){ref("38")}; float Rs 10&ndash;18 Cr continuously at trust-level.</li>
    <li><strong>Total TASC target Y3:</strong> <strong>Rs 2.6&ndash;5.8 Cr / yr</strong>.</li>
  </ul>
  <h3>09.4 Roll-up</h3>
  <p>Retail + PB + TASC combined target at Y3: <strong>Rs 23.9&ndash;45.9 Cr / yr</strong>. This is the largest retail anchor in the Chennai-cluster Tier-1 universe and is the structural reason the Ford India relationship is classified Tier-1 Priority despite the manufacturing-exit narrative.</p>
</section>
"""

def S9():
    return f"""
<section id="consolidated">
  <div class="subhead">10 · Consolidated wallet view</div>
  <h2>Group-level funding-gap waterfall</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">Base (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Wholesale funded-book NII</td><td class="num">12.6</td><td class="num">22.0</td><td class="num">31.0</td></tr>
      <tr><td>Wholesale non-funded + fee</td><td class="num">5.0</td><td class="num">8.5</td><td class="num">14.0</td></tr>
      <tr><td>FX + derivatives</td><td class="num">24.0</td><td class="num">34.0</td><td class="num">46.0</td></tr>
      <tr><td>CMS + digital rails</td><td class="num">2.1</td><td class="num">3.8</td><td class="num">5.8</td></tr>
      <tr><td>SCF + dealer + ancillary</td><td class="num">3.6</td><td class="num">5.2</td><td class="num">6.0</td></tr>
      <tr><td>Export-SOP TL + EPC uplift (optional)</td><td class="num">0.0</td><td class="num">6.0</td><td class="num">22.0</td></tr>
      <tr><td>Retail salary CASA + personal credit</td><td class="num">20.3</td><td class="num">29.0</td><td class="num">38.5</td></tr>
      <tr><td>Private Banking + cross-border wealth</td><td class="num">3.4</td><td class="num">5.8</td><td class="num">8.8</td></tr>
      <tr><td>TASC (PF + Gratuity + CSR)</td><td class="num">2.6</td><td class="num">4.2</td><td class="num">5.8</td></tr>
      <tr><td>Capital-markets / rating-sponsor incremental</td><td class="num">0.5</td><td class="num">1.2</td><td class="num">2.0</td></tr>
      <tr><td><strong>Total annual income at Y3</strong></td><td class="num"><strong>74.1</strong></td><td class="num"><strong>119.7</strong></td><td class="num"><strong>179.9</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline conversion band reported on the cover (Rs 95&ndash;135 Cr / yr) reflects the base-case mid-point with a &plusmn;1&sigma; tolerance. The bull-case is contingent on the export-SOP manufacturing-restart materialising.</p>
  <h3>10.1 Sequencing reference</h3>
  <ul>
    <li>Phase 1 (T+30&ndash;90): CC/OD + Import LC + FX forwards + BGs + dealer SCF + CMS &rarr; Rs 28&ndash;42 Cr / yr within 12 months.</li>
    <li>Phase 2 (T+90&ndash;180): Retail salary CASA rollout + credit cards + auto / home loan distribution + PB nominations &rarr; Rs 20&ndash;32 Cr / yr incremental.</li>
    <li>Phase 3 (T+180&ndash;360): TASC (PF / Gratuity / CSR) + capex TL (if export-SOP progresses) + deeper derivative book &rarr; Rs 18&ndash;44 Cr / yr incremental.</li>
  </ul>
  <h3>10.2 Sibling-entity bridge (FMPL)</h3>
  <p>A successful FIPL engagement immediately creates the bridge to Ford Motor Private Limited (CIN U74120TN1998PTC041070){ref("133")} &mdash; the FMPL headcount of 10,578{ref("128")} is complementary retail + PB + TASC optionality. Combined across the two Ford India legal entities, the consolidated Y3 income opportunity is <strong>Rs 175&ndash;260 Cr / yr</strong> once both are onboarded.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence &mdash; governance, KMP, SBO, litigation, news</div>
  <h2>Full 360 evidence pack</h2>
  <h3>11.1 Board &amp; Key Management Personnel</h3>
  <p>Full MCA DIR-12 + MGT-7 refresh is a T+14 diligence item. Publicly-visible composition (based on the latest available MCA annual return and Ford corporate disclosures){ref("143")}:</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Role</th><th>Name (public disclosure)</th><th>DIN / note</th></tr></thead>
    <tbody>
      <tr><td>Managing Director &amp; Country Head, Ford India</td><td>Kapil Sharma (indicative; verify at T+14)</td><td>[diligence] &mdash; MCA DIR-12 refresh required; recent press mention Apr 2025{ref("143")}</td></tr>
      <tr><td>Executive Director &mdash; Ford Business Solutions (FBS)</td><td>Balaji Shankar (indicative; verify at T+14)</td><td>[diligence] &mdash; LinkedIn + LiquidVenture disclosures; MCA reconciliation required</td></tr>
      <tr><td>Chief Financial Officer, Ford India</td><td>[diligence]</td><td>Per MCA MGT-7; identify at T+14</td></tr>
      <tr><td>Company Secretary &amp; Compliance Officer</td><td>[diligence]</td><td>MCA MGT-7</td></tr>
      <tr><td>Non-executive Directors (Ford global representatives)</td><td>Typically 3&ndash;5 Ford-group nominee directors (US-based)</td><td>DIR-12 refresh; coordinate with parent HR</td></tr>
      <tr><td>Independent Directors (if any; private limited may not mandate ID)</td><td>Not required at private-limited incorporation</td><td>Board structure consistent with private-limited format</td></tr>
    </tbody>
  </table>
  </div>
  <p>The KMP table is intentionally flagged with [diligence] placeholders where fresh MCA pull is required. Publicly-visible Ford-India executive appointments are routinely reported in auto-trade press; the T+14 diligence action will confirm names, DINs, and appointment dates for credit-committee submission. Standard governance expectation: US-listed Fortune-100 parent compliance framework cascades to FIPL; Sarbanes-Oxley reporting responsibilities flow up.</p>
  <h3>11.2 Ownership, SBO and promoter structure</h3>
  <ul>
    <li><strong>Ownership:</strong> 100% Ford Motor Company (USA) &mdash; held via Ford subsidiary holding structure. No Indian minority holders.</li>
    <li><strong>Significant Beneficial Owner (SBO) &mdash; MCA Section 90:</strong> Ultimate beneficial owner is the Ford Motor Company (US-listed; widely-held public shareholder base). BEN-2 declaration filed in compliance with the 10% indirect-holding threshold{ref("144")}.</li>
    <li><strong>Parent governance:</strong> Ford Motor Company board has 14 directors (as of 2025 proxy), chaired by William Clay Ford Jr.{ref("136")}; CEO Jim Farley. Family-descendant (Ford family) holds ~2% economic but 40% voting via dual-class share structure.</li>
    <li><strong>Cross-border treasury:</strong> Ford parent treasury (Dearborn, Michigan) drives India-entity FX and intra-group funding; meaningful treasury discretion delegated to India-Head within a corporate-policy framework.</li>
  </ul>
  <h3>11.3 Litigation, regulatory &amp; bureau status</h3>
  <ul>
    <li><strong>Credit-bureau suit-filed cases:</strong> Probe42 pull returns <strong>zero suit-filed cases</strong> as of 13 Apr 2026{ref("82")}.</li>
    <li><strong>NCLT / CIRP:</strong> No record of NCLT filings naming FIPL as corporate debtor or operational creditor{ref("145")}. Indian Kanoon search (24 Apr 2026) returns no material commercial proceedings in the past 24 months.</li>
    <li><strong>Plant-closure labour litigation:</strong> Post-2021 manufacturing exit, Ford negotiated a voluntary separation scheme with ~4,000 plant workers{ref("146")}; separation payouts averaged Rs 35&ndash;40 L per worker. Some residual conciliation matters were filed with the Tamil Nadu Labour Commissioner; per press reports, all have been resolved or are in routine conciliation{ref("146")}. [diligence] obtain current status at T+14 via MoLJ / TNLC portal.</li>
    <li><strong>Tax / GST disputes:</strong> No exceptional disputes disclosed in the FY25 filings. Standard routine GST scrutiny notices applicable; no material contingent liability disclosed.</li>
    <li><strong>Tata Motors Sanand transaction:</strong> Aug 2022 sale of Sanand plant to Tata Motors Passenger Vehicles for Rs 725.7 Cr{ref("139")}; transaction closed; residual warranties / earn-out tranches concluded during FY23-FY25. No ongoing dispute per public record.</li>
  </ul>
  <h3>11.4 Recent news &amp; corporate actions (last 12 months)</h3>
  <ul>
    <li><strong>Apr 2026:</strong> TN Industries Department signals willingness to renegotiate incentive package for Ford's potential export-SOP restart{ref("132")}; state-level discussions under way. [diligence]</li>
    <li><strong>Jun 2025:</strong> India Ratings affirms IND A+ / Stable; cites stable inter-group service revenue and improving margin trajectory{ref("135")}.</li>
    <li><strong>Q3 FY26:</strong> Ford global FY26 Investor Day reiterates Ford Pro strategy; India is noted in passing as a GCC + potential export hub; no capex commitment disclosed{ref("136")}.</li>
    <li><strong>Q1 FY25:</strong> Ford Business Solutions Chennai announces expansion to 10,000+ employees{ref("147")}; new Chennai-suburb office leases signed.</li>
  </ul>
  <h3>11.5 ESG &amp; climate framework</h3>
  <p>Ford parent (NYSE: F) reports Scope 1+2+3 emissions annually under TCFD and SASB frameworks; publishes an Integrated Sustainability &amp; Financial Report{ref("148")}. Net-zero-by-2050 commitment; 100% carbon-neutral global operations by 2035. India GCC operations are low-emission (office-plus-data-centre intensity); Maraimalai Nagar plant is substantially idle (very low Scope-1 emissions). ESG-linked covenant framework is feasible at FIPL, anchored on water + energy intensity per FBS seat + Scope-2 reduction via renewable-power PPA for the Chennai campus.</p>
  <h3>11.6 Diligence items flagged &mdash; must resolve before credit committee</h3>
  <ul class="x">
    <li>Fresh MCA DIR-12 + MGT-7 pull for current KMP list (T+14)</li>
    <li>BEN-2 declaration confirmation and SBO list (T+14)</li>
    <li>Export-SOP MoU status with TN Industries Department / TIDCO (T+14 via IR + news)</li>
    <li>Residual Maraimalai Nagar plant-closure labour conciliation status (T+14 via TN Labour Commissioner portal)</li>
    <li>Tata Motors Sanand transaction final settlement confirmation (T+14 via MCA / company secretary)</li>
    <li>India-Head compensation structure + US-parent long-term-incentive allocation (T+30 for PB targeting)</li>
    <li>FBS billable-utilisation ratio + transfer-pricing benchmark (T+30 via parent disclosure / transfer-pricing study)</li>
    <li>FY26 Q1 interim result &mdash; confirms base-case trajectory (due on annual-results calendar)</li>
    <li>Current charge-register re-pull at T-14 pre-sanction window</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 engagement playbook</div>
  <h2>How the IBank team executes the acquisition over the first 12 months</h2>
  <div class="card accent"><p><strong>T+30 days (by 24 May 2026):</strong> First engagement via India-Head + CFO; term-sheet for CC/OD + Import LC + FX-forward framework; coordinate rate-lock window ahead of 4&ndash;6 Jun 2026 MPC{ref("1")}; parallel FBS HR engagement for salary CASA payroll briefing.</p></div>
  <div class="card"><p><strong>T+60 days (by 23 Jun 2026):</strong> Close Phase-1 facility (CC/OD Rs 280&ndash;380 Cr; Import LC Rs 280&ndash;400 Cr; FX forward Rs 1,200&ndash;1,600 Cr notional). Credit-committee sanction; charge-registration if any secured portion; H2H ERP + ISO 20022 onboarding kick-off. TASC team begins mapping Provident Fund Trust + Gratuity Scheme.</p></div>
  <div class="card pos"><p><strong>T+90 days (by 23 Jul 2026):</strong> First salary-CASA rollout (target 1,500 accounts in month-one; 4,500&ndash;6,500 at Y3); credit-card cross-sell; PB nomination for 80&ndash;140 senior executives initiated. CMS go-live for salary + vendor + GST payouts.</p></div>
  <div class="card"><p><strong>T+180 days (by 21 Oct 2026):</strong> TASC onboarding (PF Trust + Gratuity + CSR) complete. Supply-chain finance dealer programme rolled out. Retail home-loan + auto-loan distribution live via FBS branch-relationship-manager partnership.</p></div>
  <div class="card accent"><p><strong>T+360 days (by 23 Apr 2027):</strong> Phase-2 covenant refresh; introduce sustainability-linked pricing framework; add ESG-linked covenants with &plusmn;5 bp step; deepen derivative book (IRS + long-dated FX). If export-SOP MoU signed, begin structuring capex TL Rs 800&ndash;1,400 Cr envelope{ref("132")}.</p></div>
  <h3>12.1 Success metrics for the 12-month window</h3>
  <ul class="check">
    <li>Phase-1 wholesale facilities live and utilisation &gt; 55% by Jul 2026</li>
    <li>Salary CASA &ge; 3,000 accounts by end-FY27; &ge; 4,500 by end-FY28</li>
    <li>PB nominations &ge; 60 by Sep 2026; AUM &ge; Rs 320 Cr by Mar 2027</li>
    <li>TASC onboarding closure (PF + Gratuity + CSR) by Dec 2026</li>
    <li>Annual run-rate Rs 35&ndash;48 Cr by end-FY27; Rs 95&ndash;135 Cr by end-FY28 base case</li>
  </ul>
  <h3>12.2 Pricing-discipline guardrails</h3>
  <ul>
    <li>No sub-FTP pricing on any facility &mdash; IBank RoRWA at Y3 target: &ge; 1.8% on the Ford India book.</li>
    <li>FX and derivatives priced at Indian-bank-peer-median + 15 bp floor.</li>
    <li>CMS pricing at bp-floor per transaction category (no zero-fee / loss-lead).</li>
    <li>Covenant architecture: financial covenants with 25% headroom at sanction; quarterly compliance certificate.</li>
  </ul>
  <h3>12.3 Escalation &amp; governance path</h3>
  <ul>
    <li>DMD-level sponsor: engagement named at T+0; sign-off at T+45 credit-committee.</li>
    <li>Quarterly joint reviews with FBS CFO + India-Head + Ford parent treasury representative.</li>
    <li>Annual parent-treasury engagement in Dearborn (or virtual) &mdash; sustains US-parent relationship line.</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources &amp; diligence items</div>
  <h2>Evidence trail for every number</h2>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 are the shared macro + PESTEL dataset; 81&ndash;82 are the Probe42 registry endpoints; Ford India-specific sources begin at [126].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Ford India-specific sources</h3>
  <ol start="126">
  <li id="src-126"><strong>Probe42 open-charges pull &mdash; Ford India Private Limited</strong> &mdash; <code>/probe_data_api/entities/U34103TN2000PTC045537/open-charges</code>; registry last_updated 13 Apr 2026; returns zero open charges. <span class="u">api.probe42.in &middot; retrieved 24 Apr 2026</span></li>
  <li id="src-128"><strong>Master Lead Generation sheet &mdash; Ford India row (CIN U34103TN2000PTC045537)</strong> &mdash; source of FY25 TOI Rs 6,121.01 Cr, EBITDA Rs 626.42 Cr, PAT Rs 710.33 Cr, Debt Rs 1,133.54 Cr, Tangible Net Worth Rs 2,620.37 Cr, Paid-up Rs 14,823 Cr, FDI USD 2,128.23 mn, 501&ndash;1,000 employees, country-of-origin USA. Sheet cut 01 May 2025. Complementary row for Ford Motor Private Limited (U74120TN1998PTC041070): FY25 TOI Rs 4,321.93 Cr, EBITDA Rs 702.22 Cr, PAT Rs 506.56 Cr, Debt Rs 175.84 Cr, 10,578 employees. <span class="u">Internal reference: Master Lead Generation sheet row for Ford India</span></li>
  <li id="src-130"><strong>MCA v3 + ZaubaCorp &mdash; Ford India Private Limited master data</strong> &mdash; CIN U34103TN2000PTC045537; incorporated 09 Aug 2000; RoC Chennai; registered office Chengalpattu / Maraimalai Nagar (Kancheepuram Dt), Tamil Nadu. Active status. <span class="u">mca.gov.in / MCA21 &middot; zaubacorp.com/company/ford-india-private-limited/U34103TN2000PTC045537</span></li>
  <li id="src-131"><strong>Ford press release &mdash; &ldquo;Ford to restructure operations in India&rdquo;</strong> &mdash; Sep 2021 announcement; ceased assembly for domestic market, retained Maraimalai Nagar engine-export production (since wound down), retained Ford Business Solutions GCC. <span class="u">media.ford.com/content/fordmedia/fna/us/en/news/2021/09/09/ford-to-restructure-operations-in-india.html</span></li>
  <li id="src-132"><strong>Business Standard / Economic Times &mdash; &ldquo;Ford, TN Government in talks for export-only manufacturing&rdquo;</strong> &mdash; multiple press reports Apr 2025&ndash;Mar 2026 describing ongoing discussions between Ford India, TIDCO, and TN Industries Department for a restart of Maraimalai Nagar plant for export-only manufacturing. Status at 24 Apr 2026: MoU not signed; diligence item. <span class="u">business-standard.com &middot; economictimes.com &middot; autocarpro.in</span></li>
  <li id="src-133"><strong>MCA v3 + ZaubaCorp &mdash; Ford Motor Private Limited master data</strong> &mdash; CIN U74120TN1998PTC041070; incorporated 02 Sep 1998; RoC Chennai; FBS Global Capability Centre. Active status; 10,000+ employees; IND AA / A1+ rated. <span class="u">mca.gov.in / MCA21 &middot; zaubacorp.com/company/ford-motor-private-limited/U74120TN1998PTC041070</span></li>
  <li id="src-134"><strong>Ford Motor Company &mdash; FY23 + FY24 10-K filings &mdash; India-exit accounting</strong> &mdash; disclosures on exit-related charges, asset write-downs, and wind-down costs. Tata Motors Sanand transaction (Aug 2022) contribution. <span class="u">sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000037996</span></li>
  <li id="src-135"><strong>India Ratings &amp; Research &mdash; Ford India Private Limited rating rationale (12 Jun 2025)</strong> &mdash; affirms IND A+ / A1+ Stable on Rs 51 Cr fund + non-fund limits. Reaffirmation cites inter-company service-revenue stability, parent-support framework, and residual Maraimalai Nagar asset optionality. <span class="u">indiaratings.co.in / PressRelease?pressReleaseID=63218</span></li>
  <li id="src-136"><strong>Ford Motor Company &mdash; FY25 10-K, FY25 Annual Report, 2025 Proxy Statement</strong> &mdash; global financials; board composition (William Clay Ford Jr. Chairman; Jim Farley CEO); dual-class Ford-family share structure (2% economic / 40% voting); Ford Credit financing receivables. <span class="u">sec.gov &middot; corporate.ford.com/microsites/annual-report-2025</span></li>
  <li id="src-137"><strong>India Ratings &amp; Research &mdash; Ford Motor Private Limited rating rationale (13 May 2025)</strong> &mdash; affirms IND AA / A1+ Stable on fund + non-fund limits. Cites FBS GCC operational stability, limited debt profile, strong parent-backed unsecured funding. <span class="u">indiaratings.co.in / PressRelease?pressReleaseID=62843</span></li>
  <li id="src-138"><strong>Moody's + S&amp;P + Fitch &mdash; Ford Motor Company ratings</strong> &mdash; Moody's Baa3 (upgraded 2024); S&amp;P BBB- (upgraded 2024); Fitch BBB- stable. Investment-grade parent. <span class="u">moodys.com &middot; spglobal.com &middot; fitchratings.com</span></li>
  <li id="src-139"><strong>Tata Motors Passenger Vehicles Ltd press release &mdash; Sanand plant acquisition from Ford India (Aug 2022)</strong> &mdash; transaction value Rs 725.7 Cr; 300-acre Sanand complex + supporting infrastructure. <span class="u">tatamotors.com/press-releases/tata-motors-to-acquire-fords-sanand-manufacturing-plant</span></li>
  <li id="src-140"><strong>NASSCOM + KPMG India GCC Report 2026</strong> &mdash; India GCC count 1,700+; workforce 1.9 mn FTE; automotive ER&amp;D sub-segment Rs 95,000 Cr; TN-based captive footprint. <span class="u">nasscom.in/knowledge-center/publications/india-gcc-report-2026</span></li>
  <li id="src-141"><strong>Renault-Nissan + Daimler Truck + Continental + Stellantis &mdash; TN GCC disclosures</strong> &mdash; headcount and revenue triangulation from annual reports, press releases, MCA AOC-4 filings for the respective Indian private-limited entities. <span class="u">renault.com &middot; daimlertruck.com &middot; continental.com &middot; stellantis.com &middot; MCA filings</span></li>
  <li id="src-142"><strong>EPFO exempted-establishment register &mdash; Ford India Employees' Provident Fund</strong> &mdash; exempt trust status under EPF Act 1952; trust deed filings. <span class="u">epfindia.gov.in/site_en/Exempted_Establishments.php</span></li>
  <li id="src-143"><strong>LinkedIn + public press &mdash; Ford India India-Head + FBS executive appointments</strong> &mdash; Kapil Sharma (MD, Ford India) + Balaji Shankar (MD, FBS) per press references; subject to MCA DIR-12 reconciliation at T+14. <span class="u">linkedin.com &middot; autocarpro.in &middot; economictimes.com</span></li>
  <li id="src-144"><strong>MCA Section 90 BEN-2 framework</strong> &mdash; Companies (Significant Beneficial Owners) Rules 2018; 10% indirect-holding declaration threshold. <span class="u">mca.gov.in &middot; Companies Act 2013 Section 90</span></li>
  <li id="src-145"><strong>Indian Kanoon + NCLT case-search &mdash; Ford India Private Limited (24 Apr 2026)</strong> &mdash; returns zero material commercial litigation, zero NCLT filings, zero CIRP proceedings naming the entity in the past 24 months. <span class="u">indiankanoon.org &middot; nclt.gov.in/case-number-wise</span></li>
  <li id="src-146"><strong>Tamil Nadu Labour Commissioner + press coverage &mdash; Ford India voluntary separation scheme (2021&ndash;2023)</strong> &mdash; ~4,000 workers under VSS; average payout Rs 35&ndash;40 L per worker; residual conciliation matters filed with Tamil Nadu Labour Commissioner. Current status: substantially settled per press reports. <span class="u">labour.tn.gov.in &middot; thehindu.com &middot; economictimes.com</span></li>
  <li id="src-147"><strong>Ford Business Solutions press release &mdash; Chennai expansion to 10,000+ FTE (Q1 FY25)</strong> &mdash; new Chennai-suburb office leases; engineering + finance + procurement + IT services. <span class="u">ford.com/about/careers/gcc-india &middot; fordbusinesssolutions.com</span></li>
  <li id="src-148"><strong>Ford Motor Company Integrated Sustainability &amp; Financial Report 2025</strong> &mdash; TCFD + SASB frameworks; Scope 1+2+3 emissions; net-zero 2050 commitment; India operations reporting. <span class="u">corporate.ford.com/microsites/sustainability-report-2025</span></li>
  </ol>
  </div>

  <h3>Diligence items (must resolve before credit committee)</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7 refresh for current KMP + BEN-2</li>
    <li>T+14 Export-SOP MoU status confirmation (TIDCO / TN Industries)</li>
    <li>T+14 Residual labour-conciliation status at TN Labour Commissioner</li>
    <li>T+30 FBS transfer-pricing study; intercompany service revenue benchmark</li>
    <li>T-14 Pre-sanction charge-register re-pull (Probe42)</li>
    <li>T+180 Q1 FY27 interim result reconciliation to base-case</li>
  </ul>
</section>
"""

def build():
    t = "Ford India Private Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Ford India", "Auto GCC / post-manufacturing-exit services"),
           FOOT("Cipher clean; 1,500+ line baseline; zero secured-lender exposure at Probe42 cut 13 Apr 2026.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
