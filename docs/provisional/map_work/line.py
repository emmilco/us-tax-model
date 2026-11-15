# Scratch: print form lines compactly (no label/source/cite); args: line ids. --gate ID prints the gate line of an input too.
import yaml,glob,sys,json
lines={}
for f in sorted(glob.glob('forms/2025/*.yaml')):
    d=yaml.safe_load(open(f)); d=d.get('form') or d.get('definition') or next(iter(d.values()))
    for l in d.get('lines',[]): lines[l['id']]=l
def strip(n):
    if isinstance(n,dict): return {k:strip(v) for k,v in n.items() if k not in('label','source','cite','note','remedy','printed')}
    if isinstance(n,list): return [strip(x) for x in n]
    return n
def comp(n):
    return json.dumps(strip(n),separators=(',',':'))
for a in sys.argv[1:]:
    l=lines.get(a)
    if not l: print(a,'?'); continue
    print(a,'::',comp(l)[:int(1e3)])
    g=l.get('gated_by')
    if g: print('   gate',g,'::',comp(lines[g])[:700])
