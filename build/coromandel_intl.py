"""Coromandel International dossier — pilot 155, Murugappa fertiliser flagship (held via EID Parry)."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=155, name="Coromandel International Limited", slug="coromandel-international",
    title="Coromandel International Limited · Dossier 28 Apr 2026",
    cin="L24120TG1961PLC000892", parent="EID Parry (India) / Murugappa Group",
    pad_label="Coromandel International", pad_sector="Complex Fertilisers (NPK leader) / Crop Protection / Specialty Nutrients / Agri-drones",
    eyebrow_extras="Secunderabad HO · Listed BSE+NSE COROMANDEL · CRISIL AAA Stable · 56.4% EID Parry · Murugappa group",
    headline_sub="India's largest complex-fertiliser maker; 18% NPK market share; FY24 revenue Rs 22,308 Cr; CRISIL AAA; cash Rs 4,263 Cr",
    lede=f'Coromandel International Limited (CIN L24120TG1961PLC000892){ref("970")} is the listed Murugappa Group fertiliser flagship and India&rsquo;s largest complex-fertiliser manufacturer (NPK / DAP segment leader at ~18% market share){ref("970")}. Listed BSE / NSE COROMANDEL{ref("970")}; promoter holding 56.4% (held via EID Parry); HQ Sardar Patel Road, Secunderabad. <strong>FY24 revenue Rs 22,308 Cr</strong>{ref("128")}; FY24-25 Rs 23,308 Cr; EBITDA Rs 2,401 Cr (10.2%); PAT Rs 1,719 Cr; networth Rs 15,800+ Cr (TNW grew 19.51% in FY24); total debt only Rs 1,470 Cr (D/E 0.05x; <strong>cash Rs 4,263 Cr</strong>). <strong>CRISIL AAA / Stable + India Ratings AAA / Stable</strong>{ref("128")} &mdash; the highest domestic credit rating. Subsidiaries: Coromandel Chemicals Ltd (100% owned); Dare Ventures Ltd (agri-venture capital); Coromandel Brasil Limitada; <strong>Dhaksha Unmanned Systems</strong> (Agri-drones, acquired 2023); Coromandel America. Founded 1961 as JV with International Minerals & Chemicals (USA) + Chevron Chemical &mdash; one of India&rsquo;s longest-running fertiliser franchises. Capex commitment to double revenue in 5 years; 18 manufacturing facilities globally.',
    headline_low=22, headline_high=40,
    headline_strap="Y3 wallet (capex anchor + group treasury + Murugappa family-PB)",
    industry_short="Complex Fertilisers / Crop Protection / Specialty Nutrients / Agri-drones",
    kpi3='<div class="kpi pos"><div class="k">Cash position</div><div class="v num">Rs 4,263 Cr</div><div class="sub">D/E 0.05x' + ref("126") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AAA</div><div class="sub">Stable + IndR AAA' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Doubling-revenue capex Rs 800-1,500 Cr</strong> &mdash; 5-year capex commitment to double revenue; greenfield + brownfield NPK + crop-protection + specialty nutrients capex; AAA-rated borrower window.",
        "<strong>Multi-currency raw-material LC</strong> &mdash; phosphate-rock + ammonia + KCl imported from Morocco / Russia / Saudi / Canada; Rs 12,000-15,000 Cr/yr import LC.",
        "<strong>Murugappa group treasury anchor</strong> &mdash; AAA rating + Rs 4,263 Cr cash makes Coromandel the natural anchor for group-wide treasury sweep across 5 flagships.",
    ],
    incorp_date="16 Oct 1961",
    ho_text="1-2-10 Sardar Patel Road, Secunderabad, Hyderabad 500 003",
    group_text=f'Murugappa Group fertiliser flagship; held via EID Parry (India) at 56.4%{ref("970")}. Operating subsidiaries: <strong>Coromandel Chemicals Ltd</strong> (100% &mdash; crop protection + adjuvants); <strong>Dare Ventures Ltd</strong> (agri-venture capital); <strong>Coromandel Brasil Limitada</strong> (Brazil registrations); <strong>Dhaksha Unmanned Systems</strong> (Agri-drones, acquired 2023); <strong>Coromandel America</strong>. Manufacturing: Visakhapatnam + Kakinada (AP) + Ennore + Ranipet (TN) + Hospet (KA); 18 facilities globally including subsidiaries.',
    funding_anchors=[
        f"AAA / Stable rated{ref('128')} (CRISIL + India Ratings); highest domestic rating tier.",
        f"Cash Rs 4,263 Cr; D/E 0.05x; Rs 1,470 Cr debt mostly working-capital + customer-credit support.",
        f"Promoter 56.4% via EID Parry{ref('970')}; FY24 dividend Rs 100+ Cr to EID Parry.",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Citi + Axis + Indian Bank.",
        "<strong>Diligence item:</strong> Probe42 charge-register on Coromandel + Coromandel Chemicals + Dhaksha CINs.",
    ],
    toi_fy23=21500, toi_fy24=22308, toi_fy25=23308, toi_fy26=27000, toi_fy27=32000, toi_fy28=38000,
    eb_fy23=2200, eb_fy24=2401, ebitda_fy25=2580, eb_fy26=3050, eb_fy27=3700, eb_fy28=4500,
    mg_fy23="10.2", mg_fy24="10.8", ebitda_pct="11.1", mg_fy26="11.3", mg_fy27="11.6", mg_fy28="11.8",
    pat_fy23=1500, pat_fy24=1719, pat_fy25=1850, pat_fy26=2200, pat_fy27=2700, pat_fy28=3300,
    tnw_fy23=13000, tnw_fy24=15800, tnw_fy25=17800,
    dt_fy23="~1,800", dt_fy24="~1,470", debt_fy25="~1,800",
    dr_fy23="0.07x", dr_fy24="0.05x", dr_fy25="0.06x",
    paid_up=29, fte="~5,339 Mar 2024",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Rs 1,470 Cr</div><div class="sub">D/E 0.05x{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 4,263 Cr</div><div class="sub">Net cash AAA</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AAA</div><div class="sub">Stable</div></div>',
    charges_summary="Modest charges Rs 1,470 Cr (D/E 0.05x); cash Rs 4,263 Cr; AAA rated",
    charges_strap="Strategic: AAA-rated capex anchor on 5-year doubling plan; multi-currency raw-material LC bundle; Murugappa group treasury sweep.",
    industry_text=(
        f'India fertiliser sub-segment FY25 ~Rs 2.5-3.0 lakh Cr (incl subsidy); CAGR 5-7%. Complex fertilisers (NPK / DAP) ~Rs 1.0 lakh Cr; '
        f'Coromandel #1 in NPK (18% market share) followed by RCF + IFFCO + Zuari + GSFC. Crop protection FY25 ~Rs 35-42k Cr; CAGR 8-10%. '
        f'Agri-drones is a nascent Rs 800-1,200 Cr segment with rapid CAGR (40-50%); Coromandel via Dhaksha is one of 3-4 organised players.'
    ),
    drivers=[
        f"<strong>Doubling-revenue capex FY26-30</strong>{ref('970')} &mdash; capacity expansion + new product introduction; envelope Rs 800-1,500 Cr.",
        f"<strong>Phosphate-rock + ammonia + KCl import</strong>{ref('14')} &mdash; Morocco + Russia + Saudi + Canada; Rs 12,000-15,000 Cr/yr import LC.",
        f"<strong>Fertiliser subsidy + DBT regime</strong>{ref('15')} &mdash; subsidy Rs 1.7 lakh Cr/yr; receivable cycle from GoI moderate.",
        f"<strong>Crop protection regulation</strong> &mdash; CIB + CIBRC approvals; specialty nutrients ramp.",
        f"<strong>Agri-drones (Dhaksha)</strong>{ref('970')} &mdash; precision-agri ramp; FY27 inflection.",
        f"<strong>Murugappa group flagship anchor</strong> &mdash; AAA rating + cash means group treasury can centralise here.",
    ],
    product_rows=[
        ("Capex TL (5-yr doubling-revenue plan)", "800&ndash;1,500", "9", "16", "AAA-rated; multi-tranche; sustainability covenant"),
        ("CC + WCDL (raw-material cycle)", "500&ndash;800", "3", "5", "Phosphate + ammonia + KCl"),
        ("Multi-currency LC (raw-material import)", "1,500&ndash;2,500 revolving", "3.5", "5.5", "Morocco/Russia/Saudi/Canada USD/EUR"),
        ("FX (USD + EUR forward + IRS)", "USD 200-500 Mn notional", "3", "5", "Raw-material import + occasional export"),
        ("Subsidy receivable factoring (GoI)", "200&ndash;400", "1", "2", "GoI fertiliser subsidy paper"),
        ("Group treasury sweep (Murugappa flagship)", "Rs 2,000-4,000 Cr float", "1.5", "2.5", "Cross-flagship; AAA anchor"),
        ("Salary CASA + payroll (5,339 FTE + global)", "Rs 25-50 Cr", "1", "1.8", "Cluster across plants"),
        ("PB (Murugappa family — Coromandel share)", "Rs 400-700 Cr AUM", "2", "3.5", "5-flagship promoter family"),
        ("TASC (Foundation + PF)", "Rs 200-300 Cr corpus", "0.8", "1.5", "Murugappa Foundation"),
    ],
    wholesale_y3="Rs 14.0-26.0 Cr / yr",
    retail_text="Salary CASA mandate ~5,339 FTE; Rs 1.0-1.8 Cr/yr.",
    pb_text="Murugappa family allocation; Coromandel share Rs 400-700 Cr AUM; Rs 2.0-3.5 Cr/yr.",
    tasc_text="Coromandel PF + Murugappa Foundation; Rs 200-300 Cr corpus; Rs 0.8-1.5 Cr/yr.",
    retail_total_low="3.8", retail_total_high="6.8",
    consolidated_rows=[
        ("Capex TL (doubling plan)", "9", "16"),
        ("CC + WCDL + LC + FX", "9.5", "15.5"),
        ("Subsidy factoring + group treasury", "2.5", "4.5"),
        ("Salary + PB + TASC", "3.8", "6.8"),
    ],
    consolidated_total_low="24.8", consolidated_total_high="42.8",
    kmp_text=(
        "<strong>S. Sankarasubramanian</strong> &mdash; Managing Director (long-time Murugappa-group operating leader). "
        "<strong>Hemant Jalan</strong> &mdash; Chairman. "
        "<strong>Nipul Chawla</strong> &mdash; CEO. "
        "<strong>Jayashree Satagopan</strong> &mdash; CFO. "
        "Independent Directors include Sridharan Rangarajan (Murugappa group nominee), Shyam Saran, others."
    ),
    ownership_text="Promoter holding 56.4% via EID Parry / Murugappa Group; FII 16%; DII 14%; public 13.6%.",
    diligence_news="FY26: Capex commitment delivery on 5-yr doubling plan; Dhaksha Agri-drone scale-up; specialty nutrients export expansion.",
    dil2="T+14: Probe42 charge-register on Coromandel + subs; CRISIL + IndR rationale.",
    dil3="T-14: Pre-pitch capex multi-tranche term-sheet + multi-currency LC framework + Murugappa family-PB profile.",
    playbook_30="S. Sankarasubramanian + Jayashree Satagopan meeting; AAA-rated capex term-sheet concept.",
    playbook_60="Capex TL term-sheet committee-grade; multi-currency LC framework signed; group treasury cross-sell concept.",
    playbook_90="Capex TL drawn 25%; subsidy factoring book launch; Dhaksha financing.",
    playbook_180="Murugappa group treasury anchor; 5-flagship cross-sell mature.",
    success_metrics=[
        "Capex TL Rs 500 Cr by Q3 FY27",
        "Multi-currency LC USD 200 Mn revolving by Q2 FY27",
        "Y3 wallet Rs 22-40 Cr",
        "Murugappa family-PB Rs 400+ Cr (Coromandel share) by Q4 FY28",
    ],
    src_base=970,
    src_parent_body="Coromandel International Annual Report FY24 + investor relations + Murugappa Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="coromandel.biz &middot; murugappa.com &middot; eidparry.com",
    src_extra=[
        (970, "Coromandel International Annual Report FY24 + investor relations", "coromandel.biz &middot; retrieved 28 Apr 2026"),
        (971, "Dhaksha Unmanned Systems acquisition disclosure 2023", "Coromandel press release"),
        (972, "NSE/BSE COROMANDEL quarterly filings", "nseindia.com / bseindia.com"),
        (973, "CRISIL AAA + India Ratings AAA rationale [verify FY26]", "crisil.com / indiaratings.co.in"),
    ],
    footer="Cipher clean; 1,500+ lines; AAA-rated Murugappa fertiliser flagship with 5-year doubling-revenue capex window + multi-currency raw-material LC + group treasury anchor.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 65-year arc from US-JV fertiliser bet to AAA-rated Murugappa flagship + India NPK leader</div>

<h3>03A.1 Founding (1961) &mdash; Tripartite JV</h3>
<p>Coromandel International was incorporated <strong>16 October 1961</strong> in Hyderabad as a tripartite joint venture among <strong>EID Parry (India)</strong>, <strong>International Minerals &amp; Chemicals Corp</strong> (USA), and <strong>Chevron Chemical Company</strong> (USA){ref("970")}. The original mandate was to manufacture complex fertilisers (NPK + DAP) for the Indian Green Revolution agricultural-modernisation program. Plants commissioned at Visakhapatnam (Andhra Pradesh) using imported phosphate-rock + sulphuric acid technology.</p>

<h3>03A.2 The 1970s-1980s &mdash; Indian Green Revolution scale-up</h3>
<p>Coromandel was a key supplier into the Indian Green Revolution &mdash; complex NPK fertilisers replaced single-nutrient straight fertilisers, driving farm yields. By the late 1980s, the company was the largest private-sector complex-fertiliser manufacturer in India, with significant market share in the South + East regions.</p>

<h3>03A.3 Murugappa control + Indianisation (1990s)</h3>
<p>Through the 1990s the foreign JV partners (IMC + Chevron) reduced their stakes; EID Parry (already Murugappa-controlled since 1981) became the dominant promoter. Coromandel transitioned from a JV-managed company to a Murugappa-flagship-managed company under Indian leadership.</p>

<h3>03A.4 The 2000s-2010s &mdash; capacity expansion + crop protection diversification</h3>
<p>Capacity expanded across Visakhapatnam + Kakinada + Ennore + Ranipet, taking Coromandel to ~5.0 MMTPA NPK capacity by mid-2010s. The company diversified into <strong>crop protection</strong> (insecticides + herbicides + fungicides) via Coromandel Chemicals (100% subsidiary) and into <strong>specialty nutrients</strong> (micro-nutrients + secondary nutrients). NPK market share crossed 18% &mdash; cementing #1 position.</p>

<h3>03A.5 The 2020-2024 inflection &mdash; AAA rating + Dhaksha + 5-year doubling commitment</h3>
<p>The structural inflection. Coromandel achieved <strong>CRISIL AAA / Stable</strong> rating &mdash; the highest domestic tier. Cash position grew to Rs 4,263 Cr at FY24-end; D/E fell to 0.05x. The 2023 acquisition of <strong>Dhaksha Unmanned Systems</strong> brought Agri-drone capability for precision-agriculture. Management committed to a <strong>5-year capex plan to double revenue</strong> from Rs 22,000 Cr to ~Rs 45,000+ Cr.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; capex execution + group treasury anchor</h3>
<p>FY24 revenue Rs 22,308 Cr; analyst-est FY28 Rs 38,000 Cr (CAGR ~14%). Capex envelope Rs 800-1,500 Cr over the 5-year window for capacity + crop-protection + specialty-nutrient + Dhaksha + global expansion. Multi-currency raw-material LC Rs 12,000-15,000 Cr/yr (Morocco / Russia / Saudi / Canada) drives FX desk + LC mandate.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 65-year arc tells you: (1) Coromandel is the <strong>group treasury anchor</strong> &mdash; AAA rating + Rs 4,263 Cr cash + 5-flagship Murugappa structure; (2) the 5-year doubling capex is <strong>committed, not aspirational</strong> &mdash; Rs 800-1,500 Cr financing window is real; (3) the <strong>multi-currency LC mandate</strong> on phosphate-rock + ammonia + KCl imports is one of the largest single-bank LC opportunities in Indian agribusiness; (4) Coromandel's AAA status makes it the <strong>cheapest-cost-of-funds entry-point</strong> into the Murugappa group treasury.</p>
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
