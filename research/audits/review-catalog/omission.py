"""Omission check (validation only, never feeds selection): every foreign line id, collection
and collection field the project's own encoding of a form references -- through every line of
the form, its helpers included, operands, refusal gates and shown_when -- must be supplied in
the new prompt with its exact interface note. Also runs input_context.assess(form, [], ...)."""
import os, sys, json, collections
R, PROMPTS = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(R, 'tools/transcription'))
import transcribe as T
import input_context as I

ids = sorted(f[:-5] for f in os.listdir(T.FORMS) if f.endswith('.yaml'))
docs = {i: T.load_form(i) for i in ids}
owner = {l['id']: i for i in ids for l in docs[i]['lines']}
ctx = T.model_type_context()


def colls(e, out):
    if isinstance(e, dict):
        if e.get('op') == 'sum_over':
            out.add(e['collection'])
        for v in e.values():
            colls(v, out)
    elif isinstance(e, list):
        for v in e:
            colls(v, out)
    return out


report = {}
total = 0
for i in ids:
    path = os.path.join(PROMPTS, i + '.preview.prompt.txt')
    if not os.path.exists(path):
        continue
    prompt = open(path, encoding='utf-8').read()
    flat = ' '.join(prompt.split())
    d = docs[i]; own = {l['id'] for l in d['lines']}
    refs, cs = set(), set()
    for l in d['lines']:
        refs |= T.operand_refs(l['expr'])
        colls(l['expr'], cs)
        for r in l.get('refuses') or []:
            refs.add(r if isinstance(r, str) else r['when'])
        if l.get('shown_when'):
            refs.add(l['shown_when'])
    miss = []
    for r in sorted(refs - own):
        if r not in owner:
            continue  # definition-internal or bound names
        g = docs[owner[r]]
        line = next(l for l in g['lines'] if l['id'] == r)
        if ' '.join(T.reference_note(g, line).split()) not in flat:
            miss.append(f"{g['id']}:{r}")
    for c in sorted(cs - {i}):
        if f"collection `{c}`" not in prompt:
            miss.append(f"{c}:(collection)")
    a = I.assess(d, [], ctx, prompt)
    report[i] = {'misses': miss, 'assess_missing': a['missing'], 'refs': len(refs - own), 'collections': sorted(cs - {i})}
    total += len(miss)
    if miss or a['missing']:
        print(i, 'MISS', miss, 'assess', a['missing'])
print('forms checked', len(report), 'total misses', total)
json.dump(report, open(sys.argv[3], 'w'), indent=1)
