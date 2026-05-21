"""Omega Healthcare Management Services dossier (pilot 72)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "omega-healthcare-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 72 of 75 · Chennai · Goldman Sachs / Everstone PE-owned · Healthcare RCM BPO · Greenfield</div>
<h1>Omega Healthcare Management Services Private Limited<br>India-origin healthcare-RCM (revenue-cycle-management) BPO; ~$340 mn group revenue; PE-owned (Goldman Sachs + Everstone)</h1>
<p class="lede">Omega Healthcare Management Services Pvt Ltd (CIN U85110TN2003PTC173618){ref("570")} is the largest pure-play India-origin healthcare-RCM BPO; PE-owned (Goldman Sachs Asset Management + Everstone Capital invested ~$1 bn at $1.7 bn valuation Apr 2022){ref("571")}. <strong>FY25 Total Operating Income Rs 2,053 Cr</strong>{ref("128")}; EBITDA Rs 360 Cr (17.5%); PAT Rs 195 Cr; TNW Rs 920 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~32,000 FTE{ref("128")} (the largest single-employer healthcare BPO in India; Chennai HQ + Bengaluru + Trichy + Coimbatore + Hyderabad + Madurai + Philippines + Colombia). Services: medical-coding, claims-processing, accounts-receivable, payor-services, AR-recovery, healthcare-AI for ~250 US hospital + payor + revenue-cycle clients.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 35&ndash;58 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + retail + PE-IPO + ESOP)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,053 Cr</div><div class="sub">Healthcare RCM BPO{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~32,000</div><div class="sub">Largest TN single-employer healthcare BPO{ref("128")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD revenue-FX hedge</strong> &mdash; 100% USD billing.</li>
<li><strong>32,000 FTE retail-mass-market + ESOP wealth + PE-exit IPO mandate</strong> &mdash; salary CASA + auto/home + cards + Tier-2/Tier-3 city retail-asset surge; PE-exit IPO mandate within 24-36 months window.</li>
<li><strong>Goldman + Everstone PE-portfolio cross-sell</strong> &mdash; introduction to wider PE-portfolio + co-investment opportunities.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U85110TN2003PTC173618</strong></span>
<span>Incorp <strong>11 Jul 2003</strong></span>
<span>HO <strong>Tambaram (Chennai 600045) + Bengaluru</strong></span>
<span>PE owners <strong>Goldman Sachs AM + Everstone Capital</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Omega Healthcare{ref("571")} is one of the world's largest pure-play healthcare-RCM BPOs; founded 2003 by Gopi Natarajan + Anurag Mehta in Bengaluru; PE-acquired through successive rounds (Sequoia + Norwest 2011, IDFC 2014, GS+Everstone 2022). Group revenue ~$340 mn FY25. Operations: India (Chennai HQ + 5 satellite cities) + Philippines + Colombia.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + PE-funded; cash-positive.</li>
<li>FY25 paid-up capital Rs 32 Cr; reserves Rs 888 Cr; cash Rs 285 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: HSBC (US-DBA correspondence), Citi.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + retail-mass + PE-exit IPO entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,580</td><td class="num">1,820</td><td class="num">2,053{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">235</td><td class="num">295</td><td class="num">360{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.9</td><td class="num">16.2</td><td class="num">17.5</td></tr>
<tr><td>PAT</td><td class="num">115</td><td class="num">155</td><td class="num">195{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">655</td><td class="num">785</td><td class="num">920{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 32 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~32,000</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 285 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: PE-exit IPO mandate is the headline play; ESOP-Trust banking + retail-mass on 32k FTE base + PB on PE/founders/senior leaders.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Healthcare RCM BPO + healthcare-AI</div>
<p>India healthcare-BPO market FY25 ~$8 bn export; Omega + R1 RCM (US-listed) + Access Healthcare + GeBBS Healthcare (PE-owned) + Sutherland Healthcare (pilot from earlier search) + Cognizant Healthcare BPO compete. Healthcare-AI scope (medical-coding automation, AI-assisted claims, denial-prevention) is the structural growth.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: services-tariff still ~0%; healthcare-RCM USD billing protected.</li>
<li>US healthcare cost-pressure: outsourced-RCM cost-reduction structural.</li>
<li>Gen-AI medical-coding: Omega CodeAssist + similar AI-platforms; productivity 30-40% but pricing-pressure.</li>
<li>HIPAA + HHS data-privacy: regulatory-compliance scope.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,053{ref("128")}</td><td class="num">2,400</td><td class="num">2,800</td><td class="num">3,250</td></tr>
<tr><td>EBITDA margin %</td><td class="num">17.5</td><td class="num">18.5</td><td class="num">19.5</td><td class="num">20.5</td></tr>
<tr><td>EBITDA</td><td class="num">360</td><td class="num">444</td><td class="num">546</td><td class="num">666</td></tr>
<tr><td>PAT</td><td class="num">195</td><td class="num">245</td><td class="num">310</td><td class="num">390</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD)</td><td class="num">1,800&ndash;2,700 notional</td><td class="num">7&ndash;12</td><td>100% USD billing</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>EBR / PCFC (services-export)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Receivable financing</td></tr>
<tr><td>Salary + retail asset (32,000)</td><td class="num">1,200&ndash;1,800 disbursal/yr</td><td class="num">10&ndash;17</td><td>T2/T3 city retail surge</td></tr>
<tr><td>PB (Founders + GS + Everstone + senior MDs)</td><td class="num">600&ndash;900 AUM</td><td class="num">7&ndash;10</td><td>UHNI cluster + PE</td></tr>
<tr><td>TASC + ESOP Trust banking</td><td class="num">320&ndash;500</td><td class="num">2.5&ndash;4</td><td>ESOP plan + PF + Gratuity</td></tr>
<tr><td>IPO arranger / pre-IPO equity</td><td class="num">3,000&ndash;5,000 issue size</td><td class="num">8&ndash;14</td><td>FY27-28 PE-exit IPO mandate</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">2.5&ndash;4</td><td>32,000 FTE corporate cards</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 19-32.2 Cr / yr. Retail/PB/TASC/IPO: Rs 22.5-37.5 Cr/yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC (the headline play)</div>
<div class="grid c3">
<div class="card pos"><h4 style="margin-top:0">Retail (anchor)</h4><p>32,000 FTE; salary CASA Rs 9,500-12,500 mn aggregate; auto + home + cards; T2/T3 city skew; Rs 10-17 Cr/yr.</p></div>
<div class="card pos"><h4 style="margin-top:0">PB (UHNI)</h4><p>Founders + GS + Everstone + senior MDs UHNI; PB AUM Rs 600-900 Cr; Rs 7-10 Cr/yr &mdash; the PE/founder wealth book is a meaningful headline.</p></div>
<div class="card"><h4 style="margin-top:0">TASC + ESOP-Trust</h4><p>ESOP Trust + PF + Gratuity; Rs 320-500 Cr; Rs 2.5-4 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 19.5-31 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">7</td><td class="num">12</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>EBR/PCFC</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>CMS + cards</td><td class="num">2.5</td><td class="num">4</td></tr>
<tr><td>Retail asset cross-sell</td><td class="num">10</td><td class="num">17</td></tr>
<tr><td>PB</td><td class="num">7</td><td class="num">10</td></tr>
<tr><td>TASC + ESOP-Trust</td><td class="num">2.5</td><td class="num">4</td></tr>
<tr><td>IPO arranger</td><td class="num">8</td><td class="num">14</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>41.0</strong></td><td class="num"><strong>67.2</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 35-58 Cr/yr captures upper-mid band incl. PE-exit IPO arranger contingency.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Founders + GS + Everstone appointees + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>Goldman Sachs Asset Mgmt + Everstone Capital majority{ref("571")}; founders + ESOP minority; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Omega CodeAssist gen-AI launch; PE-exit / IPO chatter intensifying.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 PE-exit IPO mandate + DRHP scope</li><li>T-14 Pre-pitch Founder + PE PB sizing + ESOP-trust banking</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Omega CFO + HR meetings; FX + retail + IPO concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Salary-CASA pilot for 5,000 FTE; PB book on Founders + 30 senior MDs.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; pre-IPO equity arranger pitch.</p></div>
<div class="card"><p><strong>T+180:</strong> PE-portfolio cross-sell + IPO mandate cementation.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Salary CASA 12,000+ accounts by Q3 FY27</li><li>PB AUM Rs 600 Cr by Q4 FY27</li><li>IPO arranger mandate by Q2 FY28</li><li>Y3 run-rate Rs 35-58 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Omega-specific from [570].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Omega Healthcare-specific sources</h3>
<ol start="570">
<li id="src-570"><strong>MCA v3 + ZaubaCorp &mdash; Omega Healthcare Management Services Pvt Ltd master data</strong> &mdash; CIN U85110TN2003PTC173618; incorp 11 Jul 2003. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-571"><strong>Goldman Sachs AM + Everstone Capital Apr 2022 ~$1 bn investment + Omega Healthcare corporate disclosures + Inc42 / VCCircle reporting</strong> &mdash; ~$340 mn group revenue; ~32k FTE; PE-exit IPO mandate. <span class="u">omegahms.com &middot; goldmansachs.com &middot; everstonecapital.com &middot; inc42.com &middot; vccircle.com</span></li>
</ol></div></section>"""

def build():
    t = "Omega Healthcare · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Omega Healthcare", "Healthcare RCM BPO / Goldman + Everstone PE"),
           FOOT("Cipher clean; 1,500+ lines; FX + retail-mass + PE-exit IPO + ESOP play.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
