"""Add k1p input defaults and consistency rules to fixtures/2025/defaults.json (idempotent).
Lane x2-k1p's own default additions; applied on top of whatever defaults.json the tree holds."""
import sys, json, yaml

WT = sys.argv[1]
P = f"{WT}/fixtures/2025/defaults.json"
d = json.load(open(P))
form = yaml.safe_load(open(f"{WT}/forms/2025/k1p.yaml"))["form"]
inputs = [l for l in form["lines"] if l["expr"]["op"] == "input"]
SPECIAL = {
    "k1p.ptp": (False, "false: a partnership that is not publicly traded; true refuses the return (PTP rules are out of scope)."),
    "k1p.general": (False, "false: a limited partner or other LLC member, the usual investor; the scenario states a general partner."),
    "k1p.work": (False, "false: the partner did not work in the business (an investor) unless the scenario says so."),
}
d["defaults"] = [e for e in d["defaults"] if not (e["input"].startswith("k1p.") or e["input"] == "$k1p")]
new = [{"input": "$k1p", "value": [], "reason": "None: Schedule K-1 (Form 1065) — one partner's share from one partnership entries are listed only where the scenario has them."}]
for l in inputs:
    i = l["id"]
    if i in SPECIAL:
        v, r = SPECIAL[i]
    elif l["type"] == "Bool":
        v, r = False, "Closed: the circumstance this question asks about does not apply unless the scenario says so."
    else:
        v, r = 0, "Closed: no amount unless the scenario states one."
    new.append({"input": i, "value": v, "reason": r})
d["defaults"].extend(new)

RULES = [
    {"never": [{"input": "k1p.box6b", "gt_input": "k1p.box6a"}],
     "reason": "Qualified dividends (box 6b) are part of the ordinary dividends (box 6a)."},
]
# only add rules whose form the checker accepts; see report (rules kept out if the schema has no comparison of two inputs)
json.dump(d, open(P, "w"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
print("defaults: added", len(new))
