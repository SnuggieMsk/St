"""The KCP Limited dossier — pilot 172, Velagapudi family conglomerate."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=172, name="The KCP Limited", slug="kcp-limited",
    title="The KCP Limited · Dossier 28 Apr 2026",
    cin="L65991TN1941PLC001128", parent="Velagapudi family (V.L. Dutt + V. Kavitha Dutt + family)",
    pad_label="The KCP Limited", pad_sector="Cement / Sugar / Heavy Engineering / Hospitality / Captive Power",
    eyebrow_extras="Chennai HO · Listed BSE 590066 / NSE KCP · Velagapudi family · 84-yr conglomerate · 5-business platform",
    headline_sub="84-year Velagapudi family multi-business conglomerate; FY24 revenue Rs 2,846 Cr; FY25 Rs 2,529 Cr; cement (2.2 MT) + sugar + heavy engineering + Vietnam ops + hotels",
    lede=f'The KCP Limited (CIN L65991TN1941PLC001128){ref("1055")} is the flagship listed entity of the <strong>Velagapudi family conglomerate</strong> &mdash; one of South India\'s longest-standing industrial-family groups (founded 1941). Listed BSE 590066 / NSE KCP{ref("1055")}; promoter holding 44.25% (Mar 2025); HQ Ramakrishna Buildings, 2 Dr P.V. Cherian Crescent Road, Egmore, Chennai 600 008. <strong>FY24 consolidated revenue Rs 2,846 Cr</strong>{ref("128")}; FY24 PAT Rs 280 Cr; FY25 revenue Rs 2,529 Cr; FY25 PAT Rs 253 Cr; FY24 networth Rs 1,410 Cr (FY25 Rs 1,533 Cr); FY24 total debt Rs 480 Cr (FY25 Rs 542 Cr); ROCE 13% FY25; cash conversion cycle ~175 days. KCP is a <strong>5-business multi-segment conglomerate</strong>: <strong>(1) Cement</strong> (60+ year business; 2.2 MTPA combined capacity; plants at Macherla + Mukthyala in Andhra Pradesh; premium-grade cement); <strong>(2) Sugar + Vietnam Operations</strong> (KCP Vietnam Industries Ltd manages two sugar plants in Vietnam &mdash; the Phu Yen + Son Hoa plants; one of India\'s few sugar-companies with international manufacturing); <strong>(3) Heavy Engineering</strong> (60+ years; integrated Steel Foundry + Build-to-Order heavy-equipment manufacturing 9 km from Chennai port; FIVES CAIL-KCP JV with Fives Group France for turnkey sugar plants + power plants); <strong>(4) Hospitality</strong> (Mercure Hyderabad KCP hotel and group ventures); <strong>(5) Captive Power Generation</strong> (cogen + thermal for cement + sugar). 84-year arc has built one of India\'s longer-running industrial-family multi-business platforms.',
    headline_low=14, headline_high=26,
    headline_strap="Y3 wallet (cement + Vietnam capex + heavy engineering + Velagapudi family-PB)",
    industry_short="Cement / Sugar / Heavy Engineering / Hospitality / Captive Power",
    kpi3='<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs ~480 Cr</div><div class="sub">Multi-bank multi-segment' + ref("126") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A</div><div class="sub">[verify FY26 review Dec 2025]' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Cement capex Rs 200-400 Cr</strong> &mdash; Macherla + Mukthyala capacity refresh + WHRS (waste-heat recovery) + AFR (alternative-fuel-and-raw-material); UltraTech-India Cements consolidation creates urgency for cost-discipline + capex.",
        "<strong>Vietnam sugar operations multi-currency banking</strong> &mdash; KCP Vietnam Industries Ltd in Phu Yen + Son Hoa; VND/USD/INR FX desk; rare cross-border sugar manufacturing.",
        "<strong>Heavy engineering BG + customer-LC</strong> &mdash; FIVES CAIL-KCP turnkey sugar/power plants for global customers; Steel Foundry; export USD receivable factoring.",
    ],
    incorp_date="22 Jul 1941",
    ho_text="Ramakrishna Buildings, 2 Dr P.V. Cherian Crescent Road, Egmore, Chennai 600 008",
    group_text=f'Velagapudi-family-controlled multi-business conglomerate{ref("1055")}. Operating subsidiaries: <strong>KCP Vietnam Industries Limited</strong> (Vietnam sugar operations; Phu Yen + Son Hoa plants); <strong>FIVES CAIL-KCP Limited</strong> (50:50 JV with Fives Group France for turnkey sugar/power plants); <strong>KCP Cement</strong> (Macherla + Mukthyala plants); <strong>KCP Heavy Engineering</strong> (Steel Foundry + heavy-equipment fabrication near Chennai port); <strong>KCP Hotels &amp; Hospitality</strong> (Mercure Hyderabad KCP). Sister concerns under broader Velagapudi family include <strong>KCP Sugar &amp; Industries Corp</strong> (separately listed BSE 533166 / NSE KCPSUGIND).',
    funding_anchors=[
        f"Listed Velagapudi family flagship; promoter 44.25%{ref('1055')}.",
        f"Total debt Rs 480 Cr FY24 (Rs 542 Cr FY25); ROCE 13%; healthy multi-business cash flow.",
        "FY24 paid-up Rs 12.89 Cr; reserves Rs 1,400+ Cr (FY24).",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Axis + Indian Bank (multi-bank multi-segment consortium); BNP Paribas (FIVES France-link).",
        "<strong>Diligence item:</strong> Probe42 charge-register on KCP Ltd + KCP Vietnam Industries + FIVES CAIL-KCP CINs; Velagapudi family DIN cross-link.",
    ],
    toi_fy23=2254, toi_fy24=2846, toi_fy25=2529, toi_fy26=2900, toi_fy27=3300, toi_fy28=3800,
    eb_fy23=300, eb_fy24=510, ebitda_fy25=440, eb_fy26=510, eb_fy27=600, eb_fy28=720,
    mg_fy23="13.3", mg_fy24="17.9", ebitda_pct="17.4", mg_fy26="17.6", mg_fy27="18.2", mg_fy28="18.9",
    pat_fy23=91, pat_fy24=280, pat_fy25=253, pat_fy26=290, pat_fy27=350, pat_fy28=425,
    tnw_fy23=1225, tnw_fy24=1410, tnw_fy25=1533,
    dt_fy23="~558", dt_fy24="~480", debt_fy25="~542",
    dr_fy23="0.46x", dr_fy24="0.34x", dr_fy25="0.35x",
    paid_up=13, fte="~3,500 (consolidated incl Vietnam ops)",
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs ~480 Cr</div><div class="sub">Multi-business multi-bank{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 350 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi"><div class="k">Rating</div><div class="v num">CRISIL A</div><div class="sub">[verify Dec 2025 review]</div></div>',
    charges_summary="Multi-bank multi-segment consortium ~Rs 480 Cr; spread across cement + sugar + heavy engineering + Vietnam + hotels",
    charges_strap="Strategic: cement capex anchor + Vietnam-operations FX + heavy engineering BG/LC + Velagapudi family-PB + cluster cross-sell.",
    industry_text=(
        f'India cement consolidation accelerating: UltraTech now owns India Cements (55.49% Sep 2024) + Kesoram + Heidelberg = ~30% market share. '
        f'Smaller cement-sugar-engineering conglomerates like KCP face pressure on cost-discipline + capex. India sugar industry under E20 ethanol-blending tailwind. '
        f'Heavy engineering / EPC market growing 10-12% on infrastructure capex. KCP\'s Vietnam sugar operations are unique — Phu Yen + Son Hoa plants serve domestic Vietnam + export.'
    ),
    drivers=[
        f"<strong>Cement industry consolidation</strong>{ref('1055')} &mdash; UltraTech + Adani Cement dominate; smaller players need cost-discipline + capex urgency.",
        f"<strong>India + Vietnam sugar cycles</strong>{ref('15')} &mdash; cane-SAP + sugar-MSP + ethanol blending E20 mandate FY27; Vietnam VND-cycle independent.",
        f"<strong>FIVES CAIL-KCP turnkey export orders</strong> &mdash; sugar/power plant EPC in Africa + South America + SE Asia; export USD receivable.",
        f"<strong>Coal + pet-coke + cane raw material</strong>{ref('14')} &mdash; commodity hedge across multi-segment.",
        f"<strong>EU CBAM</strong>{ref('9')} &mdash; cement on Phase-1; potential export-receivable impact.",
        f"<strong>RBI repo cycle</strong>{ref('7')} &mdash; cement + sugar WC benchmarked.",
        f"<strong>Velagapudi family transition</strong> &mdash; V.L. Dutt patriarch generation transitioning to V. Kavitha Dutt + next-gen; family-stewardship + governance.",
    ],
    product_rows=[
        ("Cement capex TL (Macherla + Mukthyala refresh)", "200&ndash;400", "1.5", "3", "Sustainability + AFR covenant"),
        ("Vietnam-operations capex TL + multi-currency", "150&ndash;300 / VND equiv", "1", "2", "Phu Yen + Son Hoa expansion"),
        ("CC + WCDL (cement + sugar cycle)", "200&ndash;400", "1.5", "2.5", "60-90 day raw material cycle"),
        ("BG (cement-tender + sugar + heavy-eng EPC)", "150&ndash;300", "1", "1.8", "EPC + sugar mill + customer-LC"),
        ("LC + Trade (Vietnam + capex + coal)", "100&ndash;200 revolving", "0.7", "1.4", "Vietnam + capex import"),
        ("FX (USD + EUR + VND multi-currency)", "USD/EUR/VND 50-100 Mn notional", "1", "2", "Vietnam ops + EPC export + Fives France"),
        ("Heavy engineering export factoring (USD)", "80&ndash;150", "0.5", "1.0", "FIVES CAIL-KCP turnkey sugar/power"),
        ("Cane-procurement BG (sugar Min Consumer Affairs)", "30&ndash;60", "0.2", "0.4", "AP + TN cane procurement"),
        ("Salary CASA + payroll (3,500 FTE consolidated)", "Rs 10-20 Cr float", "0.5", "0.9", "Multi-plant + Vietnam"),
        ("PB (Velagapudi family + senior leadership)", "Rs 200-400 Cr AUM", "1.2", "2.2", "V.L. Dutt + V. Kavitha + family"),
        ("Hotel-segment (Mercure KCP) WC + capex", "30&ndash;60", "0.2", "0.4", "Hospitality cycle"),
        ("Group treasury sweep (multi-segment)", "Rs 350-600 Cr float", "0.3", "0.6", "Cross-business liquidity"),
    ],
    wholesale_y3="Rs 8.6-17.2 Cr / yr",
    retail_text="Salary CASA mandate ~3,500 FTE + cement-dealer-network + sugar farmer KCC; Rs 0.5-0.9 Cr/yr.",
    pb_text="Velagapudi family + senior leadership; PB AUM Rs 200-400 Cr; Rs 1.2-2.2 Cr/yr.",
    tasc_text="KCP PF + Velagapudi Foundation; Rs 80-150 Cr corpus; Rs 0.4-0.7 Cr/yr.",
    retail_total_low="2.1", retail_total_high="3.8",
    consolidated_rows=[
        ("Cement + Vietnam capex + LC + FX", "5.2", "9.4"),
        ("CC + WCDL + BG + factoring", "3.4", "5.7"),
        ("Cane BG + group treasury + hotel", "0.7", "1.4"),
        ("Salary + PB + TASC", "2.1", "3.8"),
    ],
    consolidated_total_low="11.4", consolidated_total_high="20.3",
    kmp_text=(
        "<strong>V.L. Dutt</strong> &mdash; Chairman Emeritus / Director (third-generation Velagapudi family patriarch; long-time KCP architect since 1960s). "
        "<strong>V. Kavitha Dutt</strong> &mdash; Joint Managing Director (fourth-generation; daughter of V.L. Dutt; operational leader). "
        "<strong>Vinod R. Sethi</strong> &mdash; Independent Director. "
        "<strong>R. Sailesh</strong> &mdash; CFO (estimated). "
        "Independent Directors include senior cement + sugar industry leaders; Velagapudi family Board representation across multiple generations."
    ),
    ownership_text="Promoter holding 44.25% (Velagapudi family + KCP Sugar Industries cross-holdings); FII 2.90%; DII 0.74%; public 52.10%.",
    diligence_news="FY26: Cement capacity refresh + WHRS + AFR + Vietnam plant scale-up + FIVES CAIL-KCP EPC orderbook execution; Velagapudi-family fourth-generation transition.",
    dil2="T+14: Probe42 charge-register on KCP Ltd + KCP Vietnam Industries + FIVES CAIL-KCP + KCP Sugar; CRISIL Dec 2025 rationale.",
    dil3="T-14: Pre-pitch cement capex term-sheet + Vietnam multi-currency FX desk + Velagapudi family-PB partner profile.",
    playbook_30="V. Kavitha Dutt Joint MD meeting; cement capex memo + Vietnam multi-currency FX concept.",
    playbook_60="Cement capex TL term-sheet committee; Vietnam FX desk; FIVES France LC + USD-receivable factoring.",
    playbook_90="Capex drawn 25%; Vietnam FX desk live; cane-procurement BG roll-out.",
    playbook_180="Velagapudi family-PB AUM Rs 200+ Cr; KCP-cluster cross-sell with KCP Sugar Industries listed-sister.",
    success_metrics=[
        "Cement capex TL Rs 200 Cr by Q3 FY27",
        "Vietnam multi-currency FX USD/VND 30-50 Mn by Q2 FY27",
        "Y3 wallet Rs 14-26 Cr",
        "Velagapudi family-PB Rs 200+ Cr by Q4 FY28",
    ],
    src_base=1055,
    src_parent_body="The KCP Limited Annual Report FY24 + investor relations + Velagapudi family disclosures + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="kcp.co.in &middot; nseindia.com &middot; bseindia.com",
    src_extra=[
        (1055, "The KCP Limited Annual Report FY24 + investor relations + screener.in financial profile", "kcp.co.in &middot; screener.in/company/KCP &middot; retrieved 28 Apr 2026"),
        (1056, "KCP Vietnam Industries Limited (Phu Yen + Son Hoa sugar operations)", "kcp.co.in/vietnam-operations &middot; corporate disclosures"),
        (1057, "FIVES CAIL-KCP JV with Fives Group France (turnkey sugar + power plant EPC)", "fives-cailkcp.com / fivesgroup.com"),
        (1058, "NSE/BSE KCP quarterly filings + KCP Sugar Industries (KCPSUGIND) sister listing", "nseindia.com / bseindia.com"),
        (1059, "CRISIL credit-rating rationale Dec 2025 [verify FY26]", "crisil.com"),
    ],
    footer="Cipher clean; 1,500+ lines; 84-yr Velagapudi family multi-business conglomerate (cement + sugar + heavy engineering + Vietnam + hotels); cement capex + Vietnam FX + EPC export factoring + family-PB triangulation.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 84-year arc from a 1941 Andhra industrial-family enterprise to a 5-business listed conglomerate with Vietnam operations</div>

<h3>03A.1 Founding (1941) &mdash; The KCP Limited (originally Krishna Cement Pvt Ltd)</h3>
<p>The KCP Limited was incorporated <strong>22 July 1941</strong> in Madras (Chennai){ref("1055")} by the Velagapudi family of industrialists from coastal Andhra Pradesh. The original mandate was cement manufacturing (originally as Krishna Cement Private Limited; "KCP" derives from this lineage). The company was one of the oldest pre-Independence cement franchises in South India.</p>

<h3>03A.2 The 1950s-1970s &mdash; Cement scale + heavy engineering diversification</h3>
<p>Through the 1950s-70s KCP built one of South India\'s leading cement franchises alongside India Cements + Madras Cements (now Ramco Cements). The company also diversified into <strong>heavy engineering</strong> &mdash; building an integrated Steel Foundry + heavy-equipment fabrication facility near the Chennai port for the post-Independence Indian engineering economy.</p>

<h3>03A.3 The 1980s-1990s &mdash; Sugar diversification + V.L. Dutt era</h3>
<p>Under the leadership of <strong>V.L. Dutt</strong> (third-generation Velagapudi family) the company diversified into <strong>sugar manufacturing</strong> &mdash; initially in Andhra Pradesh, then through KCP Sugar &amp; Industries Corporation (separately listed BSE 533166 / NSE KCPSUGIND). The Velagapudi family thus operates dual listed sugar entities &mdash; The KCP Limited (this entity, multi-segment incl sugar) and KCP Sugar &amp; Industries (focused sugar play).</p>

<h3>03A.4 Vietnam expansion (early 2000s) &mdash; KCP Vietnam Industries</h3>
<p>In the early 2000s KCP made one of Indian sugar industry\'s most distinctive moves &mdash; setting up <strong>KCP Vietnam Industries Limited</strong>{ref("1056")} with two sugar plants: the <strong>Phu Yen plant</strong> + the <strong>Son Hoa plant</strong> in Vietnam. This made KCP one of the very few Indian sugar manufacturers with significant overseas manufacturing capacity. The Vietnam operations have grown into a meaningful contributor to KCP consolidated revenue + EBITDA.</p>

<h3>03A.5 The FIVES CAIL-KCP JV (2010s) &mdash; turnkey sugar + power plant EPC</h3>
<p>KCP entered a <strong>50:50 joint venture with Fives Group (France)</strong>{ref("1057")} as <strong>FIVES CAIL-KCP Limited</strong> &mdash; offering turnkey sugar plant + power plant EPC for global customers (Africa, South America, SE Asia). This combined the Fives Group\'s 200-year French engineering heritage with KCP\'s heavy-engineering manufacturing capability.</p>

<h3>03A.6 The 2020-2024 inflection &mdash; revenue scale + margin expansion</h3>
<p>FY22 revenue Rs 2,108 Cr; FY23 Rs 2,254 Cr; <strong>FY24 Rs 2,846 Cr</strong>{ref("1055")} (with PAT Rs 280 Cr; +208% YoY); FY25 Rs 2,529 Cr; FY25 PAT Rs 253 Cr. EBITDA margin recovered from 13.3% FY23 to 17.9% FY24. ROCE 13% FY25. Multi-business multi-bank consortium ~Rs 480 Cr (FY24); cement + sugar + heavy engineering + Vietnam + hotels each separately financed.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 84-year arc tells you: (1) The KCP Limited is a <strong>genuine multi-business conglomerate</strong> &mdash; not a thematic play but five distinct operating businesses (cement / sugar / heavy engineering / Vietnam / hotels) under one listed entity; (2) the <strong>Vietnam operations</strong> + FIVES France JV make KCP one of the few Indian-cement-sugar players with structural multi-currency banking needs; (3) the <strong>UltraTech-India Cements consolidation context</strong> creates urgency for cement-segment capex + cost-discipline; (4) the <strong>Velagapudi family-PB</strong> opportunity is real (V.L. Dutt patriarch + V. Kavitha Dutt fourth-generation Joint MD) and largely uninstitutionalised; (5) the <strong>FIVES CAIL-KCP EPC export</strong> brings USD receivable factoring + customer-LC + advance-BG opportunities.</p>
</section>
"""


def build():
    from pathlib import Path
    emit(CFG)
    p = Path("/home/user/St") / f"{CFG['slug']}-dossier.html"
    html = p.read_text()
    if 'id="history"' not in html:
        html = html.replace(
            '<li><a href="#group">03 Group</a></li><li><a href="#entity">04 Entity</a></li>',
            '<li><a href="#group">03 Group</a></li><li><a href="#history">03A History</a></li><li><a href="#entity">04 Entity</a></li>'
        )
        html = html.replace('\n\n<section id="entity">', '\n\n' + HISTORY_BLOCK_HTML + '\n\n<section id="entity">', 1)
        p.write_text(html)
        print(f"Injected history block into {p}")


if __name__ == "__main__":
    build()
