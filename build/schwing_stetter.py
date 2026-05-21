"""Schwing Stetter India dossier — pilot 170, XCMG-Schwing concrete equipment."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=170, name="Schwing Stetter India Private Limited", slug="schwing-stetter-india",
    title="Schwing Stetter India Private Limited · Dossier 28 Apr 2026",
    cin="U45309TN1998PTC046270", parent="SCHWING GmbH (Germany) → XCMG Group, China (100% via XCMG acquisition)",
    pad_label="Schwing Stetter India", pad_sector="Construction equipment / Concrete pumps / Batching plants / Transit mixers",
    eyebrow_extras="Chennai HO · Unlisted Pvt Ltd · XCMG-Schwing 100% · CRISIL A · Construction-equipment leader",
    headline_sub="27-yr SCHWING-Germany subsidiary (now XCMG-China-controlled); FY23 revenue Rs 5,450 Cr; CY24 Rs 5,500-5,600 Cr; concrete-equipment market leader",
    lede=f'Schwing Stetter India Private Limited (CIN U45309TN1998PTC046270){ref("1045")} is the Chennai-headquartered Indian subsidiary of <strong>SCHWING GmbH (Germany)</strong> &mdash; a €850 Mn annual concrete-equipment manufacturer that was acquired by <strong>XCMG Group, China</strong> in 2012 for €300 Mn. Listed: unlisted Pvt Ltd. Incorporated 1998{ref("1045")}; HQ Chennai. <strong>FY23 revenue Rs 5,450 Cr (38% CAGR)</strong>; <strong>CY24 revenue ~Rs 5,500-5,600 Cr (+4% growth)</strong>{ref("128")}; XCMG product segment driving double-digit volume growth. Operating segments: <strong>Concrete pumps</strong> (truck-mounted + stationary); <strong>Batching plants</strong> (concrete production); <strong>Transit mixers</strong>; <strong>Mobile and stationary equipment</strong> for construction industry. Plants: Chennai (HQ + manufacturing), Pune, Hyderabad, Bengaluru (regional assembly + service). Customers: <strong>Construction majors (L&T, Tata Projects, Shapoorji Pallonji), Real estate (DLF, Prestige, Lodha, Brigade), Infra contractors (NHAI tier-1), Ready-Mix Concrete (RMC) companies</strong>. <strong>CRISIL A/Stable + A1 (bank facilities reaffirmed Oct 2024)</strong>{ref("128")}. ~1,500 FTE (estimate).',
    headline_low=10, headline_high=18,
    headline_strap="Y3 wallet (capex + multi-currency FX (EUR+CNY) + dealer/customer-finance)",
    industry_short="Construction Equipment: Concrete Pumps + Batching Plants + Transit Mixers",
    kpi3='<div class="kpi pos"><div class="k">Growth</div><div class="v num">+38%</div><div class="sub">FY23 CAGR' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A</div><div class="sub">Stable + A1' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Capex TL Rs 200-400 Cr</strong> &mdash; XCMG product-line localisation + electric-pump R&D + capacity expansion at Chennai plant; sustainability-linked covenant.",
        "<strong>Multi-currency FX desk (EUR + CNY + USD)</strong> &mdash; SCHWING Germany parent + XCMG China parent; capex import + parent royalty; Rs 800-1,200 Cr/yr forex.",
        "<strong>Dealer + customer-finance for construction majors</strong> &mdash; equipment-finance for L&T + Tata Projects + Shapoorji + RMC operators; OEM-anchor SCF.",
    ],
    incorp_date="1998",
    ho_text="32 PB No. 3050, Mt-Poonamallee Road, Anna Nagar, Chennai 600 019",
    group_text=f'XCMG Group, China (since 2012 acquisition) via SCHWING GmbH (Germany){ref("1045")}. SCHWING was acquired by XCMG (Xuzhou Construction Machinery Group, China) in 2012 for €300 Mn. Operating: Chennai HQ + manufacturing; Pune + Hyderabad + Bengaluru regional service. Sister concerns: XCMG construction-equipment cluster (cranes + earth-movers + road-construction-equipment) globally.',
    funding_anchors=[
        f"Privately held; XCMG Group China 100%{ref('1045')}.",
        "FY23 revenue Rs 5,450 Cr (+38% CAGR); CY24 Rs 5,500-5,600 Cr; turnaround complete.",
        "CRISIL A/Stable + A1; healthy operating cash; XCMG support.",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Citi + Deutsche (parent-link); foreign-MNC FX desk.",
        "<strong>Diligence item:</strong> Probe42 + XCMG China cross-link + China-sanctions navigation.",
    ],
    toi_fy23=5450, toi_fy24=5550, toi_fy25=5800, toi_fy26=6500, toi_fy27=7400, toi_fy28=8400,
    eb_fy23=380, eb_fy24=420, ebitda_fy25=480, eb_fy26=565, eb_fy27=665, eb_fy28=775,
    mg_fy23="7.0", mg_fy24="7.6", ebitda_pct="8.3", mg_fy26="8.7", mg_fy27="9.0", mg_fy28="9.2",
    pat_fy23=120, pat_fy24=160, pat_fy25=210, pat_fy26=280, pat_fy27=360, pat_fy28=440,
    tnw_fy23=850, tnw_fy24=920, tnw_fy25=1050,
    dt_fy23="~250", dt_fy24="~200", debt_fy25="~250",
    dr_fy23="0.29x", dr_fy24="0.22x", dr_fy25="0.24x",
    paid_up=10, fte="~1,500",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Total debt</div><div class="v num">Rs ~200 Cr</div><div class="sub">Conservative leverage{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 350 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A</div><div class="sub">Stable + A1</div></div>',
    charges_summary="Conservative leverage Rs ~200 Cr; XCMG / SCHWING parent support; A/Stable",
    charges_strap="Strategic: capex + multi-currency FX + dealer/customer-finance for construction majors.",
    industry_text=(
        f'India construction-equipment market FY25 ~Rs 28-32k Cr; CAGR 10-12% on infrastructure capex tailwind. '
        f'Concrete equipment niche ~Rs 5-7k Cr; Schwing Stetter is #1-2 in India (alongside ACE Putzmeister + KCP + Aquarius + Kaushik Engineering). '
        f'XCMG product-line localisation drives double-digit volume growth.'
    ),
    drivers=[
        f"<strong>Construction + infra capex tailwind</strong>{ref('1045')} &mdash; NHAI + Smart Cities + airport + metro + housing.",
        f"<strong>XCMG product-line localisation</strong> &mdash; cost-discipline + market-share gain.",
        f"<strong>Electric concrete pump R&D</strong> &mdash; sustainability + emission-norm tailwind.",
        f"<strong>Steel + components</strong>{ref('14')} &mdash; raw material cost; commodity hedge.",
        f"<strong>EUR/CNY parent FX</strong> &mdash; SCHWING Germany royalty + XCMG China capex import.",
    ],
    product_rows=[
        ("Capex TL (XCMG localisation + e-pump R&amp;D)", "200&ndash;400", "1.5", "3", "Sustainability-linked"),
        ("CC + WCDL (steel + components cycle)", "150&ndash;300", "1", "1.8", "60-90 day RM cycle"),
        ("BG (capex + customer LC)", "100&ndash;200", "0.7", "1.2", "Construction-major BG"),
        ("LC + Trade (EUR + CNY capex import)", "100&ndash;200 revolving", "0.6", "1.2", "Germany + China parent"),
        ("Multi-currency FX (EUR + CNY + USD)", "USD/EUR/CNY 80-150 Mn notional", "1.2", "2.4", "Parent + capex"),
        ("Dealer + customer-finance (RMC + construction)", "150&ndash;300", "1", "1.8", "L&T / Tata / Shapoorji equipment-finance"),
        ("Receivable factoring (construction-customer paper)", "80&ndash;150", "0.5", "1.0", "Real-estate developer paper"),
        ("Salary CASA + payroll (1,500 FTE)", "Rs 5-10 Cr float", "0.3", "0.5", "Multi-plant"),
        ("PB (senior leadership + parent-link)", "Rs 80-150 Cr AUM", "0.4", "0.7", "Senior leadership"),
    ],
    wholesale_y3="Rs 6.0-12.0 Cr / yr",
    retail_text="Salary CASA mandate ~1,500 FTE; Rs 0.3-0.5 Cr/yr.",
    pb_text="Senior leadership + XCMG/SCHWING parent-link expat; PB AUM Rs 80-150 Cr; Rs 0.4-0.7 Cr/yr.",
    tasc_text="SS-India PF + Foundation; Rs 30-50 Cr corpus; Rs 0.2-0.3 Cr/yr.",
    retail_total_low="0.9", retail_total_high="1.5",
    consolidated_rows=[
        ("Capex TL + LC + FX", "3.3", "6.6"),
        ("CC + WCDL + BG + dealer-fin", "3.2", "5.8"),
        ("Salary + PB + TASC", "0.9", "1.5"),
    ],
    consolidated_total_low="7.4", consolidated_total_high="13.9",
    kmp_text=(
        "<strong>V.G. Sakthikumar</strong> &mdash; Managing Director (long-time SS-India operating leader). "
        "<strong>Anand Sundaresan</strong> &mdash; Director (XCMG/SCHWING nominee). "
        "<strong>Ralf Rebhan</strong> &mdash; Director (Germany SCHWING parent appointee, estimated). "
        "Senior leadership: Indian + German + Chinese mix; XCMG nominee Board majority."
    ),
    ownership_text="Promoter holding 100% (XCMG Group China via SCHWING GmbH Germany).",
    diligence_news="FY26: XCMG product-line scale + electric concrete-pump launch + capacity-utilisation efficiency.",
    dil2="T+14: Probe42 + XCMG China cross-link + sanctions navigation diligence.",
    dil3="T-14: Pre-pitch capex term-sheet + EUR/CNY FX desk consolidation + dealer-finance pilot.",
    playbook_30="V.G. Sakthikumar MD meeting; capex + FX consolidation concept.",
    playbook_60="Capex TL term-sheet + multi-currency FX desk + dealer-finance pilot.",
    playbook_90="Capex drawn 25%; FX desk live; dealer-finance book onboarding.",
    playbook_180="XCMG-cluster cross-sell (other Indian XCMG product lines) + senior leadership PB.",
    success_metrics=[
        "Capex TL Rs 250 Cr by Q3 FY27",
        "Multi-currency FX book USD/EUR/CNY 80 Mn by Q2 FY27",
        "Y3 wallet Rs 10-18 Cr",
    ],
    src_base=1045,
    src_parent_body="Schwing Stetter India FY23/CY24 disclosures + CRISIL rationale Oct 2024 + XCMG/SCHWING parent (28 Apr 2026).",
    src_parent_url="schwingstetterindia.com &middot; xcmg-schwing.com",
    src_extra=[
        (1045, "Schwing Stetter India FY23/CY24 disclosures + CRISIL rationale Oct 2024", "schwingstetterindia.com &middot; crisil.com &middot; retrieved 28 Apr 2026"),
        (1046, "SCHWING GmbH Germany + XCMG China parent group", "xcmg-schwing.com / xcmg.com global"),
        (1047, "MCA / ROC Schwing Stetter India Private Limited", "mca.gov.in / zaubacorp.com"),
    ],
    footer="Cipher clean; 1,500+ lines; XCMG-Schwing concrete-equipment leader; capex + multi-currency FX (EUR+CNY) + dealer-customer-finance for construction majors.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 27-year arc from German JV to XCMG-Chinese-controlled Indian construction-equipment leader</div>

<h3>03A.1 Founding (1998) &mdash; SCHWING Germany greenfield in Chennai</h3>
<p>Schwing Stetter India was incorporated in <strong>1998</strong>{ref("1045")} as a 100% subsidiary of <strong>SCHWING GmbH (Germany)</strong> &mdash; the world\'s leading concrete-equipment manufacturer (founded 1934 in Herne, Germany; €850 Mn annual revenue at peak). The original mandate was to manufacture concrete pumps + batching plants for the Indian construction economy. Chennai plant became the manufacturing centre.</p>

<h3>03A.2 The 2000s &mdash; Indian construction boom + market leadership</h3>
<p>Through the 2000s the Indian construction + real-estate boom drove explosive demand for concrete-equipment. SS-India built market leadership in <strong>concrete pumps</strong> (truck-mounted boom + stationary + line) and <strong>batching plants</strong> (mobile + stationary). Indian Cement-Concrete Construction (3C) market grew at 15%+ CAGR.</p>

<h3>03A.3 The 2012 XCMG acquisition of SCHWING &mdash; new ownership</h3>
<p>In <strong>2012, XCMG (Xuzhou Construction Machinery Group, China) acquired SCHWING GmbH for €300 Mn</strong>{ref("1046")} &mdash; making SS-India effectively an XCMG-Chinese-controlled subsidiary. XCMG is China\'s largest construction-equipment manufacturer and one of the global top-3 (alongside Caterpillar + Komatsu). The acquisition strengthened SS-India\'s product range with XCMG cranes + earth-movers + road-construction-equipment.</p>

<h3>03A.4 The 2010s-2020s &mdash; XCMG product-line localisation</h3>
<p>Through the 2010s-2020s, SS-India increasingly localised XCMG product lines &mdash; not just SCHWING concrete-equipment but also XCMG cranes + excavators + road-construction-equipment for the Indian market. The Chennai plant + Pune / Hyderabad / Bengaluru regional service centres expanded.</p>

<h3>03A.5 The 2020-2024 inflection &mdash; revenue 38% CAGR + market leadership</h3>
<p>FY23 revenue Rs 5,450 Cr (with 38% CAGR over the previous period){ref("1045")}. CY24 revenue Rs 5,500-5,600 Cr. CRISIL A/Stable + A1 reaffirmed October 2024. The infrastructure capex tailwind (NHAI + Smart Cities + airports + metro + housing) drove construction-equipment demand at structural high levels.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; XCMG localisation + e-pump + capex</h3>
<p>FY24 Rs 5,550 Cr; analyst-est FY28 Rs 8,400 Cr (CAGR ~11%). EBITDA margin expansion from 7.6% FY24 to ~9.2% FY28 on XCMG localisation cost-discipline + product-mix + electric-pump premium. Capex envelope Rs 200-400 Cr expected for: (a) Chennai plant capacity expansion, (b) electric concrete-pump R&D + production line, (c) regional service centres.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 27-year arc tells you: (1) SS-India is the <strong>#1-2 concrete-equipment player in India</strong> &mdash; capex window real and ongoing; (2) the <strong>multi-currency FX desk</strong> (EUR + CNY parent flows) is structurally complex and high-value &mdash; PSU consortium cannot price this; (3) the <strong>construction-major customer base</strong> (L&T, Tata Projects, Shapoorji, RMC operators) is OEM-anchor SCF + dealer-finance opportunity; (4) the <strong>XCMG cluster cross-sell</strong> (other XCMG product lines in India: cranes, earth-movers, road equipment) is a long-game banking opportunity.</p>
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
