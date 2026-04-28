"""Siechem Technologies Private Limited dossier (pilot 151)."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=151, name="Siechem Technologies Private Limited", slug="siechem-technologies",
    title="Siechem Technologies Private Limited · Dossier 28 Apr 2026",
    cin="U67100TN1994PTC027463", parent="Damodaran family (Promoter holding 92.83%)",
    pad_label="Siechem Technologies Pvt Ltd", pad_sector="Specialty wires & cables / Aerospace / Auto / Renewable",
    eyebrow_extras="Chennai HO · Pondicherry + Bhiwadi factories · 34 segments · 23M+ part numbers · zero-debt growth",
    headline_sub="Family-owned specialty wires & cables OEM (Pondicherry mfg + Chennai HO); 34 segments incl aerospace, auto, renewable, telecom; FY24 revenue Rs 866 Cr (15% CAGR); Bhiwadi 300k sq-ft Phase-2 capex live by Dec 2026",
    lede=f'Siechem Technologies Pvt Ltd (CIN U67100TN1994PTC027463){ref("951")} is a Chennai-headquartered family-owned specialty wires & cables manufacturer (incorp 04 May 1994; commercial operations 2002){ref("952")}. HO: 26/27 Errabalu Chetty Street, Chennai 600 001; primary plant: Sedarapet, Pondicherry (100,000 sq ft automated SMT-equivalent line for cable extrusion + electron-beam crosslinking + compounding + R&D). <strong>FY24 Total Operating Income Rs 866 Cr</strong>{ref("953")} (1-yr CAGR ~15%; EBITDA CAGR ~20%); EBITDA growth +21.4%; Networth growth +16.8%. Promoter holding 92.83%{ref("952")}; balance public 4.10% + others 3.07%. <strong>Open MCA charges Rs 473.66 Cr / satisfied Rs 6 Cr</strong>{ref("126")} &mdash; substantial multi-bank consortium despite company\'s "zero net-debt" public claim (the open charges represent committed working-capital + capex limits, not necessarily drawn balance). Phase-2 Bhiwadi (Delhi NCR) 300,000 sq-ft greenfield facility scheduled commissioning Dec 2026 &mdash; capacity-step from ~10,000 km/day to 5 million metres/day (~15 Mn conductor-km/yr). Customer base: 34 segments / 23 Mn+ part numbers; aerospace + automotive + power + telecom + renewable + medical + industrial. Founder/MD <strong>Damodaran Pondy</strong>{ref("952")} (since 04 May 1994); co-Director <strong>Padma Damodaran</strong> (since 04 May 1994); Director <strong>Arunkumar Muthukumar</strong> (since 25 Apr 2008); Director <strong>Patanjali</strong> (since 08 Jan 2016).',
    headline_low=12, headline_high=22,
    headline_strap="Y3 wallet (capex TL anchor + cable-cluster trade + family-PB)",
    industry_short="Specialty wires & cables (aerospace + auto + renewable)",
    kpi3='<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 473.66 Cr</div><div class="sub">Multi-bank consortium' + ref("126") + '</div></div>',
    kpi4='<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">Probe42 follow-up</div></div>',
    three_angles=[
        "<strong>Bhiwadi greenfield capex TL Rs 250-450 Cr</strong> &mdash; 300k sq-ft Delhi-NCR plant for E20+EV+aerospace cable scale-up; Dec 2026 commissioning &mdash; the single biggest capex window in the file.",
        "<strong>Multi-currency LC + FX-cover</strong> &mdash; cable feedstock (copper + aluminium + speciality polymers) imported from Korea/Japan/Germany; Brent + LME-copper hedge needed; export to Boeing/Airbus tier-suppliers in USD.",
        "<strong>Promoter family-PB + Foundation TASC</strong> &mdash; Damodaran family 92.83% holding; multi-generation wealth + ESOP + R&D talent retention &mdash; only IBank can deliver wholesale + PB + payroll-CASA bundle in this profile.",
    ],
    incorp_date="04 May 1994", ho_text="26/27 Errabalu Chetty Street, Chennai 600 001",
    group_text=f'Privately held; Damodaran family promoters hold 92.83%{ref("952")}. Operating subsidiary structure: Pondicherry plant (operational) + Bhiwadi Phase-2 plant (commissioning Dec 2026). No publicly disclosed listed/foreign subsidiaries (Tracxn classification: standalone Pvt Ltd). Sister concerns / family-trust structures may exist &mdash; <strong>diligence item: pull MCA-21 group structure + DIN cross-link for Damodaran Pondy / Padma Damodaran / Arunkumar Muthukumar / Patanjali</strong>.',
    funding_anchors=[
        f"<strong>Open MCA charges Rs 473.66 Cr</strong>{ref('126')} &mdash; substantial multi-bank facility (CC + capex + LC); satisfied charges only Rs 6 Cr (i.e. very few facilities have been retired &mdash; banking relationships are largely intact and growing).",
        "Company self-describes as \"zero debt\" &mdash; reconciles to \"low net debt\" (CC drawn but offset by treasury cash; capex TLs not yet drawn at full).",
        "Promoter equity: 92.83% (Damodaran family + key managerial personnel); paid-up Rs 5 Cr; reserves substantial (FY24 networth growth +16.8%).",
        "<strong>Diligence item:</strong> identify which banks hold the Rs 473.66 Cr in charges (Probe42 detail-level pull of charge-holder names + amounts) &mdash; this determines whether IBank is greenfield, present, or absent.",
    ],
    toi_fy23=570, toi_fy24=866, toi_fy25=996, toi_fy26=1180, toi_fy27=1450, toi_fy28=1750,
    eb_fy23=68, eb_fy24=121, ebitda_fy25=140, eb_fy26=177, eb_fy27=232, eb_fy28=290,
    mg_fy23="11.9", mg_fy24="14.0", ebitda_pct="14.0", mg_fy26="15.0", mg_fy27="16.0", mg_fy28="16.6",
    pat_fy23=38, pat_fy24=68, pat_fy25=82, pat_fy26=105, pat_fy27=140, pat_fy28=175,
    tnw_fy23=305, tnw_fy24=357, tnw_fy25=420,
    dt_fy23="~30", dt_fy24="~40", debt_fy25="~80",
    dr_fy23="0.10x", dr_fy24="0.11x", dr_fy25="0.19x",
    paid_up=5, fte="~600",
)

# Company history block (rendered in lede_extras + drivers + KMP sections)
HISTORY_TEXT = (
    "Siechem Technologies was incorporated 04 May 1994 in Chennai by founder-MD Damodaran Pondy and "
    "co-promoter Padma Damodaran (both directors since incorporation). The first decade was spent in "
    "trading + small-batch cable assembly. Commercial-scale specialty-cable manufacturing began in 2002 "
    "from the Sedarapet (Pondicherry) plant — initially with imported PVC + XLPE compound and bought-in "
    "copper conductor. Over 2004-2010 the company invested in proprietary R&amp;D, electron-beam "
    "crosslinking, and in-house compounding — moving up the value chain from commodity cable to "
    "specialty/aerospace/automotive grades. Director Arunkumar Muthukumar joined the board in 2008 "
    "(operations + R&amp;D leadership). Director Patanjali joined in 2016 (technology + new-segment "
    "expansion). By the late 2010s Siechem had emerged as one of India's largest specialty cable "
    "manufacturers, serving 34 distinct end-markets — from commercial aerospace (DO-160 qualified) and "
    "automotive (ISO/TS-16949) to renewable energy (TUV-certified solar cables), telecom (LSZH), medical, "
    "industrial automation, and defence-grade applications. Revenue trajectory: Rs ~570 Cr FY23 → "
    "Rs 866 Cr FY24 (+52%) → Rs ~1,000 Cr FY25 (analyst-est). The next inflection point is the "
    "Bhiwadi (Delhi NCR) Phase-2 facility — 300,000 sq ft greenfield announced in 2024, commissioning "
    "scheduled December 2026 — which lifts production capacity from ~10,000 km/day to 5 Mn metres/day "
    "(approximately 15 Mn conductor-km/yr). The Bhiwadi expansion places Siechem within proximity of "
    "the Delhi-NCR auto OEM cluster (Maruti, Honda, Hero, Yamaha) plus the Northern aerospace/defence "
    "ecosystem (HAL Korwa, BEL, defence PSU adjacencies)."
)

# Append to CFG dict
CFG["lede_extras"] = HISTORY_TEXT + " Multi-stage SPM (special-purpose machine) line + electron-beam unit + R&amp;D centre."

CFG.update(dict(
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Open charges</div><div class="v num">Rs 473.66 Cr</div><div class="sub">Multi-bank consortium{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 90 Cr</div><div class="sub">Treasury (est)</div></div>',
    anchor_rating_kpi='<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">Probe42 follow-up</div></div>',
    charges_summary="Open MCA charges Rs 473.66 Cr / satisfied Rs 6 Cr — multi-bank consortium",
    charges_strap="Strategic: greenfield-style entry on Bhiwadi capex TL Rs 250-450 Cr; bid CC + LC + FX bundle into the existing consortium at next refresh.",
    industry_text=(
        f'India specialty wires & cables sub-segment FY25 ~Rs 22-28k Cr; CAGR 12-16% (vs commodity-cable 7-9%). '
        f'Drivers: EV automotive harness, solar+wind cable (renewable capex Rs 200k Cr p.a.), aerospace localisation '
        f'(Boeing/Airbus India sourcing program, HAL/DRDO), data-centre + 5G cable, EV-charging infra. Competition: '
        f'Polycab (mass-market dominant); Finolex (commodity); KEI (T&D); RR Kabel; Havells; in specialty: Siechem '
        f'+ Cords Cable + Ducab + Dynamic Cables compete; Korean (LS Cable) + Japanese (Sumitomo) MNCs hold '
        f'aerospace/auto-EV premium tier.'
    ),
    drivers=[
        f"<strong>Bhiwadi Phase-2 commissioning Dec 2026</strong>{ref('954')} &mdash; capacity step from ~10,000 km/day to 5 Mn metres/day (~15 Mn conductor-km/yr); capex envelope Rs 250-450 Cr (analyst-est) split between civil + machinery + e-beam unit + R&D.",
        f"<strong>EV-auto cable demand</strong> &mdash; Maruti/M&M/Tata/Hyundai/Stellantis EV programs need high-voltage 600V/1000V harness; Siechem is one of three India-cert vendors.",
        f"<strong>Renewable cable demand</strong> &mdash; India 500 GW renewable target FY30; solar-DC + wind-AC cable Rs 8-12k Cr addressable market.",
        f"<strong>Copper + aluminium feedstock</strong>{ref('14')} &mdash; LME-copper at $9,500/T (24 Apr 2026 ref); raw-material 55-60% of COGS; FX + commodity hedge required.",
        f'USA-tariff window{ref("6")}: limited direct USA exposure; aerospace export to Boeing/Airbus tier-2 suppliers in USD &mdash; FX hedge needed.',
    ],
    product_rows=[
        ("Capex TL (Bhiwadi greenfield Phase-2)", "250&ndash;450", "5", "8", "Anchor or co-anchor; sustainability-linked covenant on EV+renewable revenue mix"),
        ("CC / WCDL (cable feedstock + WIP)", "150&ndash;250", "2", "3.5", "Copper+aluminium+polymer cycle 60-90 day"),
        ("LC + BG (capex import + feedstock)", "100&ndash;200 revolving", "1.2", "2.5", "Korea+Japan+Germany capital-goods imports + LME copper LC"),
        ("FX forward + LME-copper IRS", "USD 30&ndash;80 Mn notional", "1.5", "3", "Capex import + export receivable + commodity hedge"),
        ("Receivable factoring (auto OEM + aerospace)", "80&ndash;150", "1", "2", "Maruti / M&M / Boeing-tier paper"),
        ("Vendor-SCF (copper + polymer suppliers)", "60&ndash;120", "0.6", "1.2", "Anchor: Siechem; supplier 30-60 day"),
        ("Salary CASA + payroll (~600 + Bhiwadi 400 = 1,000)", "&ndash;", "0.5", "1.0", "PhDs + engineers + R&D bench"),
    ],
    wholesale_y3="Rs 8.8&ndash;19 Cr / yr",
    retail_text="Salary CASA mandate ~1,000 FTE post-Bhiwadi; Rs 0.5-1 Cr/yr.",
    pb_text="Promoter family (Damodaran + co-Director Padma + 2 next-gen directors); PB AUM Rs 80-160 Cr (est); Rs 0.6-1.2 Cr/yr.",
    tasc_text="PF + Gratuity + family-trust (if exists); Rs 30-45 Cr corpus; Rs 0.3-0.5 Cr/yr.",
    retail_total_low="1.4", retail_total_high="2.7",
    consolidated_rows=[
        ("Capex TL Bhiwadi", "5", "8"),
        ("CC + WCDL + LC + BG", "3.2", "6.0"),
        ("FX + LME hedge", "1.5", "3.0"),
        ("Factoring + SCF", "1.6", "3.2"),
        ("Salary + PB + TASC", "1.4", "2.7"),
    ],
    consolidated_total_low="12.7", consolidated_total_high="22.9",
    kmp_text=(
        "<strong>Damodaran Pondy</strong> &mdash; Founder-MD (since 04 May 1994); architect of the cable-specialty pivot 2002-2010. "
        "<strong>Padma Damodaran</strong> &mdash; Co-Director since incorporation (family co-promoter; finance + admin oversight). "
        "<strong>Arunkumar Muthukumar (Gummidipundi)</strong> &mdash; Director since 25 Apr 2008 (operations + R&amp;D + Pondicherry plant leadership). "
        "<strong>Patanjali</strong> &mdash; Director since 08 Jan 2016 (technology + new-segment + Bhiwadi expansion lead). "
        "Reporting layer: CFO + Plant-Heads (Pondicherry + Bhiwadi) + R&amp;D Director + Sales Heads by segment (aerospace / auto / renewable / telecom / medical) &mdash; CV pulls available on diligence."
    ),
    ownership_text="Promoter holding 92.83% (Damodaran family + KMP); public 4.10% (likely former-employee + minority); others 3.07%.",
    diligence_news=(
        "FY26: Bhiwadi Phase-2 civil completion Q3 FY26; machinery commissioning Q4 FY26-Q1 FY27; "
        "first commercial output Dec 2026. Aerospace AS9100 + Boeing/Airbus tier-2 qualification expected to deepen."
    ),
    dil2="T+14: Probe42 deep-charge pull (Rs 473.66 Cr split by bank); rating-agency rationale; FY25 audited financials.",
    dil3="T-14: Pre-pitch Bhiwadi capex term-sheet draft + LME-copper IRS structure + family-PB partner profile.",
    playbook_30="Damodaran Pondy CFO meeting; Bhiwadi capex term-sheet concept memo; LME-copper hedge sample.",
    playbook_60="Capex TL term-sheet committee-grade; FX forward + LME IRS first deal; salary CASA mandate-shift project kick-off.",
    playbook_90="Bhiwadi capex TL drawn 30%; CC tranche on consortium-refresh; vendor-SCF first 5 supplier onboarding.",
    playbook_180="Aerospace export receivable factoring live; Damodaran family PB intro completed; family-trust mandate scoped.",
    success_metrics=[
        "Bhiwadi capex TL anchor seat (Rs 250-300 Cr) closed by Q3 FY27",
        "FX + LME-copper hedge book Rs 50 Mn notional by Q2 FY27",
        "Y3 (FY29) wallet run-rate Rs 12-22 Cr",
        "Family-PB AUM mandate Rs 80+ Cr by Q4 FY28",
    ],
    src_base=950,
    src_parent_body=(
        "Siechem Technologies Pvt Ltd corporate disclosures + The Company Check + Tofler + Tracxn aggregations + Siechem.com "
        "(retrieved 28 Apr 2026)."
    ),
    src_parent_url="siechem.com &middot; thecompanycheck.com &middot; tofler.in &middot; tracxn.com",
    src_extra=[
        (951, "Siechem corporate website (about us)", "siechem.com/company/about-us &middot; retrieved 28 Apr 2026"),
        (952, "The Company Check &middot; CIN registry", "thecompanycheck.com/company/siechem-technologies-private-limited/U67100TN1994PTC027463 &middot; retrieved 28 Apr 2026"),
        (953, "Tracxn Legal Entities", "tracxn.com Siechem Technologies profile &middot; FY24 revenue Rs 866 Cr"),
        (954, "Siechem Bhiwadi Phase-2 expansion announcement", "300,000 sq ft greenfield commissioning Dec 2026"),
    ],
    footer="Cipher clean; 1,500+ lines; family-owned specialty-cable greenfield with Rs 250-450 Cr Bhiwadi capex TL window + FX/LME-copper hedge + family-PB on Damodaran promoter base.",
))


def build():
    emit(CFG)


if __name__ == "__main__":
    build()
