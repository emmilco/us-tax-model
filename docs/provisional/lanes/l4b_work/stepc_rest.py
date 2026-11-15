import sys,json,re,glob,os; sys.path.insert(0,'/tmp/l4b')
from bank import Bank
F='For this person (you, or your spouse on a joint return) — '
END=' A return with this is outside what this tool prepares; a Yes ends the interview here.'
b=Bank()
# --- 144: the educator pair, turned round
b.set('person.eligible_educator',order=144,seq=1,
  prompt=F+'In 2025, did you work in a school, from kindergarten through grade 12, as a teacher, instructor, counselor, principal or aide, for at least 900 hours during a school year?')
b.set('person.educator_expenses',order=144,seq=2,
  prompt=F+'How much of your own money did you spend in 2025 on your classroom or your teaching: books, supplies, equipment, software, and courses you took for your work?',
  help='Count only what nobody paid you back. Leave out home schooling costs, and supplies for health or physical education courses that are not for athletics. Subtract any tax-free savings bond interest, 529 plan or Coverdell money that paid for them.')
# --- 180: saving in an IRA
b.add_after('person.sav_claimed','person.ira_owner',order=180,seq=1,
  prompt=F+'Do you have an IRA (an individual retirement account) of any kind?',
  help='Traditional, Roth, SEP and SIMPLE IRAs count, and so do an IRA you inherited and one opened in early 2026 for 2025. A 401(k) or a pension at work is not an IRA. If you are not sure, answer Yes.')
b.set('person.sav_trad',order=180,seq=2,
  prompt=F+'Did you put money into a traditional IRA for 2025? Money put in by April 15, 2026 for 2025 counts; a rollover from another retirement account does not.',
  help='It counts whether or not you can deduct it. Do not count money that went into a SEP IRA or a SIMPLE IRA, whether an employer paid it or you paid it for yourself from your own business.')
b.set('person.ira_trad',order=180,seq=3,
  prompt=F+'How much did you put into your traditional IRAs for 2025, in 2025 or by April 15, 2026?',
  help="Form 5498 or a statement from the IRA's trustee shows it. Leave out rollovers, money you deducted on your 2024 return, anything you took back out with its earnings by the deadline for your return, trustee's fees billed separately, and SEP or SIMPLE contributions.")
b.set('person.age50_at_year_end',order=180,seq=4)
b.set('person.ira_work_plan',order=180,seq=5,
  prompt=F+'Were you covered by a retirement plan at work in 2025, such as a pension or a 401(k), even if you were not vested in it? If you were, the "Retirement plan" box in box 13 of your Form W-2 should be ticked.',
  help='If you are not sure, ask your employer. Social security and railroad retirement are not a plan. A SEP or SIMPLE IRA of your own business is taken from your answers about the business.')
b.set('person.ira_excess',input='person.ira_extra_left',order=180,seq=6,
  prompt=F+'Did you put more into your IRAs for 2025 than you were allowed, and was the extra still there after the deadline for your 2025 return?',
  help='The limit for traditional and Roth IRAs together is $7,000 ($8,000 if you were 50 or older at the end of 2025), or your taxable pay if that is less; a Roth IRA has a lower limit at higher incomes.'+END)
b=Bank.__new__(Bank) if False else b
b.save(); b=Bank()
b.add_after('person.ira_extra_left','person.ira_recharacterized',order=180,seq=7,
  prompt=F+'Did you move a 2025 IRA contribution from a traditional IRA to a Roth IRA, or the other way (a "recharacterization")?',
  help=END.strip())
b.add_after('person.ira_recharacterized','person.x_ira_prior_excess',order=180,seq=8,
  prompt=F+'At the end of 2025, did your IRA still hold money put in above the limit in an earlier year?',
  help='This is an excess contribution from before 2025 that was never taken out or used up.'+END)
for s,i in enumerate(['person.ira_basis','person.ira_basis_adjusted','person.ira_dist'],9): b.set(i,order=180,seq=s)
# --- 177: required withdrawals, with the retirement money
b.add_after('person.x_births','person.inherited_account',order=177,seq=1,
  prompt=F+'Have you inherited an IRA or a workplace retirement account, such as a 401(k), from someone who died?',
  help='It counts even if the money is still in the account.')
b.add_after('person.inherited_account','person.rmd_missed',order=177,seq=2,
  prompt=F+'Did you take less than the required yearly minimum out of a retirement account by its deadline, even if you made up the shortfall later?',
  help='People aged 73 or older, and people who inherited an account, usually must take a minimum amount out each year.'+END)
b.set('person.x_prior09',order=177,seq=3); b.set('person.x_births',order=177,seq=4)
# --- 192: health savings accounts
b.set('person.x_other',input='person.x_hsa_prior_excess',order=192,seq=1,
  prompt=F+'Before 2025, was more put into your HSA than the limit for the year, with some of the extra still in the account at the start of 2025?',
  help='Answer Yes if your 2024 Form 5329 has an amount on line 48, or if you never reported the excess.'+END)
b.save(); b=Bank()
b.add_after('person.x_hsa_prior_excess','person.x_archer_excess',order=192,seq=2,
  prompt=F+'Was more put into an Archer MSA of yours (an older kind of medical savings account) than its limit, and is the extra still there?',
  help=END.strip())
# --- 247: education and ABLE accounts
b.add_after('person.x_archer_excess','person.x_edu_account',order=247,seq=1,
  prompt=F+'At any time in 2025, did you have a 529 plan, a Coverdell education savings account or an ABLE account, or was one held for you?',
  help='Answer Yes if you own the account or are the person it is for. A Form 1099-Q or Form 1099-QA sent to you for 2025 means Yes.')
b.add_after('person.x_edu_account','person.x_edu_taxable',order=247,seq=2,
  prompt=F+'Was any money that came out of the account in 2025 taxable: more than the education costs, or for an ABLE account the disability costs, that it paid for?',
  help='Money used for the costs the account is meant for is not taxable.'+END)
b.add_after('person.x_edu_taxable','person.x_edu_excess',order=247,seq=3,
  prompt=F+'Was more put into a Coverdell education savings account or an ABLE account held for you than its yearly limit, and is the extra still in the account?',
  help='This includes an excess from an earlier year.'+END)
b.save()
# --- defaults
p='fixtures/2025/defaults.json'; d=json.load(open(p))
CL='Closed: the circumstance this question asks about does not apply unless the scenario says so.'
new=[('person.ira_owner',False,'Closed: the ordinary filer of the defaults has no IRA; a scenario with an IRA contribution states it.'),
     ('person.ira_extra_left',False,CL),('person.ira_recharacterized',False,CL),('person.x_edu_account',False,CL),('person.x_edu_taxable',False,CL),
     ('person.x_edu_excess',False,CL),('person.x_archer_excess',False,CL),('person.x_ira_prior_excess',False,CL),('person.x_hsa_prior_excess',False,CL),
     ('person.inherited_account',False,CL),('person.rmd_missed',False,CL)]
d['defaults']=[e for e in d['defaults'] if e['input'] not in ('person.x_other','person.ira_excess')]
k=max(i for i,e in enumerate(d['defaults']) if e['input'].startswith('person.'))
d['defaults'][k+1:k+1]=[{'input':i,'value':v,'reason':r} for i,v,r in new]
open(p,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
# --- profiles
XS='  - person.x_edu_account\n  - person.x_edu_taxable\n  - person.x_edu_excess\n  - person.x_archer_excess\n  - person.x_ira_prior_excess\n  - person.x_hsa_prior_excess\n  - person.inherited_account\n  - person.rmd_missed\n  - person.ira_owner\n'
for f in ['stage4','sales','social-security']:
    p=f'interview/2025/{f}.yaml'; t=open(p).read()
    assert t.count('  - person.x_other\n')==1
    t=t.replace('  - person.x_other\n',XS).replace('  - person.ira_excess\n','  - person.ira_extra_left\n  - person.ira_recharacterized\n')
    open(p,'w').write(t)
