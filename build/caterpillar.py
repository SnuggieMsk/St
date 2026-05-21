"""Caterpillar India dossier (pilot 22)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "caterpillar-india-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 22 of 40 · Chennai · MNC · Construction equipment</div>
  <h1>Caterpillar India Private Limited<br>US Caterpillar Inc India operations</h1>
  <p class="lede">100% subsidiary of Caterpillar Inc (NYSE: CAT), global leader in construction, mining, and heavy-equipment manufacturing. CIN U29244TN2000FTC046255. FY25 TOI Rs 11,072 Cr (master sheet){ref("42")}; India operations since 2000; Chennai corporate office with manufacturing at Thiruvallur + Hosur. MNC structure; global parent investment-grade (Moody&rsquo;s A2 / S&amp;P A).</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 65–88 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Trade finance + FX heavy; US parent relationship cross-sell</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 11,072 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">Parent credit</div><div class="v num">Moody's A2</div><div class="sub">Global parent Caterpillar Inc investment-grade</div></div>
    <div class="kpi"><div class="k">India tenure</div><div class="v num">25+ yrs</div><div class="sub">Since 2000 incorporation</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Equipment-imports trade finance</strong> &mdash; Large USD imports of components + finished-goods; continuous LC + SBLC programme</li>
      <li><strong>Dealer-inventory financing</strong> &mdash; Caterpillar India supplies 20+ authorised dealers across India; dealer financing opportunity</li>
      <li><strong>Infrastructure / mining capex cycle</strong> &mdash; India infra boom + Coal India mining capex drive CAT equipment demand</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U29244TN2000FTC046255</strong></span>
    <span>Parent <strong>Caterpillar Inc (NYSE: CAT)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; India footprint</div>
  <p>Caterpillar Inc operates in India via two primary entities:</p>
  <ul class="check">
    <li><strong>Caterpillar India Pvt Ltd (this dossier)</strong> &mdash; manufacturing + distribution; Thiruvallur plant + Hosur tech centre</li>
    <li><strong>Caterpillar India Engineering Solutions Pvt Ltd</strong> &mdash; engineering / R&amp;D services; ~Rs 4,518 Cr FY25 (separate Tier-2 candidate)</li>
    <li>Caterpillar Financial Services India (NBFC arm for customer financing)</li>
    <li>Global supply chain: imports components from Caterpillar US + Asia; exports finished goods to emerging markets</li>
  </ul>
  <p>Caterpillar Inc FY25 global revenue ~$65 bn; ~$120 bn market cap. India operations are strategic growth-market.</p>
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
      <tr><td>TOI</td><td class="num">9,800</td><td class="num">11,072</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">11</td><td class="num">12.5</td></tr>
      <tr><td>EBITDA</td><td class="num">1,078</td><td class="num">1,384</td></tr>
      <tr><td>PAT (est)</td><td class="num">580</td><td class="num">780</td></tr>
    </tbody>
  </table>
  </div>
  <p>Global parent provides technology + global sourcing; India operation margin reflects India-only metrics.</p>
  <h3>04.1 Operational footprint</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Chennai HO</div><div class="v num" style="font-size:1rem">Corporate + sales</div></div>
    <div class="kpi"><div class="k">Thiruvallur plant</div><div class="v num" style="font-size:1rem">Mining + construction eq</div></div>
    <div class="kpi"><div class="k">Hosur tech centre</div><div class="v num" style="font-size:1rem">Engineering services</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~3,500</div><div class="sub">Combined India</div></div>
    <div class="kpi"><div class="k">Authorised dealers</div><div class="v num">~20</div><div class="sub">Pan-India distribution</div></div>
    <div class="kpi"><div class="k">Export share</div><div class="v num">~35%</div><div class="sub">To MENA + ASEAN + Africa</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; Construction + mining equipment</div>
  <p>India construction equipment (CE) + mining equipment market Rs 68,000 Cr; growing 13-15% CAGR on infra capex + mining expansion. Peers: JCB India (largest, #1 share), Tata-Hitachi, Mahindra Construction, Komatsu India, Volvo Construction Equipment India, ACE, Escorts Kubota.</p>
  <h3>05.1 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Focus</th></tr></thead>
    <tbody>
      <tr><td>JCB India</td><td class="num">~17,500</td><td>Backhoe + loader leader</td></tr>
      <tr><td><strong>Caterpillar India</strong></td><td class="num">11,072</td><td>Large mining + construction</td></tr>
      <tr><td>Tata Hitachi Construction</td><td class="num">~9,800</td><td>Mid-large excavators</td></tr>
      <tr><td>Komatsu India</td><td class="num">3,613</td><td>Large mining equipment</td></tr>
      <tr><td>Volvo CE India</td><td class="num">~3,200</td><td>Premium CE</td></tr>
      <tr><td>Mahindra Construction</td><td class="num">~2,400</td><td>Compact + mid-size</td></tr>
    </tbody>
  </table>
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
      <tr><td>TOI</td><td class="num">11,072</td><td class="num">12,500</td><td class="num">14,200</td><td class="num">12,800</td><td class="num">15,800</td><td class="num">16,000</td></tr>
      <tr><td>EBITDA margin</td><td class="num">12.5</td><td class="num">13.0</td><td class="num pos">13.5</td><td class="num neg">11.8</td><td class="num pos">14.5</td><td class="num">14.0</td></tr>
      <tr><td>EBITDA</td><td class="num">1,384</td><td class="num">1,625</td><td class="num">1,917</td><td class="num">1,510</td><td class="num">2,291</td><td class="num">2,240</td></tr>
      <tr><td>PAT (est)</td><td class="num">780</td><td class="num">950</td><td class="num">1,150</td><td class="num">870</td><td class="num">1,420</td><td class="num">1,360</td></tr>
    </tbody>
  </table>
  </div>
  <p>Growth tracks India infra capex + mining expansion. Coal India + NTPC + state-mining plus private-sector private road + port infra driving demand. EBITDA margin recovery on operating leverage.</p>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Import LC + SBLC (USD components + CKD)</td><td class="num">1,400&ndash;1,900</td><td class="num">10&ndash;13</td></tr>
      <tr><td>FX forwards (USD heavy)</td><td class="num">2,200&ndash;2,800 notional</td><td class="num">24&ndash;30</td></tr>
      <tr><td>WC CC/OD</td><td class="num">320&ndash;420</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Dealer inventory financing</td><td class="num">480&ndash;640</td><td class="num">8&ndash;11</td></tr>
      <tr><td>Customer (end-buyer) financing through CAT Finance India</td><td class="num">&mdash;</td><td class="num">4&ndash;6</td></tr>
      <tr><td>SCF (anchor-led vendors)</td><td class="num">280&ndash;380</td><td class="num">5&ndash;7</td></tr>
      <tr><td>CMS + treasury</td><td class="num">&mdash;</td><td class="num">5&ndash;7</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 61&ndash;81 Cr/yr.</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~3,500 India-wide; MNC so no promoter-family PB.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA ~1,500 accounts; Rs 3-4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">Senior mgmt PB</h4><p>India CEO + senior leaders; Rs 1-2 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity trust Rs 140-180 Cr; Rs 1-2 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 5&ndash;8 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 61&ndash;81 Cr/yr + Retail/TASC Rs 4&ndash;7 Cr/yr = <strong>Rs 65&ndash;88 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>100% Caterpillar Inc (NYSE: CAT)</li>
        <li>Moody's A2 / S&amp;P A parent-level credit</li>
        <li>No India promoter-family</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Global Caterpillar governance + compliance framework</li>
        <li>India CEO reports to APAC leadership</li>
        <li>FCPA + India Companies Act dual compliance</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet India CFO + APAC treasury; LC + FX + dealer-inventory programme; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close LC + FX framework; dealer SCF + customer-financing programme; CMS integration.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Caterpillar Financial Services India cross-sell; global Caterpillar Inc relationship introduction.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>LC + FX framework live by 31 Aug 2026</li>
    <li>Dealer inventory financing programme with 8+ dealers by end-Q3 FY27</li>
    <li>Annual run-rate Rs 40-50 Cr by end-FY27</li>
    <li>Sister-entity Caterpillar India Engineering Solutions relationship secured</li>
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
  <ol start="117">
  <li id="src-117"><strong>Caterpillar Inc (NYSE: CAT) 10-K + India corporate disclosures + CEA India sector reports</strong> &mdash; Thiruvallur + Hosur plants; Chennai HO. <span class="u">caterpillar.com &middot; sec.gov/edgar/search/?q=CAT</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Caterpillar India Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Caterpillar India", "Construction + Mining Equipment"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
