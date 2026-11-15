# Edits forms/ny/2025/ny_it201.yaml for the New York redraft (lane ny). Run once from the worktree root.
import re,sys
p='forms/ny/2025/ny_it201.yaml'
s=open(p).read()
def rep(a,b):
    global s
    n=s.count(a)
    if n!=1: sys.exit("count %d for: %s"%(n,a[:120]))
    s=s.replace(a,b)
def line(id_, label, expr, cite, typ='Bool', gated=None, printed='(gate)'):
    out="    - id: %s\n      printed: '%s'\n      label: '%s'\n      type: %s\n      expr: %s\n      cite: %s\n"%(id_,printed,label.replace("'","''"),typ,expr,cite)
    if gated: out+="      gated_by: %s\n"%gated
    return out
def q(id_, label, source, cite, gated=None):
    return line(id_, label, "{ op: input, source: '%s' }"%source.replace("'","''"), cite, 'Bool', gated, '(question)')
C_RES='{ doc: ny_it201i, locator: ''p. 30, Resident, "You maintain a permanent place of abode in New York State for substantially all of the tax year and spend 184 days or more in New York State during the tax year"'' }'
C_ACC='{ doc: ny_it201i, locator: ''p. 31, Special accruals, "you may have to use special accrual rules (see below) to calculate your New York State and New York City personal income tax for 2025"'' }'
C_G='{ doc: ny_it201i, locator: ''p. 5, Item G, "If you qualify for one or more of the special conditions below, enter the specified two-character code."'' }'
C_C='{ doc: ny_it201i, locator: ''p. 5, Item C, "If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box."'' }'
C_21='{ doc: ny_it201i, locator: ''p. 8, Line 21, "Are you a public employee of New York State or its local governments?"'' }'
C_22='{ doc: ny_it201i, locator: ''p. 8, Line 22, "Did you make a nonqualified withdrawal during 2025 from an account established under New York’s 529 college savings program?"'' }'
C_30='{ doc: ny_it201i, locator: ''p. 10, Line 30, "During 2025, did you, as an account owner, make contributions to or a withdrawal from one or more tuition savings accounts established under New York’s 529 college savings program?"'' }'
C_26='{ doc: ny_it201i, locator: ''p. 9, Line 26, "Did you receive a pension or other distribution from a New York State or local government pension plan or federal government pension plan that was included in your federal adjusted gross income?"'' }'
C_29='{ doc: ny_it201i, locator: ''p. 9, Line 29, "If Yes, and you were 59½ before January 1, 2025, enter the qualifying pension and annuity income included in your 2025 federal adjusted gross income, but not more than $20,000."'' }'
C_20='{ doc: ny_it201i, locator: ''p. 7, Line 20, "Do you have interest income from state and local bonds and obligations from states other than New York State or its local governments?"'' }'
C_25='{ doc: ny_it201i, locator: ''p. 8, Line 25, "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25."'' }'
C_34='{ doc: ny_it201i, locator: ''p. 10, Line 34, "You may take either the New York standard deduction or the New York itemized deduction."'' }'
C_53='{ doc: ny_it201i, locator: ''p. 15, Line 53, "Can you claim the New York City unincorporated business tax (UBT) credit, the New York City accumulation distribution credit, or the part-year resident nonrefundable New York City child and dependent care credit?"'' }'
C_59='{ doc: ny_it201i, locator: ''p. 18, Line 59: Sales or use tax, "You must use Form ST-141 to calculate your sales and use tax liability to be reported on this return if any of the following apply:"'' }'
C_67='{ doc: ny_it214i, locator: ''p. 1, Do I qualify for this credit?, "Your federal adjusted gross income was $18,000 or less."'' }'
C_68='{ doc: ny_it201i, locator: ''p. 19, Line 68, "Did you or your spouse or any dependents pay college tuition expenses during 2025?"'' }'
C_72='{ doc: ny_it201i, locator: ''p. 21, Lines 72, 73, and 74, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following:"'' }'
C_75='{ doc: ny_it201i, locator: ''p. 22, Line 75: Total estimated tax payments and amount paid with Form IT-370, "your 2025 estimated tax payments for New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax"'' }'
C_79='{ doc: ny_it201i, locator: ''p. 23, Line 79: Estimated tax, "Enter the amount of overpayment from line 77 that you want applied to your New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax estimated tax for 2026."'' }'
C_82='{ doc: ny_it201i, locator: ''p. 24, Line 82, "If you owe a late filing penalty, late payment penalty, or interest:"'' }'

def test_eq(x, v): return '{ op: test, eq: ["%s", { const: %s }] }'%(x, v)
def choose(guard, then_t, then_f="ny_it201.no"):
    return '{ op: choose, alternatives: [{ guard: %s, then: "%s" }, { guard: %s, then: "%s" }] }'%(test_eq(guard,'true'), then_t, test_eq(guard,'false'), then_f)

# ---- residency: city first; the State question only after a No; active duty from the federal armed-forces answer
rep("      cite: { doc: ny_it201i, locator: 'p. 30, Resident, \"You maintain a permanent place of abode in New York State for substantially all of the tax year and spend 184 days or more in New York State during the tax year\"' }\n    - id: ny_it201.ask.city_resident",
    "      cite: { doc: ny_it201i, locator: 'p. 30, Resident, \"You maintain a permanent place of abode in New York State for substantially all of the tax year and spend 184 days or more in New York State during the tax year\"' }\n      gated_by: ny_it201.state_resident_if_not_city\n    - id: ny_it201.ask.city_resident")
new_top = (
  line("ny_it201.yes","Yes (a helper: always true)",'{ op: test, eq: ["ny_it201.no", { const: false }] }',C_RES,printed='(helper)')
 +line("ny_it201.state_resident_if_not_city","A full-year New York State resident: yes for a full-year New York City resident, otherwise the answer to ny_it201.ask.state_resident",choose("ny_it201.ask.city_resident","ny_it201.yes","ny_it201.ask.state_resident"),C_RES)
 +q("ny_it201.ask.active_duty","On active duty in the armed forces in 2025","At any time in 2025, were you (or, on a joint return, your spouse) on active duty in the U.S. armed forces?",'{ doc: ny_it201i, locator: ''p. 30, Resident, "whether or not you were domiciled in New York State (unless you were in active service in the military)"'' }',"ny_it201.active_duty_if_armed_forces")
 +line("ny_it201.active_duty_if_armed_forces","Active duty in 2025 (asked only when the federal answer says you or your spouse served in the armed forces since 2022; otherwise no)",choose("scope.armed_forces","ny_it201.ask.active_duty"),'{ doc: ny_it201i, locator: ''p. 30, Resident, "whether or not you were domiciled in New York State (unless you were in active service in the military)"'' }')
 +q("ny_it201.ask.moved_in","Moved into New York City on January 1, 2025","Did you (or, on a joint return, your spouse) move into New York City on January 1, 2025?",C_ACC)
 +q("ny_it201.ask.moved_out","Moved out of New York City on January 1, 2026","Did you (or, on a joint return, your spouse) move out of New York City on January 1, 2026?",C_ACC)
 +line("ny_it201.moved","Moved into New York City at the start of 2025 or out of it at the start of 2026",'{ op: test, any: [%s, %s] }'%(test_eq("ny_it201.ask.moved_in","true"),test_eq("ny_it201.ask.moved_out","true")),C_ACC,printed='(helper)')
 +q("ny_it201.ask.bab","Interest from Build America Bonds","Was any of your interest or dividends from Build America Bonds?",C_G,"ny_it201.bab_if_interest")
 +line("ny_it201.bab_if_interest","Build America Bond interest (asked only with interest, dividends, business or partnership income; otherwise no)",choose("ny_it201.has_line28_income","ny_it201.ask.bab"),C_G)
 +q("ny_it201.ask.abroad","Outside the U.S. and filing on the extra time that gives","Were you outside the United States and Puerto Rico on April 15, 2026, and are you using the extra time to file that this gives?",'{ doc: ny_it201i, locator: ''p. 5, Item G, "Enter this code if you qualify for an automatic two-month extension of time to file your federal return because you are out of the country."'' }')
 +q("ny_it201.ask.installment","Asking to pay the tax owed in installments","If you owe New York tax, will you ask to pay it in installments?",'{ doc: ny_it201i, locator: ''p. 5, Item G, "Enter this code if you cannot pay your tax due in full by April 15, 2026, and would like to request an installment payment agreement (IPA)."'' }')
)
rep("    - id: ny_it201.ask.special_code\n", new_top + "    - id: ny_it201.ask.special_code\n")
# special_code: now derived
old_sc = re.search(r"    - id: ny_it201.ask.special_code\n(?:      .*\n)+?(?=    - id: ny_it201.ask.decedent)", s).group(0)
s = s.replace(old_sc, line("ny_it201.ask.special_code","A New York special condition code applies (item G): Build America Bond interest, an extension for being abroad, or a request to pay in installments; the other codes are refused elsewhere",
   '{ op: test, any: [%s, %s, %s] }'%(test_eq("ny_it201.bab_if_interest","true"),test_eq("ny_it201.ask.abroad","true"),test_eq("ny_it201.ask.installment","true")),C_G))
# special accrual gated on a move
rep("      cite: { doc: ny_it201i, locator: 'p. 31, Special accruals, \"you may have to use special accrual rules (see below) to calculate your New York State and New York City personal income tax for 2025\"' }\n    - id: ny_it201.ask.yonkers",
    "      cite: { doc: ny_it201i, locator: 'p. 31, Special accruals, \"you may have to use special accrual rules (see below) to calculate your New York State and New York City personal income tax for 2025\"' }\n      gated_by: ny_it201.gate.special_accrual\n    - id: ny_it201.ask.yonkers")
rep('      expr: { op: test, eq: ["ny_it201.ask.special_accrual", { const: true }] }\n', '      expr: %s\n'%choose("ny_it201.moved","ny_it201.ask.special_accrual"))
# part-year state gate: active duty, or not a full-year State resident
rep('      expr: { op: test, eq: ["ny_it201.ask.state_resident", { const: false }] }\n',
    '      expr: { op: test, any: [%s, %s] }\n'%(test_eq("ny_it201.active_duty_if_armed_forces","true"),test_eq("ny_it201.state_resident_if_not_city","false")))
# decedent told before the special-code entry on line 1 (special_code can wait for the last question of the New York part)
dec = """        - when: ny_it201.gate.decedent
          form: 'A deceased taxpayer''s return'
          remedy: 'Returns for a taxpayer who died are outside this tool.'
          cite: { doc: ny_it201i, locator: 'p. 31, Deceased taxpayers, "the taxpayer’s spouse or personal representative may have to file and sign a return for that taxpayer"' }
"""
rep(dec,"")
rep("        - when: ny_it201.gate.special_code\n", dec+"        - when: ny_it201.gate.special_code\n")
# item C: federal Yes settles it
rep('      expr: { op: copy, from: "ny_it201.ask.item_c" }\n', '      expr: %s\n'%choose("sa.dependent","ny_it201.yes","ny_it201.ask.item_c").replace('then: "ny_it201.yes" }, { guard','then: "ny_it201.yes" }, { guard'))
rep("      cite: { doc: ny_it201i, locator: 'p. 5, Item C, \"If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box.\"' }\n    - id: ny_it201.ask.inflation_check",
    "      cite: { doc: ny_it201i, locator: 'p. 5, Item C, \"If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box.\"' }\n      gated_by: ny_it201.item_c\n    - id: ny_it201.ask.inflation_check")
open(p,'w').write(s)
print("part 1 ok")
