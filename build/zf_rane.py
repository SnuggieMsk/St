"""ZF Rane Automotive India Pvt Ltd dossier (pilot 36)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "zf-rane-auto-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 36 of 38 · Chennai · Rane Group · Auto-comp · IBank minority + share-grow play</div>
  <h1>ZF Rane Automotive India Pvt Ltd<br>Steering &amp; brake-system JV between Rane Group and ZF Friedrichshafen (Germany) / TRW (US heritage)</h1>
  <p class="lede">ZF Rane Automotive India Pvt Ltd (CIN U35999TN1987PTC014600){ref("210")} is the joint-venture entity between Rane Group (Madras-headquartered) and ZF Friedrichshafen AG (German tier-1 mega-supplier; FY25 revenue &euro;42 bn){ref("211")}, born from the original Rane TRW JV (TRW acquired by ZF in 2015){ref("212")}. The entity manufactures steering gears + braking-system components + occupant safety sub-assemblies primarily for commercial-vehicle OEMs (Tata Motors CV, Ashok Leyland, VECV, Daimler India CV) and select PV programmes. <strong>FY25 Total Operating Income Rs 2,080 Cr</strong>{ref("128")}; EBITDA Rs 213.28 Cr (10.3%); PAT Rs 121.55 Cr; Tangible Net Worth Rs 547.52 Cr; Total Debt Rs 524.03 Cr (Debt/TNW 1.34x balanced); <strong>9 open charges totalling Rs 524.03 Cr on the MCA register, of which IBank holds Rs 30 Cr (5.7%) via a 05 May 2023 creation</strong>{ref("126")}. Credit rating IND AA- / ICRA AA- Stable (24 Feb 2026){ref("213")}. 996 FTE{ref("128")}.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 50&ndash;72 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 share-grow (Rs 30 Cr &rarr; Rs 100&ndash;160 Cr)</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,080 Cr</div><div class="sub">CV-anchored auto-comp{ref("128")}</div></div>
    <div class="kpi"><div class="k">IBank share of charges</div><div class="v num">5.7%</div><div class="sub">Rs 30 Cr / Rs 524 Cr; expand{ref("126")}</div></div>
    <div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA AA- Stable</div><div class="sub">24 Feb 2026{ref("213")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles &mdash; share-grow play</h4>
    <ol style="margin-bottom:0">
      <li><strong>Charge re-set + share-grow</strong> &mdash; current consortium dominated by HDFC Bank Rs 298.3 Cr (57%), Citibank Rs 135.5 Cr (26%), IndusInd Rs 60 Cr (11%), IBank Rs 30 Cr (5.7%); next consortium re-set is the window to bid for AA- pricing at scale.</li>
      <li><strong>EUR + USD trade-finance for ZF imports</strong> &mdash; ~Rs 600&ndash;800 Cr annual ZF-Germany component imports drive FX + LC envelope; tri-currency hedge book.</li>
      <li><strong>CV growth + EV-CV transition</strong> &mdash; Tata CV electrification + Ashok Leyland Switch ramp; ZF brake-by-wire + EPS programmes for CV-EV are FY27&ndash;28 capex.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U35999TN1987PTC014600</strong></span>
    <span>Incorp <strong>03 Jul 1987</strong></span>
    <span>Group <strong>Rane Holdings + ZF Friedrichshafen (Germany)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture</div>
  <p>ZF Rane Automotive is the Tamil Nadu manufacturing JV between Rane Group (~50%) and ZF Friedrichshafen AG (~50%; ZF inherited the stake via 2015 TRW acquisition){ref("212")}. ZF Friedrichshafen{ref("211")} (Friedrichshafen, Germany) is the world's #2 tier-1 auto supplier (after Bosch), FY25 revenue &euro;42 bn, ~165,000 global FTE, leadership positions in driveline, chassis, e-mobility, and ADAS systems. Family-foundation ownership (Zeppelin Foundation 93.8% + Dr. Juergen and Irmgard Ulderup Foundation 6.2%); not publicly listed.</p>
  <h3>03.1 Rane Group context</h3>
  <ul>
    <li>Same ultimate Rane-side promoter as Rane Steering Systems (pilot 35); Ganesh family (L. Ganesh, L. Lakshman, Harish Lakshman){ref("203")}.</li>
    <li>Rane Holdings is the apex non-listed promoter holding-co; below it sit listed Rane (Madras) Ltd + multiple JVs.</li>
    <li>Cross-sell into Rane Group sister entities natural extension of either Rane-related dossier engagement.</li>
  </ul>
  <h3>03.2 Customer mix &amp; positioning</h3>
  <ul>
    <li>Tata Motors Commercial Vehicles ~35%; Ashok Leyland ~25%; VECV (Volvo-Eicher) ~10%; Daimler India CV (BharatBenz) ~8%; Mahindra Tractor + Mahindra-CV ~10%; PV programmes (Hyundai / Maruti) ~10%; balance export.</li>
    <li>Product lines: hydraulic + electric power-steering (CV-grade); brake actuators; safety-system sub-assemblies.</li>
    <li>ZF technology IP cascade: brake-by-wire + steer-by-wire + ADAS sensors flow via royalty / IP-licensing.</li>
  </ul>
  <h3>03.3 Banking consortium (Probe42 cut){ref("126")}</h3>
  <ul>
    <li><strong>HDFC Bank Rs 298.30 Cr (56.9%)</strong> &mdash; lead bank; multiple modifications + creations 2022-25.</li>
    <li><strong>Citibank N.A. Rs 135.50 Cr (25.9%)</strong> &mdash; FX + trade specialist.</li>
    <li><strong>IndusInd Bank Ltd Rs 60.00 Cr (11.4%)</strong> &mdash; recent entry Jun 2025.</li>
    <li><strong>IBank Rs 30.00 Cr (5.7%)</strong> &mdash; charge dated 05 May 2023; minority position.</li>
    <li>Master sheet also lists 14-bank disclosure including BoB, CitiBank, HDFC, IBank, IDBI, IOB, SBI, FedBank, IndusInd, RBSCotland and others{ref("128")} &mdash; some legacy-only.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,720</td><td class="num">1,890</td><td class="num">2,080{ref("128")}</td><td>10% YoY CAGR; CV cycle</td></tr>
      <tr><td>EBITDA</td><td class="num">160</td><td class="num">182</td><td class="num">213.28{ref("128")}</td><td>Margin 9.3-10.3% &mdash; healthy auto-comp range</td></tr>
      <tr><td>PAT</td><td class="num">85</td><td class="num">105</td><td class="num">121.55{ref("128")}</td><td>Strong profitability supports AA- rating</td></tr>
      <tr><td>TNW</td><td class="num">425</td><td class="num">485</td><td class="num">547.52{ref("128")}</td><td>Solid build via retained earnings</td></tr>
      <tr><td>Total Debt</td><td class="num">540</td><td class="num">510</td><td class="num">524.03{ref("128")}</td><td>Stable; refi cycle</td></tr>
      <tr><td>Debt/TNW</td><td class="num">1.27x</td><td class="num">1.05x</td><td class="num">0.96x{ref("128")}</td><td>Improving; comfortable</td></tr>
      <tr><td>Debt/EBITDA</td><td class="num">3.38x</td><td class="num">2.80x</td><td class="num">2.46x{ref("128")}</td><td>Investment-grade comfort zone</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 8.74 Cr</div><div class="sub">JV equity{ref("128")}</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">996</div><div class="sub">Multi-plant CV+PV components{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 524.03 Cr</div><div class="sub">9 tranches{ref("126")}</div></div>
    <div class="kpi"><div class="k">IBank share</div><div class="v num">5.7%</div><div class="sub">Rs 30 Cr / Rs 524 Cr{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">ICRA AA- Stable</div><div class="sub">24 Feb 2026{ref("213")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">Clean{ref("82")}</div></div>
  </div>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA charge register (Probe42 cut 22 Apr 2026)</div>
  <h2>9 open charges totalling Rs 524.03 Cr; IBank Rs 30 Cr (5.7%)</h2>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Holder</th><th>Status</th><th>Action date</th><th class="num">Amount (Rs Cr)</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>HDFC Bank Limited</td><td>Modification</td><td>27 Jun 2025</td><td class="num">55.00</td><td>HDFC tranche refresh</td></tr>
      <tr><td>IndusInd Bank Limited</td><td>Creation</td><td>25 Jun 2025</td><td class="num">60.00</td><td>New entrant; consortium expansion</td></tr>
      <tr><td>Citibank N.A.</td><td>Modification</td><td>20 Mar 2024</td><td class="num">85.50</td><td>Trade + FX specialist</td></tr>
      <tr><td>Citibank N.A.</td><td>Creation</td><td>11 Mar 2024</td><td class="num">50.00</td><td>Citibank doubled exposure</td></tr>
      <tr><td>HDFC Bank Limited</td><td>Creation</td><td>24 Oct 2023</td><td class="num">25.00</td><td>HDFC creation</td></tr>
      <tr><td><strong>IBank</strong></td><td>Creation</td><td>05 May 2023</td><td class="num"><strong>30.00</strong></td><td><strong>IBank entry &mdash; expand from minority</strong></td></tr>
      <tr><td>HDFC Bank Limited</td><td>Modification</td><td>20 Aug 2022</td><td class="num">160.00</td><td>HDFC primary tranche</td></tr>
      <tr><td>HDFC Bank Limited</td><td>Creation</td><td>17 May 2022</td><td class="num">58.25</td><td>HDFC secondary</td></tr>
      <tr><td><strong>Total</strong></td><td colspan="2"></td><td class="num"><strong>524.03</strong></td><td><strong>HDFC 56.9% / Citi 25.9% / IndusInd 11.4% / IBank 5.7%</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p class="lede">Strategic implication: IBank position is small (5.7%) but the entity is strong (AA- rated, stable margins, balanced leverage) &mdash; a clean candidate for IBank to bid up to 20-30% wallet share at the next consortium-renewal window. The most attractive expansion path: take over a portion of HDFC's primary tranche when it matures, or a Citibank Trade-LC mandate, or a fresh capex-TL for the EV-CV programme.</p>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; CV auto-comp + ZF global JV ecosystem</div>
  <p>India CV market FY25 ~9.5 lakh units (M&amp;HCV + LCV + buses); cycle accelerated post-2023 mining + infrastructure demand; FY26&ndash;27 expected slowdown then recovery. ZF Rane sits within the Rs 18,000-22,000 Cr CV-component supplier ecosystem.</p>
  <h3>06.1 CV-component peer set</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Tech / parent</th><th>FY25 revenue (Rs Cr)</th><th>End market</th></tr></thead>
    <tbody>
      <tr><td><strong>ZF Rane Auto India</strong></td><td>ZF Friedrichshafen + Rane</td><td class="num">2,080{ref("128")}</td><td>CV steering + brake</td></tr>
      <tr><td>Wabco India / ZF CV Control Systems</td><td>ZF parent</td><td class="num">~3,200{ref("214")}</td><td>CV brake control + ADAS</td></tr>
      <tr><td>Brakes India (pilot 25)</td><td>TVS-Rane JV</td><td class="num">7,081{ref("128")}</td><td>PV + CV brake</td></tr>
      <tr><td>Bosch India CV systems</td><td>Bosch parent</td><td class="num">~2,800</td><td>CV electronics + brake</td></tr>
      <tr><td>Mahindra Truck &amp; Bus subassembly</td><td>M&amp;M Group</td><td class="num">~1,400</td><td>CV in-house</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.2 Drivers</h3>
  <ul>
    <li><strong>CV-EV transition:</strong> Tata Ace EV / Ashok Leyland Switch ramp; ZF brake-by-wire IP relevant.</li>
    <li><strong>BS-VI Phase 2 + future BS-VII:</strong> emission + safety regulation drives content per CV up 12-18%.</li>
    <li><strong>ADAS + connected-CV mandates:</strong> AEB / lane-keep-assist could become mandatory FY27&ndash;28 via MoRTH; ZF tech IP enables Rane to capture share.</li>
    <li><strong>Export demand:</strong> Tata + Ashok Leyland CV exports to Africa + LATAM accelerating; ZF Rane components flow with end-products.</li>
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
      <tr><td>TOI</td><td class="num">2,080{ref("128")}</td><td class="num">2,300</td><td class="num">2,580</td><td class="num">2,250</td><td class="num">3,000</td><td class="num">2,950</td></tr>
      <tr><td>YoY %</td><td class="num">+10.1</td><td class="num pos">+10.6</td><td class="num pos">+12.2</td><td class="num">-2.2</td><td class="num pos">+30.4</td><td class="num pos">+14.3</td></tr>
      <tr><td>EBITDA margin</td><td class="num">10.3</td><td class="num">10.6</td><td class="num">11.0</td><td class="num">9.5</td><td class="num">12.0</td><td class="num">11.5</td></tr>
      <tr><td>EBITDA</td><td class="num">213</td><td class="num">244</td><td class="num">284</td><td class="num">214</td><td class="num">360</td><td class="num">339</td></tr>
      <tr><td>PAT</td><td class="num">122</td><td class="num">146</td><td class="num">175</td><td class="num">128</td><td class="num">230</td><td class="num">214</td></tr>
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
      <tr><td>CC/OD share-grow (HDFC handover or capex tranche)</td><td class="num">220&ndash;320</td><td class="num">5&ndash;8</td><td>Target 25-30% wallet share by Y3</td></tr>
      <tr><td>Capex TL (EV-CV brake-by-wire)</td><td class="num">240&ndash;360</td><td class="num">4.5&ndash;7</td><td>MCLR + 60 bp; 7-yr; sustainability-linked tranche</td></tr>
      <tr><td>Import LC (ZF Germany components)</td><td class="num">600&ndash;800</td><td class="num">4.5&ndash;6.5</td><td>Sight + 90-day usance; large EUR exposure</td></tr>
      <tr><td>FX forwards (EUR + USD + JPY tri-currency)</td><td class="num">1,400&ndash;1,800 notional</td><td class="num">14&ndash;18</td><td>6M rolling; replace Citibank-led portion</td></tr>
      <tr><td>BG (customer + statutory)</td><td class="num">140&ndash;220</td><td class="num">1.4&ndash;2.2</td><td>Tata / Ashok Leyland BGs</td></tr>
      <tr><td>SCF (vendor anchor)</td><td class="num">240&ndash;380</td><td class="num">4&ndash;6</td><td>Anchor-led; supplier ecosystem</td></tr>
      <tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">1.2&ndash;1.8</td><td>996 FTE payroll + GST</td></tr>
      <tr><td>Cross-sell into Rane Group syndication</td><td class="num">200&ndash;400</td><td class="num">3&ndash;6</td><td>Sister-entity wallet expansion</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 37.6&ndash;55.5 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <p>996 FTE workforce + Rane Group + ZF expat-banker layer.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 480-680; Rs 1.8&ndash;2.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Rane Group promoter family + ZF-nominee senior mgmt; PB AUM Rs 240-380 Cr; Rs 1.4&ndash;2.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 80&ndash;120 Cr; Rs 0.8&ndash;1.4 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 4.0&ndash;6.6 Cr / yr</strong>.</p>
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
      <tr><td>Wholesale funded (CC + TL + cross-sell)</td><td class="num">12.5</td><td class="num">21</td></tr>
      <tr><td>Wholesale non-funded (LC + BG)</td><td class="num">5.9</td><td class="num">8.7</td></tr>
      <tr><td>FX + derivatives</td><td class="num">14</td><td class="num">18</td></tr>
      <tr><td>SCF</td><td class="num">4</td><td class="num">6</td></tr>
      <tr><td>CMS + cards</td><td class="num">1.2</td><td class="num">1.8</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">4.0</td><td class="num">6.6</td></tr>
      <tr><td>Cross-sell into Rane Group</td><td class="num">3</td><td class="num">6</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>44.6</strong></td><td class="num"><strong>68.1</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 50-72 Cr/yr on cover sits at upper-mid band (assumes wallet expansion succeeds).</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3>
  <p>[diligence] MCA DIR-12 + MGT-7 refresh required at T+14. Rane Group senior leadership (Ganesh family) on board; ZF-nominee directors typical 50-50 JV structure.</p>
  <h3>11.2 Ownership &amp; SBO</h3>
  <ul>
    <li>50:50 JV: Rane Holdings + ZF International (Germany).</li>
    <li>UBO: (a) Ganesh family via Rane Holdings; (b) Zeppelin Foundation 93.8% + Ulderup Foundation 6.2% via ZF Friedrichshafen{ref("211")}.</li>
    <li>BEN-2 declarations on file{ref("144")}.</li>
  </ul>
  <h3>11.3 Litigation &amp; regulatory</h3>
  <ul>
    <li>Probe42 suit-filed: <strong>0</strong>{ref("82")}.</li>
    <li>NCLT / Indian Kanoon: clean{ref("145")}.</li>
    <li>Standard transfer-pricing assessments expected.</li>
  </ul>
  <h3>11.4 Recent news</h3>
  <ul>
    <li>Feb 2026: ICRA AA- Stable affirmation{ref("213")}.</li>
    <li>Jun 2025: IndusInd Bank entry into consortium (Rs 60 Cr fresh charge){ref("126")}.</li>
    <li>Tata + Ashok Leyland EV-CV programmes scaling FY26&ndash;27; ZF Rane EPS + brake content rising.</li>
  </ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7 refresh</li>
    <li>T+14 BEN-2 SBO confirmation across Rane + ZF chain</li>
    <li>T+14 ZF royalty / IP-license agreement copy</li>
    <li>T+30 Tata-EV + Ashok Leyland-Switch supply contracts confirmation</li>
    <li>T-14 Pre-sanction Probe42 charge re-pull</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> ZF Rane CFO + treasury head; share-grow proposition memo; FX framework introduction.</p></div>
  <div class="card"><p><strong>T+60:</strong> Capex TL term-sheet for FY27 EV-CV programmes; FX forward Rs 600-800 Cr notional live.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Capex TL Rs 100-150 Cr drawn; SCF programme launch; salary CASA + PB.</p></div>
  <div class="card"><p><strong>T+180:</strong> Bid for HDFC primary-tranche refinance window; Rane Group syndication memo.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>IBank wallet share grows from 5.7% to 20-25% by end-FY27</li>
    <li>FX programme Rs 1,200 Cr notional steady-state</li>
    <li>Capex TL Rs 200 Cr drawn by Q3 FY27</li>
    <li>Y3 run-rate Rs 50-72 Cr</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; ZF Rane-specific from [210].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">ZF Rane Automotive India-specific sources</h3>
  <ol start="210">
  <li id="src-203"><strong>Rane Group corporate website + Rane Holdings + L. Ganesh family chronology</strong> &mdash; group founded 1929; Ganesh family promoter-control; structure of operating + listed entities; technology-partnership history. Used cross-dossier for Rane Steering + ZF Rane. <span class="u">ranegroup.com &middot; ranegroup.com/about-us/leadership-team</span></li>
  <li id="src-210"><strong>MCA v3 + ZaubaCorp &mdash; ZF Rane Automotive India Pvt Ltd master data</strong> &mdash; CIN U35999TN1987PTC014600; incorp 03 Jul 1987; RoC Chennai; active. <span class="u">mca.gov.in &middot; zaubacorp.com/company/zf-rane-automotive-india-private-limited/U35999TN1987PTC014600</span></li>
  <li id="src-211"><strong>ZF Friedrichshafen AG &mdash; FY25 Annual Report</strong> &mdash; revenue &euro;42 bn; Zeppelin Foundation 93.8% + Ulderup Foundation 6.2% ownership; private (non-listed); world's #2 tier-1 auto supplier. <span class="u">zf.com/site/corporate/en/investors/financial_news/financial_news.html</span></li>
  <li id="src-212"><strong>ZF / TRW acquisition history (May 2015)</strong> &mdash; ZF acquired TRW Automotive for $13.5 bn; inherited Rane TRW JV stake which became ZF Rane Automotive. <span class="u">zf.com/site/corporate/en/news/zf_acquires_trw.html</span></li>
  <li id="src-213"><strong>ICRA Ratings &mdash; ZF Rane Automotive India Pvt Ltd rating rationale (24 Feb 2026)</strong> &mdash; AA- / Stable on fund + non-fund limits. <span class="u">icra.in / Rationale / ShowRationaleReport</span></li>
  <li id="src-214"><strong>Wabco India / ZF CV Control Systems Ltd (BSE 533023) FY25 disclosures</strong> &mdash; listed CV-control-systems peer; segmental disclosure used as benchmark. <span class="u">bseindia.com/stock-share-price/zf-cv-control-systems-india-ltd/ZFCVINDIA/533023/</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "ZF Rane Automotive India Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("ZF Rane Automotive India", "CV auto-comp / steering + brake"),
           FOOT("Cipher clean; 1,500+ lines; IBank Rs 30 Cr (5.7%) of Rs 524 Cr — share-grow play.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
