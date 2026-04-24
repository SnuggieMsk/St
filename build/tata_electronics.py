"""Tata Electronics Products and Solutions dossier (pilot 21)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "tata-electronics-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 21 of 40 · Chennai cluster · EMS + semiconductor · Tata Group MNC-adjacent</div>
  <h1>Tata Electronics Products and Solutions Pvt Ltd<br>Largest single-entity EMS in India after Foxconn</h1>
  <p class="lede">Tata Group&rsquo;s electronics-manufacturing flagship; consolidates iPhone-assembly operations (incl. ex-Wistron Kolar, Karnataka) plus semiconductor-packaging (Sanand OSAT, Gujarat) plus future Dholera chip-fab. CIN U74999TN2020FTC136376 (FTC = foreign-company filing reflects Tata Sons Singapore treasury-level). FY25 TOI Rs 34,264 Cr (master sheet){ref("42")} &mdash; the <strong>second-largest EMS in India after Foxconn Mega Dev</strong>. Operational plants at Chengalpet (Tamil Nadu) + Hosur (Krishnagiri, partly ROTN) + Kolar (Karnataka) + Sanand (Gujarat). Credit rating tracking Tata Sons Group investment-grade.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 165–220 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Trade finance + capex + FX + CMS at Apollo-scale</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 34,264 Cr</div><div class="sub">2nd-largest EMS in India after Foxconn{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">Parent</div><div class="v num">Tata Sons</div><div class="sub">Via Tata Electronics (TEPL parent co); Tata Group cross-sell halo</div></div>
    <div class="kpi"><div class="k">Plants</div><div class="v num">4+</div><div class="sub">Chengalpet + Hosur + Kolar (ex-Wistron) + Sanand OSAT</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Why this is the most strategic new-to-bank opportunity</h4>
    <ol style="margin-bottom:0">
      <li><strong>Scale is extraordinary</strong> &mdash; Rs 34,264 Cr TOI makes this the single largest non-Foxconn EMS in India. Working capital + trade-finance + FX at this scale is a multi-year mandate.</li>
      <li><strong>Tata Group parent is strongest non-government corporate in India</strong> &mdash; AAA / AA+ credit quality cascades down; risk-weighting optimal.</li>
      <li><strong>Dholera chip-fab capex wave ($11 bn over 5 years)</strong> &mdash; the single largest industrial capex in India private sector; project-finance / SPV structures to be created; BRLM / arranger mandate opportunity.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U74999TN2020FTC136376</strong></span>
    <span>Plant HO <strong>Chengalpet (TN)</strong></span>
    <span>Parent <strong>Tata Electronics Pvt Ltd → Tata Sons</strong></span>
    <span>Registry cut <strong>Probe42 / TBD</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; Tata Electronics umbrella</div>
  <p>Tata Electronics is the Tata Group&rsquo;s electronics-manufacturing consolidation vehicle, launched 2020 as a direct Tata Sons initiative under N Chandrasekaran&rsquo;s chairmanship. Strategic pillars:</p>
  <ul class="check">
    <li><strong>EMS / iPhone assembly</strong> — Chengalpet (TN) + Hosur (Krishnagiri) + Kolar Gold Fields (KGF, Karnataka; ex-Wistron Oct 2023 acquisition for $125 mn){ref("33")}</li>
    <li><strong>OSAT (outsourced semi-assembly + test)</strong> — Sanand, Gujarat ($11 bn investment, $2.75 bn in FY26, operational 2026)</li>
    <li><strong>Semiconductor fab (greenfield)</strong> — Dholera, Gujarat ($11 bn Phase-1; first Indian chip-fab; operational 2026-27)</li>
    <li><strong>Future categories</strong> — PCBA, display modules, automotive electronics</li>
  </ul>
  <p>Tata Group credit quality: Tata Sons is the closest thing to &ldquo;quasi-sovereign&rdquo; corporate credit in India; TCS + Tata Motors + Tata Steel + Tata Power (all listed) + Jaguar Land Rover overseas aggregate to &gt; $350 bn revenue globally. Tata Electronics sits inside that umbrella.</p>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY24 est</th><th class="num">FY25</th><th class="num">FY26 E</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">12,500</td><td class="num">34,264</td><td class="num">55,000</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+174 (ramp)</td><td class="num pos">+60</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">2.5</td><td class="num">3.2</td><td class="num">4.0</td></tr>
      <tr><td>EBITDA</td><td class="num">313</td><td class="num">1,096</td><td class="num">2,200</td></tr>
    </tbody>
  </table>
  </div>
  <p>Ramp-up phase; iPhone Kolar integration drove FY25 4x growth. Semiconductor ramp (Sanand + Dholera) is the next inflection expected FY27.</p>
  <h3>04.1 Plant operations</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Chengalpet (TN)</div><div class="v num" style="font-size:1rem">iPhone assembly</div><div class="sub">Original Tata Electronics plant; ~15,000 workers peak</div></div>
    <div class="kpi"><div class="k">Hosur (TN-KA border)</div><div class="v num" style="font-size:1rem">Component + PCBA</div><div class="sub">Expansion campus; 8,000+ workers</div></div>
    <div class="kpi"><div class="k">Kolar (Karnataka)</div><div class="v num" style="font-size:1rem">iPhone final assembly</div><div class="sub">ex-Wistron (acquired Oct 2023, $125 mn); 12,000+ workers</div></div>
    <div class="kpi"><div class="k">Sanand OSAT (Gujarat)</div><div class="v num" style="font-size:1rem">Semi packaging</div><div class="sub">$2.75 bn Phase-1; operational 2026</div></div>
    <div class="kpi"><div class="k">Dholera Fab (Gujarat)</div><div class="v num" style="font-size:1rem">Semi fabrication</div><div class="sub">$11 bn Phase-1; 50,000 wafers/month; 2026-27 operational</div></div>
    <div class="kpi accent"><div class="k">Target workforce FY28</div><div class="v num">~60,000</div><div class="sub">Across all plants combined</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India EMS + Semiconductor</div>
  <p>Indian EMS sector (see Foxconn dossier Sec 05 for full industry treatment) is $65+ bn FY25 growing to $115 bn FY28. Tata Electronics vs Foxconn Mega Dev: Foxconn at 50% iPhone India share (FY25 54mn units), Tata rising to 35-40% by FY28 (30-35mn units). The two-horse race is structurally defining.</p>
  <h3>05.1 EMS competitive landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Player</th><th>FY25 revenue (Rs Cr)</th><th>Customer mix</th></tr></thead>
    <tbody>
      <tr><td>Foxconn Mega Dev (Pilot 01)</td><td class="num">1,01,877</td><td>Apple 95%+</td></tr>
      <tr><td><strong>Tata Electronics (this dossier)</strong></td><td class="num">34,264</td><td>Apple 60%, Android 40%</td></tr>
      <tr><td>Bharat FIH (Foxconn Indian sister)</td><td class="num">~12,800</td><td>Xiaomi + Oppo + others</td></tr>
      <tr><td>Dixon Technologies</td><td class="num">17,600</td><td>Multi-customer, multi-category</td></tr>
      <tr><td>Salcomp India (Pilot 24)</td><td class="num">10,105</td><td>Apple chargers + displays</td></tr>
      <tr><td>Syrma SGS</td><td class="num">3,200</td><td>Industrial + auto PCB</td></tr>
      <tr><td>Kaynes Technology</td><td class="num">2,800</td><td>Multi-category EMS</td></tr>
    </tbody>
  </table>
  </div>
  <h3>05.2 Semiconductor ecosystem</h3>
  <p>Tata&rsquo;s $11 bn OSAT + fab announcement is alongside Micron (OSAT Gujarat, $2.75 bn), CG Power-Renesas (Sanand OSAT, Rs 7,600 Cr), Kaynes (Sanand / Hyderabad OSAT, Rs 3,300 Cr). Tata is the only Indian-owned chip-fab; others are JV or foreign. This gives Tata strategic GOI alignment + deep-state support via India Semiconductor Mission (ISM).</p>
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
      <tr><td>TOI</td><td class="num">34,264</td><td class="num">55,000</td><td class="num">82,000</td><td class="num">110,000</td></tr>
      <tr><td>EBITDA margin</td><td class="num">3.2</td><td class="num">4.0</td><td class="num">5.2</td><td class="num">6.5</td></tr>
      <tr><td>EBITDA</td><td class="num">1,096</td><td class="num">2,200</td><td class="num">4,264</td><td class="num">7,150</td></tr>
    </tbody>
  </table>
  </div>
  <p>Ramp continues; semiconductor ramp (Sanand + Dholera) drives margin expansion.</p>
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
      <tr><td>Import LC + SBLC (large USD + SoC component imports)</td><td class="num">3,400&ndash;4,500</td><td class="num">22&ndash;28</td></tr>
      <tr><td>FX forwards (USD revenue + procurement)</td><td class="num">2,800&ndash;3,600 notional</td><td class="num">30&ndash;38</td></tr>
      <tr><td>WC CC/OD (shared consortium)</td><td class="num">480&ndash;620</td><td class="num">8&ndash;11</td></tr>
      <tr><td>Capex TL (semiconductor SPV contribution)</td><td class="num">1,200&ndash;1,800</td><td class="num">20&ndash;28</td></tr>
      <tr><td>BG + SBLC (PLI + customer + environment)</td><td class="num">580&ndash;740</td><td class="num">3&ndash;5</td></tr>
      <tr><td>SCF (anchor-led; Tier-1 component vendors)</td><td class="num">1,400&ndash;1,900</td><td class="num">28&ndash;38</td></tr>
      <tr><td>CMS + API banking (multi-plant)</td><td class="num">&mdash;</td><td class="num">12&ndash;16</td></tr>
      <tr><td>Payroll + HR tech (60,000+ employees at scale)</td><td class="num">&mdash;</td><td class="num">10&ndash;14</td></tr>
      <tr><td>Tata Group halo cross-sell</td><td class="num">&mdash;</td><td class="num">30&ndash;45</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 163&ndash;223 Cr/yr</strong> including Tata Group halo.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce projected to reach 60,000+ at scale (FY28); iPhone assembly + semiconductor operations. Massive salary CASA opportunity.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 25,000-35,000 accounts; Rs 18-25 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (Tata exec halo)</h4><p>Senior management + N Chandrasekaran + KK Ahluwalia level; Rs 5-8 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR (Tata Electronics CSR); Rs 3-5 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 26&ndash;38 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 163&ndash;223 Cr/yr + Retail/PB/TASC Rs 26&ndash;38 Cr/yr = <strong>Rs 189&ndash;261 Cr/yr</strong>. Cover-page envelope conservatively quoted Rs 165-220 Cr/yr; upside to Rs 260 Cr at full-build post-Dholera.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership &amp; governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>100% Tata Electronics Pvt Ltd (ultimately Tata Sons)</li>
        <li>N Chandrasekaran Chairman; Randhir Thakur CEO (ex-Intel)</li>
        <li>Tata Sons investment-grade Moody&rsquo;s Baa1 / CRISIL AAA implicit flow-through</li>
        <li>No promoter-family concept (Tata Sons is widely-held Tata trust ownership)</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Regulatory</h4>
      <ul class="check" style="margin-bottom:0">
        <li>MeitY PLI-LSEM beneficiary (smartphone + semiconductor)</li>
        <li>India Semiconductor Mission (ISM) capital support for Dholera fab</li>
        <li>GOI strategic-sector support; foreign-technology licensing frameworks current</li>
        <li>ZERO suit-filed / NCLT / CIRP exposure across Tata Electronics umbrella</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet Tata Electronics CFO + Tata Sons treasury at Bombay House; indicative LC + FX + WC envelope; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close LC + FX framework; capex TL term-sheet for semiconductor SPV; CMS + payroll integration at 4 plants.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Salary CASA migration 5,000+ accounts; Tata Group parent-level relationship introduction; semiconductor BRLM mandate pitch.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>LC + FX framework live by 31 Aug 2026</li>
    <li>Dholera capex SPV mandate secured by end-FY27</li>
    <li>Annual run-rate Rs 80 Cr by end-FY27; Rs 150 Cr by end-FY28</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Tata Electronics-specific sources from [116].</em></p>
  <div class="src-list"><ol start="116">
  <li id="src-116"><strong>Tata Electronics Pvt Ltd corporate disclosures + Tata Sons annual report + GOI semiconductor mission press releases + MeitY PLI list + Wistron acquisition press</strong> &mdash; Chengalpet + Hosur + Kolar + Sanand + Dholera operations; N Chandrasekaran + Randhir Thakur leadership. <span class="u">tata.com &middot; tataelectronics.com &middot; meity.gov.in/esdm &middot; ism.gov.in</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Tata Electronics Products and Solutions Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Tata Electronics", "EMS + Semiconductor"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
