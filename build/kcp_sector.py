"""KCP Limited bespoke sector deep-dive (pilot 172) using rich-sector framework."""
from ._rich_sector import build_one

SPEC = {
    "pilot": 172, "name": "The KCP Limited",
    "dossier_slug": "kcp-limited", "cluster_label": "Cement / Sugar / Heavy Engineering / Hospitality / Vietnam Operations",
    "headline_low": 14, "headline_high": 26, "y3_sub": "Multi-business + Vietnam FX + family-PB",
    "play_strap": "Anchor cement capex · run Vietnam multi-currency FX · capture FIVES France EPC export factoring · Velagapudi family-PB",
    "tldr_lede": "The KCP Limited is the listed Velagapudi-family multi-business conglomerate (Chennai HO; BSE 590066/NSE KCP; promoter holding 44.25%); founded 1941; FY24 revenue Rs 2,846 Cr; FY25 Rs 2,529 Cr; networth Rs 1,533 Cr; ROCE 13%. Five operating businesses: cement (2.2 MTPA at Macherla + Mukthyala AP) + sugar + KCP Vietnam Industries (Phu Yen + Son Hoa plants) + heavy engineering (Steel Foundry near Chennai port + FIVES CAIL-KCP JV with Fives Group France for turnkey EPC) + hospitality (Mercure Hyderabad). The play is anchor cement capex Rs 200-400 Cr (Macherla + Mukthyala refresh + WHRS + AFR) on the UltraTech-consolidation urgency, run the Vietnam multi-currency FX desk (VND + USD + INR), capture FIVES CAIL-KCP EPC export USD-receivable factoring, and build family-PB on the Velagapudi-family wealth.",
    "kpi_b_label": "Cement capacity", "kpi_b_val": "2.2 MTPA", "kpi_b_sub": "Macherla + Mukthyala AP",
    "kpi_c_label": "FY24 revenue", "kpi_c_val": "Rs 2,846 Cr", "kpi_c_sub": "+26% YoY",
    "kpi_d_label": "Vietnam ops", "kpi_d_val": "2 plants", "kpi_d_sub": "Phu Yen + Son Hoa",
    "walking_in": "\"Mr. Velagapudi / Ms. Kavitha — KCP\'s Vietnam operations + FIVES CAIL-KCP EPC are unique in Indian cement-sugar industry. We want to be the multi-currency FX bank for Vietnam, capture the FIVES France EPC export-receivable factoring, and anchor the Macherla-Mukthyala cement-capex window. Three structural ideas in 30 minutes.\"",
    "history_strap": "the 84-year arc from 1941 Andhra industrial-family enterprise to multi-business listed conglomerate with Vietnam operations",
    "history": [
        ("Founding (1941) — Krishna Cement Pvt Ltd", "The KCP Limited was incorporated 22 July 1941 in Madras (Chennai) by the Velagapudi family of industrialists from coastal Andhra Pradesh. The original mandate was cement manufacturing (originally as Krishna Cement Private Limited; \"KCP\" derives from this lineage). Pre-Independence cement franchise."),
        ("The 1950s-1970s — Cement scale + heavy engineering diversification", "Built one of South India\'s leading cement franchises alongside India Cements + Madras Cements (now Ramco Cements). Diversified into heavy engineering — integrated Steel Foundry + heavy-equipment fabrication facility near Chennai port for post-Independence Indian engineering economy."),
        ("The 1980s-1990s — Sugar diversification + V.L. Dutt era", "Under leadership of V.L. Dutt (third-generation Velagapudi family) diversified into sugar manufacturing — initially in Andhra Pradesh, then through KCP Sugar & Industries Corporation (separately listed BSE 533166 / NSE KCPSUGIND). Velagapudi family thus operates dual listed sugar entities."),
        ("Vietnam expansion (early 2000s) — KCP Vietnam Industries", "One of Indian sugar industry\'s most distinctive moves — setting up KCP Vietnam Industries Limited with two sugar plants: Phu Yen + Son Hoa in Vietnam. Made KCP one of the very few Indian sugar manufacturers with significant overseas manufacturing capacity. Vietnam operations have grown into meaningful contributor to KCP consolidated revenue + EBITDA."),
        ("The FIVES CAIL-KCP JV (2010s) — turnkey EPC", "Entered 50:50 joint venture with Fives Group (France) as FIVES CAIL-KCP Limited — offering turnkey sugar + power plant EPC for global customers (Africa, South America, SE Asia). Combined Fives Group\'s 200-year French engineering heritage with KCP\'s heavy-engineering manufacturing capability."),
        ("The 2020-2024 inflection — revenue scale + margin expansion", "FY22 revenue Rs 2,108 Cr; FY23 Rs 2,254 Cr; FY24 Rs 2,846 Cr (with PAT Rs 280 Cr +208% YoY); FY25 Rs 2,529 Cr; FY25 PAT Rs 253 Cr. EBITDA margin recovered from 13.3% FY23 to 17.9% FY24. ROCE 13% FY25. Multi-business multi-bank consortium ~Rs 480 Cr (FY24)."),
        ("Why this matters for the IBank pitch", "(1) Genuine multi-business conglomerate — five distinct operating businesses under one listed entity. (2) Vietnam operations + FIVES France JV = structural multi-currency banking needs unique in Indian cement-sugar industry. (3) UltraTech-India Cements consolidation creates urgency for cement-segment capex. (4) Velagapudi family-PB opportunity (V.L. Dutt patriarch + V. Kavitha Dutt fourth-generation Joint MD) largely uninstitutionalised. (5) FIVES CAIL-KCP EPC export brings USD receivable factoring + customer-LC + advance-BG opportunities."),
    ],
    "kmp": [
        ("V.L. Dutt — Chairman Emeritus / Director", "Third-generation Velagapudi family patriarch; long-time KCP architect since 1960s. Strategic focus: family-stewardship + multi-business portfolio governance + sugar industry leadership. Decision style: family-first; respects bankers who understand multi-business conglomerates and bring international banking capability. RM angle: introduction via senior MD-level."),
        ("V. Kavitha Dutt — Joint Managing Director", "Fourth-generation; daughter of V.L. Dutt; operational leader with strong cement + sugar industry engagement. Decision style: execution + cost-discipline focused; growth-oriented; will deep-test bank\'s multi-currency + EPC export capability. RM angle: primary banking counterparty; bring multi-currency FX dealer + cement capex underwriter."),
        ("CFO + Senior Leadership", "[diligence: name + DIN cross-link]. Day-to-day banking counterparty; multi-business multi-bank consortium relationship lead. RM angle: monthly meetings; bring treasury head + cement-cluster lead + sugar-cluster lead."),
        ("Subsidiaries / Operating structure", "<strong>KCP Vietnam Industries Limited</strong> (Vietnam sugar; Phu Yen + Son Hoa plants); <strong>FIVES CAIL-KCP Limited</strong> (50:50 JV with Fives Group France for turnkey sugar/power EPC); <strong>KCP Cement</strong> (Macherla + Mukthyala plants AP); <strong>KCP Heavy Engineering</strong> (Steel Foundry + heavy-equipment fabrication near Chennai port); <strong>KCP Hotels &amp; Hospitality</strong> (Mercure Hyderabad KCP). Sister concern: <strong>KCP Sugar &amp; Industries Corporation</strong> separately listed BSE 533166 / NSE KCPSUGIND."),
    ],
}

SPEC.update({
    "valuechain_strap": "5-business multi-segment cluster + Vietnam ops + FIVES France EPC",
    "valuechain_text": "KCP operates across five distinct value-chains under one listed entity. (1) <strong>Cement</strong>: limestone + coal + fly-ash &rarr; clinker &rarr; cement (OPC + PPC + Composite) &rarr; AP/TN/Karnataka markets. (2) <strong>Sugar (India + Vietnam)</strong>: cane procurement (TN-SAP / AP-SAP / Vietnam) &rarr; mill &rarr; sugar + molasses + bagasse + cogen power. (3) <strong>Heavy Engineering</strong>: steel + casting + raw materials &rarr; Steel Foundry + Build-to-Order heavy-equipment fabrication &rarr; B2B + Indian railways + capital-goods customers. (4) <strong>FIVES CAIL-KCP EPC</strong>: design + engineering + project management &rarr; turnkey sugar + power plants &rarr; Africa + South America + SE Asia customers. (5) <strong>Hospitality</strong>: Mercure Hyderabad KCP hotel + group ventures.",
    "valuechain_table": "<table><thead><tr><th>Segment</th><th>Pricing power</th><th>WC + financing impact</th><th>Bank product</th></tr></thead><tbody><tr><td>Cement (Macherla + Mukthyala AP, 2.2 MTPA)</td><td>Limited; pricing-cycle dependent</td><td>30-60 day; coal + pet-coke + limestone cycle</td><td>Capex TL + WCDL + LME-coal hedge</td></tr><tr><td>Sugar India (AP/TN cane)</td><td>Limited; SAP regulated; ethanol off-take strong</td><td>Bimodal; cane payment 14-day; sugar realisation 60-90 day</td><td>Cane-procurement BG + WCDL + OMC ethanol factoring</td></tr><tr><td>Sugar Vietnam (Phu Yen + Son Hoa)</td><td>Strong; Vietnam VND market access; export to ASEAN</td><td>Vietnam VND-denominated cycle; cross-currency exposure</td><td>VND/USD/INR FX desk + multi-currency LC + WCDL</td></tr><tr><td>Heavy Engineering (Steel Foundry near Chennai)</td><td>Strong; Build-to-Order; specialty steel + capital goods</td><td>Long WC cycle; project receivables 60-180 day</td><td>WCDL + project-LC + customer-LC</td></tr><tr><td>FIVES CAIL-KCP EPC export</td><td>Strong; turnkey + IP; Africa/SAm/SE Asia customers</td><td>Long-cycle; advance + retention; USD denominated</td><td>BG (advance + performance + retention) + USD LC + export-receivable factoring</td></tr><tr><td>Hospitality (Mercure Hyderabad)</td><td>Limited; hotel-cycle dependent</td><td>Daily F&B + room cycle; modest WC</td><td>WCDL + capex TL on refresh</td></tr></tbody></table>",
    "driver_fs_intro": "Sized to FY24 baseline (TOI ~Rs 2,846 Cr; EBITDA ~Rs 510 Cr; promoter 44.25%; multi-bank Rs 480 Cr). FY25 modest contraction (Rs 2,529 Cr) reflects cement-pricing cycle + Vietnam-translation FX impact.",
    "driver_fs": [
        ("Cement industry consolidation (UltraTech-India Cements Sep 2024)", "Smaller cement players need cost-discipline + capex urgency; KCP Macherla + Mukthyala face South India competitive intensity", "<strong>Cement capex TL Rs 200-400 Cr + WHRS + AFR financing</strong>"),
        ("E20 ethanol mandate FY27", "Sugar mills reallocate B-heavy molasses to ethanol; AP + TN distillery scale-up", "Distillery capex TL + OMC ethanol receivable factoring"),
        ("Vietnam VND/USD/INR FX (KCP Vietnam Industries)", "Phu Yen + Son Hoa plants Rs 600-800 Cr revenue contribution; cross-currency translation; ASEAN export receivable", "<strong>Multi-currency FX desk (VND + USD + INR) + Vietnam multi-currency LC</strong>"),
        ("FIVES CAIL-KCP EPC export orderbook", "Turnkey sugar + power EPC for Africa + South America + SE Asia; USD-receivable; advance + retention BG", "<strong>USD receivable factoring + advance/retention BG framework</strong>"),
        ("LME-coal + pet-coke + cement raw material", "30-40% of cement COGS; commodity hedge", "Commodity-WCDL + IRS structures"),
        ("Indian sugar SAP / cane price (TN+AP)", "Statutory 14-day cane payment cycle; WC pressure peak Nov-Feb", "Cane-procurement BG (Min Consumer Affairs) + WCDL"),
        ("Steel Foundry + heavy engineering project-cycle", "Build-to-order; long WC; project LC + retention", "Project-LC + customer-LC + WCDL"),
        ("EU CBAM (cement on Phase-1 list)", "Limited direct exposure but auto-OEM scope-3 reporting", "Sustainability-linked covenant pricing"),
        ("RBI repo cycle", "Cement + sugar WC benchmarked to MCLR; June MPC cut consensus", "WCDL + IRS lock"),
        ("Velagapudi family transition (V.L. Dutt → next-gen)", "Family-stewardship + multi-gen wealth structuring", "PB AUM mandate + family-trust"),
        ("Hotel-segment revenue (Mercure Hyderabad cycle)", "Discretionary travel + business-travel dependent", "WCDL + capex TL on refresh"),
    ],
    "products": [
        ("Cement capex TL (Macherla + Mukthyala refresh)", "Sustainability-linked: AFR + WHRS + EV-mix step-down", "Rs 200-400 Cr", "MCLR + 80-110 bps", "Rs 1.5-3 Cr/yr"),
        ("Vietnam-operations capex TL + multi-currency LC", "VND + USD + INR cross-currency", "Rs 150-300 Cr / VND equiv", "MCLR/Vietnam-prime mix", "Rs 1-2 Cr/yr"),
        ("CC + WCDL (cement + sugar cycle)", "Coal + cane raw material; bimodal sugar", "Rs 200-400 Cr", "MCLR + 60-90 bps", "Rs 1.5-2.5 Cr/yr"),
        ("BG (cement + sugar + heavy engineering EPC)", "Cane-procurement + EPC advance + retention + customer-LC", "Rs 150-300 Cr", "0.30-0.45% fee", "Rs 1-1.8 Cr/yr"),
        ("Multi-currency FX (USD + EUR + VND)", "Vietnam ops + EPC export + Fives France", "USD/EUR/VND 50-100 Mn notional", "Spread 5-15 bps", "Rs 1-2 Cr/yr"),
        ("FIVES CAIL-KCP EPC export factoring (USD)", "Africa + SAm + SE Asia customer-LC", "Rs 80-150 Cr", "MCLR + 50-80 bps", "Rs 0.5-1.0 Cr/yr"),
        ("LC + Trade (Vietnam + capex + coal)", "Coal + machinery + Vietnam consumables", "Rs 100-200 Cr revolving", "0.30-0.45% fee", "Rs 0.7-1.4 Cr/yr"),
        ("Salary CASA + payroll (3,500 FTE consolidated)", "Multi-plant + Vietnam", "Rs 10-20 Cr float", "0%", "Rs 0.5-0.9 Cr/yr"),
        ("PB (Velagapudi family + senior leadership)", "V.L. Dutt + V. Kavitha + family + senior leadership", "Rs 200-400 Cr AUM", "50-80 bps", "Rs 1.2-2.2 Cr/yr"),
        ("Hotel-segment WC + capex (Mercure Hyderabad)", "Hotel cycle + refresh", "Rs 30-60 Cr", "MCLR + 70-100 bps", "Rs 0.2-0.4 Cr/yr"),
    ],
    "product_extra": "<h3>F.1 Y3 wallet build-up</h3><div class='card'><ul><li>Wholesale + capex (cement + Vietnam): Rs 2.5-5 Cr</li><li>Trade + BG + LC + FX: Rs 3.5-7.6 Cr</li><li>EPC export factoring + group treasury: Rs 1.5-3 Cr</li><li>Retail + PB + TASC: Rs 2.1-3.8 Cr</li><li>Hotel WC + cane BG: Rs 0.6-1 Cr</li><li><strong>Total: Rs 14-26 Cr/yr</strong></li></ul></div>",
    "hooks": [
        ("Cement capex anchor", "\"Mr. Velagapudi/Ms. Kavitha &mdash; UltraTech-India Cements consolidation Sep 2024 changed South India cement competitive intensity. Macherla + Mukthyala plants need WHRS + AFR + grinding-unit refresh capex Rs 200-400 Cr. We have a 7-day capex term-sheet with sustainability-linked covenant: AFR-mix &gt; 25% by FY29 = 5 bps step-down.\""),
        ("Vietnam multi-currency FX desk", "\"KCP Vietnam Industries (Phu Yen + Son Hoa) is unique in Indian sugar industry. We can consolidate VND + USD + INR FX desk + Vietnam multi-currency LC + cross-border WC. PSU consortium banks cannot do this at scale.\""),
        ("FIVES CAIL-KCP EPC USD-receivable factoring", "\"FIVES France-KCP turnkey sugar + power plant EPC for Africa + South America + SE Asia &mdash; USD receivable Rs 80-150 Cr book opportunity at MCLR-plus-50 non-recourse factoring. Plus advance + retention BG framework.\""),
        ("Velagapudi family-PB", "\"4-generation Velagapudi family wealth + dual-listed sugar entities + multi-business conglomerate &mdash; one of TN\'s most uninstitutionalised promoter-PB opportunities. Senior partner can fly down for no-commitment first conversation.\""),
        ("KCP-cluster cross-sell (KCP Sugar Industries listed-sister)", "\"KCP Limited (this entity, multi-business) + KCP Sugar &amp; Industries Corporation (separately listed BSE 533166) = dual-listed Velagapudi family banking ecosystem. Cross-sell potential to sister listed entity.\""),
    ],
    "questions": [
        "What is the Macherla + Mukthyala cement capacity-utilisation today + capex sequencing FY26-29?",
        "How is the WHRS + AFR commitment structured at the cement plants?",
        "Vietnam operations: what is the Phu Yen + Son Hoa capacity, current capacity-utilisation, and FY26-28 expansion?",
        "What is the FIVES CAIL-KCP EPC orderbook today + execution cycle?",
        "How is the Vietnam multi-currency exposure managed today (which bank consolidates VND + USD + INR)?",
        "What is the FIVES France royalty + dividend repatriation flow?",
        "Heavy Engineering: what is the Steel Foundry + Build-to-Order revenue split?",
        "How is the dual-listed structure (KCP Limited + KCP Sugar Industries) managed at promoter family level?",
        "Velagapudi family-wealth: HUF / family-trust / individual structure?",
        "What is the open MCA charges Rs 480 Cr split by bank?",
        "Sustainability covenant appetite for cement + sugar capex?",
        "Hotel segment (Mercure Hyderabad KCP) capex cycle + expansion plans?",
    ],
    "questions_not": [
        "Do not ask about KCP Sugar Industries directly in first KCP Limited meeting (separate entity, separate consortium).",
        "Do not pitch on rate &mdash; multi-bank consortium has tight rate-discipline.",
        "Do not propose family-succession in first meeting.",
        "Do not name specific competitor banks unless asked.",
        "Do not over-pitch Vietnam business &mdash; family is sensitive about Vietnam political-economic risks.",
    ],
    "objections": [
        ("\"We are happy with our current banks (multi-business consortium ~Rs 480 Cr).\"", "\"Mr. Velagapudi &mdash; we are not asking to displace anyone. The 5-business structure means each business has its own consortium. We are asking to anchor one specific sleeve where our differentiated capability matters: Vietnam multi-currency FX, FIVES France EPC USD-factoring, or cement-capex sustainability-linked TL. Not displacing, adding on right product.\""),
        ("\"Your rates are not competitive vs PSU.\"", "\"On commodity products yes. Differentiation: multi-currency FX desk + sustainability-linked covenant + EPC export-receivable factoring at scale + family-PB platform. PSU consortium cannot bundle this.\""),
        ("\"Vietnam operations are sensitive — we manage them ourselves.\"", "\"That\'s exactly the point. Vietnam VND/USD/INR cross-currency + ASEAN export needs sophisticated multi-currency banking. Most PSUs cannot price VND or do correspondent-banking in Hanoi/HCMC. We have the global network + advisory team.\""),
        ("\"FIVES CAIL-KCP is a JV — financing comes from JV side.\"", "\"Understood. But the Indian-side WC + receivable + advance-BG can be standalone-financed at IBank India. That gives KCP single-bank visibility on the JV cash flows on the India side.\""),
        ("\"Velagapudi family wealth is private.\"", "\"That\'s the design point of our PB platform &mdash; most discrete senior promoter PB. Senior partner can fly down for 30-min conversation. No commitment.\""),
        ("\"You don\'t understand cement-sugar-engineering multi-business conglomerates.\"", "\"We have worked with Birla cement + Sankarapandian-era India Cements + Ramco Cements + Bajaj Hindusthan + Triveni Engineering across cement-sugar-engineering. We can bring multi-segment cluster team for technical due-diligence visit.\""),
    ],
})

SPEC.update({
    "math_html": """
<h3>J.1 12-month plan (FY27)</h3>
<div class="card"><table><thead><tr><th>Quarter</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>Q1 FY27 (Apr-Jun 2026)</td><td>(a) Cement capex term-sheet (Macherla + Mukthyala WHRS + AFR); (b) Vietnam multi-currency FX desk consolidation pitch; (c) Senior PB partner introduction.</td><td>Rs 0.6 Cr LC + Rs 0.5 Cr FX deal</td></tr>
<tr><td>Q2 FY27 (Jul-Sep 2026)</td><td>(a) Cement capex committee approval; (b) Vietnam VND/USD/INR FX desk first quarter; (c) FIVES CAIL-KCP USD-receivable factoring concept.</td><td>Rs 1.0 Cr IRS + Rs 0.6 Cr Vietnam-FX</td></tr>
<tr><td>Q3 FY27 (Oct-Dec 2026)</td><td>(a) Cement capex drawn 20%; (b) FIVES first USD-factoring deal Rs 30-50 Cr; (c) Cane-procurement BG roll-out for AP + TN sugar.</td><td>Rs 1.5 Cr capex Y1 + Rs 0.4 Cr factoring + Rs 0.3 Cr BG</td></tr>
<tr><td>Q4 FY27 (Jan-Mar 2027)</td><td>(a) Vietnam multi-currency LC + WCDL Rs 50 Cr; (b) Heavy engineering project-LC; (c) Velagapudi family-PB AUM diagnostic.</td><td>Rs 0.5 Cr Vietnam + Rs 0.4 Cr project-LC</td></tr>
<tr><td><strong>Y1 (FY27) total wallet</strong></td><td></td><td class="num"><strong>Rs 5.8 Cr</strong></td></tr>
</tbody></table></div>

<h3>J.2 24-month plan (FY28)</h3>
<div class="card"><table><thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>H1 FY28</td><td>Cement capex fully drawn; Vietnam FX desk consolidated; FIVES CAIL-KCP USD-factoring book Rs 80 Cr; Velagapudi family-PB AUM Rs 100+ Cr signed.</td><td>Rs 4 Cr Y2 add</td></tr>
<tr><td>H2 FY28</td><td>Sustainability KPI first measurement (cement AFR-mix); Vietnam plant scale-up; cane-BG mandate; KCP-cluster cross-sell to listed sister.</td><td>Rs 3 Cr Y2 add</td></tr>
<tr><td><strong>Y2 (FY28) wallet</strong></td><td></td><td class="num"><strong>Rs 12.8 Cr</strong></td></tr>
</tbody></table></div>

<h3>J.3 36-month plan (FY29) &mdash; the inflection year</h3>
<div class="card"><table><thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>H1 FY29</td><td>Cement capex refresh tranche; Velagapudi family-PB AUM Rs 250+ Cr; Vietnam Phase-2 expansion finance.</td><td>Rs 4.5 Cr Y3 add</td></tr>
<tr><td>H2 FY29</td><td>Sustainability KPI step-down kicks in; FIVES CAIL-KCP orderbook factoring stabilises Rs 120+ Cr; KCP Sugar Industries listed-sister cross-sell.</td><td>Rs 2.7 Cr Y3 add</td></tr>
<tr><td><strong>Y3 (FY29) wallet</strong></td><td></td><td class="num"><strong>Rs 20 Cr base case</strong></td></tr>
</tbody></table></div>

<h3>J.4 Sensitivity</h3>
<div class="card"><ul>
<li><strong>Bull (cement-capex won + Vietnam FX consolidated + FIVES factoring + family-PB):</strong> Rs 26 Cr Y3.</li>
<li><strong>Base (cement-capex + Vietnam FX + partial FIVES):</strong> Rs 20 Cr Y3.</li>
<li><strong>Bear (cement-capex sleeve only, Vietnam declined, PB declined):</strong> Rs 12-14 Cr Y3.</li>
</ul></div>
""",
    "ecosystem_html": """
<h3>K.1 Receivables (who pays KCP) &mdash; multi-segment</h3>
<div class="card"><table><thead><tr><th>Counterparty</th><th>Segment</th><th>Annual flow (FY24 est)</th><th>Cycle</th><th>Bank product</th></tr></thead><tbody>
<tr><td>Real-estate developers (Brigade, Lodha, DLF, Prestige etc) + infra contractors (L&T, Tata Projects)</td><td>Cement (Macherla + Mukthyala)</td><td>Rs 1,000-1,200 Cr</td><td>30-60 day</td><td>Receivable factoring + dealer-finance</td></tr>
<tr><td>Sugar trade dealers + OMC (BPCL/IOC/HPCL ethanol)</td><td>Sugar India + ethanol off-take</td><td>Rs 500-700 Cr</td><td>15-30 day (sugar) / 30-45 day (OMC ethanol)</td><td>OMC ethanol factoring + dealer-CMS</td></tr>
<tr><td>Vietnam customers (sugar trade + ASEAN export)</td><td>Sugar Vietnam (Phu Yen + Son Hoa)</td><td>Rs 600-800 Cr (VND-translated)</td><td>30-60 day VND</td><td>Vietnam multi-currency factoring + LC</td></tr>
<tr><td>Indian Railways + Capital-goods customers + Capital projects</td><td>Heavy Engineering (Steel Foundry + Build-to-Order)</td><td>Rs 200-300 Cr</td><td>60-180 day project-cycle</td><td>Project-LC + customer-LC</td></tr>
<tr><td>Africa + South America + SE Asia EPC customers</td><td>FIVES CAIL-KCP turnkey EPC (USD)</td><td>Rs 200-400 Cr USD</td><td>30-90 day with advance + retention</td><td>USD export factoring + BG framework</td></tr>
<tr><td>Hotel guests + corporate F&B + events</td><td>Mercure Hyderabad KCP</td><td>Rs 50-80 Cr</td><td>0-30 day</td><td>CMS + corporate-card</td></tr>
</tbody></table></div>

<p><strong>RM read:</strong> The cement-developer receivable book (Rs 1,000-1,200 Cr) + FIVES CAIL-KCP EPC receivable (USD Rs 200-400 Cr) + Vietnam VND book (Rs 600-800 Cr) are the three structural opportunities. Single-bank consolidation of multi-currency factoring delivers Rs 1.5-2.5 Cr/yr at low cost-of-acquisition.</p>

<h3>K.2 Payables (suppliers — who KCP pays)</h3>
<div class="card"><table><thead><tr><th>Counterparty</th><th>Spend</th><th>Annual outflow</th><th>Cycle</th><th>Bank product</th></tr></thead><tbody>
<tr><td>Coal + pet-coke (Coal India + import) + limestone (captive + open-market)</td><td>Cement raw material (35-40% COGS)</td><td>Rs 800-1,000 Cr</td><td>30 day</td><td>WCDL + LME-coal IRS + LC import</td></tr>
<tr><td>~10,000-15,000 cane farmers (AP + TN)</td><td>Cane procurement (statutory 14-day cycle)</td><td>Rs 350-500 Cr (sugar India)</td><td>14 day statutory</td><td>Cane-procurement BG (Min Consumer Affairs) + IMPS bulk-payout</td></tr>
<tr><td>Vietnam cane farmers + sugarcane growers</td><td>Vietnam cane procurement</td><td>Rs 250-400 Cr (VND)</td><td>30-60 day Vietnam</td><td>Vietnam VND-WCDL + multi-currency LC</td></tr>
<tr><td>Steel + alloy + casting raw material (Tata Steel, JSW, SAIL)</td><td>Heavy Engineering</td><td>Rs 150-200 Cr</td><td>30 day</td><td>WCDL + LME-steel IRS</td></tr>
<tr><td>Capital goods (cement plant + sugar plant + heavy-eq tooling — German/Chinese/Korean)</td><td>Capex (multi-business)</td><td>Rs 100-300 Cr in capex years</td><td>30/60/10 milestone</td><td>BG (advance + performance) + LC capital-goods + FX</td></tr>
<tr><td>Salary (~3,500 FTE consolidated incl Vietnam)</td><td>Payroll</td><td>Rs 200-280 Cr/yr</td><td>Monthly</td><td>Salary CASA mandate</td></tr>
<tr><td>Power + chemicals + diesel + spares</td><td>Operating across all segments</td><td>Rs 200-300 Cr</td><td>30 day</td><td>Trade SCF + corp-cards</td></tr>
</tbody></table></div>

<p><strong>RM read:</strong> The 14-day statutory cane-payment cycle (Rs 350-500 Cr/yr to ~10-15k farmers) is the under-banked structural opportunity in KCP\'s sugar India business. Cane-procurement BG (Min Consumer Affairs cover) + farmer-KCC under Bannari/Triveni-style cluster framework. PSU consortium has not built farmer-KCC infrastructure.</p>
""",
    "competitors_html": """
<p><strong>Diligence note:</strong> Probe42 detail-level pull required across KCP Limited + KCP Vietnam Industries + FIVES CAIL-KCP CINs to confirm bank-by-bank split.</p>
<div class="card"><table><thead><tr><th>Bank</th><th>Likely position</th><th>Strength</th><th>Weakness we exploit</th></tr></thead><tbody>
<tr><td>SBI</td><td>Lead candidate (multi-segment + cement)</td><td>Largest BG capacity; cement-cluster experience; multi-business handling</td><td>Slow on capex term-sheet; no Vietnam VND capability; no FIVES France EPC factoring at scale; no PB platform</td></tr>
<tr><td>HDFC Bank</td><td>Likely #2-3 (sugar + cement)</td><td>Auto-OEM SCF + payroll execution; sugar-cluster customer relationships</td><td>Limited Vietnam multi-currency depth; modest EPC factoring</td></tr>
<tr><td>Indian Bank</td><td>Likely #3-4 (TN-headquartered relationship)</td><td>TN local + AP cement-cluster relationship; original WC-line</td><td>No FX desk at scale; cannot lead cement capex; limited PB</td></tr>
<tr><td>Axis / Kotak</td><td>Specialty WC + EPC</td><td>Specialty WC + factoring</td><td>FX/derivative tier-2; PB platform less developed</td></tr>
<tr><td>BNP Paribas / SocGen / Citi (French link)</td><td>Possible FX + capex-import + FIVES France relationship</td><td>FX depth; capital-goods LC; FIVES France banking link</td><td>Limited domestic retail/CASA/farmer-KCC capability</td></tr>
<tr><td>Vietcombank + ACB Vietnam</td><td>Local Vietnam ops banker (KCP Vietnam Industries)</td><td>Vietnam VND deposit + WC + farmer-payment cycle</td><td>Cannot do cross-border to India; cannot consolidate global FX</td></tr>
<tr><td><strong>IBank target seat</strong></td><td>Cement capex anchor + Vietnam FX consolidation + FIVES USD-factoring + family-PB</td><td>7-day capex term-sheet; multi-currency FX (USD+EUR+VND); FIVES France EPC factoring; family-PB platform; KCP-cluster cross-sell</td><td>Need anchor seat to be relevant on multi-business consortium</td></tr>
</tbody></table></div>
<p><strong>Diagnosis:</strong> KCP\'s multi-business multi-currency multi-bank consortium (~Rs 480 Cr) has structural openings for IBank: (a) <strong>cement-capex sleeve</strong> on Macherla + Mukthyala (UltraTech-consolidation urgency), (b) <strong>Vietnam VND + multi-currency FX consolidation</strong> (no Indian bank does this at scale), (c) <strong>FIVES CAIL-KCP EPC USD-receivable factoring</strong> at MCLR-plus-50, (d) <strong>Velagapudi family-PB</strong> on multi-gen Andhra industrial-family wealth.</p>
""",
    "plays": [
        ("Play 1: Cement capex anchor (Macherla + Mukthyala WHRS + AFR refresh)", "<strong>Trigger:</strong> UltraTech-India Cements Sep 2024 consolidation creates competitive intensity in South India cement; KCP needs cost-discipline + capex urgency at Macherla + Mukthyala. <strong>Offer:</strong> 7-yr capex TL Rs 200-400 Cr with sustainability-linked covenant: AFR-mix &gt; 25% by FY29 = 5 bps step-down. <strong>Bait:</strong> Pre-validated Board paper; 7-day SLA; AFR + WHRS methodology pre-priced. <strong>Y2-Y3 income:</strong> Rs 1.5-3 Cr/yr stable for 7 years. <strong>Risk:</strong> Lost to SBI lead. <strong>Mitigation:</strong> Position as co-anchor; bring credit-decisioning speed advantage."),
        ("Play 2: Vietnam multi-currency FX desk (VND + USD + INR)", "<strong>Trigger:</strong> KCP Vietnam Industries Phu Yen + Son Hoa plants Rs 600-800 Cr revenue (VND-translated); FY26-29 capacity-expansion + ASEAN export drive multi-currency exposure; current consolidation tier-2. <strong>Offer:</strong> Consolidated VND + USD + INR FX desk + Vietnam multi-currency LC + cross-border WCDL + ASEAN export-receivable factoring. <strong>Bait:</strong> Diagnostic showing Rs 1.5-2.5 Cr/yr saving from FX consolidation + cross-border efficiency. <strong>Y1-Y3 income:</strong> Rs 1-2 Cr/yr deal fee + spread. <strong>Risk:</strong> Family declines cross-currency consolidation. <strong>Mitigation:</strong> Phase-1 Vietnam VND-only desk to prove value."),
        ("Play 3: FIVES CAIL-KCP EPC USD-receivable factoring + Velagapudi family-PB", "<strong>Trigger:</strong> FIVES France-KCP turnkey sugar + power EPC orderbook for Africa + South America + SE Asia &mdash; USD receivable Rs 200-400 Cr; advance + retention BG required. <strong>Offer:</strong> Non-recourse USD factoring at MCLR + 50-80 bps + advance + performance + retention BG framework + Velagapudi family-PB on multi-gen wealth. <strong>Bait:</strong> Family-portfolio diagnostic + USD-LC pre-priced. <strong>Y3 income:</strong> Rs 0.5-1 Cr USD factoring + Rs 1.2-2.2 Cr family-PB AUM = Rs 1.7-3.2 Cr/yr. <strong>Risk:</strong> Family declines PB. <strong>Mitigation:</strong> introduction via mutual-friend in Velagapudi-aware Andhra industrial-family network."),
    ],
    "firstcall_html": """
<h3>N.1 Opening (5 min)</h3>
<div class="card"><p><em>"Mr. Velagapudi / Ms. Kavitha &mdash; thank you for the time. We are not here for share-of-wallet on the existing book. We have studied KCP\'s 5-business structure, the Vietnam operations, the FIVES CAIL-KCP orderbook, and the cement-capex urgency post UltraTech-India Cements consolidation. Three structural ideas &mdash; one cement, one Vietnam-FX, one family/EPC. If at the end of 30 minutes you do not see value, we leave it there."</em></p></div>

<h3>N.2 Mid-call (3 blocks, 15 min each)</h3>
<div class="card">
<p><strong>Block 1 (Cement capex):</strong> "UltraTech-India Cements Sep 2024 changed South India cement competitive intensity. Macherla + Mukthyala need WHRS + AFR + grinding-unit refresh capex Rs 200-400 Cr. We have a 7-day capex term-sheet with sustainability-linked covenant: AFR-mix &gt; 25% by FY29 = 5 bps step-down. Anchor or co-anchor?"</p>
<p><strong>Block 2 (Vietnam multi-currency FX):</strong> "KCP Vietnam Industries (Phu Yen + Son Hoa) is unique in Indian sugar. Rs 600-800 Cr revenue translation drives complex VND/USD/INR FX. We can consolidate the multi-currency FX desk + Vietnam LC + cross-border WC. PSU consortium cannot do this at scale."</p>
<p><strong>Block 3 (FIVES EPC + family-PB):</strong> "FIVES CAIL-KCP turnkey sugar+power plants for Africa + SAm + SE Asia &mdash; USD receivable Rs 200-400 Cr book + advance + retention BG. Non-recourse factoring at MCLR-plus-50 + BG framework. Separately, our senior PB partner can fly down to discuss Velagapudi family wealth structuring."</p>
</div>

<h3>N.3 The ask (5 min)</h3>
<div class="card"><p>"Three takeaways: (1) cement-capex term-sheet to CFO + V. Kavitha Dutt in 14 days; (2) Vietnam FX consolidation diagnostic in May; (3) PB conversation with V.L. Dutt in Q2."</p></div>

<h3>N.4 Follow-up (T+24)</h3>
<div class="card">
<ul>
<li>One-page recap email; cement-capex term-sheet draft; Vietnam FX diagnostic; FIVES CAIL-KCP EPC factoring one-pager; PB partner profile.</li>
<li>CC: V.L. Dutt, V. Kavitha Dutt, CFO, Vietnam-ops head, FIVES CAIL-KCP MD.</li>
</ul>
</div>

<h3>N.5 What NOT to do</h3>
<div class="card"><ul>
<li>Do not pitch on rate &mdash; multi-bank consortium will undercut.</li>
<li>Do not show up without capex term-sheet draft.</li>
<li>Do not propose KCP Sugar Industries cross-sell in first KCP Limited meeting (separate consortium).</li>
<li>Do not propose family-succession or ESOP advisory in first meeting.</li>
<li>Do not over-pitch Vietnam business or hint at political risk &mdash; family is sensitive.</li>
</ul></div>
""",
    "sources": [
        "The KCP Limited Annual Report FY24 + investor relations &middot; kcp.co.in &middot; 28 Apr 2026",
        "The KCP Limited financials &middot; screener.in/company/KCP &middot; 28 Apr 2026",
        "KCP Vietnam Industries Limited (Phu Yen + Son Hoa sugar operations)",
        "FIVES CAIL-KCP JV with Fives Group France",
        "NSE/BSE KCP quarterly filings &middot; KCP Sugar Industries (KCPSUGIND) sister listing",
        "CRISIL credit-rating rationale Dec 2025 [verify FY26]",
        "Probe42 open-charges API &middot; CIN L65991TN1941PLC001128",
        "MCA / ZaubaCorp THE K C P LIMITED filings",
        "Tofler The KCP Limited financial profile",
        "Velagapudi family disclosures (V.L. Dutt + V. Kavitha Dutt)",
        "RBI MPC Apr 2026 &middot; rbi.org.in",
        "USD/INR FBIL reference rate &middot; fbil.org.in &middot; 28 Apr 2026",
        "VND/INR cross-currency reference &middot; State Bank of Vietnam",
        "LME coal + pet-coke commodity reference &middot; lme.com / argus media",
        "EU CBAM scheme &middot; taxation-customs.ec.europa.eu &middot; cement Phase-1",
        "TN-SAP + AP-SAP cane price &middot; State Agriculture Departments",
        "CACP Sugarcane FRP &middot; cacp.dacnet.nic.in",
        "ISMA + Vietnam Sugar Association production estimates",
        "UltraTech-India Cements acquisition Sep 2024 (consolidation context)",
        "MoSPI quarterly GDP &middot; mospi.gov.in &middot; FY26 Q3",
    ],
})


def build():
    out, lines = build_one(SPEC)
    print(f"[kcp-sector] wrote {out} ({lines} lines)")


if __name__ == "__main__":
    build()
