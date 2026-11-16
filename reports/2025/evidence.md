# Evidence coverage per line

**Scoreboard.** Share of computed lines with at least one outside-family assertion: 561 of 3883 (14.4%). H (human source reading): 0, B (human worked values): 0, second-family M: 448, E: 223.

A computed line is one whose atom is not `input`, `param` or `copy`. An outside-family assertion is a signed human source reading (H), a class B fixture (human worked values), a class M fixture whose recorded model is not a Claude model (second-family M), or an engine assertion (E) under the rule below. The sub-counts overlap: a line with several kinds counts once in the share. H checks the encoded rule against IRS text; B and M check worked values. Second-family transcription and render readings are reported separately in second_family.md and do not yet enter this scoreboard. Class A, Claude-family M, C and R do not move it.

H — a MATCH verdict and a reason in the reader's own words, with a current per-line receipt covering the displayed reading, folded helpers, dependencies and sources. The log's exact contents must have been committed by its named reader. A guided question credits only its own computation. Other packets credit their printed line and helpers actually expanded in the reading; referenced amounts do not receive credit. See the linked human logs for the scope of each reading. H supplies no hand-calculated expected value and never fills the B column. No tool issues receipts at present (the reading packets and their renderer are retired), so no receipt is current and no line earns H; the recorded readings are kept and listed below with their verdicts.

Optional human readings pending or ineligible (no H credit; original findings retained): f1040: f1040.line12e: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; person: person.age65: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.standardbase: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.extra: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.extra: MISMATCH; no H credit; finding retained for investigation; sa: sa.boxes_age65: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.boxes_blind: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.extra_age65: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.extra_age65: MISMATCH; no H credit; finding retained for investigation; sa: sa.extra_blind: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.extra_blind: MISMATCH; no H credit; finding retained for investigation; sa: sa.standardraw: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.standardraw: UNCLEAR; no H credit; finding retained for investigation; sa: sa.mfs: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.mfs_spouse_itemizes: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.standard: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.itemizes: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit; sa: sa.deduction: no reading tool issues receipts (the reading packets are retired), so its receipt cannot be current; no H credit.

Fixtures that assert each line, by evidence class, as a count of cases (ids listed when two or fewer). A — official IRS worked example, cited. B — human hand-work recorded with the worker and the document revision; none yet. C — a named, versioned calculator or engine record in fixtures/2025/differential/ (spec 6.1); none yet. M — isolated model hand-work with the model, prompt hash and snapshot recorded (fixtures/2025/classm.json, reviews/2025/classm/); second-family M fixtures are those whose recorded model does not start with "claude". E — the engine differential (tools/engines; reports/2025/engine_differential.md and .json): PolicyEngine-US (PE), Tax-Calculator (TC), OpenTaxSolver, UsTaxes run over 1700 generated returns. A line gets an E assertion only when, for at least one engine, the engine computes the line rather than taking it whole as an input, the project value was nonzero on at least 50 compared returns, and fewer than half of the nonzero returns the engine reached (compared plus excluded) were excluded under an engine limitation; the cell prints each engine's compared, nonzero and excluded counts, and an engine that falls short of the rule is marked "below rule" and asserts nothing. R — recorded regression from the project's own evaluator, no class claimed; agreement with the Lean reference evaluator (reports/2025/evaluator_agreement.md) is evaluator agreement over the same data, not an independent engine, and earns no class.

An outside-family assertion (B, second-family M or E) on a line whose atom is `copy` also credits the first line along its copy chain whose atom is not `copy`, because a copy's value equals its source's exactly, so agreement on the copy is agreement on the source; the table marks each such credit "via <copy line>" (the chain walked, when longer than one copy), the copy line keeps its own cell, and the sub-counts above include credited lines. In this report 498 assertions are credited through copies (B cases: 0; second-family M cases: 452; engine-line assertions: 46); 4 assertions on 2 copy lines could not be resolved statically and stay on the copy line only (qdcg.line22, qdcg.line24).

Engine ids with no line of their own (never an E assertion): f1040.tax_before_credits (PE), f1040.tax_before_credits (TC), f1040.tax_before_credits (OpenTaxSolver), f1040.tax_before_credits (UsTaxes). Mapped lines taken whole from the generator's facts: none. Components of compared lines that enter the engine as generator facts rather than the engine's own form arithmetic (the line still counts as engine-computed; the component does not): PolicyEngine-US f1040.line10: the HSA deduction (Form 8889 line 13) enters as the generator's health_savings_account_ald; the engine computes the educator, half-of-self-employment-tax, IRA and student loan interest components and the sum; PolicyEngine-US f8962.line11d: the Form 1095-A column B total (line 11 column (b)) enters as the engine's slcsp, and every member of the return as enrolled (pays_aca_premium); the engine computes the contribution and the difference; PolicyEngine-US f8962.line11e: the Form 1095-A column A total (line 11 column (a)) enters as slcsp times selected_marketplace_plan_benchmark_ratio; the engine takes the smaller of it and the credit (used_aca_ptc); PolicyEngine-US f8962.line26: as line 11 column (e); compared only where no advance payments were made; Tax-Calculator f1040.line10: the HSA deduction (e03290), the educator expenses deduction (e03220) and the IRA contributions (e03150) enter as the generator's amounts; the engine computes the half-of-self-employment-tax component and the sum (returns with student loan interest, or an IRA deduction phased out by modified AGI, are excluded); Tax-Calculator f1040.line20: the foreign tax paid (e07300) is a supplied amount; the engine computes the credit limit; Tax-Calculator f1040.line19: the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; the engine subtracts them in Credit Limit Worksheet A; Tax-Calculator f1040.line24: the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; the engine applies the tax limit; returns with a saver's credit are excluded; OpenTaxSolver person[taxpayer].f8889[hsa].line12: Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; the program does not compute the line 3 limitation chart; it computes lines 5 to 13; OpenTaxSolver person[taxpayer].f8889[hsa].line13: Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; the program computes lines 5 to 13; OpenTaxSolver f1040.line10: Schedule 1 line 11 (educator expenses after the $300 limit) and line 20 (the IRA deduction) enter as the generator's amounts; lines 13 and 15 come from the engine's own Form 8889 and Schedule SE runs; line 21 is the engine's student loan worksheet; OpenTaxSolver f1040.line20: Schedule 3 line 1 (the foreign tax credit) is the smaller of the creditable foreign tax and the engine's own line 16, figured by the adapter; OpenTaxSolver f8960.line17: Form 8960 line 13 (modified AGI) and line 5a (net gain) are the engine's own Form 1040 lines 11a and 7a; line 9a is the investment interest when the engine itemized; lines 8, 11, 12 and 15 to 17 are the program's; OpenTaxSolver f8995.line15: Form 8995 line 12 (net capital gain plus qualified dividends) is figured from the facts; line 1 column (c) is the program's own Schedule C line 31 less Schedule 1 lines 15 to 17 from its Form 1040 output; line 11 is its Form 1040 lines 11a less 12 less 13b; OpenTaxSolver s8812.line14: Schedule 8812 line 13 (Credit Limit Worksheet A) is the engine's own Form 1040 line 18 less Schedule 3 lines 1 and 2, figured by the adapter; OpenTaxSolver s8812.line27: Schedule 8812 line 18a (earned income) is the engine's own Form 1040 line 1z plus Schedule SE line 3 (profit or loss) less line 13, not below zero, and line 13 the adapter's Credit Limit Worksheet A; lines 21 (boxes 4 and 6), 22 (Schedule 1 line 15) and 24 (zero: no EIC, no excess social security) are supplied; OpenTaxSolver f2441.line11: Form 2441 line 4 (earned income) is the engine's own Form 1040 line 1z less the spouse's wages, plus its Schedule SE lines 3 less 13 by file import; line 10 is its own Form 1040 line 18 less Schedule 3 line 1; OpenTaxSolver sd.line19: Schedule D line 19 is supplied as Form 1099-DIV box 2b; the program takes the Unrecaptured Section 1250 Gain Worksheet result as an input; OpenTaxSolver f8959.line18: Form 8959 line 8 (self-employment income) is the engine's own Schedule SE line 6; UsTaxes f1040.line10: Schedule 1 line 19a (UsTaxes' slot for the IRA deduction, `otherIncome.iraDeduction`) enters as the generator's contributions and the educator expenses as paid (the engine applies the $300 limit); lines 13 and 21 are the engine's own Form 8889 and student loan interest worksheet; UsTaxes s1.line26: Schedule 1 line 19a (the IRA deduction) enters as the generator's contributions; the engine computes the other adjustments and the sum; UsTaxes f1040.line20: Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid; returns where the tax limits it are excluded; UsTaxes f1040.line24: Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid, and Form 5695 Part II as the generator's credit; returns with either limited, or with any Schedule 3 credit, are excluded after the credits; UsTaxes sd.line16: the sales enter as Form 8949 rows (UsTaxes' Asset list, all on boxes C and F); the engine computes the gains, the wash-sale adjustments and Schedule D's totals.

## Form 4562 — one item of depreciable property (other than a vehicle) of a business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| asset.zero | — | — | — | — | — | — | — |
| asset.class | — | — | — | — | — | — | — |
| asset.period | — | — | — | 4 | — | — | — |
| asset.outside | — | — | — | — | — | — | — |
| asset.qip_early | — | — | — | — | — | — | — |
| asset.claims_bonus | — | — | — | — | — | — | — |
| asset.kind_excluded | — | — | — | — | — | — | — |
| asset.software | — | — | — | — | — | — | — |
| asset.software_spread | — | — | — | — | — | — | — |
| asset.software_spread_if_software | — | — | — | — | — | — | — |
| asset.industry | — | — | — | — | — | — | — |
| asset.industry_item | — | — | — | — | — | — | — |
| asset.industry_item_if_industry | — | — | — | — | — | — | — |
| asset.long_production | — | — | — | — | — | — | — |
| asset.got_other | — | — | — | — | — | — | — |
| asset.acquired_before_bonus_date | — | — | — | — | — | — | — |
| asset.used_before | — | — | — | — | — | — | — |
| asset.used_before_if_bonus | — | — | — | — | — | — | — |
| asset.ended_this_year | — | — | — | — | — | — | — |
| asset.basis_changed | — | — | — | — | — | — | — |
| asset.use_changed | — | — | — | — | — | — | — |
| asset.use_changed_if_earlier | — | — | — | — | — | — | — |
| asset.short_year | — | — | — | — | — | — | — |
| asset.method_other | — | — | — | — | — | — | — |
| asset.ads_required | — | — | — | — | — | — | — |
| asset.outside_use | — | — | — | — | — | — | — |
| asset.qbu_low | — | — | — | — | — | — | — |
| asset.qbu_low_if_listed | — | — | — | — | — | — | — |
| asset.screen | — | — | — | — | — | — | 1 (mutation.m4.asset.qip_2016_screen) |
| asset.screened | — | — | — | — | — | — | — |
| asset.placed | — | — | — | — | — | — | — |
| asset.cost | — | — | — | — | — | — | 6 |
| asset.pct | — | — | — | — | — | — | — |
| asset.cent | — | — | — | — | — | — | — |
| asset.hundred | — | — | — | — | — | — | — |
| asset.pct_c | — | — | — | — | — | — | — |
| asset.pct_bad | — | — | — | — | — | — | — |
| asset.listed | — | — | — | — | — | — | — |
| asset.half | — | — | — | — | — | — | — |
| asset.over_half | — | — | — | — | — | — | — |
| asset.listed_low | — | — | — | — | — | — | — |
| asset.basis | — | — | — | 3 | — | — | 3 |
| asset.placed_this_year | — | — | — | — | — | — | 1 (stage14.mut.asset_2025_listed_unanswered) |
| asset.on_19 | — | — | — | — | — | — | 1 (stage14.asset.listed_forty) |
| asset.on_17 | — | — | — | — | — | — | 2 (stage14.asset.refuse_listed_low_past_gds, stage14.mut.asset_2025_listed_unanswered) |
| asset.on_26_this_year | — | — | — | — | — | — | 1 (stage14.asset.listed_forty) |
| asset.year | — | — | — | — | — | — | — |
| asset.last | — | — | — | — | — | — | — |
| asset.done | — | — | — | — | — | — | — |
| asset.quarter | — | — | — | — | — | — | — |
| asset.qconv | — | — | — | — | — | — | — |
| asset.s179 | — | — | — | — | — | — | — |
| asset.not179 | — | — | — | — | — | — | — |
| asset.s179_bad | — | — | — | — | — | — | 2 (stage14.mut.s179_half_fifty_cents, mutation.m4.asset.fully_recovered_no_179) |
| asset.after179 | — | — | — | — | — | — | 5 |
| asset.after_jan19 | — | — | — | — | — | — | — |
| asset.bonus_choice | — | — | — | — | — | — | — |
| asset.bonus_claimed | — | — | — | — | — | — | — |
| asset.bonus_same | — | — | — | — | — | — | — |
| asset.bonus_mixed | — | — | — | — | — | — | — |
| asset.rate40 | — | — | — | — | — | — | — |
| asset.bonus_full | — | — | — | — | — | — | 1 (stage14.asset.refuse_bonus_mixed) |
| asset.bonus_forty | — | — | — | — | — | — | 1 (stage14.asset.refuse_bonus_mixed_forty) |
| asset.bonus_fullcase | — | — | — | — | — | — | — |
| asset.bonus | — | — | — | 3 | — | — | 7 |
| asset.bonus_elected | — | — | — | — | — | — | — |
| asset.f25 | — | — | — | 1 (classm.asset.2) | — | — | 3 |
| asset.f26i | — | — | — | 1 (classm.asset.2) | — | — | 1 (stage14.asset.listed_and_not) |
| asset.ub | — | — | — | — | — | — | — |
| asset.col19c | — | — | — | 3 | — | — | 1 (stage14.asset.listed_and_not) |
| asset.hy | — | — | — | — | — | — | — |
| asset.rate_hy | — | — | — | — | — | — | — |
| asset.rate_mq | — | — | — | — | — | — | — |
| asset.macrs_hy | — | — | — | — | — | — | — |
| asset.macrs_mq | — | — | — | — | — | — | — |
| asset.macrs_this_year | — | — | — | 3 | — | — | 17 |
| asset.mqbase | — | — | — | — | — | — | — |
| asset.mqbase_q4 | — | — | — | — | — | — | — |
| asset.prior_conv | — | — | — | — | — | — | — |
| asset.prior_179 | — | — | — | — | — | — | — |
| asset.prior_bonus | — | — | — | — | — | — | — |
| asset.ub_prior_a | — | — | — | — | — | — | 1 (stage14.asset.prior_179_full) |
| asset.ub_prior | — | — | — | — | — | — | 1 (stage14.asset.prior_179_bonus) |
| asset.rate_prior | — | — | — | — | — | — | — |
| asset.macrs_prior_live | — | — | — | — | — | — | — |
| asset.macrs_prior | — | — | — | 2 (classm.asset.1, classm.asset.4) | — | — | 10 |
| asset.dep_this_year | — | — | — | — | — | — | — |
| asset.bonus_this_year | — | — | — | — | — | — | — |
| asset.s179_this_year | — | — | — | — | — | — | — |
| asset.mq_q4 | — | — | — | — | — | — | — |
| asset.mq_total | — | — | — | — | — | — | — |
| asset.cost179 | — | — | — | — | — | — | — |
| asset.cost179_over_half | — | — | — | — | — | — | — |
| asset.is_section179 | — | — | — | — | — | — | — |
| asset.cost179_real | — | — | — | — | — | — | — |
| asset.dep_prior | — | — | — | — | — | — | — |
| asset.dep_listed | — | — | — | 1 (classm.asset.2) | — | — | 3 |
| asset.no | — | — | — | — | — | — | — |
| asset.s179_bad_test1 | — | — | — | — | — | — | — |
| asset.s179_bad_test2 | — | — | — | — | — | — | — |
| asset.s179_bad_test2_test1 | — | — | — | — | — | — | — |
| asset.s179_bad_test2_test2 | — | — | — | — | — | — | — |
| asset.s179_bad_test2_from2 | — | — | — | — | — | — | — |

Unasserted lines: asset.zero, asset.outside, asset.qip_early, asset.claims_bonus, asset.software_spread_if_software, asset.industry_item_if_industry, asset.used_before_if_bonus, asset.use_changed_if_earlier, asset.qbu_low_if_listed, asset.screened, asset.cent, asset.hundred, asset.pct_c, asset.pct_bad, asset.half, asset.over_half, asset.listed_low, asset.year, asset.last, asset.done, asset.qconv, asset.bonus_claimed, asset.bonus_mixed, asset.rate40, asset.bonus_fullcase, asset.bonus_elected, asset.ub, asset.hy, asset.rate_hy, asset.rate_mq, asset.macrs_hy, asset.macrs_mq, asset.mqbase, asset.mqbase_q4, asset.rate_prior, asset.macrs_prior_live, asset.dep_this_year, asset.bonus_this_year, asset.s179_this_year, asset.mq_q4, asset.mq_total, asset.cost179, asset.cost179_over_half, asset.is_section179, asset.cost179_real, asset.dep_prior, asset.no, asset.s179_bad_test1, asset.s179_bad_test2, asset.s179_bad_test2_test1, asset.s179_bad_test2_test2, asset.s179_bad_test2_from2

## Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| carloan.zero | — | — | — | — | — | — | — |
| carloan.kind | — | — | — | — | — | — | — |
| carloan.requirements | — | — | — | — | — | — | — |
| carloan.vehicle | — | — | — | — | — | — | — |
| carloan.eligible | — | — | — | — | — | — | — |
| carloan.interest | — | — | — | — | — | — | — |
| carloan.mixed | — | — | — | — | — | — | — |
| carloan.financed | — | — | — | — | — | — | — |
| carloan.nonqualifying | — | — | — | — | — | — | — |
| carloan.down | — | — | — | — | — | — | — |
| carloan.nonqualifying_debt | — | — | — | — | — | — | — |
| carloan.mixed_qualifying | — | — | — | — | — | — | — |
| carloan.refi_balance | — | — | — | — | — | — | — |
| carloan.refi_whole | — | — | — | — | — | — | — |
| carloan.refi_qualifying | — | — | — | — | — | — | — |
| carloan.refi_nested | — | — | — | — | — | — | — |
| carloan.allocated | — | — | — | — | — | — | — |
| carloan.refi_interest | — | — | — | — | — | — | — |
| carloan.mixed_interest | — | — | — | — | — | — | — |
| carloan.mixed_prorated | — | — | — | — | — | — | — |
| carloan.qpvli | — | — | — | — | — | — | 1 (stage12.car.mixed_sc_interest_prorated) |
| carloan.col_ii_input | — | — | — | — | — | — | — |
| carloan.sc_interest | — | — | — | — | — | — | — |
| carloan.sc_mixed_prorated | — | — | — | — | — | — | — |
| carloan.sc_mixed | — | — | — | — | — | — | — |
| carloan.sc_refi | — | — | — | — | — | — | — |
| carloan.sc_allocated | — | — | — | — | — | — | — |
| carloan.col_ii | — | — | — | 2 (classm.carloan.1, classm.carloan.2) | — | — | 1 (stage12.car.mixed_sc_interest_prorated) |
| carloan.col_iii | — | — | — | 2 (classm.carloan.1, classm.carloan.2) | — | — | 1 (stage12.car.mixed_sc_interest_prorated) |

Unasserted lines: carloan.zero, carloan.eligible, carloan.nonqualifying_debt, carloan.mixed_qualifying, carloan.refi_qualifying, carloan.refi_nested, carloan.allocated, carloan.refi_interest, carloan.mixed_interest, carloan.mixed_prorated, carloan.sc_interest, carloan.sc_mixed_prorated, carloan.sc_mixed, carloan.sc_refi, carloan.sc_allocated

## Capital Loss Carryover Worksheet—Lines 6 and 14

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clcw.zero | — | — | — | — | — | — | — |
| clcw.spouse_screen | — | — | — | — | — | — | — |
| clcw.prior_11 | — | — | — | — | — | — | — |
| clcw.prior_14 | — | — | — | — | — | — | — |
| clcw.prior_sd7 | — | — | — | — | — | — | — |
| clcw.prior_sd15 | — | — | — | — | — | — | — |
| clcw.prior_sd21 | — | — | — | via clcw.line2: 3 | — | E via clcw.line2 (OpenTaxSolver) | — |
| clcw.prior_16 | — | — | — | — | — | — | — |
| clcw.prior_loss | — | — | — | — | — | — | — |
| clcw.prior_limit | — | — | — | — | — | — | — |
| clcw.prior_limit_mfs | — | — | — | — | — | — | — |
| clcw.prior_floor | — | — | — | — | — | — | — |
| clcw.bad | — | — | — | — | — | — | 4 |
| clcw.applies | — | — | — | — | — | — | 4 |
| clcw.show_st | — | — | — | — | — | — | 2 (stage20.line21_at_floor, stage20.mut.line21_at_loss_negative_income) |
| clcw.show_lt | — | — | — | — | — | — | 3 |
| clcw.line1 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (238 nonzero), 0 excluded | 13 |
| clcw.line2 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (238 nonzero), 0 excluded | 19 |
| clcw.combined | — | — | — | — | — | — | — |
| clcw.line3 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (170 nonzero), 0 excluded | 12 |
| clcw.line4 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (170 nonzero), 0 excluded | 12 |
| clcw.st_loss | — | — | — | — | — | — | — |
| clcw.lt_loss | — | — | — | — | — | — | — |
| clcw.line5 | — | — | — | 6 | — | OpenTaxSolver: 196 compared (196 nonzero), 0 excluded | 12 |
| clcw.line6 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (85 nonzero), 0 excluded | 5 |
| clcw.line7 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (167 nonzero), 0 excluded | 7 |
| clcw.line8 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (187 nonzero), 0 excluded | 11 |
| clcw.line9 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (153 nonzero), 0 excluded | 5 |
| clcw.line10 | — | — | — | 4 | — | OpenTaxSolver below rule: 153 compared (42 nonzero), 0 excluded | 5 |
| clcw.line11 | — | — | — | 4 | — | OpenTaxSolver below rule: 153 compared (31 nonzero), 0 excluded | 5 |
| clcw.line12 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (51 nonzero), 0 excluded | 5 |
| clcw.line13 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (153 nonzero), 0 excluded | 6 |
| clcw.figures_notice | — | — | — | — | — | — | — |

Unasserted lines: clcw.zero, clcw.prior_16, clcw.prior_loss, clcw.prior_limit, clcw.prior_limit_mfs, clcw.prior_floor, clcw.combined, clcw.st_loss, clcw.lt_loss, clcw.figures_notice

## Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clcw_next_year.zero | — | — | — | — | — | — | — |
| clcw_next_year.show | — | — | — | — | — | — | — |
| clcw_next_year.show_st | — | — | — | — | — | — | — |
| clcw_next_year.show_lt | — | — | — | — | — | — | 1 (stage20.blind.r6) |
| clcw_next_year.line1 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line2 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.combined | — | — | — | — | — | — | — |
| clcw_next_year.line3 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line4 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line5 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line6 | — | — | — | 4 | — | — | — |
| clcw_next_year.line7 | — | — | — | 4 | — | — | — |
| clcw_next_year.line8 | — | — | — | 4 | — | — | 14 |
| clcw_next_year.line9 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line10 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line11 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line12 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw_next_year.line13 | — | — | — | 4 | — | — | 14 |
| clcw_next_year.decedent_notice | — | — | — | — | — | — | 1 (mutation.t2.mfj_sdtw_skip23) |
| clcw_next_year.no | — | — | — | — | — | — | — |
| clcw_next_year.not_joint | — | — | — | — | — | — | — |
| clcw_next_year.final_ask | — | — | — | — | — | — | 2 (bug0477.clcw26.final_return_long, bug0477.clcw26.not_final_return) |
| clcw_next_year.final_return | — | — | — | — | — | — | — |
| clcw_next_year.final_return_if_carryover | — | — | — | — | — | — | 1 (bug0477.clcw26.final_return_long) |
| clcw_next_year.carries | — | — | — | — | — | — | — |
| clcw_next_year.show_st_carry | — | — | — | — | — | — | 3 |
| clcw_next_year.show_lt_carry | — | — | — | — | — | — | 4 |
| clcw_next_year.final_notice | — | — | — | — | — | — | 4 |

Unasserted lines: clcw_next_year.zero, clcw_next_year.show, clcw_next_year.show_st, clcw_next_year.combined, clcw_next_year.no, clcw_next_year.not_joint, clcw_next_year.carries

## Form 2441, Part I — persons or organizations who provided the care, one entry per care provider

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dcprov.one | — | — | — | — | — | — | — |
| dcprov.tin_kind | — | — | — | — | — | — | — |
| dcprov.household | — | — | — | — | — | — | — |
| dcprov.paid | — | — | — | — | — | — | — |
| dcprov.related | — | — | — | — | — | — | — |
| dcprov.see_statement | — | — | — | 1 (classm.dcprov.1) | — | — | — |

Unasserted lines: dcprov.one

## Dependents — qualifying child and qualifying relative tests, per person listed

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dependent.relationship | — | — | — | — | — | — | — |
| dependent.age | — | — | — | — | — | — | — |
| dependent.student | — | — | — | — | — | — | — |
| dependent.disabled | — | — | — | — | — | — | — |
| dependent.months | — | — | — | — | — | — | — |
| dependent.self_support | — | — | — | — | — | — | — |
| dependent.joint_return | — | — | — | — | — | — | — |
| dependent.citizen | — | — | — | — | — | — | — |
| dependent.canada_mexico | — | — | — | — | — | — | — |
| dependent.married | — | — | — | — | — | — | — |
| dependent.tin | — | — | — | — | — | — | — |
| dependent.work_ssn | — | — | — | — | — | — | — |
| dependent.gross_income | — | — | — | — | — | — | — |
| dependent.supported | — | — | — | — | — | — | — |
| dependent.kidnapped | — | — | — | — | — | — | — |
| dependent.other_claimant | — | — | — | — | — | — | — |
| dependent.other_nontaxpayer | — | — | — | — | — | — | — |
| dependent.divorced_rule | — | — | — | — | — | — | — |
| dependent.multiple_support | — | — | — | — | — | — | — |
| dependent.parent_home_paid | — | — | — | — | — | — | — |
| dependent.born_died | — | — | — | — | — | — | — |
| dependent.placed | — | — | — | — | — | — | — |
| dependent.part_year_home | — | — | — | — | — | — | — |
| dependent.hoh_part_year | — | — | — | — | — | — | — |
| dependent.hoh_part_year_relative | — | — | — | — | — | — | — |
| dependent.born_died_or_placed | — | — | — | — | — | — | — |
| dependent.hoh_lived_half | — | — | — | — | — | — | — |
| dependent.dc_lived_half | — | — | — | — | — | — | 2 (stage8.hoh.adopted_part_year, stage15.mut.dc_parent_part_year_born_died_unanswered) |
| dependent.one | — | — | — | — | — | — | — |
| dependent.zero | — | — | — | — | — | — | — |
| dependent.qc_relationship | — | — | — | — | — | — | 22 |
| dependent.younger | — | — | — | — | — | — | 18 |
| dependent.us_half | — | — | — | — | — | — | — |
| dependent.eic_ssn | — | — | — | — | — | — | — |
| dependent.under_19 | — | — | — | — | — | — | — |
| dependent.under_24 | — | — | — | — | — | — | — |
| dependent.qc_age_younger | — | — | — | — | — | — | — |
| dependent.qc_age_19 | — | — | — | — | — | — | — |
| dependent.qc_age_student | — | — | — | — | — | — | — |
| dependent.qc_age | — | — | — | — | — | — | 19 |
| dependent.lived_half | — | — | — | — | — | — | 21 |
| dependent.kidnap_residency | — | — | — | — | — | — | — |
| dependent.no | — | — | — | — | — | — | — |
| dependent.qc_tests | — | — | — | — | — | — | — |
| dependent.qc_from_age | — | — | — | — | — | — | — |
| dependent.qc_from_support | — | — | — | — | — | — | — |
| dependent.qc_from_joint | — | — | — | — | — | — | — |
| dependent.qualifying_child | — | — | — | — | — | — | 35 |
| dependent.resident | — | — | — | — | — | — | 20 |
| dependent.qc_dependent_resident | — | — | — | — | — | — | — |
| dependent.filer_not_dependent | — | — | — | — | — | — | — |
| dependent.qc_dependent | — | — | — | — | — | — | 26 |
| dependent.qr_listed_relative | — | — | — | — | — | — | — |
| dependent.qr_household_member | — | — | — | — | — | — | 1 (xleak.spouse_relative.household_member_all_year_unanswered) |
| dependent.qr_other_relation | — | — | — | — | — | — | 1 (xleak.spouse_relative.other_all_year_lawful_unanswered) |
| dependent.qr_other_lawful | — | — | — | — | — | — | — |
| dependent.spouse_relative_joint | — | — | — | — | — | — | — |
| dependent.qr_relationship | — | — | — | — | — | — | 15 |
| dependent.spouse_relative | — | — | — | — | — | — | — |
| dependent.qr_all_year | — | — | — | — | — | — | — |
| dependent.lawful | — | — | — | — | — | — | — |
| dependent.qr_income | — | — | — | — | — | — | 7 |
| dependent.income_exception | — | — | — | — | — | — | 8 |
| dependent.qr_income_fails | — | — | — | — | — | — | — |
| dependent.qr_kidnapped | — | — | — | — | — | — | 1 (t091.kidnapped.age19) |
| dependent.qualifying_relative | — | — | — | — | — | — | 14 |
| dependent.qr_dependent_resident | — | — | — | — | — | — | — |
| dependent.qr_dependent | — | — | — | — | — | — | 10 |
| dependent.claimed_no_tin | — | — | — | — | — | — | 4 |
| dependent.claimed | — | — | — | — | — | — | 39 |
| dependent.under_ctc_age | — | — | — | — | — | — | 15 |
| dependent.ctc_from_tin | — | — | — | — | — | — | — |
| dependent.ctc_from_citizen | — | — | — | — | — | — | — |
| dependent.ctc_from_age | — | — | — | — | — | — | — |
| dependent.ctc_from_work_ssn | — | — | — | — | — | — | — |
| dependent.ctc_child | — | — | — | — | — | — | 29 |
| dependent.odc_person | — | — | — | — | — | — | 27 |
| dependent.ctc_per_child | — | — | — | — | — | — | — |
| dependent.ctc_amount | — | — | — | — | — | — | 28 |
| dependent.odc_per_dependent | — | — | — | — | — | — | — |
| dependent.odc_amount | — | — | — | — | — | — | 27 |
| dependent.actc_per_child | — | — | — | — | — | — | — |
| dependent.actc_amount | — | — | — | — | — | — | 24 |
| dependent.absence_no_return | — | — | — | — | — | — | — |
| dependent.hoh_test2_lived | — | — | — | — | — | — | 2 (stage8.mut.parent_lives_with_you_mexico_resident, stage8.mut.hoh_niece_17) |
| dependent.hoh_absence | — | — | — | — | — | — | 1 (t091.absence.test1_not_reached) |
| dependent.hoh_test2 | — | — | — | — | — | — | 29 |
| dependent.hoh_test1 | — | — | — | — | — | — | 26 |
| dependent.tiebreak_other | — | — | — | — | — | — | — |
| dependent.qc_tiebreak | — | — | — | — | — | — | 2 (mfsl4.spouse_not_claiming, mfsl4.settled_not_qc_spouse_nontaxpayer) |
| dependent.eic_child_tests | — | — | — | — | — | — | — |
| dependent.eic_child_from_age | — | — | — | — | — | — | — |
| dependent.eic_child_from_joint | — | — | — | — | — | — | — |
| dependent.eic_child | — | — | — | — | — | — | 7 |
| dependent.eic_tiebreak | — | — | — | — | — | — | 1 (mfsl4.spouse_not_claiming) |
| dependent.kidnap_eic_kidnapped | — | — | — | — | — | — | — |
| dependent.not_us_half | — | — | — | — | — | — | — |
| dependent.kidnap_eic | — | — | — | — | — | — | 1 (stage9.mut.kidnapped_household_child_other_claimant_unanswered) |
| dependent.eic_ssn_child | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.dc_child_all_year | — | — | — | — | — | — | 1 (stage15.mut.f2441_care_after_13_only) |
| dependent.dc_age13 | — | — | — | — | — | — | — |
| dependent.dc_under13 | — | — | — | — | — | — | — |
| dependent.dc_child | — | — | — | — | — | — | 1 (stage15.mut.f2441_care_after_13_only) |
| dependent.dc_incapable | — | — | — | — | — | — | — |
| dependent.dc_disabled_qp | — | — | — | — | — | — | — |
| dependent.dc_qp | — | — | — | — | — | — | 4 |
| dependent.dc_count | — | — | — | — | — | — | — |
| dependent.dc_paid | — | — | — | via dependent.dc_line2d: 5 | — | — | — |
| dependent.dc_line2d | — | — | — | 10 | — | — | — |
| dependent.dc_over12_care | — | — | — | — | — | — | — |
| dependent.dc_line2c | — | — | — | 10 | — | — | 4 |
| dependent.ptc_files | — | — | — | — | — | — | — |
| dependent.ptc_magi | — | — | — | — | — | — | — |
| dependent.ptc_magi_counted | — | — | — | — | — | — | — |
| dependent.edu | — | — | — | — | — | — | — |
| dependent.edu_1098t | — | — | — | — | — | — | — |
| dependent.edu_student | — | — | — | — | — | — | 1 (mutation.t4.dependent_edu_paid_no_disabled_care) |
| dependent.edu_student_claimed | — | — | — | — | — | — | — |
| dependent.edu_student_edu | — | — | — | — | — | — | — |
| dependent.edu_student_tin | — | — | — | — | — | — | — |
| dependent.edu_inst | — | — | — | — | — | — | — |
| dependent.edu_mat | — | — | — | — | — | — | — |
| dependent.edu_a_this_year | — | — | — | — | — | — | — |
| dependent.edu_a_next_year | — | — | — | — | — | — | — |
| dependent.edu_refunds | — | — | — | — | — | — | — |
| dependent.edu_adj_sum | — | — | — | — | — | — | — |
| dependent.edu_adj | — | — | — | — | — | — | — |
| dependent.edu_over | — | — | — | — | — | — | — |
| dependent.edu_has_adj | — | — | — | — | — | — | — |
| dependent.edu_over_if_adj | — | — | — | — | — | — | — |
| dependent.edu_over_refused | — | — | — | — | — | — | 3 |
| dependent.edu_line23 | — | — | — | — | — | — | 4 |
| dependent.edu_show24 | 1 (stage19.example.jack_kay) | — | — | — | — | — | 3 |
| dependent.edu_line24 | — | — | — | — | — | — | 3 |
| dependent.edu_show25 | 1 (stage19.example.jack_kay) | — | — | — | — | — | 2 (stage19.mut.classm_f5329_3_dependent_no_ein, stage19.mut.dependent_line24_no) |
| dependent.edu_line25 | — | — | — | — | — | — | 3 |
| dependent.edu_show26 | 1 (stage19.example.jack_kay) | — | — | — | — | — | 2 (stage19.mut.classm_f5329_3_dependent_no_ein, stage19.mut.dependent_line24_no) |
| dependent.edu_line26 | — | — | — | — | — | — | 2 (stage19.blind.e2, stage19.blind.e4) |
| dependent.edu_ein | — | — | — | — | — | — | — |
| dependent.edu_no | — | — | — | — | — | — | — |
| dependent.edu_aoc | — | — | — | — | — | — | 3 |
| dependent.edu_aoc23 | — | — | — | — | — | — | — |
| dependent.edu_aoc24 | — | — | — | — | — | — | — |
| dependent.edu_aoc25 | — | — | — | — | — | — | — |
| dependent.edu_aoc26 | — | — | — | — | — | — | — |
| dependent.edu_aoc_tin | — | — | — | — | — | — | — |
| dependent.edu_llc | — | — | — | — | — | — | 3 |
| dependent.edu_tin_issued | — | — | — | — | — | — | — |
| dependent.edu_llc_tin_refused | — | — | — | — | — | — | — |
| dependent.edu_line27 | 4 | — | — | — | — | — | 6 |
| dependent.edu_line28 | — | — | — | — | — | — | 3 |
| dependent.edu_line29 | — | — | — | — | — | — | 3 |
| dependent.edu_line30 | 3 | — | — | — | — | — | 5 |
| dependent.edu_line31 | — | — | — | — | — | — | 7 |
| dependent.under_7_months | — | — | — | — | — | — | — |
| dependent.under_19_kidnap | — | — | — | — | — | — | — |
| dependent.meets_tests | — | — | — | — | — | — | — |
| dependent.odc_from_tin | — | — | — | — | — | — | — |
| dependent.odc_from_citizen | — | — | — | — | — | — | — |
| dependent.odc_from_ctc | — | — | — | — | — | — | — |
| dependent.qr_from_child | — | — | — | — | — | — | — |
| dependent.qr_from_income | — | — | — | — | — | — | — |
| dependent.lived_all_year | — | — | — | — | — | — | — |
| dependent.lived_half_counted | — | — | — | — | — | — | — |
| dependent.under_7_counted | — | — | — | — | — | — | — |
| dependent.kidnapped_if_part_year | — | — | — | — | — | — | — |
| dependent.household_all_year | — | — | — | — | — | — | — |
| dependent.ever_married | — | — | — | — | — | — | — |
| dependent.joint_return_if_ever_married | — | — | — | — | — | — | — |
| dependent.own_money | — | — | — | — | — | — | — |
| dependent.self_support_if_own_money | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.parents_apart | — | — | — | — | — | — | — |
| dependent.divorced_rule_screen | — | — | — | — | — | — | — |
| dependent.divorced_rule_if_parents_apart | — | — | — | — | — | — | — |
| dependent.married_screen_qc | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.married_if_ever_married_qc | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.married_screen_qr | — | — | — | — | — | — | — |
| dependent.married_if_ever_married_qr | — | — | — | — | — | — | — |
| dependent.married_screen_eic | — | — | — | — | — | — | — |
| dependent.married_if_ever_married_eic | — | — | — | — | — | — | — |
| dependent.qc_tiebreak_from_age | — | — | — | — | — | — | — |
| dependent.qc_tiebreak_claimant | — | — | — | — | — | — | — |
| dependent.qc_tiebreak_not_child | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.other_is_taxpayer | — | — | — | — | — | — | — |
| dependent.self_support_view | — | — | — | — | — | — | — |
| dependent.self_support_view_over | — | — | — | — | — | — | — |
| dependent.self_support_by_view | — | — | — | — | — | — | — |
| dependent.supported_view | — | — | — | — | — | — | — |
| dependent.supported_view_over | — | — | — | — | — | — | — |
| dependent.supported_by_view | — | — | — | — | — | — | — |
| dependent.citizen_ssn | — | — | — | — | — | — | — |
| dependent.citizen_known | — | — | — | — | — | — | — |
| dependent.tin_known | — | — | — | — | — | — | — |
| dependent.work_ssn_known | — | — | — | — | — | — | — |
| dependent.eic_ssn_known | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.married_known | — | — | — | — | — | — | 1 (mutation.m2.dependent.plain_answers) |
| dependent.qc_tiebreak_other_age | — | — | — | — | — | — | — |
| dependent.other_only_spouse | — | — | — | — | — | — | — |
| dependent.other_only_spouse_if_mfs | — | — | — | — | — | — | — |
| dependent.spouse_claims | — | — | — | — | — | — | — |
| dependent.spouse_claims_if_only_spouse | — | — | — | — | — | — | — |
| dependent.filer_parent | — | — | — | — | — | — | — |
| dependent.filer_parent_if_child | — | — | — | — | — | — | — |
| dependent.spouse_settles | — | — | — | — | — | — | 6 |
| dependent.spouse_settles_unclaimed | — | — | — | — | — | — | — |
| dependent.tiebreak_unsettled | — | — | — | — | — | — | — |
| dependent.tiebreak_settled | — | — | — | — | — | — | 2 (mfsl4.settled_not_qc_spouse_taxpayer, mfsl4.settled_not_qc_spouse_nontaxpayer) |
| dependent.tiebreak_spouse_or_other | — | — | — | — | — | — | — |
| dependent.eic_tiebreak_unsettled | — | — | — | — | — | — | — |

Unasserted lines: dependent.hoh_part_year, dependent.hoh_part_year_relative, dependent.born_died_or_placed, dependent.hoh_lived_half, dependent.one, dependent.zero, dependent.under_19, dependent.under_24, dependent.qc_age_younger, dependent.qc_age_19, dependent.qc_age_student, dependent.kidnap_residency, dependent.no, dependent.qc_tests, dependent.qc_from_age, dependent.qc_from_support, dependent.qc_from_joint, dependent.qc_dependent_resident, dependent.filer_not_dependent, dependent.qr_listed_relative, dependent.qr_other_lawful, dependent.spouse_relative_joint, dependent.qr_income_fails, dependent.qr_dependent_resident, dependent.ctc_from_tin, dependent.ctc_from_citizen, dependent.ctc_from_age, dependent.ctc_from_work_ssn, dependent.ctc_per_child, dependent.odc_per_dependent, dependent.actc_per_child, dependent.tiebreak_other, dependent.eic_child_tests, dependent.eic_child_from_age, dependent.eic_child_from_joint, dependent.kidnap_eic_kidnapped, dependent.not_us_half, dependent.dc_age13, dependent.dc_disabled_qp, dependent.dc_count, dependent.ptc_magi_counted, dependent.edu_student_claimed, dependent.edu_student_edu, dependent.edu_student_tin, dependent.edu_adj_sum, dependent.edu_adj, dependent.edu_has_adj, dependent.edu_over_if_adj, dependent.edu_no, dependent.edu_aoc23, dependent.edu_aoc24, dependent.edu_aoc25, dependent.edu_aoc26, dependent.edu_aoc_tin, dependent.edu_llc_tin_refused, dependent.under_7_months, dependent.under_19_kidnap, dependent.meets_tests, dependent.odc_from_tin, dependent.odc_from_citizen, dependent.odc_from_ctc, dependent.qr_from_child, dependent.qr_from_income, dependent.lived_half_counted, dependent.under_7_counted, dependent.kidnapped_if_part_year, dependent.household_all_year, dependent.joint_return_if_ever_married, dependent.divorced_rule_screen, dependent.divorced_rule_if_parents_apart, dependent.married_screen_qr, dependent.married_if_ever_married_qr, dependent.married_screen_eic, dependent.married_if_ever_married_eic, dependent.qc_tiebreak_from_age, dependent.qc_tiebreak_claimant, dependent.other_is_taxpayer, dependent.self_support_view_over, dependent.self_support_by_view, dependent.supported_view_over, dependent.supported_by_view, dependent.citizen_known, dependent.tin_known, dependent.work_ssn_known, dependent.qc_tiebreak_other_age, dependent.other_only_spouse_if_mfs, dependent.spouse_claims_if_only_spouse, dependent.filer_parent_if_child, dependent.spouse_settles_unclaimed, dependent.tiebreak_unsettled, dependent.tiebreak_spouse_or_other, dependent.eic_tiebreak_unsettled

## Form 1099-DIV — distribution components and scope screening

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| div.box2b | — | — | — | — | — | — | — |
| div.box2c | — | — | — | — | — | — | — |
| div.box2d | — | — | — | — | — | — | — |
| div.box2e | — | — | — | — | — | — | — |
| div.box2f | — | — | — | — | — | — | — |
| div.box3 | — | — | — | — | — | — | — |
| div.box9 | — | — | — | — | — | — | — |
| div.box10 | — | — | — | — | — | — | — |
| div.box12 | — | — | — | — | — | — | — |
| div.box13 | — | — | — | — | — | — | — |
| div.basis_reconciled | — | — | — | — | — | — | — |
| div.box1a | — | — | — | — | — | — | — |
| div.box1b | — | — | — | — | — | — | 1 (mutation.div.capital_gain_distributions_only) |
| div.box2a | — | — | — | — | — | — | — |
| div.box5 | — | — | — | — | — | — | 1 (mutation.div.capital_gain_distributions_only) |
| div.section1202 | — | — | — | — | — | — | 1 (mutation.div.ordinary_dividends_only) |
| div.amt | — | — | — | — | — | — | — |
| div.unsupported | — | — | — | — | — | — | 3 |
| div.bad_special | — | — | — | — | — | — | — |
| div.screen | — | — | — | via u1250.line10: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek); via u1250.line12: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | — | 3 |
| div.bad_components | — | — | — | — | — | — | — |
| div.special_total | — | — | — | — | — | — | 1 (mutation.div.ordinary_dividends_only) |
| div.any | — | — | — | — | — | — | — |
| div.has_ordinary | — | — | — | — | — | — | — |
| div.has_capital_gain | — | — | — | — | — | — | — |
| div.has_return_of_capital | — | — | — | — | — | — | 1 (mutation.div.box3_zero_basis_unread) |
| div.zero | — | — | — | — | — | — | — |
| div.no | — | — | — | — | — | — | — |
| div.other_boxes | — | — | — | — | — | — | — |
| div.other_boxes_if_dividends | — | — | — | — | — | — | — |
| div.capital_gain_boxes | — | — | — | — | — | — | — |
| div.ordinary_boxes | — | — | — | — | — | — | — |
| div.box2b_if_capital_gain | — | — | — | via u1250.line11: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | — | — |
| div.box2c_if_capital_gain | — | — | — | — | — | — | — |
| div.box2d_if_capital_gain | — | — | — | via g28.line4: 1 (classm.g28.2.deepseek) | — | — | — |
| div.box2f_if_capital_gain | — | — | — | — | — | — | — |
| div.box2e_if_ordinary | — | — | — | — | — | — | — |
| div.box3_if_dividends | — | — | — | — | — | — | — |
| div.box9_if_dividends | — | — | — | — | — | — | — |
| div.box10_if_dividends | — | — | — | — | — | — | — |
| div.box12_if_dividends | — | — | — | — | — | — | — |
| div.box13_if_dividends | — | — | — | — | — | — | — |
| div.basis_reconciled_if_return_of_capital | — | — | — | — | — | — | 1 (mutation.div.box3_zero_basis_unread) |

Unasserted lines: div.box1a, div.box2a, div.amt, div.bad_special, div.bad_components, div.has_ordinary, div.has_capital_gain, div.zero, div.no, div.other_boxes_if_dividends, div.capital_gain_boxes, div.ordinary_boxes, div.box2c_if_capital_gain, div.box2f_if_capital_gain, div.box2e_if_ordinary, div.box3_if_dividends, div.box9_if_dividends, div.box10_if_dividends, div.box12_if_dividends, div.box13_if_dividends

## Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eic.lived_with_relative | — | — | — | — | — | — | — |
| eic.qc_of_another | — | — | — | — | — | — | — |
| eic.qc_of_another_if_lived | — | — | — | — | — | — | — |
| eic.age_range_count | — | — | — | — | — | — | — |
| eic.died_this_year | — | — | — | — | — | — | — |
| eic.age_range | — | — | — | — | — | — | 1 (stage13.eic_spouse_in_age_range) |
| eic.us_home | — | — | — | — | — | — | — |
| eic.zero | — | — | — | via eic.step5_line4: 5 | — | — | — |
| eic.qc_count | — | — | — | — | — | — | 1 (stage21.f1.where_kidnapped_withheld_eic) |
| eic.ssn_count | — | — | — | — | — | — | 6 |
| eic.has_qc | — | — | — | — | — | — | 4 |
| eic.status_mfs | — | — | — | — | — | — | — |
| eic.married_rules | — | — | — | — | — | — | 1 (t264.eic.mfs_no_child_step4) |
| eic.top_limit | — | — | — | — | — | — | — |
| eic.below_top | — | — | — | — | — | — | — |
| eic.limit0_other | — | — | — | — | — | — | — |
| eic.limit1_other | — | — | — | — | — | — | — |
| eic.limit2_other | — | — | — | — | — | — | — |
| eic.limit3_other | — | — | — | — | — | — | — |
| eic.limit0_joint | — | — | — | — | — | — | — |
| eic.limit1_joint | — | — | — | — | — | — | — |
| eic.limit2_joint | — | — | — | — | — | — | — |
| eic.limit3_joint | — | — | — | — | — | — | — |
| eic.limit_other | — | — | — | — | — | — | — |
| eic.limit_joint | — | — | — | — | — | — | — |
| eic.limit | — | — | — | — | — | — | 1 (stage21.choose.eic_limit_status_unanswered) |
| eic.step1_income | — | — | — | — | — | — | — |
| eic.step1_ssn | — | — | — | — | — | — | 2 (audit.eic.filer_eic_ssn_without_work_ssn, audit.eic.filer_without_eic_ssn) |
| eic.step1_foreign | — | — | — | — | — | — | — |
| eic.step1_resident | — | — | — | — | — | — | — |
| eic.gain_7a | — | — | — | — | — | — | 1 (stage9.eic.capital_gain_in_investment_income) |
| eic.investment_income | — | — | — | — | — | — | — |
| eic.step2_income | — | — | — | — | — | — | 3 |
| eic.step2_other | — | — | — | — | — | — | 1 (t264.eic.step2_schedule1) |
| eic.same_home | — | — | — | — | — | — | — |
| eic.mfs_same_home | — | — | — | — | — | — | — |
| eic.same_principal_home | — | — | — | — | — | — | — |
| eic.legally_separated | — | — | — | — | — | — | — |
| eic.step3_married | — | — | — | — | — | — | 3 |
| eic.status_mfj | — | — | — | — | — | — | — |
| eic.step3_not_joint | — | — | — | — | — | — | — |
| eic.not_qc_of_another | — | — | — | — | — | — | — |
| eic.step3 | — | — | — | — | — | — | 5 |
| eic.step4_age | — | — | — | — | — | — | — |
| eic.step4_home | — | — | — | — | — | — | — |
| eic.step4_dependent | — | — | — | — | — | — | — |
| eic.step4 | — | — | — | — | — | — | 4 |
| eic.step34 | — | — | — | — | — | — | — |
| eic.reached_step5 | 1 (stage19.example.jane.include_all) | — | — | — | — | — | 1 (stage9.eic.wsb_not_reached) |
| eic.step5_line1 | — | — | — | 14 | — | — | 1 (stage9.eic.refuse.clergy_schedule1.step5) |
| eic.step5_line2 | — | — | — | 14 | — | — | 6 |
| eic.step5_line3 | — | — | — | 14 | — | — | — |
| eic.step5_line4 | — | — | — | 14 | — | — | 1 (stage9.eic.refuse.other_income) |
| eic.earned_income | — | — | — | 14 | — | PE: 1400 compared (1400 nonzero), 300 excluded; TC: 1400 compared (1400 nonzero), 300 excluded | 1 (stage9.eic.no_schedule_c.earned_over_limit) |
| eic.sc_count | — | — | — | — | — | — | — |
| eic.self_employed | — | — | — | — | — | — | — |
| eic.wsb_se | — | — | — | — | — | — | — |
| eic.show_wsb4b | 1 (stage19.example.jane.include_all) | — | — | — | — | — | 2 (stage9.eic.wsb_not_reached, stage14.sc.basic) |
| eic.wsb_4b | — | — | — | 4 | — | — | 11 |
| eic.show_wsb6 | — | — | — | — | — | — | 2 (stage9.eic.wsb_not_reached, stage14.eic.wsb_line5_stop_27c) |
| eic.wsb_6 | — | — | — | 3 | — | — | 1 (stage14.eic.wsb_stop_27c) |
| eic.earned_for_limit | — | — | — | — | — | — | — |
| eic.step5_income | — | — | — | — | — | — | — |
| eic.no | — | — | — | — | — | — | — |
| eic.eligible | — | — | — | — | — | — | 22 |
| eic.line1 | — | — | — | 12 | — | PE: 1700 compared (1699 nonzero), 0 excluded; TC: 1700 compared (1699 nonzero), 0 excluded | 15 |
| eic.line1_in_table | — | — | — | — | — | — | — |
| eic.line1_table0 | — | — | — | — | — | — | — |
| eic.line1_table1 | — | — | — | — | — | — | — |
| eic.line1_table2 | — | — | — | — | — | — | — |
| eic.line1_table3 | — | — | — | — | — | — | — |
| eic.line1_table | — | — | — | — | — | — | — |
| eic.line2 | — | — | — | 12 | — | — | 30 |
| eic.show3 | 1 (stage19.example.jack_kay) | — | — | — | — | — | 1 (stage9.eic.no_earned_income) |
| eic.line3 | — | — | — | 9 | — | — | — |
| eic.line4 | — | — | — | 9 | — | — | 9 |
| eic.threshold_other | — | — | — | — | — | — | — |
| eic.threshold_joint | — | — | — | — | — | — | — |
| eic.line5_threshold | — | — | — | — | — | — | 1 (stage21.choose.eic_limit_status_unanswered) |
| eic.threshold0_other | — | — | — | — | — | — | — |
| eic.threshold1_other | — | — | — | — | — | — | — |
| eic.threshold0_joint | — | — | — | — | — | — | — |
| eic.threshold1_joint | — | — | — | — | — | — | — |
| eic.line5_blank | — | — | — | — | — | — | 3 |
| eic.line3_table0 | — | — | — | — | — | — | — |
| eic.line3_table1 | — | — | — | — | — | — | — |
| eic.line3_table2 | — | — | — | — | — | — | — |
| eic.line3_table3 | — | — | — | — | — | — | — |
| eic.show5 | 1 (stage19.example.jane.include_all) | — | — | — | — | — | 3 |
| eic.line5 | — | — | — | 2 (classm.eic.8.deepseek, classm.eic.1) | — | — | 7 |
| eic.smaller | — | — | — | — | — | — | — |
| eic.after_line4 | — | — | — | — | — | — | — |
| eic.line6 | — | — | — | 11 | — | — | 23 |
| eic.credit | — | — | — | via f1040.line27a: 6 | — | E via f1040.line27a (PE, TC) | 4 |
| eic.reached_step3 | — | — | — | — | — | — | — |
| eic.check_27c | — | — | — | via f1040.line27c: 6 | — | — | 8 |
| eic.wsb_4b_positive | — | — | — | — | — | — | 1 (stage14.sehi.profit_limit) |
| eic.wsb_line5_stop | — | — | — | — | — | — | 1 (stage14.eic.wsb_line5_stop_27c) |
| eic.separated_box | — | — | — | via f1040.separated_spouses: 6 | — | — | 1 (stage9.mut.eic_married_hoh_qc_of_another) |
| eic.clergy | — | — | — | via f1040.line27b: 6 | — | — | — |
| eic.from_step1_income | — | — | — | — | — | — | — |
| eic.from_step1_ssn | — | — | — | — | — | — | — |
| eic.from_step1_foreign | — | — | — | — | — | — | — |
| eic.from_step1_resident | — | — | — | — | — | — | — |
| eic.from_step2_income | — | — | — | — | — | — | — |
| eic.line2_zero | — | — | — | — | — | — | — |
| eic.worksheet_a_stop | — | — | — | — | — | — | — |

Unasserted lines: eic.qc_of_another_if_lived, eic.age_range_count, eic.status_mfs, eic.top_limit, eic.below_top, eic.limit0_other, eic.limit1_other, eic.limit2_other, eic.limit3_other, eic.limit0_joint, eic.limit1_joint, eic.limit2_joint, eic.limit3_joint, eic.limit_other, eic.limit_joint, eic.step1_income, eic.step1_foreign, eic.step1_resident, eic.investment_income, eic.mfs_same_home, eic.same_principal_home, eic.status_mfj, eic.step3_not_joint, eic.not_qc_of_another, eic.step4_age, eic.step4_home, eic.step4_dependent, eic.step34, eic.sc_count, eic.self_employed, eic.wsb_se, eic.earned_for_limit, eic.step5_income, eic.no, eic.line1_in_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line1_table, eic.threshold_other, eic.threshold_joint, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.smaller, eic.after_line4, eic.reached_step3, eic.from_step1_income, eic.from_step1_ssn, eic.from_step1_foreign, eic.from_step1_resident, eic.from_step2_income, eic.line2_zero, eic.worksheet_a_stop

## Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.status | 1 (example.official) | — | — | — | — | — | 58 |
| f1040.digital_assets | — | — | — | — | — | — | — |
| f1040.digital_sales | — | — | — | — | — | — | 1 (f1040.digital_assets.no_with_stock) |
| f1040.digital_conflict | — | — | — | — | — | — | 2 (f1040.digital_assets.yes_no_sales, f1040.digital_assets.no_with_stock) |
| f1040.line1a | — | — | — | 14 | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 41 |
| f1040.line1b | — | — | — | 8 | — | — | 1 (x2pay.household.w5) |
| f1040.line1c | — | — | — | 8 | — | — | 3 |
| f1040.line1d | — | — | — | 8 | — | — | 7 |
| f1040.line1e | — | — | — | 14 | — | — | 19 |
| f1040.line1g | — | — | — | 8 | — | — | 1 (x2pay.f8919.w3) |
| f1040.line1h | — | — | — | 8 | — | — | 2 (x2pay.strike.w8, x2pay.disability.w6) |
| f1040.line1z | — | — | — | 14; via eic.step5_line1: 5 | — | OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 49 |
| f1040.tax_exempt_interest | — | — | — | — | — | — | — |
| f1040.line2a | — | — | — | 14 | — | — | 1 (stage10.ss.exempt_interest_dividends) |
| f1040.line2b | — | — | — | 14 | — | — | 12 |
| f1040.line3b | — | — | — | 14 | — | — | 10 |
| f1040.line3a | 1 (example.official) | — | — | — | — | — | 67 |
| f1040.line4a | — | — | — | 14 | — | — | 8 |
| f1040.line4b | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 14 | — | — | 20 |
| f1040.ira_rollovers | — | — | — | — | — | — | — |
| f1040.line4c_rollover | — | — | — | 14 | — | — | 7 |
| f1040.line5a | — | — | — | 14 | — | — | 17 |
| f1040.line5b | — | — | — | 14 | — | — | 33 |
| f1040.plan_rollovers | — | — | — | — | — | — | — |
| f1040.line5c_rollover | — | — | — | 14 | — | — | 6 |
| f1040.line6a | — | — | — | 14 | — | — | 2 (stage16.ira.i10, stage10.ss.top) |
| f1040.line6b | — | — | — | 14 | — | PE: 1666 compared (477 nonzero), 19 excluded; TC: 1370 compared (418 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (477 nonzero), 111 excluded; UsTaxes: 1166 compared (304 nonzero), 534 excluded | 24 |
| f1040.line6c | — | — | — | 14 | — | — | 1 (stage10.refuse.lump_sum) |
| f1040.line6d | — | — | — | 14 | — | — | 5 |
| f1040.line7a | 8 | — | — | 14 | — | OpenTaxSolver: 1700 compared (1404 nonzero), 0 excluded; UsTaxes: 1400 compared (1152 nonzero), 300 excluded | 173 |
| f1040.line8 | — | — | — | 14 | — | OpenTaxSolver: 1700 compared (576 nonzero), 0 excluded; UsTaxes below rule: 1400 compared (280 nonzero), 300 excluded | 60 |
| f1040.line9 | — | — | — | 14 | — | OpenTaxSolver: 1589 compared (1589 nonzero), 111 excluded; UsTaxes: 1166 compared (1166 nonzero), 534 excluded; E via sli.line2 (UsTaxes) | 38 |
| f1040.line10 | — | — | — | 14 | — | PE: 1640 compared (975 nonzero), 19 excluded; TC: 1370 compared (771 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (955 nonzero), 111 excluded; UsTaxes: 1166 compared (600 nonzero), 534 excluded | 48 |
| f1040.line11a | — | — | — | 14; via eic.line3 → f1040.line11b: 4; via f1040.line11b: 6; via f2441.line7: 3; via f8863.line3 → f1040.line11b: 4; via f8863.line14 → f1040.line11b: 1 (classm.f8863.4.deepseek); via f8880.line8: 3; via f8960.line13 → sa.agi → f1040.line11b: 3; via s8812.line1: 4 | — | UsTaxes: 1166 compared (1166 nonzero), 534 excluded; E via f1040.line11b (PE, TC, OpenTaxSolver, UsTaxes); E via f2441.line7 (OpenTaxSolver) | 204 |
| f1040.line11b | 8 | — | — | 14 | — | PE: 1640 compared (1640 nonzero), 19 excluded; TC: 1370 compared (1370 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (1589 nonzero), 111 excluded; UsTaxes: 1166 compared (1166 nonzero), 534 excluded | 62 |
| f1040.line12b | — | — | — | 8 | — | — | 2 (mfs.m1.basic, mfs.m2.spouse_itemizes) |
| f1040.line12e | — | — | — | 14 | — | OpenTaxSolver: 1476 compared (1476 nonzero), 224 excluded; UsTaxes: 1070 compared (1070 nonzero), 630 excluded | 103 |
| f1040.line13a | — | — | — | 14 | — | PE: 1490 compared (380 nonzero), 139 excluded; TC below rule: 1039 compared (135 nonzero), 643 excluded; OpenTaxSolver: 387 compared (329 nonzero), 130 excluded; UsTaxes below rule: 828 compared (0 nonzero), 872 excluded | 13 |
| f1040.line13b | — | — | — | 14 | — | PE: 1536 compared (514 nonzero), 143 excluded; TC: 1370 compared (492 nonzero), 330 excluded; OpenTaxSolver: 1437 compared (447 nonzero), 263 excluded; UsTaxes below rule: 828 compared (252 nonzero), 872 excluded | 19 |
| f1040.line14 | — | — | — | 14 | — | OpenTaxSolver: 1235 compared (1235 nonzero), 465 excluded; UsTaxes: 828 compared (828 nonzero), 872 excluded | 28 |
| f1040.line15 | 3 | — | — | 14 | — | PE: 1384 compared (1227 nonzero), 256 excluded; TC: 902 compared (902 nonzero), 798 excluded; OpenTaxSolver: 1235 compared (1096 nonzero), 465 excluded; UsTaxes: 828 compared (733 nonzero), 872 excluded; E via qdcg.line1 (OpenTaxSolver, UsTaxes); E via sdtw.line1 (OpenTaxSolver) | 185 |
| f1040.gate.qdcg_applies | 1 (example.official) | — | — | — | — | — | 65 |
| f1040.gate.sdtw | — | — | — | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| f1040.line16 | 8 | — | — | 14 | — | PE: 1342 compared (1164 nonzero), 298 excluded; TC: 911 compared (788 nonzero), 772 excluded; OpenTaxSolver: 1075 compared (929 nonzero), 625 excluded; UsTaxes below rule: 725 compared (627 nonzero), 975 excluded | 197 |
| f1040.line17 | — | — | — | 14 | — | OpenTaxSolver below rule: 1431 compared (0 nonzero), 238 excluded; UsTaxes below rule: 690 compared (17 nonzero), 1010 excluded | 11 |
| f1040.line18 | — | — | — | 14; via f2441.clw1: 3; via f8863.clw4: 3; via f8880.clw1: 2 (classm.f8880.3.deepseek, classm.f8880.4.deepseek); via s8812.clw_a1: 2 (classm.s8812.1.deepseek, classm.s8812.3.deepseek) | — | OpenTaxSolver: 993 compared (858 nonzero), 707 excluded; UsTaxes below rule: 690 compared (601 nonzero), 1010 excluded | 153 |
| f1040.line19 | — | — | — | 14 | — | PE: 872 compared (374 nonzero), 788 excluded; TC below rule: 654 compared (338 nonzero), 1046 excluded; OpenTaxSolver below rule: 359 compared (297 nonzero), 611 excluded; UsTaxes below rule: 378 compared (152 nonzero), 1322 excluded | 96 |
| f1040.line20 | — | — | — | 14 | — | TC: 852 compared (429 nonzero), 840 excluded; OpenTaxSolver below rule: 632 compared (210 nonzero), 1068 excluded; UsTaxes below rule: 378 compared (91 nonzero), 1322 excluded | 9 |
| f1040.line21 | — | — | — | 14 | — | OpenTaxSolver below rule: 632 compared (363 nonzero), 1068 excluded; UsTaxes below rule: 378 compared (201 nonzero), 1322 excluded | 10 |
| f1040.line22 | 8 | — | — | 14 | — | OpenTaxSolver below rule: 632 compared (462 nonzero), 1068 excluded; UsTaxes below rule: 378 compared (318 nonzero), 1322 excluded | 32 |
| f1040.line23 | — | — | — | 14 | — | OpenTaxSolver: 1264 compared (319 nonzero), 436 excluded; UsTaxes below rule: 935 compared (122 nonzero), 765 excluded | 33 |
| f1040.line24 | 3 | — | — | 14 | — | TC below rule: 729 compared (521 nonzero), 956 excluded; OpenTaxSolver below rule: 587 compared (443 nonzero), 1113 excluded; UsTaxes below rule: 335 compared (278 nonzero), 1365 excluded | 34 |
| f1040.line25a | — | — | — | 14 | — | UsTaxes: 1330 compared (1330 nonzero), 370 excluded | 9 |
| f1040.withheld_other_any | — | — | — | — | — | — | — |
| f1040.line25b | — | — | — | — | — | — | 9 |
| f1040.line25b_if_withheld_other | — | — | — | — | — | — | 1 (mutation.m3.f1040.withholding_25b_25c) |
| f1040.line25c_other | — | — | — | — | — | — | — |
| f1040.line25c_other_if_withheld_other | — | — | — | — | — | — | — |
| f1040.line25c | — | — | — | 14 | — | — | 12 |
| f1040.line25d | — | — | — | 14 | — | OpenTaxSolver: 1567 compared (1567 nonzero), 133 excluded; UsTaxes: 1330 compared (1330 nonzero), 370 excluded | 10 |
| f1040.estimated_any | — | — | — | — | — | — | — |
| f1040.line26 | — | — | — | — | — | — | 9 |
| f1040.line27a | 5 | — | — | 14 | — | PE: 1511 compared (250 nonzero), 150 excluded; TC: 1260 compared (215 nonzero), 440 excluded; UsTaxes below rule: 876 compared (0 nonzero), 824 excluded | 109 |
| f1040.line27b | — | — | — | 14 | — | — | 2 (stage9.eic.no_child.4000, stage9.eic.refuse.clergy_schedule1) |
| f1040.line27c | — | — | — | 14 | — | — | 23 |
| f1040.separated_spouses | — | — | — | 14 | — | — | 8 |
| f1040.line28 | 4 | — | — | 14 | — | PE: 883 compared (194 nonzero), 788 excluded; TC below rule: 654 compared (88 nonzero), 1046 excluded; OpenTaxSolver below rule: 233 compared (38 nonzero), 737 excluded; UsTaxes below rule: 247 compared (8 nonzero), 1453 excluded | 40 |
| f1040.line28_box | — | — | — | 14 | — | — | — |
| f1040.line29 | 10 | — | — | 14 | — | PE: 1529 compared (86 nonzero), 164 excluded; TC: 1258 compared (81 nonzero), 442 excluded; UsTaxes: 132 compared (64 nonzero), 80 excluded | 27 |
| f1040.line30 | — | — | — | 12 | — | — | 16 |
| f1040.line31 | — | — | — | 14 | — | — | 38 |
| f1040.line32 | — | — | — | 14 | — | OpenTaxSolver below rule: 476 compared (38 nonzero), 1224 excluded; UsTaxes below rule: 247 compared (26 nonzero), 1453 excluded | 10 |
| f1040.line26_if_estimated | — | — | — | — | — | — | — |
| f1040.line33 | 5 | — | — | 14 | — | OpenTaxSolver below rule: 476 compared (476 nonzero), 1224 excluded; UsTaxes below rule: 245 compared (245 nonzero), 1455 excluded | 25 |
| f1040.line34 | 5 | — | — | 10 | — | OpenTaxSolver below rule: 438 compared (310 nonzero), 1262 excluded; UsTaxes below rule: 221 compared (153 nonzero), 1479 excluded | 52 |
| f1040.line35a | — | — | — | — | — | — | 9 |
| f1040.line36 | — | — | — | — | — | — | 9 |
| f1040.line37 | — | — | — | 10 | — | OpenTaxSolver below rule: 438 compared (128 nonzero), 1262 excluded; UsTaxes below rule: 221 compared (68 nonzero), 1479 excluded | 64 |
| f1040.line3a_if_ordinary | — | — | — | via f4952.line4b: 4 | — | E via qdcg.line2 (OpenTaxSolver) | — |

Unasserted lines: f1040.ira_rollovers, f1040.plan_rollovers, f1040.line25c_other_if_withheld_other, f1040.line26_if_estimated

## Form 1095-A, Health Insurance Marketplace Statement (one entry per form)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1095a.one | — | — | — | — | — | — | — |
| f1095a.void | — | — | — | — | — | — | — |
| f1095a.months | — | — | — | — | — | — | — |
| f1095a.no | — | — | — | — | — | — | — |
| f1095a.same_months | — | — | — | — | — | — | — |
| f1095a.b_blank | — | — | — | — | — | — | — |
| f1095a.b_changed | — | — | — | — | — | — | — |
| f1095a.b_wrong | — | — | — | 5 | — | — | — |
| f1095a.b_doubt | — | — | — | — | — | — | — |
| f1095a.no_aptc | — | — | — | 2 (classm.f1095a.1, classm.f1095a.2) | — | — | — |
| f1095a.b_check | — | — | — | 4 | — | — | — |
| f1095a.b_wrong_asked | — | — | — | 5 | — | — | — |
| f1095a.b_fixed_same | — | — | — | — | — | — | — |
| f1095a.b_fixed_same_if_b_wrong | — | — | — | 3 | — | — | — |
| f1095a.uniform | — | — | — | 4 | — | — | 3 |
| f1095a.months_uniform | — | — | — | 2 (classm.f1095a.1, classm.f1095a.3) | — | — | — |
| f1095a.annual_ok | — | — | — | 3 | — | — | — |
| f1095a.mo_a | — | — | — | — | — | — | — |
| f1095a.mo_b | — | — | — | — | — | — | — |
| f1095a.c_total | — | — | — | — | — | — | — |
| f1095a.in_a_jan | — | — | — | — | — | — | — |
| f1095a.in_a_feb | — | — | — | — | — | — | — |
| f1095a.in_a_mar | — | — | — | — | — | — | — |
| f1095a.in_a_apr | — | — | — | — | — | — | — |
| f1095a.in_a_may | — | — | — | — | — | — | — |
| f1095a.in_a_jun | — | — | — | — | — | — | — |
| f1095a.in_a_jul | — | — | — | — | — | — | — |
| f1095a.in_a_aug | — | — | — | — | — | — | — |
| f1095a.in_a_sep | — | — | — | — | — | — | — |
| f1095a.in_a_oct | — | — | — | — | — | — | — |
| f1095a.in_a_nov | — | — | — | — | — | — | — |
| f1095a.in_a_dec | — | — | — | — | — | — | — |
| f1095a.in_b_jan | — | — | — | — | — | — | — |
| f1095a.in_b_feb | — | — | — | — | — | — | — |
| f1095a.in_b_mar | — | — | — | — | — | — | — |
| f1095a.in_b_apr | — | — | — | — | — | — | — |
| f1095a.in_b_may | — | — | — | — | — | — | — |
| f1095a.in_b_jun | — | — | — | — | — | — | — |
| f1095a.in_b_jul | — | — | — | — | — | — | — |
| f1095a.in_b_aug | — | — | — | — | — | — | — |
| f1095a.in_b_sep | — | — | — | — | — | — | — |
| f1095a.in_b_oct | — | — | — | — | — | — | — |
| f1095a.in_b_nov | — | — | — | — | — | — | — |
| f1095a.in_b_dec | — | — | — | — | — | — | — |
| f1095a.in_c_jan | — | — | — | — | — | — | — |
| f1095a.in_c_feb | — | — | — | — | — | — | — |
| f1095a.in_c_mar | — | — | — | — | — | — | — |
| f1095a.in_c_apr | — | — | — | — | — | — | — |
| f1095a.in_c_may | — | — | — | — | — | — | — |
| f1095a.in_c_jun | — | — | — | — | — | — | — |
| f1095a.in_c_jul | — | — | — | — | — | — | — |
| f1095a.in_c_aug | — | — | — | — | — | — | — |
| f1095a.in_c_sep | — | — | — | — | — | — | — |
| f1095a.in_c_oct | — | — | — | — | — | — | — |
| f1095a.in_c_nov | — | — | — | — | — | — | — |
| f1095a.in_c_dec | — | — | — | — | — | — | — |
| f1095a.a_jan | — | — | — | 7 | — | — | — |
| f1095a.a_feb | — | — | — | 7 | — | — | — |
| f1095a.a_mar | — | — | — | 7 | — | — | — |
| f1095a.a_apr | — | — | — | 7 | — | — | — |
| f1095a.a_may | — | — | — | 7 | — | — | — |
| f1095a.a_jun | — | — | — | 7 | — | — | — |
| f1095a.a_jul | — | — | — | 7 | — | — | — |
| f1095a.a_aug | — | — | — | 7 | — | — | — |
| f1095a.a_sep | — | — | — | 7 | — | — | — |
| f1095a.a_oct | — | — | — | 7 | — | — | — |
| f1095a.a_nov | — | — | — | 7 | — | — | — |
| f1095a.a_dec | — | — | — | 7 | — | — | — |
| f1095a.b_jan | — | — | — | 7 | — | — | — |
| f1095a.b_feb | — | — | — | 7 | — | — | — |
| f1095a.b_mar | — | — | — | 7 | — | — | — |
| f1095a.b_apr | — | — | — | 7 | — | — | — |
| f1095a.b_may | — | — | — | 7 | — | — | — |
| f1095a.b_jun | — | — | — | 7 | — | — | — |
| f1095a.b_jul | — | — | — | 7 | — | — | — |
| f1095a.b_aug | — | — | — | 7 | — | — | — |
| f1095a.b_sep | — | — | — | 7 | — | — | — |
| f1095a.b_oct | — | — | — | 7 | — | — | — |
| f1095a.b_nov | — | — | — | 7 | — | — | — |
| f1095a.b_dec | — | — | — | 7 | — | — | — |
| f1095a.yr_a_monthly | — | — | — | 6 | — | — | — |
| f1095a.yr_a_uniform | — | — | — | 4 | — | — | — |
| f1095a.line33a | — | — | — | 7 | — | — | 3 |
| f1095a.yr_b_monthly | — | — | — | 5 | — | — | — |
| f1095a.yr_b_uniform | — | — | — | 4 | — | — | — |
| f1095a.line33b | — | — | — | 7 | — | — | 3 |
| f1095a.yr_c_monthly | — | — | — | 6 | — | — | — |
| f1095a.line33c | — | — | — | 7 | — | — | 3 |
| f1095a.b_counted | — | — | — | — | — | — | — |
| f1095a.b_used | — | — | — | 7 | — | — | — |

Unasserted lines: f1095a.one, f1095a.months, f1095a.no

## Form 1116 — Foreign Tax Credit (passive category, one form)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1116.zero | — | — | — | — | — | — | — |
| f1116.foreign_gain | — | — | — | — | — | — | — |
| f1116.redetermination | — | — | — | — | — | — | — |
| f1116.reduction | — | — | — | — | — | — | — |
| f1116.loss_accounts | — | — | — | — | — | — | — |
| f1116.other_category | — | — | — | — | — | — | — |
| f1116.not_on_statement | — | — | — | — | — | — | — |
| f1116.not_creditable | — | — | — | — | — | — | — |
| f1116.business | — | — | — | — | — | — | — |
| f1116.rental | — | — | — | — | — | — | — |
| f1116.itemized_unread | — | — | — | — | — | — | — |
| f1116.interest_threshold | — | — | — | — | — | — | — |
| f1116.foreign_over | — | — | — | — | — | — | — |
| f1116.hmi_applies | — | — | — | — | — | — | 1 (f1116.m1116_asset_method_standard_deduction) |
| f1116.asset_method | — | — | — | — | — | — | 2 (f1116.c4_asset_method_at_5000, f1116.m1116_asset_method_standard_deduction) |
| f1116.l5 | — | — | — | — | — | — | 1 (f1116.m1116_exception_ceiling_plus_1) |
| f1116.must_adjust | — | — | — | — | — | — | — |
| f1116.exception_ceiling | — | — | — | — | — | — | — |
| f1116.exception_qd_limit | — | — | — | — | — | — | — |
| f1116.div_total | — | — | — | — | — | — | — |
| f1116.exception | — | — | — | — | — | — | 1 (f1116.m1116_exception_ceiling_plus_1) |
| f1116.adjust | — | — | — | — | — | — | 1 (f1116.m1116_exception_ceiling_plus_1) |
| f1116.int_total | — | — | — | — | — | — | — |
| f1116.income_over | — | — | — | — | — | — | 1 (f1116.c1_income_at) |
| f1116.tax_mismatch | — | — | — | — | — | — | — |
| f1116.line1a_total | — | — | — | 4 | — | — | — |
| f1116.line3a_itemized | — | — | — | — | — | — | — |
| f1116.line3a | — | — | — | 3 | — | — | 1 (f1116.c4_interest_at_5000) |
| f1116.line3b | — | — | — | 4 | — | — | — |
| f1116.line3c | — | — | — | 3 | — | — | 1 (f1116.c4_gifts) |
| f1116.line3d_total | — | — | — | — | — | — | — |
| f1116.gains | — | — | — | — | — | — | 1 (f1116.m1116_zero_taxable_capital_loss) |
| f1116.line3e | — | — | — | 4 | — | — | 2 (f1116.m1116_no_gross_income, f1116.m1116_zero_taxable_capital_loss) |
| f1116.has_gross | — | — | — | — | — | — | 1 (f1116.m1116_no_gross_income) |
| f1116.line6_total | — | — | — | 4 | — | — | 4 |
| f1116.line7_total | — | — | — | 4 | — | — | 8 |
| f1116.line8 | — | — | — | 4 | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116.gross_hi | — | — | — | — | — | — | 3 |
| f1116.tax_hi | — | — | — | — | — | — | 3 |
| f1116.gross_lo | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116.tax_lo | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116.hmi_total | — | — | — | — | — | — | — |
| f1116.ratable | — | — | — | — | — | — | — |
| f1116.exp_hi_figured | — | — | — | — | — | — | — |
| f1116.exp_hi | — | — | — | — | — | — | 3 |
| f1116.net_hi | — | — | — | — | — | — | 1 (f1116.m1116_no_gross_income) |
| f1116.limit_hi | — | — | — | — | — | — | 3 |
| f1116.exp_lo_figured | — | — | — | — | — | — | — |
| f1116.exp_lo | — | — | — | — | — | — | 2 (f1116.c3_htko_at_limit, f1116.m1116_no_gross_income) |
| f1116.net_lo | — | — | — | — | — | — | 1 (f1116.m1116_no_gross_income) |
| f1116.limit_lo | — | — | — | — | — | — | 1 (f1116.c3_htko_at_limit) |
| f1116.high_taxed | — | — | — | — | — | — | 2 (f1116.m1116_no_gross_income, f1116.mint_line33_refused_line20_zero_line18) |
| f1116.line9 | — | — | — | 4 | — | — | — |
| f1116.line10 | — | — | — | 4 | — | — | 5 |
| f1116.line11 | — | — | — | 4 | — | — | — |
| f1116.line12 | — | — | — | 4 | — | — | — |
| f1116.line13 | — | — | — | 4 | — | — | — |
| f1116.line14_less12 | — | — | — | — | — | — | — |
| f1116.line14 | — | — | — | 4 | — | — | 2 (f1116.c5_carryover_in, f1116.c5_carryover_and_excess) |
| f1116.line15 | — | — | — | 4 | — | — | 1 (f1116.mint_line33_refused_line20_zero_line18) |
| f1116.line16 | — | — | — | 4 | — | — | — |
| f1116.line17 | — | — | — | 4 | — | — | — |
| f1116.line18_less14 | — | — | — | — | — | — | — |
| f1116.line18_raw | — | — | — | — | — | — | — |
| f1116.line18 | — | — | — | 4 | — | — | 4 |
| f1116.us_loss | — | — | — | — | — | — | 2 (f1116.c9_only_foreign, f1116.mint_line33_refused_line20_zero_line18) |
| f1116.has_line18 | — | — | — | — | — | — | 1 (f1116.m1116_zero_taxable_capital_loss) |
| f1116.line20 | — | — | — | 4 | — | — | 7 |
| f1116.line21_figured | — | — | — | — | — | — | — |
| f1116.line21 | — | — | — | 1 (classm.f1116.4) | — | — | 11 |
| f1116.line22 | — | — | — | 4 | — | — | — |
| f1116.line23 | — | — | — | 1 (classm.f1116.4) | — | — | 2 (f1116.m1116_zero_taxable_capital_loss, f1116.m1116_zero_taxable_other_tax) |
| f1116.line24 | — | — | — | 3 | — | — | 2 (f1116.c1_unlimited, f1116.mint_line33_refused_line20_zero_line18) |
| f1116.line27 | — | — | — | 3 | — | — | — |
| f1116.line32 | — | — | — | 3 | — | — | — |
| f1116.line33 | — | — | — | 3 | — | — | 2 (f1116.m1116_zero_taxable_other_tax, f1116.mint_line33_refused_line20_zero_line18) |
| f1116.line34 | — | — | — | 4 | — | — | — |
| f1116.line35 | — | — | — | 3 | — | — | 1 (f1116.mint_line33_refused_line20_zero_line18) |

Unasserted lines: f1116.zero, f1116.other_category, f1116.not_on_statement, f1116.not_creditable, f1116.business, f1116.rental, f1116.itemized_unread, f1116.interest_threshold, f1116.foreign_over, f1116.must_adjust, f1116.exception_ceiling, f1116.exception_qd_limit, f1116.div_total, f1116.int_total, f1116.tax_mismatch, f1116.line3a_itemized, f1116.line3d_total, f1116.hmi_total, f1116.ratable, f1116.exp_hi_figured, f1116.exp_lo_figured, f1116.line14_less12, f1116.line18_less14, f1116.line18_raw, f1116.line21_figured

## Form 1116 (passive category) — one column of Part I and its line of Part II

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1116col.kind | — | — | — | — | — | — | — |
| f1116col.zero | — | — | — | — | — | — | — |
| f1116col.has_div | — | — | — | — | — | — | — |
| f1116col.has_int | — | — | — | — | — | — | — |
| f1116col.div_income | — | — | — | — | — | — | — |
| f1116col.div_income_if_div | — | — | — | — | — | — | — |
| f1116col.int_income | — | — | — | — | — | — | — |
| f1116col.int_income_if_int | — | — | — | — | — | — | — |
| f1116col.line1a | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116col.line3d | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | — |
| f1116col.line3g | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | 2 (f1116.m1116_no_gross_income, f1116.mint_line33_refused_line20_zero_line18) |
| f1116col.line3g_figured | — | — | — | — | — | — | — |
| f1116col.line4a | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | — |
| f1116col.line4a_figured | — | — | — | — | — | — | — |
| f1116col.line6 | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | — |
| f1116col.line7 | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | 2 (f1116.m1116_no_gross_income, f1116.mint_line33_refused_line20_zero_line18) |
| f1116col.tax_div | — | — | — | — | — | — | — |
| f1116col.tax_div_if_div | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | — |
| f1116col.tax_int | — | — | — | — | — | — | — |
| f1116col.tax_int_if_int | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | — |
| f1116col.line8u | — | — | — | 2 (classm.f1116col.1, classm.f1116col.2) | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116col.div_15 | — | — | — | — | — | — | — |
| f1116col.div_hi | — | — | — | — | — | — | — |
| f1116col.div_lo | — | — | — | — | — | — | — |
| f1116col.div_gross_hi | — | — | — | — | — | — | — |
| f1116col.div_tax_hi | — | — | — | — | — | — | — |
| f1116col.div_gross_lo | — | — | — | — | — | — | — |
| f1116col.div_tax_lo | — | — | — | — | — | — | — |
| f1116col.int_15 | — | — | — | — | — | — | — |
| f1116col.int_hi | — | — | — | — | — | — | — |
| f1116col.int_lo | — | — | — | — | — | — | — |
| f1116col.int_gross_hi | — | — | — | — | — | — | — |
| f1116col.int_tax_hi | — | — | — | — | — | — | — |
| f1116col.int_gross_lo | — | — | — | — | — | — | — |
| f1116col.int_tax_lo | — | — | — | — | — | — | — |
| f1116col.gross_hi | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116col.tax_hi | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116col.gross_lo | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |
| f1116col.tax_lo | — | — | — | — | — | — | 2 (f1116.m1116_col_mixed_groups, f1116.m1116_col_interest_and_cent) |

Unasserted lines: f1116col.zero, f1116col.has_div, f1116col.has_int, f1116col.div_income_if_div, f1116col.int_income_if_int, f1116col.line3g_figured, f1116col.line4a_figured, f1116col.div_15, f1116col.div_hi, f1116col.div_lo, f1116col.div_gross_hi, f1116col.div_tax_hi, f1116col.div_gross_lo, f1116col.div_tax_lo, f1116col.int_15, f1116col.int_hi, f1116col.int_lo, f1116col.int_gross_hi, f1116col.int_tax_hi, f1116col.int_gross_lo, f1116col.int_tax_lo

## Schedule B (Form 1116) — Foreign Tax Carryover Reconciliation Schedule (passive category)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1116sb.zero | — | — | — | — | — | — | — |
| f1116sb.no | — | — | — | — | — | — | — |
| f1116sb.l1_i | — | — | — | 3 | — | — | — |
| f1116sb.l1_ii | — | — | — | 3 | — | — | — |
| f1116sb.l1_iii | — | — | — | 3 | — | — | — |
| f1116sb.l1_iv | — | — | — | 3 | — | — | — |
| f1116sb.l1_v | — | — | — | 3 | — | — | — |
| f1116sb.l1_vi | — | — | — | 3 | — | — | — |
| f1116sb.l1_ix | — | — | — | 3 | — | — | — |
| f1116sb.l1_x | — | — | — | 3 | — | — | — |
| f1116sb.l1_xi | — | — | — | 3 | — | — | — |
| f1116sb.l1_xii | — | — | — | 3 | — | — | — |
| f1116sb.l3_i | — | — | — | 3 | — | — | — |
| f1116sb.l3_ii | — | — | — | 3 | — | — | — |
| f1116sb.l3_iii | — | — | — | 3 | — | — | — |
| f1116sb.l3_iv | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_v | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_vi | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_ix | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_x | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_xi | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_xii | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.current | — | — | — | — | — | — | — |
| f1116sb.excess_limit | — | — | — | — | — | — | 4 |
| f1116sb.used_i | — | — | — | — | — | — | — |
| f1116sb.room_ii | — | — | — | — | — | — | — |
| f1116sb.used_ii | — | — | — | — | — | — | — |
| f1116sb.room_iii | — | — | — | — | — | — | — |
| f1116sb.used_iii | — | — | — | — | — | — | — |
| f1116sb.room_iv | — | — | — | — | — | — | — |
| f1116sb.used_iv | — | — | — | — | — | — | — |
| f1116sb.room_v | — | — | — | — | — | — | — |
| f1116sb.used_v | — | — | — | — | — | — | — |
| f1116sb.room_vi | — | — | — | — | — | — | — |
| f1116sb.used_vi | — | — | — | — | — | — | — |
| f1116sb.room_ix | — | — | — | — | — | — | — |
| f1116sb.used_ix | — | — | — | — | — | — | — |
| f1116sb.room_x | — | — | — | — | — | — | — |
| f1116sb.used_x | — | — | — | — | — | — | — |
| f1116sb.room_xi | — | — | — | — | — | — | — |
| f1116sb.used_xi | — | — | — | — | — | — | — |
| f1116sb.room_xii | — | — | — | — | — | — | — |
| f1116sb.used_xii | — | — | — | — | — | — | — |
| f1116sb.l4_i | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.c5_carryover_in, f1116.c5_carryover_expires) |
| f1116sb.l4_ii | — | — | — | 1 (classm.f1116sb.1) | — | — | 3 |
| f1116sb.l4_iii | — | — | — | 1 (classm.f1116sb.1) | — | — | 3 |
| f1116sb.l4_iv | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_v | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_vi | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_ix | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_x | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_xi | — | — | — | 1 (classm.f1116sb.1) | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l4_xii | — | — | — | 1 (classm.f1116sb.1) | — | — | 3 |
| f1116sb.l5_i | — | — | — | 3 | — | — | 5 |
| f1116sb.l6_xiii | — | — | — | 2 (classm.f1116sb.2, classm.f1116sb.3) | — | — | 7 |
| f1116sb.l7_xiii | — | — | — | 3 | — | — | — |
| f1116sb.l8_ii | — | — | — | 3 | — | — | — |
| f1116sb.l8_iii | — | — | — | 3 | — | — | 3 |
| f1116sb.l8_iv | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_v | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_vi | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_ix | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_x | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_xi | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l8_xii | — | — | — | 3 | — | — | 4 |
| f1116sb.l8_xiii | — | — | — | 3 | — | — | 1 (f1116.c2_carryover_generated) |
| f1116sb.l1_vii | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l1_xiv | — | — | — | 3 | — | — | 2 (f1116.m1116_sb_limit_ends_in_xii, f1116.m1116_sb_no_excess_limit) |
| f1116sb.l3_vii | — | — | — | 3 | — | — | — |
| f1116sb.l3_xiv | — | — | — | 3 | — | — | 1 (f1116.c2_carryover_generated) |
| f1116sb.l4_vii | — | — | — | 1 (classm.f1116sb.1) | — | — | — |
| f1116sb.l4_xiv | — | — | — | 1 (classm.f1116sb.1) | — | — | 4 |
| f1116sb.l8_vii | — | — | — | 3 | — | — | 3 |
| f1116sb.l8_xiv | — | — | — | 3 | — | — | 6 |
| f1116sb.changed | — | — | — | — | — | — | — |
| f1116sb.changed_if_carry | — | — | — | — | — | — | — |
| f1116sb.split | — | — | — | — | — | — | — |
| f1116sb.split_if_carry | — | — | — | — | — | — | — |
| f1116sb.generated | — | — | — | — | — | — | — |
| f1116sb.prior_none | — | — | — | — | — | — | — |
| f1116sb.prior_year | — | — | — | — | — | — | — |
| f1116sb.prior_year_if_excess | — | — | — | — | — | — | — |
| f1116sb.carryback | — | — | — | — | — | — | — |

Unasserted lines: f1116sb.zero, f1116sb.no, f1116sb.current, f1116sb.used_i, f1116sb.room_ii, f1116sb.used_ii, f1116sb.room_iii, f1116sb.used_iii, f1116sb.room_iv, f1116sb.used_iv, f1116sb.room_v, f1116sb.used_v, f1116sb.room_vi, f1116sb.used_vi, f1116sb.room_ix, f1116sb.used_ix, f1116sb.room_x, f1116sb.used_x, f1116sb.room_xi, f1116sb.used_xi, f1116sb.room_xii, f1116sb.used_xii, f1116sb.changed_if_carry, f1116sb.split_if_carry, f1116sb.generated, f1116sb.prior_none, f1116sb.prior_year_if_excess, f1116sb.carryback

## Schedule B (Form 1116) — one earlier year's foreign tax carried into 2025

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1116sbyr.year | — | — | — | — | — | — | — |
| f1116sbyr.amount | — | — | — | — | — | — | — |

## Form 2441 — Child and Dependent Care Expenses (Parts I to III)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f2441.zero | — | — | — | via f2441.line9b: 3; via f2441.line22: 6 | — | — | — |
| f2441.benefits | — | — | — | — | — | — | — |
| f2441.care | — | — | — | — | — | — | — |
| f2441.filing | — | — | — | — | — | — | — |
| f2441.student | — | — | — | — | — | — | — |
| f2441.unable | — | — | — | — | — | — | — |
| f2441.student_disabled | — | — | — | — | — | — | — |
| f2441.spouse_died | — | — | — | — | — | — | — |
| f2441.spouse_died_gate | — | — | — | — | — | — | — |
| f2441.mfs_qp_count | — | — | — | — | — | — | — |
| f2441.mfs_qp_home | — | — | — | — | — | — | — |
| f2441.line_a_home | — | — | — | — | — | — | — |
| f2441.line_a | — | — | — | 12 | — | — | 5 |
| f2441.mfs_married | — | — | — | — | — | — | — |
| f2441.care_other | — | — | — | — | — | — | — |
| f2441.nondependent | — | — | — | — | — | — | — |
| f2441.care_other_or_claimable | — | — | — | — | — | — | — |
| f2441.nondependent_if_other | — | — | — | — | — | — | — |
| f2441.nondependent_gate | — | — | — | — | — | — | 1 (mutation.m2.f2441.care_other_dependent) |
| f2441.provider_count | — | — | — | — | — | — | — |
| f2441.related_count | — | — | — | — | — | — | — |
| f2441.provider_ineligible | — | — | — | — | — | — | — |
| f2441.many_providers | — | — | — | — | — | — | — |
| f2441.no | — | — | — | — | — | — | — |
| f2441.line1_box | — | — | — | 18 | — | — | 3 |
| f2441.statement_count | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.any_statement | — | — | — | — | — | — | — |
| f2441.statement_notice | — | — | — | — | — | — | 2 (stage15.regress.f2441.providers_statement_household, stage15.mut.f2441_one_provider_no_notices) |
| f2441.household_count | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.any_household | — | — | — | — | — | — | — |
| f2441.household_notice | — | — | — | — | — | — | 3 |
| f2441.provider_paid | — | — | — | — | — | — | — |
| f2441.line1_paid | — | — | — | — | — | — | — |
| f2441.qp_count | — | — | — | — | — | — | 6 |
| f2441.line2_box | — | — | — | 18 | — | — | 2 (stage15.regress.f2441.three_qualifying_persons, mutation.eic.line5_key.no_child) |
| f2441.paid_total | — | — | — | — | — | — | 4 |
| f2441.limit_one | — | — | — | — | — | — | — |
| f2441.limit_two | — | — | — | — | — | — | — |
| f2441.two_or_more | — | — | — | — | — | — | — |
| f2441.limit | — | — | — | via f2441.line27: 6 | — | — | 1 (stage15.regress.f2441.nonqualifying_dependent) |
| f2441.line3_expenses | — | — | — | — | — | — | — |
| f2441.line3 | — | — | — | 12 | — | OpenTaxSolver: 285 compared (285 nonzero), 0 excluded | 33 |
| f2441.has_1e | — | — | — | — | — | — | — |
| f2441.box10_persons | — | — | — | — | — | — | 1 (stage19.mut.dc_box10_spouse_only) |
| f2441.one_box10 | — | — | — | — | — | — | 1 (mutation.t2.mfj_no_trad_ira) |
| f2441.attrib_gate | — | — | — | — | — | — | — |
| f2441.line4 | — | — | — | 12 | — | OpenTaxSolver: 285 compared (285 nonzero), 0 excluded | 36 |
| f2441.spouse_earned | — | — | — | — | — | — | — |
| f2441.line5 | — | — | — | 12 | — | — | 39 |
| f2441.joint | — | — | — | — | — | — | — |
| f2441.line6_34 | — | — | — | — | — | — | — |
| f2441.line6_345 | — | — | — | — | — | — | — |
| f2441.line6 | — | — | — | 12 | — | OpenTaxSolver: 285 compared (270 nonzero), 0 excluded | 28 |
| f2441.line7 | — | — | — | 12 | — | OpenTaxSolver: 267 compared (267 nonzero), 18 excluded | 28 |
| f2441.line8 | — | — | — | 12 | — | — | 28 |
| f2441.line9a | — | — | — | 12 | — | OpenTaxSolver: 266 compared (251 nonzero), 19 excluded | 30 |
| f2441.line9b | — | — | — | 12 | — | — | 1 (stage15.refuse.f2441.prior_year) |
| f2441.prior_year | — | — | — | — | — | — | — |
| f2441.line9c | — | — | — | 12 | — | PE: 1511 compared (247 nonzero), 150 excluded; OpenTaxSolver: 250 compared (238 nonzero), 35 excluded | 28 |
| f2441.clw1 | — | — | — | 12 | — | — | 12 |
| f2441.clw2 | — | — | — | 12 | — | — | 12 |
| f2441.clw3 | — | — | — | 12; via f2441.line10: 3 | — | E via f2441.line10 (OpenTaxSolver) | 12 |
| f2441.line10 | — | — | — | 12 | — | OpenTaxSolver: 162 compared (136 nonzero), 123 excluded | 30 |
| f2441.line11_figured | — | — | — | — | — | — | — |
| f2441.line11 | — | — | — | 12 | — | PE: 1239 compared (170 nonzero), 404 excluded; TC: 844 compared (123 nonzero), 840 excluded; OpenTaxSolver: 162 compared (130 nonzero), 123 excluded | 38 |
| f2441.line12 | — | — | — | 11 | — | — | 11 |
| f2441.line13 | — | — | — | — | — | — | 7 |
| f2441.line14 | — | — | — | — | — | — | 7 |
| f2441.line15_sum | — | — | — | — | — | — | — |
| f2441.line14_bad | — | — | — | — | — | — | 3 |
| f2441.line15 | — | — | — | 11 | — | — | 15 |
| f2441.other_care_expenses | — | — | — | — | — | — | — |
| f2441.line16 | — | — | — | 11 | — | — | 10 |
| f2441.line17 | — | — | — | 11 | — | — | 13 |
| f2441.employer_care_l16 | — | — | — | — | — | — | 2 (stage21.t073.employer_care_nothing_paid_refused, stage21.t073.employer_care_paid_equals_benefits) |
| f2441.line18 | — | — | — | 11 | — | — | 15 |
| f2441.spouse_earned_b | — | — | — | — | — | — | — |
| f2441.mfs_spouse_earned | — | — | — | — | — | — | — |
| f2441.mfs_spouse_earned_if_married | — | — | — | — | — | — | — |
| f2441.mfs_spouse_deemed | — | — | — | — | — | — | — |
| f2441.mfs_spouse_deemed_if_married | — | — | — | — | — | — | — |
| f2441.line19_other | — | — | — | — | — | — | — |
| f2441.line19 | — | — | — | 11 | — | — | 14 |
| f2441.line20_17_18 | — | — | — | — | — | — | — |
| f2441.line20_all | — | — | — | — | — | — | — |
| f2441.line20 | — | — | — | 11 | — | — | 12 |
| f2441.plans_differ | — | — | — | — | — | — | — |
| f2441.employer_care | — | — | — | — | — | — | — |
| f2441.employer_care_gate | — | — | — | — | — | — | 1 (mutation.t2.no_5695_part1_s3_5a) |
| f2441.plan_max | — | — | — | — | — | — | — |
| f2441.exclusion_max | — | — | — | — | — | — | 1 (stage15.regress.f2441.exclusion_max) |
| f2441.exclusion_max_mfs | — | — | — | — | — | — | — |
| f2441.exclusion_cap | — | — | — | — | — | — | — |
| f2441.line21 | — | — | — | 11 | — | — | 13 |
| f2441.line22 | — | — | — | 11 | — | — | 7 |
| f2441.line23 | — | — | — | 11 | — | — | 8 |
| f2441.line24_20_21 | — | — | — | — | — | — | — |
| f2441.line24 | — | — | — | 11 | — | — | 8 |
| f2441.line13_earned | — | — | — | — | — | — | 5 |
| f2441.line25 | — | — | — | 11 | — | — | 12 |
| f2441.line26 | — | — | — | 11 | — | — | 16 |
| f2441.line27 | — | — | — | 10 | — | — | 7 |
| f2441.line28 | — | — | — | 10 | — | — | 9 |
| f2441.line29 | — | — | — | 8 | — | — | 9 |
| f2441.line30 | — | — | — | 4 | — | — | 4 |
| f2441.line31 | — | — | — | 4 | — | — | 4 |

Unasserted lines: f2441.filing, f2441.student_disabled, f2441.spouse_died_gate, f2441.mfs_qp_count, f2441.mfs_qp_home, f2441.line_a_home, f2441.mfs_married, f2441.care_other_or_claimable, f2441.nondependent_if_other, f2441.provider_count, f2441.related_count, f2441.provider_ineligible, f2441.many_providers, f2441.no, f2441.any_statement, f2441.any_household, f2441.provider_paid, f2441.line1_paid, f2441.limit_one, f2441.limit_two, f2441.two_or_more, f2441.line3_expenses, f2441.has_1e, f2441.attrib_gate, f2441.spouse_earned, f2441.joint, f2441.line6_34, f2441.line6_345, f2441.line11_figured, f2441.line15_sum, f2441.spouse_earned_b, f2441.mfs_spouse_earned_if_married, f2441.mfs_spouse_deemed_if_married, f2441.line19_other, f2441.line20_17_18, f2441.line20_all, f2441.exclusion_max_mfs, f2441.exclusion_cap, f2441.line24_20_21

## Form 4137 — Social Security and Medicare Tax on Unreported Tip Income, lines 2 to 13, one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f4137.files | — | — | — | — | — | — | 1 (x2pay.f4137.noncash_only) |
| f4137.line2 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 1 (x2pay.f4137.w1) |
| f4137.line3 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 1 (x2pay.f4137.w1) |
| f4137.line4 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 2 (x2pay.f4137.w1, x2pay.f4137.line5_over) |
| f4137.line5 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 1 (x2pay.f4137.w1) |
| f4137.line5_over | — | — | — | — | — | — | 2 (mexist.f4137.line5_equals_line4, mexist.f4137.reported_over_unreported) |
| f4137.line6 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 4 |
| f4137.line7 | — | — | — | — | — | — | — |
| f4137.line8 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 2 (x2pay.f4137.w1, mexist.f4137.line8_rrta) |
| f4137.line9 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 2 (x2pay.f4137.w1, x2pay.f4137.over_ss_base) |
| f4137.line10 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 4 |
| f4137.rate_062 | — | — | — | — | — | — | — |
| f4137.line11 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 2 (x2pay.f4137.w1, x2pay.f4137.over_ss_base) |
| f4137.rate_0145 | — | — | — | — | — | — | — |
| f4137.line12 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 5 |
| f4137.line13 | — | — | — | 2 (classm.f4137.1, classm.f4137.2) | — | — | 4 |

Unasserted lines: f4137.line7, f4137.rate_062, f4137.rate_0145

## Form 4137, line 1 — one row per employer to whom this person was required to but did not report all tips

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f4137row.col_c | — | — | — | — | — | — | — |
| f4137row.col_d | — | — | — | — | — | — | — |

## Form 4562 — Depreciation and Amortization, one per business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f4562.line12 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line14 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line17 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19a | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19b | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19c | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19d | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19f | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line19e | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line21 | — | — | — | 1 (classm.f4562.1) | — | — | 1 (mexist.scveh.macrs_heavy.suv_q1) |
| f4562.line22 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line25 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line26h | — | — | — | 1 (classm.f4562.1) | — | — | 1 (mexist.scveh.macrs_heavy.suv_q1) |
| f4562.line28 | — | — | — | 1 (classm.f4562.1) | — | — | 1 (mexist.scveh.macrs_heavy.suv_q1) |
| f4562.line29 | — | — | — | 1 (classm.f4562.1) | — | — | — |

## Form 4952 — supported investment-interest deduction and election

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f4952.has_interest | — | — | — | — | — | — | — |
| f4952.no | — | — | — | — | — | — | — |
| f4952.no_interest | — | — | — | — | — | — | — |
| f4952.line1_if_interest | — | — | — | 3 | — | — | — |
| f4952.line1 | — | — | — | — | — | — | 1 (stage20.blind.r9) |
| f4952.carryover_if_interest | — | — | — | — | — | — | — |
| f4952.carryover | — | — | — | — | — | — | — |
| f4952.prior_7 | — | — | — | — | — | — | — |
| f4952.unsupported | — | — | — | — | — | — | — |
| f4952.alternative_allocation | — | — | — | — | — | — | — |
| f4952.line4g_if_interest | — | — | — | — | — | — | — |
| f4952.line4a | — | — | — | 7 | — | — | 1 (stage4.f4952.line4a_taxable_interest_and_dividends) |
| f4952.line4g | — | — | — | — | — | — | — |
| f4952.zero | — | — | — | via f4952.line5: 4 | — | — | — |
| f4952.used | — | — | — | — | — | — | 1 (mutation.f4952.election_without_interest_used) |
| f4952.line2 | — | — | — | 7 | — | — | 6 |
| f4952.line3 | — | — | — | 7 | — | — | 7 |
| f4952.line4b | — | — | — | 7 | — | — | 1 (stage4.f4952.line4a_taxable_interest_and_dividends) |
| f4952.bad_dividends | — | — | — | — | — | — | — |
| f4952.line4c | — | — | — | 7 | — | — | 2 (stage4.f4952.line4a_taxable_interest_and_dividends, stage16.f4952.required_unanswered_bad_dividends) |
| f4952.line4d | — | — | — | 7 | — | — | 1 (stage4.interest.short_term) |
| f4952.line4e | — | — | — | 7 | — | — | 1 (stage4.interest.short_term) |
| f4952.line4f | — | — | — | 7 | — | — | 1 (stage4.interest.short_term) |
| f4952.election_limit | — | — | — | — | — | — | 1 (stage4.interest.short_term) |
| f4952.bad_election | — | — | — | — | — | — | — |
| f4952.election_checked | — | — | — | — | — | — | — |
| f4952.has_election | — | — | — | — | — | — | — |
| f4952.election | — | — | — | — | — | — | 6 |
| f4952.line4h | — | — | — | 7 | — | — | 3 |
| f4952.line5 | — | — | — | 7 | — | — | 4 |
| f4952.line6 | — | — | — | 7 | — | — | 4 |
| f4952.line7 | — | — | — | 7 | — | — | 6 |
| f4952.deduction | — | — | — | — | — | — | — |
| f4952.line8 | — | — | — | 7; via sa.line9: 6 | — | — | 13 |
| f4952.exception | — | — | — | — | — | — | 2 (mutation.t2.f8962_months_r4, mutation.t2.person.eic_se_refusal_order) |
| f4952.required_test | — | — | — | — | — | — | — |
| f4952.required | — | — | — | — | — | — | 16 |

Unasserted lines: f4952.no, f4952.no_interest, f4952.carryover_if_interest, f4952.line4g_if_interest, f4952.bad_dividends, f4952.bad_election, f4952.election_checked, f4952.has_election, f4952.deduction, f4952.required_test

## Form 5329, Additional Taxes on Qualified Plans (Including IRAs) and Other Tax-Favored Accounts (Parts I and VII), one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f5329.l1 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | UsTaxes below rule: 1083 compared (17 nonzero), 617 excluded | 19 |
| f5329.l2 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | — | 17 |
| f5329.l3 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | — | 17 |
| f5329.l3_s | — | — | — | — | — | — | — |
| f5329.l3_other | — | — | — | — | — | — | — |
| f5329.rate10 | — | — | — | — | — | — | — |
| f5329.rate25 | — | — | — | — | — | — | — |
| f5329.tax10 | — | — | — | — | — | — | — |
| f5329.tax25 | — | — | — | — | — | — | — |
| f5329.l4 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | UsTaxes below rule: 1083 compared (17 nonzero), 617 excluded | 19 |
| f5329.l47 | — | — | — | 6 | — | — | 4 |
| f5329.l48 | — | — | — | 6 | — | — | 3 |
| f5329.l49_base | — | — | — | — | — | — | — |
| f5329.rate6 | — | — | — | — | — | — | — |
| f5329.l49_tax | — | — | — | — | — | — | — |
| f5329.has_excess | — | — | — | — | — | — | — |
| f5329.zero | — | — | — | — | — | — | — |
| f5329.l49 | — | — | — | 6 | — | — | 5 |
| f5329.tax | — | — | — | — | — | — | — |
| f5329.must | — | — | — | — | — | — | — |
| f5329.one | — | — | — | — | — | — | — |
| f5329.files | 1 (stage21.example.teacher_education) | — | — | — | — | — | 11 |

Unasserted lines: f5329.l3_s, f5329.l3_other, f5329.rate10, f5329.rate25, f5329.tax10, f5329.tax25, f5329.l49_base, f5329.rate6, f5329.l49_tax, f5329.has_excess, f5329.zero, f5329.tax, f5329.must, f5329.one

## Form 5695 — Residential Energy Credits (Parts I and II)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f5695.zero | — | — | — | — | — | — | — |
| f5695.any | — | — | — | — | — | — | — |
| f5695.solar | — | — | — | — | — | — | — |
| f5695.solar_if_any | — | — | — | — | — | — | — |
| f5695.solar_water | — | — | — | — | — | — | — |
| f5695.solar_water_if_any | — | — | — | — | — | — | — |
| f5695.wind | — | — | — | — | — | — | — |
| f5695.wind_if_any | — | — | — | — | — | — | — |
| f5695.geothermal | — | — | — | — | — | — | — |
| f5695.geothermal_if_any | — | — | — | — | — | — | — |
| f5695.insulation | — | — | — | — | — | — | — |
| f5695.insulation_if_any | — | — | — | — | — | — | — |
| f5695.doors | — | — | — | — | — | — | — |
| f5695.doors_if_any | — | — | — | — | — | — | — |
| f5695.windows | — | — | — | — | — | — | — |
| f5695.windows_if_any | — | — | — | — | — | — | — |
| f5695.panel | — | — | — | — | — | — | — |
| f5695.panel_if_any | — | — | — | — | — | — | — |
| f5695.audit | — | — | — | — | — | — | — |
| f5695.audit_if_any | — | — | — | — | — | — | — |
| f5695.heat_pump | — | — | — | — | — | — | — |
| f5695.heat_pump_if_any | — | — | — | — | — | — | — |
| f5695.hp_water_heater | — | — | — | — | — | — | — |
| f5695.hp_water_heater_if_any | — | — | — | — | — | — | — |
| f5695.central_ac | — | — | — | — | — | — | — |
| f5695.central_ac_if_any | — | — | — | — | — | — | — |
| f5695.water_heater | — | — | — | — | — | — | — |
| f5695.water_heater_if_any | — | — | — | — | — | — | — |
| f5695.furnace | — | — | — | — | — | — | — |
| f5695.furnace_if_any | — | — | — | — | — | — | — |
| f5695.biomass | — | — | — | — | — | — | — |
| f5695.biomass_if_any | — | — | — | — | — | — | — |
| f5695.line7a_if_any | — | — | — | — | — | — | — |
| f5695.carry | — | — | — | — | — | — | — |
| f5695.carry_if_prior | — | — | — | — | — | — | — |
| f5695.sec_a_kinds | — | — | — | — | — | — | — |
| f5695.sec_b_kinds | — | — | — | — | — | — | — |
| f5695.kinds_answered | — | — | — | — | — | — | — |
| f5695.part1_some | — | — | — | — | — | — | — |
| f5695.part1_any | — | — | — | — | — | — | 1 (bug0478.f5695.paid_2024_installed_2025) |
| f5695.part2_some | — | — | — | — | — | — | — |
| f5695.part2_any | — | — | — | — | — | — | — |
| f5695.business_use | — | — | — | — | — | — | — |
| f5695.construction_later | — | — | — | — | — | — | — |
| f5695.line1 | — | — | — | — | — | — | 9 |
| f5695.line1_if_solar | — | — | — | — | — | — | — |
| f5695.line2 | — | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line2_if_solar_water | — | — | — | — | — | — | — |
| f5695.line3 | — | — | — | — | — | — | 1 (stage16.cleanup.f5695_small_wind) |
| f5695.line3_if_wind | — | — | — | — | — | — | — |
| f5695.line4 | — | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line4_if_geothermal | — | — | — | — | — | — | — |
| f5695.line5a | — | — | — | — | — | — | — |
| f5695.line5a_if_any | — | — | — | — | — | — | — |
| f5695.battery_cost | — | — | — | — | — | — | — |
| f5695.line5b | — | — | — | 3 | — | — | 2 (stage15.f5695.s4, bug0478.f5695.battery_paid_2024_installed_2025) |
| f5695.line6a | — | — | — | 33 | — | — | 13 |
| f5695.rce_rate | — | — | — | — | — | — | — |
| f5695.line6b | — | — | — | 33 | — | — | 11 |
| f5695.line7a | — | — | — | — | — | — | — |
| f5695.line11 | — | — | — | — | — | — | 1 (stage15.refuse.f5695.fuel_cell) |
| f5695.line12 | — | — | — | — | — | — | 1 (stage15.f5695.s5) |
| f5695.line12_if_carry | — | — | — | — | — | — | — |
| f5695.line6b_if_any | — | — | — | — | — | — | — |
| f5695.line11_if_any | — | — | — | — | — | — | — |
| f5695.line13 | — | — | — | 35 | — | PE: 1681 compared (173 nonzero), 19 excluded | 15 |
| f5695.no | — | — | — | — | — | — | — |
| f5695.line13_positive | — | — | — | — | — | — | — |
| f5695.claiming_part1 | — | — | — | — | — | — | 1 (stage15.mut.f5695_part1_one_cent) |
| f5695.rce_ws1 | — | — | — | — | — | — | 11 |
| f5695.ctc_line19 | — | — | — | — | — | — | — |
| f5695.ctc | — | — | — | — | — | — | — |
| f5695.rce_ws2 | — | — | — | — | — | — | 12 |
| f5695.rce_ws3 | — | — | — | via f5695.line14: 16 | — | — | 11 |
| f5695.line14 | — | — | — | 33 | — | — | 12 |
| f5695.line15 | — | — | — | 35 | — | PE: 1225 compared (96 nonzero), 418 excluded | 12 |
| f5695.line16 | — | — | — | 12 | — | — | 9 |
| f5695.line17a | — | — | — | — | — | — | — |
| f5695.line17b | — | — | — | — | — | — | — |
| f5695.line17c | — | — | — | — | — | — | — |
| f5695.sec_a_home | — | — | — | — | — | — | — |
| f5695.sec_a_original | — | — | — | — | — | — | — |
| f5695.sec_a_claimed | — | — | — | — | — | — | — |
| f5695.line17e | — | — | — | — | — | — | — |
| f5695.sec_a_new_home | — | — | — | — | — | — | — |
| f5695.eehi_rate | — | — | — | — | — | — | — |
| f5695.line18a | — | — | — | — | — | — | 6 |
| f5695.line18a_if_insulation | — | — | — | — | — | — | — |
| f5695.ins_30 | — | — | — | — | — | — | — |
| f5695.insulation_max | — | — | — | — | — | — | — |
| f5695.ins_capped | — | — | — | — | — | — | — |
| f5695.line18b | — | — | — | 23 | — | — | 8 |
| f5695.line19a | — | — | — | — | — | — | 4 |
| f5695.line19a_if_doors | — | — | — | — | — | — | — |
| f5695.door1_30 | — | — | — | — | — | — | — |
| f5695.door_max | — | — | — | — | — | — | — |
| f5695.line19c | — | — | — | 23 | — | — | 5 |
| f5695.line19d_i | — | — | — | — | — | — | — |
| f5695.line19d_i_if_doors | — | — | — | — | — | — | — |
| f5695.line19d_ii | — | — | — | — | — | — | — |
| f5695.line19d_ii_if_doors | — | — | — | — | — | — | — |
| f5695.line19e | — | — | — | — | — | — | 4 |
| f5695.line19e_if_doors | — | — | — | — | — | — | — |
| f5695.line19f | — | — | — | 23 | — | — | 4 |
| f5695.line19g | — | — | — | 23 | — | — | 4 |
| f5695.doors_sum | — | — | — | — | — | — | — |
| f5695.doors_max | — | — | — | — | — | — | — |
| f5695.doors_cost | — | — | — | — | — | — | — |
| f5695.qmid_doors | — | — | — | — | — | — | — |
| f5695.doors_costs | — | — | — | — | — | — | — |
| f5695.doors_qmid_missing | — | — | — | — | — | — | — |
| f5695.doors_no_qmid | — | — | — | — | — | — | — |
| f5695.doors_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line19h | — | — | — | 23 | — | — | 8 |
| f5695.line20a_i | — | — | — | — | — | — | — |
| f5695.line20a_i_if_windows | — | — | — | — | — | — | — |
| f5695.line20a_ii | — | — | — | — | — | — | — |
| f5695.line20a_ii_if_windows | — | — | — | — | — | — | — |
| f5695.line20a_iii | — | — | — | — | — | — | — |
| f5695.line20a_iii_if_windows | — | — | — | — | — | — | — |
| f5695.line20a_iv | — | — | — | — | — | — | — |
| f5695.line20a_iv_if_windows | — | — | — | — | — | — | — |
| f5695.line20b | — | — | — | — | — | — | 4 |
| f5695.line20b_if_windows | — | — | — | — | — | — | — |
| f5695.line20c | — | — | — | 23 | — | — | 4 |
| f5695.windows_30 | — | — | — | — | — | — | — |
| f5695.windows_max | — | — | — | — | — | — | — |
| f5695.qmid_windows | — | — | — | — | — | — | — |
| f5695.windows_costs | — | — | — | — | — | — | — |
| f5695.windows_qmid_missing | — | — | — | — | — | — | — |
| f5695.windows_no_qmid | — | — | — | — | — | — | — |
| f5695.windows_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line20d | — | — | — | 23 | — | — | 6 |
| f5695.line21a | — | — | — | — | — | — | — |
| f5695.line21b | — | — | — | — | — | — | — |
| f5695.sec_b_home | — | — | — | — | — | — | — |
| f5695.sec_b_claimed | — | — | — | — | — | — | — |
| f5695.b_new_home | — | — | — | — | — | — | — |
| f5695.sec_b_new_home | — | — | — | — | — | — | — |
| f5695.item_max | — | — | — | — | — | — | — |
| f5695.line22a | — | — | — | — | — | — | 3 |
| f5695.line22a_if_central_ac | — | — | — | — | — | — | — |
| f5695.line22b | — | — | — | — | — | — | 3 |
| f5695.line22b_if_central_ac | — | — | — | — | — | — | — |
| f5695.line22c | — | — | — | 15 | — | — | 3 |
| f5695.ac_30 | — | — | — | — | — | — | — |
| f5695.qmid_ac | — | — | — | — | — | — | — |
| f5695.ac_costs | — | — | — | — | — | — | — |
| f5695.ac_qmid_missing | — | — | — | — | — | — | — |
| f5695.ac_no_qmid | — | — | — | — | — | — | 1 (stage15.mut.f5695_one_cent_no_qmid_condo) |
| f5695.ac_capped | — | — | — | — | — | — | 2 (stage15.refuse.f5695.qmid_doors_windows_ac, stage15.mut.f5695_furnace_ac_no_qmid) |
| f5695.line22d | — | — | — | 15 | — | — | 5 |
| f5695.line23a_i | — | — | — | — | — | — | — |
| f5695.line23a_i_if_water_heater | — | — | — | — | — | — | — |
| f5695.line23a_ii | — | — | — | — | — | — | — |
| f5695.line23a_ii_if_water_heater | — | — | — | — | — | — | — |
| f5695.line23b | — | — | — | — | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line23b_if_water_heater | — | — | — | — | — | — | — |
| f5695.line23c | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.wh_30 | — | — | — | — | — | — | — |
| f5695.qmid_wh | — | — | — | — | — | — | — |
| f5695.wh_costs | — | — | — | — | — | — | — |
| f5695.wh_qmid_missing | — | — | — | — | — | — | — |
| f5695.wh_no_qmid | — | — | — | — | — | — | 1 (stage15.mut.f5695_one_cent_no_qmid_condo) |
| f5695.wh_capped | — | — | — | — | — | — | 3 |
| f5695.line23d | — | — | — | 15 | — | — | 4 |
| f5695.line24a | — | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24a_if_furnace | — | — | — | — | — | — | — |
| f5695.line24b | — | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24b_if_furnace | — | — | — | — | — | — | — |
| f5695.line24c | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.furnace_30 | — | — | — | — | — | — | — |
| f5695.qmid_furnace | — | — | — | — | — | — | — |
| f5695.furnace_costs | — | — | — | — | — | — | — |
| f5695.furnace_qmid_missing | — | — | — | — | — | — | — |
| f5695.furnace_no_qmid | — | — | — | — | — | — | 1 (stage15.mut.f5695_one_cent_no_qmid_condo) |
| f5695.furnace_capped | — | — | — | — | — | — | 3 |
| f5695.line24d | — | — | — | 15 | — | — | 3 |
| f5695.line25a | — | — | — | — | — | — | — |
| f5695.line25a_if_panel | — | — | — | — | — | — | — |
| f5695.enabling_claimed | — | — | — | — | — | — | — |
| f5695.line25c | — | — | — | — | — | — | 2 (stage15.f5695-2.e6, stage15.f5695-2.e7) |
| f5695.enabling_30 | — | — | — | — | — | — | — |
| f5695.qmid_enabling | — | — | — | — | — | — | — |
| f5695.enabling_costs | — | — | — | — | — | — | — |
| f5695.enabling_qmid_missing | — | — | — | — | — | — | — |
| f5695.enabling_no_qmid | — | — | — | — | — | — | 1 (stage15.mut.f5695_one_cent_no_qmid_condo) |
| f5695.enabling_capped | — | — | — | — | — | — | 2 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp, stage15.regress.f5695.enabling_cap) |
| f5695.line25e | — | — | — | 5 | — | — | 6 |
| f5695.line26a | — | — | — | — | — | — | — |
| f5695.line26a_if_audit | — | — | — | — | — | — | — |
| f5695.line26b | — | — | — | — | — | — | 2 (stage15.f5695.s6, stage15.f5695-2.e9) |
| f5695.audit_30 | — | — | — | — | — | — | — |
| f5695.audit_max | — | — | — | — | — | — | — |
| f5695.audit_capped | — | — | — | — | — | — | — |
| f5695.line26c | — | — | — | 4 | — | — | 4 |
| f5695.line27 | — | — | — | 35 | — | — | 24 |
| f5695.annual_max | — | — | — | — | — | — | — |
| f5695.line28 | — | — | — | 35 | — | — | 22 |
| f5695.line29a | — | — | — | — | — | — | 4 |
| f5695.line29a_if_heat_pump | — | — | — | — | — | — | — |
| f5695.line29b | — | — | — | — | — | — | 5 |
| f5695.line29b_if_heat_pump | — | — | — | — | — | — | — |
| f5695.line29c | — | — | — | — | — | — | 1 (stage15.f5695-2.e10) |
| f5695.line29c_if_hp_water_heater | — | — | — | — | — | — | — |
| f5695.line29d | — | — | — | — | — | — | 3 |
| f5695.line29d_if_hp_water_heater | — | — | — | — | — | — | — |
| f5695.line29e | — | — | — | — | — | — | — |
| f5695.line29e_if_biomass | — | — | — | — | — | — | — |
| f5695.line29f | — | — | — | — | — | — | 3 |
| f5695.line29f_if_biomass | — | — | — | — | — | — | — |
| f5695.line29g | — | — | — | 15 | — | — | 5 |
| f5695.hp_30 | — | — | — | — | — | — | — |
| f5695.heat_pump_max | — | — | — | — | — | — | — |
| f5695.qmid_hp | — | — | — | — | — | — | — |
| f5695.hp_costs | — | — | — | — | — | — | — |
| f5695.hp_qmid_missing | — | — | — | — | — | — | — |
| f5695.hp_no_qmid | — | — | — | — | — | — | — |
| f5695.hp_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line29h | — | — | — | 15 | — | — | 10 |
| f5695.joint_occupancy | — | — | — | — | — | — | — |
| f5695.separate_homes | — | — | — | — | — | — | — |
| f5695.separate_homes_joint | — | — | — | — | — | — | — |
| f5695.line30 | — | — | — | 35 | — | PE: 1641 compared (146 nonzero), 59 excluded | 37 |
| f5695.eehi_ws1 | — | — | — | — | — | — | 20 |
| f5695.eehi_ws2 | — | — | — | — | — | — | 21 |
| f5695.eehi_ws3 | — | — | — | via f5695.line31: 18 | — | — | 20 |
| f5695.line31 | — | — | — | 35 | — | — | 20 |
| f5695.eehi_credit | — | — | — | — | — | — | — |
| f5695.line32 | — | — | — | 35 | — | PE: 1252 compared (91 nonzero), 445 excluded | 23 |
| f5695.line32a | — | — | — | 35 | — | — | 3 |
| f5695.condo | — | — | — | — | — | — | — |
| f5695.line32b | — | — | — | 35 | — | — | 2 (stage15.refuse.f5695.joint_occupancy, stage15.mut.f5695_one_cent_no_qmid_condo) |

Unasserted lines: f5695.zero, f5695.solar_if_any, f5695.solar_water_if_any, f5695.wind_if_any, f5695.geothermal_if_any, f5695.insulation_if_any, f5695.doors_if_any, f5695.windows_if_any, f5695.panel_if_any, f5695.audit_if_any, f5695.heat_pump_if_any, f5695.hp_water_heater_if_any, f5695.central_ac_if_any, f5695.water_heater_if_any, f5695.furnace_if_any, f5695.biomass_if_any, f5695.line7a_if_any, f5695.carry_if_prior, f5695.sec_a_kinds, f5695.sec_b_kinds, f5695.kinds_answered, f5695.part1_some, f5695.part2_some, f5695.part2_any, f5695.line1_if_solar, f5695.line2_if_solar_water, f5695.line3_if_wind, f5695.line4_if_geothermal, f5695.line5a_if_any, f5695.rce_rate, f5695.line12_if_carry, f5695.line6b_if_any, f5695.line11_if_any, f5695.no, f5695.line13_positive, f5695.ctc_line19, f5695.ctc, f5695.sec_a_home, f5695.sec_a_original, f5695.sec_a_claimed, f5695.sec_a_new_home, f5695.eehi_rate, f5695.line18a_if_insulation, f5695.ins_30, f5695.insulation_max, f5695.ins_capped, f5695.line19a_if_doors, f5695.door1_30, f5695.door_max, f5695.line19d_i_if_doors, f5695.line19d_ii_if_doors, f5695.line19e_if_doors, f5695.doors_sum, f5695.doors_max, f5695.doors_cost, f5695.doors_costs, f5695.doors_qmid_missing, f5695.doors_no_qmid, f5695.line20a_i_if_windows, f5695.line20a_ii_if_windows, f5695.line20a_iii_if_windows, f5695.line20a_iv_if_windows, f5695.line20b_if_windows, f5695.windows_30, f5695.windows_max, f5695.windows_costs, f5695.windows_qmid_missing, f5695.windows_no_qmid, f5695.sec_b_home, f5695.sec_b_claimed, f5695.sec_b_new_home, f5695.item_max, f5695.line22a_if_central_ac, f5695.line22b_if_central_ac, f5695.ac_30, f5695.ac_costs, f5695.ac_qmid_missing, f5695.line23a_i_if_water_heater, f5695.line23a_ii_if_water_heater, f5695.line23b_if_water_heater, f5695.wh_30, f5695.wh_costs, f5695.wh_qmid_missing, f5695.line24a_if_furnace, f5695.line24b_if_furnace, f5695.furnace_30, f5695.furnace_costs, f5695.furnace_qmid_missing, f5695.line25a_if_panel, f5695.enabling_claimed, f5695.enabling_30, f5695.enabling_costs, f5695.enabling_qmid_missing, f5695.line26a_if_audit, f5695.audit_30, f5695.audit_max, f5695.audit_capped, f5695.annual_max, f5695.line29a_if_heat_pump, f5695.line29b_if_heat_pump, f5695.line29c_if_hp_water_heater, f5695.line29d_if_hp_water_heater, f5695.line29e_if_biomass, f5695.line29f_if_biomass, f5695.hp_30, f5695.heat_pump_max, f5695.hp_costs, f5695.hp_qmid_missing, f5695.hp_no_qmid, f5695.separate_homes_joint, f5695.eehi_credit

## Form 7203, S Corporation Shareholder Stock and Debt Basis Limitations (Parts I and III), one per S corporation

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f7203.zero | — | — | — | — | — | — | — |
| f7203.no | — | — | — | — | — | — | — |
| f7203.required | — | — | — | — | — | — | 3 |
| f7203.election | — | — | — | — | — | — | — |
| f7203.election_if_req | — | — | — | — | — | — | — |
| f7203.loans | — | — | — | — | — | — | — |
| f7203.loans_if_req | — | — | — | — | — | — | — |
| f7203.line1 | — | — | — | — | — | — | — |
| f7203.line1_if_req | — | — | — | — | — | — | — |
| f7203.line2 | — | — | — | — | — | — | — |
| f7203.line2_if_req | — | — | — | — | — | — | — |
| f7203.l3a | — | — | — | 3 | — | — | — |
| f7203.l3b | — | — | — | 3 | — | — | — |
| f7203.l3c | — | — | — | 3 | — | — | — |
| f7203.l3d | — | — | — | 3 | — | — | — |
| f7203.l3e | — | — | — | 3 | — | — | 1 (mk1.k1s.f7203_dividends_and_gain_with_loss) |
| f7203.l3f | — | — | — | 3 | — | — | 1 (mk1.k1s.f7203_dividends_and_gain_with_loss) |
| f7203.l3g | — | — | — | 3 | — | — | 3 |
| f7203.l3h | — | — | — | 3 | — | — | 1 (mk1.k1s.f7203_dividends_and_gain_with_loss) |
| f7203.l3i | — | — | — | 3 | — | — | — |
| f7203.l3j | — | — | — | 3 | — | — | — |
| f7203.l3k | — | — | — | 3 | — | — | 1 (k1s.withholding_taxexempt_st_loss) |
| f7203.l3l | — | — | — | 3 | — | — | — |
| f7203.l3m | — | — | — | 3 | — | — | — |
| f7203.line4 | — | — | — | 3 | — | — | 6 |
| f7203.line5 | — | — | — | 3 | — | — | 8 |
| f7203.line6 | — | — | — | 3 | — | — | 1 (mk1.k1s.f7203_distribution_equal_to_basis) |
| f7203.dist_over | — | — | — | — | — | — | — |
| f7203.line7 | — | — | — | 3 | — | — | 3 |
| f7203.l8a | — | — | — | 3 | — | — | — |
| f7203.l8b | — | — | — | 3 | — | — | — |
| f7203.l8c | — | — | — | 3 | — | — | — |
| f7203.line9 | — | — | — | 3 | — | — | — |
| f7203.line10 | — | — | — | 3 | — | — | 12 |
| f7203.a35 | — | — | — | 3 | — | — | — |
| f7203.a36 | — | — | — | 3 | — | — | — |
| f7203.a37 | — | — | — | 3 | — | — | — |
| f7203.a38 | — | — | — | 3 | — | — | — |
| f7203.a47 | — | — | — | 3 | — | — | 1 (k1s.loss_over_basis_prorata) |
| f7203.has_loss | — | — | — | — | — | — | — |
| f7203.c35_p | — | — | — | — | — | — | — |
| f7203.c35 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 6 |
| f7203.c36_p | — | — | — | — | — | — | — |
| f7203.c36 | — | — | — | 3 | — | — | 2 (k1s.loss_over_basis_prorata, mk1.k1s.box2_loss_box3_income) |
| f7203.c37_p | — | — | — | — | — | — | — |
| f7203.c37 | — | — | — | 3 | — | — | 3 |
| f7203.c38_p | — | — | — | — | — | — | — |
| f7203.c38 | — | — | — | 3 | — | — | 2 (k1s.withholding_taxexempt_st_loss, mk1.k1s.box7_loss_box8_gain) |
| f7203.c47 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | — |
| f7203.line11 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 5 |
| f7203.line12 | — | — | — | 3 | — | — | — |
| f7203.line13 | — | — | — | 3 | — | — | — |
| f7203.line14 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 1 (mk1.k1s.f7203_loss_over_basis_line14) |
| f7203.line15 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 8 |
| f7203.e35 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 3 |
| f7203.e36 | — | — | — | 3 | — | — | 1 (k1s.loss_over_basis_prorata) |
| f7203.e37 | — | — | — | 3 | — | — | 1 (k1s.loss_over_basis_ratio_rounding) |
| f7203.e38 | — | — | — | 3 | — | — | 1 (mk1.k1s.box7_loss_box8_gain) |
| f7203.e47 | — | — | — | 2 (classm.f7203.1, classm.f7203.2) | — | — | 2 (k1s.loss_within_basis, k1s.loss_over_basis_prorata) |
| f7203.cap_limited | — | — | — | — | — | — | — |
| f7203.one | — | — | — | — | — | — | — |

Unasserted lines: f7203.zero, f7203.no, f7203.election_if_req, f7203.loans_if_req, f7203.line1_if_req, f7203.line2_if_req, f7203.dist_over, f7203.has_loss, f7203.c35_p, f7203.c36_p, f7203.c37_p, f7203.c38_p, f7203.cap_limited, f7203.one

## Form 8582 — Passive Activity Loss Limitations

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8582.zero | — | — | — | — | — | — | — |
| f8582.line1a_rental | — | — | — | — | — | — | — |
| f8582.p4a | — | — | — | — | — | — | — |
| f8582.line2a_rental | — | — | — | — | — | — | — |
| f8582.p5a | — | — | — | — | — | — | — |
| f8582.line1b_rental | — | — | — | — | — | — | — |
| f8582.p4b | — | — | — | — | — | — | — |
| f8582.line2b_rental | — | — | — | — | — | — | — |
| f8582.p5b | — | — | — | — | — | — | — |
| f8582.line1c_rental | — | — | — | — | — | — | — |
| f8582.p4c | — | — | — | — | — | — | — |
| f8582.line2c_rental | — | — | — | — | — | — | — |
| f8582.p5c | — | — | — | — | — | — | — |
| f8582.line1a | — | — | — | 1 (classm.f8582.2) | — | — | 1 (x1sche.f4.two_properties) |
| f8582.line1b | — | — | — | 1 (classm.f8582.2) | — | — | 1 (x1sche.f3.pub925_phaseout) |
| f8582.line1c | — | — | — | 1 (classm.f8582.2) | — | — | 2 (mrental.f8582.part5_prior_loss, x1sche.f5.prior_loss_absorbed) |
| f8582.line1d | — | — | — | 1 (classm.f8582.2) | — | — | 4 |
| f8582.line2a | — | — | — | 1 (classm.f8582.2) | — | — | — |
| f8582.line2b | — | — | — | 1 (classm.f8582.2) | — | — | 1 (x1sche.f10.part5) |
| f8582.line2c | — | — | — | 1 (classm.f8582.2) | — | — | 1 (mrental.f8582.part5_prior_loss) |
| f8582.line2d | — | — | — | 1 (classm.f8582.2) | — | — | 2 (mrental.f8582.part5_prior_loss, x1sche.f13.part4_and_part5) |
| f8582.line3 | — | — | — | 1 (classm.f8582.2) | — | — | 5 |
| f8582.loss1d | — | — | — | — | — | — | — |
| f8582.loss3 | — | — | — | — | — | — | — |
| f8582.line4_both | — | — | — | — | — | — | — |
| f8582.part2 | — | — | — | — | — | — | — |
| f8582.line4 | — | — | — | 1 (classm.f8582.2) | — | — | 8 |
| f8582.line5 | — | — | — | 1 (classm.f8582.2) | — | — | — |
| f8582.magi_income | — | — | — | — | — | — | — |
| f8582.magi_adj | — | — | — | — | — | — | — |
| f8582.line6 | — | — | — | 1 (classm.f8582.2) | — | — | 3 |
| f8582.line7 | — | — | — | — | — | — | 2 (mrental.f8582.part5_prior_loss, x1sche.f3.pub925_phaseout) |
| f8582.half7 | — | — | — | — | — | — | — |
| f8582.max8 | — | — | — | — | — | — | — |
| f8582.line8 | — | — | — | — | — | — | 5 |
| f8582.line9 | — | — | — | 1 (classm.f8582.2) | — | — | 12 |
| f8582.line10 | — | — | — | 1 (classm.f8582.2) | — | — | 2 (mrental.f8582.part5_prior_loss, x1sche.f4.two_properties) |
| f8582.line11 | — | — | — | 1 (classm.f8582.2) | — | — | 4 |
| f8582.p6_total_rental | — | — | — | — | — | — | — |
| f8582.p6_total | — | — | — | 2 (classm.f8582.1, classm.f8582.3) | — | — | 1 (mrental.rental.excluded_home_beside_a_loss) |
| f8582.p7_total_rental | — | — | — | — | — | — | — |
| f8582.p7_total | — | — | — | 3 | — | — | 1 (mrental.rental.excluded_home_beside_a_loss) |
| f8582.p7_C | — | — | — | 3 | — | — | 5 |
| f8582.exception | — | — | — | — | — | — | 6 |
| f8582.deductions | — | — | — | — | — | — | — |
| f8582.required | — | — | — | — | — | — | 13 |

Unasserted lines: f8582.zero, f8582.line1a_rental, f8582.p4a, f8582.line2a_rental, f8582.p5a, f8582.line1b_rental, f8582.p4b, f8582.line2b_rental, f8582.p5b, f8582.line1c_rental, f8582.p4c, f8582.line2c_rental, f8582.p5c, f8582.loss1d, f8582.loss3, f8582.line4_both, f8582.part2, f8582.magi_income, f8582.magi_adj, f8582.half7, f8582.max8, f8582.p6_total_rental, f8582.p7_total_rental, f8582.deductions

## Form 8606 — Nondeductible IRAs, Part I (nondeductible contributions with no 2025 distribution), one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8606.files | — | — | — | 1 (classm.f8606.1) | — | — | — |
| f8606.line1 | — | — | — | — | — | — | 8 |
| f8606.line2 | — | — | — | — | — | — | 7 |
| f8606.line3 | — | — | — | — | — | — | 8 |
| f8606.dist | — | — | — | — | — | — | — |
| f8606.line14 | — | — | — | — | — | — | 8 |

Unasserted lines: f8606.dist

## Form 8853, Section C — long-term care insurance contracts, one per insured person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8853c.zero | — | — | — | — | — | — | — |
| f8853c.no | — | — | — | — | — | — | — |
| f8853c.periodic | — | — | — | — | — | — | — |
| f8853c.line17 | — | — | — | — | — | — | — |
| f8853c.line17_if_periodic | — | — | — | — | — | — | — |
| f8853c.line18 | — | — | — | 3 | — | — | — |
| f8853c.line19 | — | — | — | — | — | — | — |
| f8853c.line19_if_periodic | — | — | — | — | — | — | — |
| f8853c.line20 | — | — | — | 3 | — | — | 3 |
| f8853c.has_periodic | — | — | — | — | — | — | — |
| f8853c.nonqualified | — | — | — | — | — | — | — |
| f8853c.has_line17 | — | — | — | — | — | — | — |
| f8853c.nonqualified_if_periodic | — | — | — | — | — | — | — |
| f8853c.others_paid | — | — | — | — | — | — | — |
| f8853c.others_paid_if_periodic | — | — | — | — | — | — | — |
| f8853c.rate_changed | — | — | — | — | — | — | — |
| f8853c.rate_changed_if_periodic | — | — | — | — | — | — | — |
| f8853c.days | — | — | — | — | — | — | — |
| f8853c.rate | — | — | — | — | — | — | — |
| f8853c.line21_figured | — | — | — | — | — | — | — |
| f8853c.line21 | — | — | — | 3 | — | — | 3 |
| f8853c.line22 | — | — | — | — | — | — | — |
| f8853c.line22_if_periodic | — | — | — | — | — | — | — |
| f8853c.line23 | — | — | — | 3 | — | — | 2 (x2s1o.f8853c.per_diem_excess, x2s1o.f8853c.costs_larger) |
| f8853c.line24 | — | — | — | — | — | — | — |
| f8853c.line24_if_periodic | — | — | — | — | — | — | — |
| f8853c.contract_before_ltc_date | — | — | — | — | — | — | — |
| f8853c.has_line24 | — | — | — | — | — | — | — |
| f8853c.contract_before_ltc_date_if_reimbursed | — | — | — | — | — | — | — |
| f8853c.line25 | — | — | — | 3 | — | — | 4 |
| f8853c.line26 | — | — | — | 3 | — | — | 10 |

Unasserted lines: f8853c.zero, f8853c.no, f8853c.line17_if_periodic, f8853c.line19_if_periodic, f8853c.has_periodic, f8853c.has_line17, f8853c.nonqualified_if_periodic, f8853c.others_paid_if_periodic, f8853c.rate_changed_if_periodic, f8853c.rate, f8853c.line21_figured, f8853c.line22_if_periodic, f8853c.line24_if_periodic, f8853c.has_line24, f8853c.contract_before_ltc_date_if_reimbursed

## Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8863.paid | — | — | — | — | — | — | — |
| f8863.zero | — | — | — | — | — | — | — |
| f8863.claimed_count | — | — | — | — | — | — | 1 (stage19.f8863.claimed_person_answer) |
| f8863.none_claimed | — | — | — | — | — | — | 2 (dep.edu_claimed_no_credit, dep.edu_claimable_not_claimed) |
| f8863.eligible_figured | — | — | — | — | — | — | — |
| f8863.eligible | — | — | — | — | — | — | 3 |
| f8863.aoc_person | — | — | — | — | — | — | — |
| f8863.aoc_dep | — | — | — | — | — | — | — |
| f8863.aoc_sum | — | — | — | — | — | — | — |
| f8863.line1 | 4 | — | — | 8 | — | UsTaxes: 142 compared (113 nonzero), 70 excluded | 13 |
| f8863.line2 | — | — | — | 8 | — | — | 11 |
| f8863.line3 | 1 (stage19.example.aoc_phaseout) | — | — | 8 | — | — | 13 |
| f8863.line4 | 1 (stage19.example.aoc_phaseout) | — | — | 7 | — | — | 13 |
| f8863.show_after4 | — | — | — | — | — | — | 3 |
| f8863.line5 | — | — | — | 6 | — | — | 10 |
| f8863.ban | — | — | — | — | — | — | — |
| f8863.aoc_claimed | — | — | — | — | — | — | — |
| f8863.no | — | — | — | — | — | — | — |
| f8863.ban_refused | — | — | — | — | — | — | 1 (stage19.mut.aoc_line4_zero_ban) |
| f8863.line7 | 11 | — | — | 6 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded | 14 |
| f8863.kid_needed | — | — | — | — | — | — | 2 (stage19.mut.aoc_line4_zero_ban, mutation.t2.f8962_months_scveh3) |
| f8863.kid | — | — | — | — | — | — | 1 (stage19.mut.aoc_joint_line7_unasked) |
| f8863.no_refund | — | — | — | 6 | — | — | 12 |
| f8863.refund_rate | — | — | — | — | — | — | — |
| f8863.line7_40 | — | — | — | — | — | — | — |
| f8863.line8 | 12 | — | — | 4 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded; UsTaxes: 142 compared (71 nonzero), 70 excluded | 11 |
| f8863.line9 | 4 | — | — | 6; via f8863.clw2: 3 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded; UsTaxes: 142 compared (71 nonzero), 70 excluded | 12 |
| f8863.llc_person | — | — | — | — | — | — | — |
| f8863.llc_dep | — | — | — | — | — | — | — |
| f8863.llc_sum | — | — | — | — | — | — | — |
| f8863.line10 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 6 | — | — | 15 |
| f8863.llc_cap | — | — | — | — | — | — | — |
| f8863.show_llc | 2 (stage19.example.jack_kay, stage19.example.llc_phaseout) | — | — | — | — | — | — |
| f8863.line11 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | — | 7 |
| f8863.llc_rate | — | — | — | — | — | — | — |
| f8863.line12 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | UsTaxes below rule: 142 compared (30 nonzero), 70 excluded | 5 |
| f8863.line13 | — | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | — | 4 |
| f8863.line14 | 1 (stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | — | 5 |
| f8863.line15 | 1 (stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | — | 4 |
| f8863.line16 | — | — | — | 2 (classm.f8863.4.deepseek, classm.f8863.4) | — | — | 4 |
| f8863.line18 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 6; via f8863.clw1: 3 | — | PE below rule: 1625 compared (31 nonzero), 34 excluded; UsTaxes below rule: 142 compared (18 nonzero), 70 excluded | 11 |
| f8863.clw1 | — | — | — | 6 | — | — | 10 |
| f8863.clw2 | — | — | — | 6 | — | — | 10 |
| f8863.clw3 | — | — | — | 6 | — | — | 10 |
| f8863.clw4 | — | — | — | 6 | — | — | 10 |
| f8863.clw5 | — | — | — | 6 | — | — | 11 |
| f8863.clw6 | — | — | — | 6 | — | — | 10 |
| f8863.clw7 | — | — | — | 6; via f8863.line19: 3 | — | E via f8863.line19 (PE, TC) | 10 |
| f8863.line19 | 14 | — | — | 6 | — | PE: 1225 compared (83 nonzero), 418 excluded; TC: 844 compared (65 nonzero), 840 excluded; UsTaxes below rule: 96 compared (45 nonzero), 116 excluded | 15 |

Unasserted lines: f8863.zero, f8863.eligible_figured, f8863.aoc_person, f8863.aoc_dep, f8863.aoc_sum, f8863.aoc_claimed, f8863.no, f8863.refund_rate, f8863.line7_40, f8863.llc_person, f8863.llc_dep, f8863.llc_sum, f8863.llc_cap, f8863.llc_rate

## Form 8880 — Credit for Qualified Retirement Savings Contributions (the saver's credit)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8880.zero | — | — | — | — | — | — | — |
| f8880.joint | — | — | — | — | — | — | — |
| f8880.line1a | — | — | — | 8 | — | — | 34 |
| f8880.line1b | — | — | — | 4 | — | — | 9 |
| f8880.line2a | — | — | — | 6 | — | — | 35 |
| f8880.line2b | — | — | — | 3 | — | — | 11 |
| f8880.line3a | — | — | — | 6 | — | — | 33 |
| f8880.line3b | — | — | — | 3 | — | — | 9 |
| f8880.dist_this_year | — | — | — | — | — | — | — |
| f8880.prior_joint_sum | — | — | — | — | — | — | — |
| f8880.prior_joint | — | — | — | — | — | — | — |
| f8880.prior_own_a | — | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.prior_own_b | — | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.line4a | — | — | — | 8 | — | — | 37 |
| f8880.line4b_joint | — | — | — | — | — | — | — |
| f8880.line4b | — | — | — | 4 | — | — | 12 |
| f8880.line5a | — | — | — | 7 | — | — | 34 |
| f8880.line5b | — | — | — | 3 | — | — | 10 |
| f8880.cap | — | — | — | — | — | — | — |
| f8880.inelig_a | — | — | — | — | — | — | — |
| f8880.inelig_b | — | — | — | — | — | — | — |
| f8880.elig_a | — | — | — | — | — | — | — |
| f8880.elig_b | — | — | — | — | — | — | — |
| f8880.line6a_figured | — | — | — | — | — | — | — |
| f8880.line6b_figured | — | — | — | — | — | — | — |
| f8880.line6a | — | — | — | 8 | — | — | 35 |
| f8880.line6b | — | — | — | 3 | — | — | 11 |
| f8880.line7 | — | — | — | 7 | — | — | 36 |
| f8880.past7 | — | — | — | — | — | — | 2 (stage21.t067.f8880_line9_stop, stage21.t067.f8880_line7_stop) |
| f8880.line8 | — | — | — | 6 | — | — | 33 |
| f8880.line9 | — | — | — | 6 | — | — | 33 |
| f8880.past9 | — | — | — | — | — | — | 2 (stage21.t067.f8880_line9_stop, stage21.t067.f8880_line7_stop) |
| f8880.line10 | — | — | — | 4 | — | PE: 1637 compared (155 nonzero), 22 excluded | 28 |
| f8880.clw1 | — | — | — | 4 | — | — | 28 |
| f8880.clw2 | — | — | — | 4 | — | — | 28 |
| f8880.clw3 | — | — | — | 4; via f8880.line11: 2 (classm.f8880.3.deepseek, classm.f8880.4.deepseek) | — | — | 28 |
| f8880.line11 | — | — | — | 4 | — | — | 28 |
| f8880.agi_limit | — | — | — | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.no | — | — | — | — | — | — | — |
| f8880.within_limit | — | — | — | — | — | — | — |
| f8880.clw_room | — | — | — | — | — | — | — |
| f8880.line3a_counted | — | — | — | — | — | — | — |
| f8880.line3b_counted | — | — | — | — | — | — | — |
| f8880.contrib_counted | — | — | — | — | — | — | — |
| f8880.has_contrib | — | — | — | — | — | — | — |
| f8880.can_take_contrib | — | — | — | — | — | — | — |
| f8880.can_take_tax | — | — | — | — | — | — | — |
| f8880.can_take | — | — | — | — | — | — | 2 (stage15.f8880.s1, stage15.regress.f8880.agi_limit) |
| f8880.line12_figured | — | — | — | — | — | — | — |
| f8880.line12 | — | — | — | 4; via s3.line4: 3 | — | PE below rule: 1243 compared (49 nonzero), 420 excluded | 30 |

Unasserted lines: f8880.zero, f8880.joint, f8880.dist_this_year, f8880.prior_joint_sum, f8880.prior_joint, f8880.line4b_joint, f8880.cap, f8880.inelig_a, f8880.inelig_b, f8880.elig_a, f8880.elig_b, f8880.line6a_figured, f8880.line6b_figured, f8880.no, f8880.within_limit, f8880.clw_room, f8880.line3a_counted, f8880.line3b_counted, f8880.contrib_counted, f8880.has_contrib, f8880.can_take_contrib, f8880.can_take_tax, f8880.line12_figured

## Form 8889 — Health Savings Accounts (Parts I and II)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8889.one | — | — | — | — | — | — | — |
| f8889.zero | — | — | — | via f8889.line4: 5; via f8889.line10: 5 | — | — | — |
| f8889.line2 | — | — | — | — | — | — | 1 (stage16.mut.hsa_contrib_and_dist) |
| f8889.line9 | — | — | — | — | — | — | — |
| f8889.any | — | — | — | — | — | — | 1 (stage18.mut.classm_f8962_4_nov_start) |
| f8889.no | — | — | — | — | — | — | — |
| f8889.yes | — | — | — | — | — | — | — |
| f8889.owner_died | — | — | — | — | — | — | — |
| f8889.inherited_any | — | — | — | — | — | — | — |
| f8889.inherited_case | — | — | — | — | — | — | — |
| f8889.inherited_case_if_any | — | — | — | — | — | — | — |
| f8889.inh_spouse_earlier | — | — | — | — | — | — | — |
| f8889.inherited | — | — | — | — | — | — | 1 (g1f1.hsa.inherited_from_spouse_earlier) |
| f8889.archer | — | — | — | — | — | — | — |
| f8889.ira_transfer | — | — | — | — | — | — | — |
| f8889.excess_withdrawn | — | — | — | — | — | — | — |
| f8889.mfs_ask | — | — | — | — | — | — | — |
| f8889.mfs_spouse_hsa | — | — | — | — | — | — | — |
| f8889.mfs_spouse_hsa_if_asked | — | — | — | — | — | — | — |
| f8889.mfs | — | — | — | — | — | — | — |
| f8889.coverage_year | — | — | — | — | — | — | — |
| f8889.clear_all_year | — | — | — | — | — | — | — |
| f8889.fsa | — | — | — | — | — | — | — |
| f8889.spouse_family | — | — | — | — | — | — | — |
| f8889.months_eligible | — | — | — | — | — | — | — |
| f8889.months_family | — | — | — | — | — | — | — |
| f8889.bad_months_counted | — | — | — | — | — | — | — |
| f8889.counts_hold | — | — | — | — | — | — | — |
| f8889.bad_months | — | — | — | — | — | — | 7 |
| f8889.clear_if_uniform | — | — | — | — | — | — | 1 (redesign.hsa.medicare_from_october) |
| f8889.fsa_if_clear | — | — | — | — | — | — | 1 (redesign.hsa.general_fsa_all_year) |
| f8889.no_fsa | — | — | — | — | — | — | 2 (redesign.hsa.general_fsa_all_year, redesign.hsa.married_fsa_spouse_plan_not_asked) |
| f8889.eligible_all | — | — | — | — | — | — | 5 |
| f8889.sf_married | — | — | — | — | — | — | — |
| f8889.sf_eligible | — | — | — | — | — | — | 2 (redesign.hsa.married_not_clear_spouse_plan_not_asked, redesign.hsa.married_fsa_spouse_plan_not_asked) |
| f8889.ask_spouse_family | — | — | — | — | — | — | 6 |
| f8889.spouse_family_if_asked | — | — | — | — | — | — | 4 |
| f8889.fsf_possible | — | — | — | — | — | — | — |
| f8889.fsf_eligible | — | — | — | — | — | — | — |
| f8889.ask_former_spouse_family | — | — | — | — | — | — | — |
| f8889.former_spouse_family | — | — | — | — | — | — | — |
| f8889.former_spouse_family_if_asked | — | — | — | — | — | — | — |
| f8889.cov_self_only | — | — | — | — | — | — | — |
| f8889.cov_family | — | — | — | — | — | — | — |
| f8889.cov_changed | — | — | — | — | — | — | — |
| f8889.coverage_self_spouse | — | — | — | — | — | — | 1 (redesign.hsa.married_spouse_family_plan) |
| f8889.coverage_self | — | — | — | — | — | — | — |
| f8889.coverage_family | — | — | — | — | — | — | — |
| f8889.coverage | — | — | — | — | — | — | 10 |
| f8889.age55 | — | — | — | — | — | — | — |
| f8889.twelve | — | — | — | — | — | — | — |
| f8889.married_family | — | — | — | — | — | — | 4 |
| f8889.age55_line3 | — | — | — | — | — | — | 1 (stage13.mut.hsa_married_last_month_self_only) |
| f8889.self_amount | — | — | — | — | — | — | — |
| f8889.self_under55 | — | — | — | — | — | — | — |
| f8889.self_55 | — | — | — | — | — | — | — |
| f8889.age55_unmarried | — | — | — | — | — | — | 2 (audit.f8889.married_hoh_family_age55, audit.f8889.unmarried_hoh_family_age55) |
| f8889.family_amount | — | — | — | — | — | — | — |
| f8889.family_under55 | — | — | — | — | — | — | — |
| f8889.family_55 | — | — | — | — | — | — | — |
| f8889.family_extra | — | — | — | — | — | — | — |
| f8889.chart_self | — | — | — | — | — | — | — |
| f8889.chart_family | — | — | — | — | — | — | — |
| f8889.chart_total | — | — | — | — | — | — | — |
| f8889.chart_limit | — | — | — | — | — | — | — |
| f8889.all_year | — | — | — | — | — | — | — |
| f8889.changed | — | — | — | — | — | — | 1 (mutation.t2.hoh_s1a_car) |
| f8889.dec_coverage | — | — | — | — | — | — | — |
| f8889.year_self_only | — | — | — | — | — | — | — |
| f8889.year_family | — | — | — | — | — | — | — |
| f8889.dec_coverage_if_changed | — | — | — | — | — | — | — |
| f8889.dec_amount | — | — | — | — | — | — | — |
| f8889.last_month | — | — | — | — | — | — | — |
| f8889.no_last_month | — | — | — | — | — | — | — |
| f8889.use_last_month | — | — | — | — | — | — | — |
| f8889.year_same | — | — | — | — | — | — | — |
| f8889.full_year | — | — | — | — | — | — | — |
| f8889.dec_family | — | — | — | — | — | — | — |
| f8889.some_family_months | — | — | — | — | — | — | — |
| f8889.family_any_time | — | — | — | — | — | — | — |
| f8889.line3_changed | — | — | — | — | — | — | — |
| f8889.line3_all_year | — | — | — | — | — | — | — |
| f8889.line3_last_month | — | — | — | — | — | — | — |
| f8889.line3_part_year | — | — | — | — | — | — | — |
| f8889.line3_months | — | — | — | — | — | — | — |
| f8889.line3 | — | — | — | 20 | — | UsTaxes: 159 compared (159 nonzero), 62 excluded | 37 |
| f8889.line4 | — | — | — | 20 | — | — | — |
| f8889.line5 | — | — | — | 20 | — | UsTaxes: 159 compared (159 nonzero), 62 excluded | 3 |
| f8889.family_year | — | — | — | — | — | — | 1 (stage16.hsa.engineering.helper_arithmetic_and_boundary) |
| f8889.family_dec_year | — | — | — | — | — | — | — |
| f8889.family_counted | — | — | — | — | — | — | — |
| f8889.step1_total | — | — | — | — | — | — | — |
| f8889.step1_line3 | — | — | — | — | — | — | — |
| f8889.step1 | — | — | — | — | — | — | 3 |
| f8889.step1_x2 | — | — | — | — | — | — | — |
| f8889.two | — | — | — | — | — | — | — |
| f8889.share_equal | — | — | — | — | — | — | — |
| f8889.allocation | — | — | — | — | — | — | — |
| f8889.allocated | — | — | — | — | — | — | — |
| f8889.share_raw | — | — | — | — | — | — | — |
| f8889.allocation_bad | — | — | — | — | — | — | 1 (mutation.t2.f8889.last_month_self_only_allocation) |
| f8889.share | — | — | — | — | — | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.self_year | — | — | — | — | — | — | 1 (stage16.hsa.engineering.helper_arithmetic_and_boundary) |
| f8889.self_counted | — | — | — | — | — | — | — |
| f8889.self_all | — | — | — | — | — | — | 1 (mutation.t2.f8889.last_month_self_only_allocation) |
| f8889.self_family_months | — | — | — | — | — | — | — |
| f8889.self_dec_year | — | — | — | — | — | — | — |
| f8889.self_in_family | — | — | — | — | — | — | — |
| f8889.step4_total | — | — | — | — | — | — | — |
| f8889.step4 | — | — | — | — | — | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.line6_split | — | — | — | — | — | — | — |
| f8889.split | — | — | — | — | — | — | — |
| f8889.line6 | — | — | — | 20 | — | UsTaxes below rule: 94 compared (94 nonzero), 127 excluded | 14 |
| f8889.additional | — | — | — | — | — | — | — |
| f8889.line7_year | — | — | — | — | — | — | — |
| f8889.line7_counted | — | — | — | — | — | — | — |
| f8889.line7_total | — | — | — | — | — | — | — |
| f8889.line7_worksheet | — | — | — | — | — | — | — |
| f8889.line7_applies | — | — | — | — | — | — | — |
| f8889.line7 | — | — | — | 20 | — | — | 7 |
| f8889.line8 | — | — | — | 20 | — | UsTaxes: 125 compared (125 nonzero), 96 excluded | 6 |
| f8889.line10 | — | — | — | 20 | — | — | — |
| f8889.line11 | — | — | — | 20 | — | UsTaxes: 221 compared (104 nonzero), 0 excluded | — |
| f8889.line12 | — | — | — | 20 | — | OpenTaxSolver: 257 compared (257 nonzero), 0 excluded; UsTaxes: 125 compared (125 nonzero), 96 excluded | 3 |
| f8889.employer_in_box1 | — | — | — | — | — | — | — |
| f8889.excess | — | — | — | — | — | — | — |
| f8889.over_limit | — | — | — | — | — | — | — |
| f8889.not_in_box1 | — | — | — | — | — | — | — |
| f8889.excess_own | — | — | — | — | — | — | — |
| f8889.excess_employer | — | — | — | — | — | — | — |
| f8889.excess_sum | — | — | — | — | — | — | — |
| f8889.excess_amt | — | — | — | — | — | — | 2 (redesign.hsa.distributions_only_coverage_unread, redesign.hsa.general_fsa_all_year) |
| f8889.covered_12 | — | — | — | — | — | — | 6 |
| f8889.not_covered_12 | — | — | — | — | — | — | 1 (redesign.hsa.testing_kept_age_unanswered) |
| f8889.ask_testing | — | — | — | — | — | — | 10 |
| f8889.ira_prior | — | — | — | — | — | — | — |
| f8889.ira_prior_if_asked | — | — | — | — | — | — | 4 |
| f8889.ira_gap | — | — | — | — | — | — | — |
| f8889.ira_gap_if_prior | — | — | — | — | — | — | — |
| f8889.ira_failed | — | — | — | — | — | — | 1 (g1f1.hsa.ira_testing_period_ended) |
| f8889.ask_last_month_prior | — | — | — | — | — | — | 4 |
| f8889.testing_prior | — | — | — | — | — | — | — |
| f8889.testing_prior_if_asked | — | — | — | — | — | — | 4 |
| f8889.testing_if_asked | — | — | — | — | — | — | 5 |
| f8889.testing_failed_figured | — | — | — | — | — | — | 1 (g1f1.hsa.testing_failed_by_disability) |
| f8889.disabled | — | — | — | — | — | — | — |
| f8889.disabled_if_failed | — | — | — | — | — | — | — |
| f8889.testing_failed | — | — | — | — | — | — | 13 |
| f8889.line13_figured | — | — | — | — | — | — | — |
| f8889.line13_none | — | — | — | — | — | — | — |
| f8889.line13 | — | — | — | 20 | — | OpenTaxSolver: 257 compared (257 nonzero), 0 excluded; UsTaxes: 1331 compared (152 nonzero), 369 excluded | 61 |
| f8889.line14a | — | — | — | — | — | — | 6 |
| f8889.has_dist | — | — | — | — | — | — | — |
| f8889.dist_code | — | — | — | — | — | — | — |
| f8889.dist_code_if_dist | — | — | — | — | — | — | 1 (redesign.hsa.dist_code_not_asked) |
| f8889.mistake_repaid | — | — | — | — | — | — | — |
| f8889.loan | — | — | — | — | — | — | — |
| f8889.medical_all | — | — | — | — | — | — | — |
| f8889.medical_all_if_dist | — | — | — | — | — | — | 1 (redesign.hsa.medical_all_not_asked) |
| f8889.rollover | — | — | — | — | — | — | — |
| f8889.rollover_bad | — | — | — | — | — | — | 1 (mutation.t2.f8889.rollover_no_dist) |
| f8889.line14b | — | — | — | 20 | — | — | 12 |
| f8889.line14c | — | — | — | 20 | — | — | 15 |
| f8889.medical | — | — | — | — | — | — | — |
| f8889.medical_if_partial | — | — | — | — | — | — | 1 (redesign.hsa.medical_all) |
| f8889.line15_dist | — | — | — | — | — | — | 1 (redesign.hsa.medical_all) |
| f8889.line15 | — | — | — | 20 | — | — | 16 |
| f8889.line16_figured | — | — | — | — | — | — | 1 (stage16.refuse.f8889.unsupported_part2) |
| f8889.line16 | — | — | — | 20 | — | — | 28 |
| f8889.has_taxable | — | — | — | — | — | — | 1 (mutation.t2.f8889.rollover_no_dist) |
| f8889.line17a | — | — | — | — | — | — | 4 |
| f8889.subject_part | — | — | — | — | — | — | — |
| f8889.subject_bad | — | — | — | — | — | — | 2 (stage11.refuse.hsa_screen, stage16.hsa.engineering.helper_arithmetic_and_boundary) |
| f8889.subject_excepted | — | — | — | — | — | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.subject | — | — | — | — | — | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.line17b_figured | — | — | — | — | — | — | — |
| f8889.line17b | — | — | — | 20 | — | — | 16 |

Unasserted lines: f8889.one, f8889.no, f8889.yes, f8889.inherited_case_if_any, f8889.inh_spouse_earlier, f8889.mfs_ask, f8889.mfs_spouse_hsa_if_asked, f8889.mfs, f8889.bad_months_counted, f8889.counts_hold, f8889.sf_married, f8889.fsf_possible, f8889.fsf_eligible, f8889.ask_former_spouse_family, f8889.former_spouse_family_if_asked, f8889.cov_self_only, f8889.cov_family, f8889.cov_changed, f8889.coverage_self, f8889.coverage_family, f8889.age55, f8889.twelve, f8889.self_amount, f8889.self_under55, f8889.self_55, f8889.family_amount, f8889.family_under55, f8889.family_55, f8889.family_extra, f8889.chart_self, f8889.chart_family, f8889.chart_total, f8889.chart_limit, f8889.all_year, f8889.year_self_only, f8889.year_family, f8889.dec_coverage_if_changed, f8889.dec_amount, f8889.no_last_month, f8889.use_last_month, f8889.year_same, f8889.full_year, f8889.dec_family, f8889.some_family_months, f8889.family_any_time, f8889.line3_changed, f8889.line3_all_year, f8889.line3_last_month, f8889.line3_part_year, f8889.line3_months, f8889.family_dec_year, f8889.family_counted, f8889.step1_total, f8889.step1_line3, f8889.step1_x2, f8889.two, f8889.share_equal, f8889.share_raw, f8889.self_counted, f8889.self_family_months, f8889.self_dec_year, f8889.self_in_family, f8889.step4_total, f8889.line6_split, f8889.split, f8889.additional, f8889.line7_year, f8889.line7_counted, f8889.line7_total, f8889.line7_worksheet, f8889.line7_applies, f8889.excess, f8889.over_limit, f8889.not_in_box1, f8889.excess_own, f8889.excess_employer, f8889.excess_sum, f8889.ira_gap_if_prior, f8889.disabled_if_failed, f8889.line13_figured, f8889.line13_none, f8889.has_dist, f8889.line17b_figured

## Form 8919 — Uncollected Social Security and Medicare Tax on Wages, lines 6 to 13, one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8919.files | — | — | — | — | — | — | 1 (mint.f8919.files.no_firm_wages) |
| f8919.line6 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 2 (x2pay.f8919.w3, mint.f8919.files.no_firm_wages) |
| f8919.line7 | — | — | — | — | — | — | — |
| f8919.line8 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 4 |
| f8919.line9 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 3 |
| f8919.line10 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 3 |
| f8919.rate_062 | — | — | — | — | — | — | — |
| f8919.line11 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 3 |
| f8919.rate_0145 | — | — | — | — | — | — | — |
| f8919.line12 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 2 (x2pay.f8919.w3, x2pay.f8919.w4_with_se) |
| f8919.line13 | — | — | — | 2 (classm.f8919.1, classm.f8919.2) | — | — | 3 |

Unasserted lines: f8919.line7, f8919.rate_062, f8919.rate_0145

## Form 8919, lines 1 to 5 — one row per firm that treated this person as an independent contractor

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8919firm.reason | — | — | — | — | — | — | — |
| f8919firm.wages | — | — | — | — | — | — | — |

## Form 8959 — Additional Medicare Tax on wages and self-employment income

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8959.territory_w2 | — | — | — | — | — | — | — |
| f8959.unsupported | — | — | — | — | — | — | — |
| f8959.zero | — | — | — | — | — | — | — |
| f8959.line1 | — | — | — | 3 | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 3 |
| f8959.line2 | — | — | — | 3 | — | — | 4 |
| f8959.line3 | — | — | — | 3 | — | — | 4 |
| f8959.line8 | — | — | — | 1 (classm.f8959.3) | — | — | 5 |
| f8959.line14 | — | — | — | 1 (classm.f8959.3) | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line23 | — | — | — | 3 | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line4 | — | — | — | 3 | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 3 |
| f8959.line5 | — | — | — | 3 | — | — | 2 (stage4.medicare.withholding, stage13.additional_medicare_joint) |
| f8959.line6 | 1 (stage4.official.medicare_example5) | — | — | 3 | — | UsTaxes: 1400 compared (138 nonzero), 300 excluded | 17 |
| f8959.line7 | — | — | — | 3 | — | OpenTaxSolver: 1700 compared (157 nonzero), 0 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded | 4 |
| f8959.line9 | — | — | — | 1 (classm.f8959.3) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line10 | — | — | — | 1 (classm.f8959.3) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line11 | — | — | — | 1 (classm.f8959.3) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line12 | — | — | — | 1 (classm.f8959.3) | — | — | 2 (stage4.medicare.withholding, stage14.f8959.se_above_threshold) |
| f8959.line13 | — | — | — | 1 (classm.f8959.3) | — | OpenTaxSolver below rule: 1700 compared (24 nonzero), 0 excluded | 3 |
| f8959.line15 | — | — | — | 1 (classm.f8959.3) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line16 | — | — | — | 1 (classm.f8959.3) | — | — | 2 (stage4.medicare.withholding, stage16.cleanup.f8959_line16_se_refused) |
| f8959.line17 | — | — | — | 1 (classm.f8959.3) | — | OpenTaxSolver below rule: 1700 compared (0 nonzero), 0 excluded | 1 (stage4.medicare.withholding) |
| f8959.line18 | — | — | — | 3; via s2.line11: 3 | — | PE: 1681 compared (168 nonzero), 19 excluded; TC: 1370 compared (130 nonzero), 330 excluded; OpenTaxSolver: 1700 compared (168 nonzero), 0 excluded; OpenTaxSolver: 1700 compared (168 nonzero), 0 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded | 24 |
| f8959.line19 | — | — | — | 3 | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line20 | — | — | — | 3 | — | — | 1 (stage4.medicare.withholding) |
| f8959.line21 | — | — | — | 3 | — | OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 1 (stage4.medicare.withholding) |
| f8959.line22 | — | — | — | 3 | — | OpenTaxSolver: 1700 compared (231 nonzero), 0 excluded; UsTaxes: 1400 compared (202 nonzero), 300 excluded | 1 (stage4.medicare.withholding) |
| f8959.line24 | — | — | — | 3 | — | OpenTaxSolver: 1700 compared (231 nonzero), 0 excluded; UsTaxes: 1400 compared (202 nonzero), 300 excluded | 6 |

Unasserted lines: f8959.unsupported, f8959.zero

## Form 8960 — wage, interest, dividend and securities slice

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8960.unsupported | — | — | — | — | — | — | — |
| f8960.prior_2i | — | — | — | — | — | — | — |
| f8960.carryforward_adj | — | — | — | — | — | — | 1 (stage20.niit_adjustment_below_threshold) |
| f8960.refund | — | — | — | — | — | — | — |
| f8960.allocated_taxes | — | — | — | — | — | — | — |
| f8960.zero | — | — | — | via f8960.line3: 3; via f8960.line4b: 3; via f8960.line5b: 3; via f8960.line5c: 3; via f8960.line6: 3; via f8960.line7: 3; via f8960.line9c: 3 | — | — | — |
| f8960.line1 | — | — | — | 5 | — | — | 5 |
| f8960.line2 | — | — | — | 5 | — | — | — |
| f8960.line3 | — | — | — | 5 | — | — | 3 |
| f8960.line4a | — | — | — | 5 | — | — | 3 |
| f8960.line4b | — | — | — | 5 | — | — | 3 |
| f8960.line5b | — | — | — | 5 | — | — | 5 |
| f8960.line5c | — | — | — | 5 | — | — | 4 |
| f8960.line6 | — | — | — | 5 | — | — | 3 |
| f8960.line7 | — | — | — | 5 | — | — | 5 |
| f8960.digital_nii | — | — | — | — | — | — | — |
| f8960.line9c | — | — | — | 5 | — | — | 4 |
| f8960.line10 | — | — | — | 5 | — | — | 4 |
| f8960.line4c | — | — | — | 5 | — | — | — |
| f8960.line5a | — | — | — | 5 | — | — | 2 (stage20.blind.r10, stage4.niit.loss_floor) |
| f8960.line5d | — | — | — | 5 | — | — | 1 (mexist.f8960.line5d.no_gains) |
| f8960.line8 | — | — | — | 5 | — | OpenTaxSolver: 1695 compared (1669 nonzero), 0 excluded; UsTaxes: 1395 compared (1373 nonzero), 300 excluded | 3 |
| f8960.line9a | — | — | — | 5 | — | UsTaxes below rule: 1070 compared (28 nonzero), 630 excluded | 5 |
| f8960.line9b | — | — | — | 5 | — | UsTaxes below rule: 965 compared (0 nonzero), 735 excluded | 3 |
| f8960.line9d | — | — | — | 5 | — | UsTaxes below rule: 902 compared (0 nonzero), 798 excluded | 2 (stage4.additional_taxes.combined, mexist.f8960.line9c.digital_nii) |
| f8960.line11 | — | — | — | 5 | — | OpenTaxSolver: 1540 compared (51 nonzero), 121 excluded; UsTaxes below rule: 902 compared (0 nonzero), 798 excluded | 3 |
| f8960.line12 | — | — | — | 5 | — | OpenTaxSolver: 1540 compared (1284 nonzero), 121 excluded; UsTaxes: 902 compared (749 nonzero), 798 excluded | 5 |
| f8960.line13 | — | — | — | 5 | — | — | 5 |
| f8960.line14 | — | — | — | 5 | — | — | — |
| f8960.line15 | — | — | — | 5 | — | OpenTaxSolver: 1589 compared (205 nonzero), 111 excluded; UsTaxes: 1166 compared (146 nonzero), 534 excluded | 1 (stage20.blind.r10) |
| f8960.used | — | — | — | — | — | — | — |
| f8960.line16_figured | — | — | — | — | — | — | — |
| f8960.line16 | — | — | — | 5 | — | OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; UsTaxes: 1044 compared (96 nonzero), 656 excluded | 5 |
| f8960.line17 | — | — | — | 5; via s2.line12: 3 | — | PE: 1472 compared (166 nonzero), 189 excluded; TC: 1300 compared (135 nonzero), 400 excluded; OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; UsTaxes: 1044 compared (96 nonzero), 656 excluded; UsTaxes: 1044 compared (96 nonzero), 656 excluded | 29 |
| f8960.allocation_over_5e | — | — | — | — | — | — | — |
| f8960.no | — | — | — | — | — | — | — |
| f8960.bad_allocation | — | — | — | — | — | — | — |

Unasserted lines: f8960.digital_nii, f8960.used, f8960.line16_figured, f8960.allocation_over_5e, f8960.no, f8960.bad_allocation

## Form 8962, Premium Tax Credit (Parts I to III)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8962.zero | — | — | — | — | — | — | — |
| f8962.forms | — | — | — | — | — | — | — |
| f8962.any | — | — | — | — | — | — | — |
| f8962.dependent_filer | — | — | — | — | — | — | — |
| f8962.shared_policy | — | — | — | — | — | — | — |
| f8962.divorced_enrolled | — | — | — | — | — | — | — |
| f8962.alloc | — | — | — | — | — | — | 1 (mexist.f8962.dependent_filer.no_allocation) |
| f8962.married_this_year | — | — | — | — | — | — | — |
| f8962.no | — | — | — | — | — | — | — |
| f8962.marriage | — | — | — | — | — | — | 1 (stage18.married_in_2025_single) |
| f8962.mfs_ask | — | — | — | — | — | — | — |
| f8962.mfs_exception | — | — | — | — | — | — | — |
| f8962.mfs_exception_if_mfs | — | — | — | — | — | — | — |
| f8962.mfs_three_years | — | — | — | — | — | — | — |
| f8962.mfs_three_years_if_exception | — | — | — | — | — | — | — |
| f8962.line_a | — | — | — | 10 | — | — | 3 |
| f8962.mfs_barred | — | — | — | — | — | — | — |
| f8962.other_coverage | — | — | — | — | — | — | — |
| f8962.mec_job_enrolled | — | — | — | — | — | — | — |
| f8962.mec_job_enrolled_if_other_coverage | — | — | — | — | — | — | — |
| f8962.job_offer | — | — | — | — | — | — | — |
| f8962.job_offer_if_other_coverage | — | — | — | — | — | — | — |
| f8962.mec_job_affordable | — | — | — | — | — | — | — |
| f8962.mec_job_affordable_if_job_offer | — | — | — | — | — | — | — |
| f8962.mec_government | — | — | — | — | — | — | — |
| f8962.mec_government_if_other_coverage | — | — | — | — | — | — | — |
| f8962.mec_other | — | — | — | — | — | — | — |
| f8962.mec_other_if_other_coverage | — | — | — | — | — | — | — |
| f8962.hra | — | — | — | — | — | — | — |
| f8962.not_lawful | — | — | — | — | — | — | — |
| f8962.incarcerated | — | — | — | — | — | — | — |
| f8962.no_family | — | — | — | — | — | — | — |
| f8962.medicaid_reversed | — | — | — | — | — | — | — |
| f8962.unpaid | — | — | — | — | — | — | — |
| f8962.a_zero_paid | — | — | — | — | — | — | — |
| f8962.other | — | — | — | — | — | — | 9 |
| f8962.midmonth_start | — | — | — | — | — | — | — |
| f8962.premium_refunded | — | — | — | — | — | — | — |
| f8962.premium_adjust | — | — | — | — | — | — | 1 (mutation.m2.f8962.premium_refunded) |
| f8962.void_forms | — | — | — | — | — | — | — |
| f8962.void_form | — | — | — | — | — | — | — |
| f8962.two_counted | — | — | — | — | — | — | 11 |
| f8962.b_zero | — | — | — | — | — | — | 11 |
| f8962.same_state_counted | — | — | — | — | — | — | — |
| f8962.deps | — | — | — | — | — | — | 1 (stage18.mut.unclaimed_relative) |
| f8962.line1 | — | — | — | 20 | — | — | 23 |
| f8962.ws1_1 | — | — | — | — | — | — | — |
| f8962.ws1_2 | — | — | — | — | — | — | — |
| f8962.ws1_3 | — | — | — | — | — | — | 1 (stage18.refuse.form_2555) |
| f8962.ws1_4 | — | — | — | — | — | — | — |
| f8962.line2a | — | — | — | 20 | — | — | 21 |
| f8962.line2b | — | — | — | 20 | — | — | 2 (stage18.blind.p15, stage18.mut.unclaimed_relative) |
| f8962.income_total | — | — | — | — | — | — | — |
| f8962.line3 | — | — | — | 20 | — | PE: 129 compared (129 nonzero), 2 excluded | 22 |
| f8962.fpl_table | — | — | — | — | — | — | — |
| f8962.big_family | — | — | — | — | — | — | 1 (stage18.mut.family_of_20) |
| f8962.line4 | — | — | — | 20 | — | — | 22 |
| f8962.line5 | — | — | — | 20 | — | — | 22 |
| f8962.aptc | — | — | — | — | — | — | 1 (stage18.mut.below_100_no_advance) |
| f8962.aptc_total | — | — | — | via f8962.line11f: 7 | — | — | — |
| f8962.estimate_100 | — | — | — | — | — | — | — |
| f8962.applicable_figured | — | — | — | — | — | — | — |
| f8962.applicable | — | — | — | — | — | — | 1 (stage18.mut.below_100_no_advance) |
| f8962.show_applicable | — | — | — | — | — | — | 2 (stage18.blind.p17, mint.f8962.show_applicable.no_1095a) |
| f8962.filing | — | — | — | — | — | — | 1 (stage18.blind.p8) |
| f8962.alien_below | — | — | — | — | — | — | — |
| f8962.alien_not_barred | — | — | — | — | — | — | — |
| f8962.alien_branch | — | — | — | — | — | — | 1 (stage18.mut.alien_below_100_no_advance) |
| f8962.line7 | — | — | — | 15 | — | — | 20 |
| f8962.line8a | — | — | — | 15; via f8962.line11c: 5 | — | PE: 125 compared (103 nonzero), 7 excluded; UsTaxes below rule: 36 compared (36 nonzero), 73 excluded | 20 |
| f8962.line8b | — | — | — | 15; via f8962.line12c: 1 (classm.f8962.2.deepseek); via f8962.line13c: 1 (classm.f8962.2.deepseek); via f8962.line14c: 1 (classm.f8962.2.deepseek); via f8962.line15c: 1 (classm.f8962.2.deepseek); via f8962.line16c: 1 (classm.f8962.2.deepseek); via f8962.line17c: 1 (classm.f8962.2.deepseek); via f8962.line18c: 1 (classm.f8962.2.deepseek); via f8962.line19c: 1 (classm.f8962.2.deepseek); via f8962.line20c: 1 (classm.f8962.2.deepseek); via f8962.line21c: 1 (classm.f8962.2.deepseek); via f8962.line22c: 2 (classm.f8962.2.deepseek, classm.f8962.4.deepseek); via f8962.line23c: 2 (classm.f8962.2.deepseek, classm.f8962.4.deepseek) | — | — | 20 |
| f8962.line9 | — | — | — | 20 | — | — | 3 |
| f8962.nonuniform | — | — | — | — | — | — | — |
| f8962.line10 | — | — | — | 20 | — | — | 31 |
| f8962.show_annual | 1 (stage4.official.medicare_example5) | — | — | — | — | — | 1 (stage18.blind.p14) |
| f8962.show_annual_calc | 1 (stage4.official.medicare_example5) | — | — | — | — | — | 1 (stage18.blind.p8) |
| f8962.line11a | — | — | — | 12 | — | — | 18 |
| f8962.line11b | — | — | — | 12 | — | — | 18 |
| f8962.line11c | — | — | — | 9 | — | — | 17 |
| f8962.line11d | — | — | — | 9 | — | PE: 114 compared (60 nonzero), 18 excluded | 17 |
| f8962.line11e | — | — | — | 9 | — | PE: 114 compared (60 nonzero), 18 excluded; UsTaxes below rule: 36 compared (11 nonzero), 73 excluded | 18 |
| f8962.line11f | — | — | — | 14 | — | — | 18 |
| f8962.show_jan | — | — | — | — | — | — | 5 |
| f8962.show_jan_calc | — | — | — | — | — | — | 3 |
| f8962.line12a | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 5 |
| f8962.line12b | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 7 |
| f8962.line12c | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 4 |
| f8962.line12d | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 4 |
| f8962.line12e | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 5 |
| f8962.line12f | — | — | — | 3 | — | — | 5 |
| f8962.show_feb | — | — | — | — | — | — | 4 |
| f8962.show_feb_calc | — | — | — | — | — | — | 3 |
| f8962.line13a | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 4 |
| f8962.line13b | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 5 |
| f8962.line13c | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 3 |
| f8962.line13d | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 3 |
| f8962.line13e | — | — | — | 2 (classm.f8962.2.deepseek, classm.f8962.2) | — | — | 3 |
| f8962.line13f | — | — | — | 3 | — | — | 3 |
| f8962.show_mar | — | — | — | — | — | — | 4 |
| f8962.show_mar_calc | — | — | — | — | — | — | 3 |
| f8962.line14a | — | — | — | 3 | — | — | 4 |
| f8962.line14b | — | — | — | 3 | — | — | 7 |
| f8962.line14c | — | — | — | 3 | — | — | 3 |
| f8962.line14d | — | — | — | 3 | — | — | 3 |
| f8962.line14e | — | — | — | 3 | — | — | 3 |
| f8962.line14f | — | — | — | 4 | — | — | 3 |
| f8962.show_apr | — | — | — | — | — | — | 5 |
| f8962.show_apr_calc | — | — | — | — | — | — | 3 |
| f8962.line15a | — | — | — | 4 | — | — | 4 |
| f8962.line15b | — | — | — | 4 | — | — | 5 |
| f8962.line15c | — | — | — | 4 | — | — | 4 |
| f8962.line15d | — | — | — | 4 | — | — | 4 |
| f8962.line15e | — | — | — | 4 | — | — | 4 |
| f8962.line15f | — | — | — | 5 | — | — | 4 |
| f8962.show_may | — | — | — | — | — | — | 4 |
| f8962.show_may_calc | — | — | — | — | — | — | 3 |
| f8962.line16a | — | — | — | 4 | — | — | 4 |
| f8962.line16b | — | — | — | 4 | — | — | 5 |
| f8962.line16c | — | — | — | 4 | — | — | 4 |
| f8962.line16d | — | — | — | 4 | — | — | 4 |
| f8962.line16e | — | — | — | 4 | — | — | 4 |
| f8962.line16f | — | — | — | 5 | — | — | 4 |
| f8962.show_jun | — | — | — | — | — | — | 3 |
| f8962.show_jun_calc | — | — | — | — | — | — | 2 (stage18.mut.alternate_months_odd, stage18.mut.alternate_months_even) |
| f8962.line17a | — | — | — | 4 | — | — | 4 |
| f8962.line17b | — | — | — | 4 | — | — | 5 |
| f8962.line17c | — | — | — | 4 | — | — | 4 |
| f8962.line17d | — | — | — | 4 | — | — | 4 |
| f8962.line17e | — | — | — | 4 | — | — | 5 |
| f8962.line17f | — | — | — | 5 | — | — | 4 |
| f8962.show_jul | — | — | — | — | — | — | 3 |
| f8962.show_jul_calc | — | — | — | — | — | — | 2 (stage18.mut.alternate_months_odd, stage18.mut.alternate_months_even) |
| f8962.line18a | — | — | — | 4 | — | — | 6 |
| f8962.line18b | — | — | — | 4 | — | — | 9 |
| f8962.line18c | — | — | — | 4 | — | — | 5 |
| f8962.line18d | — | — | — | 4 | — | — | 5 |
| f8962.line18e | — | — | — | 4 | — | — | 7 |
| f8962.line18f | — | — | — | 5 | — | — | 5 |
| f8962.show_aug | — | — | — | — | — | — | 4 |
| f8962.show_aug_calc | — | — | — | — | — | — | 3 |
| f8962.line19a | — | — | — | 4 | — | — | 5 |
| f8962.line19b | — | — | — | 4 | — | — | 5 |
| f8962.line19c | — | — | — | 4 | — | — | 4 |
| f8962.line19d | — | — | — | 4 | — | — | 4 |
| f8962.line19e | — | — | — | 4 | — | — | 4 |
| f8962.line19f | — | — | — | 5 | — | — | 4 |
| f8962.show_sep | — | — | — | — | — | — | 3 |
| f8962.show_sep_calc | — | — | — | — | — | — | 2 (stage18.mut.alternate_months_odd, stage18.mut.alternate_months_even) |
| f8962.line20a | — | — | — | 4 | — | — | 5 |
| f8962.line20b | — | — | — | 4 | — | — | 6 |
| f8962.line20c | — | — | — | 4 | — | — | 4 |
| f8962.line20d | — | — | — | 4 | — | — | 4 |
| f8962.line20e | — | — | — | 4 | — | — | 4 |
| f8962.line20f | — | — | — | 5 | — | — | 4 |
| f8962.show_oct | — | — | — | — | — | — | 4 |
| f8962.show_oct_calc | — | — | — | — | — | — | 3 |
| f8962.line21a | — | — | — | 4 | — | — | 5 |
| f8962.line21b | — | — | — | 4 | — | — | 6 |
| f8962.line21c | — | — | — | 4 | — | — | 4 |
| f8962.line21d | — | — | — | 4 | — | — | 4 |
| f8962.line21e | — | — | — | 4 | — | — | 4 |
| f8962.line21f | — | — | — | 5 | — | — | 4 |
| f8962.show_nov | — | — | — | — | — | — | 4 |
| f8962.show_nov_calc | — | — | — | — | — | — | 3 |
| f8962.line22a | — | — | — | 5 | — | — | 6 |
| f8962.line22b | — | — | — | 5 | — | — | 7 |
| f8962.line22c | — | — | — | 5 | — | — | 4 |
| f8962.line22d | — | — | — | 5 | — | — | 4 |
| f8962.line22e | — | — | — | 5 | — | — | 4 |
| f8962.line22f | — | — | — | 6 | — | — | 5 |
| f8962.show_dec | — | — | — | — | — | — | 4 |
| f8962.show_dec_calc | — | — | — | — | — | — | 3 |
| f8962.line23a | — | — | — | 5 | — | — | 6 |
| f8962.line23b | — | — | — | 5 | — | — | 10 |
| f8962.line23c | — | — | — | 5 | — | — | 4 |
| f8962.line23d | — | — | — | 5 | — | — | 4 |
| f8962.line23e | — | — | — | 5 | — | — | 5 |
| f8962.line23f | — | — | — | 6 | — | — | 5 |
| f8962.monthly_e | — | — | — | — | — | — | — |
| f8962.monthly_f | — | — | — | — | — | — | — |
| f8962.allowed | — | — | — | — | — | — | — |
| f8962.line24 | — | — | — | 19 | — | — | 52 |
| f8962.line25 | — | — | — | 20 | — | UsTaxes below rule: 36 compared (26 nonzero), 73 excluded | 40 |
| f8962.net | — | — | — | — | — | — | 5 |
| f8962.line26 | — | — | — | 7 | — | PE below rule: 29 compared (18 nonzero), 103 excluded; UsTaxes below rule: 36 compared (6 nonzero), 73 excluded | 25 |
| f8962.excess | — | — | — | — | — | — | 4 |
| f8962.line27 | — | — | — | 12 | — | — | 6 |
| f8962.repay_200 | — | — | — | — | — | — | — |
| f8962.repay_300 | — | — | — | — | — | — | — |
| f8962.repay_400 | — | — | — | — | — | — | — |
| f8962.show_28 | — | — | — | — | — | — | 2 (stage18.blind.p4, stage18.blind.p10) |
| f8962.line28 | — | — | — | 9 | — | — | 5 |
| f8962.line29 | — | — | — | 12 | — | UsTaxes below rule: 36 compared (25 nonzero), 73 excluded | 7 |
| f8962.income_100 | — | — | — | — | — | — | — |
| f8962.estimate_exception | — | — | — | — | — | — | — |
| f8962.alien_from_income | — | — | — | — | — | — | — |
| f8962.b_zero_month | — | — | — | — | — | — | — |

Unasserted lines: f8962.zero, f8962.forms, f8962.any, f8962.dependent_filer, f8962.no, f8962.mfs_ask, f8962.mfs_exception_if_mfs, f8962.mfs_three_years_if_exception, f8962.mfs_barred, f8962.mec_job_enrolled_if_other_coverage, f8962.job_offer_if_other_coverage, f8962.mec_job_affordable_if_job_offer, f8962.mec_government_if_other_coverage, f8962.mec_other_if_other_coverage, f8962.void_forms, f8962.void_form, f8962.ws1_1, f8962.ws1_2, f8962.ws1_4, f8962.income_total, f8962.applicable_figured, f8962.alien_not_barred, f8962.nonuniform, f8962.monthly_e, f8962.monthly_f, f8962.allowed, f8962.repay_200, f8962.repay_300, f8962.repay_400, f8962.income_100, f8962.estimate_exception, f8962.alien_from_income, f8962.b_zero_month

## Form 8995 — Qualified Business Income Deduction Simplified Computation

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (296 nonzero), 0 excluded | 3 |
| f8995.line3 | — | — | — | 3 | — | — | 1 (stage14.qbi.carryforward) |
| f8995.line4_sum | — | — | — | — | — | — | — |
| f8995.line4 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (259 nonzero), 0 excluded | 2 (stage14.qbi.carryforward, stage14.sc.loss) |
| f8995.line5 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (259 nonzero), 0 excluded | 2 (stage14.qbi.carryforward, stage14.sc.basic) |
| f8995.line7 | — | — | — | 3 | — | — | — |
| f8995.loss | — | — | — | — | — | — | — |
| f8995.line16 | — | — | — | 3 | — | — | 1 (stage14.sc.loss) |
| f8995.line17 | — | — | — | 3 | — | — | — |
| f8995.line6 | — | — | — | 3 | — | — | — |
| f8995.line8 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (274 nonzero), 0 excluded | — |
| f8995.line9 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (274 nonzero), 0 excluded | — |
| f8995.line10 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (483 nonzero), 0 excluded | — |
| f8995.line11 | — | — | — | 3 | — | OpenTaxSolver: 387 compared (356 nonzero), 130 excluded | — |
| f8995.line12 | — | — | — | 3 | — | — | — |
| f8995.line13 | — | — | — | 3 | — | OpenTaxSolver: 387 compared (349 nonzero), 130 excluded | — |
| f8995.line14 | — | — | — | 3 | — | OpenTaxSolver: 387 compared (349 nonzero), 130 excluded | 1 (stage14.sc.basic) |
| f8995.line15 | — | — | — | 3 | — | OpenTaxSolver: 387 compared (329 nonzero), 130 excluded | 8 |

Unasserted lines: f8995.line4_sum, f8995.loss

## Form 8995-A — Part IV dividend-only computation

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8995a.line27 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line29 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line38 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line40 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line28 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line30 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line31 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line32 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line33 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line34 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line35 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line36 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line37 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | — |
| f8995a.line39 | — | — | — | 2 (classm.f8995a.1, classm.f8995a.2) | — | — | 6 |

## Foreign tax credit — election without Form 1116, or Form 1116

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ftc.taxes | — | — | — | — | — | — | — |
| ftc.asked | — | — | — | — | — | — | — |
| ftc.taxes_if_asked | — | — | — | — | — | — | — |
| ftc.carryover | — | — | — | — | — | — | — |
| ftc.carryover_ask | — | — | — | — | — | — | 2 (redesign.credits.refuse.ftc_carryover_prior_return, redesign.credits.prior_not_asked) |
| ftc.carryover_if_asked | — | — | — | — | — | — | 2 (redesign.credits.foreign_none, redesign.credits.prior_not_asked) |
| ftc.all_passive | — | — | — | — | — | — | — |
| ftc.statements | — | — | — | — | — | — | — |
| ftc.eligible | — | — | — | — | — | — | — |
| ftc.elect | — | — | — | — | — | — | — |
| ftc.yes | — | — | — | — | — | — | — |
| ftc.limit | — | — | — | — | — | — | — |
| ftc.zero | — | — | — | — | — | — | — |
| ftc.has_tax | — | — | — | — | — | — | 4 |
| ftc.no | — | — | — | — | — | — | — |
| ftc.all_passive_if_tax | — | — | — | — | — | — | — |
| ftc.statements_if_tax | — | — | — | — | — | — | — |
| ftc.eligible_if_tax | — | — | — | — | — | — | — |
| ftc.elect_if_tax | — | — | — | — | — | — | — |
| ftc.needs1116 | — | — | — | — | — | — | 3 |
| ftc.carryover_no_tax | — | — | — | — | — | — | 1 (f1116.m1116_carryover_unanswered_with_tax) |
| ftc.regular_tax | — | — | — | — | — | — | — |
| ftc.limited | — | — | — | — | — | — | — |
| ftc.credit_tax | — | — | — | — | — | — | — |
| ftc.credit | — | — | — | via f2441.clw2 → s3.line1: 3; via s3.line1: 3 | — | — | 56 |

Unasserted lines: ftc.asked, ftc.taxes_if_asked, ftc.elect, ftc.yes, ftc.limit, ftc.zero, ftc.no, ftc.all_passive_if_tax, ftc.statements_if_tax, ftc.eligible_if_tax, ftc.elect_if_tax, ftc.regular_tax, ftc.limited, ftc.credit_tax

## 28% Rate Gain Worksheet — distribution-only path

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| g28.reached | — | — | — | — | — | — | — |
| g28.line1 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — | — |
| g28.line2 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — | — |
| g28.line3 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — | — |
| g28.line5 | — | — | — | 2 (classm.g28.1, classm.g28.2) | — | — | — |
| g28.line4 | — | — | — | 3 | — | — | — |
| g28.line6 | — | — | — | 3; via u1250.line15: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | — | — |
| g28.combined | — | — | — | — | — | — | — |
| g28.line7 | — | — | — | 3 | — | — | 2 (stage16.sd.line17_no_skips_18, stage4.feeders.shortloss) |

Unasserted lines: g28.reached, g28.combined

## Form 8283 — groups of similar noncash property

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gift.deduction | — | — | — | — | — | — | — |
| gift.public_securities | — | — | — | — | — | — | — |
| gift.special | — | — | — | — | — | — | — |
| gift.over_5000 | — | — | — | 1 (classm.gift.1) | — | — | — |
| gift.not_public | — | — | — | 1 (classm.gift.1) | — | — | — |
| gift.no | — | — | — | — | — | — | — |
| gift.section_b | — | — | — | 1 (classm.gift.1) | — | — | — |
| gift.allowed | — | — | — | 1 (classm.gift.1) | — | — | — |

Unasserted lines: gift.no

## Household facts for dependents and head of household

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| household.persons | — | — | — | — | — | — | — |
| household.taxpayers | — | — | — | — | — | — | — |
| household.spouses | — | — | — | — | — | — | — |
| household.roster_ok | — | — | — | — | — | — | 3 |
| household.roster_bad | — | — | — | — | — | — | 1 (mutation.t3.roster_ok_role_unanswered) |
| household.hsa_people | — | — | — | — | — | — | — |
| household.hsa_both | — | — | — | — | — | — | — |
| household.hsa_split_count | — | — | — | — | — | — | — |
| household.hsa_agreed_count | — | — | — | — | — | — | — |
| household.hsa_step1_sum | — | — | — | — | — | — | 1 (stage19.mut.hsa_one_form_no_split) |
| household.hsa_share_sum | — | — | — | — | — | — | 1 (stage19.mut.hsa_one_form_no_split) |
| household.work_ssn_count | — | — | — | — | — | — | — |
| household.any_work_ssn | — | — | — | — | — | — | 1 (audit.eic.filer_eic_ssn_without_work_ssn) |
| household.eic_ssn_count | — | — | — | — | — | — | — |
| household.all_eic_ssn | — | — | — | — | — | — | 2 (audit.eic.filer_eic_ssn_without_work_ssn, audit.eic.filer_without_eic_ssn) |
| household.birth_year_bad_count | — | — | — | — | — | — | — |
| household.birth_year_bad | — | — | — | — | — | — | 1 (mutation.m1.person.birth_year_after_tax_year) |
| household.under16_count | — | — | — | — | — | — | — |
| household.filer_under16 | — | — | — | — | — | — | 1 (audit.household.filer_under16) |
| household.tin_count | — | — | — | — | — | — | — |
| household.all_tin | — | — | — | — | — | — | — |
| household.id_count | — | — | — | — | — | — | — |
| household.ctc_ssn | — | — | — | — | — | — | 1 (stage8.mut.mfj_spouse_itin_applied_ctc) |
| household.taxpayer_work_ssn_count | — | — | — | — | — | — | — |
| household.taxpayer_work_ssn | — | — | — | — | — | — | — |
| household.home_cost | — | — | — | — | — | — | — |
| household.considered_unmarried | — | — | — | — | — | — | — |
| household.considered_unmarried_if_married | — | — | — | — | — | — | — |
| household.not_married | — | — | — | — | — | — | — |
| household.unmarried | — | — | — | — | — | — | — |
| household.ever_married | — | — | — | — | — | — | — |
| household.status_states_marriage | — | — | — | — | — | — | — |
| household.marriage_possible | — | — | — | — | — | — | — |
| household.married_dec31 | — | — | — | — | — | — | — |
| household.married | — | — | — | — | — | — | — |
| household.community_property | — | — | — | — | — | — | — |
| household.hoh_cp_married | — | — | — | — | — | — | — |
| household.hoh_community_property | — | — | — | — | — | — | 4 |
| household.credit_disallowed | — | — | — | — | — | — | — |
| household.no | — | — | — | — | — | — | — |
| household.eic_above_zero | — | — | — | — | — | — | — |
| household.eic_claimed | — | — | — | — | — | — | 2 (mutation.household.eic_ineligible_no_8862, mutation.household.hoh_community_property_eic_not_claimed) |
| household.claims_8862_credit | — | — | — | — | — | — | 1 (mutation.household.eic_ineligible_no_8862) |
| household.credit_disallowed_if_claimed | — | — | — | — | — | — | — |
| household.ctc_disallowed_claim | — | — | — | — | — | — | 1 (f2.t101.credit_disallowed_no_credit_claimed) |
| household.eic_disallowed_claim | — | — | — | — | — | — | 2 (f2.t101.credit_disallowed_no_credit_claimed, stage9.mut.eic_no_child_credit_disallowed) |
| household.test1_persons | — | — | — | — | — | — | 24 |
| household.test2_persons | — | — | — | — | — | — | 25 |
| household.test2_absence_persons | — | — | — | — | — | — | — |
| household.hoh_absence_from_test1 | — | — | — | — | — | — | — |
| household.hoh_absence_from_cost | — | — | — | — | — | — | — |
| household.hoh_absence_from_test2 | — | — | — | — | — | — | — |
| household.no_test2_persons | — | — | — | — | — | — | — |
| household.any_test2_absence | — | — | — | — | — | — | — |
| household.hoh_absence | — | — | — | — | — | — | 4 |
| household.test1_met | — | — | — | — | — | — | 26 |
| household.any_test2_person | — | — | — | — | — | — | — |
| household.test2_met | — | — | — | — | — | — | 26 |
| household.hoh_eligible | — | — | — | — | — | — | 28 |
| household.hoh_fails | — | — | — | — | — | — | 25 |
| household.dependents_listed | — | — | — | — | — | — | 1 (b1mutB.household.single_member_not_test2) |
| household.dependents_any | — | — | — | — | — | — | — |
| household.hoh_missed_cost | — | — | — | — | — | — | — |
| household.test2_lived_persons | — | — | — | — | — | — | 2 (b1mutB.household.single_child_hoh_missed, b1mutB.household.single_member_not_test2) |
| household.hoh_missed_person | — | — | — | — | — | — | — |
| household.hoh_missed_test2 | — | — | — | — | — | — | — |
| household.hoh_missed | — | — | — | — | — | — | 2 (b1mutB.household.single_child_hoh_missed, b1mutB.household.single_member_not_test2) |
| household.qss_eligible | — | — | — | — | — | — | — |
| household.qss_fails | — | — | — | — | — | — | 2 (stage21.pending1.single_claims_qss_refused, stage21.pending1.qss_valid_computes) |
| household.rdp | — | — | — | — | — | — | — |
| household.spouse_died_this_year | — | — | — | — | — | — | — |
| household.spouse_died_this_year_if_ever_married | — | — | — | — | — | — | — |
| household.widowed_this_year | — | — | — | — | — | — | 4 |
| household.cp_married | — | — | — | — | — | — | — |
| household.cp_married_if_ever_married | — | — | — | — | — | — | — |
| household.cp_not_joint | — | — | — | — | — | — | — |
| household.cp_unmarried | — | — | — | — | — | — | — |
| household.cp_marriage_ended | — | — | — | — | — | — | 6 |
| household.rdp_community_property | — | — | — | — | — | — | 1 (stage21.pending2.rdp_community_income_refused) |
| household.joint_unmarried | — | — | — | — | — | — | — |
| household.no_spouse_died | — | — | — | — | — | — | — |
| household.filing_status_conflict | — | — | — | — | — | — | 9 |
| household.mfs | — | — | — | — | — | — | — |
| household.mfs_spouse_notice | — | — | — | — | — | — | 2 (mfs.household.living_helpers, mfs.household.living_not_mfs) |
| household.mfs_living | — | — | — | — | — | — | — |
| household.mfs_living_else | — | — | — | — | — | — | — |
| household.mfs_living_if_mfs | — | — | — | — | — | — | — |
| household.mfs_apart_all_year | — | — | — | — | — | — | 2 (mfs.household.living_helpers, mfs.household.living_not_mfs) |
| household.mfs_apart_last6 | — | — | — | — | — | — | 2 (mfs.household.living_helpers, mfs.household.living_not_mfs) |
| household.mfs_community_property | — | — | — | — | — | — | 2 (mfs.household.community_property, mfs.household.not_community_property) |

Unasserted lines: household.persons, household.taxpayers, household.spouses, household.hsa_people, household.hsa_both, household.hsa_split_count, household.hsa_agreed_count, household.work_ssn_count, household.eic_ssn_count, household.birth_year_bad_count, household.under16_count, household.tin_count, household.all_tin, household.id_count, household.taxpayer_work_ssn_count, household.taxpayer_work_ssn, household.considered_unmarried_if_married, household.not_married, household.unmarried, household.status_states_marriage, household.marriage_possible, household.married, household.hoh_cp_married, household.no, household.eic_above_zero, household.credit_disallowed_if_claimed, household.test2_absence_persons, household.hoh_absence_from_test1, household.hoh_absence_from_cost, household.hoh_absence_from_test2, household.no_test2_persons, household.any_test2_absence, household.any_test2_person, household.dependents_any, household.hoh_missed_cost, household.hoh_missed_person, household.hoh_missed_test2, household.spouse_died_this_year_if_ever_married, household.cp_married_if_ever_married, household.cp_not_joint, household.cp_unmarried, household.joint_unmarried, household.no_spouse_died, household.mfs, household.mfs_living_else, household.mfs_living_if_mfs

## Schedule B — interest payer entries

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| interest.amount | — | — | — | — | — | — | — |
| interest.penalty | — | — | — | — | — | — | — |

## IRA Deduction Worksheet — Schedule 1, Line 20

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ira.zero | — | — | — | — | — | — | — |
| ira.joint | — | — | — | — | — | — | — |
| ira.joint_type | — | — | — | — | — | — | — |
| ira.contrib_total | — | — | — | — | — | — | — |
| ira.roth_total | — | — | — | — | — | — | — |
| ira.any_trad | — | — | — | — | — | — | — |
| ira.cov_count | — | — | — | — | — | — | — |
| ira.anyone_covered | — | — | — | — | — | — | 1 (stage21.f1.lower_bound_still_decides) |
| ira.mfs_cov_matters | — | — | — | — | — | — | — |
| ira.mfs_cov_matters_trad | — | — | — | — | — | — | — |
| ira.mfs_spouse_covered | — | — | — | — | — | — | — |
| ira.mfs_spouse_covered_if_asked | — | — | — | — | — | — | — |
| ira.lines2to6 | — | — | — | — | — | — | — |
| ira.cov_gate | — | — | — | — | — | — | — |
| ira.cov_you | — | — | — | — | — | — | — |
| ira.cov_spouse | — | — | — | — | — | — | — |
| ira.line1a | — | — | — | 4 | — | — | 18 |
| ira.line1b | — | — | — | 1 (classm.ira.4) | — | — | 5 |
| ira.line2a_sum | — | — | — | — | — | — | — |
| ira.line2b_sum | — | — | — | — | — | — | — |
| ira.line2a | — | — | — | 2 (classm.ira.3, classm.ira.4) | — | — | 13 |
| ira.line2b | — | — | — | 1 (classm.ira.4) | — | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line3 | — | — | — | 3 | — | — | 7 |
| ira.line4 | — | — | — | 3 | — | — | 6 |
| ira.line5 | — | — | — | 3 | — | — | 2 (stage16.mut.ira_joint_full_edge, stage19.mut.ira_single_full_edge) |
| ira.line6a_sum | — | — | — | — | — | — | — |
| ira.line6b_sum | — | — | — | — | — | — | — |
| ira.line6a | — | — | — | 3 | — | — | 9 |
| ira.line6b | — | — | — | 2 (classm.ira.2, classm.ira.4) | — | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line7a_sum | — | — | — | — | — | — | — |
| ira.line7b_sum | — | — | — | — | — | — | — |
| ira.line7a | — | — | — | 4 | — | — | 20 |
| ira.line7b | — | — | — | 2 (classm.ira.2, classm.ira.4) | — | — | 7 |
| ira.wages | — | — | — | — | — | — | — |
| ira.line8 | — | — | — | 4 | — | — | 10 |
| ira.line9 | — | — | — | 4 | — | — | 11 |
| ira.line10 | — | — | — | 4 | — | — | 19 |
| ira.age50_count | — | — | — | — | — | — | — |
| ira.kbh_none | — | — | — | — | — | — | — |
| ira.kbh_one | — | — | — | — | — | — | — |
| ira.kbh_both | — | — | — | — | — | — | — |
| ira.kbh_amount | — | — | — | — | — | — | — |
| ira.kbh_short | — | — | — | — | — | — | — |
| ira.both_kinds | — | — | — | — | — | — | — |
| ira.all_total | — | — | — | — | — | — | — |
| ira.over_comp | — | — | — | — | — | — | — |
| ira.special | — | — | — | — | — | — | — |
| ira.deferred_comp | — | — | — | — | — | — | — |
| ira.fellowship | — | — | — | — | — | — | — |
| ira.reservist_repaid | — | — | — | — | — | — | — |
| ira.care_payments | — | — | — | — | — | — | — |
| ira.se_capital | — | — | — | — | — | — | — |
| ira.se_capital_gate | — | — | — | — | — | — | — |
| ira.special_gate | — | — | — | — | — | — | — |
| ira.no | — | — | — | — | — | — | — |
| ira.combat_gate | — | — | — | — | — | — | — |
| ira.excl_gate | — | — | — | — | — | — | — |
| ira.line11a | — | — | — | 4 | — | — | 15 |
| ira.line11b | — | — | — | 2 (classm.ira.2, classm.ira.4) | — | — | 6 |
| ira.line12a | — | — | — | 4 | — | — | 20 |
| ira.line12b | — | — | — | 2 (classm.ira.2, classm.ira.4) | — | — | 7 |
| ira.total | — | — | — | — | — | E via s1.line20 → ira.line20 (PE) | 1 (stage16.refuse.ira.deduct_less) |
| ira.deduct_less | — | — | — | — | — | — | — |
| ira.has_deduction | — | — | — | — | — | — | — |
| ira.less_gate | — | — | — | — | — | — | — |
| ira.line20 | — | — | — | — | — | — | 10 |
| ira.basis_total | — | — | — | — | — | — | — |

Unasserted lines: ira.zero, ira.joint, ira.joint_type, ira.contrib_total, ira.roth_total, ira.any_trad, ira.cov_count, ira.mfs_cov_matters, ira.mfs_cov_matters_trad, ira.mfs_spouse_covered_if_asked, ira.lines2to6, ira.cov_gate, ira.cov_you, ira.cov_spouse, ira.line2a_sum, ira.line2b_sum, ira.line6a_sum, ira.line6b_sum, ira.line7a_sum, ira.line7b_sum, ira.wages, ira.age50_count, ira.kbh_none, ira.kbh_one, ira.kbh_both, ira.kbh_amount, ira.kbh_short, ira.both_kinds, ira.all_total, ira.over_comp, ira.special, ira.reservist_repaid, ira.se_capital_gate, ira.special_gate, ira.no, ira.combat_gate, ira.excl_gate, ira.has_deduction, ira.less_gate, ira.basis_total

## Schedule K-1 (Form 1065) — one partner's share from one partnership

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| k1p.zero | — | — | — | — | — | — | — |
| k1p.no | — | — | — | — | — | — | — |
| k1p.yes | — | — | — | — | — | — | — |
| k1p.one | — | — | — | — | — | — | — |
| k1p.ptp | — | — | — | — | — | — | — |
| k1p.general | — | — | — | — | — | — | — |
| k1p.has_b1 | — | — | — | — | — | — | — |
| k1p.box1 | — | — | — | — | — | — | — |
| k1p.box1_if_any | — | — | — | — | — | — | — |
| k1p.has_b2 | — | — | — | — | — | — | — |
| k1p.box2 | — | — | — | — | — | — | — |
| k1p.box2_if_any | — | — | — | — | — | — | — |
| k1p.has_b3 | — | — | — | — | — | — | — |
| k1p.box3 | — | — | — | — | — | — | — |
| k1p.box3_if_any | — | — | — | — | — | — | — |
| k1p.has_b4a | — | — | — | — | — | — | — |
| k1p.box4a | — | — | — | — | — | — | — |
| k1p.box4a_if_any | — | — | — | — | — | — | — |
| k1p.has_b5 | — | — | — | — | — | — | — |
| k1p.box5 | — | — | — | — | — | — | — |
| k1p.box5_if_any | — | — | — | — | — | — | — |
| k1p.has_b6a | — | — | — | — | — | — | — |
| k1p.box6a | — | — | — | — | — | — | — |
| k1p.box6a_if_any | — | — | — | — | — | — | — |
| k1p.has_b8 | — | — | — | — | — | — | — |
| k1p.box8 | — | — | — | — | — | — | — |
| k1p.box8_if_any | — | — | — | — | — | — | — |
| k1p.has_b9a | — | — | — | — | — | — | — |
| k1p.box9a | — | — | — | — | — | — | — |
| k1p.box9a_if_any | — | — | — | — | — | — | — |
| k1p.has_b14a | — | — | — | — | — | — | — |
| k1p.box14a | — | — | — | — | — | — | — |
| k1p.box14a_if_any | — | — | — | — | — | — | — |
| k1p.has_b15o | — | — | — | — | — | — | — |
| k1p.box15o | — | — | — | — | — | — | — |
| k1p.box15o_if_any | — | — | — | — | — | — | — |
| k1p.has_b18a | — | — | — | — | — | — | — |
| k1p.box18a | — | — | — | — | — | — | — |
| k1p.box18a_if_any | — | — | — | — | — | — | — |
| k1p.has_b20z | — | — | — | — | — | — | — |
| k1p.box20z | — | — | — | — | — | — | — |
| k1p.box20z_if_any | — | — | — | — | — | — | — |
| k1p.box6b | — | — | — | — | — | — | — |
| k1p.box6b_if_any | — | — | — | — | — | — | — |
| k1p.has_b9bc | — | — | — | — | — | — | — |
| k1p.has_b9bc_if_9a | — | — | — | — | — | — | — |
| k1p.box9b | — | — | — | — | — | — | — |
| k1p.box9b_if_any | — | — | — | — | — | — | — |
| k1p.box9c | — | — | — | — | — | — | — |
| k1p.box9c_if_any | — | — | — | — | — | — | — |
| k1p.has_b19 | — | — | — | — | — | — | — |
| k1p.has_b20ab | — | — | — | — | — | — | — |
| k1p.r_b4b | — | — | — | — | — | — | — |
| k1p.r_b7 | — | — | — | — | — | — | — |
| k1p.r_b10 | — | — | — | — | — | — | — |
| k1p.r_b11 | — | — | — | — | — | — | — |
| k1p.r_b12 | — | — | — | — | — | — | — |
| k1p.r_b13 | — | — | — | — | — | — | — |
| k1p.r_b14bc | — | — | — | — | — | — | — |
| k1p.r_b15 | — | — | — | — | — | — | — |
| k1p.r_b16 | — | — | — | — | — | — | — |
| k1p.r_b17 | — | — | — | — | — | — | — |
| k1p.r_b20 | — | — | — | — | — | — | — |
| k1p.r_b21 | — | — | — | — | — | — | — |
| k1p.r_b2223 | — | — | — | — | — | — | — |
| k1p.r_foreign | — | — | — | — | — | — | — |
| k1p.r_disposed | — | — | — | — | — | — | — |
| k1p.b19_other | — | — | — | — | — | — | — |
| k1p.b19_other_if_any | — | — | — | — | — | — | — |
| k1p.dist_over | — | — | — | — | — | — | — |
| k1p.dist_over_if_any | — | — | — | — | — | — | — |
| k1p.z_other | — | — | — | — | — | — | — |
| k1p.z_other_if_z | — | — | — | — | — | — | — |
| k1p.trader | — | — | — | — | — | — | — |
| k1p.trader_if_b1 | — | — | — | — | — | — | — |
| k1p.work | — | — | — | — | — | — | — |
| k1p.work_if_b1 | — | — | — | — | — | — | — |
| k1p.hours500 | — | — | — | — | — | — | — |
| k1p.hours500_if_work | — | — | — | — | — | — | — |
| k1p.under500 | — | — | — | — | — | — | — |
| k1p.gp_under500 | — | — | — | — | — | — | — |
| k1p.most_hours | — | — | — | — | — | — | — |
| k1p.most_hours_if_gp | — | — | — | — | — | — | — |
| k1p.ask_nearly_all | — | — | — | — | — | — | — |
| k1p.nearly_all | — | — | — | — | — | — | — |
| k1p.nearly_all_if_asked | — | — | — | — | — | — | — |
| k1p.ask_five | — | — | — | — | — | — | — |
| k1p.five_of_ten | — | — | — | — | — | — | — |
| k1p.five_of_ten_if_asked | — | — | — | — | — | — | — |
| k1p.ask_other | — | — | — | — | — | — | — |
| k1p.t6 | — | — | — | — | — | — | — |
| k1p.t6_if_asked | — | — | — | — | — | — | — |
| k1p.ask_other_gp | — | — | — | — | — | — | — |
| k1p.t4 | — | — | — | — | — | — | — |
| k1p.t4_if_gp | — | — | — | — | — | — | — |
| k1p.t7 | — | — | — | — | — | — | — |
| k1p.t7_if_gp | — | — | — | — | — | — | — |
| k1p.material | — | — | — | — | — | — | 12 |
| k1p.ask_active | — | — | — | — | — | — | — |
| k1p.decisions | — | — | — | — | — | — | — |
| k1p.decisions_if_asked | — | — | — | — | — | — | — |
| k1p.tenth | — | — | — | — | — | — | — |
| k1p.tenth_if_decisions | — | — | — | — | — | — | — |
| k1p.active | — | — | — | — | — | — | 3 |
| k1p.has_activity | — | — | — | — | — | — | — |
| k1p.prior_any | — | — | — | — | — | — | — |
| k1p.prior_any_if_activity | — | — | — | — | — | — | — |
| k1p.prior_b1_any | — | — | — | — | — | — | — |
| k1p.prior_b1_any_if | — | — | — | — | — | — | — |
| k1p.prior_b1 | — | — | — | — | — | — | — |
| k1p.prior_b1_if | — | — | — | — | — | — | — |
| k1p.prior_b2_any | — | — | — | — | — | — | — |
| k1p.prior_b2_any_if | — | — | — | — | — | — | — |
| k1p.prior_b2 | — | — | — | — | — | — | — |
| k1p.prior_b2_if | — | — | — | — | — | — | — |
| k1p.prior_b3_any | — | — | — | — | — | — | — |
| k1p.prior_b3_any_if | — | — | — | — | — | — | — |
| k1p.prior_b3 | — | — | — | — | — | — | — |
| k1p.prior_b3_if | — | — | — | — | — | — | — |
| k1p.former_passive | — | — | — | — | — | — | — |
| k1p.ask_prior_active | — | — | — | — | — | — | — |
| k1p.prior_not_active | — | — | — | — | — | — | — |
| k1p.prior_not_active_if | — | — | — | — | — | — | — |
| k1p.any_loss | — | — | — | — | — | — | 6 |
| k1p.basis_short | — | — | — | — | — | — | — |
| k1p.basis_short_if_loss | — | — | — | — | — | — | — |
| k1p.not_at_risk | — | — | — | — | — | — | — |
| k1p.not_at_risk_if_loss | — | — | — | — | — | — | — |
| k1p.se_loss_not_material | — | — | — | — | — | — | 1 (mk1.k1p.material_box1_and_se_loss) |
| k1p.b1_passive | — | — | — | — | — | — | — |
| k1p.b1_pos | — | — | — | — | — | — | — |
| k1p.b1_neg | — | — | — | — | — | — | — |
| k1p.b2_pos | — | — | — | — | — | — | — |
| k1p.b2_neg | — | — | — | — | — | — | — |
| k1p.b3_pos | — | — | — | — | — | — | — |
| k1p.b3_neg | — | — | — | — | — | — | — |
| k1p.b1_net_income | — | — | — | 10 | — | — | 3 |
| k1p.b1_net_loss | — | — | — | 10 | — | — | 4 |
| k1p.b2_net_income | — | — | — | 10 | — | — | 4 |
| k1p.b2_net_loss | — | — | — | 10 | — | — | 2 (mk1.k1p.passive_three_losses, mk1.k1p.box2_loss_box3_income) |
| k1p.b3_net_income | — | — | — | 10 | — | — | 3 |
| k1p.b3_net_loss | — | — | — | 10 | — | — | 2 (mk1.k1p.passive_three_losses, mk1.k1p.material_box1_box3_loss) |
| k1p.b1_loss_sum | — | — | — | — | — | — | 2 (x2k1p.prior_box1_partly_used, mk1.k1p.passive_box1_loss_only) |
| k1p.b1_overall_loss | — | — | — | 10 | — | — | 5 |
| k1p.b2_loss_sum | — | — | — | — | — | — | 1 (mk1.k1p.box2_income_prior_only) |
| k1p.b2_overall_loss | — | — | — | 10 | — | — | 7 |
| k1p.b3_loss_sum | — | — | — | — | — | — | 2 (mk1.k1p.passive_box3_loss_only, mk1.k1p.box3_income_prior_only) |
| k1p.b3_overall_loss | — | — | — | 10 | — | — | 5 |
| k1p.p4_income | — | — | — | 10 | — | — | 4 |
| k1p.p4_loss | — | — | — | 10 | — | — | 4 |
| k1p.p4_prior | — | — | — | 10 | — | — | 2 (x2k1p.prior_box2_active, mk1.k1p.passive_three_income_with_priors) |
| k1p.p6_loss | — | — | — | 10 | — | — | 3 |
| k1p.p5_b2_income | — | — | — | — | — | — | — |
| k1p.p5_b2_loss | — | — | — | — | — | — | — |
| k1p.p5_b2_prior | — | — | — | — | — | — | — |
| k1p.p5_income | — | — | — | 10 | — | — | 12 |
| k1p.p5_loss | — | — | — | 10 | — | — | 9 |
| k1p.p5_prior | — | — | — | 10 | — | — | 6 |
| k1p.prior_total | — | — | — | — | — | — | — |
| k1p.passive_loss | — | — | — | — | — | — | 8 |
| k1p.col_h | — | — | — | 10 | — | — | 17 |
| k1p.np_b1_income | — | — | — | — | — | — | — |
| k1p.col_k | — | — | — | 10 | — | — | 12 |
| k1p.col_i | — | — | — | 10 | — | — | 8 |
| k1p.nonpassive_net | — | — | — | — | — | — | 4 |
| k1p.sche_row | — | — | — | — | — | — | 10 |
| k1p.se_pos | — | — | — | — | — | — | — |
| k1p.screened | — | — | — | — | — | — | 18 |

Unasserted lines: k1p.zero, k1p.no, k1p.yes, k1p.one, k1p.box1_if_any, k1p.box2_if_any, k1p.box3_if_any, k1p.box4a_if_any, k1p.box5_if_any, k1p.box6a_if_any, k1p.box8_if_any, k1p.box9a_if_any, k1p.box14a_if_any, k1p.box15o_if_any, k1p.box18a_if_any, k1p.box20z_if_any, k1p.box6b_if_any, k1p.has_b9bc_if_9a, k1p.box9b_if_any, k1p.box9c_if_any, k1p.b19_other_if_any, k1p.dist_over_if_any, k1p.z_other_if_z, k1p.trader_if_b1, k1p.work_if_b1, k1p.hours500_if_work, k1p.under500, k1p.gp_under500, k1p.most_hours_if_gp, k1p.ask_nearly_all, k1p.nearly_all_if_asked, k1p.ask_five, k1p.five_of_ten_if_asked, k1p.ask_other, k1p.t6_if_asked, k1p.ask_other_gp, k1p.t4_if_gp, k1p.t7_if_gp, k1p.ask_active, k1p.decisions_if_asked, k1p.tenth_if_decisions, k1p.has_activity, k1p.prior_any_if_activity, k1p.prior_b1_any_if, k1p.prior_b1_if, k1p.prior_b2_any_if, k1p.prior_b2_if, k1p.prior_b3_any_if, k1p.prior_b3_if, k1p.former_passive, k1p.ask_prior_active, k1p.prior_not_active_if, k1p.basis_short_if_loss, k1p.not_at_risk_if_loss, k1p.b1_passive, k1p.b1_pos, k1p.b1_neg, k1p.b2_pos, k1p.b2_neg, k1p.b3_pos, k1p.b3_neg, k1p.p5_b2_income, k1p.p5_b2_loss, k1p.p5_b2_prior, k1p.prior_total, k1p.np_b1_income, k1p.se_pos

## Schedule K-1 (Form 1120-S), Shareholder's Share of Income, Deductions, Credits, etc., one per S corporation

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| k1s.zero | — | — | — | — | — | — | — |
| k1s.no | — | — | — | — | — | — | — |
| k1s.multi | — | — | — | — | — | — | — |
| k1s.disposed | — | — | — | — | — | — | — |
| k1s.box1_any | — | — | — | — | — | — | — |
| k1s.box2_any | — | — | — | — | — | — | — |
| k1s.box3_any | — | — | — | — | — | — | — |
| k1s.box4_any | — | — | — | — | — | — | — |
| k1s.box5_any | — | — | — | — | — | — | — |
| k1s.box1 | — | — | — | — | — | — | — |
| k1s.box1_if_any | — | — | — | — | — | — | — |
| k1s.box2 | — | — | — | — | — | — | — |
| k1s.box2_if_any | — | — | — | — | — | — | — |
| k1s.box3 | — | — | — | — | — | — | — |
| k1s.box3_if_any | — | — | — | — | — | — | — |
| k1s.box4 | — | — | — | — | — | — | — |
| k1s.box4_if_any | — | — | — | — | — | — | — |
| k1s.box5a | — | — | — | — | — | — | — |
| k1s.box5a_if_any | — | — | — | — | — | — | — |
| k1s.box5b | — | — | — | — | — | — | — |
| k1s.box5b_if_any | — | — | — | — | — | — | — |
| k1s.box6 | — | — | — | — | — | — | — |
| k1s.box7_any | — | — | — | — | — | — | — |
| k1s.box8_any | — | — | — | — | — | — | — |
| k1s.box9 | — | — | — | — | — | — | — |
| k1s.box10 | — | — | — | — | — | — | — |
| k1s.box11_12 | — | — | — | — | — | — | — |
| k1s.box7 | — | — | — | — | — | — | — |
| k1s.box7_if_any | — | — | — | — | — | — | — |
| k1s.box8a | — | — | — | — | — | — | — |
| k1s.box8a_if_any | — | — | — | — | — | — | — |
| k1s.box8b | — | — | — | — | — | — | — |
| k1s.box8b_if_any | — | — | — | — | — | — | — |
| k1s.box8c | — | — | — | — | — | — | — |
| k1s.box8c_if_any | — | — | — | — | — | — | — |
| k1s.box8_stmt | — | — | — | — | — | — | — |
| k1s.box8_stmt_if_any | — | — | — | — | — | — | — |
| k1s.box13o_any | — | — | — | — | — | — | — |
| k1s.box13_other | — | — | — | — | — | — | — |
| k1s.box14 | — | — | — | — | — | — | — |
| k1s.box15 | — | — | — | — | — | — | — |
| k1s.box16_any | — | — | — | — | — | — | — |
| k1s.box17_any | — | — | — | — | — | — | — |
| k1s.box13o | — | — | — | — | — | — | — |
| k1s.box13o_if_any | — | — | — | — | — | — | — |
| k1s.box16a_any | — | — | — | — | — | — | — |
| k1s.box16a_any_if_16 | — | — | — | — | — | — | — |
| k1s.box16b_any | — | — | — | — | — | — | — |
| k1s.box16b_any_if_16 | — | — | — | — | — | — | — |
| k1s.box16c_any | — | — | — | — | — | — | — |
| k1s.box16c_any_if_16 | — | — | — | — | — | — | — |
| k1s.box16d_any | — | — | — | — | — | — | — |
| k1s.box16d_any_if_16 | — | — | — | — | — | — | — |
| k1s.box16ef | — | — | — | — | — | — | — |
| k1s.box16ef_if_16 | — | — | — | — | — | — | — |
| k1s.box16a | — | — | — | — | — | — | — |
| k1s.box16a_if_any | — | — | — | — | — | — | — |
| k1s.box16b | — | — | — | — | — | — | — |
| k1s.box16b_if_any | — | — | — | — | — | — | — |
| k1s.box16c | — | — | — | — | — | — | — |
| k1s.box16c_if_any | — | — | — | — | — | — | — |
| k1s.box16d | — | — | — | — | — | — | — |
| k1s.box16d_if_any | — | — | — | — | — | — | — |
| k1s.box17v_any | — | — | — | — | — | — | — |
| k1s.box17v_any_if_17 | — | — | — | — | — | — | — |
| k1s.box17_other | — | — | — | — | — | — | — |
| k1s.box17_other_if_17 | — | — | — | — | — | — | — |
| k1s.qbi_stmt | — | — | — | — | — | — | — |
| k1s.qbi_stmt_if_any | — | — | — | — | — | — | — |
| k1s.v_other | — | — | — | — | — | — | — |
| k1s.v_other_if_any | — | — | — | — | — | — | — |
| k1s.work | — | — | — | — | — | — | — |
| k1s.work_if_b1 | — | — | — | — | — | — | — |
| k1s.hours500 | — | — | — | — | — | — | — |
| k1s.hours500_if_work | — | — | — | — | — | — | — |
| k1s.under500 | — | — | — | — | — | — | — |
| k1s.most_hours | — | — | — | — | — | — | — |
| k1s.most_hours_if_under | — | — | — | — | — | — | — |
| k1s.mp_now | — | — | — | — | — | — | — |
| k1s.past_ask | — | — | — | — | — | — | — |
| k1s.past_years | — | — | — | — | — | — | — |
| k1s.past_years_if_ask | — | — | — | — | — | — | 1 (mk1.k1s.test1_earlier_years_not_used) |
| k1s.other_ask | — | — | — | — | — | — | — |
| k1s.mp_other | — | — | — | — | — | — | — |
| k1s.mp_other_if_ask | — | — | — | — | — | — | — |
| k1s.material | — | — | — | — | — | — | 6 |
| k1s.active | — | — | — | — | — | — | — |
| k1s.active_if_b2 | — | — | — | — | — | — | — |
| k1s.tenth | — | — | — | — | — | — | — |
| k1s.tenth_if_active | — | — | — | — | — | — | — |
| k1s.part4 | — | — | — | — | — | — | 3 |
| k1s.prior_any | — | — | — | — | — | — | — |
| k1s.basis_carry | — | — | — | — | — | — | — |
| k1s.risk_carry | — | — | — | — | — | — | — |
| k1s.b1_prior | — | — | — | — | — | — | — |
| k1s.b1_prior_if_any | — | — | — | — | — | — | — |
| k1s.b2_prior | — | — | — | — | — | — | — |
| k1s.b2_prior_if_any | — | — | — | — | — | — | — |
| k1s.b3_prior | — | — | — | — | — | — | — |
| k1s.b3_prior_if_any | — | — | — | — | — | — | — |
| k1s.former_passive | — | — | — | — | — | — | — |
| k1s.gain1 | — | — | — | — | — | — | — |
| k1s.loss1 | — | — | — | — | — | — | — |
| k1s.gain2 | — | — | — | — | — | — | — |
| k1s.loss2 | — | — | — | — | — | — | — |
| k1s.gain3 | — | — | — | — | — | — | — |
| k1s.loss3 | — | — | — | — | — | — | — |
| k1s.gain7 | — | — | — | — | — | — | — |
| k1s.loss7 | — | — | — | — | — | — | — |
| k1s.gain8 | — | — | — | — | — | — | — |
| k1s.loss8 | — | — | — | — | — | — | — |
| k1s.loss_items | — | — | — | — | — | — | — |
| k1s.f7203_required | — | — | — | — | — | — | — |
| k1s.allowed1 | — | — | — | — | — | — | — |
| k1s.allowed2 | — | — | — | — | — | — | — |
| k1s.allowed3 | — | — | — | — | — | — | — |
| k1s.basis_carry_out | — | — | — | — | — | — | — |
| k1s.f7203_n | — | — | — | — | — | — | — |
| k1s.not_at_risk | — | — | — | — | — | — | — |
| k1s.has_loss | — | — | — | — | — | — | — |
| k1s.not_at_risk_if_loss | — | — | — | — | — | — | — |
| k1s.ok | — | — | — | — | — | — | 17 |
| k1s.b1_net | — | — | — | — | — | — | 2 (k1s.loss_within_basis, k1s.loss_over_basis_prorata) |
| k1s.b2_net | — | — | — | — | — | — | 1 (k1s.loss_over_basis_prorata) |
| k1s.b3_net | — | — | — | — | — | — | — |
| k1s.basis_cut | — | — | — | — | — | — | 1 (k1s.loss_over_basis_prorata) |
| k1s.b1_np | — | — | — | — | — | — | — |
| k1s.b1_passive | — | — | — | — | — | — | — |
| k1s.col_k | — | — | — | 8 | — | — | 28 |
| k1s.np_income | — | — | — | — | — | — | — |
| k1s.np_loss | — | — | — | — | — | — | — |
| k1s.col_i | — | — | — | 8 | — | — | 10 |
| k1s.p1_income | — | — | — | — | — | — | — |
| k1s.p1_loss | — | — | — | — | — | — | — |
| k1s.p2_income | — | — | — | — | — | — | — |
| k1s.p2_loss | — | — | — | — | — | — | — |
| k1s.p3_income | — | — | — | — | — | — | — |
| k1s.p3_loss | — | — | — | — | — | — | — |
| k1s.passive_income | — | — | — | — | — | — | — |
| k1s.col_h | — | — | — | 8 | — | — | 7 |
| k1s.p4_income_raw | — | — | — | — | — | — | — |
| k1s.p4_loss_raw | — | — | — | — | — | — | — |
| k1s.p4_prior_raw | — | — | — | — | — | — | — |
| k1s.p5_b2_income | — | — | — | — | — | — | — |
| k1s.p5_b2_loss | — | — | — | — | — | — | — |
| k1s.p5_b2_prior | — | — | — | — | — | — | — |
| k1s.p4_income | — | — | — | — | — | — | 1 (mk1.k1s.rental_active_with_prior_and_box3) |
| k1s.p4_loss | — | — | — | — | — | — | 1 (mk1.k1s.rental_active_with_prior_and_box3) |
| k1s.p4_prior | — | — | — | — | — | — | 1 (mk1.k1s.rental_active_with_prior_and_box3) |
| k1s.p5_income_raw | — | — | — | — | — | — | — |
| k1s.p5_loss_raw | — | — | — | — | — | — | — |
| k1s.p1_prior_passive | — | — | — | — | — | — | — |
| k1s.p5_prior_raw | — | — | — | — | — | — | — |
| k1s.p5_income | — | — | — | — | — | — | 4 |
| k1s.p5_loss | — | — | — | — | — | — | 4 |
| k1s.p5_prior | — | — | — | — | — | — | 2 (mk1.k1s.rental_active_with_prior_and_box3, mk1.k1s.material_with_box3_prior) |
| k1s.int | — | — | — | — | — | — | — |
| k1s.ord_div | — | — | — | — | — | — | — |
| k1s.qual_div | — | — | — | — | — | — | — |
| k1s.st | — | — | — | — | — | — | — |
| k1s.lt | — | — | — | — | — | — | — |
| k1s.g28 | — | — | — | — | — | — | — |
| k1s.u1250 | — | — | — | — | — | — | — |
| k1s.backup | — | — | — | — | — | — | — |
| k1s.taxexempt | — | — | — | — | — | — | — |
| k1s.nonpassive | — | — | — | — | — | — | — |
| k1s.qbi_cut | — | — | — | — | — | — | — |
| k1s.qbi | — | — | — | — | — | — | 3 |
| k1s.one | — | — | — | — | — | — | — |
| k1s.sche_any | — | — | — | — | — | — | — |

Unasserted lines: k1s.zero, k1s.no, k1s.box1_if_any, k1s.box2_if_any, k1s.box3_if_any, k1s.box4_if_any, k1s.box5a_if_any, k1s.box5b_if_any, k1s.box7_if_any, k1s.box8a_if_any, k1s.box8b_if_any, k1s.box8c_if_any, k1s.box8_stmt_if_any, k1s.box13o_if_any, k1s.box16a_any_if_16, k1s.box16b_any_if_16, k1s.box16c_any_if_16, k1s.box16d_any_if_16, k1s.box16ef_if_16, k1s.box16a_if_any, k1s.box16b_if_any, k1s.box16c_if_any, k1s.box16d_if_any, k1s.box17v_any_if_17, k1s.box17_other_if_17, k1s.qbi_stmt_if_any, k1s.v_other_if_any, k1s.work_if_b1, k1s.hours500_if_work, k1s.under500, k1s.most_hours_if_under, k1s.mp_now, k1s.past_ask, k1s.other_ask, k1s.mp_other_if_ask, k1s.active_if_b2, k1s.tenth_if_active, k1s.b1_prior_if_any, k1s.b2_prior_if_any, k1s.b3_prior_if_any, k1s.former_passive, k1s.gain1, k1s.loss1, k1s.gain2, k1s.loss2, k1s.gain3, k1s.loss3, k1s.gain7, k1s.loss7, k1s.gain8, k1s.loss8, k1s.loss_items, k1s.f7203_required, k1s.allowed1, k1s.allowed2, k1s.allowed3, k1s.basis_carry_out, k1s.f7203_n, k1s.has_loss, k1s.not_at_risk_if_loss, k1s.b3_net, k1s.b1_np, k1s.b1_passive, k1s.np_income, k1s.np_loss, k1s.p1_income, k1s.p1_loss, k1s.p2_income, k1s.p2_loss, k1s.p3_income, k1s.p3_loss, k1s.passive_income, k1s.p4_income_raw, k1s.p4_loss_raw, k1s.p4_prior_raw, k1s.p5_b2_income, k1s.p5_b2_loss, k1s.p5_b2_prior, k1s.p5_income_raw, k1s.p5_loss_raw, k1s.p1_prior_passive, k1s.p5_prior_raw, k1s.int, k1s.ord_div, k1s.qual_div, k1s.st, k1s.lt, k1s.g28, k1s.u1250, k1s.backup, k1s.taxexempt, k1s.nonpassive, k1s.qbi_cut, k1s.one, k1s.sche_any

## Form 7206, line 2 — qualified long-term care insurance, one per person covered

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ltc.payments | — | — | — | — | — | — | — |
| ltc.age | — | — | — | — | — | — | — |
| ltc.limit | — | — | — | 2 (classm.ltc.1, classm.ltc.2) | — | — | — |
| ltc.amount | — | — | — | 2 (classm.ltc.1, classm.ltc.2) | — | — | — |

## Mid-quarter convention test for property placed in service in 2025

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mq.q4 | — | — | — | — | — | — | — |
| mq.total | — | — | — | — | — | — | — |
| mq.five | — | — | — | — | — | — | — |
| mq.two | — | — | — | — | — | — | — |
| mq.q4x5 | — | — | — | — | — | — | — |
| mq.totalx2 | — | — | — | — | — | — | — |
| mq.applies | — | — | — | — | — | — | 6 |

Unasserted lines: mq.q4, mq.total, mq.five, mq.two, mq.q4x5, mq.totalx2

## Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ny_it2.state_withheld | — | — | — | — | — | — | — |
| ny_it2.yonkers_withheld | — | — | — | — | — | — | — |
| ny_it2.yonkers_gate | — | — | — | — | — | — | — |
| ny_it2.state_whole | — | — | — | — | — | — | — |
| ny_it2.city_withheld | — | — | — | — | — | — | — |
| ny_it2.city_whole | — | — | — | — | — | — | — |

Unasserted lines: ny_it2.yonkers_gate, ny_it2.state_whole, ny_it2.city_whole

## Form IT-201 (2025), Resident Income Tax Return — New York State and New York City

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ny_it201.ask.state_resident | — | — | — | — | — | — | — |
| ny_it201.ask.city_resident | — | — | — | — | — | — | — |
| ny_it201.ask.special_accrual | — | — | — | — | — | — | — |
| ny_it201.ask.yonkers | — | — | — | — | — | — | — |
| ny_it201.state_resident_if_not_city | — | — | — | — | — | — | — |
| ny_it201.ask.active_duty | — | — | — | — | — | — | — |
| ny_it201.active_duty_if_armed_forces | — | — | — | — | — | — | — |
| ny_it201.ask.moved_in | — | — | — | — | — | — | — |
| ny_it201.ask.moved_out | — | — | — | — | — | — | — |
| ny_it201.moved | — | — | — | — | — | — | — |
| ny_it201.ask.bab | — | — | — | — | — | — | — |
| ny_it201.bab_if_interest | — | — | — | — | — | — | — |
| ny_it201.ask.abroad | — | — | — | — | — | — | — |
| ny_it201.ask.installment | — | — | — | — | — | — | — |
| ny_it201.ask.special_code | — | — | — | — | — | — | — |
| ny_it201.ask.decedent | — | — | — | — | — | — | — |
| ny_it201.ask.item_c | — | — | — | — | — | — | — |
| ny_it201.ask.inflation_check | — | — | — | — | — | — | — |
| ny_it201.ask.out_of_state_bond_interest | — | — | — | — | — | — | — |
| ny_it201.ask.414h | — | — | — | — | — | — | — |
| ny_it201.ask.529_nonqualified | — | — | — | — | — | — | — |
| ny_it201.ask.it225 | — | — | — | — | — | — | — |
| ny_it201.ask.gov_pension | — | — | — | — | — | — | — |
| ny_it201.ask.us_obligation_interest | — | — | — | — | — | — | — |
| ny_it201.ask.pension_exclusion | — | — | — | — | — | — | — |
| ny_it201.ask.529_owner | — | — | — | — | — | — | — |
| ny_it201.ask.itemize | — | — | — | — | — | — | — |
| ny_it201.ask.resident_credit | — | — | — | — | — | — | — |
| ny_it201.ask.other_credits | — | — | — | — | — | — | — |
| ny_it201.ask.other_taxes | — | — | — | — | — | — | — |
| ny_it201.ask.city_credits | — | — | — | — | — | — | — |
| ny_it201.ask.mctmt | — | — | — | — | — | — | — |
| ny_it201.ask.owes_use_tax | — | — | — | — | — | — | — |
| ny_it201.ask.use_tax_st141 | — | — | — | — | — | — | — |
| ny_it201.ask.contributions | — | — | — | — | — | — | — |
| ny_it201.ask.dependent_care | — | — | — | — | — | — | — |
| ny_it201.ask.noncustodial | — | — | — | — | — | — | — |
| ny_it201.ask.real_property_credit | — | — | — | — | — | — | — |
| ny_it201.ask.college_tuition | — | — | — | — | — | — | — |
| ny_it201.ask.other_withholding | — | — | — | — | — | — | — |
| ny_it201.ask.refund_529 | — | — | — | — | — | — | — |
| ny_it201.ask.late_penalty | — | — | — | — | — | — | — |
| ny_it201.ask.prior_agi_high | — | — | — | — | — | — | — |
| ny_it201.ask.abode_part_year | — | — | — | — | — | — | — |
| ny_it201.ask.prior_full_year | — | — | — | — | — | — | — |
| ny_it201.ask.est_late | — | — | — | — | — | — | — |
| ny_it201.ask.spouse_resident | — | — | — | — | — | — | — |
| ny_it201.ask.prior_year_tax | — | — | — | — | — | — | — |
| ny_it201.gate.part_year_state | — | — | — | — | — | — | — |
| ny_it201.gate.part_year_city | — | — | — | — | — | — | — |
| ny_it201.gate.spouse_nonresident | — | — | — | — | — | — | — |
| ny_it201.gate.special_accrual | — | — | — | — | — | — | — |
| ny_it201.gate.yonkers | — | — | — | — | — | — | — |
| ny_it201.gate.special_code | — | — | — | — | — | — | — |
| ny_it201.gate.decedent | — | — | — | — | — | — | — |
| ny_it201.item_c_if_not_federal | — | — | — | — | — | — | — |
| ny_it201.item_c | — | — | — | — | — | — | — |
| ny_it201.item_h_count | — | — | — | — | — | — | — |
| ny_it201.line1 | — | — | — | — | — | — | — |
| ny_it201.line2 | — | — | — | — | — | — | — |
| ny_it201.line3 | — | — | — | — | — | — | — |
| ny_it201.line4 | — | — | — | — | — | — | — |
| ny_it201.line5 | — | — | — | — | — | — | — |
| ny_it201.line6 | — | — | — | — | — | — | — |
| ny_it201.line7 | — | — | — | — | — | — | — |
| ny_it201.line8 | — | — | — | — | — | — | — |
| ny_it201.line9 | — | — | — | — | — | — | — |
| ny_it201.line10 | — | — | — | — | — | — | — |
| ny_it201.line11 | — | — | — | — | — | — | — |
| ny_it201.line12 | — | — | — | — | — | — | — |
| ny_it201.line13 | — | — | — | — | — | — | — |
| ny_it201.line14 | — | — | — | — | — | — | — |
| ny_it201.line15 | — | — | — | — | — | — | — |
| ny_it201.line16 | — | — | — | — | — | — | — |
| ny_it201.line17 | — | — | — | — | — | — | — |
| ny_it201.line18 | — | — | — | — | — | — | — |
| ny_it201.line19 | — | — | — | — | — | — | — |
| ny_it201.fagi_rounded | — | — | — | — | — | — | — |
| ny_it201.line19_agrees | — | — | — | — | — | — | — |
| ny_it201.has_tax_exempt | — | — | — | — | — | — | — |
| ny_it201.gate.line20 | — | — | — | — | — | — | — |
| ny_it201.line20 | — | — | — | — | — | — | — |
| ny_it201.ask.public_job | — | — | — | — | — | — | — |
| ny_it201.public_job_if_w2 | — | — | — | — | — | — | — |
| ny_it201.gate.line21 | — | — | — | — | — | — | — |
| ny_it201.line21 | — | — | — | — | — | — | — |
| ny_it201.edu_people | — | — | — | — | — | — | — |
| ny_it201.has_edu_account | — | — | — | — | — | — | — |
| ny_it201.ask.ny_529 | — | — | — | — | — | — | — |
| ny_it201.ny_529_if_account | — | — | — | — | — | — | — |
| ny_it201.gate.line22 | — | — | — | — | — | — | — |
| ny_it201.line22 | — | — | — | — | — | — | — |
| ny_it201.gate.it225 | — | — | — | — | — | — | — |
| ny_it201.line23 | — | — | — | — | — | — | — |
| ny_it201.line24 | — | — | — | — | — | — | — |
| ny_it201.has_other_income | — | — | — | — | — | — | — |
| ny_it201.inflation_if_other_income | — | — | — | — | — | — | — |
| ny_it201.gate.line25 | — | — | — | — | — | — | — |
| ny_it201.line25 | — | — | — | — | — | — | — |
| ny_it201.no | — | — | — | — | — | — | — |
| ny_it201.has_pension_income | — | — | — | — | — | — | — |
| ny_it201.gov_pension_if_income | — | — | — | — | — | — | — |
| ny_it201.gov_said_no | — | — | — | — | — | — | — |
| ny_it201.ask.gov_pension_other | — | — | — | — | — | — | — |
| ny_it201.gov_pension_other_if_no | — | — | — | — | — | — | — |
| ny_it201.gov_pension_any | — | — | — | — | — | — | — |
| ny_it201.gate.line26 | — | — | — | — | — | — | — |
| ny_it201.line26 | — | — | — | — | — | — | — |
| ny_it201.line27 | — | — | — | — | — | — | — |
| ny_it201.has_line28_income | — | — | — | — | — | — | — |
| ny_it201.gate.line28 | — | — | — | — | — | — | — |
| ny_it201.line28 | — | — | — | — | — | — | — |
| ny_it201.pension_59_people | — | — | — | — | — | — | — |
| ny_it201.pension_59_known | — | — | — | — | — | — | — |
| ny_it201.pension_exclusion_if_young | — | — | — | — | — | — | — |
| ny_it201.pension_exclusion_line | — | — | — | — | — | — | — |
| ny_it201.pension_exclusion_after_gov | — | — | — | — | — | — | — |
| ny_it201.gate.line29 | — | — | — | — | — | — | — |
| ny_it201.line29 | — | — | — | — | — | — | — |
| ny_it201.gate.line30 | — | — | — | — | — | — | — |
| ny_it201.line30 | — | — | — | — | — | — | — |
| ny_it201.line31 | — | — | — | — | — | — | — |
| ny_it201.line32 | — | — | — | — | — | — | — |
| ny_it201.line33 | — | — | — | — | — | — | — |
| ny_it201.ask.spouse_itemizes | — | — | — | — | — | — | — |
| ny_it201.spouse_itemizes_if_mfs | — | — | — | — | — | — | — |
| ny_it201.gate.itemize | — | — | — | — | — | — | — |
| ny_it201.dependent_single | — | — | — | — | — | — | — |
| ny_it201.std_deduction | — | — | — | — | — | — | — |
| ny_it201.std_deduction_dependent | — | — | — | — | — | — | — |
| ny_it201.line34 | — | — | — | — | — | — | — |
| ny_it201.line35 | — | — | — | — | — | — | — |
| ny_it201.exemption | — | — | — | — | — | — | — |
| ny_it201.line36 | — | — | — | — | — | — | — |
| ny_it201.line37 | — | — | — | — | — | — | — |
| ny_it201.line38 | — | — | — | — | — | — | — |
| ny_it201.agi_table_range | — | — | — | — | — | — | — |
| ny_it201.ti_table_range | — | — | — | — | — | — | — |
| ny_it201.tax_table | — | — | — | — | — | — | — |
| ny_it201.tax_schedule | — | — | — | — | — | — | — |
| ny_it201.tax_low | — | — | — | — | — | — | — |
| ny_it201.tcw.w1 | — | — | — | — | — | — | — |
| ny_it201.tcw.w7 | — | — | — | — | — | — | — |
| ny_it201.tcw.w12 | — | — | — | — | — | — | — |
| ny_it201.tcw.w2 | — | — | — | — | — | — | — |
| ny_it201.tcw.w3 | — | — | — | — | — | — | — |
| ny_it201.tcw.w4 | — | — | — | — | — | — | — |
| ny_it201.tcw.w5 | — | — | — | — | — | — | — |
| ny_it201.tcw.w8 | — | — | — | — | — | — | — |
| ny_it201.tcw.w9 | — | — | — | — | — | — | — |
| ny_it201.tcw.w10 | — | — | — | — | — | — | — |
| ny_it201.tcw.w13 | — | — | — | — | — | — | — |
| ny_it201.tcw.w14 | — | — | — | — | — | — | — |
| ny_it201.tcw.w15 | — | — | — | — | — | — | — |
| ny_it201.tcw.top | — | — | — | — | — | — | — |
| ny_it201.tcw.mfj | — | — | — | — | — | — | — |
| ny_it201.tcw.single | — | — | — | — | — | — | — |
| ny_it201.tcw.hoh | — | — | — | — | — | — | — |
| ny_it201.tcw.by_status | — | — | — | — | — | — | — |
| ny_it201.agi_top | — | — | — | — | — | — | — |
| ny_it201.tax_high | — | — | — | — | — | — | — |
| ny_it201.line39 | — | — | — | — | — | — | — |
| ny_it201.hh_agi | — | — | — | — | — | — | — |
| ny_it201.one | — | — | — | — | — | — | — |
| ny_it201.spouse_count | — | — | — | — | — | — | — |
| ny_it201.hh_people | — | — | — | — | — | — | — |
| ny_it201.hh_state_p1 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p1 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p2 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p2 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p3 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p3 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p4 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p4 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p5 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p5 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p6 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p6 | — | — | — | — | — | — | — |
| ny_it201.hh_state_p7 | — | — | — | — | — | — | — |
| ny_it201.hh_city_p7 | — | — | — | — | — | — | — |
| ny_it201.hh_state_t2 | — | — | — | — | — | — | — |
| ny_it201.hh_city_t5 | — | — | — | — | — | — | — |
| ny_it201.hh_state_t1 | — | — | — | — | — | — | — |
| ny_it201.hh_city_t4 | — | — | — | — | — | — | — |
| ny_it201.zero | — | — | — | — | — | — | — |
| ny_it201.hh_state_in_range | — | — | — | — | — | — | — |
| ny_it201.gate.hh_state_mfs | — | — | — | — | — | — | — |
| ny_it201.gate.hh_state_over7 | — | — | — | — | — | — | — |
| ny_it201.hh_state_by_status | — | — | — | — | — | — | — |
| ny_it201.hh_city_in_range | — | — | — | — | — | — | — |
| ny_it201.gate.hh_city_mfs | — | — | — | — | — | — | — |
| ny_it201.gate.hh_city_over7 | — | — | — | — | — | — | — |
| ny_it201.hh_city_by_status | — | — | — | — | — | — | — |
| ny_it201.line40 | — | — | — | — | — | — | — |
| ny_it201.gate.resident_credit | — | — | — | — | — | — | — |
| ny_it201.line41 | — | — | — | — | — | — | — |
| ny_it201.gate.other_credits | — | — | — | — | — | — | — |
| ny_it201.line42 | — | — | — | — | — | — | — |
| ny_it201.line43 | — | — | — | — | — | — | — |
| ny_it201.line44 | — | — | — | — | — | — | — |
| ny_it201.gate.other_taxes | — | — | — | — | — | — | — |
| ny_it201.line45 | — | — | — | — | — | — | — |
| ny_it201.line46 | — | — | — | — | — | — | — |
| ny_it201.line47 | — | — | — | — | — | — | — |
| ny_it201.city_table_range | — | — | — | — | — | — | — |
| ny_it201.city_tax_table | — | — | — | — | — | — | — |
| ny_it201.city_tax_schedule | — | — | — | — | — | — | — |
| ny_it201.line47a | — | — | — | — | — | — | — |
| ny_it201.line48 | — | — | — | — | — | — | — |
| ny_it201.line49 | — | — | — | — | — | — | — |
| ny_it201.line50 | — | — | — | — | — | — | — |
| ny_it201.line51 | — | — | — | — | — | — | — |
| ny_it201.line52 | — | — | — | — | — | — | — |
| ny_it201.gate.city_credits | — | — | — | — | — | — | — |
| ny_it201.line53 | — | — | — | — | — | — | — |
| ny_it201.line54 | — | — | — | — | — | — | — |
| ny_it201.mctmt_people | — | — | — | — | — | — | — |
| ny_it201.mctmt_possible | — | — | — | — | — | — | — |
| ny_it201.gate.mctmt | — | — | — | — | — | — | — |
| ny_it201.line54a | — | — | — | — | — | — | — |
| ny_it201.line54b | — | — | — | — | — | — | — |
| ny_it201.line54c | — | — | — | — | — | — | — |
| ny_it201.line54d | — | — | — | — | — | — | — |
| ny_it201.line54e | — | — | — | — | — | — | — |
| ny_it201.line55 | — | — | — | — | — | — | — |
| ny_it201.line56 | — | — | — | — | — | — | — |
| ny_it201.line57 | — | — | — | — | — | — | — |
| ny_it201.line58 | — | — | — | — | — | — | — |
| ny_it201.sut.b1 | — | — | — | — | — | — | — |
| ny_it201.sut.b2 | — | — | — | — | — | — | — |
| ny_it201.sut.b3 | — | — | — | — | — | — | — |
| ny_it201.sut.b4 | — | — | — | — | — | — | — |
| ny_it201.sut.b5 | — | — | — | — | — | — | — |
| ny_it201.sut.b6 | — | — | — | — | — | — | — |
| ny_it201.sut.b7 | — | — | — | — | — | — | — |
| ny_it201.sut.top_product | — | — | — | — | — | — | — |
| ny_it201.sut.cap | — | — | — | — | — | — | — |
| ny_it201.sut.top | — | — | — | — | — | — | — |
| ny_it201.sut.chart | — | — | — | — | — | — | — |
| ny_it201.gate.use_tax_abode | — | — | — | — | — | — | — |
| ny_it201.ask.use_tax_exact | — | — | — | — | — | — | — |
| ny_it201.use_tax_exact_if_small | — | — | — | — | — | — | — |
| ny_it201.gate.use_tax_st141 | — | — | — | — | — | — | — |
| ny_it201.line59 | — | — | — | — | — | — | — |
| ny_it201.zero_sut | — | — | — | — | — | — | — |
| ny_it201.gate.contributions | — | — | — | — | — | — | — |
| ny_it201.line60 | — | — | — | — | — | — | — |
| ny_it201.line61 | — | — | — | — | — | — | — |
| ny_it201.line62 | — | — | — | — | — | — | — |
| ny_it201.under17_count | — | — | — | — | — | — | — |
| ny_it201.gate.child_credit | — | — | — | — | — | — | — |
| ny_it201.line63 | — | — | — | — | — | — | — |
| ny_it201.federal_care | — | — | — | — | — | — | — |
| ny_it201.gate.dependent_care | — | — | — | — | — | — | — |
| ny_it201.line64 | — | — | — | — | — | — | — |
| ny_it201.gate.eic | — | — | — | — | — | — | — |
| ny_it201.line65 | — | — | — | — | — | — | — |
| ny_it201.gate.noncustodial | — | — | — | — | — | — | — |
| ny_it201.line66 | — | — | — | — | — | — | — |
| ny_it201.low_income | — | — | — | — | — | — | — |
| ny_it201.gate.real_property | — | — | — | — | — | — | — |
| ny_it201.line67 | — | — | — | — | — | — | — |
| ny_it201.gate.college_tuition | — | — | — | — | — | — | — |
| ny_it201.line68 | — | — | — | — | — | — | — |
| ny_it201.stc_income | — | — | — | — | — | — | — |
| ny_it201.stc_fixed_eligible | — | — | — | — | — | — | — |
| ny_it201.stc_fixed_amount | — | — | — | — | — | — | — |
| ny_it201.line69 | — | — | — | — | — | — | — |
| ny_it201.zero_stc | — | — | — | — | — | — | — |
| ny_it201.gate.stc_rr_income | — | — | — | — | — | — | — |
| ny_it201.stc_rr_low | — | — | — | — | — | — | — |
| ny_it201.stc_rr_excess | — | — | — | — | — | — | — |
| ny_it201.stc_rr_excess_product | — | — | — | — | — | — | — |
| ny_it201.stc_rr_base | — | — | — | — | — | — | — |
| ny_it201.stc_rr_high | — | — | — | — | — | — | — |
| ny_it201.stc_rr_low_band | — | — | — | — | — | — | — |
| ny_it201.stc_rr | — | — | — | — | — | — | — |
| ny_it201.line69a | — | — | — | — | — | — | — |
| ny_it201.line70 | — | — | — | — | — | — | — |
| ny_it201.gate.it270 | — | — | — | — | — | — | — |
| ny_it201.line70a | — | — | — | — | — | — | — |
| ny_it201.line71 | — | — | — | — | — | — | — |
| ny_it201.has_other_payments | — | — | — | — | — | — | — |
| ny_it201.gate.other_withholding | — | — | — | — | — | — | — |
| ny_it201.line72 | — | — | — | — | — | — | — |
| ny_it201.line73 | — | — | — | — | — | — | — |
| ny_it201.line74 | — | — | — | — | — | — | — |
| ny_it201.ask.est_any | — | — | — | — | — | — | — |
| ny_it201.line75_amount | — | — | — | — | — | — | — |
| ny_it201.line75 | — | — | — | — | — | — | — |
| ny_it201.line76 | — | — | — | — | — | — | — |
| ny_it201.tax_due | — | — | — | — | — | — | — |
| ny_it201.prepayments | — | — | — | — | — | — | — |
| ny_it201.safe_harbor_100 | — | — | — | — | — | — | — |
| ny_it201.safe_harbor_110 | — | — | — | — | — | — | — |
| ny_it201.safe_harbor | — | — | — | — | — | — | — |
| ny_it201.tax_due_positive | — | — | — | — | — | — | — |
| ny_it201.est_penalty_balance | — | — | — | — | — | — | — |
| ny_it201.est_below_safe_harbor | — | — | — | — | — | — | — |
| ny_it201.estimated_payments_positive | — | — | — | — | — | — | — |
| ny_it201.est_penalty_late | — | — | — | — | — | — | — |
| ny_it201.gate.estimated_penalty | — | — | — | — | — | — | — |
| ny_it201.line81 | — | — | — | — | — | — | — |
| ny_it201.gate.late | — | — | — | — | — | — | — |
| ny_it201.line82 | — | — | — | — | — | — | — |
| ny_it201.overpaid_before_penalty | — | — | — | — | — | — | — |
| ny_it201.line77 | — | — | — | — | — | — | — |
| ny_it201.has_overpayment | — | — | — | — | — | — | — |
| ny_it201.ask.apply_any | — | — | — | — | — | — | — |
| ny_it201.apply_if_overpaid | — | — | — | — | — | — | — |
| ny_it201.line79_wanted | — | — | — | — | — | — | — |
| ny_it201.line79_amount | — | — | — | — | — | — | — |
| ny_it201.line79 | — | — | — | — | — | — | — |
| ny_it201.gate.line79_over | — | — | — | — | — | — | — |
| ny_it201.line78 | — | — | — | — | — | — | — |
| ny_it201.has_refund | — | — | — | — | — | — | — |
| ny_it201.gate.refund_529 | — | — | — | — | — | — | — |
| ny_it201.line78a | — | — | — | — | — | — | — |
| ny_it201.line78b | — | — | — | — | — | — | — |
| ny_it201.line80 | — | — | — | — | — | — | — |
| ny_it201.spouse_not_resident | — | — | — | — | — | — | — |

Unasserted lines: ny_it201.state_resident_if_not_city, ny_it201.active_duty_if_armed_forces, ny_it201.moved, ny_it201.bab_if_interest, ny_it201.ask.special_code, ny_it201.gate.part_year_state, ny_it201.gate.part_year_city, ny_it201.gate.spouse_nonresident, ny_it201.gate.special_accrual, ny_it201.gate.yonkers, ny_it201.gate.special_code, ny_it201.gate.decedent, ny_it201.item_c_if_not_federal, ny_it201.item_c, ny_it201.item_h_count, ny_it201.line1, ny_it201.line2, ny_it201.line3, ny_it201.line4, ny_it201.line5, ny_it201.line6, ny_it201.line7, ny_it201.line8, ny_it201.line9, ny_it201.line10, ny_it201.line11, ny_it201.line12, ny_it201.line13, ny_it201.line14, ny_it201.line15, ny_it201.line16, ny_it201.line17, ny_it201.line18, ny_it201.line19, ny_it201.fagi_rounded, ny_it201.line19_agrees, ny_it201.has_tax_exempt, ny_it201.gate.line20, ny_it201.line20, ny_it201.public_job_if_w2, ny_it201.gate.line21, ny_it201.line21, ny_it201.edu_people, ny_it201.has_edu_account, ny_it201.ny_529_if_account, ny_it201.gate.line22, ny_it201.line22, ny_it201.gate.it225, ny_it201.line23, ny_it201.line24, ny_it201.has_other_income, ny_it201.inflation_if_other_income, ny_it201.gate.line25, ny_it201.line25, ny_it201.no, ny_it201.has_pension_income, ny_it201.gov_pension_if_income, ny_it201.gov_said_no, ny_it201.gov_pension_other_if_no, ny_it201.gov_pension_any, ny_it201.gate.line26, ny_it201.line26, ny_it201.line27, ny_it201.has_line28_income, ny_it201.gate.line28, ny_it201.line28, ny_it201.pension_59_people, ny_it201.pension_59_known, ny_it201.pension_exclusion_if_young, ny_it201.pension_exclusion_line, ny_it201.pension_exclusion_after_gov, ny_it201.gate.line29, ny_it201.line29, ny_it201.gate.line30, ny_it201.line30, ny_it201.line31, ny_it201.line32, ny_it201.line33, ny_it201.spouse_itemizes_if_mfs, ny_it201.gate.itemize, ny_it201.dependent_single, ny_it201.std_deduction, ny_it201.std_deduction_dependent, ny_it201.line34, ny_it201.line35, ny_it201.exemption, ny_it201.line36, ny_it201.line37, ny_it201.line38, ny_it201.agi_table_range, ny_it201.ti_table_range, ny_it201.tax_table, ny_it201.tax_schedule, ny_it201.tax_low, ny_it201.tcw.w1, ny_it201.tcw.w7, ny_it201.tcw.w12, ny_it201.tcw.w2, ny_it201.tcw.w3, ny_it201.tcw.w4, ny_it201.tcw.w5, ny_it201.tcw.w8, ny_it201.tcw.w9, ny_it201.tcw.w10, ny_it201.tcw.w13, ny_it201.tcw.w14, ny_it201.tcw.w15, ny_it201.tcw.top, ny_it201.tcw.mfj, ny_it201.tcw.single, ny_it201.tcw.hoh, ny_it201.tcw.by_status, ny_it201.agi_top, ny_it201.tax_high, ny_it201.line39, ny_it201.hh_agi, ny_it201.one, ny_it201.spouse_count, ny_it201.hh_people, ny_it201.hh_state_p1, ny_it201.hh_city_p1, ny_it201.hh_state_p2, ny_it201.hh_city_p2, ny_it201.hh_state_p3, ny_it201.hh_city_p3, ny_it201.hh_state_p4, ny_it201.hh_city_p4, ny_it201.hh_state_p5, ny_it201.hh_city_p5, ny_it201.hh_state_p6, ny_it201.hh_city_p6, ny_it201.hh_state_p7, ny_it201.hh_city_p7, ny_it201.hh_state_t2, ny_it201.hh_city_t5, ny_it201.hh_state_t1, ny_it201.hh_city_t4, ny_it201.zero, ny_it201.hh_state_in_range, ny_it201.gate.hh_state_mfs, ny_it201.gate.hh_state_over7, ny_it201.hh_state_by_status, ny_it201.hh_city_in_range, ny_it201.gate.hh_city_mfs, ny_it201.gate.hh_city_over7, ny_it201.hh_city_by_status, ny_it201.line40, ny_it201.gate.resident_credit, ny_it201.line41, ny_it201.gate.other_credits, ny_it201.line42, ny_it201.line43, ny_it201.line44, ny_it201.gate.other_taxes, ny_it201.line45, ny_it201.line46, ny_it201.line47, ny_it201.city_table_range, ny_it201.city_tax_table, ny_it201.city_tax_schedule, ny_it201.line47a, ny_it201.line48, ny_it201.line49, ny_it201.line50, ny_it201.line51, ny_it201.line52, ny_it201.gate.city_credits, ny_it201.line53, ny_it201.line54, ny_it201.mctmt_people, ny_it201.mctmt_possible, ny_it201.gate.mctmt, ny_it201.line54a, ny_it201.line54b, ny_it201.line54c, ny_it201.line54d, ny_it201.line54e, ny_it201.line55, ny_it201.line56, ny_it201.line57, ny_it201.line58, ny_it201.sut.b1, ny_it201.sut.b2, ny_it201.sut.b3, ny_it201.sut.b4, ny_it201.sut.b5, ny_it201.sut.b6, ny_it201.sut.b7, ny_it201.sut.top_product, ny_it201.sut.cap, ny_it201.sut.top, ny_it201.sut.chart, ny_it201.gate.use_tax_abode, ny_it201.use_tax_exact_if_small, ny_it201.gate.use_tax_st141, ny_it201.line59, ny_it201.zero_sut, ny_it201.gate.contributions, ny_it201.line60, ny_it201.line61, ny_it201.line62, ny_it201.under17_count, ny_it201.gate.child_credit, ny_it201.line63, ny_it201.federal_care, ny_it201.gate.dependent_care, ny_it201.line64, ny_it201.gate.eic, ny_it201.line65, ny_it201.gate.noncustodial, ny_it201.line66, ny_it201.low_income, ny_it201.gate.real_property, ny_it201.line67, ny_it201.gate.college_tuition, ny_it201.line68, ny_it201.stc_income, ny_it201.stc_fixed_eligible, ny_it201.stc_fixed_amount, ny_it201.line69, ny_it201.zero_stc, ny_it201.gate.stc_rr_income, ny_it201.stc_rr_low, ny_it201.stc_rr_excess, ny_it201.stc_rr_excess_product, ny_it201.stc_rr_base, ny_it201.stc_rr_high, ny_it201.stc_rr_low_band, ny_it201.stc_rr, ny_it201.line69a, ny_it201.line70, ny_it201.gate.it270, ny_it201.line70a, ny_it201.line71, ny_it201.has_other_payments, ny_it201.gate.other_withholding, ny_it201.line72, ny_it201.line73, ny_it201.line74, ny_it201.line75, ny_it201.line76, ny_it201.tax_due, ny_it201.prepayments, ny_it201.safe_harbor_100, ny_it201.safe_harbor_110, ny_it201.safe_harbor, ny_it201.tax_due_positive, ny_it201.est_penalty_balance, ny_it201.est_below_safe_harbor, ny_it201.estimated_payments_positive, ny_it201.est_penalty_late, ny_it201.gate.estimated_penalty, ny_it201.line81, ny_it201.gate.late, ny_it201.line82, ny_it201.overpaid_before_penalty, ny_it201.line77, ny_it201.has_overpayment, ny_it201.apply_if_overpaid, ny_it201.line79_wanted, ny_it201.line79, ny_it201.gate.line79_over, ny_it201.line78, ny_it201.has_refund, ny_it201.gate.refund_529, ny_it201.line78a, ny_it201.line78b, ny_it201.line80, ny_it201.spouse_not_resident

## Schedule 1, line 8z — other income, one entry per item listed

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| oi8z.kind | — | — | — | — | — | — | — |
| oi8z.amount | — | — | — | — | — | — | — |
| oi8z.recovery | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | — |
| oi8z.additional_tax | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | — |
| oi8z.figured | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | — |
| oi8z.no | — | — | — | — | — | — | — |
| oi8z.injury | — | — | — | — | — | — | — |
| oi8z.damages | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | — |
| oi8z.injury_if_damages | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | — |
| oi8z.taxable | — | — | — | 2 (classm.oi8z.1, classm.oi8z.2) | — | — | 7 |

Unasserted lines: oi8z.no

## Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| otjob.one | — | — | — | — | — | — | — |
| otjob.zero | — | — | — | — | — | — | — |
| otjob.flsa | — | — | — | — | — | — | — |
| otjob.special_rule | — | — | — | — | — | — | — |
| otjob.method | — | — | — | — | — | — | — |
| otjob.statement | — | — | — | — | — | — | — |
| otjob.refused | — | — | — | 3 | — | — | — |
| otjob.figured | — | — | — | 3 | — | — | — |
| otjob.by_third | — | — | — | 2 (classm.otjob.1, classm.otjob.2) | — | — | — |
| otjob.by_half | — | — | — | 2 (classm.otjob.1, classm.otjob.2) | — | — | — |
| otjob.by_quarter | — | — | — | 2 (classm.otjob.1, classm.otjob.3) | — | — | — |
| otjob.col_b | — | — | — | 3 | — | — | — |

Unasserted lines: otjob.one, otjob.zero

## Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| person.role | — | — | — | — | — | — | — |
| person.one | — | — | — | — | — | — | — |
| person.birth_year | — | — | — | — | — | — | — |
| person.birth_cut_year | — | — | — | — | — | — | — |
| person.born_jan1 | — | — | — | — | — | — | — |
| person.born_jan1_if_cut_year | — | — | — | — | — | — | — |
| person.birth_year_bad | — | — | — | — | — | — | 1 (mutation.m1.person.birth_year_after_tax_year) |
| person.age65 | — | — | — | — | — | — | — |
| person.under24 | — | — | — | — | — | — | 2 (mutation.m1.person.jan1_2001_2002, mutation.m1.person.born_2002_not_jan1_and_jan1_2007) |
| person.blind | — | — | — | — | — | — | — |
| person.tin | — | — | — | — | — | — | — |
| person.itin_applied | — | — | — | — | — | — | — |
| person.work_ssn | — | — | — | — | — | — | — |
| person.eic_ssn | — | — | — | — | — | — | — |
| person.under16 | — | — | — | — | — | — | 2 (mutation.m1.person.born_2010_under16, mutation.m1.person.born_2010_not_under16) |
| person.under16_open_year | — | — | — | — | — | — | — |
| person.under16_at_year_end | — | — | — | — | — | — | — |
| person.under16_at_year_end_if_open_year | — | — | — | — | — | — | — |
| person.educator_expenses | — | — | — | — | — | — | — |
| person.eligible_educator | — | — | — | — | — | — | — |
| person.educator_expenses_if_educator | — | — | — | — | — | — | — |
| person.eic_age25 | — | — | — | — | — | — | 1 (mutation.m1.person.jan1_2001_2002) |
| person.eic_under65 | — | — | — | — | — | — | — |
| person.age65_box | — | — | — | — | — | — | — |
| person.not_died_before_65 | — | — | — | — | — | — | — |
| person.tin_or_itin_applied | — | — | — | — | — | — | 1 (mutation.m1.person.died_at_64_and_born_1961) |
| person.work_ssn_or_tin | — | — | — | — | — | — | — |
| person.turned_65_this_year | — | — | — | — | — | — | 1 (mutation.m1.person.died_at_64_and_born_1961) |
| person.died_before_65 | — | — | — | — | — | — | 1 (mutation.m1.person.died_at_64_and_born_1961) |
| person.died_at_64 | — | — | — | — | — | — | — |
| person.educator_max | — | — | — | — | — | — | — |
| person.has_educator_expenses | — | — | — | — | — | — | — |
| person.educator_limited | — | — | — | — | — | — | — |
| person.educator_eligible_amount | — | — | — | — | — | — | — |
| person.educator_deduction | — | — | — | — | — | — | — |
| person.hsa_forms | — | — | — | — | — | — | — |
| person.hsa_repeated | — | — | — | — | — | — | — |
| person.hsa_split | — | — | — | — | — | — | — |
| person.hsa_agreed | — | — | — | — | — | — | — |
| person.hsa_step1 | — | — | — | — | — | — | 1 (stage19.mut.hsa_one_form_no_split) |
| person.hsa_share | — | — | — | — | — | — | 1 (stage19.mut.hsa_one_form_no_split) |
| person.hsa_deduction | — | — | — | — | — | — | — |
| person.hsa_taxable | — | — | — | — | — | — | — |
| person.hsa_addtax | — | — | — | — | — | — | — |
| person.tip_employers | — | — | — | — | — | — | — |
| person.tip_total | — | — | — | — | — | — | — |
| person.tip_reported | — | — | — | — | — | — | — |
| person.ot_employers | — | — | — | — | — | — | — |
| person.ot_total | — | — | — | — | — | — | — |
| person.rrta | — | — | — | — | — | — | — |
| person.sc_rrta_count | — | — | — | — | — | — | — |
| person.se_rrta | — | — | — | — | — | — | — |
| person.employers | — | — | — | 24 | — | — | — |
| person.overcount | — | — | — | 24 | — | — | — |
| person.over | — | — | — | 24 | — | — | — |
| person.wages | — | — | — | 9 | — | — | — |
| person.withheld | — | — | — | 24 | — | — | — |
| person.box1 | — | — | — | — | — | — | — |
| person.box2 | — | — | — | — | — | — | — |
| person.f8919_firms | — | — | — | — | — | — | — |
| person.f8919_wages | — | — | — | — | — | — | — |
| person.f8919_any | — | — | — | — | — | — | — |
| person.f8919_line10_figured | — | — | — | — | — | — | — |
| person.f8919_line10 | — | — | — | — | — | — | — |
| person.f8919_tax_figured | — | — | — | — | — | — | — |
| person.f8919_tax | — | — | — | — | — | — | — |
| person.f4137_rows_c | — | — | — | — | — | — | — |
| person.f4137_col_c | — | — | — | — | — | — | — |
| person.f4137_rows_d | — | — | — | — | — | — | — |
| person.f4137_col_d | — | — | — | — | — | — | — |
| person.f4137_under20 | — | — | — | — | — | — | — |
| person.f4137_under20_if_rows | — | — | — | — | — | — | — |
| person.tips_gov | — | — | — | — | — | — | — |
| person.tips_gov_if_rows | — | — | — | — | — | — | — |
| person.tips_noncash | — | — | — | — | — | — | — |
| person.tips_noncash_if_unreported | — | — | — | — | — | — | — |
| person.f4137_line4 | — | — | — | — | — | — | — |
| person.f4137_line6_figured | — | — | — | — | — | — | — |
| person.f4137_line6 | — | — | — | — | — | — | — |
| person.f4137_line10_figured | — | — | — | — | — | — | — |
| person.f4137_line10 | — | — | — | — | — | — | — |
| person.f4137_tax_figured | — | — | — | — | — | — | — |
| person.f4137_tax | — | — | — | — | — | — | — |
| person.line1c | — | — | — | — | — | — | — |
| person.f4137_filed | — | — | — | — | — | — | 1 (mexist.person.f4137_filed.noncash_only) |
| person.household_wages | — | — | — | — | — | — | — |
| person.household_wages_if_pay | — | — | — | — | — | — | — |
| person.strike | — | — | — | — | — | — | — |
| person.strike_if_pay | — | — | — | — | — | — | — |
| person.mw_box1 | — | — | — | — | — | — | — |
| person.mw_box1_if_mw | — | — | — | — | — | — | — |
| person.mw_not_box1 | — | — | — | — | — | — | — |
| person.mw_not_box1_if_mw | — | — | — | — | — | — | — |
| person.mw_has_not_box1 | — | — | — | — | — | — | — |
| person.mw_1099 | — | — | — | — | — | — | — |
| person.mw_1099_if_not_box1 | — | — | — | — | — | — | — |
| person.mw_has_1099 | — | — | — | — | — | — | — |
| person.mw_1099_over | — | — | — | — | — | — | — |
| person.mw_business | — | — | — | — | — | — | — |
| person.mw_business_if_1099 | — | — | — | — | — | — | — |
| person.mw_total | — | — | — | — | — | — | — |
| person.mw_paid | — | — | — | — | — | — | — |
| person.mw_earned | — | — | — | — | — | — | — |
| person.mw_earned_if_paid | — | — | — | — | — | — | — |
| person.mw_other | — | — | — | — | — | — | — |
| person.mw_other_1d | — | — | — | — | — | — | — |
| person.line1d | — | — | — | — | — | — | — |
| person.line8s | — | — | — | — | — | — | — |
| person.mw_not_earned | — | — | — | — | — | — | — |
| person.earned_not_w2 | — | — | — | — | — | — | — |
| person.ira_amount_a | — | — | — | — | — | — | — |
| person.ira_taxable | — | — | — | — | — | — | — |
| person.ira_rollovers | — | — | — | — | — | — | — |
| person.plan_amount_a | — | — | — | — | — | — | — |
| person.plan_taxable | — | — | — | — | — | — | — |
| person.dis_wages | — | — | — | — | — | — | — |
| person.line1h | — | — | — | — | — | — | — |
| person.plan_rollovers | — | — | — | — | — | — | — |
| person.sav_dist | — | — | — | — | — | — | — |
| person.eligible | — | — | — | 24 | — | — | — |
| person.excess | — | — | — | 24 | — | — | — |
| person.zero | — | — | — | — | — | — | — |
| person.credit | — | — | — | 24 | — | — | — |
| person.medicare5 | — | — | — | — | — | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.medicare6 | — | — | — | — | — | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.sc_count | — | — | — | — | — | — | — |
| person.ho_count | — | — | — | — | — | — | — |
| person.sc_credit_count | — | — | — | — | — | — | — |
| person.sc_fuel_count | — | — | — | — | — | — | — |
| person.mq_q4 | — | — | — | — | — | — | — |
| person.mq_total | — | — | — | — | — | — | — |
| person.cost179 | — | — | — | — | — | — | — |
| person.s179_nonlisted | — | — | — | — | — | — | — |
| person.s179_listed | — | — | — | — | — | — | — |
| person.income179 | — | — | — | — | — | — | — |
| person.has_sc | — | — | — | — | — | — | — |
| person.sc_total | — | — | — | — | — | — | — |
| person.se_screen | — | — | — | — | — | — | — |
| person.se_screened | — | — | — | — | — | — | — |
| person.se_line2 | — | — | — | — | — | — | 2 (stage14.asset.s179, stage14.refuse.se_screen) |
| person.se_line6 | — | — | — | — | — | OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 5 |
| person.se_line12 | — | — | — | — | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded; OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 12 |
| person.se_line13 | — | — | — | — | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded; OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 2 (x2pay.f8919.w4_with_se, stage14.refuse.se_railroad) |
| person.se_line4c | — | — | — | — | — | OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 2 (stage19.mut.se_not_filed_loss, stage14.refuse.se_railroad) |
| person.plan | — | — | — | — | — | — | — |
| person.plan_screen | — | — | — | — | — | — | — |
| person.plan_screened | — | — | — | — | — | — | — |
| person.cent | — | — | — | — | — | — | — |
| person.hundred | — | — | — | — | — | — | — |
| person.sep_rate | — | — | — | — | — | — | — |
| person.sep_contrib | — | — | — | — | — | — | 1 (stage14.plan.refuse_screen) |
| person.sep_rate_c | — | — | — | — | — | — | — |
| person.sep_rate_plus | — | — | — | — | — | — | — |
| person.sep_shown | — | — | — | — | — | — | 2 (stage14.sep.worksheet_shown, stage14.sep.worksheet_hidden) |
| person.sep_s1 | — | — | — | 1 (classm.person.6) | — | — | 2 (stage14.sep.step1_other_se_income, stage14.sep.loss_floor) |
| person.sep_s2 | — | — | — | 1 (classm.person.6) | — | — | — |
| person.sep_s3 | — | — | — | 1 (classm.person.6) | — | — | 1 (stage14.sep.loss_floor) |
| person.sep_s5 | — | — | — | 1 (classm.person.6) | — | — | 3 |
| person.comp_limit | — | — | — | — | — | — | — |
| person.sep_s6 | — | — | — | 1 (classm.person.6) | — | — | 1 (stage14.sep.dollar_limit) |
| person.sep_s7 | — | — | — | 1 (classm.person.6) | — | — | 2 (stage14.sep.rate_5, stage14.sep.loss_floor) |
| person.sep_s8 | — | — | — | — | — | — | — |
| person.sep_s21 | — | — | — | 1 (classm.person.6) | — | — | 5 |
| person.sep_excess | — | — | — | — | — | — | 1 (stage14.sep.loss_floor) |
| person.sep_deduction | — | — | — | — | — | — | 2 (stage14.sep.refuse_excess, stage14.plan.refuse_two_businesses) |
| person.simple_deferral | — | — | — | — | — | — | 1 (stage14.plan.refuse_screen_simple) |
| person.simple_age | — | — | — | — | — | — | 3 |
| person.simple_age_60_63_years | — | — | — | — | — | — | — |
| person.simple_age_50_59_years | — | — | — | — | — | — | — |
| person.simple_age_under50_years | — | — | — | — | — | — | — |
| person.simple_open_year | — | — | — | — | — | — | — |
| person.simple_age_at_year_end | — | — | — | — | — | — | — |
| person.simple_age_if_open_year | — | — | — | — | — | — | — |
| person.simple_age_from_age50 | — | — | — | — | — | — | — |
| person.catchup_under50 | — | — | — | — | — | — | — |
| person.catchup_age50 | — | — | — | — | — | — | — |
| person.catchup_age60_63 | — | — | — | — | — | — | — |
| person.simple_kind | — | — | — | — | — | — | — |
| person.simple_employer | — | — | — | — | — | — | — |
| person.simple_comp | — | — | — | — | — | — | 1 (stage14.simple.match_age50) |
| person.simple_cap | — | — | — | — | — | — | — |
| person.simple_regular | — | — | — | — | — | — | — |
| person.simple_catchup | — | — | — | — | — | — | — |
| person.catchup_limit | — | — | — | — | — | — | — |
| person.comp_after_regular | — | — | — | — | — | — | — |
| person.catchup_max | — | — | — | — | — | — | 2 (stage14.simple.nonelective_60, stage14.simple.refuse_catchup_comp) |
| person.rate3 | — | — | — | — | — | — | — |
| person.rate2 | — | — | — | — | — | — | — |
| person.match_3pct | — | — | — | — | — | — | — |
| person.deferrals_total | — | — | — | — | — | — | — |
| person.match_max | — | — | — | — | — | — | 2 (stage14.simple.match_age50, stage14.simple.match_high_comp) |
| person.ne_comp | — | — | — | — | — | — | — |
| person.ne_max | — | — | — | — | — | — | 2 (stage14.simple.nonelective_60, stage14.simple.comp_cap) |
| person.employer_max | — | — | — | — | — | — | — |
| person.simple_excess | — | — | — | — | — | — | 1 (stage14.mut.simple_deferral_over_compensation) |
| person.simple_deduction | — | — | — | — | — | — | 4 |
| person.plan_deduction | — | — | — | — | — | — | — |
| person.s16 | — | — | — | — | — | — | — |
| person.positive_profits | — | — | — | — | — | — | — |
| person.sehi | — | — | — | — | — | — | — |
| person.amt_dep_f17 | — | — | — | — | — | — | — |
| person.amt_dep_y3 | — | — | — | — | — | — | — |
| person.amt_dep_y5 | — | — | — | — | — | — | — |
| person.amt_dep_y7 | — | — | — | — | — | — | — |
| person.amt_dep_y10 | — | — | — | — | — | — | — |
| person.amt_dep_listed | — | — | — | — | — | — | — |
| person.amt_dep | — | — | — | — | — | — | — |
| person.qbi | — | — | — | — | — | — | — |
| person.eic_part1 | — | — | — | — | — | — | — |
| person.files_se | — | — | — | — | — | — | 1 (stage19.mut.se_not_filed_loss) |
| person.eic_se_has | — | — | — | — | — | — | — |
| person.eic_se | — | — | — | — | — | — | 1 (stage14.sep.step1_other_se_income) |
| person.sc_1a | — | — | — | — | — | — | — |
| person.dc_benefits | — | — | — | — | — | — | — |
| person.dc_box10 | — | — | — | — | — | — | — |
| person.dc_has_box10 | — | — | — | — | — | — | 1 (stage15.refuse.w2.box10_bad) |
| person.dc_1e_mine | — | — | — | — | — | — | — |
| person.dc_1e_counted | — | — | — | — | — | — | — |
| person.dc_zero | — | — | — | — | — | — | — |
| person.dc_1e | — | — | — | — | — | — | — |
| person.dc_earned | — | — | — | — | — | — | — |
| person.dc_earned_b | — | — | — | — | — | — | — |
| person.sav_born | — | — | — | — | — | — | 1 (mutation.m1.person.jan1_2008) |
| person.sav_student | — | — | — | — | — | — | — |
| person.sav_claimed | — | — | — | — | — | — | — |
| person.sav_ineligible | — | — | — | — | — | — | 2 (dep.saver_claimed_no_credit, stage4.mut.savers_claimed_dependent) |
| person.ira_owner | — | — | — | — | — | — | — |
| person.sav_trad_if_ira_owner | — | — | — | — | — | — | — |
| person.sav_trad | — | — | — | — | — | — | — |
| person.sav_able | — | — | — | — | — | — | — |
| person.sav_roth | — | — | — | — | — | — | — |
| person.sav_roth_if_ira_owner | — | — | — | — | — | — | — |
| person.sav_line1 | — | — | — | — | — | — | 2 (stage15.refuse.person.sav_able, stage16.refuse.person.ira_excess) |
| person.sav_w2 | — | — | — | — | — | — | — |
| person.sav_excess | — | — | — | — | — | — | — |
| person.no | — | — | — | — | — | — | — |
| person.sav_has_w2 | — | — | — | — | — | — | — |
| person.sav_excess_gate | — | — | — | — | — | — | — |
| person.sav_voluntary | — | — | — | — | — | — | — |
| person.sav_simple_plan | — | — | — | — | — | — | — |
| person.sav_simple | — | — | — | — | — | — | — |
| person.sav_line2 | — | — | — | — | — | — | 2 (mutation.m1.person.spouse_no_deferrals_excess_other, stage15.refuse.person.sav_excess) |
| person.sav_prior_joint | — | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.sav_prior_other | — | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.ira_trad | — | — | — | — | — | — | — |
| person.ira_contrib | — | — | — | — | — | — | — |
| person.ira_has | — | — | — | — | — | — | — |
| person.ira_any_contrib | — | — | — | — | — | — | 1 (mutation.t2.no_5695_part1_s3_5a) |
| person.ira_excess | — | — | — | — | — | — | — |
| person.ira_extra_left | — | — | — | — | — | — | — |
| person.ira_recharacterized | — | — | — | — | — | — | — |
| person.ira_excess_gate | — | — | — | — | — | — | 1 (mutation.t3.roth_excess_screen) |
| person.ira_age50 | — | — | — | — | — | — | 1 (mutation.m1.person.born_1976_age50_both_answers) |
| person.age50_open_year | — | — | — | — | — | — | — |
| person.age50_at_year_end | — | — | — | — | — | — | — |
| person.age50_at_year_end_if_open_year | — | — | — | — | — | — | — |
| person.age55_open_year | — | — | — | — | — | — | — |
| person.age55_at_year_end | — | — | — | — | — | — | — |
| person.age55_at_year_end_if_open_year | — | — | — | — | — | — | 1 (mutation.m1.person.born_1971_age55_and_1970) |
| person.ira_work_plan | — | — | — | — | — | — | — |
| person.ira_se_plan | — | — | — | — | — | — | 1 (mutation.t2.no_carloan_part4) |
| person.ira_cov | — | — | — | — | — | — | 2 (stage21.f1.lower_bound_still_decides, mutation.t2.no_carloan_part4) |
| person.ira_limit_under50 | — | — | — | — | — | — | — |
| person.ira_limit_over50 | — | — | — | — | — | — | — |
| person.ira_limit | — | — | — | — | — | — | — |
| person.ira_not_covered_joint | — | — | — | — | — | — | — |
| person.ira_line2_table | — | — | — | — | — | — | — |
| person.ira_line2_apart | — | — | — | — | — | — | — |
| person.ira_line2_status | — | — | — | — | — | — | — |
| person.ira_line2_nc | — | — | — | — | — | — | — |
| person.ira_line2 | — | — | — | — | — | — | — |
| person.ira_line6 | — | — | — | — | — | — | 2 (audit.ira.covered_age50_single_phaseout, audit.ira.covered_age50_joint_phaseout) |
| person.ira_line6_yes | — | — | — | — | — | — | — |
| person.ira_wide | — | — | — | — | — | — | 1 (mutation.t2.mfj_sdtw_skip23) |
| person.ira_full_narrow | — | — | — | — | — | — | — |
| person.ira_full_joint | — | — | — | — | — | — | — |
| person.ira_full | — | — | — | — | — | — | — |
| person.ira_at_full | — | — | — | — | — | — | — |
| person.ira_p70 | — | — | — | — | — | — | — |
| person.ira_p80 | — | — | — | — | — | — | — |
| person.ira_p35 | — | — | — | — | — | — | — |
| person.ira_p40 | — | — | — | — | — | — | — |
| person.ira_prod_wide | — | — | — | — | — | — | — |
| person.ira_prod_joint | — | — | — | — | — | — | — |
| person.ira_prod | — | — | — | — | — | — | 2 (audit.ira.covered_age50_single_phaseout, audit.ira.covered_age50_joint_phaseout) |
| person.ira_rounded | — | — | — | — | — | — | 2 (audit.ira.covered_age50_single_phaseout, audit.ira.covered_age50_joint_phaseout) |
| person.ira_min | — | — | — | — | — | — | — |
| person.ira_floor | — | — | — | — | — | — | — |
| person.ira_below | — | — | — | — | — | — | — |
| person.ira_line7_figured | — | — | — | — | — | — | — |
| person.ira_line7 | — | — | — | — | — | — | — |
| person.ira_over_limit | — | — | — | — | — | — | — |
| person.ira_own_total | — | — | — | — | — | — | — |
| person.ira_line11 | — | — | — | — | — | — | 11 |
| person.ira_7or10 | — | — | — | — | — | — | — |
| person.ira_line12 | — | — | — | — | — | — | 1 (stage16.refuse.ira.dist) |
| person.ira_deduction | — | — | — | — | — | — | 1 (stage16.refuse.ira.dist) |
| person.ira_10or11 | — | — | — | — | — | — | — |
| person.ira_nd_figured | — | — | — | — | — | — | — |
| person.ira_nondeductible | — | — | — | — | — | — | — |
| person.ira_files_8606 | — | — | — | — | — | — | 1 (mutation.eic.line5_key.no_child) |
| person.ira_basis | — | — | — | — | — | — | — |
| person.ira_basis_adjusted | — | — | — | — | — | — | — |
| person.ira_basis_gate | — | — | — | — | — | — | — |
| person.ira_8606_line2 | — | — | — | — | — | — | 1 (stage16.refuse.person.ira_basis_adjusted) |
| person.ira_dist | — | — | — | — | — | — | — |
| person.ira_dist_if_files | — | — | — | — | — | — | — |
| person.ira_dist_gate | — | — | — | — | — | — | — |
| person.ira_8606_line14 | — | — | — | — | — | — | — |
| person.ira_ssb_lim | — | — | — | — | — | — | 1 (stage19.mut.ira_ssb_copy_limit) |
| person.ira_ssb_figured | — | — | — | — | — | — | 1 (stage16.refuse.ira.ssb_covered) |
| person.ira_ssb | — | — | — | — | — | — | 1 (stage16.refuse.ira.ssb_covered) |
| person.ira_se_take | — | — | — | — | — | — | — |
| person.ira_se_figured | — | — | — | — | — | — | — |
| person.ira_se | — | — | — | — | — | — | — |
| person.edu | — | — | — | — | — | — | — |
| person.edu_1098t | — | — | — | — | — | — | — |
| person.edu_student | — | — | — | — | — | — | 1 (mutation.t4.person_edu_paid_no_ira_dist) |
| person.edu_student_edu | — | — | — | — | — | — | — |
| person.edu_student_tin | — | — | — | — | — | — | — |
| person.edu_student_itin | — | — | — | — | — | — | — |
| person.edu_inst | — | — | — | — | — | — | — |
| person.edu_mat | — | — | — | — | — | — | — |
| person.edu_a_this_year | — | — | — | — | — | — | — |
| person.edu_a_next_year | — | — | — | — | — | — | — |
| person.edu_refunds | — | — | — | — | — | — | — |
| person.edu_adj_sum | — | — | — | — | — | — | — |
| person.edu_adj | — | — | — | — | — | — | — |
| person.edu_over | — | — | — | — | — | — | — |
| person.edu_has_adj | — | — | — | — | — | — | — |
| person.edu_over_if_adj | — | — | — | — | — | — | — |
| person.edu_over_refused | — | — | — | — | — | — | 2 (mutation.t3.person_edu_1098t_unanswered, mutation.t4.person_edu_paid_no_ira_dist) |
| person.edu_line23 | — | — | — | — | — | — | 9 |
| person.edu_show24 | 1 (stage19.example.aoc_phaseout) | — | — | — | — | — | 1 (stage19.refuse.period_over_person) |
| person.edu_line24 | — | — | — | — | — | — | 9 |
| person.edu_show25 | 1 (stage19.example.aoc_phaseout) | — | — | — | — | — | — |
| person.edu_line25 | — | — | — | — | — | — | 7 |
| person.edu_show26 | 1 (stage19.example.aoc_phaseout) | — | — | — | — | — | 1 (stage19.refuse.period_over_dependent) |
| person.edu_line26 | — | — | — | — | — | — | 6 |
| person.edu_ein | — | — | — | — | — | — | — |
| person.edu_no | — | — | — | — | — | — | — |
| person.edu_aoc | — | — | — | — | — | — | 1 (mutation.t4.person_edu_paid_no_ira_dist) |
| person.edu_aoc23 | — | — | — | — | — | — | — |
| person.edu_aoc24 | — | — | — | — | — | — | — |
| person.edu_aoc25 | — | — | — | — | — | — | — |
| person.edu_aoc26 | — | — | — | — | — | — | — |
| person.edu_aoc_tin | — | — | — | — | — | — | — |
| person.edu_llc | — | — | — | — | — | — | 1 (mutation.t4.person_edu_paid_no_ira_dist) |
| person.edu_llc_tin_refused | — | — | — | — | — | — | — |
| person.edu_line27 | 7 | — | — | — | — | — | 9 |
| person.edu_line28 | — | — | — | — | — | — | 7 |
| person.edu_line29 | — | — | — | — | — | — | 7 |
| person.edu_line30 | 1 (stage19.example.aoc_phaseout) | — | — | — | — | — | 9 |
| person.edu_line31 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | — | — | — | 7 |
| person.edu_over18 | — | — | — | — | — | — | 1 (mutation.m1.person.born_2002_not_jan1_and_jan1_2007) |
| person.edu_age24 | — | — | — | — | — | — | 2 (mutation.m1.person.jan1_2001_2002, mutation.m1.person.born_2002_not_jan1_and_jan1_2007) |
| person.edu_fulltime | — | — | — | — | — | — | — |
| person.edu_half_support | — | — | — | — | — | — | — |
| person.edu_parent | — | — | — | — | — | — | — |
| person.edu_kid_age | — | — | — | — | — | — | — |
| person.edu_kid_18 | — | — | — | — | — | — | — |
| person.edu_kid_18_support | — | — | — | — | — | — | — |
| person.edu_kid_student_age | — | — | — | — | — | — | — |
| person.edu_kid_support | — | — | — | — | — | — | — |
| person.edu_kid_fulltime | — | — | — | — | — | — | — |
| person.edu_kid | — | — | — | — | — | — | 2 (stage19.mut.aoc_student_18_half_support, stage19.mut.aoc_student_20_not_fulltime) |
| person.x_l1 | — | — | — | via f5329.l1: 3 | — | — | — |
| person.x_l2_all | — | — | — | — | — | — | — |
| person.x_l1_s | — | — | — | — | — | — | — |
| person.x_l2_s | — | — | — | — | — | — | — |
| person.x_e05 | — | — | — | — | — | — | — |
| person.x_e09 | — | — | — | — | — | — | — |
| person.x_e19 | — | — | — | — | — | — | — |
| person.x_e22 | — | — | — | — | — | — | — |
| person.x_e23 | — | — | — | — | — | — | — |
| person.x_tax | — | — | — | — | — | — | — |
| person.x_must | — | — | — | — | — | — | — |
| person.x_prior09 | — | — | — | — | — | — | — |
| person.x_cap09_base | — | — | — | — | — | — | — |
| person.x_cap09 | — | — | — | — | — | — | — |
| person.x_births | — | — | — | — | — | — | — |
| person.x_cap19_one | — | — | — | — | — | — | — |
| person.x_cap19 | — | — | — | — | — | — | — |
| person.x_cap22 | — | — | — | — | — | — | — |
| person.x_cap23 | — | — | — | — | — | — | — |
| person.x_c05 | — | — | — | — | — | — | 1 (mutation.m1.person.no_e05_schedule_a_refused) |
| person.x_has05 | — | — | — | — | — | — | — |
| person.x_c05_min | — | — | — | — | — | — | — |
| person.x_has09 | — | — | — | — | — | — | — |
| person.x_c09_min | — | — | — | — | — | — | — |
| person.x_c09 | — | — | — | — | — | — | — |
| person.x_has19 | — | — | — | — | — | — | — |
| person.x_c19_min | — | — | — | — | — | — | — |
| person.x_c19 | — | — | — | — | — | — | — |
| person.x_c22 | — | — | — | — | — | — | — |
| person.x_c23 | — | — | — | — | — | — | — |
| person.x_n23 | — | — | — | — | — | — | — |
| person.x_two23 | — | — | — | — | — | — | — |
| person.x_capped_sum | — | — | — | — | — | — | — |
| person.x_limited_sum | — | — | — | — | — | — | — |
| person.x_other_exc | — | — | — | — | — | — | — |
| person.x_limit_binds | — | — | — | — | — | — | — |
| person.x_other | — | — | — | — | — | — | — |
| person.x_edu_account | — | — | — | — | — | — | — |
| person.x_edu_taxable | — | — | — | — | — | — | — |
| person.x_edu_taxable_if_account | — | — | — | — | — | — | — |
| person.x_edu_excess | — | — | — | — | — | — | — |
| person.x_edu_excess_if_account | — | — | — | — | — | — | — |
| person.x_archer_excess | — | — | — | — | — | — | — |
| person.x_ira_prior_excess | — | — | — | — | — | — | — |
| person.x_ira_prior_excess_if_ira_owner | — | — | — | — | — | — | — |
| person.has_hsa | — | — | — | — | — | — | 1 (mutation.m1.person.hsa_prior_excess_born_1950) |
| person.x_hsa_prior_excess | — | — | — | — | — | — | — |
| person.x_hsa_prior_excess_if_hsa | — | — | — | — | — | — | 2 (mutation.m1.person.jan1_2008, mutation.m1.person.hsa_prior_excess_born_1950) |
| person.rmd_age | — | — | — | — | — | — | 1 (mutation.m1.person.born_1971_age55_and_1970) |
| person.inherited_account | — | — | — | — | — | — | — |
| person.inherited_account_if_under_73 | — | — | — | — | — | — | 2 (mutation.m1.person.rmd_age_and_inherited, mutation.m1.person.hsa_prior_excess_born_1950) |
| person.rmd_possible | — | — | — | — | — | — | 1 (mutation.m1.person.rmd_age_and_inherited) |
| person.rmd_missed | — | — | — | — | — | — | — |
| person.rmd_missed_if_possible | — | — | — | — | — | — | — |
| person.x_hsa_value | — | — | — | — | — | — | — |
| person.x_hsa_excess | — | — | — | via f5329.l47: 3; via f5329.l48 → f5329.l47: 3 | — | — | — |
| person.senior_work_ssn | — | — | — | — | — | — | — |
| person.spouse_senior_work_ssn | — | — | — | — | — | — | — |
| person.k1p_total_passive_income | — | — | — | — | — | — | 3 |
| person.k1p_total_nonpassive_income | — | — | — | — | — | — | 4 |
| person.k1p_total_nonpassive_loss | — | — | — | — | — | — | 4 |
| person.k1p_total_nonpassive | — | — | — | — | — | — | 3 |
| person.k1p_total_p4_income | — | — | — | — | — | — | 3 |
| person.k1p_total_p4_loss | — | — | — | — | — | — | 2 (x2k1p.fk3b_general_active, mk1.k1p.refuse_box4b) |
| person.k1p_total_p4_prior | — | — | — | — | — | — | 1 (x2k1p.refuse_prior_not_active) |
| person.k1p_total_p5_income | — | — | — | — | — | — | 4 |
| person.k1p_total_p5_loss | — | — | — | — | — | — | 7 |
| person.k1p_total_p5_prior | — | — | — | — | — | — | 5 |
| person.k1p_total_p6_loss | — | — | — | — | — | — | 2 (x2k1p.fk3b_general_active, mk1.k1p.refuse_box4b) |
| person.k1p_total_prior | — | — | — | — | — | — | 5 |
| person.k1p_total_interest | — | — | — | — | — | — | 4 |
| person.k1p_total_ord_div | — | — | — | — | — | — | 3 |
| person.k1p_total_qual_div | — | — | — | — | — | — | 3 |
| person.k1p_total_st_gain | — | — | — | — | — | — | 3 |
| person.k1p_total_lt_gain | — | — | — | — | — | — | 5 |
| person.k1p_total_collectibles | — | — | — | — | — | — | 4 |
| person.k1p_total_unrecap_1250 | — | — | — | — | — | — | 4 |
| person.k1p_total_se_earnings | — | — | — | — | — | — | 2 (x2k1p.fk2_general_material, x2k1p.refuse_se_loss_passive) |
| person.k1p_total_se_pos | — | — | — | — | — | — | 3 |
| person.k1p_total_backup_wh | — | — | — | — | — | — | 3 |
| person.k1p_total_taxexempt_int | — | — | — | — | — | — | 3 |
| person.k1p_total_qbi_stmt | — | — | — | — | — | — | 4 |
| person.k1p_count | — | — | — | — | — | — | 2 (mk1.k1p.refuse_box4b, mk1.k1p.refuse_box12) |
| person.k1p_count_sche | — | — | — | — | — | — | 10 |
| person.k1p_count_passive_loss | — | — | — | — | — | — | 5 |
| person.k1p_count_inv | — | — | — | — | — | — | 3 |
| person.k1p_count_general | — | — | — | — | — | — | 2 (mk1.k1p.refuse_box4b, mk1.k1p.refuse_test7) |
| person.k1s_total_interest | — | — | — | — | — | — | 1 (k1s.loss_over_basis_prorata) |
| person.k1s_total_ord_div | — | — | — | — | — | — | 2 (k1s.passive_investor_portfolio, mk1.k1s.count_schedule_e_rows) |
| person.k1s_total_qual_div | — | — | — | — | — | — | 1 (k1s.passive_investor_portfolio) |
| person.k1s_total_st_gain | — | — | — | — | — | — | 4 |
| person.k1s_total_lt_gain | — | — | — | — | — | — | 3 |
| person.k1s_total_collectibles | — | — | — | — | — | — | 1 (mk1.k1s.box7_loss_box8_gain) |
| person.k1s_total_unrecap_1250 | — | — | — | — | — | — | 1 (k1s.passive_investor_portfolio) |
| person.k1s_total_backup_wh | — | — | — | — | — | — | 1 (k1s.withholding_taxexempt_st_loss) |
| person.k1s_total_taxexempt_int | — | — | — | — | — | — | 1 (k1s.withholding_taxexempt_st_loss) |
| person.k1s_total_passive_income | — | — | — | — | — | — | 4 |
| person.k1s_total_nonpassive_loss | — | — | — | — | — | — | 5 |
| person.k1s_total_nonpassive_income | — | — | — | — | — | — | 17 |
| person.k1s_total_nonpassive | — | — | — | — | — | — | 5 |
| person.k1s_total_p4_income | — | — | — | — | — | — | 2 (k1s.rental_not_active, mk1.k1s.rental_active_with_prior_and_box3) |
| person.k1s_total_p4_loss | — | — | — | — | — | — | 1 (k1s.loss_over_basis_prorata) |
| person.k1s_total_p4_prior | — | — | — | — | — | — | 1 (mk1.k1s.rental_active_with_prior_and_box3) |
| person.k1s_total_p5_income | — | — | — | — | — | — | 5 |
| person.k1s_total_p5_loss | — | — | — | — | — | — | 7 |
| person.k1s_total_p5_prior | — | — | — | — | — | — | 2 (k1s.passive_rental_prior_loss, mk1.k1s.material_with_box3_prior) |
| person.k1s_total_qbi | — | — | — | — | — | — | 3 |
| person.k1s_count_sche | — | — | — | — | — | — | 1 (mk1.k1s.count_schedule_e_rows) |

Unasserted lines: person.one, person.birth_cut_year, person.born_jan1_if_cut_year, person.age65, person.under16_open_year, person.under16_at_year_end_if_open_year, person.educator_expenses_if_educator, person.eic_under65, person.age65_box, person.not_died_before_65, person.work_ssn_or_tin, person.educator_max, person.has_educator_expenses, person.educator_limited, person.educator_eligible_amount, person.educator_deduction, person.hsa_forms, person.hsa_repeated, person.hsa_split, person.hsa_agreed, person.hsa_deduction, person.hsa_taxable, person.hsa_addtax, person.tip_employers, person.tip_total, person.tip_reported, person.ot_employers, person.ot_total, person.sc_rrta_count, person.se_rrta, person.box1, person.box2, person.f8919_firms, person.f8919_wages, person.f8919_any, person.f8919_line10_figured, person.f8919_line10, person.f8919_tax_figured, person.f8919_tax, person.f4137_rows_c, person.f4137_col_c, person.f4137_rows_d, person.f4137_col_d, person.f4137_under20_if_rows, person.tips_gov_if_rows, person.tips_noncash_if_unreported, person.f4137_line4, person.f4137_line6_figured, person.f4137_line6, person.f4137_line10_figured, person.f4137_line10, person.f4137_tax_figured, person.f4137_tax, person.line1c, person.household_wages_if_pay, person.strike_if_pay, person.mw_box1_if_mw, person.mw_not_box1_if_mw, person.mw_has_not_box1, person.mw_1099_if_not_box1, person.mw_has_1099, person.mw_1099_over, person.mw_business_if_1099, person.mw_total, person.mw_paid, person.mw_earned_if_paid, person.mw_other, person.mw_other_1d, person.line1d, person.line8s, person.mw_not_earned, person.earned_not_w2, person.ira_amount_a, person.ira_taxable, person.ira_rollovers, person.plan_amount_a, person.plan_taxable, person.dis_wages, person.line1h, person.plan_rollovers, person.sav_dist, person.zero, person.sc_count, person.ho_count, person.sc_credit_count, person.sc_fuel_count, person.mq_q4, person.mq_total, person.cost179, person.s179_nonlisted, person.s179_listed, person.income179, person.has_sc, person.sc_total, person.se_screened, person.plan_screened, person.cent, person.hundred, person.sep_rate_c, person.sep_rate_plus, person.comp_limit, person.sep_s8, person.simple_age_60_63_years, person.simple_age_50_59_years, person.simple_age_under50_years, person.simple_open_year, person.simple_age_if_open_year, person.simple_age_from_age50, person.catchup_under50, person.catchup_age50, person.catchup_age60_63, person.simple_cap, person.simple_regular, person.simple_catchup, person.catchup_limit, person.comp_after_regular, person.rate3, person.rate2, person.match_3pct, person.deferrals_total, person.ne_comp, person.employer_max, person.plan_deduction, person.s16, person.positive_profits, person.sehi, person.amt_dep_f17, person.amt_dep_y3, person.amt_dep_y5, person.amt_dep_y7, person.amt_dep_y10, person.amt_dep_listed, person.amt_dep, person.qbi, person.eic_part1, person.eic_se_has, person.sc_1a, person.dc_benefits, person.dc_box10, person.dc_1e_mine, person.dc_1e_counted, person.dc_zero, person.dc_1e, person.dc_earned, person.dc_earned_b, person.sav_trad_if_ira_owner, person.sav_roth_if_ira_owner, person.sav_w2, person.sav_excess, person.no, person.sav_has_w2, person.sav_excess_gate, person.sav_simple_plan, person.sav_simple, person.ira_contrib, person.ira_has, person.ira_excess, person.age50_open_year, person.age50_at_year_end_if_open_year, person.age55_open_year, person.ira_limit_under50, person.ira_limit_over50, person.ira_limit, person.ira_not_covered_joint, person.ira_line2_table, person.ira_line2_apart, person.ira_line2_status, person.ira_line2_nc, person.ira_line2, person.ira_line6_yes, person.ira_full_narrow, person.ira_full_joint, person.ira_full, person.ira_at_full, person.ira_p70, person.ira_p80, person.ira_p35, person.ira_p40, person.ira_prod_wide, person.ira_prod_joint, person.ira_min, person.ira_floor, person.ira_below, person.ira_line7_figured, person.ira_line7, person.ira_over_limit, person.ira_own_total, person.ira_7or10, person.ira_10or11, person.ira_nd_figured, person.ira_nondeductible, person.ira_basis_gate, person.ira_dist_if_files, person.ira_dist_gate, person.ira_8606_line14, person.ira_se_take, person.ira_se_figured, person.ira_se, person.edu_student_edu, person.edu_student_tin, person.edu_student_itin, person.edu_adj_sum, person.edu_adj, person.edu_has_adj, person.edu_over_if_adj, person.edu_no, person.edu_aoc23, person.edu_aoc24, person.edu_aoc25, person.edu_aoc26, person.edu_aoc_tin, person.edu_llc_tin_refused, person.edu_kid_age, person.edu_kid_18, person.edu_kid_18_support, person.edu_kid_student_age, person.edu_kid_support, person.edu_kid_fulltime, person.x_l2_all, person.x_l1_s, person.x_l2_s, person.x_e05, person.x_e09, person.x_e19, person.x_e22, person.x_e23, person.x_tax, person.x_must, person.x_cap09_base, person.x_cap09, person.x_cap19_one, person.x_cap19, person.x_cap22, person.x_cap23, person.x_has05, person.x_c05_min, person.x_has09, person.x_c09_min, person.x_c09, person.x_has19, person.x_c19_min, person.x_c19, person.x_c22, person.x_c23, person.x_n23, person.x_two23, person.x_capped_sum, person.x_limited_sum, person.x_other_exc, person.x_limit_binds, person.x_other, person.x_edu_taxable_if_account, person.x_edu_excess_if_account, person.x_ira_prior_excess_if_ira_owner, person.rmd_missed_if_possible, person.senior_work_ssn, person.spouse_senior_work_ssn

## Qualified business income and section 199A dividends — amounts and the choice of Form 8995

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| qbi.dividends | — | — | — | — | — | — | — |
| qbi.no | — | — | — | — | — | — | — |
| qbi.prior_form | — | — | — | — | — | — | — |
| qbi.reit_loss | — | — | — | — | — | — | — |
| qbi.reit_loss_if_prior_form | — | — | — | — | — | — | — |
| qbi.suspended | — | — | — | — | — | — | — |
| qbi.suspended_if_business | — | — | — | — | — | — | — |
| qbi.coop_patron | — | — | — | — | — | — | — |
| qbi.unsupported | — | — | — | — | — | — | — |
| qbi.zero | — | — | — | — | — | — | — |
| qbi.eligible | — | — | — | — | — | — | 2 (mutation.m4.qbi.reit_loss_carryforward, mutation.m4.qbi.suspended_losses) |
| qbi.carryforward | — | — | — | — | — | — | — |
| qbi.carryforward_if_prior_form | — | — | — | — | — | — | — |
| qbi.business_any | — | — | — | — | — | — | — |
| qbi.via_8995a | — | — | — | — | — | — | 1 (stage14.refuse.qbi_8995a) |
| qbi.deductions_before | — | — | — | — | — | — | — |
| qbi.taxable_before | — | — | — | — | — | E via f8995.line11 (OpenTaxSolver) | 2 (stage4.qbi.income_limit, stage4.qbi.zero_income) |
| qbi.net_capital_gain | — | — | — | — | — | — | — |
| qbi.threshold | — | — | — | — | — | — | — |
| qbi.use_8995a | — | — | — | — | — | — | 3 |
| qbi.deduction | — | — | — | via f1040.line13a: 6 | — | OpenTaxSolver: 387 compared (329 nonzero), 130 excluded; E via f1040.line13a (PE, OpenTaxSolver) | 19 |
| qbi.dividends_if_ordinary | — | — | — | — | — | E via f8995.line8 → f8995.line6 → qbi.eligible (OpenTaxSolver) | — |

Unasserted lines: qbi.no, qbi.reit_loss_if_prior_form, qbi.suspended_if_business, qbi.unsupported, qbi.zero, qbi.carryforward_if_prior_form, qbi.business_any, qbi.deductions_before, qbi.net_capital_gain, qbi.threshold

## Qualified Dividends and Capital Gain Tax Worksheet—Line 16

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| qdcg.schedule_d_filed | — | — | — | — | — | — | 12 |
| qdcg.schedule_d_net_gain | — | — | — | — | — | — | 1 (qdcg.sd.side) |
| qdcg.line1 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 58 |
| qdcg.line2 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (607 nonzero), 313 excluded; UsTaxes below rule: 519 compared (375 nonzero), 551 excluded | 58 |
| qdcg.line3 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (386 nonzero), 313 excluded; UsTaxes below rule: 519 compared (292 nonzero), 551 excluded | 15 |
| qdcg.line4 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes below rule: 519 compared (519 nonzero), 551 excluded | 12 |
| qdcg.line5 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 519 compared (455 nonzero), 551 excluded | 12 |
| qdcg.line6 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes below rule: 519 compared (519 nonzero), 551 excluded | 58 |
| qdcg.line7 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 58 |
| qdcg.line8 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 519 compared (455 nonzero), 551 excluded | 12 |
| qdcg.line9 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (378 nonzero), 313 excluded; UsTaxes below rule: 519 compared (206 nonzero), 551 excluded; E via qdcg.line11 (OpenTaxSolver) | 12 |
| qdcg.line10 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 12 |
| qdcg.line11 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (378 nonzero), 313 excluded; UsTaxes below rule: 519 compared (206 nonzero), 551 excluded | 12 |
| qdcg.line12 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 519 compared (281 nonzero), 551 excluded | 12 |
| qdcg.line13 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes below rule: 519 compared (519 nonzero), 551 excluded | 58 |
| qdcg.line14 | 1 (example.official) | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 58 |
| qdcg.line15 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 12 |
| qdcg.line16 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 519 compared (281 nonzero), 551 excluded | 12 |
| qdcg.line17 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 519 compared (281 nonzero), 551 excluded | 12 |
| qdcg.line18 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 519 compared (281 nonzero), 551 excluded | 12 |
| qdcg.line19 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 12 |
| qdcg.line20 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver below rule: 793 compared (0 nonzero), 313 excluded; UsTaxes below rule: 519 compared (0 nonzero), 551 excluded | 12 |
| qdcg.line21 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver below rule: 793 compared (0 nonzero), 313 excluded; UsTaxes below rule: 519 compared (0 nonzero), 551 excluded | 12 |
| qdcg.line22 | — | — | — | — | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 519 compared (455 nonzero), 551 excluded | 13 |
| qdcg.line23 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 519 compared (455 nonzero), 551 excluded | 13 |
| qdcg.line24 | 1 (example.official) | — | — | — | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 519 compared (470 nonzero), 551 excluded | 59 |
| qdcg.line25 | — | — | — | 2 (classm.qdcg.1, classm.qdcg.2) | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 519 compared (455 nonzero), 551 excluded | 13 |

## Pub. 525 Worksheets 2a and 2 — recoveries of 2024 itemized deductions (Schedule 1, lines 1 and 8z)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rec.zero | — | — | — | — | — | — | — |
| rec.no | — | — | — | — | — | — | — |
| rec.before_prior_year | — | — | — | — | — | — | — |
| rec.before_prior_year_if_any | — | — | — | — | — | — | — |
| rec.nonitemized | — | — | — | — | — | — | — |
| rec.nonitemized_if_any | — | — | — | — | — | — | — |
| rec.sales_tax | — | — | — | — | — | — | — |
| rec.sales_tax_if_any | — | — | — | — | — | — | — |
| rec.joint_any | — | — | — | — | — | — | — |
| rec.two_returns | — | — | — | — | — | — | — |
| rec.two_returns_if_joint | — | — | — | — | — | — | — |
| rec.path | — | — | — | — | — | — | — |
| rec.has_property_tax | — | — | — | — | — | — | — |
| rec.has_property_tax_if_path | — | — | — | — | — | — | — |
| rec.property_tax | — | — | — | — | — | — | — |
| rec.property_tax_if_has | — | — | — | — | — | — | — |
| rec.has_mortgage | — | — | — | — | — | — | — |
| rec.has_mortgage_if_path | — | — | — | — | — | — | — |
| rec.mortgage | — | — | — | — | — | — | — |
| rec.mortgage_if_has | — | — | — | — | — | — | — |
| rec.has_medical | — | — | — | — | — | — | — |
| rec.has_medical_if_path | — | — | — | — | — | — | — |
| rec.medical | — | — | — | — | — | — | — |
| rec.medical_deducted | — | — | — | — | — | — | — |
| rec.medical_if_has | — | — | — | — | — | — | — |
| rec.medical_deducted_if_has | — | — | — | — | — | — | — |
| rec.medical_counted | — | — | — | — | — | — | 1 (rec.medical_cap) |
| rec.has_other | — | — | — | — | — | — | — |
| rec.has_other_if_path | — | — | — | — | — | — | — |
| rec.other | — | — | — | — | — | — | — |
| rec.other_deducted | — | — | — | — | — | — | — |
| rec.other_if_has | — | — | — | — | — | — | — |
| rec.other_deducted_if_has | — | — | — | — | — | — | — |
| rec.other_counted | — | — | — | — | — | — | — |
| rec.w2a_line1 | — | — | — | 5 | — | — | — |
| rec.w2a_line2 | — | — | — | 5 | — | — | — |
| rec.w2a_line6 | — | — | — | 5 | — | — | — |
| rec.w2a_line3 | — | — | — | 5 | — | — | 2 (rec.salt_cap_absorbs, mrental.rec.w2a_refunds_over_5d) |
| rec.w2a_cap | — | — | — | — | — | — | — |
| rec.w2a_line4 | — | — | — | 5 | — | — | 3 |
| rec.w2a_line5_more | — | — | — | — | — | — | — |
| rec.w2a_line5 | — | — | — | 1 (classm.rec.3) | — | — | 2 (rec.salt_cap_partial, mrental.rec.w2a_refunds_over_5d) |
| rec.w2a_line7_share | — | — | — | — | — | — | — |
| rec.w2a_line7_capped | — | — | — | — | — | — | — |
| rec.w2a_line7 | — | — | — | 5 | — | — | 3 |
| rec.w2a_line8_share | — | — | — | — | — | — | — |
| rec.w2a_line8_capped | — | — | — | — | — | — | — |
| rec.w2a_line8 | — | — | — | 5 | — | — | 3 |
| rec.line1a | — | — | — | 5 | — | — | 2 (rec.ex31_allocation, mrental.rec.salt_limited_no_tax_refunds) |
| rec.line1b | — | — | — | 5 | — | — | 2 (rec.below_standard, mrental.rec.salt_limited_no_tax_refunds) |
| rec.line2 | — | — | — | 5 | — | — | 1 (rec.medical_cap) |
| rec.line3 | 2 (rec.ex30, rec.ex32) | — | — | 5 | — | — | 7 |
| rec.line4 | — | — | — | 5 | — | — | — |
| rec.line5 | — | — | — | 5 | — | — | — |
| rec.line6 | — | — | — | 5 | — | — | — |
| rec.line7_mfs | — | — | — | — | — | — | — |
| rec.prior_mfs | — | — | — | — | — | — | — |
| rec.line7 | — | — | — | 5 | — | — | 2 (mrental.rec.prior_mfs_spouse_standard, mrental.rec.prior_mfs_spouse_itemized) |
| rec.line8 | 2 (rec.ex30, rec.ex32) | — | — | 5 | — | — | 5 |
| rec.line9 | 1 (rec.ex32) | — | — | 4 | — | — | 3 |
| rec.ti_positive | — | — | — | — | — | — | — |
| rec.agi_prior | — | — | — | — | — | — | — |
| rec.ded_prior | — | — | — | — | — | — | — |
| rec.line10 | 1 (rec.ex33) | — | — | 4 | — | — | 1 (mrental.rec.negative_ti_line9_is_line3) |
| rec.negative_ti | — | — | — | — | — | — | — |
| rec.line11_negative | — | — | — | — | — | — | — |
| rec.nol_negative | — | — | — | — | — | — | — |
| rec.line11 | 3 | — | — | 4 | — | — | 17 |
| rec.line11_is_line3 | — | — | — | — | — | — | — |
| rec.line_b_share | — | — | — | — | — | — | — |
| rec.line_b | 2 (rec.ex30, rec.ex32) | — | — | 4 | — | — | 7 |
| rec.line_c | 2 (rec.ex30, rec.ex32) | — | — | 4 | — | — | 6 |
| rec.to_line1 | — | — | — | — | — | — | — |
| rec.to_line8z | — | — | — | — | — | — | 5 |

Unasserted lines: rec.zero, rec.no, rec.before_prior_year_if_any, rec.nonitemized_if_any, rec.sales_tax_if_any, rec.joint_any, rec.two_returns_if_joint, rec.path, rec.has_property_tax_if_path, rec.property_tax_if_has, rec.has_mortgage_if_path, rec.mortgage_if_has, rec.has_medical_if_path, rec.medical_if_has, rec.medical_deducted_if_has, rec.has_other_if_path, rec.other_if_has, rec.other_deducted_if_has, rec.other_counted, rec.w2a_cap, rec.w2a_line5_more, rec.w2a_line7_share, rec.w2a_line7_capped, rec.w2a_line8_share, rec.w2a_line8_capped, rec.line7_mfs, rec.prior_mfs, rec.negative_ti, rec.line11_negative, rec.nol_negative, rec.line11_is_line3, rec.line_b_share, rec.to_line1

## State and Local Income Tax Refund Worksheet—Schedule 1, Line 1

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refund.zero | — | — | — | — | — | — | — |
| refund.any | — | — | — | — | — | — | — |
| refund.received | — | — | — | — | — | — | — |
| refund.has | — | — | — | — | — | — | — |
| refund.box8 | — | — | — | — | — | — | — |
| refund.other_year | — | — | — | — | — | — | — |
| refund.paid_other_time | — | — | — | — | — | — | — |
| refund.not_prior_year | — | — | — | — | — | — | — |
| refund.no | — | — | — | — | — | — | — |
| refund.joint | — | — | — | — | — | — | — |
| refund.two_returns | — | — | — | — | — | — | — |
| refund.two_returns_if_joint | — | — | — | — | — | — | — |
| refund.two_itemized | — | — | — | — | — | — | — |
| refund.two_itemized_if_two | — | — | — | — | — | — | — |
| refund.itemized | — | — | — | — | — | — | — |
| refund.sales | — | — | — | — | — | — | — |
| refund.worksheet | — | — | — | — | — | — | 1 (mutation.m3.refund.sales_tax_2024) |
| refund.worksheet_one | — | — | — | — | — | — | — |
| refund.exc_tax | — | — | — | — | — | — | — |
| refund.exc_who | — | — | — | — | — | — | — |
| refund.line5d_prior_year | — | — | — | — | — | — | — |
| refund.line5e_prior_year | — | — | — | — | — | — | — |
| refund.received_if_worksheet | — | — | — | — | — | — | 1 (g1f4.refuse.refund.two_itemized) |
| refund.line5e_bad | — | — | — | — | — | — | — |
| refund.line1 | — | — | — | 7 | — | — | 12 |
| refund.line2_more | — | — | — | — | — | — | 2 (stage16.mut.refund_single_unasked, stage16.mut.refund_line3_stop) |
| refund.line2 | — | — | — | 1 (classm.refund.1) | — | — | 5 |
| refund.line3_more | — | — | — | — | — | — | 1 (stage16.mut.refund_line3_stop) |
| refund.line3 | — | — | — | 7 | — | — | 9 |
| refund.line17_prior_year | — | — | — | — | — | — | — |
| refund.line4 | — | — | — | 7 | — | — | 8 |
| refund.status | — | — | — | — | — | — | — |
| refund.mfs_spouse_itemized | — | — | — | — | — | — | — |
| refund.std_single | — | — | — | — | — | — | — |
| refund.std_joint | — | — | — | — | — | — | — |
| refund.std_hoh | — | — | — | — | — | — | — |
| refund.line5 | — | — | — | 7 | — | — | 10 |
| refund.box_married | — | — | — | — | — | — | — |
| refund.box_unmarried | — | — | — | — | — | — | — |
| refund.per_box | — | — | — | — | — | — | — |
| refund.you_born | — | — | — | — | — | — | — |
| refund.you_blind | — | — | — | — | — | — | — |
| refund.spouse_born | — | — | — | — | — | — | — |
| refund.spouse_blind | — | — | — | — | — | — | — |
| refund.spouse_boxes | — | — | — | — | — | — | — |
| refund.amt_you_born | — | — | — | — | — | — | — |
| refund.amt_you_blind | — | — | — | — | — | — | — |
| refund.amt_spouse_born | — | — | — | — | — | — | — |
| refund.amt_spouse_born_checked | — | — | — | — | — | — | — |
| refund.amt_spouse_blind | — | — | — | — | — | — | — |
| refund.amt_spouse_blind_checked | — | — | — | — | — | — | — |
| refund.line6 | — | — | — | 7 | — | — | 11 |
| refund.line7 | — | — | — | 7 | — | — | 11 |
| refund.line8_figured | — | — | — | — | — | — | — |
| refund.line8 | — | — | — | 4 | — | — | 10 |
| refund.line8_mfs | — | — | — | — | — | — | — |
| refund.line9_figured | — | — | — | — | — | — | — |
| refund.line9 | — | — | — | 4 | — | — | 11 |
| refund.taxable_1040 | — | — | — | — | — | — | — |
| refund.taxable | — | — | — | — | — | — | 6 |

Unasserted lines: refund.zero, refund.has, refund.not_prior_year, refund.no, refund.joint, refund.two_returns_if_joint, refund.two_itemized_if_two, refund.worksheet_one, refund.line5e_bad, refund.std_single, refund.std_joint, refund.std_hoh, refund.box_married, refund.box_unmarried, refund.per_box, refund.spouse_boxes, refund.amt_you_born, refund.amt_you_blind, refund.amt_spouse_born, refund.amt_spouse_born_checked, refund.amt_spouse_blind, refund.amt_spouse_blind_checked, refund.line8_figured, refund.line8_mfs, refund.line9_figured, refund.taxable_1040

## Schedule E, Part I — one rental real estate property

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rental.zero | — | — | — | — | — | — | — |
| rental.no | — | — | — | — | — | — | — |
| rental.one | — | — | — | — | — | — | — |
| rental.kind | — | — | — | — | — | — | — |
| rental.self_rental | — | — | — | — | — | — | — |
| rental.days_fair | — | — | — | — | — | — | — |
| rental.personal_any | — | — | — | — | — | — | — |
| rental.days_personal | — | — | — | — | — | — | — |
| rental.days_overlap | — | — | — | — | — | — | — |
| rental.day_cents | — | — | — | — | — | — | — |
| rental.tenth_cents | — | — | — | — | — | — | — |
| rental.fair_c | — | — | — | — | — | — | — |
| rental.personal_raw | — | — | — | — | — | — | — |
| rental.personal_c | — | — | — | — | — | — | — |
| rental.overlap_raw | — | — | — | — | — | — | — |
| rental.overlap_c | — | — | — | — | — | — | — |
| rental.use_c | — | — | — | — | — | — | — |
| rental.total_c | — | — | — | — | — | — | — |
| rental.home_rent_c | — | — | — | — | — | — | — |
| rental.home_pers10 | — | — | — | — | — | — | — |
| rental.home_pers10_if_any | — | — | — | — | — | — | — |
| rental.home | — | — | — | — | — | — | 3 |
| rental.excluded | — | — | — | — | — | — | 3 |
| rental.reported | — | — | — | — | — | — | — |
| rental.ws51 | — | — | — | — | — | — | — |
| rental.short_stays | — | — | — | — | — | — | — |
| rental.stay7 | — | — | — | — | — | — | — |
| rental.stay7_if_short | — | — | — | — | — | — | — |
| rental.services | — | — | — | — | — | — | — |
| rental.under_tenth | — | — | — | — | — | — | — |
| rental.not_for_profit | — | — | — | — | — | — | — |
| rental.depletion | — | — | — | — | — | — | — |
| rental.part_home | — | — | — | — | — | — | — |
| rental.vehicle | — | — | — | — | — | — | — |
| rental.active | — | — | — | — | — | — | — |
| rental.rents | — | — | — | — | — | — | — |
| rental.has_advertising | — | — | — | — | — | — | — |
| rental.amt5 | — | — | — | — | — | — | — |
| rental.amt5_if_any | — | — | — | — | — | — | — |
| rental.div5 | — | — | — | — | — | — | — |
| rental.line5 | — | — | — | 3 | — | — | 2 (mrental.rental.shared_costs_divided, mrental.rental.rental_only_costs_full) |
| rental.has_cleaning | — | — | — | — | — | — | — |
| rental.amt7 | — | — | — | — | — | — | — |
| rental.amt7_if_any | — | — | — | — | — | — | — |
| rental.div7 | — | — | — | — | — | — | — |
| rental.line7 | — | — | — | 3 | — | — | 2 (mrental.rental.shared_costs_divided, mrental.rental.rental_only_costs_full) |
| rental.has_commissions | — | — | — | — | — | — | — |
| rental.amt8 | — | — | — | — | — | — | — |
| rental.amt8_if_any | — | — | — | — | — | — | — |
| rental.div8 | — | — | — | — | — | — | — |
| rental.line8 | — | — | — | 3 | — | — | 2 (mrental.rental.shared_costs_divided, mrental.rental.rental_only_costs_full) |
| rental.has_insurance | — | — | — | — | — | — | — |
| rental.amt9 | — | — | — | — | — | — | — |
| rental.amt9_if_any | — | — | — | — | — | — | — |
| rental.div9 | — | — | — | — | — | — | — |
| rental.line9 | — | — | — | 3 | — | — | 2 (x1sche.f8.personal_use_not_home, mrental.rental.shared_costs_divided) |
| rental.has_legal | — | — | — | — | — | — | — |
| rental.amt10 | — | — | — | — | — | — | — |
| rental.amt10_if_any | — | — | — | — | — | — | — |
| rental.div10 | — | — | — | — | — | — | — |
| rental.line10 | — | — | — | 3 | — | — | 2 (mrental.rental.shared_costs_divided, mrental.rental.rental_only_costs_full) |
| rental.has_management | — | — | — | — | — | — | — |
| rental.amt11 | — | — | — | — | — | — | — |
| rental.amt11_if_any | — | — | — | — | — | — | — |
| rental.div11 | — | — | — | — | — | — | — |
| rental.line11 | — | — | — | 3 | — | — | 2 (mrental.rental.shared_costs_divided, mrental.rental.rental_only_costs_full) |
| rental.has_mortgage | — | — | — | — | — | — | — |
| rental.amt12 | — | — | — | — | — | — | — |
| rental.amt12_if_any | — | — | — | — | — | — | — |
| rental.div12 | — | — | — | — | — | — | — |
| rental.line12 | — | — | — | 3 | — | — | 2 (x1sche.f8.personal_use_not_home, mrental.rental.shared_costs_divided) |
| rental.has_other_interest | — | — | — | — | — | — | — |
| rental.amt13 | — | — | — | — | — | — | — |
| rental.amt13_if_any | — | — | — | — | — | — | — |
| rental.div13 | — | — | — | — | — | — | — |
| rental.line13 | — | — | — | 3 | — | — | 1 (mrental.rental.shared_costs_divided) |
| rental.has_repairs | — | — | — | — | — | — | — |
| rental.amt14 | — | — | — | — | — | — | — |
| rental.amt14_if_any | — | — | — | — | — | — | — |
| rental.div14 | — | — | — | — | — | — | — |
| rental.line14 | — | — | — | 3 | — | — | 1 (mrental.rental.shared_costs_divided) |
| rental.has_supplies | — | — | — | — | — | — | — |
| rental.amt15 | — | — | — | — | — | — | — |
| rental.amt15_if_any | — | — | — | — | — | — | — |
| rental.div15 | — | — | — | — | — | — | — |
| rental.line15 | — | — | — | 3 | — | — | 1 (mrental.rental.shared_costs_divided) |
| rental.has_taxes | — | — | — | — | — | — | — |
| rental.amt16 | — | — | — | — | — | — | — |
| rental.amt16_if_any | — | — | — | — | — | — | — |
| rental.div16 | — | — | — | — | — | — | — |
| rental.line16 | — | — | — | 3 | — | — | 3 |
| rental.has_utilities | — | — | — | — | — | — | — |
| rental.amt17 | — | — | — | — | — | — | — |
| rental.amt17_if_any | — | — | — | — | — | — | — |
| rental.div17 | — | — | — | — | — | — | — |
| rental.line17 | — | — | — | 3 | — | — | 2 (x1sche.f8.personal_use_not_home, mrental.rental.shared_costs_divided) |
| rental.has_other | — | — | — | — | — | — | — |
| rental.amt19 | — | — | — | — | — | — | — |
| rental.amt19_if_any | — | — | — | — | — | — | — |
| rental.div19 | — | — | — | — | — | — | — |
| rental.line19 | — | — | — | 3 | — | — | 1 (mrental.rental.shared_costs_divided) |
| rental.dep_full | — | — | — | — | — | — | — |
| rental.div18 | — | — | — | — | — | — | — |
| rental.line18 | — | — | — | 3 | — | — | 5 |
| rental.line20 | — | — | — | 3 | — | — | 4 |
| rental.line21_full | — | — | — | — | — | — | — |
| rental.line3 | — | — | — | 3 | — | — | 1 (mrental.rental.excluded_home_with_costs) |
| rental.line21 | — | — | — | 3 | — | — | 22 |
| rental.net_income | — | — | — | 3 | — | — | — |
| rental.net_loss | — | — | — | 3 | — | — | — |
| rental.prior_any | — | — | — | — | — | — | — |
| rental.prior_amt | — | — | — | — | — | — | — |
| rental.prior_amt_if_any | — | — | — | — | — | — | — |
| rental.prior_not_active | — | — | — | — | — | — | — |
| rental.prior_not_active_if_both | — | — | — | — | — | — | — |
| rental.prior_and_active | — | — | — | — | — | — | — |
| rental.prior_loss | — | — | — | 3 | — | — | 1 (mrental.rental.prior_loss_inactive_year) |
| rental.part4 | — | — | — | — | — | — | — |
| rental.loss_sum | — | — | — | — | — | — | — |
| rental.overall_loss | — | — | — | 3 | — | — | 2 (x1sche.f5.prior_loss_absorbed, mrental.rental.prior_loss_inactive_year) |
| rental.p6_loss | — | — | — | 3 | — | — | — |
| rental.p6c | — | — | — | 3 | — | — | 5 |
| rental.p6_on | — | — | — | — | — | — | — |
| rental.p6c_share | — | — | — | — | — | — | — |
| rental.p7a | — | — | — | 3 | — | — | 1 (x1sche.f3.pub925_phaseout) |
| rental.p7c | — | — | — | 3 | — | — | 6 |
| rental.p7_on | — | — | — | — | — | — | — |
| rental.p7c_share | — | — | — | — | — | — | — |
| rental.allowed | — | — | — | 3 | — | — | 3 |
| rental.carryforward | — | — | — | 3 | — | — | 6 |
| rental.not_at_risk | — | — | — | — | — | — | — |
| rental.not_at_risk_if_loss | — | — | — | — | — | — | 1 (mrental.rental.excluded_home_with_costs) |
| rental.has_loss | — | — | — | — | — | — | — |
| rental.line22 | — | — | — | 3 | — | — | 22 |
| rental.dep_prior | — | — | — | — | — | — | — |
| rental.dep_res25 | — | — | — | — | — | — | — |
| rental.dep_non25 | — | — | — | — | — | — | — |
| rental.count25 | — | — | — | — | — | — | — |
| rental.needs_4562 | — | — | — | — | — | — | 1 (mrental.rprop.form4562_needed) |

Unasserted lines: rental.zero, rental.no, rental.one, rental.self_rental, rental.day_cents, rental.tenth_cents, rental.fair_c, rental.personal_raw, rental.personal_c, rental.overlap_raw, rental.overlap_c, rental.use_c, rental.total_c, rental.home_rent_c, rental.home_pers10, rental.home_pers10_if_any, rental.reported, rental.ws51, rental.stay7_if_short, rental.amt5_if_any, rental.div5, rental.amt7_if_any, rental.div7, rental.amt8_if_any, rental.div8, rental.amt9_if_any, rental.div9, rental.amt10_if_any, rental.div10, rental.amt11_if_any, rental.div11, rental.amt12_if_any, rental.div12, rental.amt13_if_any, rental.div13, rental.amt14_if_any, rental.div14, rental.amt15_if_any, rental.div15, rental.amt16_if_any, rental.div16, rental.amt17_if_any, rental.div17, rental.amt19_if_any, rental.div19, rental.dep_full, rental.div18, rental.line21_full, rental.prior_amt_if_any, rental.prior_not_active_if_both, rental.prior_and_active, rental.part4, rental.loss_sum, rental.p6_on, rental.p6c_share, rental.p7_on, rental.p7c_share, rental.has_loss, rental.dep_prior, rental.dep_res25, rental.dep_non25, rental.count25

## Form 1099-R distributions (IRAs, pensions and annuities)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| retirement.account | — | — | — | — | — | — | — |
| retirement.code | — | — | — | — | — | — | — |
| retirement.box1 | — | — | — | via retirement.smw1: 5 | — | — | — |
| retirement.box5 | — | — | — | — | — | — | — |
| retirement.rollover | — | — | — | — | — | — | — |
| retirement.no | — | — | — | — | — | — | — |
| retirement.rollover_any | — | — | — | — | — | — | — |
| retirement.rolled_some | — | — | — | — | — | — | — |
| retirement.put_back | — | — | — | — | — | — | 2 (mutation.m1.retirement.direct_rollover_put_back, mutation.m1.retirement.partial_rollover_put_back) |
| retirement.rollover_if_any | — | — | — | — | — | — | — |
| retirement.is_trad | — | — | — | — | — | — | — |
| retirement.is_death | — | — | — | — | — | — | — |
| retirement.plan_death | — | — | — | — | — | — | 2 (mutation.m1.retirement.plan_death_code4, mutation.m1.retirement.roth_ira_code4) |
| retirement.roth_moved | — | — | — | — | — | — | — |
| retirement.roth_moved_if_put_back | — | — | — | — | — | — | — |
| retirement.rollover_property | — | — | — | — | — | — | — |
| retirement.rollover_property_if_put_back | — | — | — | — | — | — | — |
| retirement.rollover_qdro | — | — | — | — | — | — | — |
| retirement.rollover_qdro_if_put_back | — | — | — | — | — | — | — |
| retirement.levy_returned | — | — | — | — | — | — | — |
| retirement.levy_returned_if_put_back | — | — | — | — | — | — | — |
| retirement.charity_hsa | — | — | — | — | — | — | — |
| retirement.charity_hsa_if_ira | — | — | — | — | — | — | — |
| retirement.ira_returned | — | — | — | — | — | — | — |
| retirement.ira_returned_if_ira | — | — | — | — | — | — | — |
| retirement.ira_basis | — | — | — | — | — | — | — |
| retirement.ira_basis_if_trad | — | — | — | — | — | — | — |
| retirement.box6 | — | — | — | — | — | — | — |
| retirement.box6_if_plan | — | — | — | — | — | — | — |
| retirement.loan_offset | — | — | — | — | — | — | — |
| retirement.loan_offset_if_plan | — | — | — | — | — | — | — |
| retirement.disability | — | — | — | — | — | — | — |
| retirement.disability_if_plan | — | — | — | — | — | — | — |
| retirement.dis_early | — | — | — | — | — | — | — |
| retirement.dis_early_if_disability | — | — | — | — | — | — | — |
| retirement.dis_all_early | — | — | — | — | — | — | — |
| retirement.dis_all_early_if_early | — | — | — | — | — | — | — |
| retirement.dis_wages | — | — | — | — | — | — | — |
| retirement.dis_split | — | — | — | — | — | — | 1 (mexist.retirement.dis_split.after_min_age) |
| retirement.dis_terror | — | — | — | — | — | — | — |
| retirement.dis_terror_if_disability | — | — | — | — | — | — | — |
| retirement.dis_military | — | — | — | — | — | — | — |
| retirement.dis_military_if_disability | — | — | — | — | — | — | — |
| retirement.pso_exclusion | — | — | — | — | — | — | — |
| retirement.pso_exclusion_if_plan | — | — | — | — | — | — | — |
| retirement.born_before_averaging_date | — | — | — | — | — | — | — |
| retirement.born_before_averaging_date_if_plan | — | — | — | — | — | — | — |
| retirement.lump_sum | — | — | — | — | — | — | — |
| retirement.lump_sum_if_born_before_averaging_date | — | — | — | — | — | — | — |
| retirement.death_exclusion | — | — | — | — | — | — | — |
| retirement.death_exclusion_if_death | — | — | — | — | — | — | — |
| retirement.ben_before_retire | — | — | — | — | — | — | — |
| retirement.ben_before_retire_if_death | — | — | — | — | — | — | — |
| retirement.ben_guaranteed | — | — | — | — | — | — | — |
| retirement.ben_guaranteed_if_death | — | — | — | — | — | — | — |
| retirement.ben_shared | — | — | — | — | — | — | — |
| retirement.ben_shared_if_death | — | — | — | — | — | — | — |
| retirement.cost_any | — | — | — | — | — | — | — |
| retirement.cost_any_if_plan | — | — | — | — | — | — | — |
| retirement.own_annuity | — | — | — | — | — | — | — |
| retirement.own_annuity_if_cost | — | — | — | — | — | — | — |
| retirement.csrs_alt | — | — | — | — | — | — | — |
| retirement.csrs_alt_if_cost | — | — | — | — | — | — | — |
| retirement.started_before_simplified_method_date | — | — | — | — | — | — | — |
| retirement.started_before_simplified_method_date_if_cost | — | — | — | — | — | — | — |
| retirement.general_rule | — | — | — | — | — | — | — |
| retirement.general_rule_if_cost | — | — | — | — | — | — | — |
| retirement.lump_at_start | — | — | — | — | — | — | — |
| retirement.lump_at_start_if_cost | — | — | — | — | — | — | — |
| retirement.disaster | — | — | — | — | — | — | — |
| retirement.special | — | — | — | — | — | — | — |
| retirement.annuity | — | — | — | — | — | — | — |
| retirement.annuity_if_cost | — | — | — | — | — | — | — |
| retirement.cost | — | — | — | via retirement.smw2: 5 | — | — | — |
| retirement.used_last_year | — | — | — | — | — | — | — |
| retirement.last_line4 | — | — | — | — | — | — | — |
| retirement.joint_life | — | — | — | — | — | — | — |
| retirement.age | — | — | — | — | — | — | — |
| retirement.combined_age | — | — | — | — | — | — | — |
| retirement.months | — | — | — | — | — | — | — |
| retirement.recovered | — | — | — | via retirement.smw6: 5 | — | — | — |
| retirement.zero | — | — | — | — | — | — | — |
| retirement.one | — | — | — | — | — | — | — |
| retirement.is_ira | — | — | — | — | — | — | — |
| retirement.roth | — | — | — | — | — | — | — |
| retirement.direct | — | — | — | — | — | — | — |
| retirement.bad_code | — | — | — | — | — | — | — |
| retirement.rolled | — | — | — | — | — | — | — |
| retirement.has_rollover | — | — | — | — | — | — | — |
| retirement.smw_shown | — | — | — | — | — | — | 4 |
| retirement.smw1 | — | — | — | 10 | — | — | — |
| retirement.smw2 | — | — | — | 10 | — | — | — |
| retirement.smw4_t1_360 | — | — | — | — | — | — | — |
| retirement.smw4_t1_310 | — | — | — | — | — | — | — |
| retirement.smw4_t1_260 | — | — | — | — | — | — | — |
| retirement.smw4_t1_210 | — | — | — | — | — | — | — |
| retirement.smw4_t1_160 | — | — | — | — | — | — | — |
| retirement.smw4_t2_410 | — | — | — | — | — | — | — |
| retirement.smw4_t2_360 | — | — | — | — | — | — | — |
| retirement.smw4_t2_310 | — | — | — | — | — | — | — |
| retirement.smw4_t2_260 | — | — | — | — | — | — | — |
| retirement.smw4_t2_210 | — | — | — | — | — | — | — |
| retirement.smw4_table1 | — | — | — | — | — | — | — |
| retirement.smw4_table2 | — | — | — | — | — | — | — |
| retirement.smw4_new | — | — | — | — | — | — | — |
| retirement.smw4 | — | — | — | 10 | — | — | 5 |
| retirement.smw5 | — | — | — | 10 | — | — | 4 |
| retirement.smw6 | — | — | — | 10 | — | — | — |
| retirement.smw7 | — | — | — | 10 | — | — | — |
| retirement.smw8 | — | — | — | 10 | — | — | 1 (stage10.smw.cost_nearly_recovered) |
| retirement.smw9 | — | — | — | 10 | — | — | — |
| retirement.smw10 | — | — | — | 10 | — | — | 5 |
| retirement.smw11 | — | — | — | 10 | — | — | 5 |
| retirement.cost_left | — | — | — | — | — | — | — |
| retirement.annuity_with_cost | — | — | — | — | — | — | — |
| retirement.annuity_rollover | — | — | — | — | — | — | 1 (stage10.mut.annuity_rollover_cost_recovered) |
| retirement.annuity_taxable | — | — | — | — | — | — | — |
| retirement.ira_taxable | — | — | — | — | — | — | — |
| retirement.ira_not_rolled | — | — | — | — | — | — | — |
| retirement.plan_excluded | — | — | — | — | — | — | — |
| retirement.plan_simple | — | — | — | — | — | — | — |
| retirement.plan_taxable | — | — | — | — | — | — | — |
| retirement.taxable | — | — | — | — | — | — | — |
| retirement.show_a | — | — | — | — | — | — | 1 (mutation.t2.mfs_sdtw_skip41) |
| retirement.amount_a | — | — | — | — | — | — | 2 (mutation.m1.retirement.ira_box5, stage16.cleanup.refuse.retirement.special_first) |
| retirement.sav_military | — | — | — | — | — | — | — |
| retirement.sav_404k | — | — | — | — | — | — | — |
| retirement.sav_inherited | — | — | — | — | — | — | — |
| retirement.sav_excluded | — | — | — | — | — | — | — |
| retirement.sav_gross | — | — | — | — | — | — | — |
| retirement.sav_amount | — | — | — | — | — | — | — |
| retirement.early | — | — | — | — | — | — | — |
| retirement.early_screen | — | — | — | — | — | — | — |
| retirement.under59 | — | — | — | — | — | — | — |
| retirement.is_code7 | — | — | — | — | — | — | — |
| retirement.under59_if_code7 | — | — | — | — | — | — | — |
| retirement.sec457 | — | — | — | — | — | — | — |
| retirement.sec457_if_under59 | — | — | — | — | — | — | — |
| retirement.code7_wrong | — | — | — | — | — | — | 1 (mutation.m1.retirement.code7_under59) |
| retirement.code2_partial | — | — | — | — | — | — | — |
| retirement.is_code2 | — | — | — | — | — | — | — |
| retirement.code2_partial_if_code2 | — | — | — | — | — | — | — |
| retirement.not_beneficiary | — | — | — | — | — | — | — |
| retirement.not_beneficiary_if_death | — | — | — | — | — | — | — |
| retirement.code_screen | — | — | — | — | — | — | — |
| retirement.screen_refused | — | — | — | — | — | — | 2 (mutation.m1.retirement.code7_under59, mutation.m1.retirement.roth_code7_under59_line4a) |
| retirement.exception | — | — | — | — | — | — | — |
| retirement.has_exception | — | — | — | — | — | — | — |
| retirement.exc_amount | — | — | — | — | — | — | — |
| retirement.wrong_kind | — | — | — | — | — | — | — |
| retirement.l1 | — | — | — | — | — | — | — |
| retirement.exc_capped | — | — | — | — | — | — | — |
| retirement.l2 | — | — | — | — | — | — | — |
| retirement.is_e05 | — | — | — | — | — | — | — |
| retirement.l2_e05 | — | — | — | — | — | — | — |
| retirement.is_e09 | — | — | — | — | — | — | — |
| retirement.l2_e09 | — | — | — | — | — | — | — |
| retirement.is_e19 | — | — | — | — | — | — | — |
| retirement.l2_e19 | — | — | — | — | — | — | — |
| retirement.is_e22 | — | — | — | — | — | — | — |
| retirement.l2_e22 | — | — | — | — | — | — | — |
| retirement.is_e23 | — | — | — | — | — | — | — |
| retirement.l2_e23 | — | — | — | — | — | — | — |
| retirement.is_s | — | — | — | — | — | — | — |
| retirement.l1_s | — | — | — | — | — | — | — |
| retirement.l2_s | — | — | — | — | — | — | — |

Unasserted lines: retirement.no, retirement.rolled_some, retirement.rollover_if_any, retirement.is_trad, retirement.is_death, retirement.roth_moved_if_put_back, retirement.rollover_property_if_put_back, retirement.rollover_qdro_if_put_back, retirement.levy_returned_if_put_back, retirement.charity_hsa_if_ira, retirement.ira_returned_if_ira, retirement.ira_basis_if_trad, retirement.box6_if_plan, retirement.loan_offset_if_plan, retirement.disability_if_plan, retirement.dis_early_if_disability, retirement.dis_all_early_if_early, retirement.dis_wages, retirement.dis_terror_if_disability, retirement.dis_military_if_disability, retirement.pso_exclusion_if_plan, retirement.born_before_averaging_date_if_plan, retirement.lump_sum_if_born_before_averaging_date, retirement.death_exclusion_if_death, retirement.ben_before_retire_if_death, retirement.ben_guaranteed_if_death, retirement.ben_shared_if_death, retirement.cost_any_if_plan, retirement.own_annuity_if_cost, retirement.csrs_alt_if_cost, retirement.started_before_simplified_method_date_if_cost, retirement.general_rule_if_cost, retirement.lump_at_start_if_cost, retirement.special, retirement.annuity_if_cost, retirement.zero, retirement.one, retirement.is_ira, retirement.roth, retirement.direct, retirement.bad_code, retirement.rolled, retirement.has_rollover, retirement.smw4_t1_360, retirement.smw4_t1_310, retirement.smw4_t1_260, retirement.smw4_t1_210, retirement.smw4_t1_160, retirement.smw4_t2_410, retirement.smw4_t2_360, retirement.smw4_t2_310, retirement.smw4_t2_260, retirement.smw4_t2_210, retirement.smw4_table1, retirement.smw4_table2, retirement.smw4_new, retirement.cost_left, retirement.annuity_with_cost, retirement.annuity_taxable, retirement.ira_taxable, retirement.ira_not_rolled, retirement.plan_excluded, retirement.plan_simple, retirement.plan_taxable, retirement.taxable, retirement.sav_excluded, retirement.sav_gross, retirement.sav_amount, retirement.early, retirement.is_code7, retirement.under59_if_code7, retirement.sec457_if_under59, retirement.is_code2, retirement.code2_partial_if_code2, retirement.not_beneficiary_if_death, retirement.code_screen, retirement.has_exception, retirement.wrong_kind, retirement.l1, retirement.exc_capped, retirement.l2, retirement.is_e05, retirement.l2_e05, retirement.is_e09, retirement.l2_e09, retirement.is_e19, retirement.l2_e19, retirement.is_e22, retirement.l2_e22, retirement.is_e23, retirement.l2_e23, retirement.is_s, retirement.l1_s, retirement.l2_s

## Form 4562 — Depreciation and Amortization, one per rental property

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rf4562.needed | — | — | — | — | — | — | 1 (mrental.rprop.form4562_needed) |
| rf4562.line17 | — | — | — | 1 (classm.rf4562.1) | — | — | 1 (xfix.f21.placed_2025_form4562) |
| rf4562.line19i | — | — | — | 1 (classm.rf4562.1) | — | — | 1 (xfix.f21.placed_2025_form4562) |
| rf4562.line19j | — | — | — | 1 (classm.rf4562.1) | — | — | 1 (xfix.f21.placed_2025_form4562) |
| rf4562.line22 | — | — | — | 1 (classm.rf4562.1) | — | — | 1 (xfix.f21.placed_2025_form4562) |

## Schedule E, Part I — one royalty property

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| royalty.zero | — | — | — | — | — | — | — |
| royalty.one | — | — | — | — | — | — | — |
| royalty.line4 | — | — | — | — | — | — | — |
| royalty.business | — | — | — | — | — | — | — |
| royalty.depletion | — | — | — | — | — | — | — |
| royalty.expenses_any | — | — | — | — | — | — | — |
| royalty.amt10 | — | — | — | — | — | — | — |
| royalty.line10 | — | — | — | 1 (classm.royalty.1) | — | — | — |
| royalty.amt16 | — | — | — | — | — | — | — |
| royalty.line16 | — | — | — | 1 (classm.royalty.1) | — | — | — |
| royalty.amt19 | — | — | — | — | — | — | — |
| royalty.line19 | — | — | — | 1 (classm.royalty.1) | — | — | — |
| royalty.line20 | — | — | — | 1 (classm.royalty.1) | — | — | 1 (mrental.royalty.expenses_and_loss) |
| royalty.line21 | — | — | — | 1 (classm.royalty.1) | — | — | 3 |
| royalty.income | — | — | — | — | — | — | — |
| royalty.loss | — | — | — | — | — | — | — |
| royalty.loss_abs | — | — | — | — | — | — | — |

Unasserted lines: royalty.zero, royalty.one, royalty.income, royalty.loss, royalty.loss_abs

## Form 4562 — one building or improvement of a rental property

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rprop.zero | — | — | — | — | — | — | — |
| rprop.kind | — | — | — | — | — | — | — |
| rprop.month | — | — | — | — | — | — | — |
| rprop.year | — | — | — | — | — | — | — |
| rprop.basis | — | — | — | — | — | — | — |
| rprop.screen | — | — | — | — | — | — | — |
| rprop.personal | — | — | — | — | — | — | — |
| rprop.early_nonres | — | — | — | — | — | — | — |
| rprop.recovery_year | — | — | — | — | — | — | — |
| rprop.rate | — | — | — | — | — | — | — |
| rprop.dep | — | — | — | 1 (classm.rprop.1) | — | — | 5 |
| rprop.placed_this_year | — | — | — | — | — | — | — |
| rprop.cent | — | — | — | — | — | — | — |
| rprop.placed_this_year_cent | — | — | — | — | — | — | — |

Unasserted lines: rprop.zero, rprop.personal, rprop.early_nonres, rprop.recovery_year, rprop.rate, rprop.placed_this_year, rprop.cent, rprop.placed_this_year_cent

## Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s1.zero | — | — | — | — | — | — | — |
| s1.line1 | 2 (rec.ex30, rec.ex32) | — | — | 17 | — | — | 30 |
| s1.uc_any | — | — | — | — | — | — | — |
| s1.uc_paid | — | — | — | — | — | — | — |
| s1.uc_paid_if_any | — | — | — | — | — | — | — |
| s1.has_uc | — | — | — | — | — | — | — |
| s1.uc_repaid | — | — | — | — | — | — | — |
| s1.uc_unsupported | — | — | — | — | — | — | — |
| s1.line7_figured | — | — | — | — | — | — | — |
| s1.line7 | — | — | — | 17 | — | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_box | — | — | — | 17 | — | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_repaid | — | — | — | 8 | — | — | 1 (stage11.uc.repaid) |
| s1.ebl_loss | — | — | — | — | — | — | — |
| s1.ebl_total | — | — | — | — | — | — | — |
| s1.ebl_sc | — | — | — | — | — | — | — |
| s1.ebl_sche_abs | — | — | — | — | — | — | — |
| s1.ebl_sche | — | — | — | — | — | — | — |
| s1.zero_ebl | — | — | — | — | — | — | — |
| s1.ebl_threshold | — | — | — | — | — | — | — |
| s1.ebl | — | — | — | — | — | — | — |
| s1.sc_count | — | — | — | — | — | — | — |
| s1.has_sc | — | — | — | — | — | — | — |
| s1.sc_1a_count | — | — | — | — | — | — | — |
| s1.sc_1a | — | — | — | — | — | — | — |
| s1.line3 | — | — | — | 17 | — | — | 14 |
| s1.ltc_payout | — | — | — | — | — | — | — |
| s1.stock_options | — | — | — | — | — | — | — |
| s1.stock_options_if_options | — | — | — | — | — | — | — |
| s1.olympic | — | — | — | — | — | — | — |
| s1.olympic_if_winnings | — | — | — | — | — | — | — |
| s1.nqdc_pension | — | — | — | — | — | — | — |
| s1.nqdc_pension_if_w2 | — | — | — | — | — | — | — |
| s1.inmate_wages | — | — | — | — | — | — | — |
| s1.options_amount | — | — | — | — | — | — | — |
| s1.line8k | — | — | — | 17 | — | — | 2 (x2s1o.line8k, x2s1o.refuse.inmate_8u) |
| s1.f8853c_total | — | — | — | — | — | — | — |
| s1.line8e | — | — | — | 17 | — | — | 7 |
| s1.digital_income | — | — | — | — | — | — | — |
| s1.digital_income_if_assets | — | — | — | — | — | — | — |
| s1.digital_amount | — | — | — | — | — | — | — |
| s1.line8v | — | — | — | 17 | — | — | 4 |
| s1.line8_other | — | — | — | — | — | — | — |
| s1.winnings_any | — | — | — | — | — | — | — |
| s1.gambling_winnings | — | — | — | — | — | — | — |
| s1.gambling_winnings_if_winnings | — | — | — | — | — | — | — |
| s1.has_gambling | — | — | — | — | — | — | — |
| s1.gambling_pro | — | — | — | — | — | — | — |
| s1.no | — | — | — | — | — | — | — |
| s1.gambling_business | — | — | — | — | — | — | — |
| s1.line8b | — | — | — | 17 | — | — | 7 |
| s1.alaska_any | — | — | — | — | — | — | — |
| s1.alaska_dividend | — | — | — | — | — | — | — |
| s1.line8g | — | — | — | 17 | — | — | 1 (stage16.other.o4) |
| s1.jury_any | — | — | — | — | — | — | — |
| s1.jury_pay | — | — | — | — | — | — | — |
| s1.line8h | — | — | — | 17 | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.prizes | — | — | — | — | — | — | — |
| s1.line8i | — | — | — | 17 | — | — | 1 (stage16.other.o6) |
| s1.hobby_any | — | — | — | — | — | — | — |
| s1.hobby_income | — | — | — | — | — | — | — |
| s1.line8j | — | — | — | 17 | — | — | 1 (stage16.other.o7) |
| s1.scholarship_any | — | — | — | — | — | — | — |
| s1.scholarship_taxable | — | — | — | — | — | — | — |
| s1.line8r | 1 (stage19.example.bill.ex3) | — | — | 17 | — | — | 1 (stage16.other.o8) |
| s1.oi8z_total | — | — | — | — | — | — | — |
| s1.line8z | 3 | — | — | 17 | — | — | 24 |
| s1.alimony_any | — | — | — | — | — | — | — |
| s1.alimony | — | — | — | — | — | — | — |
| s1.alimony_if_any | — | — | — | — | — | — | — |
| s1.alimony_received | — | — | — | — | — | — | — |
| s1.alimony_paid | — | — | — | — | — | — | — |
| s1.alimony_unsupported | — | — | — | — | — | — | — |
| s1.alimony_refused | — | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_received) |
| s1.line2a | — | — | — | 17 | — | — | 5 |
| s1.line2b_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.cod_any | — | — | — | — | — | — | — |
| s1.cod_amount | — | — | — | — | — | — | — |
| s1.has_cod | — | — | — | — | — | — | — |
| s1.cod_unsupported | — | — | — | — | — | — | — |
| s1.cod_refused | — | — | — | — | — | — | 2 (stage20.refuse.excluded_canceled_debt, stage16.refuse.s1.cod_unsupported) |
| s1.cod_figured | — | — | — | — | — | — | — |
| s1.line8c | — | — | — | 17 | — | — | 6 |
| s1.line8f | — | — | — | 17 | — | — | 11 |
| s1.nol_amount | — | — | — | — | — | — | — |
| s1.nol_amount_if_nol | — | — | — | — | — | — | — |
| s1.nol_before_limit_date | — | — | — | — | — | — | — |
| s1.nol_before_limit_date_if_nol | — | — | — | — | — | — | — |
| s1.nol_ebl | — | — | — | — | — | — | — |
| s1.nol_ebl_if_nol | — | — | — | — | — | — | — |
| s1.nol_joint | — | — | — | — | — | — | — |
| s1.nol_separate | — | — | — | — | — | — | — |
| s1.nol_not_married | — | — | — | — | — | — | — |
| s1.nol_not_married_if_joint | — | — | — | — | — | — | — |
| s1.nol_was_joint | — | — | — | — | — | — | — |
| s1.nol_was_joint_if_separate | — | — | — | — | — | — | — |
| s1.nol_marital | — | — | — | — | — | — | — |
| s1.line8a | — | — | — | 17 | — | — | 7 |
| s1.nol_ti | — | — | — | — | — | — | — |
| s1.nol_ti4 | — | — | — | — | — | — | — |
| s1.nol_limit_test | — | — | — | — | — | — | — |
| s1.nol_limit | — | — | — | — | — | — | 1 (mint.s1.nol.limit_refused_positive_income) |
| s1.line8s | — | — | — | 17 | — | — | 6 |
| s1.line8s_neg | — | — | — | — | — | — | — |
| s1.line9 | — | — | — | 17 | — | OpenTaxSolver below rule: 1700 compared (0 nonzero), 0 excluded | 38 |
| s1.line5 | — | — | — | 17; via f8960.line4a: 3 | — | — | 5 |
| s1.line10_ex5 | — | — | — | — | — | — | — |
| s1.line10 | — | — | — | 17; via f1040.line8: 6 | — | OpenTaxSolver: 1700 compared (576 nonzero), 0 excluded; UsTaxes below rule: 1400 compared (280 nonzero), 300 excluded; E via f1040.line8 (OpenTaxSolver) | 45 |
| s1.line11 | — | — | — | 17 | — | UsTaxes: 1400 compared (146 nonzero), 300 excluded | 5 |
| s1.line13 | — | — | — | 17 | — | UsTaxes: 1331 compared (152 nonzero), 369 excluded | 41 |
| s1.line15 | — | — | — | 17; via s8812.line22: 1 (classm.s8812.3.deepseek); via s8812.clwb_8 → s8812.line22: 1 (classm.s8812.3.deepseek) | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 10 |
| s1.line16 | — | — | — | 17 | — | — | 11 |
| s1.line17 | — | — | — | 17 | — | — | 3 |
| s1.line18 | — | — | — | 17; via f8960.line10: 3 | — | — | 2 (stage16.small.s10, stage16.small.s1) |
| s1.paid_refused | — | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_paid) |
| s1.line19a | — | — | — | 17 | — | — | 4 |
| s1.line19b_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line19c_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line20 | — | — | — | 17 | — | PE: 1640 compared (504 nonzero), 19 excluded | 39 |
| s1.line20_box | — | — | — | 17 | — | — | 5 |
| s1.line21 | — | — | — | 17 | — | OpenTaxSolver: 1589 compared (127 nonzero), 111 excluded; UsTaxes: 1166 compared (94 nonzero), 534 excluded | 4 |
| s1.jury_to_employer | — | — | — | — | — | — | — |
| s1.has_jury_pay | — | — | — | — | — | — | — |
| s1.jury_to_employer_if_pay | — | — | — | — | — | — | — |
| s1.jury_over | — | — | — | — | — | — | — |
| s1.line24a | — | — | — | 17 | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line25 | — | — | — | 17 | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line26 | — | — | — | 17; via f1040.line10: 6 | — | OpenTaxSolver: 1589 compared (955 nonzero), 111 excluded; UsTaxes: 1166 compared (600 nonzero), 534 excluded; E via f1040.line10 (PE, TC, OpenTaxSolver, UsTaxes) | 19 |

Unasserted lines: s1.zero, s1.uc_paid_if_any, s1.has_uc, s1.line7_figured, s1.ebl_loss, s1.ebl_total, s1.ebl_sc, s1.ebl_sche_abs, s1.ebl_sche, s1.zero_ebl, s1.ebl_threshold, s1.ebl, s1.sc_count, s1.has_sc, s1.sc_1a_count, s1.sc_1a, s1.stock_options_if_options, s1.olympic_if_winnings, s1.nqdc_pension_if_w2, s1.f8853c_total, s1.digital_income_if_assets, s1.line8_other, s1.gambling_winnings_if_winnings, s1.has_gambling, s1.no, s1.gambling_business, s1.oi8z_total, s1.alimony_if_any, s1.has_cod, s1.cod_figured, s1.nol_amount_if_nol, s1.nol_before_limit_date_if_nol, s1.nol_ebl_if_nol, s1.nol_joint, s1.nol_separate, s1.nol_not_married_if_joint, s1.nol_was_joint_if_separate, s1.nol_marital, s1.nol_ti, s1.nol_ti4, s1.nol_limit_test, s1.line8s_neg, s1.line10_ex5, s1.has_jury_pay, s1.jury_to_employer_if_pay, s1.jury_over

## Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s179.line2 | — | — | — | 4 | — | — | 7 |
| s179.max | — | — | — | — | — | — | — |
| s179.line1 | — | — | — | 1 (classm.s179.2) | — | — | 2 (stage14.s179.carryover_no_property, stage14.s179.dollar_limit) |
| s179.line3 | — | — | — | 4 | — | — | — |
| s179.line4 | — | — | — | 4 | — | — | 4 |
| s179.line5_full | — | — | — | — | — | — | — |
| s179.separate | — | — | — | — | — | — | — |
| s179.line5_mfs | — | — | — | — | — | — | — |
| s179.line5 | — | — | — | 1 (classm.s179.2) | — | — | 10 |
| s179.mfs | — | — | — | — | — | — | 1 (stage14.s179.mfs_no_election) |
| s179.line6 | — | — | — | 1 (classm.s179.3) | — | — | — |
| s179.line7 | — | — | — | 1 (classm.s179.3) | — | — | — |
| s179.line8 | — | — | — | 1 (classm.s179.3) | — | — | — |
| s179.over_limit | — | — | — | — | — | — | — |
| s179.line9 | — | — | — | 1 (classm.s179.3) | — | — | 4 |
| s179.show10 | 1 (stage4.official.medicare_example5) | — | — | — | — | — | 1 (stage14.s179.zero_limit_carryover) |
| s179.prior_form | — | — | — | — | — | — | — |
| s179.prior_form_if_before | — | — | — | — | — | — | — |
| s179.carryover | — | — | — | — | — | — | — |
| s179.carryover_if_prior_form | — | — | — | — | — | — | — |
| s179.line10 | — | — | — | 1 (classm.s179.3) | — | — | — |
| s179.income_sc | — | — | — | — | — | — | — |
| s179.income_wages | — | — | — | — | — | — | — |
| s179.zero | — | — | — | — | — | — | — |
| s179.no | — | — | — | — | — | — | — |
| s179.has179 | — | — | — | — | — | — | — |
| s179.income_below5 | — | — | — | — | — | — | — |
| s179.income_binds | — | — | — | — | — | — | — |
| s179.has_interest | — | — | — | — | — | — | — |
| s179.wc_ask | — | — | — | — | — | — | 4 |
| s179.wc_interest | — | — | — | — | — | — | — |
| s179.wc_interest_if_limited | — | — | — | — | — | — | — |
| s179.wc_more | — | — | — | — | — | — | — |
| s179.wc_over | — | — | — | — | — | — | — |
| s179.income | — | — | — | — | — | — | 5 |
| s179.income0 | — | — | — | — | — | — | — |
| s179.line11 | — | — | — | 1 (classm.s179.3) | — | — | 13 |
| s179.line9_10 | — | — | — | — | — | — | — |
| s179.line12 | — | — | — | 4 | — | — | 18 |
| s179.sc_count | — | — | — | — | — | — | — |
| s179.orphan | — | — | — | — | — | — | 1 (stage21.t068.no_business_no_carryover) |
| s179.line13 | — | — | — | 4 | — | — | 16 |
| s179.differs | — | — | — | — | — | — | 1 (mutation.t2.f8962_months_asset3) |
| s179.multi | — | — | — | — | — | — | — |

Unasserted lines: s179.max, s179.line5_full, s179.separate, s179.line5_mfs, s179.over_limit, s179.prior_form_if_before, s179.carryover_if_prior_form, s179.income_sc, s179.income_wages, s179.zero, s179.no, s179.has179, s179.income_below5, s179.income_binds, s179.has_interest, s179.wc_interest_if_limited, s179.wc_more, s179.wc_over, s179.income0, s179.line9_10, s179.sc_count, s179.multi

## Schedule 1-A (Form 1040) — Additional Deductions

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s1a.zero | — | — | — | — | — | — | — |
| s1a.line1 | — | — | — | 9 | — | — | — |
| s1a.line2a | — | — | — | 6 | — | — | — |
| s1a.line2b | — | — | — | 6 | — | — | — |
| s1a.line2c | — | — | — | 6 | — | — | — |
| s1a.line2d | — | — | — | 6 | — | — | — |
| s1a.line2e | — | — | — | 6 | — | — | — |
| s1a.line3 | — | — | — | 9 | — | UsTaxes: 1166 compared (1166 nonzero), 534 excluded | 1 (stage12.tips.one_employer) |
| s1a.tips | — | — | — | — | — | — | — |
| s1a.tip_employers | — | — | — | — | — | — | — |
| s1a.tip_total | — | — | — | — | — | — | — |
| s1a.tip_reported | — | — | — | — | — | — | — |
| s1a.tip_multi | — | — | — | — | — | — | — |
| s1a.tip_ssn_count | — | — | — | — | — | — | — |
| s1a.tip_ssn | — | — | — | — | — | — | 1 (mutation.t3.mfj_no_tips_ssn_unanswered) |
| s1a.part2 | — | — | — | — | — | — | 2 (t264.s1a.mfs_parts_2_3, t264.s1a.mfs_spouse_entry) |
| s1a.line4a_calc | — | — | — | — | — | — | — |
| s1a.line4a | — | — | — | 4 | — | — | 7 |
| s1a.f4137_total | — | — | — | — | — | — | — |
| s1a.f4137 | — | — | — | — | — | — | — |
| s1a.line4b_calc | — | — | — | — | — | — | — |
| s1a.line4b | — | — | — | 4 | — | — | 3 |
| s1a.line4c_one | — | — | — | — | — | — | — |
| s1a.line4c_calc | — | — | — | — | — | — | — |
| s1a.line4c | — | — | — | 4 | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 9 |
| s1a.line5_calc | — | — | — | — | — | — | 2 (stage14.refuse.sch1a_tips, stage14.sch1a.tips_with_sc) |
| s1a.line5 | — | — | — | 3 | — | — | — |
| s1a.line6_calc | — | — | — | — | — | — | — |
| s1a.line6 | — | — | — | 4 | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 2 (stage12.tips.cap, stage12.refuse.tips_trade_or_business) |
| s1a.line7_calc | — | — | — | — | — | — | — |
| s1a.line7 | — | — | — | 4 | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 4 |
| s1a.tips_max | — | — | — | — | — | — | — |
| s1a.base_other | — | — | — | — | — | — | — |
| s1a.base_joint | — | — | — | — | — | — | — |
| s1a.line8_calc | — | — | — | — | — | — | — |
| s1a.line8 | — | — | — | 4 | — | UsTaxes: 138 compared (138 nonzero), 21 excluded | 1 (stage13.tips_only_spouse_no_ssn) |
| s1a.line9_calc | — | — | — | — | — | — | — |
| s1a.line9 | — | — | — | 4 | — | — | 4 |
| s1a.line10_calc | — | — | — | — | — | — | — |
| s1a.line10 | — | — | — | 4 | — | — | 3 |
| s1a.line10_over | — | — | — | — | — | — | — |
| s1a.line10_pos | — | — | — | — | — | — | — |
| s1a.line11_thousands | — | — | — | — | — | — | — |
| s1a.line12_calc | — | — | — | — | — | — | — |
| s1a.line12 | — | — | — | 1 (classm.s1a.5) | — | UsTaxes below rule: 138 compared (20 nonzero), 21 excluded | 5 |
| s1a.line13_figured | — | — | — | — | — | — | — |
| s1a.line13_amount | — | — | — | — | — | — | — |
| s1a.line13_ssn | — | — | — | — | — | — | — |
| s1a.line13_claim | — | — | — | — | — | — | — |
| s1a.line13 | — | — | — | 5 | — | PE: 1554 compared (163 nonzero), 143 excluded; TC: 1370 compared (168 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (190 nonzero), 111 excluded; UsTaxes: 1166 compared (135 nonzero), 534 excluded | 23 |
| s1a.overtime | — | — | — | — | — | — | — |
| s1a.ot_ssn_count | — | — | — | — | — | — | — |
| s1a.ot_ssn | — | — | — | — | — | — | — |
| s1a.part3 | — | — | — | — | — | — | 1 (t264.s1a.mfs_parts_2_3) |
| s1a.line14a_calc | — | — | — | — | — | — | — |
| s1a.line14a | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | — | 12 |
| s1a.line14b_calc | — | — | — | — | — | — | 1 (stage14.sch1a.refuse_overtime_1099) |
| s1a.line14b | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | — | — |
| s1a.line14c_calc | — | — | — | — | — | — | — |
| s1a.line14c | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | UsTaxes: 1400 compared (160 nonzero), 300 excluded | 2 (stage12.ot.premium, stage12.refuse.overtime_nonemployee) |
| s1a.ot_max_other | — | — | — | — | — | — | — |
| s1a.ot_max_joint | — | — | — | — | — | — | — |
| s1a.ot_max | — | — | — | — | — | — | — |
| s1a.line15_calc | — | — | — | — | — | — | — |
| s1a.line15 | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | UsTaxes: 1400 compared (160 nonzero), 300 excluded | 7 |
| s1a.line16_calc | — | — | — | — | — | — | — |
| s1a.line16 | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | UsTaxes: 126 compared (126 nonzero), 34 excluded | 2 (mutation.t2.mfj_no_overtime_part3, stage13.overtime_only_spouse_no_ssn) |
| s1a.line17_calc | — | — | — | — | — | — | — |
| s1a.line17 | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | — | 3 |
| s1a.line18_calc | — | — | — | — | — | — | — |
| s1a.line18 | — | — | — | 2 (classm.s1a.3, classm.s1a.5) | — | — | 1 (stage12.ot.phaseout) |
| s1a.line18_over | — | — | — | — | — | — | — |
| s1a.line18_pos | — | — | — | — | — | — | — |
| s1a.line19_thousands | — | — | — | — | — | — | — |
| s1a.line20_calc | — | — | — | — | — | — | — |
| s1a.line20 | — | — | — | 1 (classm.s1a.5) | — | UsTaxes below rule: 126 compared (26 nonzero), 34 excluded | 2 (stage12.ot.phaseout, stage12.mfj.tips_overtime) |
| s1a.line21_figured | — | — | — | — | — | — | — |
| s1a.line21_amount | — | — | — | — | — | — | — |
| s1a.line21_ssn | — | — | — | — | — | — | — |
| s1a.line21_claim | — | — | — | — | — | — | — |
| s1a.line21 | — | — | — | 3 | — | PE: 1553 compared (146 nonzero), 143 excluded; TC: 1370 compared (139 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (164 nonzero), 111 excluded; UsTaxes: 1166 compared (116 nonzero), 534 excluded | 20 |
| s1a.carloan | — | — | — | — | — | — | — |
| s1a.line23_total | — | — | — | — | — | — | — |
| s1a.line23 | — | — | — | 4 | — | UsTaxes below rule: 1266 compared (0 nonzero), 434 excluded | 7 |
| s1a.car_max | — | — | — | — | — | — | — |
| s1a.part4 | — | — | — | — | — | — | — |
| s1a.line24_calc | — | — | — | — | — | — | — |
| s1a.line24 | — | — | — | 4 | — | UsTaxes below rule: 1266 compared (0 nonzero), 434 excluded | 3 |
| s1a.car_base_other | — | — | — | — | — | — | — |
| s1a.car_base_joint | — | — | — | — | — | — | — |
| s1a.line25_calc | — | — | — | — | — | — | — |
| s1a.line25 | — | — | — | 4 | — | UsTaxes: 116 compared (116 nonzero), 18 excluded | 1 (mutation.t2.no_carloan_part4_b) |
| s1a.line26_calc | — | — | — | — | — | — | — |
| s1a.line26 | — | — | — | 4 | — | — | 5 |
| s1a.line27_calc | — | — | — | — | — | — | — |
| s1a.line27 | — | — | — | 4 | — | — | 2 (stage12.car.phaseout, stage12.car.phaseout_round_up) |
| s1a.line27_over | — | — | — | — | — | — | — |
| s1a.line27_pos | — | — | — | — | — | — | — |
| s1a.line28_thousands | — | — | — | — | — | — | — |
| s1a.line29_calc | — | — | — | — | — | — | — |
| s1a.line29 | — | — | — | 2 (classm.s1a.2, classm.s1a.3) | — | UsTaxes below rule: 116 compared (38 nonzero), 18 excluded | 4 |
| s1a.line30_figured | — | — | — | — | — | — | — |
| s1a.line30_amount | — | — | — | — | — | — | — |
| s1a.line30 | — | — | — | 4 | — | PE: 1552 compared (99 nonzero), 143 excluded; TC: 1370 compared (98 nonzero), 330 excluded; OpenTaxSolver below rule: 1437 compared (0 nonzero), 263 excluded; UsTaxes below rule: 1050 compared (0 nonzero), 650 excluded | 16 |
| s1a.senior_count | — | — | — | — | — | — | 1 (t264.person.senior_counts_under_65) |
| s1a.senior_any | — | — | — | — | — | — | — |
| s1a.part5 | — | — | — | — | — | — | — |
| s1a.line31_calc | — | — | — | — | — | — | — |
| s1a.line31 | — | — | — | 3 | — | UsTaxes: 187 compared (187 nonzero), 49 excluded | 2 (mutation.t2.no_senior_part5, stage13.seniors_none) |
| s1a.senior_base_other | — | — | — | — | — | — | — |
| s1a.senior_base_joint | — | — | — | — | — | — | — |
| s1a.line32_calc | — | — | — | — | — | — | — |
| s1a.line32 | — | — | — | 3 | — | — | 4 |
| s1a.line33_calc | — | — | — | — | — | — | — |
| s1a.line33 | — | — | — | 3 | — | — | 3 |
| s1a.line33_over | — | — | — | — | — | — | — |
| s1a.line33_pos | — | — | — | — | — | — | — |
| s1a.line34_calc | — | — | — | — | — | — | — |
| s1a.line34 | — | — | — | 2 (classm.s1a.3, classm.s1a.9) | — | UsTaxes: 187 compared (93 nonzero), 49 excluded | 4 |
| s1a.senior_amount | — | — | — | — | — | — | — |
| s1a.line35_figured | — | — | — | — | — | — | — |
| s1a.line35_calc | — | — | — | — | — | — | — |
| s1a.line35 | — | — | — | 3 | — | UsTaxes: 187 compared (155 nonzero), 49 excluded | 10 |
| s1a.died_before_65_count | — | — | — | — | — | — | — |
| s1a.died_before_65 | — | — | — | — | — | — | — |
| s1a.senior_decedent | — | — | — | — | — | — | — |
| s1a.line36a_senior | — | — | — | — | — | — | 1 (mutation.t2.mfj_sdtw_skip23) |
| s1a.line36a_claim | — | — | — | — | — | — | — |
| s1a.line36a | — | — | — | 3 | — | UsTaxes: 1166 compared (139 nonzero), 534 excluded | 16 |
| s1a.spouse_senior_count | — | — | — | — | — | — | 1 (t264.person.senior_counts_under_65) |
| s1a.spouse_senior | — | — | — | — | — | — | — |
| s1a.spouse_died_before_65_count | — | — | — | — | — | — | — |
| s1a.spouse_died_before_65 | — | — | — | — | — | — | — |
| s1a.spouse_senior_decedent | — | — | — | — | — | — | — |
| s1a.line36b_senior | — | — | — | — | — | — | — |
| s1a.line36b | — | — | — | 2 (classm.s1a.3, classm.s1a.7) | — | UsTaxes below rule: 1166 compared (19 nonzero), 534 excluded | 8 |
| s1a.line37 | — | — | — | 4 | — | PE: 1668 compared (218 nonzero), 19 excluded; TC: 1370 compared (187 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (212 nonzero), 111 excluded; UsTaxes: 1166 compared (155 nonzero), 534 excluded | 16 |
| s1a.line38 | — | — | — | 9; via f1040.line13b: 6 | — | OpenTaxSolver: 1437 compared (447 nonzero), 263 excluded; UsTaxes: 1076 compared (324 nonzero), 624 excluded; E via f1040.line13b (PE, TC, OpenTaxSolver) | 7 |
| s1a.no | — | — | — | — | — | — | — |
| s1a.part2_ssn | — | — | — | — | — | — | — |
| s1a.part3_ssn | — | — | — | — | — | — | — |

Unasserted lines: s1a.zero, s1a.tip_employers, s1a.tip_total, s1a.tip_reported, s1a.tip_multi, s1a.tip_ssn_count, s1a.line4a_calc, s1a.f4137_total, s1a.f4137, s1a.line4b_calc, s1a.line4c_one, s1a.line4c_calc, s1a.line6_calc, s1a.line7_calc, s1a.tips_max, s1a.base_other, s1a.base_joint, s1a.line8_calc, s1a.line9_calc, s1a.line10_calc, s1a.line10_over, s1a.line10_pos, s1a.line11_thousands, s1a.line12_calc, s1a.line13_figured, s1a.line13_amount, s1a.line13_ssn, s1a.line13_claim, s1a.ot_ssn_count, s1a.ot_ssn, s1a.line14a_calc, s1a.line14c_calc, s1a.ot_max_other, s1a.ot_max_joint, s1a.ot_max, s1a.line15_calc, s1a.line16_calc, s1a.line17_calc, s1a.line18_calc, s1a.line18_over, s1a.line18_pos, s1a.line19_thousands, s1a.line20_calc, s1a.line21_figured, s1a.line21_amount, s1a.line21_ssn, s1a.line21_claim, s1a.line23_total, s1a.car_max, s1a.part4, s1a.line24_calc, s1a.car_base_other, s1a.car_base_joint, s1a.line25_calc, s1a.line26_calc, s1a.line27_calc, s1a.line27_over, s1a.line27_pos, s1a.line28_thousands, s1a.line29_calc, s1a.line30_figured, s1a.line30_amount, s1a.senior_any, s1a.part5, s1a.line31_calc, s1a.senior_base_other, s1a.senior_base_joint, s1a.line32_calc, s1a.line33_calc, s1a.line33_over, s1a.line33_pos, s1a.line34_calc, s1a.senior_amount, s1a.line35_figured, s1a.line35_calc, s1a.died_before_65_count, s1a.died_before_65, s1a.senior_decedent, s1a.line36a_claim, s1a.spouse_senior, s1a.spouse_died_before_65_count, s1a.spouse_died_before_65, s1a.spouse_senior_decedent, s1a.line36b_senior, s1a.no, s1a.part2_ssn, s1a.part3_ssn

## Schedule 2 — Additional Taxes (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s2.no | — | — | — | — | — | — | — |
| s2.options_any | — | — | — | — | — | — | — |
| s2.iso | — | — | — | — | — | — | — |
| s2.iso_if_options | — | — | — | — | — | — | — |
| s2.iso_vested | — | — | — | — | — | — | — |
| s2.amt_mfs_max | — | — | — | — | — | — | — |
| s2.amt_exemption | — | — | — | — | — | — | — |
| s2.amt_l19 | — | — | — | — | — | — | — |
| s2.amt_l25 | — | — | — | — | — | — | — |
| s2.amt_l1a | — | — | — | — | — | — | — |
| s2.amt_l1b | — | — | — | — | — | — | 1 (s2.reg.amt_wages_none) |
| s2.amt_l2a | — | — | — | — | — | — | 1 (s2.reg.amt_wages_none) |
| s2.amt_dep | — | — | — | — | — | — | 2 (s2.mut.amt_depreciation_bound, s2.mut.amt_related_without_depreciation) |
| s2.amt_dep_any | — | — | — | — | — | — | 2 (s2.mut.amt_depreciation_bound, s2.mut.amt_related_without_depreciation) |
| s2.amt_rel_items | — | — | — | — | — | — | 2 (s2.mut.amt_depreciation_bound, s2.mut.amt_related_without_depreciation) |
| s2.amt_rel | — | — | — | — | — | — | 2 (s2.mut.amt_depreciation_bound, s2.mut.amt_related_without_depreciation) |
| s2.amt_l4_known | — | — | — | — | — | — | — |
| s2.amt_l4_sum | — | — | — | — | — | — | — |
| s2.amt_pab | — | — | — | — | — | — | — |
| s2.amt_pab_ask | — | — | — | — | — | — | — |
| s2.amt_pab_if_could | — | — | — | — | — | — | — |
| s2.amt_pab_over | — | — | — | — | — | — | 1 (s2.mut.amt_pab_over_tax_exempt) |
| s2.amt_l4 | — | — | — | — | — | — | 9 |
| s2.amt_mfs | — | — | — | — | — | — | — |
| s2.amt_mfs_over | — | — | — | — | — | — | 1 (s2.mut.amt_mfs_addback) |
| s2.amt_mfs_quarter | — | — | — | — | — | — | 1 (s2.mut.amt_mfs_addback) |
| s2.amt_mfs_add | — | — | — | — | — | — | 2 (s2.mut.amt_mfs_addback, s2.mut.amt_mfs_addback_max) |
| s2.amt_l4_mfs | — | — | — | — | — | — | — |
| s2.amt_l4m | — | — | — | — | — | — | 2 (s2.mut.amt_mfs_addback, s2.mut.amt_mfs_addback_max) |
| s2.amt_ex_over | — | — | — | — | — | — | — |
| s2.amt_ex_cut | — | — | — | — | — | — | — |
| s2.amt_l5 | — | — | — | — | — | — | 3 |
| s2.amt_l6 | — | — | — | — | — | — | 12 |
| s2.amt_l6_high | — | — | — | — | — | — | 2 (s2.mut.amt_line6_at_bracket, s2.mut.amt_line6_over_bracket) |
| s2.amt_l39_low | — | — | — | — | — | — | — |
| s2.amt_l39_product | — | — | — | — | — | — | — |
| s2.amt_l39_high | — | — | — | — | — | — | — |
| s2.amt_l39 | — | — | — | — | — | — | 9 |
| s2.amt_l13 | — | — | — | — | — | — | 5 |
| s2.amt_l14 | — | — | — | — | — | — | 4 |
| s2.amt_l13_14 | — | — | — | — | — | — | — |
| s2.amt_l15_sdtw | — | — | — | — | — | — | — |
| s2.amt_l15 | — | — | — | — | — | — | 3 |
| s2.amt_l16 | — | — | — | — | — | — | 1 (s2.mut.amt_line15_sdtw_line10) |
| s2.amt_l17 | — | — | — | — | — | — | 6 |
| s2.amt_l17_high | — | — | — | — | — | — | 1 (s2.mut.amt_line17_at_bracket) |
| s2.amt_l18_low | — | — | — | — | — | — | — |
| s2.amt_l18_product | — | — | — | — | — | — | — |
| s2.amt_l18_high | — | — | — | — | — | — | — |
| s2.amt_l18 | — | — | — | — | — | — | 3 |
| s2.amt_l20 | — | — | — | — | — | — | — |
| s2.amt_l21 | — | — | — | — | — | — | 1 (s2.reg.amt_dividends_owes) |
| s2.amt_l22 | — | — | — | — | — | — | — |
| s2.amt_l23 | — | — | — | — | — | — | 1 (s2.reg.amt_dividends_part3_none) |
| s2.amt_l24 | — | — | — | — | — | — | — |
| s2.amt_l27 | — | — | — | — | — | — | — |
| s2.amt_l28 | — | — | — | — | — | — | 1 (s2.mut.amt_sdtw_phaseout) |
| s2.amt_l29 | — | — | — | — | — | — | 1 (s2.mut.amt_sdtw_phaseout) |
| s2.amt_l30 | — | — | — | — | — | — | 3 |
| s2.amt_l31 | — | — | — | — | — | — | 1 (s2.reg.amt_dividends_owes) |
| s2.amt_l32 | — | — | — | — | — | — | — |
| s2.amt_l33 | — | — | — | — | — | — | 2 (s2.reg.amt_dividends_owes, s2.mut.amt_sdtw_phaseout) |
| s2.amt_l34 | — | — | — | — | — | — | 1 (s2.reg.amt_dividends_owes) |
| s2.amt_l35 | — | — | — | — | — | — | 1 (s2.mut.amt_sdtw_phaseout) |
| s2.amt_l36 | — | — | — | — | — | — | 3 |
| s2.amt_l14_any | — | — | — | — | — | — | 2 (s2.mut.amt_line17_at_bracket, s2.mut.amt_pab_over_tax_exempt) |
| s2.amt_l37_rate | — | — | — | — | — | — | — |
| s2.amt_l37 | — | — | — | — | — | — | 4 |
| s2.amt_l38 | — | — | — | — | — | — | 5 |
| s2.amt_l40 | — | — | — | — | — | — | 1 (s2.mut.amt_line40_rounding) |
| s2.amt_l7 | — | — | — | — | — | — | 9 |
| s2.amt_l10 | — | — | — | — | — | — | 3 |
| s2.amt_tmt_over | — | — | — | — | — | — | 5 |
| s2.amt_mortgage | — | — | — | — | — | — | 1 (s2.mut.amt_boat_mortgage) |
| s2.amt_h_extra | — | — | — | — | — | — | — |
| s2.amt_h4 | — | — | — | — | — | — | 3 |
| s2.amt_h_mfs_over | — | — | — | — | — | — | — |
| s2.amt_h_mfs_quarter | — | — | — | — | — | — | — |
| s2.amt_h_mfs_add | — | — | — | — | — | — | 2 (s2.mut.amt_mfs_addback, s2.mut.amt_mfs_addback_max) |
| s2.amt_h4_mfs | — | — | — | — | — | — | — |
| s2.amt_h4m | — | — | — | — | — | — | 2 (s2.mut.amt_mfs_addback, s2.mut.amt_mfs_addback_max) |
| s2.amt_h_ex_over | — | — | — | — | — | — | — |
| s2.amt_h_ex_cut | — | — | — | — | — | — | — |
| s2.amt_h5 | — | — | — | — | — | — | 1 (s2.mut.amt_sdtw_phaseout) |
| s2.amt_h6 | — | — | — | — | — | — | 3 |
| s2.amt_h6_high | — | — | — | — | — | — | 1 (s2.mut.amt_line6_at_bracket) |
| s2.amt_h39_low | — | — | — | — | — | — | — |
| s2.amt_h39_product | — | — | — | — | — | — | — |
| s2.amt_h39_high | — | — | — | — | — | — | — |
| s2.amt_h39 | — | — | — | — | — | — | 2 (s2.mut.amt_sdtw_phaseout, s2.mut.amt_boat_mortgage) |
| s2.amt_could | — | — | — | — | — | — | 5 |
| s2.amt_boat | — | — | — | — | — | — | — |
| s2.amt_boat_ask | — | — | — | — | — | — | 1 (s2.mut.amt_boat_mortgage) |
| s2.amt_boat_if_could | — | — | — | — | — | — | — |
| s2.amt_business | — | — | — | — | — | — | — |
| s2.amt_business_if_sc | — | — | — | — | — | — | — |
| s2.amt_owed | — | — | — | — | — | — | 1 (s2.mut.amt_boat_mortgage) |
| s2.amt | — | — | — | — | — | — | 4 |
| s2.w2_marks | — | — | — | — | — | — | — |
| s2.w2_marks_if_w2 | — | — | — | — | — | — | — |
| s2.household_help | — | — | — | — | — | — | — |
| s2.household_employee | — | — | — | — | — | — | — |
| s2.household_employee_if_help | — | — | — | — | — | — | — |
| s2.mortgage_subsidy | — | — | — | — | — | — | — |
| s2.mortgage_subsidy_if_interest | — | — | — | — | — | — | — |
| s2.hsa_testing | — | — | — | — | — | — | — |
| s2.credit_recapture | — | — | — | — | — | — | — |
| s2.lookback | — | — | — | — | — | — | — |
| s2.lookback_if_business | — | — | — | — | — | — | — |
| s2.other_tax | — | — | — | — | — | — | — |
| s2.other | — | — | — | — | — | — | — |
| s2.zero | — | — | — | via s2.line2: 3 | — | — | — |
| s2.line1a | — | — | — | 11; via s2.line1z: 3 | — | — | 9 |
| s2.line1z | — | — | — | 11 | — | — | — |
| s2.line2 | — | — | — | 11 | — | — | 12 |
| s2.line3 | — | — | — | 11; via f1040.line17: 6 | — | — | 5 |
| s2.line4 | — | — | — | 11 | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 4 |
| s2.line5 | — | — | — | 8 | — | — | 2 (x2pay.f4137.w1, x2pay.f4137.noncash_only) |
| s2.line6 | — | — | — | 8 | — | — | 3 |
| s2.line7 | — | — | — | 8 | — | — | 3 |
| s2.line8_must | — | — | — | — | — | — | — |
| s2.line8_file | — | — | — | — | — | — | — |
| s2.e05_total | — | — | — | — | — | — | 1 (mutation.m1.person.no_e05_schedule_a_refused) |
| s2.e05_over | — | — | — | — | — | — | — |
| s2.line8 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 11 | — | UsTaxes below rule: 1094 compared (28 nonzero), 606 excluded | 22 |
| s2.line8_box | — | — | — | 11 | — | — | 10 |
| s2.line11 | — | — | — | 11 | — | — | 2 (stage4.additional_taxes.combined, stage16.small.s10) |
| s2.line12 | — | — | — | 11 | — | — | 2 (stage4.additional_taxes.combined, stage16.small.s10) |
| s2.line17c | — | — | — | 11; via s2.line18: 3 | — | — | 8 |
| s2.line18 | — | — | — | 11 | — | — | 5 |
| s2.line21 | — | — | — | 11; via f1040.line23: 6 | — | OpenTaxSolver: 1264 compared (319 nonzero), 436 excluded; UsTaxes below rule: 935 compared (122 nonzero), 765 excluded; E via f1040.line23 (OpenTaxSolver) | 12 |

Unasserted lines: s2.no, s2.iso_if_options, s2.amt_mfs_max, s2.amt_exemption, s2.amt_l19, s2.amt_l25, s2.amt_l1a, s2.amt_l4_known, s2.amt_l4_sum, s2.amt_pab_ask, s2.amt_pab_if_could, s2.amt_mfs, s2.amt_l4_mfs, s2.amt_ex_over, s2.amt_ex_cut, s2.amt_l39_low, s2.amt_l39_product, s2.amt_l39_high, s2.amt_l13_14, s2.amt_l15_sdtw, s2.amt_l18_low, s2.amt_l18_product, s2.amt_l18_high, s2.amt_l20, s2.amt_l22, s2.amt_l24, s2.amt_l27, s2.amt_l32, s2.amt_l37_rate, s2.amt_h_extra, s2.amt_h_mfs_over, s2.amt_h_mfs_quarter, s2.amt_h4_mfs, s2.amt_h_ex_over, s2.amt_h_ex_cut, s2.amt_h39_low, s2.amt_h39_product, s2.amt_h39_high, s2.amt_boat_if_could, s2.amt_business_if_sc, s2.w2_marks_if_w2, s2.household_employee_if_help, s2.mortgage_subsidy_if_interest, s2.lookback_if_business, s2.other, s2.line8_must, s2.line8_file, s2.e05_over

## Schedule 3 — selected lines

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | 18 | — | — | 8 |
| s3.line2 | — | — | — | 18 | — | PE: 1287 compared (170 nonzero), 404 excluded; TC: 859 compared (123 nonzero), 840 excluded; OpenTaxSolver: 993 compared (130 nonzero), 707 excluded | 38 |
| s3.zero | — | — | — | — | — | — | — |
| s3.line3 | — | — | — | 18 | — | PE: 1273 compared (83 nonzero), 418 excluded; TC: 855 compared (65 nonzero), 840 excluded; UsTaxes below rule: 96 compared (45 nonzero), 116 excluded | 14 |
| s3.line4 | — | — | — | 18 | — | — | 36 |
| s3.line5a | — | — | — | 18; via s8812.clwb_15: 1 (classm.s8812.3.deepseek) | — | PE: 1278 compared (96 nonzero), 418 excluded | 42 |
| s3.line5b | — | — | — | 18 | — | PE: 1252 compared (91 nonzero), 445 excluded | 33 |
| s3.no | — | — | — | — | — | — | — |
| s3.adoption_any | — | — | — | — | — | — | — |
| s3.adoption | — | — | — | — | — | — | — |
| s3.adoption_asked_if_any | — | — | — | — | — | — | — |
| s3.adoption_final | — | — | — | — | — | — | — |
| s3.adoption_final_if_adoption | — | — | — | — | — | — | — |
| s3.adoption_stepchild | — | — | — | — | — | — | — |
| s3.adoption_stepchild_if_final | — | — | — | — | — | — | — |
| s3.adoption_if_any | — | — | — | — | — | — | 3 |
| s3.adoption_earlier | — | — | — | — | — | — | — |
| s3.adoption_earlier_if_any | — | — | — | — | — | — | 3 |
| s3.adoption_us | — | — | — | — | — | — | — |
| s3.adoption_us_if_earlier | — | — | — | — | — | — | 3 |
| s3.credit_bond | — | — | — | — | — | — | — |
| s3.seniors | — | — | — | — | — | — | 2 (redesign.credits.refuse.elderly_65, redesign.credits.elderly_not_asked) |
| s3.under65s | — | — | — | — | — | — | 2 (redesign.credits.refuse.elderly_65, redesign.credits.elderly_not_asked) |
| s3.any_senior | — | — | — | — | — | — | 1 (redesign.credits.refuse.elderly_disability) |
| s3.any_under65 | — | — | — | — | — | — | 2 (redesign.credits.refuse.elderly_disability, redesign.credits.elderly_65_no) |
| s3.disability_retired | — | — | — | — | — | — | — |
| s3.disability_if_under65 | — | — | — | — | — | — | 2 (redesign.credits.refuse.elderly_disability, redesign.credits.elderly_65_no) |
| s3.elderly_ask | — | — | — | — | — | — | 5 |
| s3.elderly_credit | — | — | — | — | — | — | — |
| s3.elderly_credit_if_asked | — | — | — | — | — | — | 3 |
| s3.ev | — | — | — | — | — | — | — |
| s3.ev_dealer | — | — | — | — | — | — | — |
| s3.ev_dealer_if_ev | — | — | — | — | — | — | 2 (redesign.credits.refuse.ev_credit, redesign.credits.ev_not_asked) |
| s3.ev_bought | — | — | — | — | — | — | — |
| s3.ev_bought_if_ev | — | — | — | — | — | — | 4 |
| s3.ev_credit | — | — | — | — | — | — | — |
| s3.ev_credit_if_bought | — | — | — | — | — | — | 3 |
| s3.ev_equipment | — | — | — | — | — | — | — |
| s3.ev_equipment_if_ev | — | — | — | — | — | — | 2 (redesign.credits.ev_leased, redesign.credits.ev_not_asked) |
| s3.farmland | — | — | — | — | — | — | — |
| s3.farmland_deferral | — | — | — | — | — | — | — |
| s3.farmland_deferral_if_sold | — | — | — | — | — | — | 1 (redesign.credits.farmland_not_asked) |
| s3.foreign_any | — | — | — | — | — | — | — |
| s3.section965 | — | — | — | — | — | — | — |
| s3.section965_if_foreign | — | — | — | — | — | — | 1 (redesign.credits.foreign_not_asked) |
| s3.section960c | — | — | — | — | — | — | — |
| s3.section960c_if_foreign | — | — | — | — | — | — | 1 (redesign.credits.foreign_not_asked) |
| s3.virgin_islands | — | — | — | — | — | — | — |
| s3.virgin_islands_if_foreign | — | — | — | — | — | — | 1 (redesign.credits.foreign_not_asked) |
| s3.kerosene | — | — | — | — | — | — | — |
| s3.kerosene_credit | — | — | — | — | — | — | — |
| s3.kerosene_credit_if_kerosene | — | — | — | — | — | — | 1 (redesign.credits.kerosene_not_asked) |
| s3.has_mortgage_interest | — | — | — | — | — | — | 3 |
| s3.mcc | — | — | — | — | — | — | — |
| s3.mcc_if_interest | — | — | — | — | — | — | 2 (redesign.credits.mcc_no_certificate, redesign.credits.mcc_not_asked) |
| s3.prior_other_forms | — | — | — | — | — | — | — |
| s3.prior_amt | — | — | — | — | — | — | — |
| s3.prior_amt_if_other_forms | — | — | — | — | — | — | — |
| s3.prior_amt_deferral | — | — | — | — | — | — | — |
| s3.prior_amt_deferral_if_amt | — | — | — | — | — | — | — |
| s3.prior_amt_if_forms | — | — | — | — | — | — | 3 |
| s3.prior_forms | — | — | — | — | — | — | — |
| s3.prior_forms_if_forms | — | — | — | — | — | — | 2 (redesign.credits.prior_other_forms_none, redesign.credits.prior_not_asked) |
| s3.repaid_income | — | — | — | — | — | — | — |
| s3.other_credit | — | — | — | — | — | — | 39 |
| s3.other_credit_2 | — | — | — | — | — | — | — |
| s3.other_credit_3 | — | — | — | — | — | — | — |
| s3.other_credit_4 | — | — | — | — | — | — | — |
| s3.other_credit_5 | — | — | — | — | — | — | — |
| s3.other_credit_6 | — | — | — | — | — | — | — |
| s3.other_credit_7 | — | — | — | — | — | — | — |
| s3.other_credit_8 | — | — | — | — | — | — | — |
| s3.other_credit_10 | — | — | — | — | — | — | — |
| s3.other_credit_11 | — | — | — | — | — | — | — |
| s3.other_credit_12 | — | — | — | — | — | — | — |
| s3.other_credit_13 | — | — | — | — | — | — | — |
| s3.other_credit_14 | — | — | — | — | — | — | — |
| s3.other_credit_15 | — | — | — | — | — | — | — |
| s3.other_credit_16 | — | — | — | — | — | — | — |
| s3.business_credit_count | — | — | — | — | — | — | — |
| s3.business_credit_any | — | — | — | — | — | — | — |
| s3.business_fuel_count | — | — | — | — | — | — | — |
| s3.business_fuel_any | — | — | — | — | — | — | — |
| s3.line7 | — | — | — | 15 | — | — | 33 |
| s3.line8 | — | — | — | 18; via f1040.line20: 6 | — | OpenTaxSolver below rule: 632 compared (210 nonzero), 1068 excluded; UsTaxes below rule: 378 compared (91 nonzero), 1322 excluded; E via f1040.line20 (TC) | 26 |
| s3.line9 | — | — | — | 18 | — | UsTaxes below rule: 36 compared (6 nonzero), 73 excluded | 29 |
| s3.line10 | — | — | — | — | — | — | — |
| s3.line11 | — | — | — | 18 | — | UsTaxes: 1400 compared (141 nonzero), 300 excluded | 26 |
| s3.line12 | — | — | — | 15 | — | — | 9 |
| s3.line14 | — | — | — | 15 | — | — | 13 |
| s3.line15 | — | — | — | 18; via f1040.line31: 6 | — | UsTaxes: 1288 compared (134 nonzero), 412 excluded | 32 |

Unasserted lines: s3.zero, s3.no, s3.adoption_asked_if_any, s3.adoption_final_if_adoption, s3.adoption_stepchild_if_final, s3.prior_amt_if_other_forms, s3.prior_amt_deferral_if_amt, s3.other_credit_2, s3.other_credit_3, s3.other_credit_4, s3.other_credit_5, s3.other_credit_6, s3.other_credit_7, s3.other_credit_8, s3.other_credit_10, s3.other_credit_11, s3.other_credit_12, s3.other_credit_13, s3.other_credit_14, s3.other_credit_15, s3.other_credit_16, s3.business_credit_count, s3.business_credit_any, s3.business_fuel_count, s3.business_fuel_any

## Schedule 8812 — Credits for Qualifying Children and Other Dependents

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s8812.line1 | — | — | — | 8 | — | — | 28 |
| s8812.zero | — | — | — | via s8812.line2a: 3; via s8812.line2b: 3; via s8812.line2c: 3; via s8812.line18b → s8812.eiw_1b: 2 (classm.s8812.1.deepseek, classm.s8812.3.deepseek) | — | — | — |
| s8812.line2a | — | — | — | 7 | — | — | 24 |
| s8812.line2b | — | — | — | 7 | — | — | 24 |
| s8812.line2c | — | — | — | 7 | — | — | 24 |
| s8812.line2d | — | — | — | 8 | — | — | 24 |
| s8812.line3 | — | — | — | 8 | — | UsTaxes: 616 compared (616 nonzero), 171 excluded | 28 |
| s8812.line4 | — | — | — | 8 | — | — | 33 |
| s8812.line5 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (775 nonzero), 81 excluded; UsTaxes: 737 compared (639 nonzero), 50 excluded | 31 |
| s8812.line6 | — | — | — | 8 | — | — | 25 |
| s8812.line7 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (317 nonzero), 81 excluded; UsTaxes: 737 compared (255 nonzero), 50 excluded | 27 |
| s8812.line8 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (889 nonzero), 81 excluded; UsTaxes: 737 compared (737 nonzero), 50 excluded | 31 |
| s8812.line9 | — | — | — | 8 | — | — | 2 (stage15.f5695-3.g2, stage16.other.o10) |
| s8812.excess | — | — | — | — | — | — | 24 |
| s8812.line10 | — | — | — | 8 | — | OpenTaxSolver: 829 compared (82 nonzero), 141 excluded; UsTaxes: 616 compared (56 nonzero), 171 excluded | 28 |
| s8812.line11 | — | — | — | 8 | — | OpenTaxSolver: 829 compared (82 nonzero), 141 excluded; UsTaxes: 616 compared (56 nonzero), 171 excluded | 28 |
| s8812.line12 | — | — | — | 6; via s8812.clwb_1: 1 (classm.s8812.3.deepseek) | — | PE: 1511 compared (814 nonzero), 150 excluded; OpenTaxSolver: 829 compared (792 nonzero), 141 excluded; UsTaxes: 616 compared (594 nonzero), 171 excluded | 32 |
| s8812.clw_a1 | — | — | — | 4 | — | — | 30 |
| s8812.clw_a2 | — | — | — | 4 | — | — | 30 |
| s8812.clw_a3 | — | — | — | 4 | — | — | 30 |
| s8812.clw_a4 | — | — | — | 4 | — | — | 30 |
| s8812.clw_a5 | — | — | — | 4; via s8812.line13: 2 (classm.s8812.1.deepseek, classm.s8812.3.deepseek) | — | — | 30 |
| s8812.show13 | — | — | — | — | — | — | 1 (stage8.single.taxpayer_without_tin) |
| s8812.line13 | — | — | — | 4 | — | — | 31 |
| s8812.line14 | — | — | — | 4; via f1040.line19: 6 | — | OpenTaxSolver below rule: 359 compared (297 nonzero), 611 excluded; UsTaxes below rule: 183 compared (152 nonzero), 604 excluded; E via f1040.line19 (PE) | 53 |
| s8812.line16a | — | — | — | 4 | — | OpenTaxSolver below rule: 359 compared (130 nonzero), 611 excluded; UsTaxes below rule: 183 compared (44 nonzero), 604 excluded | 28 |
| s8812.show16b | — | — | — | — | — | — | 1 (stage8.hoh.child.ctc) |
| s8812.line16b | — | — | — | 4; via s8812.clwb_2: 1 (classm.s8812.3.deepseek) | — | OpenTaxSolver: 275 compared (275 nonzero), 32 excluded; UsTaxes: 737 compared (639 nonzero), 50 excluded | 28 |
| s8812.show_iia | 1 (stage19.example.pell.ex2.no_tax) | — | — | — | — | — | 2 (stage8.hoh.child.ctc, stage8.hoh.actc.one_child.low_wages) |
| s8812.line17 | — | — | — | 4 | — | OpenTaxSolver below rule: 359 compared (113 nonzero), 611 excluded; UsTaxes below rule: 183 compared (37 nonzero), 604 excluded | 29 |
| s8812.combat_pay | — | — | — | — | — | — | — |
| s8812.puerto_rico | — | — | — | — | — | — | — |
| s8812.no | — | — | — | — | — | — | — |
| s8812.has_qualifying_child | — | — | — | — | — | — | — |
| s8812.puerto_rico_if_child | — | — | — | — | — | — | — |
| s8812.eiw_1a | — | — | — | — | — | — | 24 |
| s8812.eiw_1b | — | — | — | — | — | — | 24 |
| s8812.eiw_2b | — | — | — | — | — | — | — |
| s8812.eiw_3sum | — | — | — | — | — | — | 2 (stage14.s8812.eiw_stop_with_se_tax, stage14.s8812.eiw_zero_with_se_tax) |
| s8812.eiw_3 | — | — | — | — | — | — | 24 |
| s8812.eiw_4 | — | — | — | — | — | — | 26 |
| s8812.eiw_5 | — | — | — | — | — | — | 24 |
| s8812.eiw_6 | — | — | — | — | — | — | 24 |
| s8812.eiw_7_figured | — | — | — | — | — | — | — |
| s8812.eiw_3_positive | — | — | — | — | — | — | 1 (stage10.ss.refuse.schedule1) |
| s8812.eiw_7 | — | — | — | via s8812.clwb_3: 1 (classm.s8812.3.deepseek) | — | — | 26 |
| s8812.taking_eic | — | — | — | — | — | — | 4 |
| s8812.chart_eic | — | — | — | — | — | — | — |
| s8812.line18a | — | — | — | 4 | — | UsTaxes: 712 compared (712 nonzero), 50 excluded | 32 |
| s8812.line18b | — | — | — | 4 | — | — | 24 |
| s8812.line19 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | OpenTaxSolver: 266 compared (266 nonzero), 39 excluded; UsTaxes: 712 compared (712 nonzero), 50 excluded | 31 |
| s8812.line20 | — | — | — | 4 | — | OpenTaxSolver: 268 compared (266 nonzero), 39 excluded; UsTaxes: 712 compared (712 nonzero), 50 excluded | 30 |
| s8812.ss_withheld | — | — | — | — | — | — | 24 |
| s8812.amt_ws4 | — | — | — | — | — | — | 24 |
| s8812.amt_ws6 | — | — | — | — | — | — | — |
| s8812.amt_ws7 | — | — | — | — | — | — | 1 (stage14.f8959.se_above_threshold) |
| s8812.show_iib | — | — | — | — | — | — | 4 |
| s8812.line21 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3); via s8812.clwb_7: 1 (classm.s8812.3.deepseek) | — | UsTaxes: 610 compared (610 nonzero), 177 excluded | 26 |
| s8812.line22 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 26 |
| s8812.line23 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | UsTaxes: 610 compared (610 nonzero), 177 excluded | 26 |
| s8812.line24 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | UsTaxes below rule: 431 compared (64 nonzero), 356 excluded | 25 |
| s8812.line25 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | UsTaxes: 333 compared (333 nonzero), 454 excluded | 26 |
| s8812.line26 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | UsTaxes below rule: 333 compared (333 nonzero), 454 excluded | 25 |
| s8812.few_children | — | — | — | — | — | — | 24 |
| s8812.earned_covers | — | — | — | — | — | — | 24 |
| s8812.from_part_iia | — | — | — | — | — | — | 24 |
| s8812.from_part_iia_figured | — | — | — | — | — | — | — |
| s8812.from_part_iib | — | — | — | — | — | — | 25 |
| s8812.part_iib_result | — | — | — | — | — | — | 24 |
| s8812.part_iib_figured | — | — | — | — | — | — | — |
| s8812.line27 | — | — | — | 4; via f1040.line28: 6 | — | OpenTaxSolver below rule: 233 compared (38 nonzero), 737 excluded; UsTaxes below rule: 102 compared (8 nonzero), 685 excluded; E via f1040.line28 (PE) | 58 |
| s8812.clwb_complete | — | — | — | — | — | — | — |
| s8812.show_clwb | 2 (stage19.example.jack_kay, stage4.refuse.gift.sectionB) | — | — | — | — | — | 1 (stage21.t067.s8812_clwb_line6_blank) |
| s8812.clwb_1 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_2 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_3 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_4 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_5 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_three | — | — | — | — | — | — | — |
| s8812.clwb_5_covers | — | — | — | — | — | — | 1 (mutation.eic.line5_key.two_children) |
| s8812.clwb_to7 | — | — | — | — | — | — | 4 |
| s8812.clwb_7 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_8 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_9 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_10 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_11_figured | — | — | — | — | — | — | — |
| s8812.clwb_11_three | — | — | — | — | — | — | — |
| s8812.clwb_11 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 8 |
| s8812.clwb_12 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_13 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_14 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |
| s8812.clwb_15 | — | — | — | 2 (classm.s8812.3.deepseek, classm.s8812.3) | — | — | 6 |

Unasserted lines: s8812.no, s8812.has_qualifying_child, s8812.puerto_rico_if_child, s8812.eiw_2b, s8812.eiw_7_figured, s8812.chart_eic, s8812.amt_ws6, s8812.from_part_iia_figured, s8812.part_iib_figured, s8812.clwb_complete, s8812.clwb_three, s8812.clwb_11_figured, s8812.clwb_11_three

## Schedule A — supported itemized deductions and standard comparison

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sa.unsupported | — | — | — | — | — | — | 3 |
| sa.gifts | — | — | — | — | — | — | — |
| sa.no | — | — | — | — | — | — | — |
| sa.charity_limited | — | — | — | — | — | — | — |
| sa.charity_limited_if_gifts | — | — | — | — | — | — | — |
| sa.gift_carryover | — | — | — | — | — | — | — |
| sa.gift_carryover_if_no_gifts | — | — | — | — | — | — | — |
| sa.excluded_income | — | — | — | — | — | — | — |
| sa.dependent | — | — | — | — | — | — | — |
| sa.spouse_extra | — | — | — | — | — | — | — |
| sa.mfs_spouse_extra | — | — | — | — | — | — | 1 (mfs.sa.spouse_itemizes_no_extra_question) |
| sa.mfs_spouse_not_itemizing | — | — | — | — | — | — | — |
| sa.age65_count | — | — | — | — | — | — | — |
| sa.age65 | — | — | — | — | — | — | — |
| sa.spouse_itemizes | — | — | — | — | — | — | — |
| sa.elect_itemize | — | — | — | — | — | — | — |
| sa.agi | — | — | — | — | — | — | — |
| sa.medical_any | — | — | — | — | — | — | — |
| sa.medical_premiums | — | — | — | — | — | — | — |
| sa.medical_premiums_if_not_large | — | — | — | — | — | — | — |
| sa.medical_asked | — | — | — | — | — | — | — |
| sa.line1 | — | — | — | — | — | — | — |
| sa.line1_if_medical | — | — | — | 8 | — | — | 1 (mutation.m3.sa.medical_premiums) |
| sa.state_tax_any | — | — | — | — | — | — | — |
| sa.state_tax_other_any | — | — | — | — | — | — | — |
| sa.line5a | — | — | — | — | — | — | 1 (stage16.other.o1) |
| sa.line5a_if_state_tax | — | — | — | — | — | — | — |
| sa.state_tax_other | — | — | — | — | — | — | — |
| sa.state_tax_other_if_any | — | — | — | — | — | — | — |
| sa.line5a_total | — | — | — | 8 | — | — | — |
| sa.home_owner | — | — | — | — | — | — | — |
| sa.home_other | — | — | — | — | — | — | — |
| sa.home_other_if_not_owner | — | — | — | — | — | — | — |
| sa.home_asked | — | — | — | — | — | — | — |
| sa.line5b | — | — | — | — | — | — | — |
| sa.line5b_if_home_owner | — | — | — | — | — | — | — |
| sa.property_tax_other_any | — | — | — | — | — | — | — |
| sa.property_tax_other_if_home | — | — | — | — | — | — | — |
| sa.property_tax_leave_out | — | — | — | — | — | — | — |
| sa.property_tax_leave_out_if_any | — | — | — | — | — | — | — |
| sa.line5b_net | — | — | — | 8 | — | — | — |
| sa.personal_property_tax_any | — | — | — | — | — | — | — |
| sa.line5c | — | — | — | — | — | — | — |
| sa.line5c_if_taxed | — | — | — | 8 | — | — | 1 (mutation.m3.sa.no_mortgage_property_tax) |
| sa.mortgage_interest | — | — | — | — | — | — | — |
| sa.line8a | — | — | — | 8 | — | — | 3 |
| sa.has_mortgage_interest | — | — | — | — | — | — | — |
| sa.mortgage_unreported | — | — | — | — | — | — | — |
| sa.mortgage_unreported_if_home | — | — | — | — | — | — | — |
| sa.mortgage_over_limit | — | — | — | — | — | — | — |
| sa.mortgage_interest_not_mfs | — | — | — | — | — | — | — |
| sa.mortgage_interest_mfs | — | — | — | — | — | — | — |
| sa.mortgage_over_limit_if_joint_limits | — | — | — | — | — | — | 2 (mfs.sa.mortgage_under_mfs_limit, mint.sa.mortgage_limit.over_limit_1098_only) |
| sa.mortgage_over_limit_mfs | — | — | — | — | — | — | — |
| sa.mortgage_over_limit_mfs_if_mfs | — | — | — | — | — | — | — |
| sa.mortgage_over_limit_if_interest | — | — | — | — | — | — | 2 (mfs.sa.mortgage_over_mfs_limit, mfs.sa.mortgage_under_mfs_limit) |
| sa.mortgage_other_use | — | — | — | — | — | — | — |
| sa.mortgage_other_use_if_interest | — | — | — | — | — | — | — |
| sa.sales_tax_wish | — | — | — | — | — | — | — |
| sa.foreign_tax_deduct | — | — | — | — | — | — | — |
| sa.foreign_tax_deduct_if_tax | — | — | — | — | — | — | — |
| sa.estate_tax_income | — | — | — | — | — | — | — |
| sa.bond_premium | — | — | — | — | — | — | — |
| sa.debt_instrument_loss | — | — | — | — | — | — | — |
| sa.pension_unrecovered | — | — | — | — | — | — | — |
| sa.impairment_work | — | — | — | — | — | — | — |
| sa.line11 | — | — | — | — | — | — | — |
| sa.line11_if_gifts | — | — | — | 14 | — | — | — |
| sa.zero | — | — | — | via sa.line6: 6; via sa.line8b: 6; via sa.line8c: 6; via sa.line13: 6; via sa.line15: 6 | — | — | — |
| sa.agi_floor | — | — | — | via sa.line2: 6 | — | — | — |
| sa.line2 | — | — | — | 14 | — | — | 2 (audit.sa.negative_agi_medical, audit.sa.negative_agi_medical_paid) |
| sa.line3 | — | — | — | 14 | — | OpenTaxSolver: 1586 compared (1586 nonzero), 111 excluded; UsTaxes: 1166 compared (1166 nonzero), 534 excluded | 3 |
| sa.line4 | — | — | — | 14 | — | OpenTaxSolver: 1586 compared (100 nonzero), 114 excluded; UsTaxes: 1166 compared (73 nonzero), 534 excluded | 5 |
| sa.line5d | — | — | — | 14 | — | OpenTaxSolver: 1700 compared (826 nonzero), 0 excluded; UsTaxes: 1400 compared (682 nonzero), 300 excluded | 3 |
| sa.saltbase | — | — | — | — | — | — | — |
| sa.saltfloor | — | — | — | — | — | — | — |
| sa.saltthreshold | — | — | — | — | — | — | — |
| sa.saltexcess | — | — | — | — | — | — | — |
| sa.saltreduction | — | — | — | — | — | — | — |
| sa.saltremaining | — | — | — | — | — | — | — |
| sa.saltfloor_applied | — | — | — | — | — | — | — |
| sa.salthalf | — | — | — | — | — | — | 1 (stage4.salt.mfs_floor) |
| sa.mfs | — | — | — | — | — | — | — |
| sa.saltlimit | — | — | — | — | — | — | — |
| sa.line5e | — | — | — | 14 | — | OpenTaxSolver: 1659 compared (800 nonzero), 0 excluded; UsTaxes: 1166 compared (568 nonzero), 534 excluded | 13 |
| sa.line6 | — | — | — | 14 | — | — | 5 |
| sa.line8b | — | — | — | 14 | — | — | 4 |
| sa.line8c | — | — | — | 14 | — | — | 4 |
| sa.line13 | — | — | — | 14 | — | — | 5 |
| sa.line15 | — | — | — | 14 | — | — | 6 |
| sa.gambling_losses | — | — | — | — | — | — | — |
| sa.line16_gambling | — | — | — | — | — | — | — |
| sa.line16 | — | — | — | 14 | — | — | 5 |
| sa.line7 | — | — | — | 14 | — | OpenTaxSolver: 1659 compared (800 nonzero), 0 excluded; UsTaxes: 1166 compared (568 nonzero), 534 excluded | 2 (stage4.deductions.combined, stage16.other.o1) |
| sa.line8e | — | — | — | 14 | — | OpenTaxSolver: 1700 compared (505 nonzero), 0 excluded; UsTaxes: 1400 compared (404 nonzero), 300 excluded | 2 (stage4.deductions.combined, stage16.other.o1) |
| sa.line9 | — | — | — | 14 | — | — | 2 (stage20.blind.r9, stage4.deductions.combined) |
| sa.line10 | — | — | — | 14 | — | OpenTaxSolver: 1579 compared (479 nonzero), 121 excluded; UsTaxes: 1070 compared (304 nonzero), 630 excluded | 2 (stage4.deductions.combined, stage16.other.o1) |
| sa.line12_noncash | — | — | — | — | — | — | — |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 14 | — | — | 10 |
| sa.form8283 | — | — | — | — | — | — | 4 |
| sa.line14 | — | — | — | 14 | — | OpenTaxSolver: 1697 compared (602 nonzero), 3 excluded; UsTaxes: 1400 compared (496 nonzero), 300 excluded | 3 |
| sa.line17 | — | — | — | 14 | — | PE: 1513 compared (661 nonzero), 172 excluded; TC: 1190 compared (515 nonzero), 510 excluded; OpenTaxSolver: 1476 compared (646 nonzero), 224 excluded; UsTaxes: 1070 compared (472 nonzero), 630 excluded | 11 |
| sa.standardbase | — | — | — | — | — | — | — |
| sa.extra | — | — | — | — | — | — | — |
| sa.boxes_age65 | — | — | — | — | — | — | 1 (stage16.sa.decedent_spouse) |
| sa.extra_age65 | — | — | — | — | — | — | — |
| sa.boxes_blind | — | — | — | — | — | — | — |
| sa.extra_blind | — | — | — | — | — | — | — |
| sa.standardraw | — | — | — | — | — | — | — |
| sa.dep_earned_sum | — | — | — | — | — | — | 1 (dep.earned_below_zero) |
| sa.dep_earned | — | — | — | — | — | — | 4 |
| sa.dep_add | — | — | — | — | — | — | — |
| sa.dep_plus | — | — | — | — | — | — | — |
| sa.dep_min | — | — | — | — | — | — | — |
| sa.dep_line2 | — | — | — | 7 | — | — | 4 |
| sa.dep_line3 | — | — | — | 7 | — | — | 1 (dep.joint_both_claimable) |
| sa.dep_line4a | — | — | — | 7 | — | — | 2 (dep.pub501_ex3_blind, dep.capped_at_basic) |
| sa.dep_line4b | — | — | — | 6 | — | — | 1 (dep.pub501_ex3_blind) |
| sa.dep_line4c | — | — | — | 6 | — | — | — |
| sa.dep_qss | — | — | — | — | — | — | — |
| sa.standard_amount | — | — | — | — | — | — | — |
| sa.standard | — | — | — | — | — | PE: 1681 compared (1681 nonzero), 19 excluded; OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 29 |
| sa.itemizes | — | — | — | — | — | — | 15 |
| sa.deduction | — | — | — | via f1040.line12e: 6 | — | PE: 1513 compared (1513 nonzero), 172 excluded; TC: 902 compared (902 nonzero), 798 excluded; OpenTaxSolver: 1476 compared (1476 nonzero), 224 excluded; UsTaxes: 1070 compared (1070 nonzero), 630 excluded; E via f1040.line12e (OpenTaxSolver, UsTaxes) | 18 |
| sa.mfs_spouse_itemizes | — | — | — | — | — | — | — |

Unasserted lines: sa.no, sa.charity_limited_if_gifts, sa.gift_carryover_if_no_gifts, sa.mfs_spouse_not_itemizing, sa.age65_count, sa.age65, sa.agi, sa.medical_premiums_if_not_large, sa.medical_asked, sa.line5a_if_state_tax, sa.state_tax_other_if_any, sa.home_other_if_not_owner, sa.home_asked, sa.line5b_if_home_owner, sa.property_tax_other_if_home, sa.property_tax_leave_out_if_any, sa.has_mortgage_interest, sa.mortgage_unreported_if_home, sa.mortgage_interest_not_mfs, sa.mortgage_interest_mfs, sa.mortgage_over_limit_mfs_if_mfs, sa.mortgage_other_use_if_interest, sa.foreign_tax_deduct_if_tax, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.line16_gambling, sa.line12_noncash, sa.standardbase, sa.extra, sa.extra_age65, sa.boxes_blind, sa.extra_blind, sa.standardraw, sa.dep_add, sa.dep_plus, sa.dep_min, sa.dep_qss, sa.standard_amount, sa.mfs_spouse_itemizes

## Form 8949 and Schedule D — manually classified securities transactions

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sales.box | — | — | — | — | — | — | — |
| sales.route | — | — | — | — | — | — | — |
| sales.detail | — | — | — | — | — | — | — |
| sales.route_if_chosen | — | — | — | — | — | — | — |
| sales.code | — | — | — | — | — | — | — |
| sales.special | — | — | — | — | — | — | — |
| sales.aggregate_eligible | — | — | — | — | — | — | — |
| sales.proceeds | — | — | — | — | — | — | — |
| sales.reported_basis | — | — | — | — | — | — | — |
| sales.correct_basis | — | — | — | — | — | — | — |
| sales.wash_loss | — | — | — | — | — | — | — |
| sales.covered | — | — | — | — | — | — | — |
| sales.digital | — | — | — | — | — | — | — |
| sales.has_b | — | — | — | — | — | — | — |
| sales.has_w | — | — | — | — | — | — | — |
| sales.bad_code | — | — | — | — | — | — | — |
| sales.bad_aggregate | — | — | — | — | — | — | — |
| sales.aggregate_fails | — | — | — | — | — | — | — |
| sales.no | — | — | — | — | — | — | — |
| sales.one | — | — | — | — | — | — | — |
| sales.zero | — | — | — | — | — | — | — |
| sales.e | 1 (sales.official.da.basis_worksheet) | — | — | 3 | — | — | — |
| sales.b_difference | — | — | — | — | — | — | — |
| sales.adjust_b | — | — | — | — | — | — | — |
| sales.b | — | — | — | — | — | — | — |
| sales.wash_over | — | — | — | — | — | — | — |
| sales.wash_bad | — | — | — | — | — | — | — |
| sales.w | — | — | — | — | — | — | 1 (sales.refuse.wash_over_loss) |
| sales.g | 5 | — | — | 3 | — | — | 29 |
| sales.before_adjustment | — | — | — | — | — | — | — |
| sales.h | 7 | — | — | 3 | — | — | 29 |

Unasserted lines: sales.detail, sales.route_if_chosen, sales.covered, sales.digital, sales.has_b, sales.has_w, sales.bad_code, sales.bad_aggregate, sales.aggregate_fails, sales.no, sales.one, sales.zero, sales.b_difference, sales.adjust_b, sales.b, sales.wash_over, sales.wash_bad, sales.before_adjustment

## Schedule B — supported interest and ordinary dividends

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sb.nominee | — | — | — | — | — | — | — |
| sb.bonds_any | — | — | — | — | — | — | — |
| sb.bond_special | — | — | — | — | — | — | — |
| sb.unsupported | — | — | — | — | — | — | — |
| sb.ordinary_dividends | — | — | — | — | — | — | — |
| sb.account_any | — | — | — | — | — | — | — |
| sb.asset_any | — | — | — | — | — | — | — |
| sb.trust_any | — | — | — | — | — | — | — |
| sb.company_any | — | — | — | — | — | — | — |
| sb.territory_any | — | — | — | — | — | — | — |
| sb.foreign_any | — | — | — | — | — | — | — |
| sb.foreign_trust_any | — | — | — | — | — | — | — |
| sb.foreign_company_any | — | — | — | — | — | — | — |
| sb.foreign_no | — | — | — | — | — | — | — |
| sb.line7a | — | — | — | — | — | — | — |
| sb.fbar_required | — | — | — | — | — | — | — |
| sb.form8938 | — | — | — | — | — | — | — |
| sb.line8 | — | — | — | — | — | — | — |
| sb.zero | — | — | — | — | — | — | — |
| sb.line2 | — | — | — | 3 | — | UsTaxes: 1400 compared (1059 nonzero), 300 excluded | 14 |
| sb.line3 | — | — | — | 3 | — | — | 7 |
| sb.line4 | — | — | — | 3; via f1040.line2b: 6; via f8960.line1 → f1040.line2b: 3 | — | UsTaxes: 1400 compared (1059 nonzero), 300 excluded | 6 |
| sb.line6 | — | — | — | 2 (classm.sb.1, classm.sb.3) | — | — | 6 |
| sb.partIII | — | — | — | — | — | — | 3 |
| sb.form5471 | — | — | — | — | — | — | — |
| sb.interest_total | — | — | — | — | — | — | — |
| sb.has_income | — | — | — | — | — | — | — |
| sb.no | — | — | — | — | — | — | — |
| sb.ordinary_dividends_if_dividends | — | — | — | via f1040.line3b → sb.line6: 6; via f8960.line2 → f1040.line3b → sb.line6: 3 | — | — | — |
| sb.nominee_if_income | — | — | — | — | — | — | — |
| sb.bonds_any_if_income | — | — | — | — | — | — | — |
| sb.bond_special_if_bonds | — | — | — | — | — | — | — |
| sb.unsupported_if_income | — | — | — | — | — | — | — |
| sb.fbar_required_if_foreign | — | — | — | — | — | — | — |
| sb.form8938_if_foreign | — | — | — | — | — | — | — |
| sb.line7a_if_foreign | — | — | — | — | — | — | — |
| sb.line8_if_foreign | — | — | — | — | — | — | — |
| sb.form5471_if_foreign | — | — | — | — | — | — | — |

Unasserted lines: sb.unsupported, sb.foreign_any, sb.foreign_trust_any, sb.foreign_company_any, sb.foreign_no, sb.zero, sb.interest_total, sb.has_income, sb.no, sb.nominee_if_income, sb.bonds_any_if_income, sb.bond_special_if_bonds, sb.unsupported_if_income, sb.fbar_required_if_foreign, sb.form8938_if_foreign, sb.line7a_if_foreign, sb.line8_if_foreign, sb.form5471_if_foreign

## Schedule C (Form 1040) — Profit or Loss From Business, one per business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sc.one | — | — | — | — | — | — | — |
| sc.rrta | — | — | — | — | — | — | — |
| sc.zero | — | — | — | — | — | — | — |
| sc.statutory | — | — | — | — | — | — | — |
| sc.passive | — | — | — | — | — | — | — |
| sc.spouse_owned | — | — | — | — | — | — | — |
| sc.method_other | — | — | — | — | — | — | — |
| sc.special | — | — | — | — | — | — | — |
| sc.business_credit | — | — | — | — | — | — | — |
| sc.fuel_credit | — | — | — | — | — | — | — |
| sc.screened | — | — | — | — | — | — | — |
| sc.line1 | — | — | — | — | — | — | 8 |
| sc.line2 | — | — | — | — | — | — | — |
| sc.line3 | — | — | — | 4 | — | — | 1 (stage14.sc.basic) |
| sc.line4 | — | — | — | 4 | — | — | 1 (stage14.sc.basic) |
| sc.line5 | — | — | — | 4 | — | — | — |
| sc.line6 | — | — | — | — | — | — | — |
| sc.line7 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | 1 (stage14.sc.basic) |
| sc.line8 | — | — | — | — | — | — | — |
| sc.line9 | — | — | — | 4 | — | — | 1 (stage14.veh.standard) |
| sc.line10 | — | — | — | — | — | — | — |
| sc.line11 | — | — | — | — | — | — | — |
| sc.line12 | — | — | — | 4 | — | — | — |
| sc.line13 | — | — | — | 4 | — | — | 21 |
| sc.employees | — | — | — | — | — | — | — |
| sc.line14 | — | — | — | — | — | — | — |
| sc.line14_if_employees | — | — | — | — | — | — | — |
| sc.line15 | — | — | — | — | — | — | — |
| sc.line16a | — | — | — | — | — | — | — |
| sc.line16b | — | — | — | — | — | — | — |
| sc.line17 | — | — | — | — | — | — | — |
| sc.line18 | — | — | — | — | — | — | — |
| sc.line19 | — | — | — | — | — | — | — |
| sc.line19_if_employees | — | — | — | — | — | — | — |
| sc.line20a | — | — | — | 4 | — | — | 2 (stage14.veh.leased_actual, stage14.sehi.with_lease) |
| sc.line20b | — | — | — | — | — | — | — |
| sc.line21 | — | — | — | — | — | — | — |
| sc.line22 | — | — | — | — | — | — | — |
| sc.line23 | — | — | — | — | — | — | — |
| sc.travel_meals | — | — | — | — | — | — | — |
| sc.line24a | — | — | — | — | — | — | — |
| sc.line24a_if_travel_meals | — | — | — | — | — | — | — |
| sc.meals_50 | — | — | — | — | — | — | — |
| sc.meals_50_if_travel_meals | — | — | — | — | — | — | — |
| sc.meals_80 | — | — | — | — | — | — | — |
| sc.meals_80_if_travel_meals | — | — | — | — | — | — | — |
| sc.meals_100 | — | — | — | — | — | — | — |
| sc.meals_100_if_travel_meals | — | — | — | — | — | — | — |
| sc.meals_50_ded | — | — | — | — | — | — | — |
| sc.meals_80_ded | — | — | — | — | — | — | — |
| sc.line24b | — | — | — | 4 | — | — | 2 (stage14.sc.basic, stage14.sc.meals_full) |
| sc.line25 | — | — | — | — | — | — | 1 (bug0475.sc.home_utilities_not_in_part2) |
| sc.line26 | — | — | — | — | — | — | — |
| sc.line26_if_employees | — | — | — | — | — | — | — |
| sc.line27a | — | — | — | 4 | — | — | — |
| sc.line48 | — | — | — | — | — | — | — |
| sc.line27b | — | — | — | 4 | — | — | — |
| sc.line28 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | 3 |
| sc.line29 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | — |
| sc.line28_pre179 | — | — | — | — | — | — | — |
| sc.line29_pre179 | — | — | — | — | — | — | — |
| sc.ho_uses | — | — | — | — | — | — | — |
| sc.ho_other | — | — | — | — | — | — | — |
| sc.ho_screened | — | — | — | — | — | — | — |
| sc.ho_multi | — | — | — | — | — | — | — |
| sc.ho_sqft | — | — | — | — | — | — | — |
| sc.ho_home_sqft | — | — | — | — | — | — | — |
| sc.ho_rate | — | — | — | — | — | — | — |
| sc.ho_cap_sqft | — | — | — | — | — | — | — |
| sc.ho_over | — | — | — | — | — | — | — |
| sc.ho_line4_actual | — | — | — | — | — | — | — |
| sc.ho_line4_cap | — | — | — | — | — | — | — |
| sc.ho_line4 | — | — | — | 4 | — | — | 3 |
| sc.ho_line1 | — | — | — | 4 | — | — | 1 (stage14.ho.with_179) |
| sc.ho_room | — | — | — | — | — | — | — |
| sc.ho_unlimited | — | — | — | — | — | — | 1 (stage14.mut.ho_100_sqft_gross_limit) |
| sc.ho_s179_max | — | — | — | — | — | — | — |
| sc.ho_no179 | — | — | — | — | — | — | — |
| sc.ho_limited | — | — | — | — | — | — | — |
| sc.ho_pre179_floor | — | — | — | — | — | — | — |
| sc.ho_both_limits | — | — | — | — | — | — | 3 |
| sc.ho_both | — | — | — | — | — | — | — |
| sc.ho_line5_lim | — | — | — | — | — | — | 1 (stage14.ho.basic) |
| sc.ho_line5 | — | — | — | 4 | — | — | 1 (bug0489.sc.no_home_office_with_179_limit) |
| sc.line30 | — | — | — | 4 | — | — | 13 |
| sc.line31 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | 18 |
| sc.line31_pre179 | — | — | — | — | — | — | — |
| sc.loss | — | — | — | — | — | — | 2 (stage14.s179.wages_count, stage14.ho.gross_limit) |
| sc.at_risk | — | — | — | — | — | — | — |
| sc.not_at_risk | — | — | — | — | — | — | — |
| sc.loss_allowed | — | — | — | — | — | — | 1 (stage14.refuse.at_risk) |
| sc.result | — | — | — | — | — | — | — |
| sc.inventory_other | — | — | — | — | — | — | — |
| sc.goods | — | — | — | — | — | — | — |
| sc.line35 | — | — | — | — | — | — | 1 (stage14.refuse.inventory) |
| sc.line35_if_goods | — | — | — | — | — | — | — |
| sc.line36 | — | — | — | — | — | — | — |
| sc.line36_if_goods | — | — | — | — | — | — | — |
| sc.line37 | — | — | — | — | — | — | — |
| sc.line37_if_goods | — | — | — | — | — | — | — |
| sc.line38 | — | — | — | — | — | — | — |
| sc.line38_if_goods | — | — | — | — | — | — | — |
| sc.line39 | — | — | — | — | — | — | — |
| sc.line39_if_goods | — | — | — | — | — | — | — |
| sc.line40 | — | — | — | 4 | — | — | — |
| sc.line41 | — | — | — | — | — | — | — |
| sc.line41_if_goods | — | — | — | — | — | — | — |
| sc.line42 | — | — | — | 4 | — | — | — |
| sc.f6 | — | — | — | — | — | — | 1 (stage14.asset.listed_and_not) |
| sc.f14 | — | — | — | — | — | — | 2 (stage14.asset.bonus_100, stage14.asset.listed_and_not) |
| sc.f17 | — | — | — | — | — | — | 3 |
| sc.f19_y3 | — | — | — | — | — | — | — |
| sc.f19_y5 | — | — | — | — | — | — | 1 (stage14.asset.hy_5yr) |
| sc.f19_y7 | — | — | — | — | — | — | — |
| sc.f19_y10 | — | — | — | — | — | — | — |
| sc.f19_y15 | — | — | — | — | — | — | — |
| sc.f19_y20 | — | — | — | — | — | — | — |
| sc.f19_y15sl | — | — | — | — | — | — | 2 (stage14.asset.qip, stage14.asset.qip_elected) |
| sc.f25_assets | — | — | — | — | — | — | — |
| sc.f25_veh | — | — | — | — | — | — | — |
| sc.f25 | — | — | — | — | — | — | 2 (stage14.asset.listed_and_not, stage14.asset.listed_forty) |
| sc.f26_assets | — | — | — | — | — | — | — |
| sc.f26_veh | — | — | — | — | — | — | — |
| sc.f26h | — | — | — | — | — | — | 3 |
| sc.f28 | — | — | — | — | — | — | 1 (stage14.asset.listed_forty) |
| sc.f29_assets | — | — | — | — | — | — | — |
| sc.f29_veh | — | — | — | — | — | — | — |
| sc.f29 | — | — | — | — | — | — | 1 (stage14.asset.listed_and_not) |
| sc.s179_elected | — | — | — | — | — | — | — |
| sc.dep_other | — | — | — | — | — | — | — |
| sc.s179_return | — | — | — | — | — | — | — |
| sc.s179_allowed | — | — | — | 4 | — | — | 1 (stage14.s179.refuse_multi) |
| sc.mq_q4_a | — | — | — | — | — | — | — |
| sc.mq_q4_v | — | — | — | — | — | — | — |
| sc.mq_q4 | — | — | — | — | — | — | — |
| sc.mq_total_a | — | — | — | — | — | — | — |
| sc.mq_total_v | — | — | — | — | — | — | — |
| sc.mq_total | — | — | — | — | — | — | — |
| sc.cost179_a | — | — | — | — | — | — | — |
| sc.cost179_v | — | — | — | — | — | — | — |
| sc.cost179 | — | — | — | — | — | — | — |
| sc.rent_equipment | — | — | — | — | — | — | — |
| sc.veh_lease | — | — | — | — | — | — | — |
| sc.profit_pos | — | — | — | — | — | — | — |
| sc.hi_uses | — | — | — | — | — | — | — |
| sc.hi_screen | — | — | — | — | — | — | — |
| sc.hi_screened | — | — | — | — | — | — | — |
| sc.f7206_line1 | — | — | — | — | — | — | 1 (stage14.sehi.refuse_ptc) |
| sc.f7206_line2 | — | — | — | 4 | — | — | 1 (stage14.sehi.ltc) |
| sc.f7206_line3 | — | — | — | 4 | — | — | — |
| sc.f7206_line4 | — | — | — | 4 | — | — | 1 (stage14.f7206.line9_no_plan_se_screened) |
| sc.f7206_line5 | — | — | — | 4 | — | — | 1 (stage14.f7206.line9_no_plan_se_screened) |
| sc.f7206_has | — | — | — | — | — | — | 1 (stage14.mut.sehi_side_business_no_profit) |
| sc.f7206_line7_pos | — | — | — | — | — | — | — |
| sc.f7206_line7 | — | — | — | 3 | — | — | 2 (stage14.sehi.two_businesses, stage14.f7206.line9_no_plan_se_screened) |
| sc.f7206_line8 | — | — | — | 3 | — | — | — |
| sc.f7206_line9_pos | — | — | — | — | — | — | — |
| sc.f7206_line9 | — | — | — | 4 | — | — | 2 (stage14.sehi.with_sep, stage14.f7206.line9_no_plan_se_screened) |
| sc.f7206_line10 | — | — | — | 3 | — | — | 1 (stage14.sehi.with_sep) |
| sc.f7206_line13 | — | — | — | 3 | — | — | — |
| sc.f7206_min | — | — | — | — | — | — | — |
| sc.f7206_line14 | — | — | — | 4 | — | — | 6 |
| sc.qbi_has | — | — | — | — | — | — | 1 (mutation.t2.person.eic_se_not_filed_health_insurance) |
| sc.qbi_se_pos | — | — | — | — | — | — | — |
| sc.qbi_se | — | — | — | — | — | — | — |
| sc.qbi_plan_pos | — | — | — | — | — | — | — |
| sc.qbi_plan | — | — | — | — | — | — | — |
| sc.qbi_ded | — | — | — | — | — | — | — |
| sc.qbi | — | — | — | 3 | — | — | 3 |
| sc.tips_ot | — | — | — | — | — | — | — |

Unasserted lines: sc.one, sc.rrta, sc.zero, sc.screened, sc.line14_if_employees, sc.line19_if_employees, sc.line24a_if_travel_meals, sc.meals_50_if_travel_meals, sc.meals_80_if_travel_meals, sc.meals_100_if_travel_meals, sc.meals_50_ded, sc.meals_80_ded, sc.line26_if_employees, sc.line28_pre179, sc.line29_pre179, sc.ho_screened, sc.ho_multi, sc.ho_rate, sc.ho_cap_sqft, sc.ho_over, sc.ho_line4_actual, sc.ho_line4_cap, sc.ho_room, sc.ho_s179_max, sc.ho_no179, sc.ho_limited, sc.ho_pre179_floor, sc.ho_both, sc.line31_pre179, sc.not_at_risk, sc.result, sc.line35_if_goods, sc.line36_if_goods, sc.line37_if_goods, sc.line38_if_goods, sc.line39_if_goods, sc.line41_if_goods, sc.f19_y3, sc.f19_y7, sc.f19_y10, sc.f19_y15, sc.f19_y20, sc.f25_assets, sc.f25_veh, sc.f26_assets, sc.f26_veh, sc.f29_assets, sc.f29_veh, sc.s179_elected, sc.dep_other, sc.s179_return, sc.mq_q4_a, sc.mq_q4_v, sc.mq_q4, sc.mq_total_a, sc.mq_total_v, sc.mq_total, sc.cost179_a, sc.cost179_v, sc.cost179, sc.veh_lease, sc.profit_pos, sc.hi_screened, sc.f7206_line7_pos, sc.f7206_line9_pos, sc.f7206_min, sc.qbi_se_pos, sc.qbi_se, sc.qbi_plan_pos, sc.qbi_plan, sc.qbi_ded

## Schedule E, Part I — totals (rental real estate and royalties)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sche.no | — | — | — | — | — | — | — |
| sche.re_pro | — | — | — | — | — | — | — |
| sche.grouped | — | — | — | — | — | — | — |
| sche.qbi_business | — | — | — | — | — | — | — |
| sche.rents | — | — | — | — | — | — | — |
| sche.line23a | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 1 (mrental.rental.excluded_home_with_costs) |
| sche.line23b | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 1 (x1sche.f7.royalty_magi) |
| sche.line23c | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | — |
| sche.line23d | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 1 (mrental.rental.excluded_home_with_costs) |
| sche.rent_exp | — | — | — | — | — | — | — |
| sche.roy_exp | — | — | — | — | — | — | — |
| sche.line23e | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 1 (mrental.royalty.expenses_and_loss) |
| sche.rent_income | — | — | — | — | — | — | — |
| sche.roy_income | — | — | — | — | — | — | — |
| sche.line24 | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 8 |
| sche.rent_loss | — | — | — | — | — | — | — |
| sche.roy_loss | — | — | — | — | — | — | — |
| sche.line25 | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 2 (x1sche.f4.two_properties, mrental.royalty.expenses_and_loss) |
| sche.line26 | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | 18 |
| sche.line41 | — | — | — | 2 (classm.sche.1, classm.sche.2) | — | — | — |
| sche.loss_prelimit | — | — | — | — | — | — | — |
| sche.rent_netloss | — | — | — | — | — | — | — |
| sche.roy_lossabs | — | — | — | — | — | — | — |
| sche.nonpassive_net | — | — | — | — | — | — | — |
| sche.count | — | — | — | — | — | — | — |
| sche.rental_count | — | — | — | — | — | — | — |
| sche.royalty_count | — | — | — | — | — | — | — |
| sche.any_listed | — | — | — | — | — | — | — |
| sche.any | — | — | — | — | — | — | 1 (x1sche.f9.excluded_home) |

Unasserted lines: sche.no, sche.rents, sche.rent_exp, sche.roy_exp, sche.rent_income, sche.roy_income, sche.rent_loss, sche.roy_loss, sche.loss_prelimit, sche.rent_netloss, sche.roy_lossabs, sche.nonpassive_net, sche.count, sche.rental_count, sche.royalty_count, sche.any_listed

## Proof-of-concept scope screening

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scope.no | — | — | — | — | — | — | — |
| scope.w2_count | — | — | — | — | — | — | — |
| scope.has_w2 | — | — | — | — | — | — | — |
| scope.noncitizen | — | — | — | — | — | — | — |
| scope.nonresident | — | — | — | — | — | — | — |
| scope.nonresident_if_noncitizen | — | — | — | — | — | — | — |
| scope.chapter11 | — | — | — | — | — | — | — |
| scope.armed_forces | — | — | — | — | — | — | — |
| scope.reservist_expenses | — | — | — | — | — | — | — |
| scope.reservist_expenses_if_armed_forces | — | — | — | — | — | — | — |
| scope.military_move | — | — | — | — | — | — | — |
| scope.military_move_if_armed_forces | — | — | — | — | — | — | — |
| scope.reservist_repaid | — | — | — | — | — | — | — |
| scope.reservist_repaid_if_armed_forces | — | — | — | — | — | — | — |
| scope.under24_count | — | — | — | — | — | — | — |
| scope.under24 | — | — | — | — | — | — | — |
| scope.under24_if_not_joint | — | — | — | — | — | — | — |
| scope.unearned_2700 | — | — | — | — | — | — | — |
| scope.unearned_2700_if_under24 | — | — | — | — | — | — | — |
| scope.f8615 | — | — | — | — | — | — | — |
| scope.f8615_if_unearned_2700 | — | — | — | — | — | — | — |
| scope.f8814 | — | — | — | — | — | — | — |
| scope.adoption_benefits | — | — | — | — | — | — | — |
| scope.adoption_benefits_if_adoption | — | — | — | — | — | — | — |
| scope.rental | — | — | — | — | — | — | — |
| scope.rent_personal | — | — | — | — | — | — | — |
| scope.rent_personal_if_rental | — | — | — | — | — | — | — |
| scope.k1 | — | — | — | — | — | — | — |
| scope.farm | — | — | — | — | — | — | — |
| scope.pay_no_w2 | — | — | — | — | — | — | — |
| scope.household_pay | — | — | — | — | — | — | — |
| scope.household_pay_if_pay | — | — | — | — | — | — | — |
| scope.contractor_pay | — | — | — | — | — | — | — |
| scope.contractor_pay_if_pay | — | — | — | — | — | — | — |
| scope.tips_unreported | — | — | — | — | — | — | — |
| scope.tips_unreported_if_pay | — | — | — | — | — | — | — |
| scope.strike_pay | — | — | — | — | — | — | — |
| scope.strike_pay_if_pay | — | — | — | — | — | — | — |
| scope.wages_no_form | — | — | — | — | — | — | — |
| scope.wages_no_form_if_pay | — | — | — | — | — | — | — |
| scope.medicaid_waiver | — | — | — | — | — | — | — |
| scope.religious_work | — | — | — | — | — | — | — |
| scope.clergy | — | — | — | — | — | — | — |
| scope.clergy_if_religious_work | — | — | — | — | — | — | — |
| scope.church_exempt_wages | — | — | — | — | — | — | — |
| scope.church_exempt_wages_if_religious_work | — | — | — | — | — | — | — |
| scope.w2_marks | — | — | — | — | — | — | — |
| scope.w2_marks_if_w2 | — | — | — | — | — | — | — |
| scope.artist_official | — | — | — | — | — | — | — |
| scope.artist_official_if_w2 | — | — | — | — | — | — | — |
| scope.performer_expenses | — | — | — | — | — | — | — |
| scope.performer_expenses_if_artist_official | — | — | — | — | — | — | — |
| scope.care_benefits_other | — | — | — | — | — | — | — |
| scope.care_benefits_other_if_benefits | — | — | — | — | — | — | — |
| scope.recovery | — | — | — | — | — | — | — |
| scope.disaster_distribution | — | — | — | — | — | — | — |
| scope.excess_deferral | — | — | — | — | — | — | — |
| scope.excess_deferral_if_w2 | — | — | — | — | — | — | — |
| scope.archer_msa | — | — | — | — | — | — | — |
| scope.education_recapture | — | — | — | — | — | — | — |
| scope.se_plan_other | — | — | — | — | — | — | — |
| scope.se_plan_other_if_business | — | — | — | — | — | — | — |
| scope.income_averaging | — | — | — | — | — | — | — |
| scope.income_averaging_if_business | — | — | — | — | — | — | — |
| scope.foreign_shares | — | — | — | — | — | — | — |
| scope.pfic | — | — | — | — | — | — | — |
| scope.pfic_if_foreign_shares | — | — | — | — | — | — | — |
| scope.cfc | — | — | — | — | — | — | — |
| scope.cfc_if_foreign_shares | — | — | — | — | — | — | — |
| scope.reforestation | — | — | — | — | — | — | — |
| scope.attorney_fees | — | — | — | — | — | — | — |
| scope.business_before | — | — | — | — | — | — | — |
| scope.nol | — | — | — | — | — | — | — |
| scope.passive | — | — | — | — | — | — | — |
| scope.passive_if_business_before | — | — | — | — | — | — | — |
| scope.f8978 | — | — | — | — | — | — | — |
| scope.f8978_if_business_before | — | — | — | — | — | — | — |
| scope.schedule1 | — | — | — | — | — | — | — |
| scope.other_income | — | — | — | — | — | — | — |
| scope.other_line16 | — | — | — | — | — | — | — |
| scope.ready_schedule1 | — | — | — | — | — | — | 9 |
| scope.ready_other_income | — | — | — | — | — | — | 9 |
| scope.ready_other_line16 | — | — | — | — | — | — | 11 |
| scope.ready_credits | — | — | — | — | — | — | — |
| scope.ready | — | — | — | — | — | — | 48 |

Unasserted lines: scope.no, scope.w2_count, scope.has_w2, scope.nonresident_if_noncitizen, scope.reservist_expenses_if_armed_forces, scope.military_move_if_armed_forces, scope.reservist_repaid_if_armed_forces, scope.under24_count, scope.under24, scope.under24_if_not_joint, scope.unearned_2700_if_under24, scope.f8615_if_unearned_2700, scope.adoption_benefits_if_adoption, scope.rent_personal_if_rental, scope.household_pay_if_pay, scope.contractor_pay_if_pay, scope.tips_unreported_if_pay, scope.strike_pay_if_pay, scope.wages_no_form_if_pay, scope.clergy_if_religious_work, scope.church_exempt_wages_if_religious_work, scope.w2_marks_if_w2, scope.artist_official_if_w2, scope.performer_expenses_if_artist_official, scope.care_benefits_other_if_benefits, scope.excess_deferral_if_w2, scope.se_plan_other_if_business, scope.income_averaging_if_business, scope.pfic_if_foreign_shares, scope.cfc_if_foreign_shares, scope.passive_if_business_before, scope.f8978_if_business_before, scope.schedule1, scope.other_income, scope.other_line16, scope.ready_credits

## Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scveh.zero | — | — | — | — | — | — | — |
| scveh.method | — | — | — | — | — | — | — |
| scveh.owned | — | — | — | — | — | — | — |
| scveh.placed_date | — | — | — | — | — | — | — |
| scveh.miles_business | — | — | — | — | — | — | — |
| scveh.miles_commuting | — | — | — | — | — | — | — |
| scveh.miles_other | — | — | — | — | — | — | — |
| scveh.cent | — | — | — | — | — | — | — |
| scveh.bm_c | — | — | — | — | — | — | — |
| scveh.cm_c | — | — | — | — | — | — | — |
| scveh.om_c | — | — | — | — | — | — | — |
| scveh.nonbusiness_c | — | — | — | — | — | — | — |
| scveh.total_c | — | — | — | — | — | — | 1 (stage14.refuse.veh_no_miles) |
| scveh.no_miles | — | — | — | — | — | — | — |
| scveh.over_half | — | — | — | — | — | — | — |
| scveh.parking | — | — | — | — | — | — | — |
| scveh.smr_always | — | — | — | — | — | — | — |
| scveh.smr_first | — | — | — | — | — | — | — |
| scveh.smr_first_if_not_always | — | — | — | — | — | — | — |
| scveh.fleet | — | — | — | — | — | — | — |
| scveh.smr_ok | — | — | — | — | — | — | — |
| scveh.smr_bad | — | — | — | — | — | — | — |
| scveh.rate | — | — | — | — | — | — | — |
| scveh.smr_amount | — | — | — | — | — | — | 1 (stage14.veh.refuse_smr) |
| scveh.line9_standard | — | — | — | — | — | — | — |
| scveh.operating | — | — | — | — | — | — | — |
| scveh.employee_use | — | — | — | — | — | — | — |
| scveh.employee_bad | — | — | — | — | — | — | — |
| scveh.operating_business | — | — | — | — | — | — | — |
| scveh.line9_actual | — | — | — | — | — | — | — |
| scveh.line9 | — | — | — | 5 | — | — | 8 |
| scveh.is_actual_owned | — | — | — | — | — | — | — |
| scveh.on_auto_limits | — | — | — | — | — | — | 1 (mutation.t2.f8962_months_scveh3) |
| scveh.is_actual_leased | — | — | — | — | — | — | — |
| scveh.lease | — | — | — | — | — | — | — |
| scveh.lease_smr_before | — | — | — | — | — | — | — |
| scveh.lease_smr_bad | — | — | — | — | — | — | — |
| scveh.lease_business | — | — | — | — | — | — | — |
| scveh.line20a | — | — | — | 5 | — | — | 1 (stage14.veh.refuse_lease_smr_before) |
| scveh.low_use | — | — | — | — | — | — | — |
| scveh.placed | — | — | — | — | — | — | 2 (stage14.veh.refuse_low_use, stage14.veh.refuse_half_use) |
| scveh.claims_bonus_this_year | — | — | — | — | — | — | — |
| scveh.records | — | — | — | — | — | — | — |
| scveh.got_other | — | — | — | — | — | — | — |
| scveh.acquired_before_bonus_date | — | — | — | — | — | — | — |
| scveh.acquired_before_bonus_date_if_this_year | — | — | — | — | — | — | — |
| scveh.used_before | — | — | — | — | — | — | — |
| scveh.used_before_if_bonus | — | — | — | — | — | — | — |
| scveh.bonus_excluded | — | — | — | — | — | — | — |
| scveh.bonus_excluded_if_bonus | — | — | — | — | — | — | — |
| scveh.prior_bonus | — | — | — | — | — | — | — |
| scveh.prior_bonus_if_earlier | — | — | — | — | — | — | — |
| scveh.prior_smr | — | — | — | — | — | — | — |
| scveh.prior_smr_if_earlier | — | — | — | — | — | — | — |
| scveh.prior_low_use | — | — | — | — | — | — | — |
| scveh.prior_low_use_if_earlier | — | — | — | — | — | — | — |
| scveh.converted | — | — | — | — | — | — | — |
| scveh.disposed | — | — | — | — | — | — | — |
| scveh.basis_changed | — | — | — | — | — | — | — |
| scveh.short_year | — | — | — | — | — | — | — |
| scveh.for_hire | — | — | — | — | — | — | — |
| scveh.investment | — | — | — | — | — | — | — |
| scveh.method_other | — | — | — | — | — | — | — |
| scveh.others_use | — | — | — | — | — | — | — |
| scveh.leasing | — | — | — | — | — | — | — |
| scveh.leasing_if_others_use | — | — | — | — | — | — | — |
| scveh.exempt_use | — | — | — | — | — | — | — |
| scveh.exempt_use_if_others_use | — | — | — | — | — | — | — |
| scveh.qbu_low | — | — | — | — | — | — | — |
| scveh.qbu_low_if_others_use | — | — | — | — | — | — | — |
| scveh.screen | — | — | — | — | — | — | — |
| scveh.screened | — | — | — | — | — | — | — |
| scveh.cost | — | — | — | — | — | — | 4 |
| scveh.passenger | — | — | — | — | — | — | — |
| scveh.suv | — | — | — | — | — | — | — |
| scveh.year | — | — | — | — | — | — | — |
| scveh.placed_this_year | — | — | — | — | — | — | — |
| scveh.first_year_after_recovery | — | — | — | — | — | — | 1 (b1mutB.veh.part3_reached) |
| scveh.y5 | — | — | — | — | — | — | — |
| scveh.part2_reached | — | — | — | — | — | — | 3 |
| scveh.part3_reached | — | — | — | — | — | — | 3 |
| scveh.bus_cost | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | — |
| scveh.s179_elect | — | — | — | — | — | — | — |
| scveh.suv_cap | — | — | — | — | — | — | — |
| scveh.s179_bad | — | — | — | — | — | — | 1 (mutation.t2.mfj_no_overtime_part3) |
| scveh.after_jan19 | — | — | — | — | — | — | — |
| scveh.bonus_choice | — | — | — | — | — | — | — |
| scveh.bonus_same | — | — | — | — | — | — | — |
| scveh.bonus_mixed | — | — | — | — | — | — | — |
| scveh.claims_bonus | — | — | — | — | — | — | — |
| scveh.rate40 | — | — | — | — | — | — | — |
| scveh.lim_first_bonus | — | — | — | — | — | — | — |
| scveh.lim_first_none | — | — | — | — | — | — | — |
| scveh.lim_this_year | — | — | — | — | — | — | — |
| scveh.lim_prior | — | — | — | — | — | — | — |
| scveh.line7 | — | — | — | 3 | — | — | 3 |
| scveh.line9w | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 3 |
| scveh.s179_this_year_ok | — | — | — | — | — | — | 2 (stage14.veh.refuse_suv_cap, stage14.veh.refuse_suv_cap_by_1) |
| scveh.line10 | — | — | — | 3 | — | — | 3 |
| scveh.line10_this_year | — | — | — | — | — | — | — |
| scveh.s179_line10 | — | — | — | — | — | — | — |
| scveh.line11 | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 5 |
| scveh.prior_179 | — | — | — | — | — | — | — |
| scveh.line14 | — | — | — | 3 | — | — | — |
| scveh.line15 | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 4 |
| scveh.bonus_full | — | — | — | — | — | — | 1 (stage14.veh.refuse_bonus_mixed) |
| scveh.bonus_forty | — | — | — | — | — | — | 1 (stage14.veh.refuse_bonus_mixed_forty) |
| scveh.bonus_fullcase | — | — | — | — | — | — | — |
| scveh.bonus_this_year | — | — | — | — | — | — | — |
| scveh.line16 | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 5 |
| scveh.bonus_allowed | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 3 |
| scveh.line17 | — | — | — | 3 | — | — | 2 (stage14.veh.2025_forty, bug0633.veh.stop_at_line16) |
| scveh.line18 | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | — |
| scveh.quarter | — | — | — | — | — | — | — |
| scveh.qconv | — | — | — | — | — | — | — |
| scveh.hy | — | — | — | — | — | — | — |
| scveh.prior_conv | — | — | — | — | — | — | — |
| scveh.rate_hy | — | — | — | — | — | — | — |
| scveh.rate_mq | — | — | — | — | — | — | — |
| scveh.rate_prior | — | — | — | — | — | — | — |
| scveh.line19_hy | — | — | — | — | — | — | — |
| scveh.line19_mq | — | — | — | — | — | — | — |
| scveh.line19_prior | — | — | — | — | — | — | — |
| scveh.line19 | — | — | — | 2 (classm.scveh.2, classm.scveh.3) | — | — | 8 |
| scveh.line19_earlier | — | — | — | — | — | — | — |
| scveh.line19_this_year | — | — | — | — | — | — | — |
| scveh.line20 | — | — | — | 3 | — | — | 12 |
| scveh.b100 | — | — | — | — | — | — | — |
| scveh.k1 | — | — | — | — | — | — | — |
| scveh.r1 | — | — | — | — | — | — | — |
| scveh.t1 | — | — | — | — | — | — | — |
| scveh.l1 | — | — | — | — | — | — | — |
| scveh.t1s | — | — | — | — | — | — | — |
| scveh.d1 | — | — | — | — | — | — | 1 (stage14.veh.2019_cheap_mq3) |
| scveh.k2 | — | — | — | — | — | — | — |
| scveh.r2 | — | — | — | — | — | — | — |
| scveh.t2 | — | — | — | — | — | — | — |
| scveh.l2 | — | — | — | — | — | — | — |
| scveh.d2 | — | — | — | — | — | — | — |
| scveh.k3 | — | — | — | — | — | — | — |
| scveh.r3 | — | — | — | — | — | — | — |
| scveh.t3 | — | — | — | — | — | — | — |
| scveh.l3 | — | — | — | — | — | — | — |
| scveh.d3 | — | — | — | — | — | — | — |
| scveh.k4 | — | — | — | — | — | — | — |
| scveh.r4 | — | — | — | — | — | — | — |
| scveh.t4 | — | — | — | — | — | — | — |
| scveh.l4 | — | — | — | — | — | — | — |
| scveh.d4 | — | — | — | — | — | — | — |
| scveh.k5 | — | — | — | — | — | — | — |
| scveh.r5 | — | — | — | — | — | — | — |
| scveh.t5 | — | — | — | — | — | — | — |
| scveh.l5 | — | — | — | — | — | — | — |
| scveh.d5 | — | — | — | — | — | — | — |
| scveh.k6 | — | — | — | — | — | — | — |
| scveh.r6 | — | — | — | — | — | — | — |
| scveh.t6 | — | — | — | — | — | — | — |
| scveh.l6 | — | — | — | — | — | — | — |
| scveh.d6 | — | — | — | — | — | — | — |
| scveh.d_total | — | — | — | — | — | — | 3 |
| scveh.unrecovered | — | — | — | — | — | — | 3 |
| scveh.post_amount | — | — | — | — | — | — | — |
| scveh.post | — | — | — | — | — | — | 3 |
| scveh.too_old | — | — | — | — | — | — | — |
| scveh.bonus_v | — | — | — | — | — | — | — |
| scveh.macrs_pass | — | — | — | — | — | — | — |
| scveh.macrs_heavy | — | — | — | — | — | — | — |
| scveh.macrs_v | — | — | — | — | — | — | 2 (stage14.veh.heavy_prior, stage14.veh.heavy_2019) |
| scveh.bonus | — | — | — | — | — | — | — |
| scveh.macrs | — | — | — | — | — | — | — |
| scveh.s179_this_year | — | — | — | 3 | — | — | 2 (stage14.veh.2025_179_over_line9, stage14.veh.2025_179_passenger_suv_unasked) |
| scveh.mq_q4 | — | — | — | — | — | — | — |
| scveh.mq_total | — | — | — | — | — | — | — |
| scveh.cost179 | — | — | — | — | — | — | — |
| scveh.bonus_o | — | — | — | — | — | — | — |
| scveh.macrs_o | — | — | — | — | — | — | — |
| scveh.s179_this_year_o | — | — | — | — | — | — | — |
| scveh.q4_basis | — | — | — | — | — | — | — |
| scveh.mq_q4_o | — | — | — | — | — | — | — |
| scveh.mq_q4_a2 | — | — | — | — | — | — | — |
| scveh.mq_total_o | — | — | — | — | — | — | — |
| scveh.mq_total_a2 | — | — | — | — | — | — | — |
| scveh.cost179_o | — | — | — | — | — | — | 1 (stage14.s179.line2_prior_vehicle) |
| scveh.cost179_a2 | — | — | — | — | — | — | — |
| scveh.no | — | — | — | — | — | — | — |
| scveh.is_actual_owned_test1 | — | — | — | — | — | — | — |
| scveh.is_actual_leased_test1 | — | — | — | — | — | — | — |
| scveh.is_actual_leased_test2 | — | — | — | — | — | — | — |

Unasserted lines: scveh.zero, scveh.cent, scveh.bm_c, scveh.cm_c, scveh.om_c, scveh.nonbusiness_c, scveh.no_miles, scveh.over_half, scveh.smr_first_if_not_always, scveh.smr_ok, scveh.smr_bad, scveh.rate, scveh.line9_standard, scveh.employee_bad, scveh.operating_business, scveh.line9_actual, scveh.is_actual_owned, scveh.is_actual_leased, scveh.lease_smr_bad, scveh.lease_business, scveh.low_use, scveh.claims_bonus_this_year, scveh.acquired_before_bonus_date_if_this_year, scveh.used_before_if_bonus, scveh.bonus_excluded_if_bonus, scveh.prior_bonus_if_earlier, scveh.prior_smr_if_earlier, scveh.prior_low_use_if_earlier, scveh.leasing_if_others_use, scveh.exempt_use_if_others_use, scveh.qbu_low_if_others_use, scveh.screen, scveh.screened, scveh.year, scveh.placed_this_year, scveh.y5, scveh.suv_cap, scveh.bonus_mixed, scveh.claims_bonus, scveh.rate40, scveh.lim_first_bonus, scveh.lim_first_none, scveh.lim_this_year, scveh.lim_prior, scveh.line10_this_year, scveh.s179_line10, scveh.bonus_fullcase, scveh.bonus_this_year, scveh.qconv, scveh.hy, scveh.rate_hy, scveh.rate_mq, scveh.rate_prior, scveh.line19_hy, scveh.line19_mq, scveh.line19_prior, scveh.line19_earlier, scveh.line19_this_year, scveh.b100, scveh.k1, scveh.r1, scveh.t1, scveh.l1, scveh.t1s, scveh.k2, scveh.r2, scveh.t2, scveh.l2, scveh.d2, scveh.k3, scveh.r3, scveh.t3, scveh.l3, scveh.d3, scveh.k4, scveh.r4, scveh.t4, scveh.l4, scveh.d4, scveh.k5, scveh.r5, scveh.t5, scveh.l5, scveh.d5, scveh.k6, scveh.r6, scveh.t6, scveh.l6, scveh.d6, scveh.post_amount, scveh.too_old, scveh.bonus_v, scveh.macrs_pass, scveh.macrs_heavy, scveh.bonus, scveh.macrs, scveh.mq_q4, scveh.mq_total, scveh.cost179, scveh.bonus_o, scveh.macrs_o, scveh.s179_this_year_o, scveh.q4_basis, scveh.mq_q4_o, scveh.mq_q4_a2, scveh.mq_total_o, scveh.mq_total_a2, scveh.cost179_a2, scveh.no, scveh.is_actual_owned_test1, scveh.is_actual_leased_test1, scveh.is_actual_leased_test2

## Schedule D — securities sales and supplied distribution subtotals

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sd.no | — | — | — | — | — | — | — |
| sd.sold_other | — | — | — | — | — | — | — |
| sd.business_property | — | — | — | — | — | — | — |
| sd.business_property_if_sold | — | — | — | — | — | — | — |
| sd.installment | — | — | — | — | — | — | — |
| sd.installment_if_sold | — | — | — | — | — | — | — |
| sd.like_kind | — | — | — | — | — | — | — |
| sd.like_kind_if_sold | — | — | — | — | — | — | — |
| sd.sec1256 | — | — | — | — | — | — | — |
| sd.condemned | — | — | — | — | — | — | — |
| sd.small_business_stock | — | — | — | — | — | — | — |
| sd.trader_election | — | — | — | — | — | — | — |
| sd.f2439 | — | — | — | — | — | — | — |
| sd.f2439_if_dividends | — | — | — | — | — | — | — |
| sd.casualty | — | — | — | — | — | — | — |
| sd.qof | — | — | — | — | — | — | — |
| sd.other_forms | — | — | — | — | — | — | — |
| sd.route_each | — | — | — | — | — | — | — |
| sd.carryover | — | — | — | — | — | — | — |
| sd.distributions | — | — | — | — | — | — | — |
| sd.line18 | — | — | — | — | — | OpenTaxSolver: 736 compared (54 nonzero), 0 excluded | 3 |
| sd.line19 | — | — | — | — | — | OpenTaxSolver: 721 compared (72 nonzero), 15 excluded | 2 (stage16.sd.line17_no_skips_19, stage4.mut.sdtw_1250_line32_is_line1) |
| sd.filing4952 | — | — | — | — | — | — | — |
| sd.investment_election | — | — | — | — | — | — | — |
| sd.count | — | — | — | — | — | — | 26 |
| sd.screen | — | — | — | — | — | — | 5 |
| sd.filed | — | — | — | — | — | — | 26 |
| sd.zero | — | — | — | via sd.line4: 3; via sd.line5: 3; via sd.line11: 3; via sd.line12: 3 | — | — | — |
| sd.line1a.d | — | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line1a.e | — | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line1a.g | — | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line1a.h | — | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line1b.d | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 19 |
| sd.line1b.e | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 19 |
| sd.line1b.g | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (61 nonzero), 0 excluded | 19 |
| sd.line1b.h | 1 (sales.official.da.basis_worksheet) | — | — | 3 | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 22 |
| sd.line2.d | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 18 |
| sd.line2.e | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 18 |
| sd.line2.g | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (68 nonzero), 0 excluded | 18 |
| sd.line2.h | — | — | — | 3 | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 19 |
| sd.line3.d | — | — | — | 3 | — | — | 16 |
| sd.line3.e | — | — | — | 3 | — | — | 16 |
| sd.line3.g | — | — | — | 3 | — | — | 16 |
| sd.line3.h | 1 (sales.official.da.paid_in_crypto) | — | — | 3 | — | — | 17 |
| sd.line8a.d | 5 | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line8a.e | 4 | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line8a.g | 1 (sales.official.da.aggregate) | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line8a.h | 4 | — | — | 2 (classm.sd.2, classm.sd.3) | — | — | 15 |
| sd.line8b.d | 1 (sales.official.da.adjustment) | — | — | 3 | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 18 |
| sd.line8b.e | 1 (sales.official.da.adjustment) | — | — | 3 | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 18 |
| sd.line8b.g | 1 (sales.official.da.adjustment) | — | — | 3 | — | OpenTaxSolver: 1404 compared (60 nonzero), 0 excluded | 18 |
| sd.line8b.h | 2 (sales.official.da.aggregate, sales.official.da.adjustment) | — | — | 3 | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 19 |
| sd.line9.d | 1 (sales.official.da.not_reported) | — | — | 3 | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 18 |
| sd.line9.e | 1 (sales.official.da.not_reported) | — | — | 3 | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 18 |
| sd.line9.g | 1 (sales.official.da.not_reported) | — | — | 3 | — | OpenTaxSolver: 1404 compared (79 nonzero), 0 excluded | 18 |
| sd.line9.h | 1 (sales.official.da.not_reported) | — | — | 3 | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 19 |
| sd.line10.d | — | — | — | 4 | — | — | 16 |
| sd.line10.e | — | — | — | 4 | — | — | 16 |
| sd.line10.g | — | — | — | 4 | — | — | 16 |
| sd.line10.h | 1 (sales.official.da.swap) | — | — | 4 | — | — | 18 |
| sd.line4 | — | — | — | 6 | — | — | 2 (sales.refuse.forms, sd.reg.qof_held) |
| sd.line5 | — | — | — | 6 | — | — | 2 (sales.refuse.forms, sd.reg.qof_held) |
| sd.line6_ws | — | — | — | — | — | — | 1 (stage20.refuse.other_forms_with_carryover) |
| sd.line6 | — | — | — | 6 | — | OpenTaxSolver: 260 compared (187 nonzero), 0 excluded | 24 |
| sd.line11 | — | — | — | 6 | — | — | 2 (sales.refuse.forms, sd.reg.qof_held) |
| sd.line12 | — | — | — | 6 | — | — | 2 (sales.refuse.forms, sd.reg.qof_held) |
| sd.line14_ws | — | — | — | — | — | — | 1 (stage20.refuse.other_forms_with_carryover) |
| sd.line14 | — | — | — | 6; via u1250.line16: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | OpenTaxSolver: 260 compared (153 nonzero), 0 excluded | 10 |
| sd.line13 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (847 nonzero), 0 excluded | 6 |
| sd.line7 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (811 nonzero), 0 excluded; UsTaxes: 1400 compared (652 nonzero), 300 excluded | 14 |
| sd.line15 | 1 (sales.official.da.swap) | — | — | 6 | — | OpenTaxSolver: 1404 compared (1269 nonzero), 0 excluded; UsTaxes: 1400 compared (1041 nonzero), 300 excluded | 15 |
| sd.line16 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (1404 nonzero), 0 excluded; UsTaxes: 1400 compared (1152 nonzero), 300 excluded | 34 |
| sd.line17 | — | — | — | 3 | — | — | 2 (stage16.sd.line17_no_skips_18, stage16.sd.line17_no_skips_19) |
| sd.line20 | — | — | — | 2 (classm.sd.2.deepseek, classm.sd.3) | — | — | 2 (mexist.f4952.exception.filing_4952, mutation.t2.mfj_sdtw_skip23) |
| sd.loss_limit | — | — | — | — | — | — | — |
| sd.limited_loss | — | — | — | — | — | — | — |
| sd.has_loss | — | — | — | — | — | — | — |
| sd.line21 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (572 nonzero), 0 excluded; UsTaxes: 1400 compared (468 nonzero), 300 excluded | 28 |
| sd.line22 | — | — | — | 4 | — | — | 61 |
| sd.to1040 | — | — | — | via f1040.line7a: 6; via f8960.line5a → f1040.line7a: 3 | — | E via f1040.line7a (OpenTaxSolver, UsTaxes) | — |
| sd.net_gain_raw | — | — | — | — | — | — | 1 (sales.loss.single.700000) |
| sd.net_gain | — | — | — | — | — | — | — |
| sd.distributions_if_dividends | — | — | — | — | — | — | — |

Unasserted lines: sd.no, sd.business_property_if_sold, sd.installment_if_sold, sd.like_kind_if_sold, sd.f2439_if_dividends, sd.other_forms, sd.filing4952, sd.investment_election, sd.loss_limit, sd.limited_loss, sd.has_loss, sd.net_gain, sd.distributions_if_dividends

## Schedule D Tax Worksheet

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sdtw.zero | — | — | — | — | — | — | — |
| sdtw.ordinary_ceiling | — | — | — | — | — | — | — |
| sdtw.after22 | — | — | — | — | — | — | 1 (stage4.sdtw.skip22) |
| sdtw.after32 | — | — | — | — | — | — | 2 (stage4.sdtw.skip32, stage4.mut.sdtw_1250_line32_is_line1) |
| sdtw.use1250 | — | — | — | — | — | — | 2 (stage4.mut.sdtw_28pct_no_1250, stage4.mut.sdtw_1250_line32_is_line1) |
| sdtw.use28 | — | — | — | — | — | — | 1 (stage4.mut.sdtw_28pct_no_1250) |
| sdtw.line1 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line2 | — | — | — | 5 | — | OpenTaxSolver below rule: 83 compared (45 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line3 | — | — | — | 5 | — | OpenTaxSolver below rule: 73 compared (0 nonzero), 51 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line4 | — | — | — | 5 | — | OpenTaxSolver below rule: 73 compared (0 nonzero), 51 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line5 | — | — | — | 5 | — | OpenTaxSolver below rule: 83 compared (0 nonzero), 41 excluded | 2 (stage4.interest.election, stage4.sdtw.special_rates) |
| sdtw.line6 | — | — | — | 5 | — | OpenTaxSolver below rule: 83 compared (45 nonzero), 41 excluded | 3 |
| sdtw.line7 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line8 | — | — | — | 5 | — | OpenTaxSolver below rule: 83 compared (0 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line9 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line10 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line11 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line12 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.line12_takes_line9) |
| sdtw.line13 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line14 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (81 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line15 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line16 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (83 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line17 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (81 nonzero), 41 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| sdtw.line18 | — | — | — | 5 | — | OpenTaxSolver: 83 compared (81 nonzero), 41 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line19 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line20 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.line21 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.line22 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw23 | — | — | — | — | — | — | — |
| sdtw.line23 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (mutation.t2.mfj_sdtw_skip23, stage4.sdtw.special_rates) |
| sdtw.raw24 | — | — | — | — | — | — | — |
| sdtw.line24 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw25 | — | — | — | — | — | — | — |
| sdtw.line25 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (mutation.t2.hoh_no_s1a_parts, stage4.sdtw.special_rates) |
| sdtw.raw26 | — | — | — | — | — | — | — |
| sdtw.line26 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw27 | — | — | — | — | — | — | — |
| sdtw.line27 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw28 | — | — | — | — | — | — | — |
| sdtw.line28 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw29 | — | — | — | — | — | — | — |
| sdtw.line29 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw30 | — | — | — | — | — | — | — |
| sdtw.line30 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw31 | — | — | — | — | — | — | — |
| sdtw.line31 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 4 |
| sdtw.raw32 | — | — | — | — | — | — | — |
| sdtw.line32 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw33 | — | — | — | — | — | — | — |
| sdtw.line33 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 3 |
| sdtw.raw34 | — | — | — | — | — | — | — |
| sdtw.line34 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw35 | — | — | — | — | — | — | — |
| sdtw.line35 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (mutation.t2.qss_sdtw_sli, stage4.sdtw.special_rates) |
| sdtw.raw36 | — | — | — | — | — | — | — |
| sdtw.line36 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw37 | — | — | — | — | — | — | — |
| sdtw.line37 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw38 | — | — | — | — | — | — | — |
| sdtw.line38 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw39 | — | — | — | — | — | — | — |
| sdtw.line39 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw40 | — | — | — | — | — | — | — |
| sdtw.line40 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw41 | — | — | — | — | — | — | — |
| sdtw.show41_43 | — | — | — | — | — | — | 1 (sales.select.sdtw.election) |
| sdtw.line41 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (mutation.t2.mfs_sdtw_skip41, stage4.sdtw.special_rates) |
| sdtw.raw42 | — | — | — | — | — | — | — |
| sdtw.line42 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw43 | — | — | — | — | — | — | — |
| sdtw.line43 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 6 |
| sdtw.line44 | — | — | — | — | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 3 |
| sdtw.line45 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line46 | — | — | — | — | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line47 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |

Unasserted lines: sdtw.zero, sdtw.ordinary_ceiling, sdtw.raw23, sdtw.raw24, sdtw.raw25, sdtw.raw26, sdtw.raw27, sdtw.raw28, sdtw.raw29, sdtw.raw30, sdtw.raw31, sdtw.raw32, sdtw.raw33, sdtw.raw34, sdtw.raw35, sdtw.raw36, sdtw.raw37, sdtw.raw38, sdtw.raw39, sdtw.raw40, sdtw.raw41, sdtw.raw42, sdtw.raw43

## Student Loan Interest Deduction Worksheet—Schedule 1, Line 21

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sli.zero | — | — | — | — | — | — | — |
| sli.no | — | — | — | — | — | — | — |
| sli.any | — | — | — | — | — | — | — |
| sli.any_if_not_mfs | — | — | — | — | — | — | 1 (mfs.sli.not_asked) |
| sli.interest | — | — | — | — | — | — | — |
| sli.interest_if_any | — | — | — | — | — | — | — |
| sli.unqualified_any | — | — | — | — | — | — | — |
| sli.unqualified_any_if_any | — | — | — | — | — | — | — |
| sli.unqualified | — | — | — | — | — | — | — |
| sli.unqualified_if_some | — | — | — | — | — | — | — |
| sli.assisted_any | — | — | — | — | — | — | — |
| sli.assisted_any_if_any | — | — | — | — | — | — | — |
| sli.assisted | — | — | — | — | — | — | — |
| sli.assisted_if_some | — | — | — | — | — | — | — |
| sli.not_counted | — | — | — | — | — | — | — |
| sli.qualified | — | — | — | — | — | — | — |
| sli.has | — | — | — | — | — | — | — |
| sli.claimed_count | — | — | — | — | — | — | 2 (stage11.sli.none_claimed_joint, stage11.sli.spouse_claimed) |
| sli.max | — | — | — | — | — | — | — |
| sli.line1 | — | — | — | 4 | — | UsTaxes: 206 compared (206 nonzero), 0 excluded | 2 (mutation.m4.sli.part_unqualified, stage11.sli.cap) |
| sli.line2 | — | — | — | 5 | — | UsTaxes: 159 compared (159 nonzero), 47 excluded | — |
| sli.line3 | — | — | — | 5 | — | UsTaxes: 159 compared (72 nonzero), 47 excluded | 1 (stage11.sli.with_adjustments) |
| sli.line4 | — | — | — | 5 | — | UsTaxes: 159 compared (159 nonzero), 47 excluded | — |
| sli.base_other | — | — | — | — | — | — | — |
| sli.base_joint | — | — | — | — | — | — | — |
| sli.line5 | — | — | — | 5 | — | — | 6 |
| sli.over | — | — | — | — | — | — | 1 (stage14.sep.basic) |
| sli.line6 | — | — | — | 2 (classm.sli.2, classm.sli.3) | — | — | 5 |
| sli.divisor_other | — | — | — | — | — | — | — |
| sli.divisor_joint | — | — | — | — | — | — | — |
| sli.divisor | — | — | — | — | — | — | — |
| sli.line8_figured | — | — | — | — | — | — | — |
| sli.line8 | — | — | — | 4 | — | UsTaxes: 159 compared (65 nonzero), 47 excluded | 10 |
| sli.line9 | — | — | — | 4 | — | UsTaxes: 159 compared (94 nonzero), 47 excluded | 3 |
| sli.eligible | — | — | — | — | — | — | 2 (stage11.sli.none_claimed_joint, stage11.sli.spouse_claimed) |
| sli.allowed | — | — | — | — | — | — | — |
| sli.deduction | — | — | — | — | — | E via s1.line21 (OpenTaxSolver, UsTaxes) | 15 |

Unasserted lines: sli.zero, sli.no, sli.interest_if_any, sli.unqualified_any_if_any, sli.unqualified_if_some, sli.assisted_any_if_any, sli.assisted_if_some, sli.not_counted, sli.qualified, sli.has, sli.max, sli.base_other, sli.base_joint, sli.divisor_other, sli.divisor_joint, sli.divisor, sli.line8_figured, sli.allowed

## Social Security Benefits Worksheet—Lines 6a and 6b

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ssb.any | — | — | — | — | — | — | — |
| ssb.no | — | — | — | — | — | — | — |
| ssb.benefits | — | — | — | — | — | — | — |
| ssb.ira_covered | — | — | — | — | — | — | — |
| ssb.repaid_more | — | — | — | — | — | — | — |
| ssb.pub915 | — | — | — | — | — | — | — |
| ssb.prior_year_pay | — | — | — | — | — | — | — |
| ssb.lump_elect | — | — | — | — | — | — | — |
| ssb.lump_sum | — | — | — | — | — | — | — |
| ssb.terror_disability | — | — | — | — | — | — | — |
| ssb.lived_apart | — | — | — | — | — | — | — |
| ssb.benefits_if_any | — | — | — | via f1040.line6a → ssb.line1: 6 | — | E via ssb.line1 (OpenTaxSolver, UsTaxes) | — |
| ssb.line1 | — | — | — | 6 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.has_benefits | — | — | — | — | — | — | — |
| ssb.line2 | — | — | — | 6 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.line3 | — | — | — | 6 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 2 (stage16.ira.i10, stage11.ss.unemployment) |
| ssb.line4 | — | — | — | 6 | — | OpenTaxSolver below rule: 530 compared (0 nonzero), 20 excluded; UsTaxes below rule: 463 compared (0 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.line5 | — | — | — | 6 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 3 |
| ssb.ira_line20 | — | — | — | — | — | — | — |
| ssb.line6 | — | — | — | 6 | — | OpenTaxSolver: 530 compared (300 nonzero), 20 excluded; UsTaxes: 343 compared (160 nonzero), 120 excluded | 4 |
| ssb.line7 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 343 compared (343 nonzero), 120 excluded | 6 |
| ssb.base_single | — | — | — | — | — | — | — |
| ssb.base_joint | — | — | — | — | — | — | — |
| ssb.zero | — | — | — | — | — | — | — |
| ssb.mfs_base | — | — | — | — | — | — | — |
| ssb.lines8_to_15 | — | — | — | — | — | — | — |
| ssb.line8 | — | — | — | 4 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 343 compared (343 nonzero), 120 excluded | 6 |
| ssb.line9 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded | 4 |
| ssb.past7 | — | — | — | — | — | — | 2 (stage10.ss.stop_line9, stage10.ss.stop_line7) |
| ssb.past9 | — | — | — | — | — | — | 1 (stage10.ss.stop_line9) |
| ssb.show8_9 | — | — | — | — | — | — | 4 |
| ssb.show10_15 | — | — | — | — | — | — | 4 |
| ssb.show16_18 | — | — | — | — | — | — | 4 |
| ssb.adjust_single | — | — | — | — | — | — | — |
| ssb.adjust_joint | — | — | — | — | — | — | — |
| ssb.mfs_adjust | — | — | — | — | — | — | — |
| ssb.line10 | — | — | — | 3 | — | OpenTaxSolver: 477 compared (477 nonzero), 17 excluded; UsTaxes: 343 compared (343 nonzero), 120 excluded | 2 (mutation.t2.ssb.mfs_apart_taxable, mutation.t2.ssb.mfs_together_skip) |
| ssb.line11 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (451 nonzero), 20 excluded; UsTaxes: 343 compared (284 nonzero), 120 excluded | 1 (mutation.t2.ssb.mfs_apart_taxable) |
| ssb.line12 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded | 1 (mutation.t2.ssb.mfs_apart_taxable) |
| ssb.line13 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded | 2 (mutation.t2.ssb.mfs_apart_taxable, stage10.ss.middle) |
| ssb.line14 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded | 2 (mutation.t2.ssb.mfs_apart_taxable, stage10.ss.small_benefits) |
| ssb.line15 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (451 nonzero), 20 excluded; UsTaxes: 343 compared (284 nonzero), 120 excluded | 2 (mutation.t2.ssb.mfs_apart_taxable, stage10.ss.middle) |
| ssb.mfs_together | — | — | — | — | — | — | — |
| ssb.line16_sum | — | — | — | — | — | — | — |
| ssb.line16_together | — | — | — | — | — | — | — |
| ssb.line16 | — | — | — | 4 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded | 5 |
| ssb.line17 | — | — | — | 4 | — | OpenTaxSolver: 477 compared (477 nonzero), 17 excluded; UsTaxes: 343 compared (343 nonzero), 120 excluded | 1 (mutation.t2.ssb.mfs_apart_taxable) |
| ssb.line18_figured | — | — | — | — | — | — | — |
| ssb.line18 | — | — | — | 4; via f1040.line6b: 6 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 343 compared (304 nonzero), 120 excluded; E via f1040.line6b (PE, TC, OpenTaxSolver, UsTaxes) | 3 |

Unasserted lines: ssb.no, ssb.pub915, ssb.lump_sum, ssb.lived_apart, ssb.has_benefits, ssb.ira_line20, ssb.base_single, ssb.base_joint, ssb.zero, ssb.mfs_base, ssb.lines8_to_15, ssb.adjust_single, ssb.adjust_joint, ssb.mfs_adjust, ssb.mfs_together, ssb.line16_sum, ssb.line16_together, ssb.line18_figured

## Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tipjob.one | — | — | — | — | — | — | — |
| tipjob.no | — | — | — | — | — | — | — |
| tipjob.zero | — | — | — | — | — | — | — |
| tipjob.listed | — | — | — | — | — | — | — |
| tipjob.other_work | — | — | — | — | — | — | — |
| tipjob.other_work_if_listed | — | — | — | — | — | — | — |
| tipjob.charged | — | — | — | — | — | — | — |
| tipjob.charged_if_listed | — | — | — | — | — | — | — |
| tipjob.unlawful | — | — | — | — | — | — | — |
| tipjob.unlawful_if_listed | — | — | — | — | — | — | — |
| tipjob.tips | — | — | — | — | — | — | — |
| tipjob.amount | — | — | — | 1 (classm.tipjob.1) | — | — | 2 (mutation.m4.tipjob.service_charge, mutation.m4.tipjob.unlawful_work) |
| tipjob.mixed | — | — | — | — | — | — | — |
| tipjob.col_c | — | — | — | — | — | — | — |
| tipjob.col_d | — | — | — | 1 (classm.tipjob.1) | — | — | — |

Unasserted lines: tipjob.one, tipjob.no, tipjob.zero, tipjob.other_work_if_listed, tipjob.charged_if_listed, tipjob.unlawful_if_listed, tipjob.mixed, tipjob.col_c

## Unrecaptured Section 1250 Gain Worksheet — distribution-only path

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| u1250.reached | — | — | — | — | — | — | — |
| u1250.line1 | — | — | — | — | — | — | — |
| u1250.line2 | — | — | — | — | — | — | — |
| u1250.line3 | — | — | — | — | — | — | — |
| u1250.line4 | — | — | — | — | — | — | — |
| u1250.line5 | — | — | — | — | — | — | — |
| u1250.line6 | — | — | — | — | — | — | — |
| u1250.line7 | — | — | — | — | — | — | — |
| u1250.line8 | — | — | — | — | — | — | — |
| u1250.line9 | — | — | — | — | — | — | — |
| u1250.line10 | — | — | — | 4 | — | — | — |
| u1250.line12 | — | — | — | 4 | — | — | — |
| u1250.line16 | — | — | — | 4 | — | — | — |
| u1250.line11 | — | — | — | 4 | — | — | — |
| u1250.line13 | — | — | — | 4 | — | — | — |
| u1250.line14 | — | — | — | 4 | — | — | — |
| u1250.line15 | — | — | — | 4 | — | — | — |
| u1250.combined | — | — | — | — | — | — | — |
| u1250.line17 | — | — | — | 4 | — | — | 1 (stage4.feeders.shortloss) |
| u1250.line18 | — | — | — | 4 | — | — | 2 (stage16.sd.line17_no_skips_19, stage4.feeders.shortloss) |

Unasserted lines: u1250.reached, u1250.line1, u1250.line2, u1250.line3, u1250.line4, u1250.line5, u1250.line6, u1250.line7, u1250.line8, u1250.line9, u1250.combined

## Form W-2 — wage, withholding and Social Security boxes by employer

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| w2.box1 | — | — | — | — | — | — | — |
| w2.box2 | — | — | — | — | — | — | — |
| w2.box3 | — | — | — | — | — | — | — |
| w2.box7 | — | — | — | — | — | — | — |
| w2.box4 | — | — | — | — | — | — | — |
| w2.wages | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.one | — | — | — | — | — | — | — |
| w2.over | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.box5 | — | — | — | — | — | — | — |
| w2.box6 | — | — | — | — | — | — | — |
| w2.box10 | — | — | — | — | — | — | — |
| w2.has_box10 | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.box10_wages | — | — | — | — | — | — | — |
| w2.box10_bad | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.dc_net | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | 1 (stage15.refuse.w2.box10_bad) |
| w2.dc_benefits | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.dc_zero | — | — | — | — | — | — | — |
| w2.box12_any | — | — | — | — | — | — | — |
| w2.box12_userra | — | — | — | — | — | — | — |
| w2.box12_d | — | — | — | — | — | — | — |
| w2.box12_e | — | — | — | — | — | — | — |
| w2.box12_f | — | — | — | — | — | — | — |
| w2.box12_g | — | — | — | — | — | — | — |
| w2.box12_h | — | — | — | — | — | — | — |
| w2.box12_s | — | — | — | — | — | — | — |
| w2.box12_aa | — | — | — | — | — | — | — |
| w2.box12_bb | — | — | — | — | — | — | — |
| w2.box12_ee | — | — | — | — | — | — | — |
| w2.has_g | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.g_governmental | — | — | — | — | — | — | — |
| w2.g_elective | — | — | — | — | — | — | — |
| w2.g_bad | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | 1 (stage15.mut.w2_g_elective_no_code_g) |
| w2.g_gov_part | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | 1 (stage15.refuse.w2.g_bad) |
| w2.g_counted | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.zero | — | — | — | — | — | — | — |
| w2.code_h | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
| w2.sav_listed | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | 2 (stage15.refuse.w2.userra, stage15.refuse.w2.code_h) |
| w2.sav_deferral | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |

Unasserted lines: w2.one, w2.dc_zero, w2.zero

## Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inst | — | — | — | — | — | — | — |
| mat | — | — | — | — | — | — | — |
| adj | — | — | — | — | — | — | — |
| ws1_aoc | — | — | — | — | — | — | — |
| ws4_aoc | — | — | — | — | — | — | — |
| ws4_llc | — | — | — | — | — | — | — |
| cap | — | — | — | — | — | — | — |
| band | — | — | — | — | — | — | — |
| rate25 | — | — | — | — | — | — | — |
| zero | — | — | — | — | — | — | — |
| line27 | — | — | — | — | — | — | — |
| line28 | — | — | — | — | — | — | — |
| line29 | — | — | — | — | — | — | — |
| line29_plus | — | — | — | — | — | — | — |
| line28_zero | — | — | — | — | — | — | — |
| line30 | — | — | — | — | — | — | — |

Unasserted lines: ws1_aoc, ws4_aoc, ws4_llc, cap, band, rate25, zero, line27, line28, line29, line29_plus, line28_zero, line30

## New York City tax rate schedule

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| single.b1.excess | — | — | — | — | — | — | — |
| single.b1.product | — | — | — | — | — | — | — |
| single.b1.base | — | — | — | — | — | — | — |
| single.b1.tax | — | — | — | — | — | — | — |
| single.b2.excess | — | — | — | — | — | — | — |
| single.b2.product | — | — | — | — | — | — | — |
| single.b2.base | — | — | — | — | — | — | — |
| single.b2.tax | — | — | — | — | — | — | — |
| single.b3.excess | — | — | — | — | — | — | — |
| single.b3.product | — | — | — | — | — | — | — |
| single.b3.base | — | — | — | — | — | — | — |
| single.b3.tax | — | — | — | — | — | — | — |
| single.b4.excess | — | — | — | — | — | — | — |
| single.b4.product | — | — | — | — | — | — | — |
| single.b4.base | — | — | — | — | — | — | — |
| single.b4.tax | — | — | — | — | — | — | — |
| single.result | — | — | — | — | — | — | — |
| mfj.b1.excess | — | — | — | — | — | — | — |
| mfj.b1.product | — | — | — | — | — | — | — |
| mfj.b1.base | — | — | — | — | — | — | — |
| mfj.b1.tax | — | — | — | — | — | — | — |
| mfj.b2.excess | — | — | — | — | — | — | — |
| mfj.b2.product | — | — | — | — | — | — | — |
| mfj.b2.base | — | — | — | — | — | — | — |
| mfj.b2.tax | — | — | — | — | — | — | — |
| mfj.b3.excess | — | — | — | — | — | — | — |
| mfj.b3.product | — | — | — | — | — | — | — |
| mfj.b3.base | — | — | — | — | — | — | — |
| mfj.b3.tax | — | — | — | — | — | — | — |
| mfj.b4.excess | — | — | — | — | — | — | — |
| mfj.b4.product | — | — | — | — | — | — | — |
| mfj.b4.base | — | — | — | — | — | — | — |
| mfj.b4.tax | — | — | — | — | — | — | — |
| mfj.result | — | — | — | — | — | — | — |
| hoh.b1.excess | — | — | — | — | — | — | — |
| hoh.b1.product | — | — | — | — | — | — | — |
| hoh.b1.base | — | — | — | — | — | — | — |
| hoh.b1.tax | — | — | — | — | — | — | — |
| hoh.b2.excess | — | — | — | — | — | — | — |
| hoh.b2.product | — | — | — | — | — | — | — |
| hoh.b2.base | — | — | — | — | — | — | — |
| hoh.b2.tax | — | — | — | — | — | — | — |
| hoh.b3.excess | — | — | — | — | — | — | — |
| hoh.b3.product | — | — | — | — | — | — | — |
| hoh.b3.base | — | — | — | — | — | — | — |
| hoh.b3.tax | — | — | — | — | — | — | — |
| hoh.b4.excess | — | — | — | — | — | — | — |
| hoh.b4.product | — | — | — | — | — | — | — |
| hoh.b4.base | — | — | — | — | — | — | — |
| hoh.b4.tax | — | — | — | — | — | — | — |
| hoh.result | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: single.b1.excess, single.b1.product, single.b1.base, single.b1.tax, single.b2.excess, single.b2.product, single.b2.base, single.b2.tax, single.b3.excess, single.b3.product, single.b3.base, single.b3.tax, single.b4.excess, single.b4.product, single.b4.base, single.b4.tax, single.result, mfj.b1.excess, mfj.b1.product, mfj.b1.base, mfj.b1.tax, mfj.b2.excess, mfj.b2.product, mfj.b2.base, mfj.b2.tax, mfj.b3.excess, mfj.b3.product, mfj.b3.base, mfj.b3.tax, mfj.b4.excess, mfj.b4.product, mfj.b4.base, mfj.b4.tax, mfj.result, hoh.b1.excess, hoh.b1.product, hoh.b1.base, hoh.b1.tax, hoh.b2.excess, hoh.b2.product, hoh.b2.base, hoh.b2.tax, hoh.b3.excess, hoh.b3.product, hoh.b3.base, hoh.b3.tax, hoh.b4.excess, hoh.b4.product, hoh.b4.base, hoh.b4.tax, hoh.result, tax

## New York State tax rate schedule

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| single.b1.excess | — | — | — | — | — | — | — |
| single.b1.product | — | — | — | — | — | — | — |
| single.b1.base | — | — | — | — | — | — | — |
| single.b1.tax | — | — | — | — | — | — | — |
| single.b2.excess | — | — | — | — | — | — | — |
| single.b2.product | — | — | — | — | — | — | — |
| single.b2.base | — | — | — | — | — | — | — |
| single.b2.tax | — | — | — | — | — | — | — |
| single.b3.excess | — | — | — | — | — | — | — |
| single.b3.product | — | — | — | — | — | — | — |
| single.b3.base | — | — | — | — | — | — | — |
| single.b3.tax | — | — | — | — | — | — | — |
| single.b4.excess | — | — | — | — | — | — | — |
| single.b4.product | — | — | — | — | — | — | — |
| single.b4.base | — | — | — | — | — | — | — |
| single.b4.tax | — | — | — | — | — | — | — |
| single.b5.excess | — | — | — | — | — | — | — |
| single.b5.product | — | — | — | — | — | — | — |
| single.b5.base | — | — | — | — | — | — | — |
| single.b5.tax | — | — | — | — | — | — | — |
| single.b6.excess | — | — | — | — | — | — | — |
| single.b6.product | — | — | — | — | — | — | — |
| single.b6.base | — | — | — | — | — | — | — |
| single.b6.tax | — | — | — | — | — | — | — |
| single.b7.excess | — | — | — | — | — | — | — |
| single.b7.product | — | — | — | — | — | — | — |
| single.b7.base | — | — | — | — | — | — | — |
| single.b7.tax | — | — | — | — | — | — | — |
| single.b8.excess | — | — | — | — | — | — | — |
| single.b8.product | — | — | — | — | — | — | — |
| single.b8.base | — | — | — | — | — | — | — |
| single.b8.tax | — | — | — | — | — | — | — |
| single.b9.excess | — | — | — | — | — | — | — |
| single.b9.product | — | — | — | — | — | — | — |
| single.b9.base | — | — | — | — | — | — | — |
| single.b9.tax | — | — | — | — | — | — | — |
| single.result | — | — | — | — | — | — | — |
| mfj.b1.excess | — | — | — | — | — | — | — |
| mfj.b1.product | — | — | — | — | — | — | — |
| mfj.b1.base | — | — | — | — | — | — | — |
| mfj.b1.tax | — | — | — | — | — | — | — |
| mfj.b2.excess | — | — | — | — | — | — | — |
| mfj.b2.product | — | — | — | — | — | — | — |
| mfj.b2.base | — | — | — | — | — | — | — |
| mfj.b2.tax | — | — | — | — | — | — | — |
| mfj.b3.excess | — | — | — | — | — | — | — |
| mfj.b3.product | — | — | — | — | — | — | — |
| mfj.b3.base | — | — | — | — | — | — | — |
| mfj.b3.tax | — | — | — | — | — | — | — |
| mfj.b4.excess | — | — | — | — | — | — | — |
| mfj.b4.product | — | — | — | — | — | — | — |
| mfj.b4.base | — | — | — | — | — | — | — |
| mfj.b4.tax | — | — | — | — | — | — | — |
| mfj.b5.excess | — | — | — | — | — | — | — |
| mfj.b5.product | — | — | — | — | — | — | — |
| mfj.b5.base | — | — | — | — | — | — | — |
| mfj.b5.tax | — | — | — | — | — | — | — |
| mfj.b6.excess | — | — | — | — | — | — | — |
| mfj.b6.product | — | — | — | — | — | — | — |
| mfj.b6.base | — | — | — | — | — | — | — |
| mfj.b6.tax | — | — | — | — | — | — | — |
| mfj.b7.excess | — | — | — | — | — | — | — |
| mfj.b7.product | — | — | — | — | — | — | — |
| mfj.b7.base | — | — | — | — | — | — | — |
| mfj.b7.tax | — | — | — | — | — | — | — |
| mfj.b8.excess | — | — | — | — | — | — | — |
| mfj.b8.product | — | — | — | — | — | — | — |
| mfj.b8.base | — | — | — | — | — | — | — |
| mfj.b8.tax | — | — | — | — | — | — | — |
| mfj.b9.excess | — | — | — | — | — | — | — |
| mfj.b9.product | — | — | — | — | — | — | — |
| mfj.b9.base | — | — | — | — | — | — | — |
| mfj.b9.tax | — | — | — | — | — | — | — |
| mfj.result | — | — | — | — | — | — | — |
| hoh.b1.excess | — | — | — | — | — | — | — |
| hoh.b1.product | — | — | — | — | — | — | — |
| hoh.b1.base | — | — | — | — | — | — | — |
| hoh.b1.tax | — | — | — | — | — | — | — |
| hoh.b2.excess | — | — | — | — | — | — | — |
| hoh.b2.product | — | — | — | — | — | — | — |
| hoh.b2.base | — | — | — | — | — | — | — |
| hoh.b2.tax | — | — | — | — | — | — | — |
| hoh.b3.excess | — | — | — | — | — | — | — |
| hoh.b3.product | — | — | — | — | — | — | — |
| hoh.b3.base | — | — | — | — | — | — | — |
| hoh.b3.tax | — | — | — | — | — | — | — |
| hoh.b4.excess | — | — | — | — | — | — | — |
| hoh.b4.product | — | — | — | — | — | — | — |
| hoh.b4.base | — | — | — | — | — | — | — |
| hoh.b4.tax | — | — | — | — | — | — | — |
| hoh.b5.excess | — | — | — | — | — | — | — |
| hoh.b5.product | — | — | — | — | — | — | — |
| hoh.b5.base | — | — | — | — | — | — | — |
| hoh.b5.tax | — | — | — | — | — | — | — |
| hoh.b6.excess | — | — | — | — | — | — | — |
| hoh.b6.product | — | — | — | — | — | — | — |
| hoh.b6.base | — | — | — | — | — | — | — |
| hoh.b6.tax | — | — | — | — | — | — | — |
| hoh.b7.excess | — | — | — | — | — | — | — |
| hoh.b7.product | — | — | — | — | — | — | — |
| hoh.b7.base | — | — | — | — | — | — | — |
| hoh.b7.tax | — | — | — | — | — | — | — |
| hoh.b8.excess | — | — | — | — | — | — | — |
| hoh.b8.product | — | — | — | — | — | — | — |
| hoh.b8.base | — | — | — | — | — | — | — |
| hoh.b8.tax | — | — | — | — | — | — | — |
| hoh.b9.excess | — | — | — | — | — | — | — |
| hoh.b9.product | — | — | — | — | — | — | — |
| hoh.b9.base | — | — | — | — | — | — | — |
| hoh.b9.tax | — | — | — | — | — | — | — |
| hoh.result | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: single.b1.excess, single.b1.product, single.b1.base, single.b1.tax, single.b2.excess, single.b2.product, single.b2.base, single.b2.tax, single.b3.excess, single.b3.product, single.b3.base, single.b3.tax, single.b4.excess, single.b4.product, single.b4.base, single.b4.tax, single.b5.excess, single.b5.product, single.b5.base, single.b5.tax, single.b6.excess, single.b6.product, single.b6.base, single.b6.tax, single.b7.excess, single.b7.product, single.b7.base, single.b7.tax, single.b8.excess, single.b8.product, single.b8.base, single.b8.tax, single.b9.excess, single.b9.product, single.b9.base, single.b9.tax, single.result, mfj.b1.excess, mfj.b1.product, mfj.b1.base, mfj.b1.tax, mfj.b2.excess, mfj.b2.product, mfj.b2.base, mfj.b2.tax, mfj.b3.excess, mfj.b3.product, mfj.b3.base, mfj.b3.tax, mfj.b4.excess, mfj.b4.product, mfj.b4.base, mfj.b4.tax, mfj.b5.excess, mfj.b5.product, mfj.b5.base, mfj.b5.tax, mfj.b6.excess, mfj.b6.product, mfj.b6.base, mfj.b6.tax, mfj.b7.excess, mfj.b7.product, mfj.b7.base, mfj.b7.tax, mfj.b8.excess, mfj.b8.product, mfj.b8.base, mfj.b8.tax, mfj.b9.excess, mfj.b9.product, mfj.b9.base, mfj.b9.tax, mfj.result, hoh.b1.excess, hoh.b1.product, hoh.b1.base, hoh.b1.tax, hoh.b2.excess, hoh.b2.product, hoh.b2.base, hoh.b2.tax, hoh.b3.excess, hoh.b3.product, hoh.b3.base, hoh.b3.tax, hoh.b4.excess, hoh.b4.product, hoh.b4.base, hoh.b4.tax, hoh.b5.excess, hoh.b5.product, hoh.b5.base, hoh.b5.tax, hoh.b6.excess, hoh.b6.product, hoh.b6.base, hoh.b6.tax, hoh.b7.excess, hoh.b7.product, hoh.b7.base, hoh.b7.tax, hoh.b8.excess, hoh.b8.product, hoh.b8.base, hoh.b8.tax, hoh.b9.excess, hoh.b9.product, hoh.b9.base, hoh.b9.tax, hoh.result, tax

## Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| agi | — | — | — | — | — | — | — |
| ti | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| start | — | — | — | — | — | — | — |
| line3 | — | — | — | — | — | — | — |
| recapture | — | — | — | — | — | — | — |
| incremental | — | — | — | — | — | — | — |
| line6 | — | — | — | — | — | — | — |
| phase | — | — | — | — | — | — | — |
| line7 | — | — | — | — | — | — | — |
| hundred | — | — | — | — | — | — | — |
| line9_scaled | — | — | — | — | — | — | — |
| line9_exact | — | — | — | — | — | — | — |
| line9 | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: line3, line6, phase, line7, hundred, line9_scaled, line9_exact, line9, tax

## Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| agi | — | — | — | — | — | — | — |
| ti | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| rate | — | — | — | — | — | — | — |
| line3 | — | — | — | — | — | — | — |
| stop | — | — | — | — | — | — | — |
| line4 | — | — | — | — | — | — | — |
| line5 | — | — | — | — | — | — | — |
| line6 | — | — | — | — | — | — | — |
| hundred | — | — | — | — | — | — | — |
| line8_scaled | — | — | — | — | — | — | — |
| line8_exact | — | — | — | — | — | — | — |
| line8 | — | — | — | — | — | — | — |
| line9_phased | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: line3, stop, line4, line5, line6, hundred, line8_scaled, line8_exact, line8, line9_phased, tax

## Schedule SE (Form 1040) — Self-Employment Tax, one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| line2 | — | — | — | — | — | — | — |
| line8a | — | — | — | — | — | — | — |
| line8b | — | — | — | — | — | — | — |
| line8c | — | — | — | — | — | — | — |
| zero | — | — | — | — | — | — | — |
| line3 | — | — | — | — | — | — | — |
| positive | — | — | — | — | — | — | — |
| rate9235 | — | — | — | — | — | — | — |
| line3pos | — | — | — | — | — | — | — |
| line4a_pos | — | — | — | — | — | — | — |
| line4a | — | — | — | — | — | — | — |
| line4b | — | — | — | — | — | — | — |
| line4c_sum | — | — | — | — | — | — | — |
| floor | — | — | — | — | — | — | — |
| owes | — | — | — | — | — | — | — |
| line4c_owes | — | — | — | — | — | — | — |
| line4c | — | — | — | — | — | — | — |
| line5b | — | — | — | — | — | — | — |
| line6 | — | — | — | — | — | — | — |
| line7 | — | — | — | — | — | — | — |
| line8d | — | — | — | — | — | — | — |
| line9 | — | — | — | — | — | — | — |
| ss_base | — | — | — | — | — | — | — |
| rate124 | — | — | — | — | — | — | — |
| line10 | — | — | — | — | — | — | — |
| rate029 | — | — | — | — | — | — | — |
| line11 | — | — | — | — | — | — | — |
| line12 | — | — | — | — | — | — | — |
| rate50 | — | — | — | — | — | — | — |
| line13 | — | — | — | — | — | — | — |

Unasserted lines: zero, line3, positive, rate9235, line3pos, line4a_pos, line4a, line4b, line4c_sum, floor, owes, line4c_owes, line4c, line5b, line6, line7, line8d, line9, ss_base, rate124, line10, rate029, line11, line12, rate50, line13

## Tax on an amount — Tax Table or Tax Computation Worksheet

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| below_boundary | — | — | — | — | — | — | — |
| table_tax | — | — | — | — | — | — | — |
| worksheet_tax | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: below_boundary, table_tax, worksheet_tax, tax

## Tax Computation Worksheet—Line 16

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | — | — | — | — | — | — | — |
| status | — | — | — | — | — | — | — |
| single.row1.product | — | — | — | — | — | — | — |
| single.row1.tax | — | — | — | — | — | — | — |
| single.row2.product | — | — | — | — | — | — | — |
| single.row2.tax | — | — | — | — | — | — | — |
| single.row3.product | — | — | — | — | — | — | — |
| single.row3.tax | — | — | — | — | — | — | — |
| single.row4.product | — | — | — | — | — | — | — |
| single.row4.tax | — | — | — | — | — | — | — |
| single.row5.product | — | — | — | — | — | — | — |
| single.row5.tax | — | — | — | — | — | — | — |
| single.result | — | — | — | — | — | — | — |
| mfj.row1.product | — | — | — | — | — | — | — |
| mfj.row1.tax | — | — | — | — | — | — | — |
| mfj.row2.product | — | — | — | — | — | — | — |
| mfj.row2.tax | — | — | — | — | — | — | — |
| mfj.row3.product | — | — | — | — | — | — | — |
| mfj.row3.tax | — | — | — | — | — | — | — |
| mfj.row4.product | — | — | — | — | — | — | — |
| mfj.row4.tax | — | — | — | — | — | — | — |
| mfj.row5.product | — | — | — | — | — | — | — |
| mfj.row5.tax | — | — | — | — | — | — | — |
| mfj.result | — | — | — | — | — | — | — |
| mfs.row1.product | — | — | — | — | — | — | — |
| mfs.row1.tax | — | — | — | — | — | — | — |
| mfs.row2.product | — | — | — | — | — | — | — |
| mfs.row2.tax | — | — | — | — | — | — | — |
| mfs.row3.product | — | — | — | — | — | — | — |
| mfs.row3.tax | — | — | — | — | — | — | — |
| mfs.row4.product | — | — | — | — | — | — | — |
| mfs.row4.tax | — | — | — | — | — | — | — |
| mfs.row5.product | — | — | — | — | — | — | — |
| mfs.row5.tax | — | — | — | — | — | — | — |
| mfs.result | — | — | — | — | — | — | — |
| hoh.row1.product | — | — | — | — | — | — | — |
| hoh.row1.tax | — | — | — | — | — | — | — |
| hoh.row2.product | — | — | — | — | — | — | — |
| hoh.row2.tax | — | — | — | — | — | — | — |
| hoh.row3.product | — | — | — | — | — | — | — |
| hoh.row3.tax | — | — | — | — | — | — | — |
| hoh.row4.product | — | — | — | — | — | — | — |
| hoh.row4.tax | — | — | — | — | — | — | — |
| hoh.row5.product | — | — | — | — | — | — | — |
| hoh.row5.tax | — | — | — | — | — | — | — |
| hoh.result | — | — | — | — | — | — | — |
| tax | — | — | — | — | — | — | — |

Unasserted lines: single.row1.product, single.row1.tax, single.row2.product, single.row2.tax, single.row3.product, single.row3.tax, single.row4.product, single.row4.tax, single.row5.product, single.row5.tax, single.result, mfj.row1.product, mfj.row1.tax, mfj.row2.product, mfj.row2.tax, mfj.row3.product, mfj.row3.tax, mfj.row4.product, mfj.row4.tax, mfj.row5.product, mfj.row5.tax, mfj.result, mfs.row1.product, mfs.row1.tax, mfs.row2.product, mfs.row2.tax, mfs.row3.product, mfs.row3.tax, mfs.row4.product, mfs.row4.tax, mfs.row5.product, mfs.row5.tax, mfs.result, hoh.row1.product, hoh.row1.tax, hoh.row2.product, hoh.row2.tax, hoh.row3.product, hoh.row3.tax, hoh.row4.product, hoh.row4.tax, hoh.row5.product, hoh.row5.tax, hoh.result, tax

Unasserted computed lines across all documents: 2700. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)

Input lines never supplied by any fixture: ny_it2.state_withheld, ny_it2.yonkers_withheld, ny_it2.city_withheld, ny_it201.ask.state_resident, ny_it201.ask.city_resident, ny_it201.ask.special_accrual, ny_it201.ask.yonkers, ny_it201.ask.active_duty, ny_it201.ask.moved_in, ny_it201.ask.moved_out, ny_it201.ask.bab, ny_it201.ask.abroad, ny_it201.ask.installment, ny_it201.ask.decedent, ny_it201.ask.item_c, ny_it201.ask.inflation_check, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.it225, ny_it201.ask.gov_pension, ny_it201.ask.us_obligation_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.529_owner, ny_it201.ask.itemize, ny_it201.ask.resident_credit, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.city_credits, ny_it201.ask.mctmt, ny_it201.ask.owes_use_tax, ny_it201.ask.use_tax_st141, ny_it201.ask.contributions, ny_it201.ask.dependent_care, ny_it201.ask.noncustodial, ny_it201.ask.real_property_credit, ny_it201.ask.college_tuition, ny_it201.ask.other_withholding, ny_it201.ask.refund_529, ny_it201.ask.late_penalty, ny_it201.ask.prior_agi_high, ny_it201.ask.abode_part_year, ny_it201.ask.prior_full_year, ny_it201.ask.est_late, ny_it201.ask.spouse_resident, ny_it201.ask.prior_year_tax, ny_it201.ask.public_job, ny_it201.ask.ny_529, ny_it201.ask.gov_pension_other, ny_it201.ask.spouse_itemizes, ny_it201.ask.use_tax_exact, ny_it201.ask.est_any, ny_it201.line75_amount, ny_it201.ask.apply_any, ny_it201.line79_amount.
Asserted keys not matching a line id: dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line27, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line29, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28_zero, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line30, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line27, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line29, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28_zero, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line30, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line3, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.positive, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line4a, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line4b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.owes, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line4c, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line5b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line6, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line7, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line8d, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line9, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line10, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line11, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line12, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"}.line13, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax