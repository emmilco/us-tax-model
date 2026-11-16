import json, sys
src = sys.argv[1]
d = json.load(open(src))
skip = lambda e: e['id'] == 'ny_it201.ask.est_any'
texts = {}
applied = skipped = 0
for e in d:
    if skip(e):
        skipped += 1; print('SKIP', e['id'], e['field']); continue
    f = e['file']
    t = texts.setdefault(f, open(f).read())
    n = t.count(e['old_raw'])
    if n != 1:
        sys.exit(f"FAIL {e['id']} {e['field']} count={n}")
    texts[f] = t.replace(e['old_raw'], e['new_raw'])
    applied += 1
for f, t in texts.items():
    open(f, 'w').write(t)
print('applied', applied, 'skipped', skipped, 'files', sorted(texts))
