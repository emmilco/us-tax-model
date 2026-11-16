"""Evaluate fixtures/2025/k1p.json cases with defaults; compare predictions; fill PENDING refusals whose gate matches."""
import sys, json, subprocess, tempfile, os
WT = sys.argv[1]; FILL = "--fill" in sys.argv
P = f"{WT}/fixtures/2025/k1p.json"; d = json.load(open(P))
main = f"{WT}/engine/dist/main.js"
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
    json.dump([{"id": c["id"], "file": "k1p.json", "inputs": c["inputs"]} for c in d["cases"]], f); cp = f.name
r = subprocess.run(["node", main, "fixture-inputs", "--cases", cp], capture_output=True, text=True, cwd=WT)
if r.returncode: print(r.stderr[:2000]); sys.exit(1)
filled = json.loads(r.stdout)["cases"]
fails = 0
for c in d["cases"]:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(filled[c["id"]], f); ip = f.name
    out = subprocess.run(["node", main, "eval", "--inputs", ip, "--json"], capture_output=True, text=True, cwd=WT)
    os.unlink(ip)
    if out.returncode:
        print("EVALFAIL", c["id"], out.stderr[:500]); fails += 1; continue
    vals = json.loads(out.stdout)["values"]
    for key, exp in c["expect"].items():
        got = vals.get(key, {}).get("value")
        if isinstance(exp, dict) and exp.get("PENDING"):
            if got and got.get("kind") == "refusal" and got.get("gate") == exp["gate"]:
                if FILL: c["expect"][key] = got
                print("ok-refusal", c["id"], got["gate"])
            else:
                fails += 1; print("MISMATCH", c["id"], key, "predicted gate", exp["gate"], "got", json.dumps(got)[:400])
        elif got != exp:
            fails += 1; print("MISMATCH", c["id"], key, "expected", exp, "got", json.dumps(got)[:400])
print("failures:", fails)
if FILL:
    json.dump(d, open(P, "w"), indent=1, ensure_ascii=False); open(P, "a").write("\n")
