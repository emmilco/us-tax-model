import json, sys, re
strip = lambda s: re.sub(r"\[[^\]]*\]", "[]", s)
for l in open(sys.argv[1]):
    r = json.loads(l)
    print(f"== {r['template']} [{r['cls']}] seed {r['seed']} i {r['i']} key {strip(r.get('key') or '-')} found {r['found']} hiddenBy {strip(r.get('hiddenBy') or '-')} next {strip(r.get('next') or '-')} {r.get('error') or ''}")
    for f in r.get("frontier", []):
        print(f"     {strip(f['line'])} [{f['op']}] = {strip(f['value'])[:70]} | also waiting on {[strip(x) for x in f['alsoWaiting']]} | {[strip(o) for o in f['operands'][:14]]}"[:900])
    if r.get("probe"): print("     probe:", [(p["v"], p["status"], strip(p["gate"] or ""), "same" if p["sameValues"] else "VALUES DIFFER") for p in r["probe"]], "others reachable:", [strip(o) for o in r.get("others", [])])
