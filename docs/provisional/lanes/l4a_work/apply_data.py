#!/usr/bin/env python3
"""Lane 4a: rewrite the inputs of fixtures, the defaults and the profile lists for the retirement and social security
model change (gen_retirement.py, gen_ssb.py). Expected values and refusals are not touched. Idempotent."""
import json, glob, re, sys

RET_NEW = ["rollover_any", "roth_moved", "rollover_property", "rollover_qdro", "levy_returned", "charity_hsa", "ira_returned",
           "ira_basis", "box6", "loan_offset", "disability", "dis_early", "dis_terror", "dis_military", "pso_exclusion",
           "born_1936", "lump_sum", "death_exclusion", "ben_before_retire", "ben_guaranteed", "ben_shared", "cost_any",
           "own_annuity", "csrs_alt", "start_1996", "general_rule", "lump_at_start", "disaster", "under59", "sec457",
           "code2_partial", "not_beneficiary"]
SSB_NEW = ["any", "ira_covered", "repaid_more", "prior_year_pay", "lump_elect"]
counts = {}
def bump(k): counts[k] = counts.get(k, 0) + 1

FULL = False   # set per file: classm*.json and mutation.json take no defaults (engine/src/fixture-inputs.ts)

def reachable(d, pre):
    """The new inputs an entry can be asked, from its stated account and code (all of them when either is missing)."""
    acct, code = d.get(pre + ".account"), d.get(pre + ".code")
    if acct is None or code is None: return list(RET_NEW)
    r = ["disaster"]
    direct = code == "direct_rollover_G"
    roll = d.get(pre + ".rollover")
    if not direct: r.append("rollover_any")
    if direct or (isinstance(roll, (int, float)) and roll > 0): r += ["roth_moved", "rollover_property", "rollover_qdro", "levy_returned"]
    if acct != "plan": r += ["charity_hsa", "ira_returned"]
    if acct == "traditional_ira": r.append("ira_basis")
    if acct == "plan":
        r += ["box6", "loan_offset", "disability", "pso_exclusion", "born_1936", "cost_any"]
        if d.get(pre + ".annuity") is True: r += ["own_annuity", "csrs_alt", "start_1996", "general_rule", "lump_at_start"]
        if code == "death_4": r += ["death_exclusion", "ben_before_retire", "ben_guaranteed", "ben_shared"]
    r += {"normal_7": ["under59"], "early_exception_2": ["code2_partial"], "death_4": ["not_beneficiary"]}.get(code, [])
    return r

def fix_inputs(d):
    """d: one dict of inputs (keys are input ids). Returns the rewritten dict, key order kept."""
    out = {}
    if FULL:
        d = dict(d)
        for k in list(d):
            m = re.match(r"(.*retirement\[[^\]]+\])\.account$", k)
            if m:
                pre = m.group(1)
                roll, code = d.get(pre + ".rollover"), d.get(pre + ".code")
                for n in reachable(d, pre):
                    v = False
                    if n == "rollover_any": v = isinstance(roll, (int, float)) and roll > 0
                    if n == "cost_any": v = d.get(pre + ".annuity") is True
                    if n == "disaster" and d.get(pre + ".special") is not None: v = d[pre + ".special"]
                    if n == "under59" and code == "normal_7" and d.get(pre + ".code_screen"): v = True
                    if n == "code2_partial" and code == "early_exception_2" and d.get(pre + ".code_screen"): v = True
                    if n == "not_beneficiary" and code == "death_4" and d.get(pre + ".code_screen"): v = True
                    d.setdefault(f"{pre}.{n}", v)
                d.pop(pre + ".special", None); d.pop(pre + ".code_screen", None)
        if "ssb.benefits" in d:
            ben = d["ssb.benefits"]
            d.setdefault("ssb.any", isinstance(ben, (int, float)) and ben > 0)
        if "ssb.pub915" in d:
            d.setdefault("ssb.repaid_more", d["ssb.pub915"]); d.setdefault("ssb.ira_covered", False); del d["ssb.pub915"]
        if "ssb.lump_sum" in d:
            d.setdefault("ssb.prior_year_pay", d["ssb.lump_sum"] is True)
            if d["ssb.lump_sum"] is True: d.setdefault("ssb.lump_elect", True)
            del d["ssb.lump_sum"]
    for k, v in d.items():
        m = re.match(r"(.*retirement\[[^\]]+\])\.(special|code_screen|rollover|annuity)$", k)
        if m:
            pre, f = m.groups()
            if f == "special":
                bump("special")
                if v is not False: out[pre + ".disaster"] = v; bump("special->disaster")
                continue
            if f == "code_screen":
                bump("code_screen")
                if v is not False:
                    code = d.get(pre + ".code", "normal_7")
                    t = {"normal_7": "under59", "early_exception_2": "code2_partial", "death_4": "not_beneficiary"}.get(code)
                    if t: out[f"{pre}.{t}"] = v; bump("code_screen->" + t)
                    else: bump("code_screen true dropped (code %s)" % code)
                continue
            if f == "rollover":
                if isinstance(v, (int, float)) and v > 0 and d.get(pre + ".code") != "direct_rollover_G" and pre + ".rollover_any" not in d:
                    out[pre + ".rollover_any"] = True; bump("rollover_any")
                out[k] = v; continue
            if f == "annuity":
                if v is True and pre + ".cost_any" not in d:
                    out[pre + ".cost_any"] = True; bump("cost_any")
                out[k] = v; continue
        if k == "ssb.benefits":
            if isinstance(v, (int, float)) and v > 0 and "ssb.any" not in d:
                out["ssb.any"] = True; bump("ssb.any")
            out[k] = v; continue
        if k == "ssb.pub915":
            bump("pub915")
            if v is not False: out["ssb.repaid_more"] = v; bump("pub915->repaid_more")
            continue
        if k == "ssb.lump_sum":
            bump("lump_sum")
            if v is not False: out["ssb.prior_year_pay"] = True; out["ssb.lump_elect"] = v; bump("lump_sum->lump_elect")
            continue
        out[k] = v
    return out

KEY = re.compile(r"retirement\[[^\]]+\]\.(special|code_screen|rollover|annuity|account)$|^ssb\.(benefits|pub915|lump_sum)$")
def walk(x):
    if isinstance(x, dict):
        if any(isinstance(k, str) and KEY.search(k) for k in x):
            x = fix_inputs(x)
        return {k: walk(v) for k, v in x.items()}
    if isinstance(x, list):
        return [walk(v) for v in x]
    return x

def rewrite_json(f, fn):
    t = open(f).read(); d = json.loads(t)
    for ind in (1, 2, None):
        for asc in (False, True):
            for nl in ("\n", ""):
                if json.dumps(d, indent=ind, ensure_ascii=asc) + nl == t:
                    n = json.dumps(fn(d), indent=ind, ensure_ascii=asc) + nl
                    if n != t: open(f, "w").write(n); print("rewrote", f)
                    return
    sys.exit("no round trip: " + f)

for f in sorted(glob.glob("fixtures/**/*.json", recursive=True)):
    if f.endswith("defaults.json"): continue
    name = f.split("/")[-1]
    FULL = name.startswith("classm") or name == "mutation.json"
    rewrite_json(f, walk)

def defaults(d):
    have = {e["input"] for e in d["defaults"]}
    out = []
    for e in d["defaults"]:
        if e["input"] in ("retirement.special", "retirement.code_screen", "ssb.pub915", "ssb.lump_sum"): continue
        out.append(e)
        new = RET_NEW if e["input"] == "retirement.used_last_year" else SSB_NEW if e["input"] == "ssb.terror_disability" else []
        pre = "retirement." if new is RET_NEW else "ssb."
        for n in new:
            if pre + n not in have:
                out.append({"input": pre + n, "value": False, "reason": "Closed: the circumstance this question asks about does not apply unless the scenario says so."})
    d["defaults"] = out
    return d
rewrite_json("fixtures/2025/defaults.json", defaults)

for p in ("interview/2025/sales.yaml", "interview/2025/stage4.yaml"):
    s = open(p).read()
    if "retirement.rollover_any" in s: continue
    s = s.replace("  - retirement.special\n", "".join(f"  - retirement.{n}\n" for n in RET_NEW if n not in ("under59", "sec457", "code2_partial", "not_beneficiary")))
    s = s.replace("  - retirement.code_screen\n", "".join(f"  - retirement.{n}\n" for n in ("under59", "sec457", "code2_partial", "not_beneficiary")))
    s = s.replace("  - ssb.pub915\n", "  - ssb.any\n  - ssb.ira_covered\n  - ssb.repaid_more\n  - ssb.prior_year_pay\n")
    s = s.replace("  - ssb.lump_sum\n", "  - ssb.lump_elect\n")
    open(p, "w").write(s); print("rewrote", p)
print(json.dumps(counts, indent=1))
