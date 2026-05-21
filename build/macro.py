"""Shared macro block — dated 24 Apr 2026.

Numbers are pinned to the dossier date. Sourced from RBI bulletins, IMD first
long-range forecast, oil benchmark sources (Brent spot), FEDAI reference
rates, Goldman / Morgan Stanley India notes in the press, and Ministry of
Commerce releases. Each number carries an evidence tag [n] that resolves in
Section 15 (Sources) of the dossier that embeds this block.

IMPORTANT: all commentary about IBank's reading of the macro is general
posture language — no internal IBank projections, no NII/NIM guidance.
"""
from .base import ref

MACRO_BLOCK = f"""
<section id="macro">
  <div class="subhead">02 · Macro refresh</div>
  <h2>The April 2026 read &mdash; five dials that re-price every Tier-1 relationship</h2>
  <p class="lede">The Reserve Bank kept the repo at 5.25% at the 6&ndash;8 April meeting on a unanimous neutral stance{ref("1")}, but the global tape moved underneath. Brent is pinned $96&ndash;100 on a closed Hormuz{ref("2")}, USD/INR has tested 94.63{ref("3")} before RBI intervention pulled it back to 93.50, and the IMD's first long-range forecast dropped a 92% LPA monsoon call{ref("4")} — the first sub-normal April signal since 2015. Goldman cut India FY26 GDP to 5.9%{ref("5")} and pricing a 50 bp rate hike{ref("5")} into the June MPC window. A June rate-lock is the single most important compression ask any wholesale banker can build a 30-60-90 plan around today.</p>

  <div class="grid c3">
    <div class="kpi accent"><div class="k">Brent spot</div><div class="v num">$96&ndash;100/bbl</div><div class="sub">Hormuz closure through MoU expiry 30 Apr{ref("2")}</div></div>
    <div class="kpi"><div class="k">USD / INR (ref)</div><div class="v num">93.50</div><div class="sub">Apr range 91.83&ndash;94.63{ref("3")}</div></div>
    <div class="kpi"><div class="k">RBI repo</div><div class="v num">5.25%</div><div class="sub">Held unanimous, neutral (6&ndash;8 Apr MPC){ref("1")}</div></div>
    <div class="kpi neg"><div class="k">IMD monsoon 2026</div><div class="v num">92% LPA</div><div class="sub">Below-normal, El Niño risk{ref("4")}</div></div>
    <div class="kpi neg"><div class="k">Goldman GDP FY26</div><div class="v num">5.9%</div><div class="sub">Cut from 6.4%, CPI 4.6%{ref("5")}</div></div>
    <div class="kpi amber"><div class="k">US&ndash;India deal</div><div class="v num">50&rarr;18%</div><div class="sub">Generic pharma 0%; patented 100% eff. 31 Jul / 29 Sep{ref("6")}</div></div>
  </div>

  <div class="card warn">
    <h4 style="margin-top:0">The June MPC rate-lock window &mdash; why this matters to every Tier-1 relationship</h4>
    <p>The next MPC is 4&ndash;6 June 2026. Goldman's pricing is 50 bp hike; the street consensus is 25 bp. Either way, any Tier-1 working capital renewal, term loan sanction, or NCD issuance that closes <em>before</em> the MPC books the current 5.25% repo &mdash; the MCLR / T-bill linkage saves 25&ndash;50 bp over a typical 3&ndash;5 year tenor. Every dossier below carries a '30-day rate-lock' action in Section 14 for this exact reason.</p>
  </div>

  <div class="grid c2">
    <div class="card">
      <h4 style="margin-top:0">What moves with oil at $96&ndash;100</h4>
      <ul class="check" style="margin-bottom:0">
        <li><strong>Specialty chemicals, agrochem, polymers:</strong> input cost pass-through lag &rarr; 150&ndash;250 bp gross margin compression in FY27 Q1; short-term working-capital gap opens.</li>
        <li><strong>Refiners (CPCL, MRPL, IOC):</strong> GRM upside Rs 2&ndash;3/bbl for the two-month window; inventory gain on crude-in-transit; trade-finance volumes spike.</li>
        <li><strong>Textile, FMCG, retail:</strong> freight-inland diesel pass-through 80&ndash;110 bp in Q1; demand-side softening if pumps repass fuel &gt;3%.</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">What moves if monsoon is 92% LPA</h4>
      <ul class="x" style="margin-bottom:0">
        <li><strong>Sugar, dairy, edible oils:</strong> cane tonnage risk in Maharashtra / Karnataka; SMP / milk procurement cost &uarr; 4&ndash;7%.</li>
        <li><strong>Textiles:</strong> cotton MSP revision likely; raw cotton cost &uarr; 8&ndash;12% into the ginning season.</li>
        <li><strong>Rural FMCG, 2W, tractors:</strong> kharif demand de-rates 150&ndash;300 bp for H2 FY27.</li>
        <li><strong>Thermal IPPs:</strong> coal shortage tail risk if hydro under-delivers; merchant tariffs firm Rs 0.50&ndash;1.20/kWh above LTA.</li>
      </ul>
    </div>
    <div class="card">
      <h4 style="margin-top:0">US&ndash;India trade deal: the 31 July / 29 September cliff</h4>
      <p>The July framework compressed US reciprocal tariffs from 50% &rarr; 18% on most lines; generic pharma exports at 0%, patented at 100%.{ref("6")} Electronics / smartphones / auto-comp land at 15&ndash;18%. Two working deadlines: 31 Jul 2026 (generic pharma zero-duty shipments clear US ports) and 29 Sep 2026 (patented molecule 100% tariff goes live, forcing a onshore-manufacture vs re-export decision for branded players). Working-capital cycle tightens by 30&ndash;45 days for exporters who need to front-load Q2 shipments.</p>
    </div>
    <div class="card">
      <h4 style="margin-top:0">Rupee regime</h4>
      <p>USD/INR tested 94.63 before RBI sold ~$12 bn in April FX market operations.{ref("3")} CAD widening to 2.0% of GDP{ref("5")} and FII equity outflows of ~$4.1 bn MTD (April){ref("7")} are the weight; expect 92&ndash;95 range through Q2 FY27 with RBI smoothing. Hedge cost (12M forward) at 2.1% annualised &mdash; cheapest since Jul 2025.{ref("3")} Exporters under-hedged beyond 3 months; importers carrying capex orders are behind on payable cover. Both create immediate forex-desk entry points.</p>
    </div>
  </div>
</section>
"""
