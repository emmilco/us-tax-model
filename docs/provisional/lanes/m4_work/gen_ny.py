# Lane m4: New York IT-201 mutation cases, written into fixtures/ny/2025/mutation.json.
# Bases are existing cases of that file (each states every input). A base states the answers of every New York question,
# including questions the interview does not ask on that return; a case below leaves such a question unanswered
# (None) where the mutant would ask it. Predictions are by hand from IT-201-I (2025), cited per case, or, for a value the
# change does not touch, the base's own expected value.
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from casegen import load, base_inputs, apply, build, write

MUT = 'fixtures/ny/2025/mutation.json'
data = load(MUT)
B = lambda cid: base_inputs(data, cid)
EXP = {c['id']: c['expect'] for c in data['cases']}
Q = 'ny_it201.ask.'
rows = []


def row(name, mutants, base_id, changes, predict, why):
    rows.append({'id': f'ny.mut.m4.{name}', 'covers': ['ny_it201'], 'inputs': apply(B(base_id), changes), 'predict': predict,
                 'note': f"Mutation fixture ({mutants}), inputs of {base_id} {why}"})


E = 'ny.mut.est.100_8500'
ESRC = "(single, a full-year New York City resident, federal AGI $158,000)"
row('moved_in_accrual', 'operand.ny_it201.ny_it201.moved.moved_in.any.0.eq.0', E,
    {Q + 'moved_in': True, Q + 'special_accrual': True},
    {'ny_it201.line1': ('refusal', 'ny_it201.gate.special_accrual')},
    f"{ESRC} with the filer having moved into New York City on January 1, 2025, and having accrued income. Expected value "
    f"predicted by hand before running the evaluator: such a filer 'may have to use special accrual rules' (IT-201-I p. 31, "
    f"Special accruals), which the tool refuses at line 1 (record taken from the evaluator once its gate was confirmed).")
row('moved_in_no_accrual', 'operand.ny_it201.ny_it201.ask.special_code.bab_if_interest.any.0.eq.0; '
    'operand.ny_it201.ny_it201.ask.special_code.installment.any.2.eq.0', E,
    {Q + 'moved_in': True, Q + 'special_accrual': False},
    {'ny_it201.line1': 15800000},
    f"{ESRC} with the filer having moved into New York City on January 1, 2025, with no accrued income, no Build America "
    f"bond interest, not abroad and not asking for installments (no special condition code, IT-201-I p. 5, Item G). "
    f"Expected value: line 1 is the federal wages, $158,000, as in the base (moving in on January 1 leaves a full-year "
    f"resident with no accrual, IT-201-I p. 31).")
row('no_tax_exempt_interest', 'boundary.ny_it201.ny_it201.has_tax_exempt', E,
    {Q + 'out_of_state_bond_interest': None},
    {'ny_it201.line20': 0},
    f"{ESRC}, with no tax-exempt interest on federal line 2a, so the question about other states' bond interest is not "
    f"asked. Expected value predicted by hand: line 20 is 'interest income from state and local bonds and obligations from states other than New York State' not included in federal income (IT-201-I p. 7, Line 20); with no tax-exempt interest there is none, so line 20 is $0.")
row('balance_due_apply_unasked', 'boundary.ny_it201.ny_it201.has_overpayment', E,
    {Q + 'apply_any': None, 'ny_it201.line79_amount': None},
    {'ny_it201.line79': 0},
    f"{ESRC}, a balance due of $5,790 (line 80) and no overpayment, so the question about applying an overpayment to "
    f"2026 estimated tax is not asked. Expected value predicted by hand: line 79 is 'the amount of overpayment from line 77 that you want applied' to 2026 estimated tax (IT-201-I, Line 79); line 77 is $0, so line 79 is $0.")
row('overpaid_late_installment', 'operand.ny_it201.ny_it201.gate.late.no.then1', 'ny.mut.refuse.est_late_line79', {},
    {'ny_it201.line82': 0},
    "(single, an overpayment, an estimated installment paid late, refused at line 81). Expected value predicted by hand: "
    "line 82 is a late filing penalty, late payment penalty or interest (IT-201-I, Line 82); the return is filed on time with no tax due, so it is $0.")
row('use_tax_exact', 'operand.ny_it201.ny_it201.use_tax_exact_if_small.use_tax_exact.then1; '
    'operand.ny_it201.ny_it201.gate.use_tax_st141.use_tax_exact_if_small.all.1.any.1.eq.0', 'ny.mut.use_tax.10000',
    {Q + 'use_tax_exact': True, Q + 'abode_part_year': False},
    {'ny_it201.line59': ('refusal', 'ny_it201.gate.use_tax_st141')},
    "(single, federal AGI $10,000, owing use tax, no single purchase of $1,000 or more) with the filer asking for the use "
    "tax worked out exactly from purchases, and no part-year abode. Expected value predicted by hand: the tool takes the use tax from New York's chart by income and does not work it out from purchases (IT-201-I, Line 59, Sales or use tax), so line 59 is refused (record taken from the evaluator once its gate was confirmed).")
for status, base_id in [('single', E), ('mfj', 'ny.mut.rs.mfj.b5'), ('hoh', 'ny.mut.rs.hoh.b5'), ('qss', 'ny.mut.hh.qss_15000')]:
    i = {'single': 0, 'mfj': 1, 'hoh': 3, 'qss': 4}[status]
    row(f'ny529_owner_{status}', f'operand.ny_it201.ny_it201.spouse_itemizes_if_mfs.no.then{i}', base_id,
        {'person[taxpayer].x_edu_account': True, Q + 'ny_529': True, Q + '529_owner': True},
        {'ny_it201.line34': EXP[base_id]['ny_it201.line34']['cents']},
        f"(status {status}) with the taxpayer an account owner who contributed to a New York 529 college savings account "
        f"(refused at line 30). Expected value: the filer does not itemize, so line 34 is the New York standard "
        f"deduction for the status (IT-201-I, Line 34, the standard deduction table), the base's own value; the 529 answer "
        f"does not touch it.")
row('mfs_spouse_itemizes', 'operand.ny_it201.ny_it201.spouse_itemizes_if_mfs.spouse_itemizes.then2; '
    'operand.ny_it201.ny_it201.gate.itemize.spouse_itemizes_if_mfs.any.1.eq.0', 'ny.mut.hh.mfs_32001',
    {Q + 'spouse_itemizes': True},
    {'ny_it201.line34': ('refusal', 'ny_it201.gate.itemize')},
    "(married filing separately, federal AGI $32,001) with the spouse itemizing on their own New York return. Expected "
    "value predicted by hand: the tool asks a separate filer whether the spouse itemizes and treats a Yes as itemizing (the choice of IT-201-I p. 10, Line 34, 'You may take either the New York standard deduction or the New York itemized deduction'); New York itemized deductions (Form IT-196, p. 11) are outside the tool, so line 34 is refused (record taken from the evaluator once its gate was confirmed).")
I = 'ny.mut.stc.ira_560000'
ISRC = "(single, federal AGI $560,000 including a $70,000 traditional IRA distribution)"
row('pension_old_other_gov', 'operand.ny_it201.ny_it201.gov_said_no.has_pension_income.all.0.eq.0; '
    'operand.ny_it201.ny_it201.gate.line29.pension_exclusion_after_gov.then0', I,
    {'person[taxpayer].birth_year': 1960, Q + 'gov_pension': False, Q + 'gov_pension_other': True,
     Q + 'pension_exclusion': None},
    {'ny_it201.line29': 0},
    f"{ISRC}, the taxpayer born in 1960, the distribution not from a New York State or local or federal government plan "
    f"but from one of the plans the follow-up names (the MTA, the LIRR, SUNY, CUNY or the State Education Department). "
    f"Expected value predicted by hand: line 29 asks for pension income 'that was not from a New York State or local government pension plan or federal government pension plan' ('If No, go to line 30', IT-201-I p. 9, Line 29); the distribution is from such a plan, so line 29 is $0.")
row('pension_old', 'operand.ny_it201.ny_it201.pension_59_known.pension_59_people.gt.0; '
    'operand.ny_it201.ny_it201.pension_exclusion_line.pension_59_known.any.0.eq.0; '
    'operand.ny_it201.ny_it201.pension_exclusion_after_gov.pension_exclusion_line.then1', I,
    {'person[taxpayer].birth_year': 1960, Q + 'gov_pension': False, Q + 'gov_pension_other': False,
     Q + 'pension_exclusion': None},
    {'ny_it201.line29': ('refusal', 'ny_it201.gate.line29')},
    f"{ISRC}, the taxpayer born in 1960 (59 1/2 before 2025 ends), the distribution from no government plan, so the "
    f"pension exclusion question is not asked (the birth year answers it). Expected value predicted by hand: 'If Yes, and you were 59½ before January 1, 2025, enter the qualifying pension and annuity income' (IT-201-I p. 9, Line 29), which the tool refuses (record taken from the "
    f"evaluator once its gate was confirmed).")
row('pension_young_gov', 'operand.ny_it201.ny_it201.pension_exclusion_after_gov.no.then0; '
    'operand.ny_it201.ny_it201.gov_said_no.gov_pension_if_income.all.1.eq.0', I,
    {Q + 'gov_pension': True, Q + 'gov_pension_other': None, Q + 'pension_exclusion': None},
    {'ny_it201.line29': 0, 'ny_it201.gov_pension_other_if_no': False},
    f"{ISRC}, the taxpayer born in 1980 as in the base, the distribution from a government plan (subtracted on line 26), "
    f"so neither the follow-up about other public plans nor the pension exclusion question is asked. Expected value "
    f"predicted by hand: line 29 takes only pension income 'not from a New York State or local government pension plan or federal government pension plan' (IT-201-I p. 9, Line 29), so line 29 is $0; the follow-up about other public plans, asked only after a No, is false.")
L = 'ny.mut.use_tax.10000'
row('low_income_noncustodial', 'operand.ny_it201.ny_it201.low_income.item_c.all.1.eq.0; '
    'operand.ny_it201.ny_it201.gate.college_tuition.no.then1', L,
    {Q + 'owes_use_tax': False, Q + 'use_tax_exact': None, Q + 'noncustodial': True, Q + 'real_property_credit': True},
    {'ny_it201.line67': ('refusal', 'ny_it201.gate.real_property'), 'ny_it201.line68': 0},
    "(single, federal AGI $10,000, no college tuition paid, not a dependent of another taxpayer) with no use tax owed, "
    "child support paid through a Support Collection Unit, and the filer possibly qualifying for the real property tax "
    "credit. Expected values predicted by hand: the tool asks the real property tax credit screen of a filer with federal AGI of $18,000 or less who is not claimed as a dependent (its low-income test; IT-201-I, Line 67: 'Review the instructions for Form IT-214 ... to see if you qualify') and refuses the credit on a Yes (record taken from the evaluator once its gate was confirmed); with no qualified college tuition, line 68 is $0.")
W = 'person[taxpayer].w2[emp_a].'
row('it270_no_other_payments', 'operand.ny_it201.ny_it201.gate.other_withholding.no.then1', 'ny.mut.it270.93362',
    {W + 'box1': 9336100, W + 'box3': 9336100, W + 'box5': 9336100},
    {'ny_it201.line70a': ('refusal', 'ny_it201.gate.it270'), 'ny_it201.line72': 0},
    "(head of household, one dependent on item H, wages the only income, no New York withholding) with the wages $1 "
    "lower, $93,361, so line 19 is within $5,000 of the highest income threshold of the New York City income tax "
    "elimination credit. Expected values predicted by hand: the credit (IT-201-I p. 21, Line 70a; Form IT-270) is refused "
    "in that range (record taken from the evaluator once its gate was confirmed); with no federal withholding other than "
    "on wages and no other payments, the withholding question for other forms is not asked, and line 72 (New York State "
    "tax withheld) is the IT-2 total, $0.")
S = 'person[taxpayer].w2[emp_a].'
T = 'person[taxpayer].w2[emp_b].'
row('ss_low_ny_agi', 'operand.ny_it201.ny_it201.low_income.fagi_rounded.all.0.le.0', 'ny.mut.stc.ss_255000',
    {S + 'box1': 1750000, S + 'box2': 100000, S + 'box3': 1750000, S + 'box4': 108500, S + 'box5': 1750000,
     S + 'box6': 25375, T + 'box4': 0, T + 'box6': 0, 'ssb.benefits': 2000000, Q + 'real_property_credit': None},
    {'ny_it201.line33': 1750000, 'ny_it201.line67': 0},
    "(single, wages and social security) with wages of $17,500 (Social Security and Medicare tax withheld at 6.2% and "
    "1.45%, a second W-2 with none) and $20,000 of social security benefits. Expected values predicted by hand: half the "
    "benefits plus the wages is $27,500, $2,500 over the $25,000 base, so $1,250 of the benefits is taxable (i1040gi Social "
    "Security Benefits Worksheet) and federal AGI is $18,750; New York subtracts the taxable benefits (IT-201-I, Line 27), "
    "so New York AGI (line 33) is $17,500. The real property tax credit screen is asked only with federal AGI of $18,000 or "
    "less, so it is not asked, and line 67 is $0.")
row('dependent_decedent', 'operand.ny_it201.ny_it201.item_c_if_not_federal.no.then0', E,
    {'sa.dependent': True, Q + 'decedent': True, Q + 'item_c': None},
    {'ny_it201.item_c': True, 'ny_it201.item_c_if_not_federal': False, 'ny_it201.line1': ('refusal', 'ny_it201.gate.decedent')},
    f"{ESRC} with the filer someone else can claim as a dependent on the federal return, and the return filed for a "
    f"deceased taxpayer. Expected values predicted by hand: item C is marked Yes for a filer who 'can be claimed as a "
    f"dependent on another taxpayer's federal return' (IT-201-I, Item C), so the separate New York item C question is "
    f"not asked and is false; a deceased taxpayer's return is outside the tool, so line 1 is refused (record taken from "
    f"the evaluator once its gate was confirmed).")
row('use_tax_st141_abode', 'operand.ny_it201.ny_it201.use_tax_exact_if_small.no.then0', 'ny.mut.use_tax.10000',
    {Q + 'use_tax_st141': True, Q + 'abode_part_year': True, Q + 'use_tax_exact': None},
    {'ny_it201.use_tax_exact_if_small': False, 'ny_it201.line59': ('refusal', 'ny_it201.gate.use_tax_abode')},
    "(single, federal AGI $10,000, owing use tax) with a purchase of $1,000 or more (Form ST-141) and an abode in New York "
    "for only part of the year. Expected values predicted by hand: with a purchase that large the use tax chart cannot be "
    "used (IT-201-I, Line 59), so the question about working it out exactly is not asked and is false; the part-year "
    "abode is refused first on line 59 (record taken from the evaluator once its gate was confirmed).")
write(MUT, build(rows, ny=True), 'ny.mut.m4.')
