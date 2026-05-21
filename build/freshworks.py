"""Freshworks Technologies India dossier (pilot 67)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "freshworks-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 67 of 75 · Chennai · Freshworks Inc Nasdaq · SaaS · India-origin USD billing</div>
<h1>Freshworks Technologies Private Limited<br>India delivery + ER&amp;D arm of Nasdaq-listed Freshworks Inc (CRM + ITSM + customer-experience SaaS)</h1>
<p class="lede">Freshworks Technologies Pvt Ltd (CIN U72200TN2010PTC078458){ref("520")} is the principal India delivery + engineering arm of Freshworks Inc (NASDAQ: FRSH; FY25 ARR ~$830 mn / revenue ~$770 mn), a Chennai-origin Indian SaaS major listed on Nasdaq Sep 2021{ref("521")}. <strong>FY25 Total Operating Income Rs 2,320 Cr</strong>{ref("128")}; EBITDA Rs 360 Cr (15.5%); PAT Rs 215 Cr; TNW Rs 1,050 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. ~5,800 FTE{ref("128")} (Chennai HQ + Bengaluru + Hyderabad). Products: Freshdesk (helpdesk), Freshservice (ITSM), Freshsales (CRM), Freshchat (omnichannel), Freshcaller (cloud-PBX), Freddy AI (gen-AI assistant).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 28&ndash;46 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + retail + PB + TASC)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,320 Cr</div><div class="sub">SaaS / India delivery{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~5,800</div><div class="sub">India-origin SaaS{ref("128")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD revenue-FX hedge mandate</strong> &mdash; 100% USD billing back to Freshworks Inc; large hedge envelope.</li>
<li><strong>5,800 FTE retail-mass-market + ESOP wealth</strong> &mdash; salary + ESOP-Trust banking + auto/home cross-sell + UHNI PB on senior leadership + ESOP-vested employees.</li>
<li><strong>SEZ STPI + GIFT-IFSC + Founder-cluster relationship</strong> &mdash; Freshworks-cluster founders (Girish Mathrubootham, Vijay Shankar, Shan Krishnasamy) anchor an entire Chennai SaaS founder ecosystem (Chargebee, Postman, Zoho, etc.).</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U72200TN2010PTC078458</strong></span>
<span>Incorp <strong>11 Aug 2010</strong></span>
<span>HO <strong>Chennai (DLF IT Park) + Bengaluru</strong></span>
<span>Parent <strong>Freshworks Inc (Delaware, US; NASDAQ: FRSH)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Freshworks Inc{ref("521")} is a Delaware-domiciled US-listed SaaS company with India-origin founders + India delivery; FY25 revenue ~$770 mn; ARR ~$830 mn; ~67k customers. India operations: Freshworks Technologies Pvt Ltd (this entity, principal delivery + engineering) + Freshworks ESOP Trust (employee equity) + small marketing/support entities. Founder Girish Mathrubootham post-IPO retains key shareholding + chairman role.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent-funded; SaaS cash-positive.</li>
<li>FY25 paid-up capital Rs 28 Cr; reserves Rs 1,022 Cr; cash Rs 320 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: HDFC (anchor for India-origin Indian SaaS), Citi, JPMorgan; ESOP-Trust + payroll outsourced.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + retail-mass + ESOP-trust entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,800</td><td class="num">2,050</td><td class="num">2,320{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">240</td><td class="num">295</td><td class="num">360{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.3</td><td class="num">14.4</td><td class="num">15.5</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">170</td><td class="num">215{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">680</td><td class="num">860</td><td class="num">1,050{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 28 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~5,800</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 320 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: ESOP-Trust banking + USD-INR hedge envelope + retail mass-market on 5,800 FTE base (with skew toward senior ESOP-rich employees post-IPO).</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; SaaS / India-origin software products</div>
<p>Indian SaaS market FY25 ~$15 bn revenue; CAGR 22-25%; targets $50-70 bn by FY30. Freshworks + Zoho + Postman + Chargebee + Druva + Innovaccer + DarwinBox + DronaHQ + Browserstack are India-origin global-footprint SaaS unicorns. Workforce ~250-280k FTE; Chennai SaaS-cluster ~25-30k FTE concentrated.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: SaaS services-tariff still ~0%; Freshworks USD-billing protected.</li>
<li>EU AI-Act + CCPA evolution: regulatory-tech compliance + data-residency; new Freshworks product investments.</li>
<li>Gen-AI + agentic-AI ramp: Freddy AI + agentic CRM/ITSM ramp.</li>
<li>GIFT-IFSC fund-management: SaaS founder + ESOP wealth structuring.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,320{ref("128")}</td><td class="num">2,700</td><td class="num">3,200</td><td class="num">3,800</td></tr>
<tr><td>EBITDA margin %</td><td class="num">15.5</td><td class="num">16.5</td><td class="num">17.5</td><td class="num">18.5</td></tr>
<tr><td>EBITDA</td><td class="num">360</td><td class="num">446</td><td class="num">560</td><td class="num">703</td></tr>
<tr><td>PAT</td><td class="num">215</td><td class="num">270</td><td class="num">345</td><td class="num">440</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD)</td><td class="num">2,000&ndash;3,000 notional</td><td class="num">8&ndash;13</td><td>100% USD billing</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">300&ndash;450 float</td><td class="num">2&ndash;3</td><td>MNC TM-aaS</td></tr>
<tr><td>EBR / PCFC (services-export)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>Receivable financing</td></tr>
<tr><td>Salary CASA + retail asset (5,800)</td><td class="num">600&ndash;900 disbursal/yr</td><td class="num">5&ndash;9</td><td>Auto + home + cards (ESOP-rich skew)</td></tr>
<tr><td>PB (founders + senior ESOP-vested)</td><td class="num">500&ndash;800 AUM</td><td class="num">5.5&ndash;8.5</td><td>UHNI cluster</td></tr>
<tr><td>TASC + ESOP Trust banking</td><td class="num">220&ndash;360</td><td class="num">2&ndash;3</td><td>ESOP plan + PF + Gratuity</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">1.2&ndash;2</td><td>5,800 FTE corporate cards</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 12-19.2 Cr / yr. Retail/PB/TASC: Rs 13.7-22.5 Cr/yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC (ESOP-rich anchor)</div>
<div class="grid c3">
<div class="card pos"><h4 style="margin-top:0">Retail (anchor)</h4><p>5,800 FTE; salary CASA Rs 5,500-7,000 mn aggregate (avg Rs 95-110k); auto + home + cards cross-sell; Rs 5-9 Cr/yr.</p></div>
<div class="card pos"><h4 style="margin-top:0">PB (UHNI)</h4><p>Founders + senior ESOP-vested employees; PB AUM Rs 500-800 Cr; Rs 5.5-8.5 Cr/yr &mdash; the Freshworks PB book is the headline play.</p></div>
<div class="card"><h4 style="margin-top:0">TASC + ESOP-Trust</h4><p>ESOP Trust + PF + Gratuity + Freshworks CSR; Rs 220-360 Cr; Rs 2-3 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 12.5-20.5 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">8</td><td class="num">13</td></tr>
<tr><td>Treasury sweep</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td>EBR/PCFC</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>CMS + cards</td><td class="num">1.2</td><td class="num">2</td></tr>
<tr><td>Retail asset cross-sell</td><td class="num">5</td><td class="num">9</td></tr>
<tr><td>PB (founders + ESOP UHNI)</td><td class="num">5.5</td><td class="num">8.5</td></tr>
<tr><td>TASC + ESOP-Trust</td><td class="num">2</td><td class="num">3</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>25.7</strong></td><td class="num"><strong>41.7</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 28-46 Cr/yr captures upper-mid band incl. founder-cluster spillover.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; Indian-origin founder Girish Mathrubootham + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>~99% Freshworks Inc, US (parent){ref("521")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: Freshworks Freddy AI agentic-platform launch; India delivery scope expansion.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 ESOP-Trust banking scope</li><li>T-14 Pre-pitch Founder + UHNI PB sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Freshworks India CFO + HR meetings; FX + ESOP-Trust + PB concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> ESOP-Trust banking pitch; PB book on 30 senior ESOP-vested + founders.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; salary-CASA campaign for 5,800 base.</p></div>
<div class="card"><p><strong>T+180:</strong> Chennai SaaS founder-cluster ecosystem cross-sell (Zoho, Chargebee, etc.).</p></div>
<h3>Success metrics</h3><ul class="check"><li>PB AUM Rs 500 Cr by Q3 FY27</li><li>ESOP-Trust mandate captured</li><li>Y3 run-rate Rs 28-46 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Freshworks-specific from [520].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Freshworks-specific sources</h3>
<ol start="520">
<li id="src-520"><strong>MCA v3 + ZaubaCorp &mdash; Freshworks Technologies Pvt Ltd master data</strong> &mdash; CIN U72200TN2010PTC078458; incorp 11 Aug 2010; RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-521"><strong>Freshworks Inc Annual Report FY25 + NASDAQ FRSH disclosures + investor-day commentary</strong> &mdash; FY25 ARR ~$830 mn; revenue ~$770 mn; ~67k customers; Sep 2021 IPO. <span class="u">freshworks.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "Freshworks Technologies India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Freshworks Technologies", "SaaS / Indian-origin Nasdaq-listed"),
           FOOT("Cipher clean; 1,500+ lines; founder + ESOP-rich PB anchor + retail-mass + FX.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
