"""Evaluate a fixture case with overrides: run.py <fixture> <case id> <targets,comma> [key=json ...]

Prints the evaluator's output for the targets. Run from the repository root.
"""
import json
import subprocess
import sys
import tempfile

fixture, case_id, targets = sys.argv[1:4]
cases = json.load(open(fixture))["cases"]
c = [c for c in cases if c["id"] == case_id][0]
inputs = dict(c["inputs"])
for kv in sys.argv[4:]:
    k, v = kv.split("=", 1)
    if v == "DELETE":
        inputs.pop(k, None)
    else:
        inputs[k] = json.loads(v)
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir="research/audits/credits-misc/witness") as f:
    json.dump(inputs, f)
    path = f.name
out = subprocess.run(["node", "engine/dist/main.js", "eval", "--inputs", path, "--target", targets],
                     capture_output=True, text=True)
import os
os.unlink(path)
print(out.stdout[:int(os.environ.get("N","2500"))], out.stderr[-2000:])
