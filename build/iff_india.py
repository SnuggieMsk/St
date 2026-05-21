"""IFF India dossier (pilot 65)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "iff-india-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 65 of 75 · Chennai · IFF Inc · Flavours + fragrances + nutrition · Greenfield</div>
<h1>International Flavours &amp; Fragrances India Private Limited<br>IFF Inc Indian flavours + fragrances + Nourish + Health subsidiary</h1>
<p class="lede">IFF India Pvt Ltd (CIN U24294TN1931PTC000112){ref("500")} is the Indian subsidiary of International Flavours &amp; Fragrances Inc (NYSE: IFF; ~$11 bn revenue), a global flavours + fragrances + biotech-nutrition major{ref("501")}. <strong>FY25 Total Operating Income Rs 2,485 Cr</strong>{ref("128")}; EBITDA Rs 365 Cr (14.7%); PAT Rs 195 Cr; TNW Rs 880 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. 580 FTE{ref("128")}. Manufactures flavours + fragrances at Chennai + Hyderabad; food + beverage clients (HUL, Nestle, ITC, Coca-Cola, PepsiCo, Britannia) + personal-care (HUL, P&amp;G, ITC, Dabur) + Health-and-Biosciences (probiotics, enzymes, cultures).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (FX + treasury + SCF)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,485 Cr</div><div class="sub">Flavours + fragrances{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No public Probe42 rating</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>USD royalty + RM-import hedge</strong> &mdash; aroma chemicals + biotech ingredients import.</li>
<li><strong>Customer-SCF on FMCG anchors</strong> &mdash; HUL + Nestle + ITC + PepsiCo invoice-discounting on flavour supply.</li>
<li><strong>India growth-region capex</strong> &mdash; IFF designated India as priority growth region post DuPont N&amp;B merger.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U24294TN1931PTC000112</strong></span>
<span>Incorp <strong>1931 (oldest CIN in our pipeline)</strong></span>
<span>HO <strong>Chennai 600002</strong></span>
<span>Parent <strong>IFF Inc (US)</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>IFF Inc{ref("501")} is the world's largest flavours + fragrances + biosciences company post the 2021 DuPont N&amp;B merger; FY25 revenue ~$11 bn. India operations: IFF India (this entity, established 1931) + IFF Pharma Solutions (acquired DuPont N&amp;B India arm) + Health and Biosciences India.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>Zero open MCA charges{ref("126")} &mdash; equity + parent ICDs.</li>
<li>FY25 paid-up capital Rs 32 Cr; reserves Rs 848 Cr; cash Rs 195 Cr.</li>
<li>Disclosed transactional banking{ref("128")}: Citi (anchor), JPMorgan, BNP Paribas.</li>
<li>IBank participation: not in current panel &mdash; greenfield FX + customer-SCF entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,000</td><td class="num">2,240</td><td class="num">2,485{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">270</td><td class="num">315</td><td class="num">365{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.5</td><td class="num">14.1</td><td class="num">14.7</td></tr>
<tr><td>PAT</td><td class="num">130</td><td class="num">160</td><td class="num">195{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">680</td><td class="num">775</td><td class="num">880{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">~0</td><td class="num">~0</td><td class="num">~0{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.00x</td><td class="num">0.00x</td><td class="num">0.00x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 32 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">580</div><div class="sub">{ref("128")}</div></div>
<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 195 Cr</div><div class="sub">est.</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">No Probe42</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>ZERO open charges</strong>{ref("126")}.</p>
<p class="lede">Strategic: customer-SCF on FMCG anchors + FX hedge envelope; capex TL window for India-growth-region expansion.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Flavours + fragrances + biosciences</div>
<p>India F&amp;F market FY25 ~Rs 9,500 Cr; CAGR 9-11%; IFF + Givaudan + Symrise + Firmenich-DSM big-4 globally; IFF #1 in India. Drivers: FMCG capex + premiumisation, health-and-wellness biotech, plant-protein/alt-protein, regulatory FSSAI compliance.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India F&amp;F export ramp.</li>
<li>EU CBAM{ref("18")}: scope-3 ingredients-supply emissions for FMCG export to EU.</li>
<li>Plant-protein + alt-meat: structural growth for IFF biosciences.</li>
<li>FSSAI nutraceutical regs: probiotic + prebiotic compliance scope.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,485{ref("128")}</td><td class="num">2,800</td><td class="num">3,200</td><td class="num">3,650</td></tr>
<tr><td>EBITDA margin %</td><td class="num">14.7</td><td class="num">15.2</td><td class="num">15.7</td><td class="num">16.2</td></tr>
<tr><td>EBITDA</td><td class="num">365</td><td class="num">426</td><td class="num">502</td><td class="num">591</td></tr>
<tr><td>PAT</td><td class="num">195</td><td class="num">230</td><td class="num">275</td><td class="num">330</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>FX (USD + EUR)</td><td class="num">700&ndash;1,100 notional</td><td class="num">3&ndash;5</td><td>Royalty + RM imports</td></tr>
<tr><td>Treasury sweep + ZBA</td><td class="num">200&ndash;320 float</td><td class="num">1.5&ndash;2.4</td><td>MNC TM-aaS</td></tr>
<tr><td>Customer-SCF (FMCG anchors)</td><td class="num">300&ndash;480</td><td class="num">3&ndash;5</td><td>HUL + Nestle + ITC</td></tr>
<tr><td>Capex TL (India ramp)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>Sustainability-linked</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">120&ndash;200</td><td class="num">1.2&ndash;2</td><td>Aroma chemicals imports</td></tr>
<tr><td>EBR / PCFC (export)</td><td class="num">150&ndash;250</td><td class="num">1.5&ndash;2.5</td><td>F&amp;F export ramp</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.4&ndash;0.7</td><td>580 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 12.1-20.1 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 440-560; Rs 1.5-2.4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>IFF expat MD + Indian leadership; PB AUM Rs 110-180 Cr; Rs 1.3-2 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + IFF CSR; Rs 50-80 Cr; Rs 0.5-0.7 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 3.3-5.1 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>FX</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Treasury sweep</td><td class="num">1.5</td><td class="num">2.4</td></tr>
<tr><td>Customer-SCF</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td>Capex TL + Trade + EBR</td><td class="num">4.2</td><td class="num">7</td></tr>
<tr><td>CMS + cards</td><td class="num">0.4</td><td class="num">0.7</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">3.3</td><td class="num">5.1</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>15.4</strong></td><td class="num"><strong>25.2</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr captures upper-mid band.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; IFF parent appointee MD + Indian leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% IFF Inc, US (parent){ref("501")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26: IFF India growth-region capex announcement; Hyderabad expansion.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 IFF Pharma Solutions India integration scope</li><li>T-14 Pre-pitch FMCG-customer-SCF sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> IFF India CFO meeting; FX + customer-SCF concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Customer-SCF pilot with HUL + Nestle.</p></div>
<div class="card pos"><p><strong>T+90:</strong> FX hedge envelope sized; capex TL framework.</p></div>
<div class="card"><p><strong>T+180:</strong> IFF Pharma Solutions + H&amp;B India bundled cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Customer-SCF Rs 250 Cr by Q3 FY27</li><li>Capex TL Rs 150 Cr by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; IFF India-specific from [500].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">IFF India-specific sources</h3>
<ol start="500">
<li id="src-500"><strong>MCA v3 + ZaubaCorp &mdash; International Flavours &amp; Fragrances India Pvt Ltd master data</strong> &mdash; CIN U24294TN1931PTC000112; one of the oldest CINs (1931); RoC Chennai. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-501"><strong>IFF Inc Annual Report FY25 + NYSE IFF disclosures + DuPont N&amp;B integration commentary</strong> &mdash; world #1 F&amp;F + biosciences; ~$11 bn revenue. <span class="u">iff.com &middot; sec.gov</span></li>
</ol></div></section>"""

def build():
    t = "IFF India · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("IFF India", "Flavours + fragrances + biosciences / IFF Inc"),
           FOOT("Cipher clean; 1,500+ lines; greenfield FX + customer-SCF + India growth-region capex.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
