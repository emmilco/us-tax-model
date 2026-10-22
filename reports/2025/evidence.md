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
| carloan.nonqualifying_debt | — | — | — | 3 |
| carloan.mixed_qualifying | — | — | — | 1 (classm.carloan.3) |
| carloan.refi_balance | — | — | — | — |
| carloan.refi_whole | — | — | — | — |
| carloan.refi_qualifying | — | — | — | 2 (classm.carloan.1, classm.carloan.2) |
| carloan.refi_nested | — | — | — | 4 |
| carloan.allocated | — | — | — | 4 |
| carloan.refi_interest | — | — | — | 3 |
| carloan.mixed_interest | — | — | — | 4 |
| carloan.mixed_prorated | — | — | — | 4 |
| carloan.qpvli | — | — | — | 4 |
| carloan.col_ii_input | — | — | — | — |
| carloan.col_ii | — | — | — | 4 |
| carloan.col_iii | — | — | — | 4 |

Unasserted lines: carloan.zero

## Form 2441, Part I — persons or organizations who provided the care, one entry per care provider

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| dcprov.one | — | — | — | — |
| dcprov.tin_kind | — | — | — | — |
| dcprov.household | — | — | — | — |
| dcprov.paid | — | — | — | — |
| dcprov.related | — | — | — | — |
| dcprov.see_statement | — | — | — | 1 (classm.dcprov.1) |

Unasserted lines: dcprov.one

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
| dependent.qc_relationship | — | — | — | 26 |
| dependent.younger | — | — | — | 18 |
| dependent.us_half | — | — | — | — |
| dependent.eic_ssn | — | — | — | — |
| dependent.qc_age | — | — | — | 23 |
| dependent.lived_half | — | — | — | 24 |
| dependent.qualifying_child | — | — | — | 29 |
| dependent.resident | — | — | — | 24 |
| dependent.qc_dependent | — | — | — | 29 |
| dependent.qr_relationship | — | — | — | 11 |
| dependent.qr_income | — | — | — | 11 |
| dependent.income_exception | — | — | — | 12 |
| dependent.qualifying_relative | — | — | — | 13 |
| dependent.qr_dependent | — | — | — | 13 |
| dependent.claimed | — | — | — | 29 |
| dependent.under_ctc_age | — | — | — | 20 |
| dependent.ctc_child | — | — | — | 29 |
| dependent.odc_person | — | — | — | 29 |
| dependent.ctc_per_child | — | — | — | — |
| dependent.ctc_amount | — | — | — | 29 |
| dependent.odc_per_dependent | — | — | — | — |
| dependent.odc_amount | — | — | — | 29 |
| dependent.actc_per_child | — | — | — | — |
| dependent.actc_amount | — | — | — | 29 |
| dependent.hoh_test2 | — | — | — | 29 |
| dependent.hoh_test1 | — | — | — | 28 |
| dependent.eic_child | — | — | — | 5 |
| dependent.eic_ssn_child | — | — | — | 5 |
| dependent.dc_child_all_year | — | — | — | 5 |
| dependent.dc_age13 | — | — | — | 5 |
| dependent.dc_under13 | — | — | — | — |
| dependent.dc_child | — | — | — | 5 |
| dependent.dc_incapable | — | — | — | — |
| dependent.dc_disabled_qp | — | — | — | 5 |
| dependent.dc_qp | — | — | — | 5 |
| dependent.dc_no_tin | — | — | — | 5 |
| dependent.dc_count | — | — | — | 1 (stage15.refuse.dependent.dc_no_tin) |
| dependent.dc_paid | — | — | — | — |
| dependent.dc_line2d | — | — | — | 2 (classm.dependent.5, stage15.refuse.dependent.dc_no_tin) |
| dependent.dc_line2c | — | — | — | 5 |

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
| eic.wsb_4b | — | — | — | 9 |
| eic.wsb_6 | — | — | — | 5 |
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
| eic.line3 | — | — | — | 3 |
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
| f1040.line1a | — | — | — | 24 |
| f1040.line1e | — | — | — | 18 |
| f1040.line1z | — | — | — | 31 |
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
| f1040.line6a | — | — | — | 6 |
| f1040.line6b | — | — | — | 21 |
| f1040.line6c | — | — | — | 5 |
| f1040.line6d | — | — | — | 6 |
| f1040.line7a | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 66 |
| f1040.line8 | — | — | — | 53 |
| f1040.line9 | — | — | — | 24 |
| f1040.line10 | — | — | — | 43 |
| f1040.line11a | — | — | — | 144 |
| f1040.line11b | — | — | — | 40 |
| f1040.line12e | — | — | — | 48 |
| f1040.line13a | — | — | — | 9 |
| f1040.line13b | — | — | — | 17 |
| f1040.line14 | — | — | — | 24 |
| f1040.line15 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 83 |
| f1040.gate.qdcg_applies | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 7 |
| f1040.gate.sdtw | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| f1040.line16 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 85 |
| f1040.line17 | — | — | — | 9 |
| f1040.line18 | — | — | — | 135 |
| f1040.line19 | — | — | — | 55 |
| f1040.line20 | — | — | — | 7 |
| f1040.line21 | — | — | — | 8 |
| f1040.line22 | — | — | — | 8 |
| f1040.line23 | — | — | — | 17 |
| f1040.line24 | — | — | — | 8 |
| f1040.line25a | — | — | — | 7 |
| f1040.line25b | — | — | — | 3 |
| f1040.line25c | — | — | — | 3 |
| f1040.line25d | — | — | — | 7 |
| f1040.line26 | — | — | — | 3 |
| f1040.line27a | — | — | — | 73 |
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

## Form 2441 — Child and Dependent Care Expenses (Parts I to III)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f2441.zero | — | — | — | — |
| f2441.benefits | — | — | — | — |
| f2441.care | — | — | — | — |
| f2441.filing | — | — | — | — |
| f2441.student_disabled | — | — | — | — |
| f2441.spouse_died | — | — | — | — |
| f2441.spouse_died_gate | — | — | — | — |
| f2441.nondependent | — | — | — | — |
| f2441.nondependent_gate | — | — | — | — |
| f2441.provider_count | — | — | — | — |
| f2441.related_count | — | — | — | — |
| f2441.provider_ineligible | — | — | — | — |
| f2441.line1_box | — | — | — | 6 |
| f2441.statement_count | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.statement_notice | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_count | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_notice | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.provider_paid | — | — | — | — |
| f2441.line1_paid | — | — | — | — |
| f2441.qp_count | — | — | — | 3 |
| f2441.line2_box | — | — | — | 7 |
| f2441.paid_total | — | — | — | 3 |
| f2441.limit_one | — | — | — | — |
| f2441.limit_two | — | — | — | — |
| f2441.two_or_more | — | — | — | — |
| f2441.limit | — | — | — | 1 (stage15.regress.f2441.nonqualifying_dependent) |
| f2441.line3_expenses | — | — | — | — |
| f2441.line3 | — | — | — | 33 |
| f2441.has_1e | — | — | — | — |
| f2441.box10_persons | — | — | — | — |
| f2441.one_box10 | — | — | — | — |
| f2441.attrib_gate | — | — | — | — |
| f2441.line4 | — | — | — | 35 |
| f2441.spouse_earned | — | — | — | — |
| f2441.line5 | — | — | — | 36 |
| f2441.joint | — | — | — | — |
| f2441.line6_34 | — | — | — | — |
| f2441.line6_345 | — | — | — | — |
| f2441.line6 | — | — | — | 32 |
| f2441.line7 | — | — | — | 31 |
| f2441.line8 | — | — | — | 31 |
| f2441.line9a | — | — | — | 32 |
| f2441.line9b | — | — | — | 7 |
| f2441.prior_year | — | — | — | — |
| f2441.line9c | — | — | — | 32 |
| f2441.clw1 | — | — | — | 15 |
| f2441.clw2 | — | — | — | 16 |
| f2441.clw3 | — | — | — | 15 |
| f2441.line10 | — | — | — | 31 |
| f2441.line11 | — | — | — | 36 |
| f2441.line12 | — | — | — | 13 |
| f2441.line13 | — | — | — | 7 |
| f2441.line14 | — | — | — | 7 |
| f2441.line15_sum | — | — | — | — |
| f2441.line14_bad | — | — | — | — |
| f2441.line15 | — | — | — | 14 |
| f2441.paid_2026 | — | — | — | — |
| f2441.line16 | — | — | — | 13 |
| f2441.line17 | — | — | — | 13 |
| f2441.line18 | — | — | — | 12 |
| f2441.spouse_earned_b | — | — | — | — |
| f2441.line19 | — | — | — | 13 |
| f2441.line20_17_18 | — | — | — | — |
| f2441.line20_all | — | — | — | — |
| f2441.line20 | — | — | — | 13 |
| f2441.plans_differ | — | — | — | — |
| f2441.employer_care | — | — | — | — |
| f2441.employer_care_gate | — | — | — | — |
| f2441.plan_max | — | — | — | — |
| f2441.exclusion_max | — | — | — | 1 (stage15.regress.f2441.exclusion_max) |
| f2441.line21 | — | — | — | 15 |
| f2441.line22 | — | — | — | 13 |
| f2441.line23 | — | — | — | 13 |
| f2441.line24_20_21 | — | — | — | — |
| f2441.line24 | — | — | — | 13 |
| f2441.line25 | — | — | — | 13 |
| f2441.line26 | — | — | — | 14 |
| f2441.line27 | — | — | — | 7 |
| f2441.line28 | — | — | — | 14 |
| f2441.line29 | — | — | — | 7 |
| f2441.line30 | — | — | — | 9 |
| f2441.line31 | — | — | — | 9 |

Unasserted lines: f2441.zero, f2441.filing, f2441.spouse_died_gate, f2441.nondependent_gate, f2441.provider_count, f2441.related_count, f2441.provider_ineligible, f2441.provider_paid, f2441.line1_paid, f2441.limit_one, f2441.limit_two, f2441.two_or_more, f2441.line3_expenses, f2441.has_1e, f2441.box10_persons, f2441.one_box10, f2441.attrib_gate, f2441.spouse_earned, f2441.joint, f2441.line6_34, f2441.line6_345, f2441.line15_sum, f2441.line14_bad, f2441.spouse_earned_b, f2441.line20_17_18, f2441.line20_all, f2441.employer_care_gate, f2441.line24_20_21

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

## Form 5695 — Residential Energy Credits (Parts I and II)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f5695.zero | — | — | — | — |
| f5695.part1_any | — | — | — | — |
| f5695.part2_any | — | — | — | — |
| f5695.business_use | — | — | — | — |
| f5695.construction_later | — | — | — | — |
| f5695.line1 | — | — | — | 6 |
| f5695.line2 | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line3 | — | — | — | — |
| f5695.line4 | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line5a | — | — | — | — |
| f5695.battery_cost | — | — | — | — |
| f5695.line5b | — | — | — | 8 |
| f5695.line6a | — | — | — | 17 |
| f5695.rce_rate | — | — | — | — |
| f5695.line6b | — | — | — | 15 |
| f5695.line7a | — | — | — | — |
| f5695.line11 | — | — | — | 8 |
| f5695.line12 | — | — | — | 1 (stage15.f5695.s5) |
| f5695.line13 | — | — | — | 16 |
| f5695.claiming_part1 | — | — | — | — |
| f5695.rce_ws1 | — | — | — | 9 |
| f5695.ctc_line19 | — | — | — | — |
| f5695.ctc | — | — | — | — |
| f5695.rce_ws2 | — | — | — | 10 |
| f5695.rce_ws3 | — | — | — | 9 |
| f5695.line14 | — | — | — | 15 |
| f5695.line15 | — | — | — | 16 |
| f5695.line16 | — | — | — | 13 |
| f5695.line17a | — | — | — | — |
| f5695.line17b | — | — | — | — |
| f5695.line17c | — | — | — | — |
| f5695.sec_a_claimed | — | — | — | — |
| f5695.line17e | — | — | — | — |
| f5695.sec_a_new_home | — | — | — | — |
| f5695.eehi_rate | — | — | — | — |
| f5695.line18a | — | — | — | 6 |
| f5695.ins_30 | — | — | — | — |
| f5695.insulation_max | — | — | — | — |
| f5695.ins_capped | — | — | — | — |
| f5695.line18b | — | — | — | 14 |
| f5695.line19a | — | — | — | 4 |
| f5695.door1_30 | — | — | — | — |
| f5695.door_max | — | — | — | — |
| f5695.line19c | — | — | — | 11 |
| f5695.line19d_i | — | — | — | — |
| f5695.line19d_ii | — | — | — | — |
| f5695.line19e | — | — | — | 4 |
| f5695.line19f | — | — | — | 11 |
| f5695.line19g | — | — | — | 11 |
| f5695.doors_sum | — | — | — | — |
| f5695.doors_max | — | — | — | — |
| f5695.doors_cost | — | — | — | — |
| f5695.qmid_doors | — | — | — | — |
| f5695.doors_no_qmid | — | — | — | — |
| f5695.doors_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line19h | — | — | — | 11 |
| f5695.line20a_i | — | — | — | — |
| f5695.line20a_ii | — | — | — | — |
| f5695.line20a_iii | — | — | — | — |
| f5695.line20a_iv | — | — | — | — |
| f5695.line20b | — | — | — | 4 |
| f5695.line20c | — | — | — | 11 |
| f5695.windows_30 | — | — | — | — |
| f5695.windows_max | — | — | — | — |
| f5695.qmid_windows | — | — | — | — |
| f5695.windows_no_qmid | — | — | — | — |
| f5695.windows_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line20d | — | — | — | 11 |
| f5695.line21a | — | — | — | — |
| f5695.line21b | — | — | — | — |
| f5695.sec_b_claimed | — | — | — | — |
| f5695.b_new_home | — | — | — | — |
| f5695.sec_b_new_home | — | — | — | — |
| f5695.item_max | — | — | — | — |
| f5695.line22a | — | — | — | 3 |
| f5695.line22b | — | — | — | 3 |
| f5695.line22c | — | — | — | 9 |
| f5695.ac_30 | — | — | — | — |
| f5695.qmid_ac | — | — | — | — |
| f5695.ac_no_qmid | — | — | — | — |
| f5695.ac_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line22d | — | — | — | 10 |
| f5695.line23a_i | — | — | — | — |
| f5695.line23a_ii | — | — | — | — |
| f5695.line23b | — | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line23c | — | — | — | 8 |
| f5695.wh_30 | — | — | — | — |
| f5695.qmid_wh | — | — | — | — |
| f5695.wh_no_qmid | — | — | — | — |
| f5695.wh_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line23d | — | — | — | 9 |
| f5695.line24a | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24b | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24c | — | — | — | 9 |
| f5695.furnace_30 | — | — | — | — |
| f5695.qmid_furnace | — | — | — | — |
| f5695.furnace_no_qmid | — | — | — | — |
| f5695.furnace_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line24d | — | — | — | 9 |
| f5695.line25a | — | — | — | — |
| f5695.enabling_claimed | — | — | — | — |
| f5695.line25c | — | — | — | 2 (stage15.f5695-2.e6, stage15.f5695-2.e7) |
| f5695.enabling_30 | — | — | — | — |
| f5695.qmid_enabling | — | — | — | — |
| f5695.enabling_no_qmid | — | — | — | — |
| f5695.enabling_capped | — | — | — | 2 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp, stage15.regress.f5695.enabling_cap) |
| f5695.line25e | — | — | — | 10 |
| f5695.line26a | — | — | — | — |
| f5695.line26b | — | — | — | 2 (stage15.f5695.s6, stage15.f5695-2.e9) |
| f5695.audit_30 | — | — | — | — |
| f5695.audit_max | — | — | — | — |
| f5695.audit_capped | — | — | — | — |
| f5695.line26c | — | — | — | 10 |
| f5695.line27 | — | — | — | 29 |
| f5695.annual_max | — | — | — | — |
| f5695.line28 | — | — | — | 29 |
| f5695.line29a | — | — | — | 4 |
| f5695.line29b | — | — | — | 5 |
| f5695.line29c | — | — | — | 1 (stage15.f5695-2.e10) |
| f5695.line29d | — | — | — | 3 |
| f5695.line29e | — | — | — | — |
| f5695.line29f | — | — | — | 3 |
| f5695.line29g | — | — | — | 12 |
| f5695.hp_30 | — | — | — | — |
| f5695.heat_pump_max | — | — | — | — |
| f5695.qmid_hp | — | — | — | — |
| f5695.hp_no_qmid | — | — | — | — |
| f5695.hp_capped | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line29h | — | — | — | 12 |
| f5695.joint_occupancy | — | — | — | — |
| f5695.separate_homes | — | — | — | — |
| f5695.separate_homes_joint | — | — | — | — |
| f5695.line30 | — | — | — | 32 |
| f5695.eehi_ws1 | — | — | — | 20 |
| f5695.eehi_ws2 | — | — | — | 21 |
| f5695.eehi_ws3 | — | — | — | 20 |
| f5695.line31 | — | — | — | 27 |
| f5695.line32 | — | — | — | 27 |
| f5695.line32a | — | — | — | 7 |
| f5695.condo | — | — | — | — |
| f5695.line32b | — | — | — | 7 |

Unasserted lines: f5695.zero, f5695.rce_rate, f5695.claiming_part1, f5695.ctc_line19, f5695.ctc, f5695.sec_a_claimed, f5695.sec_a_new_home, f5695.eehi_rate, f5695.ins_30, f5695.insulation_max, f5695.ins_capped, f5695.door1_30, f5695.door_max, f5695.doors_sum, f5695.doors_max, f5695.doors_cost, f5695.doors_no_qmid, f5695.windows_30, f5695.windows_max, f5695.windows_no_qmid, f5695.sec_b_claimed, f5695.sec_b_new_home, f5695.item_max, f5695.ac_30, f5695.ac_no_qmid, f5695.wh_30, f5695.wh_no_qmid, f5695.furnace_30, f5695.furnace_no_qmid, f5695.enabling_claimed, f5695.enabling_30, f5695.enabling_no_qmid, f5695.audit_30, f5695.audit_max, f5695.audit_capped, f5695.annual_max, f5695.hp_30, f5695.heat_pump_max, f5695.hp_no_qmid, f5695.separate_homes_joint

## Form 8606 — Nondeductible IRAs, Part I (nondeductible contributions with no 2025 distribution), one per person

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8606.files | — | — | — | 1 (classm.f8606.1) |
| f8606.line1 | — | — | — | 7 |
| f8606.line2 | — | — | — | 7 |
| f8606.line3 | — | — | — | 8 |
| f8606.dist | — | — | — | — |
| f8606.line14 | — | — | — | 8 |

Unasserted lines: f8606.dist

## Form 8880 — Credit for Qualified Retirement Savings Contributions (the saver's credit)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8880.zero | — | — | — | — |
| f8880.joint | — | — | — | — |
| f8880.line1a | — | — | — | 37 |
| f8880.line1b | — | — | — | 12 |
| f8880.line2a | — | — | — | 36 |
| f8880.line2b | — | — | — | 13 |
| f8880.line3a | — | — | — | 36 |
| f8880.line3b | — | — | — | 12 |
| f8880.dist_2025 | — | — | — | — |
| f8880.prior_joint_sum | — | — | — | — |
| f8880.prior_joint | — | — | — | — |
| f8880.prior_own_a | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.prior_own_b | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.line4a | — | — | — | 38 |
| f8880.line4b_joint | — | — | — | — |
| f8880.line4b | — | — | — | 14 |
| f8880.line5a | — | — | — | 37 |
| f8880.line5b | — | — | — | 13 |
| f8880.cap | — | — | — | — |
| f8880.inelig_a | — | — | — | — |
| f8880.inelig_b | — | — | — | — |
| f8880.elig_a | — | — | — | — |
| f8880.elig_b | — | — | — | — |
| f8880.line6a_figured | — | — | — | — |
| f8880.line6b_figured | — | — | — | — |
| f8880.line6a | — | — | — | 37 |
| f8880.line6b | — | — | — | 13 |
| f8880.line7 | — | — | — | 37 |
| f8880.line8 | — | — | — | 34 |
| f8880.line9 | — | — | — | 34 |
| f8880.line10 | — | — | — | 31 |
| f8880.clw1 | — | — | — | 27 |
| f8880.clw2 | — | — | — | 27 |
| f8880.clw3 | — | — | — | 27 |
| f8880.line11 | — | — | — | 30 |
| f8880.agi_limit | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line3_total | — | — | — | — |
| f8880.can_take | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line12_figured | — | — | — | — |
| f8880.line12 | — | — | — | 32 |

Unasserted lines: f8880.zero, f8880.joint, f8880.dist_2025, f8880.prior_joint_sum, f8880.prior_joint, f8880.line4b_joint, f8880.cap, f8880.inelig_a, f8880.inelig_b, f8880.elig_a, f8880.elig_b, f8880.line6a_figured, f8880.line6b_figured, f8880.line3_total, f8880.line12_figured

## Form 8889 — Health Savings Accounts (Parts I and II)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8889.one | — | — | — | — |
| f8889.zero | — | — | — | — |
| f8889.line2 | — | — | — | 1 (stage16.mut.hsa_contrib_and_dist) |
| f8889.line9 | — | — | — | — |
| f8889.any | — | — | — | 5 |
| f8889.unsupported | — | — | — | — |
| f8889.mfs | — | — | — | 5 |
| f8889.months_eligible | — | — | — | — |
| f8889.months_family | — | — | — | — |
| f8889.bad_months | — | — | — | 9 |
| f8889.age55 | — | — | — | — |
| f8889.twelve | — | — | — | — |
| f8889.married_family | — | — | — | 5 |
| f8889.age55_line3 | — | — | — | 5 |
| f8889.self_amount | — | — | — | 5 |
| f8889.self_under55 | — | — | — | — |
| f8889.self_55 | — | — | — | — |
| f8889.age55_unmarried | — | — | — | 5 |
| f8889.family_amount | — | — | — | 5 |
| f8889.family_under55 | — | — | — | — |
| f8889.family_55 | — | — | — | — |
| f8889.family_extra | — | — | — | 5 |
| f8889.chart_self | — | — | — | 5 |
| f8889.chart_family | — | — | — | 5 |
| f8889.chart_total | — | — | — | 5 |
| f8889.chart_limit | — | — | — | 5 |
| f8889.all_year | — | — | — | 5 |
| f8889.changed | — | — | — | 5 |
| f8889.dec_coverage | — | — | — | — |
| f8889.dec_amount | — | — | — | 5 |
| f8889.last_month | — | — | — | — |
| f8889.use_last_month | — | — | — | 5 |
| f8889.line3_changed | — | — | — | 5 |
| f8889.line3_all_year | — | — | — | 4 |
| f8889.line3_last_month | — | — | — | 5 |
| f8889.line3_part_year | — | — | — | 4 |
| f8889.line3 | — | — | — | 16 |
| f8889.line4 | — | — | — | 5 |
| f8889.line5 | — | — | — | 5 |
| f8889.family_year | — | — | — | 4 |
| f8889.family_dec_year | — | — | — | 5 |
| f8889.family_counted | — | — | — | 5 |
| f8889.step1_total | — | — | — | 5 |
| f8889.step1_line3 | — | — | — | 5 |
| f8889.step1 | — | — | — | 8 |
| f8889.step1_x2 | — | — | — | 5 |
| f8889.two | — | — | — | — |
| f8889.share_equal | — | — | — | 5 |
| f8889.allocation | — | — | — | — |
| f8889.allocated | — | — | — | — |
| f8889.share_raw | — | — | — | 4 |
| f8889.allocation_bad | — | — | — | 5 |
| f8889.share | — | — | — | 6 |
| f8889.self_year | — | — | — | 5 |
| f8889.self_counted | — | — | — | 5 |
| f8889.self_all | — | — | — | 5 |
| f8889.self_family_months | — | — | — | 5 |
| f8889.self_dec_year | — | — | — | 5 |
| f8889.self_in_family | — | — | — | 5 |
| f8889.step4_total | — | — | — | 5 |
| f8889.step4 | — | — | — | 7 |
| f8889.line6_split | — | — | — | 4 |
| f8889.split | — | — | — | 5 |
| f8889.line6 | — | — | — | 13 |
| f8889.additional | — | — | — | — |
| f8889.line7_year | — | — | — | 5 |
| f8889.line7_counted | — | — | — | 5 |
| f8889.line7_total | — | — | — | 5 |
| f8889.line7_worksheet | — | — | — | 5 |
| f8889.line7_applies | — | — | — | 5 |
| f8889.line7 | — | — | — | 8 |
| f8889.line8 | — | — | — | 7 |
| f8889.line10 | — | — | — | 5 |
| f8889.line11 | — | — | — | 5 |
| f8889.line12 | — | — | — | 7 |
| f8889.excess | — | — | — | 5 |
| f8889.line13_figured | — | — | — | 5 |
| f8889.line13 | — | — | — | 23 |
| f8889.line14a | — | — | — | 6 |
| f8889.has_dist | — | — | — | 5 |
| f8889.rollover | — | — | — | — |
| f8889.rollover_bad | — | — | — | 5 |
| f8889.line14b | — | — | — | 11 |
| f8889.line14c | — | — | — | 12 |
| f8889.medical | — | — | — | — |
| f8889.line15 | — | — | — | 11 |
| f8889.line16_figured | — | — | — | 6 |
| f8889.line16 | — | — | — | 13 |
| f8889.has_taxable | — | — | — | 5 |
| f8889.line17a | — | — | — | 4 |
| f8889.subject_part | — | — | — | — |
| f8889.subject_bad | — | — | — | 5 |
| f8889.subject_excepted | — | — | — | 6 |
| f8889.subject | — | — | — | 6 |
| f8889.line17b_figured | — | — | — | 5 |
| f8889.line17b | — | — | — | 11 |

Unasserted lines: f8889.one, f8889.zero, f8889.twelve, f8889.self_under55, f8889.self_55, f8889.family_under55, f8889.family_55, f8889.two, f8889.additional

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
| f8959.line7 | — | — | — | 6 |
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
| f8960.line2 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) |
| f8960.line3 | — | — | — | 5 |
| f8960.line4a | — | — | — | 5 |
| f8960.line4b | — | — | — | 5 |
| f8960.line5b | — | — | — | 5 |
| f8960.line5c | — | — | — | 5 |
| f8960.line6 | — | — | — | 5 |
| f8960.line7 | — | — | — | 5 |
| f8960.line9c | — | — | — | 5 |
| f8960.line10 | — | — | — | 6 |
| f8960.line4c | — | — | — | 2 (classm.f8960.1, classm.f8960.2) |
| f8960.line5a | — | — | — | 3 |
| f8960.line5d | — | — | — | 2 (classm.f8960.1, classm.f8960.2) |
| f8960.line8 | — | — | — | 4 |
| f8960.line9a | — | — | — | 5 |
| f8960.line9b | — | — | — | 5 |
| f8960.line9d | — | — | — | 3 |
| f8960.line11 | — | — | — | 4 |
| f8960.line12 | — | — | — | 6 |
| f8960.line13 | — | — | — | 6 |
| f8960.line14 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) |
| f8960.line15 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) |
| f8960.line16 | — | — | — | 3 |
| f8960.line17 | — | — | — | 22 |
| f8960.bad_allocation | — | — | — | — |

Unasserted lines: f8960.zero, f8960.bad_allocation

## Form 8995 — Qualified Business Income Deduction Simplified Computation

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | 6 |
| f8995.line3 | — | — | — | 4 |
| f8995.line4_sum | — | — | — | — |
| f8995.line4 | — | — | — | 5 |
| f8995.line5 | — | — | — | 5 |
| f8995.line7 | — | — | — | 3 |
| f8995.loss | — | — | — | — |
| f8995.line16 | — | — | — | 4 |
| f8995.line17 | — | — | — | 3 |
| f8995.line6 | — | — | — | 3 |
| f8995.line8 | — | — | — | 3 |
| f8995.line9 | — | — | — | 3 |
| f8995.line10 | — | — | — | 3 |
| f8995.line11 | — | — | — | 3 |
| f8995.line12 | — | — | — | 3 |
| f8995.line13 | — | — | — | 3 |
| f8995.line14 | — | — | — | 4 |
| f8995.line15 | — | — | — | 11 |

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
| interest.penalty | — | — | — | — |

## IRA Deduction Worksheet — Schedule 1, Line 20

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| ira.zero | — | — | — | — |
| ira.joint | — | — | — | — |
| ira.joint_type | — | — | — | — |
| ira.contrib_total | — | — | — | — |
| ira.roth_total | — | — | — | — |
| ira.any_trad | — | — | — | — |
| ira.cov_count | — | — | — | — |
| ira.anyone_covered | — | — | — | — |
| ira.lines2to6 | — | — | — | — |
| ira.cov_gate | — | — | — | — |
| ira.cov_you | — | — | — | — |
| ira.cov_spouse | — | — | — | — |
| ira.line1a | — | — | — | 14 |
| ira.line1b | — | — | — | 5 |
| ira.line2a_sum | — | — | — | — |
| ira.line2b_sum | — | — | — | — |
| ira.line2a | — | — | — | 9 |
| ira.line2b | — | — | — | 3 |
| ira.line3 | — | — | — | 8 |
| ira.line4 | — | — | — | 8 |
| ira.line5 | — | — | — | 2 (classm.ira.2, stage16.mut.ira_joint_full_edge) |
| ira.line6a_sum | — | — | — | — |
| ira.line6b_sum | — | — | — | — |
| ira.line6a | — | — | — | 9 |
| ira.line6b | — | — | — | 4 |
| ira.line7a_sum | — | — | — | — |
| ira.line7b_sum | — | — | — | — |
| ira.line7a | — | — | — | 17 |
| ira.line7b | — | — | — | 8 |
| ira.wages | — | — | — | — |
| ira.line8 | — | — | — | 12 |
| ira.line9 | — | — | — | 12 |
| ira.line10 | — | — | — | 18 |
| ira.age50_count | — | — | — | — |
| ira.kbh_none | — | — | — | — |
| ira.kbh_one | — | — | — | — |
| ira.kbh_both | — | — | — | — |
| ira.kbh_amount | — | — | — | — |
| ira.kbh_short | — | — | — | — |
| ira.both_kinds | — | — | — | — |
| ira.all_total | — | — | — | — |
| ira.over_comp | — | — | — | — |
| ira.special | — | — | — | — |
| ira.se_capital | — | — | — | — |
| ira.se_capital_gate | — | — | — | — |
| ira.special_gate | — | — | — | — |
| ira.combat_gate | — | — | — | — |
| ira.excl_gate | — | — | — | — |
| ira.line11a | — | — | — | 17 |
| ira.line11b | — | — | — | 8 |
| ira.line12a | — | — | — | 19 |
| ira.line12b | — | — | — | 8 |
| ira.total | — | — | — | 1 (stage16.refuse.ira.deduct_less) |
| ira.deduct_less | — | — | — | — |
| ira.less_gate | — | — | — | — |
| ira.line20 | — | — | — | 10 |
| ira.basis_total | — | — | — | — |

Unasserted lines: ira.zero, ira.joint, ira.joint_type, ira.contrib_total, ira.roth_total, ira.any_trad, ira.cov_count, ira.anyone_covered, ira.lines2to6, ira.cov_gate, ira.cov_you, ira.cov_spouse, ira.line2a_sum, ira.line2b_sum, ira.line6a_sum, ira.line6b_sum, ira.line7a_sum, ira.line7b_sum, ira.wages, ira.age50_count, ira.kbh_none, ira.kbh_one, ira.kbh_both, ira.kbh_amount, ira.kbh_short, ira.both_kinds, ira.all_total, ira.over_comp, ira.se_capital_gate, ira.special_gate, ira.combat_gate, ira.excl_gate, ira.less_gate, ira.basis_total

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

## Schedule 1, line 8z — other income, one entry per item listed

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| oi8z.kind | — | — | — | — |
| oi8z.amount | — | — | — | — |
| oi8z.recovery | — | — | — | 1 (classm.oi8z.1) |
| oi8z.additional_tax | — | — | — | 1 (classm.oi8z.1) |
| oi8z.figured | — | — | — | 1 (classm.oi8z.1) |
| oi8z.taxable | — | — | — | 4 |

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
| person.has_educator_expenses | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.educator_limited | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.educator_eligible_amount | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.educator_deduction | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_forms | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_repeated | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_split | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_agreed | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_step1 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_share | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_deduction | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_taxable | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.hsa_addtax | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.tip_employers | — | — | — | 1 (classm.person.1) |
| person.tip_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.tip_reported | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ot_employers | — | — | — | 1 (classm.person.1) |
| person.ot_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.rrta | — | — | — | — |
| person.sc_rrta_count | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.se_rrta | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.employers | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.overcount | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.over | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.wages | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.withheld | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.box1 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.box2 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.eligible | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.excess | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.zero | — | — | — | — |
| person.credit | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.medicare5 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.medicare6 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sc_count | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ho_count | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.mq_q4 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.mq_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.cost179 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.s179_nonlisted | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.s179_listed | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.income179 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.has_sc | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sc_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.se_screen | — | — | — | — |
| person.se_screened | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.se_line2 | — | — | — | 4 |
| person.se_line6 | — | — | — | 4 |
| person.se_line12 | — | — | — | 11 |
| person.se_line13 | — | — | — | 1 (stage14.refuse.se_railroad) |
| person.se_line4c | — | — | — | 1 (stage14.refuse.se_railroad) |
| person.plan | — | — | — | — |
| person.plan_screen | — | — | — | — |
| person.plan_screened | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.cent | — | — | — | — |
| person.hundred | — | — | — | — |
| person.sep_rate | — | — | — | — |
| person.sep_contrib | — | — | — | 1 (stage14.plan.refuse_screen) |
| person.sep_rate_c | — | — | — | — |
| person.sep_rate_plus | — | — | — | — |
| person.sep_s1 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sep_s2 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sep_s3 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sep_s5 | — | — | — | 4 |
| person.comp_limit | — | — | — | — |
| person.sep_s6 | — | — | — | 3 |
| person.sep_s7 | — | — | — | 3 |
| person.sep_s8 | — | — | — | — |
| person.sep_s21 | — | — | — | 5 |
| person.sep_excess | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sep_deduction | — | — | — | 4 |
| person.simple_deferral | — | — | — | 1 (stage14.plan.refuse_screen_simple) |
| person.simple_age | — | — | — | — |
| person.simple_kind | — | — | — | — |
| person.simple_employer | — | — | — | — |
| person.simple_comp | — | — | — | 3 |
| person.simple_cap | — | — | — | — |
| person.simple_regular | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.simple_catchup | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.catchup_limit | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.comp_after_regular | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.catchup_max | — | — | — | 4 |
| person.rate3 | — | — | — | — |
| person.rate2 | — | — | — | — |
| person.match_3pct | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.deferrals_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.match_max | — | — | — | 4 |
| person.ne_comp | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ne_max | — | — | — | 4 |
| person.employer_max | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.simple_excess | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.simple_deduction | — | — | — | 6 |
| person.plan_deduction | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.s16 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.positive_profits | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sehi | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.qbi | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.eic_part1 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.files_se | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.eic_se_has | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.eic_se | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sc_1a | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_benefits | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_box10 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_has_box10 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_1e_mine | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_1e_counted | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_zero | — | — | — | — |
| person.dc_1e | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_earned | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.dc_earned_b | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sav_born | — | — | — | — |
| person.sav_student | — | — | — | — |
| person.sav_claimed | — | — | — | — |
| person.sav_ineligible | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sav_trad | — | — | — | — |
| person.sav_able | — | — | — | — |
| person.sav_roth | — | — | — | — |
| person.sav_line1 | — | — | — | 4 |
| person.sav_w2 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sav_excess | — | — | — | — |
| person.sav_excess_gate | — | — | — | 1 (classm.person.1) |
| person.sav_voluntary | — | — | — | — |
| person.sav_simple_plan | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sav_simple | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.sav_line2 | — | — | — | 3 |
| person.sav_prior_joint | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.sav_prior_other | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.ira_trad | — | — | — | — |
| person.ira_contrib | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_has | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_any_contrib | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_excess | — | — | — | — |
| person.ira_excess_gate | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_age50 | — | — | — | — |
| person.ira_work_plan | — | — | — | — |
| person.ira_se_plan | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_cov | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_limit_under50 | — | — | — | — |
| person.ira_limit_over50 | — | — | — | — |
| person.ira_limit | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_not_covered_joint | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_line2_status | — | — | — | — |
| person.ira_line2_nc | — | — | — | — |
| person.ira_line2 | — | — | — | 1 (classm.person.1) |
| person.ira_line6 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_line6_yes | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_wide | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_full_narrow | — | — | — | — |
| person.ira_full_joint | — | — | — | — |
| person.ira_full | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_at_full | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_p70 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_p80 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_p35 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_p40 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_prod_wide | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_prod_joint | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_prod | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_rounded | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_min | — | — | — | — |
| person.ira_floor | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_below | — | — | — | 1 (classm.person.2) |
| person.ira_line7_figured | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_line7 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_over_limit | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_own_total | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_line11 | — | — | — | 10 |
| person.ira_7or10 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_line12 | — | — | — | 3 |
| person.ira_deduction | — | — | — | 3 |
| person.ira_10or11 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_nd_figured | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_nondeductible | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_files_8606 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_basis | — | — | — | — |
| person.ira_basis_adjusted | — | — | — | — |
| person.ira_basis_gate | — | — | — | — |
| person.ira_8606_line2 | — | — | — | 3 |
| person.ira_dist | — | — | — | — |
| person.ira_dist_gate | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_8606_line14 | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_ssb_lim | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_ssb_figured | — | — | — | 3 |
| person.ira_ssb | — | — | — | 3 |
| person.ira_se_take | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_se_figured | — | — | — | 2 (classm.person.1, classm.person.2) |
| person.ira_se | — | — | — | 2 (classm.person.1, classm.person.2) |

Unasserted lines: person.one, person.educator_max, person.zero, person.cent, person.hundred, person.sep_rate_c, person.sep_rate_plus, person.comp_limit, person.sep_s8, person.simple_cap, person.rate3, person.rate2, person.dc_zero, person.ira_limit_under50, person.ira_limit_over50, person.ira_line2_status, person.ira_line2_nc, person.ira_full_narrow, person.ira_full_joint, person.ira_min, person.ira_basis_gate

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

## State and Local Income Tax Refund Worksheet—Schedule 1, Line 1

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| refund.zero | — | — | — | — |
| refund.received | — | — | — | — |
| refund.has | — | — | — | — |
| refund.box8 | — | — | — | — |
| refund.not_2024 | — | — | — | — |
| refund.itemized | — | — | — | — |
| refund.sales | — | — | — | — |
| refund.worksheet | — | — | — | — |
| refund.exc_tax | — | — | — | — |
| refund.exc_who | — | — | — | — |
| refund.line5d_2024 | — | — | — | — |
| refund.line5e_2024 | — | — | — | — |
| refund.line5e_bad | — | — | — | — |
| refund.line1 | — | — | — | 13 |
| refund.line2_more | — | — | — | 2 (stage16.mut.refund_single_unasked, stage16.mut.refund_line3_stop) |
| refund.line2 | — | — | — | 6 |
| refund.line3_more | — | — | — | 1 (stage16.mut.refund_line3_stop) |
| refund.line3 | — | — | — | 10 |
| refund.line17_2024 | — | — | — | — |
| refund.line4 | — | — | — | 9 |
| refund.status | — | — | — | — |
| refund.mfs_spouse_itemized | — | — | — | — |
| refund.std_single | — | — | — | — |
| refund.std_joint | — | — | — | — |
| refund.std_hoh | — | — | — | — |
| refund.line5 | — | — | — | 9 |
| refund.box_married | — | — | — | — |
| refund.box_unmarried | — | — | — | — |
| refund.per_box | — | — | — | — |
| refund.you_born | — | — | — | — |
| refund.you_blind | — | — | — | — |
| refund.spouse_born | — | — | — | — |
| refund.spouse_blind | — | — | — | — |
| refund.spouse_boxes | — | — | — | — |
| refund.amt_you_born | — | — | — | — |
| refund.amt_you_blind | — | — | — | — |
| refund.amt_spouse_born | — | — | — | — |
| refund.amt_spouse_born_checked | — | — | — | — |
| refund.amt_spouse_blind | — | — | — | — |
| refund.amt_spouse_blind_checked | — | — | — | — |
| refund.line6 | — | — | — | 9 |
| refund.line7 | — | — | — | 9 |
| refund.line8_figured | — | — | — | — |
| refund.line8 | — | — | — | 8 |
| refund.line8_mfs | — | — | — | — |
| refund.line9_figured | — | — | — | — |
| refund.line9 | — | — | — | 9 |
| refund.taxable | — | — | — | 4 |

Unasserted lines: refund.zero, refund.has, refund.worksheet, refund.line5e_bad, refund.std_single, refund.std_joint, refund.std_hoh, refund.box_married, refund.box_unmarried, refund.per_box, refund.spouse_boxes, refund.amt_you_born, refund.amt_you_blind, refund.amt_spouse_born, refund.amt_spouse_born_checked, refund.amt_spouse_blind, refund.amt_spouse_blind_checked, refund.line8_figured, refund.line8_mfs, refund.line9_figured

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
| retirement.is_ira | — | — | — | 4 |
| retirement.roth | — | — | — | 4 |
| retirement.direct | — | — | — | 4 |
| retirement.bad_code | — | — | — | 4 |
| retirement.rolled | — | — | — | 4 |
| retirement.has_rollover | — | — | — | 4 |
| retirement.smw1 | — | — | — | 4 |
| retirement.smw2 | — | — | — | 4 |
| retirement.smw4_t1_360 | — | — | — | 4 |
| retirement.smw4_t1_310 | — | — | — | 4 |
| retirement.smw4_t1_260 | — | — | — | 4 |
| retirement.smw4_t1_210 | — | — | — | 4 |
| retirement.smw4_t1_160 | — | — | — | 4 |
| retirement.smw4_t2_410 | — | — | — | 4 |
| retirement.smw4_t2_360 | — | — | — | 4 |
| retirement.smw4_t2_310 | — | — | — | 4 |
| retirement.smw4_t2_260 | — | — | — | 4 |
| retirement.smw4_t2_210 | — | — | — | 4 |
| retirement.smw4_table1 | — | — | — | 4 |
| retirement.smw4_table2 | — | — | — | 4 |
| retirement.smw4_new | — | — | — | 4 |
| retirement.smw4 | — | — | — | 8 |
| retirement.smw5 | — | — | — | 7 |
| retirement.smw6 | — | — | — | 4 |
| retirement.smw7 | — | — | — | 4 |
| retirement.smw8 | — | — | — | 5 |
| retirement.smw9 | — | — | — | 4 |
| retirement.smw10 | — | — | — | 8 |
| retirement.smw11 | — | — | — | 8 |
| retirement.cost_left | — | — | — | 4 |
| retirement.annuity_with_cost | — | — | — | 4 |
| retirement.annuity_rollover | — | — | — | 4 |
| retirement.annuity_taxable | — | — | — | 4 |
| retirement.ira_taxable | — | — | — | 4 |
| retirement.ira_not_rolled | — | — | — | 4 |
| retirement.plan_excluded | — | — | — | 4 |
| retirement.plan_simple | — | — | — | 4 |
| retirement.plan_taxable | — | — | — | 4 |
| retirement.taxable | — | — | — | 4 |
| retirement.show_a | — | — | — | 4 |
| retirement.amount_a | — | — | — | 4 |
| retirement.sav_military | — | — | — | — |
| retirement.sav_404k | — | — | — | — |
| retirement.sav_inherited | — | — | — | — |
| retirement.sav_excluded | — | — | — | 4 |
| retirement.sav_gross | — | — | — | 4 |
| retirement.sav_amount | — | — | — | 4 |

Unasserted lines: retirement.zero, retirement.one

## Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s1.zero | — | — | — | — |
| s1.line1 | — | — | — | 20 |
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
| s1.line3 | — | — | — | 14 |
| s1.line8_other | — | — | — | — |
| s1.gambling_winnings | — | — | — | — |
| s1.has_gambling | — | — | — | — |
| s1.gambling_pro | — | — | — | — |
| s1.gambling_business | — | — | — | — |
| s1.line8b | — | — | — | 9 |
| s1.line8g | — | — | — | 1 (stage16.other.o4) |
| s1.line8h | — | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line8i | — | — | — | 1 (stage16.other.o6) |
| s1.line8j | — | — | — | 1 (stage16.other.o7) |
| s1.line8r | — | — | — | 1 (stage16.other.o8) |
| s1.line8z | — | — | — | 7 |
| s1.alimony | — | — | — | — |
| s1.alimony_received | — | — | — | — |
| s1.alimony_paid | — | — | — | — |
| s1.alimony_unsupported | — | — | — | — |
| s1.alimony_refused | — | — | — | 1 (stage16.refuse.s1.alimony_received) |
| s1.line2a | — | — | — | 7 |
| s1.line2b_notice | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.cod_any | — | — | — | — |
| s1.cod_amount | — | — | — | — |
| s1.has_cod | — | — | — | — |
| s1.cod_unsupported | — | — | — | — |
| s1.cod_refused | — | — | — | 1 (stage16.refuse.s1.cod_unsupported) |
| s1.cod_figured | — | — | — | — |
| s1.line8c | — | — | — | 8 |
| s1.line8f | — | — | — | 10 |
| s1.line9 | — | — | — | 27 |
| s1.line10 | — | — | — | 46 |
| s1.line11 | — | — | — | 8 |
| s1.line13 | — | — | — | 20 |
| s1.line15 | — | — | — | 11 |
| s1.line16 | — | — | — | 12 |
| s1.line17 | — | — | — | 6 |
| s1.line18 | — | — | — | 5 |
| s1.paid_refused | — | — | — | 1 (stage16.refuse.s1.alimony_paid) |
| s1.line19a | — | — | — | 7 |
| s1.line19b_notice | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line19c_notice | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line20 | — | — | — | 31 |
| s1.line21 | — | — | — | 5 |
| s1.jury_to_employer | — | — | — | — |
| s1.jury_over | — | — | — | — |
| s1.line24a | — | — | — | 5 |
| s1.line25 | — | — | — | 5 |
| s1.line26 | — | — | — | 21 |

Unasserted lines: s1.zero, s1.has_uc, s1.line7_figured, s1.ebl_loss, s1.ebl_total, s1.zero_ebl, s1.ebl_threshold, s1.ebl, s1.sc_count, s1.has_sc, s1.sc_1a_count, s1.sc_1a, s1.has_gambling, s1.gambling_business, s1.has_cod, s1.cod_figured, s1.jury_over

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
| s2.line4 | — | — | — | 4 |
| s2.line11 | — | — | — | 3 |
| s2.line12 | — | — | — | 3 |
| s2.line17c | — | — | — | 7 |
| s2.line18 | — | — | — | 6 |
| s2.line21 | — | — | — | 12 |

Unasserted lines: s2.zero

## Schedule 3 — selected lines

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | 3 |
| s3.line2 | — | — | — | 34 |
| s3.zero | — | — | — | — |
| s3.line4 | — | — | — | 36 |
| s3.line5a | — | — | — | 30 |
| s3.line5b | — | — | — | 31 |
| s3.line8 | — | — | — | 5 |
| s3.mfs | — | — | — | — |
| s3.line9 | — | — | — | — |
| s3.line10 | — | — | — | — |
| s3.line11 | — | — | — | 27 |
| s3.line12 | — | — | — | — |
| s3.line14 | — | — | — | — |
| s3.line15 | — | — | — | 24 |

Unasserted lines: s3.zero, s3.mfs

## Schedule 8812 — Credits for Qualifying Children and Other Dependents

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s8812.line1 | — | — | — | 30 |
| s8812.zero | — | — | — | — |
| s8812.line2a | — | — | — | 28 |
| s8812.line2b | — | — | — | 28 |
| s8812.line2c | — | — | — | 28 |
| s8812.line2d | — | — | — | 28 |
| s8812.line3 | — | — | — | 30 |
| s8812.line4 | — | — | — | 33 |
| s8812.line5 | — | — | — | 33 |
| s8812.line6 | — | — | — | 29 |
| s8812.line7 | — | — | — | 29 |
| s8812.line8 | — | — | — | 33 |
| s8812.line9 | — | — | — | 6 |
| s8812.excess | — | — | — | 24 |
| s8812.line10 | — | — | — | 30 |
| s8812.line11 | — | — | — | 30 |
| s8812.line12 | — | — | — | 31 |
| s8812.clw_a1 | — | — | — | 28 |
| s8812.clw_a2 | — | — | — | 28 |
| s8812.clw_a3 | — | — | — | 28 |
| s8812.clw_a4 | — | — | — | 28 |
| s8812.clw_a5 | — | — | — | 28 |
| s8812.line13 | — | — | — | 31 |
| s8812.line14 | — | — | — | 52 |
| s8812.line16a | — | — | — | 30 |
| s8812.line16b | — | — | — | 30 |
| s8812.line17 | — | — | — | 30 |
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
| s8812.line18a | — | — | — | 32 |
| s8812.line18b | — | — | — | 28 |
| s8812.line19 | — | — | — | 31 |
| s8812.line20 | — | — | — | 29 |
| s8812.ss_withheld | — | — | — | 24 |
| s8812.amt_ws4 | — | — | — | 24 |
| s8812.amt_ws6 | — | — | — | — |
| s8812.amt_ws7 | — | — | — | 1 (stage14.f8959.se_above_threshold) |
| s8812.line21 | — | — | — | 26 |
| s8812.line22 | — | — | — | 29 |
| s8812.line23 | — | — | — | 26 |
| s8812.line24 | — | — | — | 26 |
| s8812.line25 | — | — | — | 27 |
| s8812.line26 | — | — | — | 25 |
| s8812.few_children | — | — | — | 24 |
| s8812.earned_covers | — | — | — | 24 |
| s8812.from_part_iia | — | — | — | 24 |
| s8812.from_part_iib | — | — | — | 25 |
| s8812.part_iib_result | — | — | — | 24 |
| s8812.line27 | — | — | — | 53 |
| s8812.clwb_complete | — | — | — | — |
| s8812.clwb_1 | — | — | — | 4 |
| s8812.clwb_2 | — | — | — | 4 |
| s8812.clwb_3 | — | — | — | 4 |
| s8812.clwb_4 | — | — | — | 4 |
| s8812.clwb_5 | — | — | — | 4 |
| s8812.clwb_three | — | — | — | — |
| s8812.clwb_5_covers | — | — | — | — |
| s8812.clwb_7 | — | — | — | — |
| s8812.clwb_8 | — | — | — | — |
| s8812.clwb_9 | — | — | — | — |
| s8812.clwb_10 | — | — | — | — |
| s8812.clwb_11_figured | — | — | — | — |
| s8812.clwb_11_three | — | — | — | — |
| s8812.clwb_11 | — | — | — | 5 |
| s8812.clwb_12 | — | — | — | 4 |
| s8812.clwb_13 | — | — | — | 4 |
| s8812.clwb_14 | — | — | — | 4 |
| s8812.clwb_15 | — | — | — | 4 |

Unasserted lines: s8812.zero, s8812.eiw_2b, s8812.eiw_7_figured, s8812.eiw_3_positive, s8812.chart_eic, s8812.amt_ws6, s8812.clwb_complete, s8812.clwb_three, s8812.clwb_5_covers, s8812.clwb_7, s8812.clwb_8, s8812.clwb_9, s8812.clwb_10, s8812.clwb_11_figured, s8812.clwb_11_three

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
| sa.line5a | — | — | — | 1 (stage16.other.o1) |
| sa.line5b | — | — | — | — |
| sa.line5c | — | — | — | — |
| sa.line8a | — | — | — | 1 (stage16.other.o1) |
| sa.line11 | — | — | — | — |
| sa.zero | — | — | — | — |
| sa.line2 | — | — | — | 7 |
| sa.line3 | — | — | — | 8 |
| sa.line4 | — | — | — | 10 |
| sa.line5d | — | — | — | 10 |
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
| sa.line5e | — | — | — | 19 |
| sa.line6 | — | — | — | 12 |
| sa.line8b | — | — | — | 11 |
| sa.line8c | — | — | — | 11 |
| sa.line13 | — | — | — | 11 |
| sa.line15 | — | — | — | 11 |
| sa.gambling_losses | — | — | — | — |
| sa.line16_gambling | — | — | — | — |
| sa.line16 | — | — | — | 12 |
| sa.line7 | — | — | — | 9 |
| sa.line8e | — | — | — | 9 |
| sa.line9 | — | — | — | 8 |
| sa.line10 | — | — | — | 9 |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 16 |
| sa.form8283 | — | — | — | 3 |
| sa.line14 | — | — | — | 8 |
| sa.line17 | — | — | — | 13 |
| sa.standardbase | — | — | — | — |
| sa.extra | — | — | — | — |
| sa.boxes_age65 | — | — | — | 1 (stage16.sa.decedent_spouse) |
| sa.extra_age65 | — | — | — | — |
| sa.boxes_blind | — | — | — | — |
| sa.extra_blind | — | — | — | — |
| sa.standardraw | — | — | — | — |
| sa.standard | — | — | — | 12 |
| sa.itemizes | — | — | — | 6 |
| sa.deduction | — | — | — | 7 |
| sa.mfs_spouse_itemizes | — | — | — | — |

Unasserted lines: sa.mfs_spouse_extra, sa.age65_count, sa.age65, sa.agi, sa.zero, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.line16_gambling, sa.standardbase, sa.extra, sa.extra_age65, sa.boxes_blind, sa.extra_blind, sa.standardraw, sa.mfs_spouse_itemizes

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
| sc.rrta | — | — | — | 4 |
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
| sc.ho_multi | — | — | — | 4 |
| sc.ho_sqft | — | — | — | — |
| sc.ho_home_sqft | — | — | — | — |
| sc.ho_rate | — | — | — | — |
| sc.ho_cap_sqft | — | — | — | — |
| sc.ho_over | — | — | — | 4 |
| sc.ho_line4_actual | — | — | — | 4 |
| sc.ho_line4_cap | — | — | — | 3 |
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
| sc.s179_return | — | — | — | 3 |
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
| sc.f7206_line4 | — | — | — | 3 |
| sc.f7206_line5 | — | — | — | 4 |
| sc.f7206_has | — | — | — | 3 |
| sc.f7206_line7_pos | — | — | — | 3 |
| sc.f7206_line7 | — | — | — | 4 |
| sc.f7206_line8 | — | — | — | 3 |
| sc.f7206_line9_pos | — | — | — | 4 |
| sc.f7206_line9 | — | — | — | 5 |
| sc.f7206_line10 | — | — | — | 4 |
| sc.f7206_line13 | — | — | — | 3 |
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

Unasserted lines: sc.one, sc.zero, sc.ho_rate, sc.ho_cap_sqft

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
| scveh.cm_c | — | — | — | 6 |
| scveh.om_c | — | — | — | — |
| scveh.nonbusiness_c | — | — | — | — |
| scveh.total_c | — | — | — | 1 (stage14.refuse.veh_no_miles) |
| scveh.no_miles | — | — | — | 6 |
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
| scveh.lease_business | — | — | — | 5 |
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
| scveh.bus_cost | — | — | — | 4 |
| scveh.s179_elect | — | — | — | — |
| scveh.suv_cap | — | — | — | — |
| scveh.s179_bad | — | — | — | 6 |
| scveh.after_jan19 | — | — | — | — |
| scveh.bonus_choice | — | — | — | — |
| scveh.bonus_same | — | — | — | — |
| scveh.bonus_mixed | — | — | — | 6 |
| scveh.claims_bonus | — | — | — | 6 |
| scveh.rate40 | — | — | — | — |
| scveh.lim_first_bonus | — | — | — | 3 |
| scveh.lim_first_none | — | — | — | 3 |
| scveh.lim_2025 | — | — | — | 3 |
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
| scveh.bonus_forty | — | — | — | 6 |
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
| scveh.rate_hy | — | — | — | 3 |
| scveh.rate_mq | — | — | — | 3 |
| scveh.rate_prior | — | — | — | 5 |
| scveh.line19_hy | — | — | — | 4 |
| scveh.line19_mq | — | — | — | 4 |
| scveh.line19_prior | — | — | — | 5 |
| scveh.line19 | — | — | — | 11 |
| scveh.line19_earlier | — | — | — | 6 |
| scveh.line19_2025 | — | — | — | 4 |
| scveh.line20 | — | — | — | 14 |
| scveh.b100 | — | — | — | 6 |
| scveh.k1 | — | — | — | — |
| scveh.r1 | — | — | — | 6 |
| scveh.t1 | — | — | — | 6 |
| scveh.l1 | — | — | — | 5 |
| scveh.t1s | — | — | — | 6 |
| scveh.d1 | — | — | — | 5 |
| scveh.k2 | — | — | — | — |
| scveh.r2 | — | — | — | 6 |
| scveh.t2 | — | — | — | 6 |
| scveh.l2 | — | — | — | 6 |
| scveh.d2 | — | — | — | 6 |
| scveh.k3 | — | — | — | — |
| scveh.r3 | — | — | — | 6 |
| scveh.t3 | — | — | — | 6 |
| scveh.l3 | — | — | — | 5 |
| scveh.d3 | — | — | — | 5 |
| scveh.k4 | — | — | — | — |
| scveh.r4 | — | — | — | 6 |
| scveh.t4 | — | — | — | 6 |
| scveh.l4 | — | — | — | 5 |
| scveh.d4 | — | — | — | 5 |
| scveh.k5 | — | — | — | — |
| scveh.r5 | — | — | — | 6 |
| scveh.t5 | — | — | — | 6 |
| scveh.l5 | — | — | — | 5 |
| scveh.d5 | — | — | — | 5 |
| scveh.k6 | — | — | — | — |
| scveh.r6 | — | — | — | 6 |
| scveh.t6 | — | — | — | 6 |
| scveh.l6 | — | — | — | 5 |
| scveh.d6 | — | — | — | 5 |
| scveh.d_total | — | — | — | 7 |
| scveh.unrecovered | — | — | — | 7 |
| scveh.post_amount | — | — | — | 4 |
| scveh.post | — | — | — | 7 |
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
| scveh.mq_total_a2 | — | — | — | 3 |
| scveh.cost179_o | — | — | — | 6 |
| scveh.cost179_a2 | — | — | — | 2 (classm.scveh.2, classm.scveh.5) |

Unasserted lines: scveh.zero, scveh.cent, scveh.bm_c, scveh.om_c, scveh.nonbusiness_c, scveh.rate, scveh.y5, scveh.suv_cap, scveh.rate40, scveh.hy, scveh.k1, scveh.k2, scveh.k3, scveh.k4, scveh.k5, scveh.k6

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
| sdtw.line6 | — | — | — | 7 |
| sdtw.line7 | — | — | — | 5 |
| sdtw.line8 | — | — | — | 6 |
| sdtw.line9 | — | — | — | 6 |
| sdtw.line10 | — | — | — | 6 |
| sdtw.line11 | — | — | — | 6 |
| sdtw.line12 | — | — | — | 6 |
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
| sli.line1 | — | — | — | 5 |
| sli.line2 | — | — | — | 4 |
| sli.line3 | — | — | — | 6 |
| sli.line4 | — | — | — | 4 |
| sli.base_other | — | — | — | — |
| sli.base_joint | — | — | — | — |
| sli.line5 | — | — | — | 5 |
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
| ssb.line1 | — | — | — | 6 |
| ssb.has_benefits | — | — | — | — |
| ssb.line2 | — | — | — | 6 |
| ssb.line3 | — | — | — | 7 |
| ssb.line4 | — | — | — | 6 |
| ssb.line5 | — | — | — | 6 |
| ssb.ira_line20 | — | — | — | — |
| ssb.line6 | — | — | — | 7 |
| ssb.line7 | — | — | — | 8 |
| ssb.base_single | — | — | — | — |
| ssb.base_joint | — | — | — | — |
| ssb.zero | — | — | — | — |
| ssb.mfs_base | — | — | — | — |
| ssb.line8 | — | — | — | 5 |
| ssb.line9 | — | — | — | 6 |
| ssb.adjust_single | — | — | — | — |
| ssb.adjust_joint | — | — | — | — |
| ssb.mfs_adjust | — | — | — | — |
| ssb.line10 | — | — | — | 3 |
| ssb.line11 | — | — | — | 4 |
| ssb.line12 | — | — | — | 5 |
| ssb.line13 | — | — | — | 6 |
| ssb.line14 | — | — | — | 6 |
| ssb.line15 | — | — | — | 5 |
| ssb.mfs_together | — | — | — | — |
| ssb.line16_sum | — | — | — | — |
| ssb.line16_together | — | — | — | — |
| ssb.line16 | — | — | — | 7 |
| ssb.line17 | — | — | — | 5 |
| ssb.line18_figured | — | — | — | — |
| ssb.line18 | — | — | — | 6 |

Unasserted lines: ssb.has_benefits, ssb.ira_line20, ssb.base_single, ssb.base_joint, ssb.zero, ssb.mfs_base, ssb.adjust_single, ssb.adjust_joint, ssb.mfs_adjust, ssb.mfs_together, ssb.line16_sum, ssb.line16_together, ssb.line18_figured

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
| w2.wages | — | — | — | 1 (classm.w2.1) |
| w2.one | — | — | — | — |
| w2.over | — | — | — | 1 (classm.w2.1) |
| w2.box5 | — | — | — | — |
| w2.box6 | — | — | — | — |
| w2.box10 | — | — | — | — |
| w2.has_box10 | — | — | — | 1 (classm.w2.1) |
| w2.box10_wages | — | — | — | — |
| w2.box10_bad | — | — | — | 1 (classm.w2.1) |
| w2.dc_net | — | — | — | 2 (classm.w2.1, stage15.refuse.w2.box10_bad) |
| w2.dc_benefits | — | — | — | 1 (classm.w2.1) |
| w2.dc_zero | — | — | — | — |
| w2.box12_any | — | — | — | — |
| w2.box12_userra | — | — | — | — |
| w2.box12_d | — | — | — | — |
| w2.box12_e | — | — | — | — |
| w2.box12_f | — | — | — | — |
| w2.box12_g | — | — | — | — |
| w2.box12_h | — | — | — | — |
| w2.box12_s | — | — | — | — |
| w2.box12_aa | — | — | — | — |
| w2.box12_bb | — | — | — | — |
| w2.box12_ee | — | — | — | — |
| w2.has_g | — | — | — | 1 (classm.w2.1) |
| w2.g_governmental | — | — | — | — |
| w2.g_elective | — | — | — | — |
| w2.g_bad | — | — | — | 1 (classm.w2.1) |
| w2.g_gov_part | — | — | — | 2 (classm.w2.1, stage15.refuse.w2.g_bad) |
| w2.g_counted | — | — | — | 1 (classm.w2.1) |
| w2.zero | — | — | — | — |
| w2.code_h | — | — | — | 1 (classm.w2.1) |
| w2.sav_listed | — | — | — | 3 |
| w2.sav_deferral | — | — | — | 1 (classm.w2.1) |

Unasserted lines: w2.one, w2.dc_zero, w2.zero

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

Unasserted computed lines across all documents: 626. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)
Asserted keys not matching a line id: person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line3, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.positive, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4a, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.owes, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4c, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line5b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line6, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line7, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line8d, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line9, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line10, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line11, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line12, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line13, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, qdcg.f1040.line15, qdcg.f1040.line3a, qdcg.f1040.status, f1040.qdcg.line25, qdcg.sd.distributions