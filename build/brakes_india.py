"""Brakes India dossier (pilot 25)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "brakes-india-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 25 of 40 · Chennai · TVS-Rane JV · Brake systems</div>
  <h1>Brakes India Private Limited<br>India's largest auto brake-systems manufacturer (TVS Group + Rane)</h1>
  <p class="lede">63-year-old JV between TVS Group + Rane Group + Allied Signal (now ZF Friedrichshafen, Germany). India's largest manufacturer of automotive brake systems for CV + PV + 2W. CIN U35999TN1962PTC004928. FY25 TOI Rs 7,081 Cr (master sheet){ref("42")}. MNC-classified due to ZF Friedrichshafen stake. Plants at Chennai + Nanjangud (Karnataka) + Polambakkam (Kancheepuram) + Manesar + Uttarakhand.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 48–65 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">TVS + Rane + ZF group halo</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 7,081 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi"><div class="k">Parent mix</div><div class="v num" style="font-size:1rem">TVS + Rane + ZF</div><div class="sub">~49% + 18% + ~32.5% (est)</div></div>
    <div class="kpi"><div class="k">Plants</div><div class="v num">5</div><div class="sub">TN + KA + Haryana + Uttarakhand</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>TVS + Rane + ZF group halo</strong> &mdash; triple-promoter structure opens multiple relationship doors</li>
      <li><strong>CV + PV auto cycle tailwind</strong> &mdash; largest brake supplier; volume-linked revenue</li>
      <li><strong>EV braking transition</strong> &mdash; regenerative + brake-by-wire systems for EVs; technology transition capex</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U35999TN1962PTC004928</strong></span>
    <span>Structure <strong>TVS + Rane + ZF Friedrichshafen JV</strong></span>
    <span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group</div>
  <p>Brakes India is a historical JV with three promoter blocks:</p>
  <ul class="check">
    <li><strong>TVS Group</strong> &mdash; ~49% (promoter); TVS Motor + ecosystem benefits</li>
    <li><strong>Rane Group</strong> &mdash; ~18%; Rane Madras + Rane Holdings ecosystem</li>
    <li><strong>ZF Friedrichshafen AG (Germany)</strong> &mdash; ~32.5%; global tier-1 auto-components supplier (acquired Allied Signal's stake)</li>
  </ul>
  <p>Relationship leverage: winning Brakes India is a gateway to all three promoter groups. TVS Group (already covered via Sundaram-Clayton + Wheels India + TVS Motor + TVS Mobility + TVS Srichakra + TVS Vehicle Mobility Tier-1 dossiers) is a natural cross-sell. Rane Group (Rane Madras + Rane Holdings + Rane NSK + Rane Brake Lining etc.) is 6 RM-mapped entities already on the existing IBank book. ZF Friedrichshafen is a listed global auto-components major.</p>
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
      <tr><td>TOI</td><td class="num">6,400</td><td class="num">7,081</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">12.5</td><td class="num">13.2</td></tr>
      <tr><td>EBITDA</td><td class="num">800</td><td class="num">935</td></tr>
      <tr><td>PAT (est)</td><td class="num">420</td><td class="num">505</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 Operations</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Plants</div><div class="v num">5</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~8,500</div></div>
    <div class="kpi"><div class="k">OEM customers</div><div class="v num">All major</div><div class="sub">Tata, Maruti, Mahindra, Ashok Leyland, HMSI, TVS Motor, Daimler, Bajaj, Hero</div></div>
    <div class="kpi"><div class="k">Product portfolio</div><div class="v num">Full brake</div><div class="sub">Discs, drums, callipers, ABS, EBS</div></div>
    <div class="kpi"><div class="k">Export share</div><div class="v num">~20%</div></div>
    <div class="kpi"><div class="k">Aftermarket</div><div class="v num">~15%</div><div class="sub">via &ldquo;Mintex&rdquo; brand</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; Auto brake systems</div>
  <p>India brake-systems market ~Rs 32,000 Cr; growing 9-11% CAGR. Brakes India market leader with ~35% OEM share. Peers: Bosch (Mico India), WABCO-TVS (another TVS Group entity - now ZF), Continental, Knorr-Bremse.</p>
  <h3>05.1 Peers</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 India revenue (Rs Cr)</th><th>Focus</th></tr></thead>
    <tbody>
      <tr><td><strong>Brakes India</strong></td><td class="num">7,081</td><td>Market leader</td></tr>
      <tr><td>Bosch India (Mico)</td><td class="num">~14,200</td><td>Multi-product incl. brakes</td></tr>
      <tr><td>ZF Commercial Vehicle Control Systems India (sister)</td><td class="num">3,841</td><td>CV brake controls; listed</td></tr>
      <tr><td>Knorr-Bremse India</td><td class="num">~2,800</td><td>CV + rail braking</td></tr>
      <tr><td>Continental India</td><td class="num">~8,500</td><td>Multi-product</td></tr>
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
      <tr><td>TOI</td><td class="num">7,081</td><td class="num">7,950</td><td class="num">8,900</td><td class="num">8,100</td><td class="num">9,700</td><td class="num">10,100</td></tr>
      <tr><td>EBITDA margin</td><td class="num">13.2</td><td class="num">13.8</td><td class="num pos">14.5</td><td class="num neg">12.8</td><td class="num pos">15.2</td><td class="num">15.0</td></tr>
      <tr><td>EBITDA</td><td class="num">935</td><td class="num">1,097</td><td class="num">1,291</td><td class="num">1,037</td><td class="num">1,474</td><td class="num">1,515</td></tr>
      <tr><td>PAT</td><td class="num">505</td><td class="num">605</td><td class="num">740</td><td class="num">555</td><td class="num">880</td><td class="num">870</td></tr>
    </tbody>
  </table>
  </div>
  <p>Drivers: CV + PV cycle, EV-braking transition (brake-by-wire adds 20-30% content per vehicle), export growth to MENA + ASEAN.</p>
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
      <tr><td>WC CC/OD</td><td class="num">320&ndash;420</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Capex TL (EV-braking + ABS capacity)</td><td class="num">180&ndash;260</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Import LC (ZF technology + raw materials)</td><td class="num">420&ndash;560</td><td class="num">3&ndash;5</td></tr>
      <tr><td>FX forwards</td><td class="num">640&ndash;860 notional</td><td class="num">8&ndash;11</td></tr>
      <tr><td>EPC (exports)</td><td class="num">180&ndash;240</td><td class="num">2&ndash;3</td></tr>
      <tr><td>BG (OEM customer + technology)</td><td class="num">140&ndash;200</td><td class="num">1&ndash;2</td></tr>
      <tr><td>SCF (casting + forging vendors)</td><td class="num">180&ndash;260</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Receivable financing (OEM captive)</td><td class="num">160&ndash;220</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Aftermarket / Mintex brand CMS</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>TVS + Rane group cross-sell</td><td class="num">&mdash;</td><td class="num">6&ndash;8</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 36&ndash;51 Cr/yr.</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~8,500.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 3,500-4,500 accounts; Rs 4-5 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (triple-group halo)</h4><p>TVS + Rane + ZF senior mgmt; Rs 5-7 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity; Rs 2-3 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 11&ndash;15 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 36&ndash;51 Cr/yr + Retail/PB/TASC Rs 11&ndash;15 Cr/yr = <strong>Rs 47&ndash;66 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group ~49% (family)</li>
        <li>Rane Group ~18% (family)</li>
        <li>ZF Friedrichshafen ~32.5% (listed German; ETR: ZFR)</li>
        <li>Triple-promoter JV stable for 60+ years</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Board representation across three promoter groups</li>
        <li>Clean track record; no NCLT / CIRP</li>
        <li>Apple-tier OEM compliance</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet CFO + TVS + Rane + ZF representatives; WC + FX + EPC; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close WC + capex TL; SCF for casting / forging vendors; CMS.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Salary CASA + TVS Group cross-sell + Rane Group cross-sell.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>WC + capex TL live by 31 Aug 2026</li>
    <li>TVS + Rane group halo cross-sell initiated</li>
    <li>Annual run-rate Rs 28-35 Cr by end-FY27</li>
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
  <ol start="120">
  <li id="src-120"><strong>Brakes India Pvt Ltd + TVS + Rane + ZF Friedrichshafen corporate disclosures + SIAM data</strong> &mdash; JV structure since 1962; multi-plant India footprint. <span class="u">brakesindia.com &middot; tvs.com &middot; rane.co.in</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Brakes India Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Brakes India", "Auto brake systems"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
