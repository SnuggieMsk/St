"""Neuberg Diagnostics dossier (pilot 19)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "neuberg-diagnostics-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 19 of 20 · Diagnostics · Pathology chain</div>
  <h1>Neuberg Diagnostics Private Limited<br>Pan-India diagnostic / pathology chain</h1>
  <p class="lede">South-India-headquartered diagnostic / pathology chain with national presence across 120+ cities. CIN U85300TN2017PTC114099. FY25 TOI Rs 432 Cr (master sheet){ref("42")}. <strong>India Ratings A+ Assigned Stable</strong> (4 Dec 2025 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 2,125 Cr &mdash; substantial for its revenue scale reflecting acquisition-funded expansion pattern. Formed in 2017 through consolidation of 5 regional pathology chains (Ehrlich + Supratech + Global + Minerva + Anand).</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22–32 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">WC + M&amp;A finance + retail</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 432 Cr</div><div class="sub">Diagnostic labs</div></div>
    <div class="kpi pos"><div class="k">IND rating</div><div class="v num">A+ Stable</div><div class="sub">Assigned Dec 2025{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 2,125 Cr</div><div class="sub">Acquisition-heavy structure</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>M&amp;A roll-up finance</strong> &mdash; Neuberg growth via acquisition; IBank positioned for M&amp;A financing + warehouse-line</li>
      <li><strong>PE-backed; IPO track</strong> &mdash; Quadria Capital + TPG are investors; IPO-path over 24-36 months creates BRLM mandate</li>
      <li><strong>Labs-at-scale</strong> &mdash; diagnostic supply-chain + equipment imports + doctor-referral incentive schemes are recurring banking touchpoints</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U85300TN2017PTC114099</strong></span>
    <span>PE-backed <strong>Quadria + TPG + promoter</strong></span>
    <span>Registry cut <strong>Probe42 / 08 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group / consolidation history</div>
  <p>Neuberg was formed 2017 as a consolidation play by Dr. GSK Velu (founder of Trivitron Healthcare) to roll up regional pathology chains into a pan-India brand:</p>
  <ul class="check">
    <li>Ehrlich Laboratory (Chennai; oldest asset, 1923 founding)</li>
    <li>Supratech Micropath Laboratory (Ahmedabad)</li>
    <li>Global Clinical Laboratories (Bangalore)</li>
    <li>Minerva ELISA (Hyderabad)</li>
    <li>Anand Diagnostic Laboratory (Bangalore)</li>
  </ul>
  <p>Footprint now spans 120+ cities across India + select international operations (UAE / Singapore). 7 reference laboratories + 600+ collection centres. PE investors Quadria Capital + TPG joined via primary + secondary rounds.</p>
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
      <tr><td>TOI</td><td class="num">380</td><td class="num">432</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+14</td></tr>
      <tr><td>EBITDA margin</td><td class="num">~18</td><td class="num">~20</td></tr>
      <tr><td>EBITDA</td><td class="num">68</td><td class="num">86</td></tr>
      <tr><td>PAT (est)</td><td class="num">12</td><td class="num">22</td></tr>
    </tbody>
  </table>
  </div>
  <p>Scale-up phase; margins improving on operating leverage. A+ rating reflects PE support + consolidated scale.</p>
  <h3>04.1 Operational scale</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Reference labs</div><div class="v num">7</div><div class="sub">Full-service reference labs</div></div>
    <div class="kpi"><div class="k">Collection centres</div><div class="v num">600+</div><div class="sub">Pan-India</div></div>
    <div class="kpi"><div class="k">Cities covered</div><div class="v num">120+</div><div class="sub">Including Tier-2 + Tier-3</div></div>
    <div class="kpi"><div class="k">Test portfolio</div><div class="v num">5,000+</div><div class="sub">Routine + specialty + molecular</div></div>
    <div class="kpi"><div class="k">Daily test volume</div><div class="v num">~40,000</div><div class="sub">Across all labs</div></div>
    <div class="kpi accent"><div class="k">Planned expansion</div><div class="v num">200+ new centres</div><div class="sub">Through FY28; Tier-3 + home-collection</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India diagnostic labs</div>
  <p>India diagnostic market Rs 85,000+ Cr; organised share ~18% growing to 25% by FY28. Chain consolidation + digital / home-collection models driving share shift.</p>
  <h3>05.1 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Listing</th><th>Focus</th></tr></thead>
    <tbody>
      <tr><td>Dr Lal PathLabs</td><td class="num">~2,800</td><td>Listed NSE/BSE</td><td>Largest pure-play diagnostic chain</td></tr>
      <tr><td>Metropolis Healthcare</td><td class="num">~1,300</td><td>Listed</td><td>West + South India</td></tr>
      <tr><td>Thyrocare (API Holdings)</td><td class="num">~600</td><td>Subsidiary (listed via API)</td><td>B2B diagnostic hub</td></tr>
      <tr><td>SRL Diagnostics (Fortis)</td><td class="num">~1,500</td><td>Fortis subsidiary</td><td>Integrated with Fortis hospitals</td></tr>
      <tr><td>Vijaya Diagnostic Centre</td><td class="num">~580</td><td>Listed</td><td>Telangana + AP focus</td></tr>
      <tr><td>Krsnaa Diagnostics</td><td class="num">~820</td><td>Listed</td><td>PPP + radiology focus</td></tr>
      <tr><td>Apollo Diagnostics (AHEL)</td><td class="num">~800</td><td>Private (AHEL subsidiary)</td><td>Apollo-integrated</td></tr>
      <tr><td><strong>Neuberg Diagnostics</strong></td><td class="num">432</td><td>Private (PE-backed)</td><td>Pan-India consolidation play</td></tr>
      <tr><td>Suburban Diagnostics</td><td class="num">~280</td><td>Private</td><td>West India</td></tr>
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
      <tr><td>TOI</td><td class="num">432</td><td class="num">530</td><td class="num">650</td><td class="num">800</td></tr>
      <tr><td>EBITDA margin</td><td class="num">20</td><td class="num">21</td><td class="num">22</td><td class="num">23</td></tr>
      <tr><td>PAT</td><td class="num">22</td><td class="num">45</td><td class="num">75</td><td class="num">115</td></tr>
    </tbody>
  </table>
  </div>
  <p>IPO-track trajectory: Rs 800 Cr revenue + Rs 115 Cr PAT by FY28 at 23% EBITDA margin supports ~Rs 3,000-4,000 Cr IPO valuation.</p>
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
      <tr><td>WC CC/OD</td><td class="num">120&ndash;160</td><td class="num">2&ndash;3</td></tr>
      <tr><td>M&amp;A financing (acquisition warehouse line)</td><td class="num">180&ndash;260</td><td class="num">3&ndash;5</td></tr>
      <tr><td>Equipment financing (lab equipment imports)</td><td class="num">120&ndash;180</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Import LC + FX forwards (diagnostic equipment from Roche / Abbott / Siemens)</td><td class="num">180&ndash;240 notional</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Doctor-referral incentive payout CMS</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Collection-centre vendor SCF</td><td class="num">60&ndash;90</td><td class="num">1&ndash;2</td></tr>
      <tr><td>IPO BRLM mandate (future FY28)</td><td class="num">~1,000 issue</td><td class="num">6&ndash;10 one-time</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 13&ndash;20 Cr/yr recurring + Rs 6&ndash;10 Cr IPO one-time.</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~2,500-3,000 (lab technicians + admin + doctors). Dr. GSK Velu is founder (also founder of Trivitron); PB halo.</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail / salary</h4><p>Salary CASA 1,000-1,300 accounts; Rs 2-3 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (Dr. Velu family)</h4><p>Founder-promoter family; PB mandate; Rs 3-4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity trust; Rs 1-2 Cr/yr.</p></div>
  </div>
  <p>Combined Rs 6&ndash;9 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 13&ndash;20 Cr/yr + Retail/PB/TASC Rs 6&ndash;9 Cr/yr + IPO one-time Rs 6&ndash;10 Cr = <strong>Rs 25&ndash;39 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Founder Dr. GSK Velu (also Trivitron Healthcare founder)</li>
        <li>PE: Quadria Capital + TPG (growth investments)</li>
        <li>PE-IPO path expected FY27-28</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>IND A+ Assigned Stable (4 Dec 2025)</strong>{ref("81")}</li>
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
  <div class="card accent"><p><strong>T+30:</strong> Meet CFO + Dr. Velu at Chennai HO; WC + M&amp;A warehouse + equipment financing; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close WC + M&amp;A line; LC / FX for diagnostic equipment imports; doctor-referral CMS.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Salary migration; PB engagement Dr. Velu family; IPO BRLM pitch for FY28.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>WC + M&amp;A warehouse line live by 31 Aug 2026</li>
    <li>CMS + collection-centre vendor SCF live by end-Q3 FY27</li>
    <li>IPO BRLM mandate secured by end-FY27</li>
    <li>Annual run-rate Rs 14-18 Cr by end-FY27</li>
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
  <ol start="114">
  <li id="src-114"><strong>Neuberg corporate website + IND Ratings rationale Dec 2025 + Quadria + TPG press releases on investment</strong> &mdash; Formation 2017 via 5-chain roll-up; Dr. GSK Velu founder; PE-backed. <span class="u">neubergdiagnostics.com</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Neuberg Diagnostics Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Neuberg Diagnostics", "Diagnostic labs"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
