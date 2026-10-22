#!/usr/bin/env python3
"""Write rulings into a transcription, render-comparison or class M log and its rulings sidecar.

Usage: rule.py --form f1040 --rulings rulings.json [--kind transcription|render|classm]
where rulings.json is {"<printed>": "Ruling: ...", ...}; a key "*" applies to every
line still open. Only sections whose ruling is open are changed. In a class M log a
section is keyed "<case> — <printed>" and a ruling given as {"ruling": "...",
"drop": true} also removes that line from the fixture (a model arithmetic error is not
evidence); the ruling text is suffixed "[dropped]".
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rulings as sidecar  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
REVIEWS = os.path.join(ROOT, "reviews", Y)


def apply(form, rulings, kind="transcription"):
    path = os.path.join(REVIEWS, kind, form + ".md")
    text = open(path, encoding="utf-8").read()
    head, sep, rest = text.partition("\n## Lines\n")
    body, sep2, tail = rest.partition("\n## Raw ")
    parts = body.split("\n### ")
    applied = []
    stored = sidecar.load(kind, form)
    for i in range(1, len(parts)):
        title, _, content = parts[i].partition("\n")
        printed = title.split(" — ")[0]
        if "Ruling: open" not in content:
            continue
        if kind == "classm":
            if " \u2014 " not in title:
                continue  # a case heading, not a line
            case, _, rest = title.partition(" \u2014 ")
            printed = f"{case} \u2014 {rest.split(' \u2014 ')[0]}"
        ruling = rulings.get(printed) or rulings.get("*")
        if ruling:
            drop = isinstance(ruling, dict) and ruling.get("drop")
            ruling = ruling["ruling"] if isinstance(ruling, dict) else ruling
            if not ruling.startswith("Ruling:"):
                ruling = "Ruling: " + ruling
            found = sidecar.section_key(kind, title, content)
            if found is None:
                raise SystemExit(f"{form}: cannot key the disagreement at {printed} for the sidecar")
            stored[found[0]] = {"ruling": ruling.rstrip(), "drop": bool(drop)}
            if drop:
                ruling = ruling.rstrip() + " [dropped]"
                drop_from_fixture(form, printed.split(" \u2014 ")[0], rest.split(" \u2014 ")[0])
            content = content.replace("Ruling: open", ruling, 1)
            applied.append(printed)
        parts[i] = title + "\n" + content
    body = "\n### ".join(parts)
    open(path, "w", encoding="utf-8").write(head + sep + body + sep2 + tail)
    if applied:
        sidecar.save(kind, form, stored)
    return applied


def drop_from_fixture(form, case_id, printed):
    """Remove one line's expectation from a class M fixture case."""
    fx_path = os.path.join(ROOT, "fixtures", Y, "classm.json")
    fx = json.load(open(fx_path))
    jobs = json.load(open(os.path.join(ROOT, ".classm", "jobs.json")))["jobs"]
    job = next(j for j in jobs if j["id"] == case_id)
    # The section is named by the line's handle (classm.handle): its printed number, or the
    # number and the line's id where two lines share the number.
    line_id = next(l["id"] for l in job["fill"] if printed in (l["printed"], f'{l["printed"]} ({l["id"]})'))
    for c in fx["cases"]:
        if c["id"] == case_id:
            c["expect"].pop(line_id, None)
            c["evidence_note"] += f"; dropped after ruling: {line_id}"
    json.dump(fx, open(fx_path, "w"), indent=1)
    open(fx_path, "a").write("\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--rulings", required=True)
    ap.add_argument("--kind", default="transcription", choices=["transcription", "render", "classm"])
    a = ap.parse_args()
    done = apply(a.form, json.load(open(a.rulings)), a.kind)
    remaining = open(os.path.join(REVIEWS, a.kind, a.form + ".md"), encoding="utf-8").read().count("Ruling: open")
    print(f"{a.form}: ruled {len(done)} line(s) {done}; open rulings remaining: {remaining}")
