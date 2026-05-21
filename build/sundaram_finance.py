"""Sundaram Finance dossier — pilot 159, TVS NBFC."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=159, name="Sundaram Finance Limited", slug="sundaram-finance",
    title="Sundaram Finance Limited · Dossier 28 Apr 2026",
    cin="L65191TN1954PLC002429", parent="TVS Group / Sundaram Finance Holdings",
    pad_label="Sundaram Finance", pad_sector="NBFC: Vehicle Finance / Home Loans / Asset Management / Insurance",
    eyebrow_extras="Chennai HO · Listed BSE 590071 / NSE SUNDARMFIN · CRISIL AAA + A1+ · 71-yr TVS NBFC",
    headline_sub="71-yr TVS Group NBFC; AUM Rs 43,987 Cr; FY24 revenue Rs 7,290 Cr; PAT Rs 1,334 Cr (+23%); CRISIL AAA",
    lede=f'Sundaram Finance Limited (CIN L65191TN1954PLC002429){ref("990")} is a 71-year-old listed TVS Group NBFC and India\'s pre-eminent vehicle-finance pioneer. Listed BSE 590071 / NSE SUNDARMFIN{ref("990")}; promoter holding 37.2%; HQ Chennai. Founded 11 August 1954; became public 1961; listed 1972. <strong>FY24 Total Income Rs 7,290 Cr</strong>{ref("128")}; TOI Rs 6,730 Cr (excl exceptional); PAT Rs 1,334 Cr (+23%); EBITDA growth +23.2% YoY; D/E 1.1x (down from 1.2x FY23); ROCE 9.27% (up from 8.43% FY23). <strong>CRISIL AAA / Stable + CRISIL A1+ (Nov 2024)</strong>{ref("128")}. AUM Rs 43,987 Cr (vs Rs 34,552 Cr FY23 &mdash; +27%). Operating subsidiaries: <strong>Sundaram Home Finance Limited</strong> (housing loans, +30% disbursement growth FY25 to Rs 6,517 Cr); <strong>Sundaram Asset Management Company Limited</strong> (mutual funds); <strong>Royal Sundaram Alliance Insurance Company Ltd</strong> (general insurance JV). 71+ branch network pan-India. The TVS Group context: SF is one of the founding TVS Group entities; pre-dates Sundram Fasteners; the original mandate was vehicle-finance for the TVS / TS Trucks dealer network in the 1950s.',
    headline_low=22, headline_high=42,
    headline_strap="Y3 wallet (NBFC funding + co-lending + Sundaram-AMC + family-PB)",
    industry_short="NBFC: Vehicle Finance / Home Loans / AMC / Insurance",
    kpi3='<div class="kpi"><div class="k">AUM</div><div class="v num">Rs 43,987 Cr</div><div class="sub">+27% FY24' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AAA</div><div class="sub">Stable + A1+' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>NBFC bilateral term loan + co-lending Rs 1,000-2,000 Cr</strong> &mdash; SF is a sophisticated NBFC borrower; bank TL + co-lending PSL + securitisation + ECB.",
        "<strong>Sundaram AMC + Sundaram Home Finance + Royal Sundaram cross-sell</strong> &mdash; multi-entity TVS-financial-services platform; bancassurance + mutual-fund distribution + housing-finance partnership.",
        "<strong>TVS family-PB on Iyengar / Srinivasan / Sundaram clan</strong> &mdash; multi-generation TVS founding-family wealth; Sundaram Iyengar lineage + Sundaram-Clayton + TVS Motor + Wabco group.",
    ],
    incorp_date="11 Aug 1954",
    ho_text="21 Patullos Road, Chennai 600 002",
    group_text=f'TVS Group NBFC flagship; held via <strong>Sundaram Finance Holdings Limited</strong> (separately listed; CIN L65100TN1993PLC025044){ref("990")}. Operating subsidiaries: <strong>Sundaram Home Finance Ltd</strong> (housing loans); <strong>Sundaram Asset Management Co Ltd</strong> (mutual funds); <strong>Royal Sundaram General Insurance Ltd</strong> (51% Sundaram + 49% Royal SunAlliance UK then Mitsui Sumitomo); <strong>Sundaram Finance Trustee Co</strong>; <strong>Sundaram Finance Properties</strong>. 71+ branches pan-India.',
    funding_anchors=[
        f"Listed TVS NBFC; promoter 37.2%{ref('990')} via SF Holdings + family.",
        "AUM Rs 43,987 Cr; D/E 1.1x; healthy NBFC leverage.",
        "FY24 paid-up Rs 111 Cr; reserves Rs 8,500+ Cr.",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Axis + Citi + ICICI Securities (note: cipher-respect &mdash; sister concern only).",
        "<strong>Diligence item:</strong> NBFC borrower scrutiny &mdash; RBI SBR list + multi-bank borrowing book.",
    ],
    toi_fy23=5800, toi_fy24=7290, ebitda_fy25=8500, eb_fy23=2100, eb_fy24=2580, eb_fy26=10000, eb_fy27=11800, eb_fy28=14000,
    toi_fy25=8800, toi_fy26=10500, toi_fy27=12500, toi_fy28=14800,
    mg_fy23="36.2", mg_fy24="35.4", ebitda_pct="36.4", mg_fy26="36.8", mg_fy27="37.2", mg_fy28="37.5",
    pat_fy23=1088, pat_fy24=1334, pat_fy25=1620, pat_fy26=1950, pat_fy27=2330, pat_fy28=2800,
    tnw_fy23=8000, tnw_fy24=9200, tnw_fy25=10800,
    dt_fy23="~38,000", dt_fy24="~46,000", debt_fy25="~55,000",
    dr_fy23="4.8x", dr_fy24="5.0x", dr_fy25="5.1x",
    paid_up=111, fte="~6,500+ pan-India",
    anchor_charges_kpi=f'<div class="kpi"><div class="k">Borrowing</div><div class="v num">Rs 46,000 Cr</div><div class="sub">FY24 NBFC{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 1,800 Cr</div><div class="sub">Liquidity</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">CRISIL AAA</div><div class="sub">Stable + A1+</div></div>',
    charges_summary="NBFC borrower; Rs 46,000+ Cr outstanding (TL + NCD + CP + ECB) at FY24",
    charges_strap="Strategic: bilateral NBFC TL + co-lending + Sundaram AMC custody + TVS family-PB.",
    industry_text=(
        f'India NBFC sector ~Rs 50 lakh Cr AUM. Vehicle finance Rs 12-14 lakh Cr; SF is mid-tier (#5-6 by AUM after Bajaj + Chola + STFC + L&T Finance). '
        f'Mutual fund AUM Rs 60+ lakh Cr; Sundaram AMC ~Rs 70-80k Cr (mid-tier). General insurance ~Rs 1.5 lakh Cr; Royal Sundaram ~Rs 4-5k Cr GWP.'
    ),
    drivers=[
        f"<strong>NBFC liability mix optimisation</strong> &mdash; bank TL + NCD + CP + ECB + co-lending; SF is sophisticated borrower.",
        f"<strong>Sundaram AMC growth</strong> &mdash; equity-MF + debt-MF; AUM custody mandate.",
        f"<strong>Sundaram Home Finance disbursement +30%</strong>{ref('990')} &mdash; mortgage demand growth.",
        f"<strong>Royal Sundaram bancassurance partnership</strong> &mdash; cross-sell into IBank retail base.",
        f"<strong>TVS family wealth</strong> &mdash; Iyengar/Srinivasan/Sundaram lineage; multi-gen.",
    ],
    product_rows=[
        ("Bilateral NBFC term-loan", "750&ndash;1,500", "5", "9", "SF NBFC liability mix"),
        ("Co-lending mandate (vehicle + home)", "1,000&ndash;2,500 facility", "4", "7", "PSL-eligible co-origination"),
        ("Direct assignment / securitisation", "300&ndash;800/yr", "2", "3.5", "Asset-pool transfer"),
        ("Sundaram AMC custody mandate", "Rs 70-80k Cr AUM", "1.5", "2.5", "Custody + fund-admin"),
        ("Bancassurance (Royal Sundaram cross-sell)", "Cross-channel", "0.6", "1.2", "IBank retail × RS GI"),
        ("Working-capital + treasury LCR", "200&ndash;400", "0.7", "1.4", "ALM optimisation"),
        ("Salary CASA (6,500+ FTE)", "Rs 15-30 Cr float", "0.6", "1.2", "Pan-India branch + HO"),
        ("PB (TVS family + senior leadership)", "Rs 600-1,200 Cr AUM", "3", "5.5", "Iyengar/Srinivasan/Sundaram + ESOP"),
        ("Family-trust + ESOP advisory", "Multi-gen + senior leadership", "1", "1.8", "TVS-clan ESOP"),
    ],
    wholesale_y3="Rs 12.8-25.4 Cr / yr",
    retail_text="Salary CASA mandate ~6,500 FTE pan-India; Rs 0.6-1.2 Cr/yr.",
    pb_text="TVS family + Sundaram clan + senior leadership ESOP; PB AUM Rs 600-1,200 Cr; Rs 3-5.5 Cr/yr.",
    tasc_text="SF PF + Gratuity + Sundaram Foundation; Rs 200-300 Cr corpus; Rs 0.8-1.2 Cr/yr.",
    retail_total_low="4.4", retail_total_high="7.9",
    consolidated_rows=[
        ("Bilateral TL + co-lending + securitisation", "11", "20"),
        ("AMC custody + bancassurance + WC", "2.8", "5.1"),
        ("Salary + PB + TASC", "4.4", "7.9"),
    ],
    consolidated_total_low="18.2", consolidated_total_high="33.0",
    kmp_text=(
        "<strong>T.T. Srinivasaraghavan</strong> &mdash; Director (long-time Sundaram Finance leader). "
        "<strong>Harsha Viji</strong> &mdash; Managing Director (since 2022; second-generation TVS family). "
        "<strong>A.N. Raju</strong> &mdash; Director. "
        "<strong>S. Ravindran</strong> &mdash; CFO. "
        "Independent Directors include S. Mahalingam, R. Venkatraman, others."
    ),
    ownership_text="Promoter holding 37.2% via SF Holdings + family + cross-holdings; FII 28%; DII 18%; public 16.8%.",
    diligence_news="FY26: AUM growth 25-30% target; Sundaram Home Finance scale; Royal Sundaram bancassurance deepening.",
    dil2="T+14: NBFC borrower diligence (RBI SBR-UL norms); Probe42 + ratings + ALM scrutiny.",
    dil3="T-14: Pre-pitch bilateral TL + co-lending PSL framework + AMC custody pitch + TVS family-PB.",
    playbook_30="Harsha Viji + S. Ravindran meeting; bilateral TL + co-lending concept.",
    playbook_60="Bilateral TL committee; co-lending agreement signed; first securitisation Rs 500 Cr.",
    playbook_90="TL drawn full; co-lending live; AMC custody mandate; Royal Sundaram bancassurance pilot.",
    playbook_180="Securitisation flow Rs 1,000 Cr+; TVS family-PB diagnostic complete.",
    success_metrics=[
        "Bilateral NBFC TL Rs 1,000 Cr + co-lending Rs 1,500 Cr by Q2 FY27",
        "Securitisation flow Rs 800 Cr/yr by Q4 FY27",
        "Y3 wallet Rs 22-42 Cr",
        "TVS family-PB Rs 600+ Cr by Q4 FY28",
    ],
    src_base=990,
    src_parent_body="Sundaram Finance Annual Report FY24 + investor presentations + RBI SBR + TVS Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="sundaramfinance.in &middot; tvs.com &middot; rbi.org.in",
    src_extra=[
        (990, "Sundaram Finance Annual Report FY24 + investor presentations", "sundaramfinance.in &middot; retrieved 28 Apr 2026"),
        (991, "Sundaram Home Finance + Sundaram AMC + Royal Sundaram disclosures", "sundaramhome.in / sundarammutual.com / royalsundaram.in"),
        (992, "NSE/BSE SUNDARMFIN quarterly filings", "nseindia.com / bseindia.com"),
        (993, "CRISIL AAA + A1+ rationale Nov 2024 [verify FY26]", "crisil.com"),
    ],
    footer="Cipher clean; 1,500+ lines; 71-yr TVS NBFC flagship at AUM Rs 43,987 Cr with bilateral TL + co-lending + AMC custody + TVS family-PB.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 71-year arc from TVS-trucks-finance startup to CRISIL AAA TVS NBFC flagship</div>

<h3>03A.1 Founding (1954) &mdash; vehicle-finance for TVS dealers</h3>
<p>Sundaram Finance Limited was incorporated <strong>11 August 1954</strong> in Madras (Chennai) by the Sundaram Iyengar family (TVS founding family){ref("990")}. The original mandate was <strong>hire-purchase + commercial-vehicle finance</strong> for the TVS Iyengar Trucks dealer network across South India. Vehicle finance in the 1950s was an under-served segment, and Sundaram Iyengar saw the opportunity to professionalise it.</p>

<h3>03A.2 The 1960s-1970s &mdash; Public Ltd + listing + South India scale</h3>
<p>Sundaram Finance became a public limited company in <strong>1961</strong> and was listed on Indian stock exchanges in <strong>1972</strong>{ref("990")}. Through the 1970s, SF built South India's leading vehicle-finance franchise &mdash; primarily commercial vehicles (Tata Trucks, Ashok Leyland, TVS Trucks) and small-car finance. The famously conservative + relationship-based credit-decision culture emerged in this period.</p>

<h3>03A.3 The 1980s-1990s &mdash; Diversification beyond vehicle finance</h3>
<p>SF diversified into <strong>leasing</strong>, <strong>hire-purchase finance</strong>, <strong>truck-fleet finance</strong>, and a growing pan-India branch network. By the 1990s it was one of the largest NBFCs in India by AUM (along with HDFC, ICICI, GIC Housing, etc.). The company stayed conservative through the Asian financial crisis, building a reputation for AAA-equivalent asset quality.</p>

<h3>03A.4 The 2000s &mdash; Sundaram AMC + Royal Sundaram + Sundaram Home Finance</h3>
<p>The 2000s brought meaningful diversification into <strong>asset management</strong> (Sundaram Asset Management Co launched 2002 for mutual funds), <strong>general insurance</strong> (Royal Sundaram Alliance Insurance JV with Royal & Sun Alliance UK in 2001 &mdash; later partnered with Mitsui Sumitomo), and <strong>housing finance</strong> (Sundaram Home Finance, formerly Sundaram BNP Paribas Home Finance &mdash; the BNP Paribas JV ended in 2015 with Sundaram taking 100%).</p>

<h3>03A.5 The 2010s-2020s &mdash; CRISIL AAA + Sundaram Finance Holdings demerger</h3>
<p>SF achieved <strong>CRISIL AAA / Stable</strong> &mdash; the highest domestic rating tier &mdash; through the 2010s. In 2017, the holding-company structure was rationalised: <strong>Sundaram Finance Holdings Limited (SFHL)</strong> was carved out as a separate listed entity holding TVS Group cross-investments + finance-services investments; SF became the operating NBFC. AUM grew from Rs 17,000 Cr (FY15) to Rs 43,987 Cr (FY24).</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; AUM scale + co-lending + TVS family-stewardship</h3>
<p>AUM trajectory FY25 Rs 55,000 Cr → FY28 Rs 95,000 Cr (CAGR ~22%). Sundaram Home Finance growing 30% on disbursement (FY25 Rs 6,517 Cr). Sundaram AMC AUM ~Rs 70-80k Cr. The structural wholesale-banking mandate is around: (a) bilateral NBFC TL + co-lending; (b) AMC custody / fund-admin; (c) bancassurance partnership (Royal Sundaram); (d) TVS family-PB. Harsha Viji is MD (second-generation TVS family); T.T. Srinivasaraghavan is non-executive Director.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 71-year arc tells you: (1) SF is the <strong>second-largest TVS-Group platform after TVS Motor</strong> &mdash; an entry into TVS-family-PB; (2) the multi-entity TVS-financial-services ecosystem (SF + Sundaram Home Finance + Sundaram AMC + Royal Sundaram) means a single relationship-bank can win 4+ products; (3) the AAA-rated NBFC funding mandate is structurally cheaper than equity-raise &mdash; SF will keep raising bilateral TL + co-lending + securitisation continuously through the cycle; (4) the <strong>TVS family wealth</strong> (Sundaram + Iyengar + Srinivasan lineages) is one of the most concentrated multi-generation industrial-family wealth pools in India.</p>
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
