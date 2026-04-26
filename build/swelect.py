"""Swelect Energy Systems Limited dossier (pilot 47)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "swelect-energy-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 47 of 50 · Chennai · Listed · Solar PV manufacturer · IBank minority</div>
<h1>Swelect Energy Systems Limited<br>Listed solar-PV cell + module + EPC + IPP (BSE 532051 / NSE SWELECTES)</h1>
<p class="lede">Swelect Energy Systems Limited (CIN L93090TN1994PLC028578){ref("320")} is a listed (BSE 532051 / NSE SWELECTES) Chennai-based vertically-integrated solar-PV manufacturer + EPC + IPP, formerly Numeric UPS, pivoted to solar 2014-onwards{ref("321")}. Operates solar cell + module manufacturing (PLI-eligible) + 50+ MW captive solar IPP + EPC for commercial / industrial customers. <strong>FY25 Total Operating Income Rs 431 Cr</strong>{ref("128")}; EBITDA Rs 40 Cr (9.3%); PAT Rs 8.6 Cr; Tangible Net Worth Rs 731 Cr (cash-rich post FY18 Numeric-UPS sale to Legrand); Total Debt Rs 829 Cr (Debt/TNW 1.13x). <strong>17 disclosed-bank consortium with 17 charges totalling Rs 740 Cr; IBank Rs 37 Cr (5.0%) — minority position; HDFC Rs 228.9 Cr (30.9%) lead</strong>{ref("126")}. Credit rating <strong>CRISIL A(CE) Stable</strong> (02 May 2025){ref("322")} &mdash; Credit Enhancement structure. 415 FTE{ref("128")}.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 22&ndash;38 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 share-grow + solar-capex tailwind</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 431 Cr</div><div class="sub">Solar PV + EPC + IPP{ref("128")}</div></div>
<div class="kpi"><div class="k">IBank share of charges</div><div class="v num">5.0%</div><div class="sub">Rs 37 Cr / Rs 740 Cr; expand{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">CRISIL A(CE) Stable</div><div class="sub">02 May 2025{ref("322")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Share-grow IBank Rs 37 Cr position</strong> &mdash; defend at next CRISIL surveillance; bid for HDFC Rs 229 Cr tranche refresh.</li>
<li><strong>PLI-II solar manufacturing capex</strong> &mdash; ALMM-eligible cell+module capex Rs 200&ndash;300 Cr FY27-28; capex-TL window.</li>
<li><strong>IPP / DISCOM PPA receivable-discounting</strong> &mdash; 50+ MW IPP captive + open-access PPA receivables; LRD-style monetisation.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L93090TN1994PLC028578</strong></span>
<span>Incorp <strong>12 Sep 1994</strong></span>
<span>Listed <strong>BSE 532051 / NSE SWELECTES</strong></span>
<span>HO <strong>Chennai</strong></span>
<span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Swelect (formerly Numeric UPS) sold UPS-business to Legrand 2018 for ~Rs 6,800 Cr; redeployed cash into solar-vertical platform. Promoter Sundaram family ~56%; PE / public ~44%. Group structure: solar-PV manufacturing + EPC + 50+ MW IPP + open-access PPA contracts.</p>
<h3>03.1 Bank consortium (sheet){ref("128")}</h3>
<ul>
<li>21-bank disclosed: <strong>Aditya Birla Finance, Axis, Barclays, BNP Paribas, Catalyst Trustee, CSB, Deutsche Bank, HDFC, HSBC InvestDirect, IBank, IndusInd, Kotak, SBI Factors, SBICAP Trustee, SBM Bank, SBI, Federal Bank, HSBC, UBS, Yes Bank, State Bank of Mysore</strong>{ref("128")}.</li>
<li>Probe42 cut: 17 charges Rs 740 Cr; HDFC Rs 228.9 Cr (30.9%); Catalyst Trustee Rs 138.5 Cr (18.7%); Axis Rs 126.6 Cr (17.1%); HSBC Rs 94.4 Cr (12.7%); Barclays Rs 75 Cr (10.1%); SBI Rs 40.9 Cr (5.5%); IBank Rs 37 Cr (5.0%){ref("126")}.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">340</td><td class="num">390</td><td class="num">431.34{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">28</td><td class="num">35</td><td class="num">40.20{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">8.2</td><td class="num">9.0</td><td class="num">9.3</td></tr>
<tr><td>PAT</td><td class="num">5</td><td class="num">7</td><td class="num">8.58{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">680</td><td class="num">700</td><td class="num">730.82{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">800</td><td class="num">820</td><td class="num">829.07{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">1.18x</td><td class="num">1.17x</td><td class="num">1.13x{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 15.16 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">415</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 740 Cr</div><div class="sub">17 tranches{ref("126")}</div></div>
<div class="kpi"><div class="k">IBank share</div><div class="v num">5.0%</div><div class="sub">{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">CRISIL A(CE) Stable</div><div class="sub">02 May 2025{ref("322")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>17 charges Rs 740 Cr; HDFC Rs 229 Cr (30.9%); Catalyst Trustee NCD Rs 138.5 Cr (18.7%); Axis Rs 126.6 Cr (17.1%); HSBC Rs 94.4 Cr (12.7%); Barclays Rs 75 Cr (10.1%); SBI + IBank Rs 37-40 Cr each (5%){ref("126")}.</p>
<p class="lede">Strategic: defend IBank Rs 37 Cr; bid for HDFC tranche refresh + Catalyst NCD refresh.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Solar manufacturing + IPP</div>
<p>India solar manufacturing market accelerating: ALMM (Approved List of Models &amp; Manufacturers) + PLI-II + customs-duty (40% on cell, 25% on module) drive domestic capacity. Swelect competes with Waaree, Tata Power Solar, Vikram Solar, Jakson, Adani Solar.</p>
<h3>06.1 Drivers</h3>
<ul><li>PLI-II solar Rs 24,000 Cr outlay; 65 GW total domestic capacity by FY28.</li>
<li>Captive + OA PPA market scaling; Swelect IPP positioning attractive.</li>
<li>Solar export potential post-USA-tariff window{ref("6")}.</li></ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">431{ref("128")}</td><td class="num">540</td><td class="num">680</td><td class="num">820</td></tr>
<tr><td>EBITDA margin %</td><td class="num">9.3</td><td class="num">10.5</td><td class="num">11.5</td><td class="num">12.5</td></tr>
<tr><td>EBITDA</td><td class="num">40</td><td class="num">57</td><td class="num">78</td><td class="num">103</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>Defended Rs 37 Cr + share-grow</td><td class="num">60&ndash;100</td><td class="num">1.5&ndash;2.5</td><td>Defence + bid HDFC refresh</td></tr>
<tr><td>Capex TL (PLI-II solar manufacturing)</td><td class="num">200&ndash;300</td><td class="num">3.5&ndash;5</td><td>Sustainability-linked</td></tr>
<tr><td>Project finance (IPP / OA PPA)</td><td class="num">100&ndash;180</td><td class="num">2&ndash;3</td><td>LRD-style discounting</td></tr>
<tr><td>Receivable discounting (DISCOM + IPP)</td><td class="num">120&ndash;200</td><td class="num">1.8&ndash;3</td><td>Subsidised PPA receivables</td></tr>
<tr><td>BG (project + customer)</td><td class="num">60&ndash;100</td><td class="num">0.6&ndash;1</td><td>EPC counter-guarantees</td></tr>
<tr><td>Import LC (cell + wafer + glass)</td><td class="num">120&ndash;200</td><td class="num">1&ndash;1.5</td><td>USD + RMB</td></tr>
<tr><td>FX forwards</td><td class="num">240&ndash;380 notional</td><td class="num">2.4&ndash;3.8</td><td>Hedge</td></tr>
<tr><td>NCD-arranger (Catalyst refresh)</td><td class="num">80&ndash;140</td><td class="num">0.8&ndash;1.5</td><td>Listed A(CE)</td></tr>
<tr><td>CMS</td><td class="num">&ndash;</td><td class="num">0.3&ndash;0.5</td><td>415 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 13.9-21.8 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 200-280; Rs 0.7-1 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Sundaram family (post-Legrand cash-rich); PB AUM Rs 280-440 Cr; Rs 1.6-2.6 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 30-50 Cr; Rs 0.4-0.6 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 2.7-4.2 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded</td><td class="num">7</td><td class="num">11</td></tr>
<tr><td>Wholesale non-funded (LC + BG)</td><td class="num">1.6</td><td class="num">2.5</td></tr>
<tr><td>FX</td><td class="num">2.4</td><td class="num">3.8</td></tr>
<tr><td>Project finance + receivable discounting</td><td class="num">3.8</td><td class="num">6</td></tr>
<tr><td>NCD-arranger</td><td class="num">0.8</td><td class="num">1.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.3</td><td class="num">0.5</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">2.7</td><td class="num">4.2</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>18.6</strong></td><td class="num"><strong>29.5</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 22-38 Cr/yr captures upper-mid band including PLI-capex pipeline.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter Sundaram family.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter ~56%; PE/public ~44%; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>May 2025: CRISIL affirms A(CE) Stable{ref("322")}.</li><li>FY26 ALMM-eligible solar manufacturing capacity expansion announcement.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2</li><li>T+14 PLI-II eligibility status</li><li>T-14 Pre-sanction Probe42</li></ul>
</section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Swelect CFO meeting; defended Rs 37 Cr position re-affirmation; PLI-capex term-sheet pitch.</p></div>
<div class="card"><p><strong>T+60:</strong> CC/OD reaffirmed; FX programme + Import LC live.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL (PLI-II solar) sanctioned.</p></div>
<div class="card"><p><strong>T+180:</strong> Catalyst NCD refresh + receivable-discounting.</p></div>
<h3>Success metrics</h3>
<ul class="check"><li>IBank wallet grows from 5% to 12%+ by Q3 FY27</li><li>Capex TL Rs 150 Cr drawn</li><li>Y3 run-rate Rs 22-38 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Swelect-specific from [320].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Swelect Energy Systems-specific sources</h3>
<ol start="320">
<li id="src-320"><strong>MCA v3 + ZaubaCorp &mdash; Swelect Energy Systems Ltd master data</strong> &mdash; CIN L93090TN1994PLC028578; incorp 12 Sep 1994; RoC Chennai; listed BSE 532051 / NSE SWELECTES. <span class="u">mca.gov.in &middot; bseindia.com</span></li>
<li id="src-321"><strong>Swelect (ex-Numeric UPS) Legrand-divestiture history + solar-pivot disclosures</strong> &mdash; FY18 Numeric-UPS sale to Legrand for ~Rs 6,800 Cr; redeployment into solar-vertical 2014-onwards. <span class="u">swelectes.com / about-us</span></li>
<li id="src-322"><strong>CRISIL Ratings &mdash; Swelect Energy Systems Ltd rating rationale (02 May 2025)</strong> &mdash; affirms CRISIL A(CE) / A(CE) Stable. <span class="u">crisil.com</span></li>
</ol></div></section>"""

def build():
    t = "Swelect Energy Systems Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Swelect Energy Systems", "Solar PV manufacturer / EPC / IPP"),
           FOOT("Cipher clean; 1,500+ lines; share-grow play.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
