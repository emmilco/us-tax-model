#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Three-way merge of a class M fixture file (fixtures/<year>/classm.json) by case id.

    merge_classm.py BASE THEIRS OURS OUT
    merge_classm.py --self-test

BASE is the file both sides started from (the lanes' common snapshot), THEIRS a lane's file, OURS the integration
tree's file; the result is written to OUT. Each case is taken from the side that changed it relative to BASE (added,
changed or removed). Two further cases are merged rather than refused:
- THEIRS removed a case and OURS only added inputs to it: the removal wins;
- both changed a case and OURS only added inputs (a new input stated in every case): THEIRS's case, with OURS's
  added inputs carried onto it.
Any other case both sides changed differently is a conflict: the merge names the cases and writes nothing. The
order is OURS's, with the cases only THEIRS added appended in THEIRS's order. Keys other than "cases" come from OURS.
"""
import json
import sys
import tempfile
from pathlib import Path


def only_added_inputs(b, o):
    """True if case o equals case b except for inputs o adds (b's inputs unchanged)."""
    return (all(o.get(k) == b.get(k) for k in set(o) | set(b) if k != "inputs")
            and all(k in o["inputs"] and o["inputs"][k] == v for k, v in b["inputs"].items()))


def merge(B, T, O):
    """Return (merged document, number of cases taken from THEIRS, conflicting case ids)."""
    bc = {c["id"]: c for c in B["cases"]}
    tc = {c["id"]: c for c in T["cases"]}
    oc = {c["id"]: c for c in O["cases"]}
    ids = list(dict.fromkeys([c["id"] for c in O["cases"]] + [c["id"] for c in T["cases"]] + list(bc)))
    merged, conflicts, taken = {}, [], 0
    for i in ids:
        b, t, o = bc.get(i), tc.get(i), oc.get(i)
        if t == o or t == b:
            r = o
        elif o == b:
            r, taken = t, taken + 1
        elif t is None and o is not None and b is not None and only_added_inputs(b, o):
            r, taken = None, taken + 1
        elif t is not None and o is not None and b is not None and only_added_inputs(b, o):
            r = dict(t)
            r["inputs"] = {**t["inputs"], **{k: v for k, v in o["inputs"].items() if k not in b["inputs"]}}
            taken += 1
        else:
            conflicts.append(i)
            continue
        if r is not None:
            merged[i] = r
    order = ([c["id"] for c in O["cases"] if c["id"] in merged]
             + [c["id"] for c in T["cases"] if c["id"] in merged and c["id"] not in oc])
    res = dict(O)
    res["cases"] = [merged[i] for i in order]
    return res, taken, conflicts


def write(doc, out):
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")


def self_test():
    def case(i, **inputs):
        return {"id": i, "inputs": dict(inputs), "expected": {"x": 1}}
    B = {"cases": [case("a", p=1), case("b", p=1), case("c", p=1), case("d", p=1)]}
    T = {"cases": [case("a", p=2), case("b", p=1), case("e", p=1)]}            # changes a, removes c and d, adds e
    O = {"cases": [case("a", p=1, n=0), case("b", p=1), case("c", p=1, n=0), case("d", p=3)]}  # adds n; changes d
    res, taken, conflicts = merge(B, T, O)
    failures = []
    if conflicts != ["d"]:
        failures.append(f"conflicts {conflicts}, expected ['d'] (both sides changed d)")
    O2 = {"cases": [case("a", p=1, n=0), case("b", p=1), case("c", p=1, n=0), case("d", p=1)]}
    res, taken, conflicts = merge(B, T, O2)
    got = {c["id"]: c["inputs"] for c in res["cases"]}
    want = {"a": {"p": 2, "n": 0}, "b": {"p": 1}, "e": {"p": 1}}
    if conflicts or got != want or [c["id"] for c in res["cases"]] != ["a", "b", "e"]:
        failures.append(f"merged {got} conflicts {conflicts}, expected {want} in order a, b, e")
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "out.json"
        write(res, out)
        if json.loads(out.read_text(encoding="utf-8")) != res:
            failures.append("written file does not read back as the merge")
    for f in failures:
        print(f"merge_classm self-test: {f}", file=sys.stderr)
    if failures:
        return 1
    print("merge_classm self-test: ok")
    return 0


def main(argv):
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) != 4:
        sys.exit(__doc__)
    base, theirs, ours, out = argv
    B, T, O = (json.loads(Path(p).read_text(encoding="utf-8")) for p in (base, theirs, ours))
    res, taken, conflicts = merge(B, T, O)
    if conflicts:
        sys.exit(f"conflicts in {len(conflicts)} case(s): {conflicts[:10]}")
    write(res, out)
    print(f"merged: {len(res['cases'])} cases; {taken} taken from theirs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
