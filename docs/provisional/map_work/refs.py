# Scratch: index of the form YAML. For each input: the lines that read it, and the refusals it leads to (directly as a
# `when`, or through a derived line whose expression reads it). Writes refs.json.
import yaml,glob,json,collections,sys
forms={}
lines={}
for f in sorted(glob.glob('forms/2025/*.yaml')):
    d=yaml.safe_load(open(f)); d=d.get('form') or d.get('definition') or next(iter(d.values()))
    for l in d.get('lines',[]):
        lines[l['id']]=(d['id'],l)
ids=set(lines)
def refs(node,acc):
    if isinstance(node,dict):
        for k,v in node.items():
            if k in('label','source','cite','note','remedy','form'): continue
            refs(v,acc)
    elif isinstance(node,list):
        for v in node: refs(v,acc)
    elif isinstance(node,str):
        if node in ids: acc.add(node)
out={}
readers=collections.defaultdict(set)
refuse_when=collections.defaultdict(list)
for i,(f,l) in lines.items():
    a=set(); refs({k:v for k,v in l.items() if k not in('refuses','id')},a)
    for r in a: readers[r].add(i)
    for r in l.get('refuses',[]) or []:
        w=r.get('when'); 
        ws=set(); refs(w,ws)
        for x in ws:
            refuse_when[x].append((i,r.get('form','')))
            readers[x].add(i+'!')
def is_input(l): 
    e=l.get('expr'); return isinstance(e,dict) and e.get('op')=='input'
res={}
for i,(f,l) in lines.items():
    if not is_input(l): continue
    direct=refuse_when.get(i,[])
    via=[]
    for r in readers.get(i,()):
        r2=r.rstrip('!')
        if r2 in refuse_when and r2!=i:
            via+= [(r2,)+x for x in refuse_when[r2]]
    res[i]={'type':l.get('type'),'readers':sorted(readers.get(i,())),'refuses_direct':direct,'refuses_via':via}
json.dump(res,open('docs/provisional/map_work/refs.json','w'),indent=0)
print(len(res),'inputs')
for q in sys.argv[1:]:
    r=res[q]; print(q, r['type']); print('  readers:',r['readers']); print('  direct:',r['refuses_direct']); print('  via:',r['refuses_via'])
