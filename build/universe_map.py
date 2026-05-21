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
        "L51100TN2017PLC118316": "sundaram-clayton-dossier.html",
        "L35921TN1960PLC004175": "wheels-india-dossier.html",
        "U15200TZ2014PLC020554": "milky-mist-dossier.html",
        "L25111TN1982PLC009414": "tvs-srichakra-dossier.html",
        "U40300TN2019FTC186573": "agp-city-gas-dossier.html",
        "U50400TN2018PTC121056": "tvs-mobility-dossier.html",
        "L40101TN1965GOI005389": "cpcl-dossier.html",
        "U34300TN2020PLC140385": "switch-mobility-dossier.html",
        "U29308TN2020FTC178231": "fs-india-solar-dossier.html",
        "U70109TN2021PLC147646": "infopark-properties-dossier.html",
        "U70109TN2021PLC143683": "dalmia-green-vision-dossier.html",
        "U85300TN2017PTC114099": "neuberg-diagnostics-dossier.html",
        "U45101TN2023PTC160276": "tvs-vehicle-mobility-dossier.html",
        "U74999TN2020FTC136376": "tata-electronics-dossier.html",
        "U29244TN2000FTC046255": "caterpillar-india-dossier.html",
        "U34200TN2007PTC072876": "daimler-india-dossier.html",
        "U32309TN2019PTC133300": "salcomp-india-dossier.html",
        "U35999TN1962PTC004928": "brakes-india-dossier.html",
        "L17111TZ1962PLC001183": "precot-limited-dossier.html",
        "U28999TN2009PTC071334": "mohanlal-jewellers-dossier.html",
        "U34103TN2000PTC045537": "ford-india-dossier.html",
        "U74120TN1998PTC041070": "ford-india-dossier.html",
        "U72300TN2001PTC046551": "verizon-dsi-dossier.html",
        "U30007TN2002PTC048391": "sanmina-sci-dossier.html",
        "U67100TN2017PTC134459": "stellantis-india-dossier.html",
        "U50102TN2012PTC189428": "stellantis-india-dossier.html",
        "U29309TN2017PTC149467": "stellantis-india-dossier.html",
        "U72900TN2020FTC189526": "stellantis-india-dossier.html",
        "U27104TN2006PTC060275": "hyundai-steel-india-dossier.html",
        "U27100TN2011PTC081333": "hyundai-steel-india-dossier.html",
        "U72200TN2006PTC058697": "paypal-india-dossier.html",
        "U24100TN2010PLC077127": "greenstar-fertilizers-dossier.html",
        "U29141TN1995PTC030621": "rane-steering-dossier.html",
        "U35999TN1987PTC014600": "zf-rane-auto-dossier.html",
        "U29130TN1997FTC037962": "faurecia-india-dossier.html",
        "U35911TN1997PTC037782": "hanon-automotive-dossier.html",
        "U35999TN1961PLC004678": "lucas-tvs-dossier.html",
        "U35999TN1930PLC005705": "lucas-indian-service-dossier.html",
        "U17111TN1983PLC009973": "ls-mills-dossier.html",
        "U29141TN1984FTC010913": "kone-elevator-dossier.html",
        "U72200TN2000PTC179280": "keimed-dossier.html",
        "U15511TN2007PTC065347": "kals-distilleries-dossier.html",
        "L85110TN1994PLC027366": "dr-agarwal-eye-dossier.html",
        "L30007TN1999PLC043479": "avalon-technologies-dossier.html",
        "L93090TN1994PLC028578": "swelect-energy-dossier.html",
        "L27209TN1986PLC012833": "thejo-engineering-dossier.html",
        "L24290TN2009PLC071563": "chemfab-alkalis-dossier.html",
        "L28920TN1991PLC020232": "ip-rings-dossier.html",
        "U24117TN1952PLC005704": "delphi-tvs-dossier.html",
        "U74999TN2006PTC069356": "nippon-paint-dossier.html",
        "L31901TN1984PLC011021": "india-nippon-electricals-dossier.html",
        "U28991TN2001FTC047397": "borgwarner-india-dossier.html",
        "U28999TN2001PTC047184": "borgwarner-india-dossier.html",
        "U33112TN1983PLC009911": "sanmar-matrix-dossier.html",
        "U50300TN2005PLC056533": "mobis-india-dossier.html",
        "U27105TN1997PTC165626": "basf-catalysts-dossier.html",
        "U34100TN2005FTC078835": "renault-india-dossier.html",
        "U74900TN2006PTC058975": "glovis-india-dossier.html",
        "U29244TN2005PTC058357": "komatsu-india-dossier.html",
        "U50401TN2007PTC064840": "rntbci-dossier.html",
        "U40107TN1982PTC009363": "turbo-energy-tvs-dossier.html",
        "U72900TN2000PTC044462": "bny-mellon-tech-dossier.html",
        "U24111TN1996PTC180780": "praxair-india-dossier.html",
        "U24294TN1931PTC000112": "iff-india-dossier.html",
        "U25119TN2009PTC071454": "michelin-india-dossier.html",
        "U72200TN2010PTC078458": "freshworks-dossier.html",
        "L29308TN2018FLC126510": "tenneco-clean-air-dossier.html",
        "U29199TZ1991PTC008636": "faiveley-transport-dossier.html",
        "U72900TN2015FTC102489": "dxc-india-dossier.html",
        "U24111TN1986PTC123423": "astrazeneca-india-dossier.html",
        "U85110TN2003PTC173618": "omega-healthcare-dossier.html",
        "L15421TZ1983PLC001358": "bannari-amman-sugars-dossier.html",
        "U29199TZ2009PTC015651": "propel-industries-dossier.html",
        "U17111TZ2006PTC012949": "space-textiles-dossier.html",
        "U31909TN2007PTC062621": "byd-india-dossier.html",
        "U31401TN2015PLC143100": "bharat-fih-dossier.html",
        "L34103TN2004PLC054667": "zf-cv-controls-dossier.html",
        "U28112TZ2006PTC013294": "zf-wind-power-dossier.html",
        "U34300TN2007PTC081587": "ge-power-conversion-dossier.html",
        "U29253TN2015PTC184205": "nordex-india-dossier.html",
        "U29199TN1999PTC041877": "danfoss-india-dossier.html",
        "U35999TN2002PTC049333": "seoyon-e-hwa-dossier.html",
        "U29253TN2011PTC084853": "perkins-india-dossier.html",
        "U34300TZ1998PTC015231": "tenneco-automotive-dossier.html",
        "U34300TN2000PTC046158": "mitsuba-india-dossier.html",
        "U15421TN1983PTC010243": "roca-bathroom-dossier.html",
        "U40105TN1996PTC043776": "same-deutz-fahr-dossier.html",
        "U31900TN1985PTC011866": "fuji-electric-dossier.html",
        "L29299TN1987PLC058738": "esab-india-dossier.html",
        # Pilots 151-173 (Siechem + 22 batched new pilots)
        "U67100TN1994PTC027463": "siechem-technologies-dossier.html",
        "L35100TN2008PLC069496": "tube-investments-india-dossier.html",
        "L29224TN1954PLC000318": "carborundum-universal-dossier.html",
        "L24211TN1975PLC006989": "eid-parry-dossier.html",
        "L24120TG1961PLC000892": "coromandel-international-dossier.html",
        "L65993TN1978PLC007576": "cholamandalam-finance-dossier.html",
        "L34101TN1948PLC000105": "ashok-leyland-dossier.html",
        "L25111TN1960PLC004306": "mrf-limited-dossier.html",
        "L65191TN1954PLC002429": "sundaram-finance-dossier.html",
        "L35999TN1962PLC004943": "sundram-fasteners-dossier.html",
        "L34102DL1982PLC129877": "eicher-motors-dossier.html",
        "L26941TN1957PLC003566": "ramco-cements-dossier.html",
        "L72300TN1997PLC037550": "ramco-systems-dossier.html",
        "L26942TN1947PLC000387": "india-cements-dossier.html",
        "L29309TN1996PLC035377": "hyundai-motor-india-dossier.html",
        "U26109TN1997PTC037875": "saint-gobain-india-dossier.html",
        "U40100TN2010PTC075961": "zoho-corporation-dossier.html",
        "L72900MH1992PLC069662": "hexaware-technologies-dossier.html",
        "U72300TN1998PTC041668": "bahwan-cybertek-dossier.html",
        "U45309TN1998PTC046270": "schwing-stetter-india-dossier.html",
        "U28999KA1996PTC020467": "lapp-india-dossier.html",
        "L65991TN1941PLC001128": "kcp-limited-dossier.html",
        "L18101TZ2005PLC012295": "sp-apparels-dossier.html",
        "U24246TN1990PTC046613": "cavinkare-dossier.html",
    }
    # CIN → city_norm / region / mnc mapping (from geocoder output)
    import json as _json
    geo_path = WORK / "companies_geo.json"
    CITY_BY_CIN = {}
    REGION_BY_CIN = {}
    MNC_BY_CIN = {}
    COO_BY_CIN = {}
    if geo_path.exists():
        for c in _json.loads(geo_path.read_text()):
            CITY_BY_CIN[c["cin"]] = c["city_norm"]
            REGION_BY_CIN[c["cin"]] = c.get("region", "ROTN")
            MNC_BY_CIN[c["cin"]] = bool(c.get("mnc", False))
            COO_BY_CIN[c["cin"]] = c.get("country_of_origin", "")

    # Regroup by Region (Chennai / ROTN), then by Industry within region
    # This is the primary organising principle per user direction (24 Apr 2026)
    by_region = {"CHENNAI": {}, "ROTN": {}}
    for ind, xs in by_ind.items():
        for r in xs:
            region = REGION_BY_CIN.get(r.get("CIN",""), "ROTN")
            by_region[region].setdefault(ind, []).append(r)

    # Top-of-list region summary
    n_chennai = sum(len(v) for v in by_region["CHENNAI"].values())
    n_rotn = sum(len(v) for v in by_region["ROTN"].values())
    n_mnc = sum(1 for cin in MNC_BY_CIN if MNC_BY_CIN[cin])
    n_nonmnc = len(MNC_BY_CIN) - n_mnc
    push("<h2>Region &amp; parent-origin split</h2>")
    push("<div class='grid c4'>")
    push(f"<div class='kpi accent'><div class='k'>Chennai cluster</div><div class='v num'>{n_chennai}</div><div class='sub'>Chennai + Sriperumbudur + Kancheepuram + Thiruvallur + Chengalpet + Maraimalai Nagar + Gummidipundi</div></div>")
    push(f"<div class='kpi'><div class='k'>ROTN (Rest of TN)</div><div class='v num'>{n_rotn}</div><div class='sub'>Coimbatore + Tirupur + Erode + Madurai + Salem + Namakkal + Hosur + Krishnagiri + others</div></div>")
    push(f"<div class='kpi'><div class='k'>MNC (foreign parent)</div><div class='v num'>{n_mnc}</div><div class='sub'>Foreign Country-Of-Origin or FTC-suffix CIN</div></div>")
    push(f"<div class='kpi pos'><div class='k'>Non-MNC (Indian promoter)</div><div class='v num'>{n_nonmnc}</div><div class='sub'>Indian parent / promoter-family-led</div></div>")
    push("</div>")

    # Per-region, per-industry collapsible sections
    for region_label, display_name, extra_class in [
        ("CHENNAI", "Chennai cluster &mdash; Chennai + close metros", "accent"),
        ("ROTN", "Rest of Tamil Nadu (ROTN) &mdash; Coimbatore + Tirupur + Erode + Madurai + others", ""),
    ]:
        reg_dict = by_region[region_label]
        reg_count = sum(len(v) for v in reg_dict.values())
        push(f"<h2 style='margin-top:2em'>{display_name} &mdash; {reg_count} names</h2>")
        for ind, xs in sorted(reg_dict.items(), key=lambda kv: -len(kv[1])):
            open_attr = " open" if len(xs) >= 20 else ""
            push(f"<details{open_attr}><summary>{html.escape(ind)} &nbsp;<span class='mono' style='font-size:.82rem;color:var(--muted)'>· {len(xs)} names</span></summary>")
            push("<div style='overflow-x:auto'><table>")
            push("<thead><tr><th>Company</th><th>Bucket</th><th>MNC</th><th>Rating (LT)</th><th>Agency</th>"
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
                is_mnc = MNC_BY_CIN.get(cin, False)
                coo = COO_BY_CIN.get(cin, "") or "Foreign parent"
                coo_title = html.escape(coo)
                if is_mnc:
                    mnc_cell = f"<span class='tag amber' title='{coo_title}'>MNC</span>"
                else:
                    mnc_cell = "<span class='tag' style='background:var(--line);color:var(--muted)'>Non-MNC</span>"
                push(f"<tr class='row'>"
                     f"<td><div class='bname'>{name_cell}</div>"
                     f"<div class='bcin'>{html.escape(cin)}</div></td>"
                     f"<td><span class='tag {bucket_tag}'>{bucket_label_short}</span></td>"
                     f"<td>{mnc_cell}</td>"
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
