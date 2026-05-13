"""S.P. Apparels Limited dossier — pilot 173, Tirupur garment exporter."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=173, name="S.P. Apparels Limited", slug="sp-apparels",
    title="S.P. Apparels Limited · Dossier 28 Apr 2026",
    cin="L18101TZ2005PLC012295", parent="P. Sundararajan family (Promoter 61.81%)",
    pad_label="S.P. Apparels", pad_sector="Knitted garments / Kids+Infant apparel exports / Crocodile retail / Adult apparel",
    eyebrow_extras="Avinashi (Tirupur) HO · Listed BSE 540048 / NSE SPAL · 36-yr P. Sundararajan founder-led · ICRA rated · Kids/infant apparel export leader",
    headline_sub="36-year P. Sundararajan family-owned Tirupur garment exporter; FY24 revenue Rs 1,087 Cr → FY25 Rs 1,395 Cr (+28%); kids+infant knitted apparel; Disney/Carter's-tier global brand customer",
    lede=f'S.P. Apparels Limited (CIN L18101TZ2005PLC012295){ref("1060")} is one of India\'s leading manufacturers + exporters of knitted garments for infants and children. Promoted by founder <strong>P. Sundararajan</strong> as a partnership firm in 1989; incorporated as a public limited company on <strong>10 November 2005</strong>{ref("1060")}; listed on BSE 540048 / NSE SPAL (IPO 2016){ref("1060")}. HQ Tirupur / Avinashi (Tamil Nadu). Promoter holding <strong>61.81%</strong>{ref("1060")} (closely-held P. Sundararajan family). <strong>FY24 revenue Rs 1,087 Cr → FY25 Rs 1,395 Cr (+28% YoY surge)</strong>{ref("128")}; FY24 EBITDA Rs 196 Cr (18.0% margin) → FY25 Rs 231 Cr (16.6%); FY24 PAT Rs 90 Cr → FY25 Rs 95 Cr; FY24 networth Rs 764 Cr → FY25 Rs 856 Cr; FY24 total debt Rs 203 Cr → FY25 Rs 381 Cr (rose on UK + Sri Lanka subsidiary capex); ROCE 13-14%. <strong>ICRA-rated</strong>{ref("128")} (latest update September 2025). Integrated end-to-end facilities: raw fabric → knitting → dyeing → cutting → stitching → finishing → packaging. Subsidiaries: <strong>S.P. Retail Ventures Limited (SPRV)</strong> (Crocodile India retail brand &mdash; the company\'s retail apparel division); <strong>S.P. Apparels (International) Private Limited</strong> (Sri Lanka, incorporated 2024); <strong>SPUK</strong> (UK subsidiary, Apr 2026 capex Rs 6.31 Cr); Jumeirah Lanka Pvt Ltd (corporate guarantee Rs 27.96 Cr for HSBC loan). Customers: <strong>Disney, Carter\'s, Babies R Us, Mothercare, Pumpkin Patch, OshKosh, Walmart-tier global retailers</strong> + Crocodile India domestic retail. Plants: multiple in Avinashi + Tirupur (Tamil Nadu) cluster + Sri Lanka. Adult-apparel + private-label segments expanding alongside core kids+infants base.',
    headline_low=10, headline_high=18,
    headline_strap="Y3 wallet (capex + USD/GBP export factoring + Sri Lanka multi-currency + family-PB)",
    industry_short="Knitted Kids+Infant Apparel / Adult Apparel / Crocodile Retail / Export to Global Brands",
    kpi3='<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs ~380 Cr</div><div class="sub">Capex + cross-border consortium' + ref("126") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA A-</div><div class="sub">[verify Sep 2025 rationale]' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Capex TL Rs 200-400 Cr</strong> &mdash; UK + Sri Lanka subsidiary capex live FY26 + Avinashi plant expansion + automation/sustainability investments; promoter committed.",
        "<strong>USD/GBP export-receivable factoring on Disney/Carter's/Walmart-tier paper</strong> &mdash; 75-80% of revenue is export; Tier-1 global retailer LCs are investment-grade factor-eligible.",
        "<strong>P. Sundararajan family-PB + Crocodile India retail-distribution finance</strong> &mdash; 61.81% closely-held promoter family + retail dealer network across Crocodile India outlets.",
    ],
    incorp_date="10 Nov 2005 (founded 1989 as partnership)",
    ho_text="39-A, Extension Street, Kaikattipudur, Avinashi, Tirupur 641 654, Tamil Nadu",
    group_text=f'P. Sundararajan family-controlled; closely-held listed company (61.81% promoter){ref("1060")}. Subsidiaries: <strong>S.P. Retail Ventures Limited (SPRV)</strong> &mdash; Crocodile India retail brand (apparel retail division); <strong>S.P. Apparels (International) Private Limited (SPAIPL)</strong> &mdash; Sri Lanka subsidiary (incorporated FY24); <strong>SPUK</strong> &mdash; UK subsidiary (Apr 2026 capex Rs 6.31 Cr); <strong>Jumeirah Lanka Pvt Ltd</strong> &mdash; corporate guarantee Rs 27.96 Cr for HSBC loan (Sri Lanka). Operating manufacturing: multiple plants across Avinashi + Tirupur (Tamil Nadu) cluster &mdash; integrated knitting + dyeing + cutting + stitching + finishing + packaging.',
    funding_anchors=[
        f"Listed P. Sundararajan family-flagship; promoter 61.81%{ref('1060')}.",
        "FY25 total debt Rs 381 Cr (+88% vs Rs 203 Cr FY24) on UK + Sri Lanka subsidiary capex + Jumeirah-Lanka corporate-guarantee deployment.",
        "FY25 paid-up Rs 25.85 Cr; reserves Rs 830+ Cr.",
        f"Disclosed banking{ref('128')}: HSBC (Sri Lanka subsidiary parent guarantee) + SBI + HDFC + Axis (India); foreign-MNC FX desk for USD/GBP export.",
        "<strong>Diligence item:</strong> Probe42 charge-register on SPAL + SPRV + SPAIPL + SPUK + Jumeirah Lanka CINs; multi-currency consortium mapping.",
    ],
    toi_fy23=1081, toi_fy24=1087, toi_fy25=1395, toi_fy26=1620, toi_fy27=1880, toi_fy28=2150,
    eb_fy23=182, eb_fy24=196, ebitda_fy25=231, eb_fy26=275, eb_fy27=325, eb_fy28=380,
    mg_fy23="16.8", mg_fy24="18.0", ebitda_pct="16.6", mg_fy26="17.0", mg_fy27="17.3", mg_fy28="17.7",
    pat_fy23=83, pat_fy24=90, pat_fy25=95, pat_fy26=120, pat_fy27=150, pat_fy28=180,
    tnw_fy23=674, tnw_fy24=764, tnw_fy25=856,
    dt_fy23="~245", dt_fy24="~203", debt_fy25="~381",
    dr_fy23="0.36x", dr_fy24="0.27x", dr_fy25="0.45x",
    paid_up=26, fte="~22,000 (estimate, Tirupur cluster integrated)",
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs ~380 Cr</div><div class="sub">Capex + cross-border{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 150 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">ICRA A-</div><div class="sub">[verify FY26]</div></div>',
    charges_summary="Multi-currency multi-bank consortium ~Rs 380 Cr including HSBC corporate-guarantee for Sri Lanka",
    charges_strap="Strategic: capex TL on UK+Sri Lanka subsidiary + USD/GBP export factoring + Crocodile India retail-dealer finance + family-PB.",
    industry_text=(
        f'India textile + apparel industry FY25 ~Rs 12-14 lakh Cr; CAGR 8-10%. Apparel exports ~USD 16-18 Bn FY25; '
        f'CAGR 6-8%. Tirupur cluster alone ~USD 4-5 Bn/yr knitwear exports &mdash; 50%+ of India knitwear export. '
        f'SP Apparels is one of top-5 Indian kids+infant apparel exporters (alongside Gokaldas Exports + Pearl Global + Eastman Industries + Shahi Exports). Bangladesh + Vietnam compete as Tier-1 sources; India PLI textile + China+1 tailwind drives capacity reallocation.'
    ),
    drivers=[
        f"<strong>UK + Sri Lanka subsidiary capex FY26</strong>{ref('1061')} &mdash; SPUK Rs 6.31 Cr + SPAIPL Rs 6.02 Cr capex live Apr 2026; subsidiary debt build.",
        f"<strong>Avinashi plant expansion + automation</strong>{ref('1060')} &mdash; integrated knitting + dyeing + finishing capacity additions; capex envelope Rs 200-400 Cr over FY26-29.",
        f"<strong>USA tariff + China+1 tailwind</strong>{ref('6')} &mdash; India apparel-export benefits from China decoupling; potential 200-300 bps gross margin opportunity.",
        f"<strong>Cotton + yarn raw material</strong>{ref('14')} &mdash; commodity cycle; cotton-fibre + yarn input 45-55% of COGS; commodity-hedge opportunity.",
        f"<strong>USD/GBP/EUR FX</strong> &mdash; 75-80% export revenue in foreign currency; Sri Lanka subsidiary in LKR/USD.",
        f"<strong>EU CBAM</strong>{ref('9')} &mdash; not currently on Phase-1 list for textiles but scope-3 reporting will reach customer brands; sustainability-linked covenant pricing.",
        f"<strong>Crocodile India domestic retail</strong> &mdash; dealer network expansion through SPRV; B2C cash + dealer-finance.",
    ],
    product_rows=[
        ("Capex TL (Avinashi + UK + Sri Lanka)", "200&ndash;400", "1.5", "3", "Sustainability + automation covenant"),
        ("USD/GBP export factoring (Disney/Carter's/Walmart paper)", "200&ndash;400", "1.5", "2.5", "Tier-1 retailer LC non-recourse"),
        ("CC + WCDL (cotton + yarn + WIP cycle)", "150&ndash;250", "1", "1.8", "60-90 day fabric → finished cycle"),
        ("LC + Trade (raw material + machinery import)", "100&ndash;200 revolving", "0.7", "1.2", "Cotton + Korean / Japanese knitting machinery"),
        ("Multi-currency FX (USD + GBP + EUR + LKR)", "USD/GBP/EUR/LKR 50-100 Mn notional", "1", "2", "Export receivable + UK/SL subsidiary"),
        ("Sri Lanka cross-border WC + LC (SPAIPL + Jumeirah Lanka)", "Rs 30-60 / LKR equiv", "0.3", "0.5", "Multi-currency cross-border"),
        ("Crocodile India retail-dealer SCF + retail-loan (SPRV)", "Rs 50-100 Cr", "0.5", "0.9", "Crocodile India outlet network"),
        ("Salary CASA + payroll (22,000 FTE Tirupur cluster)", "Rs 40-80 Cr float", "1.5", "2.5", "Pan-Tirupur + Sri Lanka workforce"),
        ("PB (P. Sundararajan family + senior leadership)", "Rs 250-500 Cr AUM", "1.5", "2.7", "61.81% closely-held promoter family"),
        ("TASC (SP Foundation + PF)", "Rs 60-120 Cr corpus", "0.3", "0.5", "Worker-welfare Foundation"),
    ],
    wholesale_y3="Rs 6.7-12.0 Cr / yr",
    retail_text="Salary CASA mandate ~22,000 FTE Tirupur cluster + Crocodile India retail-dealer; Rs 1.5-2.5 Cr/yr salary + Rs 0.5-0.9 Cr/yr dealer-SCF.",
    pb_text="P. Sundararajan family closely-held; PB AUM Rs 250-500 Cr (61.81% promoter); Rs 1.5-2.7 Cr/yr.",
    tasc_text="SPAL PF + worker-welfare Foundation; Rs 60-120 Cr corpus; Rs 0.3-0.5 Cr/yr.",
    retail_total_low="3.8", retail_total_high="6.6",
    consolidated_rows=[
        ("Capex TL + LC + FX", "3.5", "6.7"),
        ("Export factoring + Sri Lanka", "1.8", "3.0"),
        ("CC + WCDL + Crocodile SCF", "1.5", "2.7"),
        ("Salary + PB + TASC", "3.3", "5.7"),
    ],
    consolidated_total_low="10.1", consolidated_total_high="18.1",
    kmp_text=(
        "<strong>P. Sundararajan</strong> &mdash; Chairman &amp; Managing Director (founder since 1989; 36-year veteran of Tirupur apparel-export industry; central figure in TN garment-exporter community). "
        "<strong>S. Latha</strong> &mdash; Whole-time Director (second-generation family). "
        "<strong>V. Balaji</strong> &mdash; CFO (estimated). "
        "<strong>P. Velusamy</strong> &mdash; Director. "
        "Independent Directors include senior textile + auditing + governance leaders. "
        "Decision style: founder-builder; export-experience deep; respects bankers who understand Tirupur knitwear cluster economics + global-brand customer dynamics."
    ),
    ownership_text="Promoter holding 61.81% (P. Sundararajan family + family-trust + cross-holdings); FII 1.48%; DII 16.57%; public 20.13%.",
    diligence_news=(
        "FY26: UK + Sri Lanka subsidiary scale-up; Avinashi plant capacity expansion; "
        "Crocodile India retail expansion + private-label adult-apparel segment growth; FY25 +28% revenue surge to Rs 1,395 Cr."
    ),
    dil2="T+14: Probe42 charge-register on SPAL + SPRV + SPAIPL + SPUK + Jumeirah Lanka CINs; ICRA Sep 2025 rationale.",
    dil3="T-14: Pre-pitch capex term-sheet + USD/GBP export factoring + Sri Lanka multi-currency LC + family-PB.",
    playbook_30="P. Sundararajan + S. Latha meeting; capex + export-factoring concept; family-PB introduction.",
    playbook_60="Capex TL term-sheet + multi-currency FX + UK/Sri Lanka subsidiary financing.",
    playbook_90="Capex drawn 25%; export factoring first 3-5 customers (Disney + Carter's); Crocodile India dealer-SCF onboarding.",
    playbook_180="Full SPAL + SPRV + SPAIPL + SPUK + Jumeirah Lanka cross-currency mandate; family-PB AUM diagnostic.",
    success_metrics=[
        "Capex TL Rs 200 Cr by Q3 FY27",
        "USD/GBP export factoring book Rs 150 Cr by Q2 FY27",
        "Y3 wallet Rs 10-18 Cr",
        "P. Sundararajan family-PB Rs 250+ Cr by Q4 FY28",
    ],
    src_base=1060,
    src_parent_body="S.P. Apparels Limited Annual Report FY24 + investor relations + ICRA rationale + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="s-p-apparels.com &middot; sprvl.in &middot; nseindia.com &middot; bseindia.com",
    src_extra=[
        (1060, "S.P. Apparels Annual Report FY24 + investor relations + screener.in financial profile", "s-p-apparels.com &middot; screener.in/company/SPAL &middot; retrieved 28 Apr 2026"),
        (1061, "SPUK + SPAIPL Sri Lanka subsidiary disclosures Apr 2026 + Jumeirah Lanka corporate guarantee HSBC", "SPAL press releases + ICRA Sep 2025"),
        (1062, "NSE/BSE SPAL quarterly filings + SPRV (Crocodile India retail) disclosures", "nseindia.com / bseindia.com / sprvl.in"),
        (1063, "ICRA credit-rating rationale Sep 2025 [verify FY26]", "icra.in"),
    ],
    footer="Cipher clean; 1,500+ lines; P. Sundararajan family Tirupur knitwear exporter; capex + export factoring + Sri Lanka cross-border + Crocodile retail + family-PB; FY25 +28% revenue surge.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 36-year arc from 1989 Tirupur partnership to listed Indian kids+infant apparel export leader with UK+Sri Lanka subsidiaries</div>

<h3>03A.1 Founding (1989) &mdash; P. Sundararajan's Tirupur partnership</h3>
<p>S.P. Apparels was originally <strong>promoted as a partnership firm by P. Sundararajan in 1989</strong>{ref("1060")} in the Tirupur knitwear cluster of Tamil Nadu. The Tirupur cluster (often called India's "Banian City") had emerged from the 1980s as the country's largest knitted-cotton-garment export hub &mdash; today producing 50%+ of India's knitwear exports. P. Sundararajan was among the second-wave entrepreneurs (after the 1970s-80s founding cohort of Tirupur exporters) building integrated knitwear export businesses for Western brand customers.</p>

<h3>03A.2 The 1990s &mdash; Integrated knitwear export capability</h3>
<p>Through the 1990s, S.P. Apparels grew from a small partnership to an integrated knitwear-export entity. The strategic moat was <strong>end-to-end vertical integration</strong>: raw cotton / yarn procurement → knitting → dyeing → cutting → stitching → finishing → packaging → export logistics. This compared favourably to the standard Tirupur model of fragmented sub-contracting across many small units. Plants expanded across Avinashi and Tirupur township.</p>

<h3>03A.3 The 2000s &mdash; Kids+infants niche + first global brand customers</h3>
<p>The 2000s saw S.P. Apparels carve out a specific niche in <strong>infant and children's knitted apparel</strong> &mdash; bodysuits, sleepsuits, tops, bottoms, dresses. The reason for the niche focus: kids+infant apparel has higher safety + quality + chemical-compliance requirements than general knitwear, creating a higher-margin segment with stickier customer relationships. Major customers added in this decade: <strong>Disney, Carter's, Babies R Us, Mothercare, Pumpkin Patch, OshKosh, Walmart, Target</strong>-tier global retailers + private-label brands.</p>

<h3>03A.4 Incorporation as Public Limited (2005) + Crocodile India retail (2010s)</h3>
<p>The partnership was <strong>incorporated as S.P. Apparels Limited on 10 November 2005</strong> (CIN L18101TZ2005PLC012295){ref("1060")} as a public limited company. The retail-apparel division was eventually hived off into a separate subsidiary, <strong>S.P. Retail Ventures Limited (SPRV)</strong>{ref("1062")}, which markets apparel under the <strong>Crocodile India</strong> brand &mdash; an Asian premium-casual menswear brand licensed/owned in India by SPRV.</p>

<h3>03A.5 IPO 2016 &mdash; Listing on BSE+NSE</h3>
<p>S.P. Apparels listed on BSE 540048 / NSE SPAL in 2016 via IPO &mdash; raising growth capital + providing partial-exit liquidity to P. Sundararajan family. Promoter holding has remained <strong>61.81%</strong> &mdash; one of the more closely-held listed Tirupur knitwear exporters.</p>

<h3>03A.6 The 2020-2024 transformation &mdash; Sri Lanka + UK + revenue surge</h3>
<p>The structural inflection. FY24 revenue Rs 1,087 Cr → <strong>FY25 revenue Rs 1,395 Cr (+28% YoY)</strong>{ref("1060")}. EBITDA margin Rs 196 Cr (18.0%) → Rs 231 Cr (16.6%). FY24 saw incorporation of <strong>S.P. Apparels (International) Private Limited (SPAIPL)</strong> in Sri Lanka{ref("1061")} &mdash; a strategic move to (a) access Sri Lankan GSP+ tariff preference for EU exports, (b) diversify away from concentration in Tamil Nadu production, (c) leverage Sri Lanka\'s skilled apparel workforce. April 2026 saw further capex: <strong>SPUK</strong> (UK subsidiary, Rs 6.31 Cr) + further SPAIPL investment (Rs 6.02 Cr); corporate guarantee of Rs 27.96 Cr extended for <strong>Jumeirah Lanka Pvt Ltd</strong>\'s HSBC loan{ref("1061")}.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 36-year arc tells you: (1) P. Sundararajan is a <strong>founder-builder</strong>, not a trader &mdash; integrated vertical capability + global-brand customer base + 36-year continuous management; (2) the <strong>kids+infants niche</strong> is one of the stickiest apparel-export segments &mdash; safety/compliance moat creates pricing power; (3) the <strong>FY25 +28% revenue surge</strong> + Sri Lanka + UK expansion signals an active growth-deployment phase, not a steady-state; (4) the <strong>USD/GBP export-receivable book</strong> (Disney/Carter's/Walmart-tier paper at investment-grade quality) is structural factoring opportunity; (5) the <strong>61.81% closely-held promoter family</strong> + private-trust + dual-generation Director cohort (P. Sundararajan + S. Latha) makes the family-PB opportunity sizeable; (6) the <strong>Crocodile India retail arm</strong> (SPRV) + adult-apparel diversification create cross-sell adjacencies.</p>
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
