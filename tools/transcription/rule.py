#!/usr/bin/env python3
"""Write rulings into a transcription or render-comparison log.

Usage: rule.py --form f1040 --rulings rulings.json [--kind transcription|render]
where rulings.json is {"<printed>": "Ruling: ...", ...}; a key "*" applies to every
line still open. Only sections whose ruling is open are changed.
"""
import argparse, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REVIEWS = os.path.join(ROOT, "reviews", "2025")


def apply(form, rulings, kind="transcription"):
    path = os.path.join(REVIEWS, kind, form + ".md")
    text = open(path, encoding="utf-8").read()
    head, sep, rest = text.partition("\n## Lines\n")
    body, sep2, tail = rest.partition("\n## Raw ")
    parts = body.split("\n### ")
    applied = []
    for i in range(1, len(parts)):
        title, _, content = parts[i].partition("\n")
        printed = title.split(" — ")[0]
        if "Ruling: open" not in content:
            continue
        ruling = rulings.get(printed) or rulings.get("*")
        if ruling:
            if not ruling.startswith("Ruling:"):
                ruling = "Ruling: " + ruling
            content = content.replace("Ruling: open", ruling, 1)
            applied.append(printed)
        parts[i] = title + "\n" + content
    body = "\n### ".join(parts)
    open(path, "w", encoding="utf-8").write(head + sep + body + sep2 + tail)
    return applied


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--rulings", required=True)
    ap.add_argument("--kind", default="transcription", choices=["transcription", "render"])
    a = ap.parse_args()
    done = apply(a.form, json.load(open(a.rulings)), a.kind)
    remaining = open(os.path.join(REVIEWS, a.kind, a.form + ".md"), encoding="utf-8").read().count("Ruling: open")
    print(f"{a.form}: ruled {len(done)} line(s) {done}; open rulings remaining: {remaining}")
