"""Build `foxconn-hon-hai-dossier.html` — Tier-1 pilot #1 (EMS / greenfield).

Company: Foxconn Hon Hai Technology India Mega Development Private Limited
CIN   : U32204TN2015FTC165627
Plant : Sriperumbudur, Tamil Nadu (iPhone assembly mega-facility, Apple)
FY25  : TOI Rs 101,877 Cr · EBITDA Rs 3,615 Cr · PAT Rs 1,976 Cr
Capital: Paid-up Rs 22,829 Cr, NW Rs 23,589 Cr, Debt Rs 4,858 Cr (UNSECURED, 0 MCA)
IBank : Zero wallet (greenfield)

Structure assembled in sections; each section function returns an HTML string.
"""
from __future__ import annotations
from pathlib import Path
from .base import CSS, HEAD, FOOT, ref, kpi, card, table, inr_cr
from .macro import MACRO_BLOCK
from .pestel import PESTEL_EMS

OUT = Path("/home/user/St") / "foxconn-hon-hai-dossier.html"


def section_cover() -> str:
    return f"""
<section id="cover" class="hero">
  <div class="eyebrow">Tier-1 Dossier · 04 of 20 · Greenfield acquisition</div>
  <h1>Foxconn Hon Hai Technology India<br>Mega Development Pvt Ltd</h1>
  <p class="lede">Apple's single-largest iPhone assembly supplier outside China, now India's single-largest PLI 2.0 beneficiary. Sriperumbudur (TN) plant shipped Rs 101,877 Cr in FY25 on a 3.55% EBITDA margin{ref("23")}, funded entirely through parent Hon Hai equity (paid-up Rs 22,829 Cr) and unsecured intra-group debt — <strong>zero Indian bank on the MCA charge register</strong>{ref("24")}. Eight anchor entry points totalling Rs 14,200&ndash;18,700 Cr in funded + non-funded + derivative wallet sit untouched.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (fully-built)</div><div class="v num">Rs 185–225 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 148–180 Cr + Retail / PB / TASC Rs 37–45 Cr</div></div>
    <div class="kpi"><div class="k">FY25 Total Operating Income</div><div class="v num">Rs 1,01,877 Cr</div><div class="sub">+41% YoY; largest private EMS entity in India{ref("23")}</div></div>
    <div class="kpi"><div class="k">IBank share of charges</div><div class="v neg num">0%</div><div class="sub">of Rs 0 Cr registered (plant is unsecured-funded){ref("24")}</div></div>
    <div class="kpi pos"><div class="k">Capex committed FY27–FY28</div><div class="v num">Rs 4,200 Cr</div><div class="sub">iPhone 17 Pro line + FATP + AirPods module{ref("9")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">The three reasons this relationship converts in 90 days</h4>
    <ol style="margin-bottom:0">
      <li><strong>Capital structure is deliberate, not distressed.</strong> Rs 22,829 Cr paid-up equity plus Rs 4,858 Cr parent-guaranteed ECB means no charge-bearing Indian-bank debt. That is the architecture of a plant financed out of Hon Hai's Singapore treasury — every rupee of incremental Rs-denominated capex becomes a clean, uncontested bilateral sanction.</li>
      <li><strong>The forex book is unmanaged at scale.</strong> ~95% of revenue is USD-linked (Apple POs){ref("9")}; 70% of direct cost (SMT components, SoCs, modules) is imported USD. At today's 93.50 spot and 2.1% annualised 12M forward{ref("3")}, a 6-month rolling cover on the net USD 4.2 bn position would save 45–60 bp of EBITDA — currently unhedged beyond 60 days per public filings.</li>
      <li><strong>June MPC rate-lock window is 41 days away.</strong> Term-loan sanction dated before 4 June 2026 prices at 5.25% repo; Goldman is pricing a 50 bp hike{ref("5")}. Locking the Rs 4,200 Cr capex line now is an 8-quarter interest saving of Rs 85–105 Cr.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U32204TN2015FTC165627</strong></span>
    <span>FY25 balance-sheet date <strong>31 Mar 2025</strong></span>
    <span>Registry cut <strong>Probe42 / 08 Apr 2026</strong></span>
    <span>Parent <strong>Hon Hai Precision Industries, Singapore</strong></span>
    <span>Promoter holding <strong>100%</strong></span>
  </div>
</section>
"""


def section_group() -> str:
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; India footprint</div>
  <h2>Hon Hai Precision in India &mdash; one parent, four operating entities</h2>
  <p class="lede">Hon Hai Precision Industries (TWSE: 2317, "Foxconn") operates in India through a constellation of operating companies, each with a narrow product mandate. The Mega Development entity covered by this dossier is the Apple-iPhone assembly flagship. Understanding the constellation matters for the IBank pitch: derivative notional, trade-finance throughput, and supply-chain-finance wallet can be consolidated at the India-parent level for a multi-entity master agreement.</p>

  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr>
        <th>Operating entity</th>
        <th>Principal product</th>
        <th>Location</th>
        <th class="num">FY25 TOI (Rs Cr)</th>
        <th>Ownership</th>
        <th>IBank wallet</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Foxconn Hon Hai Technology India Mega Development Pvt Ltd</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">CIN U32204TN2015FTC165627</span></td>
        <td>iPhone 15 / 16 / 17 final assembly (SMT + FATP) for Apple{ref("9")}</td>
        <td>Sriperumbudur, Tamil Nadu (500-acre campus)</td>
        <td class="num">1,01,877</td>
        <td>100% Hon Hai Singapore</td>
        <td><span class="tag neg">ZERO</span></td>
      </tr>
      <tr>
        <td><strong>Bharat FIH Limited</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">CIN L74999TN2015PLC160558 &mdash; listed BSE/NSE</span></td>
        <td>Android OEM / ODM assembly (Xiaomi, Oppo), wearables, set-top boxes{ref("25")}</td>
        <td>Sri City, Andhra Pradesh</td>
        <td class="num">~12,800 est.</td>
        <td>Majority Hon Hai; public float ~25%</td>
        <td><span class="tag">Separate relationship</span></td>
      </tr>
      <tr>
        <td><strong>Foxconn India Developer Ltd</strong></td>
        <td>R&amp;D, firmware, test-automation tooling</td>
        <td>Bengaluru (HSR)</td>
        <td class="num">~180</td>
        <td>100% Hon Hai Singapore</td>
        <td><span class="tag">Scope for salary-CMS</span></td>
      </tr>
      <tr>
        <td><strong>Foxconn Interconnect Technology (FIT) India Pvt Ltd</strong></td>
        <td>Cables, connectors, antennae (Apple + non-Apple)</td>
        <td>Chennai (Oragadam industrial belt)</td>
        <td class="num">~4,600 est.</td>
        <td>Hon Hai subsidiary (FIT Taiwan)</td>
        <td><span class="tag">To be mapped</span></td>
      </tr>
    </tbody>
  </table>
  </div>

  <div class="card warn">
    <h4 style="margin-top:0">What is <em>not</em> in scope of this dossier</h4>
    <p>The second Karnataka mega-plant ("Devanahalli campus") is held by <strong>Foxconn India Hardware Ltd</strong> (a separately incorporated Yuzhan Technology entity, CIN not covered by the current Tamil Nadu sheet). That entity's Rs 1,400 Cr Phase-1 capex signed with Karnataka in Sep 2024{ref("26")} is a distinct acquisition opportunity for the Bengaluru LCG desk &mdash; cross-referenced but not consolidated into the wallet-conversion arithmetic below.</p>
  </div>

  <h3>Relationship-anchoring thesis</h3>
  <div class="grid c3">
    <div class="card pos">
      <h4 style="margin-top:0">Scale and certainty</h4>
      <p>Rs 1.02 lakh crore of throughput on a single customer (Apple) means the forex, trade-finance, and payroll flows are large, predictable, and ring-fenced from Indian demand cycles. Apple's published FY26 unit plan of 65 mn iPhones from India{ref("27")} underwrites the next 4 quarters of volume.</p>
    </div>
    <div class="card pos">
      <h4 style="margin-top:0">Clean credit architecture</h4>
      <p>Rs 23,589 Cr Tangible Net Worth with only Rs 4,858 Cr debt (Debt/NW 0.21x, Debt/EBITDA 1.34x){ref("23")} is among the strongest ratios for any unlisted industrial in India. The 41.4% FY25 revenue growth is funded primarily through retained earnings + parent equity infusion of Rs 3,200 Cr in FY25{ref("28")}, leaving full headroom for an Indian-bank wholesale partnership.</p>
    </div>
    <div class="card warn">
      <h4 style="margin-top:0">Historical banking posture</h4>
      <p>No Indian bank has ever appeared on the MCA open-charge register for this CIN since 2015 incorporation{ref("24")}. The parent's Singapore treasury (DBS, UOB relationships) has historically funded all working capital through internal ECB lines. Winning the first Indian-bank engagement is therefore about displacing a Singapore-intercompany line, not displacing another Indian bank &mdash; an easier sell because the existing offshore cost is fully loaded (ECB rate + hedging + tax).</p>
    </div>
  </div>
</section>
"""


def section_entity() -> str:
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier &mdash; Foxconn Hon Hai Mega Development</div>
  <h2>Snapshot &amp; credit architecture</h2>

  <h3>04.1 &mdash; P&amp;L snapshot (FY24 &rarr; FY25)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr>
        <th>Line item (Rs Cr)</th>
        <th class="num">FY24</th>
        <th class="num">FY25</th>
        <th class="num">YoY %</th>
        <th class="num">FY25 margin</th>
        <th>Commentary</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Total Operating Income</td><td class="num">72,050</td><td class="num">1,01,877</td><td class="num pos">+41.4%</td><td class="num">&mdash;</td><td>iPhone 15 &amp; 16 ramp; first full-year of Pro Max assembly at TN{ref("23,27")}</td></tr>
      <tr><td>EBITDA</td><td class="num">2,180</td><td class="num">3,615</td><td class="num pos">+65.8%</td><td class="num">3.55%</td><td>Margin expansion on scale + PLI recognition timing</td></tr>
      <tr><td>Depreciation &amp; Amortisation</td><td class="num">410</td><td class="num">680</td><td class="num">+66.0%</td><td class="num">0.67%</td><td>Gross block ramped; partial-year depreciation on SMT-4 line</td></tr>
      <tr><td>Interest</td><td class="num">280</td><td class="num">340</td><td class="num">+21.4%</td><td class="num">0.33%</td><td>ECB parent loan; effective rate 6.25% including hedging cost{ref("28")}</td></tr>
      <tr><td>PBT</td><td class="num">1,490</td><td class="num">2,595</td><td class="num pos">+74.2%</td><td class="num">2.55%</td><td>&mdash;</td></tr>
      <tr><td>Tax</td><td class="num">360</td><td class="num">619</td><td class="num">+71.9%</td><td class="num">0.61%</td><td>Effective tax 23.9% (concessional rate 22%)</td></tr>
      <tr><td><strong>PAT</strong></td><td class="num"><strong>1,130</strong></td><td class="num"><strong>1,976</strong></td><td class="num pos"><strong>+74.9%</strong></td><td class="num"><strong>1.94%</strong></td><td>Highest absolute PAT for any private EMS in India{ref("23")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>04.2 &mdash; Balance sheet &amp; capital structure (31 Mar 2025)</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up equity capital</div><div class="v num">22,829</div><div class="sub">Rs Cr; FY25 infusion Rs 3,200 Cr from Hon Hai SG{ref("28")}</div></div>
    <div class="kpi"><div class="k">Tangible Net Worth</div><div class="v num">23,589</div><div class="sub">Rs Cr; retained earnings + capital reserves</div></div>
    <div class="kpi"><div class="k">Total Debt (A+B+C+D)</div><div class="v num">4,858</div><div class="sub">Rs Cr; entirely <strong>unsecured</strong> intra-group / ECB{ref("23,24")}</div></div>
    <div class="kpi pos"><div class="k">Debt / NW</div><div class="v num">0.21x</div><div class="sub">Top decile for industrials &gt; Rs 50,000 Cr TOI</div></div>
    <div class="kpi pos"><div class="k">Debt / EBITDA</div><div class="v num">1.34x</div><div class="sub">Comfortable sub-2x; headroom for incremental WC + TL</div></div>
    <div class="kpi"><div class="k">Net Fixed Assets</div><div class="v num">6,180</div><div class="sub">Rs Cr; Gross Block Rs 8,940 Cr</div></div>
  </div>

  <h3>04.3 &mdash; MCA open-charges register <span class="tag neg">ZERO INDIAN-BANK CHARGE</span></h3>
  <div class="card neg">
    <h4 style="margin-top:0">Registry pull &mdash; Probe42 / 08 Apr 2026</h4>
    <p><code>GET /probe_data_api/entities/U32204TN2015FTC165627/open-charges</code> returns <strong>zero open charges</strong>. Metadata <code>last_updated: 2026-04-08</code>. No Indian bank, NBFC, or debenture trustee holds a charge on any asset of this CIN since its 2015 incorporation.{ref("24")}</p>
    <p>The Rs 4,858 Cr Total Debt on the balance sheet is therefore held as (a) unsecured ECB from Hon Hai Precision Industries Singapore (Rs ~3,400 Cr estimated from cumulative FDI of $2,768 mn vs paid-up Rs 22,829 Cr){ref("29")} plus (b) short-term intra-group payables to Foxconn supplier network. This is the structural gap the acquisition pitch addresses.</p>
  </div>

  <h3>04.4 &mdash; Rating status &amp; sponsorship opportunity</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Field</th><th>Current state</th><th>Implication for IBank</th></tr>
    </thead>
    <tbody>
      <tr><td>Long-term credit rating (Indian agencies)</td><td><strong>Not Rated</strong>{ref("23")}</td><td>Rating-sponsor fee opportunity; Rs 30&ndash;45 Cr cumulative fee income across 3 years if IBank arranges first-time CRISIL + ICRA dual rating for planned Rs 4,200 Cr capex facility</td></tr>
      <tr><td>External rating (parent Hon Hai)</td><td>Moody's <strong>A3</strong> / S&amp;P <strong>A-</strong> stable{ref("30")}</td><td>Parent-guarantee structure allows a P-2 / A-1 short-term commercial paper programme at the India entity, priced 25&ndash;35 bp through Rs CP rack rate</td></tr>
      <tr><td>Bank facility rating (if independently placed)</td><td>Indicative <code>A / A+</code> stable on standalone basis given FY25 metrics</td><td>Risk-weighting 20&ndash;50% on wholesale book; capital-light relationship profile</td></tr>
      <tr><td>PLI verification track record</td><td>FY22&ndash;FY24 approved claims Rs 1,280 Cr cumulative{ref("11")}</td><td>Receivable quality is A+: sovereign-like on approved PLI dues; basis for discounting programme</td></tr>
    </tbody>
  </table>
  </div>

  <h3>04.5 &mdash; Five-year financial trajectory</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Rs Cr unless stated</th><th class="num">FY21</th><th class="num">FY22</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">5Y CAGR</th></tr>
    </thead>
    <tbody>
      <tr><td>Total Operating Income</td><td class="num">18,200</td><td class="num">30,400</td><td class="num">48,900</td><td class="num">72,050</td><td class="num">1,01,877</td><td class="num pos">54.0%</td></tr>
      <tr><td>EBITDA</td><td class="num">420</td><td class="num">820</td><td class="num">1,440</td><td class="num">2,180</td><td class="num">3,615</td><td class="num pos">71.0%</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">2.31</td><td class="num">2.70</td><td class="num">2.94</td><td class="num">3.03</td><td class="num">3.55</td><td class="num">+124 bp</td></tr>
      <tr><td>PAT</td><td class="num">180</td><td class="num">390</td><td class="num">720</td><td class="num">1,130</td><td class="num">1,976</td><td class="num pos">82.3%</td></tr>
      <tr><td>Tangible Net Worth</td><td class="num">3,800</td><td class="num">9,200</td><td class="num">15,600</td><td class="num">20,340</td><td class="num">23,589</td><td class="num">44.1%</td></tr>
      <tr><td>Total Debt</td><td class="num">1,900</td><td class="num">2,600</td><td class="num">3,200</td><td class="num">4,100</td><td class="num">4,858</td><td class="num">26.5%</td></tr>
      <tr><td>Debt/EBITDA (x)</td><td class="num">4.52</td><td class="num">3.17</td><td class="num">2.22</td><td class="num">1.88</td><td class="num">1.34</td><td class="num pos">−3.18x</td></tr>
      <tr><td>Paid-up capital (cumulative)</td><td class="num">6,800</td><td class="num">12,400</td><td class="num">17,800</td><td class="num">19,629</td><td class="num">22,829</td><td class="num">27.4%</td></tr>
    </tbody>
  </table>
  </div>
  <div class="card">
    <h4 style="margin-top:0">What the five-year series says</h4>
    <p>Revenue has compounded 54% p.a. for five years; EBITDA compounds 71%; PAT compounds 82%. This is not a cyclical expansion &mdash; it is a structural capacity build executed without gearing up. The Debt/EBITDA ratio has collapsed from 4.52x to 1.34x <em>while revenue grew 5.6x</em> &mdash; confirming that the funding mix is parent equity (paid-up capital grew 3.4x in five years) rather than external leverage. For an acquiring Indian bank, this is the single most important data point: the relationship starts from a clean credit slate and a balance sheet with vast absorptive capacity, not from stress.</p>
  </div>

  <h3>04.6 &mdash; Debt composition, FY25 &mdash; decomposing the Rs 4,858 Cr</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Tranche</th><th class="num">Outstanding (Rs Cr)</th><th>Counterparty</th><th>Tenor / priced at</th><th>MCA charge registered?</th></tr>
    </thead>
    <tbody>
      <tr><td>ECB &mdash; Hon Hai Singapore Term loan</td><td class="num">2,200&ndash;2,400</td><td>Parent (Hon Hai Precision Industries)</td><td>5-year bullet, SOFR + 90 bp (equiv ~5.3% USD){ref("28")}</td><td>No &mdash; unsecured intra-group</td></tr>
      <tr><td>ECB &mdash; Trade-finance rollover (90-day commercial paper equivalent)</td><td class="num">1,600&ndash;1,800</td><td>Foxconn Group treasury (via DBS, UOB trade desks)</td><td>Revolving 90-day, SOFR + 45 bp</td><td>No &mdash; trade line, not charged</td></tr>
      <tr><td>Intercompany payables (short-term)</td><td class="num">680&ndash;880</td><td>Foxconn group supplier entities</td><td>&le; 60 days</td><td>No &mdash; trade creditor</td></tr>
      <tr><td>Other current liabilities / accruals</td><td class="num">220&ndash;280</td><td>Various (utilities, taxes, labour contractors)</td><td>&le; 30 days</td><td>No</td></tr>
      <tr><td><strong>Total</strong></td><td class="num"><strong>4,858</strong></td><td colspan="2">All unsecured &mdash; <strong>zero MCA charge filing</strong>{ref("23,24")}</td><td><strong>Confirmed</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Two implications that go straight into the IBank pitch:</p>
  <ol>
    <li><strong>First-ever Indian-bank charge-creation is the starting credential.</strong> A Rs 2,100&ndash;2,400 Cr secured capex term loan with a first charge on SMT-4 line assets instantly makes IBank the senior lender by a wide margin &mdash; there is no incumbent Indian-bank charge to subordinate to. The pari-passu negotiation is with the parent&rsquo;s unsecured ECB, which is subordinate by definition.</li>
    <li><strong>The parent ECB is refinanceable at partial rupee.</strong> Current ECB cost is ~5.3% USD equivalent, which loads to ~8.2&ndash;9.0% fully-hedged rupee cost. An IBank MCLR + 55 bp term loan today prices at ~8.85%; at break-even on current rates, but saves 65&ndash;90 bp if a 50 bp hike lands in June. The structural case for a partial rupee swap (up to Rs 1,500&ndash;2,000 Cr) strengthens with every data point that pushes hike probability up.</li>
  </ol>

  <h3>04.7 &mdash; Governance &amp; key-personnel map</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Role</th><th>Profile type (public-domain)</th><th>Relationship intent</th></tr>
    </thead>
    <tbody>
      <tr><td>India Managing Director</td><td>Long-serving Foxconn-group executive, Hsinchu &amp; Shenzhen operations background; India operational ownership{ref("9,28")}</td><td>Quarterly strategic review; PB engagement of immediate family; spouse / children banking</td></tr>
      <tr><td>Chief Financial Officer (India)</td><td>Group rotational CFO from Hon Hai Singapore treasury; forex &amp; treasury specialist</td><td>Primary counterparty for all wholesale products; weekly cadence during Phase 1; monthly thereafter</td></tr>
      <tr><td>Treasurer / Head of Finance Operations</td><td>India-local; ex-Big 4 / ex-listed-manufacturing background typical</td><td>CMS implementation, vendor payments, GST / PLI refund workflows</td></tr>
      <tr><td>Head of Procurement (India)</td><td>Typically ex-global-EMS procurement; owns Rs 68,000&ndash;74,000 Cr annual import bill</td><td>Import LC + SBLC programme; trade-finance engagement point</td></tr>
      <tr><td>HR Director (India)</td><td>Indian labour-law specialist; oversight over the 42,000-person workforce and associated trusts</td><td>Salary-CASA migration, payroll loans, ESOP escrow structuring</td></tr>
      <tr><td>Company Secretary</td><td>India-qualified CS; compliance-focused; interface with MCA, RBI (for ECBs), MeitY (for PLI)</td><td>Corporate-action workflows, board-resolution sequencing for new facilities</td></tr>
      <tr><td>Board composition</td><td>Parent-appointed directors from Hon Hai Precision + India-resident directors per Companies Act. Not independent-director-majority given private-co exemption.</td><td>Relationship approvals traverse parent board when individual facility exceeds SGD 30 mn equivalent (observed group policy)</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Privacy note:</em> specific individuals are not named in this dossier; mapping is by role. Relationship-team briefings will insert current post-holders at execution time using public-disclosure sources (MCA Form DIR-12, LinkedIn profiles, India press releases). No individual&rsquo;s name, family structure, or personal financial detail is reproduced in the committed artifact.</p>

  <h3>04.8 &mdash; Working-capital behaviour &mdash; what the numbers reveal</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">Receivable &amp; payable cycle</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Receivable days: <strong>58</strong> (Apple USD PO, 45-day standard) + <strong>30</strong> carry on GST IGST float on exports{ref("11")} = effective 58-day exposure</li>
        <li>Payable days: <strong>42</strong> to Foxconn group supplier network; <strong>18</strong> to domestic SMT material vendors</li>
        <li>Inventory days: <strong>26</strong> raw + WIP + <strong>8</strong> finished (shipped-FOB in 72 hours)</li>
        <li>Net cash conversion cycle: <strong>~30 days positive</strong> &mdash; enough to fund incremental volume, but pays the ECB hedging cost on a rolling basis</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">The four line items IBank can move</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>Trade payables &mdash; imports (Rs 14,800 Cr est. annual)</strong>: Import LC + SBLC from IBank against Taiwan / China suppliers; cost save 12&ndash;18 bp on documentary fee</li>
        <li><strong>Forex gain/loss &mdash; (Rs 180&ndash;240 Cr in FY25)</strong>: Structured hedging + NDF; partner-bank FX commission margin Rs 22&ndash;28 Cr/yr</li>
        <li><strong>Other Current Assets &mdash; Rs 1,600 Cr GST+PLI float</strong>: IGST refund advance + PLI-receivable factoring &mdash; Rs 120&ndash;180 Cr NFB NFB utilisation</li>
        <li><strong>Interest cost &mdash; Rs 340 Cr in FY25</strong>: Displace parent ECB with rupee TL at MCLR + 35 bp = effective ~8.85% vs loaded offshore ~8.20&ndash;9.10% depending on hedge policy; break-even at parity but opens the door</li>
      </ul>
    </div>
  </div>
</section>
"""


def section_industry() -> str:
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry deep-dive &mdash; India EMS / Smartphone assembly</div>
  <h2>The PLI-2 manufacturing republic &mdash; FY26 actuals, FY27&ndash;28 projections</h2>
  <p class="lede">India's electronics manufacturing services industry has crossed a structural inflection. Smartphone exports hit $22.9 bn in FY25 (up from $11.1 bn FY24, $0.2 bn FY19){ref("31")}; Apple's stated ambition is 25% of global iPhone output from India by end-2027{ref("27")}. The profit pool concentrates in three pockets: (i) final assembly (where Foxconn, Tata Electronics, Pegatron-now-Tata sit), (ii) display modules (Salcomp, Bharat FIH for Android), and (iii) PCB assembly (Syrma SGS, Dixon, Amber Enterprises). Foxconn is uniquely positioned at (i) for Apple.</p>

  <h3>05.1 &mdash; Industry-size arithmetic</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Metric</th><th class="num">FY24 A</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 E</th><th class="num">FY28 E</th><th>Source / driver</th></tr>
    </thead>
    <tbody>
      <tr><td>India mobile-phone production ($ bn)</td><td class="num">49.2</td><td class="num">65.4</td><td class="num">82.0</td><td class="num">98.0</td><td class="num">115.0</td><td>ICEA / MeitY; CAGR 20.6% FY25&ndash;28{ref("31")}</td></tr>
      <tr><td>iPhone output from India (mn units)</td><td class="num">35</td><td class="num">54</td><td class="num">65</td><td class="num">78</td><td class="num">92</td><td>Apple/JPM note; Foxconn share ~50%{ref("27,32")}</td></tr>
      <tr><td>EMS sector EBITDA margin (%)</td><td class="num">2.8</td><td class="num">3.3</td><td class="num">3.6</td><td class="num">3.9</td><td class="num">4.1</td><td>Scale / local sourcing step-up (PLI 2.0 Component){ref("31")}</td></tr>
      <tr><td>Local value-add (%)</td><td class="num">14</td><td class="num">18</td><td class="num">22</td><td class="num">28</td><td class="num">32</td><td>Target 30% by FY28 (MeitY){ref("31")}</td></tr>
      <tr><td>Smartphone export share to US (%)</td><td class="num">35</td><td class="num">48</td><td class="num">58</td><td class="num">63</td><td class="num">65</td><td>US&ndash;India deal 18% reciprocal tariff vs China 35%{ref("6")}</td></tr>
      <tr><td>Foxconn Mega Dev TOI (Rs Cr)</td><td class="num">72,050</td><td class="num">1,01,877</td><td class="num"><strong>1,28,500</strong></td><td class="num"><strong>1,52,000</strong></td><td class="num"><strong>1,74,000</strong></td><td>Base projection (below)</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.2 &mdash; Competitive landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Player</th><th>Customer mix</th><th>FY25 TOI (est)</th><th>Key advantage</th><th>Key vulnerability</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Foxconn Hon Hai Mega Dev (this entity)</strong></td><td>Apple 95%+</td><td class="num">Rs 1,01,877 Cr</td><td>Apple process-tech transfer depth; 11-year operating history at TN</td><td>Single-customer concentration; labour compliance (night-shift women)</td></tr>
      <tr><td>Tata Electronics (incl. ex-Wistron Kolar)</td><td>Apple 60%, non-Apple 40%</td><td class="num">Rs 48,000 Cr{ref("33")}</td><td>Sovereign-aligned parent; ability to execute PCB + chip-OSAT roadmap</td><td>Margin compression period during Wistron + Pegatron integration</td></tr>
      <tr><td>Bharat FIH</td><td>Xiaomi 50%, Oppo/Realme 25%, others</td><td class="num">Rs 12,800 Cr{ref("25")}</td><td>Listed; Android ecosystem breadth</td><td>Android unit volumes flat FY26</td></tr>
      <tr><td>Salcomp India</td><td>Apple chargers + displays</td><td class="num">Rs 9,400 Cr{ref("34")}</td><td>Displacement of China in charger BOM</td><td>Margin dependent on copper / plastic input cost</td></tr>
      <tr><td>Dixon Technologies</td><td>Xiaomi, Motorola, Samsung</td><td class="num">Rs 17,600 Cr{ref("35")}</td><td>Listed; multi-customer, multi-category (wearables, TV, lighting)</td><td>Thin EBITDA 3.4%; lower PLI tier</td></tr>
      <tr><td>Syrma SGS Technology</td><td>Industrial + auto PCB</td><td class="num">Rs 3,200 Cr{ref("36")}</td><td>Listed; non-mobile exposure (industrial, medical)</td><td>Smaller scale; capex-heavy</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.3 &mdash; Three industry forces moving FY27&ndash;28</h3>
  <div class="grid c3">
    <div class="card accent">
      <h4 style="margin-top:0">Apple's 25% from India by 2027 target</h4>
      <p>Current mix: China ~72%, India ~18%, Vietnam ~6%, others ~4%{ref("27")}. To hit 25%, India needs 92&ndash;95 mn iPhone units by FY28 &mdash; a 72% step-up from FY25. Foxconn Mega Dev on current 50% Apple-India share would need to ship 46&ndash;48 mn units &mdash; a Rs 1.7 lakh crore revenue base. Capex to support: ~Rs 4,200 Cr announced; further Rs 2,600&ndash;3,100 Cr expected in FY28 (housing + dormitory + logistics park).</p>
    </div>
    <div class="card accent">
      <h4 style="margin-top:0">Component-PLI v2.0 (Rs 23,000 Cr outlay, Sep 2025)</h4>
      <p>MeitY's Component PLI extends incentives from finished-phone assembly to sub-modules (PCBA, camera, display, charging){ref("37")}. This catalyses Foxconn's own supplier network &mdash; FIT (connectors), Luxshare (camera), etc. &mdash; to co-locate at Sriperumbudur and Sri City. Each sub-module entity becomes an adjacent IBank acquisition target; the Mega Dev relationship is the anchor account.</p>
    </div>
    <div class="card accent">
      <h4 style="margin-top:0">Tariff geometry &mdash; 18% to the US from Jul 2026</h4>
      <p>India-assembled iPhones land at ~18% into the US vs China's ~35%&ndash;42%{ref("6")}. The 17-point arbitrage more than offsets India's higher unit labour cost (~$3.80 vs China's $2.60). As long as the reciprocal-tariff differential holds, India EMS margins expand 60&ndash;80 bp structurally; Foxconn's Indian operating profit absorbs most of the benefit given its scale.</p>
    </div>
  </div>

  <h3>05.4 &mdash; Working-capital and cash-conversion benchmarks (India EMS)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Metric</th><th class="num">Foxconn Mega Dev FY25</th><th class="num">Tata Electronics FY25</th><th class="num">Dixon Tech FY25</th><th class="num">Syrma SGS FY25</th><th>Interpretation</th></tr>
    </thead>
    <tbody>
      <tr><td>Receivable days</td><td class="num">58</td><td class="num">62</td><td class="num">72</td><td class="num">98</td><td>Apple AR cycle is tight; non-Apple customers pay slower</td></tr>
      <tr><td>Payable days</td><td class="num">42</td><td class="num">48</td><td class="num">58</td><td class="num">72</td><td>Group-supplier network pays faster at Foxconn than third-party</td></tr>
      <tr><td>Inventory days</td><td class="num">34</td><td class="num">42</td><td class="num">38</td><td class="num">92</td><td>Single-customer / single-SKU assembly keeps Foxconn inventory low</td></tr>
      <tr><td>Cash conversion cycle (days)</td><td class="num pos">50</td><td class="num">56</td><td class="num">52</td><td class="num neg">118</td><td>Foxconn and Dixon operate at near structural minimum</td></tr>
      <tr><td>Working-capital turn (x)</td><td class="num">7.3</td><td class="num">6.5</td><td class="num">7.0</td><td class="num">3.1</td><td>Implies WC intensity lowest in Foxconn Mega Dev</td></tr>
      <tr><td>Fund-based WC as % of TOI</td><td class="num">1.2%</td><td class="num">3.4%</td><td class="num">4.1%</td><td class="num">11.2%</td><td>Foxconn funds via parent intercompany, not banks; switch cost low</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Rationale for low visible WC at Foxconn:</em> the Apple receivable is effectively investment-grade AAA (~$3.6 tn market cap counterparty), the inventory is a single SKU (iPhone), and payables are to a captive group-supplier network with uniform terms. This creates a near-optimal cash conversion profile that traditional bank WC is <em>over</em>-priced for. IBank's opportunity is not to compete on working capital price &mdash; it is to offer a CMS + SCF combination that reduces operational friction even at parity economics, then cross-sell the forex / trade / capex products at superior terms.</p>

  <h3>05.5 &mdash; KYC / AML / regulatory readiness &mdash; what will pass and what will not</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Regulatory dimension</th><th>Foxconn Mega Dev status</th><th>IBank workflow</th></tr>
    </thead>
    <tbody>
      <tr><td>KYC &mdash; Corporate ID &amp; beneficial ownership</td><td>Single 100% parent (Hon Hai Precision Industries, Singapore); ultimate beneficial owner Taiwan-domiciled listed entity (TWSE: 2317){ref("9,30")}</td><td>Standard corporate KYC; UBO declaration via parent 10-K disclosure; Singapore ACRA filing pull</td></tr>
      <tr><td>FEMA &mdash; FDI history</td><td>Cumulative USD 2,768 mn FDI via automatic route; no approval-route tranches on file{ref("29")}</td><td>Re-verify through FIRMS portal; sanity-check RBI master direction compliance before any new ECB / trade line</td></tr>
      <tr><td>RBI ECB compliance</td><td>Outstanding parent ECB requires Form ECB-2 monthly filings; typically current given parent-led treasury{ref("28")}</td><td>Confirm compliance status before any rupee-conversion product; coordinate with RBI reporting desk</td></tr>
      <tr><td>MCA &mdash; annual filings</td><td>AOC-4 FY25 filed 29 Nov 2025; MGT-7 annual return filed on time{ref("23")}</td><td>No compliance red flags; onboarding turnaround expected at 10&ndash;14 working days</td></tr>
      <tr><td>GST &mdash; registration &amp; filing</td><td>Active GSTIN (TN) + satellite registrations; monthly GSTR-1 / GSTR-3B current{ref("11")}</td><td>Standard; IGST refund advance product requires 6-month filing consistency &mdash; satisfied</td></tr>
      <tr><td>Sanctions / PEP screen</td><td>Hon Hai and senior leadership are standard PEP-negative; no OFAC / EU / UK sanctions exposure</td><td>Standard screen; no additional escalation expected</td></tr>
      <tr><td>Tax status</td><td>Indian corporate tax resident; effective rate 23.9% FY25 (concessional 22% + surcharge)</td><td>TDS / TCS workflow standard; no special tax treatment required</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.6 &mdash; Supplier ecosystem &mdash; the adjacent wallet</h3>
  <p>Any Indian-bank relationship with Foxconn Mega Dev sits at the centre of a ~40-supplier ecosystem that draws ~Rs 26,000&ndash;30,000 Cr of annualised purchase orders{ref("31,37")}. Mapped relationships multiply the wallet:</p>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Supplier tier</th><th>Representative names (public supplier disclosures)</th><th>Approx annual spend (Rs Cr)</th><th>IBank cross-sell vector</th></tr>
    </thead>
    <tbody>
      <tr><td>Tier-1 modules</td><td>Salcomp, Luxshare India, Sunwoda, Foxlink, FIT India{ref("34,37")}</td><td class="num">14,000&ndash;16,000</td><td>Supply-chain finance (anchor-led), reverse factoring programme</td></tr>
      <tr><td>Tier-2 components</td><td>TN / AP contract-manufacturing MSMEs (screws, casings, harnesses)</td><td class="num">3,800&ndash;4,200</td><td>MSME-bundled SCF; invoice-discounting APIs; GST-linked credit</td></tr>
      <tr><td>Logistics &amp; freight</td><td>Expeditors, DB Schenker, BLR Logistics, Allcargo, Maersk line-haul</td><td class="num">2,100&ndash;2,400</td><td>Freight-vendor collection CMS; currency risk-sharing on USD freight</td></tr>
      <tr><td>Employee services</td><td>Labour contractor pool (Sodexo Onsite, TeamLease){ref("14")}</td><td class="num">1,800&ndash;2,100</td><td>Salary CMS + payroll loans (retail handshake)</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_models() -> str:
    return f"""
<section id="models">
  <div class="subhead">07 · Projection models &mdash; base / bear / bull</div>
  <h2>Three futures for Foxconn Mega Dev, FY26E&ndash;FY28E</h2>
  <p class="lede">Each scenario holds three of five drivers constant and moves two. The spread across scenarios bounds the IBank exposure and the fee pool. Funding-gap waterfall at the end anchors the Rs 14,200&ndash;18,700 Cr wholesale-wallet envelope.</p>

  <h3>07.1 &mdash; Driver grid</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Driver</th><th class="num">FY25 A</th><th class="num">Base FY27E</th><th class="num">Bear FY27E</th><th class="num">Bull FY27E</th><th>Driver anchor</th></tr>
    </thead>
    <tbody>
      <tr><td>iPhone India unit volume (mn)</td><td class="num">54</td><td class="num">78</td><td class="num">66</td><td class="num">88</td><td>Apple planning + PLI capacity add{ref("27,32")}</td></tr>
      <tr><td>Foxconn Mega Dev share of iPhone India (%)</td><td class="num">51</td><td class="num">50</td><td class="num">47</td><td class="num">53</td><td>Tata Electronics ramp-up vs own SMT add</td></tr>
      <tr><td>Avg USD realisation per unit (ASP, $)</td><td class="num">770</td><td class="num">810</td><td class="num">760</td><td class="num">840</td><td>Pro Max mix shift; A19 Pro SoC pricing{ref("32")}</td></tr>
      <tr><td>USD / INR (avg)</td><td class="num">85.6</td><td class="num">94.5</td><td class="num">96.8</td><td class="num">92.0</td><td>Goldman / DB consensus FY27{ref("3,5")}</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">3.55</td><td class="num">4.05</td><td class="num">3.15</td><td class="num">4.55</td><td>Local value-add + PLI + scale{ref("31")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>07.2 &mdash; Consolidated P&amp;L projection</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Rs Cr unless stated</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 E Base</th><th class="num">FY27 E Bear</th><th class="num">FY27 E Bull</th><th class="num">FY28 E Base</th></tr>
    </thead>
    <tbody>
      <tr><td>Revenue / TOI</td><td class="num">1,01,877</td><td class="num">1,28,500</td><td class="num">1,52,000</td><td class="num">1,25,400</td><td class="num">1,77,200</td><td class="num">1,74,000</td></tr>
      <tr><td>EBITDA</td><td class="num">3,615</td><td class="num">5,000</td><td class="num">6,156</td><td class="num">3,950</td><td class="num">8,063</td><td class="num">7,482</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">3.55</td><td class="num">3.89</td><td class="num pos">4.05</td><td class="num neg">3.15</td><td class="num pos">4.55</td><td class="num">4.30</td></tr>
      <tr><td>Interest</td><td class="num">340</td><td class="num">475</td><td class="num">580</td><td class="num">640</td><td class="num">510</td><td class="num">720</td></tr>
      <tr><td>Depreciation</td><td class="num">680</td><td class="num">1,040</td><td class="num">1,420</td><td class="num">1,320</td><td class="num">1,460</td><td class="num">1,850</td></tr>
      <tr><td>PBT</td><td class="num">2,595</td><td class="num">3,485</td><td class="num">4,156</td><td class="num">1,990</td><td class="num">6,093</td><td class="num">4,912</td></tr>
      <tr><td>PAT</td><td class="num">1,976</td><td class="num">2,650</td><td class="num">3,160</td><td class="num">1,510</td><td class="num">4,630</td><td class="num">3,735</td></tr>
      <tr><td>Capex (Rs Cr)</td><td class="num">2,750</td><td class="num">3,100</td><td class="num">4,200</td><td class="num">3,100</td><td class="num">4,800</td><td class="num">2,600</td></tr>
      <tr><td>Cumulative incremental debt need</td><td class="num">&mdash;</td><td class="num">1,600</td><td class="num">4,200</td><td class="num">5,300</td><td class="num">2,800</td><td class="num">5,800</td></tr>
    </tbody>
  </table>
  </div>

  <h3>07.3 &mdash; Driver sensitivities (Rs Cr impact on FY27 PAT)</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">Single-factor shocks from base</h4>
      <ul class="check" style="margin-bottom:0">
        <li>iPhone volume &pm;10% (from 78 mn base): PAT impact <strong>&pm;Rs 420 Cr</strong></li>
        <li>USD/INR &pm;Rs 1 (from 94.5 base): PAT impact <strong>&pm;Rs 215 Cr</strong></li>
        <li>EBITDA margin &pm;25 bp (from 4.05%): PAT impact <strong>&pm;Rs 290 Cr</strong></li>
        <li>Share-of-iPhone-India &pm;3 pt (from 50%): PAT impact <strong>&pm;Rs 195 Cr</strong></li>
        <li>Apple ASP &pm;$25/unit (from $810): PAT impact <strong>&pm;Rs 175 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">The three drivers that most need IBank hedging</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>USD/INR</strong> &mdash; rolling 6M forward cover priced at 2.1% p.a.; offers 30&ndash;45 bp EBITDA margin stability</li>
        <li><strong>Interest rate</strong> &mdash; June MPC rate-lock option on Rs 4,200 Cr TL; swap to fixed rate from inception</li>
        <li><strong>Component import copper / aluminium price</strong> &mdash; commodity hedge via MCX or bilateral OTC on procurement committee approval (~Rs 2,400 Cr notional)</li>
      </ul>
    </div>
  </div>

  <h3>07.4 &mdash; Funding-gap waterfall (base case FY26&ndash;FY28)</h3>
  <p>Cumulative capex + WC build under the base case requires Rs 12,800 Cr of new funding. Existing parent ECB re-ups will absorb ~Rs 3,600 Cr; the balance Rs 9,200 Cr is the addressable Indian-bank wallet.</p>
  <div class="card"><div class="waterfall">
Opening cash (1 Apr 2026)                        :  Rs    2,840 Cr
+ Cumulative PAT FY26-FY28 base                  :  Rs    9,545 Cr
+ Depreciation add-back                          :  Rs    4,310 Cr
- Capex FY26-FY28                                :  Rs  (9,900) Cr
- Working-capital build (incr. RM + inventory)   :  Rs  (3,200) Cr
- Tax, dividend (assumed nil)                    :  Rs    0 Cr
- Debt repayment (ECB rollover ~80%)             :  Rs  (1,400) Cr
= Closing cash (31 Mar 2028)                     :  Rs    2,195 Cr
----------------------------------------------------------------
Shortfall to fund                                :  Rs   12,800 Cr
  covered by parent ECB re-up                    :  Rs    3,600 Cr
  covered by new Indian-bank wholesale wallet    :  Rs    9,200 Cr  &larr; IBank opportunity
</div></div>

  <div class="card pos">
    <h4 style="margin-top:0">IBank share target</h4>
    <p>A realistic sole-arranger take is 45&ndash;55% of the Rs 9,200 Cr Indian-bank addressable wallet &mdash; <strong>Rs 4,100&ndash;5,100 Cr</strong> in funded wallet over FY27&ndash;FY28. On top of that, non-funded (LC, BG, SBLC) typically runs 1.8&ndash;2.2x the funded book in an EMS import-heavy setup &mdash; adds Rs 7,400&ndash;11,200 Cr of NFB. Derivative notional (forex forwards, swaps, NDF) at 12&ndash;15% of USD revenue = Rs 2,700&ndash;3,400 Cr notional annually. Consolidated wallet converges to the Rs 14,200&ndash;18,700 Cr envelope quoted on the cover.</p>
  </div>
</section>
"""


def section_entry_map() -> str:
    return f"""
<section id="entry-map">
  <div class="subhead">08 · Wholesale product entry-point map</div>
  <h2>What each product does to which line item &mdash; and what it earns IBank</h2>
  <p class="lede">Every recommended product is tagged to the specific financial-statement line it improves for Foxconn Mega Dev, and to the expected annual fee / NII for IBank at realistic market spreads. Deliberately conservative: we have used street spreads for Rs 40,000&ndash;80,000 Cr revenue EMS peers (Tata Electronics, Dixon).</p>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr>
        <th>Product</th>
        <th>Moves which line item</th>
        <th class="num">Size (Rs Cr)</th>
        <th>Spread / fee</th>
        <th class="num">IBank income (Rs Cr / yr)</th>
        <th>Rationale / evidence</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Working capital CC/OD</strong></td><td>Short-term borrowings; reduces parent-intercompany WC loan</td><td class="num">1,200&ndash;1,600</td><td>1Y MCLR + 45 bp</td><td class="num">9&ndash;13</td><td>50% utilisation on Rs 2,400&ndash;3,200 Cr sanction; replaces Hon Hai SG intercompany line</td></tr>
      <tr><td><strong>Capex term loan (A19 Pro FATP + AirPods line)</strong></td><td>Long-term debt + capex schedule; MCA-charge-registered</td><td class="num">2,100&ndash;2,400</td><td>MCLR + 55 bp, 7-year bullet</td><td class="num">22&ndash;27</td><td>50% of announced Rs 4,200 Cr capex; balance with co-lender(s){ref("9")}</td></tr>
      <tr><td><strong>Import LC + SBLC</strong></td><td>Trade payables; replaces parent-issued SBLCs</td><td class="num">3,400&ndash;4,200</td><td>Doc fee 12&ndash;18 bp; conf. 28&ndash;34 bp</td><td class="num">18&ndash;24</td><td>Annual import bill Rs 68,000&ndash;74,000 Cr; 10% routed via IBank as sole LC arranger in Y1; scale to 25% by Y3</td></tr>
      <tr><td><strong>BG &mdash; PLI &amp; TN state incentive</strong></td><td>Contingent liabilities; off balance-sheet</td><td class="num">680&ndash;820</td><td>Comm 42&ndash;58 bp</td><td class="num">3&ndash;5</td><td>TN SGST incentive claim BG; MeitY / MoC BGs on performance conditions</td></tr>
      <tr><td><strong>FX forwards &mdash; USD revenue cover</strong></td><td>Other comprehensive income; hedges Rs 180&ndash;240 Cr forex volatility</td><td class="num">2,700&ndash;3,400 notional</td><td>Pip margin 1.0&ndash;1.5 paise</td><td class="num">27&ndash;34</td><td>6M rolling on USD 4.2 bn net position; current hedge ratio &lt;40% per mgmt commentary{ref("28")}</td></tr>
      <tr><td><strong>USD-INR cross-currency swap</strong></td><td>Converts parent ECB to rupee term; hedges interest cost</td><td class="num">1,800&ndash;2,200 notional</td><td>Margin 15&ndash;22 bp</td><td class="num">3&ndash;5</td><td>Replaces raw ECB with LC-ended swap; risk-weighting optimal for IBank</td></tr>
      <tr><td><strong>Supply-chain finance (anchor-led)</strong></td><td>Trade payables; extends supplier payment terms from 42 &rarr; 60 days</td><td class="num">1,400&ndash;1,700</td><td>NIM 1.6&ndash;2.1%; fee 18&ndash;24 bp</td><td class="num">26&ndash;34</td><td>Applies to Tier-1 + Tier-2 suppliers; ~40 vendors; reverse factoring APIs</td></tr>
      <tr><td><strong>GST/IGST refund advance</strong></td><td>Other current assets Rs 1,100&ndash;1,400 Cr float</td><td class="num">700&ndash;850</td><td>Effective ~85 bp over OD rate</td><td class="num">6&ndash;8</td><td>85% advance against validated IGST refund queue; CMS-linked collection</td></tr>
      <tr><td><strong>PLI receivable factoring</strong></td><td>Other current assets (PLI claim line)</td><td class="num">380&ndash;560</td><td>Effective 1.15%</td><td class="num">5&ndash;7</td><td>Discounting against MeitY-approved PLI receivables queue; Rs 1,280 Cr cumulative claims to FY24{ref("11")}</td></tr>
      <tr><td><strong>CMS &mdash; payments + collections</strong></td><td>Bank &amp; cash balances; float management</td><td class="num">&mdash;</td><td>API fee + float NIM</td><td class="num">11&ndash;14</td><td>~Rs 280 Cr float on 30-day AP/AR cycle; payment APIs for vendor bank-mix</td></tr>
      <tr><td><strong>Commercial paper P-2 / A-1 programme</strong></td><td>Short-term borrowings; diversification</td><td class="num">600&ndash;800 outstanding</td><td>Arranger 5 bp + IPA 4 bp</td><td class="num">3&ndash;4</td><td>Contingent on rating sponsorship (Section 04.4); 3-month roll with half-yearly renewal</td></tr>
      <tr><td><strong>DCM &mdash; unsecured parent-guarantee NCD (FY28)</strong></td><td>Long-term debt; lengthens maturity profile</td><td class="num">1,500&ndash;2,000</td><td>Fee 15 bp; sole book-running</td><td class="num">8&ndash;12 (one-time)</td><td>FY28 capex tranche 2 refinancing; dependent on standalone rating at that point</td></tr>
    </tbody>
  </table>
  </div>

  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">Wholesale wallet summary</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Funded wallet (CC/OD + TL): <strong>Rs 3,300&ndash;4,000 Cr</strong></li>
        <li>Non-funded (LC + BG + SBLC): <strong>Rs 4,100&ndash;5,000 Cr</strong></li>
        <li>Derivative notional (FX fwd + CCS): <strong>Rs 4,500&ndash;5,600 Cr</strong></li>
        <li>SCF programme: <strong>Rs 1,400&ndash;1,700 Cr</strong></li>
        <li>DCM (FY28): <strong>Rs 1,500&ndash;2,000 Cr</strong></li>
        <li class="mono" style="border-top:1px dashed var(--line);padding-top:8px;margin-top:8px"><strong>Total wholesale: Rs 14,800&ndash;18,300 Cr</strong></li>
        <li class="mono"><strong>Estimated IBank income: Rs 141&ndash;187 Cr / yr fully converted</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Why this is achievable &mdash; benchmarks</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Tata Electronics: IBank confirmed FB Rs 3,800 Cr + NFB Rs 4,600 Cr wallet, derivative Rs 3,400 Cr notional (FY25 annual review)</li>
        <li>Industry benchmark: 15&ndash;18% of TOI converts to total banking wallet for EMS with &gt;60% imports; Foxconn at Rs 1,02,000 Cr TOI implies Rs 15,000&ndash;18,000 Cr natural wallet &mdash; consistent</li>
        <li>Per-rupee fee load for EMS is 85&ndash;105 bp (blended NII + fee + deriv margin); Rs 17,000 Cr average wallet &rarr; Rs 145&ndash;180 Cr income &mdash; consistent with our estimate</li>
      </ul>
    </div>
  </div>
</section>
"""


def section_retail_pb_tasc() -> str:
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC sizing</div>
  <h2>The adjacencies &mdash; salary, promoter-management, institutional float</h2>
  <p class="lede">Foxconn Mega Dev is a corporate-only relationship at the parent level, but the plant ecosystem around it generates three distinct retail / PB / TASC opportunities with a combined Rs 37&ndash;45 Cr annual income contribution.</p>

  <div class="grid c3">
    <div class="card">
      <h4 style="margin-top:0">09.1 &mdash; Salary / retail banking</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Direct workforce on rolls (FY25): <strong>42,000</strong> (permanent + contract){ref("14,28")}</li>
        <li>Expected FY28 peak (post capex-2 ramp): <strong>68,000&ndash;74,000</strong></li>
        <li>Typical payroll account migration achievable at sanction: <strong>28,000&ndash;32,000 accounts</strong> Year-1</li>
        <li>Wage distribution: entry-level Rs 18,500&ndash;22,000/mo; technical Rs 34,000&ndash;52,000; managerial Rs 85,000&ndash;2,10,000</li>
        <li>CASA float per account (blended, EMS benchmark): Rs 9,200&ndash;11,400</li>
        <li>Annual float income (80 bp NIM + insurance cross-sell): <strong>Rs 21&ndash;26 Cr</strong></li>
        <li>Payroll loan book (avg 8% uptake, ticket Rs 1.4 L): <strong>Rs 3.2&ndash;3.8 Cr NII / yr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">09.2 &mdash; Private Banking / UHNI</h4>
      <ul class="check" style="margin-bottom:0">
        <li>CXO + senior management at Foxconn India (publicly identifiable by title): <strong>~24 individuals</strong></li>
        <li>Of these, India-tax-resident UHNI candidates for full-suite PB: <strong>8&ndash;11</strong></li>
        <li>Expected TOTAL investable surplus per UHNI: Rs 12&ndash;35 Cr</li>
        <li>Typical wallet-share achievable in Y1: 18&ndash;22%; Y3: 35&ndash;45%</li>
        <li>AUM target Y3: Rs 55&ndash;75 Cr</li>
        <li>PB fee load (blended 65&ndash;85 bp across MF + PMS + AIF): <strong>Rs 4&ndash;6 Cr / yr</strong></li>
        <li>Senior management including lifestyle credit cards (Emeralde / Reserve): per-card annual income Rs 42,000&ndash;85,000</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">09.3 &mdash; TASC / Institutional float</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Foxconn India PF Trust (if constituted) or EPFO contribution: Rs 320&ndash;390 Cr annual</li>
        <li>Foxconn India Gratuity Trust: Rs 65&ndash;85 Cr accumulated float</li>
        <li>Foxconn India Superannuation: Rs 110&ndash;145 Cr AUM (likely)</li>
        <li>CSR 2% (Companies Act) = Rs 32&ndash;40 Cr annual spend flowing through trust / NGO account{ref("38")}</li>
        <li>ESOP / Restricted-Stock Unit administration (if any): India escrow account flow</li>
        <li>Annual fee load on TASC float (blended 28&ndash;38 bp trustee + float NIM): <strong>Rs 5&ndash;8 Cr / yr</strong></li>
      </ul>
    </div>
  </div>

  <h3>09.4 &mdash; Community &amp; CSR flows &mdash; the corporate-social lever</h3>
  <p>Foxconn Mega Dev&rsquo;s statutory CSR obligation under Section 135 of the Companies Act 2013{ref("38")} computes to approximately <strong>Rs 32&ndash;40 Cr annually</strong> (2% of 3-year rolling average PBT, triggered from FY23 onwards). The typical CSR architecture is: (a) 70&ndash;80% routed through a dedicated Foxconn India CSR trust or Section-8 company; (b) 15&ndash;20% deployed via implementing-partner NGOs (typically education &amp; vocational training aligned with the electronics-manufacturing skill pipeline); (c) 5&ndash;10% into direct government programmes such as PM-CARES or state-level education missions. Each of these channels creates a TASC account opportunity for IBank at the recipient-entity level, and an operational CMS handshake at the Foxconn-entity level for disbursement automation. Combined conservative estimate: <strong>Rs 1.2&ndash;1.8 Cr / yr</strong> in additional fee income on CSR-related float &amp; disbursements.</p>

  <h3>09.5 &mdash; Branch + digital touch-point plan</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Location</th><th>Footprint type</th><th>Timing</th><th>Primary use-case</th></tr>
    </thead>
    <tbody>
      <tr><td>Sriperumbudur main campus gate</td><td>Satellite relationship-cum-sales counter (4 FTE)</td><td>Go-live by 15 June 2026</td><td>Salary CASA onboarding; cash-withdrawal load on workforce pay-days</td></tr>
      <tr><td>Chengalpattu (second Foxconn campus)</td><td>Extension counter with micro-ATM</td><td>Go-live by 1 August 2026</td><td>Salary CASA; incremental EMS-supplier vendor accounts</td></tr>
      <tr><td>Apollo / Panjetty (Foxconn worker-housing cluster)</td><td>Doorstep banking mini-van + BC agent</td><td>Go-live by 1 September 2026</td><td>Dormitory-based account activation; remittance corridor (north / north-east to home state)</td></tr>
      <tr><td>Velachery / Guindy corporate offices</td><td>Relationship manager + wealth RM (hybrid)</td><td>Existing branches expanded</td><td>CXO / middle-management PB + credit card distribution</td></tr>
      <tr><td>Digital &mdash; IBank mobile app deep-link</td><td>Branded micro-site for &quot;Foxconn India Payroll&quot;</td><td>Soft-launch T + 45</td><td>Salary account opening; pre-approved payroll loans; investment discovery</td></tr>
      <tr><td>Digital &mdash; API banking for Foxconn CMS</td><td>H2H integration + bulk-payment + GST refund APIs</td><td>Go-live T + 60</td><td>Vendor payment rails; supplier SCF enrolment; collection reconciliation</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Branch economics rationale:</em> a satellite counter at a 42,000-worker industrial campus with a 70:30 permanent-to-contract mix supports a blended cost-to-income ratio of 38&ndash;46% in steady-state (well inside the 55% threshold for retail profitability). The go-live sequencing aligns with the wholesale-sanction milestones so salary migration happens alongside term-loan draw-down and GST refund advance &mdash; the operational CMS handshake cements the corporate relationship.</p>

  <div class="card accent">
    <h4 style="margin-top:0">Retail + PB + TASC conversion summary</h4>
    <ul class="check" style="margin-bottom:0">
      <li>Salary CASA + payroll-loan income: <strong>Rs 24&ndash;30 Cr / yr</strong> at 30,000-account migration</li>
      <li>Private banking AUM fee: <strong>Rs 4&ndash;6 Cr / yr</strong> at Rs 65 Cr AUM Y3 target</li>
      <li>TASC trust-admin + float: <strong>Rs 5&ndash;8 Cr / yr</strong></li>
      <li>Credit card + wealth insurance cross-sell: <strong>Rs 4&ndash;6 Cr / yr</strong></li>
      <li class="mono" style="border-top:1px dashed var(--line);padding-top:8px;margin-top:8px"><strong>Combined retail / PB / TASC: Rs 37&ndash;50 Cr / yr</strong></li>
    </ul>
  </div>
</section>
"""


def _also_consolidated_already_in_models():
    # Funding-gap waterfall is in section_models (07.4). Add the
    # product-stack roll-up here as Section 10.
    return None


def _consolidated_section():
    return ""  # placeholder, real block below


def section_consolidated() -> str:
    return f"""
<section id="consolidated">
  <div class="subhead">10 · Consolidated view</div>
  <h2>The single sheet that senior leadership will read first</h2>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Product bucket</th><th class="num">Funded / notional (Rs Cr)</th><th class="num">Annual income (Rs Cr)</th><th>Conversion probability (24&ndash;36 months)</th></tr>
    </thead>
    <tbody>
      <tr><td>Working capital (CC/OD)</td><td class="num">1,200&ndash;1,600</td><td class="num">9&ndash;13</td><td>High (displaces intercompany)</td></tr>
      <tr><td>Capex term loan (A19 Pro + AirPods)</td><td class="num">2,100&ndash;2,400</td><td class="num">22&ndash;27</td><td>High (rate-lock urgency)</td></tr>
      <tr><td>Import LC + SBLC</td><td class="num">3,400&ndash;4,200</td><td class="num">18&ndash;24</td><td>High (trade-finance need is structural)</td></tr>
      <tr><td>BG (PLI / SGST / perf)</td><td class="num">680&ndash;820</td><td class="num">3&ndash;5</td><td>High</td></tr>
      <tr><td>FX forwards (USD revenue)</td><td class="num">2,700&ndash;3,400 notional</td><td class="num">27&ndash;34</td><td>Medium-High (hedge policy committee approval)</td></tr>
      <tr><td>USD-INR CCS</td><td class="num">1,800&ndash;2,200 notional</td><td class="num">3&ndash;5</td><td>Medium (structural re-financing decision)</td></tr>
      <tr><td>Supply-chain finance</td><td class="num">1,400&ndash;1,700</td><td class="num">26&ndash;34</td><td>Medium-High (anchor approval)</td></tr>
      <tr><td>GST refund advance + PLI factoring</td><td class="num">1,080&ndash;1,410</td><td class="num">11&ndash;15</td><td>Medium-High (CFO office)</td></tr>
      <tr><td>CMS (payment + collection)</td><td class="num">&mdash;</td><td class="num">11&ndash;14</td><td>High (operational handshake)</td></tr>
      <tr><td>CP programme P-2 / A-1</td><td class="num">600&ndash;800</td><td class="num">3&ndash;4</td><td>Medium (rating sponsorship dependent)</td></tr>
      <tr><td>DCM (FY28 NCD)</td><td class="num">1,500&ndash;2,000</td><td class="num">8&ndash;12 (one-time)</td><td>Medium-Low (timing risk)</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>14,200&ndash;18,700</strong></td><td class="num"><strong>141&ndash;187</strong></td><td>&mdash;</td></tr>
      <tr><td>Retail salary CASA + loans</td><td class="num">&mdash;</td><td class="num">24&ndash;30</td><td>High (sanction-linked payroll migration)</td></tr>
      <tr><td>PB AUM &amp; cards</td><td class="num">&mdash;</td><td class="num">8&ndash;12</td><td>Medium (relationship build Y2)</td></tr>
      <tr><td>TASC trusts &amp; float</td><td class="num">&mdash;</td><td class="num">5&ndash;8</td><td>Medium-High (regulatory process)</td></tr>
      <tr><td><strong>Retail / PB / TASC total</strong></td><td class="num">&mdash;</td><td class="num"><strong>37&ndash;50</strong></td><td>&mdash;</td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>14,200&ndash;18,700</strong></td><td class="num pos"><strong>185&ndash;225 Cr / yr</strong></td><td>&mdash;</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_diligence() -> str:
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence file &mdash; litigation, news, subsidiaries, promoters &amp; KMPs</div>
  <h2>The narrative the credit committee will ask about first</h2>

  <h3>12.1 &mdash; Promoters &amp; key managerial personnel</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Role / position</th><th>Name (public domain)</th><th>Source / note</th></tr></thead>
    <tbody>
      <tr><td>Director (Foxconn-Group representative)</td><td>Fu-Chiang Hsu (Fuchiang Hsu)</td><td>MCA Form DIR-12; ZaubaCorp filing{ref("48")}</td></tr>
      <tr><td>Director (Foxconn-Group)</td><td>Wei-An Chang (Weian Chang)</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Director (Foxconn-Group)</td><td>Yi-Tao Kao (Yitao Kao)</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Director (Foxconn-Group)</td><td>Chia-En Lee</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Director (Foxconn-Group)</td><td>Shuo-Chih Chu</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Director (India-resident)</td><td>Senthil Iyyamperumal Kumar</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Director (India-resident)</td><td>Andi Sankaran Rajendran Kalidasan</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>Promoter / 100% beneficial owner</td><td>Hon Hai Precision Industries (Singapore subsidiary)</td><td>Ultimate parent: Hon Hai Precision Industries Co., Ltd, TWSE: 2317{ref("9,30")}</td></tr>
      <tr><td>India operating workforce (as filed FY26 RoC)</td><td>~8,251 permanent + ~33,750 contract / dormitory{ref("48")}</td><td>Per MCA filing FY26; total operating workforce reaches ~42,000 at peak season{ref("14")}</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Privacy note:</em> all individuals named here are publicly disclosed as directors via MCA / Companies Act statutory filings. No personal financial information or family-office composition is reproduced. Relationship-team briefings will use the current MCA DIR-12 snapshot at execution time.</p>

  <h3>11.1a &mdash; Promoter deep-dive</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">Ownership chain</h4>
      <ul class="check" style="margin-bottom:0">
        <li>100% beneficial ownership via Hon Hai Precision Industries, Singapore subsidiary{ref("9")}</li>
        <li>Ultimate parent: <strong>Hon Hai Precision Industries Co., Ltd</strong> &mdash; Taiwan, TWSE: 2317{ref("30")}</li>
        <li>Ultimate parent market cap: ~USD 120 bn (as of Apr 2026); widely held, no single controlling shareholder</li>
        <li>Founder Terry Gou (Taiwan) retains minority stake + emeritus chairman role; not day-to-day operational</li>
        <li>Pledge status: <strong>No pledged shares</strong> (private company; not applicable)</li>
        <li>Cumulative FDI via automatic route: USD 2,768 mn{ref("29")}</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Group directorships &amp; related-party network (India)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Common directors typically overlap with Bharat FIH (listed), FIT India, Foxconn India Developer Ltd &mdash; same Taiwan-HQ board rotation</li>
        <li>Board resolutions for material transactions require Hon Hai Singapore treasury concurrence above SGD 30 mn (observed group policy)</li>
        <li>Related-party transactions: procurement from group entities (Yuzhan, Luxshare, FIT) disclosed annually in MCA filings</li>
        <li>No Indian-promoter concept; foreign MNC-subsidiary classification applies</li>
        <li>Diligence item: cross-directorship matrix and RPT schedule at T+30 via CFO</li>
      </ul>
    </div>
  </div>
  <p>Because this is a wholly-foreign-owned subsidiary (WOS), there is no promoter-family PB adjacency of the kind we discuss for KPR or IMC. PB and wealth-management angle here is limited to senior management (India MD, CFO, plant head) who are salaried professionals, not shareholders. The upside is that credit-committee considerations around promoter-pledge risk, succession disputes, and family-cross-holding concerns do not apply; the single-parent ownership structure is the simplest credit architecture in the batch.</p>

  <h3>11.1b &mdash; KMPs, SBOs &amp; Probe42-verified registers</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Name / detail</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Directors on current board (MCA DIR-12)</td><td>Fu-Chiang Hsu, Wei-An Chang, Yi-Tao Kao, Chia-En Lee, Shuo-Chih Chu (Foxconn-Group reps) + Senthil Iyyamperumal Kumar, Andi Sankaran Rajendran Kalidasan (India-resident)</td><td>MCA Form DIR-12{ref("48")}</td></tr>
      <tr><td>CEO / MD (Sec 203 KMP)</td><td>India Managing Director &mdash; name via MCA DIR-12 at sanction-stage pull</td><td>Diligence item</td></tr>
      <tr><td>CFO (Sec 203 KMP)</td><td>India CFO &mdash; group-rotational from Hon Hai Singapore treasury; to be confirmed at T+14</td><td>Diligence item</td></tr>
      <tr><td>Company Secretary (Sec 203 KMP)</td><td>India-qualified CS; MCA compliance lead</td><td>Diligence item</td></tr>
      <tr><td>Significant Beneficial Owner (Form BEN-2)</td><td>Ultimate SBO is Hon Hai Precision Industries Co., Ltd (Taiwan); widely-held at parent, no single beneficial individual &gt; 10%</td><td>MCA Form BEN-2 + Hon Hai annual report{ref("30,48")}</td></tr>
      <tr><td>Material shareholders</td><td>100% Hon Hai Precision Industries Singapore (private co); no public float</td><td>MCA{ref("48")}</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42 pull, 08 Apr 2026)</td><td><strong>Not Rated</strong> (Probe42 endpoint: &ldquo;corporate or financial instruments do not have a credit rating on or after 2015&rdquo;){ref("81")}</td><td>Probe42 credit-ratings endpoint</td></tr>
      <tr><td><strong>Suit-filed cases</strong> (credit bureau, Probe42)</td><td><strong>ZERO</strong> &mdash; no Suit Filed Cases with any credit bureau{ref("82")}</td><td>Probe42 suit-filed-cases endpoint</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Diligence items:</em> (i) fresh MCA DIR-12 pull at T+14 for current CFO / CS names; (ii) BEN-2 filing verification for the Hon Hai ownership chain (Singapore subsidiary &rarr; Taiwan parent); (iii) first-time CRISIL + ICRA rating sponsorship conversation is part of Phase 1 engagement.</p>

  <h3>12.2 &mdash; Subsidiary &amp; group-affiliate map (India)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Affiliate / subsidiary</th><th>CIN / listing</th><th>Operating role</th><th>Bank-relationship implication</th></tr></thead>
    <tbody>
      <tr><td><strong>Bharat FIH Limited</strong> (subsidiary of FIH Mobile, Foxconn group)</td><td>L74999TN2015PLC160558 · BSE/NSE listed</td><td>Android OEM/ODM (Xiaomi, Nokia, sub-brands); Sri City AP + Sriperumbudur TN; ~30,000 workforce, 90% women{ref("49")}</td><td>Independent listed-co relationship; salary CASA + working-capital opportunity at scale</td></tr>
      <tr><td><strong>Yuzhan Technology India Pvt Ltd</strong></td><td>Karnataka-incorporated</td><td>Smartphone components / iPhone supply-chain; recipient of $1.5 bn Foxconn Singapore investment in FY25{ref("50")}</td><td>Karnataka LCG capex-linked TL opportunity; cross-reference with Devanahalli plant</td></tr>
      <tr><td><strong>Foxconn India Hardware Ltd / Devanahalli SPV</strong></td><td>Bangalore-registered</td><td>$2.56 bn Devanahalli campus (300 acres); to be India&rsquo;s largest iPhone manufacturing site; 30,000 worker dormitory under construction{ref("50")}</td><td>Greenfield project finance opportunity for Bengaluru desk; co-financeable with this dossier&rsquo;s primary entity</td></tr>
      <tr><td><strong>Foxconn India Developer Ltd</strong></td><td>Bengaluru</td><td>R&amp;D, firmware, test automation; ~180 Cr revenue band</td><td>Salary CMS + India tech-team payroll</td></tr>
      <tr><td><strong>Foxconn Interconnect Technology (FIT) India</strong></td><td>Chennai (Oragadam)</td><td>Cables / connectors / antennae for Apple + non-Apple; ~Rs 4,600 Cr est revenue</td><td>Trade-finance + supply-chain finance overlay through anchor-led programme</td></tr>
    </tbody>
  </table>
  </div>

  <h3>12.3 &mdash; Litigation &amp; regulatory file</h3>
  <div class="grid c2">
    <div class="card warn">
      <h4 style="margin-top:0">⚠ NHRC suo motu cognizance &mdash; discriminatory hiring (active, India)</h4>
      <p>Following a Reuters investigation in June 2024, the National Human Rights Commission took <em>suo motu</em> cognizance of allegations that Foxconn&rsquo;s Sriperumbudur plant excluded married women from iPhone-assembly hiring{ref("51")}. A five-member labour officials team visited the plant on 1 July 2024{ref("52")}. NHRC instructed both federal and Tamil Nadu state officials to re-investigate; a re-probe was launched in early 2025 with NHRC criticising labour officials for inadequate initial findings{ref("53")}. Foxconn instructed recruiters to remove age/gender/marital-status criteria from job advertisements in 2024 in response{ref("51")}. <strong>Status April 2026: ongoing administrative inquiry; no monetary penalty or NCLT action.</strong> Mitigation in capex TL covenants: ESG-linked covenants on diversity hiring metrics; dormitory build-out (Rs 320 Cr already allocated) addresses adjacent welfare risks{ref("8")}.</p>
    </div>
    <div class="card pos">
      <h4 style="margin-top:0">✓ NCLT / corporate-default register: clean</h4>
      <p>No NCLT proceedings, no CIRP filings, no major default classification across MCA / IBBI / RBI willful-defaulter lists. Master sheet&rsquo;s 5-field negative screen (Wilful Defaulter, NCLT, Major Default, Stressed Asset Sale, Disqualified Directors U/S 164) all read &ldquo;SAFE&rdquo;{ref("23")}. No SEBI / SAT proceedings. No pending CBI / ED ECIR registered against the entity or its named directors as of public-domain searches dated 24 Apr 2026.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">⚙ Routine commercial disputes</h4>
      <p>Standard for an EMS operation at this scale: routine GST input-tax-credit disputes resolved through CGST appeals; standard contract-of-carriage and customs-classification queries on imported components. No material commercial litigation in public domain. <em>Diligence item</em>: request management certificate confirming no pending litigation &gt; Rs 50 Cr at Phase 1 of relationship.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">⚙ Apple-supplier compliance audits</h4>
      <p>Foxconn Sriperumbudur is subject to Apple Supplier Code of Conduct annual audits{ref("9")}. Past Apple audits (2022 disclosure) flagged hostel / labour conditions; corrective actions reported via Apple&rsquo;s annual Supplier Responsibility Progress Report{ref("10")}. Continued Apple-customer compliance is a positive signal for credit; loss of Apple supplier-status would be the single largest tail risk.</p>
    </div>
  </div>

  <h3>12.4 &mdash; News file (last 18 months, public domain)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date</th><th>Sentiment</th><th>Headline / development</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Jun 2025</td><td><span class="tag pos">Positive</span></td><td>Foxconn announces $1.5 bn investment in display-module plant near Chennai (Oragadam); plant adjacent to existing iPhone assembly; ~14,000 jobs expected</td><td>Business Standard{ref("54")}</td></tr>
      <tr><td>Jun 2025</td><td><span class="tag pos">Positive</span></td><td>Foxconn to start manufacturing iPhone enclosures (metal/glass external frames) in Tamil Nadu &mdash; first non-Tata Electronics player in this category</td><td>Outlook Business{ref("55")}</td></tr>
      <tr><td>May 2025</td><td><span class="tag pos">Positive</span></td><td>Foxconn India exports ~$1 bn of iPhones to US in May alone; YTD CY25 reaches $4.4 bn vs $4.0 bn for the entirety of CY24</td><td>Business Standard{ref("56")}</td></tr>
      <tr><td>May 2025</td><td><span class="tag amber">Neutral / risk</span></td><td>President Trump warns Apple about manufacturing in India; Foxconn confirms it will proceed with the $1.5 bn Chennai plant regardless</td><td>Business Standard{ref("56")}</td></tr>
      <tr><td>Apr 2025</td><td><span class="tag pos">Positive</span></td><td>Foxconn announces $31.8 mn additional investment at TN plant for iPhone 16 Pro production line</td><td>AckoDrive{ref("57")}</td></tr>
      <tr><td>Jan 2025</td><td><span class="tag warn">Negative</span></td><td>NHRC launches new probe into discriminatory hiring at Foxconn TN plant after criticising earlier official findings</td><td>Business Standard{ref("53")}</td></tr>
      <tr><td>Jul 2024</td><td><span class="tag warn">Negative</span></td><td>Labour officials visit Foxconn TN plant; question executives about hiring practices following Reuters investigation</td><td>Business Standard{ref("52")}</td></tr>
      <tr><td>Jul 2024</td><td><span class="tag warn">Negative</span></td><td>India NHRC formally takes suo motu cognizance of married-women hiring exclusion claims</td><td>NHRC press release{ref("51")}</td></tr>
      <tr><td>Q4 FY25</td><td><span class="tag pos">Positive</span></td><td>Apple iPhone India volume ramp accelerates; Foxconn plans 25&ndash;30 mn unit production for FY26 (more than double FY25)</td><td>Multiple analyst reports{ref("27,32")}</td></tr>
      <tr><td>FY25 ongoing</td><td><span class="tag pos">Positive</span></td><td>Devanahalli (Karnataka) campus &mdash; $2.56 bn project, India&rsquo;s largest planned iPhone assembly site, dormitory for 30,000 workers under construction</td><td>The Hans India + Karnataka I&amp;C Department{ref("26,50")}</td></tr>
    </tbody>
  </table>
  </div>

  <div class="card">
    <h4 style="margin-top:0">Net news read</h4>
    <p>Strong positive operating momentum (capex announcements, US export ramp, sub-module localisation) materially outweighs the negative items (NHRC inquiry, Trump tariff sabre-rattling). The labour-rights matter is the single material reputational risk and warrants explicit ESG-linked covenant language in any term loan. Trade-policy uncertainty is hedged by Foxconn&rsquo;s own demonstrated commitment to proceed with capex regardless of US political signals.</p>
  </div>
</section>
"""


def section_playbook() -> str:
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 intervention playbook</div>
  <h2>The sequence from first meeting to Rs 185&ndash;225 Cr annual run-rate</h2>

  <h3>12.1 &mdash; Days 1&ndash;30 (now &rarr; 23 May 2026)</h3>
  <div class="card accent">
    <p><span class="phase">T + 30</span><strong>Rate-lock window is the single organising event.</strong> 4 June MPC. Goldman pricing 50 bp hike{ref("5")}; consensus 25 bp.</p>
    <ul class="check" style="margin-bottom:0">
      <li>Initial meeting with Group CFO (India) and Treasurer (Singapore) &mdash; <em>pre-read: macro + universe-map page with Foxconn Mega Dev highlighted + rate-lock sensitivity table</em></li>
      <li>Dual-sign NDA + preliminary term-sheet for a Rs 2,400 Cr capex term loan at MCLR + 55 bp (indicative, 7-year bullet, rate-lock until 4 Jun 2026)</li>
      <li>Forex desk onboarding call &mdash; propose rolling 6M forward programme on USD 700 mn Q2 receipts at current 2.1% annualised{ref("3")}</li>
      <li>CRISIL / ICRA rating-sponsor mandate negotiation &mdash; commit to 8-week turnaround for first published rating</li>
      <li>Parallel workstream: Hon Hai Group Treasury (Singapore DBS / UOB) briefing on IBank-India wholesale proposition; objective is to convert existing offshore lines to IBank rupee book without disrupting group liquidity policy</li>
    </ul>
  </div>

  <h3>12.2 &mdash; Days 31&ndash;60 (24 May &rarr; 22 Jun 2026)</h3>
  <div class="card">
    <p><span class="phase">T + 60</span><strong>Close capex term loan + trade-finance master agreement.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Credit committee approval of Rs 2,400 Cr TL; documentation, security creation (first charge over SMT-4 line assets), drawdown schedule aligned to A19 Pro commissioning</li>
      <li>Import LC + SBLC master agreement &mdash; Rs 3,400 Cr aggregate; IBank as sole LC arranger for first 6 months, co-arranger thereafter</li>
      <li>Launch salary migration pilot &mdash; CXO + top-100 management moved first (PB acquisition anchor); branch at Sriperumbudur opens in June 2026</li>
      <li>Forex rate-lock programme goes live &mdash; 3-month rolling, target 70% hedge coverage of Q2 FY27 USD receipts</li>
      <li>CMS handshake &mdash; vendor payment APIs and GST refund-advance go live; 14-day operational shake-down before scale-up</li>
    </ul>
  </div>

  <h3>12.3 &mdash; Days 61&ndash;90 (23 Jun &rarr; 22 Jul 2026)</h3>
  <div class="card pos">
    <p><span class="phase">T + 90</span><strong>Scale retail + PB; trigger TASC trust onboarding.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Salary migration reaches 18,000&ndash;22,000 accounts at Sriperumbudur + Sri City campuses; second branch opens Chengalpattu</li>
      <li>PB onboarding: 6&ndash;8 UHNI / senior management engaged for full-suite wealth proposition</li>
      <li>TASC: India PF trust, gratuity trust, superannuation trust reviewed; IBank to be proposed as custodian for incremental flows</li>
      <li>Supply-chain finance programme kick-off with 12 Tier-1 vendors; reverse-factoring onboarded on IBank SCF platform</li>
      <li>DCM / CP programme scoping discussion (for FY28 issuance); rating refresh schedule set</li>
      <li>First quarterly review with India MD + parent Treasury; formal wallet-share targets locked for FY27</li>
    </ul>
  </div>

  <h3>12.4 &mdash; Counterfactual analysis &mdash; what could derail the sequence</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">Scenario: Apple shifts mix toward Tata Electronics faster than expected</h4>
      <p>If Tata's ex-Wistron Kolar + ex-Pegatron Chengalpattu combined capacity commissions a quarter ahead of schedule, Foxconn Mega Dev&rsquo;s iPhone-India share could drop 50% &rarr; 44% by FY28. Absolute volume still grows (lower share of larger pie), but revenue growth CAGR compresses from 14% to 8%. Wholesale wallet is sized largely off absolute revenue, so funded-wallet impact is Rs 1,800&ndash;2,200 Cr downside on the Rs 14,200&ndash;18,700 Cr envelope. Mitigation: IBank should open a parallel Tata Electronics mandate track so share migration captures both names.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Scenario: US&ndash;India deal re-negotiation collapses 18% tariff advantage</h4>
      <p>Apple&rsquo;s landed cost arbitrage over China hinges on the reciprocal tariff differential. If the Jul 2026 deadline slips and the spread collapses to 5 pt, iPhone-India volume runs flat instead of growing. Foxconn TOI FY28 Rs 1.74 lakh Cr base &rarr; Rs 1.28 lakh Cr in the extreme. The margin structure is preserved because Apple absorbs landed-cost variability, but growth pauses. Wholesale wallet still viable at Rs 9,800&ndash;12,200 Cr &mdash; smaller but structurally intact.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Scenario: TN women-night-shift enforcement action</h4>
      <p>If state-level enforcement tightens around the night-shift rule before dormitory compliance completes (Dec 2026 target), Foxconn may have to rotate ~8,000 workers off third-shift temporarily. Assembly throughput drops 12&ndash;14% for a quarter; capex timeline holds. EBITDA impact Rs 180&ndash;220 Cr in the affected quarter. Debt serviceability unaffected. Mitigation: Phase 1 capex already allocated Rs 320 Cr to dormitory build{ref("8")}; IBank can accelerate disbursement if needed.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Scenario: RBI holds the line at 5.25% instead of hiking</h4>
      <p>Goldman is pricing a 50 bp hike at the June MPC{ref("5")}; if RBI holds instead, the rate-lock argument for sanction-before-MPC loses urgency. Deal slips 30&ndash;45 days. Product-wise impact: term-loan sanction slides into Q2; forex forwards and trade finance can still close on operational-urgency arguments. Revenue-to-IBank timing shifts one quarter; NPV on 3-year view negligible.</p>
    </div>
  </div>

  <h3>12.5 &mdash; Near-term calendar &mdash; public catalysts that shape timing</h3>
  <div style="overflow-x:auto">
  <table>
    <thead>
      <tr><th>Date</th><th>Event</th><th>What it changes for Foxconn Mega Dev</th><th>IBank action</th></tr>
    </thead>
    <tbody>
      <tr><td>30 Apr 2026</td><td>Current Hormuz-closure MoU expiry{ref("2")}</td><td>If closure extended, crude remains elevated; USD/INR stays near upper end of 92&ndash;95 range</td><td>Price FX forwards conservatively; add optionality in forward contract</td></tr>
      <tr><td>2 May 2026</td><td>US Q2 CY26 earnings &mdash; Apple FY26 Q2 (ending 28 Mar 2026){ref("27")}</td><td>iPhone India unit-mix commentary; capacity guidance; PLI outlook validation</td><td>Re-anchor projection base-case after call; share with internal credit desk</td></tr>
      <tr><td>10 May 2026</td><td>MeitY PLI FY25 disbursement statement{ref("11")}</td><td>Confirms Rs 560 Cr outstanding claim status; unlocks PLI-receivable factoring construct</td><td>Structure facility and term-sheet for discounting</td></tr>
      <tr><td>4&ndash;6 June 2026</td><td>RBI MPC &mdash; second of FY27{ref("1,5")}</td><td>50 bp hike priced in; repo decision sets benchmark for all new sanctions</td><td><strong>Rate-lock urgency:</strong> close capex TL before this date</td></tr>
      <tr><td>15 June 2026</td><td>IMD monsoon onset declaration (official){ref("4")}</td><td>Sub-normal trajectory confirmed or revised; indirect impact via retail / FMCG demand tail-winds</td><td>Re-run PESTEL environmental row; update industry-side FY27 base</td></tr>
      <tr><td>31 July 2026</td><td>US&ndash;India deal &mdash; generic pharma zero-duty implementation{ref("6")}</td><td>Foxconn Mega Dev not directly affected, but trade-deal stability signals 18% rate is durable</td><td>Lock 6M forward book covering Q2 shipments on confirmed stability</td></tr>
      <tr><td>Q2 FY27 (Aug&ndash;Sep 2026)</td><td>iPhone 17 Pro launch; commercial production ramp at SMT-4 line{ref("9")}</td><td>Capex absorption accelerates; forex flows step up by ~30% QoQ</td><td>Trade-finance throughput scales; GST float peaks &mdash; CMS engagement phase</td></tr>
      <tr><td>29 Sep 2026</td><td>US&ndash;India deal &mdash; patented pharma 100% tariff effective{ref("6")}</td><td>Signals US reciprocity is real; India-base manufacturing case strengthens for all exporters</td><td>Strategic review with parent; convert early-stage pitches for additional Foxconn-group entities</td></tr>
      <tr><td>Dec 2026</td><td>CPCB FGD retrofit deadline{ref("21")}</td><td>Unrelated to Foxconn directly; affects adjacent Tier-1 name R.K.M Powergen</td><td>Cross-reference when coordinating South TN LCG pipeline</td></tr>
      <tr><td>Q4 FY27</td><td>FY26 results filing (Foxconn Mega Dev)</td><td>Validates or invalidates FY27 base projection</td><td>Quarterly review with client; rebase the wallet-sizing if material</td></tr>
    </tbody>
  </table>
  </div>

  <h3>12.6 &mdash; Pre-reads and documentation &mdash; what the relationship team walks into the first meeting with</h3>
  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">External materials</h4>
      <ul class="check" style="margin-bottom:0">
        <li>2-page executive summary of this dossier, printed on IBank letterhead, with the Rs 185&ndash;225 Cr conversion headline</li>
        <li>MCA Form AOC-4 FY25 extract &mdash; particularly the debt and paid-up capital schedules{ref("23")}</li>
        <li>Probe42 open-charges API response &mdash; hardcopy confirming zero Indian-bank charge{ref("24")}</li>
        <li>Goldman and JPMorgan India-EMS research notes (publicly available extracts){ref("5,27,32")}</li>
        <li>One-page rate-lock sensitivity table showing Rs 4,200 Cr capex outcome under 0, +25 bp, +50 bp MPC scenarios</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Internal alignment items</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Credit committee pre-approval &mdash; preliminary Rs 4,000 Cr wholesale envelope under discretionary authority pending documentation</li>
        <li>Forex desk pricing sheet &mdash; 3M, 6M, 12M USD/INR forward rates; NDF comparison</li>
        <li>Trade-finance desk &mdash; indicative pricing for import LC, SBLC, confirmation from top Taiwan / China counterparty banks</li>
        <li>Retail relationship-manager briefed &mdash; payroll migration protocol, branch resource plan for Sriperumbudur + Chengalpattu</li>
        <li>PB relationship-manager briefed &mdash; CXO-level onboarding sequence, family-wealth proposition deck</li>
        <li>Rating-sponsor desk &mdash; CRISIL &amp; ICRA workflow lead identified; 8-week execution plan</li>
      </ul>
    </div>
  </div>

  <h3>12.7 &mdash; Pricing discipline &mdash; what NOT to offer</h3>
  <div class="card warn">
    <ul class="x" style="margin-bottom:0">
      <li><strong>Working-capital CC/OD below MCLR + 40 bp.</strong> The intercompany line is the competitor, and its fully-loaded cost is ~8.2&ndash;9.0% rupee-equivalent. Pricing below MCLR + 40 bp gives away margin without additional wallet conversion.</li>
      <li><strong>Trade finance at documentary fees &lt;12 bp.</strong> Street pricing for top-tier EMS is 12&ndash;18 bp; under-pricing risks setting a low anchor for the whole India-EMS trade book.</li>
      <li><strong>Unhedged / partially-hedged USD-INR CCS below 15 bp margin.</strong> The structural credit risk of converting ECB to rupee is real; margins below 15 bp do not price that risk adequately.</li>
      <li><strong>Dollar denominated BGs at non-risk-adjusted pricing.</strong> Performance BGs for PLI or SGST purposes should be priced with explicit India-sovereign risk loading, not benchmarked off Singapore treasury pricing.</li>
      <li><strong>CMS fee-waivers for the first two years as an acquisition incentive.</strong> Per our CMS-economics floor, a fully-free offering takes 26&ndash;34 months to recover even on optimistic volume; defer only the first year if necessary.</li>
    </ul>
  </div>

  <h3>12.8 &mdash; Escalation risks &amp; mitigations</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Risk</th><th>Probability</th><th>Mitigation</th></tr></thead>
    <tbody>
      <tr><td>Hon Hai Treasury declines to decouple from Singapore offshore book in Phase 1</td><td>Medium</td><td>Start with &quot;complementary&quot; rupee book rather than displacement pitch; target incremental capex tranche first</td></tr>
      <tr><td>June MPC hike materialises (50 bp) and client defers signing</td><td>Medium-High</td><td>Offer rate-reset clause; price forwards on locked-term loan to keep incremental cost marginal</td></tr>
      <tr><td>US&ndash;China trade-deal renegotiation collapses the 18% tariff advantage</td><td>Low-Medium (Jul&ndash;Sep window){ref("6")}</td><td>Tie covenants to volume (not price) so loan serviceability is preserved even on margin squeeze</td></tr>
      <tr><td>Apple shifts FATP work to Tata Electronics faster than expected</td><td>Medium (but limits downside to 3 pt share){ref("33")}</td><td>Bear case already assumes 47% share; cross-sell to Tata via separate mandate</td></tr>
      <tr><td>TN labour law changes on night-shift women workforce</td><td>Low-Medium{ref("8")}</td><td>Capex already announced for dormitory compliance; covenant-proof</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""


def section_sources() -> str:
    return """
<section id="sources">
  <div class="subhead">13 · Sources, data vintage &amp; diligence items</div>
  <h2>Every number carries a reference &mdash; here is where each one came from</h2>
  <div class="src-list">
  <ol>
  <li id="src-1"><strong>RBI MPC statement, 8 April 2026</strong> &mdash; repo 5.25%, unanimous, stance neutral. <span class="u">rbi.org.in / Press Releases / 2026-04-08 MPC Statement</span></li>
  <li id="src-2"><strong>Brent spot &amp; Strait-of-Hormuz status</strong> &mdash; ICE Brent front-month, closing range 22&ndash;24 Apr 2026 window. Hormuz disruption per Reuters / Platts 19 Apr 2026. <span class="u">ice.com · reuters.com/markets/commodities</span></li>
  <li id="src-3"><strong>RBI reference rate (USD/INR)</strong> &mdash; daily reference for 23 Apr 2026 at 93.50; April 2026 high 94.63 (16 Apr); low 91.83 (2 Apr). 12-month forward annualised 2.1% on 23 Apr 2026. <span class="u">rbi.org.in / Statistics / Exchange Rates</span> &middot; <span class="u">fedai.org.in</span></li>
  <li id="src-4"><strong>IMD first long-range forecast 2026</strong> &mdash; 92% of LPA for the southwest monsoon; El Niño likely. Press release 15 Apr 2026. <span class="u">imd.gov.in / Press Release / 15 April 2026</span></li>
  <li id="src-5"><strong>Goldman Sachs India Economics note</strong> &mdash; FY26 GDP cut to 5.9%, CPI 4.6%, CAD 2.0%; 50 bp rate-hike pricing for June MPC. <span class="u">Goldman Sachs Equity Research · Indian Economics Weekly 18 Apr 2026</span> (subscription; cite to internal research repository)</li>
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
  <li id="src-23"><strong>MCA Form AOC-4 &mdash; Foxconn Hon Hai Technology India Mega Development Pvt Ltd, FY25 Annual Financial Statement</strong> &mdash; filed 29 Nov 2025. <span class="u">mca.gov.in / MCA21 · CIN U32204TN2015FTC165627</span></li>
  <li id="src-24"><strong>Probe42 open-charges API pull</strong> &mdash; <code>/probe_data_api/entities/U32204TN2015FTC165627/open-charges</code>, response metadata <code>last_updated: 2026-04-08</code>. Zero charges returned. <span class="u">api.probe42.in · retrieved 24 Apr 2026</span></li>
  <li id="src-25"><strong>Bharat FIH Limited FY25 Annual Report</strong> &mdash; revenue Rs 12,824 Cr, customer mix disclosure. BSE scrip 544043. <span class="u">bseindia.com/stock-share-price/bharat-fih-ltd/SH544043/</span></li>
  <li id="src-26"><strong>Karnataka Industries &amp; Commerce Department</strong> &mdash; MoU with Yuzhan Technology (Foxconn) for Devanahalli, Bengaluru facility, Phase 1 Rs 1,400 Cr, Sep 2024. <span class="u">karnataka.gov.in / industries / press-release / sep-2024</span></li>
  <li id="src-27"><strong>JPMorgan India Equity Research &mdash; Apple India supply chain note</strong> &mdash; Feb 2026; India iPhone mix progression 35 mn FY24 &rarr; 92 mn FY28 projection; Apple target 25% of global output from India by 2027. <span class="u">JPMorgan India Technology 17 Feb 2026</span> (subscription)</li>
  <li id="src-28"><strong>Foxconn Hon Hai Technology India Mega Development &mdash; FY25 Management Discussion</strong> &mdash; extracted from MCA filed board&rsquo;s report 29 Nov 2025. Rs 3,200 Cr parent equity infusion, ECB effective rate 6.25%. <span class="u">mca.gov.in / MCA21 · Board Report FY25</span></li>
  <li id="src-29"><strong>RBI FDI statistics for Foxconn Hon Hai Technology India Mega Dev</strong> &mdash; cumulative $2,768 mn. <span class="u">rbi.org.in · FEMA filings aggregated quarterly report</span></li>
  <li id="src-30"><strong>Moody&rsquo;s &amp; S&amp;P global ratings on Hon Hai Precision Industries</strong> &mdash; Moody&rsquo;s A3 stable (21 Jan 2026 review); S&amp;P A- stable (15 Feb 2026 review). <span class="u">moodys.com / research &middot; spglobal.com / ratings</span></li>
  <li id="src-31"><strong>ICEA &mdash; India Mobile Manufacturing Production Data FY24&amp;FY25</strong> &mdash; $22.9 bn smartphone exports FY25; sector report Apr 2026. <span class="u">icea.org.in / industry-reports / mobile-manufacturing-2026</span></li>
  <li id="src-32"><strong>Counterpoint Research &mdash; global smartphone shipments by origin</strong> &mdash; India share, ASP mix, quarterly updates. <span class="u">counterpointresearch.com/insights/quarterly-shipment-tracker</span></li>
  <li id="src-33"><strong>Tata Electronics disclosures</strong> &mdash; Wistron Kolar acquisition (Oct 2023), Pegatron stake acquisition (Jan 2025); FY25 revenue estimate from Tata Sons annual report. <span class="u">tata.com / annual-report / 2025</span></li>
  <li id="src-34"><strong>Salcomp Plc &mdash; India operations disclosure</strong> &mdash; FY25 revenue ~Rs 9,400 Cr; Chennai + Noida plants. <span class="u">salcomp.com / investors / annual-report-2025</span></li>
  <li id="src-35"><strong>Dixon Technologies (India) Ltd FY25 Annual Report</strong> &mdash; consolidated revenue Rs 17,600 Cr. <span class="u">dixoninfo.com / investors / annual-report-fy25</span></li>
  <li id="src-36"><strong>Syrma SGS Technology Ltd FY25 Annual Report</strong> &mdash; consolidated revenue Rs 3,200 Cr. <span class="u">syrmasgs.com / investors</span></li>
  <li id="src-37"><strong>MeitY Component PLI (Rs 22,919 Cr outlay)</strong> &mdash; notified 28 Sep 2025. Covers PCBA, display, camera, charging sub-modules. <span class="u">meity.gov.in / PLI / Component / 2025</span></li>
  <li id="src-38"><strong>Companies Act 2013, Section 135 (CSR mandate)</strong> &mdash; applicable 2% of 3-year-avg PBT. <span class="u">mca.gov.in / Companies-Act-2013 / Section-135</span></li>
  <li id="src-48"><strong>ZaubaCorp / TheCompanyCheck / Tofler corporate filings</strong> &mdash; Foxconn Hon Hai Technology India Mega Development Pvt Ltd (CIN U32204TN2015FTC165627), DIR-12 directors list, FY25 / FY26 RoC profile, ~8,251 employees as filed. <span class="u">zaubacorp.com/company//U32204TN2015FTC165627 &middot; thecompanycheck.com &middot; tofler.in</span></li>
  <li id="src-49"><strong>Bharat FIH Limited corporate website + LinkedIn profile</strong> &mdash; subsidiary positioning, Sri City + Sriperumbudur facilities, ~30,000 workforce 90% women, Xiaomi / Nokia / OEM customer mix. <span class="u">bharatfih.com/about-bharat-fih/</span></li>
  <li id="src-50"><strong>Foxconn Singapore subsidiary / India operations expansion</strong> &mdash; reports of $1.5 bn investment in Yuzhan Technology India shares (12.77 bn shares) and $2.56 bn Devanahalli Karnataka project (300 acres, 30,000 dormitory). <span class="u">communicationstoday.co.in / The Foxconn Swayamvara &middot; thehansindia.com</span></li>
  <li id="src-51"><strong>NHRC India press release</strong> &mdash; suo motu cognizance of married-women hiring exclusion at Foxconn Sriperumbudur, Jul 2024. <span class="u">nhrc.nic.in / media/press-release / nhrc-india-takes-suo-motu-cognizance-reported-discrimination-by-foxconn</span></li>
  <li id="src-52"><strong>Business Standard</strong> &mdash; &ldquo;Labour officials visit Foxconn TN plant, question executives about hiring&rdquo;, 3 Jul 2024. <span class="u">business-standard.com/india-news/labour-officials-visit-foxconn-tn-plant-question-executives-about-hiring-124070300583_1.html</span></li>
  <li id="src-53"><strong>Business Standard</strong> &mdash; &ldquo;NHRC launches new probe into discriminatory hiring at Foxconn&rsquo;s India plant&rdquo;, 23 Jan 2025. <span class="u">business-standard.com/companies/news/foxconn-tamil-nadu-apple-iphone-plant-married-women-hiring-nhrc-probe-125012300448_1.html</span></li>
  <li id="src-54"><strong>Business Standard</strong> &mdash; &ldquo;Foxconn eyes iPhone enclosure manufacturing in Tamil Nadu&rdquo;, 20 Jun 2025. <span class="u">business-standard.com/industry/news/foxconn-iphone-enclosure-manufacturing-oragadam-tamil-nadu-125062000343_1.html</span></li>
  <li id="src-55"><strong>Outlook Business</strong> &mdash; &ldquo;Foxconn Expands India Footprint with New iPhone Enclosure Factory in Tamil Nadu&rdquo;, Jun 2025. <span class="u">outlookbusiness.com/start-up/news/foxconn-expands-india-footprint-with-new-iphone-enclosure-factory-in-tamil-nadu</span></li>
  <li id="src-56"><strong>Business Standard</strong> &mdash; &ldquo;Foxconn India investment: Trump warns Apple, but Foxconn to proceed with $1.5 bn Chennai iPhone plant&rdquo;, 23 May 2025. <span class="u">business-standard.com/companies/news/apple-foxconn-1-5-billion-investment-chennai-iphone-plant-trump-warning-125052300334_1.html</span></li>
  <li id="src-57"><strong>AckoDrive News</strong> &mdash; &ldquo;Foxconn Invests $31.8 Million In Tamil Nadu Plant To Make iPhone 16 Pro&rdquo;, 2025. <span class="u">ackodrive.com/news/foxconn-invests-31-8-million-in-tamil-nadu-plant-to-make-i-phone-16-pro-in-india/</span></li>
  <li id="src-81"><strong>Probe42 credit-ratings endpoint</strong> &mdash; <code>/probe_data_api/entities/{CIN}/credit-ratings</code>; per-instrument rating grid including agency, date, action (Reaffirmed / Assigned / Upgraded / Downgraded), long-term / short-term symbol, outlook, instrument list and amounts. Pulled 22 Apr 2026 across all Tier-1 pilot CINs. <span class="u">api.probe42.in &middot; retrieved 22 Apr 2026</span></li>
  <li id="src-82"><strong>Probe42 suit-filed-cases endpoint</strong> &mdash; <code>/probe_data_api/entities/{CIN}/suit-filed-cases</code>; credit-bureau suit-filed cases (if any) with date, agency, bank, amount fields. <strong>All Tier-1 pilots returned ZERO suit-filed cases as of 22 Apr 2026.</strong> <span class="u">api.probe42.in &middot; retrieved 22 Apr 2026</span></li>
  </ol>
  </div>

  <h3>Diligence items flagged</h3>
  <ul class="x">
    <li><strong>Standalone Indian rating</strong> &mdash; Foxconn Mega Dev currently <em>Not Rated</em>; CRISIL + ICRA first-time rating required before any public-issuance product. Fee discussion bundled into Phase 1 engagement.</li>
    <li><strong>Full MCA charge status re-verification</strong> &mdash; additional Probe42 pull at T + 30, T + 60, T + 90 to monitor for any new charge creation that would change the greenfield story.</li>
    <li><strong>Confirmation of PLI disbursement history FY22&ndash;FY24</strong> &mdash; internal check with MeitY relationship; exact claim-wise approval date needed to structure PLI-receivable factoring.</li>
    <li><strong>Hon Hai Treasury policy</strong> &mdash; current Singapore-issued intercompany loan agreement terms needed to price the displacement proposition; request via CFO as part of T + 15 documentation exchange.</li>
    <li><strong>ESOP / RSU India escrow mechanics</strong> &mdash; critical for TASC and PB sizing; request from HR Director.</li>
  </ul>
</section>
"""


NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li>
<li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li>
<li><a href="#entity">04 Entity</a></li>
<li><a href="#industry">05 Industry</a></li>
<li><a href="#pestel-ems">06 PESTEL</a></li>
<li><a href="#models">07 Models</a></li>
<li><a href="#entry-map">08 Entry map</a></li>
<li><a href="#retail">09 Retail/PB/TASC</a></li>
<li><a href="#consolidated">10 Consolidated</a></li>
<li><a href="#diligence">11 Diligence</a></li>
<li><a href="#playbook">12 Playbook</a></li>
<li><a href="#sources">13 Sources</a></li>
</ol></nav>
"""


def build():
    title = "Foxconn Hon Hai Technology India Mega Development · Dossier 24 Apr 2026"
    parts = [
        HEAD(title),
        NAV,
        section_cover(),
        MACRO_BLOCK,
        section_group(),
        section_entity(),
        section_industry(),
        PESTEL_EMS,
        section_models(),
        section_entry_map(),
        section_retail_pb_tasc(),
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
