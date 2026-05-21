"""Eicher Motors dossier — pilot 161, Royal Enfield + VECV."""
from .base import ref
from ._template import emit

CFG = dict(
    pilot=161, name="Eicher Motors Limited", slug="eicher-motors",
    title="Eicher Motors Limited · Dossier 28 Apr 2026",
    cin="L34102DL1982PLC129877", parent="Lal family (Siddhartha Lal)",
    pad_label="Eicher Motors", pad_sector="Royal Enfield motorcycles / Volvo Eicher CV (VECV) / Flying Flea EV",
    eyebrow_extras="New Delhi HO (RE Chennai mfg) · Listed BSE 505200 / NSE EICHERMOT · Lal family · Volvo JV",
    headline_sub="42-yr Lal-family Eicher; Royal Enfield (250cc-650cc+ motorcycles, 902k units FY25); VECV Volvo JV; Flying Flea EV launching Q1 FY26",
    lede=f'Eicher Motors Limited (CIN L34102DL1982PLC129877){ref("1000")} is the listed Lal-family controlled flagship operating two distinct businesses: <strong>Royal Enfield</strong> (100% subsidiary; middleweight motorcycles 250cc-650cc+) and <strong>VE Commercial Vehicles Limited</strong> (VECV; 50% Eicher + 50% Volvo Group JV; medium + heavy + light commercial vehicles). Listed BSE 505200 / NSE EICHERMOT{ref("1000")}; Lal family promoter; HQ New Delhi; Royal Enfield manufacturing + R&D at Oragadam + Vallam Vadagal (Chennai). Founded 14 October 1982 (evolved from Eicher Goodearth); acquired Royal Enfield (26% stake Feb 1990, majority 60% by 1993). <strong>FY24 consolidated revenue Rs 16,536 Cr</strong>{ref("128")}; EBITDA Rs 4,327 Cr (26.2%, up from 23.8% FY23); PAT Rs 4,001 Cr (+37.4%); total debt Rs 419 Cr (largely VECV); LT debt Rs 200 Cr. Royal Enfield FY25: 902,757 domestic units + 100,136 exports (+29.7% YoY). Subsidiaries: Royal Enfield Motors India; VE Commercial Vehicles (VECV); <strong>Flying Flea</strong> (electric-motorcycle brand &mdash; 1.5 lakh units/yr capacity at Vallam plant; production start Q1 FY26). 2,500 FTE Eicher + RE; 4 manufacturing + 49 marketing offices.',
    headline_low=20, headline_high=38,
    headline_strap="Y3 wallet (Royal Enfield + VECV capex + Flying Flea EV + Lal family-PB)",
    industry_short="Royal Enfield motorcycles / Volvo Eicher CV / Flying Flea EV",
    kpi3='<div class="kpi pos"><div class="k">EBITDA margin</div><div class="v num">26.2%</div><div class="sub">FY24 best-in-class' + ref("128") + '</div></div>',
    kpi4='<div class="kpi pos"><div class="k">PAT growth</div><div class="v num">+37.4%</div><div class="sub">FY24' + ref("128") + '</div></div>',
    three_angles=[
        "<strong>Flying Flea EV capex Rs 800-1,200 Cr</strong> &mdash; Vallam plant 1.5 lakh units/yr capacity; Q1 FY26 production start; sustainability-linked.",
        "<strong>VECV expansion + Brazil + Indonesia + ASEAN exports</strong> &mdash; Pithampur + Bhandara + Hosur capacity; Brazil CKD plant FY25 commissioning; ASEAN-hub strategy.",
        "<strong>Lal family-PB on Siddhartha Lal + multi-gen wealth</strong> &mdash; Eicher's 26% EBITDA margin makes the family one of the highest-net-worth promoter cohorts in Indian auto.",
    ],
    incorp_date="14 Oct 1982 (Royal Enfield acquired 1990)",
    ho_text="3rd Floor, Select City Walk, A-3 District Centre, Saket, New Delhi 110 017",
    group_text=f'Lal family-controlled; Siddhartha Lal as Executive Chairman{ref("1000")}. Operating subsidiaries: <strong>Royal Enfield Motors India Ltd</strong> (100% subsidiary; motorcycles); <strong>VE Commercial Vehicles Limited (VECV)</strong> (50% Eicher + 50% Volvo Group; CV manufacturing); <strong>Flying Flea</strong> (e-motorcycle brand, FY26 production); <strong>PT VECV Automotive Indonesia</strong>. Royal Enfield manufacturing: Oragadam + Vallam Vadagal (Chennai TN). VECV manufacturing: Pithampur (MP) + Bhandara (MH) + Hosur (TN). Brazil CKD plant near completion FY25; ASEAN-hub strategy; Thailand + Colombia + Argentina operations.',
    funding_anchors=[
        f"Listed Lal-family flagship; Siddhartha Lal Executive Chairman{ref('1000')}.",
        "Total debt Rs 419 Cr (largely VECV JV); LT debt Rs 200 Cr; comfortable leverage.",
        "FY24 paid-up Rs 27 Cr; reserves Rs 17,500+ Cr; market cap Rs 128,120 Cr (one of highest book value/share Rs 659).",
        f"Disclosed banking{ref('128')}: SBI + HDFC + Citi + Axis + Deutsche; Volvo-side European bank consortium.",
        "<strong>Diligence item:</strong> Probe42 charge-register on Eicher + RE + VECV + Flying Flea CINs.",
    ],
    toi_fy23=14400, toi_fy24=16536, toi_fy25=18800, toi_fy26=21500, toi_fy27=24500, toi_fy28=28000,
    eb_fy23=3430, eb_fy24=4327, ebitda_fy25=5000, eb_fy26=5810, eb_fy27=6750, eb_fy28=7780,
    mg_fy23="23.8", mg_fy24="26.2", ebitda_pct="26.6", mg_fy26="27.0", mg_fy27="27.5", mg_fy28="27.8",
    pat_fy23=2914, pat_fy24=4001, pat_fy25=4500, pat_fy26=5200, pat_fy27=6050, pat_fy28=7000,
    tnw_fy23=14000, tnw_fy24=17500, tnw_fy25=21000,
    dt_fy23="~410", dt_fy24="~419", debt_fy25="~600",
    dr_fy23="0.03x", dr_fy24="0.02x", dr_fy25="0.03x",
    paid_up=27, fte="~2,500 (Eicher+RE) · ~7,000+ VECV consolidated",
    anchor_charges_kpi=f'<div class="kpi pos"><div class="k">Total debt</div><div class="v num">Rs 419 Cr</div><div class="sub">D/E 0.02x{ref("126")}</div></div>',
    anchor_cash_kpi='<div class="kpi pos"><div class="k">Cash float</div><div class="v num">Rs 12,000+ Cr</div><div class="sub">Treasury (consolidated)</div></div>',
    anchor_rating_kpi='<div class="kpi pos"><div class="k">Rating</div><div class="v num">[diligence]</div><div class="sub">Implied AAA-equivalent</div></div>',
    charges_summary="Conservative leverage Rs 419 Cr; Rs 12,000+ Cr cash; AAA-equivalent",
    charges_strap="Strategic: Flying Flea EV capex anchor + VECV global expansion + Volvo-JV cross-currency + Lal family-PB.",
    industry_text=(
        f'India motorcycle market FY25 ~Rs 1.4-1.5 lakh Cr; CAGR 6-8%. Royal Enfield is the dominant middleweight (250-650cc) brand &mdash; 50%+ of '
        f'>250cc segment. India CV market FY25 ~Rs 3.2-3.5 lakh Cr; VECV ~6-8% market share (#3-4 after Tata Motors + Ashok Leyland). EV-motorcycle '
        f'segment nascent ~Rs 2-3k Cr; CAGR 50-70%. Flying Flea is one of the most-anticipated premium-EV-motorcycle launches.'
    ),
    drivers=[
        f"<strong>Flying Flea EV launch Q1 FY26</strong>{ref('1001')} &mdash; 1.5 lakh units/yr Vallam capacity; premium electric-motorcycle.",
        f"<strong>Royal Enfield 650cc+ premium expansion</strong> &mdash; Hunter, Continental GT, Super Meteor, Shotgun, Bullet 650; Brazil CKD; ASEAN.",
        f"<strong>VECV Pro-X LCV platform</strong> &mdash; Bharat Mobility Expo 2025 launch; EV-first SCV segment.",
        f"<strong>Steel + commodity hedge</strong>{ref('14')} &mdash; raw material; LME hedge.",
        f"<strong>Multi-currency FX</strong> &mdash; Brazil + Thailand + Colombia + Argentina + ASEAN; USD/EUR/BRL/THB.",
    ],
    product_rows=[
        ("Capex TL (Flying Flea EV + VECV expansion)", "500&ndash;1,200", "5", "9", "Sustainability-linked + Volvo-JV"),
        ("CC + WCDL (motorcycle + CV cycle)", "200&ndash;400", "2", "3.5", "Steel + components + RM"),
        ("LC + Trade (capex + Brazil/ASEAN)", "150&ndash;300 revolving", "0.8", "1.6", "Brazil + Thailand + ASEAN capex import"),
        ("Multi-currency FX (USD + EUR + BRL + THB)", "USD 100-300 Mn", "2", "4", "Royal Enfield exports + VECV global"),
        ("Dealer-finance + retail (motorcycle network)", "200&ndash;400", "1.2", "2.4", "RE 1,800+ dealer + retail-loan"),
        ("OEM-anchor SCF (VECV)", "100&ndash;200", "0.7", "1.4", "Component supplier SCF"),
        ("Salary CASA + payroll (2,500 + VECV)", "Rs 15-30 Cr float", "0.6", "1.2", "Multi-plant"),
        ("PB (Lal family + senior leadership)", "Rs 1,000-2,000 Cr AUM", "5", "9", "Multi-gen + Volvo-JV partner"),
        ("TASC (Eicher Foundation + PF)", "Rs 200-400 Cr corpus", "0.8", "1.5", "Foundation"),
    ],
    wholesale_y3="Rs 11.7-22.9 Cr / yr",
    retail_text="Salary CASA + RE dealer network 1,800+ outlets cross-sell; Rs 1.8-3.6 Cr/yr.",
    pb_text="Lal family + Volvo-JV partner + senior leadership ESOP; PB AUM Rs 1,000-2,000 Cr; Rs 5-9 Cr/yr.",
    tasc_text="Eicher PF + Foundation; Rs 200-400 Cr corpus; Rs 0.8-1.5 Cr/yr.",
    retail_total_low="7.6", retail_total_high="14.1",
    consolidated_rows=[
        ("Capex TL (Flying Flea + VECV) + LC + FX", "7.8", "14.6"),
        ("CC + WCDL + dealer + OEM-SCF", "4.7", "8.9"),
        ("Salary + PB + TASC", "7.6", "14.1"),
    ],
    consolidated_total_low="20.1", consolidated_total_high="37.6",
    kmp_text=(
        "<strong>Siddhartha Lal</strong> &mdash; Executive Chairman Eicher (since 2024 succession from MD role; family second-generation). "
        "<strong>B. Govindarajan</strong> &mdash; Managing Director Eicher / Royal Enfield. "
        "<strong>Vinod Aggarwal</strong> &mdash; Vice-Chairman (Non-Executive) + MD &amp; CEO VECV. "
        "<strong>Sandeep Sandilya</strong> &mdash; CFO (estimated). "
        "Independent Directors: Inder Mohan Singh, S. Madhavan, Tejpreet S. Chopra, Arun Vasu, Ira Gupta."
    ),
    ownership_text="Promoter holding [diligence] (Lal-family controlled; Siddhartha Lal personal + family-trust); FII 36%; DII 18%; public ~25%.",
    diligence_news="FY26: Flying Flea EV production launch Q1 FY26; VECV Brazil CKD commissioning; ASEAN-hub strategy execution; PT VECV Automotive Indonesia.",
    dil2="T+14: Probe42 + ratings + Lal family DIN cross-link; VECV consolidation specifics.",
    dil3="T-14: Pre-pitch Flying Flea capex + multi-currency FX desk + Lal family-PB.",
    playbook_30="Siddhartha Lal + B. Govindarajan + Vinod Aggarwal meeting; Flying Flea concept.",
    playbook_60="Capex TL term-sheet; multi-currency FX consolidation; dealer-finance partnership.",
    playbook_90="Capex drawn 25%; FX desk live; Lal family-PB diagnostic.",
    playbook_180="Volvo JV cross-currency mandate; full Eicher group + VECV cross-sell.",
    success_metrics=[
        "Flying Flea capex TL Rs 500 Cr by Q3 FY27",
        "Multi-currency FX book USD 200 Mn by Q2 FY27",
        "Y3 wallet Rs 20-38 Cr",
        "Lal family-PB Rs 1,000+ Cr by Q4 FY28",
    ],
    src_base=1000,
    src_parent_body="Eicher Motors Integrated Annual Report 2024-25 + investor relations + Volvo Group + NSE/BSE filings (28 Apr 2026).",
    src_parent_url="eicher.in &middot; royalenfield.com &middot; vecv.in &middot; nseindia.com",
    src_extra=[
        (1000, "Eicher Motors Integrated Annual Report 2024-25 + investor relations", "eicher.in &middot; retrieved 28 Apr 2026"),
        (1001, "Flying Flea EV brand announcement + Vallam capacity", "Eicher / Royal Enfield press releases 2024-2025"),
        (1002, "NSE/BSE EICHERMOT quarterly filings", "nseindia.com / bseindia.com"),
        (1003, "VECV Brazil CKD + ASEAN-hub strategy", "VECV press releases"),
    ],
    footer="Cipher clean; 1,500+ lines; Lal-family Eicher with Royal Enfield + VECV (Volvo JV) + Flying Flea EV; 26% EBITDA margin auto franchise.",
)


HISTORY_BLOCK_HTML = """
<section id="history"><div class="subhead">03A &middot; Company history &mdash; the 42-year arc from Eicher Goodearth to Royal Enfield iconic-brand revival + VECV Volvo JV</div>

<h3>03A.1 Origin &mdash; Eicher Goodearth (1948-1982)</h3>
<p>The Eicher name traces to 1948 when the Lal family established Goodearth Tractors in Faridabad, distributing German Eicher tractors. By the 1970s the family had built a tractor manufacturing presence under the Eicher Tractors brand. <strong>Eicher Motors Limited</strong> was incorporated <strong>14 October 1982</strong>{ref("1000")} as a more diversified automotive holding entity.</p>

<h3>03A.2 Royal Enfield acquisition (1990-1993) &mdash; the inflection</h3>
<p>The single most important moment in Eicher's history. <strong>Royal Enfield</strong>, a 1901-British motorcycle brand that had been manufacturing in Madras since 1955 (originally for the Indian Army), was acquired by Eicher: <strong>26% stake in February 1990</strong>, majority <strong>60% by 1993</strong>{ref("1000")}, and 100% subsidiary status thereafter. At the time, Royal Enfield's iconic Bullet 350 was a niche cult bike with declining volumes.</p>

<h3>03A.3 The 2000s &mdash; Siddhartha Lal joins; Royal Enfield revival</h3>
<p>In 2000-2004 <strong>Siddhartha Lal</strong> (then in his early 30s) took operational control of Royal Enfield as CEO. He drove a fundamental quality + design + manufacturing-process revival. The Classic 350 launched 2009 became iconic. The Oragadam + Vallam Vadagal (Chennai) plants modernised. By the early 2010s Royal Enfield was selling 200,000 units/yr; by 2014 it had crossed 300,000 units.</p>

<h3>03A.4 The 2010s &mdash; Volvo JV (VECV) + 650cc twin platform + global expansion</h3>
<p>In 2008 Eicher and Volvo Group signed the <strong>VE Commercial Vehicles JV</strong> &mdash; 50:50 partnership in medium + heavy + light commercial vehicles in India. Pithampur (MP) + Bhandara (MH) + Hosur (TN) plants. Through the 2010s, Royal Enfield launched the 650cc twin platform (Continental GT 650, Interceptor 650) &mdash; opening up Western markets. Royal Enfield exports grew to 100+ countries.</p>

<h3>03A.5 The 2020-2024 surge &mdash; record sales + 26% EBITDA + Flying Flea announce</h3>
<p>FY24 was a structural inflection: revenue Rs 16,536 Cr; EBITDA Rs 4,327 Cr at <strong>26.2% margin</strong> (best-in-class globally for an auto OEM); PAT Rs 4,001 Cr +37.4%. Royal Enfield FY25 hit 902,757 domestic + 100,136 export units (+29.7%). The <strong>Flying Flea electric-motorcycle</strong> brand was announced{ref("1001")} for Q1 FY26 production start at the Vallam plant (1.5 lakh units/yr capacity). Brazil CKD plant FY25 commissioning. PT VECV Automotive Indonesia incorporated.</p>

<h3>03A.6 Next 36 months (FY26-FY29) &mdash; Flying Flea ramp + VECV global + Lal family transition</h3>
<p>FY24 Rs 16,536 Cr; analyst-est FY28 Rs 28,000 Cr (CAGR ~14%). FY26 capex Rs 1,200 Cr planned. Flying Flea production ramp-up + Royal Enfield 750cc+ next-platform + VECV Pro-X LCV platform + ASEAN expansion. Leadership transition: <strong>Siddhartha Lal &rarr; Executive Chairman</strong>; <strong>Vinod Aggarwal &rarr; VC (Non-Executive) + VECV MD &amp; CEO</strong>; B. Govindarajan continues as MD Eicher / Royal Enfield.</p>

<h3>03A.7 Why this matters for the IBank pitch</h3>
<p>The 42-year arc tells you: (1) Siddhartha Lal is a <strong>builder + brand-architect</strong> &mdash; the Royal Enfield revival is one of Indian industry's most successful brand-turnarounds; (2) the 26% EBITDA margin makes Eicher one of the highest-quality auto franchises globally &mdash; cash-positive Rs 12,000+ Cr; (3) the <strong>Volvo JV (VECV)</strong> is a sophisticated cross-currency banking opportunity rare in Indian banking; (4) the Lal family wealth is concentrated, multi-generation, and largely uninstitutionalised; (5) Flying Flea + VECV capex + ASEAN/Brazil expansion demand multi-currency FX desk + capex-import LC + sustainability-linked TL.</p>
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
