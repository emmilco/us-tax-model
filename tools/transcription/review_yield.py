#!/usr/bin/env python3
"""Set each review kind's cost against the evidence it produced (T-220).

Usage: review_yield.py [--ledger PATH] [--agent-runs PATH] [--window-ref GIT_REF] [--out PATH]

Sources: the cost ledger (.transcription/costs.jsonl), research/costs/agent_runs.jsonl, the rulings under
reviews/<year>/{transcription,render,classm}/*.rulings.json, reviews/<year>/completeness/rulings.json and
reviews/<year>/screens/rulings.json, reviews/<year>/false_no/rulings.json, reviews/<year>/questions/rulings.json, and the "Caught by" lines of BUG_INVENTORY.md.

The ledger covers only calls since it began; rulings written before stamping carry no date. The "window"
table therefore counts only rulings and bug entries that are absent at --window-ref (the commit just before
the ledger began), which pairs the dollars with the evidence they bought. The "all-time" table counts every
ruling and has no cost. The "exact join" table joins each stamped ruling (rule.py stamps the reply it rules,
`run`) to the ledger call that returned that reply (`response_sha256`), with findings by severity.

Ruling classes are read from the head of the ruling text ("Ruling: model error; ..."). Noise is a ruling
whose head names a model error (transcription, render, class M, screens); for completeness it is the model's
claim ruled covered or wrong. A finding is a ruling classed finding, defect or real gap, and a screen
NARROW finding ruled a defect. Severity is recorded only on stamped findings (rule.py requires it), so it is
tabulated only in the exact-join table.
"""
import argparse, glob, json, os, re, subprocess, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import families  # noqa: E402
import rulings  # noqa: E402

KINDS = ["transcription", "render", "classm", "completeness", "screen", "false_no", "question"]
CLASSES = ["model error", "scope", "representation", "ambiguity", "interface gap", "finding", "other"]
BUG_KIND_WORDS = [("question review", "question"), ("completeness", "completeness"), ("false-no", "false_no"), ("screen", "screen"), ("class m", "classm"),
                  ("render", "render"), ("transcription", "transcription")]
HEAD_CLASSES = (("model", "model error"), ("finding", "finding"), ("defect", "finding"), ("real gap", "finding"),
                ("interface gap", "interface gap"), ("scope", "scope"), ("representation", "representation"),
                ("equivalent", "representation"), ("ambiguity", "ambiguity"), ("genuine ambiguity", "ambiguity"),
                ("agent reading", "ambiguity"), ("owner accepted", "ambiguity"))


def classify(text):
    """Normalized class from the head of a ruling's text."""
    head = re.sub(r"^\s*ruling:\s*", "", (text or "").lower())
    head = re.split(r"[;.:,]| — | \(", head, maxsplit=1)[0].strip()
    for key, cls in HEAD_CLASSES:
        if head.startswith(key):
            return cls
    return "other"


def family_of_file(path, doc):
    if doc.get("family"):
        return doc["family"]
    parts = os.path.basename(path).split(".")
    return parts[1] if len(parts) > 3 and parts[1] in ("deepseek", "gpt") else families.DEFAULT


def git_show(ref, relpath):
    if not ref:
        return None
    r = subprocess.run(["git", "show", f"{ref}:{relpath}"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def key_of(item, kind=None):
    """A ruling's identity for the window: its row in the stored form (an older revision's embedded
    expressions hashed as now), without what is recorded beside the ruling (rulings.EXTRA)."""
    if kind is not None:
        item = {k: v for k, v in rulings.compact_row(kind, item).items() if k not in rulings.EXTRA}
    return json.dumps(item, sort_keys=True)


def ruling_items(root, ref=None):
    """Yield (kind, family, cls, is_new) for every ruling; is_new is True when absent at ref."""
    pats = {"transcription": "transcription/*.rulings.json", "render": "render/*.rulings.json",
            "classm": "classm/*.rulings.json"}
    for kind, pat in pats.items():
        for path in sorted(glob.glob(os.path.join(root, "reviews", "*", pat))):
            doc = json.load(open(path, encoding="utf-8"))
            fam = family_of_file(path, doc)
            old = git_show(ref, os.path.relpath(path, root))
            seen = Counter(key_of(r, kind) for r in json.loads(old).get("rulings", [])) if old else Counter()
            for r in doc.get("rulings", []):
                k = key_of(r, kind)
                new = bool(ref) and seen[k] == 0
                if seen[k]:
                    seen[k] -= 1
                yield kind, fam, classify(r.get("ruling")), new
    for path in sorted(glob.glob(os.path.join(root, "reviews", "*", "completeness", "rulings.json"))):
        old = git_show(ref, os.path.relpath(path, root))
        before = json.loads(old).get("rulings", {}) if old else {}
        for name, r in json.load(open(path, encoding="utf-8")).get("rulings", {}).items():
            cls = {"real gap": "finding", "wrong": "model error", "covered": "model error"}.get(r.get("class", ""), "other")
            yield "completeness", families.DEFAULT, cls, bool(ref) and before.get(name) != r
    for path in sorted(glob.glob(os.path.join(root, "reviews", "*", "screens", "rulings.json"))):
        old = git_show(ref, os.path.relpath(path, root))
        before = json.loads(old).get("rulings", {}) if old else {}
        for name, r in json.load(open(path, encoding="utf-8")).get("rulings", {}).items():
            changed = bool(ref) and before.get(name) != r
            for f in r.get("findings", []):
                c = (f.get("class") or "").lower()
                cls = "finding" if c == "defect" else "model error" if c == "model error" else "other"
                yield "screen", families.DEFAULT, cls, changed
    # The false-no and question reviews' rulings (false_no_review.py, question_review.py): a finding ruled a defect
    # counts as a finding.
    for kind, folder in (("false_no", "false_no"), ("question", "questions")):
        for path in sorted(glob.glob(os.path.join(root, "reviews", "*", folder, "rulings.json"))):
            old = git_show(ref, os.path.relpath(path, root))
            before = json.loads(old).get("rulings", {}) if old else {}
            for name, r in json.load(open(path, encoding="utf-8")).get("rulings", {}).items():
                changed = bool(ref) and before.get(name) != r
                for f in r.get("findings", []):
                    c = (f.get("class") or "").lower()
                    # The question review's classes: "real, changes value" and "real, low" are findings, "wrong"
                    # is the reviewer's error.
                    real = c == "defect" or c.startswith("real")
                    cls = "finding" if real else "model error" if c in ("model error", "wrong") else "other"
                    yield kind, families.DEFAULT, cls, changed


def stamped_items(root):
    """Yield (kind, family, cls, run, severity) for every transcription, render and class M ruling
    stamped with the reply it rules (rulings.STAMPS; rule.py stamps every ruling it writes)."""
    for kind in ("transcription", "render", "classm"):
        for path in sorted(glob.glob(os.path.join(root, "reviews", "*", kind, "*.rulings.json"))):
            doc = json.load(open(path, encoding="utf-8"))
            fam = family_of_file(path, doc)
            for r in doc.get("rulings", []):
                if r.get("run"):
                    yield kind, fam, classify(r.get("ruling")), r["run"], r.get("severity")


def exact_table(ledger, stamped):
    """Per (kind, family): the calls that returned a reply the ledger identifies, their cost, and the
    stamped rulings joined to them by reply identity. A stamped ruling whose reply no ledger call
    returned (a call made before the ledger recorded reply identities) is counted apart."""
    calls = {}
    t = defaultdict(lambda: {"calls": 0, "usd": 0.0, "ruled_calls": set(), "rulings": 0, "classes": Counter(),
                             "severity": Counter(), "unjoined": 0})
    for r in ledger:
        if r.get("response_sha256"):
            k = (r.get("kind") or "-", families.family_of(r.get("model_requested") or "-"))
            calls.setdefault(r["response_sha256"], (k, r))
            t[k]["calls"] += 1
            t[k]["usd"] += r.get("estimated_cost_usd") or 0
    for kind, fam, cls, run, severity in stamped:
        hit = calls.get(run)
        if hit is None:
            t[(kind, fam)]["unjoined"] += 1
            continue
        g = t[hit[0]]
        g["ruled_calls"].add(run)
        g["rulings"] += 1
        g["classes"][cls] += 1
        if cls == "finding":
            g["severity"][severity or "unstated"] += 1
    return t


def bug_entries(root, ref=None):
    """Yield (kind, family, is_new) per BUG_INVENTORY entry, by what its Caught by line names."""
    text = open(os.path.join(root, "BUG_INVENTORY.md"), encoding="utf-8").read()
    old = git_show(ref, "BUG_INVENTORY.md") or ""
    old_ids = set(re.findall(r"^## (BUG-\d+)", old, re.M))
    for e in re.split(r"\n(?=## BUG-)", text)[1:]:
        bid = re.match(r"## (BUG-\d+)", e).group(1)
        m = re.search(r"\*\*Caught by:\*\*(.*)", e)
        caught = (m.group(1) if m else "").lower()
        kind = next((k for w, k in BUG_KIND_WORDS if w in caught), "other")
        fam = "deepseek" if "deepseek" in caught else "gpt" if re.search(r"\bgpt", caught) else families.DEFAULT
        yield kind, fam, bool(ref) and bid not in old_ids


def read_jsonl(path):
    rows = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def cost_table(rows):
    t = defaultdict(lambda: {"calls": 0, "failed": 0, "usd": 0.0})
    for r in rows:
        g = t[(r.get("kind") or "-", families.family_of(r.get("model_requested") or "-"))]
        g["calls"] += 1
        g["failed"] += r.get("outcome") != "ok"
        g["usd"] += r.get("estimated_cost_usd") or 0
    return t


def evidence_table(items, bugs, new_only):
    t = defaultdict(lambda: {"rulings": 0, "classes": Counter(), "bugs": 0})
    for kind, fam, cls, new in items:
        if new_only and not new:
            continue
        g = t[(kind, fam)]
        g["rulings"] += 1
        g["classes"][cls] += 1
    for kind, fam, new in bugs:
        if new_only and not new:
            continue
        t[(kind, fam)]["bugs"] += 1
    return t


def agent_table(runs):
    t = defaultdict(lambda: {"runs": 0, "tokens": 0, "tool_uses": 0, "minutes": 0.0})
    for r in runs:
        g = t[r.get("date", "-")]
        g["runs"] += 1
        g["tokens"] += r.get("subagent_tokens") or 0
        g["tool_uses"] += r.get("tool_uses") or 0
        g["minutes"] += (r.get("duration_ms") or 0) / 60000
    return dict(sorted(t.items()))


def per(usd, n):
    return f"{usd / n:.2f}" if n else "-"


def noise(classes, n):
    return f"{100 * classes['model error'] / n:.0f}" if n else "-"


def render(ledger, runs, items, bugs, ref, stamped=()):
    items, bugs, stamped = list(items), list(bugs), list(stamped)
    cost = cost_table(ledger)
    out = []
    w = out.append
    w("# Review yield: cost against evidence (T-220)\n")
    w("Generated by `python3 tools/transcription/costs.py --yield`. Limits, read these first:\n")
    first = min((r.get("timestamp", "") for r in ledger), default="-")
    last = max((r.get("timestamp", "") for r in ledger), default="-")
    w(f"- The ledger covers only {len(ledger)} calls from {first[:16]} to {last[:16]} UTC. Earlier reviews have rulings but no cost.")
    w(f"- Rulings written before stamping (T-223) carry no date. The window table counts rulings and bug entries absent at `{ref}` (the commit before the ledger began), so the "
      "dollars sit beside the evidence they bought. A ruling edited in the window counts as new; window output not yet ruled is cost with no evidence. "
      "Stamped rulings are also joined to their calls exactly (the exact-join table).")
    w("- Dollars are the ledger's estimated cost (the transport-reported cost where one exists, else the cited list price). "
      "gpt-6-astra calls were mostly usage-limit failures and cost nothing.")
    w("- A finding is a ruling classed finding, defect or real gap, or a screen NARROW finding ruled a defect. Severity is recorded only on stamped "
      "findings, so only the exact-join table splits findings by severity. Bugs are the BUG_INVENTORY entries whose Caught by line names the kind.")
    w("- Noise is the model-error share of rulings (completeness: claims ruled covered or wrong). A transcription or render ruling is a "
      "disagreement to adjudicate, not a claimed defect, so the model-error share is the adjudication cost of the kind.\n")
    for title, new_only in (("Window (rulings and bugs new since the ledger began)", True), ("All-time (no cost attached)", False)):
        ev = evidence_table(items, bugs, new_only)
        w(f"## {title}\n")
        head = ["kind", "family"] + (["calls", "failed", "$"] if new_only else []) + ["rulings"] + CLASSES + ["noise %", "bugs caught"] \
            + (["$/finding", "$/bug"] if new_only else [])
        w("| " + " | ".join(head) + " |")
        w("|" + " --- |" * len(head))
        keys = sorted(set(ev) | (set(cost) if new_only else set()), key=lambda k: (KINDS.index(k[0]) if k[0] in KINDS else 99, k[1]))
        tot = {"calls": 0, "failed": 0, "usd": 0.0, "rulings": 0, "bugs": 0, "classes": Counter()}
        empty = {"calls": 0, "failed": 0, "usd": 0.0}
        for k in keys:
            c = cost.get(k, empty) if new_only else empty
            e = ev.get(k, {"rulings": 0, "classes": Counter(), "bugs": 0})
            row = [k[0], k[1]]
            if new_only:
                row += [str(c["calls"]), str(c["failed"]), f"{c['usd']:.2f}"]
            row += [str(e["rulings"])] + [str(e["classes"][x]) for x in CLASSES]
            row += [noise(e["classes"], e["rulings"]), str(e["bugs"])]
            if new_only:
                row += [per(c["usd"], e["classes"]["finding"]), per(c["usd"], e["bugs"])]
            w("| " + " | ".join(row) + " |")
            for x in empty:
                tot[x] += c[x]
            tot["rulings"] += e["rulings"]
            tot["bugs"] += e["bugs"]
            tot["classes"].update(e["classes"])
        row = ["total", ""]
        if new_only:
            row += [str(tot["calls"]), str(tot["failed"]), f"{tot['usd']:.2f}"]
        row += [str(tot["rulings"])] + [str(tot["classes"][x]) for x in CLASSES]
        row += [noise(tot["classes"], tot["rulings"]), str(tot["bugs"])]
        if new_only:
            row += [per(tot["usd"], tot["classes"]["finding"]), per(tot["usd"], tot["bugs"])]
        w("| " + " | ".join(row) + " |\n")
    w("## Exact join (stamped rulings)\n")
    w("Rulings rule.py wrote since stamping (T-223) name the reply they rule (`run`); calls the ledger recorded since then name "
      "the reply they returned (`response_sha256`). Joined on that identity, cost and evidence need no git window. Ledger calls "
      "without a reply identity (before stamping, or failed) are not counted here; a stamped ruling on a reply no such call "
      "returned is counted as unjoined.\n")
    exact = exact_table(ledger, stamped)
    if not exact:
        w("No stamped ruling and no ledger call with a reply identity yet.\n")
    else:
        head = ["kind", "family", "calls", "$", "calls ruled", "rulings"] + CLASSES + ["findings by severity", "$/finding", "unjoined rulings"]
        w("| " + " | ".join(head) + " |")
        w("|" + " --- |" * len(head))
        for k in sorted(exact, key=lambda k: (KINDS.index(k[0]) if k[0] in KINDS else 99, k[1])):
            g = exact[k]
            sev = ", ".join(f"{s} {n}" for s, n in sorted(g["severity"].items())) or "-"
            w("| " + " | ".join([k[0], k[1], str(g["calls"]), f"{g['usd']:.2f}", str(len(g["ruled_calls"])), str(g["rulings"])]
                                + [str(g["classes"][x]) for x in CLASSES]
                                + [sev, per(g["usd"], g["classes"]["finding"]), str(g["unjoined"])]) + " |")
        w("")
    w("## Agent tokens per day (research/costs/agent_runs.jsonl)\n")
    w("Subagent tokens are as the task notifications reported them (cost_usd is null). They are not comparable to ledger dollars.\n")
    w("| day | runs | subagent tokens | tool uses | minutes |")
    w("| --- | --- | --- | --- | --- |")
    for day, g in agent_table(runs).items():
        w(f"| {day} | {g['runs']} | {g['tokens']:,} | {g['tool_uses']} | {g['minutes']:.0f} |")
    return "\n".join(out) + "\n"


def run(ledger_path, runs_path, ref, root=ROOT, out=None):
    text = render(read_jsonl(ledger_path), read_jsonl(runs_path), ruling_items(root, ref), bug_entries(root, ref), ref,
                  stamped_items(root))
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    return text


def default_ledger():
    import transcribe
    return os.path.join(transcribe.RAW, transcribe.LEDGER_NAME)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--agent-runs", default=os.path.join(ROOT, "research", "costs", "agent_runs.jsonl"))
    ap.add_argument("--window-ref", default="0a43f15")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    text = run(a.ledger or default_ledger(), a.agent_runs, a.window_ref, out=a.out)
    if not a.out:
        print(text)


if __name__ == "__main__":
    main()
