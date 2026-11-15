"""Step C fixture inputs: person.x_other and person.ira_excess stated as the new questions; person.ira_owner where an
IRA contribution is stated; person.eligible_educator where only the expenses were stated (files without defaults)."""
import sys,json,glob,os,re; sys.path.insert(0,'/tmp/l4b')
from migrate_fmt import fmt
n=dict(x=0,ira=0,exc=0,edu=0)
for f in sorted(glob.glob('fixtures/2025/*.json')+glob.glob('fixtures/ny/2025/*.json')):
    if f.endswith('defaults.json'): continue
    t=open(f).read(); d=json.loads(t)
    if 'cases' not in d: continue
    dump=fmt(t); nodef=os.path.basename(f).startswith('classm') or os.path.basename(f)=='mutation.json'; ch=False
    for c in d['cases']:
        inp=c['inputs']
        ps=sorted({m.group(1) for k in inp for m in [re.match(r'person\[([^\]]+)\]\.',k)] if m})
        for p in ps:
            P=f'person[{p}].'; g=lambda k: inp.get(P+k)
            has=lambda k: (P+k) in inp
            out={}
            trad=g('sav_trad') is True or (has('sav_trad') and g('sav_trad') is None); roth=has('sav_roth') and g('sav_roth') not in (0,None,False)
            owner=trad or roth
            need_owner = owner or (nodef and (has('x_other') or has('sav_trad') or has('sav_roth')))
            for k,v in inp.items():
                if k==P+'x_other':
                    n['x']+=1
                    if v is None: out[P+'x_edu_account']=None; out[P+'x_archer_excess']=None; out[P+'inherited_account']=None; out[P+'rmd_missed']=None; continue
                    out[P+'x_edu_account']=bool(v)
                    if v: out[P+'x_edu_taxable']=True
                    if nodef or v:
                        if v: out[P+'x_edu_excess']=False
                        out[P+'x_archer_excess']=False; out[P+'inherited_account']=False; out[P+'rmd_missed']=False
                        out[P+'x_hsa_prior_excess']=False; out[P+'x_ira_prior_excess']=False
                elif k==P+'ira_excess':
                    n['exc']+=1
                    if v is None: out[P+'ira_extra_left']=None; out[P+'ira_recharacterized']=None
                    else: out[P+'ira_extra_left']=bool(v); out[P+'ira_recharacterized']=False
                elif k==P+'educator_expenses':
                    out[k]=v
                    if nodef and not has('eligible_educator'): out[P+'eligible_educator']=False; n['edu']+=1
                else: out[k]=v
            if need_owner and not has('ira_owner'):
                # beside the contribution answer where there is one
                o2={}; put=False
                for k,v in out.items():
                    if not put and k in (P+'sav_trad',P+'sav_roth',P+'x_edu_account'): o2[P+'ira_owner']=owner; put=True
                    o2[k]=v
                if not put: o2[P+'ira_owner']=owner
                out=o2; n['ira']+=1
            if out!=inp or list(out)!=list(inp): ch=True
            c['inputs']=inp=out
    if ch: open(f,'w').write(dump(d))
print(n)
