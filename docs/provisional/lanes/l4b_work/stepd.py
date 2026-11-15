"""ira.special taken apart into four questions (ira.yaml); person.sav_roth moved into the IRA block; fixtures, bank,
defaults, profiles, generator."""
import sys,json,re,glob,os; sys.path.insert(0,'/tmp/l4b')
from bank import Bank
from migrate_fmt import fmt
p='forms/2025/ira.yaml'; t=open(p).read()
m=re.search(r'(?ms)^  - id: ira\.special\n.*?(?=^  - id: )', t); blk=m.group(0)
cite=re.search(r'(?ms)^    cite:\n.*?(?=^    [a-z_]+:|\Z)', blk).group(0)
amb=re.search(r'(?m)^    ambiguity: .*\n', blk).group(0)
def q(i,label,src,a=''):
    return f"""  - id: {i}
    printed: (screen)
    label: {json.dumps(label)}
    type: Bool
    expr:
      op: input
      source: {json.dumps(src)}
{cite}{a}"""
items=[('ira.deferred_comp','Income from a nonqualified deferred compensation plan or a nongovernmental section 457 plan',
        'Did you (or your spouse on a joint return) have income from a nonqualified deferred compensation plan or a nongovernmental section 457 plan (an amount in box 11 of your Form W-2, in box 12 with code Z, or in box 15 of Form 1099-MISC)?',''),
       ('ira.fellowship','Taxable non-tuition fellowship or stipend payments not reported on a Form W-2',
        'Did you (or your spouse on a joint return) receive taxable non-tuition fellowship or stipend payments for graduate or postdoctoral study that were not reported on a Form W-2?',amb),
       ('ira.reservist_repaid','A repayment to an IRA of a qualified reservist distribution',
        'Did you (or your spouse on a joint return) repay a qualified reservist distribution to an IRA?',''),
       ('ira.care_payments','Difficulty of care payments used to increase the nondeductible IRA contribution limit',
        'Did you (or your spouse on a joint return) use difficulty of care payments (qualified foster care payments) to increase your nondeductible IRA contribution limit?','')]
new=re.sub(r'(?ms)^    expr:\n.*?(?=^    cite:)', "    expr:\n      op: test\n      any:\n"+''.join(f"      - op: test\n        eq:\n        - {i}\n        - const: true\n" for i,_,_,_ in items), blk)
new=new.replace(amb,'')
new=re.sub(r'(?m)^    label: .*\n','    label: One of the IRA deduction special cases applies (deferred compensation, a fellowship not on a Form W-2, a reservist repayment, difficulty of care payments)\n',new)
t=t.replace(blk,new+''.join(q(*x) for x in items)); open(p,'w').write(t)
# bank
b=Bank(); END=' A return with this is outside what this tool prepares; a Yes ends the interview here.'
b.set('ira.special',input='ira.deferred_comp',order=181,seq=1,
  prompt='In 2025, were you (or, on a joint return, your spouse) paid money from a deferred compensation plan: an amount in box 11 of a Form W-2, in box 12 with code Z, or in box 15 of a Form 1099-MISC?',
  help='This is pay earned in an earlier year under a plan that put off paying it. It does not count as pay for the IRA limit.'+END)
b.save(); b=Bank()
b.add_after('ira.deferred_comp','ira.fellowship',order=181,seq=2,
  prompt='In 2025, did you (or, on a joint return, your spouse) get a taxable fellowship or stipend for graduate or postdoctoral study that was not on a Form W-2?',
  help='Money for tuition does not count. Such a payment counts as pay for the IRA limit.'+END)
b.add_after('ira.fellowship','ira.reservist_repaid',order=181,seq=3,
  prompt='In 2025, did you (or, on a joint return, your spouse) pay back into an IRA money taken out while called to active duty as a military reservist?',
  help='This is the repayment of a "qualified reservist distribution".'+END)
b.add_after('ira.reservist_repaid','ira.care_payments',order=181,seq=4,
  prompt='In 2025, did you (or, on a joint return, your spouse) get tax-free payments for caring for a person with a disability in your home ("difficulty of care" payments) and put them into an IRA?',
  help=END.strip())
b.set('ira.se_capital',order=181,seq=5)
b.set('ira.deduct_less',order=181,seq=6,
  prompt="Do you want to deduct less of your (or, on a joint return, your spouse's) traditional IRA contributions than the most the rules allow, and treat the rest as not deducted?",
  help='Almost everyone answers No. A return that deducts less is outside what this tool prepares; a Yes ends the interview here. To go on with the full deduction, answer No.')
# the Roth amount belongs with the IRA questions
order=['person.ira_owner','person.sav_trad','person.ira_trad','person.sav_roth','person.age50_at_year_end','person.ira_work_plan','person.ira_extra_left','person.ira_recharacterized','person.x_ira_prior_excess','person.ira_basis','person.ira_basis_adjusted','person.ira_dist']
for s,i in enumerate(order,1): b.set(i,order=180,seq=s)
for s,i in enumerate(['person.sav_student','person.sav_claimed','person.sav_voluntary','person.sav_able','person.sav_excess','person.sav_prior_joint','person.sav_prior_other'],1): b.set(i,order=315,seq=s)
b.save()
# fixtures
n=0
for f in sorted(glob.glob('fixtures/2025/*.json')+glob.glob('fixtures/ny/2025/*.json')):
    tt=open(f).read(); d=json.loads(tt)
    if f.endswith('defaults.json'):
        if any(e['input']=='ira.special' for e in d['defaults']):
            k=[e['input'] for e in d['defaults']].index('ira.special'); r=d['defaults'][k]['reason']
            d['defaults'][k:k+1]=[{'input':i,'value':False,'reason':r} for i in sorted(x[0] for x in items)]
            d['defaults'].sort(key=lambda e:0)  # order kept
            open(f,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
        continue
    if 'cases' not in d: continue
    dump=fmt(tt); nodef=os.path.basename(f).startswith('classm') or os.path.basename(f)=='mutation.json'; ch=False
    for c in d['cases']:
        if 'ira.special' not in c['inputs']: continue
        out={}
        for k,v in c['inputs'].items():
            if k=='ira.special':
                n+=1
                if v is None:
                    for i,_,_,_ in items: out[i]=None
                else:
                    out['ira.deferred_comp']=bool(v)
                    if nodef or v:
                        for i,_,_,_ in items[1:]: out[i]=False
            else: out[k]=v
        c['inputs']=out; ch=True
    if ch: open(f,'w').write(dump(d))
print('ira.special cases',n)
for f in ['stage4','sales','social-security']:
    p=f'interview/2025/{f}.yaml'; t=open(p).read()
    t=t.replace('  - ira.special\n',''.join(f'  - {i}\n' for i,_,_,_ in items)); open(p,'w').write(t)
p='engine/src/generate.ts'; t=open(p).read(); a='"ira.special", "ira.se_capital"'
assert t.count(a)==1; t=t.replace(a,'"ira.deferred_comp", "ira.fellowship", "ira.reservist_repaid", "ira.care_payments", "ira.se_capital"'); open(p,'w').write(t)
