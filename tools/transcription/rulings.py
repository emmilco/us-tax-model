#!/usr/bin/env python3
"""Rulings on review disagreements, kept as data beside each log.

Each review log (`reviews/<year>/<kind>/<form>.md`, or `<form>.<family>.md` for a
model family other than Claude: families.py) is rendered by its tool; the rulings a
person wrote on its disagreements live in `<form>.rulings.json` (`<form>.<family>.rulings.json`) next
to it, keyed by the disagreement they answer (the printed line and the two sides
of the disagreement), with a context hash covering the reviewed subject,
prompts and source excerpts. Only an unchanged disagreement in the same
recorded context can reuse a ruling. `rule.py` writes both files;
`check_logs.py` fails when a log's rulings and its sidecar disagree.

    rulings.py --migrate     # build every sidecar from the rulings already in the logs
    rulings.py --check       # report log/sidecar disagreements (exit 1 on any)
    rulings.py --prune       # drop sidecar entries whose disagreement no longer occurs
"""
import argparse, hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402

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


def sidecar_path(kind, form, family=families.DEFAULT):
    return os.path.join(REVIEWS, kind, families.stem(form, family) + ".rulings.json")


def log_path(kind, form, family=families.DEFAULT):
    return os.path.join(REVIEWS, kind, families.stem(form, family) + ".md")


def load(kind, form, family=families.DEFAULT):
    """{key tuple: {"ruling": text without the dropped suffix, "drop": bool}}."""
    path = sidecar_path(kind, form, family)
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding="utf-8"))
    fields = KINDS[kind]
    return {tuple(r[f] for f in fields): {"ruling": r["ruling"], "drop": bool(r.get("drop")),
                                        **({"context": r["context"]} if r.get("context") else {})}
            for r in data["rulings"]}


def save(kind, form, rulings, family=families.DEFAULT):
    fields = KINDS[kind]
    rows = []
    for key in sorted(rulings, key=lambda k: tuple(str(x) for x in k)):
        row = dict(zip(fields, key))
        row["ruling"] = rulings[key]["ruling"]
        if rulings[key].get("drop"):
            row["drop"] = True
        if rulings[key].get("context"):
            row["context"] = rulings[key]["context"]
        rows.append(row)
    path = sidecar_path(kind, form, family)
    head = {"kind": kind, "form": form}
    if family != families.DEFAULT:
        head["family"] = family
    with open(path, "w", encoding="utf-8") as f:
        json.dump({**head, "rulings": rows}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


def review_context(kind, text):
    """Bind a ruling to what was reviewed, including input wording carried by the prompt.

    Exclude dates and outcome counts. Class M records its prompts on case headings;
    the other writers record one prompt in the header. Legacy rulings without a
    context remain historical records, but are never automatically reused.
    """
    head = text.partition("\n## Lines\n")[0]
    names = ("subject sha256", "prompt sha256", "prompt policy", "system sha256",
             "model requested", "reasoning effort", "output token budget")
    fields = {name: (re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", head, re.M) or [None, ""])[1]
              for name in names}
    comparison = re.search(r"^\| comparison policy \| (.*?) \|$", head, re.M)
    if kind == "transcription" and comparison:
        fields["comparison policy"] = comparison.group(1)
        for name in ("type validation policy", "model type validation", "input context policy", "complete input context"):
            match = re.search(rf"^\| {name} \| (.*?) \|$", head, re.M)
            if match:
                fields[name] = match.group(1)
    sources = re.findall(r"^\| \S+ \| [^|]* \| [^|]* \| [^|]* \| [0-9a-f]{64} \|[^\n]*$", head, re.M)
    cases = sorted(re.findall(r"^### case (\S+) — prompt sha256 ([0-9a-f]{64});", text, re.M)) if kind == "classm" else []
    return hashlib.sha256(json.dumps({"kind": kind, "fields": fields, "sources": sorted(sources),
                                     "case_prompts": cases}, sort_keys=True).encode()).hexdigest()


def kept(kind, form, family=families.DEFAULT, *, context):
    """Only reuse rulings explicitly made in this review context."""
    return {k: v["ruling"] + (DROPPED if v["drop"] else "") for k, v in load(kind, form, family).items()
            if v.get("context") == context}


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
    """[(form, family)] for every log of a kind, the Claude family first within a form."""
    d = os.path.join(REVIEWS, kind)
    if not os.path.isdir(d):
        return []
    pairs = [families.split_stem(f[:-3]) for f in os.listdir(d) if f.endswith(".md")]
    return sorted(pairs, key=lambda p: (p[0], p[1] != families.DEFAULT, p[1]))


def migrate():
    total = 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = open(log_path(kind, form, family), encoding="utf-8").read()
            rulings = load(kind, form, family)
            for key, line in log_sections(kind, text):
                if line != OPEN:
                    t, drop = split_ruling(line)
                    # Migration copies historical rulings; it cannot establish that
                    # their rationale was adjudicated in the current context.
                    prior = rulings.get(key, {})
                    rulings[key] = {**prior, "ruling": t, "drop": drop}
            if rulings:
                save(kind, form, rulings, family); total += len(rulings)
    print(f"rulings: {total} written to sidecars")


def prune():
    """Drop sidecar entries whose disagreement no longer occurs in the log."""
    dropped = 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = open(log_path(kind, form, family), encoding="utf-8").read()
            live = {key for key, _ in log_sections(kind, text)}
            side = load(kind, form, family)
            kept = {k: v for k, v in side.items() if k in live}
            if len(kept) != len(side):
                dropped += len(side) - len(kept)
                if kept:
                    save(kind, form, kept, family)
                else:
                    os.remove(sidecar_path(kind, form, family))
    print(f"rulings: {dropped} stale sidecar entries pruned")


def check():
    """A log's non-open rulings must each equal the sidecar's; sidecar entries with no
    matching section are reported (a disagreement that no longer occurs) but pass."""
    problems, stale, total = [], 0, 0
    for kind in KINDS:
        for form, family in forms_with_logs(kind):
            text = open(log_path(kind, form, family), encoding="utf-8").read()
            side = load(kind, form, family)
            seen = set()
            stem = families.stem(form, family)
            for key, line in log_sections(kind, text):
                if line == OPEN:
                    continue
                total += 1; seen.add(key)
                t, drop = split_ruling(line)
                s = side.get(key)
                if s is None:
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} is in the log but not in {stem}.rulings.json")
                elif s["ruling"] != t or s["drop"] != drop:
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} differs between the log and {stem}.rulings.json")
                elif s.get("context") and s["context"] != review_context(kind, text):
                    problems.append(f"{kind}/{stem}: ruling on {key[:2]} belongs to a different review context")
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
