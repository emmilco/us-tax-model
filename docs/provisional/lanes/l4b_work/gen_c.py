p='engine/src/generate.ts'; t=open(p).read()
def rep(a,b,n=1):
    global t
    assert t.count(a)==n,(a,t.count(a)); t=t.replace(a,b)
rep('''const FIXED = new Set([''','''// The questions person.x_other and person.ira_excess were taken apart into, and the IRA parent: none is drawn (no
// generated person has one of the situations); putPersonFacts sets each for every person, the IRA parent from the
// contributions drawn.
const PERSON_NO = ["x_edu_account", "x_edu_taxable", "x_edu_excess", "x_archer_excess", "x_ira_prior_excess", "x_hsa_prior_excess",
  "inherited_account", "rmd_missed", "ira_extra_left", "ira_recharacterized"];
const FIXED = new Set([
  ...PERSON_NO.map((k) => `person[taxpayer].${k}`), "person[taxpayer].ira_owner",''')
rep('''const EARLY_ROOTS = ["x_other", "x_prior09",''','''const EARLY_ROOTS = ["x_prior09",''')
rep('''"person[taxpayer].ira_trad", "person[taxpayer].ira_excess", "person[taxpayer].ira_age50",''','''"person[taxpayer].ira_trad",''')
rep('''    Object.assign(inputs, { [`${P}.x_other`]: false, [`${P}.x_prior09`]: 0,''','''    Object.assign(inputs, { [`${P}.x_prior09`]: 0,''')
rep(''' [`${P}.ira_trad`]: 0, [`${P}.ira_excess`]: false, [`${P}.ira_age50`]: false,''',''' [`${P}.ira_trad`]: 0,''')
rep('''    inputs[`${P}.died_at_64`] = year === 1960 && died;
  }''','''    inputs[`${P}.died_at_64`] = year === 1960 && died;
    for (const k of PERSON_NO) inputs[`${P}.${k}`] = false;
    inputs[`${P}.ira_owner`] = inputs[`${P}.sav_trad`] === true || ((inputs[`${P}.sav_roth`] as number | undefined) ?? 0) > 0;
  }''')
open(p,'w').write(t)
print('ok')
