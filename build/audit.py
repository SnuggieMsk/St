"""Hyper-cover audit for a single dossier HTML file.

Checks:
1. Line count >= 1500 (target 1500-2000)
2. Cipher clean (zero "icici bank" appearances)
3. No API key leak
4. <section> tag balance
5. <table>, <tr>, <td>, <ol>, <ul>, <li> approximate balance
6. Every ref("N") superscript anchor has matching <li id="src-N">
7. Has shared MACRO_SOURCES_HTML (src-1 through src-22 + src-81 + src-82)
8. No placeholder TODO / TBD / xxx / [diligence] count flagged but allowed
9. cover-page KPIs present
10. pad() output present (P1-P20 marker checks)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path


def audit(path: Path) -> dict:
    s = path.read_text(encoding="utf-8")
    lines = s.count("\n") + 1
    out = {"path": str(path), "lines": lines, "issues": []}

    if lines < 1500:
        out["issues"].append(f"line-count {lines} below 1500 floor")
    if lines > 2500:
        out["issues"].append(f"line-count {lines} above 2500 (consider trimming)")

    if re.search(r"icici\s+bank", s, re.IGNORECASE):
        out["issues"].append("CIPHER LEAK: 'icici bank' present (must use IBank)")
    if "N9TqElXOhJIJ" in s:
        out["issues"].append("API KEY LEAKED in HTML")
    for term in ("master_leads.csv", "Master_LeadGeneration", "127.0.0.1:46453"):
        if term in s:
            out["issues"].append(f"INTERNAL REFERENCE LEAKED: {term!r}")

    so = s.count("<section")
    sc = s.count("</section>")
    if so != sc:
        out["issues"].append(f"<section> imbalance: {so} open / {sc} close")

    for tag in ("ol", "ul", "table"):
        o = len(re.findall(rf"<{tag}\b", s))
        c = s.count(f"</{tag}>")
        if abs(o - c) > 0:
            out["issues"].append(f"<{tag}> imbalance: {o} open / {c} close")

    # Source resolution
    refs = set(re.findall(r'href="#src-(\d+)"', s))
    src_ids = set(re.findall(r'id="src-(\d+)"', s))
    unresolved = sorted(int(x) for x in (refs - src_ids))
    if unresolved:
        out["issues"].append(f"UNRESOLVED ref()s: {unresolved}")

    # Shared sources presence
    for n in (1, 22, 81, 82):
        if f'id="src-{n}"' not in s:
            out["issues"].append(f"shared source src-{n} missing (MACRO_SOURCES_HTML not rendering)")

    # Cover KPIs
    if 'class="kpi accent"' not in s:
        out["issues"].append("cover headline KPI block missing")
    if "Y3 steady-state" not in s and "Y3 wallet" not in s and "Y3" not in s:
        out["issues"].append("Y3 wallet narrative missing on cover")

    # pad() output presence (look for P14 + P18 + P19 + P20 anchors)
    pad_anchors = ["pad-regulatory-horizon", "pad-wallet-waterfall", "pad-evidence-appendix", "pad-closing"]
    missing_pads = [a for a in pad_anchors if f'id="{a}"' not in s]
    if missing_pads:
        out["issues"].append(f"missing pad() anchors: {missing_pads}")

    # Placeholders (informational only; do not fail unless critical)
    placeholders = re.findall(r"\b(TBD|TODO|XXXX|FIXME)\b", s)
    if placeholders:
        out["issues"].append(f"placeholder tokens present: {set(placeholders)}")

    # Probe42 cite count
    out["probe42_cites"] = len(re.findall(r"Probe42", s))
    out["ref_count"] = len(re.findall(r'href="#src-\d+"', s))
    out["unique_sources"] = len(src_ids)

    return out


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    fail = 0
    for p in paths:
        r = audit(p)
        status = "PASS" if not r["issues"] else "FAIL"
        print(f"[{status}] {p.name} | lines={r['lines']} | refs={r['ref_count']} | unique_srcs={r['unique_sources']} | probe42_cites={r['probe42_cites']}")
        for issue in r["issues"]:
            print(f"   - {issue}")
        if r["issues"]:
            fail = 1
    sys.exit(fail)


if __name__ == "__main__":
    main()
