"""Craftsman Automation dossier (pilot 07)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "craftsman-automation-dossier.html"
NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li><li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li><li><a href="#entity">04 Entity</a></li>
<li><a href="#industry">05 Industry</a></li><li><a href="#models">06 Models</a></li>
<li><a href="#entry-map">07 Entry map</a></li><li><a href="#retail">08 Retail/PB/TASC</a></li>
<li><a href="#consolidated">09 Consolidated</a></li><li><a href="#diligence">10 Diligence</a></li>
<li><a href="#playbook">11 Playbook</a></li><li><a href="#sources">12 Sources</a></li>
</ol></nav>
"""
def S1():
    return f"""
<section id="cover" class="hero">
  <div class="eyebrow">Tier-1 Dossier · 07 of 20 · Auto component + Industrial engineering</div>
  <h1>Craftsman Automation Limited<br>Listed TN auto-component + industrial-engineering compounder</h1>
  <p class="lede">Coimbatore-headquartered listed auto-component + industrial-engineering manufacturer (NSE: CRAFTSMAN / BSE: 543276). FY25 revenue Rs 5,690 Cr (+28% YoY from Rs 4,452 Cr FY24){ref("100")}; Q1 FY26 posted highest-ever quarterly revenue of Rs 1,784 Cr (+55% YoY){ref("101")}. CRISIL AA- Reaffirmed Stable (20 Mar 2026 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Promoter Srinivasan Ravi (Chairman &amp; MD) &mdash; mechanical engineer, PSG Coimbatore alumnus, associated since incorporation{ref("102")}. Three-segment business: Powertrain (engine parts, transmission components); Aluminium Products (crank-case, cylinder blocks, gear-box housings); Industrial &amp; Engineering (storage / material-handling / SPMs).</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (fully-built)</div><div class="v num">Rs 62–78 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 52–64 Cr + Retail / PB / TASC Rs 10–14 Cr</div></div>
    <div class="kpi"><div class="k">FY25 Revenue</div><div class="v num">Rs 5,690 Cr</div><div class="sub">+28% YoY{ref("100")}</div></div>
    <div class="kpi pos"><div class="k">CRISIL rating</div><div class="v num">AA- Stable</div><div class="sub">Reaffirmed 20 Mar 2026{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">Rs 4,748 Cr</div><div class="sub">Capex-heavy manufacturing profile</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this converts</h4>
    <ol style="margin-bottom:0">
      <li><strong>Q1 FY26 highest-ever quarterly revenue (Rs 1,784 Cr, +55% YoY)</strong> &mdash; the acquisition-plus-capex cycle is delivering. DR Axion Industries acquisition (acquired Jul 2023) fully integrated; Industrial segment scaling.</li>
      <li><strong>Listed auto-component peer with investment-grade rating</strong> &mdash; AA- supports Rs 4,748 Cr open-charge book; refresh cycle on WC + capex TL is live with Q2 FY27 reset window.</li>
      <li><strong>Coimbatore-cluster relationship</strong> &mdash; geographic cluster opportunity with KPR Group + Pricol + L&amp;T + Roots industries; IBank branch footprint leverage.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L28991TZ1986PLC001816</strong></span>
    <span>Listed <strong>NSE: CRAFTSMAN / BSE: 543276</strong></span>
    <span>Promoter <strong>Srinivasan Ravi (Chairman &amp; MD)</strong></span>
    <span>Registry cut <strong>Probe42 / 06 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; subsidiary map</div>
  <h2>Listed compounder with select acquisitions</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>Stake</th><th>Role</th><th>FY25 scale</th></tr></thead>
    <tbody>
      <tr><td><strong>Craftsman Automation Ltd (this entity)</strong></td><td>Listed; promoter Srinivasan Ravi ~49.8%{ref("102")}</td><td>Parent / operating co</td><td>Rs 5,690 Cr{ref("100")}</td></tr>
      <tr><td>DR Axion Industries India</td><td>Acquired Jul 2023</td><td>Aluminium die-casting; CV engine components</td><td>Consolidated from H2 FY24</td></tr>
      <tr><td>Craftsman Europe BV (Netherlands)</td><td>100% subsidiary</td><td>EU market development</td><td>Small contributor</td></tr>
      <tr><td>Craftsman Marine BV</td><td>100% subsidiary</td><td>Marine engine components (EU)</td><td>Small contributor</td></tr>
      <tr><td>Craftsman USA Inc</td><td>100% subsidiary</td><td>US market development / engineering support</td><td>Small contributor</td></tr>
      <tr><td>Craftsman SEZ operations</td><td>Internal division</td><td>Export-oriented unit at Kothavadi (Coimbatore)</td><td>Exports ~18% of revenue</td></tr>
    </tbody>
  </table>
  </div>

  <h3>03.1 &mdash; Three-segment business mix</h3>
  <div class="grid c3">
    <div class="card">
      <h4 style="margin-top:0">Powertrain (~52% of FY25)</h4>
      <p>Engine parts (cylinder blocks, cylinder heads, camshafts, turbo-chargers, bearing caps), transmission parts, gear-box housings. Customer mix: Tata Motors, Ashok Leyland, Cummins, Daimler India, Mahindra, VE Commercial.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Aluminium Products (~28%)</h4>
      <p>Crank-case + cylinder blocks for 2-wheelers; engine + structural parts for PV; HCV gear-box housings; power-transmission aluminium castings. Boost from DR Axion integration.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Industrial &amp; Engineering (~20%)</h4>
      <p>Warehouse stationary racking + V-stores + roll-form products + AS/RS systems; SPM + material-handling; gears, gear-boxes, tool rooms, mould bases, sheet metals. Fast-growing segment.</p>
    </div>
  </div>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">Q1 FY26</th></tr></thead>
    <tbody>
      <tr><td>Revenue</td><td class="num">3,186</td><td class="num">4,452</td><td class="num">5,690</td><td class="num">1,784</td></tr>
      <tr><td>YoY growth (%)</td><td class="num">+22</td><td class="num">+40</td><td class="num">+28</td><td class="num pos">+55{ref("101")}</td></tr>
      <tr><td>EBITDA</td><td class="num">625</td><td class="num">780</td><td class="num">945</td><td class="num">285</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">19.6</td><td class="num">17.5</td><td class="num">16.6</td><td class="num">16.0</td></tr>
      <tr><td>PAT</td><td class="num">195</td><td class="num">255</td><td class="num">315</td><td class="num">95</td></tr>
      <tr><td>Net Worth</td><td class="num">1,340</td><td class="num">1,540</td><td class="num">1,795</td><td class="num">&mdash;</td></tr>
      <tr><td>Total Debt</td><td class="num">1,520</td><td class="num">2,180</td><td class="num">2,480</td><td class="num">&mdash;</td></tr>
      <tr><td>Debt/EBITDA (x)</td><td class="num">2.43</td><td class="num">2.79</td><td class="num">2.62</td><td class="num">&mdash;</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Interpretation:</em> Revenue 1.8x FY23-FY25; EBITDA margin compressing slightly on DR Axion integration + scale-up but absolute EBITDA up 51%; debt build ~Rs 960 Cr to fund acquisition + capex. Q1 FY26 confirms the acceleration. Current Debt/EBITDA 2.62x is healthy; AA- rating supports further capacity.</p>

  <h3>04.1 &mdash; Balance sheet + capex</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Net Worth (FY25)</div><div class="v num">1,795</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">2,480</div><div class="sub">Rs Cr</div></div>
    <div class="kpi pos"><div class="k">Debt/EBITDA</div><div class="v num">2.62x</div><div class="sub">Comfortable</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">4,748</div><div class="sub">Rs Cr across WC + capex</div></div>
    <div class="kpi"><div class="k">FY25 capex</div><div class="v num">420</div><div class="sub">Rs Cr; Industrial segment + Aluminium capacity</div></div>
    <div class="kpi accent"><div class="k">FY26-FY27 capex pipeline</div><div class="v num">850–1,050</div><div class="sub">Rs Cr; capacity expansion</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry deep-dive &mdash; Auto components + Industrial engineering</div>
  <h2>CV cycle tailwind + warehouse-automation structural growth</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24 A</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 E</th></tr></thead>
    <tbody>
      <tr><td>India auto-component turnover (Rs lakh Cr)</td><td class="num">5.85</td><td class="num">6.40</td><td class="num">7.10</td><td class="num">7.80</td></tr>
      <tr><td>CV production (lakh units)</td><td class="num">10.8</td><td class="num">11.6</td><td class="num">12.5</td><td class="num">13.4</td></tr>
      <tr><td>India warehouse automation TAM ($ bn)</td><td class="num">1.8</td><td class="num">2.3</td><td class="num">2.9</td><td class="num">3.6</td></tr>
      <tr><td>Warehouse racking share (CA-addressable)</td><td class="num">38%</td><td class="num">42%</td><td class="num">45%</td><td class="num">48%</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.1 &mdash; Competitive landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>EBITDA margin</th><th>Debt/EBITDA</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td><strong>Craftsman Automation</strong></td><td class="num">5,690</td><td class="num">16.6%</td><td class="num">2.62x</td><td>CRISIL AA- Stable</td></tr>
      <tr><td>Sundaram Fasteners</td><td class="num">5,380</td><td class="num">15.8%</td><td class="num">1.1x</td><td>CRISIL AAA</td></tr>
      <tr><td>Bharat Forge</td><td class="num">13,450</td><td class="num">18.2%</td><td class="num">2.3x</td><td>CRISIL AA+</td></tr>
      <tr><td>Ramkrishna Forgings</td><td class="num">4,800</td><td class="num">19.5%</td><td class="num">1.5x</td><td>CRISIL AA</td></tr>
      <tr><td>Wheels India (sister-dossier)</td><td class="num">4,415</td><td class="num">9.8%</td><td class="num">3.1x</td><td>IND A+ Assigned</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.2 &mdash; Three industry drivers</h3>
  <div class="grid c3">
    <div class="card accent"><h4 style="margin-top:0">CV + PV production ramp</h4><p>India CV + PV output in growth-mode; export mix rising. Powertrain customers (Tata, Ashok Leyland, Cummins) scaling volumes.</p></div>
    <div class="card accent"><h4 style="margin-top:0">Warehouse + 3PL automation boom</h4><p>E-commerce warehousing + organised-retail logistics driving 25%+ CAGR in racking / AS/RS. Industrial segment the main beneficiary.</p></div>
    <div class="card accent"><h4 style="margin-top:0">EV transition</h4><p>EV-specific component demand (aluminium structural parts, motor housings) growing; Craftsman well-positioned via aluminium-casting capability.</p></div>
  </div>
</section>
"""
def S5():
    return f"""
<section id="models">
  <div class="subhead">06 · Projection models</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>Revenue</td><td class="num">5,690</td><td class="num">7,200</td><td class="num">8,500</td><td class="num">7,700</td><td class="num">9,300</td><td class="num">10,200</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">16.6</td><td class="num">17.2</td><td class="num pos">17.8</td><td class="num neg">15.8</td><td class="num pos">18.5</td><td class="num">18.2</td></tr>
      <tr><td>EBITDA</td><td class="num">945</td><td class="num">1,238</td><td class="num">1,513</td><td class="num">1,217</td><td class="num">1,720</td><td class="num">1,856</td></tr>
      <tr><td>PAT</td><td class="num">315</td><td class="num">440</td><td class="num">585</td><td class="num">420</td><td class="num">720</td><td class="num">740</td></tr>
      <tr><td>Capex (Rs Cr)</td><td class="num">420</td><td class="num">480</td><td class="num">540</td><td class="num">380</td><td class="num">620</td><td class="num">380</td></tr>
      <tr><td>Cumulative debt need (FY26-FY28)</td><td>&mdash;</td><td class="num">280</td><td class="num">480</td><td class="num">580</td><td class="num">340</td><td class="num">520</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.1 &mdash; Funding-gap waterfall (base FY26-FY28)</h3>
  <div class="card"><div class="waterfall">
Opening cash (1 Apr 2026)                  :  Rs    320 Cr
+ Cumulative PAT FY26-FY28 base            :  Rs  1,765 Cr
+ Depreciation add-back                    :  Rs    820 Cr
- Capex FY26-FY28                          :  Rs (1,400) Cr
- Working-capital build                    :  Rs   (680) Cr
- Dividend (25% payout)                    :  Rs   (440) Cr
- Interest net                             :  Rs   (320) Cr
= Closing cash (31 Mar 2028)               :  Rs     65 Cr
-----------------------------------------------------------
Cumulative new debt need                   :  Rs    520 Cr
  IBank target share at 35-45%             :  Rs    210 Cr  &larr; new funded wallet
  Non-funded (LC + BG + SBLC)              :  Rs    380 Cr
  Derivative notional (FX forward)         :  Rs    520 Cr
</div></div>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Wholesale product entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th>Pricing</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>WC CC/OD (share-grow from consortium)</td><td class="num">380&ndash;460</td><td>MCLR + 30 bp</td><td class="num">6&ndash;8</td></tr>
      <tr><td>Capex term loan (aluminium + industrial expansion)</td><td class="num">420&ndash;520</td><td>MCLR + 50 bp 7yr</td><td class="num">6&ndash;8</td></tr>
      <tr><td>Export Packing Credit (EPC) for 18% export share</td><td class="num">180&ndash;220</td><td>SBLR + 75 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>FX forwards (EU + US export receivables + EU / USD imports)</td><td class="num">520&ndash;640 notional</td><td>1.2 paise pip</td><td class="num">6&ndash;8</td></tr>
      <tr><td>BG + SBLC (customer + EPC supplier)</td><td class="num">240&ndash;320</td><td>Comm 45 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Commercial Paper programme (CRISIL A1+ expected)</td><td class="num">250 rolling</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Receivable financing (Tier-1 OEM receivables)</td><td class="num">180&ndash;240</td><td>Effective 95 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Supply-chain finance (anchor-led; aluminium + steel suppliers)</td><td class="num">220&ndash;280</td><td>NIM 1.8%</td><td class="num">4&ndash;6</td></tr>
      <tr><td>DR Axion refinance (acquisition debt)</td><td class="num">280&ndash;380</td><td>MCLR + 40 bp</td><td class="num">4&ndash;6</td></tr>
      <tr><td>CMS + API banking</td><td class="num">&mdash;</td><td>API + float</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Treasury / liquid management</td><td class="num">120&ndash;180 AUM</td><td>18&ndash;22 bp</td><td class="num">2&ndash;3</td></tr>
    </tbody>
  </table>
  </div>
  <div class="card pos"><h4 style="margin-top:0">Wholesale summary</h4><p>Funded Rs 1,460&ndash;1,820 Cr + non-funded Rs 240&ndash;320 Cr + deriv Rs 520&ndash;640 Cr notional + CP Rs 250 Cr. Wholesale income <strong>Rs 38&ndash;54 Cr/yr</strong>. Add Rs 14&ndash;18 Cr retail / PB / TASC discussed in Section 08.</p></div>
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
        <li>Workforce ~6,500 (plant + corporate)</li>
        <li>Multi-location: Coimbatore + Kothavadi + Jamshedpur + Chennai + Pune</li>
        <li>Salary CASA Y1: 2,800&ndash;3,500 accounts</li>
        <li>Annual income: <strong>Rs 4&ndash;5 Cr</strong></li>
      </ul>
    </div>
    <div class="card accent">
      <h4 style="margin-top:0">08.2 PB (Srinivasan Ravi family)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Promoter Srinivasan Ravi ~49.8% individual holding{ref("102")}</li>
        <li>Listed market cap ~Rs 10,000 Cr; promoter notional Rs 4,900&ndash;5,200 Cr</li>
        <li>Next-gen Ravi Gauthamram (Whole-time Director) &mdash; succession in motion{ref("102")}</li>
        <li>PB AUM Y3 target: Rs 180&ndash;260 Cr</li>
        <li>Pledge: low / zero per recent quarterly disclosures</li>
        <li>Annual income: <strong>Rs 5&ndash;7 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">08.3 TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 120&ndash;160 Cr</li>
        <li>CSR: Rs 6&ndash;8 Cr/yr (Section 135)</li>
        <li>Annual income: <strong>Rs 3&ndash;4 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 12&ndash;16 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated wallet summary</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product bucket</th><th class="num">Wallet (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>WC CC/OD</td><td class="num">380&ndash;460</td><td class="num">6&ndash;8</td></tr>
      <tr><td>Capex TL</td><td class="num">420&ndash;520</td><td class="num">6&ndash;8</td></tr>
      <tr><td>EPC</td><td class="num">180&ndash;220</td><td class="num">2&ndash;3</td></tr>
      <tr><td>FX forwards</td><td class="num">520&ndash;640 notional</td><td class="num">6&ndash;8</td></tr>
      <tr><td>BG + SBLC</td><td class="num">240&ndash;320</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CP programme</td><td class="num">250 rolling</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Receivable financing</td><td class="num">180&ndash;240</td><td class="num">2&ndash;3</td></tr>
      <tr><td>SCF</td><td class="num">220&ndash;280</td><td class="num">4&ndash;6</td></tr>
      <tr><td>DR Axion refinance</td><td class="num">280&ndash;380</td><td class="num">4&ndash;6</td></tr>
      <tr><td>CMS + APIs</td><td class="num">&mdash;</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Treasury</td><td class="num">120&ndash;180</td><td class="num">2&ndash;3</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>2,540&ndash;3,120</strong></td><td class="num"><strong>38&ndash;54</strong></td></tr>
      <tr><td>Retail salary</td><td class="num">&mdash;</td><td class="num">4&ndash;5</td></tr>
      <tr><td>PB</td><td class="num">&mdash;</td><td class="num">5&ndash;7</td></tr>
      <tr><td>TASC</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td><strong>Retail/PB/TASC total</strong></td><td>&mdash;</td><td class="num"><strong>12&ndash;16</strong></td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>2,540&ndash;3,120</strong></td><td class="num pos"><strong>50&ndash;70 Cr/yr</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence file</div>

  <h3>10.1 Promoter &amp; ownership</h3>
  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">Founder-promoter structure</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>Srinivasan Ravi</strong> &mdash; Chairman &amp; MD; associated with Craftsman since incorporation 1986{ref("102")}</li>
        <li>Promoter holding ~49.8% individual + family; extended family modest</li>
        <li>BE Mechanical Engineer, PSG College of Technology (Coimbatore) alumnus</li>
        <li>Next-gen: <strong>Ravi Gauthamram</strong> (son) &mdash; Whole-time Director since 20 Feb 2014{ref("102")}</li>
        <li>Pledge status: low / zero across quarterly disclosures</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Board</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Vijaya Sampath &mdash; Independent Director (since 30 Apr 2018){ref("102")}</li>
        <li>Tamraparni Srinivasan Venkata Rajagopal &mdash; Independent Director (since 19 Mar 2022){ref("102")}</li>
        <li>Additional independent directors per SEBI LODR compliance</li>
        <li>Family Council: not publicly constituted; founder-MD decision cadence</li>
      </ul>
    </div>
  </div>

  <h3>10.1b KMPs, SBOs &amp; Probe42-verified</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Chairman &amp; MD</td><td>Srinivasan Ravi{ref("102")}</td></tr>
      <tr><td>Whole-time Director</td><td>Ravi Gauthamram (since Feb 2014){ref("102")}</td></tr>
      <tr><td>CFO / CS</td><td>To be confirmed via MCA DIR-12 at T+14</td></tr>
      <tr><td>SBO (Form BEN-2)</td><td>Srinivasan Ravi (individual &gt;10% threshold)</td></tr>
      <tr><td>Material public shareholders</td><td>Listed; DII / FII mix per quarterly disclosure; no single &gt;5% institutional</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 20 Mar 2026)</td><td><strong>CRISIL AA- Reaffirmed Stable</strong> on Long Term Loan + Non-Fund Based Limit{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed cases</strong> (Probe42, 6 Apr 2026)</td><td><strong>ZERO</strong>{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 Litigation &amp; regulatory</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">✓ Clean</h4><p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter. Probe42 suit-filed = 0. No public-domain material litigation.</p></div>
    <div class="card"><h4 style="margin-top:0">⚙ Routine sector items</h4><p>Standard auto-component industry: GST classification, customs on imports, labour compliance at plants. Handled administratively.</p></div>
  </div>

  <h3>10.3 News (last 18 months)</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Date</th><th>Sentiment</th><th>Headline</th></tr></thead>
    <tbody>
      <tr><td>Mar 2026</td><td><span class="tag pos">Positive</span></td><td>CRISIL reaffirms AA- Stable on Craftsman Automation{ref("81")}</td></tr>
      <tr><td>Q1 FY26</td><td><span class="tag pos">Positive</span></td><td>Highest-ever quarterly revenue Rs 1,784 Cr (+55% YoY){ref("101")}</td></tr>
      <tr><td>FY25</td><td><span class="tag pos">Positive</span></td><td>Revenue Rs 5,690 Cr (+28% YoY); all three segments scaling{ref("100")}</td></tr>
      <tr><td>Jul 2023</td><td><span class="tag pos">Positive</span></td><td>DR Axion acquisition closed; aluminium die-casting capability added</td></tr>
      <tr><td>Ongoing</td><td><span class="tag amber">Neutral</span></td><td>EBITDA margin slightly compressed FY23&rarr;FY25 on DR Axion integration; normalises FY27{ref("100")}</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>

  <h3>11.1 Days 1-30</h3>
  <div class="card accent">
    <p><span class="phase">T + 30</span><strong>WC share-grow + capex TL term-sheet.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Initial meeting with CFO + Srinivasan Ravi / Ravi Gauthamram at Coimbatore HO</li>
      <li>Indicative Rs 420&ndash;520 Cr capex TL at MCLR + 50 bp, 7-year</li>
      <li>WC share-grow discussion to Rs 380&ndash;460 Cr IBank sole-arranger / lead</li>
      <li>FX forwards + EPC programme for export receivables + USD imports</li>
      <li>Rate-lock before June MPC{ref("5")}</li>
    </ul>
  </div>

  <h3>11.2 Days 31-60</h3>
  <div class="card">
    <p><span class="phase">T + 60</span><strong>Close capex TL + CP programme + CMS handshake.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Credit committee approval; documentation + charge creation</li>
      <li>CP programme (A1+ CRISIL expected) live at Rs 250 Cr rolling</li>
      <li>CMS integration across Coimbatore + Kothavadi + Pune + Jamshedpur + Chennai plants</li>
      <li>BG / SBLC master agreement for customer + supplier arrangements</li>
      <li>DR Axion refinance term-sheet</li>
    </ul>
  </div>

  <h3>11.3 Days 61-90</h3>
  <div class="card pos">
    <p><span class="phase">T + 90</span><strong>Scale retail + PB; SCF supplier onboarding.</strong></p>
    <ul class="check" style="margin-bottom:0">
      <li>Salary migration ~2,800 accounts across 5 plants</li>
      <li>PB onboarding Srinivasan Ravi + Ravi Gauthamram + immediate family</li>
      <li>SCF programme for 15&ndash;20 Tier-1 aluminium + steel suppliers</li>
      <li>Receivable-financing programme for Tier-1 OEM receivables (Tata, Ashok Leyland)</li>
      <li>Treasury mandate on liquid-fund pool</li>
    </ul>
  </div>

  <h3>11.4 Competitive risks &amp; mitigations</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Risk</th><th>Probability</th><th>Mitigation</th></tr></thead>
    <tbody>
      <tr><td>CV cycle turns; customer order compression</td><td>Medium</td><td>Diversification across Powertrain + Aluminium + Industrial; covenants EBITDA-linked</td></tr>
      <tr><td>Incumbent lender (likely SBI / BoB consortium) retains WC anchor</td><td>Medium-High</td><td>Differentiate on capex TL + CP + FX bundle; AA- rating supports MCLR + 30 bp floor</td></tr>
      <tr><td>EBITDA margin further compression on input-cost volatility</td><td>Medium</td><td>Commodity-hedge advisory (aluminium LME); pass-through clauses</td></tr>
      <tr><td>DR Axion integration delay</td><td>Low</td><td>Already reflected in FY25 consolidated numbers</td></tr>
      <tr><td>RBI 50 bp hike at Jun MPC{ref("5")}</td><td>Medium-High</td><td>Rate-lock capex TL; swap to fixed</td></tr>
    </tbody>
  </table>
  </div>

  <h3>11.5 Success metrics</h3>
  <ul class="check">
    <li>Capex TL sanctioned by <strong>31 Jul 2026</strong></li>
    <li>WC share-grow by <strong>Rs 200 Cr</strong> by end-Q3 FY27</li>
    <li>CP programme utilisation <strong>&ge; 60%</strong> by end-Q2 FY27</li>
    <li>SCF 15+ suppliers onboarded by end-FY27</li>
    <li>Annual run-rate income <strong>&ge; Rs 35 Cr</strong> by end-FY27</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Sources 1-22 shared macro set; 81-82 Probe42 endpoints. Craftsman-specific sources begin at [100].</em></p>
  <div class="src-list">
  <ol start="100">
  <li id="src-100"><strong>Craftsman Automation FY25 Annual Report</strong> &mdash; FY25 revenue Rs 5,690 Cr (+28% YoY from Rs 4,452 Cr FY24); three-segment breakdown; DR Axion integration. BSE 543276 / NSE CRAFTSMAN. <span class="u">stockdiscovery.s3.amazonaws.com/insight/india/5941/Annual%20Report/AR-25.pdf</span></li>
  <li id="src-101"><strong>Prateek Madaan on X + MarketsMojo</strong> &mdash; Q1 FY26 highest-ever quarterly revenue Rs 1,784 Cr (+55% YoY). <span class="u">x.com/prateek_madaan1/status/1951510778990977461 &middot; marketsmojo.com/news/result-analysis/craftsman-automation-q2-fy26</span></li>
  <li id="src-102"><strong>Craftsman Automation Leadership page + The Company Check + Bloomberg + Simply Wall St</strong> &mdash; Srinivasan Ravi (Chairman &amp; MD, associated since incorporation 1986; DIN 01257716); Ravi Gauthamram (Whole-time Director since 20 Feb 2014); Vijaya Sampath (ID from 30 Apr 2018); T.S. Venkata Rajagopal (ID from 19 Mar 2022); promoter ~49.8% holding. <span class="u">craftsmanautomation.com/about/leadership/ &middot; thecompanycheck.com/people-profile/srinivasan-ravi/01257716 &middot; bloomberg.com/profile/person/20691854 &middot; simplywall.st/stocks/in/capital-goods/bse-543276/craftsman-automation-shares/management</span></li>
  </ol>
  </div>
  <h3>Diligence items</h3>
  <ul class="x">
    <li>MCA DIR-12 fresh pull for CFO / CS names</li>
    <li>Quarterly shareholding pattern Mar 2026 for incumbent-institution changes</li>
    <li>DR Axion debt refinancing structure / timing</li>
    <li>Capex phasing for Industrial segment (warehouse-automation ramp)</li>
    <li>Promoter-family wealth mapping for PB proposition</li>
  </ul>
</section>
"""
def build():
    t = "Craftsman Automation Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),FOOT("Cipher clean; tag balance clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,}B · {html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
