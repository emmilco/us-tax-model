#!/usr/bin/env python3
"""Check the quotes of the TY2026 change map (research/ty2026/changes/*.md or changes.md): every
`doc` p. N[–M] ...: "quote" on a **2026:** or **2025:** bullet must be printed on the cited page(s) of
sources/<year>/<doc> (either text layer, whitespace and soft hyphens normalised; "..." splits a quote into
parts, each of which must be printed). A bullet's year is the year of its label; a quote with no page is
looked for in the whole document. Prints each failure; exits 1 if any."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def norm(s):
    s = s.replace("­", "").replace("‐", "-").replace("‑", "-")
    s = re.sub(r"[‘’]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    return re.sub(r"\s+", " ", s).strip().lower()


CACHE = {}


def pages(year, doc):
    key = (year, doc)
    if key not in CACHE:
        layers = []
        for ext in ("cols.txt", "txt"):
            p = ROOT / "sources" / str(year) / f"{doc}.{ext}"
            if p.exists():
                layers.append([norm(x) for x in p.read_text().split("\f")])
        CACHE[key] = layers
    return CACHE[key]


SEG = re.compile(r"`([a-z0-9-]+)`(?: (?:p|pp)\. ([0-9]+)(?:[–-]([0-9]+))?)?([^`]*?)(?=`[a-z0-9-]+`(?: (?:p|pp)\. )|$)")
QUOTE = re.compile(r"\"([^\"]+)\"|“([^”]+)”")


def check_file(path):
    fails, n = [], 0
    for ln_no, line in enumerate(path.read_text().splitlines(), 1):
        m = re.match(r"^- \*\*(2026|2025)(?: \([^)]*\))?:\*\* (.*)$", line)
        if not m:
            continue
        year, body = int(m.group(1)), m.group(2)
        # split the bullet into document segments: each starts with `doc`
        parts = re.split(r"(?=`[a-z0-9][a-z0-9-]*`)", body)
        cur_doc, lo, hi = None, None, None
        for part in parts:
            dm = re.match(r"`([a-z0-9][a-z0-9-]*)`(?: (?:p|pp)\. ([0-9]+)(?:[–-]([0-9]+))?)?", part)
            if dm and (ROOT / "sources" / str(year) / f"{dm.group(1)}.txt").exists():
                cur_doc = dm.group(1)
                lo = int(dm.group(2)) if dm.group(2) else None
                hi = int(dm.group(3)) if dm.group(3) else lo
            # later page mentions inside the segment ("; p. 3:") move the page
            for sub in re.split(r"(?=(?:^|[;,] )p\. [0-9]+)", part):
                pm = re.match(r"(?:[;,] )?p\. ([0-9]+)(?:[–-]([0-9]+))?", sub)
                if pm and cur_doc:
                    lo = int(pm.group(1)); hi = int(pm.group(2) or pm.group(1))
                for q in QUOTE.finditer(sub):
                    text = q.group(1) or q.group(2)
                    if cur_doc is None:
                        continue
                    n += 1
                    L = pages(year, cur_doc)
                    want = [norm(x) for x in re.split(r"\s*(?:\.\.\.|…)\s*", text) if x.strip()]
                    def ok(pg):
                        return any(all(w in layer[pg - 1] for w in want) for layer in L if 0 < pg <= len(layer))
                    rng = range(lo, hi + 1) if lo else range(1, max((len(x) for x in L), default=0) + 1)
                    if not any(ok(pg) for pg in rng):
                        # allow the parts to sit on adjacent cited pages
                        joined_ok = lo and any(all(any(w in layer[pg - 1] for pg in rng if 0 < pg <= len(layer)) for w in want) for layer in L)
                        if not joined_ok:
                            where = [i + 1 for layer in L for i, pgt in enumerate(layer) if all(w in pgt for w in want)]
                            fails.append(f"{path.name}:{ln_no}: {year} `{cur_doc}` p. {lo}{'' if hi == lo else '–' + str(hi)}: not printed: \"{text[:100]}\"" + (f" (found on p. {sorted(set(where))})" if where else ""))
    return n, fails


def main():
    files = [Path(a) for a in sys.argv[1:]] or [ROOT / "research/ty2026/changes.md"]
    total, allf = 0, []
    for f in files:
        n, fails = check_file(f)
        total += n
        allf += fails
        print(f"{f.name}: {n} quotes, {len(fails)} not found")
    for x in allf:
        print(x)
    sys.exit(1 if allf else 0)


if __name__ == "__main__":
    main()
