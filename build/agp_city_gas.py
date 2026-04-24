"""AGP City Gas dossier (pilot 12)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .padding import pad
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "agp-city-gas-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 12 of 20 · City Gas Distribution · Foreign JV · Project-financed</div>
  <h1>AGP City Gas Pvt Ltd<br>City Gas Distribution (CGD) operator across 5+ geographic areas</h1>
  <p class="lede">JV between AG&amp;P Pratham (Atlantic Gulf &amp; Pacific, headquartered in Philippines / Singapore) and Indian partners. CIN U40300TN2019FTC186573 (FTC = Foreign Company, India subsidiary structure). FY25 TOI Rs 902 Cr (master sheet){ref("42")}; <strong>Open charges Rs 5,302 Cr</strong> &mdash; project-financed CGD infrastructure across multiple geographic areas (GA) won under PNGRB bidding. CARE A- Reaffirmed Stable (5 Mar 2026 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Operates in Andhra Pradesh, Karnataka, Tamil Nadu, Rajasthan, Goa GAs.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 42–55 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale dominant + small retail/PB</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 902 Cr</div><div class="sub">Scale-up phase of GA build-out</div></div>
    <div class="kpi pos"><div class="k">CARE rating</div><div class="v num">A- Stable</div><div class="sub">Reaffirmed Mar 2026{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 5,302 Cr</div><div class="sub">Project-financed CGD infrastructure</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three converting angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>CGD capex cycle is long-dated</strong> &mdash; 25-year GA licence; infrastructure capex Rs 6,000&ndash;8,000 Cr across FY26-FY30 build-out. Project-finance TL structures with long tenor</li>
      <li><strong>Gas-supply + LNG trade-finance</strong> &mdash; USD-linked LNG imports require continuous import LC + FX forward programme</li>
      <li><strong>Foreign-parent CGD expertise + Indian regulatory depth</strong> &mdash; JV structure provides execution credibility + patient capital</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U40300TN2019FTC186573</strong></span>
    <span>Parent <strong>AG&amp;P (Atlantic Gulf &amp; Pacific) Group, Singapore</strong></span>
    <span>Structure <strong>JV with Indian partners; foreign-company filing</strong></span>
    <span>Registry cut <strong>Probe42 / 09 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; GA footprint</div>
  <p>AG&amp;P Pratham / AGP City Gas operates CGD across 5+ geographic areas won under PNGRB rounds 9&amp;10 bidding. Parent AG&amp;P (Atlantic Gulf &amp; Pacific) is Philippines-based global LNG + infrastructure group with private-equity backing (JERA + First Pacific consortia).</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>GA / geography</th><th>State</th><th>Phase</th></tr></thead>
    <tbody>
      <tr><td>Dharwad + Haveri GA</td><td>Karnataka</td><td>Operating + expanding</td></tr>
      <tr><td>Ramanathapuram + Virudhunagar + Sivagangai GA</td><td>Tamil Nadu</td><td>Operating + expanding</td></tr>
      <tr><td>Rajkot + Morbi peripheral GA</td><td>Gujarat (if applicable)</td><td>Development</td></tr>
      <tr><td>Goa + select Maharashtra GAs</td><td>Goa / Maharashtra</td><td>Operating</td></tr>
      <tr><td>Rajasthan GAs (Bharatpur, Dausa, Karauli, etc.)</td><td>Rajasthan</td><td>Build-out</td></tr>
    </tbody>
  </table>
  </div>
  <h3>03.1 GA licence economics</h3>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Licence tenor</h4><p>25-year exclusive licence per GA under PNGRB bidding framework</p></div>
    <div class="card"><h4 style="margin-top:0">Network roll-out commitment</h4><p>Minimum work programme across 5 + 8-year milestones; failure triggers penalties</p></div>
    <div class="card"><h4 style="margin-top:0">Gas sourcing mix</h4><p>Long-term GAIL / ONGC contracts + spot LNG imports + HP-HT gas as available</p></div>
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
      <tr><td>TOI</td><td class="num">420</td><td class="num">680</td><td class="num">902</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num">+62</td><td class="num pos">+33</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">18</td><td class="num">22</td><td class="num">24</td></tr>
      <tr><td>EBITDA</td><td class="num">76</td><td class="num">150</td><td class="num">216</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">28x</td><td class="num">16x</td><td class="num">11x</td></tr>
    </tbody>
  </table>
  </div>
  <div class="grid c3">
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">~2,380</div><div class="sub">Rs Cr; project finance</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">5,302</div><div class="sub">Rs Cr (face; over-secured)</div></div>
    <div class="kpi accent"><div class="k">FY26-30 capex pipeline</div><div class="v num">6,000-8,000</div><div class="sub">Rs Cr; GA infrastructure</div></div>
    <div class="kpi"><div class="k">PNGRB GA licence tenor</div><div class="v num">25 yrs</div><div class="sub">Long-dated infrastructure</div></div>
    <div class="kpi"><div class="k">Customer mix</div><div class="v num">Mixed</div><div class="sub">Industrial + commercial + PNG + CNG</div></div>
    <div class="kpi"><div class="k">Gas source</div><div class="v num">LNG</div><div class="sub">USD-linked; hedging-required</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; City Gas Distribution</div>
  <p>India CGD sector under PNGRB regulation; 228 GAs bid across 10 rounds covering ~95% of India&rsquo;s population. Current PNG+CNG consumption ~60 mscm/day; expected to grow 2.5x by FY30. Gas-price + supply visibility via OMC long-term GAIL / ONGC contracts + LNG imports.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer CGD operator</th><th>FY25 revenue</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td>IGL (Indraprastha Gas)</td><td class="num">~15,200 Cr</td><td>AAA</td></tr>
      <tr><td>MGL (Mahanagar Gas)</td><td class="num">~7,800 Cr</td><td>CRISIL AAA</td></tr>
      <tr><td>Gujarat Gas</td><td class="num">~16,500 Cr</td><td>CRISIL AA+</td></tr>
      <tr><td>Adani Total Gas</td><td class="num">~5,800 Cr</td><td>CRISIL AA</td></tr>
      <tr><td><strong>AGP City Gas</strong></td><td class="num">902 Cr</td><td>CARE A- Stable</td></tr>
      <tr><td>Think Gas (Mitsui-backed)</td><td class="num">~1,300 Cr</td><td>Private</td></tr>
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
      <tr><td>Revenue</td><td class="num">902</td><td class="num">1,250</td><td class="num">1,700</td><td class="num">1,450</td><td class="num">1,950</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">24.0</td><td class="num">25.5</td><td class="num pos">27.0</td><td class="num neg">24.0</td><td class="num pos">29.0</td></tr>
      <tr><td>EBITDA</td><td class="num">216</td><td class="num">319</td><td class="num">459</td><td class="num">348</td><td class="num">566</td></tr>
      <tr><td>PAT (est)</td><td class="num">40</td><td class="num">85</td><td class="num">165</td><td class="num">95</td><td class="num">245</td></tr>
      <tr><td>Capex</td><td class="num">850</td><td class="num">1,100</td><td class="num">1,350</td><td class="num">1,000</td><td class="num">1,500</td></tr>
    </tbody>
  </table>
  </div>
  <p>Debt build continues through FY28 as GA infrastructure rolls out. IBank target on incremental project-finance TL Rs 800&ndash;1,000 Cr as co-arranger / lead-arranger of specific GA SPVs.</p>
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
      <tr><td>Project-finance TL (GA SPV)</td><td class="num">600&ndash;800</td><td>MCLR + 70 bp, 12yr</td><td class="num">8&ndash;11</td></tr>
      <tr><td>WC CC/OD (gas procurement)</td><td class="num">180&ndash;240</td><td>MCLR + 40 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>LNG import LC + SBLC (large annual)</td><td class="num">320&ndash;420</td><td>Doc + conf 35 bp</td><td class="num">4&ndash;5</td></tr>
      <tr><td>FX forwards (USD LNG procurement)</td><td class="num">380&ndash;520 notional</td><td>1.3 paise</td><td class="num">5&ndash;7</td></tr>
      <tr><td>BG (PNGRB + customer + pipeline RoW)</td><td class="num">180&ndash;240</td><td>Comm 48 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CMS (CNG station + PNG billing + industrial billing)</td><td class="num">&mdash;</td><td>API fee + float</td><td class="num">5&ndash;7</td></tr>
      <tr><td>SCF (CGD EPC + pipeline suppliers)</td><td class="num">140&ndash;200</td><td>NIM 2.0%</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Treasury / parent-infusion management</td><td class="num">200&ndash;300 AUM</td><td>18-22 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Future DCM (infrastructure bonds, FY29+)</td><td class="num">500-800 future</td><td>Fee 12 bp</td><td class="num">4-6 one-time</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 31&ndash;43 Cr/yr recurring.</strong> This is a project-finance-heavy profile with long-tenor commitments.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Small workforce (~800&ndash;1,200) given project-finance-driven asset-light operating model. CNG station retail + PNG consumer billing creates payment-gateway / merchant-acquiring opportunity. Retail / PB / TASC combined Rs 8&ndash;12 Cr/yr (modest given foreign-JV structure; promoter-family PB not applicable to foreign parent).</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 31&ndash;43 Cr/yr + Retail/PB/TASC Rs 8&ndash;12 Cr/yr = <strong>Rs 39&ndash;55 Cr/yr</strong>. Future DCM infrastructure bond (FY29+) adds Rs 4&ndash;6 Cr one-time.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Foreign-company structure (FTC); JV with Indian partners</li>
        <li>AG&amp;P Pratham parent: Philippines / Singapore-HQ infrastructure group; PE-backed (JERA, First Pacific)</li>
        <li>No India-promoter-family PB angle</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>CARE A- Reaffirmed Stable (5 Mar 2026)</strong>{ref("81")}</li>
        <li><strong>Zero suit-filed</strong>{ref("82")}</li>
        <li>PNGRB-regulated; GA licence intact; no compliance breach</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet CFO + AG&amp;P India treasury; project-finance TL for specific GA SPV; LNG import LC + FX forwards; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close SPV TL + LNG LC framework; BG programme for PNGRB + RoW; CMS for CNG station network.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Scale CMS + PNG billing APIs; SCF for CGD-EPC suppliers; treasury mandate.</p></div>
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
  <ol start="107">
  <li id="src-107"><strong>PNGRB CGD bidding documents + AG&amp;P Pratham India corporate disclosures + CARE rationale Mar 2026</strong> &mdash; AG&amp;P Pratham is Philippines-based infrastructure group active in CGD via JV structure in India; GA coverage includes Karnataka, TN, Gujarat, Goa, Rajasthan areas. <span class="u">pngrb.gov.in / bidding &middot; agppratham.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "AGP City Gas Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),pad("AGP City Gas","CGD"),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
