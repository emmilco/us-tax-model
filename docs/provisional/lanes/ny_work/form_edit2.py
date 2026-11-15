import re,sys
exec(open('/tmp/nywork/form_edit.py').read().split("# ---- residency")[0].replace("s=open(p).read()","s=open(p).read()"))
def gt(x, c=0, typ=None): return '{ op: test, gt: ["%s", { const: %s%s }] }'%(x,c,', type: %s'%typ if typ else '')
def ne0(x): return '{ op: test, ne: ["%s", { const: 0 }] }'%x
def anyof(*t): return '{ op: test, any: [%s] }'%", ".join(t)
def allof(*t): return '{ op: test, all: [%s] }'%", ".join(t)
def add_gated(qid, gate):
    global s
    m=re.search(r"    - id: %s\n(?:      .*\n)+?"%re.escape(qid), s)
    blk=m.group(0)
    assert "gated_by" not in blk, qid
    s=s.replace(blk, blk+"      gated_by: %s\n"%gate)
def set_expr(lid, expr):
    global s
    m=re.search(r"(    - id: %s\n(?:      (?!expr).*\n)*?)      expr:.*\n(?:        .*\n)*"%re.escape(lid), s)
    s=s.replace(m.group(0), m.group(1)+"      expr: %s\n"%expr)
def before(lid, text):
    rep("    - id: %s\n"%lid, text+"    - id: %s\n"%lid)

# inflation check: only with other income on the federal return
before("ny_it201.gate.line25",
  line("ny_it201.has_other_income","Other income on federal Schedule 1 (line 9 is not zero)",ne0("s1.line9"),C_25,printed='(helper)')
 +line("ny_it201.inflation_if_other_income","An inflation refund check in federal income (asked only with other income on Schedule 1; otherwise no)",choose("ny_it201.has_other_income","ny_it201.ask.inflation_check"),C_25))
set_expr("ny_it201.gate.line25", anyof(gt("ny_it201.line4"), test_eq("ny_it201.inflation_if_other_income","true")))
add_gated("ny_it201.ask.inflation_check","ny_it201.inflation_if_other_income")
# other states' bonds: only with tax-exempt interest
before("ny_it201.gate.line20", line("ny_it201.has_tax_exempt","Tax-exempt interest or exempt-interest dividends on federal line 2a",gt("f1040.line2a"),C_20,printed='(helper)'))
set_expr("ny_it201.gate.line20", choose("ny_it201.has_tax_exempt","ny_it201.ask.out_of_state_bond_interest"))
add_gated("ny_it201.ask.out_of_state_bond_interest","ny_it201.gate.line20")
# 414(h): a public job in New York, asked only with a W-2
before("ny_it201.gate.line21",
  q("ny_it201.ask.public_job","A government job in New York","In 2025, did you (or, on a joint return, your spouse) work for the government in New York, including a public school or college or the MTA?",C_21,"ny_it201.public_job_if_w2")
 +line("ny_it201.public_job_if_w2","A public employer in New York (asked only when the return has a Form W-2; otherwise no)",choose("scope.has_w2","ny_it201.ask.public_job"),C_21))
set_expr("ny_it201.gate.line21", choose("ny_it201.public_job_if_w2","ny_it201.ask.414h"))
add_gated("ny_it201.ask.414h","ny_it201.gate.line21")
# 529: only with a 529, Coverdell or ABLE account entered on the federal part, and a New York 529 account
before("ny_it201.gate.line22",
  line("ny_it201.edu_people","Number of persons on the return who had a 529 plan, Coverdell or ABLE account (federal answer)",
       '{ op: sum_over, collection: person, field: person.one, where: %s }'%test_eq("person.x_edu_account","true"),C_30,typ='Count',printed='(helper)')
 +line("ny_it201.has_edu_account","A 529 plan, Coverdell or ABLE account on the return",gt("ny_it201.edu_people",0,"Count"),C_30,printed='(helper)')
 +q("ny_it201.ask.ny_529","Owns an account in New York's 529 college savings program","Is any 529 account you (or, on a joint return, your spouse) own part of New York's own 529 college savings program?",C_30,"ny_it201.ny_529_if_account")
 +line("ny_it201.ny_529_if_account","An account in New York's 529 program (asked only with a 529, Coverdell or ABLE account; otherwise no)",choose("ny_it201.has_edu_account","ny_it201.ask.ny_529"),C_30))
set_expr("ny_it201.gate.line22", choose("ny_it201.ny_529_if_account","ny_it201.ask.529_nonqualified"))
add_gated("ny_it201.ask.529_nonqualified","ny_it201.gate.line22")
set_expr("ny_it201.gate.line30", choose("ny_it201.ny_529_if_account","ny_it201.ask.529_owner"))
add_gated("ny_it201.ask.529_owner","ny_it201.gate.line30")
# government pensions: the plain parent and, after a No, the public plans a filer may not count as government
before("ny_it201.gate.line26",
  q("ny_it201.ask.gov_pension_other","A pension from the MTA, MABSTOA, the Long Island Rail Road or a SUNY, CUNY or State Education Department plan","Was any of it from the MTA, MABSTOA, the Long Island Rail Road, or a SUNY, CUNY or State Education Department plan (such as TIAA)?",C_26,"ny_it201.gov_pension_other_if_no")
 +line("ny_it201.gov_pension_other_if_no","Asked only after a No to the government pension question; otherwise no",choose("ny_it201.ask.gov_pension","ny_it201.no","ny_it201.ask.gov_pension_other"),C_26)
 +line("ny_it201.gov_pension_any","A New York State or local or federal government pension (either question)",anyof(test_eq("ny_it201.ask.gov_pension","true"),test_eq("ny_it201.gov_pension_other_if_no","true")),C_26,printed='(helper)'))
set_expr("ny_it201.gate.line26", choose("ny_it201.has_pension_income","ny_it201.gov_pension_any"))
# pension exclusion: a recipient born in 1965 or earlier settles it; otherwise the question
before("ny_it201.gate.line29",
  line("ny_it201.pension_59_people","Number of persons with taxable IRA, pension or annuity income who were born in 1965 or earlier (59½ or older at some time in 2025)",
       '{ op: sum_over, collection: person, field: person.one, where: %s }'%allof(anyof(gt("person.ira_taxable"),gt("person.plan_taxable")),'{ op: test, le: ["person.birth_year", { const: 1965, type: Count }] }'),C_29,typ='Count',printed='(helper)')
 +line("ny_it201.pension_59_known","A person who received taxable IRA, pension or annuity income was born in 1965 or earlier",gt("ny_it201.pension_59_people",0,"Count"),C_29,printed='(helper)')
 +line("ny_it201.pension_exclusion_line","The pension exclusion may apply: yes when a recipient was born in 1965 or earlier, otherwise the answer to ny_it201.ask.pension_exclusion",choose("ny_it201.pension_59_known","ny_it201.yes","ny_it201.ask.pension_exclusion"),C_29))
set_expr("ny_it201.gate.line29", choose("ny_it201.has_pension_income","ny_it201.pension_exclusion_line"))
rep("      gated_by: ny_it201.gate.line29\n","      gated_by: ny_it201.pension_exclusion_line\n")
# itemizing: the wish, asked only with amounts New York itemizes; the spouse's choice, asked only married filing separately
before("ny_it201.gate.itemize",
  line("ny_it201.itemizable","Federal Schedule A amounts New York also itemizes: medical, real estate and personal property taxes, interest, gifts, casualty and other deductions (not income taxes)",
       '{ op: sum, of: ["sa.line1", "sa.line5b", "sa.line5c", "sa.line10", "sa.line14", "sa.line15", "sa.line16"] }',C_34,typ='NonNegDollars',printed='(helper)')
 +line("ny_it201.has_itemizable","Any amount New York itemizes",gt("ny_it201.itemizable"),C_34,printed='(helper)')
 +line("ny_it201.itemize_if_amounts","The wish to itemize (asked only with amounts New York itemizes; otherwise no)",choose("ny_it201.has_itemizable","ny_it201.ask.itemize"),C_34)
 +q("ny_it201.ask.spouse_itemizes","Married filing separately, with a spouse who itemizes on their New York return","Is your husband or wife itemizing deductions on their own New York return?",'{ doc: ny_it201i, locator: ''p. 11, Notes, "If you are married filing separately and your spouse itemizes deductions, you must also itemize"'' }',"ny_it201.spouse_itemizes_if_mfs")
 +line("ny_it201.spouse_itemizes_if_mfs","The spouse itemizes (asked only married filing separately; otherwise no)",
       '{ op: choose, alternatives: [{ guard: %s, then: "ny_it201.no" }, { guard: %s, then: "ny_it201.no" }, { guard: %s, then: "ny_it201.ask.spouse_itemizes" }, { guard: %s, then: "ny_it201.no" }, { guard: %s, then: "ny_it201.no" }] }'%tuple(test_eq("f1040.status",x) for x in ["single","mfj","mfs","hoh","qss"]),C_34))
set_expr("ny_it201.gate.itemize", anyof(test_eq("ny_it201.itemize_if_amounts","true"),test_eq("ny_it201.spouse_itemizes_if_mfs","true")))
add_gated("ny_it201.ask.itemize","ny_it201.itemize_if_amounts")
# city credits: only the unincorporated business tax credit is open to a full-year City resident within this tool; asked only with a business
set_expr("ny_it201.gate.city_credits", choose("s1.has_sc","ny_it201.ask.city_credits"))
add_gated("ny_it201.ask.city_credits","ny_it201.gate.city_credits")
# real property tax credit: only with federal AGI of $18,000 or less and item C No
before("ny_it201.gate.real_property",
  line("ny_it201.low_income","Federal adjusted gross income of $18,000 or less and not claimable as another's dependent (the first tests of Form IT-214)",
       allof('{ op: test, le: ["ny_it201.fagi_rounded", { const: 1800000 }] }', test_eq("ny_it201.item_c","false")),C_67,printed='(helper)'))
set_expr("ny_it201.gate.real_property", choose("ny_it201.low_income","ny_it201.ask.real_property_credit"))
add_gated("ny_it201.ask.real_property_credit","ny_it201.gate.real_property")
# college tuition: only when the federal part says college tuition was paid
set_expr("ny_it201.gate.college_tuition", choose("f8863.paid","ny_it201.ask.college_tuition"))
add_gated("ny_it201.ask.college_tuition","ny_it201.gate.college_tuition")
# other withholding: only with a pension, IRA, unemployment or other income payment
before("ny_it201.gate.other_withholding",
  line("ny_it201.has_other_payments","IRA, pension, unemployment or other income that can carry withholding outside a Form W-2",
       anyof(gt("f1040.line4a"),gt("f1040.line5a"),gt("s1.line7"),ne0("s1.line9")),C_72,printed='(helper)'))
set_expr("ny_it201.gate.other_withholding", choose("ny_it201.has_other_payments","ny_it201.ask.other_withholding"))
add_gated("ny_it201.ask.other_withholding","ny_it201.gate.other_withholding")
# use tax: the exact-amount wish, asked only after a No to the large or business purchase
before("ny_it201.gate.use_tax_st141",
  q("ny_it201.ask.use_tax_exact","Wants the use tax figured exactly (Form ST-141) rather than from the chart","Do you want your use tax worked out exactly from your purchases instead of taken from New York''s chart by income?".replace("''","'"),C_59,"ny_it201.use_tax_exact_if_small")
 +line("ny_it201.use_tax_exact_if_small","The exact-amount wish (asked only after a No to the large or business purchase; otherwise no)",choose("ny_it201.ask.use_tax_st141","ny_it201.no","ny_it201.ask.use_tax_exact"),C_59))
set_expr("ny_it201.gate.use_tax_st141", allof(test_eq("ny_it201.ask.owes_use_tax","true"), anyof(test_eq("ny_it201.ask.use_tax_st141","true"),test_eq("ny_it201.use_tax_exact_if_small","true"))))
# line 75: a plain parent, the amount beneath
old75 = re.search(r"    - id: ny_it201.line75\n(?:      .*\n)+?(?=    - id: ny_it201.line76)", s).group(0)
amt = old75.replace("    - id: ny_it201.line75\n      printed: '75'\n","    - id: ny_it201.line75_amount\n      printed: '(question)'\n").rstrip("\n")+"\n      gated_by: ny_it201.line75\n"
s = s.replace(old75,
  q("ny_it201.ask.est_any","Paid New York income tax for 2025 in advance, or had a 2024 refund applied","Apart from tax taken out of your pay, did you (or, on a joint return, your spouse) pay New York income tax for 2025 ahead of time, or have a 2024 New York refund applied to it?",C_75)
 + amt
 + line("ny_it201.line75","Total estimated tax payments and amount paid with Form IT-370",choose("ny_it201.ask.est_any","ny_it201.line75_amount","ny_it201.zero"),C_75,typ='NonNegDollars',printed='75'))
# line 79: a plain parent over the amount
before("ny_it201.line79_amount",
  q("ny_it201.ask.apply_any","Wants part of the overpayment applied to 2026 estimated tax","Do you want any of your New York refund kept as a payment toward your 2026 New York tax, instead of paid to you?",C_79,"ny_it201.apply_if_overpaid")
 +line("ny_it201.apply_if_overpaid","Asked only with an overpayment; otherwise no",choose("ny_it201.has_overpayment","ny_it201.ask.apply_any"),C_79)
 +line("ny_it201.line79_wanted","The amount to apply (zero unless asked for)",choose("ny_it201.apply_if_overpaid","ny_it201.line79_amount","ny_it201.zero"),C_79,typ='NonNegDollars',printed='(helper)'))
rep("      gated_by: ny_it201.line79\n","      gated_by: ny_it201.line79_wanted\n")
set_expr("ny_it201.line79", choose("ny_it201.has_overpayment","ny_it201.line79_wanted","ny_it201.zero"))
# late penalty: only with a balance due
set_expr("ny_it201.gate.late", choose("ny_it201.tax_due_positive","ny_it201.ask.late_penalty"))
add_gated("ny_it201.ask.late_penalty","ny_it201.gate.late")
open(p,'w').write(s)
print("part 2 ok")
