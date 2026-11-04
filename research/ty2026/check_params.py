#!/usr/bin/env python3
"""Second check of research/ty2026/params-2026.proposed.yaml (TY2026 step 4): for every parameter with a 2026
value, (1) the quote is printed on the cited page of the archived 2026 source (either text layer; whitespace
normalised; "..." separates parts), and (2) the quote prints the amount: each dollar amount of the value as
$X,XXX (a negative amount as ($X,XXX)), each rate as N% (or "by N" for 1/N). A count, or a rate the quote
does not print as a number, is reported as structural (it rests on the quote's wording, not a printed figure).
Exits 1 on any failure of (1) or of (2) for an amount."""
import re, sys
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).parent))
from check_quotes import norm, pages

ROOT = Path(__file__).resolve().parents[2]


def money(c):
    d, cents = divmod(abs(c), 100)
    s = f"${d:,}" + (f".{cents:02d}" if cents else "")
    return f"({s})" if c < 0 else s


def rate_forms(r):
    n, d = r["num"], r["den"]
    pct = n * 100 / d
    p = (f"{pct:.10f}".rstrip("0").rstrip("."))
    forms = [f"{p}%"]
    if n == 1:
        forms.append(f"by {d}")
    return forms


def main():
    data = yaml.safe_load((ROOT / "research/ty2026/params-2026.proposed.yaml").read_text())["params"]["values"]
    fails, structural, ok = [], [], 0
    for pid, e in data.items():
        if e["source"] == "none":
            continue
        c = e["cite"]
        m = re.match(r"p\. ([0-9]+)", c["locator"])
        page = int(m.group(1)) if m else None
        L = pages(2026, c["doc"])
        parts = [norm(x) for x in re.split(r"\s*(?:\.\.\.|…)\s*", c["quote"]) if x.strip()]
        if not any(0 < page <= len(l) and all(p in l[page - 1] for p in parts) for l in L):
            where = sorted({i + 1 for l in L for i, t in enumerate(l) if all(p in t for p in parts)})
            fails.append(f"{pid}: quote not printed on `{c['doc']}` p. {page}" + (f" (found on p. {where})" if where else " (not found)"))
            continue
        q = norm(c["quote"])
        v, t = e["value"], e["type"]
        if t.startswith("Enum"):
            structural.append(pid); continue
        if t == "Rate":
            vals = list(v.values()) if "num" not in v else [v]
            if not all(any(f.lower() in q for f in rate_forms(r)) for r in vals):
                structural.append(pid); continue
        elif t == "Count":
            if str(v) not in re.findall(r"\d+", q):
                structural.append(pid); continue
        else:
            vals = set(v.values()) if isinstance(v, dict) else {v}
            missing = [money(x) for x in vals if money(x).lower() not in q]
            if missing:
                fails.append(f"{pid}: quote does not print {', '.join(missing)}"); continue
        ok += 1
    print(f"{ok} amounts printed in their quotes; {len(structural)} structural (no printed figure): {', '.join(structural)}")
    for f in fails:
        print("FAIL", f)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
