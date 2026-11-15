#!/usr/bin/env python3
"""List answers stated for an id that is not an input of the forms: in fixture inputs, coverage rows and sets, personas,
the profiles' question lists and the bank. Run from the worktree root after a merge. Exit 1 when any is found."""
import glob, json, re, sys, yaml
from collections import defaultdict

inputs, rosters = set(), set()
for f in glob.glob('forms/2025/*.yaml') + glob.glob('forms/ny/2025/*.yaml'):
    d = yaml.safe_load(open(f))
    def walk(x):
        if isinstance(x, dict):
            if 'id' in x and isinstance(x.get('expr'), dict) and x['expr'].get('op') == 'input': inputs.add(x['id'])
            if 'roster' in x and isinstance(x['roster'], str): rosters.add(x['roster'])
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(d)

def stripped(key):
    return key.split('@')[0] if key.startswith('$') else re.sub(r'\[[^\]]*\]', '', key)

bad = defaultdict(lambda: defaultdict(int))
def check(where, key):
    t = stripped(key)
    if t.startswith('$'): return
    parts = t.split('.')
    if any('.'.join(parts[i:]) in inputs for i in range(len(parts) - 1)): return
    bad['.'.join(parts[-2:])][where] += 1

us_only = len(sys.argv) > 1 and sys.argv[1] == '--us'
for f in sorted(glob.glob('fixtures/2025/*.json') + ([] if us_only else glob.glob('fixtures/ny/2025/*.json'))):
    d = json.load(open(f))
    if f.endswith('defaults.json'):
        for k in (d.get('defaults') or d): check(f, k) if isinstance(k, str) and '.' in k else None
        continue
    for c in d.get('cases', []) if isinstance(d, dict) else []:
        for k in (c.get('inputs') or {}): check(f, k)
for f in sorted(glob.glob('interview/2025/coverage/*.yaml')):
    d = yaml.safe_load(open(f))
    for s in (d.get('sets') or {}).values():
        for k in (s.get('answers') or {}): check(f, k)
    for r in d.get('rows') or []:
        for k in (r.get('answers') or {}): check(f, k)
for f in sorted(glob.glob('interview/2025/personas/*.yaml')):
    for k in (yaml.safe_load(open(f)).get('answers') or {}): check(f, k)
for f in ['interview/2025/full.yaml', 'interview/2025/sales.yaml', 'interview/2025/stage4.yaml', 'interview/2025/social-security.yaml']:
    qs = (yaml.safe_load(open(f)).get('interview') or {}).get('questions') or []
    for k in (qs if isinstance(qs, list) else []): check(f, k)
for q in yaml.safe_load(open('interview/2025/questions.yaml'))['bank']['questions']: check('interview/2025/questions.yaml', q['input'])
for t in sorted(bad):
    print(t, dict(bad[t]))
print(f'{len(bad)} id(s) stated that are not inputs ({len(inputs)} inputs read)')
sys.exit(1 if bad else 0)
