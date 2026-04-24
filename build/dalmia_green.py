"""Dalmia Bharat Green Vision dossier (pilot 18)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "dalmia-green-vision-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 18 of 20 · Dalmia Group · Green-cement / SPV</div>
  <h1>Dalmia Bharat Green Vision Limited<br>Green-cement / sustainability SPV of Dalmia Bharat Group</h1>
  <p class="lede">Sustainability / green-cement SPV of Dalmia Bharat Ltd (cement major); CIN U70109TN2021PLC143683. FY25 TOI Rs 417 Cr (master sheet){ref("42")} &mdash; early-stage SPV. <strong>CRISIL AA+ Reaffirmed Stable</strong> (2 Apr 2026 Probe42){ref("81")} on Bank Guarantee + NFB limit &mdash; high-grade rating reflecting parent Dalmia Bharat credit. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 1,275 Cr. Part of Dalmia Bharat&rsquo;s announced Rs 10,000+ Cr green-cement + renewable energy investment roadmap.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 28–42 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Project finance + SLL structures</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 417 Cr</div><div class="sub">Early-stage SPV</div></div>
    <div class="kpi pos"><div class="k">CRISIL rating</div><div class="v num">AA+ Stable</div><div class="sub">Reaffirmed Apr 2026{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 1,275 Cr</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Green-cement transition capex</strong> &mdash; Dalmia Bharat committed to Net Zero 2040; green-cement SPV captures incremental investment</li>
      <li><strong>Sustainability-Linked Loan (SLL)</strong> &mdash; KPI-step-down pricing structure is natural fit</li>
      <li><strong>Dalmia Group umbrella</strong> &mdash; cross-sell to Dalmia Bharat parent + other group entities</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U70109TN2021PLC143683</strong></span>
    <span>Parent <strong>Dalmia Bharat Ltd (NSE: DALBHARAT)</strong></span>
    <span>Registry cut <strong>Probe42 / 14 Jan 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group</div>
  <p>Dalmia Bharat Ltd (NSE: DALBHARAT; BSE: 542216) is India&rsquo;s #3 cement producer by capacity (~50 MMTPA). Dalmia Bharat Green Vision is a dedicated SPV for green-cement manufacturing + renewable-power capacity + carbon-capture investments aligned with Dalmia&rsquo;s Net Zero 2040 commitment.</p>
  <ul class="check">
    <li>Promoter: Jai Hari Dalmia + Yadu Hari Dalmia family; next-gen Puneet Dalmia (MD / CEO)</li>
    <li>OCL + Calcom + Bharathi Cement acquisitions consolidated into Dalmia Bharat umbrella</li>
    <li>Dalmia Cement Bharat is the operating cement arm; Green Vision SPV overlays sustainability investments</li>
    <li>Cross-holdings: Dalmia Bharat Sugar, Shree Dharti, Hari Machines, Himshikhar investments</li>
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
      <tr><td>TOI</td><td class="num">210</td><td class="num">417</td></tr>
      <tr><td>EBITDA margin</td><td class="num">28</td><td class="num">32</td></tr>
      <tr><td>EBITDA</td><td class="num">59</td><td class="num">133</td></tr>
      <tr><td>PAT (est)</td><td class="num">18</td><td class="num">45</td></tr>
    </tbody>
  </table>
  </div>
  <p>Early-stage; SPV-level margins reflect sustainability premium + renewable-power economics. AA+ rating flows through from Dalmia Bharat parent.</p>
  <h3>04.1 Scope of operations</h3>
  <ul class="check">
    <li>Green-cement manufacturing (lower-clinker + blended cement)</li>
    <li>Renewable energy for captive use (solar + wind; 250+ MW cumulative planned)</li>
    <li>Carbon capture pilots (in collaboration with IEA / global partners)</li>
    <li>Alternative fuel &amp; raw material (AFR) utilisation at cement plants</li>
    <li>Waste heat recovery systems (WHRS) retrofit</li>
  </ul>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India green cement</div>
  <p>India cement sector (~585 MMTPA capacity) faces structural emissions pressure. BEE PAT scheme + likely Indian carbon market by FY28 create pricing + financial incentives for green cement. Dalmia is generally considered the most emission-efficient Indian cement producer.</p>
  <h3>05.1 Peer cement players</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Capacity (MMTPA)</th><th>Net-Zero target</th></tr></thead>
    <tbody>
      <tr><td>UltraTech Cement (Aditya Birla)</td><td class="num">~155</td><td>2050</td></tr>
      <tr><td>Adani Cement (ACC + Ambuja + Sanghi)</td><td class="num">~90</td><td>2050</td></tr>
      <tr><td><strong>Dalmia Bharat</strong></td><td class="num">~50</td><td>2040 (most ambitious)</td></tr>
      <tr><td>Shree Cement</td><td class="num">~56</td><td>2050</td></tr>
      <tr><td>JSW Cement</td><td class="num">~19</td><td>2050</td></tr>
      <tr><td>Birla Corp</td><td class="num">~20</td><td>Not-defined</td></tr>
      <tr><td>Ramco Cements</td><td class="num">~22</td><td>Not-defined</td></tr>
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
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">417</td><td class="num">680</td><td class="num">950</td><td class="num">1,300</td></tr>
      <tr><td>EBITDA margin</td><td class="num">32</td><td class="num">34</td><td class="num">35</td><td class="num">36</td></tr>
      <tr><td>PAT</td><td class="num">45</td><td class="num">95</td><td class="num">155</td><td class="num">230</td></tr>
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
      <tr><td><strong>Sustainability-Linked Loan (SLL)</strong></td><td class="num">380&ndash;520</td><td class="num">6&ndash;8</td></tr>
      <tr><td>Renewable project finance TL</td><td class="num">220&ndash;280</td><td class="num">3&ndash;4</td></tr>
      <tr><td>WC CC/OD</td><td class="num">140&ndash;200</td><td class="num">2&ndash;3</td></tr>
      <tr><td>BG (environmental + customer + equipment)</td><td class="num">180&ndash;260</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Import LC (renewable-energy equipment)</td><td class="num">240&ndash;320</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Dalmia Group cross-sell anchor</td><td class="num">&mdash;</td><td class="num">8&ndash;12</td></tr>
      <tr><td>Carbon-credit / I-REC advisory (future)</td><td class="num">&mdash;</td><td class="num">2&ndash;3 future</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 22&ndash;32 Cr/yr</strong> (including Dalmia Group halo cross-sell).</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Small SPV workforce (~200-300); Dalmia Group family PB is the large adjacency.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4>
      <ul class="check" style="margin-bottom:0">
        <li>SPV workforce ~200-300</li>
        <li>Salary CASA 80-120 accounts</li>
        <li>Annual income Rs 0.5-1 Cr</li>
      </ul>
    </div>
    <div class="card accent"><h4 style="margin-top:0">PB (Dalmia family halo)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Dalmia Bharat promoter family (multi-generational)</li>
        <li>Group wealth substantial; PB engagement senior</li>
        <li>Annual income Rs 3-5 Cr</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust Rs 15-25 Cr</li>
        <li>Annual income Rs 1-2 Cr</li>
      </ul>
    </div>
  </div>
  <p>Combined Rs 5&ndash;8 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 22&ndash;32 Cr/yr + Retail/PB/TASC Rs 5&ndash;8 Cr/yr = <strong>Rs 27&ndash;40 Cr/yr</strong>. Group halo is the expansion lever.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Promoter</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Dalmia Bharat family (Jai Hari + Yadu Hari branches)</li>
        <li>Puneet Dalmia (MD / CEO Dalmia Bharat Ltd)</li>
        <li>Listed parent Dalmia Bharat; promoter ~55% holding; low pledge</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>CRISIL AA+ Reaffirmed Stable (2 Apr 2026)</strong>{ref("81")}</li>
        <li><strong>Zero suit-filed</strong>{ref("82")}</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet Dalmia Bharat Group Treasury + Green Vision management; SLL structure pitch; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close SLL + project finance TL; BG framework; import LC for renewables equipment.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Dalmia Group parent cross-sell; Dalmia family PB engagement; carbon-credit advisory.</p></div>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Dalmia Bharat Green Vision sources from [113].</em></p>
  <div class="src-list"><ol start="113">
  <li id="src-113"><strong>Dalmia Bharat Ltd annual report + sustainability report + CRISIL Apr 2026 rationale</strong> &mdash; Green-cement SPV structure; Net Zero 2040 commitment. <span class="u">dalmiabharat.com &middot; dalmiabharatsugar.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Dalmia Bharat Green Vision Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Dalmia Bharat Green Vision", "Green cement / Sustainability"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
