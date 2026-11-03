import yaml,glob,json,re
lines={}
def walk(ls):
    for l in ls:
        if 'lines' in l: walk(l['lines'])
        if 'id' in l: lines[l['id']]=l
for f in glob.glob('forms/2025/*.yaml'):
    d=yaml.safe_load(open(f)); d=d.get('form') or d.get('def'); walk(d.get('lines',[]))
gates=set()
for i,l in lines.items():
    for r in l.get('refuses') or []: gates.add(r['when'])
def refs(e,acc):
    if isinstance(e,dict):
        for v in e.values(): refs(v,acc)
    elif isinstance(e,list):
        for x in e: refs(x,acc)
    elif isinstance(e,str) and e in lines: acc.add(e)
    return acc
feed={}
for g in gates:
    if g not in lines: continue
    seen=set();front={g}
    for depth in range(4):
        nxt=set()
        for x in front:
            l=lines[x]; e=l.get('expr') or {}
            if e.get('op')=='input': 
                if x!=g or True: seen.add(x)
                continue
            nxt|=refs(e,set())
        front=nxt-seen
    for x in seen:
        if str(lines[x].get('type','')).startswith('Bool'):
            feed.setdefault(x,set()).add(g)
json.dump({'gates':sorted(gates),'feed':{k:sorted(v) for k,v in feed.items()}},open('/tmp/claude-0/sp/sweep_meta.json','w'))
print(len(lines),len(gates),len(feed))
