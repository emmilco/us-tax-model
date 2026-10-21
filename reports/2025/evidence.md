# Evidence coverage per line

Fixtures that assert each line, by evidence class. A — official IRS example. B — human hand-work (pending; marked where recorded). C — recorded value also confirmed by the independently written Lean reference evaluator (running evaluator agreement, reports/2025/evaluator_agreement.md); the external-calculator comparison is the Stage 5 differential and remains pending. M — an isolated model worked the document by hand from its archived pages and the amounts flowing into it (reviews/2025/classm/). R — recorded synthetic regression, no class claimed, human review pending.

## Form 4562 — one item of depreciable property (other than a vehicle) of a business

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| asset.zero | — | — | — | — |
| asset.class | — | — | — | — |
| asset.period | — | — | — | 4 |
| asset.outside | — | — | — | 4 |
| asset.screen | — | — | — | — |
| asset.screened | — | — | — | 4 |
| asset.placed | — | — | — | — |
| asset.cost | — | — | — | 1 (stage14.asset.refuse_class) |
| asset.pct | — | — | — | — |
| asset.cent | — | — | — | — |
| asset.hundred | — | — | — | — |
| asset.pct_c | — | — | — | — |
| asset.pct_bad | — | — | — | 4 |
| asset.listed | — | — | — | — |
| asset.half | — | — | — | — |
| asset.over_half | — | — | — | 4 |
| asset.listed_low | — | — | — | 4 |
| asset.basis | — | — | — | 7 |
| asset.is2025 | — | — | — | 4 |
| asset.on_19 | — | — | — | 4 |
| asset.on_17 | — | — | — | 4 |
| asset.on_26_2025 | — | — | — | 4 |
| asset.year | — | — | — | 4 |
| asset.last | — | — | — | 4 |
| asset.done | — | — | — | 4 |
| asset.quarter | — | — | — | — |
| asset.qconv | — | — | — | 4 |
| asset.s179 | — | — | — | — |
| asset.s179_bad | — | — | — | 4 |
| asset.after179 | — | — | — | 7 |
| asset.after_jan19 | — | — | — | — |
| asset.bonus_choice | — | — | — | — |
| asset.bonus_same | — | — | — | — |
| asset.bonus_mixed | — | — | — | 4 |
| asset.rate40 | — | — | — | — |
| asset.bonus_full | — | — | — | 4 |
| asset.bonus_forty | — | — | — | 4 |
| asset.bonus_fullcase | — | — | — | 3 |
| asset.bonus | — | — | — | 7 |
| asset.f25 | — | — | — | 3 |
| asset.f26i | — | — | — | 2 (classm.asset.2, stage14.asset.listed_and_not) |
| asset.ub | — | — | — | 4 |
| asset.col19c | — | — | — | 4 |
| asset.hy | — | — | — | — |
| asset.rate_hy | — | — | — | 3 |
| asset.rate_mq | — | — | — | 3 |
| asset.macrs_hy | — | — | — | 3 |
| asset.macrs_mq | — | — | — | 3 |
| asset.macrs2025 | — | — | — | 16 |
| asset.mqbase | — | — | — | 4 |
| asset.mq_q4_2025 | — | — | — | 4 |
| asset.prior_conv | — | — | — | — |
| asset.prior_179 | — | — | — | — |
| asset.prior_bonus | — | — | — | — |
| asset.ub_prior_a | — | — | — | 5 |
| asset.ub_prior | — | — | — | 5 |
| asset.rate_prior | — | — | — | 4 |
| asset.macrs_prior_live | — | — | — | 4 |
| asset.macrs_prior | — | — | — | 9 |
| asset.dep_2025 | — | — | — | 4 |
| asset.bonus_2025 | — | — | — | 4 |
| asset.s179_2025 | — | — | — | 4 |
| asset.mq_q4 | — | — | — | 4 |
| asset.mq_total | — | — | — | 4 |
| asset.cost179 | — | — | — | 4 |
| asset.cost179_2025 | — | — | — | 3 |
| asset.dep_prior | — | — | — | 4 |
| asset.dep_listed | — | — | — | 3 |

Unasserted lines: asset.zero, asset.cent, asset.hundred, asset.pct_c, asset.half, asset.rate40, asset.hy

## Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| carloan.zero | — | — | — | — |
| carloan.kind | — | — | — | — |
| carloan.requirements | — | — | — | — |
| carloan.vehicle | — | — | — | — |
| carloan.eligible | — | — | — | 4 |
| carloan.interest | — | — | — | — |
| carloan.mixed | — | — | — | — |
| carloan.financed | — | — | — | — |
| carloan.nonqualifying | — | — | — | — |
| carloan.down | — | — | — | — |
| carloan.nonqualifying_debt | — | — | — | 2 (classm.carloan.1, classm.carloan.4) |
| carloan.mixed_qualifying | — | — | — | 2 (classm.carloan.1, classm.carloan.4) |
| carloan.refi_balance | — | — | — | — |
| carloan.refi_whole | — | — | — | — |
| carloan.refi_qualifying | — | — | — | 2 (classm.carloan.1, classm.carloan.3) |
| carloan.refi_nested | — | — | — | 2 (classm.carloan.1, classm.carloan.3) |
| carloan.allocated | — | — | — | 4 |
| carloan.refi_interest | — | — | — | 2 (classm.carloan.1, classm.carloan.3) |
| carloan.mixed_interest | — | — | — | 3 |
| carloan.mixed_prorated | — | — | — | 2 (classm.carloan.1, classm.carloan.4) |
| carloan.qpvli | — | — | — | — |
| carloan.col_ii_input | — | — | — | — |
| carloan.col_ii | — | — | — | — |
| carloan.col_iii | — | — | — | 4 |

Unasserted lines: carloan.zero, carloan.qpvli, carloan.col_ii

## Dependents — qualifying child and qualifying relative tests, per person listed

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| dependent.relationship | — | — | — | — |
| dependent.age | — | — | — | — |
| dependent.student | — | — | — | — |
| dependent.disabled | — | — | — | — |
| dependent.months | — | — | — | — |
| dependent.self_support | — | — | — | — |
| dependent.joint_return | — | — | — | — |
| dependent.citizen | — | — | — | — |
| dependent.canada_mexico | — | — | — | — |
| dependent.married | — | — | — | — |
| dependent.tin | — | — | — | — |
| dependent.work_ssn | — | — | — | — |
| dependent.gross_income | — | — | — | — |
| dependent.supported | — | — | — | — |
| dependent.other_claimant | — | — | — | — |
| dependent.divorced_rule | — | — | — | — |
| dependent.multiple_support | — | — | — | — |
| dependent.parent_home_paid | — | — | — | — |
| dependent.one | — | — | — | — |
| dependent.zero | — | — | — | — |
| dependent.qc_relationship | — | — | — | 24 |
| dependent.younger | — | — | — | 18 |
| dependent.us_half | — | — | — | — |
| dependent.eic_ssn | — | — | — | — |
| dependent.qc_age | — | — | — | 21 |
| dependent.lived_half | — | — | — | 22 |
| dependent.qualifying_child | — | — | — | 27 |
| dependent.resident | — | — | — | 22 |
| dependent.qc_dependent | — | — | — | 27 |
| dependent.qr_relationship | — | — | — | 9 |
| dependent.qr_income | — | — | — | 9 |
| dependent.income_exception | — | — | — | 10 |
| dependent.qualifying_relative | — | — | — | 11 |
| dependent.qr_dependent | — | — | — | 11 |
| dependent.claimed | — | — | — | 27 |
| dependent.under_ctc_age | — | — | — | 18 |
| dependent.ctc_child | — | — | — | 27 |
| dependent.odc_person | — | — | — | 27 |
| dependent.ctc_per_child | — | — | — | — |
| dependent.ctc_amount | — | — | — | 27 |
| dependent.odc_per_dependent | — | — | — | — |
| dependent.odc_amount | — | — | — | 27 |
| dependent.actc_per_child | — | — | — | — |
| dependent.actc_amount | — | — | — | 27 |
| dependent.hoh_test2 | — | — | — | 27 |
| dependent.hoh_test1 | — | — | — | 27 |
| dependent.eic_child | — | — | — | 3 |
| dependent.eic_ssn_child | — | — | — | 3 |

Unasserted lines: dependent.one, dependent.zero, dependent.ctc_per_child, dependent.odc_per_dependent, dependent.actc_per_child

## Form 1099-DIV — distribution components and scope screening

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| div.box2b | — | — | — | — |
| div.box2c | — | — | — | — |
| div.box2d | — | — | — | — |
| div.box2e | — | — | — | — |
| div.box2f | — | — | — | — |
| div.box3 | — | — | — | — |
| div.box9 | — | — | — | — |
| div.box10 | — | — | — | — |
| div.box12 | — | — | — | — |
| div.box13 | — | — | — | — |
| div.basis_reconciled | — | — | — | — |
| div.box1a | — | — | — | — |
| div.box1b | — | — | — | — |
| div.box2a | — | — | — | — |
| div.box5 | — | — | — | — |
| div.section1202 | — | — | — | — |
| div.amt | — | — | — | — |
| div.unsupported | — | — | — | — |
| div.bad_special | — | — | — | — |
| div.screen | — | — | — | — |
| div.bad_components | — | — | — | — |
| div.special_total | — | — | — | — |

Unasserted lines: div.box1a, div.box1b, div.box2a, div.box5, div.section1202, div.amt, div.unsupported, div.bad_special, div.screen, div.bad_components, div.special_total

## Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| eic.qc_of_another | — | — | — | — |
| eic.age_range_count | — | — | — | — |
| eic.age_range | — | — | — | 1 (stage13.eic_spouse_in_age_range) |
| eic.us_home | — | — | — | — |
| eic.married | — | — | — | — |
| eic.zero | — | — | — | — |
| eic.qc_count | — | — | — | — |
| eic.ssn_count | — | — | — | 3 |
| eic.has_qc | — | — | — | 2 (stage9.eic.child_without_ssn, stage9.eic.parent_not_qualifying_child) |
| eic.married_rules | — | — | — | — |
| eic.top_limit | — | — | — | — |
| eic.below_top | — | — | — | — |
| eic.limit0_other | — | — | — | — |
| eic.limit1_other | — | — | — | — |
| eic.limit2_other | — | — | — | — |
| eic.limit3_other | — | — | — | — |
| eic.limit0_joint | — | — | — | — |
| eic.limit1_joint | — | — | — | — |
| eic.limit2_joint | — | — | — | — |
| eic.limit3_joint | — | — | — | — |
| eic.limit_other | — | — | — | — |
| eic.limit_joint | — | — | — | — |
| eic.limit | — | — | — | — |
| eic.step1_income | — | — | — | — |
| eic.step1_ssn | — | — | — | — |
| eic.step1_foreign | — | — | — | — |
| eic.step1_resident | — | — | — | — |
| eic.gain_7a | — | — | — | 1 (stage9.eic.capital_gain_in_investment_income) |
| eic.investment_income | — | — | — | — |
| eic.step2_income | — | — | — | 3 |
| eic.step2_other | — | — | — | — |
| eic.same_home | — | — | — | — |
| eic.legally_separated | — | — | — | — |
| eic.step3_married | — | — | — | 3 |
| eic.step3 | — | — | — | — |
| eic.step4 | — | — | — | 2 (stage9.eic.no_child.over65, stage9.eic.no_child.born_jan1_1961) |
| eic.step34 | — | — | — | — |
| eic.step5_line1 | — | — | — | — |
| eic.step5_line2 | — | — | — | — |
| eic.step5_line3 | — | — | — | — |
| eic.step5_line4 | — | — | — | — |
| eic.earned_income | — | — | — | — |
| eic.sc_count | — | — | — | — |
| eic.self_employed | — | — | — | — |
| eic.wsb_se | — | — | — | — |
| eic.wsb_4b | — | — | — | 5 |
| eic.wsb_6 | — | — | — | 1 (stage14.eic.wsb_stop_27c) |
| eic.earned_for_limit | — | — | — | — |
| eic.step5_income | — | — | — | — |
| eic.eligible | — | — | — | 20 |
| eic.line1 | — | — | — | 11 |
| eic.line1_in_table | — | — | — | — |
| eic.line1_table0 | — | — | — | — |
| eic.line1_table1 | — | — | — | — |
| eic.line1_table2 | — | — | — | — |
| eic.line1_table3 | — | — | — | — |
| eic.line1_table | — | — | — | — |
| eic.line2 | — | — | — | 22 |
| eic.line3 | — | — | — | 2 (classm.eic.1, classm.eic.7) |
| eic.line4 | — | — | — | 11 |
| eic.threshold_other | — | — | — | — |
| eic.threshold_joint | — | — | — | — |
| eic.line5_threshold | — | — | — | — |
| eic.threshold0_other | — | — | — | — |
| eic.threshold1_other | — | — | — | — |
| eic.threshold0_joint | — | — | — | — |
| eic.threshold1_joint | — | — | — | — |
| eic.line5_blank | — | — | — | 1 (stage9.eic.one_child.at_line5_amount) |
| eic.line3_table0 | — | — | — | — |
| eic.line3_table1 | — | — | — | — |
| eic.line3_table2 | — | — | — | — |
| eic.line3_table3 | — | — | — | — |
| eic.line5 | — | — | — | 6 |
| eic.smaller | — | — | — | — |
| eic.after_line4 | — | — | — | — |
| eic.line6 | — | — | — | 16 |
| eic.credit | — | — | — | — |
| eic.reached_step3 | — | — | — | — |
| eic.check_27c | — | — | — | 2 (stage14.eic.wsb_stop_27c, stage14.eic.wsb_line5_stop_27c) |
| eic.wsb_4b_positive | — | — | — | — |
| eic.wsb_line5_stop | — | — | — | 1 (stage14.eic.wsb_line5_stop_27c) |
| eic.separated_box | — | — | — | — |
| eic.clergy | — | — | — | — |

Unasserted lines: eic.age_range_count, eic.zero, eic.qc_count, eic.married_rules, eic.top_limit, eic.below_top, eic.limit0_other, eic.limit1_other, eic.limit2_other, eic.limit3_other, eic.limit0_joint, eic.limit1_joint, eic.limit2_joint, eic.limit3_joint, eic.limit_other, eic.limit_joint, eic.limit, eic.step1_income, eic.step1_ssn, eic.step1_foreign, eic.step1_resident, eic.investment_income, eic.step2_other, eic.step3, eic.step34, eic.step5_line1, eic.step5_line2, eic.step5_line3, eic.step5_line4, eic.earned_income, eic.sc_count, eic.self_employed, eic.wsb_se, eic.earned_for_limit, eic.step5_income, eic.line1_in_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line1_table, eic.threshold_other, eic.threshold_joint, eic.line5_threshold, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.smaller, eic.after_line4, eic.credit, eic.reached_step3, eic.wsb_4b_positive, eic.separated_box, eic.clergy

## Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f1040.status | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| f1040.line1a | — | — | — | 10 |
| f1040.line1z | — | — | — | 7 |
| f1040.tax_exempt_interest | — | — | — | — |
| f1040.line2a | — | — | — | 5 |
| f1040.line2b | — | — | — | 7 |
| f1040.line3b | — | — | — | 7 |
| f1040.line3a | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| f1040.line4a | — | — | — | 8 |
| f1040.line4b | — | — | — | 12 |
| f1040.ira_rollovers | — | — | — | — |
| f1040.line4c_rollover | — | — | — | 10 |
| f1040.line5a | — | — | — | 15 |
| f1040.line5b | — | — | — | 19 |
| f1040.plan_rollovers | — | — | — | — |
| f1040.line5c_rollover | — | — | — | 9 |
| f1040.line6a | — | — | — | 5 |
| f1040.line6b | — | — | — | 20 |
| f1040.line6c | — | — | — | 5 |
| f1040.line6d | — | — | — | 6 |
| f1040.line7a | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 66 |
| f1040.line8 | — | — | — | 12 |
| f1040.line9 | — | — | — | 13 |
| f1040.line10 | — | — | — | 17 |
| f1040.line11a | — | — | — | 12 |
| f1040.line11b | — | — | — | 30 |
| f1040.line12e | — | — | — | 32 |
| f1040.line13a | — | — | — | 9 |
| f1040.line13b | — | — | — | 15 |
| f1040.line14 | — | — | — | 14 |
| f1040.line15 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 14 |
| f1040.gate.qdcg_applies | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 7 |
| f1040.gate.sdtw | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| f1040.line16 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 16 |
| f1040.line17 | — | — | — | 9 |
| f1040.line18 | — | — | — | 9 |
| f1040.line19 | — | — | — | 32 |
| f1040.line20 | — | — | — | 7 |
| f1040.line21 | — | — | — | 8 |
| f1040.line22 | — | — | — | 8 |
| f1040.line23 | — | — | — | 7 |
| f1040.line24 | — | — | — | 8 |
| f1040.line25a | — | — | — | 7 |
| f1040.line25b | — | — | — | 3 |
| f1040.line25c | — | — | — | 3 |
| f1040.line25d | — | — | — | 7 |
| f1040.line26 | — | — | — | 3 |
| f1040.line27a | — | — | — | 57 |
| f1040.line27b | — | — | — | 6 |
| f1040.line27c | — | — | — | 14 |
| f1040.separated_spouses | — | — | — | 8 |
| f1040.line28 | — | — | — | 33 |
| f1040.line29 | — | — | — | 7 |
| f1040.line30 | — | — | — | 7 |
| f1040.line31 | — | — | — | 28 |
| f1040.line32 | — | — | — | 8 |
| f1040.line33 | — | — | — | 23 |
| f1040.line34 | — | — | — | 46 |
| f1040.line35a | — | — | — | 3 |
| f1040.line36 | — | — | — | 3 |
| f1040.line37 | — | — | — | 47 |

Unasserted lines: f1040.ira_rollovers, f1040.plan_rollovers

## Form 4562 — Depreciation and Amortization, one per business

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f4562.line12 | — | — | — | 1 (classm.f4562.1) |
| f4562.line14 | — | — | — | 1 (classm.f4562.1) |
| f4562.line17 | — | — | — | 1 (classm.f4562.1) |
| f4562.line19a | — | — | — | 1 (classm.f4562.1) |
| f4562.line19b | — | — | — | 1 (classm.f4562.1) |
| f4562.line19c | — | — | — | 1 (classm.f4562.1) |
| f4562.line19d | — | — | — | 1 (classm.f4562.1) |
| f4562.line19f | — | — | — | 1 (classm.f4562.1) |
| f4562.line19e | — | — | — | 1 (classm.f4562.1) |
| f4562.line21 | — | — | — | 1 (classm.f4562.1) |
| f4562.line22 | — | — | — | 1 (classm.f4562.1) |
| f4562.line25 | — | — | — | 1 (classm.f4562.1) |
| f4562.line26h | — | — | — | 1 (classm.f4562.1) |
| f4562.line28 | — | — | — | 1 (classm.f4562.1) |
| f4562.line29 | — | — | — | 1 (classm.f4562.1) |

## Form 4952 — supported investment-interest deduction and election

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f4952.line1 | — | — | — | — |
| f4952.carryover | — | — | — | — |
| f4952.unsupported | — | — | — | — |
| f4952.alternative_allocation | — | — | — | — |
| f4952.line4a | — | — | — | 3 |
| f4952.line4g | — | — | — | — |
| f4952.zero | — | — | — | — |
| f4952.line2 | — | — | — | 7 |
| f4952.line3 | — | — | — | 3 |
| f4952.line4b | — | — | — | 3 |
| f4952.bad_dividends | — | — | — | — |
| f4952.line4c | — | — | — | 3 |
| f4952.line4d | — | — | — | 4 |
| f4952.line4e | — | — | — | 4 |
| f4952.line4f | — | — | — | 4 |
| f4952.election_limit | — | — | — | 1 (stage4.interest.short_term) |
| f4952.bad_election | — | — | — | — |
| f4952.election | — | — | — | 5 |
| f4952.line4h | — | — | — | 3 |
| f4952.line5 | — | — | — | 7 |
| f4952.line6 | — | — | — | 3 |
| f4952.line7 | — | — | — | 6 |
| f4952.line8 | — | — | — | 11 |
| f4952.exception | — | — | — | — |
| f4952.required | — | — | — | 7 |

Unasserted lines: f4952.zero, f4952.bad_dividends, f4952.bad_election, f4952.exception

## Form 8889 — HSA contributions and deduction (Part I)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8889.one | — | — | — | — |
| f8889.zero | — | — | — | — |
| f8889.line2 | — | — | — | — |
| f8889.line9 | — | — | — | — |
| f8889.any | — | — | — | 3 |
| f8889.unsupported | — | — | — | — |
| f8889.mfs | — | — | — | 3 |
| f8889.months_eligible | — | — | — | — |
| f8889.months_family | — | — | — | — |
| f8889.bad_months | — | — | — | 3 |
| f8889.age55 | — | — | — | — |
| f8889.twelve | — | — | — | — |
| f8889.married_family | — | — | — | 3 |
| f8889.age55_line3 | — | — | — | 3 |
| f8889.self_amount | — | — | — | 3 |
| f8889.self_under55 | — | — | — | — |
| f8889.self_55 | — | — | — | — |
| f8889.age55_unmarried | — | — | — | — |
| f8889.family_amount | — | — | — | 3 |
| f8889.family_under55 | — | — | — | — |
| f8889.family_55 | — | — | — | — |
| f8889.family_extra | — | — | — | 3 |
| f8889.chart_self | — | — | — | 3 |
| f8889.chart_family | — | — | — | 3 |
| f8889.chart_total | — | — | — | 3 |
| f8889.chart_limit | — | — | — | 3 |
| f8889.all_year | — | — | — | 3 |
| f8889.changed | — | — | — | 3 |
| f8889.dec_coverage | — | — | — | — |
| f8889.dec_amount | — | — | — | 3 |
| f8889.last_month | — | — | — | — |
| f8889.use_last_month | — | — | — | 3 |
| f8889.line3_changed | — | — | — | 3 |
| f8889.line3_all_year | — | — | — | 3 |
| f8889.line3_last_month | — | — | — | 1 (classm.f8889.1) |
| f8889.line3_part_year | — | — | — | 3 |
| f8889.line3 | — | — | — | 13 |
| f8889.line4 | — | — | — | 3 |
| f8889.line5 | — | — | — | 3 |
| f8889.family_year | — | — | — | 3 |
| f8889.family_dec_year | — | — | — | 3 |
| f8889.family_counted | — | — | — | 3 |
| f8889.step1_total | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.step1_line3 | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.step1 | — | — | — | 5 |
| f8889.step1_x2 | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.two | — | — | — | — |
| f8889.share_equal | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.allocation | — | — | — | — |
| f8889.allocated | — | — | — | — |
| f8889.share_raw | — | — | — | 1 (classm.f8889.2) |
| f8889.allocation_bad | — | — | — | 2 (classm.f8889.2, classm.f8889.3) |
| f8889.share | — | — | — | 3 |
| f8889.self_year | — | — | — | 3 |
| f8889.self_counted | — | — | — | 3 |
| f8889.self_all | — | — | — | 3 |
| f8889.self_family_months | — | — | — | 3 |
| f8889.self_dec_year | — | — | — | 3 |
| f8889.self_in_family | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.step4_total | — | — | — | 2 (classm.f8889.1, classm.f8889.2) |
| f8889.step4 | — | — | — | 4 |
| f8889.line6_split | — | — | — | 1 (classm.f8889.2) |
| f8889.split | — | — | — | 3 |
| f8889.line6 | — | — | — | 11 |
| f8889.additional | — | — | — | — |
| f8889.line7_year | — | — | — | 3 |
| f8889.line7_counted | — | — | — | 3 |
| f8889.line7_total | — | — | — | 3 |
| f8889.line7_worksheet | — | — | — | 3 |
| f8889.line7_applies | — | — | — | 3 |
| f8889.line7 | — | — | — | 6 |
| f8889.line8 | — | — | — | 5 |
| f8889.line10 | — | — | — | 3 |
| f8889.line11 | — | — | — | 3 |
| f8889.line12 | — | — | — | 5 |
| f8889.excess | — | — | — | 3 |
| f8889.line13_figured | — | — | — | 3 |
| f8889.line13 | — | — | — | 16 |

Unasserted lines: f8889.one, f8889.zero, f8889.twelve, f8889.self_under55, f8889.self_55, f8889.age55_unmarried, f8889.family_under55, f8889.family_55, f8889.two, f8889.additional

## Form 8959 — Additional Medicare Tax on wages and self-employment income

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8959.unsupported | — | — | — | — |
| f8959.zero | — | — | — | — |
| f8959.line1 | — | — | — | 5 |
| f8959.line2 | — | — | — | 4 |
| f8959.line3 | — | — | — | 4 |
| f8959.line8 | — | — | — | 7 |
| f8959.line14 | — | — | — | 4 |
| f8959.line23 | — | — | — | 4 |
| f8959.line4 | — | — | — | 3 |
| f8959.line5 | — | — | — | 3 |
| f8959.line6 | 1 (stage4.official.medicare_example5) | — | — | 19 |
| f8959.line7 | — | — | — | 5 |
| f8959.line9 | — | — | — | 2 (classm.f8959.2, stage4.medicare.withholding) |
| f8959.line10 | — | — | — | 3 |
| f8959.line11 | — | — | — | 2 (classm.f8959.2, stage4.medicare.withholding) |
| f8959.line12 | — | — | — | 4 |
| f8959.line13 | — | — | — | 4 |
| f8959.line15 | — | — | — | 2 (classm.f8959.2, stage4.medicare.withholding) |
| f8959.line16 | — | — | — | 3 |
| f8959.line17 | — | — | — | 3 |
| f8959.line18 | — | — | — | 22 |
| f8959.line19 | — | — | — | 4 |
| f8959.line20 | — | — | — | 3 |
| f8959.line21 | — | — | — | 3 |
| f8959.line22 | — | — | — | 3 |
| f8959.line24 | — | — | — | 6 |

Unasserted lines: f8959.zero

## Form 8960 — wage, interest, dividend and securities slice

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8960.unsupported | — | — | — | — |
| f8960.refund | — | — | — | — |
| f8960.allocated_taxes | — | — | — | — |
| f8960.zero | — | — | — | — |
| f8960.line1 | — | — | — | 6 |
| f8960.line2 | — | — | — | 3 |
| f8960.line3 | — | — | — | 6 |
| f8960.line4a | — | — | — | 6 |
| f8960.line4b | — | — | — | 6 |
| f8960.line5b | — | — | — | 6 |
| f8960.line5c | — | — | — | 6 |
| f8960.line6 | — | — | — | 6 |
| f8960.line7 | — | — | — | 6 |
| f8960.line9c | — | — | — | 6 |
| f8960.line10 | — | — | — | 6 |
| f8960.line4c | — | — | — | 3 |
| f8960.line5a | — | — | — | 4 |
| f8960.line5d | — | — | — | 3 |
| f8960.line8 | — | — | — | 5 |
| f8960.line9a | — | — | — | 6 |
| f8960.line9b | — | — | — | 6 |
| f8960.line9d | — | — | — | 4 |
| f8960.line11 | — | — | — | 4 |
| f8960.line12 | — | — | — | 6 |
| f8960.line13 | — | — | — | 6 |
| f8960.line14 | — | — | — | 3 |
| f8960.line15 | — | — | — | 3 |
| f8960.line16 | — | — | — | 3 |
| f8960.line17 | — | — | — | 22 |
| f8960.bad_allocation | — | — | — | — |

Unasserted lines: f8960.zero, f8960.bad_allocation

## Form 8995 — Qualified Business Income Deduction Simplified Computation

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | 5 |
| f8995.line3 | — | — | — | 3 |
| f8995.line4_sum | — | — | — | — |
| f8995.line4 | — | — | — | 4 |
| f8995.line5 | — | — | — | 4 |
| f8995.line7 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.loss | — | — | — | — |
| f8995.line16 | — | — | — | 3 |
| f8995.line17 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line6 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line8 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line9 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line10 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line11 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line12 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line13 | — | — | — | 2 (classm.f8995.1, classm.f8995.2) |
| f8995.line14 | — | — | — | 3 |
| f8995.line15 | — | — | — | 10 |

Unasserted lines: f8995.line4_sum, f8995.loss

## Form 8995-A — Part IV dividend-only computation

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8995a.line27 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line29 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line38 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line40 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line28 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line30 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line31 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line32 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line33 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line34 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line35 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line36 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line37 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) |
| f8995a.line39 | — | — | — | 8 |

## Foreign tax credit — election without Form 1116

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| ftc.taxes | — | — | — | — |
| ftc.all_passive | — | — | — | — |
| ftc.statements | — | — | — | — |
| ftc.eligible | — | — | — | — |
| ftc.elect | — | — | — | — |
| ftc.limit | — | — | — | — |
| ftc.zero | — | — | — | — |
| ftc.has_tax | — | — | — | 1 (stage4.base) |
| ftc.needs1116 | — | — | — | — |
| ftc.limited | — | — | — | — |
| ftc.credit | — | — | — | 9 |

Unasserted lines: ftc.limit, ftc.zero, ftc.needs1116, ftc.limited

## 28% Rate Gain Worksheet — distribution-only path

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| g28.line1 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.line2 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.line3 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.line5 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.line4 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.line6 | — | — | — | 2 (classm.g28.1, classm.g28.2) |
| g28.combined | — | — | — | — |
| g28.line7 | — | — | — | 3 |

Unasserted lines: g28.combined

## Form 8283 — groups of similar noncash property

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| gift.deduction | — | — | — | — |
| gift.public_securities | — | — | — | — |
| gift.special | — | — | — | — |
| gift.section_b | — | — | — | 1 (classm.gift.1) |
| gift.allowed | — | — | — | 1 (classm.gift.1) |

## Household facts for dependents and head of household

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| household.persons | — | — | — | — |
| household.taxpayers | — | — | — | — |
| household.spouses | — | — | — | — |
| household.roster_ok | — | — | — | — |
| household.roster_bad | — | — | — | — |
| household.hsa_people | — | — | — | — |
| household.hsa_both | — | — | — | — |
| household.hsa_split_count | — | — | — | — |
| household.hsa_agreed_count | — | — | — | — |
| household.hsa_step1_sum | — | — | — | — |
| household.hsa_share_sum | — | — | — | — |
| household.work_ssn_count | — | — | — | — |
| household.any_work_ssn | — | — | — | — |
| household.all_work_ssn | — | — | — | — |
| household.tin_count | — | — | — | — |
| household.all_tin | — | — | — | — |
| household.id_count | — | — | — | — |
| household.ctc_ssn | — | — | — | — |
| household.taxpayer_work_ssn_count | — | — | — | — |
| household.taxpayer_work_ssn | — | — | — | — |
| household.home_cost | — | — | — | — |
| household.unmarried | — | — | — | — |
| household.test1_persons | — | — | — | 24 |
| household.test2_persons | — | — | — | 24 |
| household.test1_met | — | — | — | 24 |
| household.test2_met | — | — | — | 24 |
| household.hoh_eligible | — | — | — | 24 |
| household.hoh_fails | — | — | — | 24 |

Unasserted lines: household.persons, household.taxpayers, household.spouses, household.roster_ok, household.roster_bad, household.hsa_people, household.hsa_both, household.hsa_split_count, household.hsa_agreed_count, household.hsa_step1_sum, household.hsa_share_sum, household.work_ssn_count, household.any_work_ssn, household.all_work_ssn, household.tin_count, household.all_tin, household.id_count, household.ctc_ssn, household.taxpayer_work_ssn_count, household.taxpayer_work_ssn

## Schedule B — interest payer entries

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| interest.amount | — | — | — | — |

## Form 7206, line 2 — qualified long-term care insurance, one per person covered

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| ltc.payments | — | — | — | — |
| ltc.age | — | — | — | — |
| ltc.limit | — | — | — | 2 (classm.ltc.1, classm.ltc.2) |
| ltc.amount | — | — | — | 2 (classm.ltc.1, classm.ltc.2) |

## Mid-quarter convention test for property placed in service in 2025

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| mq.q4 | — | — | — | — |
| mq.total | — | — | — | — |
| mq.five | — | — | — | — |
| mq.two | — | — | — | — |
| mq.q4x5 | — | — | — | — |
| mq.totalx2 | — | — | — | — |
| mq.applies | — | — | — | 6 |

Unasserted lines: mq.q4, mq.total, mq.five, mq.two, mq.q4x5, mq.totalx2

## Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| otjob.one | — | — | — | — |
| otjob.zero | — | — | — | — |
| otjob.flsa | — | — | — | — |
| otjob.special_rule | — | — | — | — |
| otjob.method | — | — | — | — |
| otjob.statement | — | — | — | — |
| otjob.refused | — | — | — | 3 |
| otjob.figured | — | — | — | 3 |
| otjob.by_third | — | — | — | 2 (classm.otjob.1, classm.otjob.2) |
| otjob.by_half | — | — | — | 2 (classm.otjob.1, classm.otjob.2) |
| otjob.by_quarter | — | — | — | 2 (classm.otjob.1, classm.otjob.3) |
| otjob.col_b | — | — | — | 3 |

Unasserted lines: otjob.one, otjob.zero

## Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| person.role | — | — | — | — |
| person.one | — | — | — | — |
| person.age65 | — | — | — | — |
| person.blind | — | — | — | — |
| person.tin | — | — | — | — |
| person.itin_applied | — | — | — | — |
| person.work_ssn | — | — | — | — |
| person.educator_expenses | — | — | — | — |
| person.eligible_educator | — | — | — | — |
| person.born_before_2001 | — | — | — | — |
| person.born_after_1960 | — | — | — | — |
| person.died_before_65 | — | — | — | — |
| person.educator_max | — | — | — | — |
| person.has_educator_expenses | — | — | — | 4 |
| person.educator_limited | — | — | — | 4 |
| person.educator_eligible_amount | — | — | — | 4 |
| person.educator_deduction | — | — | — | 4 |
| person.hsa_forms | — | — | — | 4 |
| person.hsa_repeated | — | — | — | 4 |
| person.hsa_split | — | — | — | 4 |
| person.hsa_agreed | — | — | — | 4 |
| person.hsa_step1 | — | — | — | 4 |
| person.hsa_share | — | — | — | 4 |
| person.hsa_deduction | — | — | — | 4 |
| person.tip_employers | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.tip_total | — | — | — | 4 |
| person.tip_reported | — | — | — | 4 |
| person.ot_employers | — | — | — | 4 |
| person.ot_total | — | — | — | 4 |
| person.rrta | — | — | — | — |
| person.employers | — | — | — | 4 |
| person.overcount | — | — | — | 4 |
| person.over | — | — | — | 4 |
| person.wages | — | — | — | 4 |
| person.withheld | — | — | — | 4 |
| person.box1 | — | — | — | 4 |
| person.box2 | — | — | — | 4 |
| person.eligible | — | — | — | 4 |
| person.excess | — | — | — | 4 |
| person.zero | — | — | — | — |
| person.credit | — | — | — | 4 |
| person.medicare5 | — | — | — | 4 |
| person.medicare6 | — | — | — | 4 |
| person.sc_count | — | — | — | — |
| person.ho_count | — | — | — | — |
| person.mq_q4 | — | — | — | — |
| person.mq_total | — | — | — | — |
| person.cost179 | — | — | — | — |
| person.s179_nonlisted | — | — | — | — |
| person.s179_listed | — | — | — | — |
| person.income179 | — | — | — | — |
| person.has_sc | — | — | — | — |
| person.sc_total | — | — | — | — |
| person.se_screen | — | — | — | — |
| person.se_screened | — | — | — | — |
| person.se_line2 | — | — | — | 2 (stage14.asset.s179, stage14.refuse.se_screen) |
| person.se_line6 | — | — | — | 3 |
| person.se_line12 | — | — | — | 10 |
| person.se_line13 | — | — | — | — |
| person.se_line4c | — | — | — | — |
| person.plan | — | — | — | — |
| person.plan_screen | — | — | — | — |
| person.plan_screened | — | — | — | — |
| person.cent | — | — | — | — |
| person.hundred | — | — | — | — |
| person.sep_rate | — | — | — | — |
| person.sep_contrib | — | — | — | 1 (stage14.plan.refuse_screen) |
| person.sep_rate_c | — | — | — | — |
| person.sep_rate_plus | — | — | — | — |
| person.sep_s1 | — | — | — | — |
| person.sep_s2 | — | — | — | — |
| person.sep_s3 | — | — | — | — |
| person.sep_s5 | — | — | — | 2 (stage14.sep.basic, stage14.sep.rate_5) |
| person.comp_limit | — | — | — | — |
| person.sep_s6 | — | — | — | 1 (stage14.sep.dollar_limit) |
| person.sep_s7 | — | — | — | 1 (stage14.sep.rate_5) |
| person.sep_s8 | — | — | — | — |
| person.sep_s21 | — | — | — | 3 |
| person.sep_excess | — | — | — | — |
| person.sep_deduction | — | — | — | 1 (stage14.sep.refuse_excess) |
| person.simple_deferral | — | — | — | 1 (stage14.plan.refuse_screen_simple) |
| person.simple_age | — | — | — | — |
| person.simple_kind | — | — | — | — |
| person.simple_employer | — | — | — | — |
| person.simple_comp | — | — | — | 1 (stage14.simple.match_age50) |
| person.simple_cap | — | — | — | — |
| person.simple_regular | — | — | — | — |
| person.simple_catchup | — | — | — | — |
| person.catchup_limit | — | — | — | — |
| person.comp_after_regular | — | — | — | — |
| person.catchup_max | — | — | — | 2 (stage14.simple.nonelective_60, stage14.simple.refuse_catchup_comp) |
| person.rate3 | — | — | — | — |
| person.rate2 | — | — | — | — |
| person.match_3pct | — | — | — | — |
| person.deferrals_total | — | — | — | — |
| person.match_max | — | — | — | 2 (stage14.simple.match_age50, stage14.simple.match_high_comp) |
| person.ne_comp | — | — | — | — |
| person.ne_max | — | — | — | 2 (stage14.simple.nonelective_60, stage14.simple.comp_cap) |
| person.employer_max | — | — | — | — |
| person.simple_excess | — | — | — | — |
| person.simple_deduction | — | — | — | 4 |
| person.plan_deduction | — | — | — | — |
| person.s16 | — | — | — | — |
| person.positive_profits | — | — | — | — |
| person.sehi | — | — | — | — |
| person.qbi | — | — | — | — |
| person.eic_part1 | — | — | — | — |
| person.files_se | — | — | — | — |
| person.eic_se_has | — | — | — | — |
| person.eic_se | — | — | — | — |
| person.sc_1a | — | — | — | — |

Unasserted lines: person.one, person.educator_max, person.zero, person.sc_count, person.ho_count, person.mq_q4, person.mq_total, person.cost179, person.s179_nonlisted, person.s179_listed, person.income179, person.has_sc, person.sc_total, person.se_screened, person.se_line13, person.se_line4c, person.plan_screened, person.cent, person.hundred, person.sep_rate_c, person.sep_rate_plus, person.sep_s1, person.sep_s2, person.sep_s3, person.comp_limit, person.sep_s8, person.sep_excess, person.simple_cap, person.simple_regular, person.simple_catchup, person.catchup_limit, person.comp_after_regular, person.rate3, person.rate2, person.match_3pct, person.deferrals_total, person.ne_comp, person.employer_max, person.simple_excess, person.plan_deduction, person.s16, person.positive_profits, person.sehi, person.qbi, person.eic_part1, person.files_se, person.eic_se_has, person.eic_se, person.sc_1a

## Qualified business income and section 199A dividends — amounts and the choice of Form 8995

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| qbi.dividends | — | — | — | — |
| qbi.unsupported | — | — | — | — |
| qbi.zero | — | — | — | — |
| qbi.eligible | — | — | — | — |
| qbi.carryforward | — | — | — | — |
| qbi.business_any | — | — | — | — |
| qbi.via_8995a | — | — | — | 1 (stage14.refuse.qbi_8995a) |
| qbi.deductions_before | — | — | — | — |
| qbi.taxable_before | — | — | — | 2 (stage4.qbi.income_limit, stage4.qbi.zero_income) |
| qbi.net_capital_gain | — | — | — | — |
| qbi.threshold | — | — | — | — |
| qbi.use_8995a | — | — | — | 3 |
| qbi.deduction | — | — | — | 11 |

Unasserted lines: qbi.zero, qbi.eligible, qbi.business_any, qbi.deductions_before, qbi.net_capital_gain, qbi.threshold

## Qualified Dividends and Capital Gain Tax Worksheet—Line 16

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| qdcg.schedule_d_filed | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.schedule_d_net_gain | — | — | 1 (qdcg.sd.side) | — |
| qdcg.line1 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line2 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line3 | — | 1 (qdcg.handworked.single) | 11 | 6 |
| qdcg.line4 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line5 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line6 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line7 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line8 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line9 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line10 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line11 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line12 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line13 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line14 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| qdcg.line15 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line16 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line17 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line18 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line19 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line20 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line21 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line22 | — | 1 (qdcg.handworked.single) | 11 | 1 (qdcg.table.minimum.regression) |
| qdcg.line23 | — | 1 (qdcg.handworked.single) | 11 | 4 |
| qdcg.line24 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 1 (qdcg.table.minimum.regression) |
| qdcg.line25 | — | 1 (qdcg.handworked.single) | 11 | 4 |

## Form 1099-R distributions (IRAs, pensions and annuities)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| retirement.account | — | — | — | — |
| retirement.code | — | — | — | — |
| retirement.box1 | — | — | — | — |
| retirement.box5 | — | — | — | — |
| retirement.rollover | — | — | — | — |
| retirement.special | — | — | — | — |
| retirement.annuity | — | — | — | — |
| retirement.cost | — | — | — | — |
| retirement.used_last_year | — | — | — | — |
| retirement.last_line4 | — | — | — | — |
| retirement.joint_life | — | — | — | — |
| retirement.age | — | — | — | — |
| retirement.combined_age | — | — | — | — |
| retirement.months | — | — | — | — |
| retirement.recovered | — | — | — | — |
| retirement.zero | — | — | — | — |
| retirement.one | — | — | — | — |
| retirement.is_ira | — | — | — | 3 |
| retirement.roth | — | — | — | 3 |
| retirement.direct | — | — | — | 3 |
| retirement.bad_code | — | — | — | 3 |
| retirement.rolled | — | — | — | 3 |
| retirement.has_rollover | — | — | — | 3 |
| retirement.smw1 | — | — | — | 3 |
| retirement.smw2 | — | — | — | 3 |
| retirement.smw4_t1_360 | — | — | — | 3 |
| retirement.smw4_t1_310 | — | — | — | 3 |
| retirement.smw4_t1_260 | — | — | — | 3 |
| retirement.smw4_t1_210 | — | — | — | 3 |
| retirement.smw4_t1_160 | — | — | — | 3 |
| retirement.smw4_t2_410 | — | — | — | 3 |
| retirement.smw4_t2_360 | — | — | — | 3 |
| retirement.smw4_t2_310 | — | — | — | 3 |
| retirement.smw4_t2_260 | — | — | — | 3 |
| retirement.smw4_t2_210 | — | — | — | 3 |
| retirement.smw4_table1 | — | — | — | 3 |
| retirement.smw4_table2 | — | — | — | 3 |
| retirement.smw4_new | — | — | — | 3 |
| retirement.smw4 | — | — | — | 7 |
| retirement.smw5 | — | — | — | 6 |
| retirement.smw6 | — | — | — | 3 |
| retirement.smw7 | — | — | — | 3 |
| retirement.smw8 | — | — | — | 4 |
| retirement.smw9 | — | — | — | 3 |
| retirement.smw10 | — | — | — | 7 |
| retirement.smw11 | — | — | — | 7 |
| retirement.cost_left | — | — | — | 3 |
| retirement.annuity_with_cost | — | — | — | 3 |
| retirement.annuity_rollover | — | — | — | 3 |
| retirement.annuity_taxable | — | — | — | 3 |
| retirement.ira_taxable | — | — | — | 3 |
| retirement.ira_not_rolled | — | — | — | 3 |
| retirement.plan_excluded | — | — | — | 3 |
| retirement.plan_simple | — | — | — | 3 |
| retirement.plan_taxable | — | — | — | 3 |
| retirement.taxable | — | — | — | 3 |
| retirement.show_a | — | — | — | 3 |
| retirement.amount_a | — | — | — | 3 |

Unasserted lines: retirement.zero, retirement.one

## Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s1.zero | — | — | — | — |
| s1.uc_paid | — | — | — | — |
| s1.has_uc | — | — | — | — |
| s1.uc_repaid | — | — | — | — |
| s1.uc_unsupported | — | — | — | — |
| s1.line7_figured | — | — | — | — |
| s1.line7 | — | — | — | 5 |
| s1.line7_box | — | — | — | 5 |
| s1.line7_repaid | — | — | — | 4 |
| s1.ebl_loss | — | — | — | — |
| s1.ebl_total | — | — | — | — |
| s1.zero_ebl | — | — | — | — |
| s1.ebl_threshold | — | — | — | — |
| s1.ebl | — | — | — | — |
| s1.sc_count | — | — | — | — |
| s1.has_sc | — | — | — | — |
| s1.sc_1a_count | — | — | — | — |
| s1.sc_1a | — | — | — | — |
| s1.line3 | — | — | — | 11 |
| s1.line10 | — | — | — | 6 |
| s1.line11 | — | — | — | 8 |
| s1.line13 | — | — | — | 15 |
| s1.line15 | — | — | — | 8 |
| s1.line16 | — | — | — | 8 |
| s1.line17 | — | — | — | 3 |
| s1.line21 | — | — | — | 5 |
| s1.line26 | — | — | — | 4 |

Unasserted lines: s1.zero, s1.has_uc, s1.line7_figured, s1.ebl_loss, s1.ebl_total, s1.zero_ebl, s1.ebl_threshold, s1.ebl, s1.sc_count, s1.has_sc, s1.sc_1a_count, s1.sc_1a

## Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s179.line2 | — | — | — | 5 |
| s179.max | — | — | — | — |
| s179.line1 | — | — | — | 2 (stage14.s179.carryover_no_property, stage14.s179.dollar_limit) |
| s179.line3 | — | — | — | 3 |
| s179.line4 | — | — | — | 6 |
| s179.line5_full | — | — | — | — |
| s179.separate | — | — | — | — |
| s179.line5_mfs | — | — | — | — |
| s179.line5 | — | — | — | 7 |
| s179.mfs | — | — | — | 1 (stage14.s179.mfs_no_election) |
| s179.line6 | — | — | — | 3 |
| s179.line7 | — | — | — | 3 |
| s179.line8 | — | — | — | 3 |
| s179.line9 | — | — | — | 4 |
| s179.line10 | — | — | — | — |
| s179.income_sc | — | — | — | — |
| s179.income | — | — | — | — |
| s179.income0 | — | — | — | — |
| s179.line11 | — | — | — | 8 |
| s179.line9_10 | — | — | — | — |
| s179.line12 | — | — | — | 14 |
| s179.sc_count | — | — | — | — |
| s179.orphan | — | — | — | — |
| s179.line13 | — | — | — | 11 |
| s179.differs | — | — | — | — |
| s179.multi | — | — | — | — |

Unasserted lines: s179.max, s179.line5_full, s179.separate, s179.line5_mfs, s179.income_sc, s179.income, s179.income0, s179.line9_10, s179.sc_count, s179.orphan, s179.differs, s179.multi

## Schedule 1-A (Form 1040) — Additional Deductions

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s1a.zero | — | — | — | — |
| s1a.line1 | — | — | — | 1 (classm.s1a.1) |
| s1a.line2a | — | — | — | 1 (classm.s1a.1) |
| s1a.line2b | — | — | — | 1 (classm.s1a.1) |
| s1a.line2c | — | — | — | 1 (classm.s1a.1) |
| s1a.line2d | — | — | — | 1 (classm.s1a.1) |
| s1a.line2e | — | — | — | 1 (classm.s1a.1) |
| s1a.line3 | — | — | — | 2 (classm.s1a.1, stage12.tips.one_employer) |
| s1a.tips | — | — | — | — |
| s1a.tip_employers | — | — | — | — |
| s1a.tip_total | — | — | — | — |
| s1a.tip_reported | — | — | — | — |
| s1a.tip_multi | — | — | — | — |
| s1a.tip_ssn_count | — | — | — | — |
| s1a.tip_ssn | — | — | — | — |
| s1a.part2 | — | — | — | — |
| s1a.line4a_calc | — | — | — | — |
| s1a.line4a | — | — | — | 6 |
| s1a.line4b_calc | — | — | — | — |
| s1a.line4b | — | — | — | 2 (classm.s1a.1, stage12.tips.one_employer) |
| s1a.line4c_one | — | — | — | — |
| s1a.line4c_calc | — | — | — | — |
| s1a.line4c | — | — | — | 8 |
| s1a.line5_calc | — | — | — | 2 (stage14.refuse.sch1a_tips, stage14.sch1a.tips_with_sc) |
| s1a.line5 | — | — | — | 1 (classm.s1a.1) |
| s1a.line6_calc | — | — | — | — |
| s1a.line6 | — | — | — | 3 |
| s1a.line7_calc | — | — | — | — |
| s1a.line7 | — | — | — | 5 |
| s1a.tips_max | — | — | — | — |
| s1a.base_other | — | — | — | — |
| s1a.base_joint | — | — | — | — |
| s1a.line8_calc | — | — | — | — |
| s1a.line8 | — | — | — | 2 (classm.s1a.1, stage13.tips_only_spouse_no_ssn) |
| s1a.line9_calc | — | — | — | — |
| s1a.line9 | — | — | — | 2 (classm.s1a.1, stage12.mfj.tips_overtime) |
| s1a.line10_calc | — | — | — | — |
| s1a.line10 | — | — | — | 4 |
| s1a.line10_over | — | — | — | — |
| s1a.line10_pos | — | — | — | — |
| s1a.line11_thousands | — | — | — | — |
| s1a.line12_calc | — | — | — | — |
| s1a.line12 | — | — | — | 6 |
| s1a.line13_figured | — | — | — | — |
| s1a.line13_amount | — | — | — | — |
| s1a.line13_ssn | — | — | — | — |
| s1a.line13_claim | — | — | — | — |
| s1a.line13 | — | — | — | 20 |
| s1a.overtime | — | — | — | — |
| s1a.ot_ssn_count | — | — | — | — |
| s1a.ot_ssn | — | — | — | — |
| s1a.part3 | — | — | — | — |
| s1a.line14a_calc | — | — | — | — |
| s1a.line14a | — | — | — | 12 |
| s1a.line14b_calc | — | — | — | 1 (stage14.sch1a.refuse_overtime_1099) |
| s1a.line14b | — | — | — | 1 (classm.s1a.1) |
| s1a.line14c_calc | — | — | — | — |
| s1a.line14c | — | — | — | 3 |
| s1a.ot_max_other | — | — | — | — |
| s1a.ot_max_joint | — | — | — | — |
| s1a.ot_max | — | — | — | — |
| s1a.line15_calc | — | — | — | — |
| s1a.line15 | — | — | — | 5 |
| s1a.line16_calc | — | — | — | — |
| s1a.line16 | — | — | — | 2 (classm.s1a.1, stage13.overtime_only_spouse_no_ssn) |
| s1a.line17_calc | — | — | — | — |
| s1a.line17 | — | — | — | 1 (classm.s1a.1) |
| s1a.line18_calc | — | — | — | — |
| s1a.line18 | — | — | — | 2 (classm.s1a.1, stage12.ot.phaseout) |
| s1a.line18_over | — | — | — | — |
| s1a.line18_pos | — | — | — | — |
| s1a.line19_thousands | — | — | — | — |
| s1a.line20_calc | — | — | — | — |
| s1a.line20 | — | — | — | 3 |
| s1a.line21_figured | — | — | — | — |
| s1a.line21_amount | — | — | — | — |
| s1a.line21_ssn | — | — | — | — |
| s1a.line21_claim | — | — | — | — |
| s1a.line21 | — | — | — | 18 |
| s1a.carloan | — | — | — | — |
| s1a.line23_total | — | — | — | — |
| s1a.line23 | — | — | — | 7 |
| s1a.car_max | — | — | — | — |
| s1a.part4 | — | — | — | — |
| s1a.line24_calc | — | — | — | — |
| s1a.line24 | — | — | — | 4 |
| s1a.car_base_other | — | — | — | — |
| s1a.car_base_joint | — | — | — | — |
| s1a.line25_calc | — | — | — | — |
| s1a.line25 | — | — | — | 1 (classm.s1a.1) |
| s1a.line26_calc | — | — | — | — |
| s1a.line26 | — | — | — | 2 (classm.s1a.1, stage12.mfj.car) |
| s1a.line27_calc | — | — | — | — |
| s1a.line27 | — | — | — | 3 |
| s1a.line27_over | — | — | — | — |
| s1a.line27_pos | — | — | — | — |
| s1a.line28_thousands | — | — | — | — |
| s1a.line29_calc | — | — | — | — |
| s1a.line29 | — | — | — | 5 |
| s1a.line30_figured | — | — | — | — |
| s1a.line30_amount | — | — | — | — |
| s1a.line30 | — | — | — | 16 |
| s1a.senior_count | — | — | — | — |
| s1a.senior_any | — | — | — | — |
| s1a.part5 | — | — | — | — |
| s1a.line31_calc | — | — | — | — |
| s1a.line31 | — | — | — | 2 (classm.s1a.1, stage13.seniors_none) |
| s1a.senior_base_other | — | — | — | — |
| s1a.senior_base_joint | — | — | — | — |
| s1a.line32_calc | — | — | — | — |
| s1a.line32 | — | — | — | 2 (classm.s1a.1, stage12.mfj.senior) |
| s1a.line33_calc | — | — | — | — |
| s1a.line33 | — | — | — | 4 |
| s1a.line33_over | — | — | — | — |
| s1a.line33_pos | — | — | — | — |
| s1a.line34_calc | — | — | — | — |
| s1a.line34 | — | — | — | 5 |
| s1a.senior_amount | — | — | — | — |
| s1a.line35_figured | — | — | — | — |
| s1a.line35_calc | — | — | — | — |
| s1a.line35 | — | — | — | 9 |
| s1a.died_before_65_count | — | — | — | — |
| s1a.died_before_65 | — | — | — | — |
| s1a.senior_decedent | — | — | — | — |
| s1a.line36a_senior | — | — | — | — |
| s1a.line36a_claim | — | — | — | — |
| s1a.line36a | — | — | — | 12 |
| s1a.spouse_senior_count | — | — | — | — |
| s1a.spouse_senior | — | — | — | — |
| s1a.spouse_died_before_65_count | — | — | — | — |
| s1a.spouse_died_before_65 | — | — | — | — |
| s1a.spouse_senior_decedent | — | — | — | — |
| s1a.line36b_senior | — | — | — | — |
| s1a.line36b | — | — | — | 9 |
| s1a.line37 | — | — | — | 17 |
| s1a.line38 | — | — | — | 8 |

Unasserted lines: s1a.zero, s1a.tip_employers, s1a.tip_total, s1a.tip_reported, s1a.tip_multi, s1a.tip_ssn_count, s1a.tip_ssn, s1a.part2, s1a.line4a_calc, s1a.line4b_calc, s1a.line4c_one, s1a.line4c_calc, s1a.line6_calc, s1a.line7_calc, s1a.tips_max, s1a.base_other, s1a.base_joint, s1a.line8_calc, s1a.line9_calc, s1a.line10_calc, s1a.line10_over, s1a.line10_pos, s1a.line11_thousands, s1a.line12_calc, s1a.line13_figured, s1a.line13_amount, s1a.line13_ssn, s1a.line13_claim, s1a.ot_ssn_count, s1a.ot_ssn, s1a.part3, s1a.line14a_calc, s1a.line14c_calc, s1a.ot_max_other, s1a.ot_max_joint, s1a.ot_max, s1a.line15_calc, s1a.line16_calc, s1a.line17_calc, s1a.line18_calc, s1a.line18_over, s1a.line18_pos, s1a.line19_thousands, s1a.line20_calc, s1a.line21_figured, s1a.line21_amount, s1a.line21_ssn, s1a.line21_claim, s1a.line23_total, s1a.car_max, s1a.part4, s1a.line24_calc, s1a.car_base_other, s1a.car_base_joint, s1a.line25_calc, s1a.line26_calc, s1a.line27_calc, s1a.line27_over, s1a.line27_pos, s1a.line28_thousands, s1a.line29_calc, s1a.line30_figured, s1a.line30_amount, s1a.senior_count, s1a.senior_any, s1a.part5, s1a.line31_calc, s1a.senior_base_other, s1a.senior_base_joint, s1a.line32_calc, s1a.line33_calc, s1a.line33_over, s1a.line33_pos, s1a.line34_calc, s1a.senior_amount, s1a.line35_figured, s1a.line35_calc, s1a.died_before_65_count, s1a.died_before_65, s1a.senior_decedent, s1a.line36a_senior, s1a.line36a_claim, s1a.spouse_senior_count, s1a.spouse_senior, s1a.spouse_died_before_65_count, s1a.spouse_died_before_65, s1a.spouse_senior_decedent, s1a.line36b_senior

## Schedule 2 — Additional Taxes (the lines this tool computes)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s2.amt | — | — | — | — |
| s2.other | — | — | — | — |
| s2.zero | — | — | — | — |
| s2.line2 | — | — | — | 4 |
| s2.line3 | — | — | — | 4 |
| s2.line4 | — | — | — | 3 |
| s2.line11 | — | — | — | 2 (classm.s2.1, stage4.additional_taxes.combined) |
| s2.line12 | — | — | — | 2 (classm.s2.1, stage4.additional_taxes.combined) |
| s2.line21 | — | — | — | 7 |

Unasserted lines: s2.zero

## Schedule 3 — selected lines

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | 1 (classm.s3.1) |
| s3.zero | — | — | — | — |
| s3.line8 | — | — | — | 4 |
| s3.mfs | — | — | — | — |
| s3.line9 | — | — | — | — |
| s3.line10 | — | — | — | — |
| s3.line11 | — | — | — | 25 |
| s3.line12 | — | — | — | — |
| s3.line14 | — | — | — | — |
| s3.line15 | — | — | — | 22 |

Unasserted lines: s3.zero, s3.mfs

## Schedule 8812 — Credits for Qualifying Children and Other Dependents

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s8812.line1 | — | — | — | 27 |
| s8812.zero | — | — | — | — |
| s8812.line2a | — | — | — | 27 |
| s8812.line2b | — | — | — | 27 |
| s8812.line2c | — | — | — | 27 |
| s8812.line2d | — | — | — | 27 |
| s8812.line3 | — | — | — | 27 |
| s8812.line4 | — | — | — | 30 |
| s8812.line5 | — | — | — | 30 |
| s8812.line6 | — | — | — | 27 |
| s8812.line7 | — | — | — | 27 |
| s8812.line8 | — | — | — | 30 |
| s8812.line9 | — | — | — | 3 |
| s8812.excess | — | — | — | 24 |
| s8812.line10 | — | — | — | 27 |
| s8812.line11 | — | — | — | 27 |
| s8812.line12 | — | — | — | 27 |
| s8812.clw_a1 | — | — | — | 24 |
| s8812.clw_a2 | — | — | — | 24 |
| s8812.clw_a3 | — | — | — | 24 |
| s8812.clw_a4 | — | — | — | 24 |
| s8812.clw_a5 | — | — | — | 24 |
| s8812.line13 | — | — | — | 26 |
| s8812.line14 | — | — | — | 27 |
| s8812.line16a | — | — | — | 27 |
| s8812.line16b | — | — | — | 26 |
| s8812.line17 | — | — | — | 27 |
| s8812.combat_pay | — | — | — | — |
| s8812.puerto_rico | — | — | — | — |
| s8812.eiw_1a | — | — | — | 24 |
| s8812.eiw_1b | — | — | — | 24 |
| s8812.eiw_2b | — | — | — | — |
| s8812.eiw_3sum | — | — | — | 2 (stage14.s8812.eiw_stop_with_se_tax, stage14.s8812.eiw_zero_with_se_tax) |
| s8812.eiw_3 | — | — | — | 24 |
| s8812.eiw_4 | — | — | — | 24 |
| s8812.eiw_5 | — | — | — | 24 |
| s8812.eiw_6 | — | — | — | 24 |
| s8812.eiw_7_figured | — | — | — | — |
| s8812.eiw_3_positive | — | — | — | — |
| s8812.eiw_7 | — | — | — | 26 |
| s8812.taking_eic | — | — | — | 4 |
| s8812.chart_eic | — | — | — | — |
| s8812.line18a | — | — | — | 31 |
| s8812.line18b | — | — | — | 27 |
| s8812.line19 | — | — | — | 30 |
| s8812.line20 | — | — | — | 28 |
| s8812.ss_withheld | — | — | — | 24 |
| s8812.amt_ws4 | — | — | — | 24 |
| s8812.amt_ws6 | — | — | — | — |
| s8812.amt_ws7 | — | — | — | 1 (stage14.f8959.se_above_threshold) |
| s8812.line21 | — | — | — | 26 |
| s8812.line22 | — | — | — | 28 |
| s8812.line23 | — | — | — | 26 |
| s8812.line24 | — | — | — | 26 |
| s8812.line25 | — | — | — | 26 |
| s8812.line26 | — | — | — | 25 |
| s8812.few_children | — | — | — | 24 |
| s8812.earned_covers | — | — | — | 24 |
| s8812.from_part_iia | — | — | — | 24 |
| s8812.from_part_iib | — | — | — | 25 |
| s8812.part_iib_result | — | — | — | 24 |
| s8812.line27 | — | — | — | 28 |

Unasserted lines: s8812.zero, s8812.eiw_2b, s8812.eiw_7_figured, s8812.eiw_3_positive, s8812.chart_eic, s8812.amt_ws6

## Schedule A — supported itemized deductions and standard comparison

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sa.unsupported | — | — | — | — |
| sa.charity_limited | — | — | — | — |
| sa.excluded_income | — | — | — | — |
| sa.dependent | — | — | — | — |
| sa.spouse_extra | — | — | — | — |
| sa.mfs_spouse_extra | — | — | — | — |
| sa.age65_count | — | — | — | — |
| sa.age65 | — | — | — | — |
| sa.spouse_itemizes | — | — | — | — |
| sa.elect_itemize | — | — | — | — |
| sa.agi | — | — | — | — |
| sa.line1 | — | — | — | — |
| sa.line5a | — | — | — | — |
| sa.line5b | — | — | — | — |
| sa.line5c | — | — | — | — |
| sa.line8a | — | — | — | — |
| sa.line11 | — | — | — | — |
| sa.zero | — | — | — | — |
| sa.line2 | — | — | — | 6 |
| sa.line3 | — | — | — | 6 |
| sa.line4 | — | — | — | 8 |
| sa.line5d | — | — | — | 8 |
| sa.saltbase | — | — | — | — |
| sa.saltfloor | — | — | — | — |
| sa.saltthreshold | — | — | — | — |
| sa.saltexcess | — | — | — | — |
| sa.saltreduction | — | — | — | — |
| sa.saltremaining | — | — | — | — |
| sa.saltfloor_applied | — | — | — | — |
| sa.salthalf | — | — | — | 1 (stage4.salt.mfs_floor) |
| sa.mfs | — | — | — | — |
| sa.saltlimit | — | — | — | — |
| sa.line5e | — | — | — | 17 |
| sa.line6 | — | — | — | 11 |
| sa.line8b | — | — | — | 10 |
| sa.line8c | — | — | — | 10 |
| sa.line13 | — | — | — | 10 |
| sa.line15 | — | — | — | 10 |
| sa.line16 | — | — | — | 10 |
| sa.line7 | — | — | — | 7 |
| sa.line8e | — | — | — | 7 |
| sa.line9 | — | — | — | 7 |
| sa.line10 | — | — | — | 7 |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 15 |
| sa.form8283 | — | — | — | 3 |
| sa.line14 | — | — | — | 7 |
| sa.line17 | — | — | — | 10 |
| sa.standardbase | — | — | — | — |
| sa.extra | — | — | — | — |
| sa.boxes_age65 | — | — | — | — |
| sa.extra_age65 | — | — | — | — |
| sa.boxes_blind | — | — | — | — |
| sa.extra_blind | — | — | — | — |
| sa.standardraw | — | — | — | — |
| sa.standard | — | — | — | 12 |
| sa.itemizes | — | — | — | 6 |
| sa.deduction | — | — | — | 7 |
| sa.mfs_spouse_itemizes | — | — | — | — |

Unasserted lines: sa.mfs_spouse_extra, sa.age65_count, sa.age65, sa.agi, sa.zero, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.standardbase, sa.extra, sa.boxes_age65, sa.extra_age65, sa.boxes_blind, sa.extra_blind, sa.standardraw, sa.mfs_spouse_itemizes

## Form 8949 and Schedule D — manually classified securities transactions

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sales.box | — | — | — | — |
| sales.route | — | — | — | — |
| sales.code | — | — | — | — |
| sales.special | — | — | — | — |
| sales.aggregate_eligible | — | — | — | — |
| sales.proceeds | — | — | — | — |
| sales.reported_basis | — | — | — | — |
| sales.correct_basis | — | — | — | — |
| sales.wash_loss | — | — | — | — |
| sales.covered | — | — | — | 1 (classm.sales.1) |
| sales.digital | — | — | — | 1 (classm.sales.1) |
| sales.has_b | — | — | — | 1 (classm.sales.1) |
| sales.has_w | — | — | — | 1 (classm.sales.1) |
| sales.bad_code | — | — | — | 1 (classm.sales.1) |
| sales.bad_aggregate | — | — | — | 1 (classm.sales.1) |
| sales.one | — | — | — | — |
| sales.zero | — | — | — | — |
| sales.e | — | — | — | 1 (classm.sales.1) |
| sales.b_difference | — | — | — | 1 (classm.sales.1) |
| sales.adjust_b | — | — | — | 1 (classm.sales.1) |
| sales.b | — | — | — | 1 (classm.sales.1) |
| sales.w | — | — | — | 1 (classm.sales.1) |
| sales.g | 4 | — | — | 13 |
| sales.before_adjustment | — | — | — | 1 (classm.sales.1) |
| sales.h | 4 | — | — | 13 |

Unasserted lines: sales.one, sales.zero

## Schedule B — supported interest and ordinary dividends

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sb.unsupported | — | — | — | — |
| sb.ordinary_dividends | — | — | — | — |
| sb.line7a | — | — | — | — |
| sb.fbar_required | — | — | — | — |
| sb.form8938 | — | — | — | — |
| sb.line8 | — | — | — | — |
| sb.zero | — | — | — | — |
| sb.line2 | — | — | — | 8 |
| sb.line3 | — | — | — | 8 |
| sb.line4 | — | — | — | 8 |
| sb.line6 | — | — | — | 7 |
| sb.partIII | — | — | — | 1 (stage4.sb.foreign_no_filing) |

Unasserted lines: sb.zero

## Schedule C (Form 1040) — Profit or Loss From Business, one per business

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sc.one | — | — | — | — |
| sc.zero | — | — | — | — |
| sc.statutory | — | — | — | — |
| sc.passive | — | — | — | — |
| sc.spouse_owned | — | — | — | — |
| sc.method_other | — | — | — | — |
| sc.special | — | — | — | — |
| sc.screened | — | — | — | 4 |
| sc.line1 | — | — | — | 5 |
| sc.line2 | — | — | — | — |
| sc.line3 | — | — | — | 5 |
| sc.line4 | — | — | — | 5 |
| sc.line5 | — | — | — | 4 |
| sc.line6 | — | — | — | — |
| sc.line7 | — | — | — | 5 |
| sc.line8 | — | — | — | — |
| sc.line9 | — | — | — | 5 |
| sc.line10 | — | — | — | — |
| sc.line11 | — | — | — | — |
| sc.line12 | — | — | — | 4 |
| sc.line13 | — | — | — | 21 |
| sc.line14 | — | — | — | — |
| sc.line15 | — | — | — | — |
| sc.line16a | — | — | — | — |
| sc.line16b | — | — | — | — |
| sc.line17 | — | — | — | — |
| sc.line18 | — | — | — | — |
| sc.line19 | — | — | — | — |
| sc.line20a | — | — | — | 6 |
| sc.line20b | — | — | — | — |
| sc.line21 | — | — | — | — |
| sc.line22 | — | — | — | — |
| sc.line23 | — | — | — | — |
| sc.line24a | — | — | — | — |
| sc.meals_50 | — | — | — | — |
| sc.meals_80 | — | — | — | — |
| sc.meals_100 | — | — | — | — |
| sc.meals_50_ded | — | — | — | 4 |
| sc.meals_80_ded | — | — | — | 4 |
| sc.line24b | — | — | — | 6 |
| sc.line25 | — | — | — | — |
| sc.line26 | — | — | — | — |
| sc.line27a | — | — | — | 4 |
| sc.line48 | — | — | — | — |
| sc.line27b | — | — | — | 4 |
| sc.line28 | — | — | — | 7 |
| sc.line29 | — | — | — | 4 |
| sc.line28_pre179 | — | — | — | 4 |
| sc.line29_pre179 | — | — | — | 4 |
| sc.ho_uses | — | — | — | — |
| sc.ho_other | — | — | — | — |
| sc.ho_screened | — | — | — | 4 |
| sc.ho_multi | — | — | — | — |
| sc.ho_sqft | — | — | — | — |
| sc.ho_home_sqft | — | — | — | — |
| sc.ho_rate | — | — | — | — |
| sc.ho_cap_sqft | — | — | — | — |
| sc.ho_over | — | — | — | 4 |
| sc.ho_line4_actual | — | — | — | 4 |
| sc.ho_line4_cap | — | — | — | 4 |
| sc.ho_line4 | — | — | — | 7 |
| sc.ho_line1 | — | — | — | 5 |
| sc.ho_room | — | — | — | 4 |
| sc.ho_unlimited | — | — | — | 4 |
| sc.ho_s179_max | — | — | — | 4 |
| sc.ho_no179 | — | — | — | 4 |
| sc.ho_limited | — | — | — | 4 |
| sc.ho_pre179_floor | — | — | — | 4 |
| sc.ho_both_limits | — | — | — | 4 |
| sc.ho_both | — | — | — | 3 |
| sc.ho_line5_lim | — | — | — | 3 |
| sc.ho_line5 | — | — | — | 4 |
| sc.line30 | — | — | — | 13 |
| sc.line31 | — | — | — | 18 |
| sc.line31_pre179 | — | — | — | 4 |
| sc.loss | — | — | — | 4 |
| sc.at_risk | — | — | — | — |
| sc.not_at_risk | — | — | — | 4 |
| sc.loss_allowed | — | — | — | 4 |
| sc.result | — | — | — | 4 |
| sc.inventory_other | — | — | — | — |
| sc.line35 | — | — | — | 1 (stage14.refuse.inventory) |
| sc.line36 | — | — | — | — |
| sc.line37 | — | — | — | — |
| sc.line38 | — | — | — | — |
| sc.line39 | — | — | — | — |
| sc.line40 | — | — | — | 4 |
| sc.line41 | — | — | — | — |
| sc.line42 | — | — | — | 4 |
| sc.f6 | — | — | — | 5 |
| sc.f14 | — | — | — | 6 |
| sc.f17 | — | — | — | 7 |
| sc.f19_y3 | — | — | — | 4 |
| sc.f19_y5 | — | — | — | 5 |
| sc.f19_y7 | — | — | — | 4 |
| sc.f19_y10 | — | — | — | 4 |
| sc.f19_y15 | — | — | — | 4 |
| sc.f19_y20 | — | — | — | 4 |
| sc.f19_y15sl | — | — | — | 5 |
| sc.f25_assets | — | — | — | 4 |
| sc.f25_veh | — | — | — | 4 |
| sc.f25 | — | — | — | 6 |
| sc.f26_assets | — | — | — | 4 |
| sc.f26_veh | — | — | — | 4 |
| sc.f26h | — | — | — | 7 |
| sc.f28 | — | — | — | 5 |
| sc.f29_assets | — | — | — | 4 |
| sc.f29_veh | — | — | — | 4 |
| sc.f29 | — | — | — | 5 |
| sc.s179_elected | — | — | — | 4 |
| sc.dep_other | — | — | — | 4 |
| sc.s179_return | — | — | — | 4 |
| sc.s179_allowed | — | — | — | 5 |
| sc.mq_q4_a | — | — | — | 4 |
| sc.mq_q4_v | — | — | — | 4 |
| sc.mq_q4 | — | — | — | 4 |
| sc.mq_total_a | — | — | — | 4 |
| sc.mq_total_v | — | — | — | 4 |
| sc.mq_total | — | — | — | 4 |
| sc.cost179_a | — | — | — | 4 |
| sc.cost179_v | — | — | — | 4 |
| sc.cost179 | — | — | — | 4 |
| sc.rent_equipment | — | — | — | — |
| sc.veh_lease | — | — | — | 4 |
| sc.profit_pos | — | — | — | 4 |
| sc.hi_uses | — | — | — | — |
| sc.hi_screen | — | — | — | — |
| sc.hi_screened | — | — | — | 4 |
| sc.f7206_line1 | — | — | — | 1 (stage14.sehi.refuse_ptc) |
| sc.f7206_line2 | — | — | — | 5 |
| sc.f7206_line3 | — | — | — | 4 |
| sc.f7206_line4 | — | — | — | 4 |
| sc.f7206_line5 | — | — | — | 4 |
| sc.f7206_has | — | — | — | 4 |
| sc.f7206_line7_pos | — | — | — | 4 |
| sc.f7206_line7 | — | — | — | 5 |
| sc.f7206_line8 | — | — | — | 4 |
| sc.f7206_line9_pos | — | — | — | 4 |
| sc.f7206_line9 | — | — | — | 5 |
| sc.f7206_line10 | — | — | — | 5 |
| sc.f7206_line13 | — | — | — | 4 |
| sc.f7206_min | — | — | — | 4 |
| sc.f7206_line14 | — | — | — | 10 |
| sc.qbi_has | — | — | — | 4 |
| sc.qbi_se_pos | — | — | — | 4 |
| sc.qbi_se | — | — | — | 4 |
| sc.qbi_plan_pos | — | — | — | 4 |
| sc.qbi_plan | — | — | — | 4 |
| sc.qbi_ded | — | — | — | 4 |
| sc.qbi | — | — | — | 7 |
| sc.tips_ot | — | — | — | — |

Unasserted lines: sc.one, sc.zero, sc.ho_multi, sc.ho_rate, sc.ho_cap_sqft

## Proof-of-concept scope screening

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| scope.schedule1 | — | — | — | — |
| scope.credits | — | — | — | — |
| scope.other_income | — | — | — | — |
| scope.other_line16 | — | — | — | — |
| scope.ready | — | — | — | 5 |

## Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| scveh.zero | — | — | — | — |
| scveh.method | — | — | — | — |
| scveh.owned | — | — | — | — |
| scveh.placed_date | — | — | — | — |
| scveh.miles_business | — | — | — | — |
| scveh.miles_commuting | — | — | — | — |
| scveh.miles_other | — | — | — | — |
| scveh.cent | — | — | — | — |
| scveh.bm_c | — | — | — | — |
| scveh.cm_c | — | — | — | 5 |
| scveh.om_c | — | — | — | — |
| scveh.nonbusiness_c | — | — | — | — |
| scveh.total_c | — | — | — | — |
| scveh.over_half | — | — | — | 6 |
| scveh.parking | — | — | — | — |
| scveh.smr_ok | — | — | — | — |
| scveh.smr_bad | — | — | — | 6 |
| scveh.rate | — | — | — | — |
| scveh.smr_amount | — | — | — | 7 |
| scveh.line9_standard | — | — | — | 6 |
| scveh.operating | — | — | — | — |
| scveh.operating_business | — | — | — | 6 |
| scveh.line9_actual | — | — | — | 6 |
| scveh.line9 | — | — | — | 11 |
| scveh.is_actual_owned | — | — | — | 6 |
| scveh.is_actual_leased | — | — | — | 6 |
| scveh.lease | — | — | — | — |
| scveh.lease_business | — | — | — | 6 |
| scveh.line20a | — | — | — | 6 |
| scveh.low_use | — | — | — | 6 |
| scveh.placed | — | — | — | 2 (stage14.veh.refuse_low_use, stage14.veh.refuse_half_use) |
| scveh.screen | — | — | — | — |
| scveh.screened | — | — | — | 6 |
| scveh.cost | — | — | — | 2 (stage14.veh.refuse_screen, stage14.veh.refuse_too_old) |
| scveh.passenger | — | — | — | — |
| scveh.suv | — | — | — | — |
| scveh.year | — | — | — | 6 |
| scveh.is2025 | — | — | — | 6 |
| scveh.is2019 | — | — | — | 6 |
| scveh.y5 | — | — | — | — |
| scveh.bus_cost | — | — | — | 3 |
| scveh.s179_elect | — | — | — | — |
| scveh.suv_cap | — | — | — | — |
| scveh.s179_bad | — | — | — | 6 |
| scveh.after_jan19 | — | — | — | — |
| scveh.bonus_choice | — | — | — | — |
| scveh.bonus_same | — | — | — | — |
| scveh.bonus_mixed | — | — | — | 6 |
| scveh.claims_bonus | — | — | — | 6 |
| scveh.rate40 | — | — | — | — |
| scveh.lim_first_bonus | — | — | — | 4 |
| scveh.lim_first_none | — | — | — | 5 |
| scveh.lim_2025 | — | — | — | 4 |
| scveh.lim_prior | — | — | — | 6 |
| scveh.line7 | — | — | — | 9 |
| scveh.line9w | — | — | — | 9 |
| scveh.s179_2025_ok | — | — | — | 8 |
| scveh.line10 | — | — | — | 7 |
| scveh.line10_2025 | — | — | — | 6 |
| scveh.s179_line10 | — | — | — | 6 |
| scveh.line11 | — | — | — | 7 |
| scveh.prior_179 | — | — | — | — |
| scveh.line14 | — | — | — | 6 |
| scveh.line15 | — | — | — | 5 |
| scveh.bonus_full | — | — | — | 5 |
| scveh.bonus_forty | — | — | — | 7 |
| scveh.bonus_fullcase | — | — | — | 4 |
| scveh.bonus_2025 | — | — | — | 6 |
| scveh.line16 | — | — | — | 8 |
| scveh.bonus_allowed | — | — | — | 8 |
| scveh.line17 | — | — | — | 7 |
| scveh.line18 | — | — | — | 4 |
| scveh.quarter | — | — | — | — |
| scveh.qconv | — | — | — | 6 |
| scveh.hy | — | — | — | — |
| scveh.prior_conv | — | — | — | — |
| scveh.rate_hy | — | — | — | 4 |
| scveh.rate_mq | — | — | — | 3 |
| scveh.rate_prior | — | — | — | 6 |
| scveh.line19_hy | — | — | — | 5 |
| scveh.line19_mq | — | — | — | 5 |
| scveh.line19_prior | — | — | — | 6 |
| scveh.line19 | — | — | — | 11 |
| scveh.line19_earlier | — | — | — | 6 |
| scveh.line19_2025 | — | — | — | 5 |
| scveh.line20 | — | — | — | 14 |
| scveh.b100 | — | — | — | 6 |
| scveh.k1 | — | — | — | — |
| scveh.r1 | — | — | — | 6 |
| scveh.t1 | — | — | — | 6 |
| scveh.l1 | — | — | — | 5 |
| scveh.t1s | — | — | — | 6 |
| scveh.d1 | — | — | — | 4 |
| scveh.k2 | — | — | — | — |
| scveh.r2 | — | — | — | 6 |
| scveh.t2 | — | — | — | 6 |
| scveh.l2 | — | — | — | 6 |
| scveh.d2 | — | — | — | 6 |
| scveh.k3 | — | — | — | — |
| scveh.r3 | — | — | — | 6 |
| scveh.t3 | — | — | — | 6 |
| scveh.l3 | — | — | — | 6 |
| scveh.d3 | — | — | — | 6 |
| scveh.k4 | — | — | — | — |
| scveh.r4 | — | — | — | 6 |
| scveh.t4 | — | — | — | 6 |
| scveh.l4 | — | — | — | 6 |
| scveh.d4 | — | — | — | 6 |
| scveh.k5 | — | — | — | — |
| scveh.r5 | — | — | — | 6 |
| scveh.t5 | — | — | — | 6 |
| scveh.l5 | — | — | — | 6 |
| scveh.d5 | — | — | — | 6 |
| scveh.k6 | — | — | — | — |
| scveh.r6 | — | — | — | 6 |
| scveh.t6 | — | — | — | 6 |
| scveh.l6 | — | — | — | 5 |
| scveh.d6 | — | — | — | 5 |
| scveh.d_total | — | — | — | 6 |
| scveh.unrecovered | — | — | — | 6 |
| scveh.post_amount | — | — | — | 3 |
| scveh.post | — | — | — | 5 |
| scveh.too_old | — | — | — | 6 |
| scveh.bonus_v | — | — | — | 6 |
| scveh.macrs_pass | — | — | — | 6 |
| scveh.macrs_heavy | — | — | — | 6 |
| scveh.macrs_v | — | — | — | 8 |
| scveh.bonus | — | — | — | 6 |
| scveh.macrs | — | — | — | 6 |
| scveh.s179_2025 | — | — | — | 6 |
| scveh.mq_q4 | — | — | — | 6 |
| scveh.mq_total | — | — | — | 6 |
| scveh.cost179 | — | — | — | 6 |
| scveh.bonus_o | — | — | — | 6 |
| scveh.macrs_o | — | — | — | 5 |
| scveh.s179_2025_o | — | — | — | 6 |
| scveh.q4_basis | — | — | — | 5 |
| scveh.mq_q4_o | — | — | — | 6 |
| scveh.mq_q4_a2 | — | — | — | 6 |
| scveh.mq_total_o | — | — | — | 6 |
| scveh.mq_total_a2 | — | — | — | 4 |
| scveh.cost179_o | — | — | — | 6 |
| scveh.cost179_a2 | — | — | — | 3 |

Unasserted lines: scveh.zero, scveh.cent, scveh.bm_c, scveh.om_c, scveh.nonbusiness_c, scveh.total_c, scveh.rate, scveh.y5, scveh.suv_cap, scveh.rate40, scveh.hy, scveh.k1, scveh.k2, scveh.k3, scveh.k4, scveh.k5, scveh.k6

## Schedule D — securities sales and supplied distribution subtotals

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sd.other_forms | — | — | — | — |
| sd.carryover | — | — | — | — |
| sd.distributions | — | — | — | — |
| sd.line18 | — | — | — | — |
| sd.line19 | — | — | — | — |
| sd.filing4952 | — | — | — | — |
| sd.investment_election | — | — | — | — |
| sd.count | — | — | — | 14 |
| sd.screen | — | — | — | — |
| sd.filed | — | — | — | 22 |
| sd.zero | — | — | — | — |
| sd.line1a.d | — | — | — | 18 |
| sd.line1a.e | — | — | — | 18 |
| sd.line1a.g | — | — | — | 18 |
| sd.line1a.h | — | — | — | 18 |
| sd.line1b.d | — | — | — | 18 |
| sd.line1b.e | — | — | — | 18 |
| sd.line1b.g | — | — | — | 18 |
| sd.line1b.h | — | — | — | 20 |
| sd.line2.d | — | — | — | 18 |
| sd.line2.e | — | — | — | 18 |
| sd.line2.g | — | — | — | 18 |
| sd.line2.h | — | — | — | 19 |
| sd.line3.d | — | — | — | 18 |
| sd.line3.e | — | — | — | 18 |
| sd.line3.g | — | — | — | 18 |
| sd.line3.h | — | — | — | 19 |
| sd.line8a.d | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 18 |
| sd.line8a.e | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 18 |
| sd.line8a.g | — | — | — | 18 |
| sd.line8a.h | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 18 |
| sd.line8b.d | — | — | — | 18 |
| sd.line8b.e | — | — | — | 18 |
| sd.line8b.g | — | — | — | 18 |
| sd.line8b.h | — | — | — | 19 |
| sd.line9.d | — | — | — | 18 |
| sd.line9.e | — | — | — | 18 |
| sd.line9.g | — | — | — | 18 |
| sd.line9.h | — | — | — | 19 |
| sd.line10.d | — | — | — | 18 |
| sd.line10.e | — | — | — | 18 |
| sd.line10.g | — | — | — | 18 |
| sd.line10.h | — | — | — | 19 |
| sd.line4 | — | — | — | 5 |
| sd.line5 | — | — | — | 5 |
| sd.line6 | — | — | — | 5 |
| sd.line11 | — | — | — | 5 |
| sd.line12 | — | — | — | 5 |
| sd.line14 | — | — | — | 5 |
| sd.line13 | — | — | — | 3 |
| sd.line7 | — | — | — | 5 |
| sd.line15 | — | — | — | 6 |
| sd.line16 | — | — | — | 24 |
| sd.line17 | — | — | — | 3 |
| sd.line20 | — | — | — | 1 (classm.sd.1) |
| sd.loss_limit | — | — | — | — |
| sd.limited_loss | — | — | — | — |
| sd.has_loss | — | — | — | — |
| sd.line21 | — | — | — | 21 |
| sd.line22 | — | — | — | 52 |
| sd.to1040 | — | — | — | — |
| sd.net_gain_raw | — | — | — | 1 (sales.loss.single.700000) |
| sd.net_gain | — | — | — | — |

Unasserted lines: sd.line18, sd.line19, sd.filing4952, sd.investment_election, sd.screen, sd.zero, sd.loss_limit, sd.limited_loss, sd.has_loss, sd.to1040, sd.net_gain

## Schedule D Tax Worksheet

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sdtw.zero | — | — | — | — |
| sdtw.ordinary_ceiling | — | — | — | — |
| sdtw.after22 | — | — | — | 1 (stage4.sdtw.skip22) |
| sdtw.after32 | — | — | — | 1 (stage4.sdtw.skip32) |
| sdtw.use1250 | — | — | — | — |
| sdtw.use28 | — | — | — | — |
| sdtw.line1 | — | — | — | 5 |
| sdtw.line2 | — | — | — | 5 |
| sdtw.line3 | — | — | — | 5 |
| sdtw.line4 | — | — | — | 5 |
| sdtw.line5 | — | — | — | 6 |
| sdtw.line6 | — | — | — | 6 |
| sdtw.line7 | — | — | — | 5 |
| sdtw.line8 | — | — | — | 5 |
| sdtw.line9 | — | — | — | 5 |
| sdtw.line10 | — | — | — | 5 |
| sdtw.line11 | — | — | — | 5 |
| sdtw.line12 | — | — | — | 5 |
| sdtw.line13 | — | — | — | 5 |
| sdtw.line14 | — | — | — | 5 |
| sdtw.line15 | — | — | — | 5 |
| sdtw.line16 | — | — | — | 5 |
| sdtw.line17 | — | — | — | 6 |
| sdtw.line18 | — | — | — | 5 |
| sdtw.line19 | — | — | — | 5 |
| sdtw.line20 | — | — | — | 5 |
| sdtw.line21 | — | — | — | 6 |
| sdtw.line22 | — | — | — | 5 |
| sdtw.raw23 | — | — | — | — |
| sdtw.line23 | — | — | — | 5 |
| sdtw.raw24 | — | — | — | — |
| sdtw.line24 | — | — | — | 5 |
| sdtw.raw25 | — | — | — | — |
| sdtw.line25 | — | — | — | 5 |
| sdtw.raw26 | — | — | — | — |
| sdtw.line26 | — | — | — | 5 |
| sdtw.raw27 | — | — | — | — |
| sdtw.line27 | — | — | — | 5 |
| sdtw.raw28 | — | — | — | — |
| sdtw.line28 | — | — | — | 5 |
| sdtw.raw29 | — | — | — | — |
| sdtw.line29 | — | — | — | 5 |
| sdtw.raw30 | — | — | — | — |
| sdtw.line30 | — | — | — | 6 |
| sdtw.raw31 | — | — | — | — |
| sdtw.line31 | — | — | — | 8 |
| sdtw.raw32 | — | — | — | — |
| sdtw.line32 | — | — | — | 5 |
| sdtw.raw33 | — | — | — | — |
| sdtw.line33 | — | — | — | 7 |
| sdtw.raw34 | — | — | — | — |
| sdtw.line34 | — | — | — | 6 |
| sdtw.raw35 | — | — | — | — |
| sdtw.line35 | — | — | — | 5 |
| sdtw.raw36 | — | — | — | — |
| sdtw.line36 | — | — | — | 5 |
| sdtw.raw37 | — | — | — | — |
| sdtw.line37 | — | — | — | 5 |
| sdtw.raw38 | — | — | — | — |
| sdtw.line38 | — | — | — | 6 |
| sdtw.raw39 | — | — | — | — |
| sdtw.line39 | — | — | — | 6 |
| sdtw.raw40 | — | — | — | — |
| sdtw.line40 | — | — | — | 6 |
| sdtw.raw41 | — | — | — | — |
| sdtw.line41 | — | — | — | 4 |
| sdtw.raw42 | — | — | — | — |
| sdtw.line42 | — | — | — | 5 |
| sdtw.raw43 | — | — | — | — |
| sdtw.line43 | — | — | — | 9 |
| sdtw.line44 | — | — | — | 3 |
| sdtw.line45 | — | — | — | 6 |
| sdtw.line46 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line47 | — | — | — | 6 |

Unasserted lines: sdtw.zero, sdtw.ordinary_ceiling, sdtw.use1250, sdtw.use28, sdtw.raw23, sdtw.raw24, sdtw.raw25, sdtw.raw26, sdtw.raw27, sdtw.raw28, sdtw.raw29, sdtw.raw30, sdtw.raw31, sdtw.raw32, sdtw.raw33, sdtw.raw34, sdtw.raw35, sdtw.raw36, sdtw.raw37, sdtw.raw38, sdtw.raw39, sdtw.raw40, sdtw.raw41, sdtw.raw42, sdtw.raw43

## Student Loan Interest Deduction Worksheet—Schedule 1, Line 21

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sli.zero | — | — | — | — |
| sli.interest | — | — | — | — |
| sli.has | — | — | — | — |
| sli.claimed | — | — | — | — |
| sli.max | — | — | — | — |
| sli.line1 | — | — | — | 6 |
| sli.line2 | — | — | — | 5 |
| sli.line3 | — | — | — | 6 |
| sli.line4 | — | — | — | 5 |
| sli.base_other | — | — | — | — |
| sli.base_joint | — | — | — | — |
| sli.line5 | — | — | — | 6 |
| sli.over | — | — | — | — |
| sli.line6 | — | — | — | 3 |
| sli.divisor_other | — | — | — | — |
| sli.divisor_joint | — | — | — | — |
| sli.divisor | — | — | — | — |
| sli.line8_figured | — | — | — | — |
| sli.line8 | — | — | — | 11 |
| sli.line9 | — | — | — | 4 |
| sli.eligible | — | — | — | — |
| sli.allowed | — | — | — | — |
| sli.deduction | — | — | — | 11 |

Unasserted lines: sli.zero, sli.has, sli.max, sli.base_other, sli.base_joint, sli.over, sli.divisor_other, sli.divisor_joint, sli.divisor, sli.line8_figured, sli.eligible, sli.allowed

## Social Security Benefits Worksheet—Lines 6a and 6b

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| ssb.benefits | — | — | — | — |
| ssb.pub915 | — | — | — | — |
| ssb.lump_sum | — | — | — | — |
| ssb.terror_disability | — | — | — | — |
| ssb.lived_apart | — | — | — | — |
| ssb.line1 | — | — | — | 5 |
| ssb.has_benefits | — | — | — | — |
| ssb.line2 | — | — | — | 5 |
| ssb.line3 | — | — | — | 6 |
| ssb.line4 | — | — | — | 5 |
| ssb.line5 | — | — | — | 5 |
| ssb.line6 | — | — | — | 6 |
| ssb.line7 | — | — | — | 7 |
| ssb.base_single | — | — | — | — |
| ssb.base_joint | — | — | — | — |
| ssb.zero | — | — | — | — |
| ssb.mfs_base | — | — | — | — |
| ssb.line8 | — | — | — | 6 |
| ssb.line9 | — | — | — | 7 |
| ssb.adjust_single | — | — | — | — |
| ssb.adjust_joint | — | — | — | — |
| ssb.mfs_adjust | — | — | — | — |
| ssb.line10 | — | — | — | 4 |
| ssb.line11 | — | — | — | 5 |
| ssb.line12 | — | — | — | 5 |
| ssb.line13 | — | — | — | 6 |
| ssb.line14 | — | — | — | 6 |
| ssb.line15 | — | — | — | 6 |
| ssb.mfs_together | — | — | — | — |
| ssb.line16_sum | — | — | — | — |
| ssb.line16_together | — | — | — | — |
| ssb.line16 | — | — | — | 7 |
| ssb.line17 | — | — | — | 5 |
| ssb.line18_figured | — | — | — | — |
| ssb.line18 | — | — | — | 5 |

Unasserted lines: ssb.has_benefits, ssb.base_single, ssb.base_joint, ssb.zero, ssb.mfs_base, ssb.adjust_single, ssb.adjust_joint, ssb.mfs_adjust, ssb.mfs_together, ssb.line16_sum, ssb.line16_together, ssb.line18_figured

## Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| tipjob.one | — | — | — | — |
| tipjob.qualified | — | — | — | — |
| tipjob.amount | — | — | — | — |
| tipjob.mixed | — | — | — | 1 (classm.tipjob.1) |
| tipjob.col_c | — | — | — | — |
| tipjob.col_d | — | — | — | 1 (classm.tipjob.1) |

Unasserted lines: tipjob.one, tipjob.col_c

## Unrecaptured Section 1250 Gain Worksheet — distribution-only path

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| u1250.line1 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line2 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line3 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line4 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line5 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line6 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line7 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line8 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line9 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line10 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line12 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line16 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line11 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line13 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line14 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.line15 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) |
| u1250.combined | — | — | — | — |
| u1250.line17 | — | — | — | 3 |
| u1250.line18 | — | — | — | 3 |

Unasserted lines: u1250.combined

## Form W-2 — wage, withholding and Social Security boxes by employer

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| w2.box1 | — | — | — | — |
| w2.box2 | — | — | — | — |
| w2.box3 | — | — | — | — |
| w2.box7 | — | — | — | — |
| w2.box4 | — | — | — | — |
| w2.wages | — | — | — | — |
| w2.one | — | — | — | — |
| w2.over | — | — | — | 1 (classm.w2.1) |
| w2.box5 | — | — | — | — |
| w2.box6 | — | — | — | — |

Unasserted lines: w2.wages, w2.one

## Schedule SE (Form 1040) — Self-Employment Tax, one per person

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| line2 | — | — | — | — |
| line8a | — | — | — | — |
| zero | — | — | — | — |
| line3 | — | — | — | — |
| positive | — | — | — | — |
| rate9235 | — | — | — | — |
| line3pos | — | — | — | — |
| line4a_pos | — | — | — | — |
| line4a | — | — | — | — |
| line4b | — | — | — | — |
| line4c_sum | — | — | — | — |
| floor | — | — | — | — |
| owes | — | — | — | — |
| line4c_owes | — | — | — | — |
| line4c | — | — | — | — |
| line5b | — | — | — | — |
| line6 | — | — | — | — |
| line7 | — | — | — | — |
| line8d | — | — | — | — |
| line9 | — | — | — | — |
| ss_base | — | — | — | — |
| rate124 | — | — | — | — |
| line10 | — | — | — | — |
| rate029 | — | — | — | — |
| line11 | — | — | — | — |
| line12 | — | — | — | — |
| rate50 | — | — | — | — |
| line13 | — | — | — | — |

Unasserted lines: zero, line3, positive, rate9235, line3pos, line4a_pos, line4a, line4b, line4c_sum, floor, owes, line4c_owes, line4c, line5b, line6, line7, line8d, line9, ss_base, rate124, line10, rate029, line11, line12, rate50, line13

## Tax on an amount — Tax Table or Tax Computation Worksheet

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| amount | — | — | — | — |
| status | — | — | — | — |
| below_boundary | — | — | — | — |
| table_tax | — | — | — | — |
| worksheet_tax | — | — | — | — |
| tax | — | — | — | — |

Unasserted lines: below_boundary, table_tax, worksheet_tax, tax

## Tax Computation Worksheet—Line 16

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| amount | — | — | — | — |
| status | — | — | — | — |
| single.row1.product | — | — | — | — |
| single.row1.tax | — | — | — | — |
| single.row2.product | — | — | — | — |
| single.row2.tax | — | — | — | — |
| single.row3.product | — | — | — | — |
| single.row3.tax | — | — | — | — |
| single.row4.product | — | — | — | — |
| single.row4.tax | — | — | — | — |
| single.row5.product | — | — | — | — |
| single.row5.tax | — | — | — | — |
| single.result | — | — | — | — |
| mfj.row1.product | — | — | — | — |
| mfj.row1.tax | — | — | — | — |
| mfj.row2.product | — | — | — | — |
| mfj.row2.tax | — | — | — | — |
| mfj.row3.product | — | — | — | — |
| mfj.row3.tax | — | — | — | — |
| mfj.row4.product | — | — | — | — |
| mfj.row4.tax | — | — | — | — |
| mfj.row5.product | — | — | — | — |
| mfj.row5.tax | — | — | — | — |
| mfj.result | — | — | — | — |
| mfs.row1.product | — | — | — | — |
| mfs.row1.tax | — | — | — | — |
| mfs.row2.product | — | — | — | — |
| mfs.row2.tax | — | — | — | — |
| mfs.row3.product | — | — | — | — |
| mfs.row3.tax | — | — | — | — |
| mfs.row4.product | — | — | — | — |
| mfs.row4.tax | — | — | — | — |
| mfs.row5.product | — | — | — | — |
| mfs.row5.tax | — | — | — | — |
| mfs.result | — | — | — | — |
| hoh.row1.product | — | — | — | — |
| hoh.row1.tax | — | — | — | — |
| hoh.row2.product | — | — | — | — |
| hoh.row2.tax | — | — | — | — |
| hoh.row3.product | — | — | — | — |
| hoh.row3.tax | — | — | — | — |
| hoh.row4.product | — | — | — | — |
| hoh.row4.tax | — | — | — | — |
| hoh.row5.product | — | — | — | — |
| hoh.row5.tax | — | — | — | — |
| hoh.result | — | — | — | — |
| tax | — | — | — | — |

Unasserted lines: single.row1.product, single.row1.tax, single.row2.product, single.row2.tax, single.row3.product, single.row3.tax, single.row4.product, single.row4.tax, single.row5.product, single.row5.tax, single.result, mfj.row1.product, mfj.row1.tax, mfj.row2.product, mfj.row2.tax, mfj.row3.product, mfj.row3.tax, mfj.row4.product, mfj.row4.tax, mfj.row5.product, mfj.row5.tax, mfj.result, mfs.row1.product, mfs.row1.tax, mfs.row2.product, mfs.row2.tax, mfs.row3.product, mfs.row3.tax, mfs.row4.product, mfs.row4.tax, mfs.row5.product, mfs.row5.tax, mfs.result, hoh.row1.product, hoh.row1.tax, hoh.row2.product, hoh.row2.tax, hoh.row3.product, hoh.row3.tax, hoh.row4.product, hoh.row4.tax, hoh.row5.product, hoh.row5.tax, hoh.result, tax

Unasserted computed lines across all documents: 504. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)
Asserted keys not matching a line id: person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line3, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.positive, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4a, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.owes, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4c, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line5b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line6, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line7, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line8d, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line9, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line10, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line11, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line12, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line13, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, qdcg.f1040.line15, qdcg.f1040.line3a, qdcg.f1040.status, f1040.qdcg.line25, qdcg.sd.distributions