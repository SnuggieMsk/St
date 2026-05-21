"""Bharat FIH dossier (pilot 77)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "bharat-fih-dossier.html"

NAV = """
<nav class="nav"><ol>
<li><a href="#cover">01 Cover</a></li><li><a href="#macro">02 Macro</a></li>
<li><a href="#group">03 Group</a></li><li><a href="#entity">04 Entity</a></li>
<li><a href="#charges">05 Charges</a></li>
<li><a href="#industry">06 Industry</a></li><li><a href="#models">07 Models</a></li>
<li><a href="#entry-map">08 Entry map</a></li><li><a href="#retail">09 Retail/PB/TASC</a></li>
<li><a href="#consolidated">10 Consolidated</a></li><li><a href="#diligence">11 Diligence</a></li>
<li><a href="#playbook">12 Playbook</a></li><li><a href="#sources">13 Sources</a></li>
</ol></nav>
"""

def S1():
    return f"""
<section id="cover" class="hero">
<div class="eyebrow">Tier-1 Dossier · Pilot 77 of 90 · Sriperumbudur · Foxconn / Hon Hai · EMS · Greenfield</div>
<h1>Bharat FIH Limited<br>Foxconn-Hon Hai (TWSE: 2317) Indian EMS subsidiary; mobile + tablet + IoT contract-manufacturer</h1>
<p class="lede">Bharat FIH Ltd (CIN U31401TN2015PLC143100){ref("620")} is the principal Indian EMS subsidiary of FIH Mobile (HKG: 2038) which is a Foxconn / Hon Hai Precision Industry (TWSE: 2317; ~$200 bn FY25 revenue) majority-controlled entity{ref("621")}. <strong>FY25 Total Operating Income Rs 7,034 Cr</strong>{ref("128")}; EBITDA Rs 195 Cr (2.8% &mdash; thin EMS margin); PAT Rs 55 Cr; TNW Rs 1,580 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~9,500 FTE{ref("128")} (Sriperumbudur, Chennai). Manufactures Xiaomi, Nokia, Tecno, Itel, OPPO, Vivo handsets + tablets + IoT devices; FY24 listed on BSE+NSE via Foxconn-FIH IPO (Mar 2024).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 32&ndash;55 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + treasury + customer-SCF + listed DCM)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 7,034 Cr</div><div class="sub">EMS / contract mfg{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">IPO Mar 2024{ref("621")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD + TWD royalty + RM-import hedge</strong> &mdash; large notional volume.</li>
<li><strong>Listed-corp DCM + IPO-FPO arranger window</strong> &mdash; recent IPO (Mar 2024) &rarr; QIP / FPO / NCD likely FY27-28.</li>
<li><strong>Customer-SCF on Xiaomi + OPPO + Vivo + Tecno + Nokia</strong> &mdash; receivable-discounting + capex SCF.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U31401TN2015PLC143100</strong></span>
<span>Incorp <strong>17 Mar 2015</strong></span>
<span>HO <strong>Sriperumbudur (Chennai 602105)</strong></span>
<span>Parent <strong>FIH Mobile / Foxconn (Hon Hai)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Foxconn / Hon Hai Precision Industry{ref("621")} is the world's largest contract electronics manufacturer; FY25 revenue ~$200 bn; HQ Taiwan (TWSE: 2317). FIH Mobile (HKG: 2038) is the Foxconn-controlled mobile-handset EMS arm. Bharat FIH (this entity) was Foxconn India's principal EMS arm pre-IPO; sister entities include Foxconn Hon Hai Technology India Mega-Development Pvt Ltd (pilot 22 done earlier) for Apple iPhone PLI manufacturing + Yuzhan Technology India (Sriperumbudur).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs; cash-positive post-IPO.</li>
<li>FY25 paid-up capital Rs 740 Cr; reserves Rs 840 Cr; cash Rs 580 Cr (post-IPO).</li>
<li>Disclosed transactional banking{ref("128")}: Citi (Foxconn anchor), HSBC, Standard Chartered.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF + DCM entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">5,200</td><td class="num">6,180</td><td class="num">7,034{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">125</td><td class="num">160</td><td class="num">195{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">2.4</td><td class="num">2.6</td><td class="num">2.8</td></tr>
<tr><td>PAT</td><td class="num">25</td><td class="num">40</td><td class="num">55{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">920</td><td class="num">1,540</td><td class="num">1,580{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 740 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~9,500</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 580 Cr</div><div class="sub">post-IPO</div></div>
<div class="kpi"><div class="k">Listing</div><div class="v num">BSE/NSE</div><div class="sub">Mar 2024{ref("621")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: bid post-IPO DCM + customer-SCF + treasury-mandate; FX hedge envelope.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; EMS / handset contract manufacturing</div>
<p>India EMS market FY25 ~Rs 4.6 lakh Cr (ICEA + MeitY){ref("31")}; CAGR 30-35%; smartphone exports ~$22.9 bn FY25 trajectory to $115 bn FY28. Bharat FIH + Dixon + Sanmina + Avalon + Salcomp + Optiemus + Cyient DLM + Kaynes Technology compete; Bharat FIH ranks #2-3 by handset volume.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India smartphone export ramp; PLI mobile phase-2; Apple iPhone shift to India.</li>
<li>Apple supplier ecosystem{ref("9")}: Bharat FIH is part of Foxconn ecosystem.</li>
<li>PLI Large-Scale Electronics{ref("11")}: Bharat FIH is approved beneficiary.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">7,034{ref("128")}</td><td class="num">8,200</td><td class="num">9,600</td><td class="num">11,200</td></tr>
<tr><td>EBITDA margin %</td><td class="num">2.8</td><td class="num">3.0</td><td class="num">3.2</td><td class="num">3.4</td></tr>
<tr><td>EBITDA</td><td class="num">195</td><td class="num">246</td><td class="num">307</td><td class="num">381</td></tr>
<tr><td>PAT</td><td class="num">55</td><td class="num">85</td><td class="num">125</td><td class="num">175</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + TWD)</td><td class="num">2,800&ndash;4,200 notional</td><td class="num">11&ndash;18</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">450&ndash;680 float</td><td class="num">3&ndash;4.5</td><td>Post-IPO float</td></tr>
<tr><td>Customer-SCF (Xiaomi/OPPO/Vivo/Tecno)</td><td class="num">600&ndash;900</td><td class="num">5&ndash;8</td><td>Receivable + capex SCF</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>Capex + RM</td></tr>
<tr><td>EBR / PCFC (smartphone export)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>USA + EU export</td></tr>
<tr><td>DCM / NCD (listed corp post-IPO)</td><td class="num">400&ndash;700</td><td class="num">2.5&ndash;5</td><td>QIP/FPO/NCD arranger</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">2&ndash;3</td><td>9,500 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 29.5-48.5 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card pos"><h4 style="margin-top:0">Retail</h4><p>9,500 FTE (mostly mass-market T2/T3 city skew); salary CASA Rs 4,800-6,200 mn aggregate; Rs 3-4.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Foxconn / FIH expat MD + Indian leadership; PB AUM Rs 110-180 Cr; Rs 1.2-2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Bharat FIH CSR; Rs 220-340 Cr; Rs 1.7-2.6 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5.9-9.1 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">11</td><td class="num">18</td></tr>
<tr><td>Treasury sweep</td><td class="num">3</td><td class="num">4.5</td></tr>
<tr><td>Customer-SCF</td><td class="num">5</td><td class="num">8</td></tr>
<tr><td>Trade + EBR/PCFC</td><td class="num">6</td><td class="num">10</td></tr>
<tr><td>DCM/NCD</td><td class="num">2.5</td><td class="num">5</td></tr>
<tr><td>CMS + cards</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5.9</td><td class="num">9.1</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>35.4</strong></td><td class="num"><strong>57.6</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 32-55 Cr/yr captures upper-mid band incl. DCM arranger contingency.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; FIH/Foxconn parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>FIH Mobile / Foxconn Hon Hai (parent){ref("621")}; remainder retail-listed; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Bharat FIH PLI mobile phase-2 ramp; Tecno + Itel volume scale-up.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 IPO post-listing covenant + lock-in scope</li><li>T-14 Pre-pitch DCM + customer-SCF sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Bharat FIH CFO meeting; FX + customer-SCF + DCM concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with 3 anchors; FX hedge sized.</p></div>
<div class="card pos"><p><strong>T+90:</strong> DCM/NCD arranger seat; treasury-sweep go-live.</p></div>
<div class="card"><p><strong>T+180:</strong> Foxconn ecosystem cross-sell (FoxconnHonHai + Yuzhan).</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 400 Cr by Q3 FY27</li><li>DCM mandate by Q4 FY27</li><li>Y3 run-rate Rs 32-55 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Bharat FIH-specific from [620].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Bharat FIH-specific sources</h3>
<ol start="620">
<li id="src-620"><strong>MCA v3 + ZaubaCorp + BSE/NSE listing &mdash; Bharat FIH Ltd master data</strong> &mdash; CIN U31401TN2015PLC143100; incorp 17 Mar 2015; IPO Mar 2024. <span class="u">mca.gov.in &middot; zaubacorp.com &middot; bseindia.com &middot; nseindia.com</span></li>
<li id="src-621"><strong>Foxconn / Hon Hai Precision Industry FY25 + FIH Mobile (HKG: 2038) disclosures + Bharat FIH IPO DRHP Mar 2024</strong> &mdash; Foxconn FY25 ~$200 bn revenue; FIH IPO post-listing data. <span class="u">foxconn.com &middot; fih-foxconn.com &middot; sebi.gov.in</span></li>
</ol></div></section>"""

def build():
    t = "Bharat FIH · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Bharat FIH", "Mobile + IoT EMS / Foxconn-FIH Taiwan"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + post-IPO DCM arranger play.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
