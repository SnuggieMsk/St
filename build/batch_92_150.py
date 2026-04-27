"""Batch generator for pilots 92-150. Compact configs expanded via _compact.expand and emitted via _template.emit."""
from ._compact import expand
from ._template import emit
from .base import ref


def _greenfield_charges():
    return dict(charges_summary="ZERO open charges", ibank_state='greenfield')


def _consol(rows, lo, hi):
    return dict(consolidated_rows=rows, consolidated_total_low=lo, consolidated_total_high=hi)


SPECS = []

# Pilot 92 — Integrated Service Point (agri-services PSU-listed)
SPECS.append(dict(
    pilot=92, slug="integrated-service-point",
    name="Integrated Service Point Limited",
    cin="U45203TN1999PLC042586",
    parent="Indian-origin promoter group",
    parent_long="an Indian-origin TN-listed agri-services + supply-chain group",
    industry_short="Agri services + supply-chain",
    industry_long="Agriculture & farming services + supply-chain logistics",
    eyebrow_extras="Chennai · Agri services · Listed · Greenfield",
    headline_sub="Listed Indian agri-services + supply-chain",
    lede_role="a TN-listed agri-services + supply-chain entity",
    lede_extras="Operations: rural agri-input distribution + farmer-supply-chain logistics + warehousing.",
    incorp_date="01 Mar 1999", ho="Chennai",
    headline_low=14, headline_high=24,
    headline_strap="Y3 wallet (CC + WCDL + agri-SCF)",
    toi=2505, ebitda_pct=4.5, fte="~850",
    angles=[
        "<strong>Agri-SCF + farmer-finance origination</strong> &mdash; cotton, coir, oil-seeds supply-chain.",
        "<strong>Listed-corp DCM access</strong> &mdash; pre-arranger position.",
        "<strong>CC + WCDL refresh</strong> &mdash; rated B; bid the next refresh.",
    ],
    rating_text="CARE B (sheet)", rating_kpi_sub=f'Sheet{ref("128")}',
    group_text="TN-listed agri-services + supply-chain group; rural distribution + farmer-supply chain + warehousing operations.",
    funding_anchors=[f"Sheet rating B{ref('128')}; bid refresh window.","FY25 paid-up Rs 25 Cr; reserves Rs 950 Cr.","IBank participation: not in current panel — CC+WCDL entry.","Listed-corp DCM mandate window."],
    industry_text=f'India agri-services + warehousing market FY25 ~Rs 1.20 lakh Cr; CAGR 8-10%; CACP MSP{ref("13")} + monsoon{ref("4")} drive demand. Storage + logistics + farmer-finance digitisation continuing.',
    drivers=[f'Monsoon{ref("4")} + MSP cycle.','Cold-chain + warehouse capex.',f'USA-tariff{ref("6")}: limited.','Digital agri-finance + Kisan-Credit-Card scope.'],
    product_rows=[
        ("CC + WCDL refresh","100&ndash;160","2","3.2","Sheet B"),
        ("Capex TL (warehouse)","100&ndash;180","1","1.8","Sustainability-linked"),
        ("Trade (LC + BG)","80&ndash;120","0.8","1.2","Agri-input imports"),
        ("Customer-SCF","150&ndash;240","1.5","2.4","Farmer + dealer"),
        ("FX (USD)","150&ndash;220 notional","0.6","1","Imports"),
        ("Cards + CMS","&ndash;","0.4","0.6","850 FTE"),
    ],
    consolidated_rows=[("CC+WCDL","2","3.2"),("Capex+Trade","1.8","3"),("Customer-SCF","1.5","2.4"),("FX","0.6","1"),("CMS","0.4","0.6"),("Retail+PB+TASC","3","4.5")],
    consolidated_total_low="9.3", consolidated_total_high="14.7",
    src_base=770,
    src_parent_url="bseindia.com &middot; nseindia.com",
    play_summary="agri-SCF + listed-corp DCM",
    pad_sector="Agri services + supply-chain / Indian-origin",
    **_greenfield_charges(),
))

# Pilot 93 — Flender Drives (Siemens-Flender German MNC)
SPECS.append(dict(
    pilot=93, slug="flender-drives",
    name="Flender Drives Private Limited",
    cin="U29309TN2020FTC137354",
    parent="Flender GmbH (Germany; Carlyle-owned)",
    parent_long="Flender GmbH (private German industrial-drives MNC, Carlyle PE-owned post-Siemens spin)",
    industry_short="Industrial drives + gearbox",
    industry_long="Industrial gearbox + drives + couplings + motor",
    eyebrow_extras="Chennai · Carlyle/Flender · Industrial drives · Greenfield",
    headline_sub="Carlyle-owned Flender GmbH Indian gearbox + drives subsidiary",
    lede_role="the Indian subsidiary of Flender GmbH (Germany; Carlyle-owned post-2021 spin from Siemens)",
    lede_extras="Manufactures industrial gearboxes + drives + couplings for cement, steel, wind, mining, marine.",
    incorp_date="06 Apr 2020", ho="Chennai",
    headline_low=18, headline_high=30,
    headline_strap="Y3 wallet (FX + customer-SCF + capex)",
    toi=2159, ebitda_pct=11.0, fte="~1,200",
    angles=[
        "<strong>EUR royalty + RM-import hedge</strong> &mdash; Flender Germany intercompany.",
        "<strong>Customer-SCF on cement + steel + wind anchors</strong>.",
        "<strong>Wind-gearbox + EV-drive capex window</strong> on offshore-wind ramp.",
    ],
    rating_text="Sheet B", rating_kpi_sub=f'Sheet{ref("128")}',
    group_text="Flender GmbH; FY25 ~€2.1 bn revenue; Carlyle PE-owned post Siemens spin Mar 2021.",
    funding_anchors=[f"Zero open MCA charges{ref('126')}; equity + parent ICDs.","FY25 paid-up Rs 80 Cr.",f"Disclosed banking{ref('128')}: Deutsche Bank, HSBC, Citi.","IBank: greenfield FX + customer-SCF entry."],
    industry_text=f'India industrial-drives market FY25 ~Rs 38,000 Cr; CAGR 10-12%; Flender + ABB + Bonfiglioli + Brevini + David Brown compete. Wind + cement + EV-drive segments structural growth.',
    drivers=[f'Wind-gearbox demand (offshore 25 GW FY30).','Cement + steel capex cycle.',f'USA-tariff{ref("6")}: India industrial-drive export ramp.',f'EU CBAM{ref("18")}: scope-3 reporting.'],
    product_rows=[
        ("FX (EUR + USD)","700&ndash;1,000 notional","3","5","Royalty + RM"),
        ("Customer-SCF (cement + wind)","250&ndash;400","2.5","4","OEM anchors"),
        ("Capex TL (wind-gearbox ramp)","150&ndash;250","1.5","2.5","Sustainability-linked"),
        ("Trade (LC + BG)","100&ndash;160","1","1.6","RM"),
        ("EBR / PCFC","100&ndash;160","1","1.6","Export"),
        ("Cards + CMS","&ndash;","0.4","0.7","1,200 FTE"),
    ],
    consolidated_rows=[("FX","3","5"),("Customer-SCF","2.5","4"),("Capex+Trade+EBR","3.5","5.7"),("CMS","0.4","0.7"),("Retail+PB+TASC","3","4.5")],
    consolidated_total_low="12.4", consolidated_total_high="19.9",
    src_base=780,
    src_parent_url="flender.com &middot; carlyle.com",
    play_summary="greenfield FX + customer-SCF + wind-gearbox capex",
    pad_sector="Industrial drives + gearbox / Flender Germany",
    **_greenfield_charges(),
))

# Pilot 94 — Visteon Electronics India (Korean Visteon-Halla)
SPECS.append(dict(
    pilot=94, slug="visteon-electronics",
    name="Visteon Electronics India Private Limited",
    cin="U35122TN2015PTC099885",
    parent="Visteon Corp (US, NASDAQ: VC)",
    parent_long="Visteon Corp (NASDAQ: VC; FY25 revenue ~$3.8 bn) automotive-cockpit electronics major",
    industry_short="Auto cockpit electronics",
    industry_long="Auto cockpit electronics + digital instrumentation + infotainment",
    eyebrow_extras="Maraimalai Nagar · Visteon Corp US · Auto cockpit electronics · Greenfield",
    headline_sub="Visteon Corp Indian cockpit-electronics + digital-cluster + infotainment subsidiary",
    lede_role="the Indian subsidiary of Visteon Corp",
    lede_extras="Manufactures digital-cockpit displays, instrument clusters, infotainment, head-up displays for global OEMs.",
    incorp_date="13 Apr 2015", ho="Maraimalai Nagar (Chennai)",
    headline_low=18, headline_high=30,
    toi=2112, ebitda_pct=11.5, fte="~1,800",
    angles=[
        "<strong>USD royalty + RM-import hedge</strong>.",
        "<strong>Customer-SCF on Hyundai + Tata + Mahindra + Maruti anchors</strong>.",
        "<strong>SDV + ADAS-cockpit transition capex window</strong>.",
    ],
    rating_text="[diligence]", rating_kpi_sub=f'No Probe42',
    group_text="Visteon Corp NASDAQ-listed; FY25 ~$3.8 bn revenue; cockpit + electronics tier-1.",
    funding_anchors=[f"Zero open MCA charges{ref('126')}.",f"Disclosed banking{ref('128')}: Citi, JPMorgan.","IBank: greenfield FX + customer-SCF entry."],
    industry_text=f'India cockpit-electronics market FY25 ~Rs 24,000 Cr; CAGR 18-22%; Visteon + Continental + Bosch + Harman + Denso compete. SDV + ADAS structural growth.',
    drivers=['SDV + ADAS-cockpit transition.',f'USA-tariff{ref("6")}: India cockpit export ramp.','EV-cockpit + digital-cluster premiumisation.','OEM software-defined-vehicle pivots.'],
    product_rows=[
        ("FX (USD)","800&ndash;1,200 notional","3.5","5.5","Royalty + RM"),
        ("Customer-SCF (Hyundai/Tata)","300&ndash;500","3","5","OEM"),
        ("Capex TL (SDV ramp)","150&ndash;250","1.5","2.5","Sustainability-linked"),
        ("Trade","150&ndash;240","1.5","2.4","Imports"),
        ("EBR / PCFC","120&ndash;200","1.2","2","Export"),
        ("Cards + CMS","&ndash;","0.6","0.9","1,800 FTE"),
    ],
    consolidated_rows=[("FX","3.5","5.5"),("Customer-SCF","3","5"),("Capex+Trade+EBR","4.2","6.9"),("CMS","0.6","0.9"),("Retail+PB+TASC","3.5","5.5")],
    consolidated_total_low="14.8", consolidated_total_high="23.8",
    src_base=790,
    src_parent_url="visteon.com &middot; sec.gov",
    play_summary="greenfield FX + customer-SCF + SDV-cockpit capex",
    pad_sector="Auto cockpit electronics / Visteon Corp US",
    **_greenfield_charges(),
))


def build_one(spec):
    cfg = expand(spec)
    emit(cfg)


def build_all():
    import traceback
    for s in SPECS:
        try:
            build_one(s)
        except Exception as e:
            print(f"FAIL pilot {s['pilot']}: {e}")
            traceback.print_exc()


def mnc_gf(pilot, slug, name, cin, parent, parent_long, ho, incorp, industry_short,
           toi, ebitda_pct, fte, paid_up, src_base, parent_url,
           industry_text, drivers, product_rows, consol_rows, consol_lo, consol_hi,
           rating="[diligence]", rating_sub="No Probe42",
           three_angles=None, headline_low=None, headline_high=None,
           lede_role=None, lede_extras="", group_text=None, pad_sector=None,
           play_summary="greenfield FX + customer-SCF + capex"):
    if headline_low is None:
        headline_low = max(14, round(toi * 0.011))
    if headline_high is None:
        headline_high = max(headline_low+8, round(toi * 0.018))
    if lede_role is None:
        lede_role = f"the Indian subsidiary of {parent}"
    if group_text is None:
        group_text = f"{parent_long}; standard MNC-captive India operations + manufacturing/services."
    if pad_sector is None:
        pad_sector = f"{industry_short} / {parent}"
    if three_angles is None:
        three_angles = [
            f"<strong>FX royalty + RM-import hedge</strong> &mdash; {parent} intercompany.",
            "<strong>Customer-SCF on Indian + global anchor customers</strong>.",
            "<strong>Capex + product capex window</strong> on India growth-region.",
        ]
    return dict(
        pilot=pilot, slug=slug, name=name, cin=cin, parent=parent, parent_long=parent_long,
        industry_short=industry_short, industry_long=industry_short,
        eyebrow_extras=f"{ho.split('(')[0].strip()} · {parent.split(';')[0].split('(')[0].strip()} · {industry_short} · Greenfield",
        headline_sub=f"{parent} Indian {industry_short.lower()} subsidiary",
        lede_role=lede_role, lede_extras=lede_extras,
        incorp_date=incorp, ho=ho,
        headline_low=headline_low, headline_high=headline_high,
        headline_strap="Y3 wallet (FX + customer-SCF + capex)",
        toi=toi, ebitda_pct=ebitda_pct, fte=fte, paid_up=paid_up,
        angles=three_angles,
        rating_text=rating, rating_kpi_sub=rating_sub,
        group_text=group_text,
        funding_anchors=[f"Zero open MCA charges{ref('126')} — equity + parent ICDs.",
                         f"FY25 paid-up Rs {paid_up} Cr; cash-positive MNC-treasury.",
                         f"Disclosed banking{ref('128')}: parent-anchor + 2-3 transactional banks.",
                         "IBank: not in current panel — greenfield FX + customer-SCF entry."],
        industry_text=industry_text, drivers=drivers, product_rows=product_rows,
        consolidated_rows=consol_rows, consolidated_total_low=consol_lo, consolidated_total_high=consol_hi,
        src_base=src_base, src_parent_url=parent_url,
        play_summary=play_summary, pad_sector=pad_sector,
        **_greenfield_charges(),
    )


# Pilot 95 — Kingfa Science (Chinese specialty plastics, listed)
SPECS.append(mnc_gf(
    pilot=95, slug="kingfa-science", name="Kingfa Science & Technology India Limited",
    cin="L25209TN1983PLC010438", parent="Kingfa Sci. & Tech. Co (China; SHE: 600143)",
    parent_long="Kingfa Sci. & Tech. Co Ltd (China; Shanghai listed) modified-plastics + biodegradable-plastics major (~$5 bn revenue)",
    ho="Chennai", incorp="06 Oct 1983", industry_short="Modified plastics + biodegradable",
    toi=1744, ebitda_pct=10.5, fte="~1,200", paid_up=85, src_base=800,
    parent_url="kingfa.com &middot; sse.com.cn",
    industry_text=f'India modified-plastics market FY25 ~Rs 28,000 Cr; CAGR 10-12%; Kingfa + Sabic + Borealis + Reliance Polymers compete.',
    drivers=[f'EU CBAM{ref("18")}: scope-3 reporting; biodegradable ramp.','Auto + appliance + EV-comp customer ramp.',f'USA-tariff{ref("6")}: India plastics export.','Premiumisation + EV-grade plastics.'],
    product_rows=[("FX (CNY + USD)","700&ndash;1,000 notional","3","5","Royalty + RM"),("Customer-SCF","250&ndash;400","2.5","4","Auto + appliance"),("Capex TL (EV-grade ramp)","150&ndash;240","1.5","2.4","Sustainability"),("Trade","100&ndash;160","1","1.6","Imports"),("EBR / PCFC","100&ndash;160","1","1.6","Export"),("Cards + CMS","&ndash;","0.4","0.7","1,200 FTE")],
    consol_rows=[("FX","3","5"),("Customer-SCF","2.5","4"),("Capex+Trade+EBR","3.5","5.6"),("CMS","0.4","0.7"),("Retail+PB+TASC","3","4.5")],
    consol_lo="12.4", consol_hi="19.8",
))

# Pilot 96 — K H Exports (Indian leather export)
SPECS.append(mnc_gf(
    pilot=96, slug="k-h-exports", name="K H Exports India Private Limited",
    cin="U19129TN1985PTC011821", parent="Promoter family (Indian-origin leather exporter)",
    parent_long="K H Exports / Florind Shoes Indian leather + footwear export major",
    ho="Chennai", incorp="14 Jun 1985", industry_short="Leather + footwear export",
    toi=1415, ebitda_pct=9.5, fte="~3,500", paid_up=65, src_base=810,
    parent_url="khexports.com",
    industry_text=f'India leather + footwear export FY25 ~Rs 36,000 Cr; CAGR 7-9%; KH + Farida + Florind + Hindustan Lever compete. EU + USA + UAE export anchors.',
    drivers=[f'USA-tariff{ref("6")}: India leather export.',f'EU CBAM{ref("18")}: scope-3 + EUDR cotton-traceability.','Premiumisation + footwear branded segments.','Vertical integration (tannery to brand).'],
    product_rows=[("CC + WCDL refresh","60&ndash;100","1.5","2.4","Sheet B"),("EBR / PCFC (export)","350&ndash;500","3","5","60%+ export"),("Trade","100&ndash;160","1","1.6","Imports"),("FX (USD + EUR)","800&ndash;1,200 notional","3.5","5.5","Export"),("Capex TL","100&ndash;160","1","1.6","Sustainability"),("Cards + CMS","&ndash;","0.4","0.7","3,500 FTE")],
    consol_rows=[("CC+WCDL","1.5","2.4"),("EBR/PCFC","3","5"),("FX","3.5","5.5"),("Trade+Capex","2","3.2"),("CMS","0.4","0.7"),("Retail+PB+TASC","3","4.5")],
    consol_lo="13.4", consol_hi="21.3",
))

# Pilot 97 — Daebu Automotive Seat (Korean auto-seat)
SPECS.append(mnc_gf(
    pilot=97, slug="daebu-automotive-seat", name="Daebu Automotive Seat India Private Limited",
    cin="U50500TN2006PTC061322", parent="Daebu Automotive Co (Korea; KOSPI)",
    parent_long="Daebu Automotive Korean auto-seat + interior tier-1 (Hyundai-Kia ecosystem)",
    ho="Sriperumbudur (Chennai)", incorp="15 Mar 2006", industry_short="Auto seat + interior",
    toi=1411, ebitda_pct=9.5, fte="~1,600", paid_up=60, src_base=820,
    parent_url="daebu.kr",
    industry_text='India auto-seat market FY25 ~Rs 9,800 Cr; CAGR 9-11%; Daebu + Faurecia (pilot 25) + Magna Seating + Adient compete. Hyundai-Kia ecosystem captive.',
    drivers=[f'Hyundai-Kia capacity ramp{ref("11")}.',f'USA-tariff{ref("6")}: HMG export benefit.','EV-seat + premiumisation.','Korean MNC ecosystem cross-sell.'],
    product_rows=[("FX (KRW + USD)","500&ndash;750 notional","2.5","4","Royalty + RM"),("Customer-SCF (Hyundai/Kia)","200&ndash;320","2","3.2","OEM"),("Capex TL","100&ndash;160","1","1.6","Sustainability"),("Trade","80&ndash;120","0.8","1.2","Imports"),("CC + WCDL refresh","60&ndash;100","1.5","2.4","Sheet A"),("Cards + CMS","&ndash;","0.4","0.6","1,600 FTE")],
    consol_rows=[("FX","2.5","4"),("Customer-SCF","2","3.2"),("Capex+Trade","1.8","2.8"),("CC+WCDL","1.5","2.4"),("CMS","0.4","0.6"),("Retail+PB+TASC","3","4.5")],
    consol_lo="11.2", consol_hi="17.5",
    rating="Sheet A",
))


# Pilot 98 — Indian Additives (Chevron-Oronite/SPIC JV; engine-oil additives)
SPECS.append(mnc_gf(98, "indian-additives", "Indian Additives Limited",
    "U24294TN1989PLC017705", "Chevron-Oronite + SPIC JV (US/India)",
    "Indian Additives Limited (Chevron-Oronite/IOCL JV) lubricant + engine-oil additives manufacturer",
    "Manali (Chennai)", "01 Jan 1989", "Lubricant + engine-oil additives",
    1307, 12.0, "~600", 60, 830, "iadditives.com",
    f'India lubricant-additives FY25 ~Rs 16,000 Cr; CAGR 7-9%; Indian Additives + Lubrizol + Afton + Infineum compete.',
    [f'BS6/Tier-V emission ramp.',f'EU CBAM{ref("18")}: scope-3.','EV-fluid + e-axle additives transition.','Refinery + petrochem capex.'],
    [("FX (USD)","550&ndash;800 notional","2","3","Royalty"),("Customer-SCF (IOCL/HPCL/BPCL)","250&ndash;380","2.5","4","PSU OMC anchors"),("Capex TL","100&ndash;180","1","1.8","Sustainability"),("Trade","100&ndash;160","1","1.6","Imports"),("EBR/PCFC","80&ndash;130","0.8","1.4","Export"),("Cards + CMS","&ndash;","0.3","0.5","600 FTE")],
    [("FX","2","3"),("Customer-SCF","2.5","4"),("Capex+Trade+EBR","2.8","4.8"),("CMS","0.3","0.5"),("Retail+PB+TASC","2.5","3.5")],
    "10.1", "15.8", rating="Sheet A"))

# Pilot 99 — Tiger Analytics (US/Indian-origin analytics consulting)
SPECS.append(mnc_gf(99, "tiger-analytics", "Tiger Analytics India Consulting Pvt Ltd",
    "U74999TN2021FTC146673", "Tiger Analytics Inc (US, PE-backed)",
    "Tiger Analytics Inc, US-headquartered Indian-origin analytics + AI consulting major (~$300 mn revenue)",
    "Chennai", "07 Apr 2021", "AI + analytics consulting / GCC",
    1298, 16.5, "~5,500", 60, 840, "tigeranalytics.com",
    f'India analytics-consulting + GCC FY25 ~Rs 2.10 lakh Cr (NASSCOM){ref("140")}; Tiger + Mu Sigma + Fractal + LatentView compete.',
    [f'USA-tariff{ref("6")}: services-tariff zero.','Gen-AI + agentic-AI scope expansion.','GCC + retail-mass on FTE base.','PE-exit + IPO mandate window 24-36 mo.'],
    [("FX (USD)","1,200&ndash;1,800 notional","5","8","100% USD billing"),("Treasury sweep","250&ndash;380","2","3","MNC TM"),("EBR / PCFC","200&ndash;320","2","3.2","Receivables"),("Salary + retail asset (5,500)","500&ndash;800/yr","4","7","Auto + home + cards"),("PB (founders + ESOP)","220&ndash;350 AUM","2.5","4","UHNI"),("TASC + ESOP-Trust","180&ndash;280","1.5","2.4","PF + Gratuity")],
    [("FX","5","8"),("Treasury+EBR","4","6.2"),("Retail+PB+TASC","8","13.4"),("Cards","1","1.8"),("Other","2","3")],
    "20", "32.4", rating="[diligence]"))

# Pilot 100 — Murata Electronics India (Japanese passive components)
SPECS.append(mnc_gf(100, "murata-electronics", "Murata Electronics India Private Limited",
    "U29268TN2010FTC077446", "Murata Manufacturing Co (Japan; TSE: 6981)",
    "Murata Manufacturing Co (TSE: 6981; ~$15 bn revenue) Japanese passive-electronics components major",
    "Chennai", "20 Sep 2010", "Passive electronics components",
    1214, 13.0, "~1,100", 50, 850, "murata.com &middot; jpx.co.jp",
    f'India passive-components market FY25 ~Rs 22,000 Cr; CAGR 13-15%; Murata + Yageo + Samsung Electro-Mechanics compete.',
    [f'EMS + smartphone export ramp{ref("31")}.','EV-passive + 5G + AI-data-centre demand.',f'USA-tariff{ref("6")}: India electronics export.','Mid-tier MLCC + capacitor capex.'],
    [("FX (JPY + USD)","700&ndash;1,000 notional","3","5","Royalty"),("Customer-SCF (EMS)","200&ndash;320","2","3.2","Bharat FIH/Foxconn"),("Capex TL","150&ndash;240","1.5","2.4","Sustainability"),("Trade","100&ndash;160","1","1.6","Imports"),("EBR/PCFC","80&ndash;130","0.8","1.4","Export"),("Cards + CMS","&ndash;","0.4","0.6","1,100 FTE")],
    [("FX","3","5"),("Customer-SCF","2","3.2"),("Capex+Trade+EBR","3.3","5.4"),("CMS","0.4","0.6"),("Retail+PB+TASC","3","4.5")],
    "11.7", "18.7"))

# Pilot 101 — KUN Auto Company (TN auto-dealer chain)
SPECS.append(mnc_gf(101, "kun-auto", "K.U.N. Auto Company Pvt Ltd",
    "U74999TN1997PTC039547", "KUN Group (Indian-origin TN auto-dealer)",
    "KUN Group multi-brand auto-dealership chain (Mercedes, Toyota, Hyundai, Maruti) headquartered Chennai",
    "Chennai", "12 Mar 1997", "Auto retail / dealership",
    1204, 4.5, "~2,500", 50, 860, "kungroup.in",
    f'India auto-retail FY25 ~Rs 5.2 lakh Cr; CAGR 7-9%; large multi-brand dealer chains consolidating.',
    [f'PV market growth{ref("11")}.','EV-retail transition.','Used-car + SCF expansion.','Service revenue annuity.'],
    [("CC + WCDL refresh","100&ndash;160","2","3.2","Sheet B"),("Inventory financing","250&ndash;380","2.5","4","Multi-brand"),("Retail auto-finance origination","400&ndash;600/yr","3","5","NBFC tie-up"),("Trade","60&ndash;100","0.6","1","Imports"),("Capex TL","80&ndash;130","0.8","1.4","Service-bay ramp"),("Cards + CMS","&ndash;","0.4","0.6","2,500 FTE")],
    [("CC+WCDL","2","3.2"),("Inventory","2.5","4"),("Retail-finance","3","5"),("Capex+Trade","1.4","2.4"),("CMS","0.4","0.6"),("Retail+PB+TASC","2.5","3.5")],
    "11.8", "18.7", rating="Sheet B"))

# Pilot 102 — Komos Automotive (Korean auto-comp)
SPECS.append(mnc_gf(102, "komos-automotive", "Komos Automotive India Pvt Ltd",
    "U50500TN2006PTC060925", "Komos Korea / Hyundai Mobis ecosystem",
    "Komos Korean auto-component (interior trim) tier-1 supplier to Hyundai-Kia",
    "Sriperumbudur (Chennai)", "06 Mar 2006", "Auto interior trim",
    1133, 8.5, "~1,400", 50, 870, "komosgroup.com",
    f'India auto-trim market ~Rs 14,000 Cr; CAGR 9-11%; Hyundai-Kia ecosystem.',
    [f'Hyundai-Kia ramp{ref("11")}.',f'USA-tariff{ref("6")}.','EV-cabin transition.','Korean MNC ecosystem cross-sell.'],
    [("FX (KRW + USD)","450&ndash;650 notional","2","3","Royalty"),("Customer-SCF","180&ndash;280","1.8","2.8","Hyundai/Kia"),("Capex TL","80&ndash;130","0.8","1.3","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("CC + WCDL","60&ndash;100","1.2","2","Sheet B"),("Cards + CMS","&ndash;","0.3","0.5","1,400 FTE")],
    [("FX","2","3"),("Customer-SCF","1.8","2.8"),("Capex+Trade","1.4","2.3"),("CC+WCDL","1.2","2"),("CMS","0.3","0.5"),("Retail+PB+TASC","2.5","3.5")],
    "9.2", "14.1", rating="Sheet B"))

# Pilot 103 — L&T Geostructure (L&T Group)
SPECS.append(mnc_gf(103, "lnt-geostructure", "L&T Geostructure Pvt Ltd",
    "U45203TN2020PTC139693", "Larsen & Toubro Limited (BSE/NSE)",
    "L&T Construction / Geostructure (subsidiary of L&T listed) civil + foundation + marine",
    "Chennai", "06 Apr 2020", "Civil + foundation construction",
    1075, 8.0, "~3,500", 50, 880, "larsentoubro.com",
    f'India infra construction FY25 ~Rs 12 lakh Cr; L&T flagship.',
    ['Bharatmala + Sagarmala capex.','Defence + naval shipbuilding.','Metro + Vande Bharat ecosystem.','Green-H2 + offshore-wind capex.'],
    [("BG (project)","300&ndash;500","3","5","PSU + private"),("CC + WCDL","100&ndash;160","2","3.2","Sheet A"),("Capex TL","80&ndash;130","0.8","1.4","Sustainability"),("FX (USD)","250&ndash;380 notional","1","1.6","Imports"),("Customer-finance","150&ndash;240","1.5","2.4","PSU receivable"),("Cards + CMS","&ndash;","0.5","0.8","3,500 FTE")],
    [("BG","3","5"),("CC+WCDL","2","3.2"),("Capex+FX","1.8","3"),("Customer-finance","1.5","2.4"),("CMS","0.5","0.8"),("Retail+PB+TASC","3","4.5")],
    "11.8", "18.9", rating="Sheet A"))

# Pilot 104 — Grundfos Pumps (Danish pump MNC)
SPECS.append(mnc_gf(104, "grundfos-pumps", "Grundfos Pumps India Pvt Ltd",
    "U29309TN1998PTC040102", "Grundfos A/S (Denmark, private)",
    "Grundfos A/S (Denmark; private; ~€4.5 bn revenue) Danish pump + circulator-pump MNC",
    "Chennai (Oragadam)", "27 Apr 1998", "Pumps + circulator pumps",
    1072, 13.5, "~950", 50, 890, "grundfos.com",
    f'India pump market FY25 ~Rs 35,000 Cr; CAGR 9-11%; Grundfos + KSB + Kirloskar Brothers + Crompton compete.',
    ['Water + sewage + agri irrigation.','Cold-chain + HVAC drives.',f'EU CBAM{ref("18")}.',f'USA-tariff{ref("6")}: India pump export.'],
    [("FX (EUR + DKK)","450&ndash;650 notional","2","3","Royalty"),("Customer-SCF","180&ndash;280","1.8","2.8","Anchors"),("Capex TL","80&ndash;130","0.8","1.4","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("EBR / PCFC","80&ndash;130","0.8","1.4","Export"),("Cards + CMS","&ndash;","0.3","0.5","950 FTE")],
    [("FX","2","3"),("Customer-SCF","1.8","2.8"),("Capex+Trade+EBR","2.2","3.8"),("CMS","0.3","0.5"),("Retail+PB+TASC","2.5","3.5")],
    "8.8", "13.6"))

# Pilot 105 — SIPCOT (Tamil Nadu state PSU industrial-corridor)
SPECS.append(mnc_gf(105, "sipcot", "State Industries Promotion Corporation of Tamilnadu Limited",
    "U74999TN1971SGC005967", "Government of Tamil Nadu",
    "SIPCOT — Tamil Nadu government PSU industrial corridor / industrial-park developer (FY25 ~Rs 1,047 Cr revenue)",
    "Chennai", "12 Aug 1971", "Industrial corridor / PSU",
    1047, 14.0, "~1,200", 50, 900, "sipcot.com",
    f'TN industrial-corridor + park development; SIPCOT operates 25+ industrial parks (Sriperumbudur, Oragadam, Mahindra World City, Hosur, Perundurai).',
    ['TN industrial-park demand from MNC ramp.','PLI + EMS + EV park-allocation.','Defence + electronics-cluster expansion.','Green-corridor + ESG-park demand.'],
    [("BG (project)","250&ndash;380","2.5","4","PSU + tenant"),("CC + WCDL","100&ndash;160","2","3.2","Sheet A"),("Capex TL (corridor)","150&ndash;240","1.5","2.4","Sustainability"),("Customer-finance (tenant)","200&ndash;320","2","3.2","Tenant-payment"),("Treasury + CMS","&ndash;","0.6","1","TN PSU treasury"),("Cards","&ndash;","0.3","0.5","1,200 FTE")],
    [("BG","2.5","4"),("CC+WCDL","2","3.2"),("Capex+Customer-finance","3.5","5.6"),("Treasury+Cards","0.9","1.5"),("Retail+PB+TASC","2.5","3.5")],
    "11.4", "17.8", rating="Sheet A"))

# Pilot 106 — Doosan Bobcat India (Korean machinery)
SPECS.append(mnc_gf(106, "doosan-bobcat", "Doosan Bobcat India Pvt Ltd",
    "U29248TN2007FTC082032", "Doosan Bobcat (Korea; KOSPI: 241560)",
    "Doosan Bobcat (Korea; ~$8 bn revenue) Korean compact-construction-equipment major",
    "Chennai", "07 Apr 2007", "Compact construction equipment",
    1026, 9.0, "~750", 50, 910, "doosanbobcat.com",
    f'India compact-construction market FY25 ~Rs 8,500 Cr; CAGR 11-13%; Bobcat + JCB + Caterpillar (compact) + Volvo CE compete.',
    [f'Coal-FSA + mining{ref("19")}.',f'USA-tariff{ref("6")}: India compact-construction export.','EV-skidsteer + Tier-V emission.','Bharatmala + EPC infra capex.'],
    [("FX (KRW + USD)","450&ndash;650 notional","2","3","Royalty"),("Customer-finance origination","300&ndash;480/yr","2.5","4","EPC + miners"),("Capex TL","80&ndash;130","0.8","1.4","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("EBR / PCFC","60&ndash;100","0.6","1","Export"),("Cards + CMS","&ndash;","0.2","0.4","750 FTE")],
    [("FX","2","3"),("Customer-finance","2.5","4"),("Capex+Trade+EBR","2","3.4"),("CMS","0.2","0.4"),("Retail+PB+TASC","2","3")],
    "8.7", "13.8"))

# Pilot 107 — Andritz Technologies (Austrian pulp/paper/hydro/separation)
SPECS.append(mnc_gf(107, "andritz-tech", "Andritz Technologies Pvt Ltd",
    "U29246TN1998PTC150895", "Andritz AG (Austria; ATX: ANDR)",
    "Andritz AG (Austria; FY25 ~€8.5 bn) global pulp+paper+hydro+separation+metals tech",
    "Chennai", "01 Jan 1998", "Pulp + paper + hydro + separation tech",
    1022, 11.0, "~1,200", 50, 920, "andritz.com",
    f'India process-equipment market FY25 ~Rs 18,000 Cr; CAGR 9-11%; Andritz + Voith + Valmet + Metso compete.',
    ['Pulp+paper+hydro capex.','Steel+metals decarbonisation.',f'EU CBAM{ref("18")}: scope-3.','Green-H2 + biofuel separation.'],
    [("FX (EUR + USD)","550&ndash;800 notional","2.5","4","Royalty"),("Customer-SCF","250&ndash;380","2.5","4","ITC + JK + steel"),("Capex TL","100&ndash;160","1","1.6","Sustainability"),("Trade","100&ndash;160","1","1.6","Imports"),("EBR/PCFC","80&ndash;130","0.8","1.4","Export"),("Cards + CMS","&ndash;","0.4","0.6","1,200 FTE")],
    [("FX","2.5","4"),("Customer-SCF","2.5","4"),("Capex+Trade+EBR","2.8","4.6"),("CMS","0.4","0.6"),("Retail+PB+TASC","2.5","3.5")],
    "10.7", "16.7", rating="Sheet A"))

# Pilot 108 — Visteon Tech & Service Centre (US Visteon GCC)
SPECS.append(mnc_gf(108, "visteon-tech-svc", "Visteon Technical and Services Centre Pvt Ltd",
    "U35990TN2006PTC060495", "Visteon Corp (US, NASDAQ: VC)",
    "Visteon Corp Indian ER&D + GCC arm (separate from manufacturing pilot 94)",
    "Chennai", "20 Apr 2006", "Auto ER&D + GCC",
    1005, 17.0, "~3,500", 50, 930, "visteon.com",
    f'India auto-ER&D GCC ~Rs 95,000 Cr (NASSCOM){ref("140")}; CAGR 14-16%.',
    ['SDV + ADAS-cockpit + EV-platform.',f'USA-tariff{ref("6")}: services-tariff zero.','Visteon-cockpit IP scope expansion.','Cybersecurity + AI-Act compliance work.'],
    [("FX (USD)","700&ndash;1,000 notional","3","5","100% USD"),("Treasury sweep","200&ndash;320","1.5","2.4","MNC TM"),("EBR/PCFC","150&ndash;240","1.5","2.4","Receivables"),("Salary + retail (3,500)","350&ndash;500/yr","3","5","Auto + home"),("PB","145&ndash;220 AUM","1.6","2.5","Senior leaders"),("TASC","120&ndash;180","1","1.5","PF + Gratuity")],
    [("FX","3","5"),("Treasury+EBR","3","4.8"),("Retail-mass","3","5"),("PB","1.6","2.5"),("TASC","1","1.5"),("Cards","0.5","0.8")],
    "12.1", "19.6"))

# Pilot 109 — NGC Transmission Chennai (Chinese gear-transmission)
SPECS.append(mnc_gf(109, "ngc-transmission", "NGC Transmission Chennai Pvt Ltd",
    "U29309TN2019FTC129259", "NGC Group (China; HKEX)",
    "NGC Group (China; Hong Kong listed) industrial gearbox + power-transmission major",
    "Chennai", "06 Mar 2019", "Industrial gearbox + transmission",
    985, 9.5, "~750", 50, 940, "ngcgroup.com",
    f'India industrial-gearbox FY25 ~Rs 28,000 Cr; CAGR 9-11%; NGC + Flender + David Brown + Bonfiglioli.',
    ['Wind + cement + steel capex.',f'EU CBAM{ref("18")}.','EV-drive + railway gearbox.','Mining + sugar industries.'],
    [("FX (CNY + USD)","450&ndash;650 notional","2","3","Royalty"),("Customer-SCF","180&ndash;280","1.8","2.8","Anchors"),("Capex TL","80&ndash;130","0.8","1.3","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("EBR/PCFC","60&ndash;100","0.6","1","Export"),("Cards + CMS","&ndash;","0.3","0.5","750 FTE")],
    [("FX","2","3"),("Customer-SCF","1.8","2.8"),("Capex+Trade+EBR","2","3.3"),("CMS","0.3","0.5"),("Retail+PB+TASC","2","3")],
    "8.1", "12.6"))

# Pilot 110 — Hyundai Wia (Korean Hyundai-Wia)
SPECS.append(mnc_gf(110, "hyundai-wia", "Hyundai Wia India Pvt Ltd",
    "U34300TN2010PTC074749", "Hyundai Wia (Korea; KOSPI: 011210)",
    "Hyundai Wia (KOSPI: 011210; ~$8 bn revenue) Korean engine + module + machine-tool tier-1 in HMG ecosystem",
    "Sriperumbudur (Chennai)", "20 Sep 2010", "Engine + module + machine-tool",
    977, 8.5, "~1,200", 50, 950, "hyundai-wia.com",
    f'Hyundai-Kia ecosystem captive engine + module supplier; HMIL + Kia Anantapur ramp.',
    [f'Hyundai-Kia post-IPO ramp{ref("11")}.',f'USA-tariff{ref("6")}.','EV-engine + module transition.','Machine-tool exports.'],
    [("FX (KRW + USD)","450&ndash;650 notional","2","3","Royalty"),("Customer-SCF","180&ndash;280","1.8","2.8","Hyundai/Kia"),("Capex TL","80&ndash;130","0.8","1.3","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("CC + WCDL","60&ndash;100","1.2","2","Sheet B"),("Cards + CMS","&ndash;","0.3","0.5","1,200 FTE")],
    [("FX","2","3"),("Customer-SCF","1.8","2.8"),("Capex+Trade","1.4","2.3"),("CC+WCDL","1.2","2"),("CMS","0.3","0.5"),("Retail+PB+TASC","2.5","3.5")],
    "9.2", "14.1"))

# Pilot 111 — Athenahealth Technology (US healthcare BPO/SaaS)
SPECS.append(mnc_gf(111, "athenahealth", "Athenahealth Technology Pvt Ltd",
    "U72200TN2005PTC057276", "athenahealth Inc (US, Bain/Hellman PE-owned)",
    "athenahealth Inc (US healthcare-EHR + RCM SaaS; FY25 ~$2.0 bn revenue; PE-owned)",
    "Chennai", "07 Mar 2005", "Healthcare EHR + RCM",
    976, 17.5, "~5,500", 50, 960, "athenahealth.com",
    f'India healthcare-tech + RCM ~$8 bn (NASSCOM){ref("140")}; athena + Omega (pilot 72) + Cognizant Healthcare compete.',
    [f'USA-tariff{ref("6")}: services-tariff zero.','Gen-AI medical-coding ramp.','HIPAA + HHS data-privacy compliance.','PE-exit IPO mandate window.'],
    [("FX (USD)","700&ndash;1,000 notional","3","5","100% USD"),("Treasury sweep","200&ndash;320","1.5","2.4","MNC TM"),("EBR/PCFC","150&ndash;240","1.5","2.4","Receivables"),("Salary + retail (5,500)","450&ndash;700/yr","4","6","Auto + home + cards"),("PB (founders+ESOP)","220&ndash;350 AUM","2.5","4","UHNI"),("TASC + ESOP-Trust","180&ndash;280","1.5","2.4","PF + Gratuity")],
    [("FX","3","5"),("Treasury+EBR","3","4.8"),("Retail+PB+TASC","8","12.4"),("CMS","0.6","1"),("IPO arranger","2","3.5")],
    "16.6", "26.7"))

# Pilot 112 — HTC Global Services (Indian-origin IT)
SPECS.append(mnc_gf(112, "htc-global", "HTC Global Services India Pvt Ltd",
    "U72900TN2001PTC047862", "HTC Global Services Inc (US, Indian-origin)",
    "HTC Global Services US-headquartered Indian-origin IT-services major (~$300 mn group revenue)",
    "Chennai", "30 Mar 2001", "IT services + GCC",
    965, 14.0, "~4,500", 50, 970, "htcinc.com",
    f'India IT-services + GCC ~$50 bn export; HTC + smaller mid-tier IT-services compete.',
    [f'USA-tariff{ref("6")}: services-tariff zero.','Gen-AI + agentic-AI scope.','EU AI-Act + DORA.','Cloud-modernisation + cybersecurity.'],
    [("FX (USD)","550&ndash;800 notional","2.5","4","100% USD"),("Treasury","180&ndash;280","1.5","2.4","MNC TM"),("EBR/PCFC","120&ndash;200","1.2","2","Receivables"),("Salary + retail (4,500)","400&ndash;600/yr","3.5","5.5","Auto+home"),("PB","145&ndash;220 AUM","1.6","2.5","Senior MDs"),("TASC","120&ndash;180","1","1.5","PF+Gratuity")],
    [("FX","2.5","4"),("Treasury+EBR","2.7","4.4"),("Retail-mass","3.5","5.5"),("PB+TASC","2.6","4"),("Cards","0.5","0.8"),("Other","1","1.5")],
    "12.8", "20.2"))

# Pilot 113 — Albonair (German emission-control)
SPECS.append(mnc_gf(113, "albonair", "Albonair India Pvt Ltd",
    "U74110TN2009PTC073654", "Albonair GmbH (Germany; subsidiary of Hinduja Group)",
    "Albonair GmbH German urea-injection + emission-control tier-1 (Hinduja Group) for global CV-OEMs",
    "Chennai", "23 Apr 2009", "Urea-injection + emission-control",
    929, 10.5, "~700", 50, 980, "albonair.com",
    f'India urea-injection market growing with BS6+ + Tier-V; Albonair + Continental + Bosch + Tenneco compete.',
    ['BS6 phase-2 + Tier-V emission ramp.',f'EU CBAM{ref("18")}.',f'USA-tariff{ref("6")}: India urea-injection export.','EV-genset + hybrid CV transition.'],
    [("FX (EUR + USD)","400&ndash;580 notional","1.8","2.8","Royalty"),("Customer-SCF","160&ndash;240","1.6","2.4","CV-OEM anchors"),("Capex TL","80&ndash;130","0.8","1.3","Sustainability"),("Trade","60&ndash;100","0.6","1","Imports"),("EBR/PCFC","60&ndash;100","0.6","1","Export"),("Cards + CMS","&ndash;","0.3","0.5","700 FTE")],
    [("FX","1.8","2.8"),("Customer-SCF","1.6","2.4"),("Capex+Trade+EBR","2","3.3"),("CMS","0.3","0.5"),("Retail+PB+TASC","2","3")],
    "7.7", "12", rating="Sheet A"))

# Pilot 114 — Daechang India Seat (Korean auto-seat sister)
SPECS.append(mnc_gf(114, "daechang-seat", "Daechang India Seat Company Pvt Ltd",
    "U74999TN2006PTC058883", "Daechang Industries (Korea)",
    "Daechang Korean auto-seat tier-1 to Hyundai-Kia",
    "Sriperumbudur (Chennai)", "06 Mar 2006", "Auto seat",
    893, 8.5, "~1,100", 50, 990, "daechang.kr",
    'Hyundai-Kia auto-seat ecosystem; sister Daebu (pilot 97).',
    [f'Hyundai-Kia post-IPO ramp{ref("11")}.','Korean MNC ecosystem cross-sell.','EV-seat + premiumisation.',f'USA-tariff{ref("6")}.'],
    [("FX (KRW + USD)","400&ndash;580 notional","1.8","2.8","Royalty"),("Customer-SCF","160&ndash;240","1.6","2.4","Hyundai/Kia"),("Capex TL","80&ndash;130","0.8","1.3","Sustainability"),("Trade","50&ndash;80","0.5","0.8","Imports"),("CC + WCDL","50&ndash;80","1","1.6","Sheet"),("Cards + CMS","&ndash;","0.3","0.4","1,100 FTE")],
    [("FX","1.8","2.8"),("Customer-SCF","1.6","2.4"),("Capex+Trade","1.3","2.1"),("CC+WCDL","1","1.6"),("CMS","0.3","0.4"),("Retail+PB+TASC","2","3")],
    "8", "12.3"))

# Pilot 115 — Bhartiya International (listed leather + textiles)
SPECS.append(mnc_gf(115, "bhartiya-international", "Bhartiya International Limited",
    "L74899TN1987PLC111744", "Bhartiya Group (Indian-origin promoter)",
    "Bhartiya International BSE/NSE-listed leather + textiles + brand house (own brands + JV with EU brands)",
    "Chennai", "01 Jan 1987", "Leather + textiles + brands",
    856, 7.5, "~3,200", 50, 1000, "bhartiyagroup.com",
    f'India leather + textile export FY25 ~Rs 36,000 Cr.',
    [f'EU CBAM{ref("18")}: scope-3 + EUDR.',f'USA-tariff{ref("6")}: India leather export.','Brand vertical-integration.','Listed-corp DCM access.'],
    [("CC + WCDL","100&ndash;160","2","3.2","Sheet B"),("EBR/PCFC","250&ndash;380","2.5","4","60%+ export"),("Trade","100&ndash;160","1","1.6","Imports"),("FX (USD + EUR)","450&ndash;650 notional","2","3","Royalty"),("Capex TL","60&ndash;100","0.6","1","Brand expansion"),("DCM/NCD","100&ndash;160","0.8","1.4","Listed-corp")],
    [("CC+WCDL","2","3.2"),("EBR/PCFC","2.5","4"),("Trade+FX","3","4.6"),("Capex+DCM","1.4","2.4"),("Retail+PB+TASC","2","3")],
    "10.9", "17.2", rating="Sheet B"))


if __name__ == "__main__":
    build_all()
