# usage: python3 -I gen_tables.py > out/catalog_tables.md   (reads the sweep, traces, family summaries)
import json, glob, re, collections, os
O = "/tmp/f1095a/out"
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
rows = [json.loads(l) for f in glob.glob(f"{O}/base_sweep/s*.jsonl") for l in open(f)]
comp = [r for r in rows if r.get("status") == "complete"]
by = collections.defaultdict(lambda: collections.defaultdict(set)); inst = collections.Counter()
for r in comp:
    out = {T(k) for k in (r.get("outOfOrder") or {})}
    for c, ks in (("out", out | {T(k) for k in r.get("reached") or []}), ("unread", {T(k) for k in r.get("askedUnread") or []}), ("early", {T(k) for k in (r.get("early") or []) + (r.get("randomEarly") or []) + (r.get("subsetEarly") or [])})):
        for t in ks: by[t][c].add((r["seed"], r["i"]))
    bank = out
    for t in bank: by[t]["outbank"].add((r["seed"], r["i"]))
    for k in r.get("askedUnread") or []: inst[T(k)] += 1
causes = json.load(open(f"{O}/causes.json"))
PROBE = {}
for l in open(f"{O}/probe_early_base.txt"):
    m = re.match(r"(\S+): left reachable at (\d+) state\(s\); an answer refuses at (\d+); an answer changes a value \(still complete\) at (\d+); gates (.*?); e\.g\.", l)
    if m: PROBE[m.group(1)] = (int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5))
try: AV = {(c, t): (after, before) for c, t, after, before in json.load(open(f"{O}/all2_vs_base.json"))["left"]}
except Exception: AV = None
fam = json.load(open(f"{O}/famsummary.json"))
CAUSE_FAM = [("dependent.odc_person", "D1"), ("dependent.qualifying_relative", "D2"), ("dependent.income_exception", "D3"), ("dependent.qr_other_relation", "D4"), ("dependent.qr_household_member", "D4"),
    ("dependent.hoh_test", "D5"), ("dependent.edu_llc_tin_refused", "D6"), ("f8962.b_zero", "P1"), ("f8962.applicable", "P2"), ("f8962.alien_branch", "P2"), ("f5695.", "E1"), ("f8889.excess", "H1"), ("f8889.married_family", "H1"),
    ("scveh.", "V1"), ("retirement.", "R1"), ("ssb.mfs_together", "S1"), ("asset.s179_bad", "A1"), ("s1a.spouse_died_before_65_count", "X1"), ("carloan.eligible", "C1"), ("eic.step3_married", "X2"), ("f2441.nondependent_gate", "X3"),
    ("sa.itemizes", "X4"), ("eic.age_range_count", "X5"), ("eic.age_range", "L1"), ("household.any_work_ssn", "L1")]
FAMKEY = {"D1": "dep_odc", "D2": "dep_qr", "D3": "dep_incx", "D4": "dep_qrrel", "D5": "dep_hoh", "D6": "dep_edutin", "P1": "f8962_bzero", "P2": "f8962_applicable", "E1": "f5695", "H1": "f8889", "V1": "scveh", "R1": "retirement", "S1": "ssb",
          "A1": "asset", "X1": "s1a_died", "C1": "carloan", "X2": "eic_step3", "X3": "f2441", "X4": "sa", "X5": "eic_age"}
def cause_lines(t, cls):
    out = []
    for c in ((cls,) if cls != "out" else ("out", "random")):
        v = causes.get(f"{t}|{c}")
        if not v: continue
        for f in v["frontier"]:
            e = f["expr"]
            if not (e.startswith(("all(", "any(")) or ("sum_over" in e and "where" in e) or f["decided"]): continue
            if f["line"].startswith("f8962.line") and f["line"].endswith("b"): continue
            if f["line"] not in [x["line"] for x in out]: out.append(f)
    return out
def fam_of(lines):
    ids = []
    for f in lines:
        for pre, fid in CAUSE_FAM:
            if f["line"].startswith(pre) and fid not in ids: ids.append(fid)
    return ids
CLS = {"early": "left reachable at completion", "out": "reached only out of bank order", "unread": "asked and unread"}
monthly = sorted(t for t in by if t.startswith("f1095a.in_"))
print(f"Sweep: {len(rows)} generated federal returns ({len({r['seed'] for r in rows})} seeds of 50), {len(comp)} complete; {len(by)} templates; {len({x for cs in by.values() for c, v in cs.items() for x in v})} complete returns show at least one.\n")
print("| Template | Class | Returns (of %d complete) | Cause line: the operand read past | Family | Gone on the witness returns with one family's rewrite alone | With every rewrite (2,000 returns) |" % len(comp))
print("|---|---|---|---|---|---|---|")
def gone_in(t, cls):
    keys = {"early": [f"randomEarly:{t}", f"early:{t}"], "out": [f"out:{t}", f"reached:{t}"], "unread": [f"unread:{t}"]}[cls]
    yes = [k for k, r in fam.items() if r.get("witness") and any(x in r["witness"]["gone"] for x in keys)]
    return ", ".join(sorted(yes)) or "-"
def row(t, label=None, members=None):
    for cls in ("early", "out", "unread"):
        ms = members or [t]
        rs = set().union(*[by[m].get(cls, set()) for m in ms])
        if not rs: continue
        cl = cause_lines(t, cls)
        fams = fam_of(cl)
        extra = ""
        if cls == "out":
            b = set().union(*[by[m].get("outbank", set()) for m in ms]); extra = f" ({len(b)} seen in the bank-order walk itself, the rest only in a random order)"
        if cls == "unread": extra = f" ({sum(inst[m] for m in ms)} questions)"
        sev = ""
        if cls == "early" and t in PROBE:
            n, ref, val, gates = PROBE[t]
            sev = (f". **At {ref} of {n} such states an answer refuses the return** (gate `{gates}`)" if ref else f". At {n} such states no answer changes the status or a value")
        cells = "; ".join("`%s` := `%s`" % (f["line"], f["expr"][:230] + ("…" if len(f["expr"]) > 230 else "")) for f in cl) or "(not traced)"
        in2000 = any(sd <= 40 for m in ms for (sd, _) in by[m].get(cls, set()))
        left = "not measured" if AV is None else ("left on %d return(s)" % sum(AV[(cls, m)][0] for m in ms if (cls, m) in AV) if any((cls, m) in AV for m in ms) else "gone" if in2000 else "not in these 2,000 on main either")
        print(f"| `{label or t}` | {CLS[cls]}{sev} | {len(rs)}{extra} | {cells} | {', '.join(fams) or '-'} | {gone_in(t, cls)} | {left} |")
for t in sorted(by):
    if t.startswith("f1095a.in_a_") or t.startswith("f1095a.in_b_"): continue
    row(t)
row("f1095a.in_a_apr", "f1095a.in_a_<month> (12 templates)", [m for m in monthly if ".in_a_" in m])
row("f1095a.in_b_apr", "f1095a.in_b_<month> (12 templates)", [m for m in monthly if ".in_b_" in m])
