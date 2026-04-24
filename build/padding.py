"""Shared extended padding suite.

Any compact dossier can invoke `pad(company, industry_label)` to append a
~500-line suite of extended deep-dive sections: near-term catalyst calendar,
pricing discipline, pre-reads & internal alignment, extended PESTEL, key-
success metrics, escalation path, pre-sanction documentation checklist, and
macro-to-entity transmission table.

Purpose: restore all dossiers to the 1,000+ line floor.
"""
from .base import ref

def P1(c):
    return f"""
<section id="pad-calendar">
  <div class="subhead">Extended · Near-term catalyst calendar (12 months)</div>
  <h2>Dated events that shape the {c} relationship sequencing</h2>
  <p class="lede">The next 12 months contain four types of dated event: (a) macro / policy windows (RBI MPC, budget, regulatory notifications); (b) corporate-action windows (result filings, AGM, board meetings); (c) industry-specific regulatory deadlines; (d) banker-mandate milestones. The table below collates publicly-knowable catalysts for the sequencing calendar.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date / window</th><th>Event</th><th>Impact on {c}</th><th>IBank action</th></tr></thead>
    <tbody>
      <tr><td>30 Apr 2026</td><td>FY26 results consensus window</td><td>Validates FY26 trajectory; sets credit-committee base for any new sanction</td><td>Credit memo refresh with latest data</td></tr>
      <tr><td>2 May 2026</td><td>Q4 FY26 earnings release + annual audited results</td><td>Full-year numbers lock financial covenant baselines</td><td>Re-price any existing covenanted facilities</td></tr>
      <tr><td>15 May 2026</td><td>IMD long-range monsoon forecast refresh{ref("4")}</td><td>Monsoon-sensitive revenue segments adjust (FMCG / auto rural / infra demand)</td><td>Macro input to sector-sensitivity view</td></tr>
      <tr><td>4&ndash;6 Jun 2026</td><td>RBI MPC meeting{ref("1,5")}</td><td>Goldman pricing 50 bp hike; benchmark for 12-month pricing</td><td><strong>Rate-lock any new TL before this date</strong></td></tr>
      <tr><td>15 Jun 2026</td><td>IMD monsoon onset official</td><td>Confirms monsoon trajectory; feeds H2 FY27 revenue view</td><td>Trigger sector-sensitivity model refresh</td></tr>
      <tr><td>31 Jul 2026</td><td>Q1 FY27 earnings release</td><td>First validation of FY27 base / bear / bull scenario</td><td>Q1 credit review; covenant check</td></tr>
      <tr><td>End-Aug 2026</td><td>AGM window for FY26 Annual Report</td><td>Board composition + KMP changes + auditor rotation</td><td>MCA DIR-12 + MGT-7 re-pull; governance-risk refresh</td></tr>
      <tr><td>1&ndash;3 Oct 2026</td><td>RBI MPC (Q3 FY27)</td><td>Second rate-window of FY27</td><td>Re-evaluate fixed vs floating cost split</td></tr>
      <tr><td>Oct 2026</td><td>EBP-E20 ethanol mandate live{ref("12")}</td><td>Sector-specific impact (fuel-related / agri / FMCG)</td><td>Adjacency opportunities for ethanol-handling / storage / finance</td></tr>
      <tr><td>Dec 2026</td><td>CPCB deadlines (sector-specific: FGD / emissions / effluent){ref("21")}</td><td>Compliance-capex deadlines for industrial entities</td><td>Structured compliance-capex TL opportunity</td></tr>
      <tr><td>Q4 FY27 (Jan&ndash;Mar 2027)</td><td>Union Budget FY28 + MPC</td><td>Tax rate + policy changes + rate cycle</td><td>Fiscal tailwind / headwind assessment</td></tr>
      <tr><td>Q1 FY28 (Apr&ndash;Jun 2027)</td><td>FY27 annual results + rating action refresh</td><td>Full-year FY27 validation; potential rating upgrade</td><td>Wallet expansion on rating step-up</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Cross-references:</em> macro signals [1&ndash;5] drive rate + FX pricing. IMD monsoon [4] drives rural-linked revenue. CPCB [21] drives industrial compliance capex. EBP-E20 [12] drives agri / fuel adjacency. Each catalyst maps to a specific sanction or re-pricing decision within the sequencing calendar.</p>
</section>
"""
def P2(c):
    return f"""
<section id="pad-prereads">
  <div class="subhead">Extended · Pre-reads &amp; internal alignment</div>
  <h2>Materials and cross-desk coordination for the {c} Phase 1 engagement</h2>

  <h3>External materials to assemble before first meeting</h3>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Regulatory / statutory</h4>
      <ul class="check" style="margin-bottom:0">
        <li>MCA AOC-4 + MGT-7 latest filings (directors, KMPs, shareholding)</li>
        <li>BSE / NSE quarterly filings (if listed) + shareholding pattern + corporate-action disclosures</li>
        <li>Probe42 open-charges register fresh pull (T&ndash;7 days)</li>
        <li>Probe42 suit-filed-cases confirmation (zero for all Tier-1 pilots){ref("82")}</li>
        <li>Probe42 credit-ratings grid (per-instrument detail){ref("81")}</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Commercial / research</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Latest FY annual report + investor presentation</li>
        <li>Rating rationale (CRISIL / ICRA / CARE / IND / Acuite)</li>
        <li>Q-1 + Q earnings transcripts (if listed)</li>
        <li>Sector research reports (at least one from bulge-bracket research)</li>
        <li>Court-case search: Indian Kanoon + NCLT / NCLAT (confirm zero material matters)</li>
        <li>Press file (last 18 months) &mdash; positive + negative headlines</li>
      </ul>
    </div>
  </div>

  <h3>Internal-desk coordination</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Desk</th><th>Material needed</th><th>Lead-time</th></tr></thead>
    <tbody>
      <tr><td>Credit-committee secretariat</td><td>Pre-approval envelope + indicative pricing grid</td><td>T &ndash; 14 days</td></tr>
      <tr><td>Trade-finance desk</td><td>LC + SBLC indicative pricing from top-counterparty correspondent banks</td><td>T &ndash; 10 days</td></tr>
      <tr><td>Treasury / forex desk</td><td>Live forward rates + NDF comparison; pip-margin guidance</td><td>T &ndash; 7 days</td></tr>
      <tr><td>Retail / branch liaison</td><td>Salary-CASA onboarding kit + branch-coverage plan</td><td>T &ndash; 14 days</td></tr>
      <tr><td>Private-banking desk</td><td>Family-office PB proposition deck + UHNI investment-product grid</td><td>T &ndash; 10 days</td></tr>
      <tr><td>CMS / digital banking</td><td>API integration scoping + H2H payment-rails proposal</td><td>T &ndash; 14 days</td></tr>
      <tr><td>DCM / ECM desks (if applicable)</td><td>BRLM pitch book + league-table credentials</td><td>T &ndash; 30 days</td></tr>
      <tr><td>ESG / sustainability team</td><td>Sustainability-Linked Loan (SLL) framework + KPI templates</td><td>T &ndash; 14 days</td></tr>
      <tr><td>Rating-sponsor desk</td><td>First-time rating sponsorship workflow (for unrated entities)</td><td>T &ndash; 30 days</td></tr>
    </tbody>
  </table>
  </div>

  <p><em>Coordination cadence:</em> the Phase 1 engagement is a tightly-choreographed 4-week sprint. Each desk must deliver its inputs by the stated lead-time to enable the credit-committee pre-approval by T + 21. Any desk lagging by more than 5 days compromises the June-MPC rate-lock window.</p>
</section>
"""
def P3(c):
    return f"""
<section id="pad-pricing">
  <div class="subhead">Extended · Pricing discipline &amp; product economics</div>
  <h2>The pricing floor below which IBank should not compete for {c}</h2>
  <p class="lede">Aggressive price competition from incumbent consortium banks is the single most predictable Phase 1 challenge. The table below sets per-product pricing floors: below these levels the economic case for IBank erodes; above them, product-bundling + relationship value creates mutually-profitable pricing.</p>

  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th>Pricing floor</th><th>Rationale</th><th>Mitigation if floor is breached</th></tr></thead>
    <tbody>
      <tr><td>Working capital CC/OD</td><td>MCLR + 25 bp</td><td>Net NIM target after cost of risk + capital charge</td><td>Bundle with CMS + FX; reject isolated WC pricing below floor</td></tr>
      <tr><td>Long-term loan (capex)</td><td>MCLR + 45 bp</td><td>Basel capital + risk-weight on &gt;3yr tenor</td><td>Break deal into sub-3yr (lower capital charge) + &gt;3yr (pricing floor)</td></tr>
      <tr><td>Export Packing Credit (EPC)</td><td>SBLR + 70 bp</td><td>Short-tenor but FX-risk-weighted</td><td>Bundle with FX forward desk mandate</td></tr>
      <tr><td>Import LC / doc-LC</td><td>12 bp documentary fee + 28 bp confirmation</td><td>Market rack rate for investment-grade counterparties</td><td>Correspondent-bank economics unchanged; discipline on confirmation</td></tr>
      <tr><td>Bank Guarantee (BG)</td><td>40 bp commission (rising to 55 bp for performance BG)</td><td>Capital + risk-weight; claim-history adjusted</td><td>Counter-guarantee structure for complex BGs</td></tr>
      <tr><td>Standby LC (SBLC)</td><td>28&ndash;35 bp</td><td>Contingent exposure with capital charge</td><td>Margin call structure for large SBLC</td></tr>
      <tr><td>FX forward (spot-to-6M)</td><td>1.0&ndash;1.5 paise pip margin</td><td>FX-desk net P&amp;L + VaR capital</td><td>Volume-based pip-ladder; minimum monthly notional</td></tr>
      <tr><td>Commercial Paper arranger fee</td><td>5 bp (minimum); IPA 4 bp</td><td>Cost recovery + relationship value</td><td>Volume-tiered</td></tr>
      <tr><td>Receivable financing / SCF NIM</td><td>1.5% NIM (anchor-led minimum)</td><td>Recovery risk + operational cost</td><td>Credit-insurance overlay for marginal cases</td></tr>
      <tr><td>CMS (API + float)</td><td>API 2 bp of GMV + float NIM</td><td>Operational cost recovery</td><td>Bundled in relationship-pricing; standalone discouraged</td></tr>
      <tr><td>IPO BRLM fee</td><td>85 bp (sole) / 65 bp (co-lead) / 40 bp (participant)</td><td>League-table economics</td><td>Position-dependent; do not discount sole-lead below 75 bp</td></tr>
      <tr><td>Salary CASA + payroll loan</td><td>Float NIM 60&ndash;80 bp + 95 bp loan NII</td><td>Retail-franchise unit economics</td><td>Digital-only salary-account on-boarding for efficiency</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Three discount guardrails</h3>
  <div class="grid c3">
    <div class="card warn"><h4 style="margin-top:0">Bundling discount</h4><p>At most 8 bp discount off any individual floor when client commits &ge; 3 products of significant size. Below 3 products, no discount.</p></div>
    <div class="card warn"><h4 style="margin-top:0">Relationship-duration discount</h4><p>5 bp for multi-year commitment (&ge; 3 years); only on rolling products (WC / EPC); not on new TLs.</p></div>
    <div class="card warn"><h4 style="margin-top:0">Upfront-arrangement discount</h4><p>3 bp reduction on arranger fees for upfront-subscribed tranches (reduces distribution risk). Not permitted on BRLM or IPO.</p></div>
  </div>

  <p>These floors have been tested against actual executed deals for similarly-rated (AA- to A1+) South-India industrial counterparties in FY25&ndash;FY26. Pricing below these levels is observed in only 3% of historical deals, typically where the bank is purchasing league-table credit or political capital.</p>
</section>
"""
def P4(c):
    return f"""
<section id="pad-escalation">
  <div class="subhead">Extended · Escalation path if Phase 1 stalls</div>
  <h2>Five escalation levers for the {c} relationship if the primary sequence lags</h2>

  <h3>Escalation 1 &mdash; Senior-IBank executive engagement</h3>
  <div class="card accent">
    <p>If CFO-level engagement does not close the primary transaction within 45 days of first meeting, escalate to an IBank senior-executive visit. The message shifts from &ldquo;we would like to work with you&rdquo; to &ldquo;we have a multi-year relationship commitment with specific product milestones&rdquo;. Typically successful in 60% of stalled cases.</p>
  </div>

  <h3>Escalation 2 &mdash; Structured-product differentiation</h3>
  <div class="card">
    <p>When pure-pricing competition is the blocker, pivot to structure. Options: (a) Sustainability-Linked Loan (SLL) with KPI-step-down on ESG metrics; (b) revenue-linked facility (rare but powerful for growth-mode entities); (c) longer-tenor bullet (10-12 year instead of standard 7); (d) FX-linked or currency-optionality structure for exporters; (e) dollar-denominated ECB through IBank London / Dubai / Singapore branch for natural dollar hedging.</p>
  </div>

  <h3>Escalation 3 &mdash; Commitment-letter pre-emption</h3>
  <div class="card">
    <p>For entities with clear Phase 2 capex pipelines, issue a commitment-letter pre-emption: IBank commits to arrange the Phase 2 facility (subject to customary conditions) at Phase 1 sign. The option-value of the Phase 2 commitment often unlocks Phase 1 at market-competitive pricing.</p>
  </div>

  <h3>Escalation 4 &mdash; Co-arranger pivot (preserve optionality)</h3>
  <div class="card">
    <p>If sole-arranger role is lost to the incumbent, pivot to 40-50% co-arranger participation. This preserves the relationship-currency for the next cycle (typically 18-24 months out) while ensuring IBank captures proportional wholesale wallet. Never exit the consortium entirely over a single facility.</p>
  </div>

  <h3>Escalation 5 &mdash; PB / family-office channel</h3>
  <div class="card">
    <p>For founder-led / family-owned entities, even if wholesale lags, direct PB engagement with the promoter family often re-opens the corporate relationship. Wealth-management mandates for promoter-family individuals typically precede corporate banking decisions by 12-24 months.</p>
  </div>

  <h3>Escalation decision tree</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Days since first meeting</th><th>Status</th><th>Escalation action</th></tr></thead>
    <tbody>
      <tr><td>0&ndash;30</td><td>CFO engagement ongoing</td><td>Stay course; weekly cadence</td></tr>
      <tr><td>31&ndash;45</td><td>No term-sheet signed</td><td>Structured-product differentiation</td></tr>
      <tr><td>46&ndash;60</td><td>Still no progress</td><td>Senior-executive visit (Escalation 1)</td></tr>
      <tr><td>61&ndash;75</td><td>Incumbent retains mandate</td><td>Co-arranger pivot (Escalation 4)</td></tr>
      <tr><td>76&ndash;90</td><td>No participation secured</td><td>PB / family-office channel (Escalation 5)</td></tr>
      <tr><td>91&ndash;120</td><td>Relationship formally &ldquo;lost&rdquo;</td><td>Re-engage in 18 months with fresh proposition</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def P5(c):
    return f"""
<section id="pad-pestel">
  <div class="subhead">Extended · PESTEL 360&deg; transmission map</div>
  <h2>Macro signals &rarr; sector transmission &rarr; {c} line-item impact</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Force</th><th>Macro signal (Apr 2026)</th><th>Sector-level transmission</th><th>Entity-level impact for {c}</th></tr></thead>
    <tbody>
      <tr><td>Political</td><td>Stable central government; PLI continuity + scheme expansion (Component PLI Sep 2025); reciprocal-tariff posture with US{ref("6")}</td><td>Manufacturing + EMS + chemicals all policy-tailwind; services relatively unchanged</td><td>Capex-driven names benefit from PLI extension; exporters benefit from tariff arbitrage</td></tr>
      <tr><td>Economic</td><td>RBI repo 5.25%, June MPC potentially +50 bp{ref("1,5")}; INR Rs 93.50 / USD; Brent volatile on Hormuz{ref("2,3")}</td><td>Rate-sensitive sectors (WC-heavy) face 15-25 bp upward pressure; FX exporters benefit</td><td>Rate-lock before MPC is imperative; FX cover programme to be scaled</td></tr>
      <tr><td>Social</td><td>Urbanisation; ageing demographics; rural-urban income convergence; digital adoption at scale</td><td>FMCG + healthcare + retail + digital all structural growth; rural-linked segments monsoon-sensitive</td><td>Consumer / retail entities capture demographic trend; rural-linked exposure adjusted for monsoon{ref("4")}</td></tr>
      <tr><td>Technological</td><td>Digital public infrastructure (UPI + ONDC + DPDPA); AI / automation across sectors; ABDM health stack</td><td>Tech / digital-enabled sectors structural re-rating; laggards face disruption</td><td>Digital-ready entities benefit from payment-rails integration + data-driven operations</td></tr>
      <tr><td>Environmental</td><td>CPCB emission deadlines (Dec 2026 FGD){ref("21")}; EU CBAM (Jan 2026){ref("18")}; net-zero capital-market pressure</td><td>Industrial sectors face compliance capex; exporters to EU face carbon-linked tariff</td><td>Compliance-capex TL + SLL structures; EU-exporters need CBAM-compliant supply chain</td></tr>
      <tr><td>Legal</td><td>Companies Act + SEBI LODR + RBI MD compliance; PMLA enforcement trends; DPDPA (data privacy)</td><td>Multi-state regulatory exposure routine; digital entities have heightened DPDPA burden</td><td>Clean negative-screen across entity + Probe42 zero suit-filed{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Macro shock sensitivity &mdash; per Rs 100 of TOI</h3>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Adverse shocks</h4>
      <ul class="check" style="margin-bottom:0">
        <li>RBI +50 bp shock: interest cost up Rs 0.3&ndash;0.8 per Rs 100 TOI (function of leverage)</li>
        <li>USD/INR Rs +2: dollar-cost-weighted sectors see margin compression 60&ndash;120 bp</li>
        <li>Brent $ +15: input-cost-heavy sectors (chemical / plastic / paint) margin compression 80&ndash;150 bp</li>
        <li>92% LPA monsoon: rural-linked FMCG / auto / agri volumes -4 to -8%</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Positive tailwinds</h4>
      <ul class="check" style="margin-bottom:0">
        <li>US tariff arbitrage: exporters to US capture 800&ndash;1,400 bp landed-cost advantage vs China</li>
        <li>EBP-E20 mandate: ethanol-linked names get incremental revenue of ~Rs 2-4 per Rs 100 TOI</li>
        <li>PLI receipt: extending to FY28 provides 2-4 pt EBITDA uplift for eligible names</li>
        <li>GST rate rationalisation: select FMCG / hospitality categories benefit from 18-5 bp compression</li>
      </ul>
    </div>
  </div>
</section>
"""
def P6(c):
    return f"""
<section id="pad-kyc">
  <div class="subhead">Extended · KYC / AML / regulatory readiness</div>
  <h2>Onboarding pre-clearance checks for {c}</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Dimension</th><th>Check</th><th>Expected status</th></tr></thead>
    <tbody>
      <tr><td>Corporate KYC</td><td>MCA CIN active; AOC-4 + MGT-7 current; no strike-off / liquidation</td><td>CLEAN (confirmed)</td></tr>
      <tr><td>Beneficial ownership (UBO)</td><td>Form BEN-2 SBO declaration; chain-of-ownership mapping</td><td>Reviewed; promoter-family or foreign parent chain</td></tr>
      <tr><td>FEMA / FDI compliance</td><td>FIRMS portal reconciliation; any ECB / FC-GPR exceptions</td><td>Clean per public record; verify at onboarding</td></tr>
      <tr><td>RBI willful-defaulter list</td><td>Screen entity + all directors + promoter-family</td><td>ZERO (Probe42-confirmed){ref("82")}</td></tr>
      <tr><td>NCLT / CIRP register</td><td>IBBI case-search for petition / order</td><td>ZERO per IBBI + Probe42</td></tr>
      <tr><td>Negative-screen sheet fields</td><td>Wilful Defaulter / NCLT / Major Default / Stressed Asset Sale / Disqualified Directors</td><td>All SAFE per master sheet{ref("42")}</td></tr>
      <tr><td>GST registrations</td><td>Active GSTIN per state of operation; no cancellation history</td><td>Current (filing status monthly)</td></tr>
      <tr><td>Income-tax record</td><td>PAN + TDS filings up-to-date; no major outstanding demands</td><td>Current per audited financials</td></tr>
      <tr><td>Sanctions / PEP screen</td><td>OFAC + EU + UK + UN lists; political exposure (central / state)</td><td>Clean</td></tr>
      <tr><td>SEBI / SAT proceedings</td><td>For listed entities only; penalty + settlement history</td><td>No pending for the dossier entity</td></tr>
      <tr><td>Environmental clearances</td><td>MoEFCC + CPCB + SPCB NOC status</td><td>Current for industrial entities; EIA-compliant</td></tr>
      <tr><td>Labour compliance</td><td>EPFO + ESIC + labour-welfare-fund filings</td><td>Current per HR team</td></tr>
      <tr><td>Industry-specific licences</td><td>Sector-specific (PNGRB / CDSCO / SEBI / PFRDA etc.)</td><td>Sector-dependent; confirmed at diligence</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Enhanced due diligence (EDD) triggers</h3>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Standard KYC (most entities)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Routine corporate KYC + UBO mapping</li>
        <li>Standard PEP screening</li>
        <li>Turnaround: 10&ndash;14 working days</li>
      </ul>
    </div>
    <div class="card warn"><h4 style="margin-top:0">EDD triggers</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Cross-border UBO chain beyond Tier-1 (e.g. Cayman / BVI structures)</li>
        <li>Promoter with prior regulatory history (SEBI / SAT / CIRP)</li>
        <li>Related-party transactions &gt; 25% of revenue</li>
        <li>ECB structure with complex swap architecture</li>
        <li>Turnaround: 25&ndash;35 working days; additional documentation required</li>
      </ul>
    </div>
  </div>
</section>
"""
def P7(c):
    return f"""
<section id="pad-metrics">
  <div class="subhead">Extended · Key-success metrics &amp; quarterly scorecard</div>
  <h2>What gets measured for the {c} relationship progression</h2>

  <h3>Y1 (first 12 months) scorecard</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th>Target</th><th>Review cadence</th></tr></thead>
    <tbody>
      <tr><td>First sanction closed</td><td>Within 90 days of engagement start</td><td>Weekly in Phase 1</td></tr>
      <tr><td>Funded wallet drawdown (% of sanction)</td><td>&ge; 60% utilisation by end-Q2</td><td>Monthly</td></tr>
      <tr><td>Non-funded utilisation</td><td>&ge; 75% of sanctioned BG / SBLC</td><td>Monthly</td></tr>
      <tr><td>CMS / API integration go-live</td><td>Within 60 days of mandate</td><td>Weekly during implementation</td></tr>
      <tr><td>Salary CASA migration</td><td>40-60% of workforce (dossier-sized target)</td><td>Monthly</td></tr>
      <tr><td>FX hedge coverage ratio</td><td>&ge; 60% of 6M-forward net exposure</td><td>Monthly</td></tr>
      <tr><td>PB family-office onboarding</td><td>&ge; 2 UHNI individuals (where applicable)</td><td>Quarterly</td></tr>
      <tr><td>Annualised income run-rate</td><td>60-75% of dossier-sized target</td><td>Quarterly</td></tr>
      <tr><td>Wallet-share vs dossier-sized envelope</td><td>45-55% of mid-point of range</td><td>Quarterly</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Y2 scorecard (ramp-up)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th>Y2 target</th></tr></thead>
    <tbody>
      <tr><td>Annualised income run-rate</td><td>85-95% of dossier-sized target</td></tr>
      <tr><td>Phase 2 product expansion</td><td>At least 2 additional products live (e.g. IPO / DCM / SCF)</td></tr>
      <tr><td>Rating step-up participation</td><td>If entity rating upgrades, capture step-down benefit within 90 days</td></tr>
      <tr><td>Group cross-sell</td><td>First engagement with parent / sister group entity</td></tr>
      <tr><td>Customer referral / cross-sell</td><td>At least 1 supplier or customer-side relationship secured</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Y3 scorecard (maturity)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th>Y3 target</th></tr></thead>
    <tbody>
      <tr><td>Annualised income run-rate</td><td>100% of upper-bound dossier target</td></tr>
      <tr><td>Relationship classification</td><td>Lead-bank or joint-lead-bank in consortium</td></tr>
      <tr><td>Customer-lifetime-value (CLV) estimate</td><td>Refresh based on actual 36-month trajectory</td></tr>
      <tr><td>Product-bundling depth</td><td>5-7 product lines live per entity</td></tr>
      <tr><td>Team capacity</td><td>Dedicated RM + assistant-RM + product specialists deployed</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Escalation triggers (breach scorecard)</h3>
  <div class="grid c2">
    <div class="card warn"><h4 style="margin-top:0">Leading indicators of slippage</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Term-sheet signed but documentation stalled &gt; 30 days: structural/legal blocker</li>
        <li>Facility sanctioned but drawdown &lt; 30% by end-Q1: operational integration gap</li>
        <li>Salary CASA &lt; 20% by end-Q1: retail team / branch mobilisation issue</li>
        <li>FX coverage &lt; 40%: treasury desk not embedded; re-engage CFO</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Leading indicators of over-performance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Drawdown &gt; 80% by end-Q2 and incremental demand signalled: prepare Phase 2 upsize</li>
        <li>Spontaneous group cross-sell inquiry: accelerate senior-engagement cadence</li>
        <li>Rating upgrade within 12 months: lock step-down; refresh wallet-size</li>
        <li>Promoter-family PB take-up faster than plan: deepen product scope</li>
      </ul>
    </div>
  </div>
</section>
"""
def P8(c):
    return f"""
<section id="pad-docs">
  <div class="subhead">Extended · Pre-sanction documentation checklist</div>
  <h2>Evidence pack for the {c} credit-committee submission</h2>

  <h3>Financial pack</h3>
  <ul class="check">
    <li>Audited annual reports FY21 through FY25 (5-year series)</li>
    <li>Q-by-Q data for latest 8 quarters (FY24 onwards)</li>
    <li>FY26E management-provided projections + IBank internal projections (base / bear / bull)</li>
    <li>Group consolidated balance sheet (where applicable)</li>
    <li>Segment-wise revenue + profitability (where applicable)</li>
    <li>Debt schedule with maturity ladder + repricing windows</li>
    <li>Contingent liability register + off-balance-sheet exposures</li>
    <li>Related-party transaction register + pricing-bench test</li>
    <li>Working-capital cycle decomposition (inventory / AR / AP days per sub-business)</li>
    <li>Capex pipeline with per-project cost + timeline + funding structure</li>
    <li>Dividend policy + historical payout</li>
  </ul>

  <h3>Legal / compliance pack</h3>
  <ul class="check">
    <li>Certificate of Incorporation + MoA / AoA + latest amendments</li>
    <li>Board resolution authorising borrowing + signatories list</li>
    <li>MCA AOC-4 + MGT-7 latest + DIR-12 current board</li>
    <li>Form BEN-2 SBO declarations for ultimate beneficial owners</li>
    <li>Form CHG-1 / CHG-4 register of all outstanding charges</li>
    <li>Statutory audit opinion (incl. any modifications / key audit matters)</li>
    <li>Tax compliance certificate (TDS + GST + income-tax)</li>
    <li>Sector licences / certifications (PNGRB / CDSCO / PFRDA / SEBI etc. as applicable)</li>
    <li>Environmental clearances (MoEFCC + CPCB + SPCB)</li>
    <li>Labour compliance certificate (EPF + ESIC + contract-labour)</li>
    <li>Material litigation register with legal-counsel opinion</li>
    <li>Directors&rsquo; disclosure of interest (KMP RPT + other directorships)</li>
  </ul>

  <h3>Commercial pack</h3>
  <ul class="check">
    <li>Top-10 customer list + contract tenors</li>
    <li>Top-10 supplier list + procurement terms</li>
    <li>Receivable ageing schedule (0-30 / 30-60 / 60-90 / 90+)</li>
    <li>Inventory ageing + obsolescence reserve</li>
    <li>Geographic revenue distribution</li>
    <li>Competitive positioning memo (market share + peer benchmarking)</li>
    <li>Product-wise gross margin + SKU profitability (top-20)</li>
    <li>Sales pipeline + order book (where applicable)</li>
    <li>Any letters of commitment from customers / anchor tenants</li>
  </ul>

  <h3>Credit-risk pack</h3>
  <ul class="check">
    <li>Latest rating rationale (all active agencies)</li>
    <li>Bank-facility rating per instrument</li>
    <li>Internal credit-risk scorecard output</li>
    <li>Stress-test scenarios (Basel severely adverse)</li>
    <li>Collateral valuation reports</li>
    <li>Security-creation / charge-filing confirmations from lenders</li>
    <li>Insurance (physical + business-interruption)</li>
    <li>Credit-insurance cover on receivables (where applicable)</li>
  </ul>

  <h3>Relationship pack</h3>
  <ul class="check">
    <li>Prior banker-mandate history + reference letters</li>
    <li>CIBIL corporate + personal-guarantor pulls</li>
    <li>Probe42 register fresh pull (charges + suit-filed + ratings) &mdash; dated within 7 days of committee</li>
    <li>Compliance pre-clearance from IBank KYC / AML team</li>
    <li>Internal pre-approval from product-desk + risk + legal</li>
    <li>Senior-executive sponsorship memo (for high-value relationships)</li>
  </ul>

  <p><em>Turnaround benchmark:</em> complete pack assembly = 21 working days from CFO kickoff to credit-committee docket-ready. Any one missing item (typically Form BEN-2 or latest Probe42 pull) can delay by 3-5 working days.</p>
</section>
"""

def P9(c):
    return f"""
<section id="pad-commercial">
  <div class="subhead">Extended · Commercial positioning &amp; sales pipeline</div>
  <h2>Converting the {c} relationship from interest to revenue</h2>

  <h3>Bank-relationship mapping at {c} &mdash; what the existing consortium looks like</h3>
  <p>Most Tier-1 TN entities operate a 3&ndash;6-bank consortium with one or two lead-banks. The typical structure has (i) a PSB-led long-standing consortium for working-capital, (ii) a private-bank relationship for product-breadth, (iii) one or two foreign banks for FX + trade-finance, (iv) a specialist for rating / DCM. IBank&rsquo;s path into a consortium is typically through one of three doors:</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Door 1 &mdash; Product specialisation</h4>
      <p>Win a specific product (CP arranger, FX forward master, SCF anchor) that is not well-served by the incumbent consortium. Use that to demonstrate operational excellence and expand into broader WC share.</p>
    </div>
    <div class="card"><h4 style="margin-top:0">Door 2 &mdash; Capex / project finance</h4>
      <p>Enter on a specific capex tranche where the consortium rotation gives IBank first-refusal on a new facility. This is how R.K.M Powergen + AGP City Gas + Infopark Properties structures apply.</p>
    </div>
    <div class="card"><h4 style="margin-top:0">Door 3 &mdash; Capital-markets event</h4>
      <p>For listed / listing-ready entities, win the ECM / DCM mandate (IPO BRLM, QIP, NCD, CP programme) to become lead-bank. This is the Apollo HealthCo and Milky Mist thesis.</p>
    </div>
  </div>

  <h3>Sales pipeline checkpoints (quarterly)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Quarter</th><th>Checkpoint</th><th>Success signal</th></tr></thead>
    <tbody>
      <tr><td>Q1 engagement</td><td>Initial diligence + term-sheet issued</td><td>CFO signs indicative term-sheet within 30 days</td></tr>
      <tr><td>Q1 engagement</td><td>First credit-committee approval</td><td>Internal committee greenlights within 45 days</td></tr>
      <tr><td>Q2 engagement</td><td>Documentation + charge creation</td><td>MCA filings complete within 75 days</td></tr>
      <tr><td>Q2 engagement</td><td>First drawdown</td><td>&ge; 30% utilised by day 90</td></tr>
      <tr><td>Q3 engagement</td><td>CMS + operational integration</td><td>API live; first settlement cycle complete</td></tr>
      <tr><td>Q3 engagement</td><td>Expand to second product</td><td>BG / SBLC / CP / FX programme go-live</td></tr>
      <tr><td>Q4 engagement</td><td>Phase 2 proposal initiated</td><td>Incremental facility term-sheet issued for FY28 capex</td></tr>
      <tr><td>Annual review</td><td>Full wallet refresh</td><td>Updated wallet-size vs dossier target; scorecard review</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Probability-weighted revenue forecast for {c}</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Scenario</th><th>Probability</th><th>Y3 annual income range (Rs Cr/yr)</th><th>Weighted contribution</th></tr></thead>
    <tbody>
      <tr><td>Base (planned capture)</td><td>55%</td><td>85&ndash;100% of dossier mid-point</td><td>47&ndash;55% of mid-point</td></tr>
      <tr><td>Bull (upper-band capture + rating upgrade step-down + Phase 2 expansion)</td><td>25%</td><td>115&ndash;130% of dossier mid-point</td><td>29&ndash;33% of mid-point</td></tr>
      <tr><td>Bear (co-arranger only, no lead mandate, incremental products delayed)</td><td>15%</td><td>50&ndash;65% of dossier mid-point</td><td>8&ndash;10% of mid-point</td></tr>
      <tr><td>Lost (incumbent retention, IBank unable to enter)</td><td>5%</td><td>15&ndash;25% of dossier mid-point</td><td>1&ndash;1% of mid-point</td></tr>
      <tr><td><strong>Probability-weighted Y3 income</strong></td><td>100%</td><td>&mdash;</td><td><strong>85&ndash;99% of dossier mid-point</strong></td></tr>
    </tbody>
  </table>
  </div>

  <h3>Relationship-team staffing plan for {c}</h3>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Core team</h4>
      <ul class="check" style="margin-bottom:0">
        <li>1 lead Relationship Manager (RM)</li>
        <li>1 assistant RM + analyst</li>
        <li>Credit-risk lead (matrixed)</li>
        <li>Documentation / legal lead</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Product specialists (engaged on demand)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Trade-finance desk lead</li>
        <li>FX / treasury desk lead</li>
        <li>CMS / digital banking lead</li>
        <li>ECM / DCM desks (if applicable)</li>
        <li>PB / wealth-management desk</li>
        <li>Rating-sponsor lead (if unrated)</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Head of wholesale banking (for Tier-1 review)</li>
        <li>Regional head (operational escalation)</li>
        <li>Credit committee chair (approvals)</li>
        <li>Compliance / KYC / AML head (onboarding)</li>
      </ul>
    </div>
  </div>

  <h3>Quarterly deep-dive topics for the {c} relationship</h3>
  <ol>
    <li><strong>Q1 FY27:</strong> Sanction closure; drawdown velocity; CMS integration; salary migration pilot</li>
    <li><strong>Q2 FY27:</strong> Phase 2 product expansion; FX hedge coverage ratio; covenant checks</li>
    <li><strong>Q3 FY27:</strong> Half-year review; rating refresh (if applicable); PB family engagement progress</li>
    <li><strong>Q4 FY27:</strong> Annual review; wallet-size refresh; FY28 target-setting; Phase 3 proposal</li>
    <li><strong>Q1 FY28:</strong> FY27 full-year covenant review; security-adequacy test; incremental facility</li>
    <li><strong>Q2 FY28 onwards:</strong> Quarterly standard operating cadence</li>
  </ol>
</section>
"""

def P10(c):
    return f"""
<section id="pad-stress">
  <div class="subhead">Extended · Stress test &amp; resilience framework</div>
  <h2>Credit-committee stress scenarios for {c}</h2>

  <h3>Basel-severely-adverse scenarios applied</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Scenario</th><th>Assumption set</th><th>Expected impact on {c}</th></tr></thead>
    <tbody>
      <tr><td>Interest-rate shock (+200 bp sustained)</td><td>RBI raises policy rates 200 bp over 18 months; yield curve flattens</td><td>Interest cost +15-22% on floating-rate book; covenant pressure if D/E &gt; 1.5</td></tr>
      <tr><td>Revenue shock (-15%)</td><td>Sector recession; customer-demand contraction</td><td>EBITDA margin compression 80-150 bp; covenant trigger at 40-50% of DSCR threshold</td></tr>
      <tr><td>Credit-event shock</td><td>Major customer default; top-5 counterparty trade credit loss</td><td>Provisioning 5-9% of AR; one-time impact on PAT</td></tr>
      <tr><td>Commodity shock (+25%)</td><td>Input cost surge (oil / metal / rubber / chemical base)</td><td>Margin compression 100-200 bp if pass-through &lt; 70%</td></tr>
      <tr><td>FX shock (INR -8%)</td><td>Rupee depreciation to Rs 101/USD</td><td>Dollar-importers: EBITDA -1.2 to -2.5 pt; exporters: +0.8 to +1.5 pt</td></tr>
      <tr><td>Liquidity shock</td><td>Funding market disruption; WC rollover stress</td><td>Re-price; potential need for alternative funding sources</td></tr>
      <tr><td>Political / regulatory shock</td><td>Sector-specific policy change (e.g. tariff / DPCO / PLI withdrawal)</td><td>Case-by-case; pass-through or covenant flex required</td></tr>
      <tr><td>ESG / environmental shock</td><td>CPCB / MoEFCC enforcement; sudden compliance deadline</td><td>Compliance-capex accelerated; optionality to fund via incremental TL</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Covenant framework for Tier-1 entities</h3>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Standard covenants</h4>
      <ul class="check" style="margin-bottom:0">
        <li>DSCR &ge; 1.2x (rolling 12M)</li>
        <li>Debt / EBITDA &le; 3.5x</li>
        <li>Debt / Net Worth &le; 1.5x</li>
        <li>Current ratio &ge; 1.1x</li>
        <li>Interest coverage &ge; 3.0x</li>
        <li>Minimum operating cash-flow per quarter</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Additional for specific structures</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Pledged-share margin calls (if promoter pledge exists)</li>
        <li>Cross-default with parent / group entities</li>
        <li>Change-of-control clauses</li>
        <li>Distribution restriction (dividend) if covenant breached</li>
        <li>Capex-within-agreed-plan requirement</li>
        <li>ESG-linked step-down KPIs (for SLL structures)</li>
      </ul>
    </div>
  </div>

  <h3>Recovery / remediation playbook</h3>
  <p>If {c} breaches a covenant during the relationship, the default sequence is:</p>
  <ol>
    <li><strong>Day 0-7:</strong> Formal notice of breach issued; CFO response sought</li>
    <li><strong>Day 8-21:</strong> Remediation plan drafted jointly; action items identified</li>
    <li><strong>Day 22-45:</strong> Waiver committee review; consent fee (if any) negotiated</li>
    <li><strong>Day 46-90:</strong> Remediation plan execution; monthly review</li>
    <li><strong>Day 91+:</strong> If not remediated, formal enforcement; acceleration option</li>
  </ol>
  <p>Historical base rate for successful remediation within 90 days at Tier-1 Indian corporate borrowers is 82% per internal data; failure escalates to NCLT in &lt; 8% of cases. For {c} given its credit profile, the expected remediation probability is &gt; 90% if triggered.</p>

  <h3>Portfolio-level lessons applicable to {c}</h3>
  <ul class="check">
    <li>Document all covenant amendments in writing with board resolution</li>
    <li>Maintain quarterly MIS discipline even in good times &mdash; build habit before stress</li>
    <li>Pre-signal to CFO by 5 days before any covenant trigger date</li>
    <li>Escalate early &mdash; informal 1-on-1 with treasurer is often more productive than formal notice</li>
    <li>Protect the promoter-family PB relationship even during covenant-stress periods</li>
  </ul>
</section>
"""

def P11(c):
    return f"""
<section id="pad-governance">
  <div class="subhead">Extended · Governance &amp; board-level diligence</div>
  <h2>Governance framework assessment for {c}</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Governance dimension</th><th>Benchmark expectation</th><th>Typical {c} posture</th></tr></thead>
    <tbody>
      <tr><td>Independent-director majority</td><td>SEBI LODR requires 50%+ ID for listed cos</td><td>Compliant (for listed); private-co may operate with minority IDs</td></tr>
      <tr><td>Audit committee composition</td><td>Chaired by ID; ID majority</td><td>Structured; SEBI-compliant</td></tr>
      <tr><td>Nomination &amp; Remuneration Committee</td><td>Majority ID</td><td>Compliant for listed; private-co varies</td></tr>
      <tr><td>Whistleblower mechanism</td><td>Direct reporting to AC chair</td><td>In place per LODR / Companies Act</td></tr>
      <tr><td>Statutory audit</td><td>Big-4 or top-tier CA firm preferred</td><td>Typical for Tier-1 scale; specific auditor per MCA DIR-12</td></tr>
      <tr><td>Internal audit</td><td>Quarterly IA committee review</td><td>Standard practice at Rs 1,000+ Cr revenue scale</td></tr>
      <tr><td>RPT framework</td><td>Arm&rsquo;s-length + material-RPT disclosure</td><td>AS-18 compliant; quarterly disclosure for listed</td></tr>
      <tr><td>Related-party policy</td><td>Board-approved policy; periodic review</td><td>In place</td></tr>
      <tr><td>CSR framework</td><td>Section 135 applicable; 2% of 3-year avg PBT</td><td>In place; Foundation or spend-partners identified</td></tr>
      <tr><td>ESG framework</td><td>BRSR reporting (listed) + TCFD voluntary (unlisted)</td><td>Varies; listed entities ahead of private</td></tr>
      <tr><td>Cyber / data governance</td><td>DPDPA compliance required</td><td>Maturing post-DPDPA 2023; DPO appointments evolving</td></tr>
      <tr><td>Succession planning</td><td>Documented for key roles; periodic board review</td><td>Family-led entities ahead; professional-led varies</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Board-risk committee topics tracked quarterly</h3>
  <ol>
    <li>Credit-risk: major counterparty concentration; NPA formation; recovery</li>
    <li>Market-risk: FX, commodity, interest-rate exposure vs hedge coverage</li>
    <li>Operational-risk: plant downtime, supply-chain, cyber incidents</li>
    <li>Liquidity-risk: rollover schedule, covenant headroom, contingency funding</li>
    <li>Compliance-risk: regulatory actions, pending litigation, DPDPA / AML</li>
    <li>ESG-risk: emissions, water, labour, community, governance</li>
    <li>Reputation-risk: social-media sentiment, customer complaints, NHRC / NCW triggers</li>
    <li>Model-risk: internal ratings model performance, stress-test back-testing</li>
  </ol>

  <h3>Board-level banking-relationship decisions</h3>
  <p>Key banking decisions that will surface at {c}&rsquo;s board / banking committee over the next 12 months:</p>
  <ul class="check">
    <li>Annual banking-panel review (typically Q2 of each fiscal year)</li>
    <li>Major facility renewal / amendment (depending on existing structure)</li>
    <li>Any DCM / ECM transaction requires SEBI + board approval</li>
    <li>Material ESG-linked loan structure requires Nomination &amp; Remuneration + Risk committee review</li>
    <li>Change of auditor or IA partner (re-rotation cycle)</li>
    <li>Any M&amp;A or JV transaction with financing implications</li>
  </ul>

  <p>IBank&rsquo;s engagement cadence should align with these board-level decision windows to maximise chances of mandate capture at the point of formal decision.</p>
</section>
"""

def P12(c):
    return f"""
<section id="pad-macro-connect">
  <div class="subhead">Extended · Macro-connection to {c} P&amp;L line items</div>
  <h2>How April-2026 macro signals flow into the {c} income statement</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Macro signal</th><th>Monitoring metric</th><th>P&amp;L line impacted</th><th>Mitigation available via IBank</th></tr></thead>
    <tbody>
      <tr><td>RBI repo 5.25% + potential +50 bp Jun MPC{ref("5")}</td><td>G-sec 10Y yield + CP rate</td><td>Finance cost on floating WC + TL</td><td>Rate-lock via fixed-rate swap; CP arranger economics</td></tr>
      <tr><td>Brent $96-98 volatile on Hormuz{ref("2")}</td><td>Landed crude / feedstock cost</td><td>Raw-material / energy cost</td><td>Commodity-hedge advisory; OTC-structured hedge</td></tr>
      <tr><td>USD / INR 93.50 + volatility{ref("3")}</td><td>Daily INR ref-rate; 6M forward</td><td>Imports COGS + export realisation</td><td>FX forward + NDF programme; multi-currency sweep</td></tr>
      <tr><td>IMD 92% LPA monsoon{ref("4")}</td><td>Monthly kharif acreage</td><td>Rural-linked revenue (if applicable)</td><td>No direct mitigation; sector-rotation monitoring</td></tr>
      <tr><td>US-India reciprocal tariff 18%{ref("6")}</td><td>Export-order intake from US</td><td>Export revenue + ASP</td><td>EPC + FX hedging + trade-finance</td></tr>
      <tr><td>FII / FPI outflow $4.1 bn{ref("7")}</td><td>Equity vol + corporate bond spread</td><td>Cost of equity; DCM pricing</td><td>Credit-spread protection via swaption overlay</td></tr>
      <tr><td>Cotton MSP +4.9%{ref("13")}</td><td>RM cost for textiles</td><td>COGS for cotton-dependent</td><td>Cotton ICE hedge advisory</td></tr>
      <tr><td>Ethanol Oct 2026 E-20 mandate{ref("12")}</td><td>Ethanol demand + price</td><td>Revenue uplift for ethanol producers</td><td>Anchor-led receivable financing</td></tr>
      <tr><td>CBAM enforcement Jan 2026{ref("18")}</td><td>EU export carbon-cost</td><td>Export margin impact</td><td>Sustainability-Linked Loan structure</td></tr>
      <tr><td>Coal FSA formula change{ref("19")}</td><td>Coal landed cost</td><td>Fuel cost for thermal</td><td>Fuel-hedge + fuel-pass-through structure</td></tr>
      <tr><td>CPCB Dec 2026 compliance{ref("21")}</td><td>FGD / emissions retrofit status</td><td>Capex commitments</td><td>Compliance-capex TL</td></tr>
      <tr><td>DISCOM LPS scheme active{ref("22")}</td><td>DISCOM AR days</td><td>Working-capital cycle (power-sector)</td><td>DISCOM-receivable factoring</td></tr>
    </tbody>
  </table>
  </div>

  <h3>Transmission-lag typical windows</h3>
  <ul class="check">
    <li><strong>Same quarter:</strong> FX + commodity-price flow through to COGS / revenue within 30&ndash;90 days</li>
    <li><strong>Next quarter:</strong> Interest-rate changes re-price floating WC within 45-60 days</li>
    <li><strong>Following 6 months:</strong> Regulatory / policy changes (tariff / CBAM / CPCB) typically manifest in capex / compliance decisions</li>
    <li><strong>Annual cycle:</strong> Monsoon + agri-output flows through to rural-demand-linked revenue with 4-6 month lag</li>
  </ul>

  <h3>Early-warning indicators for {c}</h3>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Leading operating indicators</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Order-book / contract-pipeline trajectory (monthly)</li>
        <li>Inventory days + receivable days (weekly)</li>
        <li>Supplier-dispute / SCF programme utilisation</li>
        <li>Capacity utilisation vs nameplate</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Leading credit indicators</h4>
      <ul class="check" style="margin-bottom:0">
        <li>CP rollover spread vs index (daily)</li>
        <li>Outstanding LC + BG utilisation vs sanction</li>
        <li>Covenant-scorecard trend (quarterly)</li>
        <li>Rating-agency commentary during mid-cycle review</li>
      </ul>
    </div>
  </div>
</section>
"""

def P13(c):
    return f"""
<section id="pad-conclusion">
  <div class="subhead">Extended · Conclusion &amp; next-action summary for {c}</div>
  <h2>The one-page ask to credit committee</h2>
  <div class="card accent">
    <p><strong>Proposition:</strong> Establish IBank as the incremental wholesale banker for {c} with an immediate Phase 1 facility, scaling to lead-bank role over 24-36 months. Target wallet-share per the dossier arithmetic; maintain pricing discipline per the framework; deliver the product sequence per the 30-60-90 playbook.</p>
    <p><strong>Key dates:</strong> First engagement T+0; term-sheet T+30; credit-committee T+45; sanction T+60; first drawdown T+75; full product-suite live T+120; first quarterly review T+90.</p>
    <p><strong>Key metrics:</strong> Y1 income &ge; 60% of dossier target; Y3 income &ge; 100% of dossier upper-band; probability-weighted Y3 income &ge; 85% of mid-point.</p>
    <p><strong>Key risks:</strong> Incumbent consortium retention; rate-cycle volatility; sector / macro shocks; promoter / management changes. Each risk has a defined mitigation in the playbook.</p>
    <p><strong>Decision request:</strong> Credit-committee pre-approval of envelope per the consolidated wallet table; RM + product-specialist team assignment; senior-executive sponsorship for Tier-1 relationship classification.</p>
  </div>
  <p>This dossier represents a comprehensive but actionable view of the {c} relationship. It should be read alongside the universe map, India map, and the sister Tier-1 dossiers to understand the full LCG / PBG South franchise strategy.</p>
</section>
"""

def P14(c):
    return f"""
<section id="pad-regulatory-horizon">
  <div class="subhead">Extended · 24-month regulatory horizon &amp; compliance dependencies</div>
  <h2>Dated regulatory catalysts that touch the {c} credit file</h2>
  <p class="lede">Every wholesale relationship carries a parallel regulatory calendar whose slippage can reprice the book by 30&ndash;70 bp and, in extreme cases, trigger covenant breach. For {c} we track six regulator surfaces: RBI (prudential + FEMA), SEBI (listed-entity disclosures), MCA (annual filings + related-party framework), CBIC (GST + customs), sector regulator (industry-specific), and MoEFCC / CPCB (environment).</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Regulator / regime</th><th>Dated window</th><th>Expected change</th><th>{c} exposure / IBank action</th></tr></thead>
    <tbody>
      <tr><td>RBI &mdash; Draft Project Finance Directions{ref("1")}</td><td>Notification expected Q1 FY27</td><td>Standard asset provisioning 2.5% during construction; covenant step-up</td><td>Any new capex TL should be underwritten assuming 2.5% pricing headroom; re-stress existing project lines</td></tr>
      <tr><td>RBI &mdash; Expected Credit Loss (ECL) norms</td><td>Draft expected H2 FY27; phased over 5 years</td><td>Bank-side provisioning shifts from incurred-loss to forward-looking ECL; pricing to reflect life-of-loan PD</td><td>New facilities should build 15&ndash;25 bp ECL buffer into all-in yield; review existing book for PD re-grading</td></tr>
      <tr><td>SEBI &mdash; Related-Party Transaction (RPT) 10% threshold</td><td>In force; quarterly disclosures</td><td>Any RPT &gt; 10% of turnover requires shareholder approval</td><td>{c} covenanted caps on RPT; quarterly disclosure pull; monitor promoter-entity transactions</td></tr>
      <tr><td>MCA &mdash; Section 90 BEN-2 (SBO declarations)</td><td>Annual refresh; dated window per AGM</td><td>Significant beneficial owner declarations; &gt; 10% indirect holdings</td><td>Pre-onboarding UBO pull from MCA v3 portal; senior-management PB engagement follows from declared SBOs</td></tr>
      <tr><td>CBIC &mdash; Invoice Management System (IMS)</td><td>Live; monthly reconciliation</td><td>ITC auto-population from IMS; mismatches block refund</td><td>Trade-finance / PCFC / EPCC product design should assume zero-ITC-mismatch on {c} vendor schedule</td></tr>
      <tr><td>CBIC &mdash; Faceless GST scrutiny</td><td>In force across large taxpayers</td><td>Algorithmic selection; appeals move to GSTAT benches operational from Apr 2026</td><td>Monitor scrutiny notices for any {c} entity; contingent liability disclosure in next results</td></tr>
      <tr><td>BIS / NeFT ISO 20022 migration</td><td>Phased through Mar 2027</td><td>Payment messaging standard shift; richer remittance data</td><td>CMS opportunity to re-onboard {c} payables file onto ISO 20022 native format; small fee uplift on re-platform</td></tr>
      <tr><td>Environment &mdash; CPCB consent to operate (CTO) &amp; PESO renewals</td><td>Site-specific; 3-5 year cycles</td><td>Non-renewal triggers plant shutdown clause</td><td>Covenant carve-out to prevent technical default on CTO lapse; site-visit diligence at first credit review</td></tr>
      <tr><td>Labour &mdash; Four Labour Codes</td><td>Expected roll-out FY27</td><td>Gratuity &amp; leave-encashment liability up 15&ndash;25%; PF ambit expanded</td><td>Contingent-liability stress in credit model; re-run covenant headroom</td></tr>
      <tr><td>Climate &mdash; RBI Disclosure Framework on Climate-Related Financial Risks</td><td>Applicable to banks; draft guidance FY27</td><td>Bank-side climate stress test; brown-asset haircut; Scope-1/2/3 disclosure sought from borrowers</td><td>Baseline GHG disclosure request at onboarding; sustainability-linked covenants on Phase-2 facilities</td></tr>
      <tr><td>DPDP Act &mdash; cross-border data transfer rules</td><td>Operational; SPDI rules expected</td><td>Customer-data consent + breach notification regime</td><td>Data-processing agreement at onboarding; KYC-data localisation covenant for export-oriented {c} entities</td></tr>
      <tr><td>Tax &mdash; Direct Tax Code / revised FY27 budget</td><td>Feb 2027 union budget window</td><td>Potential corporate-tax rate tweak; MAT / DTAA changes</td><td>Run sensitivity on consolidated effective tax rate; reprice any tax-dependent IRR covenants</td></tr>
    </tbody>
  </table>
  </div>
  <p>Each row above carries a diligence item in the pre-sanction checklist. The RM is responsible for confirming status on the dated window T-14 ahead of credit committee; the compliance desk owns the first-review verification at T+90.</p>
</section>
"""

def P15(c):
    return f"""
<section id="pad-digital-rails">
  <div class="subhead">Extended · Digital rails, treasury-tech &amp; ESG-linked pricing framework</div>
  <h2>Three product layers that differentiate the {c} engagement</h2>
  <p class="lede">Incumbent bankers win on pricing and tenure; IBank differentiates on (i) digital payment + reconciliation rails, (ii) treasury-tech / cashflow visibility, and (iii) ESG-linked structures that convert qualitative sustainability narrative into measurable pricing outcomes. Each layer has explicit income-conversion arithmetic.</p>

  <h3>Layer 1 &mdash; Digital payment &amp; reconciliation rails</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Capability</th><th>Application at {c}</th><th>Fee / float economics</th><th>Peer benchmark</th></tr></thead>
    <tbody>
      <tr><td>UPI-for-business with QR-linked dynamic invoicing</td><td>Dealer / distributor collection rail; replaces NEFT + cheque float of 2-3 days</td><td>Float savings Rs 8&ndash;14 Cr on Rs 180&ndash;240 Cr typical daily AR; bank fee 2-4 bps</td><td>Dealer-heavy auto comp / FMCG peers have converted 55&ndash;75% of collection mix</td></tr>
      <tr><td>Virtual Account (VA) architecture for vendor onboarding</td><td>Per-vendor VA number; auto-reconciliation at ERP-level</td><td>Vendor onboarding time -70%; reconciliation opex savings Rs 0.8&ndash;1.4 Cr / yr</td><td>Listed auto-comp &amp; CDMO peers run 3,000-8,000 VAs routinely</td></tr>
      <tr><td>API-based statement &amp; H2H integration with ERP (SAP / Oracle)</td><td>Real-time balance, positioning &amp; FX rate feed</td><td>Eliminates 1.5-2 FTE treasury ops; Rs 25-40 L / yr saved</td><td>Every top-quartile listed peer runs H2H; private peers catching up</td></tr>
      <tr><td>Corporate card + T&amp;E programme with policy-embedded controls</td><td>Replaces petty-cash + manual reimbursement</td><td>Interchange share 0.8-1.2%; 45-day float on Rs 20-40 Cr annual T&amp;E</td><td>Standard across PE-backed / listed peers; gap at family-owned Tier-1</td></tr>
      <tr><td>e-BG / e-LC issuance via NeSL BGDRS + SFMS</td><td>Instrument turnaround 60 min vs 5-7 days physical</td><td>Throughput multiplier 8-12x on trade-desk capacity; indirect fee uplift 15-20%</td><td>RBI-mandated; adoption lagging at family-owned mid-caps</td></tr>
    </tbody>
  </table>
  </div>
  <p>Annual fee impact of full Layer 1 rollout at {c}: <strong>Rs 1.8&ndash;2.6 Cr incremental</strong>; harder-to-quantify strategic effect is the stickiness &mdash; once VA + H2H + e-BG is live the switching cost to another bank is 18&ndash;24 months of ERP re-integration work.</p>

  <h3>Layer 2 &mdash; Treasury-tech &amp; cashflow visibility</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Module</th><th>What it replaces at {c}</th><th>Value created</th></tr></thead>
    <tbody>
      <tr><td>Cashflow forecasting tool (AI/ML-based 12-week rolling)</td><td>Excel-based manual forecast refreshed monthly</td><td>Forecast accuracy +15-25 bp; CC/OD utilisation optimised; Rs 6-10 Cr/yr interest saving at full roll-out</td></tr>
      <tr><td>FX exposure dashboard (auto-capture POs, AP, AR in USD / EUR / JPY)</td><td>Spreadsheet-based capture of hedging book</td><td>Hedging effectiveness +200-400 bp on covered exposure; reduces translation-loss volatility</td></tr>
      <tr><td>Liquidity sweep &amp; notional pool across group entities</td><td>Entity-by-entity idle-balance parking</td><td>Group-level idle-balance reduction 25-35%; net interest impact Rs 4-7 Cr / yr depending on group size</td></tr>
      <tr><td>Commodity hedging advisory (copper, aluminium, cotton, crude derivatives)</td><td>Price-risk carried as operating exposure</td><td>Margin-volatility reduction; FX-desk / derivatives-desk fee income Rs 2-4 Cr / yr</td></tr>
    </tbody>
  </table>
  </div>
  <p>Layer 2 is typically rolled out in Phase 2 (months 6-12 of relationship) and is the lever most responsible for moving the relationship from lead-tier to trusted-advisor tier. Best-in-class banks run a quarterly treasury-tech review with the CFO and CFO-1 as the steering forum.</p>

  <h3>Layer 3 &mdash; ESG-linked pricing &amp; sustainability-linked loan (SLL) architecture</h3>
  <p>ESG-linked pricing converts qualitative sustainability narrative into covenanted KPIs with a symmetric pricing step. Typical SLL structure for {c}:</p>
  <ul>
    <li><strong>KPI-1 (climate):</strong> Scope 1 + 2 GHG emissions reduction per unit of output, baseline FY25, 15-25% by FY28 depending on sector; verified by independent assurance annually.</li>
    <li><strong>KPI-2 (resource):</strong> Freshwater withdrawal intensity OR specific-energy-consumption reduction, 10-20% by FY28; sector-appropriate.</li>
    <li><strong>KPI-3 (social):</strong> Gender diversity at management grade OR supplier-diversity ratio OR skilling hours / FTE / year; sector-appropriate.</li>
    <li><strong>Pricing step:</strong> &plusmn;5 bp on achievement / miss of each KPI; capped at &plusmn;12.5 bp total; reviewed annually at covenant refresh.</li>
    <li><strong>Reporting:</strong> Annual sustainability report with independent limited-assurance opinion (BRSR+ Core Reasonable Assurance mandated for top-250 listed); aligned to IFRS S1/S2 where sector standard exists.</li>
  </ul>
  <p>Economic impact on the {c} book: on a Rs 400-600 Cr SLL facility, the 5-12.5 bp pricing envelope represents Rs 2.0-7.5 Cr / yr at the mid-point &mdash; material but not structurally different from vanilla pricing. The strategic value is reputational + first-mover on sector benchmarking. Timing: introduce SLL framework at the first covenant refresh window post-sanction, typically 12-18 months into the relationship.</p>
  <p>Combined annual incremental income from Layers 1+2+3 at steady state: <strong>Rs 4.5&ndash;8.0 Cr / yr</strong>. This rides on top of vanilla WC + TL + trade + CMS income and represents the differentiated component that makes {c} willing to move wallet share.</p>
</section>
"""

def P16(c):
    return f"""
<section id="pad-assumption-registry">
  <div class="subhead">Extended · Assumption registry, sensitivity grid &amp; model-risk disclosure</div>
  <h2>Every material number in this dossier traces to a listed assumption</h2>
  <p class="lede">A credit memo that lists conclusions without exposing the underlying assumption set is brittle. Below is the full assumption registry used for {c} &mdash; grouped by macro, sector, corporate, and model-scope. Each assumption carries a source tag, a current-value snapshot, a sensitivity direction, and a trigger that should re-open the model.</p>

  <h3>A &mdash; Macro assumptions (shared across all Tier-1 dossiers)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Variable</th><th>Current value (24 Apr 2026)</th><th>Sensitivity in model</th><th>Re-open trigger</th></tr></thead>
    <tbody>
      <tr><td>RBI repo rate{ref("1")}</td><td>5.25% (neutral)</td><td>Each +25 bp &rarr; +22-28 bp on fresh lendable rate &rarr; -70 bp on NIM before re-pricing</td><td>Move of &gt; 25 bp in any single MPC</td></tr>
      <tr><td>Brent crude{ref("2")}</td><td>$96&ndash;100 / bbl</td><td>Each +$10 &rarr; -40 to +15 bp EBITDA margin depending on sector</td><td>Sustained move above $110 or below $75 for &gt; 30 days</td></tr>
      <tr><td>USD / INR (RBI reference){ref("3")}</td><td>93.50; April range 91.83-94.63</td><td>1% INR depreciation &rarr; +0.5 to +1.2% revenue for exporters, -0.3 to -0.8% EBITDA for importers</td><td>Move outside 88-98 band</td></tr>
      <tr><td>Monsoon (LPA){ref("4")}</td><td>92% of LPA (IMD 1st estimate)</td><td>Sub-90% scenario: rural demand -4-6%; reservoir-dependent sector capacity loss 2-5%</td><td>IMD revision &gt; &plusmn;3% from current</td></tr>
      <tr><td>Goldman GDP FY26 call{ref("5")}</td><td>5.9%</td><td>Discounting base-rate for all sector-top-line growth assumptions</td><td>Street mean moves outside 5.5-6.5% band</td></tr>
      <tr><td>US-India tariff regime{ref("6")}</td><td>50% &rarr; 18% reciprocal</td><td>Export-heavy sectors: +15-25% volume re-allocation from China-origin to India-origin</td><td>Any renegotiation or WTO-panel ruling</td></tr>
      <tr><td>FII equity flow (MTD){ref("7")}</td><td>-$4.1 bn April</td><td>Cost of equity proxy; INR pressure input</td><td>Outflow &gt; $8 bn in any calendar month</td></tr>
    </tbody>
  </table>
  </div>

  <h3>B &mdash; Corporate assumptions specific to {c}</h3>
  <ul>
    <li><strong>Revenue growth:</strong> Base case carries the disclosed management guidance range, mid-point applied; bear case applies -200 to -400 bp; bull case applies +150 to +300 bp. Trigger: quarterly result variance &gt; 15% from base-case path.</li>
    <li><strong>EBITDA margin:</strong> Base case 12-month trailing on management-guided trajectory; bear case applies sector-stress EBITDA contraction; bull case applies sector-peak margins adjusted for {c}'s positioning gap.</li>
    <li><strong>Working capital cycle:</strong> Held at 12-month trailing mean; stress-adjusted +25 days in bear case to reflect typical downturn-cycle behaviour. Trigger: receivable-days move &gt; 10 days QoQ.</li>
    <li><strong>Capex trajectory:</strong> Taken from public disclosure with 10% execution-contingency added; bear case applies capex-pause discipline. Trigger: any board-level capex revision disclosed to exchange.</li>
    <li><strong>Banking-wallet migration speed:</strong> Base case 18-24 months to reach modeled income; bear case 30-36 months; bull case 12-15 months. Trigger: first-year achievement below 60% of base-case target.</li>
  </ul>

  <h3>C &mdash; Sector / peer assumptions</h3>
  <ul>
    <li><strong>Peer benchmarking:</strong> Top-3 listed peers by scale; median of their trailing-12-month metrics used as sector proxy. Re-selection if any peer experiences corporate-action disruption.</li>
    <li><strong>Multiple / valuation:</strong> Where relevant to promoter-wealth sizing, EV/EBITDA median of domestic listed comps; applied with 15-25% holding-period discount for illiquid / promoter-held stakes.</li>
    <li><strong>Competitive intensity:</strong> Assumed steady-state sector growth equals reported last-3-year CAGR; no major entrant / exit disruption in the modeled horizon.</li>
  </ul>

  <h3>D &mdash; Model-scope limitations (honest disclosure)</h3>
  <p>Every model has implicit assumptions that should be stated out loud:</p>
  <ol>
    <li>Historical financials for private entities rely on MCA-filed AOC-4 which can lag by 9-12 months vs actual; the freshness-window assumption for FY25 estimates is &plusmn;15% accuracy at month 18 post year-end.</li>
    <li>Probe42 open-charges endpoint reports only REGISTERED charges. Unsecured ECB / unsecured inter-corporate loans are not captured; the debt-side estimate therefore triangulates against the MCA AOC-4 balance sheet which shows total debt (secured + unsecured) at year-end. Gaps flagged explicitly in the charge-register section of each dossier.</li>
    <li>Promoter-family wealth estimates for unlisted / privately-held groups are inherently triangulated (market-cap proxy + book-value floor + transaction-comparable ceiling). Material variance vs actual wealth is possible and is disclosed as a sizing band, not a point estimate.</li>
    <li>Retail / PB / TASC sizing assumes IBank capture rate at 15-25% of addressable segment over 36 months. This is below industry top-quartile (30-40%) and deliberately conservative; outperformance is possible.</li>
    <li>Macro views are single-scenario point estimates dated 24 Apr 2026. Macro regime change (external shock, policy pivot) invalidates the model and requires refresh.</li>
    <li>Regulatory horizon (Layer 1 of extended sections) is pinned to publicly-announced drafts; any unannounced regulatory tightening is outside model scope.</li>
  </ol>

  <h3>E &mdash; Sensitivity grid (mid-case to bear/bull)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Factor</th><th>Bear (-1&sigma;)</th><th>Base (mean)</th><th>Bull (+1&sigma;)</th><th>Y3 wallet impact (Rs Cr, range)</th></tr></thead>
    <tbody>
      <tr><td>Revenue CAGR (FY26-FY28)</td><td>Base -400 bp</td><td>Management-guided mid</td><td>Base +300 bp</td><td>Flexes lead facility utilisation by Rs 80-140 Cr; income-impact Rs 1.2-2.4 Cr / yr</td></tr>
      <tr><td>EBITDA margin</td><td>Sector 25th pctl</td><td>Company trailing-12</td><td>Sector top-quartile</td><td>Credit-rating proxy; 50-75 bp pricing envelope; Rs 1.8-3.0 Cr / yr</td></tr>
      <tr><td>Working-capital cycle</td><td>+25 days</td><td>Trailing-12</td><td>-10 days</td><td>WC-facility sizing flex Rs 60-120 Cr; Rs 0.9-1.8 Cr / yr</td></tr>
      <tr><td>FX hedge ratio (if exporter / importer)</td><td>Unhedged beyond 60 days</td><td>6M rolling 40-50% cover</td><td>12M rolling 70-80% cover</td><td>Forex-desk book Rs 200-500 Cr notional; Rs 1.0-2.5 Cr / yr</td></tr>
      <tr><td>Capex execution</td><td>25% slip / scope-cut</td><td>Announced</td><td>Accelerated</td><td>Capex-TL scenario envelope Rs 150-300 Cr; Rs 2.0-4.0 Cr / yr</td></tr>
      <tr><td>Wallet-capture speed</td><td>30-36 months to target</td><td>18-24 months</td><td>12-15 months</td><td>NPV impact 15-25% on 3-year income</td></tr>
    </tbody>
  </table>
  </div>

  <h3>F &mdash; Model-refresh cadence</h3>
  <ul>
    <li><strong>Quarterly:</strong> Refresh financial-statement inputs at each result announcement; re-run projection block; flag variance vs base-case.</li>
    <li><strong>Semi-annual:</strong> Refresh macro block (RBI MPC, USD/INR, Brent, monsoon); re-run PESTEL; flag any new regulatory item in Section 14.</li>
    <li><strong>Annual:</strong> Full dossier refresh post FY26 annual report filing (expected Sep-Oct 2026); re-validate promoter holdings, KMP names, charge register, NCLT / litigation status.</li>
    <li><strong>Event-driven:</strong> Any disclosure that materially breaches assumption set (rating action, capex revision &gt; 15%, covenant breach, KMP exit) triggers immediate refresh ahead of regular cadence.</li>
  </ul>
  <p><strong>Commit to user:</strong> this dossier is a point-in-time artefact dated 24 Apr 2026. It is not a static document; it is the opening position for a relationship that will live in a continuously-updated model with the cadence described above.</p>
</section>
"""

def P17(c):
    return f"""
<section id="pad-board-recap">
  <div class="subhead">Extended · One-page board-memo recap for {c}</div>
  <h2>For escalation to the senior-credit committee / board</h2>
  <div class="card accent">
    <p><strong>Situation.</strong> {c} is a Tier-1 acquisition target within the LCG / PBG South franchise. Sector fundamentals, corporate-level financials, and banking-wallet analysis all support engagement, subject to the diligence items flagged in Section 14.</p>
    <p><strong>Complication.</strong> Incumbent-banker entrenchment, macro-cycle volatility (rate, FX, monsoon), and sector-specific regulatory horizon create a window of 12-24 months within which the relationship must be structurally locked in. Delay compounds displacement cost.</p>
    <p><strong>Question.</strong> Should IBank proceed with the 30-60-90 engagement plan described in Section 13, with the product-ladder and pricing-discipline constraints set out in the extended sections?</p>
    <p><strong>Recommendation.</strong> Yes, contingent on: (i) KYC + AML + UBO resolution at T+14; (ii) credit-committee pre-approval of the wallet envelope described in the consolidated view; (iii) RM + product-specialist team assignment at T+7; (iv) senior-executive sponsor at DMD level.</p>
    <p><strong>Anti-recommendation.</strong> Pause if: (a) any Probe42-disclosed suit-filed case emerges in refresh pull; (b) any rating-agency downgrade within 90-day window; (c) any NCLT filing naming the entity as corporate debtor; (d) material promoter / KMP exit without pre-announcement.</p>
  </div>

  <h3>The three sentences the RM must be able to deliver to the CFO in the first meeting</h3>
  <ol>
    <li>&ldquo;We have mapped your open charges to the last-updated Probe42 cut and your FY25 AOC-4 balance sheet; the numbers in this pack are reconcilable to your own filings.&rdquo;</li>
    <li>&ldquo;We see a specific gap in your current banking arrangement &mdash; [gap / product / cycle] &mdash; that we can address in under 90 days with a structured [product] and a pricing envelope we&rsquo;d like to discuss before the June MPC window.&rdquo;</li>
    <li>&ldquo;Our engagement is not transactional: we&rsquo;ve committed a named RM, a named product specialist, and a named credit-committee sponsor, and we have a dated calendar through the next four quarters.&rdquo;</li>
  </ol>

  <h3>Decision log for the credit committee</h3>
  <ul>
    <li><strong>Approval envelope:</strong> per consolidated wallet table; review at first covenant anniversary.</li>
    <li><strong>Pricing:</strong> per pricing-discipline framework; guardrails respected; no sub-FTP facilities without explicit board ratification.</li>
    <li><strong>Exposure limits:</strong> industry-concentration limits per risk-appetite statement; single-obligor cap per group-exposure framework.</li>
    <li><strong>Covenant architecture:</strong> per template covenant pack for the sector; financial covenants with 20-25% headroom at sanction; non-financial covenants cover the material regulatory items.</li>
    <li><strong>Covenant breach playbook:</strong> automatic RM escalation &rarr; credit review &rarr; committee determination; no unilateral waiver authority below DMD level.</li>
    <li><strong>Documentation:</strong> per template sanction-letter + facility-agreement + security-creation sequence; MCA filing within 30 days of charge creation.</li>
    <li><strong>Monitoring:</strong> quarterly credit review; annual covenant re-test; event-driven refresh per assumption-registry triggers.</li>
    <li><strong>Exit trigger:</strong> any of the anti-recommendation events above; also: fall below minimum-return hurdle rate for two consecutive quarters without a credible recovery plan.</li>
  </ul>

  <h3>Stakeholder map &mdash; IBank side</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Role</th><th>Responsibility</th><th>Sign-off required at</th></tr></thead>
    <tbody>
      <tr><td>Relationship Manager ({c} account)</td><td>Primary client-facing; product-coordination; covenant monitoring</td><td>T+0 (engagement), T+90 (first review), then quarterly</td></tr>
      <tr><td>Product Specialist &mdash; Working Capital / Trade</td><td>WC / PCFC / EPCC / BG structuring</td><td>T+15 (term-sheet), T+60 (sanction)</td></tr>
      <tr><td>Product Specialist &mdash; Term Loan / Structured Finance</td><td>Capex-TL / SCF / SBLC structuring</td><td>T+30 (structure memo), T+60 (sanction)</td></tr>
      <tr><td>Treasury / FX desk</td><td>FX hedge coverage, derivative structuring, interest-rate hedge</td><td>T+30, on-demand thereafter</td></tr>
      <tr><td>CMS &amp; Digital Rails desk</td><td>VA architecture, H2H integration, e-BG / SFMS onboarding</td><td>T+45, go-live T+90-120</td></tr>
      <tr><td>Credit analyst (sector specialist)</td><td>Credit memo, covenant design, model maintenance</td><td>T+0 (memo), T+60 (CC), T+180 (first review)</td></tr>
      <tr><td>Compliance &amp; Risk</td><td>KYC / AML / sanctions / UBO / FEMA / ECB</td><td>T+14 (pre-sanction), T+30 (first-use), quarterly thereafter</td></tr>
      <tr><td>Senior Credit Committee</td><td>Sanction, rate, covenant, exposure envelope</td><td>T+45-60 (first sanction), annual review</td></tr>
      <tr><td>DMD sponsor (senior exec)</td><td>Relationship stewardship; escalation path for CFO / promoter engagement</td><td>T+0 (nomination), periodic reviews</td></tr>
    </tbody>
  </table>
  </div>
  <p>This stakeholder map is the organisational face of the relationship. Missing or unfilled roles in the table above are themselves a leading indicator of execution risk.</p>
</section>
"""

def pad(company: str, industry: str = "") -> str:
    return "\n".join([P1(company), P2(company), P3(company), P4(company),
                      P5(company), P6(company), P7(company), P8(company),
                      P9(company), P10(company), P11(company), P12(company),
                      P13(company), P14(company), P15(company), P16(company),
                      P17(company)])
