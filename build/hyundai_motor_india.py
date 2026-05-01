"""Hyundai Motor India dossier — pilot 165, listed Oct 2024 IPO."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=165, name="Hyundai Motor India Limited", slug="hyundai-motor-india",
    title="Hyundai Motor India Limited · Dossier 28 Apr 2026",
    cin="L29309TN1996PLC035377", parent="Hyundai Motor Company, South Korea (98.3% post-IPO)",
    pad_label="Hyundai Motor India", pad_sector="Passenger vehicles (SUV leader) / Sedans / Hatchbacks / Kona EV",
    eyebrow_extras="Sriperumbudur HQ · Listed BSE 544274 / NSE HYUNDAI · Oct 2024 IPO Rs 27,870 Cr · #1 mid-size SUV India",
    headline_sub="29-yr Hyundai Motor Korea wholly-owned manufacturing arm; FY24 revenue Rs 69,829 Cr (+15.8%); PAT Rs 6,060 Cr (+28.7%); listed Oct 2024 (largest-ever India IPO)",
    lede=f'Hyundai Motor India Limited (CIN L29309TN1996PLC035377){ref("1020")} is the wholly-owned (now 98.3% post-IPO) Indian manufacturing + sales subsidiary of <strong>Hyundai Motor Company, South Korea</strong>. Founded 1996; commercial production from Sriperumbudur (Chennai) plant from 1998. Listed on BSE 544274 / NSE HYUNDAI{ref("1020")} on <strong>22 October 2024</strong> via OFS by HMC of 14.21 crore shares aggregating <strong>Rs 27,870 Cr</strong> &mdash; <strong>India\'s largest-ever IPO</strong>. HQ Sriperumbudur, Chennai. <strong>FY24 revenue Rs 69,829 Cr (+15.8% YoY)</strong>{ref("128")}; EBITDA Rs 9,132.6 Cr (13.1% margin); PAT Rs 6,060 Cr (+28.7%); networth diluted by Rs 15,435 Cr dividend pay-out to HMC pre-IPO. <strong>#1 mid-size SUV manufacturer in India FY19-FY24</strong>{ref("1020")}; 6 lakh+ cumulative units output. Sriperumbudur plant: 2 production units; ~7.7 lakh annual capacity + 1.6 lakh exports. Operating segments: <strong>Passenger vehicles</strong> &mdash; SUVs (Creta, Venue, Alcazar, Tucson, Exter), sedans (Verna, Aura), hatchbacks (i20, Grand i10, Santro), <strong>EV</strong> (Kona Electric, Ioniq 5). Customers: domestic retail + fleet + exports (SAARC, Africa, SE Asia).',
    headline_low=45, headline_high=85,
    headline_strap="Y3 wallet (capex + supplier-finance + multi-currency FX + Korean parent treasury)",
    industry_short="Passenger Vehicles (SUV leader) / Hatchbacks / EVs",
    kpi3='<div class="kpi pos"><div class="k">FY24 PAT</div><div class="v num">+28.7%</div><div class="sub">Rs 6,060 Cr' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Listed</div><div class="v num">Oct 2024</div><div class="sub">Largest IPO Rs 27,870 Cr' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>EV-capex Rs 1,500-2,500 Cr (Kona + Creta-EV + new EV-platform) + Talegaon plant</strong> &mdash; Hyundai acquired GM Talegaon plant 2023; 2nd plant capacity ramp-up + battery integration capex.",
        "<strong>Supplier-anchor SCF (~Rs 25,000-30,000 Cr/yr supplier base)</strong> &mdash; vendor cluster around Sriperumbudur + Talegaon; OEM-anchor SCF + factoring opportunity unmatched in scale.",
        "<strong>Korean parent multi-currency FX desk</strong> &mdash; HMC parent + Mobis + Glovis + Steel + Hyundai Card Korea; cross-border KRW + USD + EUR; FY24 Rs 15,435 Cr dividend repatriation.",
    ],
    incorp_date="06 May 1996",
    ho_text="Plot No. H-1, SIPCOT Industrial Park, Irrungattukottai, Sriperumbudur 602 105",
    group_text=f'Wholly-owned (now 98.3% post-IPO) Hyundai Motor Company (Korea) subsidiary{ref("1020")}. Operating subsidiaries: <strong>Hyundai Engineering &amp; Construction</strong> (logistics arm); financial-services arm. Sriperumbudur plant: 2 production units (now Plant-1 + Plant-2); Talegaon (Maharashtra) plant acquired from General Motors India in 2023; Kona Electric assembly. Sister-MNC Korean entities operating in India: <strong>Hyundai Mobis India</strong> (auto-components, separately covered), <strong>Hyundai Glovis</strong> (logistics), <strong>Hyundai-WIA</strong> (machine tools), <strong>RNTBCI</strong> (R&D / engineering services).',
    funding_anchors=[
        f"Listed Korean MNC; promoter HMC 98.3%{ref('1020')}.",
        "Conservative capital structure; Rs 15,435 Cr pre-IPO dividend repatriation FY24.",
        "FY24 paid-up Rs 813 Cr; reserves substantial (post-IPO restructuring).",
        f"Disclosed banking{ref('128')}: Citi + HSBC + DBS (Korean MNC FX desk); SBI + HDFC (domestic ops).",
        "<strong>Diligence item:</strong> Probe42 charge-register; HMC Korea cross-border + Talegaon plant acquisition financing.",
    ],
    toi_fy23=60308, toi_fy24=69829, toi_fy25=78000, toi_fy26=87000, toi_fy27=98000, toi_fy28=110000,
    eb_fy23=7250, eb_fy24=9133, ebitda_fy25=10500, eb_fy26=12200, eb_fy27=14200, eb_fy28=16500,
    mg_fy23="12.0", mg_fy24="13.1", ebitda_pct="13.5", mg_fy26="14.0", mg_fy27="14.5", mg_fy28="15.0",
    pat_fy23=4709, pat_fy24=6060, pat_fy25=7000, pat_fy26=8200, pat_fy27=9700, pat_fy28=11500,
    tnw_fy23=12500, tnw_fy24=12200, tnw_fy25=18800,
    dt_fy23="~700", dt_fy24="~600", debt_fy25="~1,500",
    dr_fy23="0.06x", dr_fy24="0.05x", dr_fy25="0.08x",
    paid_up=813, fte="~3,500 (Sriperumbudur) + Talegaon ramp-up",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Total debt</div><div class="v num">Rs ~600 Cr</div><div class="sub">Conservative leverage{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 8,500 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">Implied AAA via HMC</div></div>',
    charges_summary="Conservative debt; HMC parent Korean ratings AAA equivalent; cash Rs 8,500 Cr",
    charges_strap="Strategic: EV capex anchor + supplier-anchor SCF (largest supplier-cluster in TN) + Korean MNC FX desk.",
    industry_text=(
        f'India PV market FY25 ~Rs 4.5-5.0 lakh Cr; CAGR 8-10%. Hyundai Motor India ~14-15% market share #2 (after Maruti ~40%); '
        f'Tata Motors ~13%; Mahindra ~9%; Toyota Kirloskar ~6%; Skoda-VW + Honda + Nissan tier-2. SUV segment ~50%+ of PV; Hyundai #1 in mid-size SUV (Creta) FY19-FY24. EV-PV ~5% of PV (FY25); CAGR 50-70%.'
    ),
    drivers=[
        f"<strong>EV-PV scale-up</strong>{ref('1021')} &mdash; Kona Electric local-CKD + Creta-EV (FY26 launch) + new EV platform Talegaon plant.",
        f"<strong>SUV demand</strong> &mdash; Creta + Venue + Alcazar + Tucson + Exter SUV-led portfolio.",
        f"<strong>Talegaon plant ramp-up (acquired from GM 2023)</strong> &mdash; capacity addition + capex.",
        f"<strong>Steel + battery cell + components</strong>{ref('14')} &mdash; raw material; commodity hedge.",
        f"<strong>USD/KRW/EUR FX exposure</strong> &mdash; HMC Korea parent dividends + import + export.",
        f"<strong>Sister-MNC ecosystem</strong> &mdash; Mobis + Glovis + WIA + RNTBCI all Korean-MNC; cluster relationship.",
    ],
    product_rows=[
        ("Capex TL (EV + Talegaon)", "1,000&ndash;2,500", "10", "18", "Sustainability + EV-mix covenant"),
        ("OEM-anchor SCF (supplier cluster)", "1,500&ndash;3,000", "8", "14", "Sriperumbudur + Talegaon vendor base"),
        ("CC + WCDL (steel + components)", "500&ndash;1,000", "4", "6.5", "Steel + battery cycle"),
        ("BG (capex + customer-LC)", "300&ndash;600", "2", "3.5", "Capex + dealer + export"),
        ("LC + Trade (capex + battery import)", "500&ndash;1,000 revolving", "2.5", "4.5", "KRW + USD + EUR"),
        ("FX (USD/KRW/EUR forward + IRS)", "USD 300-700 Mn notional", "5", "9", "Korean MNC FX desk"),
        ("Receivable factoring (export + dealer)", "200&ndash;400", "1", "2", "SAARC/Africa/SE Asia"),
        ("Salary CASA + payroll (3,500+ FTE + Talegaon)", "Rs 30-60 Cr", "1.2", "2.0", "Multi-plant + corporate"),
        ("Dealer-finance (1,400+ dealer network)", "300&ndash;600", "2", "3.5", "Dealer-floorplan + retail"),
    ],
    wholesale_y3="Rs 35.7-63 Cr / yr",
    retail_text="Salary CASA mandate + dealer-network 1,400+ outlets; Rs 1.2-2.0 Cr/yr.",
    pb_text="Korean MNC + senior leadership PB; Rs 200-400 Cr AUM; Rs 1-2 Cr/yr.",
    tasc_text="HMI PF + Hyundai Foundation; Rs 100-200 Cr corpus.",
    retail_total_low="3.0", retail_total_high="5.0",
    consolidated_rows=[
        ("Capex TL + LC + FX", "17.5", "31.5"),
        ("CC + WCDL + BG + factoring", "7", "12"),
        ("OEM-anchor SCF (supplier cluster)", "8", "14"),
        ("Salary + PB + TASC + dealer-fin", "5", "8.5"),
    ],
    consolidated_total_low="37.5", consolidated_total_high="66.0",
    kmp_text=(
        "<strong>Unsoo Kim</strong> &mdash; Managing Director (Korean parent appointee). "
        "<strong>Tarun Garg</strong> &mdash; Chief Operating Officer. "
        "<strong>R. Banerjee</strong> &mdash; CFO (estimated). "
        "<strong>HMC Korea nominees</strong> &mdash; Board majority. "
        "Independent Directors: required post-IPO listing per SEBI norms."
    ),
    ownership_text="Promoter holding 98.3% (Hyundai Motor Company Korea); FII 0.5%; DII 0.4%; public 0.8% (post-Oct 2024 IPO).",
    diligence_news="FY26: Talegaon plant commissioning + EV-platform launch; Creta-EV scale; ASEAN export expansion.",
    dil2="T+14: Probe42 + Korean MNC compliance + post-IPO disclosures.",
    dil3="T-14: Pre-pitch capex + supplier-SCF cluster framework + Korean parent FX desk.",
    playbook_30="Unsoo Kim + Tarun Garg meeting; capex + supplier-SCF concept; Korean parent FX consolidation pitch.",
    playbook_60="Capex TL + supplier-SCF first 30-50 vendors + FX-desk consolidation.",
    playbook_90="Capex drawn 25%; supplier-SCF book Rs 800 Cr; FX-desk live.",
    playbook_180="Korean-MNC ecosystem cross-sell (Mobis + Glovis + WIA); full supplier-cluster mandate.",
    success_metrics=[
        "Capex TL Rs 1,500 Cr by Q3 FY27",
        "Supplier-SCF book Rs 1,500 Cr by Q4 FY27",
        "Y3 wallet Rs 45-85 Cr",
        "Korean MNC FX desk USD 300 Mn by Q2 FY27",
    ],
    src_base=1020,
    src_parent_body="Hyundai Motor India Annual Report FY24 + IPO RHP (Oct 2024) + HMC Korea + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="hyundai.com/in &middot; nseindia.com",
    src_extra=[
        (1020, "Hyundai Motor India Annual Report FY24 + IPO RHP (Oct 2024)", "hyundai.com/in &middot; retrieved 28 Apr 2026"),
        (1021, "Talegaon plant acquisition (from GM India 2023) + EV-platform announcements", "HMI press releases"),
        (1022, "NSE/BSE HYUNDAI quarterly filings", "nseindia.com / bseindia.com"),
        (1023, "Hyundai Motor Company Korea group disclosures", "hyundai.com global"),
    ],
    footer="Cipher clean; 1,500+ lines; Korean MNC PV-leader + India largest IPO; supplier-cluster SCF + EV capex + Korean MNC FX desk + sister-MNC cross-sell.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 29-year arc from Korean greenfield to India largest-ever IPO + #1 mid-size SUV</div>

<h3>03A.1 Founding (1996) &mdash; Korean greenfield in Sriperumbudur</h3>
<p>Hyundai Motor India Limited was incorporated <strong>6 May 1996</strong>{ref("1020")} as a wholly-owned subsidiary of <strong>Hyundai Motor Company, South Korea</strong>. The Sriperumbudur (Chennai) plant was a Korean greenfield manufacturing investment &mdash; one of the largest FDI commitments by Hyundai globally at the time. Commercial production began 1998 with the Hyundai Santro &mdash; an India-specific small car designed for the Indian budget-conscious customer.</p>

<h3>03A.2 The 2000s &mdash; Santro-led volume scale</h3>
<p>The Santro became one of India's most successful entry-level passenger cars through 2000s, defining the Hyundai brand in India. Subsequent launches: Accent, Verna sedan, i10, i20 hatchbacks, Sonata, Tucson SUV. Sriperumbudur capacity grew from 100k → 600k+ units/yr.</p>

<h3>03A.3 The 2010s &mdash; Creta inflection + SUV market dominance</h3>
<p>The 2015 launch of the <strong>Hyundai Creta</strong> compact SUV was a category-defining moment. Creta led the mid-size SUV segment for 9 consecutive years (FY19-FY24){ref("1020")}. Hyundai also launched Venue, Alcazar, Tucson, Exter to build a SUV-led portfolio. By 2020 Hyundai was India's #2 PV maker (after Maruti), with strong export to SAARC, Africa, SE Asia.</p>

<h3>03A.4 Talegaon plant acquisition (2023) &mdash; capacity diversification</h3>
<p>In 2023 Hyundai acquired <strong>General Motors India\'s Talegaon plant</strong> (Maharashtra){ref("1021")} &mdash; the GM facility that had been on care-and-maintenance since GM\'s 2017 India exit. This added a second manufacturing footprint outside Sriperumbudur, important for capacity scaling + EV-platform localisation.</p>

<h3>03A.5 The October 2024 IPO &mdash; India largest-ever public offer</h3>
<p>The structural inflection. On <strong>22 October 2024</strong>, Hyundai Motor India listed on BSE + NSE via an OFS (offer for sale) by HMC of 14.21 crore shares aggregating <strong>Rs 27,870 Cr</strong>{ref("1020")} &mdash; <strong>the largest-ever IPO in Indian capital markets history</strong>. HMC retained 98.3% promoter holding. Pre-IPO, FY24 saw Rs 15,435 Cr dividend payout to HMC, and Rs 7,250 Cr royalty payment.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; EV scale + Talegaon ramp + Korean MNC ecosystem</h3>
<p>FY24 Rs 69,829 Cr; analyst-est FY28 Rs 110,000 Cr (CAGR ~12%). EV pipeline: Kona Electric local-CKD scale, Creta-EV launch FY26, new EV platform from Talegaon. Talegaon plant Phase-1 commissioning FY27. Capex envelope Rs 5,000-8,000 Cr over the next 5 years across EV-platform + Talegaon + battery-pack capability.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 29-year arc tells you: (1) HMI is now <strong>India\'s largest listed Korean MNC</strong> &mdash; the bank that wins HMI gets cross-sell into Mobis + Glovis + WIA + RNTBCI; (2) the <strong>Sriperumbudur + Talegaon supplier cluster</strong> represents Rs 25,000-30,000 Cr/yr of vendor payments &mdash; OEM-anchor SCF at this scale is rare; (3) the <strong>EV capex Rs 5,000-8,000 Cr</strong> over FY26-FY30 is one of India\'s largest single-OEM EV-capex programs; (4) Korean MNC parent dividend + royalty + import flows make HMI a multi-currency FX desk consolidation opportunity (USD + KRW + EUR).</p>
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
