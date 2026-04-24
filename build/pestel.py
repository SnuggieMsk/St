"""PESTEL 360° panels — one per industry cluster.

Each panel is a 6-row × N-column table where columns are the entities in the
Tier-1 cluster. Rows are Political, Economic, Social, Technological,
Environmental, Legal. Each cell maps the factor to a specific P&L / BS line
impact and carries an evidence tag.

Only panels needed for the 3 pilots are defined here; more will be added in
subsequent commits for the remaining 17 dossiers.
"""
from .base import ref


def _cell(header, impact, line_item_delta, cls=""):
    """One PESTEL cell."""
    c = f" {cls}" if cls else ""
    return (f'<td class="pestel-cell{c}">'
            f'<span class="tt">{header}</span>{impact} '
            f'<em style="color:var(--muted)">&mdash; {line_item_delta}</em></td>')


# ============================================================================
# Panel A : Electronics Manufacturing Services (EMS) / Smartphone assembly
# Entities: Foxconn Hon Hai Tech India Mega Dev
# ============================================================================

PESTEL_EMS = f"""
<h3 id="pestel-ems">A · PESTEL 360° &mdash; Electronics Manufacturing Services (EMS) / Smartphone assembly</h3>
<p class="lede">Foxconn's Sriperumbudur plant is the single largest PLI 2.0 beneficiary in TN, co-located with the Apple supplier chain (Tata Electronics Hosur, Pegatron Chengalpattu, Salcomp Chennai). The unit operates on an ultra-thin EBITDA margin (3&ndash;4%) with working capital turned 8&ndash;10x a year; every macro signal hits a specific line.</p>
<div style="overflow-x:auto">
<table>
<thead>
<tr><th style="width:120px">Factor</th><th>Impact on Foxconn Hon Hai TN &mdash; line-item delta</th></tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Political</span></td>
{_cell("US&ndash;India deal 50%&rarr;18%",
  "Smartphone export tariffs to US capped at 15&ndash;18% (effective 31 Jul 2026).{}".format(ref("6")),
  "Export Sales line <strong>+18&ndash;22%</strong> YoY in FY27; freight & port charges tight in Q2")}
</tr>
<tr>
<td><strong>E</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Economic</span></td>
{_cell("USD/INR at 93.50, forward 12M 2.1%",
  "~95% of Foxconn revenue is USD-linked (Apple purchase orders in USD).{}".format(ref("3")),
  "Forex gain <strong>Rs 180&ndash;240 Cr</strong> on unhedged $ flows; hedging uplift 45&ndash;60 bp on EBITDA if 6M rolling cover locked at current forward")}
</tr>
<tr>
<td><strong>S</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Social</span></td>
{_cell("TN Women on Night Shift Bill; dormitory guidelines",
  "~70% of line-workers are women; 3-shift dormitory compliance cost Rs 280&ndash;340 Cr capex over FY27{}".format(ref("8")),
  "Capex FY27 <strong>+Rs 320 Cr</strong>; opex +Rs 80 Cr/yr post-commissioning")}
</tr>
<tr>
<td><strong>T</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Technological</span></td>
{_cell("iPhone 17 ramp; AirPods Pro 3 line; module import",
  "New SMT + FATP lines for A19 Pro SoC assembly; ~Rs 4,200 Cr capex committed{}".format(ref("9")),
  "Gross Block <strong>+Rs 4,200 Cr</strong> by Q3 FY27; depreciation +Rs 420 Cr/yr; IB entry point: ECB hedge + capex term loan")}
</tr>
<tr>
<td><strong>En</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Environmental</span></td>
{_cell("Apple 2030 net-zero supply chain mandate",
  "Apple requires 100% renewable power by 2030; Foxconn TN at ~40% RE via open-access PPAs.{}".format(ref("10")),
  "Green capex Rs 700&ndash;900 Cr FY27&ndash;FY28 (rooftop + offsite PPA); opportunity: green term loan + RE-linked NCD")}
</tr>
<tr>
<td><strong>L</strong><br><span class="mono" style="font-size:.72rem;color:var(--muted)">Legal</span></td>
{_cell("PLI 2.0 disbursement cycle; GST IGST refund lag",
  "PLI claim FY25 ~Rs 560 Cr pending MeitY verification; IGST refund float Rs 1,100&ndash;1,400 Cr typical{}".format(ref("11")),
  "Other Current Assets carries <strong>Rs 1,600 Cr float</strong>; CMS opportunity: GST refund advance + PLI-receivable factoring (Rs 120&ndash;180 Cr NFB)")}
</tr>
</tbody>
</table>
</div>
"""


# ============================================================================
# Panel B : Textiles & Garments / Sugar-Apparel
# Entities: K.P.R. Mill, KPR Sugar & Apparels
# ============================================================================

PESTEL_TEXTILE = f"""
<h3 id="pestel-textile">B · PESTEL 360° &mdash; Textiles &amp; Garments / Sugar&ndash;Apparel vertical integration</h3>
<p class="lede">The KPR Group is a fully vertically integrated cotton-to-garment platform with captive sugar providing ethanol optionality. PESTEL reads differently on mill vs sugar&ndash;apparel; both share the weather floor.</p>
<div style="overflow-x:auto">
<table>
<thead>
<tr><th style="width:120px">Factor</th><th>K.P.R. Mill (textile / garment)</th><th>KPR Sugar &amp; Apparels</th></tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
{_cell("US&ndash;India deal",
  "India garment RCEP lines 0% US MFN from 31 Jul{}".format(ref("6")),
  "Export Sales <strong>+12&ndash;15%</strong> FY27; H&M / Primark order-book +8&ndash;10%")}
{_cell("Ethanol blending EBP-E20",
  "GoI target 20% blending by Oct 2026; SAP revised{}".format(ref("12")),
  "Ethanol realisation Rs 62&ndash;66/L; segmental EBITDA <strong>+Rs 40&ndash;55 Cr</strong>")}
</tr>
<tr>
<td><strong>E</strong></td>
{_cell("Cotton MSP revision",
  "Kharif 2026&ndash;27 MSP up 4.9% (Rs 7,521/qtl Medium Staple){}".format(ref("13")),
  "Raw cotton cost <strong>+Rs 85&ndash;100 Cr</strong> on FY27 volumes; GP margin -110 bp")}
{_cell("Sugar MSP Rs 42/kg floor",
  "Sep 2025 revision held; ethanol price +Rs 3/L to cross-subsidise{}".format(ref("12")),
  "Revenue mix shift: sugar 38%&rarr;32%, ethanol 12%&rarr;19% FY27E")}
</tr>
<tr>
<td><strong>S</strong></td>
{_cell("Labour: migrant wage premium Tirupur",
  "Karnataka / TN minimum wage revisions; migrant retention bonus{}".format(ref("14")),
  "Employee cost <strong>+Rs 18&ndash;22 Cr</strong>; absorbed within 18% EBITDA margin")}
{_cell("Cane farmer payment guarantee",
  "TN SAP Rs 3,500&ndash;3,650/tonne; FRP revision Oct 2026{}".format(ref("15")),
  "Cane payment float <strong>Rs 280&ndash;320 Cr</strong> Q3&ndash;Q4 FY27")}
</tr>
<tr>
<td><strong>T</strong></td>
{_cell("Waterless dyeing / recycled poly",
  "Primark / Inditex mandate; capex Rs 180 Cr FY27",
  "Machinery imports DE/CH; ECB + term loan window")}
{_cell("Drip + precision-ag sensors",
  "Yield +8&ndash;11% per hectare demonstrated{}".format(ref("16")),
  "Capex <strong>Rs 85 Cr</strong> over 2 seasons; possible NABARD subvention")}
</tr>
<tr>
<td><strong>En</strong></td>
{_cell("Monsoon 92% LPA",
  "Cotton acreage risk in MH / Telangana 8&ndash;12% area cut{}".format(ref("4")),
  "Raw cotton cost <strong>+8&ndash;12%</strong>; gross margin -180&ndash;220 bp if passed-through partially")}
{_cell("Cane crush volume",
  "TN crush 2026&ndash;27 at 55&ndash;58 lakh tonnes vs 62 LMT FY26{}".format(ref("17")),
  "Sugar production <strong>-8%</strong>; fixed-cost absorption drops")}
</tr>
<tr>
<td><strong>L</strong></td>
{_cell("EU CBAM / EUDR for cotton",
  "Traceability compliance 2026{}".format(ref("18")),
  "Compliance cost Rs 6&ndash;8 Cr; premium price 3&ndash;5% on EU-compliant cotton lines")}
{_cell("Ethanol purchase agreement (EPA)",
  "OMCs long-term contracts through FY29{}".format(ref("12")),
  "Receivable days <strong>28&rarr;22</strong> once EPA kicks in; CMS opportunity")}
</tr>
</tbody>
</table>
</div>
"""


# ============================================================================
# Panel C : Thermal Power & Independent Power Producers (IPP)
# Entities: R.K.M Powergen
# ============================================================================

PESTEL_POWER = f"""
<h3 id="pestel-power">C · PESTEL 360° &mdash; Thermal Power (IPP)</h3>
<p class="lede">R.K.M Powergen operates 1,440 MW supercritical coal at Uchpinda, Chhattisgarh. Revenue is 80% long-term PPA (TANGEDCO, Haryana DISCOMs), 20% merchant on IEX. PESTEL is dominated by three dials: coal availability, merchant tariff, rate-cycle.</p>
<div style="overflow-x:auto">
<table>
<thead>
<tr><th style="width:120px">Factor</th><th>Impact on R.K.M Powergen &mdash; line-item delta</th></tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
{_cell("Coal India FSA re-negotiation FY27",
  "New coal pricing formula with ceiling linked to Richards Bay index; domestic linkage tight{}".format(ref("19")),
  "Fuel cost <strong>+Rs 280&ndash;340 Cr</strong> FY27 if spot top-up needed; PPA variable-cost pass-through covers 70%")}
</tr>
<tr>
<td><strong>E</strong></td>
{_cell("RBI repo 5.25% (neutral); June MPC +25&ndash;50 bp pricing",
  "Existing PFC debt @ 9.75% PLR-linked; any repo cut repriced by +45 bp lag{}".format(ref("1,5")),
  "Interest cost <strong>-Rs 28&ndash;35 Cr/yr</strong> on Rs 4,400 Cr debt if full 25 bp cycle passed through; refi window critical")}
</tr>
<tr>
<td><strong>S</strong></td>
{_cell("TN load growth 8.2% YoY",
  "Summer 2026 peak demand 19.8 GW (prev 18.3 GW){}".format(ref("20")),
  "PLF <strong>85%&rarr;91%</strong> May&ndash;Jul; merchant realisation Rs 5.80&ndash;6.40/kWh; top-line <strong>+Rs 110&ndash;150 Cr</strong>")}
</tr>
<tr>
<td><strong>T</strong></td>
{_cell("FGD retrofit compliance Dec 2026",
  "CPCB mandate for SO2 scrubbers; Rs 40&ndash;50 lakh/MW capex{}".format(ref("21")),
  "Capex commitment <strong>Rs 600&ndash;720 Cr</strong> over 18 months; funding gap: incremental term loan + ECB")}
</tr>
<tr>
<td><strong>En</strong></td>
{_cell("Monsoon 92% LPA; hydro under-perf",
  "Thermal share of grid dispatch 69%&rarr;73% H2 FY27{}".format(ref("4,20")),
  "Merchant volume <strong>+18&ndash;22%</strong>; IEX realisation firms Rs 0.50&ndash;1.20/kWh above LTA")}
</tr>
<tr>
<td><strong>L</strong></td>
{_cell("DISCOM payment security mechanism (LPS)",
  "RBI's ECL-linked discom payment cycle forces 30-day pay{}".format(ref("22")),
  "Receivable days <strong>92&rarr;66</strong> over FY27; Rs 240&ndash;290 Cr working-capital cash released")}
</tr>
</tbody>
</table>
</div>
"""


# ============================================================================
# Mapping helpers
# ============================================================================

def panel_for(industry_key: str) -> str:
    return {
        "EMS": PESTEL_EMS,
        "TEXTILE": PESTEL_TEXTILE,
        "POWER": PESTEL_POWER,
    }.get(industry_key, "")
