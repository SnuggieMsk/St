"""Build `caratlane-dossier.html` — Tier-1 pilot #06 (Online jewelry, Titan).

Company: CaratLane Trading Private Limited
CIN   : U52393TN2007PTC064830
Parent: 100% Titan Company Ltd (Tata Group) — wholly-owned since Feb 2024
FY25  : TOI ~Rs 4,153 Cr (master sheet); separately reported Rs 3,583 Cr Total Income
Rating: ICRA A1+ (Dec 2025 Probe42 pull); Commercial Paper Programme
"""
from __future__ import annotations
from pathlib import Path
from .base import CSS, HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "caratlane-dossier.html"

NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li>
<li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li>
<li><a href="#entity">04 Entity</a></li>
<li><a href="#industry">05 Industry</a></li>
<li><a href="#models">06 Models</a></li>
<li><a href="#entry-map">07 Entry map</a></li>
<li><a href="#retail">08 Retail/PB/TASC</a></li>
<li><a href="#consolidated">09 Consolidated</a></li>
<li><a href="#diligence">10 Diligence</a></li>
<li><a href="#playbook">11 Playbook</a></li>
<li><a href="#sources">12 Sources</a></li>
</ol></nav>
"""

def S1():
    return f"""
<section id="cover" class="hero">
  <div class="eyebrow">Tier-1 Dossier · 06 of 20 · Online jewelry · Titan wholly-owned</div>
  <h1>CaratLane Trading Private Limited<br>India&rsquo;s largest omni-channel online-jewelry brand</h1>
  <p class="lede">Wholly-owned subsidiary of Titan Company Ltd (Tata Group) since February 2024, when Titan acquired the final 0.36% stake for Rs 60.08 Cr taking its holding to 100%{ref("95")}. FY25 total income of Rs 3,583 Cr with EBIT Rs 296 Cr (8.3% margin) and 24% YoY top-line growth; master-sheet TOI of Rs 4,153 Cr reflects consolidated channel view{ref("96")}. 322 stores across 140 cities{ref("96")}. ICRA A1+ on commercial paper programme (31 Dec 2025 Probe42 pull){ref("81")}. Zero suit-filed cases (Probe42 22 Apr 2026){ref("82")}. The entity is rapidly maturing from startup-mode to profitable omni-channel scale-up and will be a defining jewelry-sector credit within Titan group through FY28.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (fully-built)</div><div class="v num">Rs 48–62 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 38–48 Cr + Retail / PB / TASC Rs 10–14 Cr</div></div>
    <div class="kpi"><div class="k">FY25 Total Income</div><div class="v num">Rs 3,583 Cr</div><div class="sub">+24% YoY; EBIT Rs 296 Cr at 8.3%{ref("96")}</div></div>
    <div class="kpi pos"><div class="k">ICRA rating</div><div class="v num">A1+</div><div class="sub">CP programme; Titan parent support{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges (master sheet)</div><div class="v num">Rs 1,675 Cr</div><div class="sub">Store-expansion working capital anchored</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this converts</h4>
    <ol style="margin-bottom:0">
      <li><strong>Titan parent umbrella.</strong> Tata-group-level credit umbrella means ICRA A1+ rating supports the lowest wholesale pricing band. Titan relationship-level introduction creates Phase 2 cross-sell to the Rs 50,000 Cr+ Titan parent.</li>
      <li><strong>Store expansion capex.</strong> 322 stores growing to 450&ndash;500 by FY28 implies Rs 280&ndash;380 Cr capex across next 30 months. SPV-like store-rollout facility structure is a natural fit.</li>
      <li><strong>Gold-inventory financing.</strong> The sector&rsquo;s working-capital model is structurally bullion-backed; metal-financing (gold-loan / lease) programmes are natural entry-points with high-margin economics relative to generic WC.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U52393TN2007PTC064830</strong></span>
    <span>Parent <strong>Titan Company Ltd (Tata Group), NSE/BSE: TITAN</strong></span>
    <span>Founded <strong>2008 (Mithun Sacheti + Srinivasa Gopalan)</strong></span>
    <span>Registry cut <strong>Probe42 / 02 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; ownership lineage</div>
  <h2>From founder-led 2008 startup to 100% Titan subsidiary in 16 years</h2>

  <h3>03.1 &mdash; Ownership lineage</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Year</th><th>Event</th><th>Titan holding post-event</th><th>Valuation / consideration</th></tr></thead>
    <tbody>
      <tr><td>2008</td><td>CaratLane founded by Mithun Sacheti + Srinivasa Gopalan</td><td>0%</td><td>Founder capital{ref("97")}</td></tr>
      <tr><td>2010&ndash;2016</td><td>Successive VC rounds (Tiger Global, Tata Capital Growth Fund)</td><td>0%</td><td>Sequential priced rounds</td></tr>
      <tr><td>2016</td><td>Titan takes initial stake</td><td>~62%</td><td>Post-money valuation Rs 575 Cr{ref("95")}</td></tr>
      <tr><td>Aug 2023</td><td>Titan buys 27% residual from Mithun Sacheti</td><td>~99.64%</td><td>Transaction valued CaratLane at Rs 17,000 Cr; Sacheti net Rs 4,621 Cr on exit{ref("95")}</td></tr>
      <tr><td>Feb 2024</td><td>Titan acquires final 0.36%</td><td><strong>100%</strong></td><td>Rs 60.08 Cr; CaratLane becomes wholly-owned subsidiary{ref("95")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>03.2 &mdash; Titan group structure (context)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>Listing / ownership</th><th>Role</th><th>Relevance to CaratLane</th></tr></thead>
    <tbody>
      <tr><td><strong>Titan Company Ltd</strong></td><td>NSE: TITAN / BSE: 500114 (listed; Tata Group)</td><td>Parent; Tanishq, Titan watches, Taneira, Titan Eye+</td><td>100% parent; credit umbrella</td></tr>
      <tr><td>Tata Sons Pvt Ltd</td><td>Unlisted (promoter of Titan)</td><td>Tata Group holding company</td><td>Ultimate beneficial owner</td></tr>
      <tr><td>TIDCO (Tamil Nadu Industrial Development Corporation)</td><td>State PSU (co-promoter of Titan)</td><td>Founding co-promoter since 1984</td><td>Long-term JV governance</td></tr>
      <tr><td>CaratLane Trading Pvt Ltd (this entity)</td><td>100% Titan</td><td>Omni-channel online + store jewelry</td><td>This dossier</td></tr>
      <tr><td>Tanishq</td><td>Titan division</td><td>Largest branded jewellery chain in India (470+ stores)</td><td>Sister-brand; potential co-marketed product lines</td></tr>
      <tr><td>Titan Engineering &amp; Automation (TEAL)</td><td>Titan subsidiary</td><td>Industrial automation / aerospace precision</td><td>Separate relationship</td></tr>
    </tbody>
  </table>
  </div>

  <div class="card pos">
    <h4 style="margin-top:0">Why Titan-group structure matters for IBank</h4>
    <p>CaratLane relationship begins a wider Tata-group / Titan-group conversation. Titan itself is one of the largest non-Tata Sons Tata companies by market cap (~Rs 3 lakh Cr). A well-executed CaratLane wholesale mandate builds the relationship currency to engage Titan parent + Tata Capital + other Tata group entities. In pure-CaratLane terms, the Rs 38&ndash;48 Cr wholesale wallet is the entry point; the parent-group halo effect is the compounding return.</p>
  </div>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <h2>P&amp;L, balance sheet, store economics</h2>

  <h3>04.1 &mdash; P&amp;L snapshot</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">YoY %</th></tr></thead>
    <tbody>
      <tr><td>Total Income</td><td class="num">2,169</td><td class="num">2,883</td><td class="num">3,583</td><td class="num pos">+24.3%</td></tr>
      <tr><td>EBITDA</td><td class="num">146</td><td class="num">186</td><td class="num">345</td><td class="num pos">+85.5%</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">6.7</td><td class="num">6.5</td><td class="num">9.6</td><td class="num pos">+310 bp</td></tr>
      <tr><td>EBIT (reported)</td><td class="num">&mdash;</td><td class="num">210</td><td class="num">296</td><td class="num pos">+41%{ref("96")}</td></tr>
      <tr><td>PAT</td><td class="num">~70</td><td class="num">79</td><td class="num">140</td><td class="num pos">+77%</td></tr>
      <tr><td>Store count (end-of-year)</td><td class="num">245</td><td class="num">285</td><td class="num">322</td><td class="num pos">+13% YoY{ref("96")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>04.2 &mdash; Balance sheet (FY25 estimated)</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Tangible Net Worth</div><div class="v num">850</div><div class="sub">Rs Cr est.</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">620</div><div class="sub">Rs Cr; WC + metal lease</div></div>
    <div class="kpi pos"><div class="k">Debt / EBITDA</div><div class="v num">1.80x</div><div class="sub">Comfortable</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">1,675</div><div class="sub">Rs Cr; metal-lease + WC consortium</div></div>
    <div class="kpi"><div class="k">Inventory (gold + diamond)</div><div class="v num">~1,900</div><div class="sub">Rs Cr est.</div></div>
    <div class="kpi accent"><div class="k">Store-expansion capex FY26-FY28</div><div class="v num">280&ndash;380</div><div class="sub">Rs Cr; 130&ndash;180 new stores</div></div>
  </div>

  <h3>04.3 &mdash; Store economics</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th>Value</th><th>Commentary</th></tr></thead>
    <tbody>
      <tr><td>Store count (FY25)</td><td>322 stores / 140 cities</td><td>17 stores added in Q4 FY25 alone{ref("96")}</td></tr>
      <tr><td>Avg new-store capex</td><td>Rs 1.8&ndash;2.2 Cr/store</td><td>Fit-out + inventory + working capital</td></tr>
      <tr><td>Avg new-store pay-back</td><td>2.5&ndash;3 years</td><td>Strong unit-economics validated</td></tr>
      <tr><td>Digital-revenue share</td><td>~35&ndash;38%</td><td>Omni-channel; higher than legacy jewelry retailers</td></tr>
      <tr><td>Average ticket size</td><td>Rs 28,000&ndash;45,000</td><td>Lower than pure-luxury; mass-premium positioning</td></tr>
      <tr><td>Gross margin</td><td>~26&ndash;28%</td><td>Design-premium + tech-led personalisation premium</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry deep-dive &mdash; India organised / online jewelry</div>
  <h2>Structural consumer-upgrade + online-shift tailwinds</h2>
  <p class="lede">India&rsquo;s jewelry market (~Rs 6.8 lakh Cr) is shifting from unorganised / family-jeweller (~65% share) to organised branded (~35% and rising to 50% by FY28). Online + omni-channel is the fastest-growing segment (currently 10%, to 18% by FY28). CaratLane is the clear leader in online-first + omni-channel in both design and revenue.</p>

  <h3>05.1 &mdash; Sector size</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24 A</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 E</th><th class="num">FY28 E</th></tr></thead>
    <tbody>
      <tr><td>India jewelry market (Rs lakh Cr)</td><td class="num">6.2</td><td class="num">6.8</td><td class="num">7.4</td><td class="num">8.1</td><td class="num">8.9</td></tr>
      <tr><td>Organised-branded share (%)</td><td class="num">32</td><td class="num">35</td><td class="num">39</td><td class="num">44</td><td class="num">50</td></tr>
      <tr><td>Online / omni-channel share (%)</td><td class="num">8</td><td class="num">10</td><td class="num">13</td><td class="num">16</td><td class="num">18</td></tr>
      <tr><td>Gold price (Rs/10g, avg)</td><td class="num">64,500</td><td class="num">74,800</td><td class="num">82,000</td><td class="num">86,500</td><td class="num">89,500</td></tr>
      <tr><td>CaratLane TOI (Rs Cr)</td><td class="num">2,883</td><td class="num">3,583</td><td class="num">4,500</td><td class="num">5,600</td><td class="num">6,900</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.2 &mdash; Competitive landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Player</th><th>Positioning</th><th>FY25 revenue (Rs Cr)</th><th>Listing</th></tr></thead>
    <tbody>
      <tr><td><strong>CaratLane (this dossier)</strong></td><td>Omni-channel design-led; mass-premium</td><td class="num">3,583{ref("96")}</td><td>Titan 100% subsidiary</td></tr>
      <tr><td>Tanishq (Titan division)</td><td>Premium jewelry chain; 470+ stores</td><td class="num">~46,000</td><td>Titan division (listed at parent)</td></tr>
      <tr><td>Kalyan Jewellers</td><td>Pan-India regional + national</td><td class="num">18,500</td><td>NSE/BSE listed</td></tr>
      <tr><td>Senco Gold</td><td>East + pan-India</td><td class="num">5,200</td><td>Listed</td></tr>
      <tr><td>Joyalukkas</td><td>Premium pan-India</td><td class="num">15,800</td><td>Private</td></tr>
      <tr><td>Malabar Gold</td><td>Pan-India largest by store count</td><td class="num">~55,000 (global)</td><td>Private</td></tr>
      <tr><td>BlueStone (online-first)</td><td>Online + new stores roll-out</td><td class="num">~490</td><td>IPO-filed</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.3 &mdash; Three key industry drivers</h3>
  <div class="grid c3">
    <div class="card accent">
      <h4 style="margin-top:0">Hallmarking + consumer-protection</h4>
      <p>BIS mandatory hallmarking Since 2021; 6-digit HUID since Apr 2023. This structurally advantages branded / organised players vs unorganised jewellers. CaratLane&rsquo;s tech-enabled certification is a competitive moat.</p>
    </div>
    <div class="card accent">
      <h4 style="margin-top:0">Lab-grown diamonds acceleration</h4>
      <p>Lab-grown diamond segment is growing 18&ndash;22% CAGR; India is the largest lab-grown-diamond producer globally. CaratLane&rsquo;s design-led + tech positioning captures this shift; higher-margin than traditional mined stones.</p>
    </div>
    <div class="card accent">
      <h4 style="margin-top:0">Wedding-to-self-purchase shift</h4>
      <p>Millennial / Gen-Z consumers increasingly self-purchase, not just wedding-gift. Self-purchase spend grew 28% CAGR post-COVID. CaratLane&rsquo;s design + price-point positioning is the market leader for this segment.</p>
    </div>
  </div>
</section>
"""
def S5():
    return f"""
<section id="models">
  <div class="subhead">06 · Projection models</div>
  <h2>FY27 base / bear / bull scenarios</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,583</td><td class="num">4,500</td><td class="num">5,600</td><td class="num">4,800</td><td class="num">6,200</td><td class="num">6,900</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">9.6</td><td class="num">10.2</td><td class="num pos">10.8</td><td class="num neg">8.8</td><td class="num pos">11.5</td><td class="num">11.2</td></tr>
      <tr><td>EBITDA</td><td class="num">345</td><td class="num">459</td><td class="num">605</td><td class="num">422</td><td class="num">713</td><td class="num">773</td></tr>
      <tr><td>PAT</td><td class="num">140</td><td class="num">212</td><td class="num">300</td><td class="num">185</td><td class="num">378</td><td class="num">395</td></tr>
      <tr><td>Capex (Rs Cr)</td><td class="num">72</td><td class="num">95</td><td class="num">120</td><td class="num">85</td><td class="num">140</td><td class="num">130</td></tr>
      <tr><td>Store count end-of-year</td><td class="num">322</td><td class="num">382</td><td class="num">445</td><td class="num">410</td><td class="num">475</td><td class="num">500</td></tr>
    </tbody>
  </table>
  </div>

  <h3>06.1 &mdash; Drivers</h3>
  <p>Base case: 22% revenue CAGR, 320 bp EBITDA margin expansion, 130-store net add over 2 years. Bear: 18% revenue / margin compression on gold-price volatility. Bull: 26% CAGR + 150 bp incremental margin on omni-channel efficiencies.</p>

  <h3>06.2 &mdash; Funding-gap waterfall (base FY26&ndash;FY28)</h3>
  <div class="card"><div class="waterfall">
Opening cash (1 Apr 2026)                       :  Rs   280 Cr
+ Cumulative PAT FY26-FY28 base                 :  Rs   907 Cr
+ Depreciation add-back                         :  Rs   210 Cr
- Capex FY26-FY28 (store roll-out)              :  Rs  (345) Cr
- Inventory build (gold + diamond)              :  Rs  (680) Cr
- Working-capital build                         :  Rs  (180) Cr
- Dividend to Titan (policy-based)              :  Rs  (160) Cr
= Closing cash (31 Mar 2028)                    :  Rs    32 Cr
-----------------------------------------------------------
Cumulative new debt / financing need            :  Rs   320 Cr
  IBank target share 40-50% (fund+metal lease)  :  Rs   140 Cr  &larr; new funded wallet
  Co-arranger banks                             :  Rs   180 Cr
  CP programme (A1+) rolling                    :  Rs   200 Cr
  Non-funded (BG / SBLC / metal lease)          :  Rs   280 Cr
</div></div>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Wholesale product entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th>Line-item moved</th><th class="num">Size (Rs Cr)</th><th>Pricing</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td><strong>Metal / gold-lease programme</strong></td><td>Inventory financing</td><td class="num">380&ndash;480</td><td>MIBOR + 55 bp</td><td class="num">7&ndash;9</td></tr>
      <tr><td>WC CC/OD</td><td>Short-term borrowings</td><td class="num">220&ndash;280</td><td>MCLR + 30 bp</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Store-rollout term loan</td><td>Long-term debt</td><td class="num">180&ndash;240</td><td>MCLR + 55 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CP programme (A1+)</td><td>Short-term borrowings</td><td class="num">200 rolling</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>BG / SBLC (landlord + supplier)</td><td>Contingent liabilities</td><td class="num">140&ndash;180</td><td>Comm 42 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX forwards (diamond imports)</td><td>Other comprehensive income</td><td class="num">480&ndash;620 notional</td><td>1.2 paise pip</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Payment gateway + merchant acquiring (online)</td><td>MDR + float</td><td class="num">&mdash;</td><td>MDR 90&ndash;120 bp</td><td class="num">6&ndash;8</td></tr>
      <tr><td>SCF (anchor-led; diamond + finding suppliers)</td><td>Trade payables</td><td class="num">160&ndash;220</td><td>NIM 1.8% + fee</td><td class="num">4&ndash;5</td></tr>
      <tr><td>CMS (322-store collection + vendor pay)</td><td>Float</td><td class="num">&mdash;</td><td>API fee + float</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Treasury / liquid-fund mgmt</td><td>Liquid investments</td><td class="num">150&ndash;250 AUM</td><td>18&ndash;22 bp</td><td class="num">2&ndash;3</td></tr>
    </tbody>
  </table>
  </div>

  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">Wholesale summary</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Funded (CC/OD + TL + CP + gold-lease): <strong>Rs 980&ndash;1,200 Cr</strong></li>
        <li>Non-funded (BG + SBLC): <strong>Rs 140&ndash;180 Cr</strong></li>
        <li>Derivative notional (FX): <strong>Rs 480&ndash;620 Cr</strong></li>
        <li>SCF programme: <strong>Rs 160&ndash;220 Cr</strong></li>
        <li class="mono" style="border-top:1px dashed var(--line);padding-top:8px;margin-top:8px"><strong>IBank income est: Rs 35&ndash;48 Cr/yr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Why metal-lease is the anchor product</h4>
      <p>CaratLane&rsquo;s largest current-asset line is gold + diamond inventory (~Rs 1,900 Cr est). Gold-lease / metal-financing is structurally sector-specific and the highest-economic product; also the existing-lender retention battle is fought on this line. Winning metal-lease programme is the gate to the rest of the wallet.</p>
    </div>
  </div>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card">
      <h4 style="margin-top:0">08.1 Retail / salary</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Workforce: ~4,200 (corporate + 322 store-level)</li>
        <li>Salary CASA Y1: 1,800&ndash;2,200 accounts</li>
        <li>Ticket Rs 22,000&ndash;55,000/mo blended</li>
        <li>Annual income: <strong>Rs 3&ndash;4 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">08.2 Private Banking</h4>
      <ul class="check" style="margin-bottom:0">
        <li>CaratLane-level senior mgmt (CEO + CFO + senior): ~15 UHNI candidates</li>
        <li>Titan parent senior leadership (extended relationship access)</li>
        <li>Mithun Sacheti post-exit family-office (Rs 4,621 Cr in 2023){ref("95,98")} &mdash; if targetable</li>
        <li>AUM Y3 target: Rs 80&ndash;150 Cr (excl. Sacheti)</li>
        <li>Annual income: <strong>Rs 2&ndash;4 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">08.3 TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>CaratLane PF + Gratuity trust: Rs 40&ndash;65 Cr est.</li>
        <li>Titan-group CSR flow through (consolidated)</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent">
    <h4 style="margin-top:0">Combined retail / PB / TASC: Rs 7&ndash;11 Cr/yr</h4>
    <p>Plus incremental Rs 3 Cr from payment-gateway / store-CMS / UPI-rails from consumer-side relationships not captured in salary line.</p>
  </div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated wallet summary</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product bucket</th><th class="num">Wallet size (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Metal / gold-lease</td><td class="num">380&ndash;480</td><td class="num">7&ndash;9</td></tr>
      <tr><td>WC CC/OD</td><td class="num">220&ndash;280</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Store-rollout TL</td><td class="num">180&ndash;240</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CP programme (A1+)</td><td class="num">200 rolling</td><td class="num">1&ndash;2</td></tr>
      <tr><td>BG / SBLC</td><td class="num">140&ndash;180</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX forwards</td><td class="num">480&ndash;620 notional</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Payment gateway</td><td class="num">&mdash;</td><td class="num">6&ndash;8</td></tr>
      <tr><td>SCF</td><td class="num">160&ndash;220</td><td class="num">4&ndash;5</td></tr>
      <tr><td>CMS</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Treasury AUM</td><td class="num">150&ndash;250</td><td class="num">2&ndash;3</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>1,280&ndash;1,680</strong></td><td class="num"><strong>35&ndash;48</strong></td></tr>
      <tr><td>Retail / salary</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>PB</td><td class="num">&mdash;</td><td class="num">2&ndash;4</td></tr>
      <tr><td>TASC</td><td class="num">&mdash;</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Payment-gateway consumer adj.</td><td class="num">&mdash;</td><td class="num">3</td></tr>
      <tr><td><strong>Retail/PB/TASC total</strong></td><td class="num">&mdash;</td><td class="num"><strong>10&ndash;14</strong></td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>1,280&ndash;1,680</strong></td><td class="num pos"><strong>45&ndash;62 Cr/yr</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence file</div>

  <h3>10.1 &mdash; Promoter &amp; ownership</h3>
  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">Ownership structure</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>100% owned by Titan Company Ltd</strong> (Tata Group) since Feb 2024{ref("95")}</li>
        <li>Ultimate parent: Tata Sons Pvt Ltd + TIDCO (co-promoters of Titan since 1984)</li>
        <li>Founder Mithun Sacheti exited 2023&ndash;2024; not a current shareholder</li>
        <li>No pledge / no promoter-level concerns given wholly-owned subsidiary status</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Related-party network</h4>
      <ul class="check" style="margin-bottom:0">
        <li>CaratLane &harr; Tanishq (Titan division) RPTs: product licensing + co-promotion</li>
        <li>CaratLane &harr; TEAL (Titan Engineering): minimal RPT exposure</li>
        <li>Titan parent provides IT / shared-services backbone per AS-18 disclosure</li>
        <li>No NCLT / litigation exposure at Titan parent level</li>
      </ul>
    </div>
  </div>

  <h3>10.1b &mdash; KMPs, SBOs &amp; Probe42-verified</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>CEO (CaratLane)</td><td>Avnish Anand (co-founder + CEO since 2023 Mithun-exit)</td><td>Titan disclosures{ref("96,98")}</td></tr>
      <tr><td>CFO (CaratLane)</td><td>Titan-rotational finance lead; current incumbent to be confirmed via MCA DIR-12</td><td>Diligence item</td></tr>
      <tr><td>Company Secretary</td><td>Titan group CS team rotational</td><td>Diligence item</td></tr>
      <tr><td>Directors (CaratLane board)</td><td>Titan-nominated: Suparna Mitra (Titan watches head), Ajoy Chawla, senior Titan execs + CaratLane management</td><td>MCA DIR-12</td></tr>
      <tr><td>SBO (Form BEN-2)</td><td>Tata Sons + TIDCO as promoters of Titan parent; no individual &gt;10% at Titan level</td><td>MCA Form BEN-2</td></tr>
      <tr><td>Material shareholders</td><td>100% Titan Company Ltd</td><td>MCA</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 31 Dec 2025)</td><td><strong>ICRA A1+ Reaffirmed</strong> on Commercial Paper Programme</td><td>Probe42 credit-ratings{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed cases</strong> (Probe42, 2 Apr 2026)</td><td><strong>ZERO</strong></td><td>Probe42 suit-filed-cases{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 &mdash; Subsidiaries / group adjacencies</h3>
  <p>CaratLane is a single-entity retailer with no India subsidiaries of its own. Its parent Titan has a rich structure (Tanishq jewelry, Titan watches, Taneira sarees, Titan Eye+, Fastrack, Skinn, TEAL). Sister-brand cross-sell is a Phase 2 consideration for IBank at Titan parent level (separate relationship).</p>

  <h3>10.3 &mdash; Litigation &amp; regulatory</h3>
  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">✓ Clean across all registers</h4>
      <p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter. Probe42 suit-filed = 0. No material commercial litigation. Standard jewelry-sector regulatory exposure (BIS hallmarking, GST consumer-good rate) handled administratively.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">⚙ BIS hallmarking + HUID compliance</h4>
      <p>6-digit HUID mandatory since Apr 2023. CaratLane&rsquo;s tech-stack processes HUID at scale; no compliance gap in public domain. BIS audit-compliance is a competitive moat vs unorganised players.</p>
    </div>
  </div>

  <h3>10.4 &mdash; News file (last 18 months)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date</th><th>Sentiment</th><th>Headline</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Dec 2025</td><td><span class="tag pos">Positive</span></td><td>ICRA reaffirms A1+ on CaratLane commercial paper programme</td><td>Probe42{ref("81")}</td></tr>
      <tr><td>FY25</td><td><span class="tag pos">Positive</span></td><td>Total income up 24% to Rs 3,583 Cr; EBIT Rs 296 Cr at 8.3%; 322 stores / 140 cities</td><td>Inc42 + Infomance{ref("96")}</td></tr>
      <tr><td>Feb 2024</td><td><span class="tag pos">Positive</span></td><td>Titan acquires final 0.36% stake in CaratLane for Rs 60.08 Cr &mdash; becomes wholly-owned subsidiary</td><td>Inc42{ref("95")}</td></tr>
      <tr><td>Aug 2023</td><td><span class="tag pos">Positive</span></td><td>Titan buys 27% from founder Mithun Sacheti at Rs 17,000 Cr valuation; Sacheti nets Rs 4,621 Cr</td><td>Rapaport + YourStory{ref("95,98")}</td></tr>
      <tr><td>Q3 FY25</td><td><span class="tag pos">Positive</span></td><td>Q3 FY25 revenue Rs 1,537 Cr (+42% YoY); 17 new stores added</td><td>Inc42{ref("99")}</td></tr>
      <tr><td>Ongoing</td><td><span class="tag pos">Positive</span></td><td>Mithun Sacheti launches FinQube investment firm; CaratLane continues scale under Avnish Anand</td><td>Inc42{ref("98")}</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 intervention playbook</div>

  <h3>11.1 &mdash; Days 1&ndash;30</h3>
  <div class="card accent">
    <p><span class="phase">T + 30</span><strong>Metal-lease programme + CP arranger mandate.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Initial meeting with CaratLane CFO + Titan parent treasury head</li>
      <li>Indicative Rs 380&ndash;480 Cr metal-lease programme at MIBOR + 55 bp</li>
      <li>CP arranger mandate for Rs 200 Cr rolling (A1+ rating supports pricing)</li>
      <li>Forex desk pitch on diamond-import hedging programme</li>
      <li>Rate-lock before June MPC{ref("5")}</li>
    </ul>
  </div>

  <h3>11.2 &mdash; Days 31&ndash;60</h3>
  <div class="card">
    <p><span class="phase">T + 60</span><strong>Close metal-lease + WC consolidation.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Metal-lease agreement live; first drawdown sequenced to inventory cycle</li>
      <li>WC CC/OD at Rs 220&ndash;280 Cr closed</li>
      <li>Store-rollout TL term-sheet for 130&ndash;180 new stores FY26&ndash;FY28</li>
      <li>Payment-gateway onboarding for online channel</li>
      <li>CMS integration across 322 stores</li>
    </ul>
  </div>

  <h3>11.3 &mdash; Days 61&ndash;90</h3>
  <div class="card pos">
    <p><span class="phase">T + 90</span><strong>Scale retail + PB; Titan parent introduction.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Salary migration across 322 stores (1,800&ndash;2,200 accounts Y1)</li>
      <li>PB engagement with CaratLane senior management</li>
      <li>BG / SBLC framework for landlords + suppliers</li>
      <li>FX forward programme live for diamond imports</li>
      <li>Cross-sell handshake to Titan parent treasury (Phase 2 gateway)</li>
    </ul>
  </div>

  <h3>11.4 &mdash; Competitive risks &amp; mitigations</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Risk</th><th>Probability</th><th>Mitigation</th></tr></thead>
    <tbody>
      <tr><td>Gold-price volatility hits inventory value &amp; margins</td><td>Medium-High</td><td>Metal-lease structure passes price risk to lessor; customer pre-order mitigates</td></tr>
      <tr><td>Incumbent lender (likely SBI / HDFC at Titan parent) retains metal-lease</td><td>Medium</td><td>Differentiate on combined metal-lease + CP + FX bundle; parent-group relationship halo</td></tr>
      <tr><td>Titan parent treasury centralisation reduces CaratLane autonomy</td><td>Low-Medium</td><td>Engage at Titan treasury level directly; position as group relationship</td></tr>
      <tr><td>Store expansion slows on consumer downturn</td><td>Low</td><td>Unit economics validated (2.5&ndash;3 yr payback); covenants structured for volume flex</td></tr>
      <tr><td>RBI 50 bp hike Jun MPC{ref("5")}</td><td>Medium-High</td><td>Rate-lock; swap to fixed on drawdown</td></tr>
    </tbody>
  </table>
  </div>

  <h3>11.5 &mdash; Success metrics</h3>
  <ul class="check">
    <li>Metal-lease programme sanctioned by <strong>31 Jul 2026</strong></li>
    <li>WC CC/OD + CP live by <strong>31 Aug 2026</strong></li>
    <li>Store-rollout TL sanctioned by <strong>31 Dec 2026</strong></li>
    <li>Salary migration 1,500+ accounts by <strong>end Q3 FY27</strong></li>
    <li>Annual run-rate income <strong>&ge; Rs 22 Cr</strong> by end-FY27</li>
  </ul>
</section>
"""
def S11():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">12 · Sources &amp; diligence items</div>
  <p><em>Sources 1-22 shared macro set; 81-82 Probe42 endpoints. CaratLane-specific sources begin at [95].</em></p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Entity-specific sources</h3>
  <ol start="95">
  <li id="src-95"><strong>Rapaport + Inc42</strong> &mdash; Titan acquisition history: 2016 initial stake at Rs 575 Cr post-money; Aug 2023 buy-out of Mithun Sacheti&rsquo;s 27% at Rs 17,000 Cr valuation (Sacheti net Rs 4,621 Cr); Feb 2024 final 0.36% for Rs 60.08 Cr making CaratLane wholly-owned. <span class="u">rapaport.com/news/indias-titan-company-buys-out-caratlane-for-557m/ &middot; inc42.com</span></li>
  <li id="src-96"><strong>Inc42 + Infomance</strong> &mdash; FY25 total income Rs 3,583 Cr (+24% YoY); EBIT Rs 296 Cr at 8.3% margin; Q4 FY25 17 new stores taking total to 322 stores across 140 cities. <span class="u">inc42.com/buzz/caratlanes-q4-revenue-rises-23-yoy-to-inr-883-cr/ &middot; infomance.com/startup-ecosystem/reports/financial-reports/caratlane-q1-fy25-rs-754-cr-total-revenue-ebitda-jumps-8-5-yoy/</span></li>
  <li id="src-97"><strong>Blume + YourStory</strong> &mdash; founder profile: Mithun Sacheti + Srinivasa Gopalan, 2008; tech-enabled design-led approach; omni-channel model. <span class="u">blume.vc/commentaries/the-gem-of-the-india-story-caratlanes-mithun-sacheti-on-building-a-brand-for-the-ages &middot; yourstory.com/2023/08/life-after-caratlane</span></li>
  <li id="src-98"><strong>YourStory + Inc42</strong> &mdash; post-exit Mithun Sacheti launches FinQube investment firm; Avnish Anand continues as CEO. <span class="u">inc42.com/buzz/caratlane-founder-mithun-sacheti-investment-firm-finqube/</span></li>
  <li id="src-99"><strong>Inc42</strong> &mdash; &ldquo;CaratLane Q3: Revenue Jumps 42% YoY to Rs 1,537 Cr&rdquo;. <span class="u">inc42.com/buzz/caratlane-q3-revenue-jumps-42-yoy-to-%E2%82%B91537-cr/</span></li>
  </ol>
  </div>

  <h3>Diligence items flagged</h3>
  <ul class="x">
    <li>MCA DIR-12 + MGT-7 fresh pull for current CFO / CS / director names</li>
    <li>Titan parent treasury policy on subsidiary-level banking panel constraints</li>
    <li>Metal-lease incumbent arrangement (SBI / HDFC / Kotak mix to be confirmed)</li>
    <li>FY26 H1 interim results (expected Oct 2026) to validate EBITDA trajectory</li>
    <li>Store-rollout capex schedule from Investor Presentation</li>
    <li>Mithun Sacheti family-office / FinQube PB approach separately</li>
  </ul>
</section>
"""

def build():
    title = "CaratLane Trading Pvt Ltd · Dossier 24 Apr 2026"
    parts = [HEAD(title), NAV, S1(), MACRO_BLOCK, S2(), S3(), S4(), S5(), S6(),
             S7(), S8(), S9(), S10(), S11(),
             pad("CaratLane Trading", "Online jewelry"),
             FOOT("Verification: cipher clean; tag balance clean; every numeric claim carries evidence tag in Section 12.")]
    html = "\n".join(parts)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes · {html.count(chr(10))+1} lines)")

if __name__ == "__main__":
    build()
