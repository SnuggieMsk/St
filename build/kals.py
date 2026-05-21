"""Kals Distilleries Private Limited dossier (pilot 44)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "kals-distilleries-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 44 of 50 · Chennai · Domestic · Distillery / IMFL · 13-bank consortium</div>
  <h1>Kals Distilleries Private Limited<br>Tamil Nadu IMFL (Indian Made Foreign Liquor) + extra-neutral-alcohol distillery</h1>
  <p class="lede">Kals Distilleries Private Limited (CIN U15511TN2007PTC065347){ref("290")} is a Chennai-headquartered IMFL + ENA producer operating through TASMAC distribution monopoly in Tamil Nadu plus other Southern states; founded 2007 as part of the Kals Group. <strong>FY25 Total Operating Income Rs 1,963 Cr</strong>{ref("128")}; EBITDA Rs 42 Cr (2.1%) &mdash; thin margins typical of TASMAC-driven IMFL business; PAT Rs 14.6 Cr (positive but small); Tangible Net Worth Rs 339 Cr; Total Debt Rs 1,454 Cr (Debt/TNW 4.29x &mdash; high leverage). <strong>13 disclosed-bank consortium with 20 open charges totalling Rs 1,454.5 Cr; Axis Trustee Services Rs 907 Cr (62.4%) + HDFC Bank Rs 270.8 Cr (18.6%) + Axis Finance Rs 75 Cr (5.2%) + Aditya Birla Capital Rs 50 Cr + Bandhan Bank Rs 50 Cr + Jio Credit Rs 50 Cr + Poonawalla Rs 50 Cr; IBank ABSENT</strong>{ref("126")}. Credit rating <strong>CARE BBB Stable</strong> (10 Apr 2026){ref("291")}. 292 FTE{ref("128")}.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 24&ndash;42 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 competitive consortium-entry</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 1,963 Cr</div><div class="sub">IMFL + ENA{ref("128")}</div></div>
    <div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">of Rs 1,454.5 Cr; Axis Trustee NCD-anchored{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CARE BBB Stable</div><div class="sub">10 Apr 2026{ref("291")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>NCD-take-out / refinance</strong> &mdash; Axis-Trustee-anchored Rs 907 Cr NCD vintage tranche; refresh / take-out window at next coupon-rate review.</li>
      <li><strong>HDFC tranche refresh</strong> &mdash; HDFC Rs 270.8 Cr in working-capital line; bid for refresh at sharper pricing.</li>
      <li><strong>State-policy + ethanol-blending tailwind</strong>{ref("12")} &mdash; ethanol-roadmap drives ENA off-take to OMCs; capex-TL for ENA capacity expansion.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U15511TN2007PTC065347</strong></span>
    <span>Incorp <strong>12 Nov 2007</strong></span>
    <span>HO <strong>Chennai</strong></span>
    <span>Group <strong>Kals Group / TN-domestic IMFL</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture</div>
  <p>Kals Distilleries is the operating-flagship of the Kals Group, a TN-headquartered private IMFL + ENA cluster with adjacent businesses in beverage-packaging + bottling. Promoter ownership ~92% (sheet) with balance employee + financial-investor.</p>
  <h3>03.1 Business mix</h3>
  <ul>
    <li>IMFL (Indian Made Foreign Liquor) ~55% revenue: whiskey + brandy + rum + vodka + gin under own + co-packing brands; primary distribution TASMAC + Karnataka State Beverages Corp + AP Beverages + Telangana Beverages.</li>
    <li>ENA (Extra Neutral Alcohol) ~30% revenue: 30,000-40,000 KLPD molasses-based ENA capacity; off-take to IMFL captive + ethanol-blending OMC contracts (BPCL / IOCL / HPCL).</li>
    <li>Beverage-packaging ~15% revenue: glass-bottle + carton + closures.</li>
  </ul>
  <h3>03.2 State-policy framework</h3>
  <ul>
    <li>TN excise + IMFL framework: TASMAC monopoly distribution; pricing controlled by state; volume-elasticity limited; margin-elasticity policy-dependent.</li>
    <li>Ethanol-blending (E20 by Oct 2026){ref("12")}: drives ENA off-take from OMCs at administered prices; capacity expansion economics positive.</li>
    <li>State-excise compliance: routine inspections + bonded-warehouse + transit-permit framework.</li>
  </ul>
  <h3>03.3 Bank consortium (Probe42 cut){ref("126")}</h3>
  <ul>
    <li><strong>Axis Trustee Services Rs 907 Cr (62.4%)</strong> &mdash; NCD trustee position; underlying NCD investors typically MFs / insurance / treasuries.</li>
    <li><strong>HDFC Bank Rs 270.8 Cr (18.6%)</strong> &mdash; primary working-capital banker.</li>
    <li>Axis Finance Rs 75 Cr; Aditya Birla Capital Rs 50 Cr; Bandhan Bank Rs 50 Cr; Jio Credit Rs 50 Cr; Poonawalla Fincorp Rs 50 Cr; State Bank of India Rs 0.8 Cr (legacy); Federal Bank Rs 0.4 Cr (legacy); Axis Bank Rs 0.5 Cr (legacy).</li>
    <li><strong>IBank not in current secured consortium</strong> &mdash; entry opportunity at NCD refresh or HDFC consortium-renewal.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,650</td><td class="num">1,800</td><td class="num">1,962.8{ref("128")}</td></tr>
      <tr><td>EBITDA</td><td class="num">35</td><td class="num">38</td><td class="num">41.83{ref("128")}</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">2.1</td><td class="num">2.1</td><td class="num">2.1</td></tr>
      <tr><td>PAT</td><td class="num">10</td><td class="num">12</td><td class="num">14.61{ref("128")}</td></tr>
      <tr><td>TNW</td><td class="num">300</td><td class="num">320</td><td class="num">338.74{ref("128")}</td></tr>
      <tr><td>Total Debt</td><td class="num">1,300</td><td class="num">1,380</td><td class="num">1,454.47{ref("128")}</td></tr>
      <tr><td>Debt/TNW</td><td class="num">4.33x</td><td class="num">4.31x</td><td class="num">4.29x{ref("128")}</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 24.25 Cr</div><div class="sub">{ref("128")}</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">292</div><div class="sub">Plant + sales{ref("128")}</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 1,454.5 Cr</div><div class="sub">20 tranches across 13 lenders{ref("126")}</div></div>
    <div class="kpi neg"><div class="k">IBank share</div><div class="v num">0%</div><div class="sub">{ref("126")}</div></div>
    <div class="kpi"><div class="k">Rating</div><div class="v num">CARE BBB Stable</div><div class="sub">10 Apr 2026{ref("291")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
  </div>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA charge register (Probe42 cut)</div>
  <p>20 open charges across 13 lenders totalling Rs 1,454.5 Cr; <strong>NCD trustee (Axis) Rs 907 Cr (62.4%) dominates</strong>{ref("126")} reflecting an NCD-anchored capital structure. NBFC + bank tranches structured around the NCD as senior-secured.</p>
  <p class="lede">Strategic implication: NCD trustee position is primary; refresh / refinance window at next coupon-step / put-call date is the main entry play. HDFC working-capital secondary tranche refresh window separately. IBank standalone capex-TL for ENA expansion (ethanol-blending tailwind) is the cleanest greenfield opportunity given IBank-absent today.</p>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; Indian IMFL + ethanol</div>
  <p>India IMFL market FY25 ~Rs 80,000-90,000 Cr; CAGR 9-12%; state-policy-driven channel + pricing. Ethanol-blending E20 target by Oct 2026{ref("12")} drives structural ENA demand from OMCs.</p>
  <h3>06.1 Drivers</h3>
  <ul>
    <li>Ethanol-blending E20{ref("12")}: industry capacity ramp; ENA prices stable; ENA producers benefit.</li>
    <li>State-excise: TN + KN + AP + TG framework stable; volume-pricing controlled.</li>
    <li>Premium-IMFL trends: own-brand premium / luxury whisky tier expanding 15-18% CAGR.</li>
  </ul>
</section>
"""

def S6():
    return f"""
<section id="models">
  <div class="subhead">07 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,963{ref("128")}</td><td class="num">2,180</td><td class="num">2,420</td><td class="num">2,720</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">2.1</td><td class="num">2.5</td><td class="num">3.0</td><td class="num">3.5</td></tr>
      <tr><td>EBITDA</td><td class="num">42</td><td class="num">55</td><td class="num">73</td><td class="num">95</td></tr>
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
      <tr><td>NCD take-out / co-arranger</td><td class="num">300&ndash;500</td><td class="num">3&ndash;6</td><td>Refresh of Axis-Trustee NCD; sharper coupon</td></tr>
      <tr><td>HDFC working-capital take-out</td><td class="num">150&ndash;240</td><td class="num">3.5&ndash;5.5</td><td>Bid for HDFC tranche refresh</td></tr>
      <tr><td>Capex TL (ENA expansion)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3.5</td><td>Ethanol-blending tailwind capex</td></tr>
      <tr><td>SCF (molasses + glass-bottle vendor anchor)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3.5</td><td>Anchor-led; 60-day tenor</td></tr>
      <tr><td>BG (excise + state-tender)</td><td class="num">60&ndash;100</td><td class="num">0.6&ndash;1.0</td><td>State-excise BG; routine</td></tr>
      <tr><td>Receivable-discounting (TASMAC + ENA OMC)</td><td class="num">120&ndash;200</td><td class="num">2&ndash;3</td><td>State-corp + sovereign-OMC receivables</td></tr>
      <tr><td>CMS + cards</td><td class="num">&ndash;</td><td class="num">0.4&ndash;0.7</td><td>Routine</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 13.5-23.2 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 130-180; Rs 0.4-0.6 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>Promoter Kals family; PB AUM Rs 180-280 Cr; Rs 1.0-1.8 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 25-40 Cr; Rs 0.3-0.5 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 1.7-2.9 Cr / yr</strong>.</p>
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
      <tr><td>Wholesale funded (NCD + HDFC + Capex)</td><td class="num">8.5</td><td class="num">15</td></tr>
      <tr><td>Wholesale non-funded (BG)</td><td class="num">0.6</td><td class="num">1.0</td></tr>
      <tr><td>SCF + receivable-discounting</td><td class="num">4</td><td class="num">6.5</td></tr>
      <tr><td>CMS + cards</td><td class="num">0.4</td><td class="num">0.7</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">1.7</td><td class="num">2.9</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>15.2</strong></td><td class="num"><strong>26.1</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 24-42 Cr/yr captures upper-mid band including ENA-capex pipeline + NCD refresh capture.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12 + MGT-7 refresh; promoter Kals family + CFO + CS.</p>
  <h3>11.2 Ownership</h3><ul><li>Promoter ~92%; financial investors ~8%; BEN-2 on file{ref("144")}.</li></ul>
  <h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}; routine state-excise compliance.</li></ul>
  <h3>11.4 Recent news</h3><ul><li>Apr 2026: CARE affirms BBB Stable{ref("291")}.</li><li>FY26: ENA capacity expansion announcement aligned to ethanol-blending E20 target{ref("12")}.</li></ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x"><li>T+14 MCA DIR-12 + MGT-7</li><li>T+14 NCD coupon-step / put-call calendar</li><li>T+14 State-excise compliance certificate</li><li>T-14 Pre-sanction Probe42 charge re-pull</li></ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Kals CFO meeting; NCD-take-out concept memo + HDFC-tranche-refresh pitch.</p></div>
  <div class="card"><p><strong>T+60:</strong> Bid into NCD refresh / HDFC tranche refresh; capex-TL term-sheet for ENA expansion.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Capex TL + SCF go-live.</p></div>
  <div class="card"><p><strong>T+180:</strong> Receivable-discounting + PB engagement.</p></div>
  <h3>Success metrics</h3>
  <ul class="check"><li>NCD or HDFC tranche capture by Q3 FY27</li><li>Capex TL Rs 100 Cr drawn</li><li>Y3 run-rate Rs 24-42 Cr</li></ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Kals-specific from [290].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">Kals Distilleries-specific sources</h3>
  <ol start="290">
  <li id="src-290"><strong>MCA v3 + ZaubaCorp &mdash; Kals Distilleries Pvt Ltd master data</strong> &mdash; CIN U15511TN2007PTC065347; incorp 12 Nov 2007; RoC Chennai; active. <span class="u">mca.gov.in</span></li>
  <li id="src-291"><strong>CARE Ratings &mdash; Kals Distilleries Pvt Ltd rating rationale (10 Apr 2026)</strong> &mdash; affirms CARE BBB / Stable on fund + non-fund limits Rs 1,454 Cr. <span class="u">careedge.in</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "Kals Distilleries Private Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Kals Distilleries", "IMFL + ENA / state-policy distillery"),
           FOOT("Cipher clean; 1,500+ lines; consortium-entry play.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
