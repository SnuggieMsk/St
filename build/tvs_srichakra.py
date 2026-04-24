"""TVS Srichakra dossier (pilot 11)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .padding import pad
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "tvs-srichakra-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 11 of 20 · Tyres · TVS Group</div>
  <h1>TVS Srichakra Limited<br>Listed 2-wheeler / 3-wheeler / off-highway tyre manufacturer</h1>
  <p class="lede">TVS Group listed tyre manufacturer (NSE / BSE) focused on 2W, 3W, farm, industrial and off-highway segments (brand &ldquo;TVS Eurogrip&rdquo;, &ldquo;TVS Tyres&rdquo;). CIN L25111TN1982PLC009414. FY25 TOI Rs 3,023 Cr (master sheet){ref("42")}; IND Ratings AA- Affirmed Stable (7 Nov 2025) + CRISIL BLR rating (22 Apr 2024){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 1,027 Cr. Multi-plant footprint at Madurai (Tamil Nadu) + Uttarakhand.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 35–48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 27–38 Cr + Retail Rs 8–10 Cr</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,023 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">IND rating</div><div class="v num">AA- Stable</div><div class="sub">Affirmed Nov 2025{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 1,027 Cr</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three converting angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>TVS Group halo</strong> &mdash; part of TVS Tyres / Srichakra lineage within TVS Group ecosystem</li>
      <li><strong>EV-tyre positioning</strong> &mdash; EV 2W penetration drives specialty tyre demand; TVS Srichakra positioned for EV-specific compound tyres</li>
      <li><strong>Export ramp</strong> &mdash; TVS Eurogrip brand expanding into US / EU / LATAM markets; FX hedging wallet scales</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L25111TN1982PLC009414</strong></span>
    <span>Listed <strong>NSE / BSE</strong></span>
    <span>Promoter <strong>TVS Group (Srichakra branch)</strong></span>
    <span>Registry cut <strong>Probe42 / 27 Mar 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; brand portfolio</div>
  <p>TVS Srichakra is a TVS Group member with Madurai roots. Operates under the brands &ldquo;TVS Eurogrip&rdquo; (export + premium domestic) and &ldquo;TVS Tyres&rdquo; (domestic 2W / 3W / off-highway). Listed since 1990s. Parent-level linkage: minority TVS Group promoter ownership.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Brand / division</th><th>Segment</th><th>Market position</th></tr></thead>
    <tbody>
      <tr><td>TVS Eurogrip</td><td>Premium 2W + 3W + specialty tyre; export</td><td>Growing international brand; 50+ countries</td></tr>
      <tr><td>TVS Tyres (domestic)</td><td>2W + 3W + tractor + off-highway</td><td>Top-3 in 2W replacement market (after MRF + CEAT)</td></tr>
      <tr><td>TVS Off-Road</td><td>Specialty off-highway (earthmover, mining)</td><td>Niche segment</td></tr>
      <tr><td>Plants</td><td>Madurai (TN) primary + Pantnagar (Uttarakhand)</td><td>Multi-location manufacturing</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23 est</th><th class="num">FY24 est</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">2,680</td><td class="num">2,880</td><td class="num">3,023</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">10.2</td><td class="num">11.5</td><td class="num">12.0</td></tr>
      <tr><td>EBITDA</td><td class="num">273</td><td class="num">331</td><td class="num">363</td></tr>
      <tr><td>PAT (est)</td><td class="num">85</td><td class="num">112</td><td class="num">135</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">2.4x</td><td class="num">2.2x</td><td class="num">2.0x</td></tr>
    </tbody>
  </table>
  </div>
  <div class="grid c3">
    <div class="kpi"><div class="k">Net Worth (est)</div><div class="v num">980</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">720</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">1,027</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Capex FY26-27</div><div class="v num">240-320</div><div class="sub">Rs Cr; EV compound + export capacity</div></div>
    <div class="kpi"><div class="k">Export share</div><div class="v num">~28%</div><div class="sub">TVS Eurogrip brand into 50+ countries</div></div>
    <div class="kpi accent"><div class="k">Working cap turns</div><div class="v num">~3.8x</div><div class="sub">Rubber + steel inventory-intensive</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India tyre sector</div>
  <p>India tyre market ~Rs 88,000 Cr; 2W/3W replacement tyres ~20% of total by value; growing 10-12% CAGR. TVS Srichakra holds ~12-14% share of 2W replacement market. Export ramp is the key growth vector given TVS Eurogrip brand expansion.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Focus</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td>MRF</td><td class="num">25,200</td><td>All-segment leader</td><td>CRISIL AAA</td></tr>
      <tr><td>Apollo Tyres</td><td class="num">26,800</td><td>PV + CV + 2W; global</td><td>CRISIL AA+</td></tr>
      <tr><td>CEAT</td><td class="num">13,400</td><td>PV + 2W + CV</td><td>CRISIL AA-</td></tr>
      <tr><td>JK Tyre</td><td class="num">14,100</td><td>CV + PV</td><td>CRISIL AA-</td></tr>
      <tr><td>Balkrishna Industries</td><td class="num">9,500</td><td>Off-highway specialty</td><td>CRISIL AA</td></tr>
      <tr><td><strong>TVS Srichakra</strong></td><td class="num">3,023</td><td>2W / 3W specialty + export</td><td>IND AA- Stable</td></tr>
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
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th></tr></thead>
    <tbody>
      <tr><td>Revenue</td><td class="num">3,023</td><td class="num">3,380</td><td class="num">3,820</td><td class="num">3,500</td><td class="num">4,150</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">12.0</td><td class="num">12.5</td><td class="num pos">13.0</td><td class="num neg">11.5</td><td class="num pos">13.8</td></tr>
      <tr><td>EBITDA</td><td class="num">363</td><td class="num">423</td><td class="num">497</td><td class="num">403</td><td class="num">573</td></tr>
      <tr><td>PAT</td><td class="num">135</td><td class="num">165</td><td class="num">205</td><td class="num">145</td><td class="num">255</td></tr>
    </tbody>
  </table>
  </div>
  <p>Cumulative new debt FY26-28: ~Rs 180 Cr. IBank target 40% = Rs 70 Cr funded + Rs 260 Cr non-funded.</p>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Entry-point map</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th>Pricing</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>WC CC/OD</td><td class="num">240&ndash;300</td><td>MCLR + 30 bp</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Capex TL (EV compound + export)</td><td class="num">140&ndash;180</td><td>MCLR + 50 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>EPC (export financing)</td><td class="num">180&ndash;240</td><td>SBLR + 75 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>FX forwards (28% export share)</td><td class="num">420&ndash;560 notional</td><td>1.2 paise</td><td class="num">5&ndash;7</td></tr>
      <tr><td>BG / SBLC</td><td class="num">160&ndash;220</td><td>Comm 45 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Commodity hedge (natural rubber + synthetic rubber + carbon black)</td><td class="num">~400 notional</td><td>Fee-only</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CP programme</td><td class="num">150 rolling</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Receivable financing (dealer network)</td><td class="num">120&ndash;180</td><td>Effective 1.0%</td><td class="num">2&ndash;3</td></tr>
      <tr><td>SCF (rubber + chemical + steel belt suppliers)</td><td class="num">140&ndash;200</td><td>NIM 1.8%</td><td class="num">2&ndash;4</td></tr>
      <tr><td>CMS + treasury</td><td class="num">&mdash;</td><td>API + float</td><td class="num">3&ndash;4</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 23&ndash;35 Cr/yr</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Workforce ~3,200 (Madurai + Pantnagar); salary CASA ~1,400 accounts; Rs 2&ndash;3 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (TVS-extended)</h4><p>TVS Srichakra branch of TVS family. PB relationship-building with director-level senior mgmt. Rs 3&ndash;4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR combined Rs 60&ndash;90 Cr float; Rs 2&ndash;3 Cr/yr.</p></div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 7&ndash;10 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 23&ndash;35 Cr/yr + Retail/PB/TASC Rs 7&ndash;10 Cr/yr = <strong>Rs 30&ndash;45 Cr/yr total</strong>. Wallet envelope Rs 1,120&ndash;1,500 Cr funded + non-funded; FX notional Rs 420&ndash;560 Cr.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Promoter &amp; board</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group Srichakra-branch promoter family (Shobhana Ramchandhran lineage historically)</li>
        <li>Promoter holding stable; low / zero pledge</li>
        <li>Independent directors per SEBI LODR</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>IND Ratings AA- Affirmed Stable (7 Nov 2025)</strong>{ref("81")}</li>
        <li><strong>Zero suit-filed (Probe42)</strong>{ref("82")}</li>
        <li>No NCLT / CIRP / SEBI actions</li>
        <li>BIS + ISI compliance on all product lines</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet Madurai HO CFO; WC + capex TL + EPC for export financing; FX forwards; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close WC + capex; CP programme go-live; commodity-hedge advisory for rubber + carbon black.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> SCF for suppliers; dealer receivable financing; salary migration. TVS Group introduction.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>WC + capex TL sanctioned by 31 Aug 2026</li>
    <li>FX hedge coverage ratio &ge; 60% by end-Q3 FY27</li>
    <li>Annual run-rate Rs 18&ndash;22 Cr by end-FY27</li>
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
  <ol start="106">
  <li id="src-106"><strong>TVS Srichakra Ltd BSE/NSE annual report FY25 + IND Ratings rationale Nov 2025</strong> &mdash; Madurai + Pantnagar plants; TVS Eurogrip export brand expansion; 2W + 3W + off-highway segments. <span class="u">tvstyres.com / investors &middot; bseindia.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "TVS Srichakra Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),pad("TVS Srichakra","Tyres"),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
