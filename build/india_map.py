"""Build `india-map.html` — interactive India map with city markers.

Reads:  work/cities_agg.json + work/companies_geo.json
Writes: india-map.html (repo root)

UX:
  - SVG India outline + Tamil Nadu highlighted
  - 39 city markers, area sized by company count
  - Click a marker → right-side panel populates with companies in that city
  - Each company row has tag (IG/HY/Potential-IG/Tier-1/IBank-in)
  - Tier-1 companies link to their dossier (target=_self)
  - Filter chips: bucket × industry × IBank-rel
  - Search box (substring match against company name)
"""
import json
from pathlib import Path
from .base import CSS

OUT = Path("/home/user/St") / "india-map.html"
WORK = Path("/home/user/St/work")

# ---- India outline (simplified ~50-point polygon, degrees) ---------------
# Lng/lat pairs, clockwise from NW (Kashmir).
INDIA = [
    (74.0,35.5),(76.5,35.0),(78.0,34.5),(80.0,33.0),(78.5,31.0),(80.5,30.5),
    (83.0,30.0),(85.0,29.0),(88.0,27.5),(89.5,26.5),(92.0,27.5),(94.5,28.0),
    (96.5,29.0),(97.5,28.5),(97.0,27.0),(95.0,25.5),(94.0,23.5),(94.5,21.5),
    (92.5,22.0),(91.5,22.5),(90.0,22.0),(88.5,22.0),(87.0,21.0),(87.0,19.0),
    (85.5,19.5),(84.0,17.0),(81.0,16.0),(80.0,13.0),(79.5,11.0),(79.0,9.5),
    (78.0,8.0),(77.5,8.2),(76.5,9.0),(75.5,11.5),(74.5,13.0),(74.0,14.0),
    (73.0,15.5),(72.5,17.5),(72.5,19.0),(72.0,21.0),(69.0,21.5),(68.5,22.5),
    (68.0,23.5),(70.0,23.0),(70.5,24.0),(68.5,25.0),(70.0,27.0),(71.0,28.5),
    (74.0,30.0),(74.0,32.0),
]

# ---- Tamil Nadu outline --------------------------------------------------
TN = [
    (80.4,13.5),(80.0,13.0),(79.5,11.0),(79.5,10.0),(78.5,9.5),(78.0,8.5),
    (77.5,8.1),(77.5,8.5),(76.8,9.5),(76.5,11.0),(76.5,12.0),(77.0,13.0),
    (77.5,13.5),(78.5,13.0),(79.5,13.5),
]

# Projection: lng/lat → SVG x/y in 1000×1000 viewBox covering India bbox
LNG_MIN, LNG_MAX = 67.5, 98.0
LAT_MIN, LAT_MAX = 6.0, 37.5
VW, VH = 1000, 1000

def proj(lng: float, lat: float):
    x = (lng - LNG_MIN) / (LNG_MAX - LNG_MIN) * VW
    y = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * VH
    return x, y

def path_from(points):
    pts = [proj(lng, lat) for lng, lat in points]
    head = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    rest = " ".join(f"L {x:.1f} {y:.1f}" for x, y in pts[1:])
    return head + " " + rest + " Z"

def build():
    cities = json.loads((WORK / "cities_agg.json").read_text())
    companies = json.loads((WORK / "companies_geo.json").read_text())

    # Wire dossier links for in-universe Tier-1 names
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
    }
    # Patch dossier links + tier1 flags inside each city's companies list
    for city in cities:
        for co in city.get("companies", []):
            cin = co.get("cin", "")
            if cin in DOSSIER_BY_CIN:
                co["dossier"] = DOSSIER_BY_CIN[cin]
                co["tier1"] = True

    # Merge Tier-1 extras (companies added outside the TN-499 sheet)
    extras_path = WORK / "tier1_extras.json"
    if extras_path.exists():
        extras = json.loads(extras_path.read_text())
        for e in extras:
            # Add to cities aggregate
            city = e["city_norm"]
            existing = next((c for c in cities if c["city"] == city), None)
            ex_co = {
                "cin": e["cin"], "company": e["company"], "industry": e["industry"],
                "bucket": e["bucket"], "rating": e["rating"], "ibank_in": e.get("ibank_in", False),
                "tier1": True, "dossier": e.get("dossier"), "toi": e.get("toi", ""),
            }
            if existing:
                existing["count"] += 1
                existing["ig"] += 1 if e["bucket"] == "IG" else 0
                existing["hy"] += 1 if e["bucket"] == "HY" else 0
                existing["pig"] += 1 if e["bucket"] == "POTENTIAL_IG" else 0
                existing["companies"].insert(0, ex_co)
            else:
                cities.append({
                    "city": city, "lat": e["lat"], "lng": e["lng"],
                    "count": 1,
                    "ig": 1 if e["bucket"] == "IG" else 0,
                    "hy": 1 if e["bucket"] == "HY" else 0,
                    "pig": 1 if e["bucket"] == "POTENTIAL_IG" else 0,
                    "ibank_in": 1 if e.get("ibank_in") else 0,
                    "companies": [ex_co],
                })
            companies.append({**e, "_score": float(e.get("score", "0") or "0")})

    # ---- HTML ----
    o = []
    a = o.append
    a("<!doctype html><html lang='en'><head><meta charset='utf-8'>")
    a("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    a("<title>India map · prospect locator · 24 April 2026</title>")
    a("<link rel='preconnect' href='https://fonts.googleapis.com'>")
    a("<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>")
    a("<link href='https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Literata:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap' rel='stylesheet'>")
    # CSS — base + map specific
    a(f"<style>{CSS}\n")
    a("""
.maplayout{display:grid;grid-template-columns:1fr 420px;gap:18px;margin-top:18px}
@media (max-width:1100px){.maplayout{grid-template-columns:1fr}}
.mapwrap{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:8px;position:relative}
.mapwrap svg{display:block;width:100%;height:auto;background:#f0ede4}
.mapland{fill:#dcd6c2;stroke:#9a8f72;stroke-width:1}
.maptn{fill:#f5e6e8;stroke:var(--accent);stroke-width:1.5}
.mapdot{cursor:pointer;transition:opacity .15s ease,r .15s ease;stroke:var(--accent);stroke-width:1;fill:rgba(122,31,43,.65)}
.mapdot.chennai-cluster{fill:rgba(28,78,128,.75);stroke:var(--cool);stroke-width:1.5}
.mapdot:hover{opacity:.85;stroke-width:2}
.mapdot.active{fill:var(--accent);stroke:#3a0d14;stroke-width:2}
.mapdot.chennai-cluster.active{fill:var(--cool);stroke:#0d2840}
.mapdot.dim{opacity:.18}
.maplabel{font-family:var(--mono);font-size:9px;fill:#1a1a1a;pointer-events:none}
.maplabel.faint{fill:#666;font-size:8px}
.legend{position:absolute;top:12px;right:12px;background:rgba(255,255,255,.95);border:1px solid var(--line);border-radius:6px;padding:10px;font-size:.78rem;font-family:var(--mono);max-width:220px}
.legend .lrow{display:flex;align-items:center;gap:8px;margin:3px 0}
.legend .ldot{width:10px;height:10px;border-radius:50%;background:rgba(122,31,43,.65);border:1px solid var(--accent)}
.legend .ldot.lg{width:18px;height:18px}
.legend .ldot.md{width:13px;height:13px}
.panel{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:14px;max-height:780px;overflow-y:auto;position:sticky;top:14px}
.panel h3{font-family:var(--serif);margin:0 0 6px;font-size:1.4rem;color:var(--accent)}
.panel .pcount{font-family:var(--mono);color:var(--muted);font-size:.78rem;margin-bottom:14px;display:block}
.panel .filterbar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px;font-family:var(--mono);font-size:.72rem}
.panel .filterbar button{padding:4px 9px;border-radius:3px;border:1px solid var(--line);background:#fff;cursor:pointer;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.panel .filterbar button.active{background:var(--ink);color:#fff;border-color:var(--ink)}
.panel input[type=search]{width:100%;padding:7px 10px;border:1px solid var(--line);border-radius:4px;font-family:var(--mono);font-size:.82rem;margin-bottom:10px;background:#fff}
.panel .crow{padding:9px 0;border-bottom:1px dashed var(--line);font-size:.84rem}
.panel .crow:last-child{border-bottom:none}
.panel .cname{font-weight:600;color:var(--ink);text-decoration:none;display:inline-block;margin-bottom:4px;line-height:1.3}
.panel .cname.dossier-link{color:var(--accent)}
.panel .cname.dossier-link::after{content:' ↗';font-size:.78rem}
.panel .cmeta{font-family:var(--mono);font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.panel .ccin{font-family:var(--mono);font-size:.66rem;color:var(--muted);margin-top:3px;letter-spacing:.02em}
.tag{display:inline-block;padding:2px 6px;border-radius:3px;font-family:var(--mono);font-size:.65rem;font-weight:600;text-transform:uppercase;margin-right:4px}
.tag.ig{background:#dff0e3;color:var(--pos)}
.tag.hy{background:#fce6c6;color:var(--amber)}
.tag.pig{background:#dde6f3;color:var(--cool)}
.tag.t1{background:var(--accent);color:#fff}
.tag.ibk{background:#dff0e3;color:var(--pos)}
.crosslinks{display:flex;gap:12px;margin-top:14px;flex-wrap:wrap;font-family:var(--mono);font-size:.82rem}
.crosslinks a{padding:8px 14px;border:1px solid var(--accent);border-radius:4px;color:var(--accent);text-decoration:none}
.crosslinks a:hover{background:var(--accent);color:#fff}
""")
    a("</style></head><body><div class='wrap'>")

    # Hero
    a("<section class='hero'>")
    a("<div class='eyebrow'>Geographic locator · 499 prospects · April 2026</div>")
    a("<h1>India map · prospect-office locator</h1>")
    a("<p class='lede'>Each circle on the India map is a city in which one or more qualifying prospects has its corporate office. Marker area is proportional to the number of qualifying companies in that city. Click any marker to populate the right-hand panel with the company list at that location, with one-click navigation to the comprehensive dossier (where one exists in the Tier-1 pilot batch). All 499 names are headquartered in Tamil Nadu, the LCG / PBG South franchise footprint.</p>")
    # region + MNC counts for summary line
    n_chennai = sum(1 for c in companies if c.get("region") == "CHENNAI")
    n_rotn = sum(1 for c in companies if c.get("region") == "ROTN")
    n_mnc = sum(1 for c in companies if c.get("mnc"))
    n_nonmnc = len(companies) - n_mnc
    a("<div class='meta'>")
    a("<span>Dossier date <strong>24 Apr 2026</strong></span>")
    a(f"<span>Chennai cluster <strong>{n_chennai}</strong></span>")
    a(f"<span>ROTN <strong>{n_rotn}</strong></span>")
    a(f"<span>MNC <strong>{n_mnc}</strong></span>")
    a(f"<span>Non-MNC <strong>{n_nonmnc}</strong></span>")
    a("<span>Tier-1 pilot dossiers <strong>20 of 20 complete</strong></span>")
    a("</div>")
    a("</section>")

    # Cross-links
    a("<div class='crosslinks'>")
    a("<a href='index.html'>← Back to index</a>")
    a("<a href='universe-map.html'>Universe map (table view)</a>")
    a("<a href='foxconn-hon-hai-dossier.html'>Foxconn dossier →</a>")
    a("<a href='kpr-group-dossier.html'>KPR Group dossier →</a>")
    a("<a href='rkm-powergen-dossier.html'>R.K.M Powergen dossier →</a>")
    a("</div>")

    a("<div class='maplayout'>")

    # ----- Map column -----
    a("<div class='mapwrap'>")
    a(f"<svg viewBox='0 0 {VW} {VH}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='India map showing 39 city markers'>")
    # India outline
    a(f"<path class='mapland' d='{path_from(INDIA)}'/>")
    # TN highlight
    a(f"<path class='maptn' d='{path_from(TN)}'/>")

    # State labels
    a(f"<text class='maplabel faint' x='{proj(78,15)[0]}' y='{proj(78,15)[1]}' text-anchor='middle'>INDIA</text>")
    a(f"<text class='maplabel' x='{proj(78.7,11.0)[0]}' y='{proj(78.7,11.0)[1]}' text-anchor='middle' font-weight='700' fill='var(--accent)'>TAMIL NADU</text>")

    # Markers
    import math
    max_count = max(c["count"] for c in cities)
    for c in cities:
        x, y = proj(c["lng"], c["lat"])
        # Marker radius: sqrt scaling, min 5, max 36
        r = 5 + 31 * math.sqrt(c["count"] / max_count)
        cname = c["city"]
        cluster_cls = "chennai-cluster" if c.get("region") == "CHENNAI" else ""
        a(f"<circle class='mapdot {cluster_cls}' data-city=\"{cname}\" data-region=\"{c.get('region','ROTN')}\" cx='{x:.1f}' cy='{y:.1f}' r='{r:.1f}'>")
        a(f"<title>{cname} · {c['count']} prospects · {c['ig']} IG / {c['hy']} HY / {c['pig']} P-IG · {c['ibank_in']} IBank-in</title>")
        a("</circle>")
        # Label only larger markers
        if c["count"] >= 8:
            a(f"<text class='maplabel' x='{x:.1f}' y='{y - r - 4:.1f}' text-anchor='middle'>{cname}</text>")
            a(f"<text class='maplabel faint' x='{x:.1f}' y='{y + r + 11:.1f}' text-anchor='middle'>{c['count']}</text>")

    a("</svg>")

    # Legend overlay
    a("<div class='legend'>")
    a("<div style='font-weight:700;margin-bottom:6px;text-transform:uppercase;letter-spacing:.05em;font-size:.7rem'>Region colour</div>")
    a("<div class='lrow'><span class='ldot' style='background:rgba(28,78,128,.75);border-color:var(--cool)'></span><span>Chennai cluster (320)</span></div>")
    a("<div class='lrow'><span class='ldot'></span><span>ROTN &mdash; Rest of TN (179)</span></div>")
    a("<div style='border-top:1px dashed var(--line);margin-top:6px;padding-top:6px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;font-size:.7rem'>Marker size = # prospects</div>")
    a("<div class='lrow'><span class='ldot lg'></span><span>Chennai · 249</span></div>")
    a("<div class='lrow'><span class='ldot md'></span><span>Coimbatore · 56</span></div>")
    a("<div class='lrow'><span class='ldot'></span><span>Small (1&ndash;10 prospects)</span></div>")
    a("<div style='border-top:1px dashed var(--line);margin-top:6px;padding-top:6px;color:var(--muted)'>Click any marker to load the city panel</div>")
    a("</div>")

    a("</div>")  # end mapwrap

    # ----- Panel column -----
    a("<aside class='panel' id='panel'>")
    a("<h3 id='ptitle'>Click a marker to begin</h3>")
    a("<span class='pcount' id='pcount'>The map currently shows <strong>39 cities</strong> across Tamil Nadu, hosting <strong>499 qualifying prospects</strong>.</span>")
    a("<input type='search' id='psearch' placeholder='Search company in current city…' aria-label='Search company name' disabled>")
    a("<div class='filterbar' id='pfilter'>")
    a("<button data-bk='all' class='active'>All</button>")
    a("<button data-bk='IG'>IG</button>")
    a("<button data-bk='HY'>HY</button>")
    a("<button data-bk='POTENTIAL_IG'>P-IG</button>")
    a("<button data-bk='ibank'>IBank-IN</button>")
    a("<button data-bk='tier1'>Tier-1</button>")
    a("<button data-bk='mnc'>MNC</button>")
    a("<button data-bk='nonmnc'>Non-MNC</button>")
    a("</div>")
    a("<div class='filterbar' id='pregion' style='margin-top:-6px;font-size:.72rem'>")
    a("<span style='padding:6px 10px;color:var(--muted);font-weight:600'>REGION:</span>")
    a("<button data-rg='all' class='active'>All Cities</button>")
    a("<button data-rg='CHENNAI'>Chennai cluster</button>")
    a("<button data-rg='ROTN'>ROTN</button>")
    a("</div>")
    a("<div id='plist'></div>")
    a("</aside>")

    a("</div>")  # end maplayout

    # Methodology
    a("<h2>Map methodology</h2>")
    a("<div class='grid c2'>")
    a("<div class='card'><h4>Geocoding</h4><p>Corporate-office cities from the sheet&rsquo;s <code>City</code> field were normalised through an alias dictionary that collapses casing variants (CHENNAI / Chennai / chennai), strips administrative suffixes (CITY CORPORATION, TALUK, DIST), maps neighbourhood names to their parent city (Saidapet → Chennai, Tambaram → Chennai, Pallipalayam → Erode), and unifies common spelling variants (Tiruppur → Tirupur, Kanchipuram → Kancheepuram). 108 raw values resolved to 39 unique geocoded cities. Coordinates are city-centroid lat/lng (WGS84) plotted via simple linear projection over India&rsquo;s bounding box.</p></div>")
    a("<div class='card'><h4>Plant vs corporate office</h4><p>This map shows <strong>corporate office</strong> location, which is the entity&rsquo;s registered address. Several Tier-1 names operate at materially different physical plant locations &mdash; e.g. R.K.M Powergen has its Chennai HO mapped here but its 1,440 MW thermal plant at Uchpinda, Chhattisgarh; Foxconn&rsquo;s registered office and Sriperumbudur plant are co-located. Plant-level locations are described in the comprehensive dossier per entity.</p></div>")
    a("<div class='card'><h4>Marker sizing</h4><p>Marker radius scales as <code>5 + 31·√(count / max_count)</code>, ensuring small clusters remain visible while the Chennai cluster (249 prospects) is dominant but not overwhelming. Labels appear only for cities with &ge; 8 prospects to maintain readability.</p></div>")
    a("<div class='card'><h4>Cross-navigation</h4><p>Each company row in the panel: (a) company name links to its dossier when a Tier-1 dossier exists; (b) tags show rating bucket and IBank-existing status. Tier-1 status is sourced from the top-20 ranked candidates; only the three pilot dossiers (Foxconn, KPR Group, R.K.M Powergen) are currently published. Subsequent dossiers will be added as the format is signed off.</p></div>")
    a("</div>")

    a("<footer class='foot'>")
    a("<div class='mono'>India map &middot; LCG / PBG South prospect-office locator &middot; 24 April 2026</div>")
    a("<div class='mono' style='margin-top:6px'>Cipher: the wholesale bank is rendered as IBank throughout the artifact.</div>")
    a("</footer>")
    a("</div>")  # wrap

    # ---- JS data + interactivity ----
    a("<script>")
    a(f"const CITIES = {json.dumps(cities)};")
    a("""
const byName = Object.fromEntries(CITIES.map(c => [c.city, c]));
let active = null;
let currentBucketFilter = 'all';
let currentRegionFilter = 'all';

function tagFor(c){
  const tags = [];
  if(c.tier1) tags.push("<span class='tag t1'>T1</span>");
  if(c.bucket==='IG') tags.push("<span class='tag ig'>IG</span>");
  if(c.bucket==='HY') tags.push("<span class='tag hy'>HY</span>");
  if(c.bucket==='POTENTIAL_IG') tags.push("<span class='tag pig'>P-IG</span>");
  if(c.ibank_in) tags.push("<span class='tag ibk'>IBank-IN</span>");
  if(c.mnc) {
    const coo = c.country_of_origin ? ` (${c.country_of_origin.split(',')[0]})` : '';
    tags.push(`<span class='tag' style='background:#fce6c6;color:var(--amber)' title='${coo}'>MNC${coo}</span>`);
  } else {
    tags.push("<span class='tag' style='background:var(--line);color:var(--muted)'>Non-MNC</span>");
  }
  return tags.join('');
}

function passes(c){
  if(currentBucketFilter==='all') return true;
  if(currentBucketFilter==='ibank') return c.ibank_in;
  if(currentBucketFilter==='tier1') return c.tier1;
  if(currentBucketFilter==='mnc') return c.mnc;
  if(currentBucketFilter==='nonmnc') return !c.mnc;
  return c.bucket === currentBucketFilter;
}

function render(city, q){
  const list = document.getElementById('plist');
  if(!city){ list.innerHTML=''; return; }
  const term = (q||'').toLowerCase().trim();
  const cs = city.companies.filter(c => passes(c) && (!term || c.company.toLowerCase().includes(term)));
  if(cs.length === 0){
    list.innerHTML = "<div style='padding:20px;color:var(--muted);text-align:center;font-style:italic'>No matches in current filter</div>";
    return;
  }
  let html = '';
  for(const c of cs){
    const linkOpen = c.dossier ? `<a class='cname dossier-link' href='${c.dossier}'>` : `<span class='cname'>`;
    const linkClose = c.dossier ? '</a>' : '</span>';
    const toi = c.toi ? `Rs ${parseFloat(c.toi).toLocaleString('en-IN', {maximumFractionDigits:0})} Cr TOI` : '—';
    html += `<div class='crow'>
      ${linkOpen}${c.company}${linkClose}<br>
      <span class='cmeta'>${c.industry} · ${c.rating} · ${toi}</span><br>
      ${tagFor(c)}
      <div class='ccin'>${c.cin}</div>
    </div>`;
  }
  list.innerHTML = html;
}

function selectCity(name){
  const city = byName[name];
  if(!city) return;
  active = city;
  document.querySelectorAll('.mapdot').forEach(d => d.classList.toggle('active', d.dataset.city===name));
  document.getElementById('ptitle').textContent = city.city;
  document.getElementById('pcount').innerHTML = `<strong>${city.count}</strong> prospects · ${city.ig} IG · ${city.hy} HY · ${city.pig} P-IG · <strong>${city.ibank_in}</strong> IBank-existing`;
  const search = document.getElementById('psearch');
  search.disabled = false;
  search.value = '';
  search.placeholder = `Search company in ${city.city}…`;
  render(city, '');
}

document.querySelectorAll('.mapdot').forEach(d => {
  d.addEventListener('click', () => selectCity(d.dataset.city));
});
document.getElementById('psearch').addEventListener('input', e => render(active, e.target.value));
document.querySelectorAll('#pfilter button').forEach(b => {
  b.addEventListener('click', () => {
    document.querySelectorAll('#pfilter button').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    currentBucketFilter = b.dataset.bk;
    render(active, document.getElementById('psearch').value);
  });
});
document.querySelectorAll('#pregion button').forEach(b => {
  b.addEventListener('click', () => {
    document.querySelectorAll('#pregion button').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    currentRegionFilter = b.dataset.rg;
    // Dim markers not in the selected region
    document.querySelectorAll('.mapdot').forEach(d => {
      const city = d.dataset.city;
      const cobj = byName[city];
      if(!cobj || currentRegionFilter==='all' || cobj.region===currentRegionFilter){
        d.classList.remove('dim');
      } else {
        d.classList.add('dim');
      }
    });
  });
});

// Honour ?city=NAME query param if present, else default to Chennai (largest cluster)
const params = new URLSearchParams(window.location.search);
const initial = (params.get('city') || 'CHENNAI').toUpperCase();
selectCity(initial in byName ? initial : 'CHENNAI');
""")
    a("</script>")
    a("</body></html>")

    OUT.write_text("\n".join(o), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
