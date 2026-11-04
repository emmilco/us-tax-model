"""Append a fixture case built from an existing one, as text, at the end of the cases array.

addcase.py <file> <base case id> <new id> <spec.json>

spec.json: {"covers": [...], "evidence": "...", "evidence_note": "...", "set": {input: value},
            "expect_from_base": true|false, "expect_drop": [...], "expect": {line: value}}
The expected values are written from the spec (the prediction), never from the evaluator.
"""
import json
import sys

path, base_id, new_id, spec_path = sys.argv[1:5]
spec = json.load(open(spec_path))
text = open(path).read()
cases = json.loads(text)["cases"]
base = [c for c in cases if c["id"] == base_id][0]
assert not any(c["id"] == new_id for c in cases), new_id
inputs = dict(base["inputs"])
inputs.update(spec.get("set", {}))
expect = dict(base["expect"]) if spec.get("expect_from_base") else {}
for k in spec.get("expect_drop", []):
    expect.pop(k)
expect.update(spec.get("expect", {}))
case = {"id": new_id, "covers": spec["covers"], "evidence": spec["evidence"],
        "evidence_note": spec["evidence_note"], "inputs": inputs, "expect": expect}
body = json.dumps(case, indent=2, ensure_ascii=False)
body = "\n".join("    " + line for line in body.split("\n"))
tail = "\n    }\n  ]\n}\n"
assert text.endswith(tail), repr(text[-40:])
text = text[: -len(tail)] + "\n    },\n" + body + "\n  ]\n}\n"
json.loads(text)
open(path, "w").write(text)
