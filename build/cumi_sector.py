"""CUMI sector deep-dive (pilot 153) using rich-sector framework."""
from ._rich_sector import build_one

SPEC = {
    "pilot": 153, "name": "Carborundum Universal Limited",
    "dossier_slug": "carborundum-universal", "cluster_label": "Abrasives / Ceramics / Electrominerals / Advanced materials",
    "headline_low": 18, "headline_high": 32, "y3_sub": "M&A + FX + group cross-sell",
    "play_strap": "Lead M&A acquisition-financing window · multi-currency FX desk · Murugappa group cross-sell",
    "tldr_lede": "CUMI is a 70-year Murugappa flagship listed on BSE+NSE (CARBORUNIV); FY24 revenue Rs 4,781 Cr; cash-positive Rs 442 Cr net; promoter holding 41.23%. The play is to anchor the M&A acquisition-financing window (Rs 200-500 Cr ongoing bolt-on pipeline in advanced-materials + aerospace-defence + battery-thermal), bundle multi-currency FX (USD + EUR + RUB + AUD across global subs), and bring Murugappa family-PB on the 5-flagship promoter base.",
    "kpi_b_label": "M&A pipeline", "kpi_b_val": "Rs 200-500 Cr", "kpi_b_sub": "Bolt-on advanced-materials",
    "kpi_c_label": "FY24 baseline", "kpi_c_val": "Rs 4,781 Cr", "kpi_c_sub": "+8.7% YoY",
    "kpi_d_label": "Net cash", "kpi_d_val": "Rs 442 Cr", "kpi_d_sub": "Cash-positive",
    "walking_in": "\"Mr. Murugappan / Anantha &mdash; CUMI's M&A pipeline is the most under-banked Murugappa-flagship opportunity. We want to be the financing-bank-of-choice on the next 2-3 bolt-ons, run your multi-currency FX desk across the global subs, and bring our PB partner to the family.\"",
    "history_strap": "the 70-year arc from tripartite JV to Murugappa industrial-materials flagship",
    "history": [
        ("Founding (1954) — Tripartite JV", "CUMI was incorporated 21 April 1954 in Madras as a tripartite JV of Murugappa Chettiar (India), Carborundum Co. (USA, then Saint-Gobain subsidiary), and Universal Grinding Wheel Co. (UK). Mandate: abrasives + bonded/coated grinding wheels for post-Independence Indian industry."),
        ("The 1960s-1980s — Domestic abrasives leadership", "Built dominant Indian abrasives + ceramics + refractories franchise. Murugappa steadily increased holding while foreign JV partners reduced exposure. Plant footprint expanded across TN (Tiruvottiyur, Hosur), Maharashtra, AP."),
        ("The 1990s-2000s — Murugappa control + electrominerals", "By early 1990s Murugappa effectively the controlling promoter. Added electrominerals (silicon carbide + fused alumina + zirconia) as distinct business line. Foskor Zirconia (South Africa) marked first global manufacturing footprint."),
        ("The 2010s — Russia + Australia + Murugappa Morgan", "Acquired Volzhsky Abrasive Works (Russia, 2007 via subsidiary), establishing major silicon-carbide manufacturing base. Murugappa-Morgan Thermal Ceramics JV with Morgan Advanced Materials UK became Tier-1 ceramic-fibre + insulation supplier. Wendt India separately listed for super-abrasives."),
        ("2022-2024 M&amp;A burst — PLUSS + RHODIUS + AWUKO + Aerospace-Defence Hub", "Structural inflection. Acquired PLUSS Advanced Technologies (India 2022) for phase-change-material + cold-chain + battery-thermal. Two German bolt-ons: RHODIUS Abrasive (2022) + CUMI AWUKO Abrasives (2023). Aerospace-Defence Innovation Hub launched 2023, signalling commitment to high-margin defence + advanced-materials adjacencies."),
        ("Next 36 months (FY26-FY29) — M&amp;A continuation + advanced-materials scale", "FY24 Rs 4,781 Cr; analyst-est FY28 Rs 8,300 Cr (CAGR ~15% with M&A optionality). M&A pipeline in advanced-materials + aerospace-defence + battery-thermal expected to consume Rs 200-500 Cr financing window. Multi-currency FX flows from global subs drive Rs 1,500-2,000 Cr/yr forex turnover."),
        ("Why this matters for the IBank pitch", "(1) CUMI is a compounder — Rs 25 Cr LT debt against Rs 442 Cr net cash means M&A capacity sits unused. (2) The M&A pipeline is real and ongoing. (3) Multi-currency FX desk + Russia/Belarus sanctions navigation is a high-value advisory mandate no domestic bank can do alone. (4) CUMI is one of 5 Murugappa flagships — cross-sell into TII + EID Parry + Coromandel + Chola Finance is the long-game."),
    ],
    "kmp": [
        ("M.M. Murugappan — Chairman", "Murugappa family fourth-generation; long-time CUMI architect since 1990s. Strategic focus on M&A bolt-ons + global manufacturing + advanced-materials pivot. Decision style: family-stewardship + portfolio thinking. RM angle: bring senior MD-level introduction; Murugappan is the strategic gate."),
        ("N. Ananthaseshan — Managing Director (since 2020)", "Operational MD with deep manufacturing background. Decision style: execution + capital-efficient. What he cares about: M&A integration delivery; ROCE on bolt-ons; global subsidiary performance. RM angle: primary banking counterparty; bring M&A advisory + treasury head."),
        ("P. Padmanabhan — CFO", "Day-to-day banking counterparty; multi-currency FX desk relationship lead. RM angle: monthly meetings; FX dealer + treasury strategist."),
        ("Subsidiaries / Operating structure", "<strong>Sterling Abrasives</strong> (India sub); <strong>Murugappa Morgan Thermal Ceramics</strong> (JV with Morgan Advanced Materials UK); <strong>RHODIUS Abrasive GmbH</strong> (Germany); <strong>CUMI AWUKO</strong> (Germany); <strong>Volzhsky Abrasive Works</strong> (Russia); <strong>Foskor Zirconia</strong> (South Africa); <strong>Wendt India</strong> (separately listed JV with Wendt GmbH); <strong>PLUSS Advanced Technologies</strong> (acquired 2022). Aerospace-Defence Innovation Hub (2023)."),
    ],
}

SPEC.update({
    "valuechain_strap": "abrasives + ceramics + electrominerals + advanced-materials cluster",
    "valuechain_text": "CUMI operates across four interlinked value-chains: (1) <strong>abrasives</strong> (alumina/silicon-carbide → bonded/coated grinding wheels → industrial / auto / construction customers); (2) <strong>ceramics + refractories</strong> (alumina + zirconia → high-temp industrial + steel + cement linings → B2B customers); (3) <strong>electrominerals</strong> (silicon-carbide + fused alumina + zirconia → EV-battery + advanced-materials + steel customers); (4) <strong>advanced materials + PCM</strong> (PLUSS phase-change-material → cold-chain logistics + battery-thermal-management).",
    "valuechain_table": "<table><thead><tr><th>Stage</th><th>Pricing power</th><th>WC impact</th><th>Bank product</th></tr></thead><tbody><tr><td>Bauxite + alumina + silicon-carbide raw material</td><td>Limited &mdash; commodity-linked</td><td>30-60 day cycle; Rs 200-300 Cr peak</td><td>WCDL + LC import</td></tr><tr><td>Manufacturing (abrasives / ceramics / electrominerals)</td><td>Strong &mdash; specialty grades 18-22% gross margin</td><td>30-45 day WIP</td><td>Capex TL on bolt-on M&amp;A</td></tr><tr><td>B2B sale (industrial + auto + steel + EV)</td><td>Strong via cert + spec</td><td>30-90 day receivable</td><td>Receivable factoring</td></tr><tr><td>Export to global subs + customer (USD/EUR)</td><td>Strong on spec; FX-exposed</td><td>30-60 day</td><td>Multi-currency FX + LC</td></tr></tbody></table>",
    "driver_fs_intro": "Sized to FY25 baseline (TOI ~Rs 5,350 Cr; EBITDA ~Rs 565 Cr; promoter 41.23%; net cash Rs 442 Cr).",
    "driver_fs": [
        ("M&amp;A pipeline (advanced-materials + defence)", "Bolt-on capex Rs 200-500 Cr over FY26-29; subsidiary-level acquisition financing", "<strong>Acquisition-financing TL Rs 200-300 Cr</strong>"),
        ("Multi-currency FX (USD/EUR/RUB/AUD)", "Global subs Germany + Russia + Australia + South Africa; Rs 1,500-2,000 Cr forex flows", "Multi-currency FX desk + IRS + LC"),
        ("Russia/Belarus sanctions exposure", "Volzhsky Abrasive Works operations; sanctions-navigation needed", "Sanctions-cleared multi-bank routing + RUB hedge"),
        ("EV-battery + cold-chain (PLUSS) tailwind", "Phase-change-material demand FY27-29 inflection", "Capex TL + sustainability covenant"),
        ("Aerospace-defence indigenisation", "HAL + DRDO + tier-2 defence supply", "BG framework + customer-LC + defence-receivable factoring"),
        ("LME-bauxite + alumina + zinc", "20-30% of COGS; commodity hedge", "Commodity-WCDL + IRS"),
        ("Murugappa group treasury", "5-flagship cross-sell: TII + EID Parry + Coromandel + Chola Finance", "Group treasury sweep + cross-sell mandate"),
        ("Family wealth (M.M. Murugappan + family)", "Multi-gen Murugappa wealth", "PB AUM + family-trust"),
        ("RBI repo cycle", "WCDL benchmarked", "WCDL + IRS lock"),
    ],
    "products": [
        ("Acquisition-financing TL (M&amp;A)", "Bolt-on advanced-materials + defence", "Rs 200-300 Cr", "MCLR + 80-110 bps", "Rs 5-8 Cr/yr stable"),
        ("Multi-currency FX desk", "USD + EUR + RUB + AUD; Rs 1,500-2,000 Cr/yr forex turnover", "USD 80-200 Mn", "Spread 8-15 bps", "Rs 2-4 Cr/yr"),
        ("LC + BG (capex import + customer-LC)", "USD/EUR LC for German + Australian capex", "Rs 150-300 Cr revolving", "0.30-0.45% fee", "Rs 1-2 Cr/yr"),
        ("WCDL + CC", "Raw material cycle + WIP", "Rs 150-250 Cr", "MCLR + 60-90 bps", "Rs 1.5-2.5 Cr/yr"),
        ("Receivable factoring (industrial paper)", "B2B customer paper", "Rs 80-150 Cr", "MCLR + 50-80 bps", "Rs 0.6-1.2 Cr/yr"),
        ("Salary CASA + payroll (5,200 FTE)", "CUMI + Indian subs", "Rs 12-25 Cr float", "0%", "Rs 0.5-1 Cr/yr"),
        ("PB (Murugappa family — CUMI share)", "5-flagship promoter family", "Rs 250-500 Cr AUM", "50-80 bps", "Rs 1.5-2.5 Cr/yr"),
        ("Group treasury sweep", "Cross-flagship liquidity", "Rs 800-1,500 Cr float", "Fee on int", "Rs 0.8-1.5 Cr/yr"),
        ("Sanctions advisory (Russia/Belarus)", "Volzhsky operations navigation", "Advisory mandate", "Fee-based", "Rs 0.5-1 Cr/yr"),
    ],
    "product_extra": "<h3>F.1 Y3 wallet build-up</h3><div class='card'><ul><li>Wholesale: Rs 9-19.5 Cr</li><li>Treasury (FX + group): Rs 5-9 Cr</li><li>Retail + PB + TASC: Rs 2.7-4.7 Cr</li><li><strong>Total: Rs 18-32 Cr/yr</strong></li></ul></div>",
    "hooks": [
        ("M&amp;A acquisition-financing", "\"Mr. Anantha &mdash; CUMI's M&A pipeline (RHODIUS, AWUKO, PLUSS done; next bolt-on imminent) needs Rs 200-300 Cr acquisition-financing on each. We have a 7-day acquisition-TL term-sheet pre-validated for Murugappa-flagship CUMI corporate-rating profile.\""),
        ("Multi-currency FX desk", "\"Global subs Germany + Russia + Australia + South Africa drive Rs 1,500-2,000 Cr forex flows annually. We can run the consolidated multi-currency FX desk + RUB sanctions navigation + IRS structure. PSU consortium cannot do this at scale.\""),
        ("Russia/Belarus sanctions advisory", "\"Volzhsky Abrasive Works needs sanctions-cleared payment routing. We have the global correspondent network + advisory team to keep your Russia operations cash-flowing without OFAC exposure.\""),
        ("Murugappa family-PB", "\"5-flagship Murugappa promoter family is multi-gen wealth not yet on any institutional PB platform. CUMI's share Rs 250-500 Cr AUM. Senior partner can fly down for no-commitment first conversation.\""),
        ("Group treasury cross-sell", "\"CUMI is one entry. CUMI + TII + EID Parry + Coromandel + Chola Finance = Rs 75,000+ Cr group-treasury opportunity. We want anchor CUMI first, then sweep across all five.\""),
    ],
    "questions": [
        "What is the M&amp;A pipeline FY26-29 sizing + sectors targeted (advanced-materials / defence / battery-thermal)?",
        "What is the Russia / Volzhsky operational outlook + sanctions-navigation status?",
        "How is the multi-currency FX desk structured today (which bank consolidates)?",
        "What is the LME hedge ratio on bauxite + alumina input?",
        "What is the PLUSS phase-change-material commercial scale-up timeline?",
        "What is the Aerospace-Defence Innovation Hub revenue target FY28?",
        "What is the Wendt India + Murugappa Morgan dividend / treasury policy?",
        "Murugappa family-PB &mdash; CUMI share via TII bundle or independent?",
        "Group treasury &mdash; centralised mandate or per-flagship today?",
        "Open MCA charges on CUMI + Wendt + PLUSS &mdash; bank-by-bank split?",
        "Sustainability covenant appetite for advanced-materials capex?",
        "FY26 capex envelope (organic vs M&amp;A split)?",
    ],
    "questions_not": [
        "Do not ask about Russia-sanctions specifics until trust is established.",
        "Do not pitch on rate &mdash; CUMI's cash-positive position means rate is irrelevant.",
        "Do not propose family-succession in first meeting.",
        "Do not name competitor banks unless asked.",
        "Do not over-pitch group cross-sell &mdash; signals greed.",
    ],
    "objections": [
        ("\"We are cash-positive — we don't need a TL.\"", "\"You are cash-positive on the standalone but not on the M&A capacity. RHODIUS + AWUKO + PLUSS each were Rs 100-200 Cr. The next bolt-on doesn't have to come out of cash &mdash; we can pre-validate acquisition-TL with 7-day SLA so M&A doesn't slow down.\""),
        ("\"Russia is too sensitive — we manage it ourselves.\"", "\"Volzhsky needs sanctions-cleared payment routing every quarter. Our global correspondent network + OFAC-advisory team is a structural advantage. No PSU peer offers this.\""),
        ("\"Your rates are not competitive vs PSU.\"", "\"On TL pricing yes &mdash; within 10-15 bps. Differentiation: M&A advisory + multi-currency FX desk + sanctions navigation + family-PB. PSU consortium cannot bundle this.\""),
        ("\"Murugappa family wealth is private.\"", "\"Exactly the design point. Most discrete senior promoter PB platform. Senior partner can fly down for 30-min conversation. No commitment.\""),
        ("\"You don't know the abrasives industry.\"", "\"We work with Norton (3M) + Saint-Gobain Abrasives + Tyrolit at the global parent level. We can bring abrasives-cluster lead + M&A advisor to the technical due-diligence visit.\""),
    ],
})

SPEC.update({
    "math_html": """
<h3>J.1 12-month plan (FY27)</h3>
<div class="card"><table><thead><tr><th>Quarter</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>Q1 FY27</td><td>(a) Pre-validated acquisition-TL term-sheet for next bolt-on M&amp;A; (b) Multi-currency FX desk consolidation pitch; (c) Senior PB partner introduction.</td><td>Rs 0.5 Cr LC + Rs 0.6 Cr FX deal</td></tr>
<tr><td>Q2 FY27</td><td>(a) M&amp;A target identified by CUMI; (b) IRS execution on alumina hedge; (c) Sanctions-advisory mandate signed for Volzhsky.</td><td>Rs 0.8 Cr IRS + Rs 0.5 Cr advisory</td></tr>
<tr><td>Q3 FY27</td><td>(a) Acquisition-TL drawn; (b) Group treasury cross-sell first to TII / Coromandel; (c) Receivable factoring book launch.</td><td>Rs 1.5 Cr capex Y1 + Rs 0.4 Cr SCF</td></tr>
<tr><td>Q4 FY27</td><td>(a) FX hedge book Rs 100 Mn established; (b) Murugappa family PB AUM diagnostic; (c) Bicycle-equivalent dealer channels.</td><td>Rs 0.5 Cr FX spread</td></tr>
<tr><td><strong>Y1 (FY27) total wallet</strong></td><td></td><td class="num"><strong>Rs 4.8 Cr</strong></td></tr>
</tbody></table></div>

<h3>J.2 24-month plan (FY28)</h3>
<div class="card"><table><thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>H1 FY28</td><td>Acquisition-TL drawn full; FX desk consolidated; Murugappa family-PB AUM Rs 200+ Cr signed.</td><td>Rs 5 Cr Y2 add</td></tr>
<tr><td>H2 FY28</td><td>Sanctions advisory steady; group treasury sweep covers 3 of 5 flagships; PCM (PLUSS) inflection drives factoring book.</td><td>Rs 4 Cr Y2 add</td></tr>
<tr><td><strong>Y2 (FY28) wallet</strong></td><td></td><td class="num"><strong>Rs 13.8 Cr</strong></td></tr>
</tbody></table></div>

<h3>J.3 36-month plan (FY29)</h3>
<div class="card"><table><thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead><tbody>
<tr><td>H1 FY29</td><td>Second M&amp;A bolt-on financed; FX book Rs 200+ Mn; family-PB AUM Rs 400+ Cr.</td><td>Rs 7 Cr Y3 add</td></tr>
<tr><td>H2 FY29</td><td>Aerospace-Defence Hub orderbook factoring; group cross-sell mature.</td><td>Rs 5 Cr Y3 add</td></tr>
<tr><td><strong>Y3 (FY29) wallet</strong></td><td></td><td class="num"><strong>Rs 25.8 Cr base</strong></td></tr>
</tbody></table></div>

<h3>J.4 Sensitivity</h3>
<div class="card"><ul>
<li><strong>Bull (2 M&amp;A bolt-ons + family-PB Rs 500 Cr + group cross-sell):</strong> Rs 32 Cr Y3.</li>
<li><strong>Base (1 bolt-on + family-PB Rs 300 Cr):</strong> Rs 25 Cr Y3.</li>
<li><strong>Bear (cash-positive maintained, no M&amp;A, PB declined):</strong> Rs 15-18 Cr Y3.</li>
</ul></div>
""",
    "ecosystem_html": """
<h3>K.1 Receivables</h3>
<div class="card"><table><thead><tr><th>Counterparty</th><th>Stream</th><th>Annual flow</th><th>Cycle</th><th>Bank product</th></tr></thead><tbody>
<tr><td>Auto OEM (Maruti / Tata / M&amp;M / Hyundai)</td><td>Bonded/coated abrasives + grinding wheels</td><td>Rs 800-1,000 Cr</td><td>30-60 day</td><td>OEM-anchor SCF + factoring</td></tr>
<tr><td>Steel + cement industrial customers</td><td>Refractories + ceramic linings</td><td>Rs 600-800 Cr</td><td>60-90 day</td><td>Receivable factoring</td></tr>
<tr><td>Construction + infra</td><td>Coated abrasives + grinding wheels</td><td>Rs 500-700 Cr</td><td>30-60 day</td><td>WCDL + dealer-finance</td></tr>
<tr><td>Global subs (RHODIUS / AWUKO / Volzhsky / Foskor / PLUSS)</td><td>Inter-company + third-party</td><td>Rs 1,500-2,000 Cr (consolidated)</td><td>30-90 day</td><td>Multi-currency FX + LC</td></tr>
<tr><td>Aerospace-defence (HAL / DRDO / tier-2)</td><td>Specialty ceramics + advanced materials</td><td>Rs 100-200 Cr (FY27 ramping)</td><td>60-120 day (PSU)</td><td>Defence-receivable factoring + BG</td></tr>
</tbody></table></div>

<h3>K.2 Payables</h3>
<div class="card"><table><thead><tr><th>Counterparty</th><th>Spend</th><th>Annual outflow</th><th>Cycle</th><th>Bank product</th></tr></thead><tbody>
<tr><td>Bauxite + alumina + silicon-carbide raw material</td><td>Domestic + import</td><td>Rs 1,000-1,300 Cr</td><td>30 day</td><td>WCDL + LC import</td></tr>
<tr><td>Energy (electricity + furnace fuel)</td><td>Operating</td><td>Rs 200-300 Cr</td><td>Monthly</td><td>Operational</td></tr>
<tr><td>Capital goods (German + Australian capex)</td><td>Multi-currency LC</td><td>Rs 100-200 Cr capex</td><td>30/60/10 milestone</td><td>BG + LC capital-goods + FX</td></tr>
<tr><td>Salary (5,200 FTE consolidated)</td><td>Payroll</td><td>Rs 350-450 Cr/yr</td><td>Monthly</td><td>Salary CASA</td></tr>
</tbody></table></div>
<p><strong>RM read:</strong> Multi-currency receivable book (Rs 1,500-2,000 Cr) is the structural opportunity. Single-bank consolidation of FX desk + LC + receivable factoring delivers Rs 4-6 Cr/yr from optimisation alone.</p>
""",
    "competitors_html": """
<p><strong>Diligence note:</strong> Probe42 detail-level pull required across CUMI + Wendt + PLUSS CINs.</p>
<div class="card"><table><thead><tr><th>Bank</th><th>Position</th><th>Strength</th><th>Weakness we exploit</th></tr></thead><tbody>
<tr><td>SBI</td><td>Lead candidate (Murugappa-group history)</td><td>BG + capex; legacy 30+ yr</td><td>FX desk tier-2 on multi-currency; no M&amp;A advisory; no PB at scale</td></tr>
<tr><td>HDFC Bank</td><td>Likely #2-3</td><td>Auto-OEM SCF + payroll</td><td>Limited multi-currency FX depth; no Russia/sanctions navigation</td></tr>
<tr><td>Citi / Deutsche / HSBC</td><td>FX + capex-import LC</td><td>Multi-currency FX strong; sanctions advisory</td><td>Domestic retail/payroll/CASA limited; PB platform tier-2</td></tr>
<tr><td>Axis / Kotak</td><td>Specialty WC</td><td>Specialty WC + factoring</td><td>FX/derivative tier-2; M&amp;A advisory limited</td></tr>
<tr><td><strong>IBank target seat</strong></td><td>M&amp;A acquisition-financing anchor + multi-currency FX + family-PB</td><td>7-day TL; multi-currency FX desk; sanctions advisory; family-PB platform; group cross-sell</td><td>Need to displace Citi/Deutsche on FX consolidation; need anchor on next M&amp;A to be relevant</td></tr>
</tbody></table></div>
<p><strong>Diagnosis:</strong> CUMI consortium runs 5-6 banks; SBI lead + private + foreign-MNC FX. IBank openings: (a) M&amp;A acquisition-financing (Citi + Deutsche typically lead this), (b) multi-currency FX desk consolidation, (c) Russia sanctions advisory, (d) Murugappa family-PB.</p>
""",
    "plays": [
        ("Play 1: M&amp;A acquisition-financing anchor", "<strong>Trigger:</strong> Next bolt-on (advanced-materials or defence) announced FY27. <strong>Offer:</strong> Pre-validated 7-day acquisition-TL Rs 200-300 Cr + LC for cross-border consideration + FX cover. <strong>Bait:</strong> CUMI's M&A track record (RHODIUS / AWUKO / PLUSS) means we already know your due-diligence cycle. <strong>Y2-Y3 income:</strong> Rs 5-8 Cr/yr stable. <strong>Risk:</strong> Lost to Citi/Deutsche cross-border M&A teams. <strong>Mitigation:</strong> Bring M&A advisory + global correspondent network."),
        ("Play 2: Multi-currency FX desk + Russia sanctions advisory", "<strong>Trigger:</strong> Quarterly Volzhsky payment + global subs FX needs. <strong>Offer:</strong> Consolidated multi-currency FX desk (USD + EUR + RUB + AUD) + sanctions-cleared correspondent network + IRS structure on commodity exposure. <strong>Bait:</strong> Diagnostic showing Rs 4-6 Cr/yr saving from FX consolidation. <strong>Y1-Y3 income:</strong> Rs 2-4 Cr/yr deal fee + spread. <strong>Risk:</strong> CFO declines consolidation. <strong>Mitigation:</strong> Phase 1 with Russia-only desk to prove value."),
        ("Play 3: Murugappa family-PB + group treasury cross-sell", "<strong>Trigger:</strong> Senior PB partner introduction via M.M. Murugappan. <strong>Offer:</strong> Multi-gen mandate covering Murugappan + Subbiah + Vellayan + 5-flagship promoter family; group treasury sweep across CUMI + TII + EID Parry + Coromandel + Chola Finance. <strong>Bait:</strong> Family-portfolio diagnostic + group cash-management efficiency pitch. <strong>Y3 income:</strong> Rs 1.5-2.5 Cr PB + Rs 0.8-1.5 Cr group treasury + Rs 0.4-0.7 Cr TASC = Rs 2.7-4.7 Cr/yr. <strong>Risk:</strong> Family declines. <strong>Mitigation:</strong> Introduction via Aru / TII relationship if CUMI-direct doesn't open."),
    ],
    "firstcall_html": """
<h3>N.1 Opening (5 min)</h3>
<div class="card"><p><em>"Mr. Murugappan / Anantha &mdash; thank you for the time. We are not here for share-of-wallet on the existing book. We have studied CUMI's M&amp;A track record (RHODIUS, AWUKO, PLUSS), the multi-currency FX flows, and the Russia/Volzhsky exposure. Three structural ideas &mdash; one M&amp;A, one treasury, one family. If at the end of 30 minutes you do not see value, we leave it there."</em></p></div>
<h3>N.2 Mid-call (3 blocks)</h3>
<div class="card">
<p><strong>Block 1 (M&amp;A financing):</strong> "Next bolt-on doesn't have to come out of cash. Pre-validated acquisition-TL with 7-day SLA on Murugappa-flagship rating profile."</p>
<p><strong>Block 2 (Multi-currency FX + Russia):</strong> "Rs 1,500-2,000 Cr forex turnover across global subs is structurally under-optimised. We can consolidate FX desk + RUB sanctions navigation + IRS. Rs 4-6 Cr/yr saving."</p>
<p><strong>Block 3 (Family-PB):</strong> "5-flagship Murugappa family wealth is the largest unbanked promoter-PB opportunity in TN. Senior partner can fly down."</p>
</div>
<h3>N.3 The ask (5 min)</h3>
<div class="card"><p>"Three takeaways: (1) Acquisition-TL term-sheet to CFO P. Padmanabhan in 14 days; (2) FX consolidation diagnostic in May; (3) PB conversation with Vellayan in Q2."</p></div>
<h3>N.4 Follow-up (T+24)</h3>
<div class="card"><ul><li>Recap email + acquisition-TL one-pager + FX diagnostic + sanctions-advisory profile + PB partner profile.</li><li>CC: M.M. Murugappan, Anantha, Padmanabhan, Vellayan.</li></ul></div>
<h3>N.5 What NOT to do</h3>
<div class="card"><ul><li>Do not pitch on rate &mdash; CUMI cash-positive.</li><li>Do not propose group-treasury lead role &mdash; that is FY28 conversation.</li><li>Do not over-discuss Russia in first meeting.</li><li>Do not over-pitch family-PB &mdash; restrained ask only.</li></ul></div>
""",
    "sources": [
        "CUMI Annual Report FY24 + investor relations &middot; cumi-murugappa.com &middot; 28 Apr 2026",
        "RHODIUS + AWUKO + PLUSS acquisition disclosures 2022-2023",
        "NSE/BSE CARBORUNIV quarterly filings &middot; nseindia.com / bseindia.com",
        "Murugappa Group corporate site &middot; murugappa.com",
        "Probe42 open-charges API &middot; CIN L29224TN1954PLC000318",
        "CRISIL credit-rating rationale CARBORUNIV [verify FY26]",
        "Screener.in CARBORUNIV financials",
        "RBI MPC Apr 2026 &middot; rbi.org.in",
        "USD/EUR/RUB/AUD FX FBIL reference &middot; 28 Apr 2026",
        "LME bauxite/alumina/zinc reference &middot; lme.com",
        "EU CBAM scheme &middot; taxation-customs.ec.europa.eu",
        "OFAC sanctions list (Russia/Belarus) &middot; treasury.gov &middot; current",
        "MCA-21 charge register &middot; mca.gov.in",
        "SEBI listed-company shareholding &middot; bseindia.com",
        "MoSPI quarterly GDP &middot; mospi.gov.in &middot; FY26 Q3",
        "FY25 audited financials &middot; [diligence]",
        "Wikipedia CUMI overview &middot; en.wikipedia.org",
        "Tofler CUMI profile &middot; tofler.in",
        "Tracxn CUMI legal entity &middot; tracxn.com",
        "Murugappa group governance disclosures &middot; group press releases",
    ],
})


def build():
    out, lines = build_one(SPEC)
    print(f"[cumi-sector] wrote {out} ({lines} lines)")


if __name__ == "__main__":
    build()
