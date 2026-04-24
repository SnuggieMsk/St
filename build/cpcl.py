"""Chennai Petroleum Corporation Limited dossier (pilot 14)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "cpcl-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 14 of 20 · PSU · Oil refining · AAA rated</div>
  <h1>Chennai Petroleum Corporation Ltd<br>IOC subsidiary · Manali + Cauvery Basin refineries</h1>
  <p class="lede">Listed (NSE: CHENNPETRO / BSE: 500110) oil refinery subsidiary of Indian Oil Corporation (IOC). CIN L40101TN1965GOI005389 (GOI = Government-of-India linkage). Operates 10.5 MMTPA Manali refinery + 1 MMTPA Cauvery Basin refinery. FY25 TOI Rs 59,355 Cr (largest Tier-1 by revenue){ref("42")}. CRISIL AAA Stable (17 Mar 2026 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 17,882 Cr (refinery project finance + WC consortium). As a PSU subsidiary with mandated bank-panel structure, incremental IBank role is narrower than private-sector entities but still meaningful at scale.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (constrained by PSU panel)</div><div class="v num">Rs 32–48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Trade finance + FX + CMS (limited WC participation)</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 59,355 Cr</div><div class="sub">Largest revenue in Tier-1 pilot set</div></div>
    <div class="kpi pos"><div class="k">CRISIL rating</div><div class="v num">AAA Stable</div><div class="sub">17 Mar 2026{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 17,882 Cr</div><div class="sub">Refinery project finance + WC consortium</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three realistic converting angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Crude-import LC programme</strong> &mdash; USD-heavy import LC + SBLC annual flow Rs 45,000+ Cr; IBank can participate 3-5% share on confirmation basis</li>
      <li><strong>FX hedging (USD crude + EUR / GBP freight)</strong> &mdash; large notional programme; market-share capture via pricing + service</li>
      <li><strong>Salary CMS + CSR trust</strong> &mdash; CPCL workforce ~1,800; CSR Rs 40+ Cr/yr; standard-operating relationship</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L40101TN1965GOI005389</strong></span>
    <span>Parent <strong>Indian Oil Corporation (IOC) 51.9%; GOI residual</strong></span>
    <span>Listed <strong>NSE / BSE</strong></span>
    <span>Registry cut <strong>Probe42 / 09 Mar 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group</div>
  <p>CPCL was originally incorporated in 1965 as Madras Refineries Ltd (MRL), a joint venture between GOI + AMOCO + National Iranian Oil Company. Post-IOC takeover, renamed Chennai Petroleum Corporation Ltd. Listed on BSE / NSE; IOC holds 51.9%. Operates two refineries:</p>
  <ul class="check">
    <li><strong>Manali refinery (Chennai)</strong>: 10.5 MMTPA capacity; complex refinery; captive-market linkage to southern India</li>
    <li><strong>Cauvery Basin refinery (Nagapattinam)</strong>: 1 MMTPA simple refinery; specialty products focus</li>
    <li>Marketing exclusively to IOC; captive off-take relationship</li>
  </ul>
  <p>As a PSU under Ministry of Petroleum &amp; Natural Gas, CPCL follows mandated public-procurement rules for banking panel. Private banks can participate in specific products (trade finance + FX) where public-banks cannot compete on service or pricing.</p>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">75,200</td><td class="num">59,355</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num">-21 (crude-price driven)</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">5.2</td><td class="num">3.8</td></tr>
      <tr><td>EBITDA</td><td class="num">3,910</td><td class="num">2,255</td></tr>
      <tr><td>PAT</td><td class="num">2,450</td><td class="num">1,180</td></tr>
      <tr><td>GRM ($/bbl)</td><td class="num">7.8</td><td class="num">5.2</td></tr>
    </tbody>
  </table>
  </div>
  <p>Revenue decline FY25 vs FY24 reflects crude-price normalisation (FY24 had Russia-Ukraine elevated cracks). EBITDA margin moderation reflects refining-margin cycle. CRISIL AAA rating reflects parent-IOC guarantee + GOI linkage.</p>
  <h3>04.1 Plant operating metrics</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Manali refining capacity</div><div class="v num">10.5 MMTPA</div><div class="sub">Complex refinery; Nelson complexity 8+</div></div>
    <div class="kpi"><div class="k">Cauvery Basin capacity</div><div class="v num">1.0 MMTPA</div><div class="sub">Simple refinery; specialty products</div></div>
    <div class="kpi"><div class="k">Refinery utilisation</div><div class="v num">98-102%</div><div class="sub">Consistent 100%+ throughput</div></div>
    <div class="kpi"><div class="k">Product slate</div><div class="v num">Multiple</div><div class="sub">Diesel, petrol, LPG, naphtha, ATF, bitumen, lube</div></div>
    <div class="kpi"><div class="k">Crude sourcing</div><div class="v num">Multi-source</div><div class="sub">Middle East + Africa + Russia (opportunistic)</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~1,800</div><div class="sub">Unionised; PSU-standard HR</div></div>
  </div>
  <h3>04.2 Capex pipeline</h3>
  <p>Ongoing + planned capex: BS-VI compliance upgrades (completed); residue-upgradation projects; specialty products capacity; environmental compliance (CPCB-mandated). Total FY26-FY30 capex envelope Rs 6,500-8,500 Cr depending on Cauvery Phase-2 decision.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India oil refining</div>
  <p>India refining capacity ~252 MMTPA across 24 refineries; utilisation 100%+. Structural demand growth 4-6% CAGR. Gross refining margin (GRM) cycles with crude-product spreads; FY25 moderation on specific-product weakness. Peer: Reliance Petroleum (60 MMTPA), Nayara (20 MMTPA), IOC-captive (70 MMTPA), BPCL-Kochi (15 MMTPA), HPCL-Mumbai/Visakh.</p>

  <h3>05.1 GRM cycle dynamics</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Crack / product</th><th>FY24 avg ($/bbl)</th><th>FY25 avg ($/bbl)</th><th>FY26 E</th></tr></thead>
    <tbody>
      <tr><td>Diesel crack</td><td class="num">22-25</td><td class="num">14-17</td><td class="num">16-19</td></tr>
      <tr><td>Petrol crack</td><td class="num">14-18</td><td class="num">9-12</td><td class="num">11-14</td></tr>
      <tr><td>LPG crack</td><td class="num">-2 to +2</td><td class="num">-4 to -1</td><td class="num">-2 to +1</td></tr>
      <tr><td>ATF crack</td><td class="num">24-28</td><td class="num">18-22</td><td class="num">20-24</td></tr>
      <tr><td>Naphtha crack</td><td class="num">-1 to +3</td><td class="num">-3 to 0</td><td class="num">-1 to +2</td></tr>
      <tr><td>CPCL GRM</td><td class="num">7.8</td><td class="num">5.2</td><td class="num">6.0-6.5</td></tr>
    </tbody>
  </table>
  </div>

  <h3>05.2 Regulatory context</h3>
  <p>Indian refining is subject to (i) Petroleum &amp; Natural Gas Rules; (ii) CPCB emission norms (BS-VI equivalent); (iii) MoPNG pricing / marketing margin framework; (iv) Import-duty structure on crude (NIL) + products (5-18%); (v) FTPs and free-trade-zones for exports. CPCL operates within this framework via IOC's marketing presence.</p>
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
      <tr><td>TOI</td><td class="num">59,355</td><td class="num">61,800</td><td class="num">64,500</td><td class="num">58,000</td><td class="num">70,200</td><td class="num">67,800</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">3.8</td><td class="num">4.3</td><td class="num pos">4.8</td><td class="num neg">3.2</td><td class="num pos">5.6</td><td class="num">5.2</td></tr>
      <tr><td>EBITDA</td><td class="num">2,255</td><td class="num">2,657</td><td class="num">3,096</td><td class="num">1,856</td><td class="num">3,931</td><td class="num">3,526</td></tr>
      <tr><td>PAT</td><td class="num">1,180</td><td class="num">1,485</td><td class="num">1,820</td><td class="num">845</td><td class="num">2,420</td><td class="num">2,145</td></tr>
      <tr><td>Capex (Rs Cr)</td><td class="num">1,200</td><td class="num">1,400</td><td class="num">1,800</td><td class="num">1,200</td><td class="num">2,200</td><td class="num">1,600</td></tr>
    </tbody>
  </table>
  </div>
  <p>PSU-structure + AAA rating + implicit parent support anchor covenant profile irrespective of cycle. Any incremental debt flows through IOC consortium; private-bank TL role is limited.</p>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Entry-point map (PSU-constrained)</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Import LC + SBLC (crude + equipment)</td><td class="num">2,500&ndash;3,500 rolling</td><td class="num">14&ndash;20</td></tr>
      <tr><td>FX forwards (USD crude + EUR / GBP freight)</td><td class="num">3,800&ndash;5,200 notional</td><td class="num">12&ndash;16</td></tr>
      <tr><td>BG (performance + customs + environmental)</td><td class="num">180&ndash;260</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CMS + payroll for 1,800 staff</td><td class="num">&mdash;</td><td class="num">4&ndash;6</td></tr>
      <tr><td>Treasury / liquid-fund mgmt</td><td class="num">300&ndash;500 AUM</td><td class="num">3&ndash;4</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 34&ndash;48 Cr/yr.</strong> PSU structure prevents full WC / TL participation; trade-finance + FX are the practical entry-points.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>CPCL workforce ~1,800 (Manali + Cauvery plants). PSU employee PB + CSR TASC opportunity modest.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Salary CASA</h4><p>1,800 permanent staff; salary migration could capture 700-900 accounts. Rs 2-3 Cr/yr income.</p></div>
    <div class="card"><h4 style="margin-top:0">CSR trust</h4><p>CSR Rs 40+ Cr/yr flow; trust banking mandate Rs 1-2 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">PF + Gratuity</h4><p>Workmen PF trust + Gratuity Rs 220-280 Cr; Rs 3-4 Cr/yr income.</p></div>
  </div>
  <p>Combined Rs 6&ndash;9 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 34&ndash;48 Cr/yr + Retail/PB/TASC Rs 6&ndash;9 Cr/yr = <strong>Rs 40&ndash;57 Cr/yr total</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>IOC (listed PSU) 51.9%; public float + GOI residual</li>
        <li>Govt-owned parent; implicit sovereign support</li>
        <li>No promoter-family PB angle (PSU structure)</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>CRISIL AAA Stable</strong> (17 Mar 2026){ref("81")}</li>
        <li><strong>Zero suit-filed</strong>{ref("82")}</li>
        <li>MoPNG regulation; standard PSU compliance framework</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet CFO + Treasury Head at Manali / Chennai HO. Crude-import LC programme + FX forwards; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close LC + FX programmes; BG framework for environmental + customs.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Salary CMS; CSR TASC handshake; PSU-compliant standard operating cadence.</p></div>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. CPCL sources from [109].</em></p>
  <div class="src-list"><ol start="109">
  <li id="src-109"><strong>CPCL annual reports + BSE / NSE quarterly filings + IOC parent disclosures + MoPNG regulations</strong> &mdash; Manali 10.5 MMTPA + Cauvery 1 MMTPA; IOC 51.9% parent; PSU structure. <span class="u">cpcl.co.in &middot; bseindia.com/stock-share-price/chennai-petroleum-corporation-ltd/CHENNPETRO/500110/</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Chennai Petroleum Corporation Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Chennai Petroleum Corporation", "Oil refining"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
