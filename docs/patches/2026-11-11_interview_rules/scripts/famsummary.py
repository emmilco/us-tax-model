# usage: python3 -I famsummary.py fam:witset ... > famsummary.json
import json, sys, os, re
res = {}
for arg in sys.argv[1:]:
    fam, ws = arg.split(":")
    O = f"/tmp/f1095a/out/fam_{fam}"
    rd = lambda f: open(f"{O}/{f}").read() if os.path.exists(f"{O}/{f}") else ""
    r = {"status": rd("done").strip() or "not finished", "nest": [l for l in rd("nest.txt").strip().split("\n") if l.startswith(("nest:", "hand:"))]}
    r["rewritten"] = [re.findall(r"nest: (\S+) ", l)[0] for l in r["nest"] if l.startswith("nest:")]
    patch = open(f"/tmp/f1095a/patches/{fam}.patch").read() if os.path.exists(f"/tmp/f1095a/patches/{fam}.patch") else ""
    r["helpers_added"] = len(re.findall(r"^\+\s*- id: ", patch, re.M)); r["files"] = re.findall(r"^\+\+\+ b/(\S+)", patch, re.M)
    r["patch_lines"] = [len(re.findall(r"^\+(?!\+\+)", patch, re.M)), len(re.findall(r"^-(?!--)", patch, re.M))]
    for j in ("fed", "ny"):
        m = re.search(r"fixtures: (\d+)/(\d+) passed", rd(f"fixtures_{j}.txt")); r[f"fixtures_{j}"] = f"{m.group(1)}/{m.group(2)}" if m else "?"
    d = rd("differential.txt"); m = re.search(r"(\d+) compared, (\d+) complete on base, (\d+) differ", d); r["differential"] = {"generated": int(m.group(1)), "complete": int(m.group(2)), "differ": int(m.group(3))} if m else None
    r["fixture_inputs_differ"] = [int(x) for x in re.findall(r"fixtures \w+ .*?: \d+ compared, (\d+) differ", d)]
    p = rd("pins.txt"); m = re.search(r"(\d+) hold on the base data, (\d+) of those move", p); r["pins"] = {"live": int(m.group(1)), "moved": int(m.group(2))} if m else None
    rc = rd("rendered_changed.txt").strip().split("\n"); r["rendered"] = [x.split()[-1] for x in rc[1:] if x.strip()]
    try:
        a = json.load(open(f"/tmp/f1095a/out/base_measure_{ws}.json")); b = json.load(open(f"{O}/measure.json"))
        cats = ("unread", "out", "reached", "randomEarly", "early"); before, after = set(), set(); qa = qb = ch = n = st = vl = er = 0
        for k, ra in a["returns"].items():
            rb = b["returns"].get(k)
            if not rb or ra.get("kind") != "walked" or rb.get("kind") != "walked": continue
            n += 1; qa += ra["asked"]; qb += rb["asked"]; ch += ra["asked"] != rb["asked"]; st += ra["status"] != rb["status"]; vl += ra["valuesKey"] != rb["valuesKey"]; er += len(rb.get("errors") or [])
            for c in cats:
                before |= {f"{c}:{t}" for t in ra.get(c) or []}; after |= {f"{c}:{t}" for t in rb.get(c) or []}
        r["witness"] = {"returns": n, "asked_before": qa, "asked_after": qb, "returns_shorter": ch, "status_differs": st, "values_differ": vl, "order_errors": er, "gone": sorted(before - after), "new": sorted(after - before), "left": sorted(after & before)}
        r["standard"] = {"walks": len(a["standard"]), "before": sum(v.get("asked", 0) for v in a["standard"].values()), "after": sum(v.get("asked", 0) for v in b["standard"].values()),
                         "differs": [k for k in a["standard"] if a["standard"][k].get("valuesKey") != b["standard"].get(k, {}).get("valuesKey") or a["standard"][k].get("status") != b["standard"].get(k, {}).get("status")]}
    except Exception as e:
        r["witness"] = None; r["error"] = str(e)
    res[fam] = r
print(json.dumps(res, indent=1))
