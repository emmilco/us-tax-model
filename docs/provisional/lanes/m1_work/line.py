import json,sys,glob,os
R='/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/canonical/2025/'
lines={}
for f in glob.glob(R+'*.json'):
    try: d=json.load(open(f))
    except Exception: continue
    if isinstance(d,dict) and 'form' in d: d=d['form']
    if isinstance(d,dict) and 'def' in d: d=d['def']
    if not isinstance(d,dict) or 'lines' not in d: continue
    for l in d['lines']: lines[l['id']]=l
def refs(x,out):
    if isinstance(x,str): out.add(x)
    elif isinstance(x,list):
        for y in x: refs(y,out)
    elif isinstance(x,dict):
        for k,v in x.items():
            if k in('source','param','const','ref'): continue
            refs(v,out)
readers={}
for i,l in lines.items():
    s=set(); refs(l.get('expr'),s)
    for r in l.get('refuses',[]) or []: s.add(r.get('when'))
    for t in s:
        readers.setdefault(t,[]).append(i)
for a in sys.argv[1:]:
    l=lines.get(a)
    if not l: print(a,'NOT FOUND'); continue
    e=dict(l['expr'])
    if 'source' in e: e['source']=e['source'][:80]
    print('==',a,l['type'],l.get('printed'),'gated_by=',l.get('gated_by'))
    print('  label:',l.get('label','')[:200])
    print('  expr:',json.dumps(e)[:900])
    for r in l.get('refuses',[]) or []: print('  refuses when',r.get('when'),'known' if r.get('when_known') else '')
    print('  readers:',readers.get(a,[]))
