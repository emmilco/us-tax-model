# Lane m4: mutation cases for qbi, tipjob and sli, written into fixtures/2025/mutation.json.
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from casegen import load, base_inputs, apply, build, write

MUT = 'fixtures/2025/mutation.json'
data = load(MUT)
classm = load('fixtures/2025/classm.json')
rows = []

QB = base_inputs(classm, 'classm.asset.4')
QSRC = "inputs of classm.asset.4 (a single filer with one Schedule C business, which has qualified business income)"
rows.append({'id': 'mutation.m4.qbi.reit_loss_carryforward', 'covers': ['qbi'],
             'inputs': apply(QB, {'qbi.prior_form': True, 'qbi.reit_loss': True}),
             'predict': {'qbi.eligible': ('refusal', 'qbi.unsupported')},
             'note': f"Mutation fixture (operand.qbi.qbi.unsupported.reit_loss_if_prior_form.any.0.eq.0), {QSRC}, with a 2024 "
                     f"Form 8995 that shows a qualified REIT dividends and PTP (loss) carryforward and no other carryforward "
                     f"($0). Expected value predicted by hand before running the evaluator: a REIT/PTP loss carryforward "
                     f"(Form 8995 (2025), lines 1-17; i8995 pp. 3-4) is outside the tool, so the qualified REIT dividends line "
                     f"is refused (record taken from the evaluator once its gate was confirmed)."})
rows.append({'id': 'mutation.m4.qbi.suspended_losses', 'covers': ['qbi'],
             'inputs': apply(QB, {'qbi.suspended': True}),
             'predict': {'qbi.eligible': ('refusal', 'qbi.unsupported')},
             'note': f"Mutation fixture (operand.qbi.qbi.unsupported.suspended_if_business.any.1.eq.0), {QSRC}, with losses or "
                     f"deductions of the business suspended in an earlier year and allowed in 2025. Expected value predicted "
                     f"by hand before running the evaluator: previously disallowed losses enter qualified business income by "
                     f"the year they arose (i8995 pp. 3-4), which the tool leaves out, so the line is refused (record taken "
                     f"from the evaluator once its gate was confirmed)."})

TB = base_inputs(classm, 'classm.f8959.2')
T1 = 'person[taxpayer].tipjob[tip_1].'
TSRC = ("inputs of classm.f8959.2 (married filing separately, three tipped jobs on Schedule 1-A Part II; the first with "
        "$16,882 of tips)")
for name, field, mid, why in [
        ('service_charge', 'charged', 'charged_if_listed.any.1', "a service charge or automatic gratuity, a negotiated amount or "
         "non-cash tips (i1040gi pp. 101-103, Schedule 1-A, Qualified Tips, Cash tips, 'Paid voluntarily, not subject to "
         "negotiation, and determined by the customer/payor')"),
        ('unlawful_work', 'unlawful', 'unlawful_if_listed.any.2', "work against the law (i1040gi pp. 101-103, 'Tips received "
         "while performing a service that is a felony or misdemeanor under applicable law are not qualified tips')")]:
    rows.append({'id': f'mutation.m4.tipjob.{name}', 'covers': ['tipjob'],
                 'inputs': apply(TB, {T1 + field: True}),
                 'predict': {T1 + 'amount': ('refusal', T1 + 'mixed')},
                 'note': f"Mutation fixture (operand.tipjob.tipjob.mixed.{mid}.eq.0), {TSRC}, with the first job's tips "
                         f"including {why.split(' (')[0]}. Expected value predicted by hand before running the evaluator: "
                         f"such amounts are not qualified tips ({why.split(' (', 1)[1]}, and separating them from the "
                         f"job's other tips is outside the tool, so the job's line 1(b) is refused (record taken from the "
                         f"evaluator once its gate was confirmed)."})

SB = base_inputs(data, 'mutation.t2.sli.qss_divisor')
rows.append({'id': 'mutation.m4.sli.part_unqualified', 'covers': ['sli'],
             'inputs': apply(SB, {'sli.interest': 200000, 'sli.unqualified_any': True, 'sli.unqualified': 50000}),
             'predict': {'sli.line1': 150000},
             'note': "Mutation fixture (operand.sli.sli.qualified.not_counted), inputs of mutation.t2.sli.qss_divisor with "
                     "$2,000 of student loan interest paid, $500 of it on a loan that is not a qualified student loan, and "
                     "none on a loan paid by an employer's assistance. Expected value predicted by hand before running the "
                     "evaluator: only interest on a qualified student loan is deductible (i1040gi pp. 98-99, Qualified "
                     "student loan), so line 1 is the smaller of $1,500 and $2,500, $1,500."})
cases = build(rows)
for prefix in ['qbi', 'tipjob', 'sli']:
    write(MUT, [c for c in cases if c['id'].startswith(f'mutation.m4.{prefix}.')], f'mutation.m4.{prefix}.')

# Schedule 1-A tips of a spouse without a valid SSN for work: the spouse's tip jobs are never asked.
MB = base_inputs(data, 'mutation.t2.mfj_no_overtime_part3')
P = 'person[taxpayer].tipjob['
new_q = {f'{P}{j}].{f}': False for j in ['tip_1', 'tip_2', 'tip_3'] for f in ['other_work', 'charged', 'unlawful']}
spouse_no_ssn = {'person[spouse].work_ssn': False, '$tipjob@person[spouse]': None}
MSRC = ("inputs of mutation.t2.mfj_no_overtime_part3 (married filing jointly, the taxpayer with a valid SSN for work and three "
        "tipped jobs in a listed occupation: $17,185, $18,740 and $3,944 of tips), the three new questions about each job "
        "(other work, service charges, unlawful work) answered No")
tip_rows = [
    {'id': 'mutation.m4.s1a.spouse_no_ssn_three_jobs', 'covers': ['s1a'],
     'inputs': apply(MB, {**new_q, **spouse_no_ssn}),
     'predict': {'s1a.line4c': 3986900},
     'note': f"Mutation fixture (filter.s1a.s1a.tip_total), {MSRC}, and the spouse without a valid SSN for work, so the "
             f"spouse's tipped jobs are not asked. Expected value predicted by hand before running the evaluator: only tips of "
             f"a person with a valid SSN for work count (i1040gi (2025) p. 101, Schedule 1-A, Part II, 'If you are married filing a joint return, the spouse who received the qualified tips must have a valid SSN'); with more than one employer "
             f"line 4c is the total of the taxpayer's tips, $17,185 + $18,740 + $3,944 = $39,869."},
    {'id': 'mutation.m4.s1a.spouse_no_ssn_one_job', 'covers': ['s1a'],
     'inputs': apply(MB, {**new_q, **spouse_no_ssn, '$tipjob@person[taxpayer]': ['tip_1'],
                          **{f'{P}{j}].{f}': None for j in ['tip_2', 'tip_3'] for f in ['listed', 'tips', 'other_work', 'charged', 'unlawful']}}),
     'predict': {'s1a.line4a': 1718500, 's1a.line4c': 1718500},
     'note': f"Mutation fixture (filter.s1a.s1a.tip_reported), {MSRC}, with only the first job ($17,185 of tips) and the "
             f"spouse without a valid SSN for work, so the spouse's tipped jobs are not asked. Expected values predicted by "
             f"hand before running the evaluator: only tips of a person with a valid SSN for work count (i1040gi (2025) p. 101, Schedule "
             f"1-A, Part II, 'If you are married filing a joint return, the spouse who received the qualified tips must have a valid SSN'); with one employer line 4a is the tips reported for it, $17,185, and line 4c the larger "
             f"of lines 4a and 4b ($0), $17,185."},
]
write(MUT, build(tip_rows), 'mutation.m4.s1a.')
