#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""New-consumer definition check (T-087), offline, in check-all.

A Bool, Enum or Count input answers one question, written for one rule. When a line governed by another section of
the sources reads it, the input must mean what that section requires (BUG-0034, BUG-0092, BUG-0096 and BUG-0157 were
inputs read by a second rule with a different definition). Every pair (input, document page cited by a reading line,
other than the pages the input itself cites) needs a verdict ruling in reviews/<year>/consumers.json:

    "consumer:<input>@<doc>:p<page>": {"verdict": "same" | "differs",
                                      "question_phrase": "<the defining words of the input's question>",
                                      "source_phrase": "<the defining words of that page's rule>",
                                      "reason": "<one sentence>"}

A "differs" verdict is a defect to fix (split the input or add one); it is accepted only with "fixed_by" naming the
bug entry. Pairs that existed when the check was introduced form the baseline (tools/baseline_check.py), each held
while the input's question is unchanged. `--prompts DIR` writes one model prompt per open pair (the question and the
page text), for drafting verdicts to adjudicate.

    check_consumers.py [--baseline] [--prompts DIR] | --self-test
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
from citations import segments  # noqa: E402
import baseline_check  # noqa: E402
import archive_text  # noqa: E402

CANONICAL = ROOT / "canonical" / Y
SOURCES = ROOT / "sources" / Y
RULINGS = ROOT / "reviews" / Y / "consumers.json"
REPORT = ROOT / "reports" / Y / "consumers.md"
KINDS = re.compile(r"^(Bool|Count|Enum\(.*\))$")


def refs(node, ids):
    if isinstance(node, str):
        return {node} if node in ids else set()
    if isinstance(node, dict):
        return set().union(*(refs(v, ids) for k, v in node.items() if k not in ("op", "source", "cite"))) if node else set()
    if isinstance(node, list):
        return set().union(*(refs(v, ids) for v in node)) if node else set()
    return set()


def pages_of(cite):
    return {(doc, p) for doc, pages, _, _, _ in segments(cite.get("doc", ""), cite.get("locator", "")) for p in pages}


def findings(forms):
    lines = {l["id"]: dict(l, form=f["id"]) for f in forms for l in f["lines"]}
    inputs = {i: l for i, l in lines.items()
              if l.get("expr", {}).get("op") == "input" and KINDS.match(str(l.get("type", "")))}
    out = []
    for cid, consumer in lines.items():
        read = refs({"expr": consumer.get("expr"), "refuses": consumer.get("refuses"), "shown": consumer.get("shown_when")},
                    inputs)
        for iid in read - {cid}:
            own = pages_of(inputs[iid].get("cite", {}))
            for doc, page in sorted(pages_of(consumer.get("cite", {})) - own):
                question = inputs[iid]["expr"].get("source", inputs[iid].get("label", ""))
                k = f"{iid}@{doc}:p{page}"
                out.append({"kind": "consumer", "line": k, "form": inputs[iid]["form"],
                            "subject": question, "input": iid, "doc": doc, "page": page, "reader": cid,
                            "detail": f"`{iid}` is read by `{cid}`, which cites {doc} p. {page}"})
    # One finding per (input, page), naming the first reader.
    seen, unique = set(), []
    for f in out:
        if f["line"] not in seen:
            seen.add(f["line"])
            unique.append(f)
    return unique


def check_rulings(found):
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    errors = []
    for k, r in data.get("rulings", {}).items():
        if not isinstance(r, dict) or r.get("verdict") not in ("same", "differs"):
            errors.append(f"  ruling {k}: verdict must be \"same\" or \"differs\"")
        elif not (r.get("question_phrase") and r.get("source_phrase")):
            errors.append(f"  ruling {k}: quote the defining phrase of the question and of the source")
        elif r["verdict"] == "differs" and not str(r.get("fixed_by", "")).startswith("BUG-"):
            errors.append(f"  ruling {k}: a \"differs\" verdict is a defect; name the bug entry that fixes it (fixed_by)")
    return errors


def write_prompts(found, folder):
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    accepted = set(data.get("rulings", {})) | set(data.get("baseline", {}))
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in found:
        k = baseline_check.key(f)
        if k in accepted:
            continue
        entry = archive_text.manifest(SOURCES).get(f["doc"], {})
        pages = archive_text.read(SOURCES, entry, key="cols_file").split("\f") if "cols_file" in entry else []
        text = pages[f["page"] - 1] if 0 < f["page"] <= len(pages) else "(page not archived)"
        (folder / (re.sub(r"[^A-Za-z0-9_.@-]", "_", f["line"]) + ".txt")).write_text(
            f"An interview question in a tax tool is answered once and read by a rule on the IRS page below.\n\n"
            f"Question (`{f['input']}`): {f['subject']}\n\nRead by: `{f['reader']}`\n\n"
            f"Does the rule on this page need exactly what the question asks? Answer \"same\" or \"differs\", quote the "
            f"defining words of the question and of the page, and give one sentence of reason.\n\n"
            f"{f['doc']} p. {f['page']}:\n{text}\n", encoding="utf-8")
        n += 1
    print(f"consumers: wrote {n} prompt(s) to {folder}")


def check(rebaseline=False):
    forms = baseline_check.load_forms(CANONICAL)
    found = findings(forms)
    status = baseline_check.run(
        "consumers", forms, found, RULINGS, REPORT, "New-consumer definition check",
        "Generated by `tools/check_consumers.py` (T-087): Bool, Enum and Count inputs read by a line citing a page "
        "the input does not cite; each pair needs a verdict that the page's rule needs what the question asks.",
        rebaseline)
    errors = check_rulings(found)
    for e in errors:
        print(e)
    return 1 if status or errors else 0


def self_test():
    forms = [{"id": "x", "lines": [
        {"id": "x.q", "type": "Bool", "expr": {"op": "input", "source": "Q?"}, "cite": {"doc": "i1040gi", "locator": "p. 14"}},
        {"id": "x.a", "type": "Bool", "expr": {"op": "test", "eq": ["x.q", {"const": True}]},
         "cite": {"doc": "i1040gi", "locator": "p. 14"}},
        {"id": "x.b", "type": "Bool", "expr": {"op": "test", "eq": ["x.q", {"const": True}]},
         "cite": {"doc": "i1040gi", "locator": "p. 42"}}]}]
    assert [f["line"] for f in findings(forms)] == ["x.q@i1040gi:p42"]
    print("consumers self-test: ok")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    if "--prompts" in sys.argv:
        write_prompts(findings(baseline_check.load_forms(CANONICAL)), sys.argv[sys.argv.index("--prompts") + 1])
        sys.exit(0)
    sys.exit(check(rebaseline="--baseline" in sys.argv))
