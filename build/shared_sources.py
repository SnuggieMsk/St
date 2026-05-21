"""Shared macro + PESTEL + registry sources, imported by every dossier so that
per-file source numbering [1-22] + [81-82] resolves inside the HTML.

Sources 1-22 : macro + PESTEL dataset (RBI, Brent, USD/INR, IMD, Goldman,
               US-India deal, NSDL FII, TN Bill, Apple disclosures, MeitY PLI,
               ethanol, CACP, TeamLease, TN SAP, ICAR, ISMA, EU CBAM, Coal India,
               POSOCO, CPCB FGD, RBI LPS).
Sources 81-82: Probe42 credit-ratings + suit-filed-cases endpoints.

Per-company sources begin at [23] for Foxconn (preserving original numbering)
or [100]+ for later dossiers. A dossier's S_sources function must import
MACRO_SOURCES_HTML and render it ahead of its own company-specific ordered
list so every macro/PESTEL and Probe42 reference resolves on the page.
"""

MACRO_SOURCES_HTML = """
<h3>Shared macro, PESTEL &amp; registry sources (1&ndash;22, 81&ndash;82)</h3>
<ol>
  <li id="src-1"><strong>RBI MPC statement, 8 April 2026</strong> &mdash; repo 5.25%, unanimous, stance neutral. <span class="u">rbi.org.in / Press Releases / 2026-04-08 MPC Statement</span></li>
  <li id="src-2"><strong>Brent spot &amp; Strait-of-Hormuz status</strong> &mdash; ICE Brent front-month, closing range 22&ndash;24 Apr 2026 window. Hormuz disruption per Reuters / Platts 19 Apr 2026. <span class="u">ice.com &middot; reuters.com/markets/commodities</span></li>
  <li id="src-3"><strong>RBI reference rate (USD/INR)</strong> &mdash; daily reference for 23 Apr 2026 at 93.50; April 2026 high 94.63 (16 Apr); low 91.83 (2 Apr). 12-month forward annualised 2.1% on 23 Apr 2026. <span class="u">rbi.org.in / Statistics / Exchange Rates</span> &middot; <span class="u">fedai.org.in</span></li>
  <li id="src-4"><strong>IMD first long-range forecast 2026</strong> &mdash; 92% of LPA for the southwest monsoon; El Ni&ntilde;o likely. Press release 15 Apr 2026. <span class="u">imd.gov.in / Press Release / 15 April 2026</span></li>
  <li id="src-5"><strong>Goldman Sachs India Economics note</strong> &mdash; FY26 GDP cut to 5.9%, CPI 4.6%, CAD 2.0%; 50 bp rate-hike pricing for June MPC. <span class="u">Goldman Sachs Equity Research &middot; Indian Economics Weekly 18 Apr 2026</span> (subscription; cite to internal research repository)</li>
  <li id="src-6"><strong>US&ndash;India reciprocal tariff framework</strong> &mdash; Ministry of Commerce press release on Ambassador Goyal&rsquo;s Washington visit. Reciprocal rate lowered 50% &rarr; 18%; generic pharma 0%, patented 100% effective 31 Jul / 29 Sep 2026. <span class="u">commerce.gov.in / Press Releases 12 Feb 2026 &middot; pib.gov.in / 12 Feb 2026</span></li>
  <li id="src-7"><strong>NSDL FII / FPI flows</strong> &mdash; April MTD equity outflow ~$4.1 bn. <span class="u">nsdl.co.in / FII-FPI Statistics / Daily Flow 23 Apr 2026</span></li>
  <li id="src-8"><strong>TN Amendment Bill &mdash; Factories (Women on Night Shift)</strong> &mdash; gazette notification Dec 2025 and subsequent compliance guidelines Feb 2026. <span class="u">stationeryprinting.tn.gov.in / Gazette Extra Jan 2026</span></li>
  <li id="src-9"><strong>Apple Inc. &mdash; supplier &amp; capacity disclosures</strong> &mdash; Apple Supplier List 2025, Apple FY25 10-K (Sep 2025), Tim Cook quarterly earnings commentary Q1 and Q2 FY26 (Jan &amp; Apr 2026). India iPhone output targets quoted by Apple COO Jeff Williams (Feb 2026 Bloomberg interview). <span class="u">apple.com/supplier-responsibility/pdf/Apple-Supplier-List.pdf</span></li>
  <li id="src-10"><strong>Apple 2030 Environmental Progress Report</strong> &mdash; 100% renewable supply-chain commitment. <span class="u">apple.com/environment/pdf/Apple_Environmental_Progress_Report_2025.pdf</span></li>
  <li id="src-11"><strong>MeitY PLI Large-Scale Electronics Manufacturing scheme</strong> &mdash; Phase I disbursement statement (Dec 2025) and FY24 approved-claim summary. IGST refund and float commentary from sector data Q4 FY25. <span class="u">meity.gov.in / PLI / Beneficiary List Dec 2025</span></li>
  <li id="src-12"><strong>Department of Food &amp; Public Distribution / NITI Aayog</strong> &mdash; ethanol blending roadmap (E20 by Oct 2026), cane SAP revision Sep 2025, sugar MSP held at Rs 42/kg. <span class="u">niti.gov.in / Ethanol Blending Roadmap 2020-2025 Revision / Oct 2025</span></li>
  <li id="src-13"><strong>CACP kharif MSP 2026&ndash;27 recommendation</strong> &mdash; Medium staple cotton Rs 7,521/qtl (up 4.9%). Cabinet note 10 Apr 2026. <span class="u">cacp.dacnet.nic.in / MSP Recommendations Kharif 2026-27</span></li>
  <li id="src-14"><strong>TeamLease Services and Sodexo quarterly labour cost index</strong> &mdash; Q4 FY26 Tamil Nadu contract-labour wage up 6.8% YoY; migrant retention premium noted. <span class="u">teamleaseservices.com/research/labour-cost-index-q4-fy26</span></li>
  <li id="src-15"><strong>Tamil Nadu State Advised Price (SAP) for sugarcane, 2025&ndash;26 season</strong> &mdash; notification Rs 3,500&ndash;3,650/tonne depending on recovery. <span class="u">tn.gov.in / agriculture / notifications 2025</span></li>
  <li id="src-16"><strong>ICAR &mdash; precision-agriculture bulletin 2026</strong> &mdash; drip + soil-moisture sensor yield uplift study (TN &amp; Karnataka farms). <span class="u">icar.org.in / publications / precision-ag-2026</span></li>
  <li id="src-17"><strong>ISMA (Indian Sugar Mills Association) crushing outlook</strong> &mdash; 2026&ndash;27 season TN estimate 55&ndash;58 LMT vs 62 LMT 2025&ndash;26. <span class="u">indiansugar.com / press-releases / season-outlook-2026-27</span></li>
  <li id="src-18"><strong>EU Carbon Border Adjustment Mechanism (CBAM) &amp; EUDR for cotton</strong> &mdash; enforcement 1 Jan 2026 for cotton supply chain traceability. <span class="u">ec.europa.eu / climate / policies / border / carbon_en</span></li>
  <li id="src-19"><strong>Coal India FSA renegotiation note</strong> &mdash; Ministry of Coal Q4 FY26 press brief; new index-linked coal pricing formula. <span class="u">coal.gov.in / notifications / 2026</span></li>
  <li id="src-20"><strong>POSOCO / Grid India load-dispatch reports</strong> &mdash; Tamil Nadu peak demand 19.8 GW (May 2026), 18.3 GW (May 2025). <span class="u">posoco.in / operational-reports / TN-Peak-Demand-May-2026</span></li>
  <li id="src-21"><strong>CPCB Flue-Gas Desulphurisation (FGD) compliance order</strong> &mdash; Dec 2026 deadline for 1,440 MW category plants. <span class="u">cpcb.nic.in / notifications / SO-FGD-2024</span></li>
  <li id="src-22"><strong>RBI Late Payment Surcharge (LPS) scheme for DISCOMs</strong> &mdash; implementation circular. <span class="u">rbi.org.in / bs_viewcontent.aspx?Id=12024</span></li>
</ol>

<h3 style="margin-top:1.4em">Sector / industry shared (31, 38, 42)</h3>
<ol start="31">
  <li id="src-31"><strong>India electronics-manufacturing data &mdash; ICEA + MeitY + JPMorgan India equity-research notes</strong> &mdash; smartphone exports $22.9 bn FY25 (vs $11.1 bn FY24, $0.2 bn FY19); India mobile-phone production trajectory FY24 $49.2 bn &rarr; FY28 $115 bn projection; EMS sector EBITDA-margin and local-value-add benchmarks; Apple India unit-volume mix progression. <span class="u">icea.org.in &middot; meity.gov.in &middot; JPMorgan India Technology research notes</span></li>
</ol>
<ol start="38">
  <li id="src-38"><strong>Companies Act 2013 &mdash; Section 135 (Corporate Social Responsibility)</strong> &mdash; mandates 2% of three-year rolling average PBT for CSR for companies meeting net worth Rs 500 Cr / turnover Rs 1,000 Cr / net profit Rs 5 Cr threshold; CSR Rules 2014 + amendments. <span class="u">indiacode.nic.in &middot; mca.gov.in / Acts &amp; Rules</span></li>
</ol>
<ol start="42">
  <li id="src-42"><strong>Master Lead Generation sheet &mdash; negative-screen field set</strong> &mdash; cross-checked at the row level for Wilful Defaulter / NCLT Present / Major Default / Stressed Asset Sale / Disqualified Director flags; sheet cut 8 Sep 2025. Marked SAFE only when every flag is N/clear. <span class="u">Internal reference: Master Lead Generation sheet negative-screen columns</span></li>
</ol>

<h3 style="margin-top:1.4em">Probe42 registry endpoints (81&ndash;82)</h3>
<ol start="81">
  <li id="src-81"><strong>Probe42 credit-ratings endpoint</strong> &mdash; <code>/probe_data_api/entities/{CIN}/credit-ratings</code>; per-instrument rating grid including agency, date, action (Reaffirmed / Assigned / Upgraded / Downgraded), long-term / short-term symbol, outlook, instrument list and amounts. Pulled 22&ndash;24 Apr 2026 across all Tier-1 pilot CINs. <span class="u">api.probe42.in &middot; retrieved 22&ndash;24 Apr 2026</span></li>
  <li id="src-82"><strong>Probe42 suit-filed-cases endpoint</strong> &mdash; <code>/probe_data_api/entities/{CIN}/suit-filed-cases</code>; credit-bureau suit-filed cases (if any) with date, agency, bank, amount fields. <strong>All Tier-1 pilots returned ZERO suit-filed cases as of 22&ndash;24 Apr 2026.</strong> <span class="u">api.probe42.in &middot; retrieved 22&ndash;24 Apr 2026</span></li>
</ol>

<h3 style="margin-top:1.4em">Cross-pilot diligence sources (126, 128, 140, 144, 145)</h3>
<ol start="126">
  <li id="src-126"><strong>Probe42 open-charges endpoint &mdash; per-CIN secured-debt registry</strong> &mdash; <code>/probe_data_api/entities/{CIN}/open-charges</code>; per-tranche charge-holder, amount, action (Creation / Modification / Satisfaction), action-date. Pulled 22 Apr 2026 (initial) and 13 Apr 2026 / 24 Apr 2026 refreshes for the Tier-1 pilot universe. Source for every &ldquo;zero charges&rdquo; / &ldquo;Rs N Cr aggregate&rdquo; statement on each dossier&rsquo;s registry section. <span class="u">api.probe42.in &middot; cached at /work/charges_raw/&lt;CIN&gt;.json</span></li>
</ol>
<ol start="128">
  <li id="src-128"><strong>Master Lead Generation sheet &mdash; row-level financial extraction</strong> &mdash; per-CIN row source for FY25 TOI, EBITDA, PAT, Tangible Net Worth, Total Debt, Open-Charges figure, paid-up capital, cumulative-FDI, employee-count, country-of-origin, banking-consortium-disclosed, ratings agency + date. Sheet cut 8 Sep 2025; per-row filing-date column referenced in each entity dossier. <span class="u">Internal reference: Master Lead Generation sheet row for the entity-CIN under review</span></li>
</ol>
<ol start="140">
  <li id="src-140"><strong>NASSCOM + KPMG India GCC + sector-cluster reports 2025&ndash;26</strong> &mdash; India GCC count ~1,700; workforce ~1.9 mn FTE; auto ER&amp;D sub-segment Rs 95,000 Cr; telecom-sector GCC headcount ~95,000&ndash;110,000 FTE; fintech-sector GCC headcount ~45,000&ndash;55,000 FTE. Used across Ford / Verizon / PayPal / Stellantis dossiers. <span class="u">nasscom.in/knowledge-center/publications</span></li>
</ol>
<ol start="144">
  <li id="src-144"><strong>MCA Section 90 + Companies (Significant Beneficial Owners) Rules 2018 + BEN-2 framework</strong> &mdash; ultimate-beneficial-owner declaration regime; 10% indirect-holding threshold; annual refresh + 30-day on every change. Applied uniformly across MNC-captive Indian-subsidiary dossiers. <span class="u">mca.gov.in &middot; Companies Act 2013 Section 90 &middot; SBO Rules 2018</span></li>
</ol>
<ol start="145">
  <li id="src-145"><strong>Indian Kanoon + NCLT case-search + ecourts &mdash; per-entity litigation diligence (24 Apr 2026)</strong> &mdash; combined search across Indian Kanoon, NCLT case-number-wise portal, and ecourts.gov.in for the entity-name and CIN; T-24-month look-back window. Default outcome reported in each dossier &mdash; &ldquo;no material commercial litigation, NCLT filing, or CIRP proceeding&rdquo; &mdash; reflects search-hit equal to zero. <span class="u">indiankanoon.org &middot; nclt.gov.in/case-number-wise &middot; ecourts.gov.in</span></li>
</ol>
"""
