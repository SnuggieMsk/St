"""Mohanlal Jewellers dossier (pilot 27)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad
OUT = Path("/home/user/St") / "mohanlal-jewellers-dossier.html"
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
  <div class="eyebrow">Tier-2 Dossier · 27 of 40 · Chennai · Non-MNC · Jewellery retail · Speculative-grade</div>
  <h1>Mohanlal Jewellers Private Limited<br>Chennai-headquartered jewellery retailer (family-led)</h1>
  <p class="lede">Family-owned unlisted gold + silver + diamond jewellery retailer operating across South India, brand-equity concentrated in Chennai-Pondicherry belt. CIN U28999TN2009PTC071334. Industry classification Retail per master sheet. FY25 TOI Rs 7,023 Cr (master sheet){ref("42")} &mdash; one of the largest single-entity jewellery revenues in the universe &mdash; but <strong>EBITDA margin only 0.92%</strong> (typical of gold-retail) with EBITDA Rs 64.52 Cr. PAT Rs 39.52 Cr. Open charges Rs 593 Cr; Total Debt Rs 175 Cr (primarily gold-lease). <strong>IND Ratings BB+/A4+</strong> &mdash; speculative grade (HY bucket); reflects thin margin + promoter-family-private structure.</p>
  <div class="grid c4" style="margin-top:18px">
    <div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22–32 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Metal-lease + gold-lease + retail CASA</div></div>
    <div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 7,023 Cr</div><div class="sub">Very high absolute revenue (gold pass-through)</div></div>
    <div class="kpi warn"><div class="k">IND rating</div><div class="v num">BB+ / A4+</div><div class="sub">Speculative grade; HY bucket{ref("81")}</div></div>
    <div class="kpi"><div class="k">Open Charges</div><div class="v num">Rs 593 Cr</div><div class="sub">Gold-lease + WC consortium</div></div>
  </div>
  <div class="card accent" style="margin-top:20px">
    <h4 style="margin-top:0">Three angles</h4>
    <ol style="margin-bottom:0">
      <li><strong>Metal-lease economics is the real product</strong> &mdash; gold-lease is the highest-economic product for jewellery retailers; structured NIM + fee combo</li>
      <li><strong>Payment-gateway + consumer UPI rails</strong> &mdash; Rs 7,000+ Cr transaction flow at retail point-of-sale; merchant-acquiring opportunity</li>
      <li><strong>Family-promoter PB</strong> &mdash; private jewellery entrepreneurs typically hold significant liquid wealth; family-office PB angle</li>
    </ol>
  </div>
  <div class="meta" style="margin-top:14px">
    <span>CIN <strong>U28999TN2009PTC071334</strong></span>
    <span>Sector <strong>Retail / Jewellery</strong></span>
    <span>Listing <strong>Unlisted (private family-owned)</strong></span>
    <span>Registry cut <strong>Probe42 / TBD</strong></span>
  </div>
</section>
"""
def S2():
    return f"""
<section id="group">
  <div class="subhead">03 · Group / positioning</div>
  <p>Mohanlal Jewellers is a private family-owned jewellery retailer, incorporated 2009 but with significantly older retail heritage (Chennai jewellery market roots). Operates branded retail stores + private-label gold, silver, and diamond jewellery. Strong regional brand in Chennai / Pondicherry / coastal TN. Revenue scale (Rs 7,000+ Cr) places it among top-10 organised jewellery retailers in India despite unlisted status.</p>
  <ul class="check">
    <li>Family-led promoter structure (specific family identity per MCA DIR-12)</li>
    <li>Chennai-headquartered; retail footprint primarily Tamil Nadu + select south India</li>
    <li>Product mix: 22k gold + 18k diamond jewellery + silver + custom-design orders</li>
    <li>Customer mix: wedding-jewellery heavy (~55% of revenue; seasonal Mar-May + Oct-Dec peaks)</li>
    <li>Workforce: 94 on-rolls per MCA + retail-floor staff on third-party contract</li>
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
      <tr><td>TOI</td><td class="num">5,900</td><td class="num">7,023</td></tr>
      <tr><td>YoY %</td><td class="num">-</td><td class="num pos">+19 (gold volume + price)</td></tr>
      <tr><td>EBITDA</td><td class="num">52</td><td class="num">64.52</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">0.88</td><td class="num">0.92</td></tr>
      <tr><td>PAT</td><td class="num">32</td><td class="num">39.52</td></tr>
      <tr><td>Tangible Net Worth</td><td class="num">262</td><td class="num">280.99</td></tr>
      <tr><td>Total Debt</td><td class="num">158</td><td class="num">174.82</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">3.04</td><td class="num">2.71</td></tr>
    </tbody>
  </table>
  </div>
  <p><em>Margin context:</em> jewellery-retail typically has 0.5-1.5% EBITDA margin because gold revenue is largely pass-through. The meaningful profitability lever is design premium + making charges. Mohanlal&rsquo;s 0.92% is industry-standard.</p>
</section>
"""
def S4():
    return f"""
<section id="industry">
  <div class="subhead">05 · Industry &mdash; India organised jewellery retail</div>
  <p>India jewellery market Rs 6.8 lakh Cr; organised share ~35% growing to 50% by FY28 (see CaratLane dossier Sec 05 for full industry treatment). Unorganised-to-organised shift + BIS hallmarking (mandatory since 2023) structurally favour chains like Mohanlal.</p>
  <h3>05.1 Peer positioning</h3>
  <div style="overflow-x:auto">
  <table>
    <thead><tr><th>Peer</th><th>Positioning</th><th>FY25 revenue (Rs Cr)</th><th>Listing</th></tr></thead>
    <tbody>
      <tr><td>Tanishq (Titan division)</td><td>National premium</td><td class="num">~46,000</td><td>Titan listed</td></tr>
      <tr><td>Malabar Gold</td><td>National; #1 by stores</td><td class="num">~55,000 (global)</td><td>Private</td></tr>
      <tr><td>Kalyan Jewellers</td><td>Pan-India national</td><td class="num">18,500</td><td>Listed</td></tr>
      <tr><td>Joyalukkas</td><td>Premium pan-India</td><td class="num">~15,800</td><td>Private</td></tr>
      <tr><td><strong>Mohanlal Jewellers</strong></td><td>Chennai / TN regional</td><td class="num">7,023</td><td>Private</td></tr>
      <tr><td>Senco Gold</td><td>East India + pan-India</td><td class="num">5,200</td><td>Listed</td></tr>
      <tr><td>CaratLane (Pilot 06)</td><td>Online / omni-channel</td><td class="num">3,583</td><td>Titan subsidiary</td></tr>
      <tr><td>Thangamayil</td><td>TN regional</td><td class="num">~3,800</td><td>Listed</td></tr>
    </tbody>
  </table>
  </div>
  <p>Mohanlal competes in the regional Chennai / Pondicherry / coastal-TN belt against Joyalukkas + Lalithaa Jewellery + Saravana Stores. Brand equity strong within that geographic corridor.</p>
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
      <tr><td>TOI</td><td class="num">7,023</td><td class="num">8,100</td><td class="num">9,200</td><td class="num">8,400</td><td class="num">10,100</td><td class="num">10,400</td></tr>
      <tr><td>EBITDA margin (%)</td><td class="num">0.92</td><td class="num">1.05</td><td class="num pos">1.20</td><td class="num neg">0.85</td><td class="num pos">1.35</td><td class="num">1.25</td></tr>
      <tr><td>EBITDA</td><td class="num">65</td><td class="num">85</td><td class="num">110</td><td class="num">71</td><td class="num">136</td><td class="num">130</td></tr>
      <tr><td>PAT</td><td class="num">40</td><td class="num">52</td><td class="num">68</td><td class="num">38</td><td class="num">90</td><td class="num">85</td></tr>
      <tr><td>Debt / EBITDA (x)</td><td class="num">2.71</td><td class="num">2.40</td><td class="num">2.10</td><td class="num">2.90</td><td class="num">1.70</td><td class="num">1.80</td></tr>
    </tbody>
  </table>
  </div>
  <p>Growth driven by gold price + festive / wedding volume. Margin improvement on making-charge mix + diamond premium. Rating step-up from BB+ to BBB- possible by end-FY28 on sustained deleveraging.</p>
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
      <tr><td><strong>Gold / metal-lease programme</strong> (jewellery anchor product)</td><td class="num">280&ndash;400</td><td class="num">6&ndash;9</td></tr>
      <tr><td>WC CC/OD (beyond metal-lease)</td><td class="num">80&ndash;120</td><td class="num">2&ndash;3</td></tr>
      <tr><td>BG (bullion + supplier + regulatory)</td><td class="num">120&ndash;160</td><td class="num">1&ndash;2</td></tr>
      <tr><td>FX forwards (diamond + stone imports)</td><td class="num">140&ndash;200 notional</td><td class="num">2&ndash;3</td></tr>
      <tr><td>Payment gateway + UPI merchant acquiring (Rs 7,000+ Cr transaction flow)</td><td class="num">&mdash;</td><td class="num">5&ndash;7</td></tr>
      <tr><td>Retail gold-loan origination (at-counter)</td><td class="num">80-140 annual flow</td><td class="num">2&ndash;3</td></tr>
      <tr><td>CMS + treasury</td><td class="num">&mdash;</td><td class="num">2&ndash;3</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Wholesale: Rs 20&ndash;30 Cr/yr.</strong> Metal-lease + payment-gateway are the top-2 economic products.</p>
</section>
"""
def S7():
    return f"""
<section id="retail">
  <div class="subhead">08 · Retail / PB / TASC</div>
  <div class="grid c3">
    <div class="card"><h4 style="margin-top:0">Retail</h4><p>94 HO employees + ~800-1,200 retail-floor staff (contract). Rs 0.8-1.2 Cr/yr.</p></div>
    <div class="card accent"><h4 style="margin-top:0">PB (promoter-family)</h4><p>Jewellery promoter families typically hold large liquid wealth (gold + investments). PB mandate potential Rs 80-150 Cr AUM; Rs 2-4 Cr/yr.</p></div>
    <div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity small; CSR compliance; Rs 0.3-0.5 Cr/yr.</p></div>
  </div>
  <div class="card accent"><h4 style="margin-top:0">Combined: Rs 3&ndash;6 Cr/yr</h4></div>
</section>
"""
def S8():
    return f"""
<section id="consolidated">
  <div class="subhead">09 · Consolidated</div>
  <p>Wholesale Rs 20&ndash;30 Cr/yr + Retail/PB/TASC Rs 3&ndash;6 Cr/yr = <strong>Rs 23&ndash;36 Cr/yr</strong>. Metal-lease is the anchor; payment-gateway + PB are the second-tier products.</p>
</section>
"""
def S9():
    return f"""
<section id="diligence">
  <div class="subhead">10 · Diligence</div>
  <div class="grid c2">
    <div class="card"><h4 style="margin-top:0">Ownership</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Private family-owned (100% promoter-family)</li>
        <li>No public filings beyond MCA; minimal disclosure visibility</li>
        <li>IND Ratings-covered only; no CARE / CRISIL / ICRA second rating</li>
      </ul>
    </div>
    <div class="card"><h4 style="margin-top:0">Diligence items (credit-committee)</h4>
      <ul class="check" style="margin-bottom:0">
        <li>Gold-lease counterparty relationships (likely bullion banks: Kotak / Axis / Indian Bank)</li>
        <li>Cash-handling / AML controls at retail points</li>
        <li>Promoter personal-guarantee structure for WC facility</li>
        <li>BIS hallmarking + 6-digit HUID compliance at all retail points</li>
        <li>Sheet lists 94 employees &mdash; HO only; need total head-count reconciliation</li>
      </ul>
    </div>
  </div>
  <h3>10.1 Probe42 (cached metadata Apr 2026)</h3>
  <ul class="check">
    <li>Suit-filed cases: to be verified at T+14 pull</li>
    <li>Credit rating: IND BB+ / A4+ (from sheet; live Probe42 refresh required)</li>
    <li>Open charges: Rs 593 Cr per sheet; Probe42 refresh to confirm composition</li>
  </ul>
</section>
"""
def S10():
    return f"""
<section id="playbook">
  <div class="subhead">11 · 30-60-90 playbook</div>
  <div class="card accent"><p><strong>T+30:</strong> Meet promoter-family + CFO; metal-lease programme pitch (anchor product); payment-gateway / UPI at-counter; rate-lock before June MPC{ref("5")}.</p></div>
  <div class="card"><p><strong>T+60:</strong> Close metal-lease Rs 280-400 Cr; WC CC/OD Rs 80-120 Cr; BG framework; diamond-import LC.</p></div>
  <div class="card pos"><p><strong>T+90:</strong> Payment-gateway go-live across all retail points; PB engagement promoter family; retail gold-loan origination programme.</p></div>
  <h3>Success metrics</h3>
  <ul class="check">
    <li>Metal-lease live by 31 Aug 2026</li>
    <li>Payment-gateway at 15+ retail points by end-Q3 FY27</li>
    <li>PB AUM Rs 50+ Cr by end-FY27</li>
    <li>Annual run-rate Rs 14-18 Cr by end-FY27</li>
  </ul>
</section>
"""
def S11():
    return """
<section id="sources">
  <div class="subhead">12 · Sources</div>
  <p><em>Shared 1-22; Probe42 81-82. Mohanlal-specific sources from [122].</em></p>
  <div class="src-list"><ol start="122">
  <li id="src-122"><strong>Master Lead Generation sheet + MCA CIN U28999TN2009PTC071334 + India Ratings coverage</strong> &mdash; Chennai private jewellery retailer; FY25 TOI Rs 7,023 Cr; IND BB+/A4+ rating. <span class="u">mca.gov.in &middot; indiaratings.co.in</span></li>
  </ol></div>
</section>
"""
def build():
    t = "Mohanlal Jewellers Pvt Ltd · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),
           pad("Mohanlal Jewellers","Jewellery retail"),
           FOOT("Cipher clean.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")
if __name__ == "__main__": build()
