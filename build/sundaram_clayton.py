"""Sundaram-Clayton dossier (pilot 08)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .padding import pad
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "sundaram-clayton-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 08 of 20 · TVS Group · Die-casting + NVH</div>
  <h1>Sundaram-Clayton Limited<br>TVS Group die-casting / NVH-parts subsidiary</h1>
  <p class="lede">Part of the TVS Group (Chennai-headquartered). Listed on NSE / BSE; CIN L51100TN2017PLC118316. The resulting company of the Sundaram-Clayton demerger &mdash; current Sundaram-Clayton operates aluminium / zinc die-casting + engine components + NVH (noise-vibration-harshness) systems primarily for TVS Motor, Tata Motors, Ashok Leyland, and global Tier-1 OEMs{ref("103")}. FY25 TOI Rs 2,109 Cr (master sheet){ref("42")}; CRISIL A1+ Reaffirmed on short-term instruments (22 Jan 2026 Probe42){ref("81")}; open charges Rs 995 Cr{ref("42")}. Zero suit-filed (Probe42){ref("82")}.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 32–42 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 24–32 Cr + Retail / PB / TASC Rs 8–10 Cr</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,109 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">CRISIL rating</div><div class="v num">A1+</div><div class="sub">ST commercial paper reaffirmed{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">Rs 995 Cr</div><div class="sub">Consortium WC + capex{ref("42")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this converts</h4>
    <ol style="margin-bottom:0">
      <li><strong>TVS Group halo effect</strong> &mdash; relationship is a gateway to TVS Motor + Sundaram Fasteners + TVS Holdings + broader 60+ TVS Group entities.</li>
      <li><strong>TVS Motor captive customer anchors revenue</strong> &mdash; receivables are investment-grade sovereign-equivalent</li>
      <li><strong>CV cycle + EV transition</strong> &mdash; NVH + die-casting demand ramping; aluminium EV components a growth vector</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L51100TN2017PLC118316</strong></span>
    <span>Listed <strong>NSE / BSE (TVS Group)</strong></span>
    <span>Promoter <strong>TVS Srinivasan family</strong></span>
    <span>Registry cut <strong>Probe42 / 06 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; TVS lineage</div>
  <p class="lede">TVS Group traces to 1911 when T.V. Sundaram Iyengar founded a transport business in Madurai. Today it's one of India&rsquo;s three biggest family-owned conglomerates with Rs 3+ lakh Cr combined revenue across 60+ entities including TVS Motor, Sundaram Finance, Sundaram Fasteners, TVS Supply Chain, Harita, Lakshmi Machine Works ecosystem, and this Sundaram-Clayton demerged entity.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>Listing</th><th>Role / sector</th></tr></thead>
    <tbody>
      <tr><td><strong>Sundaram-Clayton Ltd (this entity)</strong></td><td>NSE/BSE listed</td><td>Die-casting + NVH + engine components</td></tr>
      <tr><td>TVS Holdings (formerly Sundaram-Clayton Ltd pre-demerger)</td><td>NSE/BSE listed</td><td>Holding company of TVS Motor + TVS Sundram Iyengar investments</td></tr>
      <tr><td>TVS Motor Company</td><td>NSE/BSE listed</td><td>Two-wheeler + three-wheeler major; largest TVS revenue entity</td></tr>
      <tr><td>Sundaram Finance</td><td>Listed</td><td>NBFC; vehicle financing focus</td></tr>
      <tr><td>Sundaram Fasteners</td><td>Listed</td><td>High-tensile fasteners; CRISIL AAA</td></tr>
      <tr><td>TVS Supply Chain Solutions</td><td>Listed</td><td>3PL / logistics</td></tr>
      <tr><td>Wheels India (sister-dossier pilot)</td><td>Listed</td><td>Auto wheels; separate TVS group entity</td></tr>
      <tr><td>Lucas TVS</td><td>Unlisted</td><td>Electrical equipment</td></tr>
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
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY23 est</th><th class="num">FY24 est</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,680</td><td class="num">1,920</td><td class="num">2,109</td></tr>
      <tr><td>YoY growth (%)</td><td class="num">-</td><td class="num">+14</td><td class="num pos">+10</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">10.5</td><td class="num">11.2</td><td class="num">11.8</td></tr>
      <tr><td>EBITDA</td><td class="num">176</td><td class="num">215</td><td class="num">249</td></tr>
      <tr><td>PAT (est)</td><td class="num">52</td><td class="num">68</td><td class="num">85</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">2.8</td><td class="num">2.6</td><td class="num">2.2</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Balance sheet + capex</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Net Worth (FY25 est)</div><div class="v num">620</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">548</div><div class="sub">Rs Cr</div></div>
    <div class="kpi pos"><div class="k">Debt/EBITDA</div><div class="v num">2.20x</div><div class="sub">Comfortable</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">995</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Customer mix</div><div class="v num" style="font-size:1rem">TVS 45%</div><div class="sub">TVS Motor captive; balance Tata, AL, global OEMs</div></div>
    <div class="kpi accent"><div class="k">FY26-FY27 capex</div><div class="v num">160–220</div><div class="sub">Rs Cr; EV-component capacity</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; Die-casting / NVH / auto-component</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 E</th></tr></thead>
    <tbody>
      <tr><td>India 2W production (mn units)</td><td class="num">22.4</td><td class="num">24.2</td><td class="num">26.0</td><td class="num">27.8</td></tr>
      <tr><td>TVS Motor 2W market share (%)</td><td class="num">14.8</td><td class="num">15.6</td><td class="num">16.2</td><td class="num">16.8</td></tr>
      <tr><td>EV 2W share in total 2W (%)</td><td class="num">6.2</td><td class="num">9.5</td><td class="num">13.8</td><td class="num">18.5</td></tr>
      <tr><td>Aluminium die-casting TAM (Rs lakh Cr)</td><td class="num">0.58</td><td class="num">0.64</td><td class="num">0.71</td><td class="num">0.79</td></tr>
    </tbody>
  </table>
  </div>
  <p>TVS Motor&rsquo;s 2W share gains (EV iQube scaling) flow directly to Sundaram-Clayton&rsquo;s die-casting order book. EV transition favours aluminium (lighter vs cast-iron), a natural tailwind.</p>
</section>
"""
def S5():
    return f"""
<section id="models">
  <div class="subhead">06 · Projections</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr unless stated</th><th class="num">FY25 A</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY27 Bear</th><th class="num">FY27 Bull</th><th class="num">FY28 Base</th></tr></thead>
    <tbody>
      <tr><td>Revenue</td><td class="num">2,109</td><td class="num">2,450</td><td class="num">2,850</td><td class="num">2,580</td><td class="num">3,100</td><td class="num">3,340</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">11.8</td><td class="num">12.2</td><td class="num pos">12.6</td><td class="num neg">11.0</td><td class="num pos">13.2</td><td class="num">13.0</td></tr>
      <tr><td>EBITDA</td><td class="num">249</td><td class="num">299</td><td class="num">359</td><td class="num">284</td><td class="num">409</td><td class="num">434</td></tr>
      <tr><td>PAT</td><td class="num">85</td><td class="num">112</td><td class="num">148</td><td class="num">98</td><td class="num">185</td><td class="num">195</td></tr>
      <tr><td>Capex (Rs Cr)</td><td class="num">85</td><td class="num">110</td><td class="num">140</td><td class="num">100</td><td class="num">165</td><td class="num">110</td></tr>
    </tbody>
  </table>
  </div>
  <p>Cumulative new debt need FY26-FY28 base: ~Rs 220 Cr. IBank target share 35-45% = Rs 80&ndash;100 Cr funded wallet; plus non-funded Rs 140 Cr; FX notional Rs 280 Cr.</p>
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
      <tr><td>WC CC/OD</td><td class="num">180&ndash;220</td><td>MCLR + 30 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Capex TL (EV-component capacity)</td><td class="num">120&ndash;160</td><td>MCLR + 45 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CP programme (A1+)</td><td class="num">150 rolling</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX forwards (EU / USD)</td><td class="num">260&ndash;340 notional</td><td>1.2 paise</td><td class="num">3&ndash;4</td></tr>
      <tr><td>BG / SBLC</td><td class="num">140&ndash;180</td><td>Comm 45 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Receivable financing (OEM receivables)</td><td class="num">120&ndash;160</td><td>Effective 95 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>SCF (aluminium + zinc suppliers)</td><td class="num">100&ndash;140</td><td>NIM 1.8%</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CMS + API banking</td><td class="num">&mdash;</td><td>API fee + float</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Commodity hedge advisory (aluminium LME)</td><td class="num">~200 notional</td><td>Fee-only</td><td class="num">1&ndash;2</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale income: Rs 18&ndash;27 Cr/yr.</strong> Per-entity ticket is smaller than Craftsman given Sundaram-Clayton&rsquo;s narrower product scope; but TVS Group halo + captive customer-quality compensate.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">08.1 Retail</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Workforce ~2,100 (Padi Chennai + Hosur + Mysore plants)</li>
        <li>Salary CASA Y1: 900&ndash;1,100 accounts</li>
        <li>Annual income: <strong>Rs 1.5&ndash;2 Cr</strong></li>
      </ul>
    </div>
    <div class="card accent"><h4 style="margin-top:0">08.2 PB (TVS Srinivasan family)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Family is one of India&rsquo;s top-5 business families; multi-generational wealth</li>
        <li>TVS Group aggregate promoter-family wealth Rs 85,000+ Cr (public-visible listed stakes)</li>
        <li>PB opportunity at Sundaram-Clayton-specific level modest; group-level halo substantial</li>
        <li>Annual income: <strong>Rs 4&ndash;5 Cr</strong></li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">08.3 TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 45&ndash;65 Cr</li>
        <li>CSR: Rs 2&ndash;3 Cr/yr</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 8&ndash;10 Cr/yr</h4></div>
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
      <tr><td>WC + Capex TL + CP</td><td class="num">450&ndash;530</td><td class="num">6&ndash;9</td></tr>
      <tr><td>FX forwards</td><td class="num">260&ndash;340 notional</td><td class="num">3&ndash;4</td></tr>
      <tr><td>BG/SBLC</td><td class="num">140&ndash;180</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Receivable + SCF</td><td class="num">220&ndash;300</td><td class="num">4&ndash;6</td></tr>
      <tr><td>CMS + Treasury + Commodity advisory</td><td class="num">&mdash;</td><td class="num">4&ndash;6</td></tr>
      <tr><td><strong>Wholesale total</strong></td><td class="num"><strong>1,070&ndash;1,350</strong></td><td class="num"><strong>18&ndash;27</strong></td></tr>
      <tr><td>Retail + PB + TASC</td><td>&mdash;</td><td class="num">8&ndash;10</td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>1,070&ndash;1,350</strong></td><td class="num pos"><strong>26&ndash;37 Cr/yr</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence file</div>

  <h3>10.1 Promoter &amp; ownership</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">TVS Srinivasan-family promoter structure</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Promoter holding through TVS Holdings (formerly Sundaram-Clayton Ltd pre-demerger) + direct family holdings</li>
        <li>TVS Group founding line: T.V. Sundaram Iyengar (1911) &rarr; T.S. Srinivasan (2G) &rarr; Venu Srinivasan (current TVS Motor Chairman Emeritus) + Gopal Srinivasan (Harita Seating) + Dr. Lakshmi Venu (Sundaram-Clayton DM-MD){ref("103")}</li>
        <li>Dr. Lakshmi Venu (Venu Srinivasan&rsquo;s daughter) was appointed Director with operating role at Sundaram-Clayton</li>
        <li>Low / zero promoter pledge typical across TVS family entities</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Related-party network</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Captive customer: TVS Motor Company (listed sister)</li>
        <li>Cross-holdings with TVS Holdings (listed) + Sundaram Fasteners + Harita</li>
        <li>TVS-group RPTs disclosed per SEBI LODR; arm&rsquo;s length pricing</li>
        <li>No NCLT / material litigation at group level</li>
      </ul>
    </div>
  </div>

  <h3>10.1b KMPs &amp; Probe42-verified</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Chairman / MD</td><td>Family / professional mix per post-demerger board composition{ref("103")}</td></tr>
      <tr><td>Director (operating)</td><td>Dr. Lakshmi Venu (TVS next-gen){ref("103")}</td></tr>
      <tr><td>CFO / CS</td><td>To be confirmed via MCA DIR-12 at T+14</td></tr>
      <tr><td>Independent directors</td><td>Per SEBI LODR</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 22 Jan 2026)</td><td><strong>CRISIL A1+ Reaffirmed</strong> on BG + Cash Credit + LC{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed</strong> (Probe42)</td><td><strong>ZERO</strong>{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 News / litigation</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">✓ Clean across all registers</h4><p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter. Probe42 suit-filed = 0. Post-demerger entity has clean operating record.</p></div>
    <div class="card pos"><h4 style="margin-top:0">Positive news</h4><p>FY25 margin expansion continued; TVS Motor EV iQube ramp drives captive order book; EV-component capacity capex on schedule.</p></div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>

  <h3>11.1 Days 1-30</h3>
  <div class="card accent">
    <p><strong>Entry via TVS Group relationship leverage.</strong> Meet CFO + Dr. Lakshmi Venu at Padi Chennai HO. WC CC/OD term-sheet at Rs 180-220 Cr; capex TL (EV-component) Rs 120-160 Cr; FX forwards programme; rate-lock before June MPC{ref("5")}.</p>
  </div>

  <h3>11.2 Days 31-60</h3>
  <div class="card">
    <p>Credit-committee approval of WC + capex TL; CP A1+ programme live at Rs 150 Cr rolling; CMS integration across Padi + Hosur + Mysore plants; BG/SBLC framework; commodity-hedge advisory for aluminium LME.</p>
  </div>

  <h3>11.3 Days 61-90</h3>
  <div class="card pos">
    <p>Salary migration ~900 accounts; PB onboarding at senior-management level; SCF programme for aluminium + zinc suppliers; receivable-financing programme for OEM captive receivables. Phase 2: TVS Group cross-sell introduction.</p>
  </div>

  <h3>11.4 Success metrics</h3>
  <ul class="check">
    <li>WC + capex TL sanctioned by 31 Aug 2026</li>
    <li>SCF 10+ suppliers by end-Q3 FY27</li>
    <li>Annual run-rate Rs 18&ndash;22 Cr by end-FY27</li>
    <li>TVS Group parent-level introduction secured</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared macro sources 1-22; Probe42 endpoints 81-82. Sundaram-Clayton-specific sources from [103].</em></p>
  <div class="src-list">
  <ol start="103">
  <li id="src-103"><strong>Sundaram-Clayton Ltd annual report + TVS Group public disclosures + BSE/NSE listing data</strong> &mdash; post-demerger entity (CIN L51100TN2017PLC118316), Padi Chennai + Hosur + Mysore plants, aluminium + zinc die-casting, NVH + engine components. Promoter family Venu Srinivasan + Dr. Lakshmi Venu next-gen. <span class="u">bseindia.com/stock-share-price/sundaram-clayton-ltd/SUNDRMFAST/</span></li>
  </ol>
  </div>
  <h3>Diligence items</h3>
  <ul class="x">
    <li>MCA DIR-12 fresh pull for CFO / CS / director names</li>
    <li>TVS Motor captive-customer contract tenor + receivable cycle confirmation</li>
    <li>EV-component capex phasing (Rs 160-220 Cr over FY26-27)</li>
    <li>TVS Group treasury centralisation policy</li>
  </ul>
</section>
"""
def build():
    t = "Sundaram-Clayton Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),pad("Sundaram-Clayton","Auto-component"),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
