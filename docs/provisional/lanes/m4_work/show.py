# Lane m4 scratch: compact view of form lines and their readers. usage: show.py LINE_ID [...] | show.py --form f5695
import sys, yaml, glob, json, re
ROOT = __file__.rsplit('/docs/', 1)[0]
lines = {}
for f in glob.glob(ROOT + '/forms/2025/*.yaml') + glob.glob(ROOT + '/forms/ny/2025/*.yaml'):
    d = yaml.safe_load(open(f))
    for top in d.values():
        if isinstance(top, dict):
            for l in top.get('lines', []) or []:
                lines[l['id']] = l
            for dd in (top.get('defs') or []):
                for l in dd.get('lines', []) or []: lines[l['id']] = l
def ex(e):
    if isinstance(e, str): return e
    if not isinstance(e, dict): return json.dumps(e)
    op = e.get('op')
    if op == 'choose':
        return 'choose{' + '; '.join(ex(a.get('guard')) + ' => ' + ex(a.get('then')) for a in e['alternatives']) + '}'
    if op == 'test':
        k = [k for k in e if k != 'op'][0]
        v = e[k]
        if k in ('all', 'any'): return k + '(' + ', '.join(ex(x) for x in v) + ')'
        if k == 'not': return 'not(' + ex(v) + ')'
        return f'{ex(v[0])} {k} {ex(v[1])}'
    if op == 'const' or set(e) == {'const'}: return json.dumps(e.get('const'))
    if op == 'input': return 'INPUT'
    if op == 'param': return 'param:' + e['ref']
    rest = {k: v for k, v in e.items() if k != 'op'}
    return f'{op}(' + ', '.join(f'{k}=' + (ex(v) if isinstance(v, dict) else ('[' + ', '.join(ex(x) for x in v) + ']' if isinstance(v, list) else str(v))) for k, v in rest.items()) + ')'
def readers(i):
    pat = re.compile(r'\b' + re.escape(i) + r'\b')
    return [k for k, l in lines.items() if k != i and (pat.search(json.dumps(l.get('expr'))) or pat.search(json.dumps(l.get('refuses', []))) or pat.search(json.dumps(l.get('gated_by', ''))) or pat.search(json.dumps(l.get('display', ''))))]
def show(i):
    l = lines[i]
    print(f"{i} [{l.get('type')}] printed={l.get('printed')} gated_by={l.get('gated_by','')}")
    print('   = ' + ex(l['expr']))
    for r in l.get('refuses', []) or []: print('   refuses:', json.dumps({k: v for k, v in r.items() if k in ('when', 'when_known')}))
    for k in ('display', 'show_if', 'when'):
        if k in l: print(f'   {k}:', json.dumps(l[k]))
    if '-r' in sys.argv: print('   readers:', ', '.join(readers(i)))
args = [a for a in sys.argv[1:] if not a.startswith('-')]
if '--form' in sys.argv:
    for k in lines:
        if k.split('.')[0] == args[0]: show(k)
else:
    for a in args: show(a)
