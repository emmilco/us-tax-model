"""Restate fixture answers to an age input that became a line derived from person.birth_year.

usage: age.py age55|under24|simple [--override FILE]
  FILE: json {case id: {person: candidate}}, a candidate as {"y": year, "j": .., "a": .., "a55": .., "u": .., "d": .., "s": ..}
Run from the worktree root. Writes the fixtures in place and v3_age_work/<phase>_report.json.
For each person whose old answer a case states, the year kept is the case's own (stated, or the default 1980) when it
gives the stated answer; otherwise the candidate that gives it and changes the fewest of the person's other derived age
facts, the nearest year to the old one on a tie. The fixtures are then run and a failing case is searched (search.mjs).
"""
import sys, json, glob, os, re

PHASE = sys.argv[1]
over = {}
if '--override' in sys.argv:
    over = json.load(open(sys.argv[sys.argv.index('--override') + 1]))
WORK = 'docs/provisional/lanes/v3_age_work'
CUTS = (1961, 2001, 2002, 2007, 2008)
DEFAULT_YEAR = 1980


def facts(c, phase):
    """The derived age facts of one candidate birth: the nine of person.yaml, and those this lane derives."""
    y, j = c['y'], c.get('j', False)
    cut = lambda Y: y < Y or (y == Y and j)
    v = {'age65': cut(1961), 'born_after_1960': y >= 1961, 'born_before_2001': cut(2001), 'edu_born_2002': cut(2002),
         'edu_born_2007': cut(2007), 'sav_born': cut(2008), 'under16': y >= 2011 or (y == 2010 and bool(c.get('u', True))),
         'ira_age50': y <= 1975 or (y == 1976 and bool(c.get('a'))),
         'died_before_65': bool(c.get('d')) and (y == 1960 or (y == 1961 and j)),
         'age55': y <= 1970 or (y == 1971 and bool(c.get('a55')))}
    if phase in ('under24', 'simple'):
        v['under24'] = y >= 2003 or (y == 2002 and not j)
    if phase == 'simple':
        v['simple_age'] = simple_band(c)
    return v


def simple_band(c):
    y = c['y']
    if y <= 1961: return 'age50'
    if y == 1962: return c.get('s', 'age60_63')
    if y <= 1965: return 'age60_63'
    if y == 1966: return c.get('s', 'age50')
    if y <= 1975: return 'age50'
    if y == 1976: return 'age50' if c.get('a') else 'under50'
    return 'under50'


def candidates():
    out = []
    for y in range(1930, 2016):
        base = [{'y': y}]
        if y in CUTS: base = [{'y': y, 'j': False}, {'y': y, 'j': True}]
        if y == 1976: base = [{'y': y, 'a': False}, {'y': y, 'a': True}]
        if y == 1971: base = [{'y': y, 'a55': False}, {'y': y, 'a55': True}]
        if y == 2010: base = [{'y': y, 'u': True}, {'y': y, 'u': False}]
        if y in (1962, 1966): base = [{'y': y, 's': 'age50'}, {'y': y, 's': 'age60_63'}]
        for b in base:
            if y == 1960 or (y == 1961 and b.get('j')):
                out += [dict(b, d=False), dict(b, d=True)]
            else:
                out.append(b)
    return out


CANDS = candidates()
NARROW = {'born_jan1': 'j', 'under16_at_year_end': 'u', 'age50_at_year_end': 'a', 'age55_at_year_end': 'a55', 'died_at_64': 'd',
          'simple_age_at_year_end': 's'}


def needs(c):
    """The narrow answers a candidate's year asks."""
    y = c['y']; o = {}
    if y in CUTS: o['born_jan1'] = c.get('j', False)
    if y == 2010: o['under16_at_year_end'] = c.get('u', True)
    if y == 1976: o['age50_at_year_end'] = c.get('a', False)
    if y == 1971: o['age55_at_year_end'] = c.get('a55', False)
    if y == 1960 or (y == 1961 and c.get('j')): o['died_at_64'] = c.get('d', False)
    if PHASE == 'simple' and y in (1962, 1966): o['simple_age_at_year_end'] = c.get('s')
    return o


def current(inp, p, takes_defaults):
    k = f'person[{p}].birth_year'
    if k in inp:
        y = inp[k]
        if y is None: return None
    elif takes_defaults:
        y = DEFAULT_YEAR
    else:
        return 'unstated'
    c = {'y': y}
    for n, s in NARROW.items():
        kk = f'person[{p}].{n}'
        if kk in inp and inp[kk] is not None: c[s] = inp[kk]
    return c


def fmt(t):
    d = json.loads(t)
    for kw in (dict(indent=2), dict(separators=(',', ':')), dict(indent=1)):
        for ea in (False, True):
            for nl in ('', '\n'):
                if json.dumps(d, ensure_ascii=ea, **kw) + nl == t: return lambda x: json.dumps(x, ensure_ascii=ea, **kw) + nl
    raise SystemExit('format')


def old_keys(inp, p):
    """The keys of the old input for person p and the required value of the derived fact."""
    if PHASE == 'age55':
        ks = [k for k in inp if re.match(rf'person\[{re.escape(p)}\]\.f8889\[[^\]]+\]\.age55$', k)]
        return ks, 'age55'
    if PHASE == 'under24':
        return (['scope.under24'] if 'scope.under24' in inp else []), 'under24'
    if PHASE == 'simple':
        k = f'person[{p}].simple_age'
        return ([k] if k in inp else []), 'simple_age'


def persons(inp):
    ps = set()
    for k in inp:
        m = re.match(r'person\[([^\]]+)\]\.', k)
        if m: ps.add(m.group(1))
    if PHASE == 'under24' and 'scope.under24' in inp: ps.add(taxpayer_of(inp))
    return sorted(ps)


def taxpayer_of(inp):
    r = inp.get('$person')
    return r[0] if isinstance(r, list) and r else 'taxpayer'


def text_edit(t, cid, before, after):
    """Within the text of case cid, remove the keys after drops, change values it changes, and put new keys where the
    first dropped key was (each key on its own line in the files this is used on)."""
    i = t.index(f'"id": "{cid}"'); j = t.find('"id": "', i + 1); j = len(t) if j < 0 else j
    seg = t[i:j]
    lines = seg.split('\n'); out = []; placed = False
    new_keys = [k for k in after if k not in before]
    for ln in lines:
        m = re.match(r'(\s*)"([^"]+)": (.*?)(,?)$', ln)
        if m and m.group(2) in before:
            k = m.group(2)
            if k not in after:
                if not placed and new_keys:
                    out += [f'{m.group(1)}{json.dumps(nk)}: {json.dumps(after[nk])},' for nk in new_keys]; placed = True
                continue
            if after[k] != before[k]:
                ln = f'{m.group(1)}{json.dumps(k)}: {json.dumps(after[k])}{m.group(4)}'
        out.append(ln)
    assert placed or not new_keys, cid
    seg = '\n'.join(out)
    seg = re.sub(r',(\s*\n\s*})', r'\1', seg)
    return t[:i] + seg + t[j:]


report = {'kept': [], 'moved': [], 'null': [], 'conflict': [], 'unstated': []}
files = sorted(glob.glob('fixtures/2025/*.json') + glob.glob('fixtures/ny/2025/*.json'))
for f in files:
    b = os.path.basename(f)
    if b == 'defaults.json': continue
    t = open(f).read()
    if 'age55' not in t and 'under24' not in t and 'simple_age' not in t: continue
    d = json.loads(t)
    try:
        dump = fmt(t)
    except SystemExit:
        dump = None  # hand-formatted: edited as text, case by case (text_edit)
    edits = []
    takes = not (b.startswith('classm') or b == 'mutation.json')
    changed = False
    for c in d.get('cases', []):
        inp = c['inputs']
        for p in persons(inp):
            if PHASE == 'under24' and p != taxpayer_of(inp): continue
            ks, fact = old_keys(inp, p)
            if not ks: continue
            vals = {json.dumps(inp[k]) for k in ks}
            if len(vals) > 1:
                report['conflict'].append([f, c['id'], p, {k: inp[k] for k in ks}]); continue
            want = inp[ks[0]]
            cur = current(inp, p, takes)
            rec = [f, c['id'], p, want, cur]
            if want is None:
                # A withheld answer withholds the year, as the earlier lane did for age65.
                if cur is None or f'person[{p}].birth_year' not in inp:
                    new = None
                else:
                    report['conflict'].append(rec + ['withheld answer with a stated year']); continue
                report['null'].append(rec)
            elif c['id'] in over and p in over[c['id']]:
                new = over[c['id']][p]; report['moved'].append(rec + [new, 'override'])
            elif cur == 'unstated' or cur is None:
                report['unstated'].append(rec); new = None if cur is None else 'unstated'
                if new == 'unstated':
                    sat = [x for x in CANDS if facts(x, PHASE)[fact] == want]
                    new = min(sat, key=lambda x: (bool(needs(x)), abs(x['y'] - DEFAULT_YEAR)))
            else:
                if facts(cur, PHASE)[fact] == want and not (PHASE == 'simple' and cur['y'] in (1962, 1966) and 's' not in cur):
                    new = dict(cur); report['kept'].append(rec)
                else:
                    if PHASE == 'simple' and cur['y'] in (1962, 1966) and facts(dict(cur, s=want), PHASE)[fact] == want:
                        new = dict(cur, s=want); report['kept'].append(rec)
                    else:
                        base = facts(cur, PHASE)
                        sat = [x for x in CANDS if facts(x, PHASE)[fact] == want]
                        def score(x):
                            v = facts(x, PHASE)
                            return (sum(v[k] != base[k] for k in v if k != fact), bool(needs(x)), abs(x['y'] - cur['y']), CANDS.index(x))
                        new = min(sat, key=score)
                        report['moved'].append(rec + [new, sorted(k for k, v in facts(new, PHASE).items() if k != fact and v != base[k])])
            # write: drop the old keys and the person's narrow answers, put the year (and the narrow answers it needs)
            out = {}; done = False
            narrow_keys = {f'person[{p}].{n}' for n in NARROW} | {f'person[{p}].birth_year'}
            if new is None:
                put = {f'person[{p}].birth_year': None}
            elif takes and f'person[{p}].birth_year' not in inp and new['y'] == DEFAULT_YEAR and not needs(new):
                put = {}  # the default year already gives the answer
            else:
                put = {f'person[{p}].birth_year': new['y']}
                put.update({f'person[{p}].{n}': v for n, v in needs(new).items()})
            # a year the case states, stated where it was; otherwise where the old answer was
            had_year = f'person[{p}].birth_year' in inp
            for k, v in inp.items():
                if k in ks:
                    if not had_year and not done: out.update(put); done = True
                    continue
                if k in narrow_keys:
                    if had_year and not done: out.update(put); done = True
                    continue
                out[k] = v
            if not done: out.update(put)
            if dump is None: edits.append((c['id'], inp, out))
            # a defaults file needs no year equal to the default with nothing else
            c['inputs'] = inp = out; changed = True
    if changed and dump is not None: open(f, 'w').write(dump(d))
    if changed and dump is None:
        for cid, before, after in edits: t = text_edit(t, cid, before, after)
        assert json.loads(t) == d, f
        open(f, 'w').write(t)
json.dump(report, open(f'{WORK}/{PHASE}_report.json', 'w'), indent=1)
print({k: len(v) for k, v in report.items()})
for r in report['moved']: print('moved', r)
for k in ('null', 'conflict', 'unstated'):
    for r in report[k]: print(k, r)
