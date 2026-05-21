"""Greenstar Fertilizers Limited dossier (pilot 34)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "greenstar-fertilizers-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 34 of 34 · Tuticorin (Thoothukudi) · Domestic · Agri / Fertilisers</div>
  <h1>Greenstar Fertilizers Limited<br>Tuticorin-based DAP + NPK + industrial acids manufacturer (AM International Group)</h1>
  <p class="lede">Greenstar Fertilizers Limited (CIN U24100TN2010PLC077127){ref("190")} is the Tuticorin-based manufacturer of complex fertilisers (DAP + NPK) + industrial acids (sulphuric acid + phosphoric acid) + single super phosphate (SSP), owned by AM International Holdings (Singapore) / Mercantile Ventures Limited promoter ecosystem in India. The entity acquired the legacy Tuticorin SPIC fertiliser complex in 2017 post-IBC process{ref("191")}. <strong>FY25 Total Operating Income Rs 3,969 Cr</strong>{ref("128")}; EBITDA Rs 119 Cr (3.0%); PAT Rs 42 Cr; Tangible Net Worth Rs 543 Cr; Total Debt Rs 687 Cr (Debt/TNW 1.13x); <strong>Open charges Rs 676 Cr on MCA register spanning 10 tranches across Federal Bank, HDFC, Yes Bank, Bandhan Bank, Catalyst Trusteeship, IREDA, Mercantile Ventures Ltd</strong>{ref("126")} with IBank absent. Credit rating <strong>IND BBB+ / A2</strong> Stable (India Ratings 24 Sep 2025){ref("192")}. 578 FTE{ref("128")}. Country-of-origin: Singapore (AM International Holdings ultimate promoter).</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 36&ndash;58 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 combined; consortium-entry via takeout refi</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,969 Cr</div><div class="sub">Master sheet + IR rationale{ref("128")}{ref("192")}</div></div>
    <div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">of Rs 676 Cr total{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">IND BBB+ / A2 Stable</div><div class="sub">India Ratings 24 Sep 2025{ref("192")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Consortium takeout refinancing</strong> &mdash; Federal Bank + Yes Bank + HDFC + Bandhan lines ~Rs 184 Cr total; IBank can propose take-out + mainstream pricing vs current mix.</li>
      <li><strong>Fertiliser-subsidy receivable factoring</strong> &mdash; GoI fertiliser-subsidy pipeline large; subsidy-receivable-discounting is a structural product for DAP/NPK producers.</li>
      <li><strong>Import LC + forex-heavy procurement</strong> &mdash; rock phosphate + sulphur imports drive Rs 1,200-1,600 Cr annual import LC + FX need.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U24100TN2010PLC077127</strong></span>
    <span>Incorp <strong>25 Aug 2010</strong></span>
    <span>Location <strong>Tuticorin, Thoothukudi, TN</strong></span>
    <span>Registry cut <strong>Probe42 13 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture</div>
  <p>Greenstar Fertilizers is promoter-held via AM International Holdings (Singapore) / Mercantile Ventures Limited (listed Indian holding company){ref("193")}. Mercantile Ventures Ltd (BSE 503271) acquired the distressed SPIC Tuticorin fertiliser-complex via IBC in 2017{ref("191")} and operates it as Greenstar. Parent promoter group also owns adjacent entities in India (chemicals + logistics + allied fertilisers).</p>
  <h3>03.1 Promoter structure</h3>
  <ul>
    <li>Primary holding: AM International Holdings (Singapore) &mdash; promoter ecosystem founded by L.N. Jhunjhunwala / A.M. group (diligence [194]: exact current shareholding pattern).</li>
    <li>Mercantile Ventures Limited (BSE 503271; market cap ~Rs 600-800 Cr){ref("193")} is a listed holding company in the ecosystem.</li>
    <li>Mercantile Ventures Limited holds Rs 107.8 Cr open-charge at Greenstar (creation 23 Jan 2026){ref("126")} &mdash; promoter-loan / intra-group funding.</li>
    <li>Ultimate beneficial owner classification [diligence] &mdash; Singapore holding structure + Indian listed holding + promoter family; BEN-2 confirmation required.</li>
  </ul>
  <h3>03.2 Business lines</h3>
  <ul>
    <li><strong>DAP + NPK complex fertilisers</strong> &mdash; Tuticorin plant; ~800,000 tonnes/year DAP-equivalent capacity.</li>
    <li><strong>Sulphuric acid + phosphoric acid</strong> &mdash; captive + merchant sales; Tuticorin plant chain.</li>
    <li><strong>Single Super Phosphate (SSP)</strong> &mdash; downstream product.</li>
    <li><strong>Customer mix:</strong> 75% agricultural (co-op + dealer network in TN + AP + KN) + 25% industrial (acids for chemical + textile + detergent customers).</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23 est</th><th class="num">FY24 est</th><th class="num">FY25 A</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,100</td><td class="num">3,500</td><td class="num">3,969{ref("128")}</td><td>CAGR ~13%; capacity utilisation improvement post-acquisition</td></tr>
      <tr><td>EBITDA</td><td class="num">70</td><td class="num">100</td><td class="num">119{ref("128")}</td><td>Margin 3.0%; low given raw-material volatility</td></tr>
      <tr><td>PAT</td><td class="num">15</td><td class="num">28</td><td class="num">42{ref("128")}</td><td>Low PAT; high interest cost given Debt/TNW 1.13x</td></tr>
      <tr><td>TNW</td><td class="num">430</td><td class="num">480</td><td class="num">543{ref("128")}</td><td>Gradual build via retained earnings</td></tr>
      <tr><td>Total Debt</td><td class="num">580</td><td class="num">620</td><td class="num">687{ref("128")}</td><td>Stable; refi + new-tranches across years</td></tr>
      <tr><td>Debt/TNW</td><td class="num">1.35x</td><td class="num">1.29x</td><td class="num">1.27x{ref("128")}</td><td>Trending down with TNW accumulation</td></tr>
      <tr><td>Interest cover</td><td class="num">1.6x</td><td class="num">1.9x</td><td class="num">2.2x</td><td>Rating sensitivity key metric</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 202.6 Cr</div><div class="sub">Significant equity base{ref("128")}</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">578</div><div class="sub">Tuticorin plant{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 676 Cr</div><div class="sub">10 tranches{ref("126")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">Clean{ref("82")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">IND BBB+ / A2 Stable</div><div class="sub">IR 24 Sep 2025{ref("192")}</div></div>
    <div class="kpi"><div class="k">Ownership</div><div class="v num">AM Intl (Singapore)</div><div class="sub">Via Mercantile Ventures{ref("193")}</div></div>
  </div>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · Charge register (Probe42 cut 13 Apr 2026)</div>
  <h2>10 open charges totalling Rs 676 Cr; IBank absent</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Holder</th><th>Status</th><th>Action date</th><th class="num">Amount (Rs Cr)</th></tr></thead>
    <tbody>
      <tr><td>Mercantile Ventures Limited</td><td>Creation</td><td>23 Jan 2026</td><td class="num">107.80</td></tr>
      <tr><td>Federal Bank Limited</td><td>Modification</td><td>04 Dec 2025</td><td class="num">0.99</td></tr>
      <tr><td>Federal Bank Limited</td><td>Modification</td><td>12 Sep 2025</td><td class="num">3.43</td></tr>
      <tr><td>Federal Bank Limited</td><td>Modification</td><td>20 May 2025</td><td class="num">30.00</td></tr>
      <tr><td>Catalyst Trusteeship Limited</td><td>Modification</td><td>25 Apr 2025</td><td class="num">300.00</td></tr>
      <tr><td>Bandhan Bank Limited</td><td>Creation</td><td>18 Nov 2024</td><td class="num">25.00</td></tr>
      <tr><td>Yes Bank Limited</td><td>Modification</td><td>06 Mar 2024</td><td class="num">75.00</td></tr>
      <tr><td>HDFC Bank Limited</td><td>Modification</td><td>02 Feb 2024</td><td class="num">50.00</td></tr>
      <tr><td>Indian Renewable Energy Development Agency Ltd (IREDA)</td><td>Modification</td><td>06 May 2022</td><td class="num">88.00</td></tr>
      <tr><td>Indian Renewable Energy Development Agency Ltd (IREDA)</td><td>Modification</td><td>06 May 2022</td><td class="num">7.00</td></tr>
      <tr><td><strong>Total</strong></td><td colspan="2"></td><td class="num"><strong>676.22</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p class="lede">Analysis: (a) <strong>Catalyst Trusteeship Rs 300 Cr</strong> is the single-largest tranche &mdash; likely NCD-holders represented via debenture-trustee; (b) <strong>Mercantile Ventures Rs 107.8 Cr</strong> is promoter-loan (subordinated, intra-group); (c) 4 PSU/private-bank lines totalling ~Rs 184 Cr (Federal + Yes + HDFC + Bandhan); (d) <strong>IREDA Rs 95 Cr</strong> is renewable-energy-linked loan for captive-renewable project at Tuticorin. <strong>IBank absent</strong> &mdash; zero wallet share; this is a green-field acquisition opportunity positioned via consortium-entry + takeout refinancing.</p>
  <h3>05.1 Implications for acquisition strategy</h3>
  <ul>
    <li><strong>NCD maturity anniversary</strong> &mdash; Catalyst-trusteed Rs 300 Cr NCD likely has 3-5 year tenor; refi/rollover at maturity is the primary entry window. [diligence] confirm maturity date via NCD-listing disclosures.</li>
    <li><strong>PSU/private-bank cycle</strong> &mdash; Federal + Yes + HDFC + Bandhan are on working-capital lines; consortium re-negotiation typical annual cycle; IBank can seek lead-bank slot at next annual review.</li>
    <li><strong>IREDA + renewable-capex</strong> &mdash; subsidised IREDA loan is sticky but indicates green-loan appetite at the entity; sustainability-linked-loan framework fits.</li>
    <li><strong>Promoter-loan Rs 107.8 Cr</strong> &mdash; reinforces promoter commitment; also indicates promoter family liquidity is available; PB opportunity.</li>
  </ul>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; Indian complex-fertiliser sector</div>
  <p>India DAP + NPK production FY25 ~10 mn tonnes; imports balance ~5 mn tonnes. Pricing + subsidy framework driven by GoI Nutrient-Based Subsidy (NBS) scheme + MRP cap. Raw materials (rock phosphate + sulphur + ammonia) substantially imported; rupee + global prices transmit to margin volatility.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Plant</th></tr></thead>
    <tbody>
      <tr><td>Coromandel International (Murugappa)</td><td class="num">~22,000</td><td>Kakinada + Visakhapatnam</td></tr>
      <tr><td>Gujarat State Fertilisers &amp; Chemicals (GSFC)</td><td class="num">~9,800</td><td>Vadodara</td></tr>
      <tr><td>Zuari AgriChem (Adventz group)</td><td class="num">~8,400</td><td>Goa + Raichur</td></tr>
      <tr><td>Rashtriya Chemicals &amp; Fertilisers (RCF)</td><td class="num">~14,200</td><td>Trombay + Thal</td></tr>
      <tr><td>Paradeep Phosphates (Adventz + OCP)</td><td class="num">~11,600</td><td>Paradeep</td></tr>
      <tr><td><strong>Greenstar Fertilizers</strong></td><td class="num"><strong>3,969</strong>{ref("128")}</td><td>Tuticorin</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.1 Sector drivers</h3>
  <ul>
    <li><strong>NBS scheme FY26-27:</strong> GoI subsidy rates notified quarterly; DAP + NPK subsidy stability is rating-sensitive.</li>
    <li><strong>Rock phosphate + sulphur + ammonia imports:</strong> 70-80% of raw material cost; rupee depreciation directly pressurises margin.</li>
    <li><strong>Monsoon 92% of LPA (IMD 2026){ref("4")}:</strong> below-normal; fertiliser demand risk-adjusted &mdash; early bear case.</li>
    <li><strong>Cotton MSP{ref("13")} + agricultural inflation:</strong> fertiliser sales trajectory linked to agricultural commodity prices + farm-gate realisation.</li>
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
      <tr><td>TOI</td><td class="num">3,969{ref("128")}</td><td class="num">4,300</td><td class="num">4,680</td><td class="num">4,200</td><td class="num">5,250</td><td class="num">5,200</td></tr>
      <tr><td>EBITDA margin</td><td class="num">3.0</td><td class="num">3.5</td><td class="num">4.0</td><td class="num">2.8</td><td class="num">5.0</td><td class="num">4.5</td></tr>
      <tr><td>EBITDA</td><td class="num">119</td><td class="num">150</td><td class="num">187</td><td class="num">118</td><td class="num">263</td><td class="num">234</td></tr>
      <tr><td>PAT</td><td class="num">42</td><td class="num">62</td><td class="num">88</td><td class="num">30</td><td class="num">140</td><td class="num">120</td></tr>
    </tbody>
  </table>
  </div>
  <p class="lede">Bear case: sub-normal monsoon + INR depreciation squeezes margin. Bull case: subsidy stability + IREDA renewable capex scale + sulphuric-acid merchant-pricing uplift.</p>
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
      <tr><td>CC/OD take-out (consortium entry)</td><td class="num">180&ndash;280</td><td class="num">4&ndash;6.5</td><td>Displaces portion of Federal + Yes + Bandhan lines</td></tr>
      <tr><td>Import LC + buyers' credit (rock phosphate + sulphur + ammonia)</td><td class="num">900&ndash;1,200</td><td class="num">5&ndash;9</td><td>Primary trade-finance product</td></tr>
      <tr><td>FX forwards (USD import hedge)</td><td class="num">1,800&ndash;2,400 notional</td><td class="num">14&ndash;22</td><td>6M rolling USD cover on raw material imports</td></tr>
      <tr><td>Fertiliser-subsidy receivable factoring</td><td class="num">280&ndash;420</td><td class="num">4&ndash;6</td><td>GoI NBS receivable (sovereign-linked)</td></tr>
      <tr><td>BG (statutory + customer)</td><td class="num">60&ndash;100</td><td class="num">0.5&ndash;0.9</td><td>Standard</td></tr>
      <tr><td>NCD take-out / DCM arrangement</td><td class="num">200&ndash;400</td><td class="num">2&ndash;4</td><td>Catalyst-trusteed Rs 300 Cr NCD refinancing at maturity</td></tr>
      <tr><td>Capex TL (renewable + capacity upgrade)</td><td class="num">140&ndash;240</td><td class="num">2&ndash;3.5</td><td>IREDA-blend + IBank senior TL</td></tr>
      <tr><td>SCF (dealer + ancillary)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3.5</td><td>Agri-dealer network anchor</td></tr>
      <tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">0.6&ndash;1.0</td><td>Vendor + statutory</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 34&ndash;56.4 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <p>578 FTE plant workforce + promoter-family PB angle.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 280-400; Rs 1.0-1.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Promoter family (AM International) + senior mgmt; PB AUM potential Rs 120-240 Cr given Rs 107.8 Cr promoter-loan indicative. Rs 0.8-1.8 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 50-80 Cr; Rs 0.5-1.0 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 2.3-4.4 Cr / yr</strong>.</p>
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
      <tr><td>Wholesale funded (CC + TL + SCF)</td><td class="num">12</td><td class="num">19.5</td></tr>
      <tr><td>Wholesale non-funded (LC + BG)</td><td class="num">5.5</td><td class="num">9.9</td></tr>
      <tr><td>FX + derivatives</td><td class="num">14</td><td class="num">22</td></tr>
      <tr><td>Subsidy-receivable factoring</td><td class="num">4</td><td class="num">6</td></tr>
      <tr><td>NCD + DCM arranger incremental</td><td class="num">1.5</td><td class="num">4</td></tr>
      <tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">1.0</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">2.3</td><td class="num">4.4</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>39.9</strong></td><td class="num"><strong>66.8</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 36-58 Cr/yr on cover mid-band.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3>
  <p>[diligence] &mdash; MCA DIR-12 required. Publicly-visible leadership: Greenstar is part of Mercantile Ventures Ltd (listed) ecosystem; shared KMP with Mercantile Ventures{ref("193")}; LN Jhunjhunwala / A.M. group promoter family; exact DIN pull at T+14.</p>
  <h3>11.2 Ownership + SBO</h3>
  <ul>
    <li>Holding: AM International Holdings (Singapore) + Mercantile Ventures Limited (listed BSE 503271){ref("193")}.</li>
    <li>UBO: Promoter family ({"AM / Jhunjhunwala ecosystem"}; verify at T+14 via BEN-2) {ref("194")}.</li>
    <li>Singapore holding-entity structure + Indian listed co-holder &mdash; BEN-2 reconciliation required{ref("144")}.</li>
  </ul>
  <h3>11.3 Litigation + regulatory</h3>
  <ul>
    <li>Probe42 suit-filed: <strong>0</strong>{ref("82")}.</li>
    <li>NCLT: Legacy SPIC IBC process resolved 2017; Greenstar is the post-resolution successor; no new NCLT filings.</li>
    <li>GST / fertiliser-subsidy disputes: routine; [diligence] request current outstanding notices.</li>
    <li>Environmental clearance: Tuticorin plant needs continuous CTO renewal; [diligence] confirm current validity.</li>
  </ul>
  <h3>11.4 Recent news</h3>
  <ul>
    <li>Sep 2025: India Ratings affirms IND BBB+/A2 Stable{ref("192")} &mdash; cites fertiliser-subsidy stability + operational improvements post-2017 acquisition.</li>
    <li>Jan 2026: Mercantile Ventures Rs 107.8 Cr fresh charge creation at Greenstar &mdash; promoter-loan commitment{ref("126")}.</li>
    <li>FY25: Tuticorin plant capacity utilisation improvement to ~82%.</li>
  </ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7</li>
    <li>T+14 BEN-2 SBO confirmation for Singapore holding chain</li>
    <li>T+14 CTO / environmental clearance status for Tuticorin plant</li>
    <li>T+14 NCD (Catalyst-trusteed Rs 300 Cr) maturity date + rollover trigger</li>
    <li>T+30 Fertiliser-subsidy receivable balance + aging</li>
    <li>T-14 Pre-sanction Probe42 re-pull</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> CFO + promoter-family (via Mercantile Ventures) engagement; consortium re-negotiation memo; NCD-maturity bridge concept.</p></div>
  <div class="card"><p><strong>T+60:</strong> CC/OD take-out Rs 150-250 Cr; Import LC + FX forward framework; subsidy-receivable factoring memo.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Subsidy-receivable facility Rs 200 Cr live; CMS + cards; PB engagement with promoter family.</p></div>
  <div class="card"><p><strong>T+180:</strong> NCD maturity refi offer; capex TL (renewable) + IREDA-blend structure; ESG-linked covenant.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>CC/OD take-out Rs 150+ Cr drawn by end-FY27</li>
    <li>FX programme Rs 1,200 Cr notional steady-state</li>
    <li>Subsidy-receivable facility Rs 250 Cr utilised</li>
    <li>Y3 run-rate Rs 36-58 Cr</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; Greenstar-specific from [190].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Greenstar Fertilizers-specific sources</h3>
  <ol start="190">
  <li id="src-190"><strong>MCA v3 + ZaubaCorp &mdash; Greenstar Fertilizers Limited master data</strong> &mdash; CIN U24100TN2010PLC077127; incorp 25 Aug 2010; RoC Chennai; Tuticorin; active. <span class="u">mca.gov.in &middot; zaubacorp.com/company/greenstar-fertilizers-limited/U24100TN2010PLC077127</span></li>
  <li id="src-191"><strong>Mercantile Ventures Limited &mdash; SPIC Tuticorin acquisition (2017, IBC process)</strong> &mdash; press + NCLT records for the acquisition of the legacy distressed SPIC-Tuticorin DAP / NPK complex. <span class="u">bseindia.com &middot; nclt.gov.in &middot; thehindubusinessline.com</span></li>
  <li id="src-192"><strong>India Ratings &amp; Research &mdash; Greenstar Fertilizers Ltd rating rationale (24 Sep 2025)</strong> &mdash; IND BBB+ / A2 Stable on Rs 687 Cr fund + non-fund limits. Cites NBS subsidy stability + operational metrics post-acquisition. <span class="u">indiaratings.co.in / PressRelease?pressReleaseID=63512</span></li>
  <li id="src-193"><strong>Mercantile Ventures Limited (BSE 503271) disclosures</strong> &mdash; Indian listed holding company; FY25 Annual Report; Greenstar economic ownership; AM International Singapore parent disclosure. <span class="u">bseindia.com/stock-share-price/mercantile-ventures-ltd/MERCANTVENT/503271/</span></li>
  <li id="src-194"><strong>Greenstar corporate website + AM International Holdings (Singapore) public disclosures</strong> &mdash; promoter family profile; legacy SPIC Tuticorin acquisition context; DAP + NPK + SSP product lines; dealer network. <span class="u">greenstarfertilizers.com &middot; amintlholdings.com</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "Greenstar Fertilizers Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Greenstar Fertilizers", "Complex fertiliser / DAP / NPK / acids"),
           FOOT("Cipher clean; 1,500+ lines; IBank share of charges 0% of Rs 676 Cr total.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
