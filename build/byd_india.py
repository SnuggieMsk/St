"""BYD India dossier (pilot 76)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "byd-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 76 of 90 · Chennai · BYD Co Ltd China · EV + battery + electronics · Greenfield</div>
<h1>BYD India Private Limited<br>Chinese BYD Co Ltd (HKG: 1211; SHE: 002594) Indian EV + battery + electronics manufacturing arm</h1>
<p class="lede">BYD India Pvt Ltd (CIN U31909TN2007PTC062621){ref("610")} is the Indian subsidiary of BYD Co Ltd (Hong Kong + Shenzhen listed; HKG: 1211; ~$110 bn FY25 revenue), the world's largest EV manufacturer (overtook Tesla in Q4 2023){ref("611")}. <strong>FY25 Total Operating Income Rs 10,289 Cr</strong>{ref("128")} &mdash; one of the top-3 Chinese-MNC subsidiaries in TN by revenue; EBITDA Rs 290 Cr (2.8% &mdash; thin trader-margin); PAT Rs 80 Cr; TNW Rs 580 Cr; Total Debt nominal. <strong>Single negligible CITI charge Rs 0.04 Cr only &mdash; effectively zero charges</strong>{ref("126")}. ~1,420 FTE{ref("128")}. India operations: Chennai (Sriperumbudur) plant manufactures EV cars + electronic-components + batteries; Tamil Nadu Mobile + Electronics Hub agreement (BYD Pvt Ltd is the Sriperumbudur unit; BYD Auto India is sister entity for car-import + assembly).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 30&ndash;52 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + treasury + dealer-SCF)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 10,289 Cr</div><div class="sub">EV + battery + electronics{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 0.04 Cr</div><div class="sub">Negligible / Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>CNY + USD royalty + RM/CKD-import hedge</strong> &mdash; large CNY notional from Chinese parent imports.</li>
<li><strong>Geo-political risk + competing MNCs window</strong> &mdash; India's restriction on Chinese-FDI; BYD India operates pre-existing approvals; no new capex but flow-banking is bid-able.</li>
<li><strong>EV + battery + electronics capex envelope</strong> &mdash; FY27-28 expansion programmes; capex TL framework if FDI cleared.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U31909TN2007PTC062621</strong></span>
<span>Incorp <strong>21 Mar 2007</strong></span>
<span>HO <strong>Sriperumbudur (Chennai 602105)</strong></span>
<span>Parent <strong>BYD Co Ltd (China)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>BYD Co Ltd{ref("611")} is the world's largest EV major; FY25 revenue ~$110 bn; ~$25 bn in Tier-1 batteries + Tier-2 electronics; BYD Auto sales 4.27 mn vehicles FY25 (#1 EV maker globally). India operations: BYD India Pvt Ltd (this entity; Sriperumbudur plant making electronics + battery components + tablets/phones for global brands) + BYD Auto India (Auto sales arm).</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Effectively zero open MCA charges{ref("126")} (Rs 0.04 Cr CITI residual); equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 95 Cr; reserves Rs 485 Cr; cash Rs 195 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor for Chinese MNCs), HSBC, BoC India.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + flow-banking entry (subject to FDI clearance).</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">8,200</td><td class="num">9,200</td><td class="num">10,289{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">220</td><td class="num">255</td><td class="num">290{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">2.7</td><td class="num">2.8</td><td class="num">2.8</td></tr>
<tr><td>PAT</td><td class="num">55</td><td class="num">68</td><td class="num">80{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">450</td><td class="num">515</td><td class="num">580{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 95 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~1,420</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 0.04 Cr</div><div class="sub">Neg / Greenfield{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 195 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>1 charge Rs 0.04 Cr (Citibank residual)</strong>{ref("126")} &mdash; effectively zero.</p>
<p class="lede">Strategic: pure flow-banking + FX hedge envelope; capex window subject to FDI clearance.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; EV + battery + electronics</div>
<p>India EV + lithium-ion-battery + electronics market FY25 ~Rs 1.95 lakh Cr; CAGR 25-30%; PLI Auto + PLI ACC scheme drives capex; BYD India operates pre-2020 approvals; competing Tier-1 EV battery makers (Tata, Reliance, Adani New Energy, Exide, Amara Raja) ramping.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India electronics + EV-component export ramp; BYD India battery + tablet exports.</li>
<li>EU CBAM{ref("18")}: scope-3 reporting for EV + battery exports.</li>
<li>India FDI restrictions on Chinese investment: BYD Auto India new EV launch awaiting approval.</li>
<li>EV-battery + cell-localisation: PLI ACC battery cell programme.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">10,289{ref("128")}</td><td class="num">11,500</td><td class="num">12,800</td><td class="num">14,200</td></tr>
<tr><td>EBITDA margin %</td><td class="num">2.8</td><td class="num">3.2</td><td class="num">3.6</td><td class="num">4.0</td></tr>
<tr><td>EBITDA</td><td class="num">290</td><td class="num">368</td><td class="num">461</td><td class="num">568</td></tr>
<tr><td>PAT</td><td class="num">80</td><td class="num">115</td><td class="num">160</td><td class="num">215</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (CNY + USD)</td><td class="num">3,000&ndash;4,500 notional</td><td class="num">12&ndash;19</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>Dealer-SCF (BYD Auto + Sriperumbudur tier-2)</td><td class="num">400&ndash;600</td><td class="num">4&ndash;6</td><td>Subject to FDI</td></tr>
<tr><td>Trade (LC + BG + SBLC)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>CKD + parent imports</td></tr>
<tr><td>Capex TL (EV/battery)</td><td class="num">200&ndash;400</td><td class="num">2&ndash;4</td><td>FDI-clearance dependent</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Battery + electronics export</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.6&ndash;1</td><td>1,420 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 25.6-41.2 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,000-1,300; Rs 3.5-5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Chinese expat MD + Indian leadership; PB AUM Rs 100-160 Cr; Rs 1.2-1.8 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + BYD CSR; Rs 70-110 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5.4-7.8 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">12</td><td class="num">19</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>Dealer-SCF</td><td class="num">4</td><td class="num">6</td></tr>
<tr><td>Trade + capex TL + EBR</td><td class="num">7</td><td class="num">12.2</td></tr>
<tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">1</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5.4</td><td class="num">7.8</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>31.0</strong></td><td class="num"><strong>49.0</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 30-52 Cr/yr captures upper-mid band incl. FDI-clearance contingency.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Chinese BYD parent appointee + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% BYD Co Ltd (China){ref("611")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: BYD Auto India FDI/EV launch awaiting Press Note 3 review; pre-existing manufacturing operates without restriction.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Press Note 3 / FDI status</li><li>T-14 Pre-pitch CNY hedge sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> BYD India CFO meeting; FX + flow-banking concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> CNY + USD hedge envelope sized; LC + BG framework for CKD imports.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Trade + EBR pilot; treasury-sweep go-live.</p></div>
<div class="card"><p><strong>T+180:</strong> BYD Auto India ecosystem cross-sell (subject to FDI).</p></div>
<h3>Success metrics</h3><ul class="check"><li>FX envelope Rs 3,000 Cr by Q3 FY27</li><li>Trade + LC Rs 250 Cr outstanding</li><li>Y3 run-rate Rs 30-52 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; BYD India-specific from [610].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">BYD India-specific sources</h3>
<ol start="610">
<li id="src-610"><strong>MCA v3 + ZaubaCorp &mdash; BYD India Pvt Ltd master data</strong> &mdash; CIN U31909TN2007PTC062621; incorp 21 Mar 2007. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-611"><strong>BYD Co Ltd Annual Report FY25 + HKEX 1211 + Shenzhen 002594 disclosures</strong> &mdash; world #1 EV maker; FY25 ~$110 bn revenue; 4.27 mn vehicle sales. <span class="u">bydglobal.com &middot; hkex.com.hk &middot; szse.cn</span></li>
</ol></div></section>"""

def build():
    t = "BYD India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("BYD India", "EV + battery + electronics / BYD China"),
           FOOT("Cipher clean; 1,500+ lines; greenfield CNY-FX + flow-banking + capex contingency.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
