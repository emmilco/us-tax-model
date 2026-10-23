#!/usr/bin/env python3
"""Compare two model families' review logs of the same form and write reports/<year>/second_family.md.

For every form that has both a Claude log and a second family's log of a kind (transcription,
render, class M; families.py), the lines judged in both logs are read and three things reported:

  agreement floor    the share of those lines on which the two families' verdicts agree and
                     neither disputes the project (transcription and class M: both AGREE; render:
                     both MATCH), per form and overall, marked against the 90% floor
  independence yield the lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where
                     the Claude log agreed or matched, each with the second family's reason
  both disputed      the lines both families disputed

A line one log judged and the other did not (MISSING, or absent from one log) is left out of the
floor and counted. A log whose subject hash is no longer current is marked stale in the table.
The report's "Summary:" line is what check_logs.py prints.

    python3 tools/transcription/compare_families.py
"""
import datetime, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402

REPORT = os.path.join(ROOT, "reports", Y, "second_family.md")
FLOOR = 0.90
KINDS = ("transcription", "render", "classm")
AGREE = {"transcription": "AGREE", "render": "MATCH", "classm": "AGREE"}
TITLE = {"transcription": "Transcription agreement", "render": "Render comparison", "classm": "Class M hand-work"}


def parse_log(kind, path):
    """The log's header fields and, per judged line, its status and the model's stated reason."""
    text = open(path, encoding="utf-8").read()
    field = lambda name: (re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", text, flags=re.M) or [None, ""])[1]
    _, _, rest = text.partition("\n## Lines\n")
    body = re.split(r"\n## ", rest)[0]
    lines = {}
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        parts = title.split(" — ")
        if kind == "classm":
            if title.startswith("case ") or len(parts) < 3:
                continue
            key = f"{parts[0]} — {parts[1]}"
        else:
            key = parts[0]
        m = re.search(r"^Status: \*\*(\w+)\*\*", content, flags=re.M)
        if not m:
            continue
        if kind == "transcription":
            note = re.search(r"^Second transcription's note: (.*)$", content, flags=re.M)
            reason = note.group(1) if note else ""
        elif kind == "render":
            note = re.search(r"^Model: (.*)$", content, flags=re.M)
            reason = note.group(1) if note else ""
        else:
            value = re.search(r"^Model: (.*)$", content, flags=re.M)
            work = re.search(r"^Work: (.*)$", content, flags=re.M)
            reason = (f"model gave {value.group(1)}" if value else "") + (f"; work: {work.group(1)}" if work else "")
        lines[key] = {"status": m.group(1), "reason": reason.strip()}
    return {"model": field("model requested"), "reported": field("model reported"), "date": field("date"),
            "subject": field("subject sha256"), "lines": lines}


def compare(kind, form, family):
    a = parse_log(kind, rulings.log_path(kind, form, families.DEFAULT))
    b = parse_log(kind, rulings.log_path(kind, form, family))
    agree = AGREE[kind]
    shared = sorted(set(a["lines"]) & set(b["lines"]))
    judged = [k for k in shared if a["lines"][k]["status"] != "MISSING" and b["lines"][k]["status"] != "MISSING"]
    both_agree = [k for k in judged if a["lines"][k]["status"] == agree and b["lines"][k]["status"] == agree]
    yield_ = [k for k in judged if a["lines"][k]["status"] == agree and b["lines"][k]["status"] != agree]
    both_disputed = [k for k in judged if a["lines"][k]["status"] != agree and b["lines"][k]["status"] != agree]
    claude_only = [k for k in judged if a["lines"][k]["status"] != agree and b["lines"][k]["status"] == agree]
    try:
        current = subjects.current(kind, form, Y)
    except FileNotFoundError:
        current = None
    return {"kind": kind, "form": form, "family": family, "a": a, "b": b, "shared": shared, "judged": judged,
            "both_agree": both_agree, "yield": yield_, "both_disputed": both_disputed, "claude_only": claude_only,
            "unjudged": len(set(a["lines"]) ^ set(b["lines"])) + len(shared) - len(judged),
            "stale": [fam for fam, log in ((families.DEFAULT, a), (family, b)) if current is None or log["subject"] != current]}


def pct(n, d):
    return f"{100 * n / d:.1f}%" if d else "n/a"


def floor_mark(r):
    if not r["judged"]:
        return "no lines"
    return "pass" if len(r["both_agree"]) / len(r["judged"]) >= FLOOR else "below"


def pairs():
    out = []
    for kind in KINDS:
        logs = rulings.forms_with_logs(kind)
        claude = {form for form, fam in logs if fam == families.DEFAULT}
        for form, fam in logs:
            if fam != families.DEFAULT and form in claude:
                out.append((kind, form, fam))
    return out


def main():
    results = [compare(kind, form, fam) for kind, form, fam in pairs()]
    fams = sorted({r["family"] for r in results})
    judged = sum(len(r["judged"]) for r in results)
    agreed = sum(len(r["both_agree"]) for r in results)
    yield_n = sum(len(r["yield"]) for r in results)
    both_n = sum(len(r["both_disputed"]) for r in results)
    passing = sum(1 for r in results if floor_mark(r) == "pass")
    below = sum(1 for r in results if floor_mark(r) == "below")
    if results:
        summary = (f"{len(results)} form-kind pair(s) with logs from Claude and {', '.join(fams)}; agreement floor overall "
                   f"{pct(agreed, judged)} ({agreed}/{judged} lines judged by both); {passing} pair(s) at or above the "
                   f"{int(FLOOR * 100)}% floor, {below} below; independence yield {yield_n} line(s); both families disputed {both_n}")
    else:
        summary = "no second-family logs yet"
    out = [f"# Second-family review comparison — {Y}", "",
           f"Summary: {summary}", "",
           f"Written by `tools/transcription/compare_families.py` on {datetime.date.today().isoformat()} from the review logs under `reviews/{Y}/`. "
           "For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.", "",
           "- **Agreement floor**: the share of lines judged by both on which the two families' verdicts agree and neither disputes the project "
           "(transcription and class M: both AGREE; render: both MATCH). The integrity plan (item 1.3) sets a provisional floor of "
           f"{int(FLOOR * 100)}%; a run below it does not count as a second-family assertion. A denominator of a few lines is marked as such: the floor on one line is one verdict.",
           "- **Independence yield**: lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where the Claude log agreed or matched, with the second family's reason. Zero is a visible result.",
           "- **Both disputed**: lines both families disputed; **Claude only**: lines only the Claude run disputed.",
           "- **Not judged by both**: lines one log has and the other does not, or that either marked MISSING; left out of the floor.",
           "- **Stale**: a log whose recorded subject hash is not the current subject (subjects.py); its verdicts describe an earlier form or rendering.", ""]
    for kind in KINDS:
        rs = [r for r in results if r["kind"] == kind]
        out += [f"## {TITLE[kind]}", ""]
        if not rs:
            out += ["No form has a second family's log of this kind.", ""]
            continue
        out += ["| form | second family (model) | lines judged by both | both agree | floor | 90% floor | yield | both disputed | Claude only | not judged by both | stale |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in sorted(rs, key=lambda r: (r["form"], r["family"])):
            out.append(f"| {r['form']} | {r['family']} ({r['b']['model']}) | {len(r['judged'])} | {len(r['both_agree'])} | {pct(len(r['both_agree']), len(r['judged']))} | "
                       f"{floor_mark(r)}{' (' + str(len(r['judged'])) + ' line' + ('s' if len(r['judged']) != 1 else '') + ')' if 0 < len(r['judged']) < 5 else ''} | "
                       f"{len(r['yield'])} | {len(r['both_disputed'])} | {len(r['claude_only'])} | {r['unjudged']} | {', '.join(r['stale']) or '-'} |")
        kj = sum(len(r["judged"]) for r in rs); ka = sum(len(r["both_agree"]) for r in rs)
        out.append(f"| **all** | | {kj} | {ka} | {pct(ka, kj)} | | {sum(len(r['yield']) for r in rs)} | {sum(len(r['both_disputed']) for r in rs)} | {sum(len(r['claude_only']) for r in rs)} | {sum(r['unjudged'] for r in rs)} | |")
        out.append("")
        ys = [(r, k) for r in rs for k in r["yield"]]
        out += ["### Independence yield", ""]
        if ys:
            out += ["| form | second family | line | second family's verdict | second family's reason |", "| --- | --- | --- | --- | --- |"]
            for r, k in ys:
                out.append(f"| {r['form']} | {r['family']} | {k} | {r['b']['lines'][k]['status']} | {cell(r['b']['lines'][k]['reason'])} |")
        else:
            out.append("None: every line the second family disputed, the Claude run disputed too.")
        out.append("")
        bs = [(r, k) for r in rs for k in r["both_disputed"]]
        out += ["### Lines both families disputed", ""]
        if bs:
            out += ["| form | second family | line | Claude | second family | second family's reason |", "| --- | --- | --- | --- | --- | --- |"]
            for r, k in bs:
                out.append(f"| {r['form']} | {r['family']} | {k} | {r['a']['lines'][k]['status']} | {r['b']['lines'][k]['status']} | {cell(r['b']['lines'][k]['reason'])} |")
        else:
            out.append("None.")
        out.append("")
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    open(REPORT, "w", encoding="utf-8").write("\n".join(out))
    print(f"second_family: {summary} -> {os.path.relpath(REPORT, ROOT)}")


def cell(text):
    """A table cell: one line, pipes escaped, long reasons cut."""
    t = re.sub(r"\s+", " ", text or "").replace("|", "\\|").strip()
    return (t[:400] + "…") if len(t) > 400 else (t or "(no reason given)")


if __name__ == "__main__":
    main()
