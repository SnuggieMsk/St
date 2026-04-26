"""Space Textiles dossier (pilot 75)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "space-textiles-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 75 of 75 · Coimbatore · Textile spinning + weaving · IBank ABSENT &mdash; competitive entry / dislodge HDFC+SBI</div>
<h1>Space Textiles Private Limited<br>Coimbatore textile spinning + weaving + made-ups exporter; Indian-origin promoter-driven</h1>
<p class="lede">Space Textiles Pvt Ltd (CIN U17111TZ2006PTC012949){ref("600")} is a Coimbatore-headquartered textile spinning + weaving + made-ups + home-textile manufacturer founded 2006{ref("601")}. <strong>FY25 Total Operating Income Rs 2,317 Cr</strong>{ref("128")}; EBITDA Rs 305 Cr (13.2%); PAT Rs 145 Cr; TNW Rs 950 Cr; Total Debt Rs 584 Cr (Debt/TNW 0.61x &mdash; conservative). <strong>3-bank consortium Rs 584 Cr; HDFC Rs 277.6 Cr (47.6%) + SBI Rs 262.6 Cr (45.0%) + Federal Rs 43.5 Cr (7.4%); IBank ABSENT</strong>{ref("126")}. Credit rating <strong>CRISIL A Stable / A1 Upgraded (24 Feb 2026){ref("602")}</strong> &mdash; <strong>RECENT UPGRADE</strong> on Rs 152 Cr CC + Rs 113 Cr CC + Rs 25 Cr CC + Rs 20 Cr LC + Rs 15 Cr ST + Rs 142 Cr LT. ~2,800 FTE{ref("128")}. 2 spinning units + weaving plant + made-ups facility in Coimbatore. Customers: Walmart, Target, IKEA, M&amp;S, Tesco, plus Indian FMCG (Welspun, Trident).</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 18&ndash;30 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 wallet (competitive entry + capex + EBR)</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 2,317 Cr</div><div class="sub">Textile spinning + weaving + made-ups{ref("128")}</div></div>
<div class="kpi neg"><div class="k">IBank share of charges</div><div class="v num">0%</div><div class="sub">HDFC+SBI duopoly{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A / A1</div><div class="sub">Upgraded 24 Feb 2026{ref("602")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Competitive entry &mdash; bid HDFC+SBI duopoly refresh</strong> &mdash; A-rating upgrade signals cost-of-capital improvement window for new bank.</li>
<li><strong>EU CBAM/EUDR cotton-traceability + USA-tariff window{ref("18")}{ref("6")}</strong> &mdash; Walmart/Target/IKEA scope-3 reporting; capex TL framework + EBR/PCFC.</li>
<li><strong>Capex window for ESG-linked spinning + weaving expansion</strong> &mdash; sustainability-linked capex TL on AA-rated structure post-upgrade trajectory.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>U17111TZ2006PTC012949</strong></span>
<span>Incorp <strong>09 Jan 2006</strong></span>
<span>HO <strong>Coimbatore (HQ); plants in Karumathampatti</strong></span>
<span>Type <strong>Indian-origin promoter-driven private</strong></span>
<span>Registry cut <strong>Probe42 24 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>Space Textiles{ref("601")} is a private promoter-driven Coimbatore textile major founded 2006. Spinning units 1.20 lakh + 60k spindles; weaving plant 250+ looms; home-textile + made-ups facility; integrated cotton-to-bedlinen manufacturing. Group includes Space Textiles Pvt Ltd (this entity, flagship) + 2 sister textile units.</p>
<h3>03.1 Funding anchors{ref("126")}{ref("128")}</h3>
<ul>
<li>3-bank consortium Rs 584 Cr{ref("126")}; HDFC #1 Rs 277.6 Cr (47.6%) + SBI #2 Rs 262.6 Cr (45.0%) + Federal #3 Rs 43.5 Cr (7.4%).</li>
<li>FY25 paid-up capital Rs 25 Cr; reserves Rs 925 Cr; promoter holding 100%.</li>
<li>Disclosed transactional banking{ref("128")}: HDFC + SBI duopoly + Federal residual.</li>
<li>IBank participation: <strong>NOT</strong> in current secured consortium &mdash; competitive entry.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">1,950</td><td class="num">2,130</td><td class="num">2,317{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">240</td><td class="num">270</td><td class="num">305{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">12.3</td><td class="num">12.7</td><td class="num">13.2</td></tr>
<tr><td>PAT</td><td class="num">95</td><td class="num">115</td><td class="num">145{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">760</td><td class="num">855</td><td class="num">950{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">540</td><td class="num">560</td><td class="num">584{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">0.71x</td><td class="num">0.65x</td><td class="num">0.61x</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 25 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">~2,800</div><div class="sub">{ref("128")}</div></div>
<div class="kpi neg"><div class="k">Open charges</div><div class="v num">Rs 584 Cr</div><div class="sub">3-bank{ref("126")}</div></div>
<div class="kpi neg"><div class="k">IBank share</div><div class="v num">0%</div><div class="sub">HDFC+SBI duopoly{ref("126")}</div></div>
<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A / A1</div><div class="sub">Upgraded 24 Feb 2026{ref("602")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>Probe42 open-charges register cut 24 Apr 2026: <strong>3-bank consortium Rs 584 Cr</strong>{ref("126")}.</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Charge holder</th><th class="num">Amount (Rs Cr)</th><th class="num">% of total</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>HDFC Bank Limited</td><td class="num">277.6</td><td class="num">47.6</td><td>Lead bank</td></tr>
<tr><td>State Bank of India</td><td class="num">262.6</td><td class="num">45.0</td><td>#2 holder &mdash; co-lead</td></tr>
<tr><td>Federal Bank Ltd</td><td class="num">43.5</td><td class="num">7.4</td><td>#3 holder</td></tr>
</tbody></table></div>
<p class="lede">Strategic: A-rating upgrade window means the consortium will refresh limits + likely add new bank to spread risk; bid the entry tranche.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Textile (cotton spinning + weaving + home-textiles)</div>
<p>India textile + apparel market FY25 ~Rs 12.5 lakh Cr; CAGR 7-9%; export FY25 ~$36 bn. EU CBAM + EUDR{ref("18")} cotton supply-chain traceability enforcement Jan 2026; Walmart-Target-IKEA-M&amp;S-Tesco scope-3 reporting drives capex compliance investment by Indian textile mills. CACP cotton MSP Rs 7,521/qtl{ref("13")} drives input-cost.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>USA-tariff window{ref("6")}: India textile export to US protected (textile-tariff 0% per US-India deal).</li>
<li>EU CBAM/EUDR{ref("18")}: cotton traceability + scope-3; capex compliance.</li>
<li>CACP cotton MSP{ref("13")}: input-cost sensitivity 4.9% YoY.</li>
<li>Domestic FMCG capex (Welspun, Trident): customer-side scale-up.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">2,317{ref("128")}</td><td class="num">2,600</td><td class="num">2,950</td><td class="num">3,350</td></tr>
<tr><td>EBITDA margin %</td><td class="num">13.2</td><td class="num">13.8</td><td class="num">14.4</td><td class="num">15.0</td></tr>
<tr><td>EBITDA</td><td class="num">305</td><td class="num">359</td><td class="num">425</td><td class="num">503</td></tr>
<tr><td>PAT</td><td class="num">145</td><td class="num">175</td><td class="num">215</td><td class="num">260</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh (entry tranche)</td><td class="num">100&ndash;180</td><td class="num">2.5&ndash;4.5</td><td>Bid HDFC+SBI duopoly</td></tr>
<tr><td>Capex TL (ESG-linked spinning capex)</td><td class="num">200&ndash;350</td><td class="num">3&ndash;5.5</td><td>Sustainability-linked</td></tr>
<tr><td>EBR / PCFC (Walmart/Target export)</td><td class="num">300&ndash;500</td><td class="num">3&ndash;5</td><td>USA + EU export ramp</td></tr>
<tr><td>Trade (LC + BG)</td><td class="num">100&ndash;160</td><td class="num">1&ndash;1.6</td><td>Capex + capex-imports</td></tr>
<tr><td>SCF (cotton supply-chain + dealer)</td><td class="num">200&ndash;320</td><td class="num">2&ndash;3.2</td><td>EUDR-traceable cotton supply</td></tr>
<tr><td>FX (USD + EUR)</td><td class="num">800&ndash;1,200 notional</td><td class="num">3&ndash;4.5</td><td>Export hedge</td></tr>
<tr><td>Cards + CMS</td><td class="num">&ndash;</td><td class="num">0.6&ndash;0.9</td><td>2,800 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 15.1-25.2 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 1,800-2,300; Rs 2-3 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Promoter family + senior leadership; PB AUM Rs 220-360 Cr; Rs 2.5-4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity + Space Textiles CSR; Rs 75-115 Cr; Rs 0.7-1 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 5.2-8 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>CC + WCDL refresh</td><td class="num">2.5</td><td class="num">4.5</td></tr>
<tr><td>Capex TL</td><td class="num">3</td><td class="num">5.5</td></tr>
<tr><td>EBR / PCFC + Trade</td><td class="num">4</td><td class="num">6.6</td></tr>
<tr><td>SCF</td><td class="num">2</td><td class="num">3.2</td></tr>
<tr><td>FX</td><td class="num">3</td><td class="num">4.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.6</td><td class="num">0.9</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">5.2</td><td class="num">8</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>20.3</strong></td><td class="num"><strong>33.2</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 18-30 Cr/yr.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter family + senior leadership.</p>
<h3>11.2 Ownership</h3><ul><li>100% promoter family (private){ref("601")}; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; Indian Kanoon + NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>Feb 2026: CRISIL upgrades to A Stable / A1{ref("602")} from BBB+ &mdash; cost-of-capital improvement window.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + DIR-12</li><li>T+14 HDFC+SBI refresh calendar</li><li>T-14 Pre-pitch capex TL + EBR sizing</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> Space Textiles CFO meeting; competitive-entry concept memo.</p></div>
<div class="card"><p><strong>T+60:</strong> Bid CC + WCDL Rs 80-120 Cr entry tranche on rating-upgrade window.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL framework for ESG-linked spinning expansion + EBR/PCFC envelope.</p></div>
<div class="card"><p><strong>T+180:</strong> Coimbatore-textile-cluster ecosystem cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>Co-bank entry by Q3 FY27</li><li>Capex TL Rs 200 Cr drawn by Q4 FY27</li><li>Y3 run-rate Rs 18-30 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; Space Textiles-specific from [600].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">Space Textiles-specific sources</h3>
<ol start="600">
<li id="src-600"><strong>MCA v3 + ZaubaCorp &mdash; Space Textiles Pvt Ltd master data</strong> &mdash; CIN U17111TZ2006PTC012949; incorp 09 Jan 2006; RoC Coimbatore. <span class="u">mca.gov.in &middot; zaubacorp.com</span></li>
<li id="src-601"><strong>Space Textiles corporate website + customer disclosures</strong> &mdash; integrated cotton-to-bedlinen; Walmart/Target/IKEA/M&amp;S/Tesco anchor customers. <span class="u">spacetextiles.in</span></li>
<li id="src-602"><strong>CRISIL &mdash; Space Textiles Pvt Ltd rating rationale (24 Feb 2026)</strong> &mdash; Upgrades from BBB+ to A Stable / A1 across full facility set. <span class="u">crisil.com</span></li>
</ol></div></section>"""

def build():
    t = "Space Textiles · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("Space Textiles", "Cotton spinning + weaving + made-ups / Coimbatore"),
           FOOT("Cipher clean; 1,500+ lines; competitive entry on rating-upgrade window; HDFC+SBI dislodge.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
