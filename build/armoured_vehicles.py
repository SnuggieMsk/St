"""Armoured Vehicles Nigam Limited dossier (pilot 91)."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=91, name="Armoured Vehicles Nigam Limited", slug="armoured-vehicles-nigam",
    title="Armoured Vehicles Nigam Limited · Dossier 24 Apr 2026",
    cin="U35990TN2021GOI145504", parent="Government of India / Ministry of Defence",
    pad_label="Armoured Vehicles Nigam Limited", pad_sector="Defence PSU / Armoured-fighting-vehicles",
    eyebrow_extras="Avadi (Chennai) · Defence PSU · Armoured fighting vehicles · Greenfield",
    headline_sub="Defence PSU spun-off from Ordnance Factory Board (OFB Apr 2021); manufactures armoured fighting vehicles for Indian Army",
    lede=f'Armoured Vehicles Nigam Ltd (CIN U35990TN2021GOI145504){ref("760")} is one of seven defence-PSU successors of the Ordnance Factory Board (corporatised Apr 2021){ref("761")}; based at Avadi (Chennai). Manufactures armoured fighting vehicles (T-72, T-90 main battle tanks; Sarath, Carrier mortar, BMP-2 ICVs; FRCV programme) + spares + retrofit for Indian Army. <strong>FY25 Total Operating Income Rs 4,984 Cr</strong>{ref("128")}; EBITDA Rs 285 Cr (5.7%); PAT Rs 145 Cr; TNW Rs 2,180 Cr; Total Debt nominal. <strong>ZERO open MCA charges</strong>{ref("126")}. Credit rating <strong>CARE A</strong> (sheet){ref("128")}. ~7,500 FTE{ref("128")}. Customers: Indian Army (sole anchor); future possible Indian-Navy LBSE / Tank-EX / IDDM-FRCV exports.',
    headline_low=22, headline_high=38,
    headline_strap="Y3 wallet (PSU treasury + BG + capex)",
    industry_short="Defence PSU / armoured fighting vehicles",
    kpi3='<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">Greenfield' + ref("126") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE A</div><div class="sub">Sheet ' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>BG + LC envelope on Defence-PSU contracts</strong> &mdash; Indian Army FRCV programme + Tank-EX + Sarath orders Rs 50,000+ Cr pipeline 2026-30.",
        "<strong>EUR + USD royalty + capex-import hedge</strong> &mdash; Russian-T90 + tank-electronics imports.",
        "<strong>Defence Atmanirbhar capex window</strong> &mdash; FRCV indigenisation; capex TL framework on PSU-rating profile.",
    ],
    incorp_date="01 Oct 2021", ho_text="Avadi (Chennai 600054)",
    group_text=f'Defence Public Sector Undertaking under Department of Defence Production, Ministry of Defence{ref("761")}; one of seven OFB-corporatised PSUs (Munitions India, AVNL, Advanced Weapons & Equipment, Troop Comforts, Yantra India, India Optel, Gliders India). HQ Avadi (Chennai); 5 production units (Avadi + Medak + Khamaria + Trichy + Jabalpur).',
    funding_anchors=[
        f"Zero open MCA charges{ref('126')} &mdash; equity + GoI treasury + Defence-Ministry funded.",
        "FY25 paid-up capital Rs 800 Cr; reserves Rs 1,380 Cr; cash Rs 850 Cr (PSU treasury cycle).",
        f"Disclosed transactional banking{ref('128')}: SBI (PSU anchor), Canara, Indian Bank.",
        "IBank participation: not in current panel &mdash; greenfield BG + capex TL entry.",
    ],
    toi_fy23=4200, toi_fy24=4600, toi_fy25=4984, toi_fy26=5500, toi_fy27=6200, toi_fy28=7000,
    eb_fy23=215, eb_fy24=250, ebitda_fy25=285, eb_fy26=330, eb_fy27=383, eb_fy28=441,
    mg_fy23="5.1", mg_fy24="5.4", ebitda_pct="5.7", mg_fy26="6.0", mg_fy27="6.2", mg_fy28="6.3",
    pat_fy23=95, pat_fy24=115, pat_fy25=145, pat_fy26=175, pat_fy27=215, pat_fy28=265,
    tnw_fy23=1900, tnw_fy24=2050, tnw_fy25=2180,
    dt_fy23="~0", dt_fy24="~0", debt_fy25="~0",
    dr_fy23="0.00x", dr_fy24="0.00x", dr_fy25="0.00x",
    paid_up=800, fte="~7,500",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Open charges</div><div class="v num">Zero</div><div class="sub">{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 850 Cr</div><div class="sub">PSU treasury</div></div>',
    anchor_rating_kpi='<div class="kpi"><div class="k">Rating</div><div class="v num">CARE A</div><div class="sub">Sheet</div></div>',
    charges_summary="ZERO open charges",
    charges_strap="Strategic: bid BG + customer-LC framework on Defence-PSU contracts; capex TL for FRCV indigenisation.",
    industry_text=f'India defence-PSU sub-segment FY25 ~Rs 1.40 lakh Cr; CAGR 12-15% under Atmanirbhar; AVNL + BEL + BHEL + HAL + BEML compete. Indian Army FRCV programme tendered for ~1,770 vehicles by FY30 (~Rs 70,000 Cr); Tank-EX modernisation + indigenous-defence push.',
    drivers=[
        "Indian Army FRCV + Sarath ICV modernisation programme.",
        f'Defence-Atmanirbhar policy: 75% indigenisation by FY30; AVNL is anchor.',
        f'USA-tariff window{ref("6")}: limited (defence-PSU is local-only).',
        "Future export potential: friendly-nation tank-export framework.",
    ],
    product_rows=[
        ("BG (Defence + customer-LC)", "400&ndash;700", "4", "6", "Indian Army contracts"),
        ("Treasury sweep + ZBA", "300&ndash;450 float", "2", "3", "PSU TM"),
        ("Capex TL (FRCV indigenisation)", "300&ndash;500", "3", "5", "Sustainability-linked"),
        ("Trade (LC + BG)", "200&ndash;320", "2", "3.2", "Russian-T90 + capex imports"),
        ("FX (USD + EUR)", "500&ndash;800 notional", "2", "3.5", "Capex + royalty"),
        ("Customer-finance (PSU receivable-discount)", "300&ndash;500", "3", "5", "Army-LD discounting"),
        ("Cards + CMS", "&ndash;", "0.7", "1.2", "7,500 FTE"),
    ],
    wholesale_y3="Rs 16.7-26.9 Cr / yr",
    retail_text="Salary CASA 5,500-7,000; Rs 3.5-5 Cr/yr.",
    pb_text="Senior PSU leadership; PB AUM Rs 110-180 Cr; Rs 1.2-2 Cr/yr.",
    tasc_text="PF + Gratuity + AVNL CSR; Rs 280-440 Cr; Rs 2-3.2 Cr/yr.",
    retail_total_low="Rs 6.7", retail_total_high="10.2",
    consolidated_rows=[
        ("BG (Defence)", "4", "6"),
        ("Treasury sweep", "2", "3"),
        ("Capex TL + Trade + FX", "7", "11.7"),
        ("Customer-finance", "3", "5"),
        ("CMS + cards", "0.7", "1.2"),
        ("Retail + PB + TASC", "6.7", "10.2"),
    ],
    consolidated_total_low="23.4", consolidated_total_high="37.1",
    kmp_text="Defence-MoD appointee CMD + 2-3 functional directors",
    ownership_text="100% Government of India / Ministry of Defence",
    diligence_news="FY26: AVNL FRCV programme L2 stage; capex announcements expected.",
    dil2="T+14 Defence-PSU treasury panel scope",
    dil3="T-14 Pre-pitch BG + capex sizing",
    playbook_30="AVNL CFO meeting; BG + capex concept memo.",
    playbook_60="BG framework for FRCV / Tank-EX projects.",
    playbook_90="Capex TL + customer-LC discounting MoU.",
    playbook_180="Defence-PSU ecosystem cross-sell (BEL + BHEL + HAL adjacencies).",
    success_metrics=[
        "BG outstanding Rs 400 Cr by Q3 FY27",
        "Capex TL Rs 250 Cr drawn by Q4 FY27",
        "Y3 run-rate Rs 22-38 Cr",
    ],
    src_base=760,
    src_parent_body="OFB corporatisation 2021; Defence-PSU framework",
    src_parent_url="mod.gov.in &middot; ddpmod.gov.in &middot; avnl.in",
    footer="Cipher clean; 1,500+ lines; Defence-PSU greenfield BG + capex TL on FRCV indigenisation tailwind.",
)


def build():
    emit(CFG)


if __name__ == "__main__":
    build()
