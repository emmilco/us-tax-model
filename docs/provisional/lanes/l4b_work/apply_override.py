import sys,json,glob,os,re; sys.path.insert(0,'/tmp/l4b')
from migrate_fmt import fmt, new_keys
over=json.load(open(sys.argv[1]))
NEW=['birth_year','born_jan1','under16_at_year_end','age50_at_year_end','died_at_64']
for f in sorted(glob.glob('fixtures/2025/*.json')+glob.glob('fixtures/ny/2025/*.json')):
    if f.endswith('defaults.json'): continue
    t=open(f).read(); d=json.loads(t)
    if 'cases' not in d: continue
    dump=fmt(t); ch=False
    for c in d['cases']:
        if c['id'] not in over: continue
        for p,cand in over[c['id']].items():
            nk=new_keys(p,cand); out={}; done=False
            for k,v in c['inputs'].items():
                if k in [f'person[{p}].{n}' for n in NEW]:
                    if not done: out.update(nk); done=True
                else: out[k]=v
            if not done: out.update(nk)
            c['inputs']=out; ch=True; print('set',c['id'],p,nk)
    if ch: open(f,'w').write(dump(d))
