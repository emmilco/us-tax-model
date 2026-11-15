#!/usr/bin/env python3
"""Lane 2a: state the new dependent inputs in the fixture files that take no defaults (class M and mutation).

Run from the worktree root. Idempotent: an input a case already states is left alone. Each new input gets the answer
that leaves the case's stated answers read as before, so no expected value moves:
  lived_all_year  true where the case states 12 months (and the person was not kidnapped, and no all-year household
                  answer of No is read); false otherwise, so the months answer is read
  ever_married, own_money, parents_apart   true (the answer that opens the questions the case already answers)
  self_support_view, supported_view        unsure (the answer that opens the full support test the case answers)
  citizen_ssn     false, so the citizenship, number and card answers the case states are read
"""
import json
FILES = [("fixtures/2025/classm.json", 2, False), ("fixtures/2025/classm.deepseek.json", 2, False),
         ("fixtures/2025/classm.gpt.json", 2, False), ("fixtures/2025/mutation.json", 2, False),
         ("fixtures/ny/2025/classm.json", 2, False), ("fixtures/ny/2025/classm.deepseek.json", 2, False),
         ("fixtures/ny/2025/mutation.json", 1, True)]
HOUSEHOLD = ("household_member", "sibling_descendant", "other")

def new_inputs(inp, d):
    g = lambda k: inp.get(f"{d}.{k}")
    all_year = g("months") == 12 and g("kidnapped") is not True and not (g("qr_all_year") is False and g("relationship") in HOUSEHOLD)
    return {"lived_all_year": all_year, "ever_married": True, "own_money": True, "parents_apart": True,
            "self_support_view": "unsure", "supported_view": "unsure", "citizen_ssn": False}

changed = 0
for path, indent, ascii_ in FILES:
    doc = json.load(open(path, encoding="utf-8"))
    for case in doc["cases"]:
        inp = case.get("inputs", {})
        for key in inp.get("$dependent") or []:
            d = f"dependent[{key}]"
            add = {f"{d}.{k}": v for k, v in new_inputs(inp, d).items() if f"{d}.{k}" not in inp}
            if not add: continue
            out, last = {}, None
            for k in inp:
                if k.startswith(d + "."): last = k
            for k, v in inp.items():
                out[k] = v
                if k == last: out.update(add)
            if last is None: out.update(add)
            case["inputs"] = inp = out
            changed += len(add)
    open(path, "w", encoding="utf-8").write(json.dumps(doc, indent=indent, ensure_ascii=ascii_) + "\n")
print("inputs added:", changed)
