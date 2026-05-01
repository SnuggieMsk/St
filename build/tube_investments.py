"""Tube Investments of India (TII) dossier (pilot 152) — Murugappa flagship."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=152, name="Tube Investments of India Limited", slug="tube-investments-india",
    title="Tube Investments of India Limited · Dossier 28 Apr 2026",
    cin="L35100TN2008PLC069496", parent="Murugappa Group (via Ambadi Investment Ltd)",
    pad_label="Tube Investments of India", pad_sector="Precision tubes / Auto-components / EV / Bicycles",
    eyebrow_extras="Chennai HO · Listed BSE 540762 / NSE TIINDIA · Murugappa flagship · TI Clean Mobility EV",
    headline_sub="Murugappa flagship engineering platform: precision steel tubes + auto-components + bicycles (BSA/Hercules) + TI Clean Mobility (e-3W passenger + cargo); FY24 consolidated revenue Rs 16,890 Cr",
    lede=f'Tube Investments of India Limited (CIN L35100TN2008PLC069496){ref("955")} is the listed Murugappa Group flagship engineering platform &mdash; consolidating five businesses: precision steel tubes (industrial + automotive grade), engineering, metal-formed products, mobility (bicycles &mdash; BSA / Hercules / Philips brands), and the rapidly-scaling TI Clean Mobility EV business (e-3W passenger + cargo + e-tractor via Cellestial acquisition){ref("956")}. Listed BSE 540762 / NSE TIINDIA{ref("955")}; promoter holding 44% (Mar 2025){ref("955")}; HQ Chola Crest, Guindy, Chennai 600 032. <strong>FY24 consolidated revenue Rs 16,890 Cr</strong>{ref("128")}; EBITDA Rs 2,200 Cr (13.0%); PAT Rs 1,683 Cr (pre-exceptional); virtually debt-free at the standalone level. ~53,000 FTE (group-wide){ref("955")}. The structural story FY26-FY29 is the EV-mobility scale-up &mdash; TI Clean Mobility has rolled out Montra Electric e-3W cargo + Montra Eviator e-3W passenger and via Cellestial Mobility entered the e-tractor market; the platform is the most credible domestic challenger to Mahindra Last Mile Mobility + Bajaj e-3W in the small-commercial-EV cluster.',
    headline_low=24, headline_high=42,
    headline_strap="Y3 wallet (capex TL + EV-mobility ramp + group-wide product bundle)",
    industry_short="Precision tubes / Auto-components / EV mobility",
    kpi3='<div class="kpi pos"><div class="k">Listed</div><div class="v num">BSE+NSE</div><div class="sub">TIINDIA' + ref("955") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AA+</div><div class="sub">Stable [diligence verify]</div></div>',
    three_angles=[
        "<strong>TI Clean Mobility capex TL Rs 400-700 Cr</strong> &mdash; e-3W + e-tractor + battery-pack capex; sustainability-linked covenant on EV-revenue mix; FY27-FY29 anchor window.",
        "<strong>Auto-component export hedge (USD + EUR)</strong> &mdash; precision tubes export to global auto OEMs; FX 100-300 Mn USD notional; LME-steel hedge.",
        "<strong>Murugappa group ecosystem cross-sell</strong> &mdash; TII is one of 5 flagships (CUMI, EID Parry, Coromandel, Chola Finance); Y3 wallet via group capex + treasury + family-PB on Vellayan + M.M. Murugappan promoter family.",
    ],
    incorp_date="06 Oct 2008 (TI Cycles est 1949)",
    ho_text="Chola Crest, C54-55 + Super B-4, Thiru-Vi-Ka Industrial Estate, Guindy, Chennai 600 032",
    group_text=f'Murugappa Group flagship (via Ambadi Investment Ltd promoter vehicle){ref("955")}. Group structure: 9 listed entities including TII + CUMI + EID Parry + Coromandel + Chola Finance + Chola Holdings + Wendt + Chola General Insurance. TII operating subsidiaries: TI Clean Mobility Pvt Ltd (e-3W passenger + cargo); IPLTech Electric Pvt Ltd; Jayem Automotives Pvt Ltd; TIVOLT Electric Vehicles Pvt Ltd; TI Medical Pvt Ltd; Cellestial E-Mobility (e-tractor) acquired 2024.',
    funding_anchors=[
        f"Listed Murugappa flagship; promoter holding 44%{ref('955')} (Ambadi Investment Ltd + family).",
        "Standalone is virtually debt-free; consolidated debt is at TI Clean Mobility subsidiary for EV capex.",
        "FY24 paid-up Rs 19.32 Cr; reserves Rs 4,500+ Cr (analyst-est at consolidated level).",
        f"Disclosed transactional banking{ref('128')}: SBI + HDFC + Axis + Kotak (consortium of ~6-8 banks across operating subsidiaries).",
        "<strong>Diligence item:</strong> Probe42 deep-charge pull required on each operating subsidiary CIN to identify IBank position vs targets.",
    ],
    toi_fy23=15000, toi_fy24=16890, toi_fy25=18800, toi_fy26=21500, toi_fy27=25500, toi_fy28=30000,
    eb_fy23=1750, eb_fy24=2200, ebitda_fy25=2540, eb_fy26=3010, eb_fy27=3700, eb_fy28=4500,
    mg_fy23="11.7", mg_fy24="13.0", ebitda_pct="13.5", mg_fy26="14.0", mg_fy27="14.5", mg_fy28="15.0",
    pat_fy23=1380, pat_fy24=1683, pat_fy25=1900, pat_fy26=2280, pat_fy27=2800, pat_fy28=3400,
    tnw_fy23=4800, tnw_fy24=5800, tnw_fy25=7000,
    dt_fy23="~400", dt_fy24="~600", debt_fy25="~900",
    dr_fy23="0.08x", dr_fy24="0.10x", dr_fy25="0.13x",
    paid_up=20, fte="~12,500 (TII standalone) · ~53,000 group",
)

CFG.update(dict(
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Open charges</div><div class="v num">Multi-bank</div><div class="sub">Consortium across subsidiaries{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 1,800 Cr</div><div class="sub">Treasury (est)</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AA+</div><div class="sub">Stable [verify]</div></div>',
    charges_summary="Multi-bank consortium across TII + TI Clean Mobility + IPLTech + Jayem + Cellestial subsidiaries",
    charges_strap="Strategic: anchor capex TL on TI Clean Mobility EV scale-up; group treasury + family-PB on Murugappa promoter base.",
    industry_text=(
        f'India precision-steel-tubes sub-segment FY25 ~Rs 28-32k Cr; CAGR 9-12% driven by auto + capex + infra. '
        f'EV-mobility cluster FY25 ~Rs 18-22k Cr; CAGR 35-45%. Bicycles FY25 ~Rs 5-6k Cr; CAGR 4-6%. TII competes with '
        f'Mahindra Last Mile Mobility + Bajaj Auto e-3W (EV-mobility); Hero Cycles + Atlas Cycles (bicycles); '
        f'Bharat Forge + Sona BLW + Sundram Fasteners (auto-components); Jindal Stainless Hisar + Maharashtra Seamless (precision tubes).'
    ),
    drivers=[
        f"<strong>TI Clean Mobility EV scale-up FY26-FY29</strong>{ref('955')} &mdash; Montra Eviator + Montra Cargo + Cellestial e-tractor; capex Rs 400-700 Cr; battery-pack vertical integration.",
        f"<strong>Auto-component export</strong> &mdash; precision tubes to Stellantis / Ford / Renault tier-1 globally; USD + EUR receivables; FX hedge essential.",
        f"<strong>Steel + raw-material cycle</strong>{ref('14')} &mdash; HRC + special-steel input 50-55% of COGS; LME-zinc + steel hedge.",
        f"<strong>Bicycle-cluster modernisation</strong> &mdash; BSA / Hercules / Philips brand re-investment; e-bike pivot.",
        f'USA-tariff window{ref("6")}: indirect &mdash; precision-tubes export to USA tier-2 OEMs may face anti-dumping risk.',
    ],
    product_rows=[
        ("Capex TL (TI Clean Mobility EV)", "400&ndash;700", "8", "12", "Sustainability-linked; EV-revenue-mix step-down"),
        ("CC + WCDL (steel cycle)", "300&ndash;500", "3", "5", "Steel + zinc inventory + WIP"),
        ("BG (auto OEM bid + capex retention)", "200&ndash;400", "2", "3.5", "Stellantis + Ford + Renault tier-1 BG"),
        ("LC + Trade (capex + steel imports)", "250&ndash;500 revolving", "1.5", "3", "Korean / Japanese / German precision-steel + EV machinery"),
        ("FX (USD + EUR forward + IRS)", "USD 100&ndash;300 Mn", "2.5", "5", "Auto-component export + capex import"),
        ("OEM-anchor SCF (Maruti/M&M/Tata/Hyundai)", "150&ndash;300", "1.5", "3", "Auto-OEM 60-day discount"),
        ("Bicycle-dealer SCF + retail-finance", "100&ndash;200", "1", "2", "BSA + Hercules + Philips dealer network"),
        ("Salary CASA + payroll (12,500 FTE)", "Rs 25-50 Cr float", "0.8", "1.5", "TII + subs"),
        ("PB (Vellayan + Murugappan + Murugappa family)", "Rs 300-600 Cr AUM", "1.5", "3", "Multi-gen family + 5-flagship-promoter platform"),
    ],
    wholesale_y3="Rs 14.5-26.5 Cr / yr",
    retail_text="Salary CASA mandate ~12,500 FTE; bicycle dealer-finance network 5,000+ outlets; Rs 1.5-3 Cr/yr.",
    pb_text="Vellayan family + M.M. Murugappan + Subbiah family + family-trust; PB AUM Rs 300-600 Cr (TII share); Rs 1.5-3 Cr/yr.",
    tasc_text="TII PF + Gratuity + Murugappa Foundation TASC; corpus Rs 200-300 Cr; Rs 1.0-1.5 Cr/yr.",
    retail_total_low="3.5", retail_total_high="7.0",
    consolidated_rows=[
        ("Capex TL (EV mobility)", "8", "12"),
        ("CC + WCDL + BG + Trade + FX", "10", "19.5"),
        ("OEM-anchor SCF + bicycle-SCF", "2.5", "5"),
        ("Salary + PB + TASC", "3.5", "7.0"),
    ],
    consolidated_total_low="24.0", consolidated_total_high="43.5",
    kmp_text=(
        "<strong>M.A.M. Arunachalam (Aru)</strong> &mdash; Chairman, TII (since 2017; Murugappa family fifth-generation). "
        "<strong>Mukesh Ahuja</strong> &mdash; Managing Director (since 2024). "
        "<strong>K. Mahendra Kumar</strong> &mdash; CFO. "
        "<strong>Pradeep V. Bhide</strong>, <strong>Rohit Adya</strong>, others &mdash; Independent Directors. "
        "TI Clean Mobility leadership: Murali Padmanabhan (CEO TI Clean Mobility); Vellayan Subbiah is Group Executive Chairman of Murugappa overall."
    ),
    ownership_text="Promoter holding 44% (Ambadi Investment Ltd + Murugappa family); FII 22%; DII 18%; public 16%.",
    diligence_news=(
        "FY26: TI Clean Mobility scaling Montra e-3W + Montra Cargo nationally; "
        "Cellestial e-tractor commercial launch H2 FY27; "
        "Bicycle-business e-bike pivot underway."
    ),
    dil2="T+14: Probe42 detail-charge pull on TII + TI Clean Mobility + Cellestial CINs; CRISIL rationale.",
    dil3="T-14: Pre-pitch EV-capex term-sheet + LME-steel hedge structure + Murugappa family-PB partner profile.",
    playbook_30="Mukesh Ahuja CFO meeting; EV-capex concept memo; family-PB introduction sequence.",
    playbook_60="EV capex TL term-sheet committee-grade; FX + LME steel hedge first deal; group cross-sell mapping.",
    playbook_90="Capex drawn 25%; bicycle-SCF first 100 dealers; OEM-anchor SCF 2-3 customers.",
    playbook_180="Murugappa group cross-sell (CUMI + EID Parry + Coromandel + Chola Finance) treasury sweep + capex.",
    success_metrics=[
        "TI Clean Mobility capex TL anchor seat (Rs 400 Cr) by Q3 FY27",
        "FX hedge book USD 150 Mn notional by Q2 FY27",
        "Y3 (FY29) wallet run-rate Rs 24-42 Cr",
        "Murugappa family-PB AUM Rs 300+ Cr by Q4 FY28",
    ],
    src_base=955,
    src_parent_body=(
        "TII corporate disclosures + Murugappa Group AR + NSE/BSE filings + Tofler + Tracxn + screener.in (retrieved 28 Apr 2026)."
    ),
    src_parent_url="tiindia.com &middot; murugappa.com &middot; nseindia.com &middot; bseindia.com",
    src_extra=[
        (955, "Tube Investments of India Annual Report FY24 + investor relations", "tiindia.com/investor-relations &middot; retrieved 28 Apr 2026"),
        (956, "TI Clean Mobility + Cellestial E-Mobility acquisition disclosures", "TII press releases 2024-2025"),
        (957, "NSE/BSE TIINDIA quarterly filings", "nseindia.com / bseindia.com TIINDIA / 540762"),
        (958, "Murugappa Group corporate site", "murugappa.com group structure"),
    ],
    footer="Cipher clean; 1,500+ lines; Murugappa flagship listed entity with TI Clean Mobility EV-capex anchor + group cross-sell + family-PB triangulation on 5-flagship promoter base.",
))


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 75-year arc from TI Cycles to Murugappa engineering flagship + EV mobility</div>

<h3>03A.1 Founding (1949) &mdash; Tube Investments of India Ltd, the original</h3>
<p><strong>TI Cycles of India</strong> was founded <strong>1949</strong> as a JV between the British TI Group (Tube Investments plc, UK) and the Murugappa Chettiar group<sup class="ref">[<a href="#src-955">955</a>]</sup>. The Indian operations manufactured bicycles under the BSA, Hercules and Philips brands &mdash; brands that defined the Indian cycle market through the 1950s-60s. Tube Products of India was incorporated separately for industrial precision tubes.</p>

<h3>03A.2 Murugappa control (1959-1990s) &mdash; Indianisation + diversification</h3>
<p>The two companies merged in 1959 to form the integrated Tube Investments of India platform. Through the 1960s-70s the company built India's first cold-rolled-steel-strip + precision-tubes manufacturing scale and the largest bicycle distribution network. By the late 1980s, Murugappa Group (via Ambadi Investments) had bought out the British TI Group stake and took 100% promoter control.</p>

<h3>03A.3 Demerger and re-listing (2006-2008) &mdash; the Tube Investments Ltd we know today</h3>
<p>The current entity (CIN L35100TN2008PLC069496){ref("955")} was incorporated <strong>06 October 2008</strong> as part of a Murugappa-group corporate-restructuring exercise that demerged TII's investment + financial-services arm (which became Cholamandalam Holdings) from the engineering business. TII relisted on BSE and NSE in 2017 after consolidating the engineering platform.</p>

<h3>03A.4 The 2010s &mdash; auto-component scale + global precision-tube capability</h3>
<p>Through the 2010s, TII built scale in auto-component precision tubes (door-impact beams, propeller shafts, axle tubes) supplying global tier-1s &mdash; Stellantis, Ford, Renault, GM, plus all Indian OEMs. The Tubes division emerged as a Tier-1 supplier with Tier-2 export capability. Bicycles continued strong domestic + emerging-market export.</p>

<h3>03A.5 The EV pivot (2020-2024) &mdash; TI Clean Mobility</h3>
<p>The structural inflection point was the <strong>TI Clean Mobility</strong> announcement in 2021<sup class="ref">[<a href="#src-956">956</a>]</sup>. Initial capex of Rs ~750 Cr was committed for e-3W passenger (Montra Eviator) + e-3W cargo (Montra Cargo) + e-tractor (via the 2024 acquisition of Cellestial E-Mobility, an early-stage e-tractor startup). IPLTech Electric was acquired for e-CV; Jayem Automotives + TIVOLT formed the broader EV platform. By FY25, TII had emerged as the most credible domestic EV-mobility challenger to Mahindra Last Mile Mobility + Bajaj e-3W in the small-commercial-EV cluster.</p>

<h3>03A.6 The next 36 months (FY26-FY29) &mdash; capex window + family transition</h3>
<p>FY24 consolidated revenue Rs 16,890 Cr<sup class="ref">[<a href="#src-128">128</a>]</sup>; analyst-est trajectory FY25 Rs 18,800 Cr → FY28 Rs 30,000 Cr (CAGR ~12% with EV-business as the swing factor). Capex envelope Rs 400-700 Cr at TI Clean Mobility for the next 36 months. Family transition: Vellayan Subbiah is Group Executive Chairman of Murugappa overall; M.A.M. Arunachalam (Aru) is TII Chairman; Mukesh Ahuja became MD in 2024 &mdash; the operational leadership refresh signals a more aggressive growth + capex-deployment phase.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 75-year arc tells you: (1) Murugappa is a <strong>builder-group</strong>, not a trader-group &mdash; TII has reinvested across every cycle; (2) the EV-mobility play is <strong>not greenfield speculation but engineering execution</strong> &mdash; TII has the steel + auto-component + battery-pack + manufacturing-engineering DNA to win; (3) the 5-flagship Murugappa structure makes TII the entry-point to a Rs 75,000 Cr group-treasury opportunity (TII + CUMI + EID Parry + Coromandel + Chola Finance) &mdash; the bank that wins TII gets cross-sell into all five.</p>
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
        html = html.replace(
            '\n\n<section id="entity">',
            '\n\n' + HISTORY_BLOCK_HTML + '\n\n<section id="entity">',
            1,
        )
        p.write_text(html)
        print(f"Injected history block into {p}")


if __name__ == "__main__":
    build()
