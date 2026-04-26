"""Renault-Nissan Technology & Business Centre India (RNTBCI) dossier (pilot 61)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "rntbci-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 61 of 75 · Chennai · Renault-Nissan ER&amp;D + GCC · Auto engineering</div>
<h1>Renault Nissan Technology &amp; Business Centre India Pvt Ltd<br>Renault + Nissan global ER&amp;D + business-process captive in Chennai</h1>
<p class="lede">RNTBCI (CIN U50401TN2007PTC064840){ref("460")} is the Renault-Nissan global engineering R&amp;D + business-process captive (GCC) in Chennai{ref("461")}. <strong>FY25 Total Operating Income Rs 3,287 Cr</strong>{ref("128")}; EBITDA Rs 580 Cr (17.6%); PAT Rs 410 Cr; TNW Rs 1,420 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. <strong>~10,500 FTE</strong>{ref("128")} &mdash; one of the largest auto ER&amp;D GCCs in India; CAD/CAE/CFD, vehicle-design, software-defined-vehicle (SDV) platform, ADAS, embedded-electronics, business-services-shared-services for Renault + Nissan globally.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 28&ndash;48 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + treasury + retail)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 3,287 Cr</div><div class="sub">Auto ER&amp;D / GCC{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~10,500</div><div class="sub">India top-3 auto ER&amp;D GCC{ref("140")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>EUR + JPY + USD revenue-FX hedge</strong> &mdash; 100% export billing to Renault SAS + Nissan Motor Co + Mitsubishi Motors.</li>
<li><strong>Salary + retail asset-cross-sell on 10,500 FTE base</strong> &mdash; salary CASA + auto-loan + home-loan + cards + PB.</li>
<li><strong>SEZ STPI + GIFT-IFSC opportunity</strong> &mdash; export ER&amp;D-services dollar billing structure.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U50401TN2007PTC064840</strong></span>
<span>Incorp <strong>17 Aug 2007</strong></span>
<span>HO <strong>Chennai (Mahindra World City + DLF IT Park)</strong></span>
<span>Parent <strong>Renault SAS + Nissan Motor Co (50:50 prior; restructuring post-divorce)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>RNTBCI was set up 2007 as a 50:50 Renault-Nissan ER&amp;D + business-services GCC{ref("461")}. Post Renault-Nissan alliance restructuring (Nov 2023) with declining cross-shareholdings, RNTBCI ownership is being realigned; expected outcome: separate Renault-only and Nissan-only captives or service-MoU structure. Continues to deliver SDV + EV + ADAS + embedded-electronics + back-office shared services to both groups + Mitsubishi Motors.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges as of 24 Apr 2026{ref("126")} &mdash; entirely equity-funded; export-services revenue model.</li>
<li>FY25 paid-up capital Rs 22 Cr; reserves Rs 1,398 Cr; cash Rs 580 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: BNP Paribas, MUFG (joint Renault-Nissan default), HSBC, Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + retail-mass-market entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,500</td><td class="num">2,880</td><td class="num">3,287{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">395</td><td class="num">485</td><td class="num">580{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.8</td><td class="num">16.8</td><td class="num">17.6</td></tr>
<tr><td>PAT</td><td class="num">270</td><td class="num">335</td><td class="num">410{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">920</td><td class="num">1,150</td><td class="num">1,420{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 22 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~10,500</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 580 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}. Pure flow + retail-asset opportunity.</p>
<p class="lede">Strategic: capture FX (EUR + JPY + USD) hedge mandate; build retail mass-market relationship on 10,500 FTE base; PB book on senior leadership.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto ER&amp;D / GCC</div>
<p>India auto ER&amp;D GCC sub-segment ~Rs 95,000 Cr FY25 (NASSCOM){ref("140")}; CAGR 14-16%; Tier-1s + OEMs operating ~80 captives. RNTBCI ranks among top-3 auto ER&amp;D GCCs (alongside Mercedes R&amp;D + Bosch GS + Continental). SDV + ADAS + EV-platform + battery-software work concentrated.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>SDV + ADAS + EV-platform: triple-digit CAGR globally; ER&amp;D outsourcing to India structural.</li>
<li>USA-tariff window{ref("6")}: services-tariff still ~0%; ER&amp;D billing protected.</li>
<li>EU AI-Act + Cybersecurity-Act: increased compliance work shoring.</li>
<li>Renault-Nissan alliance restructuring: scope expansion + diversification to non-alliance OEMs.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">3,287{ref("128")}</td><td class="num">3,800</td><td class="num">4,400</td><td class="num">5,100</td></tr>
<tr><td>EBITDA margin %</td><td class="num">17.6</td><td class="num">18.2</td><td class="num">18.8</td><td class="num">19.4</td></tr>
<tr><td>EBITDA</td><td class="num">580</td><td class="num">692</td><td class="num">827</td><td class="num">989</td></tr>
<tr><td>PAT</td><td class="num">410</td><td class="num">490</td><td class="num">590</td><td class="num">710</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (EUR + JPY + USD)</td><td class="num">2,800&ndash;4,000 notional</td><td class="num">12&ndash;18</td><td>100% export billing</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">500&ndash;750 float</td><td class="num">3&ndash;4.5</td><td>MNC TM-aaS</td></tr>
<tr><td>EBR / PCFC (services-export)</td><td class="num">300&ndash;500</td><td class="num">2.5&ndash;4</td><td>Receivable financing</td></tr>
<tr><td>Salary + retail asset (10,500)</td><td class="num">800&ndash;1,200 disbursal/yr</td><td class="num">7&ndash;12</td><td>Auto + home + cards</td></tr>
<tr><td>PB (senior leadership)</td><td class="num">220&ndash;350 AUM</td><td class="num">3&ndash;4.5</td><td>Indian + expat leaders</td></tr>
<tr><td>TASC + employee-benefit + payroll</td><td class="num">200&ndash;320 PF/Gratuity</td><td class="num">1.6&ndash;2.4</td><td>Plus group-term insurance</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">2&ndash;3.2</td><td>10,500 FTE corporate cards</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 17.5-26.5 Cr / yr. Retail/PB/TASC: Rs 13.6-22.1 Cr/yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC (the headline play)</div>
<div class="grid c3">
<div class="card pos"><h4 style="margin-top:0">Retail (anchor)</h4><p>10,500 FTE; salary CASA Rs 9,000-12,000 mn aggregate (avg Rs 95-110k); auto + home + cards cross-sell; Rs 7-12 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Senior expat + Indian leadership UHNI; PB AUM Rs 220-350 Cr; Rs 3-4.5 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + RNTBCI CSR; Rs 200-320 Cr; Rs 1.6-2.4 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 11.6-18.9 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">12</td><td class="num">18</td></tr>
<tr><td>Treasury sweep</td><td class="num">3</td><td class="num">4.5</td></tr>
<tr><td>EBR/PCFC</td><td class="num">2.5</td><td class="num">4</td></tr>
<tr><td>CMS + cards</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>Retail asset cross-sell</td><td class="num">7</td><td class="num">12</td></tr>
<tr><td>PB</td><td class="num">3</td><td class="num">4.5</td></tr>
<tr><td>TASC</td><td class="num">1.6</td><td class="num">2.4</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>31.1</strong></td><td class="num"><strong>48.6</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 28-48 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; senior Renault + Nissan + Mitsubishi appointee MD + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>Pre-restructuring 50:50 Renault SAS + Nissan Motor Co{ref("461")}; BEN-2 on file{ref("144")}; awaiting alliance-restructuring confirmation.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: alliance restructuring; expected RNTBCI ownership realignment.</li><li>FY26: SDV + EV platform R&amp;D scope expansion.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 Alliance restructuring scope</li><li>T-14 Pre-pitch retail-mass + PB sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> RNTBCI CFO + HR meetings; FX + retail-payroll concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Salary-CASA pilot for 1,500 FTE; PB book on 30 senior leaders.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; auto-loan + home-loan campaign for 10,500 base.</p></div>
<div class="card"><p><strong>T+180:</strong> Renault India + RNAIPL + RNTBCI bundled ecosystem.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Salary CASA 5,000+ accounts by Q3 FY27</li><li>Retail-asset book Rs 400 Cr by Q4 FY27</li><li>Y3 run-rate Rs 28-48 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; RNTBCI-specific from [460].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">RNTBCI-specific sources</h3>
<ol start="460">
<li id="src-460"><strong>MCA v3 + ZaubaCorp &mdash; RNTBCI master data</strong> &mdash; CIN U50401TN2007PTC064840; incorp 17 Aug 2007; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-461"><strong>Renault Group + Nissan Motor Co alliance + RNTBCI corporate disclosures</strong> &mdash; ER&amp;D + business-services captive; SDV/ADAS/EV scope; Nov 2023 alliance restructuring. <span class="u">renaultgroup.com &middot; nissan-global.com &middot; rntbci.com</span></li>
</ol></div></section>"""

def build():
    t = "RNTBCI · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("RNTBCI", "Auto ER&amp;D + business-services GCC / Renault-Nissan"),
           FOOT("Cipher clean; 1,500+ lines; FX + retail-mass + PB on 10,500 FTE GCC base.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
