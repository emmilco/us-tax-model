# Data-level properties

The refusal properties of spec 6.3 checked over 400 generated returns with New York answers (fast-check, seed 7, every filing status): a generated federal return and the answers of the New York documents (`generate.ts` `nyReturnArbitrary`), every federal and New York line evaluated. "Applicable" counts the cases where the property's premise held. A failure is reported with the smallest counterexample fast-check found. The branch coverage below is of the New York documents.

| Property | Statement | Cases | Applicable | Result |
| --- | --- | --- | --- | --- |
| refusal_propagates | No line computes a value from an operand that is a refusal; every line evaluated from a refused operand is a refusal. | 400 | 393 | holds |
| refusal_outranks_unknown | On generated returns with up to eight answers removed, every line evaluated from a refused operand is a refusal, whatever its other operands are; in particular an unknown operand does not hide a refused one. A choose whose guard is unknown is a refusal exactly when every way it can still resolve is a refusal, whatever the order of its guards. | 400 | 359 | holds |

## refusal_outranks_unknown

- Cases with a refused operand somewhere: 359; cases with a line that has both a refused and an unknown operand (the order this property guards): 314; cases with a choose stopped at an unknown guard: 400, of which 40 have one refused on every way it can still resolve.

## Branch coverage of the generated corpus

450 of 516 branches (choose guards, Bool lines both ways, floor and positive sides of subtract_floor0, left and right of smaller_of and larger_of) reached by the 400 generated returns. Unreached:

- ny_it201.active_duty_if_armed_forces:true
- ny_it201.use_tax_dmv_only_if_bought:true
- ny_it201.use_tax_not_dmv:false
- ny_it201.gate.part_year_state:true
- ny_it201.gate.spouse_nonresident:true
- ny_it201.gate.special_accrual:true
- ny_it201.gate.line19_gap:true
- ny_it201.gate.line20:true
- ny_it201.public_job_if_w2#1
- ny_it201.gate.line21:true
- ny_it201.has_edu_account:true
- ny_it201.ny_529_if_account#0
- ny_it201.ny_529_if_account:true
- ny_it201.gate.line22#0
- ny_it201.gate.line22:true
- ny_it201.gate.suv_179:true
- ny_it201.alimony_later_if_not_old#1
- ny_it201.alimony_later_if_any#0
- ny_it201.alimony_later_if_any:true
- ny_it201.nyc_flex_if_public:true
- ny_it201.gate.alimony_later:true
- ny_it201.gate.nyc_flex:true
- ny_it201.inflation_if_other_income:true
- ny_it201.gate.line25:true
- ny_it201.no:true
- ny_it201.has_pension_income:true
- ny_it201.gov_pension_candidate:true
- ny_it201.gov_pension_if_income#0
- ny_it201.gov_pension_if_income:true
- ny_it201.gov_said_no:true
- ny_it201.gov_pension_other_if_no#0
- ny_it201.gov_pension_other_if_no:true
- ny_it201.gov_pension_any:true
- ny_it201.gate.line26:true
- ny_it201.pension_59_known:true
- ny_it201.pension_exclusion_if_young#0
- ny_it201.pension_exclusion_after_gov#0
- ny_it201.gate.line29#0
- ny_it201.gate.line29:true
- ny_it201.gate.line30#0
- ny_it201.gate.line30:true
- ny_it201.tcw.mfj#3
- ny_it201.tcw.mfj#4
- ny_it201.tcw.single#2
- ny_it201.tcw.single#3
- ny_it201.tcw.hoh#2
- ny_it201.tcw.hoh#3
- ny_it201.agi_top:true
- ny_it201.tax_high#0
- ny_it201.hh_state_t2#5
- ny_it201.hh_state_t2#6
- ny_it201.hh_city_t5#5
- ny_it201.hh_city_t5#6
- ny_it201.gate.hh_state_over7:true
- ny_it201.gate.hh_city_over7:true
- ny_it201.sut.top:right
- ny_it201.gate.use_tax_abode:true
- ny_it201.gate.use_tax_st141:true
- ny_it201.gate.dependent_care:true
- ny_it201.gate.real_property:true
- ny_it201.gate.college_tuition:true
- ny_it201.gate.other_withholding:true
- ny_it201.apply_if_overpaid:true
- ny_it201.line79_wanted#0
- ny_it201.gate.line79_over:true
- ny_it201.gate.refund_529:true
