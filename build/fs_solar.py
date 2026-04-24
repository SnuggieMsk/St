"""FS India Solar Ventures dossier (pilot 16)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "fs-india-solar-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 16 of 20 · First Solar India · Thin-film PV module</div>
  <h1>FS India Solar Ventures Private Limited<br>First Solar's India thin-film PV module manufacturing arm</h1>
  <p class="lede">India subsidiary of First Solar Inc (NASDAQ: FSLR; global leader in thin-film cadmium telluride PV modules). CIN U29308TN2020FTC178231 (FTC = Foreign Company). Established to manufacture thin-film PV modules at Sriperumbudur, Tamil Nadu as part of First Solar's ~$1.1 bn India PLI-backed factory. FY25 TOI Rs 5,483 Cr (master sheet){ref("42")} &mdash; ramp-up phase. NOT RATED (Probe42 credit-ratings confirms){ref("81")}. Zero suit-filed (Probe42){ref("82")}. Open charges ZERO (master sheet) &mdash; entirely parent-funded.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion (greenfield)</div><div class="v num">Rs 48–62 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Trade finance + FX + first Indian-bank relationship</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 5,483 Cr</div><div class="sub">PV module ramp-up{ref("42")}</div></div>
    <div class="kpi amber"><div class="k">Credit rating</div><div class="v num">Not Rated</div><div class="sub">Parent First Solar investment-grade{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">Rs 0</div><div class="sub">Parent-equity funded; zero Indian-bank charge</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three converting angles (classic greenfield)</h4>
    <ol style="margin-bottom:0">
      <li><strong>First-ever Indian-bank charge</strong> &mdash; zero Indian-bank relationship today; entire Rs 5,483 Cr of operations funded via First Solar parent equity. Any rupee TL commitment is pioneering.</li>
      <li><strong>USD imports + USD exports</strong> &mdash; raw material + equipment imports USD-denominated; export sales to US / EU utility-scale solar developers. Large FX programme opportunity.</li>
      <li><strong>PLI receivable factoring</strong> &mdash; MeitY PLI for solar module manufacturing (Rs 19,500 Cr total outlay; FS participated){ref("31")} creates recurring receivable flow; discounting programme.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U29308TN2020FTC178231</strong></span>
    <span>Parent <strong>First Solar Inc (NASDAQ: FSLR)</strong></span>
    <span>Plant <strong>Sriperumbudur, Tamil Nadu</strong></span>
    <span>Registry cut <strong>Probe42 / 20 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; India operations</div>
  <p>First Solar Inc (NASDAQ: FSLR) is global leader in thin-film Cadmium Telluride PV modules (non-silicon technology); ~25 GW cumulative deployed worldwide. India entry via 100% subsidiary FS India Solar Ventures:</p>
  <ul class="check">
    <li><strong>3.3 GW annual capacity</strong> at Sriperumbudur (commissioned H1 CY23)</li>
    <li>~$684 mn factory capex + technology transfer from First Solar US</li>
    <li>PLI beneficiary under MeitY Solar PLI scheme</li>
    <li>Market mix: India utility-scale solar developers + US / EU export</li>
    <li>Differentiated technology vs crystalline silicon (most Indian peers)</li>
  </ul>
  <p>First Solar Inc FY25 revenue ~$4.2 bn; market cap ~$20 bn; investment-grade credit. The Indian entity is ring-fenced but benefits from parent credit halo.</p>
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
      <tr><td>TOI</td><td class="num">1,850</td><td class="num">5,483</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+196 (ramp-up)</td></tr>
      <tr><td>EBITDA margin (est)</td><td class="num">~15</td><td class="num">~22</td></tr>
      <tr><td>EBITDA (est)</td><td class="num">~278</td><td class="num">~1,206</td></tr>
      <tr><td>PAT (est)</td><td class="num">85</td><td class="num">650</td></tr>
    </tbody>
  </table>
  </div>
  <p>Rapid ramp-up phase; margins reflect high-ASP thin-film module pricing + PLI benefits. Zero Indian-bank debt; 100% parent-equity funded.</p>
  <h3>04.1 Plant operating metrics</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Commissioned capacity</div><div class="v num">3.3 GW</div><div class="sub">Thin-film CdTe modules</div></div>
    <div class="kpi"><div class="k">Module technology</div><div class="v num">Series 7</div><div class="sub">First Solar proprietary thin-film</div></div>
    <div class="kpi"><div class="k">Efficiency (module-level)</div><div class="v num">~19.5%</div><div class="sub">Competitive vs silicon peers</div></div>
    <div class="kpi"><div class="k">Domestic market share (thin-film)</div><div class="v num">100%</div><div class="sub">Only thin-film player in India</div></div>
    <div class="kpi"><div class="k">Export share</div><div class="v num">~55%</div><div class="sub">US + EU utility-scale solar developers</div></div>
    <div class="kpi accent"><div class="k">ALMM listing</div><div class="v num">Approved</div><div class="sub">Eligible for Govt + DISCOM tenders</div></div>
  </div>
  <h3>04.2 Capex + PLI eligibility</h3>
  <p>First Solar India participated in MeitY PLI-II (Rs 19,500 Cr outlay) and has been allocated capacity commitments. Plant capex ~$684 mn (~Rs 5,700 Cr) fully equity-funded by First Solar parent (USD); no Indian-bank charge. Phase-2 expansion to 6.6 GW (brownfield) under evaluation for FY28 commissioning; would be the next capex vector with potential Indian-bank participation.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India solar PV module manufacturing</div>
  <p>India solar PV manufacturing capacity: ~35 GW (FY25) &rarr; 70 GW (FY28 target). ALMM (Approved List of Models &amp; Manufacturers) policy protects domestic manufacturers. PLI-II (Rs 19,500 Cr outlay) catalysed ~55 GW capacity additions. First Solar is the only major non-silicon (thin-film CdTe) player in India; offers differentiated technology for utility-scale + rooftop applications.</p>
  <p>Peers: Waaree Energies (listed FY24 IPO), Premier Energies (listed 2024 IPO), Adani Solar, Vikram Solar, Tata Power Solar, Saatvik Solar, RenewSys, Goldi Solar. First Solar's thin-film positioning differentiates vs silicon peers.</p>
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
      <tr><td>TOI</td><td class="num">5,483</td><td class="num">7,200</td><td class="num">8,800</td><td class="num">10,500</td></tr>
      <tr><td>EBITDA margin</td><td class="num">22</td><td class="num">23</td><td class="num">24</td><td class="num">25</td></tr>
      <tr><td>PAT</td><td class="num">650</td><td class="num">920</td><td class="num">1,180</td><td class="num">1,500</td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S6():
    return f"""
<section id="entry-map">
  <div class="subhead">07 · Entry-point map (full greenfield)</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>WC CC/OD (first Indian-bank line)</td><td class="num">380&ndash;480</td><td class="num">7&ndash;9</td></tr>
      <tr><td>Import LC + SBLC (USD equipment + raw materials)</td><td class="num">520&ndash;680</td><td class="num">4&ndash;6</td></tr>
      <tr><td>FX forwards (large USD exposure)</td><td class="num">1,200&ndash;1,600 notional</td><td class="num">14&ndash;18</td></tr>
      <tr><td>BG (customer + PLI)</td><td class="num">220&ndash;300</td><td class="num">1&ndash;2</td></tr>
      <tr><td>PLI receivable factoring</td><td class="num">340&ndash;460</td><td class="num">4&ndash;6</td></tr>
      <tr><td>CMS + API banking</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Treasury / liquid-fund management</td><td class="num">400&ndash;600 AUM</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Rating-sponsor fee (first-time CRISIL + ICRA)</td><td class="num">&mdash;</td><td class="num">8&ndash;12 (one-time)</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 37&ndash;50 Cr/yr recurring + Rs 8&ndash;12 Cr one-time (rating + CP arranger).</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Workforce ~1,200-1,500 at Sriperumbudur plant. Professional management (expatriate + Indian).</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail / salary</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Salary CASA 600-800 accounts Y1</li>
        <li>Ticket Rs 35,000-75,000/mo (technical + professional)</li>
        <li>Annual income Rs 2-3 Cr</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">PB (limited)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>No Indian promoter family</li>
        <li>Senior-management + expatriate-leadership PB</li>
        <li>Annual income Rs 2-3 Cr</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 40-60 Cr</li>
        <li>CSR: Rs 5-7 Cr/yr</li>
        <li>Annual income Rs 2-3 Cr</li>
      </ul>
    </div>
  </div>
  <p>Combined Rs 8&ndash;10 Cr/yr.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 37&ndash;50 Cr/yr + Retail/TASC Rs 8&ndash;10 Cr/yr + Rating sponsor Rs 8&ndash;12 Cr one-time = <strong>Rs 53&ndash;72 Cr/yr fully-built (incl. one-time)</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>100% First Solar Inc (NASDAQ: FSLR); investment-grade US parent</li>
        <li>Foreign-company structure (FTC)</li>
        <li>No promoter-family (professional management)</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>Not Rated</strong> &mdash; rating-sponsor opportunity{ref("81")}</li>
        <li><strong>Zero suit-filed</strong>{ref("82")}</li>
        <li>MeitY PLI compliance framework</li>
      </ul>
    </div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet India CFO + global First Solar treasury. First WC line + FX programme + rating-sponsorship mandate; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close WC; LC framework for equipment + RM imports; FX hedging go-live.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> PLI factoring programme; CRISIL / ICRA dual rating kickoff; treasury mandate.</p></div>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. FS India Solar sources from [111].</em></p>
  <div class="src-list"><ol start="111">
  <li id="src-111"><strong>First Solar Inc (NASDAQ: FSLR) annual reports + India press release on Sriperumbudur 3.3 GW plant + MeitY PLI scheme list</strong> &mdash; India operations ramp-up; thin-film PV technology; export-oriented. <span class="u">firstsolar.com &middot; sec.gov/edgar/search/?q=FSLR</span></li>
  </ol></div>
</section>
"""
def build():
    t = "FS India Solar Ventures Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("FS India Solar", "Solar PV manufacturing"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
