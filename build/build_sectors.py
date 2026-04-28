"""Driver: build sector deepdives for all 149 spec'd companies."""
from build._sector import build_one
from build._sector_specs import ROWS

def to_spec(row):
    """Convert tuple row to spec dict."""
    base = {
        "dossier_slug": row[0],
        "name": row[1],
        "pilot": row[2],
        "cluster": row[3],
        "headline_low": row[4],
        "headline_high": row[5],
        "position": row[6],
    }
    if len(row) > 7 and isinstance(row[7], dict):
        base.update(row[7])
    return base


def build_all():
    ok = 0; fail = 0
    for r in ROWS:
        try:
            spec = to_spec(r)
            out, lines = build_one(spec)
            ok += 1
        except Exception as e:
            fail += 1
            print(f"[FAIL] {r[0]}: {e}")
    print(f"[sector-build] OK={ok} FAIL={fail}")


if __name__ == "__main__":
    build_all()
