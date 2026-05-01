"""Hexaware Technologies dossier — pilot 168, Carlyle PE-backed IT services."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=168, name="Hexaware Technologies Limited", slug="hexaware-technologies",
    title="Hexaware Technologies Limited · Dossier 28 Apr 2026",
    cin="L72900MH1992PLC069662", parent="The Carlyle Group (~79% post-2025 IPO)",
    pad_label="Hexaware Technologies", pad_sector="IT Services / Digital Transformation / Cloud / Data & Analytics / Automation",
    eyebrow_extras="Mumbai/Chennai dual HQ · Listed BSE+NSE HEXT (relisted 2025) · Carlyle PE 79% · 33,844 FTE 30+ countries",
    headline_sub="Re-listed 2025 IT services platform; Carlyle PE-controlled; CY25 revenue USD 1,537 Mn (+7.6% USD / +12.2% INR); 33,844 FTE",
    lede=f'Hexaware Technologies Limited (CIN L72900MH1992PLC069662){ref("1035")} is a global IT services + digital-transformation + cloud + data analytics company. Founded 1992; acquired by <strong>The Carlyle Group</strong> (US PE) in 2021 for $3 Bn enterprise value; <strong>relisted on BSE + NSE in 2025</strong> (ticker HEXT){ref("1035")} with Carlyle retaining ~79% post-IPO. Dual HQ Mumbai + Chennai; major delivery centres in India + USA + Philippines + Europe. <strong>CY25 revenue USD 1,537.4 Mn (~Rs 12,800 Cr; +7.6% YoY USD / +12.2% INR)</strong>{ref("128")}; CY25 EBITDA margin 17.1% (+122 bps YoY); CY25 PAT INR 13,683 Mn (~Rs 1,370 Cr; +16.6% YoY). 33,844 FTE in 30+ countries (FY25). Operating segments: <strong>Digital transformation</strong>; <strong>Cloud migration</strong>; <strong>Data &amp; Analytics</strong>; <strong>Automation</strong>; <strong>Testing</strong>. Customers: Healthcare + Financial Services + Retail + Telecom majors globally. Carlyle Group nominees on Board: Michael W. Bender (Chairman) + Patrick McCarter + Sandra Horbach + Kapil Modi.',
    headline_low=18, headline_high=34,
    headline_strap="Y3 wallet (multi-currency FX + workforce CASA + Carlyle PE relationship)",
    industry_short="IT Services / Digital Transformation / Cloud / Data Analytics",
    kpi3='<div class="kpi pos"><div class="k">CY25 revenue</div><div class="v num">USD 1,537 Mn</div><div class="sub">+12.2% INR' + ref("128") + '</div></div>',
    kpi4='<div class="kpi"><div class="k">PE Owner</div><div class="v num">Carlyle 79%</div><div class="sub">Post-2025 IPO' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Multi-currency FX desk (USD/EUR/GBP)</strong> &mdash; 75%+ international revenue; consolidated forex Rs 8,000-10,000 Cr/yr.",
        "<strong>33,844-FTE workforce CASA + senior leadership ESOP</strong> &mdash; pan-India employee CASA mandate at scale; senior leadership ESOP-equivalent post-2025 IPO.",
        "<strong>Carlyle Group PE relationship + M&amp;A advisory</strong> &mdash; ongoing M&amp;A pipeline; cross-border banking + investment-banking advisory mandate.",
    ],
    incorp_date="04 Mar 1992",
    ho_text="Millennium Business Park, Mahape, Navi Mumbai 400 710 (Mumbai); Chennai delivery centres",
    group_text=f'Carlyle PE-controlled (~79% post-2025 IPO){ref("1035")}. Operating: India delivery centres at Mumbai + Bangalore + Pune + Hyderabad + Chennai; USA delivery + commercial offices; Philippines BPO + delivery; UK + Europe presence; Latin America offices. Recent M&A: multiple delivery + capability acquisitions 2024-25.',
    funding_anchors=[
        f"Listed Carlyle PE-controlled IT-services platform; Carlyle ~79%{ref('1035')}.",
        "Healthy operating cash; M&A-driven growth strategy.",
        "Post-2025 IPO capital structure under reconfiguration.",
        f"Disclosed banking{ref('128')}: Citi + JPMorgan + DBS (Carlyle global relationships); SBI + HDFC (domestic).",
        "<strong>Diligence item:</strong> Probe42 charge-register; Carlyle India + cross-border M&A financing structure.",
    ],
    toi_fy23=10044, toi_fy24=11400, toi_fy25=12800, toi_fy26=14500, toi_fy27=16400, toi_fy28=18500,
    eb_fy23=1700, eb_fy24=1900, ebitda_fy25=2190, eb_fy26=2540, eb_fy27=2950, eb_fy28=3420,
    mg_fy23="16.9", mg_fy24="16.7", ebitda_pct="17.1", mg_fy26="17.5", mg_fy27="18.0", mg_fy28="18.5",
    pat_fy23=1100, pat_fy24=1200, pat_fy25=1370, pat_fy26=1620, pat_fy27=1900, pat_fy28=2200,
    tnw_fy23=4000, tnw_fy24=4500, tnw_fy25=5200,
    dt_fy23="~600", dt_fy24="~500", debt_fy25="~700",
    dr_fy23="0.15x", dr_fy24="0.11x", dr_fy25="0.13x",
    paid_up=607, fte="~33,844 globally",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Total debt</div><div class="v num">Rs ~500 Cr</div><div class="sub">Conservative leverage{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 1,200 Cr</div><div class="sub">Treasury</div></div>',
    anchor_rating_kpi='<div class="kpi"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">Probe42 follow-up</div></div>',
    charges_summary="Conservative leverage Rs ~500 Cr; cash Rs 1,200 Cr; post-IPO 2025",
    charges_strap="Strategic: multi-currency FX desk + workforce CASA mandate at scale + Carlyle M&A advisory + cross-border IB.",
    industry_text=(
        f'Global IT services market FY25 ~USD 1.4 Tn; CAGR 7-9%. Indian IT services exports ~USD 200 Bn. Hexaware competes with TCS + Infosys + Wipro + HCLTech '
        f'(tier-1) and LTI Mindtree + Mphasis + Coforge + Persistent + Birlasoft (tier-2). PE-backed IT-services peers: Mphasis (Blackstone), Mindtree (now LTI Mindtree).'
    ),
    drivers=[
        f"<strong>USD/EUR/GBP appreciation cycle</strong> &mdash; 75%+ international revenue; FX-margin sensitive.",
        f"<strong>M&amp;A-driven growth</strong>{ref('1035')} &mdash; Carlyle continues capability + delivery acquisitions.",
        f"<strong>AI/automation product-mix shift</strong> &mdash; pyramid restructure + AI-driven productivity.",
        f"<strong>USA H-1B / immigration policy</strong>{ref('6')} &mdash; onshore margin sensitivity.",
        f"<strong>Healthcare + BFSI + retail demand</strong> &mdash; vertical-specific demand cycles.",
    ],
    product_rows=[
        ("Multi-currency FX desk (USD + EUR + GBP)", "USD 700-1,200 Mn notional", "5", "9", "75%+ international revenue"),
        ("M&amp;A acquisition-financing TL", "300&ndash;800", "2", "4", "Carlyle ongoing M&amp;A pipeline"),
        ("WC + AR factoring (multi-currency receivable)", "200&ndash;400", "1", "2", "T&M + fixed-bid customer paper"),
        ("Salary CASA + payroll (33,844 FTE)", "Rs 80-150 Cr float", "3", "5", "Pan-India workforce + global"),
        ("Senior leadership PB + post-IPO ESOP", "Rs 800-1,500 Cr AUM", "4", "7", "Senior + middle leadership post-IPO"),
        ("Carlyle Group treasury + advisory mandate", "Cross-currency", "1", "2.5", "PE-owner relationship"),
        ("Treasury sweep (cash management)", "Rs 1,200+ Cr float", "0.6", "1.2", "Multi-currency cash"),
        ("LC + Trade (capex)", "50&ndash;100 revolving", "0.3", "0.5", "Office + IT capex"),
        ("TASC (Hexaware Foundation + PF)", "Rs 80-150 Cr corpus", "0.4", "0.7", "PF + Foundation"),
    ],
    wholesale_y3="Rs 9.3-19 Cr / yr",
    retail_text="Salary CASA mandate ~33,844 FTE pan-India + global; Rs 3-5 Cr/yr.",
    pb_text="Senior leadership + post-IPO ESOP; PB AUM Rs 800-1,500 Cr; Rs 4-7 Cr/yr.",
    tasc_text="HEXT PF + Foundation; Rs 80-150 Cr corpus; Rs 0.4-0.7 Cr/yr.",
    retail_total_low="7.4", retail_total_high="12.7",
    consolidated_rows=[
        ("FX + M&A TL + WC factoring", "8", "15"),
        ("Carlyle treasury + advisory + sweep", "1.6", "3.7"),
        ("Salary + senior PB + TASC", "7.4", "12.7"),
    ],
    consolidated_total_low="17.0", consolidated_total_high="31.4",
    kmp_text=(
        "<strong>Michael W. Bender</strong> &mdash; Chairman (Carlyle nominee). "
        "<strong>Patrick McCarter</strong> &mdash; Director (Carlyle MD). "
        "<strong>Sandra Horbach</strong> &mdash; Director (Carlyle MD). "
        "<strong>Kapil Modi</strong> &mdash; Director (Carlyle MD). "
        "<strong>R. Srikrishna (Srik)</strong> &mdash; CEO (long-time Hexaware operating leader). "
        "<strong>Vikash Jain</strong> &mdash; CFO."
    ),
    ownership_text="Promoter holding ~79% (The Carlyle Group via Carlyle Asia + India funds); FII 12%; DII 6%; public 3%.",
    diligence_news="FY26: Continued M&A; AI/cloud capability ramp; margin expansion target; ESOP cycles for senior leadership.",
    dil2="T+14: Probe42 + Carlyle India entity structure + cross-border M&A book.",
    dil3="T-14: Pre-pitch FX desk consolidation + M&A financing framework + workforce CASA.",
    playbook_30="Srik / Vikash Jain meeting; FX desk + workforce CASA concept.",
    playbook_60="FX consolidation + first M&A advisory deal + workforce CASA mandate.",
    playbook_90="FX desk live; CASA mandate Q1; senior leadership PB diagnostic.",
    playbook_180="Full Hexaware ecosystem + Carlyle India cross-portfolio mandate.",
    success_metrics=[
        "FX desk USD 700 Mn by Q2 FY27",
        "Workforce CASA mandate 22,000+ FTE by Q4 FY27",
        "Y3 wallet Rs 18-34 Cr",
    ],
    src_base=1035,
    src_parent_body="Hexaware Technologies CY24/CY25 disclosures + Carlyle Group portfolio + 2025 IPO RHP + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="hexaware.com &middot; carlyle.com &middot; nseindia.com",
    src_extra=[
        (1035, "Hexaware Technologies CY24/CY25 disclosures + Carlyle Group + 2025 IPO RHP", "hexaware.com &middot; retrieved 28 Apr 2026"),
        (1036, "Carlyle Group portfolio + Hexaware acquisition 2021 + 2025 IPO", "carlyle.com press releases"),
        (1037, "NSE/BSE HEXT relisting 2025 quarterly filings", "nseindia.com / bseindia.com"),
        (1038, "Hexaware M&A pipeline 2024-25", "Hexaware press releases"),
    ],
    footer="Cipher clean; 1,500+ lines; Carlyle PE-controlled IT-services platform; FX desk + workforce CASA + M&A advisory + Carlyle India cross-portfolio.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 33-year arc from APTECH spin-off to Carlyle PE platform + 2025 re-listing</div>

<h3>03A.1 Founding (1992) &mdash; APTECH Information Technology spin-off</h3>
<p>Hexaware Technologies Limited was incorporated <strong>4 March 1992</strong>{ref("1035")} as a spin-off from APTECH Limited\'s IT services division (founded by Atul Nishar). The original mandate was IT services for Indian + international enterprises &mdash; offshore software development + maintenance.</p>

<h3>03A.2 The 1990s-2000s &mdash; PeopleSoft/Oracle ERP focus</h3>
<p>Through the 1990s-2000s Hexaware built a deep specialisation in PeopleSoft (later Oracle) ERP implementation + maintenance + upgrade services for global enterprise customers. The company stayed at tier-2 IT-services scale (~USD 200-400 Mn revenue) but built strong vertical depth in Healthcare + Financial Services + Travel & Transportation + Manufacturing.</p>

<h3>03A.3 The 2010s &mdash; Baring Asia + automation pivot + IPO 2014</h3>
<p>Baring Private Equity Asia acquired control of Hexaware from Atul Nishar in 2013 (~$420M deal). Hexaware listed on BSE / NSE in 2014. Through 2014-2020, the company pivoted aggressively into <strong>automation</strong> (Hexaware Robotic Automation Platform), <strong>cloud migration</strong> (AWS / Azure), and <strong>digital transformation</strong>. Revenue grew from ~Rs 2,500 Cr to ~Rs 7,000 Cr.</p>

<h3>03A.4 The 2021 Carlyle acquisition &mdash; the inflection</h3>
<p>In <strong>2021 The Carlyle Group acquired Hexaware Technologies for $3 Bn enterprise value</strong>{ref("1036")} (one of the largest PE buyouts in Indian IT services). Carlyle delisted Hexaware (Sep 2020 announce; Oct 2020 close). Under Carlyle ownership 2021-2024, Hexaware aggressively pursued M&A (capability + delivery acquisitions), AI/cloud capability build-up, and margin expansion.</p>

<h3>03A.5 The 2025 re-listing &mdash; back on BSE+NSE</h3>
<p>In <strong>2025 Carlyle re-listed Hexaware on BSE+NSE (ticker HEXT)</strong>{ref("1037")} via partial-exit IPO &mdash; Carlyle retained ~79% post-IPO. The relisting brought ~Rs 4,000-6,000 Cr capital raise (estimate; subject to RHP confirmation). Hexaware emerged as one of India\'s largest PE-backed IT-services platforms.</p>

<h3>03A.6 The CY25 results &mdash; revenue USD 1.5 Bn + margin expansion + 33,844 FTE</h3>
<p>CY25 revenue USD 1,537.4 Mn (+7.6% USD / +12.2% INR){ref("1035")}; EBITDA margin 17.1% (+122 bps YoY); PAT Rs 1,370 Cr (+16.6%). 33,844 FTE in 30+ countries. Strong M&A pipeline; AI/cloud capability scale-up.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 33-year arc tells you: (1) Hexaware is a <strong>PE-controlled IT-services platform</strong> &mdash; M&A + capability acquisitions are continuous; (2) the <strong>Carlyle relationship</strong> opens entry to broader Carlyle India portfolio (Carlyle has Indian investments in PNB Housing + Yes Bank + Atotech + others); (3) the <strong>33,844-FTE workforce</strong> is one of the largest tier-2 IT-services employee bases &mdash; salary CASA at scale; (4) the <strong>2025 IPO</strong> created senior-leadership ESOP wealth that needs PB structuring; (5) <strong>multi-currency FX</strong> at USD 700-1,200 Mn notional is significant.</p>
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
