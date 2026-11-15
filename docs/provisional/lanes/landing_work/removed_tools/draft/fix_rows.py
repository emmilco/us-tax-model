#!/usr/bin/env python3
"""Apply the mechanical part of what `interview-coverage` reports to the row files, and print every change for review.
usage: node engine/dist/main.js interview-coverage --rows FILE > out.txt; python3 tools/draft/fix_rows.py out.txt [--values k=v ...]
For each failing row it does one of three things, none of which touches the row's `expect`:
  - "the walk asks K, which the row does not answer": adds K with the closed answer (no, zero, none), or the value given
    for K's template with --values (an amount or a choice the situation's filer would give). A choice with no value given
    is printed and left.
  - "the refusal at G came on a background answer (K = V)": adds K: V to the row (the filer's own answer to K).
  - "the row's answer to K is never asked before the walk ends": removes K from the row.
Anything else is printed under MANUAL. The answers added are what a filer with nothing else to report gives; read the
printed list and correct any the situation's filer would answer otherwise."""
import glob, re, sys, yaml

types = {}
for f in glob.glob('forms/2025/*.yaml') + glob.glob('forms/ny/2025/*.yaml'):
    def walk(x):
        if isinstance(x, dict):
            if 'id' in x and isinstance(x.get('expr'), dict) and x['expr'].get('op') == 'input': types[x['id']] = (x.get('type'), x.get('values'))
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(yaml.safe_load(open(f)))

def template(key):
    if key.startswith('$'): return key.split('@')[0]
    parts = re.sub(r'\[[^\]]*\]', '', key).split('.')
    for i in range(len(parts) - 1):
        if '.'.join(parts[i:]) in types: return '.'.join(parts[i:])
    return None

given = {}
args = sys.argv[2:]
if args and args[0] == '--values':
    for a in args[1:]:
        k, v = a.split('=', 1); given[k] = v

def closed(key):
    t = template(key)
    if t in given: return given[t]
    if key.startswith('$'): return '[]'
    if t is None: return None
    ty, vals = types[t]
    if ty == 'Bool': return 'false'
    if ty == 'Enum' or vals: return None
    return '1980' if t == 'person.birth_year' else '0'

def block(lines, row):
    start = next((i for i, l in enumerate(lines) if re.match(r'^\s*- id: ' + re.escape(row) + r'\s*$', l)), None)
    if start is None: return None
    end = next((i for i in range(start + 1, len(lines)) if re.match(r'^\s*- id: ', lines[i])), len(lines))
    while end > start and not lines[end - 1].strip(): end -= 1
    return start, end

def keyof(line):
    m = re.match(r'^\s*(?:"([^"]+)"|\'([^\']+)\'|([^:\s][^:]*)):', line)
    return (m.group(1) or m.group(2) or m.group(3)).strip() if m else None

def answers_span(lines, start, end):
    a = next((i for i in range(start, end) if re.match(r'^\s*answers:\s*$', lines[i])), None)
    if a is None: return None
    ind = len(lines[a]) - len(lines[a].lstrip())
    b = a + 1
    while b < end and lines[b].strip() and len(lines[b]) - len(lines[b].lstrip()) > ind: b += 1
    return a, b, ind

done, manual = [], []
files = {}
for msg in open(sys.argv[1]):
    m = re.match(r'^\s*(interview/\S+\.yaml): row (\S+): (.*)$', msg.rstrip('\n'))
    if not m: continue
    path, row, text = m.groups()
    lines = files.setdefault(path, open(path).read().split('\n'))
    blk = block(lines, row)
    if blk is None: manual.append((row, 'row not found: ' + text[:120])); continue
    start, end = blk
    span = answers_span(lines, start, end)
    ask = re.match(r'the walk asks (\S+) \(after \d+ answers?\), which the row does not answer', text)
    bg = re.match(r'the refusal at \S+ came on a background answer \(question \d+, (\S+) = (.+?) \(a background answer\)\)', text)
    stale = re.match(r"the row's answer to (\S+) is never asked before the walk ends", text)
    if ask or bg:
        key = (ask or bg).group(1)
        val = closed(key) if ask else bg.group(2)
        if ask and template(key) in given: val = given[template(key)]
        if val is None: manual.append((row, f'needs a value: {key} (type {types.get(template(key))}); opened: {text[text.find("It was opened"):][:160]}')); continue
        if span is None:
            e = next(i for i in range(start, end) if re.match(r'^\s*expect:\s*$', lines[i]))
            ind = len(lines[e]) - len(lines[e].lstrip())
            lines.insert(e, ' ' * ind + 'answers:'); span = (e, e + 1, ind)
        a, b, ind = span
        if any(keyof(lines[i]) == key for i in range(a + 1, b)): manual.append((row, f'already answers {key}: {text[:140]}')); continue
        k = f'"{key}"' if any(lines[i].lstrip().startswith('"') for i in range(a + 1, b)) else key
        lines.insert(b, ' ' * (ind + 2) + f'{k}: {val}')
        done.append((row, 'add', key, val, 'row answer opened it' if ask and 'the row is incomplete' in text else 'background' if bg else 'not led to by the row'))
    elif stale:
        key = stale.group(1)
        if span is None: manual.append((row, f'stale {key} but the row has no answers (a set?)')); continue
        a, b, ind = span
        hit = [i for i in range(a + 1, b) if keyof(lines[i]) == key]
        if not hit: manual.append((row, f'stale {key} is not among the row\'s own answers (a set?)')); continue
        val = lines[hit[0]].split(':', 1)[1].strip()
        del lines[hit[0]]
        done.append((row, 'remove', key, val, re.search(r'\((it .*?)\):', text).group(1)[:90] if re.search(r'\((it .*?)\):', text) else ''))
    else:
        manual.append((row, text[:300]))
for path, lines in files.items(): open(path, 'w').write('\n'.join(lines))
for d in done: print('  '.join(str(x) for x in d))
print(f'{len(done)} change(s) in {len(files)} file(s)')
for r, t in manual: print('MANUAL', r, '|', t)
