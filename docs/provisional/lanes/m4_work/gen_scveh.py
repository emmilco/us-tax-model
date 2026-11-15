# Lane m4: the business vehicle (scveh) mutation cases, written into fixtures/2025/mutation.json.
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from casegen import load, base_inputs, apply, build, write

MUT = 'fixtures/2025/mutation.json'
data = load(MUT)
classm = load('fixtures/2025/classm.json')
rows = []
V1 = 'person[taxpayer].sc[biz_a].scveh[car_1].'
rows.append({'id': 'mutation.m4.scveh.smr_first_year_not_always', 'covers': ['scveh'],
             'inputs': apply(base_inputs(classm, 'classm.asset.4'), {V1 + 'smr_always': False, V1 + 'smr_first': True}),
             'predict': {V1 + 'line9': 2099790},
             'note': "Mutation fixture (operand.scveh.scveh.smr_ok.smr_first_if_not_always.all.1.any.1.eq.0), inputs of "
                     "classm.asset.4 (a car on the standard mileage rate, 29,997 business miles, no parking or tolls, not a "
                     "fleet) with the standard mileage rate not used in every year of the car's use but used in the first "
                     "year it was used for business. Expected value predicted by hand before running the evaluator: "
                     "i1040sc (2025) p. 6, Line 9: 'You can take the standard mileage rate for 2025 only if you: Owned the "
                     "vehicle and used the standard mileage rate for the first year you placed the vehicle in service', and "
                     "'Multiply the number of business miles driven by 0.70' and 'Add to this amount your parking fees and "
                     "tolls'; its commuting and other miles are not asked on that method. Line 9 of the vehicle is 29,997 "
                     "miles at $0.70, $20,997.90, plus $0 of parking and tolls."})
V2 = 'person[taxpayer].sc[r].scveh[car].'
rows.append({'id': 'mutation.m4.scveh.bonus_used_before', 'covers': ['scveh'],
             'inputs': apply(base_inputs(data, 'mutation.t2.scveh.bonus_mixed_line16'), {V2 + 'bonus_same': True, V2 + 'used_before': True}),
             'predict': {V2 + 'cost': ('refusal', 'person[taxpayer].sc[r].scveh[car].screened')},
             'note': "Mutation fixture (operand.scveh.scveh.claims_bonus_this_year.claims_bonus.then0), inputs of "
                     "mutation.t2.scveh.bonus_mixed_line16 (a car placed in service in 2025, acquired after January 19, 2025, "
                     "used more than 50% for business, the full special allowance claimed) with the same choice for the whole "
                     "class, and the car used by someone before the filer got it. Expected value predicted by hand before "
                     "running the evaluator: a vehicle someone used before is used property, which qualifies for the "
                     "special allowance only in certain cases (i4562 (2025) p. 6, 'Qualified property can be either new "
                     "property or certain used property'; p946 p. 31, 'Original use means the first use to which the property "
                     "is put, whether or not by you'); the tool screens a used vehicle claiming the allowance out, so the "
                     "vehicle's depreciation is refused at its cost (column (d)) with the screen's record, taken from the "
                     "evaluator once its gate was confirmed."})
write(MUT, build(rows), 'mutation.m4.scveh.')
