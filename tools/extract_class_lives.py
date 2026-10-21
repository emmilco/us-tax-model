#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Extract Pub. 946 Appendix B (Tables B-1 and B-2, Table of Class Lives and Recovery Periods)
from the archived layout text into tables/<year>/class_lives.yaml and the asset_class enum file
tables/<year>/class_lives.enum.yaml.

Each asset class gives its class life, GDS (MACRS) recovery period and ADS recovery period. A
footnote mark joined to a number (GDS "74" is 7 with footnote 4) or to a description is kept
as a flag, never folded into a value; a class with any footnote, a farming class (01.x, reported
on Schedule F), and a class whose GDS period is not one this tool depreciates (3, 5, 7, 10, 15
and 20 years) get the period `outside`, so the form refuses them with the footnote cited.

    python3 tools/extract_class_lives.py            # writes the two files
    python3 tools/extract_class_lives.py --json     # prints the parsed rows (for the second transcription compare)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
ARCHIVE = ROOT / "sources" / Y
OUT = ROOT / "tables" / Y / "class_lives.yaml"
VERSION = "0.1"
PAGES = range(99, 109)            # Tables B-1 and B-2
GDS_OK = {"3": "y3", "5": "y5", "7": "y7", "10": "y10", "15": "y15", "20": "y20"}
VALID_GDS = {"3", "5", "7", "10", "15", "20", "25", "27.5", "39", "50"}


def header(lines):
    """Column centres of Class Life, GDS and ADS and the column of the class code."""
    for i, line in enumerate(lines):
        if "(in years) (MACRS)" in line:
            cl = line.index("(in years)") + 5
            gds = line.index("(MACRS)") + 3
            ads = line.index("ADS") + 1
            code = lines[i].index("class") if "class" in lines[i] else lines[i - 1].index("Asset")
            return cl, gds, ads, code
    return None


def split_mark(tok, valid=None):
    """A number with a footnote digit joined to it: '74' -> ('7', '4') when 74 is not a valid value."""
    if valid is not None and tok not in valid and len(tok) >= 2 and tok[:-1] in valid:
        return tok[:-1], tok[-1]
    return tok, None


def parse(pages):
    rows = []
    for n in PAGES:
        lines = pages[n - 1].splitlines()
        h = header(lines)
        if not h:
            continue
        code_c = h[3]
        start = next(i for i, l in enumerate(lines) if "(in years) (MACRS)" in l)
        right = lines[start - 1].index("Class Life") - 6   # numbers right of this are table values
        cur = None
        for line in lines[start + 1:]:
            if "Publication 946" in line:
                continue
            m = re.match(r"\s*(\d\d\.\d+)\s+(\S.*)?$", line)
            if m and abs(line.index(m.group(1)) - code_c) <= 3:
                cur = {"code": m.group(1), "page": n, "text": [], "nums": []}
                rows.append(cur)
            elif "Certain Property for Which" in line or re.match(r"\s*\d\s+[A-Z]", line) and len(line) - len(line.lstrip()) < code_c:
                cur = None
            if cur is None:
                continue
            cur["text"].append(line[:right].strip())
            cur["nums"] += re.findall(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])", line[right:])
    out = []
    for r in rows:
        desc = re.sub(r"^\d\d\.\d+\s+", "", " ".join(t for t in r["text"] if t)).strip()
        nums, marks = list(r["nums"]), []
        life = gds = ads = None
        if len(nums) == 3:
            life, gds, ads = nums
        elif len(nums) == 6:
            # The row's values, then those printed beside an unnumbered heading that follows it (49.1 before 49.11).
            life, gds, ads = nums[:3]
        elif len(nums) == 2:
            gds, ads = nums
            marks.append("no class life")
        elif nums:
            marks.append("values " + " ".join(nums))
        else:
            marks.append("no values")
        if gds is not None:
            gds, mark = split_mark(gds, VALID_GDS)
            if mark:
                marks.append(f"gds footnote {mark}")
        ads_note = None
        if ads is not None and life not in (None, "1") and ads != life and ads[:-1] == life:
            ads, ads_note = ads[:-1], ads[-1]
        if life == "1" and gds is not None:
            marks.append("class life footnote 1")   # footnote 1: assigned recovery periods but no class lives
            life = None
        if re.search(r"[a-z\)]\d\b", desc):
            marks.append("description footnote")
        out.append({"code": r["code"], "page": r["page"], "description": desc, "life": life, "gds": gds, "ads": ads, "marks": marks,
                    "ads_footnote": ads_note})
    return out


# Property assigned a recovery period outside the asset classes: the lettered paragraphs at the end of Table B-2
# ("Certain Property for Which Recovery Periods Assigned", p. 108) and qualified improvement property (i4562 p. 10,
# 15-year property; Pub. 946 Table 4-1, "GDS using SL ... Qualified improvement property ... placed in service after
# 2017"). Paragraphs D to F (energy and biomass property) and Section 1245 real property are refused.
EXTRA = [
    ("cA_personal", "y7", "Table B-2, Certain Property for Which Recovery Periods Assigned, A. Personal Property With No Class Life"),
    ("cA_1245real", "outside", "Table B-2, A. Section 1245 Real Property With No Class Life"),
    ("cB_qte", "y5", "Table B-2, B. Qualified Technological Equipment, as defined in section 168(i)(2)"),
    ("cC_research", "y5", "Table B-2, C. Property Used in Connection with Research and Experimentation referred to in section 168(e)(3)(B)"),
    ("cDEF_energy", "outside", "Table B-2, D, E and F (alternative energy, biomass and energy property)"),
    ("cqip", "y15sl", "Qualified improvement property placed in service after 2017 (i4562 p. 10; Pub. 946 Table 4-1)"),
]


def period(row):
    if row["code"].startswith("01.") or row["marks"] or row["gds"] not in GDS_OK:
        return "outside"
    return GDS_OK[row["gds"]]


def main():
    manifest = {d["id"]: d for d in json.loads((ARCHIVE / "manifest.json").read_text())["documents"]}
    entry = manifest["p946"]
    if hashlib.sha256((ARCHIVE / entry["file"]).read_bytes()).hexdigest() != entry["sha256"]:
        raise SystemExit("p946.pdf does not match its manifest hash")
    pages = (ARCHIVE / entry["text_file"]).read_text(encoding="utf-8").split("\f")
    rows = parse(pages)
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1))
        return
    codes = [r["code"] for r in rows]
    if len(codes) != len(set(codes)):
        raise SystemExit("duplicate asset classes")
    lines = [
        f"# Pub. 946 ({Y}) Appendix B, Tables B-1 and B-2, Table of Class Lives and Recovery Periods: the GDS recovery",
        "# period of each asset class, or `outside` for a farming class, a class with a footnote, or a GDS period this tool",
        "# does not depreciate.",
        f"# Source: sources/{Y}/p946.pdf sha256 {entry['sha256']}",
        f"# Extractor: tools/extract_class_lives.py v{VERSION}",
        "# Regenerate with: python3 tools/extract_class_lives.py",
        "table:",
        "  id: class_lives",
        "  kind: keyed",
        '  title: "GDS recovery period by asset class (Pub. 946, Appendix B, Tables B-1 and B-2)"',
        f"  tax_year: {Y}",
        "  cite:",
        "    doc: p946",
        '    locator: "Appendix B, Tables B-1 and B-2, Table of Class Lives and Recovery Periods, pp. 98-108"',
        '    quote: "Generally, if the property is listed in Table B-1, you use the recovery period shown in that table. However, if the property is specifically listed in Table B-2 under the type of activity in which it is used, you use the recovery period listed under the activity in that table."',
        "  keys:",
        "    - { name: asset_class, type: Enum(asset_class) }",
        "  cell: Enum(macrs_period)",
        "  rows:",
    ]
    for r in rows:
        lines.append(f"    - {{ keys: [c{r['code'].replace('.', '_')}], value: {period(r)} }}")
    for key, value, what in EXTRA:
        lines.append(f"    - {{ keys: [{key}], value: {value} }}   # {what}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    enum = [f"c{c.replace('.', '_')}" for c in codes] + [k for k, _, _ in EXTRA]
    (ROOT / "tables" / Y / "class_lives.enum.json").write_text(json.dumps({"values": enum, "descriptions": {**{f"c{r['code'].replace('.', '_')}": f"{r['code']} {r['description']}" for r in rows}, **{k: w for k, _, w in EXTRA}}}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = {}
    for r in rows:
        counts[period(r)] = counts.get(period(r), 0) + 1
    print(f"class lives: {len(rows)} asset classes; " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
