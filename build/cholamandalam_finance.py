"""Cholamandalam Investment & Finance dossier — pilot 156, Murugappa NBFC flagship."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=156, name="Cholamandalam Investment & Finance Company Limited", slug="cholamandalam-finance",
    title="Cholamandalam Investment & Finance Company Limited (Chola) · Dossier 28 Apr 2026",
    cin="L65993TN1978PLC007576", parent="Cholamandalam Financial Holdings / Murugappa Group",
    pad_label="Cholamandalam Finance", pad_sector="Diversified NBFC: vehicle finance + home loan + LAP + SME",
    eyebrow_extras="Chennai HO · Listed BSE+NSE CHOLAFIN · CRISIL A1+ · 1,757 branches · Murugappa NBFC flagship",
    headline_sub="46-year Murugappa NBFC; AUM Rs 1.48 lakh Cr (+36% FY24); 44.7 lakh+ retail customers; pan-India 1,757 branches",
    lede=f'Cholamandalam Investment &amp; Finance Company Limited (CIN L65993TN1978PLC007576){ref("975")} is a 46-year-old listed Murugappa Group NBFC and one of India&rsquo;s largest non-bank lenders. Listed BSE+NSE CHOLAFIN{ref("975")}; promoter holding 49.90% (Jun 2025); HQ Chennai. <strong>FY24 Total Income Rs 19,216 Cr</strong>{ref("128")}; AUM grew 36% from Rs 1,08,840 Cr to <strong>Rs 1,48,167 Cr</strong>{ref("975")}; PAT Rs 3,423 Cr (+28% YoY); ROTA 2.55%; D/E 0.36x (down from 0.47x FY23); gearing 7.1x; <strong>CRISIL A1+ on Commercial Paper + Debt instruments</strong>{ref("128")}. 44.7 lakh+ retail customers; 1,577 branches Dec 2024 (1,757 latest); FY24 raised Rs 4,000 Cr capital (Rs 2,000 Cr QIP + Rs 2,000 Cr CCD). Operating segments: <strong>Vehicle Finance</strong> (commercial + passenger + 2W); <strong>Home Loans</strong>; <strong>Loan Against Property (LAP)</strong>; <strong>SME / Business Loans</strong>; <strong>Consumer + Small Enterprise Loans</strong>; <strong>Loan Against Securities</strong>. Chola Holdings (Cholamandalam Financial Holdings) is the holding company; Cholamandalam MS General Insurance is a sister concern.',
    headline_low=28, headline_high=50,
    headline_strap="Y3 wallet (NBFC term-loan + securitisation/co-lending + group cross-sell + family-PB)",
    industry_short="Diversified NBFC: vehicle finance + home loans + LAP + SME",
    kpi3='<div class="kpi"><div class="k">AUM</div><div class="v num">Rs 1.48L Cr</div><div class="sub">+36% FY24' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A1+</div><div class="sub">Highest CP rating' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>NBFC term-loan + co-lending mandate Rs 800-1,500 Cr</strong> &mdash; Chola is one of the largest NBFC liability raisers in India; bilateral TL + co-lending arrangements + securitisation + ECB.",
        "<strong>Cash-management + treasury at NBFC scale</strong> &mdash; pan-India 1,757 branches + 44.7 lakh customers means Chola needs payment-rails partner; CMS + UPI rails + corp-card + treasury sweep.",
        "<strong>Murugappa group + Chola family-PB</strong> &mdash; Vellayan Subbiah (Chola Group Chairman) + multi-gen family wealth + Chola management + senior leadership ESOP.",
    ],
    incorp_date="17 Aug 1978",
    ho_text="Dare House, Parry's, Chennai 600 001",
    group_text=f'Murugappa NBFC flagship; held via <strong>Cholamandalam Financial Holdings Ltd</strong> (CFHL, separately listed){ref("975")}. Sister concerns: <strong>Cholamandalam MS General Insurance Co. Ltd</strong> (51% Chola + 49% Mitsui Sumitomo); <strong>Cholamandalam MS Risk Services Ltd</strong>. Chola operates via 1,757 branches pan-India.',
    funding_anchors=[
        f"Listed Murugappa NBFC flagship; promoter 49.90%{ref('975')} (CFHL + family + cross-holdings).",
        "FY24 capital raise Rs 4,000 Cr (Rs 2,000 Cr QIP + Rs 2,000 Cr CCD); D/E 0.36x; gearing 7.1x &mdash; healthy for NBFC scale.",
        "AUM Rs 1.48 lakh Cr (Mar 2024) → Rs 1.85 lakh Cr (Mar 2025 est).",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Axis + Citi + Deutsche (large multi-bank borrowing relationships).",
        "<strong>Diligence item:</strong> NBFC borrower needs different lens &mdash; Probe42 + RBI + CRISIL deep-dive.",
    ],
    toi_fy23=15800, toi_fy24=19216, toi_fy25=23500, toi_fy26=28500, toi_fy27=34500, toi_fy28=42000,
    eb_fy23=4250, eb_fy24=5904, ebitda_fy25=7300, eb_fy26=9000, eb_fy27=11200, eb_fy28=14000,
    mg_fy23="26.9", mg_fy24="30.7", ebitda_pct="31.1", mg_fy26="31.6", mg_fy27="32.5", mg_fy28="33.3",
    pat_fy23=2666, pat_fy24=3423, pat_fy25=4280, pat_fy26=5350, pat_fy27=6700, pat_fy28=8400,
    tnw_fy23=10500, tnw_fy24=14500, tnw_fy25=18800,
    dt_fy23="~74,000", dt_fy24="~92,000", debt_fy25="~115,000",
    dr_fy23="7.1x", dr_fy24="6.3x", dr_fy25="6.1x",
    paid_up=164, fte="~24,000+ pan-India",
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Borrowing</div><div class="v num">Rs 92,000 Cr</div><div class="sub">FY24 outstanding (NBFC){ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 4,500 Cr</div><div class="sub">Treasury / liquidity</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL A1+</div><div class="sub">Highest CP rating</div></div>',
    charges_summary="NBFC borrower; Rs 92,000+ Cr outstanding borrowings (TL + NCD + CP + ECB) at FY24",
    charges_strap="Strategic: bilateral NBFC term loan + co-lending + securitisation; CMS / UPI / corp-card; Murugappa family-PB.",
    industry_text=(
        f'India NBFC sector FY25 ~Rs 50 lakh Cr AUM; Chola is among top 5-6 NBFCs. Vehicle finance ~Rs 12-14 lakh Cr; Chola #2-3 after '
        f'Bajaj Finance + Sundaram Finance. Home loans ~Rs 32 lakh Cr; LAP ~Rs 8-10 lakh Cr. RBI scale-based regulation (SBR) puts top NBFCs in '
        f'NBFC-Upper Layer (UL); higher capital + governance; CRR/SLR-equivalent prudential norms emerging.'
    ),
    drivers=[
        f"<strong>NBFC liability mix optimisation</strong> &mdash; bank TL + NCD + CP + ECB + securitisation + co-lending; Chola is sophisticated borrower.",
        f"<strong>RBI SBR-UL regulation</strong> &mdash; capital + governance + leverage caps; Chola is in Upper Layer; ALM management critical.",
        f"<strong>Vehicle finance demand</strong> &mdash; CV cycle + 2W + passenger demand drives AUM growth.",
        f"<strong>Home loan + LAP</strong> &mdash; mortgage demand growth; rate-sensitive.",
        f"<strong>Asset quality</strong> &mdash; GNPA Chola ~3-4%; NNPA ~2%; provisioning + write-back cycle.",
        f"<strong>Murugappa group treasury anchor</strong> &mdash; Chola's payment + retail-rails capability for group-wide.",
    ],
    product_rows=[
        ("Bilateral NBFC term-loan", "500&ndash;1,000", "5", "8", "Chola NBFC liability mix"),
        ("Co-lending mandate (mortgage / vehicle)", "1,000&ndash;2,500 facility", "4", "7", "PSL-eligible co-origination"),
        ("Direct assignment / securitisation", "500&ndash;1,500/yr", "3", "5", "Asset-pool transfer to bank"),
        ("Working-capital + treasury LCR", "200&ndash;400", "1", "2", "ALM optimisation"),
        ("CMS + UPI + corp-card (44.7 lakh customers)", "Rs 5,000-8,000 Cr GMV", "2", "3.5", "Payment rails + interchange"),
        ("Salary CASA (24,000+ FTE)", "Rs 60-100 Cr float", "1.5", "2.5", "Pan-India branch + HO"),
        ("PB (Murugappa family + Chola management)", "Rs 500-1,000 Cr AUM", "2.5", "4.5", "Vellayan + Chola CXO + ESOP"),
        ("Family-trust + ESOP advisory", "Multi-gen + senior leadership", "0.8", "1.5", "Chola CXO ESOP"),
        ("Sister-concern cross-sell (Chola MS General Insurance)", "Cross-channel", "0.6", "1.2", "Bancassurance partnership"),
    ],
    wholesale_y3="Rs 13.5-26.5 Cr / yr (NBFC + payment rails)",
    retail_text="Salary CASA mandate ~24,000+ FTE pan-India; Rs 1.5-2.5 Cr/yr.",
    pb_text="Murugappa family + Chola CXO ESOP; PB AUM Rs 500-1,000 Cr; Rs 2.5-4.5 Cr/yr.",
    tasc_text="Chola PF + Gratuity + Murugappa Foundation; Rs 250-400 Cr corpus; Rs 1.0-1.5 Cr/yr.",
    retail_total_low="5.0", retail_total_high="8.5",
    consolidated_rows=[
        ("Bilateral NBFC TL + co-lending + securitisation", "12", "20"),
        ("WC + treasury + payment rails", "3", "5.5"),
        ("Cross-sell (Chola MS Insurance)", "0.6", "1.2"),
        ("Salary + PB + TASC", "5.0", "8.5"),
    ],
    consolidated_total_low="20.6", consolidated_total_high="35.2",
    kmp_text=(
        "<strong>Vellayan Subbiah</strong> &mdash; Chairman, Cholamandalam (also Group Executive Chairman of Murugappa overall). "
        "<strong>Ravindra Kundu</strong> &mdash; Managing Director (since 2024 succession). "
        "<strong>Arul Selvan</strong> &mdash; Chief Financial Officer. "
        "<strong>D. Arul Selvan</strong>, <strong>Bhama Krishnamurthy</strong>, <strong>N. Ramesh Rajan</strong>, others &mdash; Independent Directors."
    ),
    ownership_text="Promoter holding 49.90% via CFHL + Murugappa Group; FII 28%; DII 12%; public 10%.",
    diligence_news="FY26: Continued AUM growth 25-30% target; vehicle finance + LAP + SME deepening; ESOP cycle for senior leadership.",
    dil2="T+14: NBFC borrower diligence (RBI SBR-UL norms); Probe42 + ratings + ALM scrutiny; Chola CFO meeting.",
    dil3="T-14: Pre-pitch bilateral TL term-sheet + co-lending PSL framework + payment-rails proposition + family-PB.",
    playbook_30="Ravindra Kundu + Arul Selvan meeting; bilateral TL + co-lending concept; payment-rails pitch.",
    playbook_60="Bilateral TL committee-grade; co-lending agreement signed; first securitisation Rs 500 Cr; CMS/UPI mandate.",
    playbook_90="TL drawn full; co-lending live; CMS/payment-rails live; Murugappa family-PB diagnostic.",
    playbook_180="Securitisation flow Rs 1,500 Cr+; Chola MS Insurance bancassurance partnership; full Murugappa group cross-sell.",
    success_metrics=[
        "Bilateral NBFC TL Rs 750 Cr + co-lending Rs 1,500 Cr facility by Q2 FY27",
        "Securitisation flow Rs 1,000 Cr/yr by Q4 FY27",
        "Y3 wallet Rs 28-50 Cr",
        "Murugappa family-PB Rs 500+ Cr (Chola share + Vellayan personal) by Q4 FY28",
    ],
    src_base=975,
    src_parent_body="Chola Annual Report FY24 + investor presentations + RBI SBR data + Murugappa Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="cholamandalam.com &middot; murugappa.com &middot; rbi.org.in",
    src_extra=[
        (975, "Cholamandalam Annual Report FY24 + investor presentations", "cholamandalam.com &middot; retrieved 28 Apr 2026"),
        (976, "RBI Scale-Based Regulation NBFC framework", "rbi.org.in/SBR-UL list"),
        (977, "NSE/BSE CHOLAFIN quarterly filings", "nseindia.com / bseindia.com"),
        (978, "CRISIL A1+ + CARE Ratings + ICRA rationale [verify FY26]", "crisil.com / careratings.com / icra.in"),
    ],
    footer="Cipher clean; 1,500+ lines; Murugappa NBFC flagship at AUM Rs 1.48 lakh Cr with bilateral TL + co-lending + securitisation + payment-rails + family-PB.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 46-year arc from vehicle-finance startup to Rs 1.48 lakh Cr Murugappa NBFC flagship</div>

<h3>03A.1 Founding (1978) &mdash; Murugappa-led credit-gap institution</h3>
<p>Cholamandalam Investment & Finance Company Limited was incorporated <strong>17 August 1978</strong> by the Murugappa Chettiar Group<sup class="ref">[<a href="#src-975">975</a>]</sup>. The original mandate was to address credit gaps in <strong>equipment finance + commercial-vehicle financing</strong> &mdash; segments where banks were under-served at the time. The Tata + Ashok Leyland CV ecosystem in TN-AP-Karnataka was the initial customer base.</p>

<h3>03A.2 The 1980s-1990s &mdash; Vehicle-finance leadership</h3>
<p>Through the 1980s-90s Chola became one of South India's leading vehicle-finance NBFCs. Disciplined credit + relationship-based lending built a portfolio of CV operator + small-fleet customers. The company stayed conservative through the Asian financial crisis + dot-com bust, building a reputation for asset-quality excellence.</p>

<h3>03A.3 The 2000s &mdash; Diversification into mortgages + LAP</h3>
<p>Chola diversified into <strong>home loans</strong> (mortgage finance) + <strong>Loan Against Property (LAP)</strong> in the 2000s. The vehicle-finance business expanded from commercial-vehicle into passenger-vehicle + 2W. The Cholamandalam MS General Insurance JV with Mitsui Sumitomo (Japan) was launched as a sister concern.</p>

<h3>03A.4 The 2010s &mdash; SME + scale-up + RBI scale-based regulation</h3>
<p>Through the 2010s Chola scaled aggressively. <strong>SME / Business Loans</strong> + <strong>Consumer Loans</strong> + <strong>Loan Against Securities</strong> diversified the AUM mix. Branch network expanded from a few hundred to 1,500+. The 2022 RBI Scale-Based Regulation (SBR) framework placed Chola in the <strong>NBFC Upper Layer (UL)</strong> &mdash; the highest tier with strictest capital + governance + leverage requirements.</p>

<h3>03A.5 The FY24 inflection &mdash; AUM Rs 1.48 lakh Cr + capital raise</h3>
<p>FY24 was a structural inflection. AUM grew <strong>36%</strong> from Rs 1,08,840 Cr to <strong>Rs 1,48,167 Cr</strong>{ref("975")}. PAT grew 28% to Rs 3,423 Cr. ROTA 2.55%. D/E fell from 0.47x to 0.36x. Capital raise Rs 4,000 Cr (Rs 2,000 Cr QIP + Rs 2,000 Cr CCD) provided runway for next-leg expansion. Branch network reached 1,577 (Dec 2024) → 1,757 (latest).</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; AUM scale + co-lending + RBI SBR-UL navigation</h3>
<p>AUM trajectory base-case: FY25 Rs 1.85 lakh Cr → FY28 Rs 3.50 lakh Cr (CAGR ~24%). The structural wholesale-banking mandate is around: (a) bilateral NBFC term-loans Rs 500-1,000 Cr ticket; (b) <strong>co-lending arrangements</strong> for PSL-eligible mortgage + vehicle; (c) <strong>direct-assignment + securitisation</strong> Rs 1,000-1,500 Cr/yr; (d) ECB at competitive cost; (e) ALM-management + LCR-prescription banking. Vellayan Subbiah is Chairman; Ravindra Kundu became MD in 2024.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 46-year arc tells you: (1) Chola is the <strong>most sophisticated NBFC borrower in the Murugappa group</strong> &mdash; the team understands liability-mix, ALM, and securitisation/co-lending economics; (2) the 24% AUM CAGR demands continuous incremental funding &mdash; bilateral TL + co-lending + securitisation are all in active mandate; (3) the <strong>payment-rails + CMS opportunity</strong> for 44.7 lakh customers + 1,757 branches is one of the largest single-NBFC retail banking-rails opportunities in India; (4) Chola's <strong>top management is itself a senior-PB pool</strong> &mdash; ESOP cycles + family + Vellayan personal wealth.</p>
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
