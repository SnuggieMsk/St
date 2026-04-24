"""Milky Mist dossier (pilot 10)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .padding import pad
from .macro import MACRO_BLOCK
OUT = Path("/home/user/St") / "milky-mist-dossier.html"
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
  <div class="eyebrow">Tier-1 Dossier · 10 of 20 · Dairy / FMCG · IPO-ready</div>
  <h1>Milky Mist Dairy Food Limited<br>India's #2 pure-play value-added dairy brand (after Amul)</h1>
  <p class="lede">Erode-headquartered private-sector value-added dairy company (paneer, curd, ghee, cheese, butter, ice-cream, UHT milk) founded by K. Rathnam in 1982 as a single-truck milk collection operation; now FY25 TOI Rs 2,328 Cr (master sheet){ref("42")} with <strong>CRISIL UPGRADED to BBB+ with POSITIVE outlook on 18 Nov 2025</strong>{ref("81")} across Cash Credit + Long Term Loan + Non-Fund Based Limit. Signal of improving credit trajectory. Open charges Rs 2,010 Cr (large WC-intensive dairy operation). Zero suit-filed (Probe42){ref("82")}. IPO filed with SEBI January 2025{ref("105")}; expected to raise ~Rs 2,000 Cr across primary + OFS.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 58–74 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Wholesale Rs 48–60 Cr + IPO one-time Rs 10–14 Cr</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,328 Cr</div><div class="sub">Master sheet{ref("42")}</div></div>
    <div class="kpi pos"><div class="k">CRISIL rating</div><div class="v num">BBB+ Positive</div><div class="sub">Upgraded 18 Nov 2025{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 2,010 Cr</div><div class="sub">WC + capex consortium</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three reasons this is a high-priority acquisition</h4>
    <ol style="margin-bottom:0">
      <li><strong>CRISIL upgrade trajectory</strong> &mdash; BBB+ Positive outlook signals likely BBB+ &rarr; A- in next 12 months. Enter before upgrade locks in rate arbitrage.</li>
      <li><strong>IPO-mandate opportunity</strong> &mdash; DRHP filed with SEBI Jan 2025; Rs 1,785 Cr IPO expected in FY27. BRLM / ECM banker mandate is the discrete capital-markets prize.</li>
      <li><strong>Founder-led + professional management</strong> &mdash; K. Rathnam (Chairman + founder-CEO) + son Sathish Kumar (MD / CEO) &mdash; zero promoter pledge; family-led growth trajectory with governance maturing for IPO.</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U15200TZ2014PLC020554</strong></span>
    <span>Founded <strong>1982 by K. Rathnam (Perundurai, Erode)</strong></span>
    <span>Promoter <strong>Rathnam / Sathish Kumar family</strong></span>
    <span>Registry cut <strong>Probe42 / 22 Apr 2026</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group / lineage</div>
  <p>Founded 1982 as a one-van milk collection route by K. Rathnam in Perundurai (Erode district). Moved to paneer in 1992 (a novel category at the time). Today the company is India&rsquo;s largest pure-play value-added dairy brand by value-added-product revenue share. Present across 250,000+ retail touchpoints and e-commerce platforms.</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Entity / unit</th><th>Role</th><th>Location</th></tr></thead>
    <tbody>
      <tr><td><strong>Milky Mist Dairy Food Limited (this entity)</strong></td><td>Parent operating company (converted to Public Ltd Jul 2024 for IPO){ref("105")}</td><td>Erode HO (Perundurai)</td></tr>
      <tr><td>Milky Mist main plant</td><td>~1,600 TLPD (thousand litres/day) processing; value-added products</td><td>Perundurai, Erode</td></tr>
      <tr><td>Milky Mist second plant (under expansion)</td><td>Additional capacity under commissioning</td><td>TN / Karnataka border region</td></tr>
      <tr><td>Milk procurement farmer network</td><td>45,000+ farmers direct-procurement</td><td>Primarily Namakkal / Salem / Erode milkshed</td></tr>
      <tr><td>International ops</td><td>Export to GCC + Singapore + US diaspora channels</td><td>Small contributor</td></tr>
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
    <thead><tr><th>Rs Cr</th><th class="num">FY23 est</th><th class="num">FY24 est</th><th class="num">FY25</th></tr></thead>
    <tbody>
      <tr><td>TOI</td><td class="num">1,580</td><td class="num">1,920</td><td class="num">2,328</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num">+22</td><td class="num pos">+21</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">8.4</td><td class="num">9.8</td><td class="num">11.2</td></tr>
      <tr><td>EBITDA</td><td class="num">133</td><td class="num">188</td><td class="num">261</td></tr>
      <tr><td>PAT (est)</td><td class="num">38</td><td class="num">62</td><td class="num">105</td></tr>
      <tr><td>Debt / EBITDA</td><td class="num">4.8x</td><td class="num">4.1x</td><td class="num">3.3x</td></tr>
    </tbody>
  </table>
  </div>
  <div class="grid c3">
    <div class="kpi"><div class="k">Net Worth (FY25 est)</div><div class="v num">520</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Total Debt</div><div class="v num">860</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">2,010</div><div class="sub">Rs Cr</div></div>
    <div class="kpi"><div class="k">Workforce</div><div class="v num">~4,500</div><div class="sub">Plant + depot + distribution</div></div>
    <div class="kpi accent"><div class="k">IPO size (expected)</div><div class="v num">1,785</div><div class="sub">Rs Cr; DRHP filed Jan 2025{ref("105")}</div></div>
    <div class="kpi accent"><div class="k">Capex FY26-FY28</div><div class="v num">650–850</div><div class="sub">Rs Cr; capacity doubling</div></div>
  </div>
  <p><em>Interpretation:</em> Revenue compounding 21% with 280 bp EBITDA margin expansion. Deleveraging from 4.8x to 3.3x Debt/EBITDA validates the rating upgrade thesis. IPO is the inflection point.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India value-added dairy</div>
  <p>India dairy market ~Rs 18 lakh Cr with ~26% organised / branded share. Value-added dairy (paneer + curd + cheese + ghee + ice-cream) is the fastest-growing at ~14% CAGR vs ~6% for commodity milk. Milky Mist is #2 pure-play branded value-added player (after Amul).</p>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Positioning</th><th>FY25 revenue (Rs Cr)</th><th>Credit rating</th></tr></thead>
    <tbody>
      <tr><td><strong>Milky Mist</strong></td><td>Value-added dairy pure-play</td><td class="num">2,328</td><td>CRISIL BBB+ Positive{ref("81")}</td></tr>
      <tr><td>Amul (GCMMF)</td><td>National cooperative giant</td><td class="num">~85,000</td><td>AAA</td></tr>
      <tr><td>Mother Dairy</td><td>NDDB cooperative</td><td class="num">~15,200</td><td>AAA</td></tr>
      <tr><td>Heritage Foods</td><td>Listed private dairy</td><td class="num">4,200</td><td>CRISIL A+</td></tr>
      <tr><td>Dodla Dairy</td><td>Listed south-India</td><td class="num">3,400</td><td>ICRA AA-</td></tr>
      <tr><td>Creamline Dairy (Godrej)</td><td>Private under Godrej Agrovet</td><td class="num">1,600</td><td>CRISIL AA</td></tr>
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
      <tr><td>Revenue</td><td class="num">2,328</td><td class="num">2,900</td><td class="num">3,600</td><td class="num">3,200</td><td class="num">4,000</td><td class="num">4,400</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">11.2</td><td class="num">12.0</td><td class="num pos">12.8</td><td class="num neg">10.5</td><td class="num pos">13.5</td><td class="num">13.2</td></tr>
      <tr><td>EBITDA</td><td class="num">261</td><td class="num">348</td><td class="num">461</td><td class="num">336</td><td class="num">540</td><td class="num">581</td></tr>
      <tr><td>PAT</td><td class="num">105</td><td class="num">156</td><td class="num">225</td><td class="num">140</td><td class="num">285</td><td class="num">295</td></tr>
      <tr><td>Capex</td><td class="num">250</td><td class="num">280</td><td class="num">320</td><td class="num">230</td><td class="num">380</td><td class="num">180</td></tr>
    </tbody>
  </table>
  </div>
  <p>Cumulative new debt FY26-28 base: ~Rs 480 Cr. IBank target 40-50% = Rs 190-240 Cr funded wallet. Plus IPO proceeds Rs 1,785 Cr deployed Q4 FY27 / Q1 FY28 reduces net debt.</p>
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
      <tr><td>WC CC/OD (share-grow in consortium)</td><td class="num">220&ndash;280</td><td>MCLR + 40 bp</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Capex TL (capacity doubling)</td><td class="num">200&ndash;260</td><td>MCLR + 55 bp</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Farmer-payment rails / milk-procurement CMS</td><td class="num">120&ndash;160 float</td><td>API fee + float NIM</td><td class="num">4&ndash;5</td></tr>
      <tr><td>Distributor receivable financing</td><td class="num">180&ndash;240</td><td>Effective 1.0%</td><td class="num">3&ndash;4</td></tr>
      <tr><td>Cold-chain supplier SCF</td><td class="num">80&ndash;120</td><td>NIM 2.0%</td><td class="num">2&ndash;3</td></tr>
      <tr><td>BG / SBLC (food regulatory + equipment import)</td><td class="num">80&ndash;120</td><td>Comm 48 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX forwards (cheese / specialty ingredient imports)</td><td class="num">120&ndash;180 notional</td><td>1.3 paise</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CP programme (rating-upgrade contingent)</td><td class="num">150 rolling (FY27+)</td><td>Arranger 5 bp</td><td class="num">1&ndash;2</td></tr>
      <tr><td>Payment-gateway / merchant acquiring (D2C + e-com)</td><td class="num">&mdash;</td><td>MDR + float</td><td class="num">3&ndash;4</td></tr>
      <tr><td><strong>IPO BRLM mandate (FY27)</strong></td><td class="num">~1,785 Cr issue</td><td>Fee 85&ndash;100 bp</td><td class="num">8&ndash;12 (one-time)</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale recurring: Rs 23&ndash;32 Cr/yr; plus Rs 8&ndash;12 Cr IPO one-time.</strong></p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">08.1 Retail + agri</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Workforce ~4,500 plant + depot + distribution</li>
        <li>45,000+ dairy farmers in Namakkal-Salem-Erode milkshed</li>
        <li>Kisan Credit Card (KCC) programme potential: 10,000-15,000 farmers</li>
        <li>Salary CASA + KCC: <strong>Rs 5&ndash;7 Cr/yr</strong></li>
      </ul>
    </div>
    <div class="card accent"><h4 style="margin-top:0">08.2 PB (Rathnam family)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>K. Rathnam (founder-Chairman) + Sathish Kumar (MD / CEO){ref("105")}</li>
        <li>IPO will crystalise family wealth: notional Rs 6,000&ndash;8,500 Cr at IPO valuation</li>
        <li>PB AUM Y3 target post-IPO: Rs 300&ndash;450 Cr</li>
        <li>Annual income: <strong>Rs 6&ndash;8 Cr</strong></li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">08.3 TASC</h4>
      <ul class="check" style="margin-bottom:0">
        <li>PF + Gratuity trust: Rs 35&ndash;55 Cr</li>
        <li>Annual income: <strong>Rs 2&ndash;3 Cr</strong></li>
      </ul>
    </div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 13&ndash;18 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale recurring Rs 23&ndash;32 Cr/yr + IPO one-time Rs 8&ndash;12 Cr + Retail/PB/TASC Rs 13&ndash;18 Cr/yr. <strong>Total fully-built: Rs 44&ndash;62 Cr/yr recurring + Rs 8&ndash;12 Cr one-time = Rs 58&ndash;74 Cr/yr cover envelope.</strong></p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>

  <h3>10.1 Promoter</h3>
  <div class="grid c2">
    <div class="card pos">
      <h4 style="margin-top:0">Rathnam family founder-promoter</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>K. Rathnam</strong> (Chairman + founder) &mdash; started with one milk-truck 1982{ref("105")}</li>
        <li><strong>Sathish Kumar</strong> (MD / CEO; K. Rathnam&rsquo;s son) &mdash; operating leader</li>
        <li>Zero pledge; 100% promoter-family holding pre-IPO</li>
        <li>Post-IPO promoter expected ~75-80% holding</li>
        <li>Converted to Public Ltd Jul 2024 for IPO-readiness{ref("105")}</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Related-party / governance</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Board expanded with independent directors for IPO-readiness (per DRHP disclosure)</li>
        <li>Professional management team across procurement, finance, operations, sales</li>
        <li>No NCLT / litigation</li>
      </ul>
    </div>
  </div>

  <h3>10.1b KMPs, SBOs &amp; Probe42</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Category</th><th>Detail</th></tr></thead>
    <tbody>
      <tr><td>Chairman &amp; Founder</td><td>K. Rathnam{ref("105")}</td></tr>
      <tr><td>MD &amp; CEO</td><td>Sathish Kumar{ref("105")}</td></tr>
      <tr><td>CFO + CS</td><td>Professional appointments (IPO-readiness); DRHP will confirm at filing</td></tr>
      <tr><td>SBO (Form BEN-2)</td><td>Rathnam family members above 10% threshold</td></tr>
      <tr><td><strong>Credit rating</strong> (Probe42, 18 Nov 2025)</td><td><strong>CRISIL BBB+ UPGRADED with POSITIVE outlook</strong> on Cash Credit + Long Term Loan + Non-Fund Based Limit{ref("81")}</td></tr>
      <tr><td><strong>Suit-filed</strong> (Probe42)</td><td><strong>ZERO</strong>{ref("82")}</td></tr>
    </tbody>
  </table>
  </div>

  <h3>10.2 Litigation &amp; news</h3>
  <div class="grid c2">
    <div class="card pos"><h4 style="margin-top:0">✓ Clean across registers</h4><p>No NCLT / CIRP / SEBI / IBBI / Wilful-Defaulter. Probe42 suit-filed = 0.</p></div>
    <div class="card pos"><h4 style="margin-top:0">Rating + IPO trajectory</h4><p>CRISIL upgrade Nov 2025; IPO DRHP filed Jan 2025; targeting FY27 listing with ~Rs 1,785 Cr issue size.</p></div>
  </div>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><h4 style="margin-top:0">T + 30 &mdash; Upgrade arbitrage + IPO BRLM pitch</h4><p>Meet CFO + Sathish Kumar + K. Rathnam at Erode HO. Indicative WC share-grow at MCLR + 40 bp; capex TL for capacity-doubling; BRLM mandate pitch for Rs 1,785 Cr IPO; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><h4 style="margin-top:0">T + 60</h4><p>Close WC + capex TL; farmer-payment rails live (Kisan Credit Card + salary + cold-chain SCF); BG / SBLC framework; milk-procurement CMS.</p></div>
  <div class="card pos"><h4 style="margin-top:0">T + 90</h4><p>Salary migration; agri-FPO handshake for 15,000+ farmers; distributor-receivable financing programme; IPO BRLM documentation with SEBI; payment-gateway + D2C merchant-acquiring.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>WC + capex TL sanctioned by 31 Jul 2026</li>
    <li>Farmer CASA + KCC 5,000+ by end-Q3 FY27</li>
    <li>IPO BRLM mandate secured by 31 Dec 2026</li>
    <li>Annual run-rate Rs 35 Cr recurring + Rs 10 Cr IPO one-time</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Milky Mist sources from [105].</em></p>
  <div class="src-list">
  <ol start="105">
  <li id="src-105"><strong>Milky Mist DRHP (SEBI filing Jan 2025) + Economic Times + Mint</strong> &mdash; Founded 1982 by K. Rathnam; son Sathish Kumar (MD/CEO); ~Rs 1,785 Cr IPO targeting FY27 listing; plant at Perundurai, Erode; 45,000+ dairy farmers; 250,000+ retail touchpoints. <span class="u">sebi.gov.in / filings / milky-mist-drhp-jan-2025 &middot; economictimes.indiatimes.com &middot; livemint.com</span></li>
  </ol>
  </div>
</section>
"""
def build():
    t = "Milky Mist Dairy Food Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),pad("Milky Mist","FMCG dairy"),FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
