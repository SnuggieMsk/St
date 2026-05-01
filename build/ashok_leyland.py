"""Ashok Leyland Limited dossier — pilot 157, Hinduja flagship CV."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=157, name="Ashok Leyland Limited", slug="ashok-leyland",
    title="Ashok Leyland Limited · Dossier 28 Apr 2026",
    cin="L34101TN1948PLC000105", parent="Hinduja Group / Hinduja Automotive Limited",
    pad_label="Ashok Leyland", pad_sector="Commercial Vehicles / Buses / Defence / Switch Mobility EV",
    eyebrow_extras="Chennai HO · Listed BSE 500477 / NSE ASHOKLEY · Hinduja flagship · Switch Mobility EV",
    headline_sub="76-yr Hinduja Group flagship CV manufacturer; FY24 revenue Rs 38,370 Cr; PAT Rs 2,696 Cr; net debt only Rs 89 Cr",
    lede=f'Ashok Leyland Limited (CIN L34101TN1948PLC000105){ref("980")} is the listed Hinduja Group flagship Indian commercial-vehicle manufacturer (medium + heavy + light CV + bus + defence). Listed BSE 500477 / NSE ASHOKLEY{ref("980")}; promoter holding 51.5% (Mar 2026); HQ Chennai. <strong>FY24 revenue Rs 38,370 Cr</strong>{ref("128")}; EBITDA Rs 4,603 Cr (12.0%); PAT Rs 2,696 Cr (7.0% margin); net debt only Rs 89 Cr (debt-free at standalone level after FY24 deleveraging){ref("980")}. <strong>CARE AA-/Negative + CARE A1+</strong>{ref("128")} for short-term debt. Operating subsidiaries: <strong>Switch Mobility Limited</strong> (EV subsidiary &mdash; e-bus + e-LCV); <strong>Hinduja Leyland Finance Limited</strong> (NBFC, captive vehicle-finance arm); <strong>Global TVS Bus Body Builders Limited</strong> (JV with TVS). 9,607 FTE. The 76-year arc &mdash; founded 1948 with British collaboration; Hinduja Group acquired control in 1987 &mdash; makes Ashok Leyland one of India\'s most senior CV manufacturers, second only to Tata Motors in the Indian CV market.',
    headline_low=30, headline_high=55,
    headline_strap="Y3 wallet (CV-finance + Switch Mobility EV capex + group + family-PB)",
    industry_short="Commercial Vehicles / Buses / Defence / Switch Mobility EV",
    kpi3='<div class="kpi pos"><div class="k">Net debt</div><div class="v num">Rs 89 Cr</div><div class="sub">Near-zero (post deleveraging)' + ref("126") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE AA-</div><div class="sub">Neg + A1+ ST' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Switch Mobility EV capex Rs 800-1,500 Cr + Rs 5,000 Cr CALB battery JV</strong> &mdash; Lucknow EV plant + battery-ecosystem partnership with CALB Group (China); 7-10 year Rs 5,000 Cr commitment; FY26 capex Rs 1,000 Cr.",
        "<strong>Hinduja Leyland Finance NBFC funding</strong> &mdash; captive vehicle-finance arm; bilateral TL + co-lending mandate; cross-sell into CV-fleet customer base.",
        "<strong>Hinduja family-PB + group cross-sell</strong> &mdash; Dheeraj Hinduja Chairman + Hinduja UK + Hinduja Bank Switzerland + IndusInd Bank cross-promoter + group treasury.",
    ],
    incorp_date="07 Sep 1948",
    ho_text="No.1, Sardar Patel Road, Guindy, Chennai 600 032",
    group_text=f'Hinduja Group flagship; Hinduja Automotive Limited primary promoter (51.5%){ref("980")}. Operating subsidiaries: <strong>Switch Mobility Ltd</strong> (EV CV); <strong>Hinduja Leyland Finance Ltd</strong> (HLF NBFC, captive vehicle-finance); <strong>Global TVS Bus Body Builders Ltd</strong> (JV with TVS). Plants: Ennore, Hosur, Bhandara, Vijayawada, Alwar, Pantnagar (India), Ras Al Khaimah (UAE), Leeds (UK). New Lucknow EV facility (2025; 70+ acres, 2,500 → 5,000 units/yr).',
    funding_anchors=[
        f"Listed Hinduja flagship; promoter 51.5%{ref('980')}.",
        "Net debt Rs 89 Cr after FY24 deleveraging; standalone debt-free.",
        "FY24 paid-up Rs 293 Cr; reserves Rs 12,000+ Cr.",
        f"Disclosed banking{ref('128')}: SBI + Axis + HDFC + Kotak + IndusInd (sister-Hinduja); South Indian Bank inventory-financing partnership Apr 2024.",
        "<strong>Diligence item:</strong> Probe42 charge-register on Ashok Leyland + Switch Mobility + HLF subsidiaries.",
    ],
    toi_fy23=36100, toi_fy24=38370, toi_fy25=42500, toi_fy26=48000, toi_fy27=54500, toi_fy28=62000,
    eb_fy23=3940, eb_fy24=4603, ebitda_fy25=5300, eb_fy26=6240, eb_fy27=7350, eb_fy28=8680,
    mg_fy23="10.9", mg_fy24="12.0", ebitda_pct="12.5", mg_fy26="13.0", mg_fy27="13.5", mg_fy28="14.0",
    pat_fy23=1380, pat_fy24=2696, pat_fy25=3050, pat_fy26=3650, pat_fy27=4350, pat_fy28=5150,
    tnw_fy23=10500, tnw_fy24=12300, tnw_fy25=14500,
    dt_fy23="~1,200", dt_fy24="~89 (net)", debt_fy25="~500",
    dr_fy23="0.10x", dr_fy24="0.01x", dr_fy25="0.03x",
    paid_up=294, fte="~9,607",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Net debt</div><div class="v num">Rs 89 Cr</div><div class="sub">FY24{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 2,800 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CARE AA-</div><div class="sub">Negative outlook</div></div>',
    charges_summary="Near-zero net debt (Rs 89 Cr FY24); EV capex via subsidiary",
    charges_strap="Strategic: Switch Mobility EV anchor + HLF NBFC funding partner + Hinduja group treasury + family-PB.",
    industry_text=(
        f'India CV market FY25 ~Rs 3.2-3.5 lakh Cr; CAGR 8-10%. Tata Motors ~46% market share; Ashok Leyland ~33%; '
        f'VECV (Volvo-Eicher) + Daimler (BharatBenz) + Force Motors + Bharat Forge tier-2. EV-CV nascent ~Rs 5-8k Cr; '
        f'CAGR 60-80%. India CV market is growing on infrastructure + e-commerce + last-mile-mobility tailwinds.'
    ),
    drivers=[
        f"<strong>Switch Mobility EV scale</strong>{ref('981')} &mdash; Lucknow plant 2,500 → 5,000 units/yr; Rs 1,000 Cr FY26 capex; e-bus + e-LCV.",
        f"<strong>CALB battery JV (Rs 5,000 Cr / 7-10 yr)</strong> &mdash; Tamil Nadu battery-pack manufacturing groundbreaking Mar 2026; vertical integration.",
        f"<strong>Defence orders (Stallion + Project Cheetah)</strong> &mdash; MoD multi-year tenders.",
        f"<strong>State Transport Corp (STC) bus orders</strong> &mdash; MSRTC 2,104-bus order Jul 2024; pan-India STC tenders.",
        f"<strong>Steel + commodity hedge</strong>{ref('14')} &mdash; HRC + special-steel raw material.",
    ],
    product_rows=[
        ("Capex TL (Switch Mobility EV)", "500&ndash;1,000", "5", "9", "Sustainability + CALB battery JV"),
        ("CC + WCDL (CV cycle + steel)", "300&ndash;500", "2", "3.5", "CV cycle + JIT OEM"),
        ("BG (defence + STC tender + dealer)", "300&ndash;500", "2", "3.5", "Defence retention + STC advance"),
        ("LC + Trade (capex + steel imports)", "200&ndash;400 revolving", "1", "2", "Korean + Chinese EV components"),
        ("FX (USD + EUR + CNY)", "USD 100-250 Mn", "2", "4", "CALB battery + capex import"),
        ("OEM-fleet finance (HLF partnership)", "200&ndash;400", "1.5", "2.5", "CV-fleet captive finance"),
        ("Customer-finance / bus-fleet leasing", "100&ndash;200", "1", "1.8", "STC + private operator leasing"),
        ("Salary CASA + payroll (9,607 FTE)", "Rs 25-50 Cr", "0.8", "1.5", "Multi-plant"),
        ("PB (Hinduja family + Switch leadership)", "Rs 400-800 Cr AUM", "2", "3.5", "Multi-gen + IndusInd cross-promoter"),
    ],
    wholesale_y3="Rs 13.5-26.0 Cr / yr",
    retail_text="Salary CASA mandate ~9,607 FTE; HLF partnership cross-sell; Rs 0.8-1.5 Cr/yr.",
    pb_text="Hinduja family + Switch leadership ESOP; PB AUM Rs 400-800 Cr; Rs 2-3.5 Cr/yr.",
    tasc_text="Ashok Leyland PF + Hinduja Foundation; Rs 200-300 Cr corpus; Rs 0.8-1.2 Cr/yr.",
    retail_total_low="3.6", retail_total_high="6.2",
    consolidated_rows=[
        ("Capex TL (EV) + LC + FX", "8", "15"),
        ("CC + WCDL + BG", "4", "7"),
        ("OEM-fleet + customer finance", "2.5", "4.3"),
        ("Salary + PB + TASC", "3.6", "6.2"),
    ],
    consolidated_total_low="18.1", consolidated_total_high="32.5",
    kmp_text=(
        "<strong>Dheeraj G Hinduja</strong> &mdash; Chairman, Ashok Leyland (Hinduja third-generation). "
        "<strong>Shenu Agarwal</strong> &mdash; CEO &amp; Managing Director. "
        "<strong>Gopal Mahadevan</strong> &mdash; Director &amp; CFO. "
        "<strong>Andrew Palmer</strong> &mdash; CEO Switch Mobility (UK). "
        "Independent Directors: Sanjay Asher, others."
    ),
    ownership_text="Promoter holding 51.5% (Hinduja Automotive Ltd + Hinduja family); FII 18%; DII 17%; public 13.5%.",
    diligence_news="FY26: Switch Mobility Lucknow commissioning; CALB battery groundbreaking Mar 2026; defence orderbook execution; STC bus tenders.",
    dil2="T+14: Probe42 charge-register on AL + Switch + HLF; CARE rationale (note Negative outlook).",
    dil3="T-14: Pre-pitch Switch Mobility + CALB capex term-sheet + HLF NBFC TL + Hinduja family-PB.",
    playbook_30="Shenu Agarwal + Gopal Mahadevan meeting; Switch capex + CALB concept; HLF partnership.",
    playbook_60="Switch capex TL committee; HLF bilateral TL signed; FX + steel hedge.",
    playbook_90="Capex drawn 25%; HLF co-lending live; defence-receivable factoring.",
    playbook_180="CALB battery TL launch; HLF securitisation flow; Hinduja family-PB AUM.",
    success_metrics=[
        "Switch Mobility capex TL Rs 500 Cr by Q3 FY27",
        "HLF NBFC bilateral TL Rs 750 Cr by Q2 FY27",
        "Y3 wallet Rs 30-55 Cr",
        "Hinduja family-PB Rs 400+ Cr by Q4 FY28",
    ],
    src_base=980,
    src_parent_body="Ashok Leyland Annual Report FY24 + investor relations + Hinduja Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="ashokleyland.com &middot; hinduja.com &middot; nseindia.com",
    src_extra=[
        (980, "Ashok Leyland Annual Report FY24 + investor relations", "ashokleyland.com &middot; retrieved 28 Apr 2026"),
        (981, "Switch Mobility EV + CALB Group battery JV announcements 2024-2025", "AL press releases"),
        (982, "NSE/BSE ASHOKLEY quarterly filings", "nseindia.com / bseindia.com"),
        (983, "CARE AA-/Negative + A1+ rationale [verify FY26]", "careratings.com"),
    ],
    footer="Cipher clean; 1,500+ lines; Hinduja flagship CV manufacturer with Switch Mobility EV capex + CALB battery JV + HLF NBFC partnership + Hinduja family-PB.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 76-year arc from British-collaboration JV to Hinduja flagship CV manufacturer + Switch Mobility EV pivot</div>

<h3>03A.1 Founding (1948) &mdash; Ashok Leyland Ltd, the original</h3>
<p>Ashok Leyland was incorporated <strong>7 September 1948</strong> in Madras (Chennai) as a JV with Leyland Motors (UK) for assembly of British Leyland trucks + buses for the post-Independence Indian transport economy<sup class="ref">[<a href="#src-980">980</a>]</sup>. The original promoter was Raghunandan Saran, with manufacturing licensed from Leyland Motors UK. The Ennore plant was commissioned and built India's first integrated CV manufacturing capability outside Tata Engineering.</p>

<h3>03A.2 The 1950s-1970s &mdash; CV market leadership beside Tata</h3>
<p>Through the 1950s-70s Ashok Leyland built the second-largest CV market position in India (after Tata Engineering / Telco). Comet truck + Leyland-Comet bus + Hippo + Beaver heavy-duty became iconic Indian transport assets. Plants expanded across Hosur (TN) + Bhandara (Maharashtra) + Alwar (Rajasthan).</p>

<h3>03A.3 Hinduja Group acquisition (1987) &mdash; the inflection</h3>
<p>The <strong>Hinduja Group acquired Ashok Leyland in 1987</strong>{ref("980")} from the Iyengar family + IDBI/UTI/LIC consortium. Hinduja brought capital + global market access + UK manufacturing know-how (Leyland UK was acquired in parallel). Through 1990s-2000s the Hinduja-led entity invested in modernisation, defence-CV diversification, bus business growth (e.g. Citystar, Stile, Falcon), and BS-IV / BS-VI emission upgrades.</p>

<h3>03A.4 The 2000s-2010s &mdash; defence + bus + LCV scale</h3>
<p>Defence orders became significant: Stallion 4x4, Stallion 6x6, Project Cheetah, FAT (Field Artillery Tractor) for the Indian Army. Bus business grew through STC tenders (state-transport corporations) and private fleet (BMTC, MSRTC etc). LCV business (Dost) entered the small-truck segment. Pantnagar plant added capacity; Vijayawada plant set up.</p>

<h3>03A.5 The 2020-2024 transformation &mdash; Switch Mobility EV + CALB battery JV + deleveraging</h3>
<p>The structural inflection. <strong>Switch Mobility</strong> was launched in 2021 (UK + India platform) for e-bus + e-LCV. By FY24 Ashok Leyland had largely deleveraged at the standalone level &mdash; net debt Rs 89 Cr from Rs 1,200+ Cr in FY23. The 2024 announcement of a <strong>Rs 5,000 Cr / 7-10 year battery ecosystem partnership with CALB Group (China)</strong>{ref("981")} signalled aggressive vertical integration. The Lucknow EV plant (70+ acres, 2,500 → 5,000 units/yr) was announced for 2025 commissioning. Maharashtra State Road Transport Corporation placed a 2,104-bus order in July 2024 &mdash; one of the largest single STC tenders in Indian history.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; capex execution + EV scale + family-stewardship</h3>
<p>FY24 revenue Rs 38,370 Cr; analyst-est FY28 Rs 62,000 Cr (CAGR ~13%). FY26 capex target Rs 1,000 Cr. Switch Mobility scale-up to 5,000 units/yr by FY27. CALB battery plant groundbreaking March 2026. The structural play is the <strong>combined Switch Mobility EV + CALB battery + HLF (Hinduja Leyland Finance) NBFC</strong> ecosystem &mdash; making Ashok Leyland a vertically-integrated EV-CV play, not just an ICE-CV manufacturer.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 76-year arc tells you: (1) Ashok Leyland under Hinduja is a <strong>builder + global operator</strong> &mdash; the UK + India + UAE + Switch Mobility footprint is rare; (2) the FY24 deleveraging means the standalone is <strong>net cash + AAA-equivalent capacity</strong> &mdash; fresh capex sleeve at top-tier pricing; (3) the <strong>CALB battery partnership Rs 5,000 Cr</strong> is the single largest battery-ecosystem capex announcement in Indian CV; (4) <strong>HLF NBFC + IndusInd Bank cross-promoter</strong> structure makes the Hinduja-group financing ecosystem one of the most complex + valuable in Indian banking.</p>
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
