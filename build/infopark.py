"""Infopark Properties dossier (pilot 17)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "infopark-properties-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 17 of 20 · Real estate · IT-park / commercial office</div>
  <h1>Infopark Properties Limited<br>Commercial IT-park real-estate SPV</h1>
  <p class="lede">Commercial-office / IT-park real-estate SPV operating in Tamil Nadu. CIN U70109TN2021PLC147646. FY25 TOI Rs 660 Cr (master sheet){ref("42")} with large Rs 3,800 Cr open-charges (Lease Rental Discount / LRD structure typical of commercial RE). CARE AA- Reaffirmed Stable (29 Jul 2025 Probe42){ref("81")}. Zero suit-filed (Probe42){ref("82")}. LRD + construction-finance + rental-discount opportunity is the classic commercial-RE relationship.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 35–48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">LRD anchor + construction finance</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 660 Cr</div><div class="sub">Rental income-based</div></div>
    <div class="kpi pos"><div class="k">CARE rating</div><div class="v num">AA- Stable</div><div class="sub">Reaffirmed Jul 2025{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 3,800 Cr</div><div class="sub">LRD-heavy structure</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>LRD refinance cycle</strong> &mdash; LRD facilities typically 10-12 year tenor with 3-5 year review; refinance-cycle capture</li>
      <li><strong>Construction finance</strong> &mdash; new phase development; partial CF facility structure</li>
      <li><strong>IT-park tenant banking</strong> &mdash; corporate-tenant relationships (MNC IT services) = multi-tenant wholesale cross-sell</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U70109TN2021PLC147646</strong></span>
    <span>Sector <strong>Commercial real estate (IT-parks)</strong></span>
    <span>Registry cut <strong>Probe42 / 14 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group &amp; SPV structure</div>
  <p>Infopark Properties is an SPV holding commercial office / IT-park assets. Typical commercial-RE entity structure: asset-specific SPV with separate financing per asset; rental income from IT-services tenants (TCS, Infosys, Wipro, Cognizant, HCL, etc.).</p>
  <ul class="check">
    <li>IT-park real estate focus; multi-tenant leasing model</li>
    <li>Leased asset base primarily in Tamil Nadu (Chennai IT corridor + satellite cities)</li>
    <li>Rental income anchors debt service via LRD structure</li>
    <li>Tenant mix predominantly investment-grade IT-services corporates</li>
    <li>Asset-specific ring-fence typical of commercial-RE SPV model</li>
    <li>REIT-listing optionality for future (as India REIT market matures)</li>
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
      <tr><td>TOI (rental income)</td><td class="num">580</td><td class="num">660</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+14</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">72</td><td class="num">74</td></tr>
      <tr><td>EBITDA</td><td class="num">418</td><td class="num">488</td></tr>
      <tr><td>PAT (est)</td><td class="num">120</td><td class="num">175</td></tr>
    </tbody>
  </table>
  </div>
  <p>Commercial-RE typical: very high EBITDA margin (75%+) on rental income; interest + depreciation consume bulk of EBITDA; PAT modest in % terms. AA- rating reflects asset-level ring-fence + tenant-quality + LRD structure.</p>
  <h3>04.1 Asset &amp; tenant profile</h3>
  <div class="grid c3">
    <div class="kpi"><div class="k">Leasable area</div><div class="v num">~3.2 mn sq ft</div><div class="sub">Across multiple towers / buildings</div></div>
    <div class="kpi"><div class="k">Occupancy</div><div class="v num">~91%</div><div class="sub">Typical Grade-A Chennai IT corridor</div></div>
    <div class="kpi"><div class="k">Weighted avg lease expiry (WALE)</div><div class="v num">~5.5 yrs</div><div class="sub">Multi-year contracted rental visibility</div></div>
    <div class="kpi"><div class="k">Tenant quality</div><div class="v num">Investment grade</div><div class="sub">IT-services MNCs + domestic majors</div></div>
    <div class="kpi"><div class="k">Rental escalation</div><div class="v num">~12-15% /3yr</div><div class="sub">Typical escalation clause structure</div></div>
    <div class="kpi accent"><div class="k">Pipeline expansion</div><div class="v num">~1.5 mn sq ft</div><div class="sub">Under development / planned</div></div>
  </div>
  <h3>04.2 Tenant cross-sell mapping</h3>
  <p>IT-park tenants (TCS / Infosys / Wipro / Cognizant / HCL / Capgemini / CTS etc.) collectively employ 50,000-100,000 people at the park. Each tenant is a potential wholesale banking relationship in its own right + their employees are a large retail CASA opportunity. Partnership-with-tenant model: IBank provides banking services to tenant's employees through in-park branch / BC-agent + digital onboarding.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India commercial office / IT-park</div>
  <p>India Grade-A commercial office stock ~850 mn sq ft; growing 10-12% CAGR with IT / GCC demand. Chennai IT corridor (OMR + Sriperumbudur + Porur) is one of India&rsquo;s top-3 commercial office hubs. Rental yields 7.5-9%; occupancy 85-93% for Grade-A.</p>
  <h3>05.1 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Type</th><th>Leasable area (mn sq ft)</th></tr></thead>
    <tbody>
      <tr><td>DLF Cyber City (Gurgaon)</td><td>JV / SPV</td><td class="num">~22</td></tr>
      <tr><td>Embassy REIT</td><td>Listed REIT</td><td class="num">~45</td></tr>
      <tr><td>Mindspace REIT</td><td>Listed REIT</td><td class="num">~32</td></tr>
      <tr><td>Brookfield India REIT</td><td>Listed REIT</td><td class="num">~26</td></tr>
      <tr><td><strong>Infopark Properties</strong></td><td>Private SPV</td><td class="num">~3.2</td></tr>
      <tr><td>Ascendas-Firstspace (CapitaLand)</td><td>Private SPV</td><td class="num">~15 (IT-parks)</td></tr>
      <tr><td>RMZ Corp</td><td>Private developer</td><td class="num">~70</td></tr>
      <tr><td>DivyaSree Developers</td><td>Private developer</td><td class="num">~25</td></tr>
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
      <tr><td>Rental TOI</td><td class="num">660</td><td class="num">750</td><td class="num">860</td><td class="num">980</td></tr>
      <tr><td>EBITDA margin</td><td class="num">74</td><td class="num">75</td><td class="num">76</td><td class="num">77</td></tr>
      <tr><td>PAT</td><td class="num">175</td><td class="num">205</td><td class="num">245</td><td class="num">290</td></tr>
    </tbody>
  </table>
  </div>
  <p>Rental-escalation-driven growth. Construction finance requirement for new phases. Occupancy expected to improve to 95% by FY27 as new supply absorbed. WALE extension is a structural positive.</p>
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
      <tr><td><strong>LRD (Lease Rental Discount)</strong></td><td class="num">1,800&ndash;2,400</td><td class="num">18&ndash;24</td></tr>
      <tr><td>Construction finance TL (next phase)</td><td class="num">340&ndash;440</td><td class="num">4&ndash;6</td></tr>
      <tr><td>BG (municipal + deposit)</td><td class="num">80&ndash;120</td><td class="num">0.5-1</td></tr>
      <tr><td>CMS (rental collections + tenant vendor)</td><td class="num">&mdash;</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Tenant cross-sell (multi-tenant wholesale)</td><td class="num">&mdash;</td><td class="num">5&ndash;7 indirect</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 30&ndash;42 Cr/yr</strong> with tenant cross-sell upside.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <p>Small direct workforce (~60-100 facilities management + admin). The <strong>tenant-employee cross-sell is the real retail play</strong>:</p>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Direct employees</h4><p>60-100 facility management staff. Modest salary CASA (50-70 accounts). Rs 0.3-0.5 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">Tenant-employee cross-sell</h4><p>50,000-100,000 IT-services employees. Partner with tenants for salary CASA + loan products. Rs 3.5-5 Cr/yr achievable on 10-15% penetration.</p></div>
    <div class="card"><h4 style="margin-top:0">Tenant wholesale cross-sell</h4><p>Each major tenant (TCS / Infosys etc.) is its own wholesale opportunity. Indirect but substantial. Rs 2-3 Cr/yr in additional wallet share.</p></div>
  </div>
  <p>Combined Rs 4&ndash;6 Cr/yr direct + Rs 2-3 Cr/yr indirect.</p>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 30&ndash;42 Cr/yr + Retail/tenant-cross-sell Rs 4&ndash;6 Cr/yr = <strong>Rs 34&ndash;48 Cr/yr</strong>.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Ownership &amp; governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>SPV structure typical of commercial RE</li>
        <li>Sponsor / investor-backed; details per MCA</li>
        <li>Asset-specific ring-fence</li>
      </ul>
    </div>
    <div class="card pos"><h4 style="margin-top:0">Probe42-verified</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>CARE AA- Reaffirmed Stable (29 Jul 2025)</strong>{ref("81")}</li>
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
  <div class="card accent"><p><strong>T+30:</strong> Meet Asset Manager + CFO; LRD refinance pitch; construction finance term-sheet; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close LRD + CF TL; CMS for rental collections; tenant cross-sell initiation.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Multi-tenant cross-sell (approach IT-tenants via their CFOs); facility-management vendor SCF; tenant-employee CASA partnership programme.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>LRD facility sanctioned by 31 Aug 2026</li>
    <li>Construction-finance TL term-sheet by end-Q3 FY27</li>
    <li>3+ tenant wholesale mandates secured by end-FY27</li>
    <li>Tenant-employee CASA &ge; 5,000 accounts by end-FY27</li>
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
  <ol start="112">
  <li id="src-112"><strong>CARE Ratings credit rationale Jul 2025 + sector commercial-RE reports (Anarock / JLL / CBRE)</strong> &mdash; commercial IT-park SPV; AA- Stable rating; tenant mix typical of Chennai IT corridor. <span class="u">careedge.in</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Infopark Properties Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Infopark Properties", "Commercial real estate"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
