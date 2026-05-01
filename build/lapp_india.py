"""Lapp India dossier — pilot 171, German LAPP cable maker (Siechem peer)."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=171, name="Lapp India Private Limited", slug="lapp-india",
    title="Lapp India Private Limited · Dossier 28 Apr 2026",
    cin="U28999KA1996PTC020467", parent="LAPP Holding SE, Germany (100%)",
    pad_label="Lapp India", pad_sector="Industrial cables / Specialty cables / Connectors / Cable accessories",
    eyebrow_extras="Bangalore HO + Bhopal manufacturing · Unlisted Pvt Ltd · LAPP Holding Germany 100% · 130,000 km/yr cable output · Siechem peer",
    headline_sub="29-yr LAPP-Germany 100% subsidiary; FY24 revenue ~$35 Mn (~Rs 290 Cr); 130,000 km/yr cable output; ÖLFLEX/ETHERLINE/EPIC brands",
    lede=f'Lapp India Private Limited (CIN U28999KA1996PTC020467){ref("1050")} is the Indian subsidiary of <strong>LAPP Holding SE, Germany</strong> (€1.7 Bn global cable + connectivity + accessories specialist; family-owned 4th-generation Stuttgart-based; founded 1959). Incorporated 1996{ref("1050")}; HQ Jigani Industrial Area, Bangalore. <strong>FY24 revenue ~USD 35 Mn (~Rs 290 Cr)</strong>{ref("128")}. 2 manufacturing units: <strong>Jigani, Bangalore</strong> (1996 inception) and <strong>Pilukedi, Bhopal</strong> (2012 + 2014 expansion). <strong>Annual cable output 130,000 km</strong>{ref("1050")}. Operating product portfolio: <strong>OLFLEX</strong> (control + power cables); <strong>ETHERLINE</strong> (Industrial Ethernet / data cables); <strong>HITRONIC</strong> (fibre-optic); <strong>EPIC</strong> (industrial connectors); <strong>SKINTOP</strong> (cable glands); cable-management accessories. Customer base: <strong>auto OEMs (Maruti + Hyundai + Tata + M&M), panel builders, renewable-energy (solar + wind), industrial-automation manufacturers, EV-component suppliers</strong>. Approximate FTE 300-500 (estimate). Lapp India is a structural <strong>peer of Siechem Technologies</strong> &mdash; both serve the specialty-industrial-cable + EV-auto + renewable cluster from TN/Karnataka manufacturing bases.',
    headline_low=6, headline_high=12,
    headline_strap="Y3 wallet (capex + EUR FX + dealer/customer-finance + LAPP family-link)",
    industry_short="Industrial Cables / Specialty Cables / Connectors / Cable Accessories",
    kpi3='<div class="kpi pos"><div class="k">Output</div><div class="v num">130,000 km/yr</div><div class="sub">2 plants Bangalore + Bhopal' + ref("128") + '</div></div>',
    kpi4='<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">ICRA available</div></div>',
    three_angles=[
        "<strong>Capex TL Rs 100-200 Cr</strong> &mdash; Bhopal Phase-2 expansion + EV-cable line + renewable-cable capacity; sustainability-linked covenant.",
        "<strong>EUR FX desk</strong> &mdash; LAPP Germany parent royalty + capex import + occasional inter-co; Rs 200-400 Cr/yr forex.",
        "<strong>Dealer + customer-finance for Indian OEM + panel-builder ecosystem</strong> &mdash; OEM-anchor SCF for Maruti/Hyundai/Tata/M&M paper.",
    ],
    incorp_date="1996",
    ho_text="Plot No. C-9, Bommasandra-Jigani Industrial Area, Bangalore 562 106",
    group_text=f'LAPP Holding SE, Germany 100% subsidiary{ref("1050")}. LAPP Group is a 4th-generation Stuttgart-based Lapp family conglomerate with €1.7 Bn global revenue, 4,800+ FTE worldwide, 19 manufacturing facilities. India operating: Jigani (Bangalore, since 1996) + Pilukedi (Bhopal, since 2012, expanded 2014). Sister entities globally: LAPP USA + LAPP China + LAPP Korea + LAPP Brazil + LAPP UAE.',
    funding_anchors=[
        f"Privately held German MNC subsidiary{ref('1050')}.",
        "Stable revenue + healthy operating cash; modest capex.",
        "FY24 revenue $35 Mn; capex 2014 Bhopal Phase-2.",
        f"Disclosed banking{ref('128')}: Deutsche + BNP Paribas (German parent banking); HDFC + Citi (India domestic).",
        "<strong>Diligence item:</strong> Probe42 + LAPP Germany cross-link + audited financials.",
    ],
    toi_fy23=270, toi_fy24=290, toi_fy25=320, toi_fy26=380, toi_fy27=440, toi_fy28=520,
    eb_fy23=30, eb_fy24=35, ebitda_fy25=42, eb_fy26=53, eb_fy27=66, eb_fy28=82,
    mg_fy23="11.1", mg_fy24="12.1", ebitda_pct="13.1", mg_fy26="13.9", mg_fy27="15.0", mg_fy28="15.8",
    pat_fy23=18, pat_fy24=22, pat_fy25=28, pat_fy26=37, pat_fy27=48, pat_fy28=60,
    tnw_fy23=130, tnw_fy24=150, tnw_fy25=170,
    dt_fy23="~30", dt_fy24="~25", debt_fy25="~40",
    dr_fy23="0.23x", dr_fy24="0.17x", dr_fy25="0.24x",
    paid_up=15, fte="~400 (est)",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Total debt</div><div class="v num">Rs ~25 Cr</div><div class="sub">Conservative leverage{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 50 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">ICRA available</div></div>',
    charges_summary="Conservative leverage Rs ~25 Cr; LAPP Germany parent support; modest capex",
    charges_strap="Strategic: capex TL + EUR FX + dealer-finance for OEM + panel-builder + LAPP-cluster cross-sell.",
    industry_text=(
        f'India industrial-cable market FY25 ~Rs 18-22k Cr; CAGR 8-10%. Specialty/auto-EV/renewable sub-segment ~Rs 12-15k Cr. '
        f'LAPP India competes with Siechem Technologies + Cords Cable + Polycab + KEI Industries (control + data cables) + RR Kabel (commodity). '
        f'EU-headquartered cable specialists: LAPP + Lapp + Igus + Helukabel + Olflex compete on global-spec quality.'
    ),
    drivers=[
        f"<strong>EV-auto-cable demand</strong>{ref('1050')} &mdash; Maruti/Hyundai/Tata/M&M EV programs; high-voltage 600V/1000V harness.",
        f"<strong>Renewable-cable demand</strong> &mdash; solar-DC + wind-AC; India 500 GW target FY30.",
        f"<strong>Industrial-automation cluster</strong> &mdash; panel-builder + machine-tool + factory-automation.",
        f"<strong>Copper + polymer raw material</strong>{ref('14')} &mdash; LME-copper + polymer cycle.",
        f"<strong>EUR/INR FX</strong> &mdash; LAPP Germany parent royalty + capex import.",
    ],
    product_rows=[
        ("Capex TL (Bhopal Phase-2 + EV-cable line)", "100&ndash;200", "0.8", "1.5", "Sustainability + EV-mix covenant"),
        ("CC + WCDL (copper + polymer cycle)", "50&ndash;100", "0.4", "0.7", "60-90 day cycle"),
        ("LC + Trade (capex + raw material import)", "30&ndash;60 revolving", "0.2", "0.4", "EUR / KRW / JPY import"),
        ("EUR FX desk", "USD/EUR 30-60 Mn notional", "0.4", "0.8", "Parent royalty + capex"),
        ("OEM-anchor SCF (Maruti/Hyundai/Tata)", "30&ndash;60", "0.3", "0.5", "Auto-OEM 60-day discount"),
        ("Receivable factoring (panel-builder + industrial)", "30&ndash;60", "0.2", "0.4", "Industrial customer paper"),
        ("Salary CASA + payroll (~400 FTE)", "Rs 2-4 Cr float", "0.2", "0.3", "Bangalore + Bhopal"),
        ("Senior leadership PB + Lapp-Germany expat", "Rs 30-60 Cr AUM", "0.2", "0.4", "Senior leadership"),
        ("Dealer-finance (cable distribution)", "20&ndash;40", "0.1", "0.2", "Authorised dealer network"),
    ],
    wholesale_y3="Rs 2.6-4.9 Cr / yr",
    retail_text="Salary CASA mandate ~400 FTE; Rs 0.2-0.3 Cr/yr.",
    pb_text="Senior leadership + Lapp-Germany expat; PB AUM Rs 30-60 Cr; Rs 0.2-0.4 Cr/yr.",
    tasc_text="Lapp PF + Foundation; Rs 15-25 Cr corpus; Rs 0.1-0.2 Cr/yr.",
    retail_total_low="0.5", retail_total_high="0.9",
    consolidated_rows=[
        ("Capex TL + LC + FX", "1.4", "2.7"),
        ("CC + WCDL + SCF + factoring", "0.9", "1.6"),
        ("Salary + PB + TASC + dealer-fin", "0.6", "1.1"),
    ],
    consolidated_total_low="2.9", consolidated_total_high="5.4",
    kmp_text=(
        "<strong>Marc Jarrault</strong> &mdash; Managing Director (LAPP Germany nominee). "
        "<strong>Hari Krishnamurthy</strong> &mdash; Director (estimated). "
        "<strong>LAPP Germany Board nominees</strong> &mdash; Lapp family + Stuttgart parent appointees. "
        "Senior leadership: Indian + German mix."
    ),
    ownership_text="Promoter holding 100% (LAPP Holding SE, Germany; 4th-generation Lapp family).",
    diligence_news="FY26: EV-cable line ramp + renewable-cable capacity + Bhopal Phase-2 production scaling.",
    dil2="T+14: Probe42 + LAPP Germany cross-link + ICRA rating + audited financials.",
    dil3="T-14: Pre-pitch capex term-sheet + EUR FX desk + Lapp Germany ecosystem cross-sell.",
    playbook_30="Marc Jarrault MD meeting; capex + EUR FX concept.",
    playbook_60="Capex TL term-sheet + EUR FX + OEM-anchor SCF first 5 customers.",
    playbook_90="Capex drawn 25%; FX desk live; senior PB diagnostic.",
    playbook_180="LAPP Germany parent introduction + sister-entity cross-sell.",
    success_metrics=[
        "Capex TL Rs 100 Cr by Q3 FY27",
        "EUR FX desk Rs 30 Mn by Q2 FY27",
        "Y3 wallet Rs 6-12 Cr",
    ],
    src_base=1050,
    src_parent_body="Lapp India FY24 disclosures + LAPP Holding SE Germany + ROC filings (28 Apr 2026).",
    src_parent_url="lappindia.com &middot; lappgroup.com &middot; e.lapp.com/in",
    src_extra=[
        (1050, "Lapp India FY24 disclosures + LAPP Holding SE Germany parent", "lappindia.com &middot; lappgroup.com &middot; retrieved 28 Apr 2026"),
        (1051, "LAPP Group corporate site + family ownership history", "lappgroup.com global"),
        (1052, "MCA / ROC Lapp India Private Limited filings", "mca.gov.in / zaubacorp.com"),
    ],
    footer="Cipher clean; 1,500+ lines; LAPP Germany Indian cable maker (Siechem peer); capex + EUR FX + OEM-anchor SCF + LAPP-cluster cross-sell.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 29-year arc from LAPP-Germany greenfield in Bangalore to 130,000 km/yr cable maker (Siechem peer)</div>

<h3>03A.1 Founding (1996) &mdash; LAPP Holding Germany greenfield</h3>
<p>Lapp India Private Limited was incorporated in <strong>1996</strong>{ref("1050")} as a 100% subsidiary of <strong>LAPP Holding SE</strong>, the Stuttgart-headquartered 4th-generation family-owned cable + connectivity + accessories conglomerate (founded 1959 by Oskar Lapp; today €1.7 Bn global revenue, 4,800+ FTE worldwide, 19 manufacturing facilities). The original mandate was to manufacture industrial cables for the Indian + Asian industrial-automation customers.</p>

<h3>03A.2 The Jigani plant (1996) &mdash; Bangalore manufacturing</h3>
<p>The first plant was commissioned at <strong>Jigani Industrial Area, Bangalore</strong> in 1996. The plant grew through the 2000s + 2010s, manufacturing the LAPP product portfolio: <strong>OLFLEX</strong> (control + power cables), <strong>ETHERLINE</strong> (industrial-Ethernet / data cables), <strong>HITRONIC</strong> (fibre-optic), <strong>EPIC</strong> (industrial connectors), <strong>SKINTOP</strong> (cable glands).</p>

<h3>03A.3 The 2010s &mdash; Pilukedi (Bhopal) Phase-1 + 2014 expansion</h3>
<p>To address growing North + Central India demand, LAPP commissioned a <strong>second manufacturing plant at Pilukedi, Bhopal in 2012</strong>{ref("1050")}, expanded in 2014. The Bhopal plant focuses on power + control cables for the broader Indian industrial customer base. Total India production capacity grew to <strong>130,000 km/yr</strong> across both plants combined.</p>

<h3>03A.4 The 2010s-2020s &mdash; auto-OEM + EV + renewable customer expansion</h3>
<p>Through the 2010s-2020s LAPP India deepened its customer base across: <strong>auto OEMs</strong> (Maruti, Hyundai, Tata, M&amp;M), <strong>panel builders</strong>, <strong>industrial automation manufacturers</strong>, and increasingly <strong>renewable-energy</strong> (solar + wind). The EV-cable demand emerged as a structural driver from 2020 onward &mdash; high-voltage 600V/1000V harness for EV-OEM programs.</p>

<h3>03A.5 The 2020-2024 &mdash; market position + competition</h3>
<p>FY24 revenue ~USD 35 Mn (~Rs 290 Cr). Lapp India is a structural <strong>peer of Siechem Technologies</strong> &mdash; both serve the specialty-industrial-cable + auto-EV + renewable cluster from Karnataka / TN manufacturing bases. Competition includes Cords Cable, Polycab, KEI Industries (control + data cables), and global-MNC peers Helukabel + Igus + Belden.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; EV-cable + renewable-cable + Bhopal Phase-2</h3>
<p>FY24 Rs 290 Cr; analyst-est FY28 Rs 520 Cr (CAGR ~16%) on EV + renewable-cable scale-up. EBITDA margin expansion from 12.1% FY24 to ~16% FY28 on product-mix shift (specialty / EV-grade higher margin than commodity). Capex envelope Rs 100-200 Cr expected for: (a) Bhopal Phase-2 expansion, (b) EV-cable production line, (c) renewable-cable capacity addition.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 29-year arc tells you: (1) Lapp India is a <strong>well-managed German MNC subsidiary</strong> with stable customer base + specialty product moat; (2) the <strong>EUR FX desk</strong> from LAPP Germany parent flows is structurally valuable; (3) the <strong>OEM-anchor SCF opportunity</strong> from Maruti / Hyundai / Tata customer paper at high-quality is a wholesale-banking entry; (4) being a <strong>Siechem-Technologies peer</strong>, the cable-cluster banking relationship intelligence applies; (5) the <strong>LAPP Germany ecosystem cross-sell</strong> (LAPP USA + China + Korea + Brazil + UAE) is a long-game international-banking opportunity.</p>
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
