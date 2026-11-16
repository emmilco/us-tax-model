"""Apply trimA.json: 'old' is the parsed YAML value. Locate the field in the entry's block, replace the scalar,
re-emit in the file's style (PyYAML plain/quoted, wrapped near column 120, continuation indent +2)."""
import json, re, sys, copy, yaml

T6 = ("Is it a service business (health, law, engineering, architecture, accounting, actuarial science, performing arts "
      "or consulting) in which you (or your spouse, whether or not you file jointly) materially participated in any 3 "
      "earlier years?")
SKIP = {'person.edu_over', 'dependent.edu_over'}
WIDTH = 120

def block(lines, ident):
    pat = re.compile(r'^(\s*)- (id|input): ' + re.escape(ident) + r'\s*$')
    hits = [i for i, l in enumerate(lines) if pat.match(l)]
    if len(hits) != 1:
        sys.exit(f'FAIL block {ident}: {len(hits)} hits')
    s = hits[0]; ind = len(pat.match(lines[s]).group(1))
    e = s + 1
    while e < len(lines) and not (re.match(r'^\s*- ', lines[e]) and len(lines[e]) - len(lines[e].lstrip()) <= ind) \
            and not (lines[e].strip() and len(lines[e]) - len(lines[e].lstrip()) < ind):
        e += 1
    return s, e

def regions(lines, s, e, field):
    kp = re.compile(r'^(\s*)(- )?' + re.escape(field) + r':( |$)')
    for i in range(s, e):
        m = kp.match(lines[i])
        if not m: continue
        kind = len(m.group(1)) + (2 if m.group(2) else 0)
        j = i + 1
        while j < e and lines[j].strip() and len(lines[j]) - len(lines[j].lstrip()) > kind:
            j += 1
        first = ' ' * kind + lines[i][kind:] if not m.group(2) else ' ' * kind + lines[i][len(m.group(1)) + 2:]
        text = '\n'.join([first[kind:]] + [l[kind:] for l in lines[i + 1:j]])
        yield i, j, kind, m.group(2), text

def emit(field, value, kind, dash, lead):
    out = yaml.dump({field: value}, width=WIDTH - kind, allow_unicode=True, sort_keys=False).rstrip('\n').split('\n')
    res = [lead + ('- ' if dash else '') + out[0]] + [' ' * kind + l for l in out[1:]]
    return res

def main(src):
    d = json.load(open(src))
    files = {}
    applied = []
    for e in d:
        if e['id'] in SKIP:
            print('SKIP', e['id'], e['field']); continue
        new = T6 if e['id'] == 'k1p.t6' else e['new']
        f = e['file']
        lines = files.setdefault(f, open(f).read().split('\n'))
        s, en = block(lines, e['id'])
        match = []
        for i, j, kind, dash, text in regions(lines, s, en, e['field']):
            val = yaml.safe_load(text)[e['field']]
            if val == e['old']:
                match.append((i, j, kind, dash))
        if len(match) != 1:
            sys.exit(f"FAIL {e['id']} {e['field']}: {len(match)} matching regions")
        i, j, kind, dash = match[0]
        lead = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
        lines[i:j] = emit(e['field'], new, kind, dash, lead)
        applied.append((f, e['id'], e['field'], e['old'], new))
        print('OK', e['id'], e['field'], len(new.split()), 'words')
    # verify: parsed docs differ only in the applied fields
    for f, lines in files.items():
        before = yaml.safe_load(open(f))
        after = yaml.safe_load('\n'.join(lines))
        exp = copy.deepcopy(before)
        def walk(o, fn):
            if isinstance(o, dict):
                fn(o)
                for v in o.values(): walk(v, fn)
            elif isinstance(o, list):
                for v in o: walk(v, fn)
        for (ff, ident, field, old, new) in applied:
            if ff != f: continue
            hits = []
            def fix(o, ident=ident, field=field, old=old, new=new):
                if o.get('id') == ident or o.get('input') == ident: hits.append(o)
            walk(exp, fix)
            assert len(hits) == 1, (ident, len(hits))
            n = []
            def rep(o):
                if o.get(field) == old: o[field] = new; n.append(1)
            walk(hits[0], rep)
            assert len(n) == 1, (ident, field, len(n))
        assert exp == after, f'parsed diff mismatch in {f}'
        open(f, 'w').write('\n'.join(lines))
        print('verified', f)
    print('applied', len(applied))

main(sys.argv[1])
