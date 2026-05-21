"""Mobis India Limited dossier (pilot 56)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "mobis-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 56 of 75 · Chennai · Hyundai-Mobis Korean MNC · Auto-comp tier-1 · Greenfield A1+ entry</div>
<h1>Mobis India Limited<br>Korean Hyundai-Mobis tier-1 module &amp; component subsidiary servicing Hyundai-Kia India</h1>
<p class="lede">Mobis India Limited (CIN U50300TN2005PLC056533){ref("410")} is the Indian subsidiary of Hyundai Mobis Co. Ltd (KOSPI: 012330; ~$58 bn global revenue), the Hyundai Motor Group's tier-1 module &amp; component supplier{ref("411")}. <strong>FY25 Total Operating Income Rs 17,003 Cr</strong>{ref("128")} &mdash; among the top-3 auto-component MNC subsidiaries in TN; EBITDA Rs 1,260 Cr (7.4%); PAT Rs 690 Cr; Tangible Net Worth Rs 4,580 Cr (cash-rich); Total Debt nominal. <strong>ZERO open charges on MCA registry</strong>{ref("126")} &mdash; classic greenfield Korean-MNC profile with internal-treasury funding. <strong>ICRA A1+ (09 Apr 2026)</strong> on Rs 70 Cr CP / short-term facility{ref("412")}. 1,250 FTE{ref("128")}. Hyundai Motor India launched HMIL IPO Oct 2024 (BSE/NSE listing); Mobis is the captive supplier &mdash; Sriperumbudur plant + Anantapur AP plant + Pune R&amp;D.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 60&ndash;100 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (treasury + FX + retail)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 17,003 Cr</div><div class="sub">Auto-comp modules / Hyundai-Kia{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA A1+</div><div class="sub">09 Apr 2026{ref("412")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Treasury / liquidity-sweep mandate</strong> &mdash; Rs 4,500+ Cr cash float, no debt; ZBA + sweep on MNC-treasury structure (TM-as-a-Service).</li>
<li><strong>Korean-FX Korea KRW + USD hedge book</strong> &mdash; royalty + import RM payments to parent; FX spot + forward + options.</li>
<li><strong>HMIL-listed IPO float adjacency</strong> &mdash; Hyundai Motor India {ref("413")} listed Oct 2024; Mobis ecosystem PB + retail + dealer-finance carry-on.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U50300TN2005PLC056533</strong></span>
<span>Incorp <strong>04 Apr 2005</strong></span>
<span>HO <strong>Sriperumbudur (Chennai 602105)</strong></span>
<span>Parent <strong>Hyundai Mobis Co. (Korea)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Hyundai Motor Group{ref("411")} is the world's third-largest auto OEM (HMC + Kia + Mobis); FY25 group revenue ~$200 bn. Mobis is the captive module + after-service supplier (chassis, cockpit, brakes, lamps, electronics). India operations: Mobis India Ltd (this entity) at Sriperumbudur supplies Hyundai Motor India (HMIL) at the adjacent OEM plant; second plant at Anantapur AP supplies Kia India.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; entire balance sheet equity-funded + parent-treasury intercompany.</li>
<li>FY25 paid-up capital Rs 1,123 Cr; reserves Rs 3,460 Cr; cash + cash-equivalents Rs 1,800 Cr (estimate from MCA filings).</li>
<li>Disclosed bank wallet (lead sheet){ref("128")}: HDFC, BNP Paribas, Standard Chartered &mdash; transactional only (no funded debt).</li>
<li>IBank participation: not in current transactional banking panel &mdash; greenfield treasury entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">13,500</td><td class="num">15,200</td><td class="num">17,003{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">920</td><td class="num">1,080</td><td class="num">1,260{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">6.8</td><td class="num">7.1</td><td class="num">7.4</td></tr>
<tr><td>PAT</td><td class="num">490</td><td class="num">580</td><td class="num">690{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">3,500</td><td class="num">4,050</td><td class="num">4,580{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 1,123 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">1,250</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 1,800 Cr</div><div class="sub">est. MNC-treasury</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA A1+</div><div class="sub">09 Apr 2026{ref("412")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. Entirely equity + intercompany funded.</p>
<p class="lede">Strategic: pure treasury-and-flow play. Y3 wallet is dominated by FX + sweep + dealer-SCF + payroll, not funded credit. Sanction-and-hold a contingent OD line for working-capital stress (rare but maps Korean-MNC structures).</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto-comp / Hyundai-Kia ecosystem</div>
<p>India auto-component industry FY25 ~Rs 6.4 lakh Cr (ACMA){ref("414")}; CAGR 9-11% to Rs 11 lakh Cr by FY28. Hyundai-Kia India captive ~17% of PV market post-HMIL listing{ref("413")}; HMIL Sriperumbudur 7.5 lakh annual capacity + Pune (Talegaon ex-GM); Kia Anantapur 4.0 lakh capacity. Mobis India operates 3 manufacturing facilities + 1 R&amp;D centre.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: Hyundai-Kia US-import substitution to India for select modules + after-market parts; Mobis India export ramp.</li>
<li>EV transition: Hyundai Creta-EV + Ioniq 5 + Kia EV5/EV6 launches; Mobis BMS + e-Axle module locally produced.</li>
<li>HMIL listing{ref("413")}: post-IPO disclosures + governance enhancements; supplier-finance ecosystem opens up.</li>
<li>FX-volatility: KRW-USD-INR triangulation; royalty + intercompany imports.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">17,003{ref("128")}</td><td class="num">19,200</td><td class="num">21,800</td><td class="num">24,500</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.4</td><td class="num">7.7</td><td class="num">8.0</td><td class="num">8.3</td></tr>
<tr><td>EBITDA</td><td class="num">1,260</td><td class="num">1,478</td><td class="num">1,744</td><td class="num">2,034</td></tr>
<tr><td>PAT</td><td class="num">690</td><td class="num">810</td><td class="num">980</td><td class="num">1,160</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>Treasury sweep + ZBA + cash-pool</td><td class="num">1,500&ndash;2,000 float</td><td class="num">7&ndash;11</td><td>MNC TM-aaS</td></tr>
<tr><td>FX (KRW + USD + EUR)</td><td class="num">3,500&ndash;5,000 notional</td><td class="num">14&ndash;22</td><td>Royalty + imports</td></tr>
<tr><td>Trade (LC + BG + SBLC)</td><td class="num">600&ndash;900</td><td class="num">5&ndash;8</td><td>Capital-goods imports</td></tr>
<tr><td>SCF dealer-finance</td><td class="num">800&ndash;1,200</td><td class="num">8&ndash;12</td><td>Hyundai-Kia dealer ecosystem</td></tr>
<tr><td>Vendor-SCF (anchor-to-supplier)</td><td class="num">600&ndash;900</td><td class="num">5&ndash;8</td><td>Mobis tier-2 base</td></tr>
<tr><td>Working-capital contingent OD</td><td class="num">200&ndash;400</td><td class="num">1&ndash;2</td><td>Sanction-and-hold</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">1.5&ndash;2.5</td><td>1,250 FTE + payments</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 41.5-65.5 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 950-1,200 accounts (avg-balance Rs 95k); Rs 4-6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Korean expat MD + senior-Indian-leadership; PB AUM Rs 220-340 Cr; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Mobis CSR; Rs 180-260 Cr; Rs 1.8-2.6 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 8.3-12.6 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Treasury sweep / TM-aaS</td><td class="num">7</td><td class="num">11</td></tr>
<tr><td>FX (KRW + USD + EUR)</td><td class="num">14</td><td class="num">22</td></tr>
<tr><td>Trade</td><td class="num">5</td><td class="num">8</td></tr>
<tr><td>SCF (dealer + vendor)</td><td class="num">13</td><td class="num">20</td></tr>
<tr><td>Contingent OD</td><td class="num">1</td><td class="num">2</td></tr>
<tr><td>CMS + cards</td><td class="num">1.5</td><td class="num">2.5</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">8.3</td><td class="num">12.6</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>49.8</strong></td><td class="num"><strong>78.1</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 60-100 Cr/yr captures upper-mid band incl. dealer-SCF scale-up post-HMIL listing tail.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Korean Mobis-parent appointee MD + Indian CFO + 2 independent directors per Section 149.</p>
<h3>11.2 Ownership</h3><ul><li>100% Hyundai Mobis Co. Ltd, Korea (parent){ref("411")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Apr 2026: ICRA reaffirms A1+ on Rs 70 Cr short-term facility{ref("412")}.</li><li>Oct 2024: parent group HMIL IPO listed BSE/NSE Rs 27,870 Cr{ref("413")}.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Korean parent guarantee + LoC framework</li><li>T-14 Pre-pitch sweep-mandate sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Mobis India CFO meeting; treasury-sweep + FX-mandate concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> ZBA + sweep go-live; FX hedge envelope sized; dealer-SCF pilot with 50 dealers.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Vendor-SCF live with 200 tier-2 suppliers; contingent OD sanctioned.</p></div>
<div class="card"><p><strong>T+180:</strong> Hyundai-Kia ecosystem cross-sell (HMIL salary + Kia-Anantapur dealer + tier-2 vendor finance).</p></div>
<h3>Success metrics</h3><ul class="check"><li>Treasury sweep Rs 1,500 Cr daily-balance by Q2 FY27</li><li>Dealer SCF Rs 600 Cr by Q3 FY27</li><li>Y3 run-rate Rs 60-100 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Mobis India-specific from [410].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Mobis India-specific sources</h3>
<ol start="410">
<li id="src-410"><strong>MCA v3 + ZaubaCorp &mdash; Mobis India Ltd master data</strong> &mdash; CIN U50300TN2005PLC056533; incorp 04 Apr 2005; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-411"><strong>Hyundai Mobis Co. Ltd corporate site + KOSPI 012330 disclosures</strong> &mdash; FY25 group revenue ~$58 bn; module + after-service; Hyundai Motor Group captive. <span class="u">mobis.com &middot; krx.co.kr</span></li>
<li id="src-412"><strong>ICRA &mdash; Mobis India Ltd rating rationale (09 Apr 2026)</strong> &mdash; reaffirms A1+ on Rs 70 Cr short-term fund-based + Rs 5 Cr / Rs 2 Cr split. <span class="u">icra.in</span></li>
<li id="src-413"><strong>Hyundai Motor India Ltd (HMIL) IPO prospectus + BSE/NSE listing 22 Oct 2024</strong> &mdash; Rs 27,870 Cr issue size; PV-market #2 in India; supplier ecosystem disclosure. <span class="u">bseindia.com / nseindia.com / sebi.gov.in</span></li>
<li id="src-414"><strong>ACMA Industry Outlook FY25 + Mar 2026 update</strong> &mdash; auto-component industry Rs 6.4 lakh Cr; growth + EV transition. <span class="u">acma.in</span></li>
</ol></div></section>"""

def build():
    t = "Mobis India Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Mobis India", "Auto-component modules / Hyundai-Mobis Korean MNC"),
           FOOT("Cipher clean; 1,500+ lines; greenfield A1+ + Hyundai-Kia ecosystem treasury.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
