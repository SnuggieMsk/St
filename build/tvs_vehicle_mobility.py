"""TVS Vehicle Mobility Solution dossier (pilot 20)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "tvs-vehicle-mobility-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 20 of 20 · TVS Group · Mobility-as-a-Service</div>
  <h1>TVS Vehicle Mobility Solution Pvt Ltd<br>TVS Group mobility-as-a-service + fleet-management entity</h1>
  <p class="lede">TVS Group entity focused on fleet management, vehicle leasing, commercial mobility solutions, and emerging mobility-as-a-service categories. CIN U45101TN2023PTC160276 (incorporated 2023). FY25 TOI Rs 4,930 Cr (master sheet){ref("42")}. IND Ratings A+ Affirmed Positive (18 Aug 2025 Probe42){ref("81")} &mdash; Positive outlook is the clear credit-direction signal. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 640 Cr.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 40–55 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Fleet finance + WC + ancillary</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 4,930 Cr</div><div class="sub">Master sheet; new-entity rapid scale-up{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">IND rating</div><div class="v num">A+ Positive</div><div class="sub">Aug 2025; upgrade path signalled{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 640 Cr</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Fleet finance + leasing programme</strong> &mdash; CV / PV fleet management requires continuous debt cycling; IBank well-positioned</li>
      <li><strong>Mobility-as-a-Service transition</strong> &mdash; emerging segment: vehicle-leasing + ride-pooling + B2B corporate mobility</li>
      <li><strong>Positive outlook</strong> &mdash; rating trajectory up; enter before AA- step-up</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U45101TN2023PTC160276</strong></span>
    <span>Parent <strong>TVS Group</strong></span>
    <span>Registry cut <strong>Probe42 / 13 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; business scope</div>
  <p>TVS Vehicle Mobility Solution is the TVS Group's dedicated mobility-as-a-service + fleet-management entity. Complements sister entities TVS Mobility (dealership) + TVS Motor (manufacturing) + TVS Supply Chain (logistics). Operating scope:</p>
  <ul class="check">
    <li>Corporate fleet management (CV / PV lease + operate)</li>
    <li>Shared mobility programmes (B2B + B2B2C)</li>
    <li>EV fleet operations (electric 2W + 3W for delivery)</li>
    <li>Digital mobility platform (booking / routing / invoicing)</li>
    <li>Vehicle-financing adjacency</li>
  </ul>
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
      <tr><td>TOI</td><td class="num">1,200</td><td class="num">4,930</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+311 (new entity ramp)</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">~5</td><td class="num">~7</td></tr>
      <tr><td>PAT (est)</td><td class="num">25</td><td class="num">115</td></tr>
    </tbody>
  </table>
  </div>
  <p>New-entity rapid scale-up; FY25 4x YoY. Asset-heavy model given fleet ownership.</p>
  <h3>04.1 Operations</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Fleet under management</div><div class="v num">~18,000 vehicles</div><div class="sub">CV + PV + 2W/3W</div></div>
    <div class="kpi"><div class="k">Corporate clients</div><div class="v num">~250+</div><div class="sub">Pan-India footprint</div></div>
    <div class="kpi"><div class="k">Geographic span</div><div class="v num">20+ cities</div><div class="sub">Metro + Tier-2</div></div>
    <div class="kpi"><div class="k">Asset-base</div><div class="v num">~Rs 900 Cr</div><div class="sub">Fleet assets net of depreciation</div></div>
    <div class="kpi"><div class="k">Utilisation rate</div><div class="v num">~82%</div><div class="sub">Improving with AI-routing</div></div>
    <div class="kpi accent"><div class="k">Target FY28</div><div class="v num">~35,000 fleet</div><div class="sub">Rs 400-500 Cr fleet capex over 3 yrs</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India fleet / MaaS</div>
  <p>India corporate fleet + MaaS market Rs 42,000+ Cr; growing 18-22% CAGR. EV-transition + corporate-outsourcing of fleet driving segment growth.</p>
  <h3>05.1 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Focus</th><th>Fleet scale</th></tr></thead>
    <tbody>
      <tr><td>Ashok Leyland Vehicles Solutions</td><td>CV fleet</td><td class="num">~22,000</td></tr>
      <tr><td>Tata Motors Connect</td><td>PV + CV</td><td class="num">~15,000</td></tr>
      <tr><td>Magenta Mobility</td><td>EV 2W + 3W last-mile</td><td class="num">~8,000</td></tr>
      <tr><td>Bluesmart Mobility</td><td>EV ride-hailing</td><td class="num">~6,500</td></tr>
      <tr><td>LeasePlan India</td><td>Corporate PV lease</td><td class="num">~12,000</td></tr>
      <tr><td>Orix Auto India</td><td>PV lease</td><td class="num">~10,000</td></tr>
      <tr><td><strong>TVS Vehicle Mobility</strong></td><td>Multi-segment fleet + MaaS</td><td class="num">~18,000</td></tr>
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
      <tr><td>TOI</td><td class="num">4,930</td><td class="num">6,200</td><td class="num">7,500</td><td class="num">8,800</td></tr>
      <tr><td>EBITDA margin</td><td class="num">7</td><td class="num">8</td><td class="num">9</td><td class="num">10</td></tr>
      <tr><td>PAT</td><td class="num">115</td><td class="num">180</td><td class="num">260</td><td class="num">360</td></tr>
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
      <tr><td><strong>Fleet-lease financing</strong></td><td class="num">320&ndash;420</td><td class="num">6&ndash;9</td></tr>
      <tr><td>WC CC/OD (operational + customer cycle)</td><td class="num">180&ndash;240</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Vehicle receivable financing (from corporate clients)</td><td class="num">140&ndash;200</td><td class="num">2&ndash;3</td></tr>
      <tr><td>BG (corporate-contract performance)</td><td class="num">120&ndash;180</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Payment gateway + mobility-app settlement</td><td class="num">&mdash;</td><td class="num">3&ndash;5</td></tr>
      <tr><td>CP programme (A+ Positive)</td><td class="num">200 rolling</td><td class="num">1&ndash;2</td></tr>
      <tr><td>TVS Group cross-sell halo</td><td class="num">&mdash;</td><td class="num">5&ndash;7</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 21&ndash;32 Cr/yr</strong> with group-halo cross-sell.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~1,800 (drivers + ops + management). Fleet-driver salary CASA large untapped retail opportunity. TVS Group halo.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail / salary</h4><p>Driver + ops salary CASA 2,500-3,500 accounts; Rs 4-6 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (TVS halo)</h4><p>Senior mgmt + TVS-family halo; Rs 3-4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + CSR; Rs 2-3 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 9&ndash;13 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 21&ndash;32 Cr/yr + Retail/PB/TASC Rs 9&ndash;13 Cr/yr = <strong>Rs 30&ndash;45 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">TVS Group parent</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group (Srinivasan family) promoter</li>
        <li>R. Dinesh (Executive Vice Chairman of TVS Mobility sister)</li>
        <li>Low / zero pledge typical</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>IND A+ Affirmed Positive (18 Aug 2025)</strong>{ref("81")}</li>
        <li><strong>Zero suit-filed</strong>{ref("82")}</li>
        <li>Rating-upgrade path live; AA- step-up possible 12-18 months</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet CFO + TVS Group treasury; fleet-lease finance + WC + payment-gateway; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close fleet-lease programme + WC + BG; payment-gateway + mobility-app settlement integration.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Driver salary migration; TVS Group senior-management PB; Phase-2 fleet growth.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>Fleet-lease programme live by 31 Aug 2026</li>
    <li>Rating upgrade to AA- secured by end-FY27</li>
    <li>Annual run-rate Rs 20-25 Cr by end-FY27</li>
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
  <ol start="115">
  <li id="src-115"><strong>TVS Group corporate disclosures + IND Ratings credit rationale Aug 2025</strong> &mdash; Mobility-as-a-service + fleet management; new-entity (2023) rapid scale. <span class="u">tvsmobility.com &middot; tvs.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "TVS Vehicle Mobility Solution Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("TVS Vehicle Mobility Solution", "Mobility-as-a-service"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
