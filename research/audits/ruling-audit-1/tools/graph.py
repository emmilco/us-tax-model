import yaml,glob,json,sys,re
lines={}
for f in glob.glob('forms/2025/*.yaml'):
    d=yaml.safe_load(open(f))
    for l in (d.get('form') or d.get('def')).get('lines',[]):
        lines[l['id']]=l
def refs(e,acc):
    if isinstance(e,dict):
        for k,v in e.items():
            if k in('ref','from') and isinstance(v,str) and v in lines: acc.add(v)
            refs(v,acc)
    elif isinstance(e,list):
        for x in e: refs(x,acc)
    elif isinstance(e,str) and e in lines: acc.add(e)
    return acc
deps={i:refs(l.get('expr'),set()) for i,l in lines.items()}
gates={}
for i,l in lines.items():
    for r in l.get('refuses',[]) or []:
        gates.setdefault(r['when'],[]).append(i)
readers={}
for i,ds in deps.items():
    for x in ds: readers.setdefault(x,set()).add(i)
json.dump({'deps':{k:sorted(v) for k,v in deps.items()},'gates':gates,'readers':{k:sorted(v) for k,v in readers.items()}},open('/tmp/claude-0/sp/graph.json','w'))
print(len(lines),len(gates))
