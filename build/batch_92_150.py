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


if __name__ == "__main__":
    build_all()
