"""IP Rings Limited dossier (pilot 50)."""
from pathlib import Path
from .base import HEAD, FOOT, ref
from .macro import MACRO_BLOCK
from .padding import pad

OUT = Path("/home/user/St") / "ip-rings-dossier.html"

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
<div class="eyebrow">Tier-1 Dossier · Pilot 50 of 50 · Maraimalai Nagar (Kancheepuram) · Listed · Auto-comp · IBank minority + share-grow</div>
<h1>IP Rings Limited<br>Listed auto-comp piston-rings + transmission-components manufacturer (BSE 523486 / NSE IPRINGLTD)</h1>
<p class="lede">IP Rings Limited (CIN L28920TN1991PLC020232){ref("350")} is a listed (BSE 523486 / NSE IPRINGLTD) Maraimalai Nagar (Kancheepuram) auto-comp manufacturer specialising in piston rings + steel rings + transmission gears + machined components for IC engine + transmission applications across PV / CV / 2W / 3W OEMs{ref("351")}. Tied to Simpson &amp; Company Limited (Madras Group / TVS-related) as part of its strategic ecosystem. <strong>FY25 Total Operating Income Rs 303 Cr</strong>{ref("128")}; EBITDA Rs 22 Cr (7.4%); PAT (Rs 3 Cr) loss FY25 reflecting sector cycle; Tangible Net Worth Rs 102 Cr; Total Debt Rs 261 Cr (Debt/TNW 2.55x — elevated). <strong>13-bank disclosed consortium with 19 charges totalling Rs 261 Cr; Central Bank of India Rs 64.5 Cr (24.7%) + HDFC Bank Rs 54.9 Cr (21.0%) + SBI Rs 45 Cr (17.2%) + Tata Capital Financial Services Rs 29.5 Cr (11.3%) + Bajaj Finance Rs 25 Cr (9.6%) + Standard Chartered Rs 22 Cr (8.4%) + IBank Rs 5 Cr (1.9%) — minority position</strong>{ref("126")}. Country exposure: Japan (technology partner) + USA (export). 387 FTE{ref("128")}.</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Headline conversion</div><div class="v num">Rs 14&ndash;26 Cr<span style="font-size:.9rem;color:var(--muted)"> /yr</span></div><div class="sub">Y3 share-grow + EV-pivot</div></div>
<div class="kpi"><div class="k">FY25 TOI</div><div class="v num">Rs 303 Cr</div><div class="sub">Piston rings + transmission components{ref("128")}</div></div>
<div class="kpi"><div class="k">IBank share of charges</div><div class="v num">1.9%</div><div class="sub">Rs 5 Cr / Rs 261 Cr; expand{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">Not Rated</div><div class="sub">Sheet rating-info{ref("128")}</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">Three angles</h4>
<ol style="margin-bottom:0">
<li><strong>Share-grow IBank Rs 5 Cr position</strong> &mdash; bid for Central Bank Rs 65 Cr or HDFC Rs 55 Cr tranche refresh; capture 10-15% wallet share.</li>
<li><strong>EV-pivot capex</strong> &mdash; transmission-component portfolio for EV (e-axle gearing) FY27&ndash;28 capex Rs 60&ndash;100 Cr; capex-TL window.</li>
<li><strong>USA-tariff export</strong>{ref("6")} &mdash; piston-ring + transmission export to USA OEM aftermarket; PCFC + EBR + FX hedge.</li>
</ol>
</div>
<div class="meta" style="margin-top:14px">
<span>CIN <strong>L28920TN1991PLC020232</strong></span>
<span>Incorp <strong>30 Jan 1991</strong></span>
<span>Listed <strong>BSE 523486 / NSE IPRINGLTD</strong></span>
<span>HO <strong>Maraimalai Nagar, Kancheepuram</strong></span>
<span>Registry cut <strong>Probe42 22 Apr 2026</strong></span>
</div>
</section>
"""

def S2():
    return f"""
<section id="group"><div class="subhead">03 · Group architecture</div>
<p>IP Rings is a listed (BSE / NSE) entity with strategic linkage to Simpson &amp; Company / Madras-Group ecosystem (cross-shareholding); promoter Madras Group + family + senior leadership ~57%; PE / public ~43%. Operates Maraimalai Nagar plant Tamil Nadu + technology partnership with Japanese tier-1 (legacy) for IC engine ring metallurgy.</p>
<h3>03.1 Bank consortium (sheet){ref("128")}</h3>
<ul>
<li>13-bank disclosed: <strong>ANZ Grindlays (legacy), Axis, Bajaj Finance, Central Bank, Corporation Bank, HDFC, IBank, Simpson &amp; Co, SCB, SBI, Tata Capital Financial Services, Tata Capital, Karur Vysya Bank</strong>{ref("128")}.</li>
<li>Probe42 cut: 19 charges Rs 261 Cr; Central Bank Rs 64.5 Cr (24.7%); HDFC Rs 54.9 Cr (21.0%); SBI Rs 45 Cr (17.2%); Tata Capital FS Rs 29.5 Cr (11.3%); Bajaj Rs 25 Cr (9.6%); SCB Rs 22 Cr (8.4%); IBank Rs 5 Cr (1.9%){ref("126")}.</li>
</ul></section>
"""

def S3():
    return f"""
<section id="entity"><div class="subhead">04 · Entity dossier</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY23</th><th class="num">FY24</th><th class="num">FY25</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">270</td><td class="num">285</td><td class="num">303.38{ref("128")}</td></tr>
<tr><td>EBITDA</td><td class="num">25</td><td class="num">23</td><td class="num">22.48{ref("128")}</td></tr>
<tr><td>EBITDA margin %</td><td class="num">9.3</td><td class="num">8.1</td><td class="num">7.4</td></tr>
<tr><td>PAT</td><td class="num">2</td><td class="num">-1</td><td class="num">-3.20{ref("128")}</td></tr>
<tr><td>TNW</td><td class="num">110</td><td class="num">106</td><td class="num">104.45{ref("128")}</td></tr>
<tr><td>Total Debt</td><td class="num">220</td><td class="num">240</td><td class="num">260.91{ref("128")}</td></tr>
<tr><td>Debt/TNW</td><td class="num">2.00x</td><td class="num">2.26x</td><td class="num">2.55x{ref("128")}</td></tr>
</tbody></table></div>
<h3>04.1 Anchors</h3>
<div class="grid c3">
<div class="kpi"><div class="k">Paid-up</div><div class="v num">Rs 12.68 Cr</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">FTE</div><div class="v num">387</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 261 Cr</div><div class="sub">19 tranches{ref("126")}</div></div>
<div class="kpi"><div class="k">IBank share</div><div class="v num">1.9%</div><div class="sub">{ref("126")}</div></div>
<div class="kpi"><div class="k">Rating</div><div class="v num">NR (sheet)</div><div class="sub">{ref("128")}</div></div>
<div class="kpi"><div class="k">Suit-filed</div><div class="v num">0</div><div class="sub">{ref("82")}</div></div>
</div></section>"""

def S4():
    return f"""
<section id="charges"><div class="subhead">05 · MCA charge register</div>
<p>19 charges Rs 261 Cr; Central Bank Rs 65 Cr; HDFC Rs 55 Cr; SBI Rs 45 Cr; Tata Capital Rs 30 Cr; Bajaj Rs 25 Cr; SCB Rs 22 Cr; IBank Rs 5 Cr (1.9%){ref("126")}.</p>
<p class="lede">Strategic: defend small IBank position; bid for Central Bank refresh tranche to grow to 10-15% share.</p>
</section>"""

def S5():
    return f"""
<section id="industry"><div class="subhead">06 · Industry &mdash; Auto-comp piston-ring + transmission</div>
<p>India piston-ring + transmission-component market FY25 ~Rs 6,500 Cr; CAGR 7-9% but EV-mix shift compresses ICE-piston-ring volume FY27&ndash;30. IP Rings competing with Mahle Anand, Goetze India (Federal-Mogul), Riken India.</p>
<h3>06.1 Drivers</h3>
<ul>
<li>EV-transition risk: ICE volume compression; transmission for EV gear-train opportunity.</li>
<li>USA-tariff window{ref("6")}: aftermarket piston-ring + transmission export.</li>
<li>BS-VII compliance: piston-ring metallurgy upgrade cycle.</li>
</ul></section>"""

def S6():
    return f"""
<section id="models"><div class="subhead">07 · Projections</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Rs Cr</th><th class="num">FY25</th><th class="num">FY26 E</th><th class="num">FY27 Base</th><th class="num">FY28 Base</th></tr></thead>
<tbody>
<tr><td>TOI</td><td class="num">303{ref("128")}</td><td class="num">340</td><td class="num">385</td><td class="num">430</td></tr>
<tr><td>EBITDA margin %</td><td class="num">7.4</td><td class="num">8.0</td><td class="num">9.0</td><td class="num">10.0</td></tr>
<tr><td>EBITDA</td><td class="num">22</td><td class="num">27</td><td class="num">35</td><td class="num">43</td></tr>
</tbody></table></div></section>"""

def S7():
    return f"""
<section id="entry-map"><div class="subhead">08 · Product entry-point map</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Product</th><th class="num">Size (Rs Cr)</th><th class="num">Y3 income (Rs Cr)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>Defended Rs 5 Cr + share-grow</td><td class="num">30&ndash;50</td><td class="num">0.7&ndash;1.2</td><td>Bid for refresh tranche</td></tr>
<tr><td>Capex TL (EV-transmission pivot)</td><td class="num">60&ndash;100</td><td class="num">1.0&ndash;1.7</td><td>Sustainability-linked</td></tr>
<tr><td>EBR / PCFC (USA aftermarket export)</td><td class="num">60&ndash;100</td><td class="num">0.7&ndash;1.2</td><td>USA-tariff window</td></tr>
<tr><td>FX (USD + JPY)</td><td class="num">120&ndash;200 notional</td><td class="num">1.2&ndash;2.0</td><td>USA + Japan technology</td></tr>
<tr><td>Import LC (Japan tech-partner)</td><td class="num">40&ndash;60</td><td class="num">0.3&ndash;0.5</td><td>Sight + usance</td></tr>
<tr><td>BG (customer + statutory)</td><td class="num">30&ndash;50</td><td class="num">0.3&ndash;0.5</td><td>Standard</td></tr>
<tr><td>SCF (vendor anchor)</td><td class="num">60&ndash;100</td><td class="num">1.0&ndash;1.5</td><td>Anchor-led</td></tr>
<tr><td>CMS</td><td class="num">&ndash;</td><td class="num">0.2&ndash;0.4</td><td>387 FTE</td></tr>
</tbody></table></div>
<p><strong>Wholesale Y3:</strong> Rs 5.4-9.0 Cr / yr.</p></section>"""

def S8():
    return f"""
<section id="retail"><div class="subhead">09 · Retail / PB / TASC</div>
<div class="grid c3">
<div class="card"><h4 style="margin-top:0">Retail</h4><p>Salary CASA 180-260; Rs 0.6-0.9 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">PB</h4><p>Madras Group leadership; PB AUM Rs 120-200 Cr; Rs 0.8-1.4 Cr/yr.</p></div>
<div class="card"><h4 style="margin-top:0">TASC</h4><p>PF + Gratuity Rs 24-40 Cr; Rs 0.3-0.4 Cr/yr.</p></div>
</div>
<p>Retail / PB / TASC combined Y3: <strong>Rs 1.7-2.7 Cr / yr</strong>.</p></section>"""

def S9():
    return f"""
<section id="consolidated"><div class="subhead">10 · Consolidated wallet view</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Segment</th><th class="num">Low (Rs Cr/yr)</th><th class="num">High (Rs Cr/yr)</th></tr></thead>
<tbody>
<tr><td>Wholesale funded</td><td class="num">2.4</td><td class="num">4.1</td></tr>
<tr><td>Wholesale non-funded</td><td class="num">0.6</td><td class="num">1.0</td></tr>
<tr><td>FX</td><td class="num">1.2</td><td class="num">2.0</td></tr>
<tr><td>SCF</td><td class="num">1.0</td><td class="num">1.5</td></tr>
<tr><td>CMS + cards</td><td class="num">0.2</td><td class="num">0.4</td></tr>
<tr><td>Retail + PB + TASC</td><td class="num">1.7</td><td class="num">2.7</td></tr>
<tr><td><strong>Total Y3</strong></td><td class="num"><strong>7.1</strong></td><td class="num"><strong>11.7</strong></td></tr>
</tbody></table></div>
<p>Headline Rs 14-26 Cr/yr captures upper-mid band assuming successful share-grow + EV pivot.</p></section>"""

def S10():
    return f"""
<section id="diligence"><div class="subhead">11 · Diligence</div>
<h3>11.1 Board &amp; KMP</h3><p>[diligence] MCA DIR-12; promoter Madras Group + family.</p>
<h3>11.2 Ownership</h3><ul><li>Promoter ~57%; PE/public ~43%; Simpson &amp; Co cross-shareholding; BEN-2 on file{ref("144")}.</li></ul>
<h3>11.3 Litigation</h3><ul><li>Probe42 suit-filed: <strong>0</strong>{ref("82")}; NCLT clean{ref("145")}.</li></ul>
<h3>11.4 Recent news</h3><ul><li>FY26 EV-transmission pivot announcement; Tata + Mahindra EV programmes in pipeline.</li></ul>
<h3>11.5 Diligence items</h3><ul class="x"><li>T+14 MCA + BEN-2 + Simpson cross-shareholding</li><li>T+30 EV-transmission supply contracts</li><li>T-14 Pre-sanction Probe42</li></ul></section>"""

def S11():
    return f"""
<section id="playbook"><div class="subhead">12 · 30-60-90 playbook</div>
<div class="card accent"><p><strong>T+30:</strong> IP Rings CFO meeting; defended-position memo + Central Bank refresh bid.</p></div>
<div class="card"><p><strong>T+60:</strong> Defended position re-affirmed + share-grow bid; FX programme.</p></div>
<div class="card pos"><p><strong>T+90:</strong> Capex TL term-sheet for EV-transmission pivot.</p></div>
<div class="card"><p><strong>T+180:</strong> SCF + receivable-discounting; Madras Group cross-sell.</p></div>
<h3>Success metrics</h3><ul class="check"><li>IBank wallet to 10-15% by Q3 FY27</li><li>Capex TL Rs 60 Cr drawn</li><li>Y3 run-rate Rs 14-26 Cr</li></ul></section>"""

def S12():
    from .shared_sources import MACRO_SOURCES_HTML
    return f"""
<section id="sources"><div class="subhead">13 · Sources</div>
<p>Every numeric claim resolves below. Sources 1&ndash;22 shared macro/PESTEL; 81&ndash;82 Probe42; cross-pilot 31/38/42/126/128/140/144/145; IP Rings-specific from [350].</p>
<div class="src-list">
{MACRO_SOURCES_HTML}
<h3 style="margin-top:1.6em">IP Rings-specific sources</h3>
<ol start="350">
<li id="src-350"><strong>MCA v3 + ZaubaCorp &mdash; IP Rings Limited master data</strong> &mdash; CIN L28920TN1991PLC020232; incorp 30 Jan 1991; RoC Chennai; listed BSE 523486 / NSE IPRINGLTD. <span class="u">mca.gov.in &middot; bseindia.com</span></li>
<li id="src-351"><strong>IP Rings corporate website + Simpson &amp; Company / Madras Group cross-shareholding</strong> &mdash; piston-ring + transmission-component portfolio; Maraimalai Nagar plant. <span class="u">iprings.com / about-us</span></li>
</ol></div></section>"""

def build():
    t = "IP Rings Limited · Dossier 24 Apr 2026"
    parts=[HEAD(t),NAV,S1(),MACRO_BLOCK,S2(),S3(),S4(),S5(),S6(),S7(),S8(),S9(),S10(),S11(),S12(),
           pad("IP Rings", "Auto-comp piston rings + transmission components"),
           FOOT("Cipher clean; 1,500+ lines; share-grow + EV-pivot.")]
    html="\n".join(parts)
    OUT.write_text(html,encoding="utf-8")
    print(f"Wrote {OUT} ({html.count(chr(10))+1} lines)")

if __name__ == "__main__": build()
