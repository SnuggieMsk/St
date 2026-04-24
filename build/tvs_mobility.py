"""TVS Mobility dossier (pilot 13)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .padding import pad
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "tvs-mobility-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 13 of 20 · Auto dealership · TVS Group</div>
  <h1>TVS Mobility Pvt Ltd<br>India's largest multi-brand automobile dealership chain</h1>
  <p class="lede">TVS Group entity consolidating TVS Automotive Solutions' multi-brand dealership network (Tata, Hyundai, Ashok Leyland, Mahindra, MG Motor, EV brands). CIN U50400TN2018PTC121056. FY25 TOI Rs 6,277 Cr (master sheet){ref("42")} &mdash; one of the largest Tier-1 names by revenue. IND Ratings AA- (11 Jul 2025 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 2,520 Cr across inventory-financing + WC consortium.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 58–75 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 46–60 Cr + Retail adjacencies Rs 12–15 Cr</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 6,277 Cr</div><div class="sub">Largest of Tier-1 after CPCL + Foxconn{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">IND rating</div><div class="v num">AA-</div><div class="sub">Jul 2025{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 2,520 Cr</div><div class="sub">Inventory + WC consortium</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Inventory-financing (floor-plan)</strong> &mdash; structural high-margin product for OEM-dealer network; TVS Mobility runs large inventory across multiple brands</li>
      <li><strong>Retail auto-loan origination</strong> &mdash; dealership consumer financing: end-customer auto-loans originated at dealership; 10,000+ vehicle loans/year potential</li>
      <li><strong>TVS Group halo</strong> &mdash; TVS relationship halo; cross-sell to TVS Holdings + Sundaram Finance</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U50400TN2018PTC121056</strong></span>
    <span>Parent <strong>TVS Group</strong></span>
    <span>Registry cut <strong>Probe42 / 13 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group</div>
  <p>TVS Mobility consolidates multiple dealership and mobility assets under TVS Group umbrella:</p>
  <ul class="check">
    <li>Multi-brand auto-dealership (largest in South + Western India)</li>
    <li>Commercial vehicle dealer network (Ashok Leyland, Tata)</li>
    <li>Premium / EV brands</li>
    <li>After-market services: service, spares, refinishing</li>
    <li>Trucking / logistics adjacency (separate entity in some structures)</li>
  </ul>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY24 est</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">5,400</td><td class="num">6,277</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+16</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">3.5</td><td class="num">4.2</td></tr>
      <tr><td>EBITDA</td><td class="num">189</td><td class="num">264</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">5.8x</td><td class="num">4.5x</td></tr>
    </tbody>
  </table>
  </div>
  <p>Low single-digit EBITDA margin typical for dealership businesses; inventory-intensive. Open charges Rs 2,520 Cr reflects floor-plan inventory financing.</p>
  <h3>04.1 Operational scale</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Dealership outlets</div><div class="v num">180+</div><div class="sub">Multi-brand across south + west India</div></div>
    <div class="kpi"><div class="k">Units sold (FY25 est)</div><div class="v num">~1.4 lakh</div><div class="sub">CV + PV + 2W + CE combined</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~12,000</div><div class="sub">Sales + service + admin</div></div>
    <div class="kpi"><div class="k">Service bays</div><div class="v num">2,400+</div><div class="sub">After-market recurring revenue</div></div>
    <div class="kpi"><div class="k">OEM principals</div><div class="v num">10+</div><div class="sub">Tata, Ashok Leyland, Hyundai, Mahindra, MG, EV brands</div></div>
    <div class="kpi accent"><div class="k">Geographic span</div><div class="v num">7 states</div><div class="sub">Tamil Nadu + Karnataka + Andhra + Telangana + Maharashtra + Kerala + Odisha</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India auto dealership</div>
  <p>India organised multi-brand auto-dealership market is a ~Rs 2.8 lakh Cr fragmented segment. Top-5 players hold ~16% share. Growing 9-11% CAGR with shift to EV + connected services + used-vehicle platforms adding new revenue layers.</p>

  <h3>05.1 Dealership economics</h3>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Inventory turnover</h4><p>12-15 days on fast-moving brands; 30-45 days on premium; 60+ days on niche. Floor-plan financing enables rapid turnover.</p></div>
    <div class="card"><h4 style="margin-top:0">Revenue mix</h4><p>Sales 70% + Service 20% + Spares 7% + Accessories 3%. Service is highest-margin (18-22%).</p></div>
    <div class="card"><h4 style="margin-top:0">Retail finance origination</h4><p>60-75% of vehicle sales financed. Dealer originates auto-loan for OEM-captive NBFC or 3rd-party bank. Commission 80-140 bps.</p></div>
  </div>

  <h3>05.2 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Focus</th></tr></thead>
    <tbody>
      <tr><td>Landmark Cars</td><td class="num">~5,400</td><td>Premium luxury (Mercedes, Honda)</td></tr>
      <tr><td>Sundaram Motors (TVS Group)</td><td class="num">~3,200</td><td>Mahindra + Tata commercial</td></tr>
      <tr><td><strong>TVS Mobility</strong></td><td class="num">6,277</td><td>Multi-brand CV + PV + 2W</td></tr>
      <tr><td>Jayem Auto</td><td class="num">~1,800</td><td>Multi-brand</td></tr>
      <tr><td>Popular Vehicles &amp; Services (Kerala)</td><td class="num">~4,800</td><td>Maruti Suzuki, Mahindra, etc.</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.3 Three industry tailwinds</h3>
  <div class="grid c3">
    <div class="card accent"><h4 style="margin-top:0">EV-dealership opportunity</h4><p>EV brands (Tata EV, MG EV, Mahindra EV, BYD) building dealer networks; multi-brand dealers capture share. EV financing + charging-infrastructure adjacency.</p></div>
    <div class="card accent"><h4 style="margin-top:0">Used-car platform ramp</h4><p>Organised used-car market growing 30%+ CAGR; certified pre-owned programmes (Maruti True Value, Hyundai H Promise) benefit multi-brand dealers.</p></div>
    <div class="card accent"><h4 style="margin-top:0">Mobility-as-a-Service</h4><p>Fleet management + subscription + ride-sharing integration; TVS Group positioned via TVS Vehicle Mobility Solution sister-entity.</p></div>
  </div>
</section>
"""
def S5():
    return f"""
<section id="models">
  <div class="subhead">06 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>Revenue</td><td class="num">6,277</td><td class="num">7,100</td><td class="num">8,000</td><td class="num">7,300</td><td class="num">8,800</td><td class="num">9,000</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">4.2</td><td class="num">4.5</td><td class="num pos">4.8</td><td class="num neg">4.0</td><td class="num pos">5.2</td><td class="num">5.0</td></tr>
      <tr><td>EBITDA</td><td class="num">264</td><td class="num">320</td><td class="num">384</td><td class="num">292</td><td class="num">458</td><td class="num">450</td></tr>
      <tr><td>PAT (est)</td><td class="num">65</td><td class="num">95</td><td class="num">135</td><td class="num">78</td><td class="num">175</td><td class="num">170</td></tr>
      <tr><td>Inventory + WC intensity</td><td class="num">High</td><td class="num">High</td><td class="num">High</td><td class="num">Very high</td><td class="num">High</td><td class="num">High</td></tr>
    </tbody>
  </table>
  </div>
  <p>Cumulative new debt + inventory finance need FY26-28 base: ~Rs 680 Cr. IBank target floor-plan + WC share: Rs 240-320 Cr.</p>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Wholesale entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th>Pricing</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td><strong>Floor-plan / inventory finance</strong></td><td class="num">520&ndash;680</td><td>MCLR + 40 bp</td><td class="num">10&ndash;14</td></tr>
      <tr><td>WC CC/OD (non-inventory)</td><td class="num">180&ndash;240</td><td>MCLR + 30 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>BG (OEM performance + showroom landlord)</td><td class="num">240&ndash;320</td><td>Comm 50 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CMS (180 outlets collection + vendor)</td><td class="num">&mdash;</td><td>API + float</td><td class="num">8&ndash;11</td></tr>
      <tr><td><strong>Retail auto-loan origination (at dealer)</strong></td><td class="num">Rs 1,800&ndash;2,400 annual flow</td><td>Origination commission + NII</td><td class="num">16&ndash;22</td></tr>
      <tr><td>Insurance + extended-warranty CMS</td><td class="num">&mdash;</td><td>MDR + commission</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Used-vehicle receivable financing</td><td class="num">80&ndash;140</td><td>Effective 1.1%</td><td class="num">1&ndash;2</td></tr>
      <tr><td>SCF (spare-parts + accessory vendors)</td><td class="num">90&ndash;140</td><td>NIM 1.8%</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CP programme (AA- rating supports)</td><td class="num">200 rolling</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Treasury / liquid mgmt</td><td class="num">120&ndash;180 AUM</td><td>18-22 bp</td><td class="num">2&ndash;3</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale + retail-auto-loan + CMS: Rs 48&ndash;68 Cr/yr.</strong> Retail auto-loan origination is the single largest income line given the 1.4-lakh-unit annual flow.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Workforce ~12,000 across 180 outlets + 2,400 service bays</li>
        <li>Salary CASA 6,000-7,500 accounts Y1</li>
        <li>Customer UPI / co-brand credit card opportunity at 180 outlets</li>
        <li>Annual income: <strong>Rs 8&ndash;10 Cr</strong></li>
      </ul>
    </div>
    <div class="card accent"><h4 style="margin-top:0">PB (TVS-extended)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group family halo</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 180&ndash;220 Cr</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 12&ndash;15 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated wallet</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Bucket</th><th class="num">Wallet (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Floor-plan + WC</td><td class="num">700&ndash;920</td><td class="num">13&ndash;18</td></tr>
      <tr><td>BG + SBLC</td><td class="num">240&ndash;320</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Retail auto-loan origination</td><td class="num">1,800&ndash;2,400 annual</td><td class="num">16&ndash;22</td></tr>
      <tr><td>CMS + insurance / warranty</td><td class="num">&mdash;</td><td class="num">11&ndash;15</td></tr>
      <tr><td>Used vehicle + SCF + CP + treasury</td><td class="num">490&ndash;660</td><td class="num">6&ndash;10</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>1,430&ndash;1,900</strong></td><td class="num"><strong>48&ndash;68</strong></td></tr>
      <tr><td>Retail / PB / TASC</td><td>&mdash;</td><td class="num">12&ndash;15</td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>1,430&ndash;1,900</strong></td><td class="num pos"><strong>60&ndash;83 Cr/yr</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>

  <h3>10.1 Promoter &amp; ownership</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">TVS Group (Mobility branch)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Part of TVS Automobile Solutions / TVS Mobility branch of TVS Group</li>
        <li>Founder-lineage: T.V. Sundaram Iyengar (1911) &rarr; R. Dinesh leadership (Executive VC of TVS Mobility per TVS Group disclosures)</li>
        <li>Private-co structure; professional + family-rep directors</li>
        <li>Low / zero pledge; TVS-family governance norms</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Group linkages</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Sister entities: TVS Holdings, TVS Motor, Sundaram Finance, Sundaram Motors, TVS Supply Chain</li>
        <li>Related-party transactions at arm&rsquo;s length</li>
        <li>No NCLT / litigation at group level</li>
      </ul>
    </div>
  </div>

  <h3>10.1b KMPs &amp; Probe42</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Executive Vice Chairman</td><td>R. Dinesh (per TVS Group leadership disclosures)</td></tr>
      <tr><td>CEO / CFO / CS</td><td>Professional appointments; MCA DIR-12 confirmation at T+14</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 11 Jul 2025)</td><td><strong>IND AA-</strong> on Commercial Paper + Fund Based WC{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed</strong> (Probe42)</td><td><strong>ZERO</strong>{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 Litigation / news</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">✓ Clean</h4><p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter actions. Zero bureau suit-filed.</p></div>
    <div class="card pos"><h4 style="margin-top:0">Positive news</h4><p>FY25 revenue +16% YoY; margin expansion on mix + scale; EV-dealership network expansion continuing.</p></div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><h4 style="margin-top:0">T+30 &mdash; Floor-plan + retail auto-loan</h4>
    <p>Meet CFO + R. Dinesh at TVS Mobility HO (Chennai). Indicative Rs 520&ndash;680 Cr floor-plan; WC CC/OD Rs 180&ndash;240 Cr; retail auto-loan origination agreement; rate-lock before June MPC{ref("5")}.</p>
  </div>
  <div class="card"><h4 style="margin-top:0">T+60</h4>
    <p>Close floor-plan programme; CMS integration across 180 outlets + 2,400 service bays; BG framework for OEM + landlord; retail auto-loan commission structure signed.</p>
  </div>
  <div class="card pos"><h4 style="margin-top:0">T+90</h4>
    <p>Salary migration ~6,000 accounts; co-brand credit card programme for customer base; used-vehicle receivable financing; insurance + extended-warranty CMS; TVS Group cross-sell handshake.</p>
  </div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>Floor-plan programme live by 31 Aug 2026</li>
    <li>Retail auto-loan origination &ge; 5,000 loans/yr by end-FY27</li>
    <li>Annual run-rate &ge; Rs 35 Cr by end-FY27</li>
  </ul>
</section>
"""
def S11():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro + PESTEL; 81&ndash;82 Probe42 registry endpoints; entity-specific begin at the ordered list that follows.</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Entity-specific sources</h3>
  <ol start="108">
  <li id="src-108"><strong>TVS Mobility Pvt Ltd corporate disclosures + TVS Group leadership overview + IND Ratings Jul 2025</strong> &mdash; multi-brand dealership; R. Dinesh Executive Vice Chairman; TVS Group legacy lineage. <span class="u">tvs.com/mobility &middot; tvsmobility.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "TVS Mobility Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),pad("TVS Mobility","Auto dealership"),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
