import yaml,subprocess,json,sys,os
W='/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1'
def load(commit):
    out={}
    if commit=='NOW':
        files=[f for f in os.listdir(W+'/forms/2025') if f.endswith('.yaml')]
        get=lambda f: open(W+'/forms/2025/'+f).read()
    else:
        files=[f.split('/')[-1] for f in subprocess.check_output(['git','-C',W,'ls-tree','--name-only',commit,'forms/2025/']).decode().split()]
        files=[f for f in files if f.endswith('.yaml')]
        get=lambda f: subprocess.check_output(['git','-C',W,'show',f'{commit}:forms/2025/{f}']).decode()
    for f in files:
        d=yaml.safe_load(get(f))
        d=d.get('form') or d.get('def') or d
        for l in d.get('lines',[]) or []: out[l['id']]=l
    return out
def refs(x,s):
    if isinstance(x,str): s.add(x)
    elif isinstance(x,list): [refs(y,s) for y in x]
    elif isinstance(x,dict):
        for k,v in x.items():
            if k in ('source','param','const','ref'): continue
            refs(v,s)
def readers(lines):
    r={}
    for i,l in lines.items():
        s=set(); refs(l.get('expr'),s)
        for g in l.get('refuses') or []: s.add(g.get('when'))
        for t in s: r.setdefault(t,set()).add(i)
    return r
def facts(l):
    e=l.get('expr',{}); e={'op':'input'} if e.get('op')=='input' else e
    return {'expr':e,'refuses':l.get('refuses') or [],'type':l.get('type'),'printed':l.get('printed'),'shown_when':l.get('shown_when')}
old_c=sys.argv[1]; prem=sys.argv[2].split(',')
A=load(old_c); B=load('NOW'); RA=readers(A); RB=readers(B)
for p in prem:
    if ':' in p: continue
    a=A.get(p); b=B.get(p)
    if a is None or b is None: print(p,'MISSING old' if a is None else 'MISSING now'); continue
    fa,fb=facts(a),facts(b)
    for k in fa:
        if json.dumps(fa[k],sort_keys=True)!=json.dumps(fb[k],sort_keys=True):
            print(p,k,'\n   old:',json.dumps(fa[k])[:600],'\n   new:',json.dumps(fb[k])[:600])
    ra,rb=RA.get(p,set()),RB.get(p,set())
    if ra!=rb: print(p,'readers -',sorted(ra-rb),'+',sorted(rb-ra))
