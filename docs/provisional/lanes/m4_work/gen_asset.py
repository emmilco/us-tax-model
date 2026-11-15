# Lane m4: the depreciable asset (asset) mutation cases, written into fixtures/2025/mutation.json.
# Every case starts from the inputs of classm.asset.4 (one business, one research-equipment item costing $37,888,
# 100% business use, placed in service in 2025, no section 179, the full special allowance claimed for the class).
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from casegen import load, base_inputs, apply, build, write

MUT = 'fixtures/2025/mutation.json'
classm = load('fixtures/2025/classm.json')
base = base_inputs(classm, 'classm.asset.4')
A = 'person[taxpayer].sc[biz_a].asset[item_1].'
SRC = ("inputs of classm.asset.4 (one business with one research-equipment item costing $37,888, used 100% for business, "
       "placed in service in 2025, no section 179 deduction, the full special allowance claimed for the class)")
EARLIER = {A + 'use_changed': False, A + 'bonus_choice': None, A + 'bonus_same': None, A + 'after_jan19': None,
           A + 'used_before': None}
rows = [
    {'id': 'mutation.m4.asset.bonus_used_before', 'covers': ['asset'],
     'inputs': apply(base, {A + 'used_before': True}),
     'predict': {A + 'cost': ('refusal', A + 'screened')},
     'note': f"Mutation fixture (operand.asset.asset.claims_bonus.bonus_claimed.then0), {SRC}, with the item used by someone "
             f"before the filer got it. Expected value predicted by hand before running the evaluator: used property "
             f"qualifies for the special allowance only in certain cases (i4562 (2025) p. 6, 'Qualified property can be "
             f"either new property or certain used property'), and the tool screens a used item claiming the allowance "
             f"out, so the item's depreciation is refused at its cost with the screen's record, taken from the evaluator "
             f"once its gate was confirmed."},
    {'id': 'mutation.m4.asset.qip_2016_screen', 'covers': ['asset'],
     'inputs': apply(base, {**EARLIER, A + 'class': 'cqip', A + 'placed': 'y2016'}),
     'predict': {A + 'screen': False, A + 'cost': ('refusal', A + 'screened')},
     'note': f"Mutation fixture (operand.asset.asset.claims_bonus.no.then1), {SRC}, with the item qualified improvement "
             f"property placed in service in 2016, its use unchanged; the special allowance and used-property questions "
             f"concern property placed in service in 2025 and are not asked. Expected values predicted by hand before "
             f"running the evaluator: no screen item applies, so the screen is false; the tool's classification of qualified "
             f"improvement property is that of property 'placed in service by you after December 31, 2017' (i4562 (2025) "
             f"p. 10, Determining the classification), so an item placed in service in 2016 is outside it and the cost is refused "
             f"with the screened record, taken from the evaluator once its gate was confirmed."},
    {'id': 'mutation.m4.asset.fully_recovered_no_179', 'covers': ['asset'],
     'inputs': apply(base, {**EARLIER, A + 'placed': 'y2018'}),
     'predict': {A + 's179_bad': False, A + 'after179': 3788800, A + 'bonus': 0, A + 'macrs_prior': 0},
     'note': f"Mutation fixture (operand.asset.asset.s179_bad.no.then1), {SRC}, with the item placed in service in 2018, "
             f"its use unchanged and no section 179 amount; the special allowance and used-property questions concern "
             f"property placed in service in 2025 and are not asked. Expected values predicted from the archived "
             f"instructions and confirmed with the evaluator: with no section 179 amount there is no election that could "
             f"be more than the business cost, the item is used 100% in the business and is section 179 property, so the "
             f"section 179 gate is false and the basis less the section 179 election is the cost, $37,888 (i4562 (2025) p. 7, "
             f"How to figure the allowance, 'subtract ... Section 179 expense deduction'). The special allowance 'applies "
             f"only for the first year the property is placed in service' (i4562 (2025) p. 5, Line 14), so line 14 is $0. "
             f"5-year property under the half-year convention has six recovery years (Pub. 946 Table A-1), 2018 to 2023, so "
             f"its recovery ended before 2025 and line 17 is $0 (i4562 (2025) p. 9, Line 17). The mutant makes the gate the "
             f"'recovery ended' test where no section 179 amount is elected, so it refuses the basis on this item."},
    {'id': 'mutation.m4.asset.listed_prior_year_line25', 'covers': ['asset'],
     'inputs': apply(base, {**EARLIER, A + 'placed': 'y2023', A + 'listed': True, A + 'prior_conv': 'hy',
                            A + 'prior_179': 0, A + 'prior_bonus': 0}),
     'predict': {A + 'f25': 0, A + 'bonus': 0, A + 'dep_listed': 727450},
     'note': f"Mutation fixture (operand.asset.asset.f25.bonus), {SRC}, with the item listed property placed in service "
             f"in 2023 under the half-year convention, its use unchanged, with no section 179 deduction and no special "
             f"allowance claimed that year; the special allowance and used-property questions concern property placed "
             f"in service in 2025 and are not asked. Expected values predicted from the archived instructions and "
             f"confirmed with the evaluator: line 25 is the special allowance for qualified listed property placed in "
             f"service during the tax year (i4562 (2025) p. 13, Line 25), and the allowance 'applies only for the first "
             f"year the property is placed in service' (p. 5, Line 14), so this item's line 25 and line 14 are $0. Used "
             f"more than 50% for business, its column (h) follows line 19 column (g) (p. 15): 2025 is the third recovery "
             f"year, 19.20% for 5-year property (Pub. 946 Table A-1), of the unadjusted basis $37,888, $7,274.50. The "
             f"mutant takes line 25 from the allowance as elected for the item's class, which reads the special allowance "
             f"question this item is never asked, so its line 25 is unknown."},
]
write(MUT, build(rows), 'mutation.m4.asset.')
