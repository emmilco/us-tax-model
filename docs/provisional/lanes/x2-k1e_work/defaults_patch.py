"""Add the k1e inputs' fixture defaults to fixtures/2025/defaults.json (lane x2-k1e). Idempotent; keeps sort order by input."""
import json, sys, yaml
path = sys.argv[1] if len(sys.argv) > 1 else "fixtures/2025/defaults.json"
form = yaml.safe_load(open("forms/2025/k1e.yaml"))["form"]
d = json.load(open(path))
have = {r["input"] for r in d["defaults"]}
new = [{"input": "$k1e", "value": [], "reason": "None: " + form["title"] + " entries are listed only where the scenario has them."}]
for l in form["lines"]:
    if l["expr"].get("op") != "input":
        continue
    if l["type"] == "Bool":
        new.append({"input": l["id"], "value": False, "reason": "Closed: the circumstance this question asks about does not apply unless the scenario says so."})
    else:
        new.append({"input": l["id"], "value": 0, "reason": "Closed: no amount unless the scenario states one."})
added = [r for r in new if r["input"] not in have]
for r in added:
    rows = d["defaults"]
    pos = next((i for i, x in enumerate(rows) if x["input"] > r["input"]), len(rows))
    rows.insert(pos, r)
with open(path, "w") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("added", len(added))
