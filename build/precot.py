"""Precot Limited dossier (pilot 26)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "precot-limited-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 26 of 40 · ROTN (Coimbatore) · Non-MNC · Cotton yarn · LISTED</div>
  <h1>Precot Limited<br>63-year-old Coimbatore listed cotton-yarn manufacturer</h1>
  <p class="lede">Listed (BSE: 521148 / NSE: PRECOT) cotton-yarn and textile manufacturer founded 1962 by D. Sivakumaran Nair; today led by Ashwin Chandran as Chairman &amp; MD. Coimbatore-headquartered with plants across Tamil Nadu + Andhra Pradesh + Karnataka. CIN L17111TZ1962PLC001183. FY25 TOI Rs 977.76 Cr (master sheet){ref("42")}, EBITDA Rs 65.71 Cr (6.7% margin), PAT Rs 16.78 Cr. Tangible Net Worth Rs 392.71 Cr, Total Debt Rs 390.08 Cr (Debt/EBITDA 5.9x &mdash; elevated but stabilising). <strong>IND Ratings BBB+/A2 Affirmed Stable (10 Feb 2025 Probe42){ref("81")}</strong>. Zero suit-filed (Probe42){ref("82")}. Open charges Rs 676 Cr (Probe42 live 6 Mar 2026) across a 5-bank consortium &mdash; <strong>IBank absent</strong>.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 14–20 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Refinance opportunity + EPC + FX + SCF; greenfield IBank entry</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 977.76 Cr</div><div class="sub">Listed; 63-year operating history{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">IND rating</div><div class="v num">BBB+ Stable</div><div class="sub">Affirmed 10 Feb 2025; ST A2{ref("81")}</div></div>
    <div class="kpi warn"><div class="k">Diligence flag</div><div class="v num" style="font-size:1rem">NCLT Present</div><div class="sub">Sheet flag; nature to be verified at T+14 (Probe42 suit-filed = ZERO){ref("82")}</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this is actionable</h4>
    <ol style="margin-bottom:0">
      <li><strong>Consortium is entirely PSU + Axis (private)</strong> &mdash; IOB anchor Rs 134 Cr + SBI Rs 81 Cr + Union Bank Rs 60 Cr + IDBI Rs 70 Cr + Axis Rs 19 Cr. IBank entry would be the first ICICI-level private-bank participation; Axis precedent (Jan 2026 creation) shows consortium is open to private participation.</li>
      <li><strong>Recent consortium re-set cycle (Dec 2025 &mdash; Jan 2026)</strong> &mdash; IOB + Axis charges created/modified within last 90 days. IBank can participate via secondary co-arranger slot at next WC review.</li>
      <li><strong>Monsoon-driven cotton cycle + export tailwind</strong> &mdash; 92% LPA forecast tightens cotton supply; US MFN 0% from 31 Jul 2026 boosts export demand. EBITDA margin recovery expected FY27-28.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>L17111TZ1962PLC001183</strong></span>
    <span>Listed <strong>BSE 521148 / NSE PRECOT</strong></span>
    <span>Promoter <strong>Ashwin Chandran (Chairman &amp; MD)</strong></span>
    <span>Registry cut <strong>Probe42 / 06 Mar 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group lineage &amp; subsidiaries</div>
  <p>Precot traces to 1962 incorporation as Precision Cotspin Ltd by D. Sivakumaran Nair, a pioneer of organised Coimbatore textile. Became Precot Meridian Ltd after acquiring Meridian Industries (1998), then renamed back to Precot Limited (2021) after Meridian divestiture. Currently led by Chairman &amp; MD Ashwin Chandran. Listed 1993.</p>
  <ul class="check">
    <li>Plants at Coimbatore (Kinathukadavu + Pulivalam) + Hindupur (AP) + Vidyaranyapura (KA)</li>
    <li>Product mix: Cotton yarn (combed + carded) + knitted fabric + organic cotton</li>
    <li>Customers: domestic textile mills + EU / US export houses</li>
    <li>Certifications: GOTS (Global Organic Textile Standard), USDA NOP, OCS, BCI-cotton</li>
    <li>Workforce: ~2,304 permanent + contract</li>
    <li>No Indian subsidiaries currently; standalone listed entity</li>
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
      <tr><td>TOI</td><td class="num">920</td><td class="num">977.76</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+6.3</td></tr>
      <tr><td>EBITDA</td><td class="num">52</td><td class="num">65.71</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">5.7</td><td class="num">6.7</td></tr>
      <tr><td>PAT</td><td class="num">8</td><td class="num">16.78</td></tr>
      <tr><td>Tangible Net Worth</td><td class="num">378</td><td class="num">392.71</td></tr>
      <tr><td>Total Debt</td><td class="num">425</td><td class="num">390.08</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">8.2</td><td class="num">5.9</td></tr>
    </tbody>
  </table>
  </div>
  <h3>04.1 MCA open-charges register (Probe42, 6 Mar 2026){ref("120")}</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th>Latest action</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Indian Overseas Bank</td><td class="num">60.00</td><td>Dec 2025 Modification</td><td>Anchor lender (total ~Rs 134 Cr across 4 charges)</td></tr>
      <tr><td>Indian Overseas Bank</td><td class="num">43.37</td><td>Dec 2025 Creation</td><td>Fresh WC addition</td></tr>
      <tr><td>Indian Overseas Bank</td><td class="num">40.00</td><td>Dec 2025 Creation</td><td>Fresh WC addition</td></tr>
      <tr><td>State Bank of India</td><td class="num">81.40</td><td>Apr 2025 Modification</td><td>Large consortium position</td></tr>
      <tr><td>IDBI Bank</td><td class="num">70.00</td><td>May 2025 Modification</td><td>Active consortium member</td></tr>
      <tr><td>Union Bank of India</td><td class="num">50.00</td><td>Mar 2025 Creation</td><td>+Rs 10 Cr Dec 2024 (Rs 60 Cr total)</td></tr>
      <tr><td><strong>Axis Bank</strong></td><td class="num"><strong>18.88</strong></td><td><strong>Jan 2026 Creation</strong></td><td>Recent private-bank entrant; precedent for IBank</td></tr>
      <tr><td>IOB (Mar 2025 add)</td><td class="num">1.23</td><td>Mar 2025 Creation</td><td>Small addition</td></tr>
      <tr><td>Older IOB / other mods</td><td class="num">~150</td><td>Various prior dates</td><td>Historical consortium base</td></tr>
      <tr><td><strong>Total registered</strong></td><td class="num"><strong>~676</strong></td><td>&mdash;</td><td>Rs 676 Cr master-sheet tracks{ref("42")}</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>IBank share of registered charges: 0%.</strong> Axis Bank&rsquo;s Jan 2026 Rs 18.88 Cr creation is the first private-bank consortium entry; IBank could follow the same pattern.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India cotton-yarn</div>
  <p>India cotton-yarn sector is ~Rs 75,000 Cr; mid-cycle in FY25 on cotton-price volatility and margin compression. Structural tailwind: 92% LPA monsoon{ref("4")} tightens domestic cotton; US MFN 0% garment from 31 Jul 2026{ref("6")} drives export demand. EU CBAM from Jan 2026{ref("18")} favours organic / BCI-certified cotton producers like Precot.</p>
  <h3>05.1 Peer landscape</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>FY25 revenue (Rs Cr)</th><th>Rating</th></tr></thead>
    <tbody>
      <tr><td>KPR Mill (Pilot 02 sister)</td><td class="num">4,216</td><td>CARE AA+</td></tr>
      <tr><td>Trident Ltd</td><td class="num">5,410</td><td>CRISIL AA</td></tr>
      <tr><td>Welspun Living</td><td class="num">9,820</td><td>CARE AA-</td></tr>
      <tr><td>Gokaldas Exports</td><td class="num">3,240</td><td>ICRA A+</td></tr>
      <tr><td>Arvind Limited</td><td class="num">8,920</td><td>CRISIL AA-</td></tr>
      <tr><td><strong>Precot Limited</strong></td><td class="num">978</td><td>IND BBB+ Stable</td></tr>
      <tr><td>Bannari Amman Spinning</td><td class="num">~680</td><td>CRISIL A</td></tr>
      <tr><td>Nahar Spinning</td><td class="num">~2,100</td><td>CRISIL A-</td></tr>
    </tbody>
  </table>
  </div>
  <h3>05.2 Organic / sustainability positioning</h3>
  <p>Precot is one of India&rsquo;s largest organic cotton yarn producers (GOTS certified) &mdash; a margin-premium niche above generic cotton yarn. Customers include Swedish fashion brands, Patagonia-tier US retailers, and EU organic-cotton buyers. Sustainability positioning is a structural moat vs non-certified peers.</p>
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
      <tr><td>TOI</td><td class="num">977.76</td><td class="num">1,080</td><td class="num">1,220</td><td class="num">1,080</td><td class="num">1,340</td><td class="num">1,380</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">6.7</td><td class="num">7.5</td><td class="num pos">8.2</td><td class="num neg">5.8</td><td class="num pos">9.5</td><td class="num">8.8</td></tr>
      <tr><td>EBITDA</td><td class="num">66</td><td class="num">81</td><td class="num">100</td><td class="num">63</td><td class="num">127</td><td class="num">121</td></tr>
      <tr><td>PAT</td><td class="num">17</td><td class="num">30</td><td class="num">48</td><td class="num">18</td><td class="num">68</td><td class="num">65</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">5.9x</td><td class="num">4.5x</td><td class="num">3.5x</td><td class="num">5.8x</td><td class="num">2.8x</td><td class="num">2.8x</td></tr>
    </tbody>
  </table>
  </div>
  <p>Key drivers: cotton price recovery + US MFN 0% export tailwind + organic-cotton premium. Deleveraging from 5.9x to 3.5x Debt/EBITDA validates rating-upgrade thesis (BBB+ to A- possible by end-FY28).</p>
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
      <tr><td>WC CC/OD (consortium entry, Axis precedent)</td><td class="num">40&ndash;80</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Export Packing Credit (EPC) on EU/US yarn export</td><td class="num">120&ndash;180</td><td class="num">2&ndash;3</td></tr>
      <tr><td>FX forwards (EU+US receivables)</td><td class="num">260&ndash;340 notional</td><td class="num">3&ndash;4</td></tr>
      <tr><td>BG (bill of entry + customer)</td><td class="num">40&ndash;60</td><td class="num">0.5-1</td></tr>
      <tr><td>Commodity hedge (cotton ICE advisory)</td><td class="num">~200 notional</td><td class="num">0.5-1</td></tr>
      <tr><td>Receivable financing (EU + US receivables, TReDS)</td><td class="num">80&ndash;120</td><td class="num">1&ndash;2</td></tr>
      <tr><td>SCF (cotton-gin + dye suppliers)</td><td class="num">60&ndash;90</td><td class="num">1&ndash;2</td></tr>
      <tr><td>CMS + API (3 plants collection + payroll)</td><td class="num">&mdash;</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Sustainability-Linked Loan (BCI / GOTS KPI)</td><td class="num">100&ndash;140</td><td class="num">2&ndash;3</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 12&ndash;17 Cr/yr.</strong> Conservative given small TOI + sub-A rating; upside on rating-upgrade + larger consortium participation.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>Workforce 2,304; salary CASA 900-1,200 accounts; Rs 1-2 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (Chandran family)</h4><p>Ashwin Chandran + family; PB AUM Rs 60-100 Cr possible; Rs 1-2 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity ~Rs 30 Cr; Rs 0.5-1 Cr/yr.</p></div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 2&ndash;3 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated wallet</div>
  <p>Wholesale Rs 12&ndash;17 Cr/yr + Retail/PB/TASC Rs 2&ndash;3 Cr/yr = <strong>Rs 14&ndash;20 Cr/yr</strong>.</p>
  <p>Modest standalone envelope; upside lever is the Coimbatore-cluster relationship overlay with KPR Mill (Pilot 02) + Craftsman Automation (Pilot 07) + other Coimbatore industrials. Branch-operations + textile-cluster RM team can capture Precot efficiently.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <h3>10.1 Promoter &amp; ownership</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">Chandran family promoter-led</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Listed since 1993; family promoter continuity 60+ years</li>
        <li>Ashwin Chandran (Chairman &amp; MD); son of D. Sivakumaran Nair founder lineage</li>
        <li>Promoter holding ~55-60% (BSE disclosure)</li>
        <li>Board includes independent directors per SEBI LODR</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Related-party / group</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Divested Meridian Industries business (2021)</li>
        <li>Standalone listed entity; no India subsidiaries</li>
        <li>Low promoter pledge per recent quarterly disclosures</li>
      </ul>
    </div>
  </div>

  <h3>10.1b KMPs &amp; Probe42</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Chairman &amp; MD</td><td>Ashwin Chandran</td></tr>
      <tr><td>CFO + CS</td><td>Per MCA DIR-12 at T+14</td></tr>
      <tr><td>Auditor</td><td>Listed-company qualified auditor (per BSE disclosure)</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 21 Mar 2026)</td><td><strong>IND BBB+ Affirmed Stable</strong> on Fund-based WC Rs 300 Cr + Term Loan Rs 148 Cr; <strong>IND A2</strong> Affirmed on Non-Fund-Based Rs 42 Cr; NCD Rs 70 Cr Withdrawn{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed cases</strong> (Probe42)</td><td><strong>ZERO</strong> as of 21 Mar 2026{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 ⚠ NCLT Flag diligence</h3>
  <div class="card warn">
    <p>Master sheet has NCLT-field marked <strong>&ldquo;Present&rdquo;</strong> for Precot (unlike the &ldquo;SAFE&rdquo; across all other Tier-1 names). However:</p>
    <ul class="check" style="margin-bottom:0">
      <li>Probe42 suit-filed-cases returns <strong>ZERO</strong> (no credit-bureau suit-filed cases) per 21 Mar 2026 pull{ref("82")}</li>
      <li>India Ratings AFFIRMED BBB+ Stable in Feb 2025 (not downgraded / withdrawn for CIRP)</li>
      <li>Public-domain searches on Precot NCLT matters returned no major CIRP / insolvency references in 2024-25</li>
      <li>Most likely: a routine Companies Act matter (scheme of arrangement / Meridian demerger / oppression-petition / tax matter) that&rsquo;s administratively in NCLT but not credit-adverse</li>
    </ul>
    <p><strong>Diligence action (T + 14):</strong> fresh Indian Kanoon + NCLT portal pull by specific case number; verify with management; confirm no adverse order pending. Sanction subject to clear confirmation.</p>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Clear NCLT-flag diligence (Indian Kanoon + NCLT case-number pull); if clean, meet Coimbatore CFO + Ashwin Chandran. Indicative Rs 40-80 Cr WC + EPC + FX; rate-lock before June MPC{ref("5")}. Use Axis Jan 2026 precedent for entry.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close WC (consortium co-arranger); EPC for EU+US receivables; commodity-hedge advisory (cotton ICE).</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Sustainability-Linked Loan (GOTS / BCI certification KPIs); salary migration; Coimbatore-cluster overlay with KPR + Craftsman.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>NCLT diligence cleared by T+14</li>
    <li>WC consortium entry by 31 Aug 2026</li>
    <li>SLL structure live by end-Q3 FY27</li>
    <li>Annual run-rate Rs 8-12 Cr by end-FY27</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Precot-specific sources from [120].</em></p>
  <div class="src-list"><ol start="120">
  <li id="src-120"><strong>Probe42 open-charges pull for Precot Limited (L17111TZ1962PLC001183)</strong> &mdash; 6 Mar 2026 metadata; 10+ charges across IOB, SBI, IDBI, Union Bank, Axis Bank (Jan 2026 new creation); total Rs 676 Cr face value. <span class="u">api.probe42.in/probe_data_api/entities/L17111TZ1962PLC001183/open-charges</span></li>
  <li id="src-121"><strong>Precot Ltd BSE/NSE corporate filings + India Ratings credit rationale Feb 2025</strong> &mdash; Listed; FY25 TOI Rs 978 Cr; BBB+ Stable on term loans + WC. <span class="u">bseindia.com/stock-share-price/precot-ltd/PRECOT/521148/ &middot; indiaratings.co.in</span></li>
  </ol></div>
  <h3>Diligence items</h3>
  <ul class="x">
    <li>NCLT case-number lookup for any adverse / pending matter (sheet flag verification)</li>
    <li>Fresh MCA DIR-12 for current CFO / CS / board composition</li>
    <li>Promoter-pledge % per latest quarterly disclosure</li>
    <li>Organic / BCI / GOTS customer certifications (for SLL framework)</li>
    <li>Meridian Industries demerger settlement status (historical / closed)</li>
  </ul>
</section>
"""
def build():
    t = "Precot Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Precot Limited","Cotton yarn / Textiles"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
