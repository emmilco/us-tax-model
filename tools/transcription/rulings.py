#!/usr/bin/env python3
"""Rulings on review disagreements, kept as data beside each log.

Each review log (`reviews/<year>/<kind>/<form>.md`) is rendered by its tool; the
rulings a person wrote on its disagreements live in `<form>.rulings.json` next
to it, keyed by the disagreement they answer (the printed line and the two sides
of the disagreement), so a rerun that reproduces the same disagreement keeps the
same ruling without parsing the prose log. `rule.py` writes both files;
`check_logs.py` fails when a log's rulings and its sidecar disagree.

    rulings.py --migrate     # build every sidecar from the rulings already in the logs
    rulings.py --check       # report log/sidecar disagreements (exit 1 on any)
    rulings.py --prune       # drop sidecar entries whose disagreement no longer occurs
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
REVIEWS = os.path.join(ROOT, "reviews", Y)
KINDS = {
    "transcription": ("printed", "project", "second"),
    "render": ("printed", "restated", "model"),
    "classm": ("case", "printed", "project", "model"),
}
OPEN = "Ruling: open"
DROPPED = " [dropped]"


def sidecar_path(kind, form):
    return os.path.join(REVIEWS, kind, form + ".rulings.json")


def log_path(kind, form):
    return os.path.join(REVIEWS, kind, form + ".md")


def load(kind, form):
    """{key tuple: {"ruling": text without the dropped suffix, "drop": bool}}."""
    path = sidecar_path(kind, form)
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding="utf-8"))
    fields = KINDS[kind]
    return {tuple(r[f] for f in fields): {"ruling": r["ruling"], "drop": bool(r.get("drop"))} for r in data["rulings"]}


def save(kind, form, rulings):
    fields = KINDS[kind]
    rows = []
    for key in sorted(rulings, key=lambda k: tuple(str(x) for x in k)):
        row = dict(zip(fields, key))
        row["ruling"] = rulings[key]["ruling"]
        if rulings[key].get("drop"):
            row["drop"] = True
        rows.append(row)
    path = sidecar_path(kind, form)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"kind": kind, "form": form, "rulings": rows}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


def kept(kind, form):
    """The rulings as a writer applies them: key -> the ruling line to print."""
    return {k: v["ruling"] + (DROPPED if v["drop"] else "") for k, v in load(kind, form).items()}


def split_ruling(text):
    """A ruling line as printed -> (text without the dropped suffix, drop flag)."""
    text = text.strip()
    if text.endswith(DROPPED.strip()):
        return text[: -len(DROPPED.strip())].rstrip(), True
    return text, False


_SECTION = {
    "transcription": re.compile(r"^Status: \*\*(?:DISAGREE|MISSING)\*\*\n\nProject:\n\n```json\n(.*?)\n```\n\nSecond:\n\n```json\n(.*?)\n```(?:\n\nSecond transcription's note: [^\n]*)?\n\n(Ruling: [^\n]*)", re.S),
    "render": re.compile(r"^Status: \*\*(?:MISMATCH|UNCLEAR|MISSING)\*\*\n\nRestated: (.*?)\n\nModel: (.*?)\n\n(Ruling: [^\n]*)", re.S),
    "classm": re.compile(r"^Status: \*\*(?:DISAGREE|MISSING)\*\*\n\nProject: ([^\n]*)\nModel: ([^\n]*)\n(?:Work: [^\n]*\n)?\n(Ruling: [^\n]*)"),
}


def section_key(kind, title, content):
    """(key tuple, ruling line) for a disagreement section of a log, else None.
    `title` is the heading text after '### '; `content` the lines below it."""
    m = _SECTION[kind].match(content)
    if not m:
        return None
    if kind == "classm":
        parts = title.split(" — ")
        if len(parts) < 3:
            return None  # a case heading, not a line
        key = (parts[0], parts[1], m.group(1), m.group(2))
    else:
        key = (title.split(" — ")[0], m.group(1), m.group(2))
    return key, m.group(3).strip()


def log_sections(kind, text):
    """Every disagreement section of a log: [(key, ruling line)]."""
    _, _, rest = text.partition("\n## Lines\n")
    body, _, _ = rest.partition("\n## Raw ")
    out = []
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        found = section_key(kind, title, content)
        if found:
            out.append(found)
    return out


def forms_with_logs(kind):
    d = os.path.join(REVIEWS, kind)
    return sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md")) if os.path.isdir(d) else []


def migrate():
    total = 0
    for kind in KINDS:
        for form in forms_with_logs(kind):
            text = open(log_path(kind, form), encoding="utf-8").read()
            rulings = load(kind, form)
            for key, line in log_sections(kind, text):
                if line != OPEN:
                    t, drop = split_ruling(line)
                    rulings[key] = {"ruling": t, "drop": drop}
            if rulings:
                save(kind, form, rulings); total += len(rulings)
    print(f"rulings: {total} written to sidecars")


def prune():
    """Drop sidecar entries whose disagreement no longer occurs in the log."""
    dropped = 0
    for kind in KINDS:
        for form in forms_with_logs(kind):
            text = open(log_path(kind, form), encoding="utf-8").read()
            live = {key for key, _ in log_sections(kind, text)}
            side = load(kind, form)
            kept = {k: v for k, v in side.items() if k in live}
            if len(kept) != len(side):
                dropped += len(side) - len(kept)
                if kept:
                    save(kind, form, kept)
                else:
                    os.remove(sidecar_path(kind, form))
    print(f"rulings: {dropped} stale sidecar entries pruned")


def check():
    """A log's non-open rulings must each equal the sidecar's; sidecar entries with no
    matching section are reported (a disagreement that no longer occurs) but pass."""
    problems, stale, total = [], 0, 0
    for kind in KINDS:
        for form in forms_with_logs(kind):
            text = open(log_path(kind, form), encoding="utf-8").read()
            side = load(kind, form)
            seen = set()
            for key, line in log_sections(kind, text):
                if line == OPEN:
                    continue
                total += 1; seen.add(key)
                t, drop = split_ruling(line)
                s = side.get(key)
                if s is None:
                    problems.append(f"{kind}/{form}: ruling on {key[:2]} is in the log but not in {form}.rulings.json")
                elif s["ruling"] != t or s["drop"] != drop:
                    problems.append(f"{kind}/{form}: ruling on {key[:2]} differs between the log and {form}.rulings.json")
            stale += sum(1 for k in side if k not in seen)
    for p in problems:
        print(p, file=sys.stderr)
    print(f"rulings: {total} in logs, all in sidecars" if not problems else f"rulings: {len(problems)} log/sidecar disagreement(s)", f"({stale} sidecar entries without a current disagreement)" if stale else "")
    return 1 if problems else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--migrate", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--prune", action="store_true", help="drop sidecar entries whose disagreement no longer occurs")
    a = ap.parse_args()
    if a.migrate:
        migrate()
    if a.prune:
        prune()
    if a.check:
        sys.exit(check())
    if not (a.migrate or a.check or a.prune):
        ap.print_help()
