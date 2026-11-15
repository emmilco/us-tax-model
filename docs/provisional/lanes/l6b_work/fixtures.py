"""Rewrite fixture inputs for the three inputs taken apart: asset.screen, scveh.screen, scveh.smr_ok.
A stated 'screen: false' becomes every child stated false (records: true); a stated 'smr_ok: true' becomes
smr_always true, smr_first false, fleet false. The three 'screen: true' cases are set by name. Text substitution, so
nothing else in a file changes."""
import re, glob, sys

def ids(path):
    s = {}
    exec(open(path).read(), s)
    return [c['id'].split('.', 1)[1] for c in s['CHILDREN']]

A = ids('docs/provisional/lanes/l6b_work/asset_spec.py')
V = ids('docs/provisional/lanes/l6b_work/scveh_spec.py')
YES = {  # case-specific: which child says the screen's Yes (see lane notes)
    'person[taxpayer].sc[desk].asset[pc].screen': 'method_other',
}
VEH_YES = {'stage14.veh.refuse_screen': 'disposed', 'stage14.veh.refuse_pre_2017': 'before_2017'}

def expand(prefix, kids, yes=None):
    out = []
    for k in kids:
        v = 'true' if (k == 'records') else 'false'
        if yes == k: v = 'true'
        out.append(f'"{prefix}.{k}": {v}')
    return ', '.join(out)

n = 0
for p in sorted(glob.glob('fixtures/2025/*.json') + glob.glob('fixtures/ny/2025/*.json')):
    if p.endswith('defaults.json'): continue
    s = open(p).read()
    def rep(m):
        global n
        prefix, form, val = m.group(1), m.group(2), m.group(3)
        n += 1
        kids = A if form == 'asset' else V
        if val == 'null':
            return ', '.join(f'"{prefix}.{k}": null' for k in kids)
        if val == 'false':
            return expand(prefix, kids)
        key = prefix + '.screen'
        if form == 'asset':
            return expand(prefix, kids, YES[key])
        # vehicle: find the case id before this position
        cid = re.findall(r'"id": "([^"]+)"', s[:m.start()])[-1]
        return expand(prefix, kids, VEH_YES[cid])
    t = re.sub(r'"((?:[^"]*\.)?(asset|scveh)(?:\[[^\]"]*\])?)\.screen": (true|false|null)', rep, s)
    def rep2(m):
        global n
        n += 1
        prefix, val = m.group(1), m.group(2)
        if val == 'true':
            return f'"{prefix}.smr_always": true, "{prefix}.smr_first": false, "{prefix}.fleet": false'
        if val == 'false':
            return f'"{prefix}.smr_always": false, "{prefix}.smr_first": false, "{prefix}.fleet": false'
        return f'"{prefix}.smr_always": null, "{prefix}.smr_first": null, "{prefix}.fleet": null'
    t = re.sub(r'"((?:[^"]*\.)?scveh(?:\[[^\]"]*\])?)\.smr_ok": (true|false|null)', rep2, t)
    if t != s:
        open(p, 'w').write(t)
print('replacements', n)

# defaults: one entry per new input, next to the old one
p = 'fixtures/2025/defaults.json'
s = open(p).read()
def entry(inp, val):
    return ('    {\n      "input": "%s",\n      "value": %s,\n      "reason": "Closed: the circumstance this question asks about does not apply unless the scenario says so."\n    },\n' % (inp, val))
for form, kids in (('asset', A), ('scveh', V)):
    m = re.search(r'    \{\n      "input": "%s\.screen",\n      "value": false,\n      "reason": "[^"]*"\n    \},\n' % form, s)
    assert m, form
    s = s[:m.start()] + ''.join(entry(f'{form}.{k}', 'true' if k == 'records' else 'false') for k in kids) + s[m.end():]
m = re.search(r'    \{\n      "input": "scveh\.smr_ok",\n      "value": false,\n      "reason": "[^"]*"\n    \},\n', s)
assert m
s = s[:m.start()] + ''.join(entry(f'scveh.{k}', 'false') for k in ('smr_always', 'smr_first', 'fleet')) + s[m.end():]
open(p, 'w').write(s)
print('defaults written')
