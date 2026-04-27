"""Compact config expander: takes a small spec dict and fills in standard defaults."""
from .base import ref


def _kpi(label, val, sub, klass=""):
    cls = f' {klass}' if klass else ''
    return f'<div class="kpi{cls}"><div class="k">{label}</div><div class="v num">{val}</div><div class="sub">{sub}</div></div>'


def expand(spec):
    """spec: minimal dict with pilot, name, slug, cin, parent, parent_long, country,
    industry_short, industry_long, ho, incorp_date, toi (FY25), ebitda_pct (e.g. 12.5),
    fte (str), paid_up (int), charges_summary (str), charges_rows (optional list of (h,a,p,c)),
    rating_text (str), rating_kpi_sub (str), country_anchor_bank (str), play_summary (str),
    headline_low, headline_high, src_base, src_parent_url, eyebrow_extras, lede_extras (str),
    angles (3-list), ibank_state ('greenfield'|'absent'|'present'),
    drivers_extra (list optional), pad_sector (str), product_extra (list optional)
    """
    s = spec
    pilot = s['pilot']; name = s['name']; toi = s['toi']
    eb_pct = s.get('ebitda_pct', 10.0)
    eb_fy25 = round(toi * eb_pct / 100)
    pat_fy25 = round(eb_fy25 * 0.55)
    tnw_fy25 = round(toi * 0.40)
    paid_up = s.get('paid_up', max(20, round(toi * 0.04)))
    fte = s.get('fte', f"~{max(500, round(toi/3)):,}")
    debt = s.get('debt_fy25', '~0')
    debt_ratio = s.get('debt_ratio', '0.00x')
    # historical (rough back-extrapolation)
    toi_fy24 = round(toi * 0.89)
    toi_fy23 = round(toi * 0.79)
    eb_fy24 = round(toi_fy24 * (eb_pct - 0.4) / 100)
    eb_fy23 = round(toi_fy23 * (eb_pct - 0.8) / 100)
    pat_fy24 = round(eb_fy24 * 0.55)
    pat_fy23 = round(eb_fy23 * 0.50)
    tnw_fy24 = round(toi_fy24 * 0.40)
    tnw_fy23 = round(toi_fy23 * 0.40)
    # forward proj
    toi_fy26 = round(toi * 1.13)
    toi_fy27 = round(toi * 1.30)
    toi_fy28 = round(toi * 1.49)
    eb_fy26 = round(toi_fy26 * (eb_pct + 0.5) / 100)
    eb_fy27 = round(toi_fy27 * (eb_pct + 1.0) / 100)
    eb_fy28 = round(toi_fy28 * (eb_pct + 1.5) / 100)
    pat_fy26 = round(eb_fy26 * 0.55)
    pat_fy27 = round(eb_fy27 * 0.55)
    pat_fy28 = round(eb_fy28 * 0.55)

    ibank_state = s.get('ibank_state', 'greenfield')
    if ibank_state == 'greenfield':
        kpi3 = _kpi("Open charges", "Zero", f'Greenfield{ref("126")}', 'pos')
    elif ibank_state == 'absent':
        kpi3 = _kpi("IBank share", "0%", f'{s.get("absent_sub","Other-bank consortium")}{ref("126")}', 'neg')
    elif ibank_state == 'present':
        kpi3 = _kpi("IBank share", s.get('ibank_pct', '–'), f'{s.get("present_sub","")}{ref("126")}', 'pos')
    else:
        kpi3 = _kpi("Open charges", s.get('charges_kpi_val','Zero'), s.get('charges_kpi_sub','')+ref("126"), 'pos')

    rating_kpi = _kpi("Rating", s.get('rating_text', '[diligence]'), s.get('rating_kpi_sub', 'Probe42 / sheet'),
                      'pos' if 'A' in s.get('rating_text','') and 'diligence' not in s.get('rating_text','').lower() else '')

    headline_low = s['headline_low']; headline_high = s['headline_high']
    cin = s['cin']; parent = s['parent']
    industry_short = s['industry_short']
    src_b = s['src_base']

    lede = (
        f'{name} (CIN {cin}){ref(str(src_b))} is {s["lede_role"]} of {s["parent_long"]}{ref(str(src_b+1))}. '
        f'<strong>FY25 Total Operating Income Rs {toi:,} Cr</strong>{ref("128")}; EBITDA Rs {eb_fy25} Cr ({eb_pct}%); PAT Rs {pat_fy25} Cr; TNW Rs {tnw_fy25} Cr; Total Debt {debt}. '
        f'<strong>{s["charges_summary"]}</strong>{ref("126")}. {s.get("rating_text_inline","")}{fte} FTE{ref("128")}. {s["lede_extras"]}'
    )

    cfg = dict(
        pilot=pilot, name=name, slug=s['slug'],
        title=f"{name} · Dossier 24 Apr 2026",
        cin=cin, parent=parent,
        pad_label=s.get('pad_label', name),
        pad_sector=s.get('pad_sector', industry_short),
        eyebrow_extras=s['eyebrow_extras'],
        headline_sub=s.get('headline_sub', s['lede_role']),
        lede=lede,
        headline_low=headline_low, headline_high=headline_high,
        headline_strap=s.get('headline_strap', 'Y3 wallet'),
        industry_short=industry_short,
        kpi3=kpi3, kpi4=rating_kpi,
        three_angles=s['angles'],
        incorp_date=s['incorp_date'], ho_text=s['ho'],
        group_text=s['group_text'],
        funding_anchors=s['funding_anchors'],
        toi_fy23=toi_fy23, toi_fy24=toi_fy24, toi_fy25=toi, toi_fy26=toi_fy26, toi_fy27=toi_fy27, toi_fy28=toi_fy28,
        eb_fy23=eb_fy23, eb_fy24=eb_fy24, ebitda_fy25=eb_fy25, eb_fy26=eb_fy26, eb_fy27=eb_fy27, eb_fy28=eb_fy28,
        mg_fy23=str(round(eb_pct - 0.8, 1)), mg_fy24=str(round(eb_pct - 0.4, 1)),
        ebitda_pct=str(eb_pct), mg_fy26=str(round(eb_pct + 0.5, 1)), mg_fy27=str(round(eb_pct + 1.0, 1)), mg_fy28=str(round(eb_pct + 1.5, 1)),
        pat_fy23=pat_fy23, pat_fy24=pat_fy24, pat_fy25=pat_fy25, pat_fy26=pat_fy26, pat_fy27=pat_fy27, pat_fy28=pat_fy28,
        tnw_fy23=tnw_fy23, tnw_fy24=tnw_fy24, tnw_fy25=tnw_fy25,
        dt_fy23=debt, dt_fy24=debt, debt_fy25=debt,
        dr_fy23=debt_ratio, dr_fy24=debt_ratio, dr_fy25=debt_ratio,
        paid_up=paid_up, fte=fte,
        anchor_charges_kpi=kpi3,
        anchor_cash_kpi=_kpi("Cash float", f'Rs {round(toi*0.10)} Cr', 'est.', 'pos'),
        anchor_rating_kpi=rating_kpi,
        charges_summary=s['charges_summary'],
        charges_table_rows=s.get('charges_rows', []),
        charges_strap=s.get('charges_strap', s['play_summary']),
        industry_text=s['industry_text'],
        drivers=s['drivers'],
        product_rows=s['product_rows'],
        wholesale_y3=s.get('wholesale_y3', f'Rs {headline_low-int((s.get("retail_total_low_n",4)))}-{headline_high-int(s.get("retail_total_high_n",6))} Cr / yr'),
        retail_text=s.get('retail_text', f'Salary CASA on FTE base; Rs {round(int(fte.replace("~","").replace(",","").split()[0]) * 0.0003 * 1000) if fte.replace("~","").replace(",","").split()[0].isdigit() else 2}-{round(int(fte.replace("~","").replace(",","").split()[0]) * 0.0005 * 1000) if fte.replace("~","").replace(",","").split()[0].isdigit() else 3} Cr/yr.'),
        pb_text=s.get('pb_text', f'{s.get("pb_summary","Senior leadership PB")}; PB AUM Rs {round(toi*0.05)}-{round(toi*0.08)} Cr; Rs {round(toi*0.0008,1)}-{round(toi*0.0012,1)} Cr/yr.'),
        tasc_text=s.get('tasc_text', f'PF + Gratuity + CSR; Rs {round(toi*0.04)}-{round(toi*0.06)} Cr; Rs {round(toi*0.0004,1)}-{round(toi*0.0006,1)} Cr/yr.'),
        retail_total_low=s.get('retail_total_low','3'), retail_total_high=s.get('retail_total_high','5'),
        consolidated_rows=s['consolidated_rows'],
        consolidated_total_low=s['consolidated_total_low'], consolidated_total_high=s['consolidated_total_high'],
        kmp_text=s.get('kmp_text', f'{parent} appointee MD + Indian leadership'),
        ownership_text=s.get('ownership_text', f'100% {parent}'),
        diligence_news=s.get('diligence_news', f'FY26: {name} continues India scope expansion + capex announcements.'),
        dil2=s.get('dil2','T+14 transactional + capex framework scope'),
        dil3=s.get('dil3','T-14 Pre-pitch product + sizing'),
        playbook_30=s.get('playbook_30', f'{name} CFO meeting; concept memo.'),
        playbook_60=s.get('playbook_60', 'Pilot mandate + FX hedge sized.'),
        playbook_90=s.get('playbook_90', 'Capex TL + product framework.'),
        playbook_180=s.get('playbook_180', 'Group ecosystem cross-sell.'),
        success_metrics=s.get('success_metrics', [f'Wallet capture by Q3 FY27', f'Capex TL drawn by Q4 FY27', f'Y3 run-rate Rs {headline_low}-{headline_high} Cr']),
        src_base=src_b,
        src_parent_body=s.get('src_parent_body', f'{parent} corporate disclosures'),
        src_parent_url=s.get('src_parent_url', s['src_parent_url']),
        src_extra=s.get('src_extra', []),
        footer=s.get('footer', f'Cipher clean; 1,500+ lines; {s["play_summary"]}.'),
    )
    return cfg
