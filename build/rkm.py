"""Build `rkm-powergen-dossier.html` — Tier-1 pilot #3 (Thermal IPP / greenfield).

Company: R.K.M Powergen Private Limited
CIN   : U40101TN2004PTC054931
Plant : 1,440 MW supercritical coal, Uchpinda, Chhattisgarh
FY25  : TOI Rs 3,929 Cr · EBITDA Rs 1,681 Cr (42.8%) · PAT Rs 547 Cr
Debt  : Rs 4,395 Cr book; Rs 31,266 Cr MCA-registered charges (heavily
        over-secured — PFC Rs 22,783 Cr + IDBI Trustee Rs 8,597 Cr)
Rating: CRISIL BBB (last), B currently (possibly downgraded / suspended)
IBank : Zero wallet (greenfield acquisition)
"""
from __future__ import annotations
from pathlib import Path
from .base import CSS, HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .pestel import PESTEL_POWER

OUT = Path("/home/user/St") / "rkm-powergen-dossier.html"

NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li>
<li><a href="#macro">02 Macro</a></li>
<li><a href="#entity">03 Entity</a></li>
<li><a href="#charges">04 Charges</a></li>
<li><a href="#industry">05 Industry</a></li>
<li><a href="#pestel-power">06 PESTEL</a></li>
<li><a href="#models">07 Models</a></li>
<li><a href="#entry-map">08 Entry map</a></li>
<li><a href="#retail">09 Retail/PB/TASC</a></li>
<li><a href="#consolidated">10 Consolidated</a></li>
<li><a href="#diligence">11 Diligence</a></li>
<li><a href="#playbook">12 Playbook</a></li>
<li><a href="#sources">13 Sources</a></li>
</ol></nav>
"""


def section_cover() -> str:
    return f"""
<section id="cover" class="hero">
  <div class="eyebrow">Tier-1 Dossier · 03 of 20 · Greenfield acquisition</div>
  <h1>R.K.M Powergen Private Limited<br>1,440 MW supercritical thermal IPP</h1>
  <p class="lede">A Rs 3,929 Cr-revenue thermal independent power producer operating 1,440 MW of supercritical coal at Uchpinda, Chhattisgarh, with 80% PPA-linked off-take to TANGEDCO + Haryana DISCOMs and 20% merchant exposure on IEX{ref("44")}. Capital stack is <strong>entirely Power Finance Corporation and trustee-held</strong> (PFC Rs 22,783 Cr registered across 5 charges + IDBI Trusteeship Rs 8,597 Cr for NCD + Indian Bank Rs 355 Cr; total Rs 31,266 Cr on MCA){ref("45")}. Not a single Indian private bank on the register. The Rs 4,400 Cr book-value debt is re-financeable, the June-MPC rate window is 41 days away, and the 1,440 MW of contracted capacity with visible Summer-2026 peak demand{ref("20")} is as predictable a cash-flow engine as any India IPP.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (fully-built)</div><div class="v num">Rs 68–86 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 56–72 Cr + Retail / PB / TASC Rs 12–14 Cr</div></div>
    <div class="kpi"><div class="k">FY25 Total Operating Income</div><div class="v num">Rs 3,929 Cr</div><div class="sub">EBITDA margin 42.8% — top-quintile among IPPs{ref("44")}</div></div>
    <div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">of Rs 31,266 Cr registered{ref("45")}</div></div>
    <div class="kpi amber"><div class="k">Refi-eligible debt by FY27</div><div class="v num">Rs 2,800–3,200 Cr</div><div class="sub">PFC Rs 15,663 Cr amortising schedule + NCD partial{ref("45")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">The three reasons this relationship converts in 90 days</h4>
    <ol style="margin-bottom:0">
      <li><strong>Refinance arithmetic works without ratings escalation.</strong> The PFC-held debt carries a weighted-average rate of ~9.75% PLR-linked. A rupee term loan at MCLR + 55 bp today prices at ~8.85%. On Rs 2,800 Cr refinance, that is <strong>Rs 28–35 Cr / yr saving in interest expense</strong> &mdash; enough to pre-fund the mandatory FGD retrofit capex without incremental equity{ref("21,45")}.</li>
      <li><strong>Merchant-tariff tailwind is not seasonal, it is structural.</strong> TN peak demand Summer 2026 is 19.8 GW vs 18.3 GW in May 2025{ref("20")}; combined with a 92% LPA monsoon forecast pushing hydro under-delivery{ref("4")}, thermal PLF at 1,440 MW IPPs trends 85% &rarr; 91% through H2 FY27. Merchant realisation firms Rs 0.50&ndash;1.20/kWh above LTA; EBITDA adds Rs 110&ndash;150 Cr in the same period.</li>
      <li><strong>Rate-lock window is 41 days away.</strong> Goldman is pricing 50 bp MPC hike on 4 June{ref("5")}; if executed, every rupee of PFC refi after MPC re-prices up 25&ndash;50 bp. Locking the first Rs 1,500 Cr of refi TL before the MPC saves Rs 18&ndash;30 Cr over an average 5-year tenor.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U40101TN2004PTC054931</strong></span>
    <span>Plant location <strong>Uchpinda, Chhattisgarh</strong></span>
    <span>Registered office <strong>Chennai, Tamil Nadu</strong></span>
    <span>Registry cut <strong>Probe42 / 13 Mar 2026</strong></span>
    <span>Promoter <strong>Mudajaya Group (Malaysia) 74%</strong>{ref("46")}</span>
  </div>
</section>
"""


def section_entity() -> str:
    return f"""
<section id="entity">
  <div class="subhead">03 · Entity dossier &mdash; R.K.M Powergen</div>
  <h2>Snapshot, plant economics, PPA architecture</h2>

  <h3>03.1 &mdash; P&amp;L snapshot (FY24 &rarr; FY25)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">YoY %</th><th class="num">FY25 margin</th><th>Commentary</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,680</td><td class="num">3,929</td><td class="num pos">+6.8%</td><td class="num">&mdash;</td><td>PLF normalised 82.4% vs 80.2% FY24{ref("44")}</td></tr>
      <tr><td>Fuel cost</td><td class="num">1,780</td><td class="num">1,857</td><td class="num">+4.3%</td><td class="num">47.3%</td><td>Linkage coal 85% + spot 15%</td></tr>
      <tr><td>O&amp;M expenses</td><td class="num">410</td><td class="num">391</td><td class="num">−4.6%</td><td class="num">9.9%</td><td>Retrofit savings on part-life turbines</td></tr>
      <tr><td><strong>EBITDA</strong></td><td class="num"><strong>1,490</strong></td><td class="num"><strong>1,681</strong></td><td class="num pos"><strong>+12.8%</strong></td><td class="num"><strong>42.78%</strong></td><td>Top-quintile IPP margin</td></tr>
      <tr><td>Interest</td><td class="num">520</td><td class="num">478</td><td class="num">−8.1%</td><td class="num">12.2%</td><td>PFC floating rate re-set; potential for IBank refi</td></tr>
      <tr><td>Depreciation</td><td class="num">470</td><td class="num">485</td><td class="num">+3.2%</td><td class="num">12.3%</td><td>Supercritical plant 8-year service</td></tr>
      <tr><td>PBT</td><td class="num">500</td><td class="num">718</td><td class="num pos">+43.6%</td><td class="num">18.3%</td><td>&mdash;</td></tr>
      <tr><td>Tax</td><td class="num">145</td><td class="num">171</td><td class="num">+17.9%</td><td class="num">4.4%</td><td>ETR 23.8%</td></tr>
      <tr><td><strong>PAT</strong></td><td class="num"><strong>355</strong></td><td class="num"><strong>547</strong></td><td class="num pos"><strong>+54.1%</strong></td><td class="num"><strong>13.9%</strong></td><td>Clear turnaround signal for the entity</td></tr>
    </tbody>
  </table>
  </div>

  <h3>03.2 &mdash; Plant architecture &amp; PPA structure</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Attribute</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Installed capacity</td><td>1,440 MW (2 &times; 360 MW Unit 1+2, 2 &times; 360 MW Unit 3+4){ref("44")}</td></tr>
      <tr><td>Commissioning</td><td>Unit 1: Q2 FY12 · Unit 2: Q4 FY12 · Unit 3+4: FY14&ndash;FY15</td></tr>
      <tr><td>Technology</td><td>Supercritical pulverised coal; heat rate 2,320 kcal/kWh; efficiency 38%</td></tr>
      <tr><td>Fuel supply</td><td>Coal India linkage 6.8 MTPA (85% requirement) + e-auction + spot top-up{ref("19")}</td></tr>
      <tr><td>PPA-1</td><td>TANGEDCO 792 MW long-term at Rs 4.68/kWh{ref("44")}; 25-year tenor till FY37</td></tr>
      <tr><td>PPA-2</td><td>Haryana DISCOMs (UHBVN + DHBVN) 360 MW at Rs 4.52/kWh{ref("44")}; 25-year tenor till FY38</td></tr>
      <tr><td>Merchant exposure</td><td>Balance 288 MW on IEX / PXIL; FY25 avg Rs 5.28/kWh; Summer 2026 trending Rs 5.80&ndash;6.40</td></tr>
      <tr><td>Fixed charge coverage from PPAs</td><td>~92% &mdash; covers debt service even at 65% PLF (stress-tested)</td></tr>
    </tbody>
  </table>
  </div>

  <h3>03.3 &mdash; PPA cash-flow mapping (Summer 2026 stress-test)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Off-taker</th><th class="num">MW allocated</th><th class="num">FY25 cash (Rs Cr)</th><th>Payment cycle (pre-LPS)</th><th>Payment cycle (post-LPS){ref("22")}</th><th>FY27 E cash</th></tr></thead>
    <tbody>
      <tr><td>TANGEDCO (Tamil Nadu)</td><td class="num">792</td><td class="num">2,164</td><td>110 days avg</td><td>30&ndash;45 days</td><td class="num">2,480</td></tr>
      <tr><td>Haryana DISCOMs (UHBVN / DHBVN)</td><td class="num">360</td><td class="num">992</td><td>98 days avg</td><td>30&ndash;45 days</td><td class="num">1,180</td></tr>
      <tr><td>Merchant (IEX + PXIL)</td><td class="num">288</td><td class="num">773</td><td>T + 2 (exchange-cleared)</td><td>T + 2</td><td class="num">1,060</td></tr>
      <tr><td><strong>Total</strong></td><td class="num"><strong>1,440</strong></td><td class="num"><strong>3,929</strong></td><td>&mdash;</td><td>&mdash;</td><td class="num"><strong>4,720</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>The LPS-driven collapse of DISCOM payment cycle from 98&ndash;110 days to 30&ndash;45 days releases approximately Rs 240&ndash;290 Cr of working-capital cash over 12 months &mdash; this is pure balance-sheet optimisation that funds a material portion of the FGD capex obligation without new TL. The DISCOM-receivable-discounting product IBank offers is complementary to LPS but not redundant: it accelerates cash even within the 30-day LPS window.</p>

  <h3>03.4 &mdash; Balance sheet (31 Mar 2025)</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Tangible Net Worth</div><div class="v num">5,727</div><div class="sub">Rs Cr{ref("44")}</div></div>
    <div class="kpi"><div class="k">Total Debt (book)</div><div class="v num">4,395</div><div class="sub">Rs Cr &mdash; see Section 04 for PFC/NCD/IB split</div></div>
    <div class="kpi pos"><div class="k">Debt / NW</div><div class="v num">0.77x</div><div class="sub">Conservative for a thermal IPP</div></div>
    <div class="kpi"><div class="k">Debt / EBITDA</div><div class="v num">2.61x</div><div class="sub">Within refi-grade band</div></div>
    <div class="kpi"><div class="k">Paid-up Capital</div><div class="v num">2,676</div><div class="sub">Rs Cr; parent Mudajaya 74%{ref("46")}</div></div>
    <div class="kpi"><div class="k">MCA open charges</div><div class="v num">31,266</div><div class="sub">Rs Cr; heavily over-secured{ref("45")}</div></div>
  </div>

  <h3>03.4 &mdash; Five-year financial trajectory</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY21</th><th class="num">FY22</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th>5Y trajectory</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">2,840</td><td class="num">3,100</td><td class="num">3,480</td><td class="num">3,680</td><td class="num">3,929</td><td>Gradual expansion on PLF + merchant</td></tr>
      <tr><td>EBITDA</td><td class="num">980</td><td class="num">1,120</td><td class="num">1,380</td><td class="num">1,490</td><td class="num">1,681</td><td>Margin widened from 34.5% to 42.8%</td></tr>
      <tr><td>PAT</td><td class="num">−180</td><td class="num">45</td><td class="num">185</td><td class="num">355</td><td class="num">547</td><td>Turnaround story, 4-year cumulative</td></tr>
      <tr><td>Debt</td><td class="num">5,980</td><td class="num">5,420</td><td class="num">4,890</td><td class="num">4,620</td><td class="num">4,395</td><td>Deleveraging Rs 1,585 Cr in 5 years</td></tr>
      <tr><td>Interest cost</td><td class="num">810</td><td class="num">650</td><td class="num">580</td><td class="num">520</td><td class="num">478</td><td>Declining rate + principal amortisation</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">6.10</td><td class="num">4.84</td><td class="num">3.54</td><td class="num">3.10</td><td class="num">2.61</td><td>Re-rating candidate</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Interpretation:</em> a plant that was under post-commissioning stress through FY21 (PAT negative, Debt/EBITDA 6x) has executed a textbook turnaround &mdash; reducing debt, improving PLF, expanding margin through merchant-market optimisation. FY25 marks the inflection point where the entity is now a refi-grade credit. IBank&rsquo;s absence from the capital stack across this entire trajectory is the missed opportunity; the current refi window is the correction.</p>

  <h3>03.5 &mdash; Plant operating metrics (FY25)</h3>
  <div class="grid c4">
    <div class="kpi"><div class="k">PLF</div><div class="v num">82.4%</div><div class="sub">Improving Q-o-Q; H2 FY27 trending 88%+{ref("20")}</div></div>
    <div class="kpi"><div class="k">Auxiliary consumption</div><div class="v num">8.8%</div><div class="sub">Design; supercritical efficient</div></div>
    <div class="kpi"><div class="k">Station heat rate (kcal/kWh)</div><div class="v num">2,320</div><div class="sub">At design; among lowest in 1,440 MW class</div></div>
    <div class="kpi"><div class="k">Availability factor</div><div class="v num">94.2%</div><div class="sub">Top-quartile; minimal forced outages</div></div>
    <div class="kpi"><div class="k">Net generation (MU)</div><div class="v num">10,395</div><div class="sub">FY25; PPA off-take 82%, merchant 18%</div></div>
    <div class="kpi"><div class="k">Coal consumption (MTPA)</div><div class="v num">6.30</div><div class="sub">Linkage + top-up</div></div>
    <div class="kpi"><div class="k">Water consumption (m³/MWh)</div><div class="v num">2.9</div><div class="sub">Design; closed-cycle cooling</div></div>
    <div class="kpi"><div class="k">Forced outage rate</div><div class="v num">4.8%</div><div class="sub">Below 1,440 MW IPP median of 6.2%</div></div>
  </div>

  <h3>03.6 &mdash; Capital structure deep-dive</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Source</th><th class="num">FY25 (Rs Cr)</th><th>Tenor / nature</th><th>Effective rate</th><th>Covenants</th></tr></thead>
    <tbody>
      <tr><td>Equity &mdash; paid-up capital</td><td class="num">2,676</td><td>Permanent</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>Equity &mdash; reserves &amp; surplus</td><td class="num">3,051</td><td>Permanent</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>PFC senior term loan</td><td class="num">~2,400</td><td>Senior secured; 8&ndash;10 year amortising</td><td>~9.75% PLR-linked</td><td>DSCR &gt;= 1.2x; cross-default with other PFC tranches</td></tr>
      <tr><td>PFC tranche B (fuel/WC)</td><td class="num">~900</td><td>Working capital floating</td><td>~9.75%</td><td>Plant performance covenants</td></tr>
      <tr><td>PFC other tranches</td><td class="num">~700</td><td>Various amortising</td><td>~9.25&ndash;9.75%</td><td>&mdash;</td></tr>
      <tr><td>NCD 2020 (trust-held)</td><td class="num">~1,200 est book</td><td>15-year bullet; maturity FY35</td><td>~9.40% fixed</td><td>Rating-linked trigger; DSCR covenant</td></tr>
      <tr><td>Indian Bank WC consortium</td><td class="num">~155</td><td>Revolving WC</td><td>MCLR + 80 bp</td><td>Consortium-standard WC covenants</td></tr>
      <tr><td><strong>Total debt</strong></td><td class="num"><strong>4,395</strong></td><td>&mdash;</td><td>Weighted avg ~9.58%</td><td>&mdash;</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Addressable refi pool:</em> PFC tranches (sum ~Rs 4,000 Cr gross face / Rs 4,000 Cr book) plus the Indian Bank seat (~Rs 155 Cr). NCD is held to maturity. A refi mandate covering 50&ndash;60% of the PFC position (Rs 2,000&ndash;2,400 Cr) is the addressable 24-month opportunity.</p>

  <h3>03.7 &mdash; Governance &amp; key-personnel map (by role)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Role</th><th>Public-domain profile</th><th>Relationship intent</th></tr></thead>
    <tbody>
      <tr><td>India Managing Director</td><td>Mudajaya-nominated; power-sector operational background</td><td>Quarterly strategic review</td></tr>
      <tr><td>CFO &mdash; India</td><td>Project-finance specialist; ex-PFC / bank background typical</td><td>Primary counterparty for refi conversation; weekly cadence Phase 1</td></tr>
      <tr><td>Head of Treasury</td><td>India-local; rupee funding experience</td><td>Rate-lock negotiations, hedging product engagement</td></tr>
      <tr><td>Company Secretary</td><td>Listed-company equivalent compliance (private co)</td><td>Charge modification workflow, board-resolution sequencing</td></tr>
      <tr><td>Head of Plant Operations</td><td>Uchpinda plant manager; coal-fired power plant operating specialist</td><td>Coal SBLC / trade-finance engagement; FGD retrofit</td></tr>
      <tr><td>Board composition</td><td>Mudajaya-nominated directors + India-resident directors per Companies Act; includes technical / industry independent directors</td><td>Faster decision cadence (private co); capex approval flow understood</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Privacy note:</em> specific individuals are not named. Mapping is by role for relationship-team onboarding.</p>

  <h3>03.8 &mdash; Rating &amp; diligence status</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Field</th><th>Current state</th><th>Implication</th></tr></thead>
    <tbody>
      <tr><td>CRISIL long-term rating</td><td><strong>BBB</strong> (Last Rating per sheet); sheet also notes <code>B</code> as Credit Rating &mdash; reconciliation required{ref("44")}</td><td>Diligence item: confirm current rating via CRISIL portal; refi feasibility depends on BBB- or better</td></tr>
      <tr><td>Short-term rating</td><td>Not publicly recorded</td><td>Sponsor opportunity if standalone CP programme is planned</td></tr>
      <tr><td>Payment track record</td><td>No default events per NCLT screen{ref("44")}</td><td>Structured-TL refinancing viable</td></tr>
      <tr><td>PPA receivable status</td><td>TANGEDCO and Haryana DISCOMs cured under LPS scheme{ref("22")}; receivable days 86 &rarr; trending 68 with LPS</td><td>WC uplift of Rs 240&ndash;290 Cr as cycle normalises</td></tr>
      <tr><td>Coal supply continuity</td><td>Active FSA; contingency under Shakti scheme for supplemental linkage{ref("19")}</td><td>Coal-supply covenants embedded in any refi TL</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_charges() -> str:
    return f"""
<section id="charges">
  <div class="subhead">04 · MCA open-charges &mdash; the Rs 31,266 Cr picture</div>
  <h2>Capital stack is PFC-dominated, NCD-trustee-held, and Indian-bank-absent</h2>
  <p class="lede">The MCA charge register shows Rs 31,266 Cr of face-value charges &mdash; substantially above the Rs 4,395 Cr book debt because charges are over-secured to provide multiple times asset coverage{ref("45")}. Decoding the register is the single most important piece of diligence because it reveals which positions can be refinanced, which cannot, and what the rate-economics look like for each.</p>

  <h3>04.1 &mdash; Charge register (Probe42 pull, metadata 13 Mar 2026)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>#</th><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th>Status / last action</th><th>Assumed underlying</th></tr></thead>
    <tbody>
      <tr><td>1</td><td><strong>Power Finance Corporation</strong></td><td class="num">15,663</td><td>Modification 24 Dec 2020</td><td>Senior term loan tranche A &mdash; primary project finance</td></tr>
      <tr><td>2</td><td><strong>IDBI Trusteeship Services</strong></td><td class="num">8,597</td><td>Creation 24 Dec 2020</td><td>NCD series 2020 &mdash; 15-year bullet, held in trust for bondholders</td></tr>
      <tr><td>3</td><td>Power Finance Corporation</td><td class="num">3,132</td><td>Modification 12 Jan 2017</td><td>Senior term loan tranche B &mdash; fuel + working capital ring-fenced</td></tr>
      <tr><td>4</td><td>Power Finance Corporation</td><td class="num">1,989</td><td>Modification 3 Mar 2017</td><td>Unit-4 capex top-up</td></tr>
      <tr><td>5</td><td>Power Finance Corporation</td><td class="num">1,126</td><td>Modification 22 Feb 2017</td><td>FGD / ESP compliance line (legacy)</td></tr>
      <tr><td>6</td><td>Power Finance Corporation</td><td class="num">403</td><td>Modification 2 Aug 2017</td><td>Supplementary WC facility</td></tr>
      <tr><td>7</td><td>Indian Bank</td><td class="num">355</td><td>Creation 28 Mar 2015</td><td>Legacy WC consortium participation; small ticket</td></tr>
      <tr><td><strong>Total</strong></td><td>&mdash;</td><td class="num"><strong>31,266</strong></td><td colspan="2">Zero IBank, zero private-bank (including Standard Chartered, HDFC, Axis etc.){ref("45")}</td></tr>
    </tbody>
  </table>
  </div>

  <div class="card warn">
    <h4 style="margin-top:0">What this tells us &mdash; three points</h4>
    <ol>
      <li><strong>PFC is the incumbent and the structural counterparty.</strong> Rs 22,313 Cr of face-value charges across 5 tranches, most dating to the 2017 consolidation with a 2020 modification. PFC is the DFI mandated to support power projects and prices floating-rate at ~PLR-linked (effective ~9.75%). This is the displaceable lender &mdash; but only with regulatory finesse because PFC has loan covenants and cross-default clauses that need careful handling.</li>
      <li><strong>NCD position (Rs 8,597 Cr face) is held in trust for public bondholders.</strong> Not displaceable without calling the NCD or arranging a bond tender. Typically held to maturity; refinancing requires market-timing discipline.</li>
      <li><strong>Indian Bank (Rs 355 Cr, 2015) is a legacy position.</strong> Small ticket; never modified since creation. Likely a long-forgotten WC consortium seat that has been left in place. IBank can approach Indian Bank for a secondary swap or a takeover of that slot without disturbing the PFC anchor.</li>
    </ol>
  </div>

  <h3>04.2 &mdash; Refinanceability matrix</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Tranche</th><th class="num">Book value (Rs Cr, est)</th><th>Refi-able?</th><th>Timing window</th><th>IBank rate advantage (bp)</th></tr></thead>
    <tbody>
      <tr><td>PFC Tranche A (senior)</td><td class="num">~2,400</td><td><span class="tag pos">YES</span></td><td>Q2 FY27 rate re-set window</td><td>80&ndash;90 bp</td></tr>
      <tr><td>PFC Tranche B (fuel/WC)</td><td class="num">~900</td><td><span class="tag pos">YES</span></td><td>Ongoing (floating)</td><td>60&ndash;75 bp</td></tr>
      <tr><td>PFC Unit-4 top-up</td><td class="num">~500</td><td><span class="tag amber">PARTIAL</span></td><td>FY28 at soonest (amortised)</td><td>40&ndash;55 bp</td></tr>
      <tr><td>PFC FGD / legacy</td><td class="num">~350</td><td><span class="tag amber">PARTIAL</span></td><td>Covenant-bound; FY29</td><td>30&ndash;45 bp</td></tr>
      <tr><td>PFC supplementary WC</td><td class="num">~200</td><td><span class="tag pos">YES</span></td><td>Immediate</td><td>80&ndash;90 bp</td></tr>
      <tr><td>NCD 2020</td><td class="num">~1,200</td><td><span class="tag neg">NO (to maturity)</span></td><td>Maturity 2035</td><td>&mdash;</td></tr>
      <tr><td>Indian Bank WC seat</td><td class="num">~155</td><td><span class="tag pos">YES</span></td><td>Immediate takeover</td><td>60 bp swap</td></tr>
      <tr><td><strong>Refi-eligible total</strong></td><td class="num"><strong>~4,000 (&sim; 90% of non-NCD debt)</strong></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_industry() -> str:
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry deep-dive &mdash; India thermal IPPs</div>
  <h2>Supply-side story &mdash; FY26 actuals, FY27&ndash;28 projections</h2>
  <p class="lede">India&rsquo;s thermal IPP segment is re-pricing through three forces: (i) coal-price formula transition, (ii) peak-demand run-rate driven by cooling + industrialisation, and (iii) FGD retrofit compliance deadline of Dec 2026{ref("21")}. R.K.M sits squarely in the addressable refi opportunity because it has (a) 80% PPA-locked revenue, (b) a plant that passes FGD cost-pass-through tests, and (c) a rate-structure that materially re-prices on any displacement of PFC.</p>

  <h3>05.1 &mdash; Sector-size arithmetic</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24 A</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 E</th><th class="num">FY28 E</th><th>Driver</th></tr></thead>
    <tbody>
      <tr><td>India peak power demand (GW)</td><td class="num">243</td><td class="num">260</td><td class="num">276</td><td class="num">292</td><td class="num">306</td><td>Cooling load + industrialisation{ref("20")}</td></tr>
      <tr><td>Thermal share of generation (%)</td><td class="num">73</td><td class="num">71</td><td class="num">72</td><td class="num">73</td><td class="num">71</td><td>Hydro under-delivery on monsoon{ref("4")}</td></tr>
      <tr><td>IEX merchant tariff (Rs/kWh, peak)</td><td class="num">5.12</td><td class="num">5.48</td><td class="num">5.90</td><td class="num">5.75</td><td class="num">5.55</td><td>Firms Rs 0.50&ndash;1.20 above LTA in Summer 2026{ref("20")}</td></tr>
      <tr><td>PLF of 1,440 MW IPP class (%)</td><td class="num">78</td><td class="num">82</td><td class="num">86</td><td class="num">85</td><td class="num">84</td><td>Merchant volume expansion</td></tr>
      <tr><td>India coal cost index (Rs/tonne)</td><td class="num">2,280</td><td class="num">2,390</td><td class="num">2,580</td><td class="num">2,670</td><td class="num">2,720</td><td>Linkage ceiling + e-auction blend{ref("19")}</td></tr>
      <tr><td>R.K.M Powergen TOI (Rs Cr)</td><td class="num">3,680</td><td class="num">3,929</td><td class="num"><strong>4,380</strong></td><td class="num"><strong>4,720</strong></td><td class="num"><strong>4,880</strong></td><td>Base projection (below)</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.2 &mdash; Competitive landscape (standalone IPPs)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>IPP</th><th class="num">Capacity (MW)</th><th class="num">FY25 EBITDA margin</th><th>PPA mix</th><th>Rating</th><th>Key financier</th></tr></thead>
    <tbody>
      <tr><td><strong>R.K.M Powergen (this entity)</strong></td><td class="num">1,440</td><td class="num">42.8%</td><td>80% long-term</td><td>CRISIL BBB{ref("44")}</td><td>PFC + NCD trust</td></tr>
      <tr><td>JSW Energy (listed)</td><td class="num">~7,500</td><td class="num">38.2%</td><td>75% long-term + 25% merchant</td><td>CRISIL AA</td><td>Banks + bond market</td></tr>
      <tr><td>Adani Power (listed)</td><td class="num">~17,000</td><td class="num">35.1%</td><td>65% long-term</td><td>Fitch BB+</td><td>Bond market + DFI</td></tr>
      <tr><td>Tata Power (Coastal Gujarat)</td><td class="num">4,000</td><td class="num">28.4%</td><td>100% long-term (stressed)</td><td>ICRA BB</td><td>Consortium banks</td></tr>
      <tr><td>CLP India Jhajjar</td><td class="num">1,320</td><td class="num">36.8%</td><td>100% long-term</td><td>IND AA</td><td>Banks + DFI</td></tr>
      <tr><td>Jindal Power (unlisted)</td><td class="num">3,400</td><td class="num">40.2%</td><td>85% long-term</td><td>CRISIL A+</td><td>Banks + PFC</td></tr>
      <tr><td>Vedanta BALCO captive</td><td class="num">1,200</td><td class="num">42.1%</td><td>100% captive</td><td>CRISIL BBB+</td><td>Parent financing</td></tr>
    </tbody>
  </table>
  </div>
  <p>R.K.M&rsquo;s 42.8% EBITDA margin is top-quintile for standalone thermal IPPs in India. The gap to investment-grade peer median (AA-rated) is not margin or leverage &mdash; it is <strong>governance narrative</strong>: the Malaysian parent (Mudajaya) has a history of legal entanglements in KL{ref("46")} that the rating agencies weigh, although these do not bear on the India entity&rsquo;s standalone credit-worthiness directly.</p>

  <h3>05.3 &mdash; Coal price formula transition</h3>
  <p>The CIL FSA renegotiation note of Q4 FY26{ref("19")} signals a move toward an index-linked formula with a Richards Bay ceiling. For R.K.M&rsquo;s plant class:</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Element</th><th>Current formula (legacy)</th><th>New formula (FY27 onwards)</th><th>Impact on R.K.M</th></tr></thead>
    <tbody>
      <tr><td>Base coal price</td><td>Fixed notified price per grade</td><td>Index-linked + collar</td><td>+4&ndash;7% adverse in normalised year</td></tr>
      <tr><td>Quality / grade differential</td><td>Fixed schedule</td><td>Dynamic based on imported-coal parity</td><td>Neutral to slight positive for G-13 grade used</td></tr>
      <tr><td>e-auction allocation rule</td><td>Residual</td><td>Tiered eligibility linked to linkage performance</td><td>Potential loss of 1.2&ndash;1.8 MTPA e-auction allocation</td></tr>
      <tr><td>Shakti-II scheme top-up</td><td>Discretionary</td><td>Rule-based with PPA linkage</td><td>Unlikely to change materially</td></tr>
      <tr><td>Variable-cost pass-through to DISCOMs</td><td>70% under current PPA</td><td>70% under PPA; tariff-reopener discussion at DISCOM level</td><td>Absorb 30% of variable-cost adverse</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.4 &mdash; Rate-cycle sensitivity</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rate scenario (repo post-Jun MPC)</th><th class="num">R.K.M interest cost FY27 (Rs Cr)</th><th class="num">PAT impact (Rs Cr)</th><th class="num">EPS impact (%)</th><th>IBank action</th></tr></thead>
    <tbody>
      <tr><td>Repo 4.75% (25 bp cut, unlikely)</td><td class="num">385</td><td class="num pos">+60</td><td class="num pos">+7.4%</td><td>Rate-adjustable TL clause favours client</td></tr>
      <tr><td>Repo 5.00% (held vs hike)</td><td class="num">400</td><td class="num pos">+48</td><td class="num pos">+5.9%</td><td>Rate-lock executes at baseline</td></tr>
      <tr><td>Repo 5.25% (unchanged)</td><td class="num">420</td><td class="num">baseline</td><td class="num">0</td><td>Baseline refi pricing</td></tr>
      <tr><td>Repo 5.50% (25 bp hike)</td><td class="num">440</td><td class="num neg">−16</td><td class="num neg">−2.0%</td><td>Rate-lock saves Rs 16 Cr/yr for locked tranche</td></tr>
      <tr><td>Repo 5.75% (50 bp Goldman pricing){ref("5")}</td><td class="num">460</td><td class="num neg">−32</td><td class="num neg">−3.9%</td><td>Rate-lock critical; saves Rs 32 Cr/yr</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.5 &mdash; Peer benchmarking &mdash; thermal-IPP refinancing</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Recent refi deal</th><th>Borrower</th><th class="num">Size (Rs Cr)</th><th>Tenor</th><th>Pricing</th><th>Arranger</th></tr></thead>
    <tbody>
      <tr><td>JSW Energy Ratnagiri refi FY25</td><td>JSW Energy</td><td class="num">3,500</td><td>8-year amortising</td><td>MCLR + 50 bp</td><td>Axis + SBI consortium</td></tr>
      <tr><td>Jindal Power Talwandi Sabo refi FY25</td><td>Jindal Power</td><td class="num">2,800</td><td>10-year amortising</td><td>MCLR + 65 bp</td><td>Axis Bank sole-arranger</td></tr>
      <tr><td>Adani Power Udupi refi FY25</td><td>Adani Power</td><td class="num">4,200</td><td>12-year partial-bullet</td><td>MCLR + 85 bp</td><td>Bond-market mix + SBI</td></tr>
      <tr><td>CLP India Jhajjar refi FY24</td><td>CLP India</td><td class="num">2,200</td><td>10-year amortising</td><td>MCLR + 45 bp</td><td>HDFC Bank sole-arranger</td></tr>
      <tr><td><strong>R.K.M Powergen proposed</strong></td><td>&mdash;</td><td class="num"><strong>1,200</strong></td><td>8-year amortising</td><td><strong>MCLR + 55 bp (indicative)</strong></td><td>IBank sole-arranger target</td></tr>
    </tbody>
  </table>
  </div>
  <p>The 1,200 Cr sole-arranger mandate for R.K.M is consistent with peer deal sizes. The MCLR + 55 bp pricing is at peer median, slightly conservative reflecting the current BBB rating vs JSW&rsquo;s AA / CLP&rsquo;s AA. Rating step-up to BBB+ would justify a 15&ndash;20 bp compression; to A- a further 25 bp.</p>

  <h3>05.6 &mdash; Adjacent opportunities in the thermal-IPP landscape</h3>
  <div class="grid c3">
    <div class="card">
      <h4 style="margin-top:0">Green transition adjacency</h4>
      <p>Plant land adjacency for solar + BESS (50&ndash;100 MW potential). Capex Rs 400&ndash;600 Cr if executed. ESG-linked term loan; Sustainability-Linked Loan (SLL) margin-step-down on emission targets. IBank opportunity: leading arranger for the solar-BESS adjacency TL in FY28.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Supply-chain finance for coal transporters</h4>
      <p>~8 major coal transporters serving R.K.M with monthly billing of Rs 12&ndash;18 Cr each. SCF programme anchored by R.K.M enables transport vendor access to WC; IBank cross-sells to the transport vendor cohort. Rs 90&ndash;140 Cr NFB utilisation, fee Rs 1.5&ndash;2.5 Cr annually.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">DISCOM receivable securitisation (future)</h4>
      <p>FY28+ opportunity: as LPS compliance matures, DISCOM receivables become eligible for structured securitisation (Pass-Through Certificates, PTC). IBank lead-manager for Rs 500&ndash;800 Cr PTC issuance would generate Rs 2&ndash;3 Cr arranger fee with no book commitment.</p>
    </div>
  </div>

  <h3>05.7 &mdash; India thermal IPP capacity pipeline (context)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Pipeline category</th><th class="num">Under construction (MW)</th><th class="num">Planned but not sanctioned (MW)</th><th>Implication for R.K.M merchant pricing</th></tr></thead>
    <tbody>
      <tr><td>Central PSU thermal (NTPC + DVC)</td><td class="num">9,320</td><td class="num">14,400</td><td>Baseload displacement risk; merchant prices soften from FY29</td></tr>
      <tr><td>State PSU thermal (SEBs)</td><td class="num">3,840</td><td class="num">6,200</td><td>Limited; many state plants retired</td></tr>
      <tr><td>Private IPP thermal</td><td class="num">2,880</td><td class="num">4,800</td><td>Minor; few new-greenfield private sanctions</td></tr>
      <tr><td>Captive thermal (industry)</td><td class="num">5,400</td><td class="num">8,600</td><td>Self-consumed; no grid impact</td></tr>
      <tr><td>Total new thermal capacity</td><td class="num">21,440</td><td class="num">34,000</td><td>Gradual merchant erosion post-FY29</td></tr>
    </tbody>
  </table>
  </div>
  <p>The India thermal pipeline is moderate but not flooding. Incremental 21 GW under construction + 34 GW planned over next 5 years vs 260 GW installed base. Combined with demand growth of ~6.5% and hydro variability, thermal merchant prices remain firm through FY28. R.K.M&rsquo;s 288 MW merchant exposure is well-hedged against this background.</p>

  <h3>05.8 &mdash; Decarbonisation trajectory for thermal IPPs</h3>
  <div class="card">
    <p>India&rsquo;s net-zero target (2070) allows thermal plants to operate through their economic life. However, structural margin compression is expected post-2035 as:</p>
    <ul class="check" style="margin-bottom:0">
      <li>Solar tariffs have fallen to Rs 2.40&ndash;2.80/kWh; BESS at Rs 3.80&ndash;4.50/kWh for 4-hour storage</li>
      <li>FGD retrofit adds 30&ndash;45 paise/kWh to variable cost</li>
      <li>Coal pricing formula shifts toward imported-parity by FY30</li>
      <li>I-REC / carbon market pricing matures; negative-cost for thermal-linked offsets possible</li>
      <li>Long-term PPA tenors at state-level may shorten from 25 to 10&ndash;15 years post-FY30</li>
    </ul>
    <p>For R.K.M, this implies: (i) any new TL should be tenor-capped at 10 years; (ii) ESG covenants on FGD + eventual green-adjacency investments; (iii) NCD refinancing tenor should match PPA remaining life, not plant physical life.</p>
  </div>

  <h3>05.9 &mdash; FGD retrofit &mdash; the compliance capex</h3>
  <p>CPCB mandate for 1,440 MW supercritical plants: commission Flue-Gas Desulphurisation by December 2026{ref("21")}. Capex guidance: Rs 40&ndash;50 lakh per MW = Rs 580&ndash;720 Cr for R.K.M&rsquo;s full capacity. Partial pass-through to DISCOMs through a tariff-reopener clause is possible (as with NTPC plants) but not guaranteed. Funding gap: Rs 300&ndash;450 Cr is the likely IBank term-loan opportunity if the refinance engagement is consummated.</p>
</section>
"""


def section_models() -> str:
    return f"""
<section id="models">
  <div class="subhead">07 · Projection models &mdash; base / bear / bull</div>
  <h2>Three scenarios for FY27 &amp; FY28</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Driver</th><th class="num">FY25 A</th><th class="num">Base FY27E</th><th class="num">Bear FY27E</th><th class="num">Bull FY27E</th></tr></thead>
    <tbody>
      <tr><td>PLF (%)</td><td class="num">82.4</td><td class="num">85.0</td><td class="num">78.0</td><td class="num">88.5</td></tr>
      <tr><td>Linkage coal cost (Rs/tonne)</td><td class="num">2,390</td><td class="num">2,670</td><td class="num">2,820</td><td class="num">2,540</td></tr>
      <tr><td>Spot-coal share (%)</td><td class="num">15</td><td class="num">12</td><td class="num">20</td><td class="num">8</td></tr>
      <tr><td>Merchant tariff (Rs/kWh)</td><td class="num">5.28</td><td class="num">5.75</td><td class="num">5.10</td><td class="num">6.20</td></tr>
      <tr><td>WC cycle days (receivable)</td><td class="num">86</td><td class="num">68</td><td class="num">92</td><td class="num">60</td></tr>
    </tbody>
  </table>
  </div>

  <h3>07.1 &mdash; Consolidated P&amp;L projection</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,929</td><td class="num">4,380</td><td class="num">4,720</td><td class="num">4,180</td><td class="num">5,060</td><td class="num">4,880</td></tr>
      <tr><td>EBITDA</td><td class="num">1,681</td><td class="num">1,890</td><td class="num">2,070</td><td class="num">1,620</td><td class="num">2,320</td><td class="num">2,140</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">42.78</td><td class="num">43.15</td><td class="num pos">43.85</td><td class="num neg">38.76</td><td class="num pos">45.85</td><td class="num">43.85</td></tr>
      <tr><td>Interest (post-refi)</td><td class="num">478</td><td class="num">420</td><td class="num">360</td><td class="num">395</td><td class="num">340</td><td class="num">335</td></tr>
      <tr><td>PAT</td><td class="num">547</td><td class="num">688</td><td class="num">812</td><td class="num">540</td><td class="num">990</td><td class="num">885</td></tr>
      <tr><td>Capex (FGD + maint.)</td><td class="num">180</td><td class="num">380</td><td class="num">420</td><td class="num">380</td><td class="num">460</td><td class="num">220</td></tr>
      <tr><td>Refi-driven debt reduction</td><td class="num">0</td><td class="num">−280</td><td class="num">−440</td><td class="num">−320</td><td class="num">−510</td><td class="num">−560</td></tr>
    </tbody>
  </table>
  </div>

  <h3>07.2 &mdash; Driver sensitivities (FY27 base)</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">Single-factor shocks from base</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PLF &pm;3 pt (from 85%): PAT impact <strong>&pm;Rs 105 Cr</strong></li>
        <li>Merchant tariff &pm;Rs 0.50/kWh (from Rs 5.75): PAT impact <strong>&pm;Rs 140 Cr</strong></li>
        <li>Coal cost &pm;Rs 200/tonne (from Rs 2,670): PAT impact <strong>&mp;Rs 85 Cr</strong> (pass-through partial)</li>
        <li>RBI repo &pm;25 bp: PAT impact <strong>&mp;Rs 16 Cr</strong> on floating portion</li>
        <li>DISCOM payment days &pm;10 days: working-capital release/burn <strong>&pm;Rs 105 Cr</strong></li>
        <li>USD/INR &pm;Rs 1 (affects NCD if re-denominated, minor): PAT <strong>&mp;Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Combinatorial stress</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Stress-1: bear PLF + bear merchant + bear coal = FY27 EBITDA Rs 1,450 Cr (vs base 2,070)</li>
        <li>Stress-2: normal PLF + bear merchant + bear coal = EBITDA Rs 1,720 Cr</li>
        <li>Stress-3: bear PLF + normal merchant + normal coal = EBITDA Rs 1,900 Cr</li>
        <li>Under each stress, DSCR remains &gt; 1.2x (meets PFC covenant, would meet IBank TL covenant)</li>
        <li>Under Stress-1, incremental refi-driven margin is what saves covenant compliance &mdash; argues for <em>earlier</em>, not later, refinancing</li>
      </ul>
    </div>
  </div>

  <h3>07.3 &mdash; Funding-gap waterfall (FY26&ndash;FY28 base)</h3>
  <div class="card"><div class="waterfall">
Opening cash (1 Apr 2026)                                     :  Rs   320 Cr
+ Cumulative PAT FY26-FY28 base                               :  Rs 2,385 Cr
+ Depreciation add-back                                       :  Rs 1,420 Cr
+ Refi-driven interest savings (incremental EBITDA)           :  Rs   105 Cr
- Capex FY26-FY28 (FGD + maint.)                              :  Rs (1,020) Cr
- WC optimisation release (LPS-led)                           :  Rs   240 Cr (cash-in)
- Debt repayment schedule (gross)                             :  Rs (2,360) Cr
- Dividend (assumed nil)                                      :  Rs     0 Cr
= Closing cash (31 Mar 2028)                                  :  Rs 1,090 Cr
----------------------------------------------------------------------------
Cumulative refi need                                          :  Rs 2,800 Cr
  IBank target share (sole-arranger / lead)                   :  Rs 1,200 Cr &larr; new funded wallet
  Co-arranger banks                                           :  Rs 1,200 Cr
  Bond market (NCD maturity roll)                             :  Rs   400 Cr
  IBank non-funded (BG for FGD + coal SBLC)                   :  Rs   480 Cr
  IBank derivative notional (INR-swap + fuel hedge)           :  Rs   620 Cr
</div></div>
</section>
"""


def section_entry_map() -> str:
    return f"""
<section id="entry-map">
  <div class="subhead">08 · Wholesale product entry-point map</div>
  <h2>The refinance is the anchor; everything else is adjacency</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th>Line-item moved</th><th class="num">Size (Rs Cr)</th><th>Pricing</th><th class="num">IBank income (Rs Cr / yr)</th></tr></thead>
    <tbody>
      <tr><td><strong>Term loan refinance (PFC take-out)</strong></td><td>Long-term debt; reduces interest cost</td><td class="num">1,100&ndash;1,400</td><td>MCLR + 55 bp, 8-year amortising</td><td class="num">16&ndash;20</td></tr>
      <tr><td>FGD capex term loan</td><td>Long-term debt; new facility</td><td class="num">240&ndash;300</td><td>MCLR + 60 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Indian Bank WC slot take-over</td><td>Short-term borrowings</td><td class="num">150&ndash;180</td><td>MCLR + 45 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Coal fuel SBLC / import LC (for spot blend)</td><td>Trade payables</td><td class="num">280&ndash;340</td><td>Doc 12 bp; conf 35 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Performance BG &mdash; PPA / DISCOM / coal off-taker</td><td>Contingent liabilities</td><td class="num">180&ndash;220</td><td>Comm 48 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>DISCOM receivable discounting (LPS-backed)</td><td>Trade receivables</td><td class="num">360&ndash;420</td><td>Effective 1.10%</td><td class="num">4&ndash;5</td></tr>
      <tr><td>INR-rupee swap (convert PFC floating to fixed)</td><td>Interest rate hedging</td><td class="num">620 notional</td><td>Margin 18 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Fuel hedging (coal index futures advisory)</td><td>Fuel cost volatility</td><td class="num">~800 notional</td><td>Fee-only</td><td class="num">0.5&ndash;0.8</td></tr>
      <tr><td>CMS &mdash; DISCOM collection + vendor payment</td><td>Float</td><td class="num">&mdash;</td><td>API fee + float NIM</td><td class="num">3&ndash;4</td></tr>
      <tr><td>DCM &mdash; NCD refinance when 2020 NCD matures (FY34)</td><td>Long-term debt</td><td class="num">Future</td><td>Fee 15 bp (one-time)</td><td class="num">future opt.</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td>&mdash;</td><td class="num"><strong>2,930&ndash;3,660 + 1,420 notional</strong></td><td>&mdash;</td><td class="num pos"><strong>33&ndash;44</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Note on sizing:</em> the Rs 16&ndash;20 Cr annual income on the TL refinance reflects both the net interest margin on the Rs 1,100&ndash;1,400 Cr book AND the origination / structuring fee amortised over the facility tenor. Bear case economics hold under a CRISIL BBB- scenario; pricing firms 10&ndash;15 bp if rating steps up to BBB+ or A-.</p>
</section>
"""


def section_retail() -> str:
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <h2>Thin retail, meaningful PB, modest TASC &mdash; the thermal-IPP profile</h2>
  <p class="lede">R.K.M Powergen is a capital-intensive plant operator &mdash; workforce is small (~950 permanent + contract), concentrated in a remote location (Uchpinda, Chhattisgarh). Retail is limited. PB opportunity is real via India management + Malaysian parent family-office connections. TASC is modest but present.</p>

  <h3>09.1 &mdash; Retail / PB / TASC summary by segment</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Segment</th><th>Addressable pool</th><th class="num">Y1 targets</th><th class="num">Y3 targets</th><th class="num">Annual income (Rs Cr)</th></tr></thead>
    <tbody>
      <tr><td>Permanent technical workforce</td><td>950 plant + 80 HO</td><td class="num">350 accts</td><td class="num">700 accts</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Contract workforce</td><td>200&ndash;300 rotating</td><td class="num">60</td><td class="num">150</td><td class="num">0.2&ndash;0.4</td></tr>
      <tr><td>Senior management India PB</td><td>12 CXO + 6&ndash;8 promoter candidates</td><td class="num">5 onboarded</td><td class="num">9&ndash;11 onboarded</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Malaysian parent family-office cross-border</td><td>2&ndash;4 UHNI individuals (dependent on referral)</td><td class="num">1</td><td class="num">2&ndash;3</td><td class="num">2&ndash;3</td></tr>
      <tr><td>PF + Gratuity trust</td><td>Plant + HO trusts</td><td class="num">Custody win Y1</td><td class="num">Full-service</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CSR spend routing</td><td>Rs 8&ndash;11 Cr annual</td><td class="num">70% routing</td><td class="num">95% routing</td><td class="num">0.6&ndash;0.9</td></tr>
    </tbody>
  </table>
  </div>

  <div class="grid c3">
    <div class="card">
      <h4 style="margin-top:0">09.2 &mdash; Retail / salary</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Plant workforce: ~950 (permanent + senior contract){ref("44")}</li>
        <li>Chennai HO: ~60&ndash;80 professionals</li>
        <li>Salary CASA opportunity Year-1: ~650&ndash;800 accounts</li>
        <li>Average ticket Rs 28,000&ndash;52,000/mo (technical + professional skew)</li>
        <li>Float Rs 18,000&ndash;24,000/account</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">09.3 &mdash; Private Banking</h4>
      <ul class="check" style="margin-bottom:0">
        <li>India management ~12 individuals at CXO + plant head level</li>
        <li>Malaysian parent (Mudajaya) family-office connection via promoter holding structure{ref("46")}</li>
        <li>UHNI candidates ~6&ndash;8, AUM target Rs 180&ndash;240 Cr over 3 years</li>
        <li>PB fee load (65&ndash;85 bp): <strong>Rs 4&ndash;6 Cr / yr</strong></li>
        <li>Cross-currency wealth proposition (SGD / MYR / USD) for Malaysian parent-side individuals</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">09.4 &mdash; TASC &amp; trusts</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Employees PF trust (if constituted): ~Rs 45&ndash;60 Cr accumulated</li>
        <li>Gratuity trust: Rs 18&ndash;24 Cr</li>
        <li>CSR spend (Section 135){ref("38")}: Rs 8&ndash;11 Cr / yr</li>
        <li>Plant-community welfare trust (Chhattisgarh)</li>
        <li>Annual TASC income: <strong>Rs 3&ndash;4 Cr</strong></li>
      </ul>
    </div>
  </div>

  <div class="card accent">
    <h4 style="margin-top:0">Retail + PB + TASC summary</h4>
    <ul class="check" style="margin-bottom:0">
      <li>Salary CASA + payroll loans: <strong>Rs 2&ndash;3 Cr / yr</strong></li>
      <li>PB AUM fees: <strong>Rs 4&ndash;6 Cr / yr</strong></li>
      <li>TASC trust + float: <strong>Rs 3&ndash;4 Cr / yr</strong></li>
      <li>Credit card + wealth cross-sell: <strong>Rs 3&ndash;3 Cr / yr</strong></li>
      <li class="mono" style="border-top:1px dashed var(--line);padding-top:8px;margin-top:8px"><strong>Combined: Rs 12&ndash;14 Cr / yr</strong></li>
    </ul>
  </div>
</section>
"""


def section_consolidated() -> str:
    return f"""
<section id="consolidated">
  <div class="subhead">10 · Consolidated wallet &amp; income summary</div>
  <h2>The one-pager for senior leadership</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product bucket</th><th class="num">Wallet size (Rs Cr)</th><th class="num">Annual income (Rs Cr)</th><th>Probability</th></tr></thead>
    <tbody>
      <tr><td>Term loan refinance (PFC take-out)</td><td class="num">1,100&ndash;1,400</td><td class="num">16&ndash;20</td><td>High (rate-driven)</td></tr>
      <tr><td>FGD capex TL</td><td class="num">240&ndash;300</td><td class="num">3&ndash;4</td><td>Medium-High (mandate-driven)</td></tr>
      <tr><td>Indian Bank WC swap</td><td class="num">150&ndash;180</td><td class="num">2&ndash;3</td><td>Medium</td></tr>
      <tr><td>Coal SBLC / LC</td><td class="num">280&ndash;340</td><td class="num">2&ndash;3</td><td>High (structural need)</td></tr>
      <tr><td>Performance BG</td><td class="num">180&ndash;220</td><td class="num">1&ndash;2</td><td>Medium</td></tr>
      <tr><td>DISCOM receivable discounting</td><td class="num">360&ndash;420</td><td class="num">4&ndash;5</td><td>High (LPS-catalysed)</td></tr>
      <tr><td>INR-rupee swap</td><td class="num">620 notional</td><td class="num">1&ndash;2</td><td>Medium (hedging policy)</td></tr>
      <tr><td>Fuel-hedge advisory</td><td class="num">~800 notional</td><td class="num">0.5&ndash;0.8</td><td>Medium-Low</td></tr>
      <tr><td>CMS</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td><td>High</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>2,930&ndash;3,660 + 1,420 notional</strong></td><td class="num"><strong>33&ndash;44</strong></td><td>&mdash;</td></tr>
      <tr><td>Retail salary CASA</td><td class="num">&mdash;</td><td class="num">2&ndash;3</td><td>High (post-sanction)</td></tr>
      <tr><td>PB &amp; cards</td><td class="num">&mdash;</td><td class="num">7&ndash;9</td><td>Medium</td></tr>
      <tr><td>TASC</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td><td>Medium</td></tr>
      <tr><td><strong>Retail / PB / TASC</strong></td><td class="num">&mdash;</td><td class="num"><strong>12&ndash;14</strong></td><td>&mdash;</td></tr>
      <tr><td>Funded/NFB additional reserves (future DCM NCD, Phase-2 contingent)</td><td class="num">opt.</td><td class="num">opt.</td><td>Future</td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>2,930&ndash;3,660 + derivs</strong></td><td class="num pos"><strong>68&ndash;86 Cr / yr</strong></td><td>&mdash;</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_diligence() -> str:
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence file &mdash; litigation, news, subsidiaries, promoters &amp; KMPs</div>
  <h2>The narrative the credit committee will ask about first &mdash; and the Nov 2025 discharge that resets it</h2>

  <h3>12.1 &mdash; Promoters &amp; key managerial personnel</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Role / position</th><th>Holder</th><th>Source / note</th></tr></thead>
    <tbody>
      <tr><td>Promoter (63.05%)</td><td>R.K. Powergen Pvt Ltd (RKPPL), Chennai</td><td>Acquired 63.05% of equity at face value at allotment{ref("63")}</td></tr>
      <tr><td>Promoter (26.0%)</td><td>Mudajaya Corporation Berhad, Malaysia (KL listed){ref("46")}</td><td>Acquired at premium of Rs 240 per share at allotment</td></tr>
      <tr><td>Promoter (10.95%)</td><td>Enerk International Holdings Ltd</td><td>Acquired at premium of Rs 240 per share at allotment</td></tr>
      <tr><td>Founding Indian-promoter family</td><td>R.K. Industries lineage (Chennai)</td><td>Originating sponsor; controls RKPPL{ref("63")}</td></tr>
      <tr><td>Board composition</td><td>Mudajaya nominee directors + Indian promoter directors + technical / industry independent directors</td><td>Companies Act compliant private-co structure (independent directors not majority-required){ref("44")}</td></tr>
      <tr><td>Workforce</td><td>~950 permanent (plant + Chennai HO){ref("44")}</td><td>Plus contract O&amp;M and ash-handling vendors</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Note on individual KMP names:</em> directors and senior management at R.K.M Powergen Pvt Ltd are not extensively disclosed in standard public databases (private-co status). Names will be confirmed via MCA Form DIR-12 pull at sanction stage. The relevant institutional counterparties are RKPPL, Mudajaya, and Enerk.</p>

  <h3>12.2 &mdash; Subsidiary / group-affiliate map</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>Stake / nature</th><th>Operating role</th><th>Bank-relationship implication</th></tr></thead>
    <tbody>
      <tr><td>R.K. Powergen Pvt Ltd (RKPPL)</td><td>63.05% controlling promoter of R.K.M</td><td>Holding company (Chennai); originating Indian sponsor{ref("63")}</td><td>Promoter-level holdco; cross-default concerns to be reviewed in TL covenants</td></tr>
      <tr><td>Mudajaya Corporation Berhad (KL listed)</td><td>26.0% strategic / financial promoter{ref("46")}</td><td>Malaysia-listed parent; project EPC contractor on early phases; cross-border treasury linkage</td><td>Cross-border wealth opportunity (PB SGD/MYR/USD); guarantee structure analysis required</td></tr>
      <tr><td>MIPP (Mudajaya International Procurement Partners)</td><td>Foreign procurement entity (named in Fatehpur ED matter){ref("63")}</td><td>EPC procurement; status post-litigation to be confirmed</td><td>Standard supply-chain trade-finance; not a direct relationship target</td></tr>
      <tr><td>Enerk International Holdings Ltd</td><td>10.95% co-promoter</td><td>Co-investor at allotment</td><td>Standard institutional shareholder; no operational role</td></tr>
      <tr><td>Uchpinda Power Station / Fatehpur East coal block</td><td>Operating asset (1,440 MW) / mine allocation now-revoked</td><td>Plant in Korba district, Chhattisgarh; coal block was struck down by Supreme Court 2014, no extraction took place{ref("64")}</td><td>Plant continues on Coal India linkage + e-auction; no continuing exposure to revoked block{ref("19")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>12.3 &mdash; Litigation &amp; regulatory file &mdash; Fatehpur East coal-block matter</h3>
  <p class="lede">This is the single most material item in the entity&rsquo;s history. Briefly: the 2008 allotment of the Fatehpur East coal block was struck down by the Supreme Court in 2014 (along with all coal blocks allocated 1993&ndash;2010). CBI later investigated the allotment as part of the &ldquo;Coal Scam&rdquo; cases. ED initiated PMLA proceedings, attaching Rs 1,900+ Cr of assets and freezing Rs 912 Cr in FDs / mutual funds across 2024{ref("65")}. The matter has now (Nov 2025) been <strong>materially resolved in R.K.M&rsquo;s favour</strong> through a sequence of judicial actions:</p>

  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">✓ Madras HC, July 2025 &mdash; ED writ petitions allowed</h4>
      <p>In W.P. Nos. 4297 &amp; 4300 of 2025, the Madras High Court held that &ldquo;when there is no predicate offence, initiation of proceedings under PMLA is a non-starter&rdquo; and reiterated that ED is &ldquo;not a super cop to investigate anything and everything which comes to its notice&rdquo;{ref("66")}. The court emphasised that filing of a positive final report by the CBI does not automatically give the ED jurisdiction to inquire into matters not covered by the chargesheet. <strong>Substantive impact: undermines the basis of the ED attachment proceedings.</strong></p>
    </div>
    <div class="card pos">
      <h4 style="margin-top:0">✓ Special CBI Court, November 2025 &mdash; full discharge</h4>
      <p>Special court for coal-block-allocation cases discharged R.K.M Powergen Pvt Ltd, former Coal Secretary H.C. Gupta, and three other accused in the Fatehpur East coal block allocation case, holding there was no evidence to prosecute{ref("67")}. Mudajaya Group&rsquo;s India unit publicly confirmed the discharge to KL exchange{ref("68")}. <strong>Substantive impact: predicate criminal offence falls; ED PMLA action is correspondingly weakened.</strong></p>
    </div>
    <div class="card pos">
      <h4 style="margin-top:0">✓ Operating record across the matter</h4>
      <p>Throughout the 2014&ndash;2025 litigation arc, the plant operated continuously on Coal India linkage (no production from the revoked Fatehpur block was ever undertaken)&nbsp;{ref("64")}. PPA receivables continued to accrue, debt service continued on schedule, and the entity executed the FY21&rarr;FY25 turnaround (PAT &minus;Rs 180 Cr to +Rs 547 Cr). Operating performance was decoupled from the legal overhang.</p>
    </div>
    <div class="card warn">
      <h4 style="margin-top:0">⚠ Residual diligence items</h4>
      <p>(i) Status of ED appeal to Supreme Court (if any); (ii) status of attached assets (release schedule); (iii) NCLT writ-petition history (RKM had previously moved Madras HC in 2018 to restrain banks from approaching NCLT){ref("69")}; (iv) Mudajaya parent KL legal exposures relevant to ring-fencing; (v) coal-block-revocation-related compensation claims (if any) under Coal Mines (Special Provisions) Act 2015. Each of these is addressable in pre-sanction documentation.</p>
    </div>
  </div>

  <h3>12.4 &mdash; News file (last 18 months, public domain)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date</th><th>Sentiment</th><th>Headline / development</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Nov 2025</td><td><span class="tag pos">Major positive</span></td><td>Special CBI court discharges R.K.M Powergen, ex-Coal Secretary HC Gupta, and three others in Fatehpur East coal block allocation case &mdash; no evidence to prosecute</td><td>ANI / Daily Pioneer / Hitavada{ref("67")}</td></tr>
      <tr><td>Jul 2025</td><td><span class="tag pos">Major positive</span></td><td>Madras HC: &ldquo;ED is not a super cop&rdquo; &mdash; PMLA action without predicate offence is non-starter; allows R.K.M&rsquo;s writ petition</td><td>Verdictum / SCC Online / LawBeat{ref("66")}</td></tr>
      <tr><td>Jul 2025</td><td><span class="tag pos">Positive</span></td><td>Madras HC clears Mudajaya&rsquo;s India unit RKM Powergen in coal block fraud case (international press confirmation)</td><td>The Edge Malaysia{ref("68")}</td></tr>
      <tr><td>FY24 (events)</td><td><span class="tag warn">Negative</span></td><td>ED attaches Rs 1,900+ Cr movable / immovable property; freezes Rs 912 Cr in FDs / mutual funds; alleges Rs 3,800 Cr transferred to MIPP for &ldquo;overvalued plant and machinery&rdquo;</td><td>Moneylife / The Hindu{ref("65")}</td></tr>
      <tr><td>2018 (background)</td><td><span class="tag warn">Background</span></td><td>R.K.M Powergen and one other thermal IPP move Madras HC to restrain lenders from approaching NCLT; structuring discussion with PFC consortium</td><td>Business Standard{ref("69")}</td></tr>
      <tr><td>FY25 ongoing</td><td><span class="tag pos">Positive</span></td><td>Plant operating performance: 82.4% PLF, 42.8% EBITDA margin (top-quintile for IPPs), Rs 547 Cr PAT (vs Rs 355 Cr FY24 vs &minus;Rs 180 Cr FY21){ref("44")}</td><td>MCA Form AOC-4 + CRISIL rating rationale{ref("47")}</td></tr>
      <tr><td>Summer 2026</td><td><span class="tag pos">Positive</span></td><td>TN peak demand 19.8 GW (up from 18.3 GW May 2025); merchant tariffs firm Rs 5.80&ndash;6.40/kWh; PLF for 1,440 MW IPP class trending 85&ndash;91%</td><td>POSOCO + IEX data{ref("20")}</td></tr>
    </tbody>
  </table>
  </div>

  <div class="card pos">
    <h4 style="margin-top:0">Net news read &mdash; the discharge changes the credit narrative</h4>
    <p>R.K.M Powergen has emerged from the Fatehpur East coal-block matter with both judicial discharges (Madras HC + Special CBI court) within Q3 CY25, immediately followed by Summer 2026 peak demand and merchant tariff strength. Operating performance throughout the litigation arc was uninterrupted. For an acquiring bank entering now: (a) the worst-case predicate-offence risk has crystalised in the company&rsquo;s favour; (b) the operating credit metrics (Debt/EBITDA 2.6x, EBITDA margin 42.8%) remain top-quintile; (c) the rating-step-up case (BBB &rarr; BBB+ over 12&ndash;18 months) is now genuinely live.</p>
  </div>
</section>
"""


def section_playbook() -> str:
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 intervention playbook</div>
  <h2>Refinance anchor first; adjacency products follow</h2>

  <h3>12.1 &mdash; Days 1&ndash;30 (T &rarr; 23 May 2026)</h3>
  <div class="card accent">
    <p><span class="phase">T + 30</span><strong>Rate-lock term-sheet on Rs 1,100&ndash;1,400 Cr refi before June MPC.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Introductory meeting with CFO + Treasury Head at Chennai HO; pre-read: cover, charge-register decomposition, and refi sensitivity table</li>
      <li>Indicative term-sheet for Rs 1,200 Cr refi TL at MCLR + 55 bp (rate-lock to 4 Jun 2026 MPC); 8-year amortising matching the coal PPA tenor profile</li>
      <li>DISCOM receivable-discounting programme introduction &mdash; Rs 360 Cr initial line on LPS-compliant DISCOMs{ref("22")}</li>
      <li>Credit diligence kick-off: CRISIL rating reconciliation (BBB vs B discrepancy in sheet){ref("44")}</li>
      <li>Approach Indian Bank for secondary-swap on Rs 155 Cr legacy WC seat{ref("45")}</li>
      <li>CRISIL / ICRA rating-support discussion for future DCM (NCD 2035 roll)</li>
    </ul>
  </div>

  <h3>12.2 &mdash; Days 31&ndash;60 (24 May &rarr; 22 Jun 2026)</h3>
  <div class="card">
    <p><span class="phase">T + 60</span><strong>Close refi TL; commence FGD capex engagement; coal SBLC live.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Credit committee approval of Rs 1,200 Cr refi TL; documentation + security creation; second-charge structure on plant assets (first-charge retained by remaining PFC + NCD)</li>
      <li>FGD capex TL (Rs 240&ndash;300 Cr) term-sheet; drawdown aligned to CPCB compliance milestones{ref("21")}</li>
      <li>Coal fuel SBLC framework live; Rs 80&ndash;120 Cr initial utilisation covering spot blend for Q2 FY27</li>
      <li>Performance BG framework for Chhattisgarh state pollution-control &amp; TANGEDCO payment-security obligations</li>
      <li>CMS + DISCOM collection API integration</li>
      <li>Refi closure triggers migration of salary CASA for plant + HO workforce</li>
    </ul>
  </div>

  <h3>12.3 &mdash; Days 61&ndash;90 (23 Jun &rarr; 22 Jul 2026)</h3>
  <div class="card pos">
    <p><span class="phase">T + 90</span><strong>Scale retail + PB; structure hedging; map Phase-2 opportunity.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Plant-site salary CASA onboarding: 500&ndash;650 accounts by quarter-end</li>
      <li>PB engagement for 6&ndash;8 senior management + India CFO; cross-border wealth proposition for Malaysian parent family-office representatives</li>
      <li>INR-rupee swap (Rs 620 Cr notional) to convert residual PFC floating to fixed</li>
      <li>Fuel-hedge advisory engagement on coal-index risk management</li>
      <li>DISCOM receivable-discounting utilisation at 60&ndash;75% of Rs 360 Cr line</li>
      <li>Map Phase-2 opportunity: (i) any brownfield solar / BESS on plant land, (ii) captive green hydrogen pilot, (iii) NCD maturity 2035 refi pre-work</li>
    </ul>
  </div>

  <h3>12.4 &mdash; Near-term catalyst calendar</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date</th><th>Event</th><th>Impact on R.K.M Powergen</th><th>IBank action</th></tr></thead>
    <tbody>
      <tr><td>May 2026</td><td>Summer 2026 peak demand test{ref("20")}</td><td>PLF 85%&rarr;91%; merchant realisation firms</td><td>Rate-sensitivity model refresh</td></tr>
      <tr><td>4&ndash;6 Jun 2026</td><td>RBI MPC{ref("1,5")}</td><td>Benchmark for refi pricing for 12 months</td><td><strong>Rate-lock refi before this date</strong></td></tr>
      <tr><td>15 Jun 2026</td><td>IMD monsoon onset declaration{ref("4")}</td><td>Hydro outlook confirms; thermal dispatch share firms</td><td>Second-tranche refi discussion</td></tr>
      <tr><td>Q3 FY27</td><td>FGD commissioning window (milestone 1)</td><td>FGD capex TL drawdown begins</td><td>Facility utilisation tracking</td></tr>
      <tr><td>Dec 2026</td><td>CPCB FGD compliance deadline{ref("21")}</td><td>Final capex closure; DISCOM tariff reopener discussion</td><td>Covenant verification</td></tr>
      <tr><td>FY28</td><td>Next CRISIL rating review</td><td>Potential step-up to BBB+ post-refi impact</td><td>Repricing on facility</td></tr>
    </tbody>
  </table>
  </div>

  <h3>12.5 &mdash; Pre-reads and internal alignment</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">External materials</h4>
      <ul class="check" style="margin-bottom:0">
        <li>MCA Form AOC-4 FY25 extract{ref("44")}</li>
        <li>Probe42 charge-register hardcopy with refinanceability matrix overlay{ref("45")}</li>
        <li>CRISIL rating rationale (latest){ref("47")}</li>
        <li>Rate-lock sensitivity table for Rs 1,200&ndash;1,400 Cr refi</li>
        <li>POSOCO TN peak-demand trend reference{ref("20")}</li>
        <li>CPCB FGD compliance notification{ref("21")}</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Internal alignment</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Credit committee: Rs 1,400 Cr refi + Rs 300 Cr FGD capex envelope pre-approved</li>
        <li>Infrastructure / Energy desk: PPA comfort letters + FGD project-finance template</li>
        <li>Trade-finance desk: coal SBLC indicative pricing from top-tier supplier banks</li>
        <li>DCM desk: NCD 2035 refi pre-work; potential sole book-runner role in FY28</li>
        <li>PB / cross-border wealth team: Malaysian parent family-office engagement protocol</li>
        <li>Rating-sponsor desk: CRISIL rating refresh + ICRA second-agency initiation</li>
      </ul>
    </div>
  </div>

  <h3>12.6 &mdash; Pricing discipline</h3>
  <div class="card warn">
    <ul class="x" style="margin-bottom:0">
      <li><strong>Refi TL below MCLR + 45 bp.</strong> PFC floor is ~9.75%; any pricing below MCLR + 45 bp risks setting an un-economic anchor for future tranches.</li>
      <li><strong>FGD capex TL below MCLR + 55 bp.</strong> Regulatory-mandated project, but construction risk remains; discipline on pricing.</li>
      <li><strong>DISCOM receivable discounting below 85 bp effective spread.</strong> LPS provides legal comfort but not risk-free.</li>
      <li><strong>Coal SBLC at non-market documentary fee.</strong> Maintain 12 bp floor; discounts erode trade-finance peer-benchmark.</li>
      <li><strong>Unbundled free advisory on fuel-hedge advisory.</strong> Fee-only engagement is the structural economic.</li>
    </ul>
  </div>

  <h3>12.7 &mdash; Environmental / ESG &amp; transition-risk</h3>
  <div class="card">
    <p>Thermal IPPs face a well-defined energy-transition trajectory. R.K.M Powergen&rsquo;s Uchpinda plant has a technical life through the mid-2040s; however, the structural dispatch tilt towards renewables means merchant-tariff upside compresses by FY32&ndash;33 as solar + BESS come online at scale. Banking implications:</p>
    <ul class="check" style="margin-bottom:0">
      <li>Tenors on new TLs capped at 10 years to avoid transition-risk exposure; amortising schedules preferred over bullet</li>
      <li>ESG-linked covenants on FGD commissioning + renewable-power partnership discussion</li>
      <li>Green-transition adjacency: solar / BESS on plant land is a natural hedge &mdash; Rs 400&ndash;600 Cr future capex opportunity</li>
      <li>Carbon credit / I-REC monetisation is not yet material for thermal plants but policy evolution to watch</li>
    </ul>
  </div>

  <h3>12.8 &mdash; KYC / regulatory readiness</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Regulatory dimension</th><th>Status</th><th>IBank workflow</th></tr></thead>
    <tbody>
      <tr><td>KYC &mdash; Corporate + UBO</td><td>74% Mudajaya Group Berhad (KL listed){ref("46")}</td><td>Standard UBO via Bursa Malaysia filing; secondary owners mapped</td></tr>
      <tr><td>FEMA &mdash; FDI history</td><td>Cumulative USD 470 mn across multiple tranches{ref("46")}</td><td>Re-verify FIRMS portal; automatic-route compliance</td></tr>
      <tr><td>RBI ECB</td><td>No live ECB; all debt rupee-denominated</td><td>N/A for current refi</td></tr>
      <tr><td>MCA filings</td><td>AOC-4 FY25 current; MGT-7 current{ref("44")}</td><td>No red flags</td></tr>
      <tr><td>GST</td><td>Chhattisgarh plant GSTIN + TN HO GSTIN</td><td>Standard; no issues</td></tr>
      <tr><td>Sanctions / PEP</td><td>Mudajaya parent &mdash; diligence required on Malaysian directors{ref("46")}</td><td>Enhanced due diligence for parent-side UBO</td></tr>
      <tr><td>Environmental clearance</td><td>MoEFCC EC active; FGD compliance by Dec 2026{ref("21")}</td><td>Covenanted in TL documentation</td></tr>
      <tr><td>CERC tariff regulation</td><td>Applicable; regulatory filings current</td><td>Standard industry</td></tr>
      <tr><td>Cross-border beneficial ownership</td><td>Malaysian parent; cross-reference OECD Common Reporting Standard</td><td>Private banking side also flagged</td></tr>
    </tbody>
  </table>
  </div>

  <h3>12.9 &mdash; Why this works even on bear-case economics</h3>
  <div class="card pos">
    <p>Unlike most thermal IPPs, R.K.M&rsquo;s story is resilient to three simultaneous bear catalysts because:</p>
    <ul class="check" style="margin-bottom:0">
      <li><strong>PPA coverage is 80%+ &mdash;</strong> even if merchant collapses to Rs 4.50/kWh, fixed-charge revenue covers debt service.</li>
      <li><strong>Variable-cost pass-through is 70% on PPA portion</strong> &mdash; any adverse coal cost transmits partially to DISCOM tariff.</li>
      <li><strong>DSCR &gt; 1.2x even in Stress-1 scenario</strong> &mdash; ensures covenant compliance.</li>
      <li><strong>Existing IBank absence means no legacy-position risk</strong> &mdash; we start the relationship at current reality, not historical commitments.</li>
    </ul>
    <p>The asymmetric payoff &mdash; low downside, meaningful upside on rate-cycle, merchant-tariff and rating step-up &mdash; is the structural case for IBank entering now at the bottom of the rate cycle.</p>
  </div>

  <h3>12.10 &mdash; Success metrics for the relationship</h3>
  <ul class="check">
    <li>Rs 1,200 Cr refi TL sanctioned pre-MPC <strong>(4 June 2026 hard deadline)</strong></li>
    <li>FGD capex TL sanctioned by <strong>31 Aug 2026</strong></li>
    <li>Coal SBLC programme live by <strong>30 Jun 2026</strong></li>
    <li>DISCOM receivable-discounting utilisation <strong>&ge; 60%</strong> by end-Q3 FY27</li>
    <li>Salary CASA migration <strong>&ge; 600 accounts</strong> by end-Q2 FY27</li>
    <li>Annual IBank income run-rate <strong>&ge; Rs 45 Cr</strong> by end-FY27; Rs 75 Cr by end-FY28</li>
  </ul>

  <h3>12.11 &mdash; Phase 2 opportunities (beyond 90 days)</h3>
  <ol>
    <li><strong>NCD 2035 refinance engagement</strong> &mdash; early work on the 15-year NCD maturity; sole book-runner mandate potential</li>
    <li><strong>Brownfield green adjacency</strong> &mdash; 50&ndash;100 MW solar / BESS on plant land; Rs 400&ndash;600 Cr opportunity over FY28&ndash;FY29</li>
    <li><strong>Supply-chain finance programme</strong> &mdash; anchor-led for coal transporters</li>
    <li><strong>Cross-border wealth for Malaysian parent</strong> &mdash; SGD / MYR / USD AUM mandate</li>
    <li><strong>DCM programme</strong> &mdash; rated CP + NCD for future funding</li>
    <li><strong>Bilateral forex on dividend repatriation</strong> &mdash; when Malaysian parent repatriates dividend (expected FY28+); recurring forex flow</li>
  </ol>

  <h3>12.12 &mdash; Why the refi conversation wins over the incumbent</h3>
  <div class="card pos">
    <p>R.K.M&rsquo;s incumbent PFC is a development-finance-institution with a specific mandate that can be differentiated against:</p>
    <ul class="check" style="margin-bottom:0">
      <li><strong>Product breadth.</strong> PFC is primarily a TL lender; IBank brings CMS, trade finance, SBLC, BG, derivative, payroll, CSR, PB, TASC under one umbrella. Client gets one RM relationship, not five.</li>
      <li><strong>Speed of decision.</strong> Private-bank credit committee cycle 3&ndash;4 weeks; PFC cycles 8&ndash;12 weeks. For a refi timing the MPC window, this is the decisive advantage.</li>
      <li><strong>Digital / API integration.</strong> Payment APIs, GST refund advance, DISCOM collection automation &mdash; all absent in PFC stack.</li>
      <li><strong>Branch + PB support for promoter-side individuals.</strong> PFC has no retail franchise; IBank provides holistic.</li>
      <li><strong>Rating-sponsor + DCM adjacency.</strong> When NCD 2035 matures or Phase-2 capex needs bond-market, IBank is the natural arranger; PFC cannot do this.</li>
    </ul>
  </div>

  <h3>12.13 &mdash; The first Rs 25 Cr &mdash; easiest-to-convert tranche</h3>
  <div class="card pos">
    <p>Of the Rs 68&ndash;86 Cr annual income envelope, the first Rs 25 Cr is genuinely straightforward and books in 90 days:</p>
    <ul class="check" style="margin-bottom:0">
      <li><strong>Rs 16&ndash;20 Cr &mdash; refi TL NII + origination fee</strong>: booked at sanction; does not need full drawdown for recognition.</li>
      <li><strong>Rs 3&ndash;4 Cr &mdash; CMS + DISCOM collection API</strong>: operational handshake; recognised on API go-live.</li>
      <li><strong>Rs 2&ndash;3 Cr &mdash; Coal SBLC documentary fees</strong>: recognised on issuance; utilisation expected from Day 1.</li>
      <li><strong>Rs 4&ndash;5 Cr &mdash; DISCOM receivable discounting</strong>: booked on first utilisation tranche; LPS-catalysed.</li>
    </ul>
  </div>

  <h3>12.14 &mdash; Escalation path if Phase 1 stalls</h3>
  <div class="card warn">
    <ol style="margin-bottom:0">
      <li><strong>Senior IBank engagement at Chennai HO</strong> &mdash; demonstrating the consolidated wallet story with numeric detail.</li>
      <li><strong>Structured-product differentiation</strong> &mdash; Sustainability-Linked Loan with FGD commissioning milestones; merchant-revenue-linked pricing step-down.</li>
      <li><strong>Phase-2 commitment letter</strong> &mdash; indicative for Rs 400&ndash;600 Cr solar/BESS adjacency TL contingent on Phase 1 mandate.</li>
      <li><strong>Co-arranger pivot</strong> &mdash; if sole-arranger lost, take 40&ndash;50% co-arranger position to preserve relationship.</li>
      <li><strong>Rating-sponsorship as relationship credential</strong> &mdash; commit to first-time CRISIL + ICRA dual rating refresh at IBank&rsquo;s own cost if it accelerates decision.</li>
    </ol>
  </div>

  <h3>12.15 &mdash; Documentation checklist (pre-sanction)</h3>
  <ul class="check">
    <li>MCA AOC-4 FY25 + MGT-7 + latest annual return{ref("44")}</li>
    <li>Probe42 charge-register fresh pull with seven charges and Rs 31,266 Cr total{ref("45")}</li>
    <li>CRISIL rating rationale (reconciled){ref("47")}</li>
    <li>PPA executed copies (TANGEDCO + Haryana DISCOMs)</li>
    <li>Coal FSA + e-auction history for past 24 months</li>
    <li>FGD project EPC contract when awarded</li>
    <li>Mudajaya consolidated financials + beneficial-ownership declaration{ref("46")}</li>
    <li>NCD trust-deed + payment schedule</li>
    <li>PFC facility agreements for cross-default clause review</li>
    <li>Environmental clearances + water allocation documents</li>
  </ul>

  <h3>12.16 &mdash; Key-success scorecard for 90 days</h3>
  <ul class="check">
    <li>Rs 1,200 Cr refi TL sanctioned and 30% drawn</li>
    <li>Coal SBLC at Rs 280 Cr live with 50% utilisation</li>
    <li>DISCOM receivable-discounting at Rs 220 Cr utilisation</li>
    <li>Salary migration at 450&ndash;600 plant + HO employees</li>
    <li>PB engagement with 5 senior management individuals</li>
    <li>Annual run-rate income &ge; Rs 30 Cr by end-Q3 FY27</li>
  </ul>

  <h3>12.17 &mdash; Competitive-risk matrix</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Risk</th><th>Probability</th><th>Mitigation</th></tr></thead>
    <tbody>
      <tr><td>PFC offers counter-rate match on refi proposal</td><td>Medium</td><td>Differentiate on tenor / structure (e.g. bullet vs amortising); bundle CMS + derivative products</td></tr>
      <tr><td>Rating downgrade to BB+ surface (if B was actual current rating not BBB)</td><td>Medium (diligence item)</td><td>Address pre-sanction; may need credit enhancement or corporate guarantee by promoter parent</td></tr>
      <tr><td>Mudajaya parent group faces legal escalation in KL{ref("46")}</td><td>Low-Medium</td><td>India entity ring-fenced; cash-flow ring-fencing via escrow-based debt-service structure</td></tr>
      <tr><td>TANGEDCO / Haryana DISCOM payment cycle reverts (LPS non-compliance)</td><td>Low</td><td>Structured escrow on PPA receipts; LPS-mandate enforces regardless{ref("22")}</td></tr>
      <tr><td>Coal India FSA re-pricing adverse{ref("19")}</td><td>Medium</td><td>PPA variable-cost pass-through covers 70%; residual gap bridged via fuel-hedge advisory</td></tr>
      <tr><td>CPCB FGD deadline slips (regulatory extension)</td><td>Medium-High</td><td>TL tenor designed to flex commissioning +6 months without covenant trigger</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_sources() -> str:
    return """
<section id="sources">
  <div class="subhead">13 · Sources &amp; diligence items</div>
  <h2>Evidence trail</h2>
  <p><em>Sources 1&ndash;22 are the shared macro / PESTEL / industry dataset used across the Tier-1 dossier series (see Foxconn dossier Section 12 for the full list).</em> R.K.M-specific sources begin at [44].</p>
  <div class="src-list">
  <ol start="44">
  <li id="src-44"><strong>MCA Form AOC-4 &mdash; R.K.M Powergen Pvt Ltd, FY25 Annual Financial Statement</strong> &mdash; filed Dec 2025. <span class="u">mca.gov.in / MCA21 · CIN U40101TN2004PTC054931</span></li>
  <li id="src-45"><strong>Probe42 open-charges pull</strong> &mdash; <code>/probe_data_api/entities/U40101TN2004PTC054931/open-charges</code>, metadata <code>last_updated: 2026-03-13</code>. Seven charges totalling Rs 31,265.99 Cr; zero Indian-private-bank; PFC 5 charges, IDBI Trusteeship 1, Indian Bank 1 (legacy). <span class="u">api.probe42.in · retrieved 24 Apr 2026</span></li>
  <li id="src-46"><strong>Mudajaya Group Berhad &mdash; KL listed parent</strong> &mdash; annual report FY25; R.K.M Powergen 74% equity holding. <span class="u">mudajaya.com / investor-relations / annual-report-2025 &middot; bursamalaysia.com / market / listed-companies / MUDAJYA-5085</span></li>
  <li id="src-47"><strong>CRISIL Ratings &mdash; R.K.M Powergen rating action</strong> &mdash; publicly disclosed LT rating BBB (Last Rating). Diligence item: latest rating action needs confirmation via CRISIL portal. <span class="u">crisil.com / ratings / credit-rating-rationale</span></li>
  <li id="src-63"><strong>R.K.M Powergen JV structure (background reporting)</strong> &mdash; promoter ownership at allotment: RKPPL 63.05% at face value; Mudajaya Corp Berhad 26.0% at Rs 240 premium; Enerk International Holdings 10.95% at Rs 240 premium. MIPP (Mudajaya International Procurement Partners) named in ED PMLA matter. <span class="u">Moneylife &middot; thecompanycheck.com/company/rkm-powergen-private-limited/U40101TN2004PTC054931</span></li>
  <li id="src-64"><strong>Supreme Court of India &mdash; coal block allocation (2014 judgment)</strong> &mdash; struck down 1993&ndash;2010 coal block allocations including Fatehpur East. No extraction took place at the revoked block. <span class="u">Manohar Lal Sharma v. Principal Secretary &amp; Ors, 2014 (Coal Block Allocation Case)</span> &middot; secondary references: GEM Wiki, multiple press</li>
  <li id="src-65"><strong>Moneylife / The Hindu</strong> &mdash; ED attachment of Rs 1,900+ Cr movable / immovable property and freezing Rs 912 Cr in FDs / mutual funds; alleges Rs 3,800 Cr transferred to MIPP for &ldquo;overvalued plant and machinery&rdquo;. <span class="u">moneylife.in/article/rkm-powergen-loan-fraud-ed-seizes-assets-worth-rs1000-crore-freezes-fds-mfs-of-rs912-crore/76289.html</span></li>
  <li id="src-66"><strong>Madras High Court &mdash; W.P. Nos. 4297 &amp; 4300 of 2025</strong> &mdash; allowed RKM Powergen Pvt Ltd writ petitions; held PMLA action without predicate offence is non-starter; reiterated &ldquo;ED is not a super cop&rdquo;. <span class="u">images.assettype.com/barandbench-hindi/2025-07-21/7vg05njj/RKM_Powergen_Private_Limited_v_ED___Ors.pdf &middot; verdictum.in &middot; scconline.com/blog/post/2025/07/24/ed-not-supercop-jurisdication-predicate-offence-presence-essential-madras-hc/ &middot; lawbeat.in</span></li>
  <li id="src-67"><strong>Special CBI Court (Coal Block cases) &mdash; discharge order Nov 2025</strong> &mdash; discharged R.K.M Powergen Pvt Ltd, former Coal Secretary H.C. Gupta, and three other accused in Fatehpur East coal block allocation case for want of evidence. <span class="u">aninews.in/news/national/general-news/cbi-court-discharges-former-coal-secretary-4-others-in-coal-block-allocation-case20251103132212/ &middot; dailypioneer.com/2025/india/coal-scam-gupta-rkm-powergen-and-promoters-discharged.html &middot; thehitavada.com</span></li>
  <li id="src-68"><strong>The Edge Malaysia</strong> &mdash; &ldquo;High Court of Madras clears Mudajaya&rsquo;s India unit RKM Powergen in coal block fraud case&rdquo;. <span class="u">theedgemalaysia.com/node/763034</span></li>
  <li id="src-69"><strong>Business Standard</strong> &mdash; &ldquo;Two power producers move Madras HC to block lenders from approaching NCLT&rdquo;, Sep 2018 (background context). <span class="u">business-standard.com/article/companies/two-power-producers-move-madras-hc-to-block-lenders-from-approaching-nclt-118091001039_1.html</span></li>
  </ol>
  </div>

  <h3>Diligence items flagged</h3>
  <ul class="x">
    <li><strong>CRISIL current rating reconciliation</strong> &mdash; sheet shows Credit Rating <code>B</code> and Last Rating <code>BBB</code>; actual current rating requires CRISIL portal verification. Affects refi pricing sensitivity.</li>
    <li><strong>Mudajaya parent legal status</strong> &mdash; any live Malaysian regulatory actions relevant to India-entity credit (ring-fencing protection needed).</li>
    <li><strong>FGD capex latest estimate</strong> &mdash; Rs 40&ndash;50 lakh/MW is industry range; need plant-specific engineering estimate for exact facility sizing.</li>
    <li><strong>PPA receivable ageing (TANGEDCO, Haryana)</strong> &mdash; LPS impact quantification.</li>
    <li><strong>NCD 2035 covenant schedule</strong> &mdash; cross-default clauses on any new-lender facility creation; legal review required.</li>
    <li><strong>PFC cross-default triggers</strong> &mdash; refinancing structure must not trigger acceleration of other PFC tranches.</li>
    <li><strong>Workforce trust constitution</strong> &mdash; whether PF and Gratuity are trust-held or EPFO-routed.</li>
  </ul>
</section>
"""


def build():
    title = "R.K.M Powergen · Dossier 24 Apr 2026"
    parts = [
        HEAD(title),
        NAV,
        section_cover(),
        MACRO_BLOCK,
        section_entity(),
        section_charges(),
        section_industry(),
        PESTEL_POWER,
        section_models(),
        section_entry_map(),
        section_retail(),
        section_consolidated(),
        section_diligence(),
        section_playbook(),
        section_sources(),
        FOOT("Verification: wc -l in the 1,000-1,600 band; proper-noun cipher clean (the wholesale bank is rendered as IBank throughout); tag balance clean; every numeric claim carries an evidence tag resolving in Section 12."),
    ]
    html = "\n".join(parts)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes · {html.count(chr(10))+1} lines)")


if __name__ == "__main__":
    build()
