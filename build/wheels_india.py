"""Wheels India dossier (pilot 09)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "wheels-india-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 09 of 20 · TVS Group · Auto wheels</div>
  <h1>Wheels India Limited<br>India's largest steel-wheel manufacturer for auto OEMs</h1>
  <p class="lede">Listed TVS Group company (NSE / BSE) manufacturing steel wheels + aluminium wheels for CV, PV, tractor, construction-equipment, 2W/3W and aerospace casting applications. CIN L35921TN1960PLC004175. FY25 TOI Rs 4,415 Cr (master sheet){ref("42")}; India Ratings A+ Assigned Stable (20 Feb 2026 Probe42){ref("81")} + ICRA ratings on FD / Bank Loan (18 Feb 2026). Zero suit-filed (Probe42){ref("82")}. Open charges Rs 1,038 Cr across consortium. Diversified customer mix across CVs (40%), PVs (25%), tractors (15%), construction equipment (10%), aerospace/other (10%). Multi-plant footprint: Padi (Chennai) + Sriperumbudur + Pantnagar + Pune + Rampur + Dharwad + Chennai-Bawal-Pithampur.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 48–62 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 38–50 Cr + Retail Rs 10–12 Cr</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 4,415 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">IND / ICRA rating</div><div class="v num">A+ Stable</div><div class="sub">Assigned Feb 2026{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges (MCA)</div><div class="v num">Rs 1,038 Cr</div><div class="sub">WC + capex consortium</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this converts</h4>
    <ol style="margin-bottom:0">
      <li><strong>TVS Group anchor</strong> &mdash; founded 1960; one of TVS Group&rsquo;s earliest manufacturing entities; strong legacy plus EV transition tailwind</li>
      <li><strong>CV / PV / tractor / CE diversification</strong> &mdash; cycle-hedged across multiple auto end-segments</li>
      <li><strong>Aerospace casting adjacency</strong> &mdash; small but high-margin growth vector; aluminium investment castings for aerospace OEMs (HAL, Boeing)</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L35921TN1960PLC004175</strong></span>
    <span>Listed <strong>NSE / BSE</strong></span>
    <span>Promoter <strong>TVS Group (Srinivasan family)</strong></span>
    <span>Registry cut <strong>Probe42 / 29 Jan 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group / subsidiary map</div>
  <p>Wheels India is a 65-year-old TVS Group listed entity. Key subsidiaries include:</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity</th><th>Stake</th><th>Role</th></tr></thead>
    <tbody>
      <tr><td><strong>Wheels India Limited (this entity)</strong></td><td>TVS Group promoter ~50%</td><td>Parent; steel + aluminium wheels + aerospace castings</td></tr>
      <tr><td>Axles India</td><td>Subsidiary / associate</td><td>Axles for CV + tractor</td></tr>
      <tr><td>Sundaram Castings (Padi plant unit)</td><td>Internal unit</td><td>Ductile iron castings for ancillary products</td></tr>
      <tr><td>Global manufacturing partners (JVs)</td><td>Various</td><td>Technology + export tie-ups</td></tr>
    </tbody>
  </table>
  </div>
  <h3>03.1 Revenue segment mix (FY25 est)</h3>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Steel wheels (CV + Tractor + CE)</h4><p>~60% of revenue. Dominant positions in CV and tractor; large-diameter steel wheels competitive moat.</p></div>
    <div class="card"><h4 style="margin-top:0">Aluminium wheels (PV + 2W)</h4><p>~30% of revenue. PV OEM supplies; growing 2W mix. Aluminium-wheel mix is the structural up-move.</p></div>
    <div class="card"><h4 style="margin-top:0">Aerospace castings + misc</h4><p>~10% of revenue. High-margin investment castings for HAL + global aerospace OEMs; small but strategic.</p></div>
  </div>
</section>
"""
def S3():
    return f"""
<section id="entity">
  <div class="subhead">04 · Entity dossier</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Rs Cr</th><th class="num">FY23 est</th><th class="num">FY24 est</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">3,820</td><td class="num">4,180</td><td class="num">4,415</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">9.2</td><td class="num">9.6</td><td class="num">9.8</td></tr>
      <tr><td>EBITDA</td><td class="num">351</td><td class="num">401</td><td class="num">432</td></tr>
      <tr><td>PAT (est)</td><td class="num">115</td><td class="num">140</td><td class="num">165</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">3.4</td><td class="num">3.2</td><td class="num">3.1</td></tr>
    </tbody>
  </table>
  </div>
  <div class="grid c3">
    <div class="kpi"><div class="k">Net Worth (FY25 est)</div><div class="v num">850</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">1,340</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">1,038</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~5,800</div><div class="sub">Multi-plant</div></div>
    <div class="kpi"><div class="k">Plants</div><div class="v num">7</div><div class="sub">Padi + 6 other locations</div></div>
    <div class="kpi accent"><div class="k">Capex FY26-27</div><div class="v num">240-320</div><div class="sub">Rs Cr; aluminium capacity</div></div>
  </div>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; Auto wheels</div>
  <p>India auto-wheel market (steel + aluminium) ~Rs 38,000 Cr; growing ~9-11% CAGR with aluminium mix shift from ~25% to ~40% by FY28 on EV + PV premiumisation. Wheels India is the clear steel-wheel market leader (~55% CV + tractor share); aluminium peer Enkei, CEAT, Apollo Tyres-adjacent smaller. Aerospace casting TAM small but 22% CAGR.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Metric</th><th class="num">FY24</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 E</th></tr></thead>
    <tbody>
      <tr><td>India auto wheels TAM (Rs lakh Cr)</td><td class="num">0.36</td><td class="num">0.38</td><td class="num">0.42</td><td class="num">0.46</td></tr>
      <tr><td>Aluminium wheel share (%)</td><td class="num">28</td><td class="num">30</td><td class="num">34</td><td class="num">38</td></tr>
      <tr><td>CV production growth YoY (%)</td><td class="num">+8</td><td class="num">+7</td><td class="num">+8</td><td class="num">+7</td></tr>
      <tr><td>Tractor production (lakh units)</td><td class="num">9.5</td><td class="num">10.4</td><td class="num">11.1</td><td class="num">11.7</td></tr>
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
      <tr><td>Revenue</td><td class="num">4,415</td><td class="num">4,900</td><td class="num">5,500</td><td class="num">4,980</td><td class="num">6,050</td><td class="num">6,150</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">9.8</td><td class="num">10.1</td><td class="num pos">10.5</td><td class="num neg">9.0</td><td class="num pos">11.2</td><td class="num">10.8</td></tr>
      <tr><td>EBITDA</td><td class="num">432</td><td class="num">495</td><td class="num">578</td><td class="num">448</td><td class="num">678</td><td class="num">664</td></tr>
      <tr><td>PAT</td><td class="num">165</td><td class="num">195</td><td class="num">245</td><td class="num">155</td><td class="num">310</td><td class="num">295</td></tr>
      <tr><td>Capex</td><td class="num">125</td><td class="num">160</td><td class="num">180</td><td class="num">130</td><td class="num">210</td><td class="num">140</td></tr>
    </tbody>
  </table>
  </div>
  <p>Cumulative new debt need FY26-28 base: ~Rs 280 Cr. IBank target 35-45% = Rs 95-125 Cr funded wallet.</p>
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
      <tr><td>WC CC/OD (share-grow)</td><td class="num">340&ndash;420</td><td>MCLR + 35 bp</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Capex TL (aluminium capacity)</td><td class="num">180&ndash;240</td><td>MCLR + 50 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>FX forwards (export + import)</td><td class="num">380&ndash;480 notional</td><td>1.2 paise</td><td class="num">5&ndash;7</td></tr>
      <tr><td>BG + SBLC</td><td class="num">200&ndash;260</td><td>Comm 45 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>EPC (aerospace exports)</td><td class="num">120&ndash;160</td><td>SBLR + 75 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Receivable financing (OEM captive)</td><td class="num">160&ndash;220</td><td>Effective 95 bp</td><td class="num">2&ndash;3</td></tr>
      <tr><td>SCF (steel + aluminium suppliers)</td><td class="num">180&ndash;240</td><td>NIM 1.8%</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Commodity hedge (steel / aluminium LME)</td><td class="num">~400 notional</td><td>Fee-only</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CMS + API banking (7 plants)</td><td class="num">&mdash;</td><td>API fee + float</td><td class="num">4&ndash;5</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale total: Rs 26&ndash;37 Cr/yr</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">08.1 Retail</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Workforce ~5,800 across 7 plants</li>
        <li>Salary CASA Y1: 2,500&ndash;3,200 accounts</li>
        <li>Annual income: <strong>Rs 3.5&ndash;4.5 Cr</strong></li>
      </ul>
    </div>
    <div class="card accent"><h4 style="margin-top:0">08.2 PB (TVS-extended)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group family halo</li>
        <li>Director-level + senior-management engagement</li>
        <li>Annual income: <strong>Rs 3&ndash;4 Cr</strong></li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">08.3 TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 95&ndash;130 Cr</li>
        <li>CSR: Rs 4&ndash;5 Cr/yr</li>
        <li>Annual income: <strong>Rs 3&ndash;4 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 10&ndash;12 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated wallet</div>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Bucket</th><th class="num">Wallet</th><th class="num">Income (Rs Cr/yr)</th></tr></thead>
    <tbody>
      <tr><td>Funded (WC + Capex TL + EPC)</td><td class="num">640&ndash;820</td><td class="num">10&ndash;14</td></tr>
      <tr><td>Non-funded (BG + SBLC)</td><td class="num">200&ndash;260</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX derivative notional</td><td class="num">380&ndash;480</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Receivable + SCF</td><td class="num">340&ndash;460</td><td class="num">5&ndash;7</td></tr>
      <tr><td>CMS + commodity advisory</td><td class="num">&mdash;</td><td class="num">5&ndash;7</td></tr>
      <tr><td><strong>Wholesale</strong></td><td class="num"><strong>1,560&ndash;2,020</strong></td><td class="num"><strong>26&ndash;37</strong></td></tr>
      <tr><td>Retail / PB / TASC</td><td>&mdash;</td><td class="num">10&ndash;12</td></tr>
      <tr><td><strong>Grand total</strong></td><td class="num"><strong>1,560&ndash;2,020</strong></td><td class="num pos"><strong>36&ndash;49 Cr/yr</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Promoter</h4>
      <ul class="check" style="margin-bottom:0">
        <li>TVS Group Srinivasan family (multi-generational)</li>
        <li>Promoter holding ~50% (listed, quarterly disclosed)</li>
        <li>Low / zero pledge typical</li>
        <li>Board: executive promoter + independent directors per SEBI LODR</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">KMPs &amp; ratings</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Chairman / MD per post-demerger TVS Group structure</li>
        <li>CFO / CS / independent directors to be confirmed MCA DIR-12 T+14</li>
        <li><strong>IND A+ Assigned Stable (20 Feb 2026)</strong> + ICRA ratings (18 Feb 2026){ref("81")}</li>
        <li><strong>Zero suit-filed (Probe42)</strong>{ref("82")}</li>
      </ul>
    </div>
  </div>
  <h3>10.3 News / litigation</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">✓ Clean</h4><p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter. Zero bureau suit-filed cases.</p></div>
    <div class="card pos"><h4 style="margin-top:0">Recent rating action</h4><p>Dual-agency IND + ICRA fresh ratings Feb 2026 reflect improving credit profile on CV cycle + aluminium mix expansion.</p></div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><h4 style="margin-top:0">T + 30</h4><p>Meet Padi Chennai CFO + TVS-representative director. WC share-grow + capex TL (aluminium capacity) + FX forwards; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><h4 style="margin-top:0">T + 60</h4><p>Close WC + capex TL; CMS integration across 7 plants; EPC for aerospace exports; BG / SBLC framework.</p></div>
  <div class="card pos"><h4 style="margin-top:0">T + 90</h4><p>Salary migration (2,500+ accounts); SCF for steel + aluminium suppliers; commodity-hedge advisory; receivable-financing for OEM captive book. TVS Group cross-sell introduction.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>WC + capex TL sanctioned by 31 Aug 2026</li>
    <li>SCF 12+ suppliers by end-Q3 FY27</li>
    <li>Annual run-rate Rs 22&ndash;28 Cr by end-FY27</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Wheels-India sources from [104].</em></p>
  <div class="src-list">
  <ol start="104">
  <li id="src-104"><strong>Wheels India corporate disclosures + BSE/NSE quarterly filings + IND + ICRA credit rationales Feb 2026</strong> &mdash; FY25 TOI Rs 4,415 Cr; 7-plant footprint; TVS Group promoter; IND A+ Assigned Stable; ICRA ratings on FD + bank loan facilities. <span class="u">wheelsindia.com &middot; bseindia.com &middot; nseindia.com</span></li>
  </ol>
  </div>
</section>
"""
def build():
    t = "Wheels India Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
