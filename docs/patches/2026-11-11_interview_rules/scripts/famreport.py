# usage: python3 -I famreport.py <family> <witness set>
import json, sys, os, re
fam, ws = sys.argv[1], sys.argv[2]
O = f"/tmp/f1095a/out/fam_{fam}"
def tail(f, n=1):
    try: return [l.rstrip()[:400] for l in open(f"{O}/{f}").read().strip().split("\n")[-n:]]
    except Exception as e: return [f"(missing {f})"]
print(f"##### {fam}: {open(O+'/done').read().strip() if os.path.exists(O+'/done') else 'not finished'}")
print("nest:", " | ".join(tail("nest.txt", 12)))
print("build:", tail("build.txt")[0])
for j in ("fed", "ny"):
    t = open(f"{O}/fixtures_{j}.txt").read() if os.path.exists(f"{O}/fixtures_{j}.txt") else ""
    fails = [l.strip()[:500] for l in t.split("\n") if re.search(r"FAIL|fail|mismatch|expected", l) and "passed" not in l]
    print(f"fixtures {j}:", " / ".join(tail(f"fixtures_{j}.txt", 2)), f"| failing lines: {len(fails)}")
    for l in fails[:12]: print("     ", l)
print("differential:", " | ".join(tail("differential.txt", 3)))
print("pins:", " | ".join(tail("pins.txt", 8)))
print("rendered files changed:", " ".join(tail("rendered_changed.txt", 30))[:600])
print("diffstat:", " | ".join(tail("diffstat.txt", 4)))
try:
    a = json.load(open(f"/tmp/f1095a/out/base_measure_{ws}.json")); b = json.load(open(f"{O}/measure.json"))
except Exception as e:
    print("measure: missing", e); sys.exit()
cats = ("unread", "out", "reached", "randomEarly", "early")
before, after = set(), set(); qa = qb = 0; changed = 0; n = 0; stat = 0; vals = 0; errs = 0
for k, ra in a["returns"].items():
    rb = b["returns"].get(k)
    if not rb or ra.get("kind") != "walked" or rb.get("kind") != "walked": print("   not comparable", k, rb); continue
    n += 1; qa += ra["asked"]; qb += rb["asked"]; changed += ra["asked"] != rb["asked"]
    stat += ra["status"] != rb["status"]; vals += ra["valuesKey"] != rb["valuesKey"]; errs += len(rb.get("errors") or [])
    for c in cats:
        before |= {(c, t) for t in ra.get(c) or []}; after |= {(c, t) for t in rb.get(c) or []}
print(f"witness returns: {n}; questions asked in bank order {qa} -> {qb} (saved {qa - qb}, on {changed} returns); status differs on {stat}, values differ on {vals}, order errors after {errs}")
print("   templates gone:", sorted(before - after))
print("   templates NEW :", sorted(after - before))
print("   templates left:", sorted(after & before))
sa = sum(v.get("asked", 0) for v in a["standard"].values()); sb = sum(v.get("asked", 0) for v in b["standard"].values())
dv = [k for k in a["standard"] if a["standard"][k].get("valuesKey") != b["standard"].get(k, {}).get("valuesKey") or a["standard"][k].get("status") != b["standard"].get(k, {}).get("status")]
print(f"standard length set (full profile: {len(a['standard'])} walks): questions {sa} -> {sb}; status/values differ on {dv}")
