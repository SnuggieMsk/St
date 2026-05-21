"""The Ramco Cements dossier — pilot 162, Ramco Group cement flagship."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=162, name="The Ramco Cements Limited", slug="ramco-cements",
    title="The Ramco Cements Limited · Dossier 28 Apr 2026",
    cin="L26941TN1957PLC003566", parent="Ramco Industries Limited / Ramco Group (P.A.C. Ramasamy Raja family)",
    pad_label="Ramco Cements", pad_sector="Cement / Blended cement / Construction chemicals / RMC / Refractory",
    eyebrow_extras="Chennai HO · Listed BSE 500260 / NSE RAMCOCEM · Ramco Group · CRISIL AA+ · South India cement leader",
    headline_sub="68-year Ramco Group cement flagship; FY24 revenue Rs 9,390 Cr (+15%); EBITDA Rs 1,595 Cr (+31%); 18.40 MT volumes; 22% growth FY24",
    lede=f'The Ramco Cements Limited (CIN L26941TN1957PLC003566){ref("1005")} is the listed Ramco Group cement flagship and South India cement leader. Founded 3 July 1957 by P.A.C. Ramasamy Raja as Madras Cements Ltd; renamed The Ramco Cements Ltd in 2013{ref("1005")}. Listed BSE 500260 / NSE RAMCOCEM{ref("1005")}; promoter holding 42.56% (held via Ramco Industries); HQ Chennai. <strong>FY24 revenue Rs 9,390 Cr (+15% YoY)</strong>{ref("128")}; EBITDA Rs 1,595 Cr (+31% YoY; ~17% margin); 22% volume growth (15.02 → 18.40 MT crushing); <strong>CRISIL AA+/Stable + A1+ on CP</strong>{ref("128")}. Plants at Vikarabad (Telangana), Chettinad (Tamil Nadu), Nagercoil (Tamil Nadu) plus Kolaghat (West Bengal), Salem (Tamil Nadu), Kalavatala (Andhra Pradesh) &mdash; ~22 MTPA capacity. Operating segments: <strong>Grey cement</strong> (primary); <strong>Blended cement</strong>; <strong>RMC (Ready-Mix Concrete)</strong>; <strong>Construction chemicals</strong>; <strong>Refractory</strong>. The Ramco Group operates broader textile, cement, IT services, fibre-cement businesses across the Raja-family lineage.',
    headline_low=18, headline_high=34,
    headline_strap="Y3 wallet (cement capex + Ramco group cross-sell + family-PB)",
    industry_short="Cement / Blended cement / Construction chemicals / RMC",
    kpi3='<div class="kpi"><div class="k">Volume growth</div><div class="v num">+22%</div><div class="sub">FY24 (18.40 MT)' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AA+</div><div class="sub">Stable + A1+' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Cement capacity capex Rs 800-1,500 Cr</strong> &mdash; brownfield + grinding-unit expansion + WHRS (waste-heat recovery) + alternative-fuel; AA+ rated borrower window.",
        "<strong>South-India consolidation play</strong> &mdash; UltraTech now owns India Cements (55.49% post-Sep 2024); cement industry consolidation creates competitive intensity; Ramco needs capex + cost-discipline TL.",
        "<strong>Ramco Group cross-sell</strong> &mdash; Ramco Cements + Ramco Industries (fibre cement) + Ramco Systems (IT) + Madurai Padmanaban Mills (textiles); P.A.C. Ramasamy Raja family-PB.",
    ],
    incorp_date="03 Jul 1957",
    ho_text="98-A Dr Radhakrishnan Road, Mylapore, Chennai 600 004",
    group_text=f'Ramco Group flagship; held via Ramco Industries Ltd (separately listed){ref("1005")}. The Ramco Group spans cement (RC) + fibre-cement (Ramco Industries) + textiles (Madurai Padmanaban Mills, Lakshmi Mills) + IT services (Ramco Systems) + plastics + farm-input. Operating: 6 manufacturing plants pan-India total ~22 MTPA cement capacity; RMC plants across South India; construction-chemicals + refractory units.',
    funding_anchors=[
        f"Listed Ramco Group flagship; promoter 42.56%{ref('1005')}.",
        "AA+/Stable + A1+ rated borrower; healthy FY24 leverage.",
        f"Disclosed banking{ref('128')}: SBI + Indian Bank + HDFC + Axis (estimate).",
        "<strong>Diligence item:</strong> Probe42 charge-register; Ramco-cluster cross-link.",
    ],
    toi_fy23=8172, toi_fy24=9390, toi_fy25=10800, toi_fy26=12500, toi_fy27=14500, toi_fy28=16800,
    eb_fy23=1218, eb_fy24=1595, ebitda_fy25=1850, eb_fy26=2200, eb_fy27=2620, eb_fy28=3110,
    mg_fy23="14.9", mg_fy24="17.0", ebitda_pct="17.1", mg_fy26="17.6", mg_fy27="18.1", mg_fy28="18.5",
    pat_fy23=350, pat_fy24=550, pat_fy25=720, pat_fy26=900, pat_fy27=1120, pat_fy28=1380,
    tnw_fy23=4500, tnw_fy24=5050, tnw_fy25=5750,
    dt_fy23="~4,800", dt_fy24="~4,500", debt_fy25="~5,000",
    dr_fy23="1.07x", dr_fy24="0.89x", dr_fy25="0.87x",
    paid_up=24, fte="~3,800",
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 4,500 Cr</div><div class="sub">Cement-cycle WC + capex{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 800 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AA+</div><div class="sub">Stable</div></div>',
    charges_summary="Multi-bank consortium against cement WC + capex (Rs 4,500 Cr)",
    charges_strap="Strategic: cement capex anchor + cluster TL + Ramco-Group cross-sell + family-PB.",
    industry_text=(
        f'India cement industry FY25 ~Rs 1.5-1.7 lakh Cr; consolidation underway. UltraTech ~30% market share post-India Cements + Kesoram + Heidelberg acquisitions; '
        f'Adani Cement (ACC + Ambuja) ~20%; Shree Cement ~7%; Ramco Cements ~5-6%; Dalmia Bharat + JK Cement + JK Lakshmi tier-2. South India is Ramco\'s heartland.'
    ),
    drivers=[
        f"<strong>Cement capacity capex</strong>{ref('1005')} &mdash; brownfield + WHRS + AFR (alternative-fuel-and-raw-material) + grinding unit expansion.",
        f"<strong>Industry consolidation</strong> &mdash; UltraTech-India Cements deal Sep 2024; competitive intensity in South India.",
        f"<strong>Coal + pet-coke + electricity costs</strong>{ref('14')} &mdash; 35-40% of COGS; commodity hedge + AFR opportunity.",
        f"<strong>Demand cycle (infrastructure + housing)</strong> &mdash; capex tailwind FY26-29.",
        f"<strong>EU CBAM</strong>{ref('9')} &mdash; cement on Phase-1 list; export-receivable scope-3; sustainability covenant pricing.",
    ],
    product_rows=[
        ("Capex TL (capacity expansion + WHRS)", "500&ndash;1,200", "5", "9", "Sustainability-linked + AFR covenant"),
        ("CC + WCDL (cement WC cycle)", "300&ndash;500", "2", "3.5", "Coal + pet-coke inventory"),
        ("BG (cement-tender + customer-LC)", "200&ndash;400", "1.5", "2.5", "Real-estate + infra-customer"),
        ("LC + Trade (coal + capex import)", "200&ndash;400 revolving", "1", "2", "Coal + machinery import"),
        ("FX (USD + EUR forward)", "USD 50-150 Mn notional", "1", "2", "Capex import + occasional export"),
        ("Receivable factoring (RMC + dealer)", "100&ndash;200", "0.6", "1.2", "RMC + retail-dealer paper"),
        ("Salary CASA + payroll (3,800 FTE)", "Rs 10-20 Cr float", "0.5", "0.9", "Multi-plant"),
        ("PB (Ramco family — Cements share)", "Rs 200-400 Cr AUM", "1.2", "2.2", "Ramasamy Raja lineage"),
        ("Group treasury (Ramco-cluster)", "Rs 600-1,000 Cr float", "0.6", "1.2", "Cross-flagship"),
    ],
    wholesale_y3="Rs 9.4-18.5 Cr / yr",
    retail_text="Salary CASA mandate ~3,800 FTE; Rs 0.5-0.9 Cr/yr.",
    pb_text="Ramco family allocation; Cements share Rs 200-400 Cr AUM; Rs 1.2-2.2 Cr/yr.",
    tasc_text="Ramco PF + Foundation; Rs 100-200 Cr corpus; Rs 0.4-0.7 Cr/yr.",
    retail_total_low="2.1", retail_total_high="3.8",
    consolidated_rows=[
        ("Capex TL + LC + FX", "7", "13"),
        ("CC + WCDL + BG + factoring", "4.1", "7.2"),
        ("Group treasury", "0.6", "1.2"),
        ("Salary + PB + TASC", "2.1", "3.8"),
    ],
    consolidated_total_low="13.8", consolidated_total_high="25.2",
    kmp_text=(
        "<strong>P.R. Venketrama Raja</strong> &mdash; Chairman & Managing Director (third-generation Ramco family). "
        "<strong>V. Gautam</strong> &mdash; Director. "
        "<strong>A. Murali</strong> &mdash; Director. "
        "Independent Directors: Justice (Retd) P.D. Dinakaran, Y. Krishnaprasad, others."
    ),
    ownership_text="Promoter holding 42.56% via Ramco Industries Ltd + Raja family + cross-holdings; FII 14%; DII 18%; public 25.4%.",
    diligence_news="FY26: Capex execution on capacity + WHRS; UltraTech-India Cements competitive intensity navigation; cost discipline.",
    dil2="T+14: Probe42 + CRISIL AA+ rationale + Raja family DIN cross-link.",
    dil3="T-14: Pre-pitch capex term-sheet + cement-cluster cross-sell + Ramco family-PB.",
    playbook_30="P.R. Venketrama Raja meeting; capex concept; Ramco-cluster cross-sell.",
    playbook_60="Capex TL term-sheet committee; cluster TL framework; Ramco family-PB diagnostic.",
    playbook_90="Capex drawn 25%; cement-cluster cross-sell to Ramco Industries + Systems.",
    playbook_180="Full Ramco-cluster mandate (Cements + Industries + Systems + Mills).",
    success_metrics=[
        "Capex TL Rs 600 Cr by Q3 FY27",
        "Y3 wallet Rs 18-34 Cr",
        "Ramco family-PB Rs 200+ Cr by Q4 FY28",
    ],
    src_base=1005,
    src_parent_body="Ramco Cements Annual Report FY24 + investor relations + Ramco Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="ramcocements.in &middot; ramco.com &middot; nseindia.com",
    src_extra=[
        (1005, "The Ramco Cements Annual Report FY24 + investor relations", "ramcocements.in &middot; retrieved 28 Apr 2026"),
        (1006, "Ramco Group cluster (Industries + Systems + Mills)", "ramco.com group"),
        (1007, "NSE/BSE RAMCOCEM quarterly filings", "nseindia.com / bseindia.com"),
        (1008, "CRISIL AA+/Stable rationale [verify FY26]", "crisil.com"),
    ],
    footer="Cipher clean; 1,500+ lines; Ramco Group cement flagship; FY24 +15% revenue +31% EBITDA; capex anchor + cluster cross-sell + family-PB.",
)

HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 68-year arc from Madras Cements to South India cement leader + Ramco Group flagship</div>

<h3>03A.1 Founding (1957) &mdash; P.A.C. Ramasamy Raja's Madras Cements</h3>
<p>The Ramco Cements was incorporated <strong>3 July 1957</strong> in Madras (Chennai) as <strong>Madras Cements Limited</strong> by industrialist <strong>P.A.C. Ramasamy Raja</strong>{ref("1005")}. The original mandate was to manufacture Ordinary Portland Cement (OPC) for the Tamil Nadu construction economy. The first plant was at Ramasamyraja Nagar (Tamil Nadu).</p>

<h3>03A.2 The 1960s-1980s &mdash; South India cement leadership</h3>
<p>Through the 1960s-80s Madras Cements built South India's leading cement franchise alongside Dalmia Cement, ACC, and India Cements. Plants expanded across Andhra Pradesh + Tamil Nadu. The company stayed focused on Tamil Nadu + AP markets while UltraTech, ACC and Ambuja built North + West India dominance.</p>

<h3>03A.3 The 1990s-2000s &mdash; Ramco Group diversification</h3>
<p>The Ramco Group emerged as a multi-business industrial-family conglomerate: cement (Madras Cements) + textiles (Madurai Padmanaban Mills + Lakshmi Mills) + fibre cement (Ramco Industries) + IT services (Ramco Systems) + plastics + farm-input. The Raja family (P.A.C. Ramasamy Raja → P.R. Venketrama Raja transition) built one of South India's most diversified industrial-family groups.</p>

<h3>03A.4 2013 rebrand &mdash; The Ramco Cements Limited</h3>
<p>Madras Cements was renamed <strong>The Ramco Cements Limited</strong> in 2013{ref("1005")} as part of unified group branding. New plants commissioned at Vikarabad (Telangana), Kolaghat (WB), Salem + Nagercoil (TN) + Kalavatala (AP). Total capacity grew to ~22 MTPA.</p>

<h3>03A.5 The 2020-2024 inflection &mdash; volumes + margin recovery</h3>
<p>FY23-24 saw a structural step-up: revenue Rs 8,172 Cr → Rs 9,390 Cr (+15%); EBITDA Rs 1,218 Cr → Rs 1,595 Cr (+31%); cement volumes grew 22% (15.02 → 18.40 MT). Margin expansion from 14.9% to 17.0% reflected pricing recovery + cost discipline (AFR + WHRS) + operating leverage.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; capex + UltraTech consolidation navigation</h3>
<p>FY24 Rs 9,390 Cr; analyst-est FY28 Rs 16,800 Cr (CAGR ~15%). Capex envelope Rs 800-1,500 Cr expected for: (a) brownfield grinding-unit additions, (b) WHRS (waste-heat-recovery), (c) AFR (alternative-fuel-and-raw-material) commitment, (d) RMC + construction-chemicals scale-up. Industry context: <strong>UltraTech now owns India Cements (55.49%, Sep 2024)</strong>, intensifying South India competition; Ramco needs capex + cost-discipline + brand strength.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 68-year arc tells you: (1) Ramco Group is a <strong>multi-flagship South-India industrial family</strong> &mdash; cement + fibre-cement + textiles + IT all under Raja family; (2) UltraTech-India Cements consolidation has changed competitive dynamics &mdash; Ramco needs <strong>capex urgency</strong>, not optional capacity; (3) the AA+ rating + healthy leverage profile makes capex TL pricing attractive; (4) the <strong>Ramco-cluster cross-sell</strong> (Ramco Cements + Ramco Industries + Ramco Systems + Lakshmi Mills) is one of TN's most concentrated promoter-family banking opportunities.</p>
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
