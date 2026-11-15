#!/usr/bin/env python3
"""Rewrite fixture inputs after a scope screen is taken apart (lane 9 scratch tool).

Usage: refix.py MAP.json [--write]
MAP.json: {"screens": {"<old id>": {"items": [<every item input of the screen>], "default_true": {<item>: true, ...}}},
           "cases": {"<case id>": {"<old id>": {<item>: true, ...}}}}
For each fixture case: an old id given false is dropped (the items default to false); given true it becomes the
case's own item answers (or the screen's default_true); given null, every item of the screen becomes null.
Expected values are not touched, except that an expected "unknown" that names an old id as its missing input is
reported, not rewritten.
"""
import json, glob, sys
m = json.load(open(sys.argv[1])); write = '--write' in sys.argv
files = sorted(glob.glob('fixtures/2025/*.json') + glob.glob('fixtures/ny/2025/*.json'))
for f in files:
    if f.endswith('defaults.json'): continue
    raw = open(f).read(); d = json.loads(raw)
    layout = None
    for ind in (2, 1, 4):
        for asc in (False, True):
            for tail in ("\n", ""):
                if json.dumps(d, indent=ind, ensure_ascii=asc) + tail == raw: layout = (ind, asc, tail)
    exact = layout is not None
    changed = 0
    for c in d['cases']:
        inp = c.get('inputs')
        if not isinstance(inp, dict): continue
        new = {}; later = {}
        for k, v in inp.items():
            if k not in m['screens']:
                new[k] = v
                continue
            changed += 1
            s = m['screens'][k]
            # A case that states a screen (class M and mutation cases state every input; the defaults do not fill
            # them) states every item: No for a screen answered No, with the plain parents No; unanswered for a
            # screen left unanswered; the case's own items Yes for a screen answered Yes, the rest No.
            for it in m['parents']: new.setdefault(it, False)
            for it in s['items']: new[it] = None if v is None else False
            if v is True:
                later.update(m.get('cases', {}).get(c['id'], {}).get(k, s['default_true']))
        new.update(later)
        for k, v in m.get('set_inputs', {}).get(c['id'], {}).items():
            # A case that states every input it needs now needs this one too: the other-income screen reads it.
            if k not in new: new[k] = v; changed += 1; print('  input added in', c['id'], k)
        ren = m.get('rename_unknown', {}).get(c['id'])
        if ren:
            e = json.dumps(c['expect'], ensure_ascii=False)
            for a, b in ren.items(): e = e.replace(a, b)
            c['expect'] = json.loads(e); print('  expected unknown renamed in', c['id'], ren)
        if c['id'] in m.get('drop_nulls', []):
            # A refusal case written "as the interview asks it" left unanswered (null) what the old order never reached.
            # The refusing question is now asked in its topic, later in the order, so those are answered by default.
            dropped = [k for k, v in new.items() if v is None]
            for k in dropped: del new[k]
            if dropped: changed += 1; print('  nulls dropped in', c['id'], dropped)
        c['inputs'] = new
        cov = c.get('covers')
        if isinstance(cov, list):
            c['covers'] = [x for x in cov]
        e = json.dumps(c.get('expect', {}))
        for k in m['screens']:
            if '"input": "%s"' % k in e: print('EXPECTED UNKNOWN names', k, 'in', f, c['id'])
    if changed:
        if not exact: sys.exit('cannot reproduce the JSON layout of ' + f)
        print(f, changed, 'inputs rewritten')
        if write: open(f, 'w').write(json.dumps(d, indent=layout[0], ensure_ascii=layout[1]) + layout[2])
