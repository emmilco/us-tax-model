# Evidence coverage per line

**Scoreboard.** Share of computed lines with at least one outside-family assertion: 19 of 1510 (1.3%). B: 0, second-family M: 0, E: 19.

A computed line is one whose atom is not `input`, `param` or `copy`. An outside-family assertion on a line is a class B fixture (human hand-work), a class M fixture whose recorded model is not a Claude model (second-family M), or an engine assertion (E) under the rule stated below; the three sub-counts are over the same computed lines, so a line with two kinds counts once in the share. Class A, Claude-family M, C and R assertions do not move the number: the first three are one model family reading the archived text, and R is the project's own evaluator.

Fixtures that assert each line, by evidence class, as a count of cases (ids listed when two or fewer). A — official IRS worked example, cited. B — human hand-work recorded with the worker and the document revision; none yet. C — a named, versioned calculator or engine record in fixtures/2025/differential/ (spec 6.1); none yet. M — isolated model hand-work with the model, prompt hash and snapshot recorded (fixtures/2025/classm.json, reviews/2025/classm/); second-family M fixtures are those whose recorded model does not start with "claude". E — the engine differential (tools/engines; reports/2025/engine_differential.md and .json): PolicyEngine-US (PE) and Tax-Calculator (TC) run over 1700 generated returns. A line gets an E assertion only when, for at least one engine, the engine computes the line rather than taking it whole as an input, the project value was nonzero on at least 50 compared returns, and fewer than half of the nonzero returns the engine reached (compared plus excluded) were excluded under an engine limitation; the cell prints each engine's compared, nonzero and excluded counts, and an engine that falls short of the rule is marked "below rule" and asserts nothing. R — recorded regression from the project's own evaluator, no class claimed; agreement with the Lean reference evaluator (reports/2025/evaluator_agreement.md) is evaluator agreement over the same data, not an independent engine, and earns no class.

An outside-family assertion (B, second-family M or E) on a line whose atom is `copy` also credits the first line along its copy chain whose atom is not `copy`, because a copy's value equals its source's exactly, so agreement on the copy is agreement on the source; the table marks each such credit "via <copy line>" (the chain walked, when longer than one copy), the copy line keeps its own cell, and the sub-counts above include credited lines. In this report 15 assertions are credited through copies (B cases: 0; second-family M cases: 0; engine-line assertions: 15); every asserted copy line resolved to a source.

Engine ids with no line of their own (never an E assertion): f1040.tax_before_credits (PE), f1040.tax_before_credits (TC). Mapped lines taken whole from the generator's facts: none. Components of compared lines that enter the engine as generator facts rather than the engine's own form arithmetic (the line still counts as engine-computed; the component does not): PolicyEngine-US f1040.line10: the HSA deduction (Form 8889 line 13) enters as the generator's health_savings_account_ald; the engine computes the educator, half-of-self-employment-tax and student loan interest components and the sum; Tax-Calculator f1040.line10: the HSA deduction (e03290) and the educator expenses deduction (e03220) enter as the generator's amounts; the engine computes the half-of-self-employment-tax component and the sum (returns with student loan interest are excluded); Tax-Calculator f1040.line20: the foreign tax paid (e07300) is a supplied amount; the engine computes the credit limit.

## Form 4562 — one item of depreciable property (other than a vehicle) of a business

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| asset.zero | — | — | — | — | — | — |
| asset.class | — | — | — | — | — | — |
| asset.period | — | — | — | 4 | — | — |
| asset.outside | — | — | — | 4 | — | — |
| asset.screen | — | — | — | — | — | — |
| asset.screened | — | — | — | 4 | — | — |
| asset.placed | — | — | — | — | — | — |
| asset.cost | — | — | — | — | — | 1 (stage14.asset.refuse_class) |
| asset.pct | — | — | — | — | — | — |
| asset.cent | — | — | — | — | — | — |
| asset.hundred | — | — | — | — | — | — |
| asset.pct_c | — | — | — | — | — | — |
| asset.pct_bad | — | — | — | 4 | — | — |
| asset.listed | — | — | — | — | — | — |
| asset.half | — | — | — | — | — | — |
| asset.over_half | — | — | — | 4 | — | — |
| asset.listed_low | — | — | — | 4 | — | — |
| asset.basis | — | — | — | 4 | — | 3 |
| asset.is2025 | — | — | — | 4 | — | — |
| asset.on_19 | — | — | — | 4 | — | — |
| asset.on_17 | — | — | — | 4 | — | — |
| asset.on_26_2025 | — | — | — | 4 | — | — |
| asset.year | — | — | — | 4 | — | — |
| asset.last | — | — | — | 4 | — | — |
| asset.done | — | — | — | 4 | — | — |
| asset.quarter | — | — | — | — | — | — |
| asset.qconv | — | — | — | 4 | — | — |
| asset.s179 | — | — | — | — | — | — |
| asset.s179_bad | — | — | — | 4 | — | — |
| asset.after179 | — | — | — | 4 | — | 3 |
| asset.after_jan19 | — | — | — | — | — | — |
| asset.bonus_choice | — | — | — | — | — | — |
| asset.bonus_same | — | — | — | — | — | — |
| asset.bonus_mixed | — | — | — | 4 | — | — |
| asset.rate40 | — | — | — | — | — | — |
| asset.bonus_full | — | — | — | 3 | — | 1 (stage14.asset.refuse_bonus_mixed) |
| asset.bonus_forty | — | — | — | 3 | — | 1 (stage14.asset.refuse_bonus_mixed_forty) |
| asset.bonus_fullcase | — | — | — | 3 | — | — |
| asset.bonus | — | — | — | 3 | — | 4 |
| asset.f25 | — | — | — | 1 (classm.asset.2) | — | 2 (stage14.asset.listed_and_not, stage14.asset.listed_forty) |
| asset.f26i | — | — | — | 1 (classm.asset.2) | — | 1 (stage14.asset.listed_and_not) |
| asset.ub | — | — | — | 4 | — | — |
| asset.col19c | — | — | — | 3 | — | 1 (stage14.asset.listed_and_not) |
| asset.hy | — | — | — | — | — | — |
| asset.rate_hy | — | — | — | 3 | — | — |
| asset.rate_mq | — | — | — | 3 | — | — |
| asset.macrs_hy | — | — | — | 3 | — | — |
| asset.macrs_mq | — | — | — | 3 | — | — |
| asset.macrs2025 | — | — | — | 3 | — | 13 |
| asset.mqbase | — | — | — | 4 | — | — |
| asset.mq_q4_2025 | — | — | — | 4 | — | — |
| asset.prior_conv | — | — | — | — | — | — |
| asset.prior_179 | — | — | — | — | — | — |
| asset.prior_bonus | — | — | — | — | — | — |
| asset.ub_prior_a | — | — | — | 4 | — | 1 (stage14.asset.prior_179_full) |
| asset.ub_prior | — | — | — | 4 | — | 1 (stage14.asset.prior_179_bonus) |
| asset.rate_prior | — | — | — | 4 | — | — |
| asset.macrs_prior_live | — | — | — | 4 | — | — |
| asset.macrs_prior | — | — | — | 2 (classm.asset.1, classm.asset.4) | — | 7 |
| asset.dep_2025 | — | — | — | 4 | — | — |
| asset.bonus_2025 | — | — | — | 4 | — | — |
| asset.s179_2025 | — | — | — | 4 | — | — |
| asset.mq_q4 | — | — | — | 4 | — | — |
| asset.mq_total | — | — | — | 4 | — | — |
| asset.cost179 | — | — | — | 4 | — | — |
| asset.cost179_2025 | — | — | — | 3 | — | — |
| asset.dep_prior | — | — | — | 4 | — | — |
| asset.dep_listed | — | — | — | 1 (classm.asset.2) | — | 2 (stage14.asset.listed_prior, stage14.asset.listed_forty) |

Unasserted lines: asset.zero, asset.cent, asset.hundred, asset.pct_c, asset.half, asset.rate40, asset.hy

## Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| carloan.zero | — | — | — | — | — | — |
| carloan.kind | — | — | — | — | — | — |
| carloan.requirements | — | — | — | — | — | — |
| carloan.vehicle | — | — | — | — | — | — |
| carloan.eligible | — | — | — | 4 | — | — |
| carloan.interest | — | — | — | — | — | — |
| carloan.mixed | — | — | — | — | — | — |
| carloan.financed | — | — | — | — | — | — |
| carloan.nonqualifying | — | — | — | — | — | — |
| carloan.down | — | — | — | — | — | — |
| carloan.nonqualifying_debt | — | — | — | 3 | — | — |
| carloan.mixed_qualifying | — | — | — | 1 (classm.carloan.3) | — | — |
| carloan.refi_balance | — | — | — | — | — | — |
| carloan.refi_whole | — | — | — | — | — | — |
| carloan.refi_qualifying | — | — | — | 2 (classm.carloan.1, classm.carloan.2) | — | — |
| carloan.refi_nested | — | — | — | 4 | — | — |
| carloan.allocated | — | — | — | 4 | — | — |
| carloan.refi_interest | — | — | — | 3 | — | — |
| carloan.mixed_interest | — | — | — | 4 | — | — |
| carloan.mixed_prorated | — | — | — | 4 | — | — |
| carloan.qpvli | — | — | — | 4 | — | — |
| carloan.col_ii_input | — | — | — | — | — | — |
| carloan.col_ii | — | — | — | 4 | — | — |
| carloan.col_iii | — | — | — | 4 | — | — |

Unasserted lines: carloan.zero

## Form 2441, Part I — persons or organizations who provided the care, one entry per care provider

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| dcprov.one | — | — | — | — | — | — |
| dcprov.tin_kind | — | — | — | — | — | — |
| dcprov.household | — | — | — | — | — | — |
| dcprov.paid | — | — | — | — | — | — |
| dcprov.related | — | — | — | — | — | — |
| dcprov.see_statement | — | — | — | 1 (classm.dcprov.1) | — | — |

Unasserted lines: dcprov.one

## Dependents — qualifying child and qualifying relative tests, per person listed

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| dependent.relationship | — | — | — | — | — | — |
| dependent.age | — | — | — | — | — | — |
| dependent.student | — | — | — | — | — | — |
| dependent.disabled | — | — | — | — | — | — |
| dependent.months | — | — | — | — | — | — |
| dependent.self_support | — | — | — | — | — | — |
| dependent.joint_return | — | — | — | — | — | — |
| dependent.citizen | — | — | — | — | — | — |
| dependent.canada_mexico | — | — | — | — | — | — |
| dependent.married | — | — | — | — | — | — |
| dependent.tin | — | — | — | — | — | — |
| dependent.work_ssn | — | — | — | — | — | — |
| dependent.gross_income | — | — | — | — | — | — |
| dependent.supported | — | — | — | — | — | — |
| dependent.other_claimant | — | — | — | — | — | — |
| dependent.divorced_rule | — | — | — | — | — | — |
| dependent.multiple_support | — | — | — | — | — | — |
| dependent.parent_home_paid | — | — | — | — | — | — |
| dependent.one | — | — | — | — | — | — |
| dependent.zero | — | — | — | — | — | — |
| dependent.qc_relationship | — | — | — | 5 | — | 21 |
| dependent.younger | — | — | — | — | — | 18 |
| dependent.us_half | — | — | — | — | — | — |
| dependent.eic_ssn | — | — | — | — | — | — |
| dependent.qc_age | — | — | — | 5 | — | 18 |
| dependent.lived_half | — | — | — | 5 | — | 19 |
| dependent.qualifying_child | — | — | — | 5 | — | 24 |
| dependent.resident | — | — | — | 5 | — | 19 |
| dependent.qc_dependent | — | — | — | 5 | — | 24 |
| dependent.qr_relationship | — | — | — | 5 | — | 6 |
| dependent.qr_income | — | — | — | 5 | — | 6 |
| dependent.income_exception | — | — | — | 5 | — | 7 |
| dependent.qualifying_relative | — | — | — | 5 | — | 8 |
| dependent.qr_dependent | — | — | — | 5 | — | 8 |
| dependent.claimed | — | — | — | 5 | — | 24 |
| dependent.under_ctc_age | — | — | — | 5 | — | 15 |
| dependent.ctc_child | — | — | — | 5 | — | 24 |
| dependent.odc_person | — | — | — | 5 | — | 24 |
| dependent.ctc_per_child | — | — | — | — | — | — |
| dependent.ctc_amount | — | — | — | 5 | — | 24 |
| dependent.odc_per_dependent | — | — | — | — | — | — |
| dependent.odc_amount | — | — | — | 5 | — | 24 |
| dependent.actc_per_child | — | — | — | — | — | — |
| dependent.actc_amount | — | — | — | 5 | — | 24 |
| dependent.hoh_test2 | — | — | — | 5 | — | 24 |
| dependent.hoh_test1 | — | — | — | 4 | — | 24 |
| dependent.eic_child | — | — | — | 5 | — | — |
| dependent.eic_ssn_child | — | — | — | 5 | — | — |
| dependent.dc_child_all_year | — | — | — | 5 | — | — |
| dependent.dc_age13 | — | — | — | 5 | — | — |
| dependent.dc_under13 | — | — | — | — | — | — |
| dependent.dc_child | — | — | — | 5 | — | — |
| dependent.dc_incapable | — | — | — | — | — | — |
| dependent.dc_disabled_qp | — | — | — | 5 | — | — |
| dependent.dc_qp | — | — | — | 5 | — | — |
| dependent.dc_no_tin | — | — | — | 5 | — | — |
| dependent.dc_count | — | — | — | — | — | 1 (stage15.refuse.dependent.dc_no_tin) |
| dependent.dc_paid | — | — | — | — | — | — |
| dependent.dc_line2d | — | — | — | 1 (classm.dependent.5) | — | 1 (stage15.refuse.dependent.dc_no_tin) |
| dependent.dc_line2c | — | — | — | 5 | — | — |

Unasserted lines: dependent.one, dependent.zero, dependent.ctc_per_child, dependent.odc_per_dependent, dependent.actc_per_child

## Form 1099-DIV — distribution components and scope screening

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| div.box2b | — | — | — | — | — | — |
| div.box2c | — | — | — | — | — | — |
| div.box2d | — | — | — | — | — | — |
| div.box2e | — | — | — | — | — | — |
| div.box2f | — | — | — | — | — | — |
| div.box3 | — | — | — | — | — | — |
| div.box9 | — | — | — | — | — | — |
| div.box10 | — | — | — | — | — | — |
| div.box12 | — | — | — | — | — | — |
| div.box13 | — | — | — | — | — | — |
| div.basis_reconciled | — | — | — | — | — | — |
| div.box1a | — | — | — | — | — | — |
| div.box1b | — | — | — | — | — | — |
| div.box2a | — | — | — | — | — | — |
| div.box5 | — | — | — | — | — | — |
| div.section1202 | — | — | — | — | — | — |
| div.amt | — | — | — | — | — | — |
| div.unsupported | — | — | — | — | — | — |
| div.bad_special | — | — | — | — | — | — |
| div.screen | — | — | — | — | — | — |
| div.bad_components | — | — | — | — | — | — |
| div.special_total | — | — | — | — | — | — |

Unasserted lines: div.box1a, div.box1b, div.box2a, div.box5, div.section1202, div.amt, div.unsupported, div.bad_special, div.screen, div.bad_components, div.special_total

## Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| eic.qc_of_another | — | — | — | — | — | — |
| eic.age_range_count | — | — | — | — | — | — |
| eic.age_range | — | — | — | — | — | 1 (stage13.eic_spouse_in_age_range) |
| eic.us_home | — | — | — | — | — | — |
| eic.married | — | — | — | — | — | — |
| eic.zero | — | — | — | — | — | — |
| eic.qc_count | — | — | — | — | — | — |
| eic.ssn_count | — | — | — | — | — | 3 |
| eic.has_qc | — | — | — | — | — | 2 (stage9.eic.child_without_ssn, stage9.eic.parent_not_qualifying_child) |
| eic.married_rules | — | — | — | — | — | — |
| eic.top_limit | — | — | — | — | — | — |
| eic.below_top | — | — | — | — | — | — |
| eic.limit0_other | — | — | — | — | — | — |
| eic.limit1_other | — | — | — | — | — | — |
| eic.limit2_other | — | — | — | — | — | — |
| eic.limit3_other | — | — | — | — | — | — |
| eic.limit0_joint | — | — | — | — | — | — |
| eic.limit1_joint | — | — | — | — | — | — |
| eic.limit2_joint | — | — | — | — | — | — |
| eic.limit3_joint | — | — | — | — | — | — |
| eic.limit_other | — | — | — | — | — | — |
| eic.limit_joint | — | — | — | — | — | — |
| eic.limit | — | — | — | — | — | — |
| eic.step1_income | — | — | — | — | — | — |
| eic.step1_ssn | — | — | — | — | — | — |
| eic.step1_foreign | — | — | — | — | — | — |
| eic.step1_resident | — | — | — | — | — | — |
| eic.gain_7a | — | — | — | — | — | 1 (stage9.eic.capital_gain_in_investment_income) |
| eic.investment_income | — | — | — | — | — | — |
| eic.step2_income | — | — | — | — | — | 3 |
| eic.step2_other | — | — | — | — | — | — |
| eic.same_home | — | — | — | — | — | — |
| eic.legally_separated | — | — | — | — | — | — |
| eic.step3_married | — | — | — | — | — | 3 |
| eic.step3 | — | — | — | — | — | — |
| eic.step4 | — | — | — | — | — | 2 (stage9.eic.no_child.over65, stage9.eic.no_child.born_jan1_1961) |
| eic.step34 | — | — | — | — | — | — |
| eic.step5_line1 | — | — | — | — | — | — |
| eic.step5_line2 | — | — | — | — | — | — |
| eic.step5_line3 | — | — | — | — | — | — |
| eic.step5_line4 | — | — | — | — | — | — |
| eic.earned_income | — | — | — | — | — | — |
| eic.sc_count | — | — | — | — | — | — |
| eic.self_employed | — | — | — | — | — | — |
| eic.wsb_se | — | — | — | — | — | — |
| eic.wsb_4b | — | — | — | 4 | — | 5 |
| eic.wsb_6 | — | — | — | 4 | — | 1 (stage14.eic.wsb_stop_27c) |
| eic.earned_for_limit | — | — | — | — | — | — |
| eic.step5_income | — | — | — | — | — | — |
| eic.eligible | — | — | — | — | — | 20 |
| eic.line1 | — | — | — | 6 | — | 5 |
| eic.line1_in_table | — | — | — | — | — | — |
| eic.line1_table0 | — | — | — | — | — | — |
| eic.line1_table1 | — | — | — | — | — | — |
| eic.line1_table2 | — | — | — | — | — | — |
| eic.line1_table3 | — | — | — | — | — | — |
| eic.line1_table | — | — | — | — | — | — |
| eic.line2 | — | — | — | 8 | — | 14 |
| eic.line3 | — | — | — | 3 | — | — |
| eic.line4 | — | — | — | 7 | — | 4 |
| eic.threshold_other | — | — | — | — | — | — |
| eic.threshold_joint | — | — | — | — | — | — |
| eic.line5_threshold | — | — | — | — | — | — |
| eic.threshold0_other | — | — | — | — | — | — |
| eic.threshold1_other | — | — | — | — | — | — |
| eic.threshold0_joint | — | — | — | — | — | — |
| eic.threshold1_joint | — | — | — | — | — | — |
| eic.line5_blank | — | — | — | — | — | 1 (stage9.eic.one_child.at_line5_amount) |
| eic.line3_table0 | — | — | — | — | — | — |
| eic.line3_table1 | — | — | — | — | — | — |
| eic.line3_table2 | — | — | — | — | — | — |
| eic.line3_table3 | — | — | — | — | — | — |
| eic.line5 | — | — | — | 3 | — | 3 |
| eic.smaller | — | — | — | — | — | — |
| eic.after_line4 | — | — | — | — | — | — |
| eic.line6 | — | — | — | 8 | — | 8 |
| eic.credit | — | — | — | — | E via f1040.line27a (PE, TC) | — |
| eic.reached_step3 | — | — | — | — | — | — |
| eic.check_27c | — | — | — | — | — | 2 (stage14.eic.wsb_stop_27c, stage14.eic.wsb_line5_stop_27c) |
| eic.wsb_4b_positive | — | — | — | — | — | — |
| eic.wsb_line5_stop | — | — | — | — | — | 1 (stage14.eic.wsb_line5_stop_27c) |
| eic.separated_box | — | — | — | — | — | — |
| eic.clergy | — | — | — | — | — | — |

Unasserted lines: eic.age_range_count, eic.zero, eic.qc_count, eic.married_rules, eic.top_limit, eic.below_top, eic.limit0_other, eic.limit1_other, eic.limit2_other, eic.limit3_other, eic.limit0_joint, eic.limit1_joint, eic.limit2_joint, eic.limit3_joint, eic.limit_other, eic.limit_joint, eic.limit, eic.step1_income, eic.step1_ssn, eic.step1_foreign, eic.step1_resident, eic.investment_income, eic.step2_other, eic.step3, eic.step34, eic.step5_line1, eic.step5_line2, eic.step5_line3, eic.step5_line4, eic.earned_income, eic.sc_count, eic.self_employed, eic.wsb_se, eic.earned_for_limit, eic.step5_income, eic.line1_in_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line1_table, eic.threshold_other, eic.threshold_joint, eic.line5_threshold, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.smaller, eic.after_line4, eic.reached_step3, eic.wsb_4b_positive, eic.separated_box, eic.clergy

## Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f1040.status | 1 (example.official) | — | — | — | — | 58 |
| f1040.line1a | — | — | — | 4 | — | 22 |
| f1040.line1e | — | — | — | 4 | — | 14 |
| f1040.line1z | — | — | — | 4 | — | 29 |
| f1040.tax_exempt_interest | — | — | — | — | — | — |
| f1040.line2a | — | — | — | 4 | — | 1 (stage10.ss.exempt_interest_dividends) |
| f1040.line2b | — | — | — | 4 | — | 5 |
| f1040.line3b | — | — | — | 4 | — | 3 |
| f1040.line3a | 1 (example.official) | — | — | — | — | 61 |
| f1040.line4a | — | — | — | 4 | — | 4 |
| f1040.line4b | — | — | — | 4 | — | 8 |
| f1040.ira_rollovers | — | — | — | — | — | — |
| f1040.line4c_rollover | — | — | — | 4 | — | 6 |
| f1040.line5a | — | — | — | 4 | — | 11 |
| f1040.line5b | — | — | — | 4 | — | 16 |
| f1040.plan_rollovers | — | — | — | — | — | — |
| f1040.line5c_rollover | — | — | — | 4 | — | 5 |
| f1040.line6a | — | — | — | 4 | — | 2 (stage10.ss.top, stage16.ira.i10) |
| f1040.line6b | — | — | — | 4 | PE: 1680 compared (488 nonzero), 20 excluded; TC: 1451 compared (428 nonzero), 249 excluded | 17 |
| f1040.line6c | — | — | — | 4 | — | 1 (stage10.refuse.lump_sum) |
| f1040.line6d | — | — | — | 4 | — | 2 (stage10.ss.mfs_together, stage10.ss.mfs_apart) |
| f1040.line7a | 1 (example.official) | — | — | 4 | — | 120 |
| f1040.line8 | — | — | — | 4 | — | 51 |
| f1040.line9 | — | — | — | 4 | — | 22 |
| f1040.line10 | — | — | — | 4 | PE: 1680 compared (681 nonzero), 20 excluded; TC: 1451 compared (513 nonzero), 249 excluded | 41 |
| f1040.line11a | — | — | — | 4 | E via f1040.line11b (PE, TC) | 142 |
| f1040.line11b | — | — | — | 4 | PE: 1680 compared (1680 nonzero), 20 excluded; TC: 1451 compared (1451 nonzero), 249 excluded | 36 |
| f1040.line12e | — | — | — | 4 | — | 46 |
| f1040.line13a | — | — | — | 4 | PE: 1547 compared (397 nonzero), 121 excluded; TC below rule: 1111 compared (143 nonzero), 571 excluded | 7 |
| f1040.line13b | — | — | — | 4 | PE: 1556 compared (530 nonzero), 144 excluded; TC: 1451 compared (530 nonzero), 249 excluded | 13 |
| f1040.line14 | — | — | — | 4 | — | 22 |
| f1040.line15 | 1 (example.official) | — | — | 4 | PE: 1440 compared (1274 nonzero), 239 excluded; TC: 973 compared (973 nonzero), 727 excluded | 139 |
| f1040.gate.qdcg_applies | 1 (example.official) | — | — | — | — | 65 |
| f1040.gate.sdtw | — | — | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| f1040.line16 | 1 (example.official) | — | — | 4 | PE: 1415 compared (1233 nonzero), 264 excluded; TC: 973 compared (853 nonzero), 710 excluded | 142 |
| f1040.line17 | — | — | — | 4 | — | 5 |
| f1040.line18 | — | — | — | 4 | — | 133 |
| f1040.line19 | — | — | — | 4 | PE: 1024 compared (486 nonzero), 661 excluded; TC: 824 compared (451 nonzero), 876 excluded | 53 |
| f1040.line20 | — | — | — | 4 | TC: 986 compared (214 nonzero), 710 excluded | 3 |
| f1040.line21 | — | — | — | 4 | — | 4 |
| f1040.line22 | — | — | — | 4 | — | 6 |
| f1040.line23 | — | — | — | 4 | — | 15 |
| f1040.line24 | — | — | — | 4 | TC: 943 compared (737 nonzero), 740 excluded | 6 |
| f1040.line25a | — | — | — | 4 | — | 3 |
| f1040.line25b | — | — | — | — | — | 3 |
| f1040.line25c | — | — | — | — | — | 3 |
| f1040.line25d | — | — | — | 4 | — | 3 |
| f1040.line26 | — | — | — | — | — | 3 |
| f1040.line27a | — | — | — | 4 | PE: 1680 compared (280 nonzero), 20 excluded; TC: 1451 compared (235 nonzero), 249 excluded | 71 |
| f1040.line27b | — | — | — | 4 | — | 2 (stage9.eic.no_child.4000, stage9.eic.refuse.clergy_schedule1) |
| f1040.line27c | — | — | — | 4 | — | 10 |
| f1040.separated_spouses | — | — | — | 4 | — | 4 |
| f1040.line28 | — | — | — | 4 | PE: 1024 compared (206 nonzero), 661 excluded; TC below rule: 824 compared (109 nonzero), 876 excluded | 31 |
| f1040.line29 | — | — | — | 4 | — | 4 |
| f1040.line30 | — | — | — | 4 | — | 4 |
| f1040.line31 | — | — | — | 4 | — | 24 |
| f1040.line32 | — | — | — | 4 | — | 4 |
| f1040.line33 | — | — | — | 4 | — | 19 |
| f1040.line34 | — | — | — | 4 | — | 42 |
| f1040.line35a | — | — | — | — | — | 3 |
| f1040.line36 | — | — | — | — | — | 3 |
| f1040.line37 | — | — | — | 4 | — | 43 |

Unasserted lines: f1040.ira_rollovers, f1040.plan_rollovers

## Form 2441 — Child and Dependent Care Expenses (Parts I to III)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f2441.zero | — | — | — | — | — | — |
| f2441.benefits | — | — | — | — | — | — |
| f2441.care | — | — | — | — | — | — |
| f2441.filing | — | — | — | — | — | — |
| f2441.student_disabled | — | — | — | — | — | — |
| f2441.spouse_died | — | — | — | — | — | — |
| f2441.spouse_died_gate | — | — | — | — | — | — |
| f2441.nondependent | — | — | — | — | — | — |
| f2441.nondependent_gate | — | — | — | — | — | — |
| f2441.provider_count | — | — | — | — | — | — |
| f2441.related_count | — | — | — | — | — | — |
| f2441.provider_ineligible | — | — | — | — | — | — |
| f2441.line1_box | — | — | — | 6 | — | — |
| f2441.statement_count | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.statement_notice | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_count | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_notice | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.provider_paid | — | — | — | — | — | — |
| f2441.line1_paid | — | — | — | — | — | — |
| f2441.qp_count | — | — | — | — | — | 3 |
| f2441.line2_box | — | — | — | 6 | — | 1 (stage15.regress.f2441.three_qualifying_persons) |
| f2441.paid_total | — | — | — | — | — | 3 |
| f2441.limit_one | — | — | — | — | — | — |
| f2441.limit_two | — | — | — | — | — | — |
| f2441.two_or_more | — | — | — | — | — | — |
| f2441.limit | — | — | — | — | — | 1 (stage15.regress.f2441.nonqualifying_dependent) |
| f2441.line3_expenses | — | — | — | — | — | — |
| f2441.line3 | — | — | — | 6 | — | 27 |
| f2441.has_1e | — | — | — | — | — | — |
| f2441.box10_persons | — | — | — | — | — | — |
| f2441.one_box10 | — | — | — | — | — | — |
| f2441.attrib_gate | — | — | — | — | — | — |
| f2441.line4 | — | — | — | 5 | — | 30 |
| f2441.spouse_earned | — | — | — | — | — | — |
| f2441.line5 | — | — | — | 5 | — | 31 |
| f2441.joint | — | — | — | — | — | — |
| f2441.line6_34 | — | — | — | — | — | — |
| f2441.line6_345 | — | — | — | — | — | — |
| f2441.line6 | — | — | — | 6 | — | 26 |
| f2441.line7 | — | — | — | 5 | — | 26 |
| f2441.line8 | — | — | — | 5 | — | 26 |
| f2441.line9a | — | — | — | 6 | — | 26 |
| f2441.line9b | — | — | — | 6 | — | 1 (stage15.refuse.f2441.prior_year) |
| f2441.prior_year | — | — | — | — | — | — |
| f2441.line9c | — | — | — | 6 | — | 26 |
| f2441.clw1 | — | — | — | 5 | — | 10 |
| f2441.clw2 | — | — | — | 6 | — | 10 |
| f2441.clw3 | — | — | — | 5 | — | 10 |
| f2441.line10 | — | — | — | 5 | — | 26 |
| f2441.line11 | — | — | — | 6 | — | 30 |
| f2441.line12 | — | — | — | 6 | — | 7 |
| f2441.line13 | — | — | — | — | — | 7 |
| f2441.line14 | — | — | — | — | — | 7 |
| f2441.line15_sum | — | — | — | — | — | — |
| f2441.line14_bad | — | — | — | — | — | — |
| f2441.line15 | — | — | — | 6 | — | 8 |
| f2441.paid_2026 | — | — | — | — | — | — |
| f2441.line16 | — | — | — | 6 | — | 7 |
| f2441.line17 | — | — | — | 6 | — | 7 |
| f2441.line18 | — | — | — | 2 (classm.f2441.2, classm.f2441.4) | — | 10 |
| f2441.spouse_earned_b | — | — | — | — | — | — |
| f2441.line19 | — | — | — | 2 (classm.f2441.2, classm.f2441.3) | — | 11 |
| f2441.line20_17_18 | — | — | — | — | — | — |
| f2441.line20_all | — | — | — | — | — | — |
| f2441.line20 | — | — | — | 6 | — | 7 |
| f2441.plans_differ | — | — | — | — | — | — |
| f2441.employer_care | — | — | — | — | — | — |
| f2441.employer_care_gate | — | — | — | — | — | — |
| f2441.plan_max | — | — | — | — | — | — |
| f2441.exclusion_max | — | — | — | — | — | 1 (stage15.regress.f2441.exclusion_max) |
| f2441.line21 | — | — | — | 6 | — | 9 |
| f2441.line22 | — | — | — | 6 | — | 7 |
| f2441.line23 | — | — | — | 6 | — | 7 |
| f2441.line24_20_21 | — | — | — | — | — | — |
| f2441.line24 | — | — | — | 6 | — | 8 |
| f2441.line25 | — | — | — | 6 | — | 7 |
| f2441.line26 | — | — | — | 6 | — | 8 |
| f2441.line27 | — | — | — | — | — | 7 |
| f2441.line28 | — | — | — | 6 | — | 8 |
| f2441.line29 | — | — | — | — | — | 7 |
| f2441.line30 | — | — | — | 6 | — | 3 |
| f2441.line31 | — | — | — | 6 | — | 3 |

Unasserted lines: f2441.zero, f2441.filing, f2441.spouse_died_gate, f2441.nondependent_gate, f2441.provider_count, f2441.related_count, f2441.provider_ineligible, f2441.provider_paid, f2441.line1_paid, f2441.limit_one, f2441.limit_two, f2441.two_or_more, f2441.line3_expenses, f2441.has_1e, f2441.box10_persons, f2441.one_box10, f2441.attrib_gate, f2441.spouse_earned, f2441.joint, f2441.line6_34, f2441.line6_345, f2441.line15_sum, f2441.line14_bad, f2441.spouse_earned_b, f2441.line20_17_18, f2441.line20_all, f2441.employer_care_gate, f2441.line24_20_21

## Form 4562 — Depreciation and Amortization, one per business

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f4562.line12 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line14 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line17 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19a | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19b | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19c | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19d | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19f | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line19e | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line21 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line22 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line25 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line26h | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line28 | — | — | — | 1 (classm.f4562.1) | — | — |
| f4562.line29 | — | — | — | 1 (classm.f4562.1) | — | — |

## Form 4952 — supported investment-interest deduction and election

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f4952.line1 | — | — | — | — | — | — |
| f4952.carryover | — | — | — | — | — | — |
| f4952.unsupported | — | — | — | — | — | — |
| f4952.alternative_allocation | — | — | — | — | — | — |
| f4952.line4a | — | — | — | 3 | — | — |
| f4952.line4g | — | — | — | — | — | — |
| f4952.zero | — | — | — | — | — | — |
| f4952.line2 | — | — | — | 3 | — | 4 |
| f4952.line3 | — | — | — | 3 | — | 1 (stage16.cleanup.refuse.f4952_unsupported) |
| f4952.line4b | — | — | — | 3 | — | — |
| f4952.bad_dividends | — | — | — | — | — | — |
| f4952.line4c | — | — | — | 3 | — | — |
| f4952.line4d | — | — | — | 3 | — | 1 (stage4.interest.short_term) |
| f4952.line4e | — | — | — | 3 | — | 1 (stage4.interest.short_term) |
| f4952.line4f | — | — | — | 3 | — | 1 (stage4.interest.short_term) |
| f4952.election_limit | — | — | — | — | — | 1 (stage4.interest.short_term) |
| f4952.bad_election | — | — | — | — | — | — |
| f4952.election | — | — | — | — | — | 5 |
| f4952.line4h | — | — | — | 3 | — | — |
| f4952.line5 | — | — | — | 3 | — | 4 |
| f4952.line6 | — | — | — | 3 | — | — |
| f4952.line7 | — | — | — | 3 | — | 3 |
| f4952.line8 | — | — | — | 3 | — | 8 |
| f4952.exception | — | — | — | — | — | — |
| f4952.required | — | — | — | — | — | 8 |

Unasserted lines: f4952.zero, f4952.bad_dividends, f4952.bad_election, f4952.exception

## Form 5695 — Residential Energy Credits (Parts I and II)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f5695.zero | — | — | — | — | — | — |
| f5695.part1_any | — | — | — | — | — | — |
| f5695.part2_any | — | — | — | — | — | — |
| f5695.business_use | — | — | — | — | — | — |
| f5695.construction_later | — | — | — | — | — | — |
| f5695.line1 | — | — | — | — | — | 9 |
| f5695.line2 | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line3 | — | — | — | — | — | 1 (stage16.cleanup.f5695_small_wind) |
| f5695.line4 | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line5a | — | — | — | — | — | — |
| f5695.battery_cost | — | — | — | — | — | — |
| f5695.line5b | — | — | — | 7 | — | 1 (stage15.f5695.s4) |
| f5695.line6a | — | — | — | 7 | — | 13 |
| f5695.rce_rate | — | — | — | — | — | — |
| f5695.line6b | — | — | — | 7 | — | 11 |
| f5695.line7a | — | — | — | — | — | — |
| f5695.line11 | — | — | — | 7 | — | 1 (stage15.refuse.f5695.fuel_cell) |
| f5695.line12 | — | — | — | — | — | 1 (stage15.f5695.s5) |
| f5695.line13 | — | — | — | 7 | — | 12 |
| f5695.claiming_part1 | — | — | — | — | — | — |
| f5695.rce_ws1 | — | — | — | — | — | 11 |
| f5695.ctc_line19 | — | — | — | — | — | — |
| f5695.ctc | — | — | — | — | — | — |
| f5695.rce_ws2 | — | — | — | — | — | 12 |
| f5695.rce_ws3 | — | — | — | — | — | 11 |
| f5695.line14 | — | — | — | 7 | — | 12 |
| f5695.line15 | — | — | — | 7 | — | 12 |
| f5695.line16 | — | — | — | 7 | — | 9 |
| f5695.line17a | — | — | — | — | — | — |
| f5695.line17b | — | — | — | — | — | — |
| f5695.line17c | — | — | — | — | — | — |
| f5695.sec_a_claimed | — | — | — | — | — | — |
| f5695.line17e | — | — | — | — | — | — |
| f5695.sec_a_new_home | — | — | — | — | — | — |
| f5695.eehi_rate | — | — | — | — | — | — |
| f5695.line18a | — | — | — | — | — | 6 |
| f5695.ins_30 | — | — | — | — | — | — |
| f5695.insulation_max | — | — | — | — | — | — |
| f5695.ins_capped | — | — | — | — | — | — |
| f5695.line18b | — | — | — | 7 | — | 7 |
| f5695.line19a | — | — | — | — | — | 4 |
| f5695.door1_30 | — | — | — | — | — | — |
| f5695.door_max | — | — | — | — | — | — |
| f5695.line19c | — | — | — | 7 | — | 4 |
| f5695.line19d_i | — | — | — | — | — | — |
| f5695.line19d_ii | — | — | — | — | — | — |
| f5695.line19e | — | — | — | — | — | 4 |
| f5695.line19f | — | — | — | 7 | — | 4 |
| f5695.line19g | — | — | — | 7 | — | 4 |
| f5695.doors_sum | — | — | — | — | — | — |
| f5695.doors_max | — | — | — | — | — | — |
| f5695.doors_cost | — | — | — | — | — | — |
| f5695.qmid_doors | — | — | — | — | — | — |
| f5695.doors_no_qmid | — | — | — | — | — | — |
| f5695.doors_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line19h | — | — | — | 7 | — | 4 |
| f5695.line20a_i | — | — | — | — | — | — |
| f5695.line20a_ii | — | — | — | — | — | — |
| f5695.line20a_iii | — | — | — | — | — | — |
| f5695.line20a_iv | — | — | — | — | — | — |
| f5695.line20b | — | — | — | — | — | 4 |
| f5695.line20c | — | — | — | 7 | — | 4 |
| f5695.windows_30 | — | — | — | — | — | — |
| f5695.windows_max | — | — | — | — | — | — |
| f5695.qmid_windows | — | — | — | — | — | — |
| f5695.windows_no_qmid | — | — | — | — | — | — |
| f5695.windows_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line20d | — | — | — | 7 | — | 4 |
| f5695.line21a | — | — | — | — | — | — |
| f5695.line21b | — | — | — | — | — | — |
| f5695.sec_b_claimed | — | — | — | — | — | — |
| f5695.b_new_home | — | — | — | — | — | — |
| f5695.sec_b_new_home | — | — | — | — | — | — |
| f5695.item_max | — | — | — | — | — | — |
| f5695.line22a | — | — | — | — | — | 3 |
| f5695.line22b | — | — | — | — | — | 3 |
| f5695.line22c | — | — | — | 7 | — | 3 |
| f5695.ac_30 | — | — | — | — | — | — |
| f5695.qmid_ac | — | — | — | — | — | — |
| f5695.ac_no_qmid | — | — | — | — | — | — |
| f5695.ac_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line22d | — | — | — | 7 | — | 3 |
| f5695.line23a_i | — | — | — | — | — | — |
| f5695.line23a_ii | — | — | — | — | — | — |
| f5695.line23b | — | — | — | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line23c | — | — | — | 7 | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.wh_30 | — | — | — | — | — | — |
| f5695.qmid_wh | — | — | — | — | — | — |
| f5695.wh_no_qmid | — | — | — | — | — | — |
| f5695.wh_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line23d | — | — | — | 7 | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line24a | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24b | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24c | — | — | — | 7 | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.furnace_30 | — | — | — | — | — | — |
| f5695.qmid_furnace | — | — | — | — | — | — |
| f5695.furnace_no_qmid | — | — | — | — | — | — |
| f5695.furnace_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line24d | — | — | — | 7 | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line25a | — | — | — | — | — | — |
| f5695.enabling_claimed | — | — | — | — | — | — |
| f5695.line25c | — | — | — | — | — | 2 (stage15.f5695-2.e6, stage15.f5695-2.e7) |
| f5695.enabling_30 | — | — | — | — | — | — |
| f5695.qmid_enabling | — | — | — | — | — | — |
| f5695.enabling_no_qmid | — | — | — | — | — | — |
| f5695.enabling_capped | — | — | — | — | — | 2 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp, stage15.regress.f5695.enabling_cap) |
| f5695.line25e | — | — | — | 7 | — | 3 |
| f5695.line26a | — | — | — | — | — | — |
| f5695.line26b | — | — | — | — | — | 2 (stage15.f5695.s6, stage15.f5695-2.e9) |
| f5695.audit_30 | — | — | — | — | — | — |
| f5695.audit_max | — | — | — | — | — | — |
| f5695.audit_capped | — | — | — | — | — | — |
| f5695.line26c | — | — | — | 7 | — | 3 |
| f5695.line27 | — | — | — | 7 | — | 24 |
| f5695.annual_max | — | — | — | — | — | — |
| f5695.line28 | — | — | — | 7 | — | 22 |
| f5695.line29a | — | — | — | — | — | 4 |
| f5695.line29b | — | — | — | — | — | 5 |
| f5695.line29c | — | — | — | — | — | 1 (stage15.f5695-2.e10) |
| f5695.line29d | — | — | — | — | — | 3 |
| f5695.line29e | — | — | — | — | — | — |
| f5695.line29f | — | — | — | — | — | 3 |
| f5695.line29g | — | — | — | 7 | — | 5 |
| f5695.hp_30 | — | — | — | — | — | — |
| f5695.heat_pump_max | — | — | — | — | — | — |
| f5695.qmid_hp | — | — | — | — | — | — |
| f5695.hp_no_qmid | — | — | — | — | — | — |
| f5695.hp_capped | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line29h | — | — | — | 7 | — | 5 |
| f5695.joint_occupancy | — | — | — | — | — | — |
| f5695.separate_homes | — | — | — | — | — | — |
| f5695.separate_homes_joint | — | — | — | — | — | — |
| f5695.line30 | — | — | — | 7 | — | 27 |
| f5695.eehi_ws1 | — | — | — | — | — | 20 |
| f5695.eehi_ws2 | — | — | — | — | — | 21 |
| f5695.eehi_ws3 | — | — | — | — | — | 20 |
| f5695.line31 | — | — | — | 7 | — | 20 |
| f5695.line32 | — | — | — | 7 | — | 22 |
| f5695.line32a | — | — | — | 7 | — | — |
| f5695.condo | — | — | — | — | — | — |
| f5695.line32b | — | — | — | 7 | — | — |

Unasserted lines: f5695.zero, f5695.rce_rate, f5695.claiming_part1, f5695.ctc_line19, f5695.ctc, f5695.sec_a_claimed, f5695.sec_a_new_home, f5695.eehi_rate, f5695.ins_30, f5695.insulation_max, f5695.ins_capped, f5695.door1_30, f5695.door_max, f5695.doors_sum, f5695.doors_max, f5695.doors_cost, f5695.doors_no_qmid, f5695.windows_30, f5695.windows_max, f5695.windows_no_qmid, f5695.sec_b_claimed, f5695.sec_b_new_home, f5695.item_max, f5695.ac_30, f5695.ac_no_qmid, f5695.wh_30, f5695.wh_no_qmid, f5695.furnace_30, f5695.furnace_no_qmid, f5695.enabling_claimed, f5695.enabling_30, f5695.enabling_no_qmid, f5695.audit_30, f5695.audit_max, f5695.audit_capped, f5695.annual_max, f5695.hp_30, f5695.heat_pump_max, f5695.hp_no_qmid, f5695.separate_homes_joint

## Form 8606 — Nondeductible IRAs, Part I (nondeductible contributions with no 2025 distribution), one per person

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8606.files | — | — | — | 1 (classm.f8606.1) | — | — |
| f8606.line1 | — | — | — | — | — | 7 |
| f8606.line2 | — | — | — | — | — | 7 |
| f8606.line3 | — | — | — | — | — | 8 |
| f8606.dist | — | — | — | — | — | — |
| f8606.line14 | — | — | — | — | — | 8 |

Unasserted lines: f8606.dist

## Form 8880 — Credit for Qualified Retirement Savings Contributions (the saver's credit)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8880.zero | — | — | — | — | — | — |
| f8880.joint | — | — | — | — | — | — |
| f8880.line1a | — | — | — | 4 | — | 33 |
| f8880.line1b | — | — | — | 4 | — | 8 |
| f8880.line2a | — | — | — | 4 | — | 32 |
| f8880.line2b | — | — | — | 4 | — | 9 |
| f8880.line3a | — | — | — | 4 | — | 32 |
| f8880.line3b | — | — | — | 4 | — | 8 |
| f8880.dist_2025 | — | — | — | — | — | — |
| f8880.prior_joint_sum | — | — | — | — | — | — |
| f8880.prior_joint | — | — | — | — | — | — |
| f8880.prior_own_a | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.prior_own_b | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.line4a | — | — | — | 4 | — | 34 |
| f8880.line4b_joint | — | — | — | — | — | — |
| f8880.line4b | — | — | — | 4 | — | 10 |
| f8880.line5a | — | — | — | 4 | — | 33 |
| f8880.line5b | — | — | — | 4 | — | 9 |
| f8880.cap | — | — | — | — | — | — |
| f8880.inelig_a | — | — | — | — | — | — |
| f8880.inelig_b | — | — | — | — | — | — |
| f8880.elig_a | — | — | — | — | — | — |
| f8880.elig_b | — | — | — | — | — | — |
| f8880.line6a_figured | — | — | — | — | — | — |
| f8880.line6b_figured | — | — | — | — | — | — |
| f8880.line6a | — | — | — | 4 | — | 33 |
| f8880.line6b | — | — | — | 4 | — | 9 |
| f8880.line7 | — | — | — | 4 | — | 33 |
| f8880.line8 | — | — | — | 2 (classm.f8880.2, classm.f8880.3) | — | 32 |
| f8880.line9 | — | — | — | 3 | — | 31 |
| f8880.line10 | — | — | — | 4 | — | 27 |
| f8880.clw1 | — | — | — | — | — | 27 |
| f8880.clw2 | — | — | — | — | — | 27 |
| f8880.clw3 | — | — | — | — | — | 27 |
| f8880.line11 | — | — | — | 3 | — | 27 |
| f8880.agi_limit | — | — | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line3_total | — | — | — | — | — | — |
| f8880.can_take | — | — | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line12_figured | — | — | — | — | — | — |
| f8880.line12 | — | — | — | 4 | — | 28 |

Unasserted lines: f8880.zero, f8880.joint, f8880.dist_2025, f8880.prior_joint_sum, f8880.prior_joint, f8880.line4b_joint, f8880.cap, f8880.inelig_a, f8880.inelig_b, f8880.elig_a, f8880.elig_b, f8880.line6a_figured, f8880.line6b_figured, f8880.line3_total, f8880.line12_figured

## Form 8889 — Health Savings Accounts (Parts I and II)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8889.one | — | — | — | — | — | — |
| f8889.zero | — | — | — | — | — | — |
| f8889.line2 | — | — | — | — | — | 1 (stage16.mut.hsa_contrib_and_dist) |
| f8889.line9 | — | — | — | — | — | — |
| f8889.any | — | — | — | 5 | — | — |
| f8889.unsupported | — | — | — | — | — | — |
| f8889.mfs | — | — | — | 5 | — | — |
| f8889.months_eligible | — | — | — | — | — | — |
| f8889.months_family | — | — | — | — | — | — |
| f8889.bad_months | — | — | — | 5 | — | 4 |
| f8889.age55 | — | — | — | — | — | — |
| f8889.twelve | — | — | — | — | — | — |
| f8889.married_family | — | — | — | 5 | — | — |
| f8889.age55_line3 | — | — | — | 5 | — | — |
| f8889.self_amount | — | — | — | 5 | — | — |
| f8889.self_under55 | — | — | — | — | — | — |
| f8889.self_55 | — | — | — | — | — | — |
| f8889.age55_unmarried | — | — | — | 5 | — | — |
| f8889.family_amount | — | — | — | 5 | — | — |
| f8889.family_under55 | — | — | — | — | — | — |
| f8889.family_55 | — | — | — | — | — | — |
| f8889.family_extra | — | — | — | 5 | — | — |
| f8889.chart_self | — | — | — | 5 | — | — |
| f8889.chart_family | — | — | — | 5 | — | — |
| f8889.chart_total | — | — | — | 5 | — | — |
| f8889.chart_limit | — | — | — | 5 | — | — |
| f8889.all_year | — | — | — | 5 | — | — |
| f8889.changed | — | — | — | 5 | — | — |
| f8889.dec_coverage | — | — | — | — | — | — |
| f8889.dec_amount | — | — | — | 5 | — | — |
| f8889.last_month | — | — | — | — | — | — |
| f8889.use_last_month | — | — | — | 5 | — | — |
| f8889.line3_changed | — | — | — | 5 | — | — |
| f8889.line3_all_year | — | — | — | 4 | — | — |
| f8889.line3_last_month | — | — | — | 5 | — | — |
| f8889.line3_part_year | — | — | — | 4 | — | — |
| f8889.line3 | — | — | — | 5 | — | 11 |
| f8889.line4 | — | — | — | 5 | — | — |
| f8889.line5 | — | — | — | 5 | — | — |
| f8889.family_year | — | — | — | 4 | — | — |
| f8889.family_dec_year | — | — | — | 5 | — | — |
| f8889.family_counted | — | — | — | 5 | — | — |
| f8889.step1_total | — | — | — | 5 | — | — |
| f8889.step1_line3 | — | — | — | 5 | — | — |
| f8889.step1 | — | — | — | 5 | — | 3 |
| f8889.step1_x2 | — | — | — | 5 | — | — |
| f8889.two | — | — | — | — | — | — |
| f8889.share_equal | — | — | — | 5 | — | — |
| f8889.allocation | — | — | — | — | — | — |
| f8889.allocated | — | — | — | — | — | — |
| f8889.share_raw | — | — | — | 4 | — | — |
| f8889.allocation_bad | — | — | — | 5 | — | — |
| f8889.share | — | — | — | 4 | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.self_year | — | — | — | 5 | — | — |
| f8889.self_counted | — | — | — | 5 | — | — |
| f8889.self_all | — | — | — | 5 | — | — |
| f8889.self_family_months | — | — | — | 5 | — | — |
| f8889.self_dec_year | — | — | — | 5 | — | — |
| f8889.self_in_family | — | — | — | 5 | — | — |
| f8889.step4_total | — | — | — | 5 | — | — |
| f8889.step4 | — | — | — | 5 | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.line6_split | — | — | — | 4 | — | — |
| f8889.split | — | — | — | 5 | — | — |
| f8889.line6 | — | — | — | 5 | — | 8 |
| f8889.additional | — | — | — | — | — | — |
| f8889.line7_year | — | — | — | 5 | — | — |
| f8889.line7_counted | — | — | — | 5 | — | — |
| f8889.line7_total | — | — | — | 5 | — | — |
| f8889.line7_worksheet | — | — | — | 5 | — | — |
| f8889.line7_applies | — | — | — | 5 | — | — |
| f8889.line7 | — | — | — | 5 | — | 3 |
| f8889.line8 | — | — | — | 5 | — | 2 (stage13.hsa_age55_line7, stage13.hsa_last_month_spouses) |
| f8889.line10 | — | — | — | 5 | — | — |
| f8889.line11 | — | — | — | 5 | — | — |
| f8889.line12 | — | — | — | 5 | — | 2 (stage11.hsa.self_full_year, stage11.hsa.employer) |
| f8889.excess | — | — | — | 5 | — | — |
| f8889.line13_figured | — | — | — | 5 | — | — |
| f8889.line13 | — | — | — | 5 | — | 19 |
| f8889.line14a | — | — | — | — | — | 6 |
| f8889.has_dist | — | — | — | 5 | — | — |
| f8889.rollover | — | — | — | — | — | — |
| f8889.rollover_bad | — | — | — | 5 | — | — |
| f8889.line14b | — | — | — | 5 | — | 6 |
| f8889.line14c | — | — | — | 5 | — | 7 |
| f8889.medical | — | — | — | — | — | — |
| f8889.line15 | — | — | — | 5 | — | 6 |
| f8889.line16_figured | — | — | — | 5 | — | 1 (stage16.refuse.f8889.unsupported_part2) |
| f8889.line16 | — | — | — | 5 | — | 9 |
| f8889.has_taxable | — | — | — | 5 | — | — |
| f8889.line17a | — | — | — | — | — | 4 |
| f8889.subject_part | — | — | — | — | — | — |
| f8889.subject_bad | — | — | — | 5 | — | — |
| f8889.subject_excepted | — | — | — | 5 | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.subject | — | — | — | 5 | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.line17b_figured | — | — | — | 5 | — | — |
| f8889.line17b | — | — | — | 5 | — | 6 |

Unasserted lines: f8889.one, f8889.zero, f8889.twelve, f8889.self_under55, f8889.self_55, f8889.family_under55, f8889.family_55, f8889.two, f8889.additional

## Form 8959 — Additional Medicare Tax on wages and self-employment income

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8959.unsupported | — | — | — | — | — | — |
| f8959.zero | — | — | — | — | — | — |
| f8959.line1 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 3 |
| f8959.line2 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line3 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line8 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 5 |
| f8959.line14 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line23 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line4 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line5 | — | — | — | 1 (classm.f8959.2) | — | 2 (stage13.additional_medicare_joint, stage4.medicare.withholding) |
| f8959.line6 | 1 (stage4.official.medicare_example5) | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 17 |
| f8959.line7 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 4 |
| f8959.line9 | — | — | — | 1 (classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line10 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line11 | — | — | — | 1 (classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line12 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage14.f8959.se_above_threshold, stage4.medicare.withholding) |
| f8959.line13 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 3 |
| f8959.line15 | — | — | — | 1 (classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line16 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage16.cleanup.f8959_line16_se_refused, stage4.medicare.withholding) |
| f8959.line17 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line18 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | PE: 1680 compared (168 nonzero), 20 excluded; TC: 1451 compared (143 nonzero), 249 excluded | 20 |
| f8959.line19 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line20 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line21 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line22 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 1 (stage4.medicare.withholding) |
| f8959.line24 | — | — | — | 2 (classm.f8959.1, classm.f8959.2) | — | 4 |

Unasserted lines: f8959.zero

## Form 8960 — wage, interest, dividend and securities slice

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8960.unsupported | — | — | — | — | — | — |
| f8960.refund | — | — | — | — | — | — |
| f8960.allocated_taxes | — | — | — | — | — | — |
| f8960.zero | — | — | — | — | — | — |
| f8960.line1 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 4 |
| f8960.line2 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | — |
| f8960.line3 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line4a | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line4b | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line5b | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line5c | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line6 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line7 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line9c | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line10 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 4 |
| f8960.line4c | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | — |
| f8960.line5a | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 1 (stage4.niit.loss_floor) |
| f8960.line5d | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | — |
| f8960.line8 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 2 (stage4.niit.allocated, stage4.additional_taxes.combined) |
| f8960.line9a | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line9b | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 3 |
| f8960.line9d | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 1 (stage4.additional_taxes.combined) |
| f8960.line11 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| f8960.line12 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 4 |
| f8960.line13 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 4 |
| f8960.line14 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | — |
| f8960.line15 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | — |
| f8960.line16 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | — | 1 (stage16.small.s10) |
| f8960.line17 | — | — | — | 2 (classm.f8960.1, classm.f8960.2) | PE: 1528 compared (181 nonzero), 172 excluded; TC: 1384 compared (154 nonzero), 316 excluded | 20 |
| f8960.bad_allocation | — | — | — | — | — | — |

Unasserted lines: f8960.zero, f8960.bad_allocation

## Form 8995 — Qualified Business Income Deduction Simplified Computation

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | 3 | — | 3 |
| f8995.line3 | — | — | — | 3 | — | 1 (stage14.qbi.carryforward) |
| f8995.line4_sum | — | — | — | — | — | — |
| f8995.line4 | — | — | — | 3 | — | 2 (stage14.sc.loss, stage14.qbi.carryforward) |
| f8995.line5 | — | — | — | 3 | — | 2 (stage14.sc.basic, stage14.qbi.carryforward) |
| f8995.line7 | — | — | — | 3 | — | — |
| f8995.loss | — | — | — | — | — | — |
| f8995.line16 | — | — | — | 3 | — | 1 (stage14.sc.loss) |
| f8995.line17 | — | — | — | 3 | — | — |
| f8995.line6 | — | — | — | 3 | — | — |
| f8995.line8 | — | — | — | 3 | — | — |
| f8995.line9 | — | — | — | 3 | — | — |
| f8995.line10 | — | — | — | 3 | — | — |
| f8995.line11 | — | — | — | 3 | — | — |
| f8995.line12 | — | — | — | 3 | — | — |
| f8995.line13 | — | — | — | 3 | — | — |
| f8995.line14 | — | — | — | 3 | — | 1 (stage14.sc.basic) |
| f8995.line15 | — | — | — | 3 | — | 8 |

Unasserted lines: f8995.line4_sum, f8995.loss

## Form 8995-A — Part IV dividend-only computation

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| f8995a.line27 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line29 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line38 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line40 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line28 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line30 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line31 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line32 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line33 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line34 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line35 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line36 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line37 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — |
| f8995a.line39 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | 6 |

## Foreign tax credit — election without Form 1116

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| ftc.taxes | — | — | — | — | — | — |
| ftc.all_passive | — | — | — | — | — | — |
| ftc.statements | — | — | — | — | — | — |
| ftc.eligible | — | — | — | — | — | — |
| ftc.elect | — | — | — | — | — | — |
| ftc.limit | — | — | — | — | — | — |
| ftc.zero | — | — | — | — | — | — |
| ftc.has_tax | — | — | — | — | — | 1 (stage4.base) |
| ftc.needs1116 | — | — | — | — | — | — |
| ftc.limited | — | — | — | — | — | — |
| ftc.credit | — | — | — | — | — | 9 |

Unasserted lines: ftc.limit, ftc.zero, ftc.needs1116, ftc.limited

## 28% Rate Gain Worksheet — distribution-only path

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| g28.line1 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.line2 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.line3 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.line5 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.line4 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.line6 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — |
| g28.combined | — | — | — | — | — | — |
| g28.line7 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | 1 (stage4.feeders.shortloss) |

Unasserted lines: g28.combined

## Form 8283 — groups of similar noncash property

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| gift.deduction | — | — | — | — | — | — |
| gift.public_securities | — | — | — | — | — | — |
| gift.special | — | — | — | — | — | — |
| gift.section_b | — | — | — | 1 (classm.gift.1) | — | — |
| gift.allowed | — | — | — | 1 (classm.gift.1) | — | — |

## Household facts for dependents and head of household

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| household.persons | — | — | — | — | — | — |
| household.taxpayers | — | — | — | — | — | — |
| household.spouses | — | — | — | — | — | — |
| household.roster_ok | — | — | — | — | — | — |
| household.roster_bad | — | — | — | — | — | — |
| household.hsa_people | — | — | — | — | — | — |
| household.hsa_both | — | — | — | — | — | — |
| household.hsa_split_count | — | — | — | — | — | — |
| household.hsa_agreed_count | — | — | — | — | — | — |
| household.hsa_step1_sum | — | — | — | — | — | — |
| household.hsa_share_sum | — | — | — | — | — | — |
| household.work_ssn_count | — | — | — | — | — | — |
| household.any_work_ssn | — | — | — | — | — | — |
| household.all_work_ssn | — | — | — | — | — | — |
| household.tin_count | — | — | — | — | — | — |
| household.all_tin | — | — | — | — | — | — |
| household.id_count | — | — | — | — | — | — |
| household.ctc_ssn | — | — | — | — | — | — |
| household.taxpayer_work_ssn_count | — | — | — | — | — | — |
| household.taxpayer_work_ssn | — | — | — | — | — | — |
| household.home_cost | — | — | — | — | — | — |
| household.unmarried | — | — | — | — | — | — |
| household.test1_persons | — | — | — | — | — | 24 |
| household.test2_persons | — | — | — | — | — | 24 |
| household.test1_met | — | — | — | — | — | 24 |
| household.test2_met | — | — | — | — | — | 24 |
| household.hoh_eligible | — | — | — | — | — | 24 |
| household.hoh_fails | — | — | — | — | — | 24 |

Unasserted lines: household.persons, household.taxpayers, household.spouses, household.roster_ok, household.roster_bad, household.hsa_people, household.hsa_both, household.hsa_split_count, household.hsa_agreed_count, household.hsa_step1_sum, household.hsa_share_sum, household.work_ssn_count, household.any_work_ssn, household.all_work_ssn, household.tin_count, household.all_tin, household.id_count, household.ctc_ssn, household.taxpayer_work_ssn_count, household.taxpayer_work_ssn

## Schedule B — interest payer entries

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| interest.amount | — | — | — | — | — | — |
| interest.penalty | — | — | — | — | — | — |

## IRA Deduction Worksheet — Schedule 1, Line 20

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| ira.zero | — | — | — | — | — | — |
| ira.joint | — | — | — | — | — | — |
| ira.joint_type | — | — | — | — | — | — |
| ira.contrib_total | — | — | — | — | — | — |
| ira.roth_total | — | — | — | — | — | — |
| ira.any_trad | — | — | — | — | — | — |
| ira.cov_count | — | — | — | — | — | — |
| ira.anyone_covered | — | — | — | — | — | — |
| ira.lines2to6 | — | — | — | — | — | — |
| ira.cov_gate | — | — | — | — | — | — |
| ira.cov_you | — | — | — | — | — | — |
| ira.cov_spouse | — | — | — | — | — | — |
| ira.line1a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 12 |
| ira.line1b | — | — | — | 1 (classm.ira.1) | — | 4 |
| ira.line2a_sum | — | — | — | — | — | — |
| ira.line2b_sum | — | — | — | — | — | — |
| ira.line2a | — | — | — | 1 (classm.ira.1) | — | 8 |
| ira.line2b | — | — | — | 1 (classm.ira.1) | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line3 | — | — | — | 1 (classm.ira.2) | — | 7 |
| ira.line4 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 6 |
| ira.line5 | — | — | — | 1 (classm.ira.2) | — | 1 (stage16.mut.ira_joint_full_edge) |
| ira.line6a_sum | — | — | — | — | — | — |
| ira.line6b_sum | — | — | — | — | — | — |
| ira.line6a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 7 |
| ira.line6b | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line7a_sum | — | — | — | — | — | — |
| ira.line7b_sum | — | — | — | — | — | — |
| ira.line7a | — | — | — | 1 (classm.ira.2) | — | 16 |
| ira.line7b | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 6 |
| ira.wages | — | — | — | — | — | — |
| ira.line8 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 10 |
| ira.line9 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 10 |
| ira.line10 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 16 |
| ira.age50_count | — | — | — | — | — | — |
| ira.kbh_none | — | — | — | — | — | — |
| ira.kbh_one | — | — | — | — | — | — |
| ira.kbh_both | — | — | — | — | — | — |
| ira.kbh_amount | — | — | — | — | — | — |
| ira.kbh_short | — | — | — | — | — | — |
| ira.both_kinds | — | — | — | — | — | — |
| ira.all_total | — | — | — | — | — | — |
| ira.over_comp | — | — | — | — | — | — |
| ira.special | — | — | — | — | — | — |
| ira.se_capital | — | — | — | — | — | — |
| ira.se_capital_gate | — | — | — | — | — | — |
| ira.special_gate | — | — | — | — | — | — |
| ira.combat_gate | — | — | — | — | — | — |
| ira.excl_gate | — | — | — | — | — | — |
| ira.line11a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 15 |
| ira.line11b | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 6 |
| ira.line12a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 17 |
| ira.line12b | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | 6 |
| ira.total | — | — | — | — | — | 1 (stage16.refuse.ira.deduct_less) |
| ira.deduct_less | — | — | — | — | — | — |
| ira.less_gate | — | — | — | — | — | — |
| ira.line20 | — | — | — | — | — | 10 |
| ira.basis_total | — | — | — | — | — | — |

Unasserted lines: ira.zero, ira.joint, ira.joint_type, ira.contrib_total, ira.roth_total, ira.any_trad, ira.cov_count, ira.anyone_covered, ira.lines2to6, ira.cov_gate, ira.cov_you, ira.cov_spouse, ira.line2a_sum, ira.line2b_sum, ira.line6a_sum, ira.line6b_sum, ira.line7a_sum, ira.line7b_sum, ira.wages, ira.age50_count, ira.kbh_none, ira.kbh_one, ira.kbh_both, ira.kbh_amount, ira.kbh_short, ira.both_kinds, ira.all_total, ira.over_comp, ira.se_capital_gate, ira.special_gate, ira.combat_gate, ira.excl_gate, ira.less_gate, ira.basis_total

## Form 7206, line 2 — qualified long-term care insurance, one per person covered

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| ltc.payments | — | — | — | — | — | — |
| ltc.age | — | — | — | — | — | — |
| ltc.limit | — | — | — | 2 (classm.ltc.1, classm.ltc.2) | — | — |
| ltc.amount | — | — | — | 2 (classm.ltc.1, classm.ltc.2) | — | — |

## Mid-quarter convention test for property placed in service in 2025

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| mq.q4 | — | — | — | — | — | — |
| mq.total | — | — | — | — | — | — |
| mq.five | — | — | — | — | — | — |
| mq.two | — | — | — | — | — | — |
| mq.q4x5 | — | — | — | — | — | — |
| mq.totalx2 | — | — | — | — | — | — |
| mq.applies | — | — | — | — | — | 6 |

Unasserted lines: mq.q4, mq.total, mq.five, mq.two, mq.q4x5, mq.totalx2

## Schedule 1, line 8z — other income, one entry per item listed

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| oi8z.kind | — | — | — | — | — | — |
| oi8z.amount | — | — | — | — | — | — |
| oi8z.recovery | — | — | — | 1 (classm.oi8z.1) | — | — |
| oi8z.additional_tax | — | — | — | 1 (classm.oi8z.1) | — | — |
| oi8z.figured | — | — | — | 1 (classm.oi8z.1) | — | — |
| oi8z.taxable | — | — | — | 1 (classm.oi8z.1) | — | 3 |

## Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| otjob.one | — | — | — | — | — | — |
| otjob.zero | — | — | — | — | — | — |
| otjob.flsa | — | — | — | — | — | — |
| otjob.special_rule | — | — | — | — | — | — |
| otjob.method | — | — | — | — | — | — |
| otjob.statement | — | — | — | — | — | — |
| otjob.refused | — | — | — | 3 | — | — |
| otjob.figured | — | — | — | 3 | — | — |
| otjob.by_third | — | — | — | 2 (classm.otjob.1, classm.otjob.2) | — | — |
| otjob.by_half | — | — | — | 2 (classm.otjob.1, classm.otjob.2) | — | — |
| otjob.by_quarter | — | — | — | 2 (classm.otjob.1, classm.otjob.3) | — | — |
| otjob.col_b | — | — | — | 3 | — | — |

Unasserted lines: otjob.one, otjob.zero

## Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| person.role | — | — | — | — | — | — |
| person.one | — | — | — | — | — | — |
| person.age65 | — | — | — | — | — | — |
| person.blind | — | — | — | — | — | — |
| person.tin | — | — | — | — | — | — |
| person.itin_applied | — | — | — | — | — | — |
| person.work_ssn | — | — | — | — | — | — |
| person.educator_expenses | — | — | — | — | — | — |
| person.eligible_educator | — | — | — | — | — | — |
| person.born_before_2001 | — | — | — | — | — | — |
| person.born_after_1960 | — | — | — | — | — | — |
| person.died_before_65 | — | — | — | — | — | — |
| person.educator_max | — | — | — | — | — | — |
| person.has_educator_expenses | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.educator_limited | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.educator_eligible_amount | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.educator_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_forms | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_repeated | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_split | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_agreed | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_step1 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_share | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_taxable | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.hsa_addtax | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.tip_employers | — | — | — | 1 (classm.person.1) | — | — |
| person.tip_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.tip_reported | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ot_employers | — | — | — | 1 (classm.person.1) | — | — |
| person.ot_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.rrta | — | — | — | — | — | — |
| person.sc_rrta_count | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.se_rrta | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.employers | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.overcount | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.over | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.wages | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.withheld | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.box1 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.box2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.eligible | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.excess | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.zero | — | — | — | — | — | — |
| person.credit | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.medicare5 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.medicare6 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.sc_count | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ho_count | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.mq_q4 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.mq_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.cost179 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.s179_nonlisted | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.s179_listed | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.income179 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.has_sc | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sc_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.se_screen | — | — | — | — | — | — |
| person.se_screened | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.se_line2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.asset.s179, stage14.refuse.se_screen) |
| person.se_line6 | — | — | — | — | — | 4 |
| person.se_line12 | — | — | — | — | — | 11 |
| person.se_line13 | — | — | — | — | — | 1 (stage14.refuse.se_railroad) |
| person.se_line4c | — | — | — | — | — | 1 (stage14.refuse.se_railroad) |
| person.plan | — | — | — | — | — | — |
| person.plan_screen | — | — | — | — | — | — |
| person.plan_screened | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.cent | — | — | — | — | — | — |
| person.hundred | — | — | — | — | — | — |
| person.sep_rate | — | — | — | — | — | — |
| person.sep_contrib | — | — | — | — | — | 1 (stage14.plan.refuse_screen) |
| person.sep_rate_c | — | — | — | — | — | — |
| person.sep_rate_plus | — | — | — | — | — | — |
| person.sep_s1 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sep_s2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sep_s3 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sep_s5 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.sep.basic, stage14.sep.rate_5) |
| person.comp_limit | — | — | — | — | — | — |
| person.sep_s6 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage14.sep.dollar_limit) |
| person.sep_s7 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage14.sep.rate_5) |
| person.sep_s8 | — | — | — | — | — | — |
| person.sep_s21 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 3 |
| person.sep_excess | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sep_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.sep.refuse_excess, stage14.plan.refuse_two_businesses) |
| person.simple_deferral | — | — | — | — | — | 1 (stage14.plan.refuse_screen_simple) |
| person.simple_age | — | — | — | — | — | — |
| person.simple_kind | — | — | — | — | — | — |
| person.simple_employer | — | — | — | — | — | — |
| person.simple_comp | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage14.simple.match_age50) |
| person.simple_cap | — | — | — | — | — | — |
| person.simple_regular | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.simple_catchup | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.catchup_limit | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.comp_after_regular | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.catchup_max | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.simple.nonelective_60, stage14.simple.refuse_catchup_comp) |
| person.rate3 | — | — | — | — | — | — |
| person.rate2 | — | — | — | — | — | — |
| person.match_3pct | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.deferrals_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.match_max | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.simple.match_age50, stage14.simple.match_high_comp) |
| person.ne_comp | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ne_max | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage14.simple.nonelective_60, stage14.simple.comp_cap) |
| person.employer_max | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.simple_excess | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.simple_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | 4 |
| person.plan_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.s16 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.positive_profits | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sehi | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.qbi | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.eic_part1 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.files_se | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.eic_se_has | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.eic_se | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sc_1a | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_benefits | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_box10 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_has_box10 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_1e_mine | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_1e_counted | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_zero | — | — | — | — | — | — |
| person.dc_1e | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_earned | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.dc_earned_b | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sav_born | — | — | — | — | — | — |
| person.sav_student | — | — | — | — | — | — |
| person.sav_claimed | — | — | — | — | — | — |
| person.sav_ineligible | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sav_trad | — | — | — | — | — | — |
| person.sav_able | — | — | — | — | — | — |
| person.sav_roth | — | — | — | — | — | — |
| person.sav_line1 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 2 (stage15.refuse.person.sav_able, stage16.refuse.person.ira_excess) |
| person.sav_w2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sav_excess | — | — | — | — | — | — |
| person.sav_excess_gate | — | — | — | 1 (classm.person.1) | — | — |
| person.sav_voluntary | — | — | — | — | — | — |
| person.sav_simple_plan | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sav_simple | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.sav_line2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage15.refuse.person.sav_excess) |
| person.sav_prior_joint | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.sav_prior_other | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.ira_trad | — | — | — | — | — | — |
| person.ira_contrib | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_has | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_any_contrib | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_excess | — | — | — | — | — | — |
| person.ira_excess_gate | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_age50 | — | — | — | — | — | — |
| person.ira_work_plan | — | — | — | — | — | — |
| person.ira_se_plan | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_cov | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_limit_under50 | — | — | — | — | — | — |
| person.ira_limit_over50 | — | — | — | — | — | — |
| person.ira_limit | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_not_covered_joint | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_line2_status | — | — | — | — | — | — |
| person.ira_line2_nc | — | — | — | — | — | — |
| person.ira_line2 | — | — | — | 1 (classm.person.1) | — | — |
| person.ira_line6 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_line6_yes | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_wide | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_full_narrow | — | — | — | — | — | — |
| person.ira_full_joint | — | — | — | — | — | — |
| person.ira_full | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_at_full | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_p70 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_p80 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_p35 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_p40 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_prod_wide | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_prod_joint | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_prod | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_rounded | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_min | — | — | — | — | — | — |
| person.ira_floor | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_below | — | — | — | 1 (classm.person.2) | — | — |
| person.ira_line7_figured | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_line7 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_over_limit | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_own_total | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_line11 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 8 |
| person.ira_7or10 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_line12 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.refuse.ira.dist) |
| person.ira_deduction | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.refuse.ira.dist) |
| person.ira_10or11 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_nd_figured | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_nondeductible | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_files_8606 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_basis | — | — | — | — | — | — |
| person.ira_basis_adjusted | — | — | — | — | — | — |
| person.ira_basis_gate | — | — | — | — | — | — |
| person.ira_8606_line2 | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.refuse.person.ira_basis_adjusted) |
| person.ira_dist | — | — | — | — | — | — |
| person.ira_dist_gate | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_8606_line14 | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_ssb_lim | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_ssb_figured | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.refuse.ira.ssb_covered) |
| person.ira_ssb | — | — | — | 2 (classm.person.1, classm.person.2) | — | 1 (stage16.refuse.ira.ssb_covered) |
| person.ira_se_take | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_se_figured | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |
| person.ira_se | — | — | — | 2 (classm.person.1, classm.person.2) | — | — |

Unasserted lines: person.one, person.educator_max, person.zero, person.cent, person.hundred, person.sep_rate_c, person.sep_rate_plus, person.comp_limit, person.sep_s8, person.simple_cap, person.rate3, person.rate2, person.dc_zero, person.ira_limit_under50, person.ira_limit_over50, person.ira_line2_status, person.ira_line2_nc, person.ira_full_narrow, person.ira_full_joint, person.ira_min, person.ira_basis_gate

## Qualified business income and section 199A dividends — amounts and the choice of Form 8995

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| qbi.dividends | — | — | — | — | — | — |
| qbi.unsupported | — | — | — | — | — | — |
| qbi.zero | — | — | — | — | — | — |
| qbi.eligible | — | — | — | — | — | — |
| qbi.carryforward | — | — | — | — | — | — |
| qbi.business_any | — | — | — | — | — | — |
| qbi.via_8995a | — | — | — | — | — | 1 (stage14.refuse.qbi_8995a) |
| qbi.deductions_before | — | — | — | — | — | — |
| qbi.taxable_before | — | — | — | — | — | 2 (stage4.qbi.income_limit, stage4.qbi.zero_income) |
| qbi.net_capital_gain | — | — | — | — | — | — |
| qbi.threshold | — | — | — | — | — | — |
| qbi.use_8995a | — | — | — | — | — | 3 |
| qbi.deduction | — | — | — | — | E via f1040.line13a (PE) | 11 |

Unasserted lines: qbi.zero, qbi.eligible, qbi.business_any, qbi.deductions_before, qbi.net_capital_gain, qbi.threshold

## Qualified Dividends and Capital Gain Tax Worksheet—Line 16

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| qdcg.schedule_d_filed | — | — | — | — | — | 12 |
| qdcg.schedule_d_net_gain | — | — | — | — | — | 1 (qdcg.sd.side) |
| qdcg.line1 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line2 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line3 | — | — | — | 3 | — | 15 |
| qdcg.line4 | — | — | — | 3 | — | 12 |
| qdcg.line5 | — | — | — | 3 | — | 12 |
| qdcg.line6 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line7 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line8 | — | — | — | 3 | — | 12 |
| qdcg.line9 | — | — | — | 3 | — | 12 |
| qdcg.line10 | — | — | — | 3 | — | 12 |
| qdcg.line11 | — | — | — | 3 | — | 12 |
| qdcg.line12 | — | — | — | 3 | — | 12 |
| qdcg.line13 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line14 | 1 (example.official) | — | — | 3 | — | 58 |
| qdcg.line15 | — | — | — | 3 | — | 12 |
| qdcg.line16 | — | — | — | 3 | — | 12 |
| qdcg.line17 | — | — | — | 3 | — | 12 |
| qdcg.line18 | — | — | — | 3 | — | 12 |
| qdcg.line19 | — | — | — | 3 | — | 12 |
| qdcg.line20 | — | — | — | 3 | — | 12 |
| qdcg.line21 | — | — | — | 3 | — | 12 |
| qdcg.line22 | — | — | — | — | — | 13 |
| qdcg.line23 | — | — | — | 3 | — | 13 |
| qdcg.line24 | 1 (example.official) | — | — | — | — | 59 |
| qdcg.line25 | — | — | — | 3 | — | 13 |

## State and Local Income Tax Refund Worksheet—Schedule 1, Line 1

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| refund.zero | — | — | — | — | — | — |
| refund.received | — | — | — | — | — | — |
| refund.has | — | — | — | — | — | — |
| refund.box8 | — | — | — | — | — | — |
| refund.not_2024 | — | — | — | — | — | — |
| refund.itemized | — | — | — | — | — | — |
| refund.sales | — | — | — | — | — | — |
| refund.worksheet | — | — | — | — | — | — |
| refund.exc_tax | — | — | — | — | — | — |
| refund.exc_who | — | — | — | — | — | — |
| refund.line5d_2024 | — | — | — | — | — | — |
| refund.line5e_2024 | — | — | — | — | — | — |
| refund.line5e_bad | — | — | — | — | — | — |
| refund.line1 | — | — | — | 1 (classm.refund.1) | — | 12 |
| refund.line2_more | — | — | — | — | — | 2 (stage16.mut.refund_single_unasked, stage16.mut.refund_line3_stop) |
| refund.line2 | — | — | — | 1 (classm.refund.1) | — | 5 |
| refund.line3_more | — | — | — | — | — | 1 (stage16.mut.refund_line3_stop) |
| refund.line3 | — | — | — | 1 (classm.refund.1) | — | 9 |
| refund.line17_2024 | — | — | — | — | — | — |
| refund.line4 | — | — | — | 1 (classm.refund.1) | — | 8 |
| refund.status | — | — | — | — | — | — |
| refund.mfs_spouse_itemized | — | — | — | — | — | — |
| refund.std_single | — | — | — | — | — | — |
| refund.std_joint | — | — | — | — | — | — |
| refund.std_hoh | — | — | — | — | — | — |
| refund.line5 | — | — | — | 1 (classm.refund.1) | — | 8 |
| refund.box_married | — | — | — | — | — | — |
| refund.box_unmarried | — | — | — | — | — | — |
| refund.per_box | — | — | — | — | — | — |
| refund.you_born | — | — | — | — | — | — |
| refund.you_blind | — | — | — | — | — | — |
| refund.spouse_born | — | — | — | — | — | — |
| refund.spouse_blind | — | — | — | — | — | — |
| refund.spouse_boxes | — | — | — | — | — | — |
| refund.amt_you_born | — | — | — | — | — | — |
| refund.amt_you_blind | — | — | — | — | — | — |
| refund.amt_spouse_born | — | — | — | — | — | — |
| refund.amt_spouse_born_checked | — | — | — | — | — | — |
| refund.amt_spouse_blind | — | — | — | — | — | — |
| refund.amt_spouse_blind_checked | — | — | — | — | — | — |
| refund.line6 | — | — | — | 1 (classm.refund.1) | — | 8 |
| refund.line7 | — | — | — | 1 (classm.refund.1) | — | 8 |
| refund.line8_figured | — | — | — | — | — | — |
| refund.line8 | — | — | — | 1 (classm.refund.1) | — | 7 |
| refund.line8_mfs | — | — | — | — | — | — |
| refund.line9_figured | — | — | — | — | — | — |
| refund.line9 | — | — | — | 1 (classm.refund.1) | — | 8 |
| refund.taxable | — | — | — | — | — | 4 |

Unasserted lines: refund.zero, refund.has, refund.worksheet, refund.line5e_bad, refund.std_single, refund.std_joint, refund.std_hoh, refund.box_married, refund.box_unmarried, refund.per_box, refund.spouse_boxes, refund.amt_you_born, refund.amt_you_blind, refund.amt_spouse_born, refund.amt_spouse_born_checked, refund.amt_spouse_blind, refund.amt_spouse_blind_checked, refund.line8_figured, refund.line8_mfs, refund.line9_figured

## Form 1099-R distributions (IRAs, pensions and annuities)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| retirement.account | — | — | — | — | — | — |
| retirement.code | — | — | — | — | — | — |
| retirement.box1 | — | — | — | — | — | — |
| retirement.box5 | — | — | — | — | — | — |
| retirement.rollover | — | — | — | — | — | — |
| retirement.special | — | — | — | — | — | — |
| retirement.annuity | — | — | — | — | — | — |
| retirement.cost | — | — | — | — | — | — |
| retirement.used_last_year | — | — | — | — | — | — |
| retirement.last_line4 | — | — | — | — | — | — |
| retirement.joint_life | — | — | — | — | — | — |
| retirement.age | — | — | — | — | — | — |
| retirement.combined_age | — | — | — | — | — | — |
| retirement.months | — | — | — | — | — | — |
| retirement.recovered | — | — | — | — | — | — |
| retirement.zero | — | — | — | — | — | — |
| retirement.one | — | — | — | — | — | — |
| retirement.is_ira | — | — | — | 4 | — | — |
| retirement.roth | — | — | — | 4 | — | — |
| retirement.direct | — | — | — | 4 | — | — |
| retirement.bad_code | — | — | — | 4 | — | — |
| retirement.rolled | — | — | — | 4 | — | — |
| retirement.has_rollover | — | — | — | 4 | — | — |
| retirement.smw1 | — | — | — | 4 | — | — |
| retirement.smw2 | — | — | — | 4 | — | — |
| retirement.smw4_t1_360 | — | — | — | 4 | — | — |
| retirement.smw4_t1_310 | — | — | — | 4 | — | — |
| retirement.smw4_t1_260 | — | — | — | 4 | — | — |
| retirement.smw4_t1_210 | — | — | — | 4 | — | — |
| retirement.smw4_t1_160 | — | — | — | 4 | — | — |
| retirement.smw4_t2_410 | — | — | — | 4 | — | — |
| retirement.smw4_t2_360 | — | — | — | 4 | — | — |
| retirement.smw4_t2_310 | — | — | — | 4 | — | — |
| retirement.smw4_t2_260 | — | — | — | 4 | — | — |
| retirement.smw4_t2_210 | — | — | — | 4 | — | — |
| retirement.smw4_table1 | — | — | — | 4 | — | — |
| retirement.smw4_table2 | — | — | — | 4 | — | — |
| retirement.smw4_new | — | — | — | 4 | — | — |
| retirement.smw4 | — | — | — | 4 | — | 4 |
| retirement.smw5 | — | — | — | 4 | — | 3 |
| retirement.smw6 | — | — | — | 4 | — | — |
| retirement.smw7 | — | — | — | 4 | — | — |
| retirement.smw8 | — | — | — | 4 | — | 1 (stage10.smw.cost_nearly_recovered) |
| retirement.smw9 | — | — | — | 4 | — | — |
| retirement.smw10 | — | — | — | 4 | — | 4 |
| retirement.smw11 | — | — | — | 4 | — | 4 |
| retirement.cost_left | — | — | — | 4 | — | — |
| retirement.annuity_with_cost | — | — | — | 4 | — | — |
| retirement.annuity_rollover | — | — | — | 4 | — | — |
| retirement.annuity_taxable | — | — | — | 4 | — | — |
| retirement.ira_taxable | — | — | — | 4 | — | — |
| retirement.ira_not_rolled | — | — | — | 4 | — | — |
| retirement.plan_excluded | — | — | — | 4 | — | — |
| retirement.plan_simple | — | — | — | 4 | — | — |
| retirement.plan_taxable | — | — | — | 4 | — | — |
| retirement.taxable | — | — | — | 4 | — | — |
| retirement.show_a | — | — | — | 4 | — | — |
| retirement.amount_a | — | — | — | 4 | — | 1 (stage16.cleanup.refuse.retirement.special_first) |
| retirement.sav_military | — | — | — | — | — | — |
| retirement.sav_404k | — | — | — | — | — | — |
| retirement.sav_inherited | — | — | — | — | — | — |
| retirement.sav_excluded | — | — | — | 4 | — | — |
| retirement.sav_gross | — | — | — | 4 | — | — |
| retirement.sav_amount | — | — | — | 4 | — | — |

Unasserted lines: retirement.zero, retirement.one

## Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s1.zero | — | — | — | — | — | — |
| s1.line1 | — | — | — | 3 | — | 17 |
| s1.uc_paid | — | — | — | — | — | — |
| s1.has_uc | — | — | — | — | — | — |
| s1.uc_repaid | — | — | — | — | — | — |
| s1.uc_unsupported | — | — | — | — | — | — |
| s1.line7_figured | — | — | — | — | — | — |
| s1.line7 | — | — | — | 3 | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_box | — | — | — | 3 | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_repaid | — | — | — | 3 | — | 1 (stage11.uc.repaid) |
| s1.ebl_loss | — | — | — | — | — | — |
| s1.ebl_total | — | — | — | — | — | — |
| s1.zero_ebl | — | — | — | — | — | — |
| s1.ebl_threshold | — | — | — | — | — | — |
| s1.ebl | — | — | — | — | — | — |
| s1.sc_count | — | — | — | — | — | — |
| s1.has_sc | — | — | — | — | — | — |
| s1.sc_1a_count | — | — | — | — | — | — |
| s1.sc_1a | — | — | — | — | — | — |
| s1.line3 | — | — | — | 3 | — | 12 |
| s1.line8_other | — | — | — | — | — | — |
| s1.gambling_winnings | — | — | — | — | — | — |
| s1.has_gambling | — | — | — | — | — | — |
| s1.gambling_pro | — | — | — | — | — | — |
| s1.gambling_business | — | — | — | — | — | — |
| s1.line8b | — | — | — | 3 | — | 6 |
| s1.line8g | — | — | — | — | — | 1 (stage16.other.o4) |
| s1.line8h | — | — | — | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line8i | — | — | — | — | — | 1 (stage16.other.o6) |
| s1.line8j | — | — | — | — | — | 1 (stage16.other.o7) |
| s1.line8r | — | — | — | — | — | 1 (stage16.other.o8) |
| s1.line8z | — | — | — | 3 | — | 4 |
| s1.alimony | — | — | — | — | — | — |
| s1.alimony_received | — | — | — | — | — | — |
| s1.alimony_paid | — | — | — | — | — | — |
| s1.alimony_unsupported | — | — | — | — | — | — |
| s1.alimony_refused | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_received) |
| s1.line2a | — | — | — | 3 | — | 4 |
| s1.line2b_notice | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.cod_any | — | — | — | — | — | — |
| s1.cod_amount | — | — | — | — | — | — |
| s1.has_cod | — | — | — | — | — | — |
| s1.cod_unsupported | — | — | — | — | — | — |
| s1.cod_refused | — | — | — | — | — | 1 (stage16.refuse.s1.cod_unsupported) |
| s1.cod_figured | — | — | — | — | — | — |
| s1.line8c | — | — | — | 3 | — | 5 |
| s1.line8f | — | — | — | 3 | — | 8 |
| s1.line9 | — | — | — | 3 | — | 24 |
| s1.line10 | — | — | — | 3 | — | 44 |
| s1.line11 | — | — | — | 3 | — | 5 |
| s1.line13 | — | — | — | 3 | — | 18 |
| s1.line15 | — | — | — | 3 | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 9 |
| s1.line16 | — | — | — | 3 | — | 9 |
| s1.line17 | — | — | — | 3 | — | 3 |
| s1.line18 | — | — | — | 3 | — | 2 (stage16.small.s1, stage16.small.s10) |
| s1.paid_refused | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_paid) |
| s1.line19a | — | — | — | 3 | — | 4 |
| s1.line19b_notice | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line19c_notice | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line20 | — | — | — | 3 | — | 28 |
| s1.line21 | — | — | — | 3 | — | 2 (stage11.sli.basic, stage11.refuse.sli_pub970) |
| s1.jury_to_employer | — | — | — | — | — | — |
| s1.jury_over | — | — | — | — | — | — |
| s1.line24a | — | — | — | 3 | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line25 | — | — | — | 3 | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line26 | — | — | — | 3 | E via f1040.line10 (PE, TC) | 19 |

Unasserted lines: s1.zero, s1.has_uc, s1.line7_figured, s1.ebl_loss, s1.ebl_total, s1.zero_ebl, s1.ebl_threshold, s1.ebl, s1.sc_count, s1.has_sc, s1.sc_1a_count, s1.sc_1a, s1.has_gambling, s1.gambling_business, s1.has_cod, s1.cod_figured, s1.jury_over

## Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s179.line2 | — | — | — | 3 | — | 2 (stage14.asset.partial_use, stage14.asset.low_use_nonlisted) |
| s179.max | — | — | — | — | — | — |
| s179.line1 | — | — | — | — | — | 2 (stage14.s179.carryover_no_property, stage14.s179.dollar_limit) |
| s179.line3 | — | — | — | 3 | — | — |
| s179.line4 | — | — | — | 3 | — | 3 |
| s179.line5_full | — | — | — | — | — | — |
| s179.separate | — | — | — | — | — | — |
| s179.line5_mfs | — | — | — | — | — | — |
| s179.line5 | — | — | — | — | — | 7 |
| s179.mfs | — | — | — | — | — | 1 (stage14.s179.mfs_no_election) |
| s179.line6 | — | — | — | 3 | — | — |
| s179.line7 | — | — | — | 3 | — | — |
| s179.line8 | — | — | — | 3 | — | — |
| s179.line9 | — | — | — | 3 | — | 1 (stage14.s179.carryover_no_room) |
| s179.line10 | — | — | — | — | — | — |
| s179.income_sc | — | — | — | — | — | — |
| s179.income | — | — | — | — | — | — |
| s179.income0 | — | — | — | — | — | — |
| s179.line11 | — | — | — | 3 | — | 5 |
| s179.line9_10 | — | — | — | — | — | — |
| s179.line12 | — | — | — | 3 | — | 11 |
| s179.sc_count | — | — | — | — | — | — |
| s179.orphan | — | — | — | — | — | — |
| s179.line13 | — | — | — | 3 | — | 8 |
| s179.differs | — | — | — | — | — | — |
| s179.multi | — | — | — | — | — | — |

Unasserted lines: s179.max, s179.line5_full, s179.separate, s179.line5_mfs, s179.income_sc, s179.income, s179.income0, s179.line9_10, s179.sc_count, s179.orphan, s179.differs, s179.multi

## Schedule 1-A (Form 1040) — Additional Deductions

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s1a.zero | — | — | — | — | — | — |
| s1a.line1 | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line2a | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line2b | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line2c | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line2d | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line2e | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line3 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.tips.one_employer) |
| s1a.tips | — | — | — | — | — | — |
| s1a.tip_employers | — | — | — | — | — | — |
| s1a.tip_total | — | — | — | — | — | — |
| s1a.tip_reported | — | — | — | — | — | — |
| s1a.tip_multi | — | — | — | — | — | — |
| s1a.tip_ssn_count | — | — | — | — | — | — |
| s1a.tip_ssn | — | — | — | — | — | — |
| s1a.part2 | — | — | — | — | — | — |
| s1a.line4a_calc | — | — | — | — | — | — |
| s1a.line4a | — | — | — | 1 (classm.s1a.1) | — | 5 |
| s1a.line4b_calc | — | — | — | — | — | — |
| s1a.line4b | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.tips.one_employer) |
| s1a.line4c_one | — | — | — | — | — | — |
| s1a.line4c_calc | — | — | — | — | — | — |
| s1a.line4c | — | — | — | 1 (classm.s1a.1) | — | 7 |
| s1a.line5_calc | — | — | — | — | — | 2 (stage14.refuse.sch1a_tips, stage14.sch1a.tips_with_sc) |
| s1a.line5 | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line6_calc | — | — | — | — | — | — |
| s1a.line6 | — | — | — | 1 (classm.s1a.1) | — | 2 (stage12.tips.cap, stage12.refuse.tips_trade_or_business) |
| s1a.line7_calc | — | — | — | — | — | — |
| s1a.line7 | — | — | — | 1 (classm.s1a.1) | — | 4 |
| s1a.tips_max | — | — | — | — | — | — |
| s1a.base_other | — | — | — | — | — | — |
| s1a.base_joint | — | — | — | — | — | — |
| s1a.line8_calc | — | — | — | — | — | — |
| s1a.line8 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage13.tips_only_spouse_no_ssn) |
| s1a.line9_calc | — | — | — | — | — | — |
| s1a.line9 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.mfj.tips_overtime) |
| s1a.line10_calc | — | — | — | — | — | — |
| s1a.line10 | — | — | — | 1 (classm.s1a.1) | — | 3 |
| s1a.line10_over | — | — | — | — | — | — |
| s1a.line10_pos | — | — | — | — | — | — |
| s1a.line11_thousands | — | — | — | — | — | — |
| s1a.line12_calc | — | — | — | — | — | — |
| s1a.line12 | — | — | — | 1 (classm.s1a.1) | — | 5 |
| s1a.line13_figured | — | — | — | — | — | — |
| s1a.line13_amount | — | — | — | — | — | — |
| s1a.line13_ssn | — | — | — | — | — | — |
| s1a.line13_claim | — | — | — | — | — | — |
| s1a.line13 | — | — | — | 1 (classm.s1a.1) | — | 19 |
| s1a.overtime | — | — | — | — | — | — |
| s1a.ot_ssn_count | — | — | — | — | — | — |
| s1a.ot_ssn | — | — | — | — | — | — |
| s1a.part3 | — | — | — | — | — | — |
| s1a.line14a_calc | — | — | — | — | — | — |
| s1a.line14a | — | — | — | 1 (classm.s1a.1) | — | 11 |
| s1a.line14b_calc | — | — | — | — | — | 1 (stage14.sch1a.refuse_overtime_1099) |
| s1a.line14b | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line14c_calc | — | — | — | — | — | — |
| s1a.line14c | — | — | — | 1 (classm.s1a.1) | — | 2 (stage12.ot.premium, stage12.refuse.overtime_nonemployee) |
| s1a.ot_max_other | — | — | — | — | — | — |
| s1a.ot_max_joint | — | — | — | — | — | — |
| s1a.ot_max | — | — | — | — | — | — |
| s1a.line15_calc | — | — | — | — | — | — |
| s1a.line15 | — | — | — | 1 (classm.s1a.1) | — | 4 |
| s1a.line16_calc | — | — | — | — | — | — |
| s1a.line16 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage13.overtime_only_spouse_no_ssn) |
| s1a.line17_calc | — | — | — | — | — | — |
| s1a.line17 | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line18_calc | — | — | — | — | — | — |
| s1a.line18 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.ot.phaseout) |
| s1a.line18_over | — | — | — | — | — | — |
| s1a.line18_pos | — | — | — | — | — | — |
| s1a.line19_thousands | — | — | — | — | — | — |
| s1a.line20_calc | — | — | — | — | — | — |
| s1a.line20 | — | — | — | 1 (classm.s1a.1) | — | 2 (stage12.ot.phaseout, stage12.mfj.tips_overtime) |
| s1a.line21_figured | — | — | — | — | — | — |
| s1a.line21_amount | — | — | — | — | — | — |
| s1a.line21_ssn | — | — | — | — | — | — |
| s1a.line21_claim | — | — | — | — | — | — |
| s1a.line21 | — | — | — | 1 (classm.s1a.1) | — | 17 |
| s1a.carloan | — | — | — | — | — | — |
| s1a.line23_total | — | — | — | — | — | — |
| s1a.line23 | — | — | — | 1 (classm.s1a.1) | — | 6 |
| s1a.car_max | — | — | — | — | — | — |
| s1a.part4 | — | — | — | — | — | — |
| s1a.line24_calc | — | — | — | — | — | — |
| s1a.line24 | — | — | — | 1 (classm.s1a.1) | — | 3 |
| s1a.car_base_other | — | — | — | — | — | — |
| s1a.car_base_joint | — | — | — | — | — | — |
| s1a.line25_calc | — | — | — | — | — | — |
| s1a.line25 | — | — | — | 1 (classm.s1a.1) | — | — |
| s1a.line26_calc | — | — | — | — | — | — |
| s1a.line26 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.mfj.car) |
| s1a.line27_calc | — | — | — | — | — | — |
| s1a.line27 | — | — | — | 1 (classm.s1a.1) | — | 2 (stage12.car.phaseout, stage12.car.phaseout_round_up) |
| s1a.line27_over | — | — | — | — | — | — |
| s1a.line27_pos | — | — | — | — | — | — |
| s1a.line28_thousands | — | — | — | — | — | — |
| s1a.line29_calc | — | — | — | — | — | — |
| s1a.line29 | — | — | — | 1 (classm.s1a.1) | — | 4 |
| s1a.line30_figured | — | — | — | — | — | — |
| s1a.line30_amount | — | — | — | — | — | — |
| s1a.line30 | — | — | — | 1 (classm.s1a.1) | — | 15 |
| s1a.senior_count | — | — | — | — | — | — |
| s1a.senior_any | — | — | — | — | — | — |
| s1a.part5 | — | — | — | — | — | — |
| s1a.line31_calc | — | — | — | — | — | — |
| s1a.line31 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage13.seniors_none) |
| s1a.senior_base_other | — | — | — | — | — | — |
| s1a.senior_base_joint | — | — | — | — | — | — |
| s1a.line32_calc | — | — | — | — | — | — |
| s1a.line32 | — | — | — | 1 (classm.s1a.1) | — | 1 (stage12.mfj.senior) |
| s1a.line33_calc | — | — | — | — | — | — |
| s1a.line33 | — | — | — | 1 (classm.s1a.1) | — | 3 |
| s1a.line33_over | — | — | — | — | — | — |
| s1a.line33_pos | — | — | — | — | — | — |
| s1a.line34_calc | — | — | — | — | — | — |
| s1a.line34 | — | — | — | 1 (classm.s1a.1) | — | 4 |
| s1a.senior_amount | — | — | — | — | — | — |
| s1a.line35_figured | — | — | — | — | — | — |
| s1a.line35_calc | — | — | — | — | — | — |
| s1a.line35 | — | — | — | 1 (classm.s1a.1) | — | 8 |
| s1a.died_before_65_count | — | — | — | — | — | — |
| s1a.died_before_65 | — | — | — | — | — | — |
| s1a.senior_decedent | — | — | — | — | — | — |
| s1a.line36a_senior | — | — | — | — | — | — |
| s1a.line36a_claim | — | — | — | — | — | — |
| s1a.line36a | — | — | — | 1 (classm.s1a.1) | — | 11 |
| s1a.spouse_senior_count | — | — | — | — | — | — |
| s1a.spouse_senior | — | — | — | — | — | — |
| s1a.spouse_died_before_65_count | — | — | — | — | — | — |
| s1a.spouse_died_before_65 | — | — | — | — | — | — |
| s1a.spouse_senior_decedent | — | — | — | — | — | — |
| s1a.line36b_senior | — | — | — | — | — | — |
| s1a.line36b | — | — | — | 1 (classm.s1a.1) | — | 8 |
| s1a.line37 | — | — | — | 1 (classm.s1a.1) | — | 16 |
| s1a.line38 | — | — | — | 1 (classm.s1a.1) | E via f1040.line13b (PE, TC) | 7 |

Unasserted lines: s1a.zero, s1a.tip_employers, s1a.tip_total, s1a.tip_reported, s1a.tip_multi, s1a.tip_ssn_count, s1a.tip_ssn, s1a.part2, s1a.line4a_calc, s1a.line4b_calc, s1a.line4c_one, s1a.line4c_calc, s1a.line6_calc, s1a.line7_calc, s1a.tips_max, s1a.base_other, s1a.base_joint, s1a.line8_calc, s1a.line9_calc, s1a.line10_calc, s1a.line10_over, s1a.line10_pos, s1a.line11_thousands, s1a.line12_calc, s1a.line13_figured, s1a.line13_amount, s1a.line13_ssn, s1a.line13_claim, s1a.ot_ssn_count, s1a.ot_ssn, s1a.part3, s1a.line14a_calc, s1a.line14c_calc, s1a.ot_max_other, s1a.ot_max_joint, s1a.ot_max, s1a.line15_calc, s1a.line16_calc, s1a.line17_calc, s1a.line18_calc, s1a.line18_over, s1a.line18_pos, s1a.line19_thousands, s1a.line20_calc, s1a.line21_figured, s1a.line21_amount, s1a.line21_ssn, s1a.line21_claim, s1a.line23_total, s1a.car_max, s1a.part4, s1a.line24_calc, s1a.car_base_other, s1a.car_base_joint, s1a.line25_calc, s1a.line26_calc, s1a.line27_calc, s1a.line27_over, s1a.line27_pos, s1a.line28_thousands, s1a.line29_calc, s1a.line30_figured, s1a.line30_amount, s1a.senior_count, s1a.senior_any, s1a.part5, s1a.line31_calc, s1a.senior_base_other, s1a.senior_base_joint, s1a.line32_calc, s1a.line33_calc, s1a.line33_over, s1a.line33_pos, s1a.line34_calc, s1a.senior_amount, s1a.line35_figured, s1a.line35_calc, s1a.died_before_65_count, s1a.died_before_65, s1a.senior_decedent, s1a.line36a_senior, s1a.line36a_claim, s1a.spouse_senior_count, s1a.spouse_senior, s1a.spouse_died_before_65_count, s1a.spouse_died_before_65, s1a.spouse_senior_decedent, s1a.line36b_senior

## Schedule 2 — Additional Taxes (the lines this tool computes)

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s2.amt | — | — | — | — | — | — |
| s2.other | — | — | — | — | — | — |
| s2.zero | — | — | — | — | — | — |
| s2.line2 | — | — | — | 1 (classm.s2.1) | — | 3 |
| s2.line3 | — | — | — | 1 (classm.s2.1) | — | 3 |
| s2.line4 | — | — | — | 1 (classm.s2.1) | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 3 |
| s2.line11 | — | — | — | 1 (classm.s2.1) | — | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| s2.line12 | — | — | — | 1 (classm.s2.1) | — | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| s2.line17c | — | — | — | 1 (classm.s2.1) | — | 6 |
| s2.line18 | — | — | — | 1 (classm.s2.1) | — | 5 |
| s2.line21 | — | — | — | 1 (classm.s2.1) | — | 11 |

Unasserted lines: s2.zero

## Schedule 3 — selected lines

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | — |
| s3.line2 | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 31 |
| s3.zero | — | — | — | — | — | — |
| s3.line4 | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 33 |
| s3.line5a | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 28 |
| s3.line5b | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 28 |
| s3.line8 | — | — | — | 2 (classm.s3.1, classm.s3.2) | E via f1040.line20 (TC) | 4 |
| s3.mfs | — | — | — | — | — | — |
| s3.line9 | — | — | — | — | — | — |
| s3.line10 | — | — | — | — | — | — |
| s3.line11 | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 24 |
| s3.line12 | — | — | — | — | — | — |
| s3.line14 | — | — | — | — | — | — |
| s3.line15 | — | — | — | 2 (classm.s3.1, classm.s3.2) | — | 21 |

Unasserted lines: s3.zero, s3.mfs

## Schedule 8812 — Credits for Qualifying Children and Other Dependents

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| s8812.line1 | — | — | — | 4 | — | 28 |
| s8812.zero | — | — | — | — | — | — |
| s8812.line2a | — | — | — | 4 | — | 24 |
| s8812.line2b | — | — | — | 4 | — | 24 |
| s8812.line2c | — | — | — | 4 | — | 24 |
| s8812.line2d | — | — | — | 4 | — | 24 |
| s8812.line3 | — | — | — | 4 | — | 28 |
| s8812.line4 | — | — | — | 4 | — | 29 |
| s8812.line5 | — | — | — | 4 | — | 31 |
| s8812.line6 | — | — | — | 4 | — | 25 |
| s8812.line7 | — | — | — | 4 | — | 27 |
| s8812.line8 | — | — | — | 4 | — | 31 |
| s8812.line9 | — | — | — | 4 | — | 2 (stage15.f5695-3.g2, stage16.other.o10) |
| s8812.excess | — | — | — | — | — | 24 |
| s8812.line10 | — | — | — | 4 | — | 28 |
| s8812.line11 | — | — | — | 4 | — | 28 |
| s8812.line12 | — | — | — | 4 | — | 29 |
| s8812.clw_a1 | — | — | — | — | — | 30 |
| s8812.clw_a2 | — | — | — | — | — | 30 |
| s8812.clw_a3 | — | — | — | — | — | 30 |
| s8812.clw_a4 | — | — | — | — | — | 30 |
| s8812.clw_a5 | — | — | — | — | — | 30 |
| s8812.line13 | — | — | — | 2 (classm.s8812.1, classm.s8812.3) | — | 31 |
| s8812.line14 | — | — | — | 4 | E via f1040.line19 (PE, TC) | 50 |
| s8812.line16a | — | — | — | 4 | — | 28 |
| s8812.line16b | — | — | — | 4 | — | 28 |
| s8812.line17 | — | — | — | 4 | — | 28 |
| s8812.combat_pay | — | — | — | — | — | — |
| s8812.puerto_rico | — | — | — | — | — | — |
| s8812.eiw_1a | — | — | — | — | — | 24 |
| s8812.eiw_1b | — | — | — | — | — | 24 |
| s8812.eiw_2b | — | — | — | — | — | — |
| s8812.eiw_3sum | — | — | — | — | — | 2 (stage14.s8812.eiw_stop_with_se_tax, stage14.s8812.eiw_zero_with_se_tax) |
| s8812.eiw_3 | — | — | — | — | — | 24 |
| s8812.eiw_4 | — | — | — | — | — | 24 |
| s8812.eiw_5 | — | — | — | — | — | 24 |
| s8812.eiw_6 | — | — | — | — | — | 24 |
| s8812.eiw_7_figured | — | — | — | — | — | — |
| s8812.eiw_3_positive | — | — | — | — | — | — |
| s8812.eiw_7 | — | — | — | — | — | 26 |
| s8812.taking_eic | — | — | — | — | — | 4 |
| s8812.chart_eic | — | — | — | — | — | — |
| s8812.line18a | — | — | — | 2 (classm.s8812.1, classm.s8812.3) | — | 32 |
| s8812.line18b | — | — | — | 4 | — | 24 |
| s8812.line19 | — | — | — | 2 (classm.s8812.1, classm.s8812.3) | — | 31 |
| s8812.line20 | — | — | — | 2 (classm.s8812.1, classm.s8812.3) | — | 29 |
| s8812.ss_withheld | — | — | — | — | — | 24 |
| s8812.amt_ws4 | — | — | — | — | — | 24 |
| s8812.amt_ws6 | — | — | — | — | — | — |
| s8812.amt_ws7 | — | — | — | — | — | 1 (stage14.f8959.se_above_threshold) |
| s8812.line21 | — | — | — | 1 (classm.s8812.3) | — | 26 |
| s8812.line22 | — | — | — | 4 | — | 26 |
| s8812.line23 | — | — | — | 1 (classm.s8812.3) | — | 26 |
| s8812.line24 | — | — | — | 2 (classm.s8812.1, classm.s8812.3) | — | 25 |
| s8812.line25 | — | — | — | 2 (classm.s8812.2, classm.s8812.3) | — | 26 |
| s8812.line26 | — | — | — | 1 (classm.s8812.3) | — | 25 |
| s8812.few_children | — | — | — | — | — | 24 |
| s8812.earned_covers | — | — | — | — | — | 24 |
| s8812.from_part_iia | — | — | — | — | — | 24 |
| s8812.from_part_iib | — | — | — | — | — | 25 |
| s8812.part_iib_result | — | — | — | — | — | 24 |
| s8812.line27 | — | — | — | 4 | E via f1040.line28 (PE) | 51 |
| s8812.clwb_complete | — | — | — | — | — | — |
| s8812.clwb_1 | — | — | — | — | — | 6 |
| s8812.clwb_2 | — | — | — | — | — | 6 |
| s8812.clwb_3 | — | — | — | — | — | 6 |
| s8812.clwb_4 | — | — | — | — | — | 6 |
| s8812.clwb_5 | — | — | — | — | — | 6 |
| s8812.clwb_three | — | — | — | — | — | — |
| s8812.clwb_5_covers | — | — | — | — | — | — |
| s8812.clwb_7 | — | — | — | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_8 | — | — | — | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_9 | — | — | — | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_10 | — | — | — | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_11_figured | — | — | — | — | — | — |
| s8812.clwb_11_three | — | — | — | — | — | — |
| s8812.clwb_11 | — | — | — | — | — | 7 |
| s8812.clwb_12 | — | — | — | — | — | 6 |
| s8812.clwb_13 | — | — | — | — | — | 6 |
| s8812.clwb_14 | — | — | — | — | — | 6 |
| s8812.clwb_15 | — | — | — | — | — | 6 |

Unasserted lines: s8812.zero, s8812.eiw_2b, s8812.eiw_7_figured, s8812.eiw_3_positive, s8812.chart_eic, s8812.amt_ws6, s8812.clwb_complete, s8812.clwb_three, s8812.clwb_5_covers, s8812.clwb_11_figured, s8812.clwb_11_three

## Schedule A — supported itemized deductions and standard comparison

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sa.unsupported | — | — | — | — | — | — |
| sa.charity_limited | — | — | — | — | — | — |
| sa.excluded_income | — | — | — | — | — | — |
| sa.dependent | — | — | — | — | — | — |
| sa.spouse_extra | — | — | — | — | — | — |
| sa.mfs_spouse_extra | — | — | — | — | — | — |
| sa.age65_count | — | — | — | — | — | — |
| sa.age65 | — | — | — | — | — | — |
| sa.spouse_itemizes | — | — | — | — | — | — |
| sa.elect_itemize | — | — | — | — | — | — |
| sa.agi | — | — | — | — | — | — |
| sa.line1 | — | — | — | — | — | — |
| sa.line5a | — | — | — | — | — | 1 (stage16.other.o1) |
| sa.line5b | — | — | — | — | — | — |
| sa.line5c | — | — | — | — | — | — |
| sa.line8a | — | — | — | — | — | 1 (stage16.other.o1) |
| sa.line11 | — | — | — | — | — | — |
| sa.zero | — | — | — | — | — | — |
| sa.line2 | — | — | — | 7 | — | — |
| sa.line3 | — | — | — | 7 | — | 1 (stage4.medical.below) |
| sa.line4 | — | — | — | 7 | — | 3 |
| sa.line5d | — | — | — | 7 | — | 3 |
| sa.saltbase | — | — | — | — | — | — |
| sa.saltfloor | — | — | — | — | — | — |
| sa.saltthreshold | — | — | — | — | — | — |
| sa.saltexcess | — | — | — | — | — | — |
| sa.saltreduction | — | — | — | — | — | — |
| sa.saltremaining | — | — | — | — | — | — |
| sa.saltfloor_applied | — | — | — | — | — | — |
| sa.salthalf | — | — | — | — | — | 1 (stage4.salt.mfs_floor) |
| sa.mfs | — | — | — | — | — | — |
| sa.saltlimit | — | — | — | — | — | — |
| sa.line5e | — | — | — | 7 | — | 12 |
| sa.line6 | — | — | — | 7 | — | 5 |
| sa.line8b | — | — | — | 7 | — | 4 |
| sa.line8c | — | — | — | 7 | — | 4 |
| sa.line13 | — | — | — | 7 | — | 4 |
| sa.line15 | — | — | — | 7 | — | 4 |
| sa.gambling_losses | — | — | — | — | — | — |
| sa.line16_gambling | — | — | — | — | — | — |
| sa.line16 | — | — | — | 7 | — | 5 |
| sa.line7 | — | — | — | 7 | — | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line8e | — | — | — | 7 | — | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line9 | — | — | — | 7 | — | 1 (stage4.deductions.combined) |
| sa.line10 | — | — | — | 7 | — | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 7 | — | 9 |
| sa.form8283 | — | — | — | — | — | 3 |
| sa.line14 | — | — | — | 7 | — | 1 (stage4.deductions.combined) |
| sa.line17 | — | — | — | 7 | PE: 1571 compared (706 nonzero), 129 excluded; TC: 1269 compared (569 nonzero), 431 excluded | 8 |
| sa.standardbase | — | — | — | — | — | — |
| sa.extra | — | — | — | — | — | — |
| sa.boxes_age65 | — | — | — | — | — | 1 (stage16.sa.decedent_spouse) |
| sa.extra_age65 | — | — | — | — | — | — |
| sa.boxes_blind | — | — | — | — | — | — |
| sa.extra_blind | — | — | — | — | — | — |
| sa.standardraw | — | — | — | — | — | — |
| sa.standard | — | — | — | — | PE: 1680 compared (1680 nonzero), 20 excluded | 12 |
| sa.itemizes | — | — | — | — | — | 6 |
| sa.deduction | — | — | — | — | PE: 1571 compared (1571 nonzero), 129 excluded; TC: 973 compared (973 nonzero), 727 excluded | 7 |
| sa.mfs_spouse_itemizes | — | — | — | — | — | — |

Unasserted lines: sa.mfs_spouse_extra, sa.age65_count, sa.age65, sa.agi, sa.zero, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.line16_gambling, sa.standardbase, sa.extra, sa.extra_age65, sa.boxes_blind, sa.extra_blind, sa.standardraw, sa.mfs_spouse_itemizes

## Form 8949 and Schedule D — manually classified securities transactions

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sales.box | — | — | — | — | — | — |
| sales.route | — | — | — | — | — | — |
| sales.code | — | — | — | — | — | — |
| sales.special | — | — | — | — | — | — |
| sales.aggregate_eligible | — | — | — | — | — | — |
| sales.proceeds | — | — | — | — | — | — |
| sales.reported_basis | — | — | — | — | — | — |
| sales.correct_basis | — | — | — | — | — | — |
| sales.wash_loss | — | — | — | — | — | — |
| sales.covered | — | — | — | 1 (classm.sales.1) | — | — |
| sales.digital | — | — | — | 1 (classm.sales.1) | — | — |
| sales.has_b | — | — | — | 1 (classm.sales.1) | — | — |
| sales.has_w | — | — | — | 1 (classm.sales.1) | — | — |
| sales.bad_code | — | — | — | 1 (classm.sales.1) | — | — |
| sales.bad_aggregate | — | — | — | 1 (classm.sales.1) | — | — |
| sales.one | — | — | — | — | — | — |
| sales.zero | — | — | — | — | — | — |
| sales.e | — | — | — | 1 (classm.sales.1) | — | — |
| sales.b_difference | — | — | — | 1 (classm.sales.1) | — | — |
| sales.adjust_b | — | — | — | 1 (classm.sales.1) | — | — |
| sales.b | — | — | — | 1 (classm.sales.1) | — | — |
| sales.w | — | — | — | 1 (classm.sales.1) | — | — |
| sales.g | 4 | — | — | 1 (classm.sales.1) | — | 12 |
| sales.before_adjustment | — | — | — | 1 (classm.sales.1) | — | — |
| sales.h | 4 | — | — | 1 (classm.sales.1) | — | 12 |

Unasserted lines: sales.one, sales.zero

## Schedule B — supported interest and ordinary dividends

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sb.unsupported | — | — | — | — | — | — |
| sb.ordinary_dividends | — | — | — | — | — | — |
| sb.line7a | — | — | — | — | — | — |
| sb.fbar_required | — | — | — | — | — | — |
| sb.form8938 | — | — | — | — | — | — |
| sb.line8 | — | — | — | — | — | — |
| sb.zero | — | — | — | — | — | — |
| sb.line2 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | 6 |
| sb.line3 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | 6 |
| sb.line4 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | 6 |
| sb.line6 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | 5 |
| sb.partIII | — | — | — | — | — | 1 (stage4.sb.foreign_no_filing) |

Unasserted lines: sb.zero

## Schedule C (Form 1040) — Profit or Loss From Business, one per business

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sc.one | — | — | — | — | — | — |
| sc.rrta | — | — | — | 4 | — | — |
| sc.zero | — | — | — | — | — | — |
| sc.statutory | — | — | — | — | — | — |
| sc.passive | — | — | — | — | — | — |
| sc.spouse_owned | — | — | — | — | — | — |
| sc.method_other | — | — | — | — | — | — |
| sc.special | — | — | — | — | — | — |
| sc.screened | — | — | — | 4 | — | — |
| sc.line1 | — | — | — | — | — | 5 |
| sc.line2 | — | — | — | — | — | — |
| sc.line3 | — | — | — | 4 | — | 1 (stage14.sc.basic) |
| sc.line4 | — | — | — | 4 | — | 1 (stage14.sc.basic) |
| sc.line5 | — | — | — | 4 | — | — |
| sc.line6 | — | — | — | — | — | — |
| sc.line7 | — | — | — | 4 | — | 1 (stage14.sc.basic) |
| sc.line8 | — | — | — | — | — | — |
| sc.line9 | — | — | — | 4 | — | 1 (stage14.veh.standard) |
| sc.line10 | — | — | — | — | — | — |
| sc.line11 | — | — | — | — | — | — |
| sc.line12 | — | — | — | 4 | — | — |
| sc.line13 | — | — | — | 4 | — | 17 |
| sc.line14 | — | — | — | — | — | — |
| sc.line15 | — | — | — | — | — | — |
| sc.line16a | — | — | — | — | — | — |
| sc.line16b | — | — | — | — | — | — |
| sc.line17 | — | — | — | — | — | — |
| sc.line18 | — | — | — | — | — | — |
| sc.line19 | — | — | — | — | — | — |
| sc.line20a | — | — | — | 4 | — | 2 (stage14.veh.leased_actual, stage14.sehi.with_lease) |
| sc.line20b | — | — | — | — | — | — |
| sc.line21 | — | — | — | — | — | — |
| sc.line22 | — | — | — | — | — | — |
| sc.line23 | — | — | — | — | — | — |
| sc.line24a | — | — | — | — | — | — |
| sc.meals_50 | — | — | — | — | — | — |
| sc.meals_80 | — | — | — | — | — | — |
| sc.meals_100 | — | — | — | — | — | — |
| sc.meals_50_ded | — | — | — | 4 | — | — |
| sc.meals_80_ded | — | — | — | 4 | — | — |
| sc.line24b | — | — | — | 4 | — | 2 (stage14.sc.basic, stage14.sc.meals_full) |
| sc.line25 | — | — | — | — | — | — |
| sc.line26 | — | — | — | — | — | — |
| sc.line27a | — | — | — | 4 | — | — |
| sc.line48 | — | — | — | — | — | — |
| sc.line27b | — | — | — | 4 | — | — |
| sc.line28 | — | — | — | 4 | — | 3 |
| sc.line29 | — | — | — | 4 | — | — |
| sc.line28_pre179 | — | — | — | 4 | — | — |
| sc.line29_pre179 | — | — | — | 4 | — | — |
| sc.ho_uses | — | — | — | — | — | — |
| sc.ho_other | — | — | — | — | — | — |
| sc.ho_screened | — | — | — | 4 | — | — |
| sc.ho_multi | — | — | — | 4 | — | — |
| sc.ho_sqft | — | — | — | — | — | — |
| sc.ho_home_sqft | — | — | — | — | — | — |
| sc.ho_rate | — | — | — | — | — | — |
| sc.ho_cap_sqft | — | — | — | — | — | — |
| sc.ho_over | — | — | — | 4 | — | — |
| sc.ho_line4_actual | — | — | — | 4 | — | — |
| sc.ho_line4_cap | — | — | — | 3 | — | — |
| sc.ho_line4 | — | — | — | 4 | — | 3 |
| sc.ho_line1 | — | — | — | 4 | — | 1 (stage14.ho.with_179) |
| sc.ho_room | — | — | — | 4 | — | — |
| sc.ho_unlimited | — | — | — | 4 | — | — |
| sc.ho_s179_max | — | — | — | 4 | — | — |
| sc.ho_no179 | — | — | — | 4 | — | — |
| sc.ho_limited | — | — | — | 4 | — | — |
| sc.ho_pre179_floor | — | — | — | 4 | — | — |
| sc.ho_both_limits | — | — | — | 4 | — | — |
| sc.ho_both | — | — | — | 3 | — | — |
| sc.ho_line5_lim | — | — | — | 3 | — | — |
| sc.ho_line5 | — | — | — | 4 | — | — |
| sc.line30 | — | — | — | 4 | — | 9 |
| sc.line31 | — | — | — | 4 | — | 14 |
| sc.line31_pre179 | — | — | — | 4 | — | — |
| sc.loss | — | — | — | 4 | — | — |
| sc.at_risk | — | — | — | — | — | — |
| sc.not_at_risk | — | — | — | 4 | — | — |
| sc.loss_allowed | — | — | — | 3 | — | 1 (stage14.refuse.at_risk) |
| sc.result | — | — | — | 4 | — | — |
| sc.inventory_other | — | — | — | — | — | — |
| sc.line35 | — | — | — | — | — | 1 (stage14.refuse.inventory) |
| sc.line36 | — | — | — | — | — | — |
| sc.line37 | — | — | — | — | — | — |
| sc.line38 | — | — | — | — | — | — |
| sc.line39 | — | — | — | — | — | — |
| sc.line40 | — | — | — | 4 | — | — |
| sc.line41 | — | — | — | — | — | — |
| sc.line42 | — | — | — | 4 | — | — |
| sc.f6 | — | — | — | 4 | — | 1 (stage14.asset.listed_and_not) |
| sc.f14 | — | — | — | 4 | — | 2 (stage14.asset.bonus_100, stage14.asset.listed_and_not) |
| sc.f17 | — | — | — | 4 | — | 3 |
| sc.f19_y3 | — | — | — | 4 | — | — |
| sc.f19_y5 | — | — | — | 4 | — | 1 (stage14.asset.hy_5yr) |
| sc.f19_y7 | — | — | — | 4 | — | — |
| sc.f19_y10 | — | — | — | 4 | — | — |
| sc.f19_y15 | — | — | — | 4 | — | — |
| sc.f19_y20 | — | — | — | 4 | — | — |
| sc.f19_y15sl | — | — | — | 4 | — | 1 (stage14.asset.qip) |
| sc.f25_assets | — | — | — | 4 | — | — |
| sc.f25_veh | — | — | — | 4 | — | — |
| sc.f25 | — | — | — | 4 | — | 2 (stage14.asset.listed_and_not, stage14.asset.listed_forty) |
| sc.f26_assets | — | — | — | 4 | — | — |
| sc.f26_veh | — | — | — | 4 | — | — |
| sc.f26h | — | — | — | 4 | — | 3 |
| sc.f28 | — | — | — | 4 | — | 1 (stage14.asset.listed_forty) |
| sc.f29_assets | — | — | — | 4 | — | — |
| sc.f29_veh | — | — | — | 4 | — | — |
| sc.f29 | — | — | — | 4 | — | 1 (stage14.asset.listed_and_not) |
| sc.s179_elected | — | — | — | 4 | — | — |
| sc.dep_other | — | — | — | 4 | — | — |
| sc.s179_return | — | — | — | 3 | — | — |
| sc.s179_allowed | — | — | — | 4 | — | 1 (stage14.s179.refuse_multi) |
| sc.mq_q4_a | — | — | — | 4 | — | — |
| sc.mq_q4_v | — | — | — | 4 | — | — |
| sc.mq_q4 | — | — | — | 4 | — | — |
| sc.mq_total_a | — | — | — | 4 | — | — |
| sc.mq_total_v | — | — | — | 4 | — | — |
| sc.mq_total | — | — | — | 4 | — | — |
| sc.cost179_a | — | — | — | 4 | — | — |
| sc.cost179_v | — | — | — | 4 | — | — |
| sc.cost179 | — | — | — | 4 | — | — |
| sc.rent_equipment | — | — | — | — | — | — |
| sc.veh_lease | — | — | — | 4 | — | — |
| sc.profit_pos | — | — | — | 4 | — | — |
| sc.hi_uses | — | — | — | — | — | — |
| sc.hi_screen | — | — | — | — | — | — |
| sc.hi_screened | — | — | — | 4 | — | — |
| sc.f7206_line1 | — | — | — | — | — | 1 (stage14.sehi.refuse_ptc) |
| sc.f7206_line2 | — | — | — | 4 | — | 1 (stage14.sehi.ltc) |
| sc.f7206_line3 | — | — | — | 4 | — | — |
| sc.f7206_line4 | — | — | — | 3 | — | — |
| sc.f7206_line5 | — | — | — | 4 | — | — |
| sc.f7206_has | — | — | — | 3 | — | — |
| sc.f7206_line7_pos | — | — | — | 3 | — | — |
| sc.f7206_line7 | — | — | — | 3 | — | 1 (stage14.sehi.two_businesses) |
| sc.f7206_line8 | — | — | — | 3 | — | — |
| sc.f7206_line9_pos | — | — | — | 4 | — | — |
| sc.f7206_line9 | — | — | — | 4 | — | 1 (stage14.sehi.with_sep) |
| sc.f7206_line10 | — | — | — | 3 | — | 1 (stage14.sehi.with_sep) |
| sc.f7206_line13 | — | — | — | 3 | — | — |
| sc.f7206_min | — | — | — | 4 | — | — |
| sc.f7206_line14 | — | — | — | 4 | — | 6 |
| sc.qbi_has | — | — | — | 4 | — | — |
| sc.qbi_se_pos | — | — | — | 4 | — | — |
| sc.qbi_se | — | — | — | 4 | — | — |
| sc.qbi_plan_pos | — | — | — | 4 | — | — |
| sc.qbi_plan | — | — | — | 4 | — | — |
| sc.qbi_ded | — | — | — | 4 | — | — |
| sc.qbi | — | — | — | 4 | — | 3 |
| sc.tips_ot | — | — | — | — | — | — |

Unasserted lines: sc.one, sc.zero, sc.ho_rate, sc.ho_cap_sqft

## Proof-of-concept scope screening

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| scope.schedule1 | — | — | — | — | — | — |
| scope.credits | — | — | — | — | — | — |
| scope.other_income | — | — | — | — | — | — |
| scope.other_line16 | — | — | — | — | — | — |
| scope.ready | — | — | — | — | — | 5 |

## Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| scveh.zero | — | — | — | — | — | — |
| scveh.method | — | — | — | — | — | — |
| scveh.owned | — | — | — | — | — | — |
| scveh.placed_date | — | — | — | — | — | — |
| scveh.miles_business | — | — | — | — | — | — |
| scveh.miles_commuting | — | — | — | — | — | — |
| scveh.miles_other | — | — | — | — | — | — |
| scveh.cent | — | — | — | — | — | — |
| scveh.bm_c | — | — | — | — | — | — |
| scveh.cm_c | — | — | — | 6 | — | — |
| scveh.om_c | — | — | — | — | — | — |
| scveh.nonbusiness_c | — | — | — | — | — | — |
| scveh.total_c | — | — | — | — | — | 1 (stage14.refuse.veh_no_miles) |
| scveh.no_miles | — | — | — | 6 | — | — |
| scveh.over_half | — | — | — | 6 | — | — |
| scveh.parking | — | — | — | — | — | — |
| scveh.smr_ok | — | — | — | — | — | — |
| scveh.smr_bad | — | — | — | 6 | — | — |
| scveh.rate | — | — | — | — | — | — |
| scveh.smr_amount | — | — | — | 6 | — | 1 (stage14.veh.refuse_smr) |
| scveh.line9_standard | — | — | — | 6 | — | — |
| scveh.operating | — | — | — | — | — | — |
| scveh.operating_business | — | — | — | 6 | — | — |
| scveh.line9_actual | — | — | — | 6 | — | — |
| scveh.line9 | — | — | — | 6 | — | 5 |
| scveh.is_actual_owned | — | — | — | 6 | — | — |
| scveh.is_actual_leased | — | — | — | 6 | — | — |
| scveh.lease | — | — | — | — | — | — |
| scveh.lease_business | — | — | — | 5 | — | — |
| scveh.line20a | — | — | — | 6 | — | — |
| scveh.low_use | — | — | — | 6 | — | — |
| scveh.placed | — | — | — | — | — | 2 (stage14.veh.refuse_low_use, stage14.veh.refuse_half_use) |
| scveh.screen | — | — | — | — | — | — |
| scveh.screened | — | — | — | 6 | — | — |
| scveh.cost | — | — | — | — | — | 2 (stage14.veh.refuse_screen, stage14.veh.refuse_too_old) |
| scveh.passenger | — | — | — | — | — | — |
| scveh.suv | — | — | — | — | — | — |
| scveh.year | — | — | — | 6 | — | — |
| scveh.is2025 | — | — | — | 6 | — | — |
| scveh.is2019 | — | — | — | 6 | — | — |
| scveh.y5 | — | — | — | — | — | — |
| scveh.bus_cost | — | — | — | 4 | — | — |
| scveh.s179_elect | — | — | — | — | — | — |
| scveh.suv_cap | — | — | — | — | — | — |
| scveh.s179_bad | — | — | — | 6 | — | — |
| scveh.after_jan19 | — | — | — | — | — | — |
| scveh.bonus_choice | — | — | — | — | — | — |
| scveh.bonus_same | — | — | — | — | — | — |
| scveh.bonus_mixed | — | — | — | 6 | — | — |
| scveh.claims_bonus | — | — | — | 6 | — | — |
| scveh.rate40 | — | — | — | — | — | — |
| scveh.lim_first_bonus | — | — | — | 3 | — | — |
| scveh.lim_first_none | — | — | — | 3 | — | — |
| scveh.lim_2025 | — | — | — | 3 | — | — |
| scveh.lim_prior | — | — | — | 6 | — | — |
| scveh.line7 | — | — | — | 6 | — | 3 |
| scveh.line9w | — | — | — | 6 | — | 3 |
| scveh.s179_2025_ok | — | — | — | 6 | — | 2 (stage14.veh.refuse_suv_cap, stage14.veh.refuse_suv_cap_by_1) |
| scveh.line10 | — | — | — | 6 | — | 1 (stage14.veh.2025_179_limit) |
| scveh.line10_2025 | — | — | — | 6 | — | — |
| scveh.s179_line10 | — | — | — | 6 | — | — |
| scveh.line11 | — | — | — | 6 | — | 1 (stage14.veh.2025_179_limit) |
| scveh.prior_179 | — | — | — | — | — | — |
| scveh.line14 | — | — | — | 6 | — | — |
| scveh.line15 | — | — | — | 4 | — | 1 (stage14.veh.2024_prior179) |
| scveh.bonus_full | — | — | — | 4 | — | 1 (stage14.veh.refuse_bonus_mixed) |
| scveh.bonus_forty | — | — | — | 5 | — | 1 (stage14.veh.refuse_bonus_mixed_forty) |
| scveh.bonus_fullcase | — | — | — | 4 | — | — |
| scveh.bonus_2025 | — | — | — | 6 | — | — |
| scveh.line16 | — | — | — | 6 | — | 2 (stage14.veh.suv_179, stage14.veh.2025_forty) |
| scveh.bonus_allowed | — | — | — | 6 | — | 2 (stage14.veh.2025_bonus, stage14.veh.2025_forty) |
| scveh.line17 | — | — | — | 6 | — | 1 (stage14.veh.2025_forty) |
| scveh.line18 | — | — | — | 4 | — | — |
| scveh.quarter | — | — | — | — | — | — |
| scveh.qconv | — | — | — | 6 | — | — |
| scveh.hy | — | — | — | — | — | — |
| scveh.prior_conv | — | — | — | — | — | — |
| scveh.rate_hy | — | — | — | 3 | — | — |
| scveh.rate_mq | — | — | — | 3 | — | — |
| scveh.rate_prior | — | — | — | 5 | — | — |
| scveh.line19_hy | — | — | — | 4 | — | — |
| scveh.line19_mq | — | — | — | 4 | — | — |
| scveh.line19_prior | — | — | — | 5 | — | — |
| scveh.line19 | — | — | — | 6 | — | 5 |
| scveh.line19_earlier | — | — | — | 6 | — | — |
| scveh.line19_2025 | — | — | — | 4 | — | — |
| scveh.line20 | — | — | — | 6 | — | 8 |
| scveh.b100 | — | — | — | 6 | — | — |
| scveh.k1 | — | — | — | — | — | — |
| scveh.r1 | — | — | — | 6 | — | — |
| scveh.t1 | — | — | — | 6 | — | — |
| scveh.l1 | — | — | — | 5 | — | — |
| scveh.t1s | — | — | — | 6 | — | — |
| scveh.d1 | — | — | — | 4 | — | 1 (stage14.veh.2019_cheap_mq3) |
| scveh.k2 | — | — | — | — | — | — |
| scveh.r2 | — | — | — | 6 | — | — |
| scveh.t2 | — | — | — | 6 | — | — |
| scveh.l2 | — | — | — | 6 | — | — |
| scveh.d2 | — | — | — | 6 | — | — |
| scveh.k3 | — | — | — | — | — | — |
| scveh.r3 | — | — | — | 6 | — | — |
| scveh.t3 | — | — | — | 6 | — | — |
| scveh.l3 | — | — | — | 5 | — | — |
| scveh.d3 | — | — | — | 5 | — | — |
| scveh.k4 | — | — | — | — | — | — |
| scveh.r4 | — | — | — | 6 | — | — |
| scveh.t4 | — | — | — | 6 | — | — |
| scveh.l4 | — | — | — | 5 | — | — |
| scveh.d4 | — | — | — | 5 | — | — |
| scveh.k5 | — | — | — | — | — | — |
| scveh.r5 | — | — | — | 6 | — | — |
| scveh.t5 | — | — | — | 6 | — | — |
| scveh.l5 | — | — | — | 5 | — | — |
| scveh.d5 | — | — | — | 5 | — | — |
| scveh.k6 | — | — | — | — | — | — |
| scveh.r6 | — | — | — | 6 | — | — |
| scveh.t6 | — | — | — | 6 | — | — |
| scveh.l6 | — | — | — | 5 | — | — |
| scveh.d6 | — | — | — | 5 | — | — |
| scveh.d_total | — | — | — | 4 | — | 3 |
| scveh.unrecovered | — | — | — | 4 | — | 3 |
| scveh.post_amount | — | — | — | 4 | — | — |
| scveh.post | — | — | — | 4 | — | 3 |
| scveh.too_old | — | — | — | 6 | — | — |
| scveh.bonus_v | — | — | — | 6 | — | — |
| scveh.macrs_pass | — | — | — | 6 | — | — |
| scveh.macrs_heavy | — | — | — | 6 | — | — |
| scveh.macrs_v | — | — | — | 6 | — | 2 (stage14.veh.heavy_prior, stage14.veh.heavy_2019) |
| scveh.bonus | — | — | — | 6 | — | — |
| scveh.macrs | — | — | — | 6 | — | — |
| scveh.s179_2025 | — | — | — | 6 | — | — |
| scveh.mq_q4 | — | — | — | 6 | — | — |
| scveh.mq_total | — | — | — | 6 | — | — |
| scveh.cost179 | — | — | — | 6 | — | — |
| scveh.bonus_o | — | — | — | 6 | — | — |
| scveh.macrs_o | — | — | — | 5 | — | — |
| scveh.s179_2025_o | — | — | — | 6 | — | — |
| scveh.q4_basis | — | — | — | 5 | — | — |
| scveh.mq_q4_o | — | — | — | 6 | — | — |
| scveh.mq_q4_a2 | — | — | — | 6 | — | — |
| scveh.mq_total_o | — | — | — | 6 | — | — |
| scveh.mq_total_a2 | — | — | — | 3 | — | — |
| scveh.cost179_o | — | — | — | 6 | — | — |
| scveh.cost179_a2 | — | — | — | 2 (classm.scveh.2, classm.scveh.5) | — | — |

Unasserted lines: scveh.zero, scveh.cent, scveh.bm_c, scveh.om_c, scveh.nonbusiness_c, scveh.rate, scveh.y5, scveh.suv_cap, scveh.rate40, scveh.hy, scveh.k1, scveh.k2, scveh.k3, scveh.k4, scveh.k5, scveh.k6

## Schedule D — securities sales and supplied distribution subtotals

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sd.other_forms | — | — | — | — | — | — |
| sd.carryover | — | — | — | — | — | — |
| sd.distributions | — | — | — | — | — | — |
| sd.line18 | — | — | — | — | — | — |
| sd.line19 | — | — | — | — | — | — |
| sd.filing4952 | — | — | — | — | — | — |
| sd.investment_election | — | — | — | — | — | — |
| sd.count | — | — | — | — | — | 14 |
| sd.screen | — | — | — | — | — | — |
| sd.filed | — | — | — | — | — | 22 |
| sd.zero | — | — | — | — | — | — |
| sd.line1a.d | — | — | — | 3 | — | 15 |
| sd.line1a.e | — | — | — | 3 | — | 15 |
| sd.line1a.g | — | — | — | 3 | — | 15 |
| sd.line1a.h | — | — | — | 3 | — | 15 |
| sd.line1b.d | — | — | — | 3 | — | 15 |
| sd.line1b.e | — | — | — | 3 | — | 15 |
| sd.line1b.g | — | — | — | 3 | — | 15 |
| sd.line1b.h | — | — | — | 3 | — | 17 |
| sd.line2.d | — | — | — | 3 | — | 15 |
| sd.line2.e | — | — | — | 3 | — | 15 |
| sd.line2.g | — | — | — | 3 | — | 15 |
| sd.line2.h | — | — | — | 3 | — | 16 |
| sd.line3.d | — | — | — | 3 | — | 15 |
| sd.line3.e | — | — | — | 3 | — | 15 |
| sd.line3.g | — | — | — | 3 | — | 15 |
| sd.line3.h | — | — | — | 3 | — | 16 |
| sd.line8a.d | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 3 | — | 15 |
| sd.line8a.e | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 3 | — | 15 |
| sd.line8a.g | — | — | — | 3 | — | 15 |
| sd.line8a.h | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 3 | — | 15 |
| sd.line8b.d | — | — | — | 3 | — | 15 |
| sd.line8b.e | — | — | — | 3 | — | 15 |
| sd.line8b.g | — | — | — | 3 | — | 15 |
| sd.line8b.h | — | — | — | 3 | — | 16 |
| sd.line9.d | — | — | — | 3 | — | 15 |
| sd.line9.e | — | — | — | 3 | — | 15 |
| sd.line9.g | — | — | — | 3 | — | 15 |
| sd.line9.h | — | — | — | 3 | — | 16 |
| sd.line10.d | — | — | — | 3 | — | 15 |
| sd.line10.e | — | — | — | 3 | — | 15 |
| sd.line10.g | — | — | — | 3 | — | 15 |
| sd.line10.h | — | — | — | 3 | — | 16 |
| sd.line4 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line5 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line6 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line11 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line12 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line14 | — | — | — | 3 | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line13 | — | — | — | 3 | — | — |
| sd.line7 | — | — | — | 3 | — | 2 (sales.netting, sales.mixed_columns) |
| sd.line15 | — | — | — | 3 | — | 3 |
| sd.line16 | — | — | — | 3 | — | 21 |
| sd.line17 | — | — | — | 3 | — | — |
| sd.line20 | — | — | — | 1 (classm.sd.1) | — | — |
| sd.loss_limit | — | — | — | — | — | — |
| sd.limited_loss | — | — | — | — | — | — |
| sd.has_loss | — | — | — | — | — | — |
| sd.line21 | — | — | — | 3 | — | 18 |
| sd.line22 | — | — | — | 3 | — | 49 |
| sd.to1040 | — | — | — | — | — | — |
| sd.net_gain_raw | — | — | — | — | — | 1 (sales.loss.single.700000) |
| sd.net_gain | — | — | — | — | — | — |

Unasserted lines: sd.line18, sd.line19, sd.filing4952, sd.investment_election, sd.screen, sd.zero, sd.loss_limit, sd.limited_loss, sd.has_loss, sd.to1040, sd.net_gain

## Schedule D Tax Worksheet

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sdtw.zero | — | — | — | — | — | — |
| sdtw.ordinary_ceiling | — | — | — | — | — | — |
| sdtw.after22 | — | — | — | — | — | 1 (stage4.sdtw.skip22) |
| sdtw.after32 | — | — | — | — | — | 1 (stage4.sdtw.skip32) |
| sdtw.use1250 | — | — | — | — | — | — |
| sdtw.use28 | — | — | — | — | — | — |
| sdtw.line1 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line2 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line3 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line4 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line5 | — | — | — | 4 | — | 2 (stage4.interest.election, stage4.sdtw.special_rates) |
| sdtw.line6 | — | — | — | 4 | — | 3 |
| sdtw.line7 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line8 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line9 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line10 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line11 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line12 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line13 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line14 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line15 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line16 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line17 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| sdtw.line18 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line19 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line20 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line21 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.line22 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw23 | — | — | — | — | — | — |
| sdtw.line23 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw24 | — | — | — | — | — | — |
| sdtw.line24 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw25 | — | — | — | — | — | — |
| sdtw.line25 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw26 | — | — | — | — | — | — |
| sdtw.line26 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw27 | — | — | — | — | — | — |
| sdtw.line27 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw28 | — | — | — | — | — | — |
| sdtw.line28 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw29 | — | — | — | — | — | — |
| sdtw.line29 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw30 | — | — | — | — | — | — |
| sdtw.line30 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw31 | — | — | — | — | — | — |
| sdtw.line31 | — | — | — | 4 | — | 4 |
| sdtw.raw32 | — | — | — | — | — | — |
| sdtw.line32 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw33 | — | — | — | — | — | — |
| sdtw.line33 | — | — | — | 4 | — | 3 |
| sdtw.raw34 | — | — | — | — | — | — |
| sdtw.line34 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw35 | — | — | — | — | — | — |
| sdtw.line35 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw36 | — | — | — | — | — | — |
| sdtw.line36 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw37 | — | — | — | — | — | — |
| sdtw.line37 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw38 | — | — | — | — | — | — |
| sdtw.line38 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw39 | — | — | — | — | — | — |
| sdtw.line39 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw40 | — | — | — | — | — | — |
| sdtw.line40 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw41 | — | — | — | — | — | — |
| sdtw.line41 | — | — | — | 3 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw42 | — | — | — | — | — | — |
| sdtw.line42 | — | — | — | 4 | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw43 | — | — | — | — | — | — |
| sdtw.line43 | — | — | — | 4 | — | 5 |
| sdtw.line44 | — | — | — | — | — | 3 |
| sdtw.line45 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line46 | — | — | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line47 | — | — | — | 4 | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |

Unasserted lines: sdtw.zero, sdtw.ordinary_ceiling, sdtw.use1250, sdtw.use28, sdtw.raw23, sdtw.raw24, sdtw.raw25, sdtw.raw26, sdtw.raw27, sdtw.raw28, sdtw.raw29, sdtw.raw30, sdtw.raw31, sdtw.raw32, sdtw.raw33, sdtw.raw34, sdtw.raw35, sdtw.raw36, sdtw.raw37, sdtw.raw38, sdtw.raw39, sdtw.raw40, sdtw.raw41, sdtw.raw42, sdtw.raw43

## Student Loan Interest Deduction Worksheet—Schedule 1, Line 21

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| sli.zero | — | — | — | — | — | — |
| sli.interest | — | — | — | — | — | — |
| sli.has | — | — | — | — | — | — |
| sli.claimed | — | — | — | — | — | — |
| sli.max | — | — | — | — | — | — |
| sli.line1 | — | — | — | 4 | — | 1 (stage11.sli.cap) |
| sli.line2 | — | — | — | 4 | — | — |
| sli.line3 | — | — | — | 5 | — | 1 (stage11.sli.with_adjustments) |
| sli.line4 | — | — | — | 4 | — | — |
| sli.base_other | — | — | — | — | — | — |
| sli.base_joint | — | — | — | — | — | — |
| sli.line5 | — | — | — | 4 | — | 1 (stage11.sli.boundary_joint) |
| sli.over | — | — | — | — | — | — |
| sli.line6 | — | — | — | — | — | 3 |
| sli.divisor_other | — | — | — | — | — | — |
| sli.divisor_joint | — | — | — | — | — | — |
| sli.divisor | — | — | — | — | — | — |
| sli.line8_figured | — | — | — | — | — | — |
| sli.line8 | — | — | — | 4 | — | 7 |
| sli.line9 | — | — | — | 4 | — | — |
| sli.eligible | — | — | — | — | — | — |
| sli.allowed | — | — | — | — | — | — |
| sli.deduction | — | — | — | — | — | 11 |

Unasserted lines: sli.zero, sli.has, sli.max, sli.base_other, sli.base_joint, sli.over, sli.divisor_other, sli.divisor_joint, sli.divisor, sli.line8_figured, sli.eligible, sli.allowed

## Social Security Benefits Worksheet—Lines 6a and 6b

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| ssb.benefits | — | — | — | — | — | — |
| ssb.pub915 | — | — | — | — | — | — |
| ssb.lump_sum | — | — | — | — | — | — |
| ssb.terror_disability | — | — | — | — | — | — |
| ssb.lived_apart | — | — | — | — | — | — |
| ssb.line1 | — | — | — | 5 | — | 1 (stage16.ira.i10) |
| ssb.has_benefits | — | — | — | — | — | — |
| ssb.line2 | — | — | — | 5 | — | 1 (stage16.ira.i10) |
| ssb.line3 | — | — | — | 5 | — | 2 (stage11.ss.unemployment, stage16.ira.i10) |
| ssb.line4 | — | — | — | 5 | — | 1 (stage16.ira.i10) |
| ssb.line5 | — | — | — | 5 | — | 1 (stage16.ira.i10) |
| ssb.ira_line20 | — | — | — | — | — | — |
| ssb.line6 | — | — | — | 5 | — | 2 (stage11.ss.educator, stage16.ira.i10) |
| ssb.line7 | — | — | — | 5 | — | 3 |
| ssb.base_single | — | — | — | — | — | — |
| ssb.base_joint | — | — | — | — | — | — |
| ssb.zero | — | — | — | — | — | — |
| ssb.mfs_base | — | — | — | — | — | — |
| ssb.line8 | — | — | — | 3 | — | 2 (stage13.ssb_joint_base, stage16.ira.i10) |
| ssb.line9 | — | — | — | 4 | — | 2 (stage10.ss.none, stage13.ssb_joint_base) |
| ssb.adjust_single | — | — | — | — | — | — |
| ssb.adjust_joint | — | — | — | — | — | — |
| ssb.mfs_adjust | — | — | — | — | — | — |
| ssb.line10 | — | — | — | 3 | — | — |
| ssb.line11 | — | — | — | 4 | — | — |
| ssb.line12 | — | — | — | 5 | — | — |
| ssb.line13 | — | — | — | 5 | — | 1 (stage10.ss.middle) |
| ssb.line14 | — | — | — | 5 | — | 1 (stage10.ss.small_benefits) |
| ssb.line15 | — | — | — | 4 | — | 1 (stage10.ss.middle) |
| ssb.mfs_together | — | — | — | — | — | — |
| ssb.line16_sum | — | — | — | — | — | — |
| ssb.line16_together | — | — | — | — | — | — |
| ssb.line16 | — | — | — | 5 | — | 2 (stage10.ss.top, stage10.ss.small_benefits) |
| ssb.line17 | — | — | — | 5 | — | — |
| ssb.line18_figured | — | — | — | — | — | — |
| ssb.line18 | — | — | — | 5 | E via f1040.line6b (PE, TC) | 1 (stage16.ira.i10) |

Unasserted lines: ssb.has_benefits, ssb.ira_line20, ssb.base_single, ssb.base_joint, ssb.zero, ssb.mfs_base, ssb.adjust_single, ssb.adjust_joint, ssb.mfs_adjust, ssb.mfs_together, ssb.line16_sum, ssb.line16_together, ssb.line18_figured

## Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| tipjob.one | — | — | — | — | — | — |
| tipjob.qualified | — | — | — | — | — | — |
| tipjob.amount | — | — | — | — | — | — |
| tipjob.mixed | — | — | — | 1 (classm.tipjob.1) | — | — |
| tipjob.col_c | — | — | — | — | — | — |
| tipjob.col_d | — | — | — | 1 (classm.tipjob.1) | — | — |

Unasserted lines: tipjob.one, tipjob.col_c

## Unrecaptured Section 1250 Gain Worksheet — distribution-only path

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| u1250.line1 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line2 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line3 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line4 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line5 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line6 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line7 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line8 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line9 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line10 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line12 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line16 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line11 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line13 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line14 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.line15 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | — |
| u1250.combined | — | — | — | — | — | — |
| u1250.line17 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | 1 (stage4.feeders.shortloss) |
| u1250.line18 | — | — | — | 2 (classm.u1250.1, classm.u1250.2) | — | 1 (stage4.feeders.shortloss) |

Unasserted lines: u1250.combined

## Form W-2 — wage, withholding and Social Security boxes by employer

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| w2.box1 | — | — | — | — | — | — |
| w2.box2 | — | — | — | — | — | — |
| w2.box3 | — | — | — | — | — | — |
| w2.box7 | — | — | — | — | — | — |
| w2.box4 | — | — | — | — | — | — |
| w2.wages | — | — | — | 1 (classm.w2.1) | — | — |
| w2.one | — | — | — | — | — | — |
| w2.over | — | — | — | 1 (classm.w2.1) | — | — |
| w2.box5 | — | — | — | — | — | — |
| w2.box6 | — | — | — | — | — | — |
| w2.box10 | — | — | — | — | — | — |
| w2.has_box10 | — | — | — | 1 (classm.w2.1) | — | — |
| w2.box10_wages | — | — | — | — | — | — |
| w2.box10_bad | — | — | — | 1 (classm.w2.1) | — | — |
| w2.dc_net | — | — | — | 1 (classm.w2.1) | — | 1 (stage15.refuse.w2.box10_bad) |
| w2.dc_benefits | — | — | — | 1 (classm.w2.1) | — | — |
| w2.dc_zero | — | — | — | — | — | — |
| w2.box12_any | — | — | — | — | — | — |
| w2.box12_userra | — | — | — | — | — | — |
| w2.box12_d | — | — | — | — | — | — |
| w2.box12_e | — | — | — | — | — | — |
| w2.box12_f | — | — | — | — | — | — |
| w2.box12_g | — | — | — | — | — | — |
| w2.box12_h | — | — | — | — | — | — |
| w2.box12_s | — | — | — | — | — | — |
| w2.box12_aa | — | — | — | — | — | — |
| w2.box12_bb | — | — | — | — | — | — |
| w2.box12_ee | — | — | — | — | — | — |
| w2.has_g | — | — | — | 1 (classm.w2.1) | — | — |
| w2.g_governmental | — | — | — | — | — | — |
| w2.g_elective | — | — | — | — | — | — |
| w2.g_bad | — | — | — | 1 (classm.w2.1) | — | — |
| w2.g_gov_part | — | — | — | 1 (classm.w2.1) | — | 1 (stage15.refuse.w2.g_bad) |
| w2.g_counted | — | — | — | 1 (classm.w2.1) | — | — |
| w2.zero | — | — | — | — | — | — |
| w2.code_h | — | — | — | 1 (classm.w2.1) | — | — |
| w2.sav_listed | — | — | — | 1 (classm.w2.1) | — | 2 (stage15.refuse.w2.userra, stage15.refuse.w2.code_h) |
| w2.sav_deferral | — | — | — | 1 (classm.w2.1) | — | — |

Unasserted lines: w2.one, w2.dc_zero, w2.zero

## Schedule SE (Form 1040) — Self-Employment Tax, one per person

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| line2 | — | — | — | — | — | — |
| line8a | — | — | — | — | — | — |
| zero | — | — | — | — | — | — |
| line3 | — | — | — | — | — | — |
| positive | — | — | — | — | — | — |
| rate9235 | — | — | — | — | — | — |
| line3pos | — | — | — | — | — | — |
| line4a_pos | — | — | — | — | — | — |
| line4a | — | — | — | — | — | — |
| line4b | — | — | — | — | — | — |
| line4c_sum | — | — | — | — | — | — |
| floor | — | — | — | — | — | — |
| owes | — | — | — | — | — | — |
| line4c_owes | — | — | — | — | — | — |
| line4c | — | — | — | — | — | — |
| line5b | — | — | — | — | — | — |
| line6 | — | — | — | — | — | — |
| line7 | — | — | — | — | — | — |
| line8d | — | — | — | — | — | — |
| line9 | — | — | — | — | — | — |
| ss_base | — | — | — | — | — | — |
| rate124 | — | — | — | — | — | — |
| line10 | — | — | — | — | — | — |
| rate029 | — | — | — | — | — | — |
| line11 | — | — | — | — | — | — |
| line12 | — | — | — | — | — | — |
| rate50 | — | — | — | — | — | — |
| line13 | — | — | — | — | — | — |

Unasserted lines: zero, line3, positive, rate9235, line3pos, line4a_pos, line4a, line4b, line4c_sum, floor, owes, line4c_owes, line4c, line5b, line6, line7, line8d, line9, ss_base, rate124, line10, rate029, line11, line12, rate50, line13

## Tax on an amount — Tax Table or Tax Computation Worksheet

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — |
| status | — | — | — | — | — | — |
| below_boundary | — | — | — | — | — | — |
| table_tax | — | — | — | — | — | — |
| worksheet_tax | — | — | — | — | — | — |
| tax | — | — | — | — | — | — |

Unasserted lines: below_boundary, table_tax, worksheet_tax, tax

## Tax Computation Worksheet—Line 16

| line | A | B | C | M | E | R |
| --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — |
| status | — | — | — | — | — | — |
| single.row1.product | — | — | — | — | — | — |
| single.row1.tax | — | — | — | — | — | — |
| single.row2.product | — | — | — | — | — | — |
| single.row2.tax | — | — | — | — | — | — |
| single.row3.product | — | — | — | — | — | — |
| single.row3.tax | — | — | — | — | — | — |
| single.row4.product | — | — | — | — | — | — |
| single.row4.tax | — | — | — | — | — | — |
| single.row5.product | — | — | — | — | — | — |
| single.row5.tax | — | — | — | — | — | — |
| single.result | — | — | — | — | — | — |
| mfj.row1.product | — | — | — | — | — | — |
| mfj.row1.tax | — | — | — | — | — | — |
| mfj.row2.product | — | — | — | — | — | — |
| mfj.row2.tax | — | — | — | — | — | — |
| mfj.row3.product | — | — | — | — | — | — |
| mfj.row3.tax | — | — | — | — | — | — |
| mfj.row4.product | — | — | — | — | — | — |
| mfj.row4.tax | — | — | — | — | — | — |
| mfj.row5.product | — | — | — | — | — | — |
| mfj.row5.tax | — | — | — | — | — | — |
| mfj.result | — | — | — | — | — | — |
| mfs.row1.product | — | — | — | — | — | — |
| mfs.row1.tax | — | — | — | — | — | — |
| mfs.row2.product | — | — | — | — | — | — |
| mfs.row2.tax | — | — | — | — | — | — |
| mfs.row3.product | — | — | — | — | — | — |
| mfs.row3.tax | — | — | — | — | — | — |
| mfs.row4.product | — | — | — | — | — | — |
| mfs.row4.tax | — | — | — | — | — | — |
| mfs.row5.product | — | — | — | — | — | — |
| mfs.row5.tax | — | — | — | — | — | — |
| mfs.result | — | — | — | — | — | — |
| hoh.row1.product | — | — | — | — | — | — |
| hoh.row1.tax | — | — | — | — | — | — |
| hoh.row2.product | — | — | — | — | — | — |
| hoh.row2.tax | — | — | — | — | — | — |
| hoh.row3.product | — | — | — | — | — | — |
| hoh.row3.tax | — | — | — | — | — | — |
| hoh.row4.product | — | — | — | — | — | — |
| hoh.row4.tax | — | — | — | — | — | — |
| hoh.row5.product | — | — | — | — | — | — |
| hoh.row5.tax | — | — | — | — | — | — |
| hoh.result | — | — | — | — | — | — |
| tax | — | — | — | — | — | — |

Unasserted lines: single.row1.product, single.row1.tax, single.row2.product, single.row2.tax, single.row3.product, single.row3.tax, single.row4.product, single.row4.tax, single.row5.product, single.row5.tax, single.result, mfj.row1.product, mfj.row1.tax, mfj.row2.product, mfj.row2.tax, mfj.row3.product, mfj.row3.tax, mfj.row4.product, mfj.row4.tax, mfj.row5.product, mfj.row5.tax, mfj.result, mfs.row1.product, mfs.row1.tax, mfs.row2.product, mfs.row2.tax, mfs.row3.product, mfs.row3.tax, mfs.row4.product, mfs.row4.tax, mfs.row5.product, mfs.row5.tax, mfs.result, hoh.row1.product, hoh.row1.tax, hoh.row2.product, hoh.row2.tax, hoh.row3.product, hoh.row3.tax, hoh.row4.product, hoh.row4.tax, hoh.row5.product, hoh.row5.tax, hoh.result, tax

Unasserted computed lines across all documents: 621. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)
Asserted keys not matching a line id: person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line3, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.positive, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4a, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.owes, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4c, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line5b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line6, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line7, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line8d, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line9, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line10, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line11, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line12, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line13, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, qdcg.f1040.line15, qdcg.f1040.line3a, qdcg.f1040.status, f1040.qdcg.line25, qdcg.sd.distributions