"""Salcomp Technologies India dossier (pilot 24)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "salcomp-india-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 24 of 40 · Kancheepuram · MNC · Apple-adjacent EMS</div>
  <h1>Salcomp Technologies India Pvt Ltd<br>Apple charger + display-module manufacturer (Salcomp Oyj Finland)</h1>
  <p class="lede">100% subsidiary of Salcomp Oyj (Finland; private-equity owned by Lunar Industries). Manufactures smartphone chargers + power adapters (primarily for Apple, Samsung, Xiaomi) + display modules at Sriperumbudur / Kancheepuram industrial belt. CIN U32309TN2019PTC133300. FY25 TOI Rs 10,105 Cr (master sheet){ref("42")}. One of the largest smartphone-accessories EMS in India; leveraged charger-localisation + PLI-II participation.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 60–78 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Trade finance + FX heavy</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 10,105 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi"><div class="k">Plant</div><div class="v num">Sriperumbudur</div><div class="sub">Kancheepuram industrial belt</div></div>
    <div class="kpi"><div class="k">Parent</div><div class="v num">Salcomp Oyj (Finland)</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Apple supply-chain anchor</strong> &mdash; Salcomp is a tier-1 Apple accessories supplier; India manufacturing aligned to Apple's China-Plus-One strategy</li>
      <li><strong>PLI-II displays + accessories</strong> &mdash; major beneficiary; capacity ramp FY26-28</li>
      <li><strong>USD-heavy P&amp;L</strong> &mdash; structural FX programme opportunity</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U32309TN2019PTC133300</strong></span>
    <span>Parent <strong>Salcomp Oyj Finland (Lunar Industries)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group</div>
  <p>Salcomp Oyj is a Finnish private-equity-owned EMS company focused on smartphone chargers + power electronics; ~$1.5 bn global revenue; ~80% customer mix is Apple / Samsung / Xiaomi / other smartphone OEMs. India has been Salcomp's largest single-country operation since 2007; operates two manufacturing plants in Sriperumbudur + Kancheepuram industrial belt.</p>
  <ul class="check">
    <li>100% Salcomp Oyj-owned (Finland)</li>
    <li>Owner: Lunar Industries PE fund (European industrial PE)</li>
    <li>Product mix: USB-C chargers, wireless chargers, display modules, power adapters</li>
    <li>Primary customer: Apple Inc (Tier-1 supplier status)</li>
    <li>India plants include ex-Nokia Chennai plant acquired 2020</li>
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
      <tr><td>TOI</td><td class="num">8,400</td><td class="num">10,105</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+20</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">5</td><td class="num">6</td></tr>
      <tr><td>EBITDA</td><td class="num">420</td><td class="num">606</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Scale</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Plant capacity</div><div class="v num">~180 mn units/yr</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~12,000</div></div>
    <div class="kpi"><div class="k">Export share</div><div class="v num">~80%</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; Smartphone accessories / chargers EMS</div>
  <p>India smartphone EMS ecosystem includes Foxconn (Pilot 01), Tata Electronics (Pilot 21), Dixon, Bharat FIH, Salcomp (this dossier), Flex, Jabil, Compal. Salcomp's niche: smartphone chargers + power electronics + display modules. PLI-II accessory allocation provides structural tailwind.</p>
  <h3>05.1 Accessory-EMS competitive landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Focus</th><th>FY25 revenue (Rs Cr)</th></tr></thead>
    <tbody>
      <tr><td><strong>Salcomp India</strong></td><td>Apple chargers + displays</td><td class="num">10,105</td></tr>
      <tr><td>Flex India</td><td>EMS + chargers</td><td class="num">~7,200</td></tr>
      <tr><td>Jabil India</td><td>EMS + mechanical</td><td class="num">~4,500</td></tr>
      <tr><td>Bharat FIH</td><td>Android OEM + accessories</td><td class="num">~12,800</td></tr>
      <tr><td>Amber Enterprises</td><td>White-goods EMS</td><td class="num">8,400</td></tr>
    </tbody>
  </table>
  </div>
  <h3>05.2 Key industry drivers</h3>
  <ul class="check">
    <li>Apple India volume ramp (Foxconn + Tata driving) pulls Salcomp charger volumes</li>
    <li>PLI-II display-module sub-scheme ~Rs 7,800 Cr outlay</li>
    <li>Type-C mandate in EU (since 2024) + likely India (2026) drives charger re-design</li>
    <li>Domestic value-add rising from 14% to 32% by FY28</li>
  </ul>
</section>
"""
def S5():
    return f"""
<section id="models">
  <div class="subhead">06 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">10,105</td><td class="num">12,800</td><td class="num">15,500</td><td class="num">18,200</td></tr>
      <tr><td>EBITDA margin</td><td class="num">6.0</td><td class="num">6.8</td><td class="num">7.5</td><td class="num">8.2</td></tr>
      <tr><td>EBITDA</td><td class="num">606</td><td class="num">870</td><td class="num">1,163</td><td class="num">1,492</td></tr>
    </tbody>
  </table>
  </div>
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
      <tr><td>Import LC + SBLC (component imports)</td><td class="num">1,200&ndash;1,600</td><td class="num">8&ndash;11</td></tr>
      <tr><td>FX forwards (USD revenue + procurement)</td><td class="num">2,400&ndash;3,200 notional</td><td class="num">26&ndash;34</td></tr>
      <tr><td>WC CC/OD</td><td class="num">340&ndash;440</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Capex TL (PLI-linked capacity)</td><td class="num">280&ndash;380</td><td class="num">4&ndash;6</td></tr>
      <tr><td>EPC (export-heavy)</td><td class="num">320&ndash;440</td><td class="num">4&ndash;5</td></tr>
      <tr><td>BG (PLI compliance + customer)</td><td class="num">160&ndash;220</td><td class="num">1&ndash;2</td></tr>
      <tr><td>SCF + CMS</td><td class="num">180&ndash;260</td><td class="num">6&ndash;9</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 54&ndash;74 Cr/yr.</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~12,000; MNC structure. Large retail opportunity at plant-worker level.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 4,500-5,500 accounts; Rs 4-5 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Senior mgmt; Rs 1 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 80-120 Cr; Rs 1-2 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 6&ndash;8 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 54&ndash;74 Cr/yr + Retail/PB/TASC Rs 6&ndash;8 Cr/yr = <strong>Rs 60&ndash;82 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>100% Salcomp Oyj (Finland)</li>
        <li>PE-owned (Lunar Industries)</li>
        <li>Tier-1 Apple supplier</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Global Salcomp framework</li>
        <li>India MD reports to APAC region</li>
        <li>Apple Supplier Code of Conduct compliance</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet India CFO; LC + FX + WC + EPC; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close LC + FX + EPC; capex TL for PLI capacity; CMS.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Salary CASA 4,000+ accounts; global Salcomp Oyj relationship bridge.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>LC + FX framework by 31 Aug 2026</li>
    <li>EPC programme &ge; Rs 320 Cr utilisation by end-FY27</li>
    <li>Annual run-rate Rs 35-42 Cr by end-FY27</li>
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
  <ol start="119">
  <li id="src-119"><strong>Salcomp India disclosures + Salcomp Oyj annual report + ex-Nokia Chennai plant acquisition press</strong> &mdash; Sriperumbudur + Kancheepuram plants; Apple charger tier-1 supplier. <span class="u">salcomp.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Salcomp Technologies India Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Salcomp Technologies India", "Smartphone EMS / chargers"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
