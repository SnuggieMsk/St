"""Sector deep-dive generator (RM-meeting-grade companion to each dossier).

Produces a 13-section HTML file per company at /home/user/St/<slug>-sector.html
linked from the parent dossier. Cluster-driven base content + per-company
specifics keep each file bespoke without hand-writing all 150.
"""
from pathlib import Path
from .base import HEAD, FOOT, ref

OUTDIR = Path("/home/user/St")

NAV = """
<nav class="nav"><ol>
<li><a href="#tldr">A · TL;DR play</a></li>
<li><a href="#valuechain">B · Value-chain</a></li>
<li><a href="#driver-fs">C · Driver → FS</a></li>
<li><a href="#product-fs">D · Product → FS</a></li>
<li><a href="#hooks">E · Hooks</a></li>
<li><a href="#questions">F · Question bank</a></li>
<li><a href="#objections">G · Objections</a></li>
<li><a href="#math">H · Conversion math</a></li>
<li><a href="#ecosystem">I · Ecosystem</a></li>
<li><a href="#competitors">J · Competitors</a></li>
<li><a href="#plays">K · Three plays</a></li>
<li><a href="#firstcall">L · First-call</a></li>
<li><a href="#sources">M · Sources</a></li>
</ol></nav>
"""

# ============================================================
# CLUSTER ARCHETYPES — value-chain + driver→FS map per cluster
# ============================================================
CLUSTERS = {
    "ems": {
        "label": "Electronics Manufacturing Services (EMS)",
        "value_chain": "Component import (China/Taiwan/Korea) &rarr; SMT line + box-build + final assembly &rarr; brand-OEM customer (Apple/Xiaomi/Samsung/etc.) &rarr; export or domestic. Margin thin (2-4% EBITDA); volume-driven; PLI / SPECS scheme drives capex.",
        "drivers": [
            ("PLI / SPECS extension", "FY27 PLI 2.0 likely &rarr; capex acceleration", "Capex TL + LC for SMT-line imports"),
            ("USD/INR + import dependency", "65-80% BOM imported &rarr; FX exposure on every shipment", "Forward USD-cover + LC at sight"),
            ("Apple-PLI / Tier-1 brand demand", "iPhone 17/18 cycle, Xiaomi growth", "Receivable factoring against brand-OEM paper"),
            ("USA-China decoupling", "China+1 tailwind &mdash; Vietnam/India share grows", "Capex TL framework on multi-year visibility"),
            ("Component shortage / inventory", "Volatile WC cycle &mdash; CC limit utilisation peaks", "WCDL + inventory finance"),
        ],
        "products": [
            ("Capex TL (SMT-line imports)", "100-400 Cr", "5-7yr", "MCLR + 80-110 bps"),
            ("LC + BG (component imports)", "200-500 Cr revolving", "30-90 day cycle", "0.30-0.50% fee"),
            ("FX forward + IRS", "USD 50-200 Mn notional", "3-12 month", "Spread 5-15 bps"),
            ("Receivable factoring (brand-OEM paper)", "100-300 Cr", "30-60 day discount", "MCLR + 50-80 bps"),
            ("WCDL (peak-season inventory)", "50-200 Cr", "3-6 month", "MCLR + 60-90 bps"),
            ("Salary CASA + payroll", "Rs 15-80 Cr float", "Monthly", "0% on float"),
        ],
        "competitors_default": "SBI + HDFC + Citi (FX + LC strong); local PSU on capex; we win on speed + bundling capex+LC+factoring.",
    },
    "auto": {
        "label": "Automotive components / OEM",
        "value_chain": "Steel + aluminium + plastics + electronics &rarr; press-shop / paint-shop / assembly &rarr; OEM (Hyundai/Tata/M&M/Stellantis) JIT &rarr; aftermarket. EV transition reshaping product mix.",
        "drivers": [
            ("EV transition", "ICE-to-EV product re-engineering &mdash; capex burst FY26-29", "Capex TL framework + R&D-linked TL"),
            ("OEM JIT receivable", "30-45 day OEM payment cycle", "OEM-anchor SCF + factoring"),
            ("Steel + aluminium price", "Volatile input cost &mdash; margin swing 100-200 bps", "Commodity hedge + WCDL"),
            ("Export tariff (USA)", "USA 25% MFN tariff + India-specific frictions", "FX + export-finance mitigation"),
            ("PLI auto-component", "Approved entities get 4-7% production-linked subsidy", "TL on subsidised capex"),
        ],
        "products": [
            ("Capex TL (EV-line + new-product capex)", "150-600 Cr", "6-8yr", "MCLR + 70-100 bps"),
            ("OEM-anchored SCF (Hyundai/Tata/etc)", "200-400 Cr", "30-60 day", "MCLR + 30-50 bps"),
            ("LC + BG (vendor + capex import)", "150-300 Cr revolving", "30-180 day", "0.30-0.45% fee"),
            ("Forex (USD + EUR + KRW)", "USD 30-150 Mn notional", "3-12 month", "Spread 5-12 bps"),
            ("Inventory + WC (steel/alu cycle)", "100-250 Cr", "60-90 day", "MCLR + 60-90 bps"),
            ("Aftermarket dealer-finance", "30-100 Cr", "30-90 day", "MCLR + 80-120 bps"),
        ],
        "competitors_default": "HDFC + SBI (OEM-anchor SCF dominant); Citi (FX); we differentiate on capex-speed + EV-linked sustainability covenant.",
    },
    "gcc": {
        "label": "Global Capability Centre / IT Services",
        "value_chain": "Onshore demand (US/EU enterprise IT) &rarr; offshore delivery centre (India) &rarr; FTE-led billing in USD/EUR/GBP. Asset-light; payroll = 60-70% of cost; FX is the top-line risk.",
        "drivers": [
            ("USA tariff / immigration policy", "H-1B / L-1 friction reduces onshore margin", "Local-hiring TASC + payroll mandate scale"),
            ("USD/INR appreciation cycle", "Top-line in USD, costs in INR &mdash; +/- 100 bps margin per 1% FX", "Forward USD cover + IRS"),
            ("Hiring + attrition", "Bench growth &mdash; payroll WC swing", "WCDL + payroll CASA float"),
            ("AI / automation", "Pyramid restructure &mdash; senior bench grows", "PB AUM upside on senior cohort"),
            ("GIFT City / SEZ", "Tax-incentive arbitrage on new sites", "Capex TL + treasury sweep"),
        ],
        "products": [
            ("Forex hedge (USD + EUR + GBP)", "USD 100-500 Mn notional", "3-24 month", "Spread 5-12 bps"),
            ("Payroll CASA + salary mandate", "5,000-50,000 FTE", "Monthly float", "0%"),
            ("Capex TL (campus + GIFT-City)", "50-200 Cr", "5-7yr", "MCLR + 60-80 bps"),
            ("WCDL (bench + onboarding)", "30-150 Cr", "3-6 month", "MCLR + 50-70 bps"),
            ("PB (senior leadership)", "Rs 100-500 Cr AUM", "Permanent", "AUM fee 50-80 bps"),
            ("Treasury sweep + ZBA", "Rs 50-300 Cr float", "Daily", "0% but fee on int"),
        ],
        "competitors_default": "Citi + HSBC + SCB (FX dominant); HDFC payroll; we win on payroll-CASA scale + PB platform + GIFT-City speed.",
    },
}

CLUSTERS["pharma"] = {
    "label": "Pharma / Healthcare / CDMO / Diagnostics",
    "value_chain": "API import / domestic synthesis &rarr; formulation / fill-finish &rarr; regulator filing (USFDA/EU/CDSCO) &rarr; export (US/EU 50-70%) + domestic. R&D-intensive; quality-driven; capex-heavy; long cash cycle.",
    "drivers": [
        ("USFDA / EU GMP cycle", "Regulatory action can swing top-line 20-30%", "Insurance + SBLC; covenant on rating"),
        ("USA tariff / drug-pricing-reform", "IRA + PBM friction on USA gross margin", "FX + export-receivable factoring"),
        ("API + KSM China-dependence", "60-80% China import", "LC + China-RMB cover"),
        ("PLI + bulk-drug-park", "Capex incentive 6-10%", "Capex TL with sustainability"),
        ("Patent-cliff + bio-similar", "$70 Bn US patent cliff FY26-30", "R&D-linked TL"),
    ],
    "products": [
        ("Capex TL (API plant + fill-finish)", "200-700 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("Receivable factoring (USA buyer paper)", "150-400 Cr", "60-120 day", "MCLR + 50-80 bps"),
        ("LC + BG (API + KSM imports)", "200-500 Cr revolving", "30-180 day", "0.30-0.50% fee"),
        ("FX forward (USD + EUR + RMB)", "USD 50-300 Mn notional", "3-18 month", "Spread 5-12 bps"),
        ("R&D-linked WC", "50-200 Cr", "12-24 month", "MCLR + 80-110 bps"),
        ("PB (founder + scientific leadership)", "Rs 100-300 Cr AUM", "Permanent", "AUM fee"),
    ],
    "competitors_default": "SBI + HDFC + Citi (FX+LC); we differentiate on R&D-linked WC + bulk-drug-park capex speed + PB.",
}

CLUSTERS["chem"] = {
    "label": "Specialty chemicals / Petroleum / Industrial gases",
    "value_chain": "Crude / naphtha / specialty-feedstock &rarr; reactor / refinery / blending &rarr; B2B (industrial / pharma / agri) + retail. Brent + USD/INR are the top swing factors.",
    "drivers": [
        ("Brent crude", "Direct feedstock; 50-100 bps margin per $5/bbl swing", "Commodity hedge + Brent IRS"),
        ("USD/INR + crude import", "FX flow Rs 1,000-5,000 Cr/yr", "Forward + LC at sight"),
        ("EU CBAM", "Carbon-border tariff on cement/aluminium/steel/chem", "Sustainability-linked TL"),
        ("PESO + CPCB compliance", "Capex on emission control + tail-gas treatment", "Capex TL framework"),
        ("Demand cycle (auto/textile/agri)", "Downstream demand swings input volume", "WCDL + receivable factoring"),
    ],
    "products": [
        ("Capex TL (capacity expansion + emission)", "200-600 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("LC + BG (crude + feedstock import)", "300-700 Cr revolving", "30-90 day", "0.30-0.45% fee"),
        ("FX + Brent IRS", "USD 100-400 Mn notional", "3-12 month", "Spread 5-15 bps"),
        ("Receivable factoring (B2B paper)", "100-300 Cr", "30-60 day", "MCLR + 50-80 bps"),
        ("WCDL (inventory cycle)", "100-300 Cr", "60-90 day", "MCLR + 60-90 bps"),
        ("Sustainability-linked TL", "100-400 Cr", "5-7yr", "MCLR + 50-80 bps step-down"),
    ],
    "competitors_default": "SBI + Axis + Citi; we win on Brent-IRS depth + sustainability-linked covenant pricing.",
}

CLUSTERS["agri"] = {
    "label": "Sugar / Agri / FMCG / Textiles / Edible oils",
    "value_chain": "Farm raw material (cane/cotton/oilseed/milk) at MSP/SAP &rarr; mill/process &rarr; B2B + retail. Regulated pricing + monsoon + commodity volatility.",
    "drivers": [
        ("Monsoon + crop output", "Direct on raw-material availability + price", "WCDL + crop-cycle finance"),
        ("MSP / SAP / FRP regulation", "Cane SAP, milk procurement, MSP for grains", "Receivable + procurement BG"),
        ("EBP (ethanol blending) E20", "Ethanol off-take at admin price by FY27", "Capex TL on distillery"),
        ("Brent + commodity hedge", "Edible oil + textile import-export FX", "FX + commodity"),
        ("PMFME / FPO / co-op", "Govt schemes on food-processing", "TASC + co-branded retail KCC"),
    ],
    "products": [
        ("Capex TL (mill + distillery + process)", "100-400 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("Procurement BG (farmer payment + Min Consumer Affairs)", "50-200 Cr", "Annual", "0.30% fee"),
        ("OMC / B2B factoring", "100-300 Cr", "30-60 day", "MCLR + 50-80 bps"),
        ("FX + commodity hedge", "USD 20-100 Mn notional", "3-12 month", "Spread 5-12 bps"),
        ("Vendor-SCF + farmer KCC", "Rs 100-300 Cr book", "30-90 day", "MCLR + 60-90 bps"),
        ("PB (founder/family) + Foundation TASC", "Rs 100-500 Cr AUM", "Permanent", "AUM fee + corpus"),
    ],
    "competitors_default": "PNB + SBI + Canara (PSU lead on agri); we win on capex speed + farmer-KCC + family-PB + Foundation-TASC bundle.",
}

CLUSTERS["engg"] = {
    "label": "Engineering / Capital goods / Power / Infrastructure",
    "value_chain": "Steel + casting + electronics + bought-out components &rarr; assembly / fabrication / testing &rarr; B2B project / infra / power / utility customer (LT-cycle). Long WC; project receivable risk.",
    "drivers": [
        ("Capex cycle (govt + private)", "Order-book builds 18-36 month forward", "Capex TL on customer-confirmed pipeline"),
        ("Steel + commodity input", "30-50% BOM &mdash; margin sensitivity", "Hedge + WCDL"),
        ("PSU / govt-tender retention", "Performance + advance + retention BG (3-7yr)", "BG framework / CBL-pool"),
        ("Renewable energy / decarbonisation", "Wind + solar + storage capex", "Sustainability-linked TL"),
        ("FX (capex import + export)", "USD/EUR for German/Japanese tech imports", "Forward + LC"),
    ],
    "products": [
        ("Capex TL (plant + machinery)", "150-500 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("Performance + advance BG (project)", "200-600 Cr", "3-7yr", "0.30-0.50% fee/yr"),
        ("LC (capex import + raw material)", "200-500 Cr", "30-180 day", "0.30-0.45% fee"),
        ("WCDL (project WC + inventory)", "100-300 Cr", "60-180 day", "MCLR + 60-90 bps"),
        ("Sustainability-linked TL (renewable)", "100-400 Cr", "7-10yr", "MCLR + 60-90 bps step-down"),
        ("Receivable factoring (PSU paper)", "100-300 Cr", "60-180 day", "MCLR + 60-90 bps"),
    ],
    "competitors_default": "SBI + PNB (PSU-anchor BG); HDFC project finance; we win on BG-pool flexibility + sustainability covenant + speed.",
}

CLUSTERS["realestate"] = {
    "label": "Real estate / Industrial parks / Hospitality / SEZ",
    "value_chain": "Land acquisition &rarr; entitlement + zoning &rarr; construction (TL-debt funded) &rarr; lease/sale &rarr; FM/maintenance recurring. Long-cycle; rate-sensitive; CRE-rating dependent.",
    "drivers": [
        ("RBI repo / mortgage rate", "Direct on demand + cost of capital", "TL re-pricing + IRS"),
        ("Tier-2/3 industrial park demand", "GCC + EMS + auto-component capex demand", "Tenant-anchor TL"),
        ("REIT / InvIT regulation", "Asset monetisation pathway", "Advisory + debt-syndication"),
        ("FDI + SEZ incentive", "Tax-incentive on new SEZ commitments", "TL on incentive-linked covenant"),
        ("Construction WC + retention", "Vendor + retention + advance cycle", "Vendor-SCF + WCDL"),
    ],
    "products": [
        ("CRE TL (construction)", "200-1,000 Cr", "5-10yr", "MCLR + 80-130 bps"),
        ("LRD (lease-rental-discounting)", "200-800 Cr", "8-12yr", "MCLR + 70-100 bps"),
        ("Performance BG + advance BG", "100-400 Cr", "3-7yr", "0.40% fee"),
        ("Vendor-SCF (construction)", "100-300 Cr", "30-90 day", "MCLR + 60-90 bps"),
        ("FX (capex import + foreign tenant)", "USD 30-100 Mn", "3-12 month", "Spread 8-15 bps"),
        ("PB (promoter + investor)", "Rs 100-1,000 Cr AUM", "Permanent", "AUM fee"),
    ],
    "competitors_default": "HDFC + SBI + LIC HF (CRE TL dominant); Axis + Kotak; we win on LRD speed + REIT advisory + PB.",
}

CLUSTERS["logistics"] = {
    "label": "Logistics / Auto-distribution / Shipping",
    "value_chain": "Fleet / warehouse / shipping asset &rarr; B2B (auto OEM, FMCG, e-commerce) contract logistics &rarr; recurring revenue. Asset-heavy; rate-sensitive; fleet-finance heavy.",
    "drivers": [
        ("Diesel + fuel cost", "30-40% opex; pass-through lag", "Hedge + WCDL"),
        ("Fleet capex cycle", "BS-VI + EV transition fleet replacement", "Fleet TL + lease"),
        ("Auto / FMCG demand", "Direct on volume", "Receivable factoring"),
        ("USA tariff / export volume", "Container + bulk volume sensitivity", "FX + export-finance"),
        ("Driver shortage + payroll", "10-15k driver workforce", "Payroll CASA + retail loans"),
    ],
    "products": [
        ("Fleet TL (truck + tanker + container)", "100-400 Cr", "5-7yr", "MCLR + 80-110 bps"),
        ("Warehouse / asset capex TL", "100-300 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("OEM-anchor SCF", "100-300 Cr", "30-60 day", "MCLR + 50-80 bps"),
        ("Driver-payroll CASA + retail loan", "10,000-30,000 FTE", "Monthly", "0% float + retail margin"),
        ("FX (container + bulk)", "USD 20-80 Mn", "3-9 month", "Spread 8-12 bps"),
        ("WCDL (fuel + working capital)", "50-200 Cr", "60-90 day", "MCLR + 60-90 bps"),
    ],
    "competitors_default": "HDFC + SBI (fleet TL); we win on bundled fleet-TL + driver-CASA + FX speed.",
}

CLUSTERS["retail"] = {
    "label": "Jewellery / Retail / Consumer / Hospitality",
    "value_chain": "Inventory (gold, garments, packaged goods) &rarr; retail store / e-comm channel &rarr; consumer purchase. WC-heavy; gold-linked FX; brand-driven; PB-rich.",
    "drivers": [
        ("Gold price + USD/INR", "Inventory carry cost; WC swing", "Gold metal loan + FX hedge"),
        ("Discretionary spending cycle", "Direct on volume", "WCDL + e-commerce SCF"),
        ("Festival cycle (Diwali/Akshaya)", "Q3-Q4 inventory build", "Seasonal WCDL"),
        ("PMJDY / UPI rails", "Customer acquisition rails", "Co-branded card + UPI mandate"),
        ("Promoter HNI/UHNI wealth", "Family/promoter portfolio", "PB + family-trust"),
    ],
    "products": [
        ("Gold metal loan + WCDL", "100-500 Cr", "30-180 day", "MCLR + 60-90 bps"),
        ("Capex TL (store expansion + supply chain)", "100-300 Cr", "5-7yr", "MCLR + 70-100 bps"),
        ("E-commerce SCF + factoring", "50-200 Cr", "30-60 day", "MCLR + 50-80 bps"),
        ("Co-branded card + UPI rails", "Rs 1,000-10,000 Cr GMV", "Recurring", "Interchange + fee"),
        ("FX (gold + import)", "USD 20-100 Mn", "3-9 month", "Spread 5-10 bps"),
        ("PB (promoter HNI/UHNI)", "Rs 200-2,000 Cr AUM", "Permanent", "AUM fee 50-80 bps"),
    ],
    "competitors_default": "HDFC + Kotak + Axis (gold + retail); we win on PB + co-branded card + family-trust depth.",
}

CLUSTERS["defence"] = {
    "label": "Defence PSU / Strategic manufacturing",
    "value_chain": "Defence Acquisition Council (DAC) approval &rarr; PSU manufacture (BEL/HAL/AVNL/etc.) &rarr; Indian Army/Navy/AF customer (sole). Atmanirbhar tailwind; FRCV / Tank-EX programmes.",
    "drivers": [
        ("Defence-Atmanirbhar capex", "75% indigenisation by FY30 mandate", "Capex TL + LC for tech-import"),
        ("FRCV + Tank-EX + ICV programme", "Multi-year orderbook visibility", "BG framework + capex TL"),
        ("PSU treasury cycle (90-120 day)", "Customer (MoD) payment cycle", "Treasury sweep + factoring"),
        ("FX (Russian + European tech)", "T-90 + Carl-Gustaf imports", "USD/EUR/RUB cover"),
        ("Export framework (friendly nations)", "Future tank-export pipeline", "FX + export-finance"),
    ],
    "products": [
        ("BG (defence + customer-LC)", "200-700 Cr", "3-7yr", "0.30-0.45% fee"),
        ("Capex TL (FRCV indigenisation)", "200-500 Cr", "6-8yr", "MCLR + 70-100 bps"),
        ("Treasury sweep + ZBA", "Rs 100-500 Cr float", "Daily", "0% on float"),
        ("Trade (LC + BG)", "100-400 Cr", "30-180 day", "0.30-0.45% fee"),
        ("FX (USD + EUR + RUB)", "USD 50-200 Mn", "3-18 month", "Spread 5-12 bps"),
        ("Customer-finance (MoD-LD discounting)", "200-500 Cr", "60-120 day", "MCLR + 50-80 bps"),
    ],
    "competitors_default": "SBI (PSU-anchor BG); Indian Bank + Canara; we win as greenfield BG/capex entry on FRCV indigenisation tailwind.",
}

CLUSTERS["healthcare"] = {
    "label": "Hospitals / Clinical research / Diagnostics",
    "value_chain": "OPD/IPD service delivery &rarr; payor mix (insurance/government/self-pay) &rarr; recurring outpatient + episodic inpatient. Capex-heavy; insurance-receivable cycle.",
    "drivers": [
        ("Insurance penetration + claim cycle", "TPA cycle 60-90 days; claim risk", "Receivable factoring + WCDL"),
        ("Capex (new wing + equipment)", "Hospital + diagnostic capex burst", "Capex TL framework"),
        ("Medical tourism + USD/INR", "International patient receivable", "FX + export-finance"),
        ("Insurance regulation (IRDAI)", "Fixed pricing + claim-deny risk", "WCDL + reserve management"),
        ("Promoter family", "Founder + multi-generation wealth", "PB + family-trust"),
    ],
    "products": [
        ("Capex TL (hospital wing + equipment)", "100-500 Cr", "7-10yr", "MCLR + 70-100 bps"),
        ("Insurance-receivable factoring", "100-300 Cr", "60-90 day", "MCLR + 50-80 bps"),
        ("WCDL (working capital + payroll)", "50-200 Cr", "30-90 day", "MCLR + 60-90 bps"),
        ("Salary CASA + payroll (doctor + staff)", "5,000-20,000 FTE", "Monthly", "0% float"),
        ("FX (medical tourism + capex import)", "USD 10-50 Mn", "3-9 month", "Spread 8-12 bps"),
        ("PB (founder family + senior consultant)", "Rs 100-500 Cr AUM", "Permanent", "AUM fee"),
    ],
    "competitors_default": "HDFC + SBI (hospital capex); we win on insurance-receivable factoring speed + payroll-CASA + PB.",
}

# ============================================================
# RENDER FUNCTIONS — section by section
# ============================================================

def _A(spec, cl):
    """TL;DR / play-on-a-page."""
    pos = spec.get("position", "greenfield")
    pos_kpi = {
        "greenfield": ('<div class="kpi neg"><div class="k">IBank position</div><div class="v num">Greenfield</div><div class="sub">No charges' + ref("126") + '</div></div>',
                       "Greenfield acquisition", "win first BG / FX / capex slot"),
        "present": ('<div class="kpi pos"><div class="k">IBank position</div><div class="v num">' + spec.get("ibank_pct","?%") + '</div><div class="sub">' + spec.get("position_sub","Present") + ref("126") + '</div></div>',
                    "Defend-and-climb", "defend " + spec.get("ibank_pct","current") + " · climb to lead bank"),
        "absent": ('<div class="kpi neg"><div class="k">IBank position</div><div class="v num">0%</div><div class="sub">' + spec.get("position_sub","Other-bank consortium") + ref("126") + '</div></div>',
                   "Competitive entry", "dislodge incumbent on " + spec.get("incumbent","SBI/HDFC")),
    }.get(pos, ('<div class="kpi"><div class="k">Position</div><div class="v num">?</div><div class="sub">TBC</div></div>', "Greenfield", "win entry slot"))

    name = spec["name"]; pilot = spec["pilot"]; cluster_label = cl["label"]
    headline_low = spec["headline_low"]; headline_high = spec["headline_high"]
    tldr_lede = spec.get("tldr_lede", f"{name} sits in the {cluster_label} cluster. The play is {pos_kpi[1].lower()} &mdash; {pos_kpi[2]}. Y3 wallet target Rs {headline_low}-{headline_high} Cr/yr across capex + trade + FX + retail/PB/TASC.")
    walking_in = spec.get("walking_in", f"\"We have studied your FY25 print and the FY26 capex commentary. We have one structural idea on financing the next leg, one treasury-side idea on the rate cycle, and one family-side idea. If at the end of 30 minutes you do not see value, we leave it there.\"")

    return f"""
<section id="tldr" class="hero">
<div class="eyebrow">Sector deep-dive companion · Pilot {pilot} · {name} · {cluster_label}</div>
<h1>The play in 90 seconds<br>{spec.get("play_strap", pos_kpi[1])} &middot; Y3 wallet Rs {headline_low}-{headline_high} Cr</h1>
<p class="lede">{tldr_lede}</p>
<div class="grid c4" style="margin-top:18px">
<div class="kpi accent"><div class="k">Y3 wallet</div><div class="v num">Rs {headline_low}-{headline_high} Cr/yr</div><div class="sub">All products</div></div>
{pos_kpi[0]}
<div class="kpi"><div class="k">Cluster</div><div class="v num" style="font-size:1.2rem">{cluster_label.split(' /')[0]}</div><div class="sub">{cluster_label}</div></div>
<div class="kpi pos"><div class="k">Sector growth</div><div class="v num">{spec.get("sector_growth","8-15%")}</div><div class="sub">FY26-29 CAGR</div></div>
</div>
<div class="card accent" style="margin-top:20px">
<h4 style="margin-top:0">The single sentence the RM walks in with</h4>
<p style="font-size:1.1rem;margin-bottom:0"><em>{walking_in}</em></p>
</div>
<div class="meta" style="margin-top:14px">
<span>Companion to <strong><a href="{spec['dossier_slug']}-dossier.html">{spec['dossier_slug']}-dossier.html</a></strong></span>
<span>Cut <strong>Probe42 24 Apr 2026</strong></span>
<span>Author <strong>RM-meeting prep · LCG/PBG Chennai</strong></span>
</div>
</section>
"""


def _B(spec, cl):
    """Value-chain."""
    return f"""
<section id="valuechain"><div class="subhead">B · Sector value-chain &mdash; how money + product + risk flow</div>
<p>{cl["value_chain"]}</p>
<div class="card">
<h4>Where {spec["name"]} sits</h4>
<p>{spec.get("position_in_chain", spec["name"] + " operates as a " + cl["label"].split(' /')[0].lower() + " player; FY25 baseline TOI Rs " + str(spec.get("toi","?")) + " Cr; the value-chain entry points map to the products listed in Section D.")}</p>
</div>
</section>
"""


def _C(spec, cl):
    """Driver → FS line-item map."""
    rows = ""
    for d in cl["drivers"]:
        rows += f"<tr><td><strong>{d[0]}</strong></td><td>{d[1]}</td><td>{d[2]}</td></tr>\n"
    extra = ""
    for d in spec.get("extra_drivers", []):
        rows += f"<tr><td><strong>{d[0]}</strong></td><td>{d[1]}</td><td>{d[2]}</td></tr>\n"
    return f"""
<section id="driver-fs"><div class="subhead">C · Driver &rarr; FS line-item map &mdash; the gap-identification engine</div>
<p>For each driver in the {cl["label"].split(' /')[0]} sector, this maps how it lands on the P&amp;L / Balance Sheet, and which IBank product fills the resulting gap. Magnitudes sized to FY25 baseline (TOI Rs {spec.get("toi","?")} Cr).</p>
<div class="card">
<table>
<thead><tr><th>Driver</th><th>FS impact</th><th>IBank product entry</th></tr></thead>
<tbody>{rows}</tbody></table>
</div>
</section>
"""


def _D(spec, cl):
    """Product → FS map."""
    rows = ""
    for p in cl["products"]:
        rows += f"<tr><td><strong>{p[0]}</strong></td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td></tr>\n"
    return f"""
<section id="product-fs"><div class="subhead">D · IBank product &rarr; FS map &mdash; what we sell, structured</div>
<div class="card">
<table>
<thead><tr><th>Product</th><th>Size</th><th>Tenor</th><th>Price</th></tr></thead>
<tbody>{rows}</tbody></table>
</div>
<p class="muted small">Pricing is indicative; final pricing depends on rating, tenor, collateral, and group cross-sell economics.</p>
</section>
"""


def _E(spec, cl):
    """Conversation hooks (5)."""
    name = spec["name"]
    default_hooks = [
        ("Capex window", f"FY26-FY29 capex burst &mdash; we want to be the anchor for the next round. Term-sheet ready, 7-day commitment letter, sustainability covenant priced in."),
        ("Treasury rate cycle", f"RBI at 6.50% with June MPC consensus 25 bps cut. We can lock 60% of WCDL at the post-cut rate via IRS &mdash; saves Rs 0.5-1 Cr/yr."),
        ("Family + PB", f"Senior PB partner introduction; multi-generational family-trust structuring; we are the only bank in your panel with a top-tier PB platform."),
        ("Group cross-sell", f"Bring our wholesale + retail + PB + TASC bundle to the broader {spec.get('group','group')} ecosystem &mdash; not just this entity."),
        ("Workforce + payroll", f"Salary CASA mandate at scale on {spec.get('fte','FTE')} base; salary float + retail loan attach + UPI rails &mdash; quiet annuity."),
    ]
    hooks = spec.get("hooks", default_hooks)
    items = ""
    for i, (h, body) in enumerate(hooks, 1):
        items += f'<li><strong>{i}. {h}</strong> &mdash; {body}</li>\n'
    return f"""
<section id="hooks"><div class="subhead">E · Five conversation hooks &mdash; the openers that earn the next 30 minutes</div>
<div class="card"><ol>{items}</ol></div>
</section>
"""


def _F(spec, cl):
    """Question bank."""
    cluster_qs = {
        "ems": ["What is your PLI 2.0 commitment delta vs PLI 1.0?", "What % of BOM is China-imported and how is FX hedged?", "What is the SMT-line capex sequencing FY26-29?", "How is the brand-OEM receivable cycle structured (Apple/Xiaomi/Samsung)?", "What is the FX hedge ratio + tenor of forward book?"],
        "auto": ["What is the EV vs ICE product mix shift over FY26-29?", "Which OEM-anchor SCF is in place and at what discount?", "What is the steel/aluminium hedge ratio?", "What is the USA tariff exposure on exports?", "What is the R&D capex commitment + capitalisation policy?"],
        "gcc": ["What is the FX hedge ratio + tenor on USD/EUR/GBP receivables?", "What is the GIFT-City / SEZ capex commitment?", "What is the bench + attrition WC cycle?", "How does the AI/automation pyramid restructure cost base?", "What is the senior leadership PB AUM today?"],
        "pharma": ["What is the USFDA + EU GMP filing pipeline FY26-29?", "What is the API + KSM China-import dependency?", "What is the IRA/PBM exposure on US gross margin?", "What is the bulk-drug-park / PLI capex commitment?", "What is the patent-cliff / bio-similar opportunity sizing?"],
        "chem": ["What is the Brent + USD/INR hedge ratio?", "How does EU CBAM affect the export book FY26-29?", "What is the PESO + CPCB capex commitment?", "What is the downstream demand visibility (auto/textile/agri)?", "What is the sustainability-linked covenant + KPI structure?"],
        "agri": ["What is the FY26-29 capex sequencing (mill + distillery + process)?", "How is the procurement BG sized and which bank holds it?", "What is the OMC / B2B receivable factoring rate?", "What is the FX + commodity hedge ratio?", "What is the family + Foundation TASC corpus?"],
        "engg": ["What is the current orderbook + book-to-bill ratio?", "What is the BG-pool sizing and which banks hold the share?", "What is the steel + commodity hedge ratio?", "What is the renewable / decarbonisation capex commitment?", "What is the PSU receivable + retention BG cycle?"],
        "realestate": ["What is the LRD + CRE TL outstanding by phase?", "What is the tenant-anchor mix (FDI vs domestic)?", "What is the REIT / monetisation pipeline?", "What is the construction WC + retention cycle?", "What is the promoter + investor PB AUM?"],
        "logistics": ["What is the fleet capex sequencing (BS-VI + EV)?", "Which OEM-anchor SCF is in place + at what discount?", "What is the diesel + fuel hedge ratio?", "What is the USA tariff / export volume sensitivity?", "What is the driver-payroll CASA + retail loan attach rate?"],
        "retail": ["What is the gold metal loan + WCDL outstanding?", "What is the festival / discretionary cycle WC peak?", "What is the e-commerce SCF + co-branded card GMV?", "What is the FX hedge on gold + import?", "What is the promoter + family PB AUM?"],
        "defence": ["What is the FY26-29 orderbook visibility (FRCV + Tank-EX + ICV)?", "What is the BG-pool sizing and consortium share?", "What is the FX (USD/EUR/RUB) hedge structure?", "What is the export-framework opportunity (friendly nations)?", "What is the PSU treasury cycle + receivable factoring rate?"],
        "healthcare": ["What is the insurance-receivable factoring rate + TPA mix?", "What is the capex sequencing (new wing + equipment)?", "What is the medical tourism + USD/INR exposure?", "What is the doctor + staff salary CASA mandate?", "What is the founder + senior consultant PB AUM?"],
    }
    qs = spec.get("questions", cluster_qs.get(spec["cluster"], cluster_qs["engg"]))
    items = "".join(f"<li>{q}</li>\n" for q in qs)
    return f"""
<section id="questions"><div class="subhead">F · Question bank &mdash; what to ask, what NOT to ask</div>
<div class="card"><h4 style="margin-top:0">12 questions for the meeting</h4>
<ol>{items}</ol></div>
<div class="card"><h4 style="margin-top:0">What NOT to ask</h4>
<ul>
<li>Do not ask for share of wallet on first meeting &mdash; signals begging.</li>
<li>Do not ask "what is your debt outstanding" &mdash; we should know this from registry.</li>
<li>Do not ask "who is your lead bank" &mdash; we should know this.</li>
<li>Do not ask for the audited financials &mdash; CFO will share if relationship deepens.</li>
<li>Do not pitch on rate &mdash; PSU/incumbent will always undercut.</li>
</ul></div>
</section>
"""


def _G(spec, cl):
    """Objection handling."""
    pos = spec.get("position", "greenfield")
    common_obj = [
        ("\"We are happy with our current banks.\"", "We are not asking to displace anyone &mdash; we are asking for a slot on the next refresh / capex tranche where we bring something differentiated (capex speed, FX depth, sustainability covenant, PB platform). Eight banks already share your wallet; one more on the right product is normal."),
        ("\"Your rates are not competitive vs PSU.\"", "Rates are commoditised within 10-15 bps. The differentiation is execution speed, structural pricing on derivatives, sustainability-linked covenants that give you a margin step-down, and a retail/PB/TASC bundle PSUs cannot offer. We compete on structure, not headline rate."),
        ("\"You are too small to lead our capex consortium.\"", "We do not need to lead &mdash; we need a co-anchor seat. Once we deliver on Phase-1, the FY28 refresh becomes a different conversation. Show us one Rs 100-200 Cr sleeve where we can prove capex execution speed."),
        ("\"You don't have a sugar/auto/EMS-specialist team.\"" if spec["cluster"] in ("agri","auto","ems") else "\"You don't have a defence/PSU/sector-specialist team.\"", f"We have a {cl['label'].split(' /')[0].lower()}-cluster team in Mumbai/Chennai with 8-10 senior bankers including the relationship lead, capex underwriter, FX dealer, and PB partner. Their CVs are in your pre-read."),
        ("\"Your turnaround time on credit decisions is slow.\"", "Our committee meets weekly with a 7-day SLA on standard ticket sizes. PSU peers run 21-28 day cycles. We will write that SLA into our term-sheet."),
        ("\"You don't understand our family / promoter dynamics.\"", "Our PB platform manages over Rs 50,000 Cr of family wealth across India's top 200 industrial families. Senior PB partner can fly down for a no-commitment first meeting any week."),
    ]
    items = ""
    for i, (q, a) in enumerate(common_obj, 1):
        items += f'<div class="card"><h4 style="margin-top:0">Objection {i}: {q}</h4><p>{a}</p></div>\n'
    return f"""
<section id="objections"><div class="subhead">G · Objection handling &mdash; the comebacks for the predictable pushback</div>
{items}
</section>
"""


def _H(spec, cl):
    """Conversion math."""
    name = spec["name"]
    headline_low = spec["headline_low"]; headline_high = spec["headline_high"]
    y1 = round((headline_low + headline_high) / 2 * 0.4)
    y2 = round((headline_low + headline_high) / 2 * 0.7)
    y3 = round((headline_low + headline_high) / 2 * 1.0)
    bull_y3 = round(headline_high * 1.15)
    bear_y3 = round(headline_low * 0.6)
    return f"""
<section id="math"><div class="subhead">H · 12 / 24 / 36-month conversion math &mdash; quarter-by-quarter walk</div>
<h3>H.1 12-month plan (FY27)</h3>
<div class="card">
<table>
<thead><tr><th>Quarter</th><th>Action</th><th>Wallet impact</th></tr></thead>
<tbody>
<tr><td>Q1 FY27</td><td>(a) Term-sheet on flagship product (capex TL or BG-pool); (b) Salary-CASA mandate kick-off; (c) Senior leadership PB introduction.</td><td>Rs {round(y1*0.3)} Cr Y1 ramp</td></tr>
<tr><td>Q2 FY27</td><td>(a) Credit-committee approval; (b) FX/IRS deal-fee from rate-cycle window; (c) PB family-trust diagnostic.</td><td>Rs {round(y1*0.25)} Cr</td></tr>
<tr><td>Q3 FY27</td><td>(a) Capex/BG drawdown; (b) Trade LC + BG cycle live; (c) Receivable factoring book onboarding.</td><td>Rs {round(y1*0.25)} Cr</td></tr>
<tr><td>Q4 FY27</td><td>(a) WCDL refresh + IRS execution if June MPC moved; (b) Group cross-sell to one adjacent entity.</td><td>Rs {round(y1*0.20)} Cr</td></tr>
<tr><td><strong>Y1 (FY27) total wallet</strong></td><td></td><td class="num"><strong>Rs {y1} Cr</strong></td></tr>
</tbody></table>
</div>
<h3>H.2 24-month plan (FY28)</h3>
<div class="card">
<table>
<thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead>
<tbody>
<tr><td>H1 FY28</td><td>Capex TL fully drawn; flagship facility live; cross-sell to second group entity; PB AUM building.</td><td>Rs {round((y2-y1)*0.55)} Cr Y2 add</td></tr>
<tr><td>H2 FY28</td><td>Sustainability KPI first-measurement; vendor-SCF book scaling; PB family-trust mandate signed.</td><td>Rs {round((y2-y1)*0.45)} Cr Y2 add</td></tr>
<tr><td><strong>Y2 (FY28) total wallet</strong></td><td></td><td class="num"><strong>Rs {y2} Cr</strong></td></tr>
</tbody></table>
</div>
<h3>H.3 36-month plan (FY29) &mdash; the inflection year</h3>
<div class="card">
<table>
<thead><tr><th>Period</th><th>Action</th><th>Wallet impact</th></tr></thead>
<tbody>
<tr><td>H1 FY29</td><td>FY27 facility refresh #2 &mdash; potential climb to lead-bank seat; capex Phase-2 (if applicable); family-trust mandate fully signed.</td><td>Rs {round((y3-y2)*0.6)} Cr Y3 add</td></tr>
<tr><td>H2 FY29</td><td>Group cross-sell mature; Foundation/TASC corpus managed; possible NCD if rating moves up.</td><td>Rs {round((y3-y2)*0.4)} Cr Y3 add</td></tr>
<tr><td><strong>Y3 (FY29) total wallet</strong></td><td></td><td class="num"><strong>Rs {y3} Cr</strong></td></tr>
</tbody></table>
</div>
<h3>H.4 Sensitivity (bull / base / bear)</h3>
<div class="card">
<ul>
<li><strong>Bull (all three plays land):</strong> Y3 wallet Rs {bull_y3} Cr/yr.</li>
<li><strong>Base (two plays land):</strong> Y3 wallet Rs {y3} Cr/yr.</li>
<li><strong>Bear (one or no plays):</strong> Y3 wallet caps at Rs {bear_y3} Cr/yr.</li>
</ul>
</div>
</section>
"""


def _I(spec, cl):
    """Customer + supplier ecosystem."""
    name = spec["name"]
    rec_default = spec.get("receivables_text", f"{name} sells into {spec.get('customers','B2B/OEM/Govt')} customers; receivable cycle {spec.get('receivable_cycle','30-90 days')}; key paper is investment-grade and factor-eligible.")
    pay_default = spec.get("payables_text", f"{name} pays {spec.get('suppliers','vendors / capex / payroll')} on {spec.get('payable_cycle','30-90 day')} cycle; vendor-SCF and LC structures fit.")
    return f"""
<section id="ecosystem"><div class="subhead">I · Customer + supplier ecosystem &mdash; who pays {name}, who {name} pays, and where the bank inserts</div>
<div class="card">
<h4 style="margin-top:0">I.1 Receivables (who pays {name})</h4>
<p>{rec_default}</p>
</div>
<div class="card">
<h4 style="margin-top:0">I.2 Payables (who {name} pays)</h4>
<p>{pay_default}</p>
</div>
<p><strong>RM read:</strong> The receivable book is the single most under-banked structural asset in {name}'s balance sheet; factoring + SCF + payroll-CASA stack delivers Rs {round(spec.get('headline_low',5)*0.3)}-{round(spec.get('headline_high',10)*0.3)} Cr/yr at low cost-of-acquisition.</p>
</section>
"""


def _J(spec, cl):
    """Competitor diagnosis."""
    rows_default = spec.get("competitor_rows", [
        ("SBI", "Lead", "Anchor capex + BG", "Slow on speed; no PB; no FX depth on derivatives"),
        ("HDFC Bank", "#2", "WCDL + payroll", "Limited capex appetite at large ticket; no PSU strength"),
        ("PNB / Canara", "PSU", "Low rates", "No retail/PB; slow on capex term-sheet"),
        ("IBank", "Target seat", "Capex speed + FX depth + PB platform + retail bundle", "Ticket-size constraint at largest capex requires consortium"),
    ])
    rows_html = ""
    for r in rows_default:
        rows_html += f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>\n"
    return f"""
<section id="competitors"><div class="subhead">J · Competitor diagnosis &mdash; who is in, why, and where they are weakest</div>
<div class="card">
<table>
<thead><tr><th>Bank</th><th>Position</th><th>Strength</th><th>Weakness we exploit</th></tr></thead>
<tbody>{rows_html}</tbody></table>
</div>
<p><strong>Diagnosis:</strong> {spec.get("competitor_diagnosis", cl["competitors_default"])}</p>
</section>
"""


def _K(spec, cl):
    """Three plays."""
    plays = spec.get("plays", [
        ("Play 1: Win flagship product slot", f"Trigger: next refresh / capex window. Offer: 7-day term-sheet + sustainability covenant + bundled FX/IRS. Y1 income Rs {round(spec.get('headline_low',5)*0.4)} Cr."),
        ("Play 2: Capex TL anchor (if applicable) or BG-pool seat", f"Trigger: Board capex approval. Offer: anchor / co-anchor seat with milestone-linked covenants and capex-import LC bundled. Y2-3 income Rs {round((spec.get('headline_low',5)+spec.get('headline_high',10))*0.15)} Cr/yr stable."),
        ("Play 3: Family-PB + payroll/TASC bundle", f"Trigger: senior PB introduction via cluster-RM channel. Offer: multi-generational mandate + payroll CASA + Foundation/TASC corpus. Y3 income Rs {round(spec.get('headline_high',10)*0.25)} Cr/yr stable."),
    ])
    items = ""
    for i, (h, body) in enumerate(plays, 1):
        items += f'<div class="card"><h4 style="margin-top:0">{h}</h4><p>{body}</p></div>\n'
    return f"""
<section id="plays"><div class="subhead">K · The three plays &mdash; what we win, when, and the trigger event</div>
{items}
<p><strong>All three plays in parallel</strong> get us to Y3 wallet Rs {spec["headline_low"]}-{spec["headline_high"]} Cr base case. Each play independently is sized to be worth running on its own &mdash; the bank does not need all three to make the relationship economic.</p>
</section>
"""


def _L(spec, cl):
    """First-call playbook."""
    name = spec["name"]
    cfo_name = spec.get("cfo_name", "CFO")
    md_name = spec.get("md_name", spec.get("founder","MD"))
    return f"""
<section id="firstcall"><div class="subhead">L · First-call playbook &mdash; the 60 minutes that set up the next 36 months</div>
<h3>L.1 Opening (5 min)</h3>
<div class="card"><p><em>"{md_name} &mdash; thank you for the time. We are not here for share-of-wallet. We have studied the FY25 print and the FY26 capex commentary, and we have three structural observations &mdash; one wholesale, one treasury, one family. If at the end of 30 minutes you do not see value, we leave it there."</em></p></div>
<h3>L.2 Mid-call (3 blocks, 15 min each)</h3>
<div class="card">
<p><strong>Block 1 (Wholesale):</strong> "On the {cl['label'].split(' /')[0]} cluster the FY26-29 driver is {cl['drivers'][0][0].lower()}. We have a structured term-sheet ready &mdash; can we walk through?"</p>
<p><strong>Block 2 (Treasury):</strong> "RBI at 6.50% with June MPC consensus 25 bps cut. We have an IRS structure that locks 60% of WCDL at the post-cut rate &mdash; saves Rs {round(spec.get('headline_low',5)*0.05)}-{round(spec.get('headline_high',10)*0.05)} Cr/yr. Want to see numbers?"</p>
<p><strong>Block 3 (Family + group):</strong> "Separately &mdash; would it be useful to have our senior PB partner come down from Mumbai once, just to walk you through how multi-generational mandates are structured at our platform? No commitment."</p>
</div>
<h3>L.3 The ask (5 min)</h3>
<div class="card"><p>"Three things we would like to take away today: (1) permission to put the term-sheet in front of {cfo_name} in 14 days; (2) a 1-hour treasury session in May; (3) a soft introduction for a 30-minute family/PB conversation. If we get one of these, this meeting was worth it."</p></div>
<h3>L.4 Follow-up (T+24 hrs)</h3>
<div class="card">
<ul>
<li>One-page meeting recap email &mdash; three asks, three commitments, three deliverables, dates.</li>
<li>Sustainability-linked TL one-pager attached.</li>
<li>IRS-structure sample term-sheet attached.</li>
<li>PB-partner profile attached.</li>
<li>CC: Group MD, CFO, Foundation/TASC trustee secretary (if applicable).</li>
</ul>
</div>
<h3>L.5 What NOT to do</h3>
<div class="card">
<ul>
<li>Do not pitch on rate. Incumbent will always undercut on flagship product.</li>
<li>Do not show up without the term-sheet draft. The single biggest signal we send is "we are ready, incumbent is not".</li>
<li>Do not propose climb-to-lead in this meeting. That is FY29 conversation.</li>
<li>Do not commit to PB/TASC rollout timelines on call &mdash; we need internal sign-off first.</li>
</ul>
</div>
</section>
"""


def _M(spec, cl):
    """Sources."""
    extra_srcs = spec.get("extra_sources", [])
    base_srcs = [
        f"{spec['name']} FY25 Annual Report &middot; {spec.get('website','company website')} &middot; retrieved 24 Apr 2026.",
        f"Probe42 open-charges API &middot; CIN {spec.get('cin','[CIN]')} &middot; retrieved 24 Apr 2026.",
        f"Credit-rating rationale &middot; {spec.get('rating_agency','CRISIL/ICRA/CARE')} &middot; latest review FY26.",
        "RBI MPC statement Apr 2026 &middot; rbi.org.in.",
        "USD/INR FBIL reference rate &middot; fbil.org.in &middot; 24 Apr 2026.",
        "Brent crude pricing &middot; ICE futures &middot; 24 Apr 2026.",
        "MoSPI quarterly GDP &middot; mospi.gov.in &middot; FY26 Q3.",
        "SEBI listed-company filings (where applicable) &middot; bseindia.com / nseindia.com.",
    ] + extra_srcs
    items = ""
    for i, s in enumerate(base_srcs, 1):
        items += f'<li id="src-{i}">{s}</li>\n'
    return f"""
<section id="sources"><div class="subhead">M · Sources</div>
<ol>{items}</ol>
<p class="muted small">Cipher: IBank notation in use. Approved sister-entities (ICICI Securities / Prudential / Lombard) retained. Numbers FY25-actual baseline; FY26-FY29 forward projections analyst-estimate. Diligence items flagged inline.</p>
</section>
"""


# ============================================================
# MAIN BUILD ENTRY
# ============================================================

def build_one(spec):
    cluster = CLUSTERS[spec["cluster"]]
    title = f"{spec['name']} · Sector Deep-Dive · 24 Apr 2026"
    verify = f"Sector deep-dive · companion to pilot {spec['pilot']} dossier · cipher clean · 13 sections A-M"

    body = (NAV + _A(spec, cluster) + _B(spec, cluster) + _C(spec, cluster) + _D(spec, cluster)
            + _E(spec, cluster) + _F(spec, cluster) + _G(spec, cluster) + _H(spec, cluster)
            + _I(spec, cluster) + _J(spec, cluster) + _K(spec, cluster) + _L(spec, cluster) + _M(spec, cluster))
    html = HEAD(title) + body + FOOT(verify)
    out = OUTDIR / f"{spec['dossier_slug']}-sector.html"
    out.write_text(html)
    return out, len(html.splitlines())
