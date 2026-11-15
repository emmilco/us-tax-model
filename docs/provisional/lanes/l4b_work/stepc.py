"""Step C model edits to person.yaml and ira.yaml: person.x_other taken apart, an IRA parent, the educator pair turned
round, person.ira_excess in two."""
import sys,re; sys.path.insert(0,'/tmp/l4b')
from pm import Form, gate, inp, yq
F=Form('forms/2025/person.yaml')
cx=F.cite('person.x_other')
def test_any(ids):
    return "      expr:\n        op: test\n        any:\n"+''.join(f"        - op: test\n          eq:\n          - {i}\n          - const: true\n" for i in ids)
# ---- the IRA parent
c_ira=F.cite('person.sav_trad')
F.add_after('person.sav_ineligible',
  inp('person.ira_owner','Do you have an individual retirement arrangement (IRA) of any kind: traditional, Roth, SEP or SIMPLE, including an inherited IRA and one opened in 2026 for 2025?',c_ira,
      label='Has an IRA of any kind (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)')
 +gate('person.sav_trad','person.sav_trad_if_ira_owner','person.ira_owner','Made traditional IRA contributions for 2025 (asked only of a person with an IRA; otherwise no)',c_ira))
F.insert_field_after('person.sav_trad','type','      gated_by: person.sav_trad_if_ira_owner\n')
F.replace_in('person.ira_contrib','            - person.sav_trad\n','            - person.sav_trad_if_ira_owner\n',2)
c_roth=F.cite('person.sav_roth')
F.insert_field_after('person.sav_roth','type','      gated_by: person.sav_roth_if_ira_owner\n')
F.add_after('person.sav_roth',gate('person.sav_roth','person.sav_roth_if_ira_owner','person.ira_owner','Roth IRA contributions for 2025 (asked only of a person with an IRA; otherwise zero)',c_roth,zero='person.zero',typ='NonNegDollars'))
n=0
for i in list(F.ids):
    if i in ('person.sav_roth','person.sav_roth_if_ira_owner'): continue
    k=F.ids.index(i); c=F.blocks[k].count('- person.sav_roth\n')
    if c: F.blocks[k]=F.blocks[k].replace('- person.sav_roth\n','- person.sav_roth_if_ira_owner\n'); n+=c
print('sav_roth readers rewired in person.yaml:',n)
# ---- person.x_other: six situations, each its own question
items=[]
F.add_after('person.x_other',
  inp('person.x_edu_account','In 2025, was money put into or taken out of a qualified tuition program (529 plan), a Coverdell ESA or an ABLE account that is yours or is held for you?',cx,
      label='A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025')
 +inp('person.x_edu_taxable','Did you receive a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account?',cx,gated_by='person.x_edu_taxable_if_account')
 +gate('person.x_edu_taxable','person.x_edu_taxable_if_account','person.x_edu_account','A taxable distribution from a Coverdell ESA, a qualified tuition program or an ABLE account (asked only with such an account; otherwise no)',cx)
 +inp('person.x_edu_excess','Do you have excess contributions to a Coverdell ESA or an ABLE account?',cx,gated_by='person.x_edu_excess_if_account')
 +gate('person.x_edu_excess','person.x_edu_excess_if_account','person.x_edu_account','Excess contributions to a Coverdell ESA or an ABLE account (asked only with such an account; otherwise no)',cx)
 +inp('person.x_archer_excess','Do you have excess contributions to an Archer MSA?',cx)
 +inp('person.x_ira_prior_excess','Did excess contributions to a traditional or Roth IRA for an earlier year remain in the IRA at the end of 2025 (whether or not you contributed for 2025)?',cx,gated_by='person.x_ira_prior_excess_if_ira_owner')
 +gate('person.x_ira_prior_excess','person.x_ira_prior_excess_if_ira_owner','person.ira_owner','An earlier year\'s excess IRA contributions remained at the end of 2025 (asked only of a person with an IRA; otherwise no)',cx)
 +f"""    - id: person.has_hsa
      printed: (helper)
      type: Bool
      label: This person listed a health savings account
      expr:
        op: test
        gt:
        - person.hsa_forms
        - const: 0
          type: Count
{cx}"""
 +inp('person.x_hsa_prior_excess','Do you have excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported)?',cx,gated_by='person.x_hsa_prior_excess_if_hsa')
 +gate('person.x_hsa_prior_excess','person.x_hsa_prior_excess_if_hsa','person.has_hsa','An earlier year\'s excess HSA contributions not removed or used up before 2025 (asked only of a person who listed a health savings account; otherwise no)',cx)
 +f"""    - id: person.rmd_age
      printed: (helper)
      type: Bool
      label: Born in 1952 or earlier (age 73 or older at the end of 2025)
      expr:
        op: test
        le:
        - person.birth_year
        - const: 1952
          type: Count
{cx}"""
 +inp('person.inherited_account','Have you inherited an IRA or an account in a retirement plan from someone who died?',cx,gated_by='person.inherited_account_if_under_73')
 +gate('person.inherited_account','person.inherited_account_if_under_73','person.rmd_age','Inherited an IRA or a retirement plan account (asked only of a person born after 1952; otherwise no)',cx)
     .replace('const: true','const: TMP').replace('const: false','const: true').replace('const: TMP','const: false')
 +f"""    - id: person.rmd_possible
      printed: (helper)
      type: Bool
      label: A required minimum distribution is possible for this person (born in 1952 or earlier, or inherited an account)
      expr:
        op: test
        any:
        - op: test
          eq:
          - person.rmd_age
          - const: true
        - op: test
          eq:
          - person.inherited_account_if_under_73
          - const: true
{cx}"""
 +inp('person.rmd_missed','Was there a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)?',cx,gated_by='person.rmd_missed_if_possible')
 +gate('person.rmd_missed','person.rmd_missed_if_possible','person.rmd_possible','A required minimum distribution not received in full by its deadline (asked only of a person born in 1952 or earlier or with an inherited account; otherwise no)',cx)
)
F.set_field('person.x_other','expr',test_any(['person.x_edu_taxable_if_account','person.x_edu_excess_if_account','person.x_archer_excess','person.x_ira_prior_excess_if_ira_owner','person.x_hsa_prior_excess_if_hsa','person.rmd_missed_if_possible']))
# ---- the educator pair turned round
ce=F.cite('person.educator_expenses')
F.insert_field_after('person.educator_expenses','type','      gated_by: person.educator_expenses_if_educator\n')
F.add_after('person.eligible_educator',gate('person.educator_expenses','person.educator_expenses_if_educator','person.eligible_educator','Qualified educator expenses paid in 2025 (asked only of an eligible educator; otherwise zero)',ce,zero='person.zero',typ='NonNegDollars'))
F.replace_in('person.has_educator_expenses','        - person.educator_expenses\n','        - person.educator_expenses_if_educator\n')
F.replace_in('person.educator_limited','        - person.educator_expenses\n','        - person.educator_expenses_if_educator\n')
# ---- person.ira_excess in two
cxs=F.cite('person.ira_excess')
F.add_after('person.ira_excess',
  inp('person.ira_extra_left','Were your contributions for 2025 to traditional and Roth IRAs together more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), with the excess not withdrawn with its earnings by the due date of your return (including extensions)?',cxs,printed='(screen)')
 +inp('person.ira_recharacterized','Did you recharacterize a 2025 contribution (move it from a traditional to a Roth IRA or the reverse)?',cxs,printed='(screen)'))
F.set_field('person.ira_excess','expr',test_any(['person.ira_extra_left','person.ira_recharacterized']))
F.set_field('person.ira_excess','label','      label: "This person\'s 2025 IRA contributions were more than allowed and not withdrawn, or were recharacterized"\n')
F.save()
p='forms/2025/ira.yaml'; t=open(p).read(); assert t.count('field: person.sav_roth\n')==1
open(p,'w').write(t.replace('field: person.sav_roth\n','field: person.sav_roth_if_ira_owner\n'))
print('ok')
