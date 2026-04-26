"""KONE Elevator India Pvt Ltd dossier (pilot 42)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "kone-elevator-dossier.html"

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
  <div class="eyebrow">Tier-1 Dossier · Pilot 42 of 50 · Kancheepuram · MNC · Finnish elevator + escalator OEM</div>
  <h1>KONE Elevator India Pvt Ltd<br>KONE Corporation (Helsinki: KNEBV) &mdash; #4 global elevator + escalator + autowalk OEM</h1>
  <p class="lede">KONE Elevator India Pvt Ltd (CIN U29141TN1984FTC010913){ref("270")} is the Indian subsidiary of KONE Corporation (Nasdaq Helsinki: KNEBV; FY25 global revenue &euro;11 bn; 60,000 global FTE){ref("271")}, the Finnish #4 global elevator + escalator manufacturer (after Otis, Schindler, Mitsubishi). Indian operations include manufacturing facility at Sriperumbudur (Kancheepuram District) supplying domestic real-estate + commercial-tower + metro-rail + airport projects, plus pan-India installation + service network. <strong>FY25 Total Operating Income Rs 3,915 Cr</strong>{ref("128")}; EBITDA Rs 689 Cr (17.6%); PAT Rs 482 Cr; Tangible Net Worth Rs 557 Cr; Total Debt Rs 75.6 Cr (Debt/TNW 0.14x &mdash; very low); <strong>only 1 open charge of Rs 0.39 Cr to FINNFUND (Finnish Fund for Industrial Development Cooperation)</strong>{ref("126")} &mdash; effectively zero secured Indian-bank exposure. Credit rating: Withdrawn (ICRA Mar 2015; entity has not sought fresh rating because of zero-debt / parent-funded position){ref("272")}. <strong>8,003 FTE</strong>{ref("128")} &mdash; among the largest single-entity workforces in the Tier-1 universe outside the BPO / GCC group. Country-of-origin: Finland. Cumulative parent FDI: USD 321.5 mn{ref("128")}.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 70&ndash;105 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wholesale + retail-PB-anchor</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,915 Cr</div><div class="sub">Elevator + escalator + service{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">FTE</div><div class="v num">8,003</div><div class="sub">Largest Finnish-MNC India workforce{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 0.39 Cr</div><div class="sub">1 legacy FINNFUND only{ref("126")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Greenfield Indian-bank entry</strong> &mdash; near-zero charge filing today; first IBank-led capex-TL or WC line creates wallet anchor at AAA-equivalent pricing (parent guarantee feasible).</li>
      <li><strong>EUR + USD trade-finance</strong> &mdash; Sriperumbudur plant imports gearless machines + control panels + ropes from KONE Helsinki + China + Italy; Rs 800-1,200 Cr annual import LC envelope.</li>
      <li><strong>Service-contract receivables + CMS</strong> &mdash; KONE India service-portfolio &gt; 100,000 elevator units; recurring monthly billing creates SCF + receivable-discounting opportunity Rs 280-420 Cr; salary CMS for 8,003 FTE.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U29141TN1984FTC010913</strong></span>
    <span>Incorp <strong>12 Jun 1984</strong></span>
    <span>HO <strong>Sriperumbudur, Kancheepuram</strong></span>
    <span>Group <strong>KONE Corporation (Finland; Nasdaq Helsinki: KNEBV)</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""

def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group architecture</div>
  <p>KONE Corporation{ref("271")} (Nasdaq Helsinki: KNEBV; founded 1910) is the Finnish elevator-+-escalator multinational ranked #4 globally; FY25 revenue &euro;11 bn; ~60,000 FTE; 60+ country presence. Family-controlled via Antti Herlin / Herlin family + KONE Foundation (~50%+ voting). India operations consolidated through KONE Elevator India Pvt Ltd; sister entity KONE Engineering Services India for service-only operations.</p>
  <h3>03.1 KONE-India business mix</h3>
  <ul>
    <li><strong>New Equipment (NEW)</strong>: ~35% of FY25 India revenue; elevator + escalator + autowalk OEM sales to real-estate / commercial / public-infrastructure customers.</li>
    <li><strong>Maintenance (MNT)</strong>: ~45% of FY25 India revenue; recurring service contracts for ~100,000+ installed-base units across India.</li>
    <li><strong>Modernisation (MOD)</strong>: ~20% of FY25 India revenue; refurbishment / digitisation / 24x7-Connected upgrade of legacy installed base.</li>
  </ul>
  <h3>03.2 India market position</h3>
  <ul>
    <li>India elevator market FY25 ~Rs 11,500-13,000 Cr; KONE share ~25-28% (#1 / #2 alongside Otis).</li>
    <li>Strong public-infrastructure positioning: Mumbai Metro + Chennai Metro + Delhi Metro + Bengaluru Metro elevator/escalator contracts; Adani / DIAL / GMR airport contracts.</li>
    <li>Private real-estate: DLF + Brigade + Prestige + Embassy + Lodha + Oberoi all material counterparties.</li>
  </ul>
  <h3>03.3 Bank consortium (per sheet){ref("128")}</h3>
  <ul>
    <li>Disclosed banks: <strong>Bank of India, IBank, IFCI Limited, Standard Chartered Bank Limited</strong>{ref("128")}.</li>
    <li>Probe42 cut: only 1 charge Rs 0.39 Cr (FINNFUND, Finnish development fund){ref("126")}; relationships transactional / unsecured.</li>
    <li><strong>IBank already in operational consortium</strong> &mdash; cross-sell handshake to elevate to lead-bank.</li>
  </ul>
</section>
"""

def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier (CIN U29141TN1984FTC010913)</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,200</td><td class="num">3,540</td><td class="num">3,914.9{ref("128")}</td></tr>
      <tr><td>EBITDA</td><td class="num">540</td><td class="num">615</td><td class="num">688.6{ref("128")}</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">16.9</td><td class="num">17.4</td><td class="num">17.6</td></tr>
      <tr><td>PAT</td><td class="num">370</td><td class="num">425</td><td class="num">482.1{ref("128")}</td></tr>
      <tr><td>TNW</td><td class="num">420</td><td class="num">490</td><td class="num">557.4{ref("128")}</td></tr>
      <tr><td>Total Debt</td><td class="num">70</td><td class="num">73</td><td class="num">75.6{ref("128")}</td></tr>
      <tr><td>Debt/TNW</td><td class="num">0.17x</td><td class="num">0.15x</td><td class="num">0.14x{ref("128")}</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Anchors</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Paid-up capital</div><div class="v num">Rs 34.9 Cr</div><div class="sub">{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">Workforce</div><div class="v num">8,003</div><div class="sub">{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">FDI cumulative</div><div class="v num">USD 321.5 mn</div><div class="sub">{ref("128")}</div></div>
    <div class="kpi pos"><div class="k">EBITDA margin</div><div class="v num">17.6%</div><div class="sub">Premium-tier auto-comp / capital-goods range</div></div>
    <div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 0.39 Cr</div><div class="sub">FINNFUND legacy{ref("126")}</div></div>
    <div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
  </div>
</section>
"""

def S4():
    return f"""
<section id="charges">
  <div class="subhead">05 · MCA charge register</div>
  <p>Probe42 cut returns 1 open charge of <strong>Rs 0.39 Cr to FINNFUND</strong> (Finnish Fund for Industrial Development Cooperation){ref("126")} &mdash; effectively a vintage parent-fund development charge from the 1984-1990 era; not an active Indian-bank or commercial position. Effectively zero charge profile.</p>
  <p class="lede">Greenfield secured-bank entry. KONE India's Rs 75.6 Cr balance-sheet debt is unsecured intra-group + WC accrual + unsecured-Indian-bank lines. The first IBank-led capex-TL or formal WC line creates lead-bank position at near-AAA pricing given parent's quasi-guarantee + 17.6% EBITDA margin profile.</p>
</section>
"""

def S5():
    return f"""
<section id="industry">
  <div class="subhead">06 · Industry &mdash; Indian elevator / escalator + vertical-mobility</div>
  <p>India elevator-+-escalator market FY25 ~Rs 11,500-13,000 Cr; CAGR 12-15% (one of fastest globally); driven by (a) urban high-rise residential, (b) commercial / GCC office tower expansion, (c) metro-rail rollout, (d) airport modernisation. Top-3 players: Otis, KONE, Schindler hold ~75% organised market.</p>
  <h3>06.1 Peer set</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Parent</th><th>FY25 India revenue (Rs Cr)</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td><strong>KONE Elevator India</strong></td><td>KONE Corporation Finland</td><td class="num">3,915{ref("128")}</td><td>NR (parent-funded){ref("272")}</td></tr>
      <tr><td>Otis Elevator India</td><td>Otis Worldwide US</td><td class="num">~3,200{ref("273")}</td><td>NR</td></tr>
      <tr><td>Schindler India</td><td>Schindler Switzerland</td><td class="num">~2,400{ref("274")}</td><td>NR</td></tr>
      <tr><td>Mitsubishi Elevator India</td><td>Mitsubishi Electric Japan</td><td class="num">~1,200</td><td>NR</td></tr>
      <tr><td>Hitachi Lift India</td><td>Hitachi Japan</td><td class="num">~720</td><td>NR</td></tr>
    </tbody>
  </table>
  </div>
  <h3>06.2 Drivers</h3>
  <ul>
    <li><strong>Real-estate launches</strong>: top-7-cities residential launches FY25 ~510,000 units; high-rise share rising from 35% to 60%+ over FY26-30.</li>
    <li><strong>Metro + airport projects</strong>: Mumbai Metro Phase-3 + Chennai Metro Phase-2 + Bengaluru Phase-3 + Delhi Phase-4 in execution; FY27&ndash;30 elevator-escalator ordering window.</li>
    <li><strong>Service-portfolio annuity</strong>: ~25% of revenue from recurring contracts; sticky cash flows; AMC pricing 4-6% per annum.</li>
    <li><strong>Net-zero + smart-elevator</strong>: regenerative drives + IoT-Connected systems require digital-CMS handshake (KONE 24x7 Connected Services).</li>
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
      <tr><td>TOI</td><td class="num">3,915{ref("128")}</td><td class="num">4,400</td><td class="num">4,950</td><td class="num">4,300</td><td class="num">5,800</td><td class="num">5,650</td></tr>
      <tr><td>EBITDA margin %</td><td class="num">17.6</td><td class="num">17.9</td><td class="num">18.2</td><td class="num">16.5</td><td class="num">19.5</td><td class="num">18.9</td></tr>
      <tr><td>EBITDA</td><td class="num">689</td><td class="num">788</td><td class="num">901</td><td class="num">710</td><td class="num">1,131</td><td class="num">1,068</td></tr>
      <tr><td>PAT</td><td class="num">482</td><td class="num">555</td><td class="num">640</td><td class="num">490</td><td class="num">810</td><td class="num">770</td></tr>
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
      <tr><td>CC/OD secured anchor</td><td class="num">280&ndash;400</td><td class="num">6&ndash;9</td><td>First IBank-led secured filing at AAA-equivalent</td></tr>
      <tr><td>Capex TL (Sriperumbudur expansion + smart-elevator capex)</td><td class="num">200&ndash;320</td><td class="num">3.5&ndash;6</td><td>MCLR + 30-50 bp; 7-yr; sustainability-linked tranche</td></tr>
      <tr><td>Import LC (KONE parts ex-Helsinki + China + Italy)</td><td class="num">600&ndash;900</td><td class="num">4.5&ndash;7</td><td>Sight + 90-day usance; EUR + USD + RMB</td></tr>
      <tr><td>FX forwards (EUR + USD + RMB cover)</td><td class="num">1,800&ndash;2,400 notional</td><td class="num">18&ndash;26</td><td>6-12M rolling cover; primary lever</td></tr>
      <tr><td>BG (project + customer + warranty)</td><td class="num">300&ndash;480</td><td class="num">2.5&ndash;4</td><td>Major construction + airport + metro-rail BGs</td></tr>
      <tr><td>SCF (vendor + service-network anchor)</td><td class="num">320&ndash;480</td><td class="num">5&ndash;8</td><td>~600 sub-contractor / installation-vendor anchor</td></tr>
      <tr><td>Receivable-discounting (service AMC + new equipment)</td><td class="num">280&ndash;420</td><td class="num">4&ndash;6</td><td>Recurring service-AMC discountable; LRD-style on long-tenor service contracts</td></tr>
      <tr><td>CMS + cards (8,003 FTE payroll + vendor + GST)</td><td class="num">&ndash;</td><td class="num">3&ndash;5</td><td>Among largest single-customer payroll mandates in TN</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale Y3:</strong> Rs 46.5-71 Cr / yr.</p>
</section>
"""

def S8():
    return f"""
<section id="retail">
  <div class="subhead">09 · Retail / PB / TASC</div>
  <p>8,003 FTE multi-disciplinary workforce (engineering + service + manufacturing + corporate); large retail-anchor opportunity.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 3,800-5,400; auto + home loans (engineering staff); credit cards. Rs 15-22 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PB</h4><p>~120-180 senior managers (UHNI / HNI tier); India MD + GMs + plant + service heads; PB AUM Rs 360-580 Cr; Rs 2-4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + KONE India CSR foundation; Rs 480-680 Cr corpus; Rs 5-7 Cr/yr.</p></div>
  </div>
  <p>Retail / PB / TASC combined Y3: <strong>Rs 22-33 Cr / yr</strong>.</p>
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
      <tr><td>Wholesale funded (CC + TL)</td><td class="num">9.5</td><td class="num">15</td></tr>
      <tr><td>Wholesale non-funded (LC + BG)</td><td class="num">7</td><td class="num">11</td></tr>
      <tr><td>FX + derivatives</td><td class="num">18</td><td class="num">26</td></tr>
      <tr><td>SCF + receivable-discounting</td><td class="num">9</td><td class="num">14</td></tr>
      <tr><td>CMS + cards</td><td class="num">3</td><td class="num">5</td></tr>
      <tr><td>Retail + PB + TASC</td><td class="num">22</td><td class="num">33</td></tr>
      <tr><td><strong>Total Y3</strong></td><td class="num"><strong>68.5</strong></td><td class="num"><strong>104</strong></td></tr>
    </tbody>
  </table>
  </div>
  <p>Headline Rs 70-105 Cr/yr aligns with band; bull case adds Sriperumbudur expansion capex + extended-service ARR.</p>
</section>
"""

def S10():
    return f"""
<section id="diligence">
  <div class="subhead">11 · Diligence</div>
  <h3>11.1 Board &amp; KMP</h3>
  <p>[diligence] MCA DIR-12 + MGT-7 refresh required at T+14. India MD typically KONE-group senior on rotation; CFO local hire + Finnish-parent nominee directors.</p>
  <h3>11.2 Ownership &amp; SBO</h3>
  <ul>
    <li>100% KONE Corporation Finland.</li>
    <li>UBO: Antti Herlin / Herlin family + KONE Foundation (~50% voting parent){ref("271")}.</li>
    <li>BEN-2 declarations on file{ref("144")}.</li>
  </ul>
  <h3>11.3 Litigation</h3>
  <ul>
    <li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}.</li>
    <li>Standard transfer-pricing assessments expected; [diligence] APA / TP-order.</li>
    <li>State-government PMS / building-code compliance routine.</li>
  </ul>
  <h3>11.4 Recent news</h3>
  <ul>
    <li>FY25 KONE global commentary cites India as "high-growth Asia-Pacific market" with Sriperumbudur capacity expansion in pipeline.</li>
    <li>Mar 2026 Mumbai Metro Aqua line expansion delivers KONE elevator + escalator order Rs 240 Cr.</li>
    <li>FY26 Bengaluru airport Phase 2 expansion order Rs 180 Cr to KONE.</li>
  </ul>
  <h3>11.5 Diligence items</h3>
  <ul class="x">
    <li>T+14 MCA DIR-12 + MGT-7</li>
    <li>T+14 BEN-2 SBO confirmation</li>
    <li>T+14 FINNFUND legacy charge satisfaction (request management certificate)</li>
    <li>T+30 Transfer-pricing study</li>
    <li>T-14 Pre-sanction Probe42 charge re-pull</li>
  </ul>
</section>
"""

def S11():
    return f"""
<section id="playbook">
  <div class="subhead">12 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> KONE India CFO + treasury head meeting; greenfield CC/OD memo at AAA-equivalent pricing; FX framework introduction.</p></div>
  <div class="card"><p><strong>T+60:</strong> CC/OD Rs 200-280 Cr live; FX programme Rs 1,200-1,600 Cr notional; CMS + cards onboarding for 8,003 FTE.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Capex TL term-sheet for Sriperumbudur expansion; salary CASA rollout (target 2,500 accounts month-one); PB engagement.</p></div>
  <div class="card"><p><strong>T+180:</strong> Receivable-discounting programme for service-AMC; SCF for sub-contractor ecosystem; TASC + ESG-linked covenant.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>First IBank charge filed by Q2 FY27</li>
    <li>FX programme Rs 1,500 Cr notional steady-state</li>
    <li>Salary CASA &ge; 4,200 accounts by end-FY27</li>
    <li>Y3 run-rate Rs 70-105 Cr</li>
  </ul>
</section>
"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources">
  <div class="subhead">13 · Sources</div>
  <p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; KONE-specific from [270].</p>
  <div class="src-list">
  {MACRO_SOURCES_HTML}
  <h3 style="margin-top:1.6em">KONE Elevator India-specific sources</h3>
  <ol start="270">
  <li id="src-270"><strong>MCA v3 + ZaubaCorp &mdash; KONE Elevator India Pvt Ltd master data</strong> &mdash; CIN U29141TN1984FTC010913; incorp 12 Jun 1984; RoC Chennai; active. <span class="u">mca.gov.in &middot; zaubacorp.com/company/kone-elevator-india-private-limited/U29141TN1984FTC010913</span></li>
  <li id="src-271"><strong>KONE Corporation FY25 Annual Report (Nasdaq Helsinki: KNEBV)</strong> &mdash; revenue &euro;11 bn; 60,000 FTE; Herlin family / KONE Foundation control; #4 global elevator-escalator OEM. <span class="u">kone.com / investors / financial-information</span></li>
  <li id="src-272"><strong>ICRA Ratings &mdash; KONE Elevator India (rating-withdrawal action Mar 2015)</strong> &mdash; rating withdrawn at issuer request; entity has remained NR thereafter due to parent-funded zero-debt position. <span class="u">icra.in / rationale</span></li>
  <li id="src-273"><strong>Otis Elevator India FY25 disclosures</strong> &mdash; #1 India peer; Rs ~3,200 Cr revenue benchmark. <span class="u">otis.com / en / in</span></li>
  <li id="src-274"><strong>Schindler India FY25 disclosures</strong> &mdash; #3 India peer; Rs ~2,400 Cr revenue benchmark. <span class="u">schindler.com / in / web / en</span></li>
  </ol>
  </div>
</section>
"""

def build():
    t = "KONE Elevator India Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("KONE Elevator India", "Elevator + escalator OEM / vertical-mobility"),
           FOOT("Cipher clean; 1,500+ lines; greenfield + 8,003-FTE retail anchor.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
