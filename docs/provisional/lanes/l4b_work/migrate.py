"""Rewrite the fixtures' birth-date answers as a birth year (and the stated answers a cut year needs).
usage: migrate.py [--override FILE]   FILE: json {case id: {person: candidate}} chosen by the search (search.py)."""
import sys,json,os; sys.path.insert(0,'/tmp/l4b')
from fx import *
DEF={'age65':False,'born_after_1960':True,'born_before_2001':True,'edu_born_2002':False,'edu_born_2007':False,'sav_born':True,'under16':False,'ira_age50':False,'died_before_65':False}
over={}
if '--override' in sys.argv: over=json.load(open(sys.argv[sys.argv.index('--override')+1]))
def fmt(t):
    d=json.loads(t)
    for kw in (dict(indent=2),dict(separators=(',',':')),dict(indent=1)):
        for ea in (False,True):
            for nl in ('','\n'):
                if json.dumps(d,ensure_ascii=ea,**kw)+nl==t: return lambda x: json.dumps(x,ensure_ascii=ea,**kw)+nl
    raise SystemExit('format')
def new_keys(p,c):
    o={f'person[{p}].birth_year':c['y']}
    if c['y'] in (1961,2001,2002,2007,2008): o[f'person[{p}].born_jan1']=c.get('j',False)
    if c['y']==2010: o[f'person[{p}].under16_at_year_end']=c.get('u',True)
    if c['y']==1976: o[f'person[{p}].age50_at_year_end']=c.get('a',False)
    if c['y']==1960 or (c['y']==1961 and c.get('j')): o[f'person[{p}].died_at_64']=c.get('d',False)
    return o
def choose(S,soft):
    hard={k:v for k,v in S.items() if v is not None}
    sat=satisfying(hard); exact=bool(sat)
    pool=sat or CANDS
    def score(c):
        v=vec(c)
        h=sum(v[k]==val for k,val in hard.items())
        return (h,0)
    best=max(pool,key=lambda c:(score(c),-pool.index(c)))
    return best,exact
report={'unsat':[], 'null':[]}
chosen={}
for f in files():
    if f.endswith('defaults.json') or 'differential' in f: continue
    t=open(f).read(); d=json.loads(t); dump=fmt(t)
    soft=not (os.path.basename(f).startswith('classm') or os.path.basename(f)=='mutation.json')
    changed=False
    for c in d['cases']:
        inp=c['inputs']
        for p in sorted(persons(inp)):
            S=stated(inp,p)
            if c['id'] in over and p in over[c['id']]: cand,exact=over[c['id']][p],True
            else: cand,exact=choose(S,soft)
            if any(v is None for v in S.values()): report['null'].append((f,c['id'],p,S))
            if not exact: report['unsat'].append((f,c['id'],p,S,cand))
            nk=new_keys(p,cand)
            if any(v is None for v in S.values()) and all(v is None for v in S.values()):
                nk={f'person[{p}].birth_year':None}
            out={}; done=False
            for k,v in inp.items():
                if k.startswith(f'person[{p}].') and k.split('.',1)[1] in OLD:
                    if not done: out.update(nk); done=True
                else: out[k]=v
            c['inputs']=inp=out; changed=True
            chosen.setdefault(c['id'],{})[p]=cand
    if changed: open(f,'w').write(dump(d))
json.dump(chosen,open('/tmp/l4b/chosen.json','w'))
json.dump(report,open('/tmp/l4b/report.json','w'),indent=1)
print('unsat',len(report['unsat']),'null',len(report['null']))
for r in report['null']: print(r)
