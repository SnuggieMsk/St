"""Build `universe-map.html` — the landing page that renders all 499
B-and-above / Potential-IG prospects grouped by industry and rating bucket.

Reads: work/universe_mapped.csv
Writes: universe-map.html (repo root)

Cipher rules (Jhaver PR #1):
  - 'ICICI Bank Limited' from raw CSV replaced by 'IBank' on render.
  - 'ICICI Securities', 'ICICI Prudential', 'ICICI Lombard' retained as-is.
  - No API keys, sheet URLs, or internal DB identifiers in output.
  - No RM / bank-staff names.
"""
from __future__ import annotations
import csv
import html
import re
from collections import defaultdict
from pathlib import Path

from .base import CSS, ref

WORK = Path("/home/user/St/work")
SRC = WORK / "universe_mapped.csv"
OUT = Path("/home/user/St") / "universe-map.html"

# Cipher: ICICI Bank -> IBank (proper-noun only; subsidiaries kept)
ALLOWED = {"ICICI SECURITIES", "ICICI PRUDENTIAL", "ICICI LOMBARD", "ICICI HOME FINANCE"}
RX_ICICI_BANK = re.compile(r"ICICI\s+BANK\s+LIMITED", re.I)
RX_ICICI_BANK_SHORT = re.compile(r"\bICICI\s+BANK\b", re.I)

def cipher(s: str) -> str:
    if not s:
        return ""
    s = RX_ICICI_BANK.sub("IBank", s)
    s = RX_ICICI_BANK_SHORT.sub("IBank", s)
    return s


BUCKET_LABEL = {
    "IG": "Investment Grade (BBB− and above)",
    "HY": "Speculative Grade (BB+ to B−)",
    "POTENTIAL_IG": "Potential Investment Grade (unrated, strong financials)",
}
BUCKET_TAG = {"IG": "pos", "HY": "amber", "POTENTIAL_IG": "cool"}


def floatz(v):
    if v is None or v == "":
        return 0.0
    try:
        return float(str(v).replace(",", ""))
    except ValueError:
        return 0.0


def fmt_inr(v, dp=0):
    f = floatz(v)
    if f == 0 and (v is None or str(v).strip() == ""):
        return "—"
    return f"{f:,.{dp}f}"


def build():
    rows = list(csv.DictReader(SRC.open()))
    by_ind = defaultdict(list)
    for r in rows:
        ind = (r.get("Industry") or "Unclassified").strip() or "Unclassified"
        ind = "IT & ITES" if ind.lower() == "it & ites" else ind
        by_ind[ind].append(r)

    # per-industry: sort by score desc
    for ind in by_ind:
        by_ind[ind].sort(key=lambda x: -floatz(x.get("_score")))

    # top-line counts
    total = len(rows)
    ig = sum(1 for r in rows if r["_bucket"] == "IG")
    hy = sum(1 for r in rows if r["_bucket"] == "HY")
    pig = sum(1 for r in rows if r["_bucket"] == "POTENTIAL_IG")
    n_with_ibank = sum(1 for r in rows if str(r.get("_ibank_rel")).lower() == "true")

    # industry-summary aggregates
    ind_rows = []
    for ind, xs in sorted(by_ind.items(), key=lambda kv: -len(kv[1])):
        toi_total = sum(floatz(r.get("Total Operating Income (Rs Crore)")) for r in xs)
        debt_total = sum(floatz(r.get("Total Debt  (A+B+C+D) (Rs Crore)")) for r in xs)
        ibank_in = sum(1 for r in xs if str(r.get("_ibank_rel")).lower() == "true")
        ind_rows.append((ind, len(xs), toi_total, debt_total, ibank_in))

    # ----- HTML -----
    out = []
    push = out.append
    push("<!doctype html><html lang='en'><head><meta charset='utf-8'>")
    push("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    push("<title>Prospect universe map · 24 April 2026</title>")
    push("<link rel='preconnect' href='https://fonts.googleapis.com'>")
    push("<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>")
    push("<link href='https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Literata:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap' rel='stylesheet'>")
    push(f"<style>{CSS}\n.filterbar{{display:flex;gap:12px;flex-wrap:wrap;padding:12px 14px;background:var(--paper);border:1px solid var(--line);border-radius:6px;margin:14px 0;font-size:.88rem;font-family:var(--mono)}}.filterbar button{{font-family:var(--mono);font-size:.78rem;padding:6px 12px;border-radius:3px;border:1px solid var(--line);background:var(--paper);cursor:pointer;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}}.filterbar button.active{{background:var(--ink);color:#fff;border-color:var(--ink)}}details summary{{cursor:pointer;padding:14px 0;font-family:var(--serif);font-size:1.35rem;color:var(--ink);list-style:none}}details summary::-webkit-details-marker{{display:none}}details summary::before{{content:'▸';margin-right:10px;color:var(--accent);display:inline-block;transition:transform .15s ease}}details[open] summary::before{{transform:rotate(90deg)}}.row{{font-size:.88rem}}.row .bname{{font-weight:600}}.row .bcin{{font-family:var(--mono);font-size:.78rem;color:var(--muted);letter-spacing:.02em}}.hrt{{display:inline-block;width:9px;height:9px;border-radius:50%;vertical-align:middle;margin-right:6px}}.hrt.y{{background:var(--pos)}}.hrt.n{{background:var(--line)}}.ibk{{font-family:var(--mono);font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}}.ibk.y{{color:var(--pos);font-weight:600}}</style>")
    push("</head><body><div class='wrap'>")

    # Hero
    push("<section class='hero'>")
    push("<div class='eyebrow'>Client Acquisition · LCG / PBG South</div>")
    push("<h1>Prospect universe map</h1>")
    push("<p class='lede'>499 Tamil Nadu–anchored companies outside the current RM-mapped book of 154, qualified against a rating floor of B− (long-term) or — for unrated entities — a four-point potential-IG screen (PAT &gt; 0, Net Worth ≥ Rs 100 Cr, Debt / EBITDA ≤ 3.5x, Interest Coverage ≥ 3x). Sourced from the Master Lead Generation sheet cut 8 Sep 2025; MCA registry cross-checked via Probe42 for the top-20 Tier-1 slice. Clustered by industry for shared PESTEL and industry-deep-dive panels. Each name carries the existing IBank charge-holder flag (Probe42 open-charges register).</p>")
    push("<div class='meta'>")
    push(f"<span>Dossier date <strong>24 Apr 2026</strong></span>")
    push(f"<span>Sheet cut <strong>8 Sep 2025</strong></span>")
    push(f"<span>Registry cut <strong>Probe42 Apr 2026 metadata</strong></span>")
    push("</div>")
    push("</section>")

    # Cross-links bar
    _btn = ("padding:8px 14px;border:1px solid var(--accent);border-radius:4px;"
            "color:var(--accent);text-decoration:none")
    push("<div style='display:flex;gap:12px;margin-top:20px;flex-wrap:wrap;font-family:var(--mono);font-size:.84rem'>")
    push(f"<a href='index.html' style='{_btn}'>← Back to index</a>")
    push(f"<a href='india-map.html' style='{_btn}'>India map (geographic view) →</a>")
    push(f"<a href='foxconn-hon-hai-dossier.html' style='{_btn}'>Foxconn dossier →</a>")
    push(f"<a href='kpr-group-dossier.html' style='{_btn}'>KPR Group dossier →</a>")
    push(f"<a href='rkm-powergen-dossier.html' style='{_btn}'>R.K.M Powergen dossier →</a>")
    push("</div>")

    # Headline KPIs
    push("<div class='grid c4' style='margin-top:28px'>")
    push(f"<div class='kpi accent'><div class='k'>Total qualified</div><div class='v num'>{total}</div><div class='sub'>of 991 unmapped names in sheet</div></div>")
    push(f"<div class='kpi pos'><div class='k'>Investment grade</div><div class='v num'>{ig}</div><div class='sub'>BBB- or better (CRISIL / ICRA / CARE / Acuite / IND)</div></div>")
    push(f"<div class='kpi amber'><div class='k'>Speculative (BB+ to B-)</div><div class='v num'>{hy}</div><div class='sub'>Actionable with structured facilities</div></div>")
    push(f"<div class='kpi'><div class='k'>Potential IG (unrated)</div><div class='v num'>{pig}</div><div class='sub'>Four-point screen pass; credit-rating sponsor opportunity</div></div>")
    push("</div>")

    push("<div class='grid c3' style='margin-top:8px'>")
    push(f"<div class='kpi'><div class='k'>IBank existing relationship</div><div class='v num'>{n_with_ibank}</div><div class='sub'>Grow-share candidates (direct charge holder or banking-relationship field)</div></div>")
    push(f"<div class='kpi'><div class='k'>Greenfield acquisition</div><div class='v num'>{total - n_with_ibank}</div><div class='sub'>Zero-wallet relationships; full product-suite pitch</div></div>")
    push(f"<div class='kpi'><div class='k'>Industry clusters</div><div class='v num'>{len(by_ind)}</div><div class='sub'>Aggregating to 7 PESTEL panels</div></div>")
    push("</div>")

    # Industry summary table
    push("<h2>Industry summary</h2>")
    push("<div style='overflow-x:auto'><table>")
    push("<thead><tr><th>Industry cluster</th><th class='num'>Names</th><th class='num'>Aggregate TOI (Rs Cr)</th><th class='num'>Aggregate Debt (Rs Cr)</th><th class='num'>IBank existing</th><th>Jhaver-style PESTEL panel</th></tr></thead><tbody>")
    panel_map = {
        "Manufacturing": "Auto / EMS / Capital Goods (A)",
        "Retail": "Consumer &amp; Retail (F)",
        "IT & ITES": "IT &amp; ITES (G)",
        "Infrastructure": "Infra / Real Estate (H)",
        "Energy & Utilities": "Power &amp; Oil-Gas (C)",
        "Agriculture & Farming": "Textiles &amp; Agri (B)",
        "Healthcare": "Healthcare &amp; Pharma (E)",
        "Services": "Services (I)",
        "Unclassified": "To be cluster-assigned",
    }
    for ind, n, toi, debt, ibk in ind_rows:
        panel = panel_map.get(ind, "— to assign")
        push(f"<tr><td><strong>{html.escape(ind)}</strong></td>"
             f"<td class='num'>{n}</td>"
             f"<td class='num'>{toi:,.0f}</td>"
             f"<td class='num'>{debt:,.0f}</td>"
             f"<td class='num'>{ibk}</td>"
             f"<td>{panel}</td></tr>")
    push("</tbody></table></div>")

    # Legend
    push("<h2>Rating bucket legend</h2>")
    push("<div class='grid c3'>")
    push("<div class='card pos'><strong>Investment grade (IG)</strong> — CRISIL / ICRA / CARE / India Ratings long-term rating <code>BBB-</code> or better after stripping short-term suffix (e.g. <code>BBB+/A2</code> → IG). Bank-facility rating drives Basel risk-weighting; these names attract 20-75% RW in wholesale book.</div>")
    push("<div class='card warn'><strong>Speculative grade (HY)</strong> — <code>BB+</code> down to <code>B-</code>. Addressable with structured facilities (LRD, receivable-backed, BG-backed, ECB), NBFC-led WC, and ratings-sponsor term loans. Higher-yield but also higher provisioning under ECL.</div>")
    push("<div class='card' style='border-left:4px solid var(--cool);background:#e8eef7'><strong>Potential IG</strong> — unrated in the sheet but passes the 4-point screen (PAT &gt; 0, Net Worth ≥ Rs 100 Cr, Debt/EBITDA ≤ 3.5x, Interest Coverage ≥ 3x). Immediate opportunity: rating-sponsor fee income + first-time IBank relationship.</div>")
    push("</div>")

    # Filter bar (CSS-only visual; actual filter is manual via expand/collapse)
    push("<h2>All qualified names by industry</h2>")
    push("<p class='lede'>Expand any industry to see the full company list with rating bucket, financial size, and existing IBank charge-holder flag. Tier-1 names (top 20 by composite opportunity score) are flagged with <code>[T1]</code>. IBank existing relationships are flagged with a green dot and <code>[IBank-IN]</code>.</p>")

    # Identify Tier-1 names for tagging
    with (WORK / "tier1_candidates.csv").open() as f:
        t1 = list(csv.DictReader(f))[:20]
        tier1_cins = {r["CIN"] for r in t1}

    # CIN → dossier mapping for cross-link
    DOSSIER_BY_CIN = {
        "U32204TN2015FTC165627": "foxconn-hon-hai-dossier.html",
        "L17111TZ2003PLC010518": "kpr-group-dossier.html",
        "U18109TZ2020PLC034666": "kpr-group-dossier.html",
        "U40101TN2004PTC054931": "rkm-powergen-dossier.html",
        "U85110TN2020PLC135839": "apollo-healthco-dossier.html",
        "U52393TN2007PTC064830": "caratlane-dossier.html",
        "L28991TZ1986PLC001816": "craftsman-automation-dossier.html",
    }
    # CIN → city_norm mapping (from geocoder output) for india-map deep-link
    import json as _json
    geo_path = WORK / "companies_geo.json"
    CITY_BY_CIN = {}
    if geo_path.exists():
        for c in _json.loads(geo_path.read_text()):
            CITY_BY_CIN[c["cin"]] = c["city_norm"]

    # Per-industry collapsible sections
    for ind, xs in sorted(by_ind.items(), key=lambda kv: -len(kv[1])):
        # open the biggest 3 industries by default
        open_attr = " open" if len(xs) >= 40 else ""
        push(f"<details{open_attr}><summary>{html.escape(ind)} &nbsp;<span class='mono' style='font-size:.82rem;color:var(--muted)'>· {len(xs)} names</span></summary>")
        push("<div style='overflow-x:auto'><table>")
        push("<thead><tr><th>Company</th><th>Bucket</th><th>Rating (LT)</th><th>Agency</th>"
             "<th class='num'>TOI (Cr)</th><th class='num'>Debt (Cr)</th>"
             "<th class='num'>NW (Cr)</th><th class='num'>Debt/EBITDA</th>"
             "<th>IBank</th><th>City</th><th>Open</th></tr></thead><tbody>")
        for r in xs:
            name = cipher(r.get("Company") or "")
            cin = r.get("CIN") or ""
            t1_flag = " <span class='tag accent' style='font-size:.62rem'>T1</span>" if cin in tier1_cins else ""
            dossier = DOSSIER_BY_CIN.get(cin)
            if dossier:
                name_cell = (f"<a href='{dossier}' style='color:var(--accent);text-decoration:none;font-weight:600' "
                             f"title='Open comprehensive dossier'>{html.escape(name)} ↗</a>{t1_flag}")
            else:
                name_cell = f"{html.escape(name)}{t1_flag}"
            bucket = r["_bucket"]
            bucket_tag = BUCKET_TAG[bucket]
            bucket_label_short = {"IG":"IG","HY":"HY","POTENTIAL_IG":"P·IG"}[bucket]
            rating = r.get("_rating_norm") or "—"
            agency = r.get("_rating_source") or "—"
            toi = fmt_inr(r.get("Total Operating Income (Rs Crore)"))
            debt = fmt_inr(r.get("Total Debt  (A+B+C+D) (Rs Crore)"))
            nw = fmt_inr(r.get("Tangible Net Worth (Rs Crore)"))
            d_e = fmt_inr(r.get("Total debt/EBIDTA (times)"), 2)
            is_ibk = str(r.get("_ibank_rel")).lower() == "true"
            ibk_cell = (f"<span class='hrt y'></span><span class='ibk y'>IBank-IN</span>"
                        if is_ibk else f"<span class='hrt n'></span><span class='ibk'>—</span>")
            city_norm = CITY_BY_CIN.get(cin, "")
            from urllib.parse import quote_plus
            map_link = (f"<a href='india-map.html?city={quote_plus(city_norm)}' "
                        f"class='mono' style='font-size:.7rem;color:var(--cool);text-decoration:none' "
                        f"title='Show on India map'>{html.escape(city_norm.title())} ↗</a>"
                        if city_norm else "—")
            dossier_link = (f"<a href='{dossier}' class='mono' style='font-size:.72rem;color:var(--accent);text-decoration:none'>dossier ↗</a>"
                            if dossier else "<span class='mono' style='font-size:.7rem;color:var(--muted)'>—</span>")
            push(f"<tr class='row'>"
                 f"<td><div class='bname'>{name_cell}</div>"
                 f"<div class='bcin'>{html.escape(cin)}</div></td>"
                 f"<td><span class='tag {bucket_tag}'>{bucket_label_short}</span></td>"
                 f"<td class='mono'>{html.escape(rating)}</td>"
                 f"<td class='mono' style='font-size:.78rem'>{html.escape(agency)}</td>"
                 f"<td class='num'>{toi}</td>"
                 f"<td class='num'>{debt}</td>"
                 f"<td class='num'>{nw}</td>"
                 f"<td class='num'>{d_e}</td>"
                 f"<td>{ibk_cell}</td>"
                 f"<td>{map_link}</td>"
                 f"<td>{dossier_link}</td></tr>")
        push("</tbody></table></div></details>")

    # Tier-1 additions outside the TN-499 universe
    extras_path = WORK / "tier1_extras.json"
    if extras_path.exists():
        extras = _json.loads(extras_path.read_text())
        if extras:
            push("<details open><summary>Tier-1 additions &mdash; outside TN-499 universe &nbsp;"
                 f"<span class='mono' style='font-size:.82rem;color:var(--muted)'>· {len(extras)} names</span></summary>")
            push("<p class='lede' style='margin-top:8px'>Names added to the Tier-1 batch on direction, "
                 "headquartered outside the TN-anchored 499-company sheet. These are the largest single-name "
                 "credit relationships sitting in the broader South / East footprint of LCG / PBG franchise.</p>")
            push("<div style='overflow-x:auto'><table>")
            push("<thead><tr><th>Company</th><th>Bucket</th><th>Rating (LT)</th><th>Agency</th>"
                 "<th class='num'>TOI (Cr)</th><th class='num'>Debt (Cr)</th>"
                 "<th class='num'>NW (Cr)</th><th class='num'>Debt/EBITDA</th>"
                 "<th>IBank</th><th>City</th><th>Open</th></tr></thead><tbody>")
            for e in extras:
                cin = e.get("cin", "")
                name = cipher(e.get("company", ""))
                dossier = e.get("dossier")
                name_cell = (f"<a href='{dossier}' style='color:var(--accent);text-decoration:none;font-weight:600'>"
                             f"{html.escape(name)} ↗</a>" + " <span class='tag accent' style='font-size:.62rem'>T1</span>"
                             if dossier else html.escape(name))
                from urllib.parse import quote_plus as _qp
                city_norm = e.get("city_norm", "")
                map_link = (f"<a href='india-map.html?city={_qp(city_norm)}' class='mono' "
                            f"style='font-size:.7rem;color:var(--cool);text-decoration:none'>"
                            f"{html.escape(city_norm.title())} ↗</a>")
                dossier_link = (f"<a href='{dossier}' class='mono' "
                                f"style='font-size:.72rem;color:var(--accent);text-decoration:none'>dossier ↗</a>")
                push(f"<tr class='row'>"
                     f"<td><div class='bname'>{name_cell}</div>"
                     f"<div class='bcin'>{html.escape(cin)}</div></td>"
                     f"<td><span class='tag pos'>IG</span></td>"
                     f"<td class='mono'>{html.escape(e.get('rating',''))}</td>"
                     f"<td class='mono' style='font-size:.78rem'>{html.escape(e.get('rating_source',''))}</td>"
                     f"<td class='num'>{e.get('toi','')}</td>"
                     f"<td class='num'>{e.get('debt','')}</td>"
                     f"<td class='num'>{e.get('nw','')}</td>"
                     f"<td class='num'>N/A</td>"
                     f"<td><span class='hrt n'></span><span class='ibk'>—</span></td>"
                     f"<td>{map_link}</td>"
                     f"<td>{dossier_link}</td></tr>")
            push("</tbody></table></div></details>")

    # Methodology + caveats
    push("<h2>Methodology &amp; caveats</h2>")
    push("<div class='grid c2'>")
    push("<div class='card'><h4>Diff against mapped book</h4><p>Canonical-name match: strip legal suffix (<code>LIMITED</code>, <code>PRIVATE LIMITED</code>, <code>PVT LTD</code>, etc.), collapse whitespace and punctuation, normalise single-letter runs (<code>M M</code> → <code>MM</code>), case-fold. Substring fallback for alias shortenings (e.g. <code>TABLETS (I) LTD</code> ↔ <code>TABLETS INDIA LIMITED</code>). Known same-group overlaps (Rane, Chettinad, Rajalakshmi, Caplin, TAFE, Sun) explicitly excluded at the subsidiary level so the unmapped book does not double-count group members already covered by a parent relationship.</p></div>")
    push("<div class='card'><h4>Rating normalisation</h4><p>Combined long/short-term ratings (e.g. <code>BBB+/A2</code>) split at <code>/</code> and the LT part kept. Modifiers in parentheses (<code>(CE)</code>, <code>(SO)</code>) stripped for bucketing. <code>Withdrawn</code> and <code>Suspended</code> treated as unrated. Sheet ratings pre-date Apr 2026 macro; live refresh required on any name taken to credit committee.</p></div>")
    push("<div class='card'><h4>Potential-IG screen</h4><p>Four-factor pass: (i) last-annual PAT &gt; 0, (ii) Tangible Net Worth ≥ Rs 100 Cr, (iii) Total Debt / EBITDA ≤ 3.5x, (iv) Interest Coverage ≥ 3x (or interest = 0). Active company, negative screens clean. These names are the highest IRR rating-sponsor opportunities — fees at sanction plus IBank-led banker for the first three years.</p></div>")
    push("<div class='card warn'><h4>Exclusions</h4><p>State Road Transport Corps, SEBs, Municipal Corps, CIRP parents (IL&amp;FS lineage), wholly-owned central-PSU subsidiaries with mandated bank panels, and competitor banks and their captives are hard-excluded. 15 banks / captives scrubbed before ranking.</p></div>")
    push("<div class='card'><h4>Opportunity score</h4><p>Composite: 40% log-TOI, 30% log-Debt, 15% log-Open-Charges, 15% IBank-existing relationship. Logs prevent whales dominating the top; the IBank-existing term explicitly rewards both grow-share and greenfield narratives. Tier-1 is the top-20 slice by this score.</p></div>")
    push("<div class='card'><h4>What this map does not yet show</h4><p>This is the <em>qualifying</em> universe. Full Jhaver-depth dossier is produced only for the Tier-1 slice. The remaining ~480 names will attract a 1–2 page brief once the pilot format is approved, and live Probe42 charge-register pulls will be batched in tranches of 50 to respect API pacing.</p></div>")
    push("</div>")

    # Sources
    push("<h2>Sources &amp; data vintage</h2>")
    push("<div class='src-list'><ol>")
    push("<li><strong>Master Lead Generation sheet</strong> · 1,104 rows · sheet metadata last-updated 8 Sep 2025 · 193 columns including CIN, rating (long- &amp; short-term), bank-wise exposure (Axis / BoB / Canara / HDFC / IBank / IndusInd / Kotak / PNB / SBI / Standard Chartered), open-charge summary, P&amp;L / BS line items, FDI / ECB flags, promoter pledge, and negative screens.</li>")
    push("<li><strong>LCG / PBG RM mapping screenshots</strong> · 7 images · 154 existing RM-mapped company names parsed and canonicalised.</li>")
    push("<li><strong>Probe42 open-charges API</strong> · <code>GET /probe_data_api/entities/{CIN}/open-charges</code> · called live for Tier-1 CINs on 24 Apr 2026 · metadata last-updated field retained per-response (Mar &ndash; Apr 2026 range).</li>")
    push("<li><strong>Negative-screen fields from sheet</strong> · Wilful Defaulter, NCLT, Major Default, Stressed Asset Sale, Disqualified Directors U/S 164 · must all read <code>SAFE</code>.</li>")
    push("</ol></div>")

    push("<footer class='foot'>")
    push("<div class='mono'>Prospect universe map · Dossier date 24 April 2026 · LCG / PBG South client-acquisition review.</div>")
    push("<div class='mono' style='margin-top:6px'>Proper-noun cipher: the wholesale bank is rendered as IBank throughout the committed artifact. IBank subsidiaries retained per editorial approval.</div>")
    push("</footer>")
    push("</div></body></html>")

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
