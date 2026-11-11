# usage: python3 -I gen_rank.py > out/catalog_rank.md
import json, glob, re, collections, sys, runpy, io, contextlib
sys.path.insert(0, "/tmp/f1095a/scripts")
from fam_meta import FAMS
O = "/tmp/f1095a/out"
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path("/tmp/f1095a/scripts/gen_tables.py")
by, inst, cause_lines, fam_of, comp, T = g["by"], g["inst"], g["cause_lines"], g["fam_of"], g["comp"], g["T"]
fs = json.load(open(f"{O}/famsummary.json"))
ORDER = ["D1", "P2", "D2", "P1", "D4", "D3", "A1", "H1", "D6", "X4", "X5", "V1", "S1", "R1", "E1", "D5", "X3", "X2", "C1", "X1", "X6"]
KEY = {m["id"]: m["key"] for m in FAMS}
ret = collections.defaultdict(set); unq = collections.Counter(); classes = collections.defaultdict(set)
for t, cs in by.items():
    rep = "f1095a.in_a_apr" if t.startswith("f1095a.in_a_") else "f1095a.in_b_apr" if t.startswith("f1095a.in_b_") else t
    for cls in ("early", "out", "unread"):
        if not cs.get(cls): continue
        fams = fam_of(cause_lines(rep, cls)) or ["?"]
        keys = {"early": [f"randomEarly:{rep}", f"early:{rep}"], "out": [f"out:{rep}", f"reached:{rep}"], "unread": [f"unread:{rep}"]}[cls]
        tested = [fid for fid in ORDER if (fs.get(KEY[fid]) or {}).get("witness") and any(k in fs[KEY[fid]]["witness"]["gone"] for k in keys)]
        f = (tested or fams)[0]
        ret[f] |= cs[cls]; classes[f].add(cls)
        if cls == "unread": unq[f] += inst[t]
ORDER = ["D1", "P2", "D2", "P1", "D4", "D3", "A1", "H1", "D6", "X4", "X5", "V1", "S1", "R1", "E1", "D5", "X3", "X2", "C1", "X1", "X6"]
WHY = {"D1": "Removes the only findings where an unanswered question can refuse a return the interview calls complete, and the most unread questions.", "P2": "Two questions on nearly every return with a Form 1095-A; closes BUG-0487 and empties the baseline.",
 "D2": "Second most unread questions; same form and review round as D1.", "P1": "Up to 24 amounts per Form 1095-A, but only for filers who are not applicable taxpayers.", "D4": "One hard question (lawful relationship) for member-of-household dependents.",
 "D3": "No question saved in bank order; its gate is one D1 stops leaving open (3 of 85 states refuse there on main).", "A1": "One question per business asset for filers who elect no section 179.", "H1": "Out of order only, and `household.married` left open at completion (benign there).",
 "D6": "One unread question on 1 return of 5,000; the dependent line is out of order only.", "X4": "`person.blind` asked of filers who then elect to itemize.", "X5": "One birth-date question; the early-completion findings on these inputs stay (L1).",
 "V1": "Out of order only; no question saved.", "S1": "Out of order only; no question saved.", "R1": "Out of order only; seven lines for no question saved.", "E1": "Out of order only bar one unread question on 1 return; ten lines.",
 "D5": "Six unread questions in 5,000 returns; changes one asserted fixture to unknown and adds questions on refused returns.", "X3": "Out of order only.", "X2": "Out of order only bar one unread question on 1 return.", "C1": "Out of order only.", "X1": "Out of order only.", "X6": "Out of order only; seen on no generated return."}
meta = {m["id"]: m for m in FAMS}
CL = {"early": "left reachable at completion", "out": "out of order", "unread": "asked and unread"}
print("| Rank | Family | Classes seen | Complete returns showing it (of %d) | Unread questions (5,000 returns) | Who meets it (share of all returns, `gate_frequencies.yaml`) | Lines rewritten + helpers | Fixtures changed | Pins un-pinned (of 52) | Forms to re-review | Why here |" % len(comp))
print("|---|---|---|---|---|---|---|---|---|---|---|")
for n, fid in enumerate(ORDER, 1):
    m = meta[fid]; r = fs.get(m["key"]) or {}
    share = f"{m['share'][0]}: {m['share'][1]:.1%}" if m["share"][1] is not None else m["share"][0]
    fx = "-"
    if r.get("fixtures_fed"):
        a, b = r["fixtures_fed"].split("/"); c, d = (r.get("fixtures_ny") or "0/0").split("/")
        fx = str((int(b) - int(a)) + (int(d) - int(c)))
    forms = ", ".join(sorted({f.split("/")[-1][:-5] for f in r.get("files", [])})) or "-"
    print(f"| {n} | **{fid}** {m['title']} | {', '.join(CL[c] for c in ('early', 'out', 'unread') if c in classes[fid]) or 'none in the sweep'} | {len(ret[fid])} | {unq[fid]} | {share} | {len(r.get('rewritten', []))} + {r.get('helpers_added', '?')} | {fx} | {(r.get('pins') or {}).get('moved', '?')} | {forms} | {WHY[fid]} |")
print()
print("Unattributed in the sweep (class L1, no rewrite proposed): %d returns." % len(ret.get("L1", set())))
if ret.get("?"): print("No cause line matched: %d returns." % len(ret["?"]))
