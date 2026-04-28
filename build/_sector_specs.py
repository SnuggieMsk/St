"""Per-company sector-deepdive specs (149 entries, Bannari excluded — bespoke).

Each spec: dict with name, dossier_slug, pilot, cluster, headline_low/high, position,
plus optional bespoke knobs (walking_in, plays, hooks, competitor_rows, etc.).
"""

# Format: (slug, name, pilot, cluster, lo, hi, position, optional_extras)
ROWS = [
    # EMS / Electronics
    ("abi-showatech", "ABI-Showatech (India)", 113, "ems", 4, 7, "greenfield"),
    ("amphenol-omniconnect", "Amphenol Omniconnect", 122, "ems", 5, 9, "greenfield"),
    ("avalon-technologies", "Avalon Technologies", 96, "ems", 6, 11, "present", {"ibank_pct":"~12%","incumbent":"SBI"}),
    ("bharat-fih", "Bharat FIH", 16, "ems", 18, 32, "absent", {"incumbent":"Citi+SBI"}),
    ("foxconn-hon-hai", "Foxconn Hon Hai (Sriperumbudur)", 22, "ems", 28, 48, "greenfield"),
    ("igarashi-motors", "Igarashi Motors India", 130, "ems", 5, 9, "greenfield"),
    ("lnw-india", "LNW India (electronics)", 145, "ems", 4, 8, "greenfield"),
    ("salcomp-india", "Salcomp India", 119, "ems", 8, 14, "greenfield"),
    ("sanmina-sci", "Sanmina-SCI India", 120, "ems", 9, 16, "greenfield"),
    ("tata-electronics", "Tata Electronics (TEPL)", 12, "ems", 35, 60, "absent", {"incumbent":"SBI lead"}),

    # Auto / Components / OEM
    ("borgwarner-india", "BorgWarner India", 56, "auto", 6, 11, "greenfield"),
    ("brakes-india", "Brakes India", 70, "auto", 8, 14, "present", {"ibank_pct":"~10%","incumbent":"SBI"}),
    ("byd-india", "BYD India", 24, "auto", 10, 18, "greenfield"),
    ("daebu-automotive-seat", "Daebu Automotive Seat", 99, "auto", 4, 7, "greenfield"),
    ("daechang-seat", "Daechang Seat", 100, "auto", 4, 7, "greenfield"),
    ("daeseung-autoparts", "Daeseung Autoparts", 101, "auto", 3, 6, "greenfield"),
    ("daimler-india", "Daimler India CV", 26, "auto", 12, 22, "absent", {"incumbent":"DBS+SBI"}),
    ("delphi-tvs", "Delphi-TVS Diesel Systems", 71, "auto", 5, 9, "present", {"ibank_pct":"~8%"}),
    ("faurecia-india", "Faurecia India", 57, "auto", 6, 11, "greenfield"),
    ("ford-india", "Ford India (Chennai mfg revival)", 27, "auto", 14, 26, "greenfield"),
    ("freudenberg-nok", "Freudenberg-NOK", 124, "auto", 5, 9, "greenfield"),
    ("hanon-automotive", "Hanon Automotive Systems India", 102, "auto", 5, 9, "greenfield"),
    ("hl-klemove", "HL Klemove", 103, "auto", 4, 8, "greenfield"),
    ("hyundai-wia", "Hyundai-WIA India", 104, "auto", 6, 11, "greenfield"),
    ("india-motor-parts", "India Motor Parts & Accessories", 134, "auto", 4, 7, "present", {"ibank_pct":"~9%"}),
    ("india-nippon-electricals", "India Nippon Electricals", 135, "auto", 4, 7, "greenfield"),
    ("ip-rings", "IP Rings", 137, "auto", 3, 6, "greenfield"),
    ("jayabheri-auto", "Jayabheri Auto Parts", 138, "auto", 3, 6, "greenfield"),
    ("komos-automotive", "Komos Automotive India", 105, "auto", 4, 7, "greenfield"),
    ("kun-auto", "Kun Auto (Hyundai dealer)", 80, "auto", 3, 6, "present", {"ibank_pct":"~10%"}),
    ("lucas-indian-service", "Lucas Indian Service", 72, "auto", 4, 7, "present", {"ibank_pct":"~10%"}),
    ("lucas-tvs", "Lucas TVS", 67, "auto", 6, 11, "present", {"ibank_pct":"~12%","position_sub":"3rd of 5-bank"}),
    ("michelin-india", "Michelin India", 30, "auto", 8, 14, "greenfield"),
    ("mitsuba-india", "Mitsuba India", 125, "auto", 4, 7, "greenfield"),
    ("mobis-india", "Mobis India (Hyundai-Mobis)", 25, "auto", 9, 16, "greenfield"),
    ("nemak", "Nemak India", 117, "auto", 5, 9, "greenfield"),
    ("ngc-transmission", "NGC Transmission", 142, "auto", 3, 6, "greenfield"),
    ("pyung-hwa", "Pyung Hwa India", 106, "auto", 3, 6, "greenfield"),
    ("rane-steering", "Rane Steering Systems", 68, "auto", 5, 9, "present", {"ibank_pct":"~11%"}),
    ("renault-india", "Renault India", 28, "auto", 10, 18, "absent", {"incumbent":"BNP+SBI"}),
    ("rntbci", "RNTBCI (Renault-Nissan Tech BC India)", 29, "auto", 8, 14, "greenfield"),
    ("seoyon-e-hwa", "Seoyon E-Hwa", 107, "auto", 4, 7, "greenfield"),
    ("stellantis-india", "Stellantis India", 31, "auto", 9, 16, "greenfield"),
    ("sundaram-clayton", "Sundaram-Clayton", 65, "auto", 7, 12, "present", {"ibank_pct":"~13%"}),
    ("switch-mobility", "Switch Mobility (Ashok Leyland EV)", 66, "auto", 6, 11, "greenfield"),
    ("taeyang-metal", "Taeyang Metal Industrial", 108, "auto", 3, 6, "greenfield"),
    ("tenneco-automotive", "Tenneco Automotive India", 58, "auto", 5, 9, "greenfield"),
    ("tenneco-clean-air", "Tenneco Clean Air India", 59, "auto", 5, 9, "greenfield"),
    ("tvs-mobility", "TVS Mobility", 64, "auto", 8, 14, "present", {"ibank_pct":"~12%"}),
    ("tvs-srichakra", "TVS Srichakra", 132, "auto", 5, 9, "present", {"ibank_pct":"~10%"}),
    ("tvs-vehicle-mobility", "TVS Vehicle Mobility Solutions", 133, "auto", 4, 8, "greenfield"),
    ("turbo-energy-tvs", "Turbo Energy (TVS Group)", 131, "auto", 4, 7, "greenfield"),
    ("visteon-electronics", "Visteon Automotive Electronics", 60, "auto", 5, 9, "greenfield"),
    ("visteon-tech-svc", "Visteon Technical & Services", 61, "auto", 4, 7, "greenfield"),
    ("wheels-india", "Wheels India", 69, "auto", 6, 10, "present", {"ibank_pct":"~11%"}),
    ("zf-cv-controls", "ZF CV Controls India", 62, "auto", 5, 9, "greenfield"),
    ("zf-rane-auto", "ZF Rane Automotive", 63, "auto", 5, 9, "greenfield"),
    ("glovis-india", "Glovis India (Hyundai logistics)", 35, "logistics", 5, 9, "greenfield"),

    # GCC / IT services
    ("andritz-tech", "Andritz Technologies (GCC)", 109, "gcc", 4, 8, "greenfield"),
    ("bny-mellon-tech", "BNY Mellon Technology India", 32, "gcc", 8, 14, "greenfield"),
    ("dxc-india", "DXC India", 86, "gcc", 6, 11, "absent", {"incumbent":"Citi+HSBC"}),
    ("freshworks", "Freshworks India", 14, "gcc", 12, 22, "absent", {"incumbent":"Citi+SCB"}),
    ("htc-global", "HTC Global Services", 87, "gcc", 5, 9, "greenfield"),
    ("mindsprint", "Mindsprint", 88, "gcc", 4, 8, "greenfield"),
    ("movate", "Movate (formerly CSS Corp)", 89, "gcc", 5, 9, "greenfield"),
    ("omega-healthcare", "Omega Healthcare Management Services", 84, "gcc", 6, 11, "greenfield"),
    ("paypal-india", "PayPal India", 33, "gcc", 7, 13, "absent", {"incumbent":"Citi+JPMorgan"}),
    ("rr-donnelley", "RR Donnelley India", 90, "gcc", 5, 9, "greenfield"),
    ("tiger-analytics", "Tiger Analytics", 85, "gcc", 6, 11, "greenfield"),
    ("verizon-dsi", "Verizon Data Services India", 34, "gcc", 9, 16, "absent", {"incumbent":"Citi+JPMorgan"}),

    # Pharma / Healthcare / Diagnostics
    ("access-healthcare", "Access Healthcare", 82, "gcc", 5, 9, "greenfield"),
    ("apollo-healthco", "Apollo HealthCo", 75, "healthcare", 7, 13, "present", {"ibank_pct":"~11%"}),
    ("appasamy", "Appasamy Associates (ophthalmic)", 81, "pharma", 4, 7, "greenfield"),
    ("astrazeneca-india", "AstraZeneca Pharma India", 13, "pharma", 8, 14, "absent", {"incumbent":"HSBC+SBI"}),
    ("athenahealth", "athenahealth Technology India", 83, "gcc", 5, 9, "greenfield"),
    ("dr-agarwal-eye", "Dr Agarwal's Eye Hospital", 78, "healthcare", 5, 9, "present", {"ibank_pct":"~9%"}),
    ("icon-clinical", "ICON Clinical Research India", 110, "pharma", 4, 8, "greenfield"),
    ("neuberg-diagnostics", "Neuberg Diagnostics", 79, "healthcare", 4, 8, "greenfield"),
    ("keimed", "Keimed (Apollo distribution)", 77, "healthcare", 6, 11, "present", {"ibank_pct":"~10%"}),
]


ROWS += [
    # Specialty chemicals / Petroleum / Industrial gases
    ("basf-catalysts", "BASF Catalysts India", 17, "chem", 7, 12, "greenfield"),
    ("chemfab-alkalis", "Chemfab Alkalis", 76, "chem", 5, 9, "present", {"ibank_pct":"~9%"}),
    ("cpcl", "Chennai Petroleum Corporation (CPCL)", 11, "chem", 12, 22, "absent", {"incumbent":"SBI+Indian Bank"}),
    ("iff-india", "IFF (Intl Flavors & Fragrances) India", 18, "chem", 6, 11, "greenfield"),
    ("indian-additives", "Indian Additives Ltd (IAL)", 136, "chem", 4, 8, "present", {"ibank_pct":"~8%"}),
    ("nippon-paint", "Nippon Paint India", 19, "chem", 7, 12, "greenfield"),
    ("praxair-india", "Praxair India (Linde)", 20, "chem", 6, 11, "greenfield"),
    ("symrise", "Symrise India", 21, "chem", 5, 9, "greenfield"),
    ("kals-distilleries", "Kals Distilleries", 139, "chem", 3, 6, "greenfield"),
    ("agp-city-gas", "AGP City Gas", 92, "chem", 4, 8, "greenfield"),
    ("sanmar-matrix", "Sanmar Matrix Metals", 121, "chem", 5, 9, "present", {"ibank_pct":"~10%"}),

    # Agri / FMCG / Textiles / Edible oils
    ("avt-mccormick", "AVT McCormick", 15, "agri", 5, 9, "greenfield"),
    ("bhartiya-international", "Bhartiya International (leather)", 74, "agri", 4, 8, "greenfield"),
    ("grace-mart", "Grace Mart (FMCG/retail)", 126, "retail", 3, 6, "greenfield"),
    ("greenstar-fertilizers", "Greenstar Fertilizers", 127, "agri", 5, 9, "greenfield"),
    ("k-h-exports", "K H Exports", 140, "agri", 4, 7, "greenfield"),
    ("kpr-group", "KPR Group", 73, "agri", 8, 14, "present", {"ibank_pct":"~12%"}),
    ("ktv-edible-oils", "KTV Health Food / KTV Edible Oils", 141, "agri", 4, 7, "greenfield"),
    ("ls-mills", "LS Mills (textile)", 144, "agri", 4, 7, "greenfield"),
    ("milky-mist", "Milky Mist Dairy Food", 146, "agri", 5, 9, "greenfield"),
    ("prakash-silks", "Prakash Silks", 148, "agri", 3, 6, "greenfield"),
    ("space-textiles", "Space Textiles", 149, "agri", 3, 6, "greenfield"),
    ("precot-limited", "Precot Limited", 150, "agri", 4, 7, "greenfield"),
    ("shri-sabhari", "Shri Sabhari (FMCG)", 147, "agri", 3, 6, "greenfield"),

    # Engineering / Capital goods / Power / Renewable
    ("caterpillar-india", "Caterpillar India", 36, "engg", 8, 14, "greenfield"),
    ("craftsman-automation", "Craftsman Automation", 37, "engg", 7, 12, "present", {"ibank_pct":"~11%"}),
    ("danfoss-india", "Danfoss India", 38, "engg", 5, 9, "greenfield"),
    ("doosan-bobcat", "Doosan Bobcat India", 111, "engg", 4, 8, "greenfield"),
    ("esab-india", "ESAB India", 39, "engg", 5, 9, "greenfield"),
    ("faiveley-transport", "Faiveley Transport India", 112, "engg", 4, 7, "greenfield"),
    ("flender-drives", "Flender Drives India", 123, "engg", 4, 7, "greenfield"),
    ("fuji-electric", "Fuji Electric India", 40, "engg", 4, 7, "greenfield"),
    ("ge-power-conversion", "GE Power Conversion India", 41, "engg", 5, 9, "greenfield"),
    ("grundfos-pumps", "Grundfos Pumps India", 42, "engg", 4, 7, "greenfield"),
    ("kingfa-science", "Kingfa Science & Technology India", 43, "engg", 5, 9, "greenfield"),
    ("komatsu-india", "Komatsu India", 44, "engg", 5, 9, "greenfield"),
    ("kone-elevator", "KONE Elevator India", 45, "engg", 6, 11, "greenfield"),
    ("madras-engineering", "Madras Engineering Industries", 143, "engg", 4, 7, "greenfield"),
    ("perkins-india", "Perkins India (engines)", 46, "engg", 5, 9, "greenfield"),
    ("propel-industries", "Propel Industries", 128, "engg", 4, 7, "greenfield"),
    ("schneider-electric-systems", "Schneider Electric Systems India", 47, "engg", 7, 12, "greenfield"),
    ("thejo-engineering", "Thejo Engineering", 129, "engg", 3, 6, "greenfield"),
    ("valmet", "Valmet India", 48, "engg", 4, 7, "greenfield"),
    ("hyundai-steel-india", "Hyundai Steel India", 118, "engg", 6, 11, "greenfield"),
    ("rkm-powergen", "RKM Powergen", 116, "engg", 7, 12, "greenfield"),
    ("dalmia-green-vision", "Dalmia Green Vision", 114, "engg", 5, 9, "greenfield"),
    ("j-ray-mcdermott", "J Ray McDermott India", 115, "engg", 6, 11, "greenfield"),
    ("lnt-geostructure", "L&T Geostructure", 49, "engg", 5, 9, "greenfield"),
    ("nordex-india", "Nordex India (wind)", 50, "engg", 5, 9, "greenfield"),
    ("zf-wind-power", "ZF Wind Power India", 51, "engg", 4, 8, "greenfield"),
    ("fs-india-solar", "First Solar India", 52, "engg", 6, 11, "greenfield"),
    ("murata-electronics", "Murata Electronics India", 53, "ems", 5, 9, "greenfield"),
    ("swelect-energy", "Swelect Energy Systems", 54, "engg", 4, 7, "greenfield"),
    ("same-deutz-fahr", "Same Deutz-Fahr India", 55, "engg", 4, 7, "greenfield"),
    ("mkk-metal", "MKK Metal Sectionals", 145, "engg", 3, 5, "greenfield"),

    # Real estate / Industrial parks / SEZ / Hospitality
    ("imc-limited", "IMC Limited", 95, "realestate", 4, 7, "greenfield"),
    ("infopark-properties", "Infopark Properties (Chennai TPark)", 97, "realestate", 5, 9, "greenfield"),
    ("mahindra-world-city", "Mahindra World City", 93, "realestate", 6, 11, "present", {"ibank_pct":"~10%"}),
    ("sipcot", "SIPCOT (TN PSU industrial parks)", 94, "realestate", 5, 9, "greenfield"),
    ("buzzworks", "Buzzworks (co-working)", 98, "realestate", 3, 6, "greenfield"),
    ("integrated-service-point", "Integrated Service Point India (Hyundai logistics)", 35, "logistics", 4, 7, "greenfield"),

    # Logistics / Shipping / Distribution
    ("cma-cgm", "CMA-CGM India (shipping)", 23, "logistics", 6, 11, "absent", {"incumbent":"BNP+SCB"}),
    ("setc", "SETC Fleet (Sundaram Logistics)", 130, "logistics", 4, 7, "present", {"ibank_pct":"~9%"}),

    # Jewellery / Retail / Consumer
    ("accentiv", "Accentiv (consumer rewards)", 9, "retail", 3, 6, "greenfield"),
    ("anixter", "Anixter India (distribution)", 10, "logistics", 4, 7, "greenfield"),
    ("caratlane", "CaratLane Trading (Tata Group)", 8, "retail", 6, 11, "present", {"ibank_pct":"~10%"}),
    ("mohanlal-jewellers", "Mohanlal Jewellers", 7, "retail", 4, 7, "greenfield"),
    ("roca-bathroom", "Roca Bathroom Products", 6, "retail", 4, 7, "greenfield"),
    ("albonair", "Albonair India", 5, "auto", 3, 6, "greenfield"),

    # Defence
    ("armoured-vehicles-nigam", "Armoured Vehicles Nigam Ltd (AVNL)", 91, "defence", 22, 38, "greenfield"),

    # Healthcare entities not above
    # already included
]

# Generate cluster_label inferences for KPI: pad-sector inheritance from cluster
# The dossier has all the financial detail; sector file is meeting-prep companion.

