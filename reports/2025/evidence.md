# Evidence coverage per line

**Scoreboard.** Share of computed lines with at least one outside-family assertion: 554 of 1908 (29.0%). H (human source reading): 0, B (human worked values): 0, second-family M: 435, E: 216.

A computed line is one whose atom is not `input`, `param` or `copy`. An outside-family assertion is a signed human source reading (H), a class B fixture (human worked values), a class M fixture whose recorded model is not a Claude model (second-family M), or an engine assertion (E) under the rule below. The sub-counts overlap: a line with several kinds counts once in the share. H checks the encoded rule against IRS text; B and M check worked values. Second-family transcription and render readings are reported separately in second_family.md and do not yet enter this scoreboard. Class A, Claude-family M, C and R do not move it.

H — a MATCH verdict and a reason in the reader's own words, with a current per-line receipt covering the displayed reading, folded helpers, dependencies and sources. The log's exact contents must have been committed by its named reader. A guided question credits only its own computation. Other packets credit their printed line and helpers actually expanded in the reading; referenced amounts do not receive credit. See the linked human logs for the scope of each reading. H supplies no hand-calculated expected value and never fills the B column.

Optional human readings pending or ineligible (no H credit; original findings retained): f1040: f1040.line12e: the reading or a dependency changed; fresh reading required for H credit; person: person.age65: the reading or a dependency changed; fresh reading required for H credit; sa: sa.standardbase: the reading or a dependency changed; fresh reading required for H credit; sa: sa.extra: the reading or a dependency changed; fresh reading required for H credit; sa: sa.extra: the recorded reading differs from the packet; sa: sa.extra: MISMATCH; no H credit; finding retained for investigation; sa: sa.boxes_age65: the reading or a dependency changed; fresh reading required for H credit; sa: sa.boxes_blind: the reading or a dependency changed; fresh reading required for H credit; sa: sa.extra_age65: the reading or a dependency changed; fresh reading required for H credit; sa: sa.extra_age65: the recorded reading differs from the packet; sa: sa.extra_age65: MISMATCH; no H credit; finding retained for investigation; sa: sa.extra_blind: the reading or a dependency changed; fresh reading required for H credit; sa: sa.extra_blind: the recorded reading differs from the packet; sa: sa.extra_blind: MISMATCH; no H credit; finding retained for investigation; sa: sa.standardraw: the reading or a dependency changed; fresh reading required for H credit; sa: sa.standardraw: the recorded reading differs from the packet; sa: sa.standardraw: UNCLEAR; no H credit; finding retained for investigation; sa: sa.mfs: the reading or a dependency changed; fresh reading required for H credit; sa: sa.mfs_spouse_itemizes: the reading or a dependency changed; fresh reading required for H credit; sa: sa.standard: the reading or a dependency changed; fresh reading required for H credit; sa: sa.itemizes: the reading or a dependency changed; fresh reading required for H credit; sa: sa.deduction: the reading or a dependency changed; fresh reading required for H credit.

Fixtures that assert each line, by evidence class, as a count of cases (ids listed when two or fewer). A — official IRS worked example, cited. B — human hand-work recorded with the worker and the document revision; none yet. C — a named, versioned calculator or engine record in fixtures/2025/differential/ (spec 6.1); none yet. M — isolated model hand-work with the model, prompt hash and snapshot recorded (fixtures/2025/classm.json, reviews/2025/classm/); second-family M fixtures are those whose recorded model does not start with "claude". E — the engine differential (tools/engines; reports/2025/engine_differential.md and .json): PolicyEngine-US (PE), Tax-Calculator (TC), OpenTaxSolver, UsTaxes run over 1700 generated returns. A line gets an E assertion only when, for at least one engine, the engine computes the line rather than taking it whole as an input, the project value was nonzero on at least 50 compared returns, and fewer than half of the nonzero returns the engine reached (compared plus excluded) were excluded under an engine limitation; the cell prints each engine's compared, nonzero and excluded counts, and an engine that falls short of the rule is marked "below rule" and asserts nothing. R — recorded regression from the project's own evaluator, no class claimed; agreement with the Lean reference evaluator (reports/2025/evaluator_agreement.md) is evaluator agreement over the same data, not an independent engine, and earns no class.

An outside-family assertion (B, second-family M or E) on a line whose atom is `copy` also credits the first line along its copy chain whose atom is not `copy`, because a copy's value equals its source's exactly, so agreement on the copy is agreement on the source; the table marks each such credit "via <copy line>" (the chain walked, when longer than one copy), the copy line keeps its own cell, and the sub-counts above include credited lines. In this report 470 assertions are credited through copies (B cases: 0; second-family M cases: 424; engine-line assertions: 46); 4 assertions on 2 copy lines could not be resolved statically and stay on the copy line only (qdcg.line22, qdcg.line24).

Engine ids with no line of their own (never an E assertion): f1040.tax_before_credits (PE), f1040.tax_before_credits (TC), f1040.tax_before_credits (OpenTaxSolver), f1040.tax_before_credits (UsTaxes). Mapped lines taken whole from the generator's facts: none. Components of compared lines that enter the engine as generator facts rather than the engine's own form arithmetic (the line still counts as engine-computed; the component does not): PolicyEngine-US f1040.line10: the HSA deduction (Form 8889 line 13) enters as the generator's health_savings_account_ald; the engine computes the educator, half-of-self-employment-tax, IRA and student loan interest components and the sum; Tax-Calculator f1040.line10: the HSA deduction (e03290), the educator expenses deduction (e03220) and the IRA contributions (e03150) enter as the generator's amounts; the engine computes the half-of-self-employment-tax component and the sum (returns with student loan interest, or an IRA deduction phased out by modified AGI, are excluded); Tax-Calculator f1040.line20: the foreign tax paid (e07300) is a supplied amount; the engine computes the credit limit; Tax-Calculator f1040.line19: the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; the engine subtracts them in Credit Limit Worksheet A; Tax-Calculator f1040.line24: the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; the engine applies the tax limit; returns with a saver's credit are excluded; OpenTaxSolver person[taxpayer].f8889[hsa].line12: Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; the program does not compute the line 3 limitation chart; it computes lines 5 to 13; OpenTaxSolver person[taxpayer].f8889[hsa].line13: Form 8889 line 3 (the contribution limit) is supplied as $4,300 or $8,550 from the coverage facts and line 7 as $1,000 for age 55; the program computes lines 5 to 13; OpenTaxSolver f1040.line10: Schedule 1 line 11 (educator expenses after the $300 limit) and line 20 (the IRA deduction) enter as the generator's amounts; lines 13 and 15 come from the engine's own Form 8889 and Schedule SE runs; line 21 is the engine's student loan worksheet; OpenTaxSolver f1040.line20: Schedule 3 line 1 (the foreign tax credit) is the smaller of the creditable foreign tax and the engine's own line 16, figured by the adapter; OpenTaxSolver f8960.line17: Form 8960 line 13 (modified AGI) and line 5a (net gain) are the engine's own Form 1040 lines 11a and 7a; line 9a is the investment interest when the engine itemized; lines 8, 11, 12 and 15 to 17 are the program's; OpenTaxSolver f8995.line15: Form 8995 line 12 (net capital gain plus qualified dividends) is figured from the facts; line 1 column (c) is the program's own Schedule C line 31 less Schedule 1 lines 15 to 17 from its Form 1040 output; line 11 is its Form 1040 lines 11a less 12 less 13b; OpenTaxSolver s8812.line14: Schedule 8812 line 13 (Credit Limit Worksheet A) is the engine's own Form 1040 line 18 less Schedule 3 lines 1 and 2, figured by the adapter; OpenTaxSolver s8812.line27: Schedule 8812 line 18a (earned income) is the engine's own Form 1040 line 1z plus Schedule SE line 3 (profit or loss) less line 13, not below zero, and line 13 the adapter's Credit Limit Worksheet A; lines 21 (boxes 4 and 6), 22 (Schedule 1 line 15) and 24 (zero: no EIC, no excess social security) are supplied; OpenTaxSolver f2441.line11: Form 2441 line 4 (earned income) is the engine's own Form 1040 line 1z less the spouse's wages, plus its Schedule SE lines 3 less 13 by file import; line 10 is its own Form 1040 line 18 less Schedule 3 line 1; OpenTaxSolver sd.line19: Schedule D line 19 is supplied as Form 1099-DIV box 2b; the program takes the Unrecaptured Section 1250 Gain Worksheet result as an input; OpenTaxSolver f8959.line18: Form 8959 line 8 (self-employment income) is the engine's own Schedule SE line 6; UsTaxes f1040.line10: Schedule 1 line 19a (UsTaxes' slot for the IRA deduction, `otherIncome.iraDeduction`) enters as the generator's contributions and the educator expenses as paid (the engine applies the $300 limit); lines 13 and 21 are the engine's own Form 8889 and student loan interest worksheet; UsTaxes s1.line26: Schedule 1 line 19a (the IRA deduction) enters as the generator's contributions; the engine computes the other adjustments and the sum; UsTaxes f1040.line20: Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid; returns where the tax limits it are excluded; UsTaxes f1040.line24: Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid, and Form 5695 Part II as the generator's credit; returns with either limited, or with any Schedule 3 credit, are excluded after the credits; UsTaxes sd.line16: the sales enter as Form 8949 rows (UsTaxes' Asset list, all on boxes C and F); the engine computes the gains, the wash-sale adjustments and Schedule D's totals.

## Form 4562 — one item of depreciable property (other than a vehicle) of a business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| asset.zero | — | — | — | — | — | — | — |
| asset.class | — | — | — | — | — | — | — |
| asset.period | — | — | — | 4 | — | — | — |
| asset.outside | — | — | — | 4 | — | — | — |
| asset.screen | — | — | — | — | — | — | — |
| asset.screened | — | — | — | 4 | — | — | — |
| asset.placed | — | — | — | — | — | — | — |
| asset.cost | — | — | — | — | — | — | 1 (stage14.asset.refuse_class) |
| asset.pct | — | — | — | — | — | — | — |
| asset.cent | — | — | — | — | — | — | — |
| asset.hundred | — | — | — | — | — | — | — |
| asset.pct_c | — | — | — | — | — | — | — |
| asset.pct_bad | — | — | — | 4 | — | — | — |
| asset.listed | — | — | — | — | — | — | — |
| asset.half | — | — | — | — | — | — | — |
| asset.over_half | — | — | — | 4 | — | — | — |
| asset.listed_low | — | — | — | 4 | — | — | — |
| asset.basis | — | — | — | 4 | — | — | 3 |
| asset.is2025 | — | — | — | 4 | — | — | — |
| asset.on_19 | — | — | — | 4 | — | — | — |
| asset.on_17 | — | — | — | 4 | — | — | — |
| asset.on_26_2025 | — | — | — | 4 | — | — | — |
| asset.year | — | — | — | 4 | — | — | — |
| asset.last | — | — | — | 4 | — | — | — |
| asset.done | — | — | — | 4 | — | — | — |
| asset.quarter | — | — | — | — | — | — | — |
| asset.qconv | — | — | — | 4 | — | — | — |
| asset.s179 | — | — | — | — | — | — | — |
| asset.s179_bad | — | — | — | 4 | — | — | — |
| asset.after179 | — | — | — | 4 | — | — | 3 |
| asset.after_jan19 | — | — | — | — | — | — | — |
| asset.bonus_choice | — | — | — | — | — | — | — |
| asset.bonus_same | — | — | — | — | — | — | — |
| asset.bonus_mixed | — | — | — | 4 | — | — | — |
| asset.rate40 | — | — | — | — | — | — | — |
| asset.bonus_full | — | — | — | 3 | — | — | 1 (stage14.asset.refuse_bonus_mixed) |
| asset.bonus_forty | — | — | — | 3 | — | — | 1 (stage14.asset.refuse_bonus_mixed_forty) |
| asset.bonus_fullcase | — | — | — | 3 | — | — | — |
| asset.bonus | — | — | — | 3 | — | — | 4 |
| asset.f25 | — | — | — | 1 (classm.asset.2) | — | — | 2 (stage14.asset.listed_and_not, stage14.asset.listed_forty) |
| asset.f26i | — | — | — | 1 (classm.asset.2) | — | — | 1 (stage14.asset.listed_and_not) |
| asset.ub | — | — | — | 4 | — | — | — |
| asset.col19c | — | — | — | 3 | — | — | 1 (stage14.asset.listed_and_not) |
| asset.hy | — | — | — | — | — | — | — |
| asset.rate_hy | — | — | — | 3 | — | — | — |
| asset.rate_mq | — | — | — | 3 | — | — | — |
| asset.macrs_hy | — | — | — | 3 | — | — | — |
| asset.macrs_mq | — | — | — | 3 | — | — | — |
| asset.macrs2025 | — | — | — | 3 | — | — | 13 |
| asset.mqbase | — | — | — | 4 | — | — | — |
| asset.mq_q4_2025 | — | — | — | 4 | — | — | — |
| asset.prior_conv | — | — | — | — | — | — | — |
| asset.prior_179 | — | — | — | — | — | — | — |
| asset.prior_bonus | — | — | — | — | — | — | — |
| asset.ub_prior_a | — | — | — | 4 | — | — | 1 (stage14.asset.prior_179_full) |
| asset.ub_prior | — | — | — | 4 | — | — | 1 (stage14.asset.prior_179_bonus) |
| asset.rate_prior | — | — | — | 4 | — | — | — |
| asset.macrs_prior_live | — | — | — | 4 | — | — | — |
| asset.macrs_prior | — | — | — | 2 (classm.asset.1, classm.asset.4) | — | — | 7 |
| asset.dep_2025 | — | — | — | 4 | — | — | — |
| asset.bonus_2025 | — | — | — | 4 | — | — | — |
| asset.s179_2025 | — | — | — | 4 | — | — | — |
| asset.mq_q4 | — | — | — | 4 | — | — | — |
| asset.mq_total | — | — | — | 4 | — | — | — |
| asset.cost179 | — | — | — | 4 | — | — | — |
| asset.cost179_2025 | — | — | — | 3 | — | — | — |
| asset.dep_prior | — | — | — | 4 | — | — | — |
| asset.dep_listed | — | — | — | 1 (classm.asset.2) | — | — | 2 (stage14.asset.listed_prior, stage14.asset.listed_forty) |

Unasserted lines: asset.zero, asset.cent, asset.hundred, asset.pct_c, asset.half, asset.rate40, asset.hy

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
| clcw.bad | — | — | — | — | — | — | 3 |
| clcw.applies | — | — | — | — | — | — | 2 (stage20.line21_small_loss, stage20.line21_at_floor) |
| clcw.show_st | — | — | — | — | — | — | — |
| clcw.show_lt | — | — | — | — | — | — | — |
| clcw.line1 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (238 nonzero), 0 excluded | 12 |
| clcw.line2 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (238 nonzero), 0 excluded | 18 |
| clcw.combined | — | — | — | — | — | — | — |
| clcw.line3 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (170 nonzero), 0 excluded | 11 |
| clcw.line4 | — | — | — | 6 | — | OpenTaxSolver: 238 compared (170 nonzero), 0 excluded | 11 |
| clcw.st_loss | — | — | — | — | — | — | — |
| clcw.lt_loss | — | — | — | — | — | — | — |
| clcw.line5 | — | — | — | 6 | — | OpenTaxSolver: 196 compared (196 nonzero), 0 excluded | 11 |
| clcw.line6 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (85 nonzero), 0 excluded | 5 |
| clcw.line7 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (167 nonzero), 0 excluded | 7 |
| clcw.line8 | — | — | — | 5 | — | OpenTaxSolver: 196 compared (187 nonzero), 0 excluded | 10 |
| clcw.line9 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (153 nonzero), 0 excluded | 5 |
| clcw.line10 | — | — | — | 4 | — | OpenTaxSolver below rule: 153 compared (42 nonzero), 0 excluded | 5 |
| clcw.line11 | — | — | — | 4 | — | OpenTaxSolver below rule: 153 compared (31 nonzero), 0 excluded | 5 |
| clcw.line12 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (51 nonzero), 0 excluded | 5 |
| clcw.line13 | — | — | — | 4 | — | OpenTaxSolver: 153 compared (153 nonzero), 0 excluded | 6 |
| clcw.figures_notice | — | — | — | — | — | — | — |

Unasserted lines: clcw.zero, clcw.prior_16, clcw.prior_loss, clcw.prior_limit, clcw.prior_limit_mfs, clcw.prior_floor, clcw.show_st, clcw.show_lt, clcw.combined, clcw.st_loss, clcw.lt_loss, clcw.figures_notice

## Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clcw26.zero | — | — | — | — | — | — | — |
| clcw26.show | — | — | — | — | — | — | — |
| clcw26.show_st | — | — | — | — | — | — | — |
| clcw26.show_lt | — | — | — | — | — | — | — |
| clcw26.line1 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line2 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.combined | — | — | — | — | — | — | — |
| clcw26.line3 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line4 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line5 | — | — | — | 7 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line6 | — | — | — | 3 | — | — | — |
| clcw26.line7 | — | — | — | 3 | — | — | — |
| clcw26.line8 | — | — | — | 3 | — | — | 12 |
| clcw26.line9 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line10 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line11 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line12 | — | — | — | 4 | — | — | 1 (stage20.mut.to2026_short_gain_long_loss) |
| clcw26.line13 | — | — | — | 4 | — | — | 12 |
| clcw26.decedent_notice | — | — | — | — | — | — | — |

Unasserted lines: clcw26.zero, clcw26.show, clcw26.show_st, clcw26.show_lt, clcw26.combined, clcw26.decedent_notice

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
| dependent.other_claimant | — | — | — | — | — | — | — |
| dependent.divorced_rule | — | — | — | — | — | — | — |
| dependent.multiple_support | — | — | — | — | — | — | — |
| dependent.parent_home_paid | — | — | — | — | — | — | — |
| dependent.born_died | — | — | — | — | — | — | — |
| dependent.placed | — | — | — | — | — | — | — |
| dependent.part_year_home | — | — | — | — | — | — | — |
| dependent.hoh_lived_half | — | — | — | — | — | — | — |
| dependent.dc_lived_half | — | — | — | — | — | — | — |
| dependent.one | — | — | — | — | — | — | — |
| dependent.zero | — | — | — | — | — | — | — |
| dependent.qc_relationship | — | — | — | — | — | — | 21 |
| dependent.younger | — | — | — | — | — | — | 18 |
| dependent.us_half | — | — | — | — | — | — | — |
| dependent.eic_ssn | — | — | — | — | — | — | — |
| dependent.qc_age | — | — | — | — | — | — | 18 |
| dependent.lived_half | — | — | — | — | — | — | 19 |
| dependent.qualifying_child | — | — | — | — | — | — | 24 |
| dependent.resident | — | — | — | — | — | — | 19 |
| dependent.qc_dependent | — | — | — | — | — | — | 25 |
| dependent.qr_relationship | — | — | — | — | — | — | 6 |
| dependent.lawful | — | — | — | — | — | — | — |
| dependent.qr_income | — | — | — | — | — | — | 6 |
| dependent.income_exception | — | — | — | — | — | — | 7 |
| dependent.qualifying_relative | — | — | — | — | — | — | 8 |
| dependent.qr_dependent | — | — | — | — | — | — | 9 |
| dependent.claimed_no_tin | — | — | — | — | — | — | 3 |
| dependent.claimed | — | — | — | — | — | — | 30 |
| dependent.under_ctc_age | — | — | — | — | — | — | 15 |
| dependent.ctc_child | — | — | — | — | — | — | 26 |
| dependent.odc_person | — | — | — | — | — | — | 25 |
| dependent.ctc_per_child | — | — | — | — | — | — | — |
| dependent.ctc_amount | — | — | — | — | — | — | 24 |
| dependent.odc_per_dependent | — | — | — | — | — | — | — |
| dependent.odc_amount | — | — | — | — | — | — | 25 |
| dependent.actc_per_child | — | — | — | — | — | — | — |
| dependent.actc_amount | — | — | — | — | — | — | 24 |
| dependent.hoh_test2 | — | — | — | — | — | — | 28 |
| dependent.hoh_test1 | — | — | — | — | — | — | 26 |
| dependent.eic_child | — | — | — | — | — | — | — |
| dependent.eic_ssn_child | — | — | — | — | — | — | — |
| dependent.dc_child_all_year | — | — | — | — | — | — | — |
| dependent.dc_age13 | — | — | — | — | — | — | — |
| dependent.dc_under13 | — | — | — | — | — | — | — |
| dependent.dc_child | — | — | — | — | — | — | — |
| dependent.dc_incapable | — | — | — | — | — | — | — |
| dependent.dc_disabled_qp | — | — | — | — | — | — | — |
| dependent.dc_qp | — | — | — | — | — | — | 2 (stage15.f2441.parent_died_part_year, stage15.refuse.dependent.dc_no_tin) |
| dependent.dc_count | — | — | — | — | — | — | — |
| dependent.dc_paid | — | — | — | via dependent.dc_line2d: 7 | — | — | — |
| dependent.dc_line2d | — | — | — | 14 | — | — | — |
| dependent.dc_over12_care | — | — | — | — | — | — | — |
| dependent.dc_line2c | — | — | — | 14 | — | — | 2 (stage15.BUG-0111.care_before_13, stage15.BUG-0111.care_after_13) |
| dependent.ptc_files | — | — | — | — | — | — | — |
| dependent.ptc_magi | — | — | — | — | — | — | — |
| dependent.ptc_magi_counted | — | — | — | — | — | — | — |
| dependent.edu | — | — | — | — | — | — | — |
| dependent.edu_1098t | — | — | — | — | — | — | — |
| dependent.edu_student | — | — | — | — | — | — | — |
| dependent.edu_inst | — | — | — | — | — | — | — |
| dependent.edu_mat | — | — | — | — | — | — | — |
| dependent.edu_a2025 | — | — | — | — | — | — | — |
| dependent.edu_a2026 | — | — | — | — | — | — | — |
| dependent.edu_refunds | — | — | — | — | — | — | — |
| dependent.edu_adj_sum | — | — | — | — | — | — | — |
| dependent.edu_adj | — | — | — | — | — | — | — |
| dependent.edu_over | — | — | — | — | — | — | — |
| dependent.edu_over_refused | — | — | — | — | — | — | — |
| dependent.edu_line23 | — | — | — | — | — | — | 4 |
| dependent.edu_show24 | — | — | — | — | — | — | — |
| dependent.edu_line24 | — | — | — | — | — | — | 3 |
| dependent.edu_show25 | — | — | — | — | — | — | — |
| dependent.edu_line25 | — | — | — | — | — | — | 3 |
| dependent.edu_show26 | — | — | — | — | — | — | — |
| dependent.edu_line26 | — | — | — | — | — | — | 2 (stage19.blind.e2, stage19.blind.e4) |
| dependent.edu_ein | — | — | — | — | — | — | — |
| dependent.edu_aoc | — | — | — | — | — | — | — |
| dependent.edu_llc | — | — | — | — | — | — | — |
| dependent.edu_line27 | 4 | — | — | — | — | — | 3 |
| dependent.edu_line28 | — | — | — | — | — | — | 3 |
| dependent.edu_line29 | — | — | — | — | — | — | 3 |
| dependent.edu_line30 | 3 | — | — | — | — | — | 3 |
| dependent.edu_line31 | — | — | — | — | — | — | 3 |

Unasserted lines: dependent.hoh_lived_half, dependent.dc_lived_half, dependent.one, dependent.zero, dependent.ctc_per_child, dependent.odc_per_dependent, dependent.actc_per_child, dependent.eic_child, dependent.eic_ssn_child, dependent.dc_child_all_year, dependent.dc_age13, dependent.dc_child, dependent.dc_disabled_qp, dependent.dc_count, dependent.ptc_magi_counted, dependent.edu_student, dependent.edu_adj_sum, dependent.edu_adj, dependent.edu_over_refused, dependent.edu_show24, dependent.edu_show25, dependent.edu_show26, dependent.edu_aoc, dependent.edu_llc

## Form 1099-DIV — distribution components and scope screening

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| div.box2b | — | — | — | via u1250.line11: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | — | — |
| div.box2c | — | — | — | — | — | — | — |
| div.box2d | — | — | — | via g28.line4: 1 (classm.g28.2.deepseek) | — | — | — |
| div.box2e | — | — | — | — | — | — | — |
| div.box2f | — | — | — | — | — | — | — |
| div.box3 | — | — | — | — | — | — | — |
| div.box9 | — | — | — | — | — | — | — |
| div.box10 | — | — | — | — | — | — | — |
| div.box12 | — | — | — | — | — | — | — |
| div.box13 | — | — | — | — | — | — | — |
| div.basis_reconciled | — | — | — | — | — | — | — |
| div.box1a | — | — | — | — | — | — | — |
| div.box1b | — | — | — | — | — | — | — |
| div.box2a | — | — | — | — | — | — | — |
| div.box5 | — | — | — | — | — | — | — |
| div.section1202 | — | — | — | — | — | — | — |
| div.amt | — | — | — | — | — | — | — |
| div.unsupported | — | — | — | — | — | — | — |
| div.bad_special | — | — | — | — | — | — | — |
| div.screen | — | — | — | via u1250.line10: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek); via u1250.line12: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | — | — |
| div.bad_components | — | — | — | — | — | — | — |
| div.special_total | — | — | — | — | — | — | — |

Unasserted lines: div.box1a, div.box1b, div.box2a, div.box5, div.section1202, div.amt, div.unsupported, div.bad_special, div.bad_components, div.special_total

## Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eic.qc_of_another | — | — | — | — | — | — | — |
| eic.age_range_count | — | — | — | — | — | — | — |
| eic.age_range | — | — | — | — | — | — | 1 (stage13.eic_spouse_in_age_range) |
| eic.us_home | — | — | — | — | — | — | — |
| eic.zero | — | — | — | via eic.step5_line2: 5; via eic.step5_line4: 5 | — | — | — |
| eic.qc_count | — | — | — | — | — | — | — |
| eic.ssn_count | — | — | — | — | — | — | 3 |
| eic.has_qc | — | — | — | — | — | — | 2 (stage9.eic.child_without_ssn, stage9.eic.parent_not_qualifying_child) |
| eic.married_rules | — | — | — | — | — | — | — |
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
| eic.limit | — | — | — | — | — | — | — |
| eic.step1_income | — | — | — | — | — | — | — |
| eic.step1_ssn | — | — | — | — | — | — | 2 (audit.eic.filer_eic_ssn_without_work_ssn, audit.eic.filer_without_eic_ssn) |
| eic.step1_foreign | — | — | — | — | — | — | — |
| eic.step1_resident | — | — | — | — | — | — | — |
| eic.gain_7a | — | — | — | — | — | — | 1 (stage9.eic.capital_gain_in_investment_income) |
| eic.investment_income | — | — | — | — | — | — | — |
| eic.step2_income | — | — | — | — | — | — | 3 |
| eic.step2_other | — | — | — | — | — | — | — |
| eic.same_home | — | — | — | — | — | — | — |
| eic.legally_separated | — | — | — | — | — | — | — |
| eic.step3_married | — | — | — | — | — | — | 3 |
| eic.step3 | — | — | — | — | — | — | — |
| eic.step4 | — | — | — | — | — | — | 2 (stage9.eic.no_child.over65, stage9.eic.no_child.born_jan1_1961) |
| eic.step34 | — | — | — | — | — | — | — |
| eic.reached_step5 | — | — | — | — | — | — | 1 (stage9.eic.wsb_not_reached) |
| eic.step5_line1 | — | — | — | 8 | — | — | 1 (stage9.eic.refuse.clergy_schedule1.step5) |
| eic.step5_line2 | — | — | — | 8 | — | — | 1 (stage9.eic.refuse.other_income) |
| eic.step5_line3 | — | — | — | 8 | — | — | — |
| eic.step5_line4 | — | — | — | 8 | — | — | 1 (stage9.eic.refuse.other_income) |
| eic.earned_income | — | — | — | 8 | — | PE: 1400 compared (1400 nonzero), 300 excluded; TC: 1400 compared (1400 nonzero), 300 excluded | 1 (stage9.eic.no_schedule_c.earned_over_limit) |
| eic.sc_count | — | — | — | — | — | — | — |
| eic.self_employed | — | — | — | — | — | — | — |
| eic.wsb_se | — | — | — | — | — | — | — |
| eic.show_wsb4b | — | — | — | — | — | — | 1 (stage9.eic.wsb_not_reached) |
| eic.wsb_4b | — | — | — | 2 (classm.eic.3.deepseek, classm.eic.3) | — | — | 7 |
| eic.show_wsb6 | — | — | — | — | — | — | 2 (stage14.eic.wsb_line5_stop_27c, stage9.eic.wsb_not_reached) |
| eic.wsb_6 | — | — | — | 2 (classm.eic.3.deepseek, classm.eic.3) | — | — | 1 (stage14.eic.wsb_stop_27c) |
| eic.earned_for_limit | — | — | — | — | — | — | — |
| eic.step5_income | — | — | — | — | — | — | — |
| eic.eligible | — | — | — | — | — | — | 21 |
| eic.line1 | — | — | — | 10 | — | PE: 1700 compared (1699 nonzero), 0 excluded; TC: 1700 compared (1699 nonzero), 0 excluded | 6 |
| eic.line1_in_table | — | — | — | — | — | — | — |
| eic.line1_table0 | — | — | — | — | — | — | — |
| eic.line1_table1 | — | — | — | — | — | — | — |
| eic.line1_table2 | — | — | — | — | — | — | — |
| eic.line1_table3 | — | — | — | — | — | — | — |
| eic.line1_table | — | — | — | — | — | — | — |
| eic.line2 | — | — | — | 10 | — | — | 14 |
| eic.show3 | — | — | — | — | — | — | 1 (stage9.eic.no_earned_income) |
| eic.line3 | — | — | — | 8 | — | — | — |
| eic.line4 | — | — | — | 8 | — | — | 5 |
| eic.threshold_other | — | — | — | — | — | — | — |
| eic.threshold_joint | — | — | — | — | — | — | — |
| eic.line5_threshold | — | — | — | — | — | — | — |
| eic.threshold0_other | — | — | — | — | — | — | — |
| eic.threshold1_other | — | — | — | — | — | — | — |
| eic.threshold0_joint | — | — | — | — | — | — | — |
| eic.threshold1_joint | — | — | — | — | — | — | — |
| eic.line5_blank | — | — | — | — | — | — | 1 (stage9.eic.one_child.at_line5_amount) |
| eic.line3_table0 | — | — | — | — | — | — | — |
| eic.line3_table1 | — | — | — | — | — | — | — |
| eic.line3_table2 | — | — | — | — | — | — | — |
| eic.line3_table3 | — | — | — | — | — | — | — |
| eic.show5 | — | — | — | — | — | — | 1 (stage9.eic.line5_skipped) |
| eic.line5 | — | — | — | 2 (classm.eic.8.deepseek, classm.eic.8) | — | — | 3 |
| eic.smaller | — | — | — | — | — | — | — |
| eic.after_line4 | — | — | — | — | — | — | — |
| eic.line6 | — | — | — | 11 | — | — | 9 |
| eic.credit | — | — | — | via f1040.line27a: 6 | — | E via f1040.line27a (PE, TC) | 3 |
| eic.reached_step3 | — | — | — | — | — | — | — |
| eic.check_27c | — | — | — | via f1040.line27c: 6 | — | — | 2 (stage14.eic.wsb_stop_27c, stage14.eic.wsb_line5_stop_27c) |
| eic.wsb_4b_positive | — | — | — | — | — | — | — |
| eic.wsb_line5_stop | — | — | — | — | — | — | 1 (stage14.eic.wsb_line5_stop_27c) |
| eic.separated_box | — | — | — | via f1040.separated_spouses: 6 | — | — | — |
| eic.clergy | — | — | — | via f1040.line27b: 6 | — | — | — |

Unasserted lines: eic.age_range_count, eic.qc_count, eic.married_rules, eic.top_limit, eic.below_top, eic.limit0_other, eic.limit1_other, eic.limit2_other, eic.limit3_other, eic.limit0_joint, eic.limit1_joint, eic.limit2_joint, eic.limit3_joint, eic.limit_other, eic.limit_joint, eic.limit, eic.step1_income, eic.step1_foreign, eic.step1_resident, eic.investment_income, eic.step2_other, eic.step3, eic.step34, eic.sc_count, eic.self_employed, eic.wsb_se, eic.earned_for_limit, eic.step5_income, eic.line1_in_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line1_table, eic.threshold_other, eic.threshold_joint, eic.line5_threshold, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.smaller, eic.after_line4, eic.reached_step3, eic.wsb_4b_positive

## Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.status | 1 (example.official) | — | — | — | — | — | 58 |
| f1040.line1a | — | — | — | 12 | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 25 |
| f1040.line1e | — | — | — | 12 | — | — | 16 |
| f1040.line1z | — | — | — | 12; via eic.step5_line1: 5 | — | OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 31 |
| f1040.tax_exempt_interest | — | — | — | — | — | — | — |
| f1040.line2a | — | — | — | 12 | — | — | 1 (stage10.ss.exempt_interest_dividends) |
| f1040.line2b | — | — | — | 12 | — | — | 5 |
| f1040.line3b | — | — | — | 12 | — | — | 3 |
| f1040.line3a | 1 (example.official) | — | — | via f4952.line4b: 4 | — | E via qdcg.line2 (OpenTaxSolver) | 61 |
| f1040.line4a | — | — | — | 12 | — | — | 7 |
| f1040.line4b | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 12 | — | — | 19 |
| f1040.ira_rollovers | — | — | — | — | — | — | — |
| f1040.line4c_rollover | — | — | — | 12 | — | — | 6 |
| f1040.line5a | — | — | — | 12 | — | — | 14 |
| f1040.line5b | — | — | — | 12 | — | — | 29 |
| f1040.plan_rollovers | — | — | — | — | — | — | — |
| f1040.line5c_rollover | — | — | — | 12 | — | — | 5 |
| f1040.line6a | — | — | — | 12 | — | — | 2 (stage10.ss.top, stage16.ira.i10) |
| f1040.line6b | — | — | — | 12 | — | PE: 1666 compared (477 nonzero), 19 excluded; TC: 1370 compared (418 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (477 nonzero), 111 excluded; UsTaxes: 1153 compared (300 nonzero), 547 excluded | 17 |
| f1040.line6c | — | — | — | 12 | — | — | 1 (stage10.refuse.lump_sum) |
| f1040.line6d | — | — | — | 12 | — | — | 2 (stage10.ss.mfs_together, stage10.ss.mfs_apart) |
| f1040.line7a | 1 (example.official) | — | — | 12 | — | OpenTaxSolver: 1700 compared (1404 nonzero), 0 excluded; UsTaxes: 1400 compared (1152 nonzero), 300 excluded | 134 |
| f1040.line8 | — | — | — | 12 | — | OpenTaxSolver: 1700 compared (576 nonzero), 0 excluded; UsTaxes below rule: 1400 compared (280 nonzero), 300 excluded | 52 |
| f1040.line9 | — | — | — | 12 | — | OpenTaxSolver: 1589 compared (1589 nonzero), 111 excluded; UsTaxes: 1153 compared (1153 nonzero), 547 excluded; E via sli.line2 (UsTaxes) | 32 |
| f1040.line10 | — | — | — | 12 | — | PE: 1640 compared (975 nonzero), 19 excluded; TC: 1370 compared (771 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (955 nonzero), 111 excluded; UsTaxes: 1153 compared (587 nonzero), 547 excluded | 41 |
| f1040.line11a | — | — | — | 12; via eic.line3 → f1040.line11b: 4; via f1040.line11b: 6; via f2441.line7: 3; via f8863.line3 → f1040.line11b: 4; via f8863.line14 → f1040.line11b: 1 (classm.f8863.2.deepseek); via f8880.line8: 1 (classm.f8880.2.deepseek); via f8960.line13 → sa.agi → f1040.line11b: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via s8812.line1: 4 | — | UsTaxes: 1153 compared (1153 nonzero), 547 excluded; E via f1040.line11b (PE, TC, OpenTaxSolver, UsTaxes); E via f2441.line7 (OpenTaxSolver) | 164 |
| f1040.line11b | 8 | — | — | 12 | — | PE: 1640 compared (1640 nonzero), 19 excluded; TC: 1370 compared (1370 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (1589 nonzero), 111 excluded; UsTaxes: 1153 compared (1153 nonzero), 547 excluded | 40 |
| f1040.line12e | — | — | — | 12 | — | OpenTaxSolver: 1476 compared (1476 nonzero), 224 excluded; UsTaxes: 1057 compared (1057 nonzero), 643 excluded | 65 |
| f1040.line13a | — | — | — | 12 | — | PE: 1490 compared (380 nonzero), 139 excluded; TC below rule: 1039 compared (135 nonzero), 643 excluded; OpenTaxSolver: 387 compared (329 nonzero), 130 excluded; UsTaxes below rule: 819 compared (0 nonzero), 881 excluded | 7 |
| f1040.line13b | — | — | — | 12 | — | PE: 1536 compared (514 nonzero), 143 excluded; TC: 1370 compared (492 nonzero), 330 excluded; OpenTaxSolver: 1437 compared (447 nonzero), 263 excluded; UsTaxes below rule: 819 compared (244 nonzero), 881 excluded | 13 |
| f1040.line14 | — | — | — | 12 | — | OpenTaxSolver: 1235 compared (1235 nonzero), 465 excluded; UsTaxes: 819 compared (819 nonzero), 881 excluded | 22 |
| f1040.line15 | 3 | — | — | 12 | — | PE: 1384 compared (1227 nonzero), 256 excluded; TC: 902 compared (902 nonzero), 798 excluded; OpenTaxSolver: 1235 compared (1096 nonzero), 465 excluded; UsTaxes: 819 compared (727 nonzero), 881 excluded; E via qdcg.line1 (OpenTaxSolver, UsTaxes); E via sdtw.line1 (OpenTaxSolver) | 159 |
| f1040.gate.qdcg_applies | 1 (example.official) | — | — | — | — | — | 65 |
| f1040.gate.sdtw | — | — | — | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| f1040.line16 | 8 | — | — | 12 | — | PE: 1342 compared (1164 nonzero), 298 excluded; TC: 911 compared (788 nonzero), 772 excluded; OpenTaxSolver: 1075 compared (929 nonzero), 625 excluded; UsTaxes below rule: 717 compared (622 nonzero), 983 excluded | 163 |
| f1040.line17 | — | — | — | 12 | — | OpenTaxSolver below rule: 1462 compared (0 nonzero), 238 excluded; UsTaxes below rule: 682 compared (17 nonzero), 1018 excluded | 5 |
| f1040.line18 | — | — | — | 12; via f2441.clw1: 3; via f8863.clw4: 3; via f8880.clw1: 1 (classm.f8880.2.deepseek); via s8812.clw_a1: 3 | — | OpenTaxSolver: 993 compared (858 nonzero), 707 excluded; UsTaxes below rule: 682 compared (596 nonzero), 1018 excluded | 146 |
| f1040.line19 | — | — | — | 12 | — | PE: 872 compared (374 nonzero), 788 excluded; TC below rule: 654 compared (338 nonzero), 1046 excluded; OpenTaxSolver below rule: 359 compared (297 nonzero), 611 excluded; UsTaxes below rule: 376 compared (152 nonzero), 1324 excluded | 73 |
| f1040.line20 | — | — | — | 12 | — | TC: 852 compared (429 nonzero), 840 excluded; OpenTaxSolver below rule: 632 compared (210 nonzero), 1068 excluded; UsTaxes below rule: 376 compared (91 nonzero), 1324 excluded | 3 |
| f1040.line21 | — | — | — | 12 | — | OpenTaxSolver below rule: 632 compared (363 nonzero), 1068 excluded; UsTaxes below rule: 376 compared (201 nonzero), 1324 excluded | 4 |
| f1040.line22 | 8 | — | — | 12 | — | OpenTaxSolver below rule: 632 compared (462 nonzero), 1068 excluded; UsTaxes below rule: 376 compared (316 nonzero), 1324 excluded | 26 |
| f1040.line23 | — | — | — | 12 | — | OpenTaxSolver: 1264 compared (319 nonzero), 436 excluded; UsTaxes below rule: 924 compared (122 nonzero), 776 excluded | 26 |
| f1040.line24 | 3 | — | — | 12 | — | TC below rule: 729 compared (521 nonzero), 956 excluded; OpenTaxSolver below rule: 587 compared (443 nonzero), 1113 excluded; UsTaxes below rule: 334 compared (277 nonzero), 1366 excluded | 25 |
| f1040.line25a | — | — | — | 12 | — | UsTaxes: 1330 compared (1330 nonzero), 370 excluded | 3 |
| f1040.line25b | — | — | — | — | — | — | 3 |
| f1040.line25c_other | — | — | — | — | — | — | — |
| f1040.line25c | — | — | — | 12 | — | — | 5 |
| f1040.line25d | — | — | — | 12 | — | OpenTaxSolver: 1567 compared (1567 nonzero), 133 excluded; UsTaxes: 1330 compared (1330 nonzero), 370 excluded | 3 |
| f1040.line26 | — | — | — | — | — | — | 3 |
| f1040.line27a | 5 | — | — | 12 | — | PE: 1511 compared (250 nonzero), 150 excluded; TC: 1260 compared (215 nonzero), 440 excluded; UsTaxes below rule: 867 compared (0 nonzero), 833 excluded | 81 |
| f1040.line27b | — | — | — | 12 | — | — | 2 (stage9.eic.no_child.4000, stage9.eic.refuse.clergy_schedule1) |
| f1040.line27c | — | — | — | 12 | — | — | 14 |
| f1040.separated_spouses | — | — | — | 12 | — | — | 5 |
| f1040.line28 | 4 | — | — | 12 | — | PE: 872 compared (194 nonzero), 788 excluded; TC below rule: 654 compared (88 nonzero), 1046 excluded; OpenTaxSolver below rule: 233 compared (38 nonzero), 737 excluded; UsTaxes below rule: 246 compared (8 nonzero), 1454 excluded | 31 |
| f1040.line28_box | — | — | — | 12 | — | — | — |
| f1040.line29 | 10 | — | — | 12 | — | PE: 1529 compared (86 nonzero), 164 excluded; TC: 1258 compared (81 nonzero), 442 excluded; UsTaxes: 127 compared (62 nonzero), 85 excluded | 15 |
| f1040.line30 | — | — | — | 10 | — | — | 4 |
| f1040.line31 | — | — | — | 12 | — | — | 24 |
| f1040.line32 | — | — | — | 12 | — | OpenTaxSolver below rule: 476 compared (38 nonzero), 1224 excluded; UsTaxes below rule: 246 compared (26 nonzero), 1454 excluded | 4 |
| f1040.line33 | 5 | — | — | 12 | — | OpenTaxSolver below rule: 476 compared (476 nonzero), 1224 excluded; UsTaxes below rule: 244 compared (244 nonzero), 1456 excluded | 19 |
| f1040.line34 | 5 | — | — | 9 | — | OpenTaxSolver below rule: 438 compared (310 nonzero), 1262 excluded; UsTaxes below rule: 220 compared (152 nonzero), 1480 excluded | 42 |
| f1040.line35a | — | — | — | — | — | — | 3 |
| f1040.line36 | — | — | — | — | — | — | 3 |
| f1040.line37 | — | — | — | 8 | — | OpenTaxSolver below rule: 438 compared (128 nonzero), 1262 excluded; UsTaxes below rule: 220 compared (68 nonzero), 1480 excluded | 56 |

Unasserted lines: f1040.ira_rollovers, f1040.plan_rollovers

## Form 1095-A, Health Insurance Marketplace Statement (one entry per form)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1095a.one | — | — | — | — | — | — | — |
| f1095a.months | — | — | — | — | — | — | — |
| f1095a.uniform | — | — | — | — | — | — | — |
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
| f1095a.a_jan | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_feb | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_mar | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_apr | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_may | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_jun | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_jul | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_aug | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_sep | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_oct | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_nov | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.a_dec | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_jan | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_feb | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_mar | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_apr | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_may | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_jun | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_jul | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_aug | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_sep | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_oct | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_nov | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.b_dec | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.yr_a_monthly | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.yr_a_uniform | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.line33a | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | 3 |
| f1095a.yr_b_monthly | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.yr_b_uniform | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.line33b | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | 3 |
| f1095a.yr_c_monthly | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |
| f1095a.line33c | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | 3 |
| f1095a.b_counted | — | — | — | — | — | — | — |
| f1095a.b_used | — | — | — | 2 (classm.f1095a.1.deepseek, classm.f1095a.1) | — | — | — |

Unasserted lines: f1095a.one, f1095a.months

## Form 2441 — Child and Dependent Care Expenses (Parts I to III)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f2441.zero | — | — | — | via f2441.line9b: 3; via f2441.line22: 6 | — | — | — |
| f2441.benefits | — | — | — | — | — | — | — |
| f2441.care | — | — | — | — | — | — | — |
| f2441.filing | — | — | — | — | — | — | — |
| f2441.student_disabled | — | — | — | — | — | — | — |
| f2441.spouse_died | — | — | — | — | — | — | — |
| f2441.spouse_died_gate | — | — | — | — | — | — | — |
| f2441.nondependent | — | — | — | — | — | — | — |
| f2441.nondependent_gate | — | — | — | — | — | — | — |
| f2441.provider_count | — | — | — | — | — | — | — |
| f2441.related_count | — | — | — | — | — | — | — |
| f2441.provider_ineligible | — | — | — | — | — | — | — |
| f2441.line1_box | — | — | — | 12 | — | — | — |
| f2441.statement_count | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.statement_notice | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_count | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.household_notice | — | — | — | — | — | — | 1 (stage15.regress.f2441.providers_statement_household) |
| f2441.provider_paid | — | — | — | — | — | — | — |
| f2441.line1_paid | — | — | — | — | — | — | — |
| f2441.qp_count | — | — | — | — | — | — | 4 |
| f2441.line2_box | — | — | — | 12 | — | — | 1 (stage15.regress.f2441.three_qualifying_persons) |
| f2441.paid_total | — | — | — | — | — | — | 4 |
| f2441.limit_one | — | — | — | — | — | — | — |
| f2441.limit_two | — | — | — | — | — | — | — |
| f2441.two_or_more | — | — | — | — | — | — | — |
| f2441.limit | — | — | — | via f2441.line27: 6 | — | — | 1 (stage15.regress.f2441.nonqualifying_dependent) |
| f2441.line3_expenses | — | — | — | — | — | — | — |
| f2441.line3 | — | — | — | 5 | — | OpenTaxSolver: 285 compared (285 nonzero), 0 excluded | 29 |
| f2441.has_1e | — | — | — | — | — | — | — |
| f2441.box10_persons | — | — | — | — | — | — | 1 (stage19.mut.dc_box10_spouse_only) |
| f2441.one_box10 | — | — | — | — | — | — | — |
| f2441.attrib_gate | — | — | — | — | — | — | — |
| f2441.line4 | — | — | — | 5 | — | OpenTaxSolver: 285 compared (285 nonzero), 0 excluded | 33 |
| f2441.spouse_earned | — | — | — | — | — | — | — |
| f2441.line5 | — | — | — | 5 | — | — | 34 |
| f2441.joint | — | — | — | — | — | — | — |
| f2441.line6_34 | — | — | — | — | — | — | — |
| f2441.line6_345 | — | — | — | — | — | — | — |
| f2441.line6 | — | — | — | 5 | — | OpenTaxSolver: 285 compared (270 nonzero), 0 excluded | 28 |
| f2441.line7 | — | — | — | 5 | — | OpenTaxSolver: 267 compared (267 nonzero), 18 excluded | 28 |
| f2441.line8 | — | — | — | 5 | — | — | 28 |
| f2441.line9a | — | — | — | 5 | — | OpenTaxSolver: 266 compared (251 nonzero), 19 excluded | 28 |
| f2441.line9b | — | — | — | 5 | — | — | 1 (stage15.refuse.f2441.prior_year) |
| f2441.prior_year | — | — | — | — | — | — | — |
| f2441.line9c | — | — | — | 5 | — | PE: 259 compared (247 nonzero), 150 excluded; OpenTaxSolver: 250 compared (238 nonzero), 35 excluded | 28 |
| f2441.clw1 | — | — | — | 5 | — | — | 12 |
| f2441.clw2 | — | — | — | 5 | — | — | 12 |
| f2441.clw3 | — | — | — | 5; via f2441.line10: 3 | — | E via f2441.line10 (OpenTaxSolver) | 12 |
| f2441.line10 | — | — | — | 5 | — | OpenTaxSolver: 162 compared (136 nonzero), 123 excluded | 28 |
| f2441.line11 | — | — | — | 5 | — | PE: 209 compared (170 nonzero), 404 excluded; TC: 152 compared (123 nonzero), 840 excluded; OpenTaxSolver: 162 compared (130 nonzero), 123 excluded | 33 |
| f2441.line12 | — | — | — | 12 | — | — | 10 |
| f2441.line13 | — | — | — | — | — | — | 7 |
| f2441.line14 | — | — | — | — | — | — | 7 |
| f2441.line15_sum | — | — | — | — | — | — | — |
| f2441.line14_bad | — | — | — | — | — | — | 3 |
| f2441.line15 | — | — | — | 12 | — | — | 11 |
| f2441.paid_2026 | — | — | — | — | — | — | — |
| f2441.line16 | — | — | — | 12 | — | — | 7 |
| f2441.line17 | — | — | — | 12 | — | — | 7 |
| f2441.line18 | — | — | — | 12 | — | — | 10 |
| f2441.spouse_earned_b | — | — | — | — | — | — | — |
| f2441.line19 | — | — | — | 12 | — | — | 11 |
| f2441.line20_17_18 | — | — | — | — | — | — | — |
| f2441.line20_all | — | — | — | — | — | — | — |
| f2441.line20 | — | — | — | 12 | — | — | 7 |
| f2441.plans_differ | — | — | — | — | — | — | — |
| f2441.employer_care | — | — | — | — | — | — | — |
| f2441.employer_care_gate | — | — | — | — | — | — | — |
| f2441.plan_max | — | — | — | — | — | — | — |
| f2441.exclusion_max | — | — | — | — | — | — | 1 (stage15.regress.f2441.exclusion_max) |
| f2441.line21 | — | — | — | 12 | — | — | 9 |
| f2441.line22 | — | — | — | 12 | — | — | 7 |
| f2441.line23 | — | — | — | 12 | — | — | 7 |
| f2441.line24_20_21 | — | — | — | — | — | — | — |
| f2441.line24 | — | — | — | 12 | — | — | 8 |
| f2441.line25 | — | — | — | 12 | — | — | 7 |
| f2441.line26 | — | — | — | 12 | — | — | 9 |
| f2441.line27 | — | — | — | 12 | — | — | 7 |
| f2441.line28 | — | — | — | 12 | — | — | 8 |
| f2441.line29 | — | — | — | 9 | — | — | 8 |
| f2441.line30 | — | — | — | 2 (classm.f2441.2.deepseek, classm.f2441.5.deepseek) | — | — | 3 |
| f2441.line31 | — | — | — | 4 | — | — | 3 |

Unasserted lines: f2441.filing, f2441.spouse_died_gate, f2441.nondependent_gate, f2441.provider_count, f2441.related_count, f2441.provider_ineligible, f2441.provider_paid, f2441.line1_paid, f2441.limit_one, f2441.limit_two, f2441.two_or_more, f2441.line3_expenses, f2441.has_1e, f2441.one_box10, f2441.attrib_gate, f2441.spouse_earned, f2441.joint, f2441.line6_34, f2441.line6_345, f2441.line15_sum, f2441.spouse_earned_b, f2441.line20_17_18, f2441.line20_all, f2441.employer_care_gate, f2441.line24_20_21

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
| f4562.line21 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line22 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line25 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line26h | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line28 | — | — | — | 1 (classm.f4562.1) | — | — | — |
| f4562.line29 | — | — | — | 1 (classm.f4562.1) | — | — | — |

## Form 4952 — supported investment-interest deduction and election

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f4952.line1 | — | — | — | — | — | — | 1 (stage20.blind.r9) |
| f4952.carryover | — | — | — | — | — | — | — |
| f4952.prior_7 | — | — | — | — | — | — | — |
| f4952.unsupported | — | — | — | — | — | — | — |
| f4952.alternative_allocation | — | — | — | — | — | — | — |
| f4952.line4a | — | — | — | 8 | — | — | — |
| f4952.line4g | — | — | — | — | — | — | — |
| f4952.zero | — | — | — | via f4952.line5: 4 | — | — | — |
| f4952.line2 | — | — | — | 8 | — | — | 6 |
| f4952.line3 | — | — | — | 8 | — | — | 3 |
| f4952.line4b | — | — | — | 8 | — | — | — |
| f4952.bad_dividends | — | — | — | — | — | — | — |
| f4952.line4c | — | — | — | 8 | — | — | — |
| f4952.line4d | — | — | — | 8 | — | — | 1 (stage4.interest.short_term) |
| f4952.line4e | — | — | — | 8 | — | — | 1 (stage4.interest.short_term) |
| f4952.line4f | — | — | — | 8 | — | — | 1 (stage4.interest.short_term) |
| f4952.election_limit | — | — | — | — | — | — | 1 (stage4.interest.short_term) |
| f4952.bad_election | — | — | — | — | — | — | — |
| f4952.election | — | — | — | — | — | — | 4 |
| f4952.line4h | — | — | — | 8 | — | — | — |
| f4952.line5 | — | — | — | 8 | — | — | 4 |
| f4952.line6 | — | — | — | 8 | — | — | 1 (stage20.blind.r9) |
| f4952.line7 | — | — | — | 8 | — | — | 5 |
| f4952.line8 | — | — | — | 8 | — | — | 9 |
| f4952.exception | — | — | — | — | — | — | — |
| f4952.required | — | — | — | — | — | — | 10 |

Unasserted lines: f4952.bad_dividends, f4952.bad_election, f4952.exception

## Form 5329, Additional Taxes on Qualified Plans (Including IRAs) and Other Tax-Favored Accounts (Parts I and VII), one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f5329.l1 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | UsTaxes below rule: 1072 compared (17 nonzero), 628 excluded | 17 |
| f5329.l2 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | — | 15 |
| f5329.l3 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | — | 15 |
| f5329.l3_s | — | — | — | — | — | — | — |
| f5329.l3_other | — | — | — | — | — | — | — |
| f5329.rate10 | — | — | — | — | — | — | — |
| f5329.rate25 | — | — | — | — | — | — | — |
| f5329.tax10 | — | — | — | — | — | — | — |
| f5329.tax25 | — | — | — | — | — | — | — |
| f5329.l4 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | UsTaxes below rule: 1072 compared (17 nonzero), 628 excluded | 17 |
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
| f5329.files | 1 (stage21.example.teacher_education) | — | — | — | — | — | 10 |

Unasserted lines: f5329.l3_s, f5329.l3_other, f5329.rate10, f5329.rate25, f5329.tax10, f5329.tax25, f5329.l49_base, f5329.rate6, f5329.l49_tax, f5329.has_excess, f5329.zero, f5329.tax, f5329.must, f5329.one

## Form 5695 — Residential Energy Credits (Parts I and II)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f5695.zero | — | — | — | — | — | — | — |
| f5695.part1_any | — | — | — | — | — | — | — |
| f5695.part2_any | — | — | — | — | — | — | — |
| f5695.business_use | — | — | — | — | — | — | — |
| f5695.construction_later | — | — | — | — | — | — | — |
| f5695.line1 | — | — | — | — | — | — | 9 |
| f5695.line2 | — | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line3 | — | — | — | — | — | — | 1 (stage16.cleanup.f5695_small_wind) |
| f5695.line4 | — | — | — | — | — | — | 1 (stage15.f5695.s13) |
| f5695.line5a | — | — | — | — | — | — | — |
| f5695.battery_cost | — | — | — | — | — | — | — |
| f5695.line5b | — | — | — | 4 | — | — | 1 (stage15.f5695.s4) |
| f5695.line6a | — | — | — | 33 | — | — | 13 |
| f5695.rce_rate | — | — | — | — | — | — | — |
| f5695.line6b | — | — | — | 33 | — | — | 11 |
| f5695.line7a | — | — | — | — | — | — | — |
| f5695.line11 | — | — | — | — | — | — | 1 (stage15.refuse.f5695.fuel_cell) |
| f5695.line12 | — | — | — | — | — | — | 1 (stage15.f5695.s5) |
| f5695.line13 | — | — | — | 34 | — | PE: 173 compared (173 nonzero), 19 excluded | 12 |
| f5695.claiming_part1 | — | — | — | — | — | — | — |
| f5695.rce_ws1 | — | — | — | — | — | — | 11 |
| f5695.ctc_line19 | — | — | — | — | — | — | — |
| f5695.ctc | — | — | — | — | — | — | — |
| f5695.rce_ws2 | — | — | — | — | — | — | 12 |
| f5695.rce_ws3 | — | — | — | via f5695.line14: 16 | — | — | 11 |
| f5695.line14 | — | — | — | 33 | — | — | 12 |
| f5695.line15 | — | — | — | 34 | — | PE: 121 compared (96 nonzero), 418 excluded | 12 |
| f5695.line16 | — | — | — | 11 | — | — | 9 |
| f5695.line17a | — | — | — | — | — | — | — |
| f5695.line17b | — | — | — | — | — | — | — |
| f5695.line17c | — | — | — | — | — | — | — |
| f5695.sec_a_claimed | — | — | — | — | — | — | — |
| f5695.line17e | — | — | — | — | — | — | — |
| f5695.sec_a_new_home | — | — | — | — | — | — | — |
| f5695.eehi_rate | — | — | — | — | — | — | — |
| f5695.line18a | — | — | — | — | — | — | 6 |
| f5695.ins_30 | — | — | — | — | — | — | — |
| f5695.insulation_max | — | — | — | — | — | — | — |
| f5695.ins_capped | — | — | — | — | — | — | — |
| f5695.line18b | — | — | — | 17 | — | — | 7 |
| f5695.line19a | — | — | — | — | — | — | 4 |
| f5695.door1_30 | — | — | — | — | — | — | — |
| f5695.door_max | — | — | — | — | — | — | — |
| f5695.line19c | — | — | — | 17 | — | — | 4 |
| f5695.line19d_i | — | — | — | — | — | — | — |
| f5695.line19d_ii | — | — | — | — | — | — | — |
| f5695.line19e | — | — | — | — | — | — | 4 |
| f5695.line19f | — | — | — | 17 | — | — | 4 |
| f5695.line19g | — | — | — | 17 | — | — | 4 |
| f5695.doors_sum | — | — | — | — | — | — | — |
| f5695.doors_max | — | — | — | — | — | — | — |
| f5695.doors_cost | — | — | — | — | — | — | — |
| f5695.qmid_doors | — | — | — | — | — | — | — |
| f5695.doors_no_qmid | — | — | — | — | — | — | — |
| f5695.doors_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line19h | — | — | — | 17 | — | — | 4 |
| f5695.line20a_i | — | — | — | — | — | — | — |
| f5695.line20a_ii | — | — | — | — | — | — | — |
| f5695.line20a_iii | — | — | — | — | — | — | — |
| f5695.line20a_iv | — | — | — | — | — | — | — |
| f5695.line20b | — | — | — | — | — | — | 4 |
| f5695.line20c | — | — | — | 17 | — | — | 4 |
| f5695.windows_30 | — | — | — | — | — | — | — |
| f5695.windows_max | — | — | — | — | — | — | — |
| f5695.qmid_windows | — | — | — | — | — | — | — |
| f5695.windows_no_qmid | — | — | — | — | — | — | — |
| f5695.windows_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line20d | — | — | — | 17 | — | — | 4 |
| f5695.line21a | — | — | — | — | — | — | — |
| f5695.line21b | — | — | — | — | — | — | — |
| f5695.sec_b_claimed | — | — | — | — | — | — | — |
| f5695.b_new_home | — | — | — | — | — | — | — |
| f5695.sec_b_new_home | — | — | — | — | — | — | — |
| f5695.item_max | — | — | — | — | — | — | — |
| f5695.line22a | — | — | — | — | — | — | 3 |
| f5695.line22b | — | — | — | — | — | — | 3 |
| f5695.line22c | — | — | — | 15 | — | — | 3 |
| f5695.ac_30 | — | — | — | — | — | — | — |
| f5695.qmid_ac | — | — | — | — | — | — | — |
| f5695.ac_no_qmid | — | — | — | — | — | — | — |
| f5695.ac_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_doors_windows_ac) |
| f5695.line22d | — | — | — | 15 | — | — | 3 |
| f5695.line23a_i | — | — | — | — | — | — | — |
| f5695.line23a_ii | — | — | — | — | — | — | — |
| f5695.line23b | — | — | — | — | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line23c | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.wh_30 | — | — | — | — | — | — | — |
| f5695.qmid_wh | — | — | — | — | — | — | — |
| f5695.wh_no_qmid | — | — | — | — | — | — | — |
| f5695.wh_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line23d | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e3, stage15.f5695-3.g1) |
| f5695.line24a | — | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24b | — | — | — | — | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line24c | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.furnace_30 | — | — | — | — | — | — | — |
| f5695.qmid_furnace | — | — | — | — | — | — | — |
| f5695.furnace_no_qmid | — | — | — | — | — | — | — |
| f5695.furnace_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line24d | — | — | — | 15 | — | — | 2 (stage15.f5695-2.e4, stage15.f5695-2.e5) |
| f5695.line25a | — | — | — | — | — | — | — |
| f5695.enabling_claimed | — | — | — | — | — | — | — |
| f5695.line25c | — | — | — | — | — | — | 2 (stage15.f5695-2.e6, stage15.f5695-2.e7) |
| f5695.enabling_30 | — | — | — | — | — | — | — |
| f5695.qmid_enabling | — | — | — | — | — | — | — |
| f5695.enabling_no_qmid | — | — | — | — | — | — | — |
| f5695.enabling_capped | — | — | — | — | — | — | 2 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp, stage15.regress.f5695.enabling_cap) |
| f5695.line25e | — | — | — | 5 | — | — | 3 |
| f5695.line26a | — | — | — | — | — | — | — |
| f5695.line26b | — | — | — | — | — | — | 2 (stage15.f5695.s6, stage15.f5695-2.e9) |
| f5695.audit_30 | — | — | — | — | — | — | — |
| f5695.audit_max | — | — | — | — | — | — | — |
| f5695.audit_capped | — | — | — | — | — | — | — |
| f5695.line26c | — | — | — | 3 | — | — | 3 |
| f5695.line27 | — | — | — | 34 | — | — | 24 |
| f5695.annual_max | — | — | — | — | — | — | — |
| f5695.line28 | — | — | — | 34 | — | — | 22 |
| f5695.line29a | — | — | — | — | — | — | 4 |
| f5695.line29b | — | — | — | — | — | — | 5 |
| f5695.line29c | — | — | — | — | — | — | 1 (stage15.f5695-2.e10) |
| f5695.line29d | — | — | — | — | — | — | 3 |
| f5695.line29e | — | — | — | — | — | — | — |
| f5695.line29f | — | — | — | — | — | — | 3 |
| f5695.line29g | — | — | — | 15 | — | — | 5 |
| f5695.hp_30 | — | — | — | — | — | — | — |
| f5695.heat_pump_max | — | — | — | — | — | — | — |
| f5695.qmid_hp | — | — | — | — | — | — | — |
| f5695.hp_no_qmid | — | — | — | — | — | — | — |
| f5695.hp_capped | — | — | — | — | — | — | 1 (stage15.refuse.f5695.qmid_wh_furnace_enabling_hp) |
| f5695.line29h | — | — | — | 15 | — | — | 5 |
| f5695.joint_occupancy | — | — | — | — | — | — | — |
| f5695.separate_homes | — | — | — | — | — | — | — |
| f5695.separate_homes_joint | — | — | — | — | — | — | — |
| f5695.line30 | — | — | — | 34 | — | PE: 146 compared (146 nonzero), 59 excluded | 27 |
| f5695.eehi_ws1 | — | — | — | — | — | — | 20 |
| f5695.eehi_ws2 | — | — | — | — | — | — | 21 |
| f5695.eehi_ws3 | — | — | — | via f5695.line31: 17 | — | — | 20 |
| f5695.line31 | — | — | — | 34 | — | — | 20 |
| f5695.line32 | — | — | — | 34 | — | PE: 112 compared (91 nonzero), 445 excluded | 22 |
| f5695.line32a | — | — | — | 34 | — | — | — |
| f5695.condo | — | — | — | — | — | — | — |
| f5695.line32b | — | — | — | 34 | — | — | — |

Unasserted lines: f5695.zero, f5695.rce_rate, f5695.claiming_part1, f5695.ctc_line19, f5695.ctc, f5695.sec_a_claimed, f5695.sec_a_new_home, f5695.eehi_rate, f5695.ins_30, f5695.insulation_max, f5695.ins_capped, f5695.door1_30, f5695.door_max, f5695.doors_sum, f5695.doors_max, f5695.doors_cost, f5695.doors_no_qmid, f5695.windows_30, f5695.windows_max, f5695.windows_no_qmid, f5695.sec_b_claimed, f5695.sec_b_new_home, f5695.item_max, f5695.ac_30, f5695.ac_no_qmid, f5695.wh_30, f5695.wh_no_qmid, f5695.furnace_30, f5695.furnace_no_qmid, f5695.enabling_claimed, f5695.enabling_30, f5695.enabling_no_qmid, f5695.audit_30, f5695.audit_max, f5695.audit_capped, f5695.annual_max, f5695.hp_30, f5695.heat_pump_max, f5695.hp_no_qmid, f5695.separate_homes_joint

## Form 8606 — Nondeductible IRAs, Part I (nondeductible contributions with no 2025 distribution), one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8606.files | — | — | — | 1 (classm.f8606.1) | — | — | — |
| f8606.line1 | — | — | — | — | — | — | 7 |
| f8606.line2 | — | — | — | — | — | — | 7 |
| f8606.line3 | — | — | — | — | — | — | 8 |
| f8606.dist | — | — | — | — | — | — | — |
| f8606.line14 | — | — | — | — | — | — | 8 |

Unasserted lines: f8606.dist

## Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8863.paid | — | — | — | — | — | — | — |
| f8863.zero | — | — | — | — | — | — | — |
| f8863.eligible | — | — | — | — | — | — | 1 (stage19.mut.claimed_filer_llc) |
| f8863.aoc_person | — | — | — | — | — | — | — |
| f8863.aoc_dep | — | — | — | — | — | — | — |
| f8863.aoc_sum | — | — | — | — | — | — | — |
| f8863.line1 | 4 | — | — | 8 | — | UsTaxes: 137 compared (109 nonzero), 75 excluded | 10 |
| f8863.line2 | — | — | — | 8 | — | — | 10 |
| f8863.line3 | 1 (stage19.example.aoc_phaseout) | — | — | 8 | — | — | 11 |
| f8863.line4 | 1 (stage19.example.aoc_phaseout) | — | — | 8 | — | — | 10 |
| f8863.show_after4 | — | — | — | — | — | — | — |
| f8863.line5 | — | — | — | 6 | — | — | 10 |
| f8863.ban | — | — | — | — | — | — | — |
| f8863.ban_refused | — | — | — | — | — | — | — |
| f8863.line7 | 11 | — | — | 6 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded | 12 |
| f8863.kid_needed | — | — | — | — | — | — | — |
| f8863.kid | — | — | — | — | — | — | — |
| f8863.no_refund | — | — | — | 6 | — | — | 10 |
| f8863.refund_rate | — | — | — | — | — | — | — |
| f8863.line7_40 | — | — | — | — | — | — | — |
| f8863.line8 | 12 | — | — | 4 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded; UsTaxes: 137 compared (69 nonzero), 75 excluded | 7 |
| f8863.line9 | 4 | — | — | 6; via f8863.clw2: 3 | — | PE: 1625 compared (96 nonzero), 34 excluded; TC: 1368 compared (92 nonzero), 332 excluded; UsTaxes: 137 compared (69 nonzero), 75 excluded | 10 |
| f8863.llc_person | — | — | — | — | — | — | — |
| f8863.llc_dep | — | — | — | — | — | — | — |
| f8863.llc_sum | — | — | — | — | — | — | — |
| f8863.line10 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 6 | — | — | 11 |
| f8863.llc_cap | — | — | — | — | — | — | — |
| f8863.show_llc | — | — | — | — | — | — | — |
| f8863.line11 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | — | 5 |
| f8863.llc_rate | — | — | — | — | — | — | — |
| f8863.line12 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | UsTaxes below rule: 137 compared (29 nonzero), 75 excluded | 4 |
| f8863.line13 | — | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | — | 4 |
| f8863.line14 | 1 (stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | — | 5 |
| f8863.line15 | 1 (stage19.example.llc_phaseout) | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | — | 4 |
| f8863.line16 | — | — | — | 2 (classm.f8863.2.deepseek, classm.f8863.2) | — | — | 4 |
| f8863.line18 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | 6; via f8863.clw1: 3 | — | PE below rule: 1625 compared (31 nonzero), 34 excluded; UsTaxes below rule: 137 compared (18 nonzero), 75 excluded | 10 |
| f8863.clw1 | — | — | — | 4 | — | — | 10 |
| f8863.clw2 | — | — | — | 4 | — | — | 10 |
| f8863.clw3 | — | — | — | 4 | — | — | 10 |
| f8863.clw4 | — | — | — | 4 | — | — | 10 |
| f8863.clw5 | — | — | — | 4 | — | — | 11 |
| f8863.clw6 | — | — | — | 4 | — | — | 10 |
| f8863.clw7 | — | — | — | 4; via f8863.line19: 3 | — | E via f8863.line19 (PE, TC) | 10 |
| f8863.line19 | 14 | — | — | 6 | — | PE: 1225 compared (83 nonzero), 418 excluded; TC: 844 compared (65 nonzero), 840 excluded; UsTaxes below rule: 92 compared (44 nonzero), 120 excluded | 11 |

Unasserted lines: f8863.zero, f8863.aoc_person, f8863.aoc_dep, f8863.aoc_sum, f8863.show_after4, f8863.ban_refused, f8863.kid_needed, f8863.kid, f8863.refund_rate, f8863.line7_40, f8863.llc_person, f8863.llc_dep, f8863.llc_sum, f8863.llc_cap, f8863.show_llc, f8863.llc_rate

## Form 8880 — Credit for Qualified Retirement Savings Contributions (the saver's credit)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8880.zero | — | — | — | — | — | — | — |
| f8880.joint | — | — | — | — | — | — | — |
| f8880.line1a | — | — | — | 8 | — | — | 34 |
| f8880.line1b | — | — | — | 4 | — | — | 9 |
| f8880.line2a | — | — | — | 8 | — | — | 33 |
| f8880.line2b | — | — | — | 4 | — | — | 10 |
| f8880.line3a | — | — | — | 8 | — | — | 33 |
| f8880.line3b | — | — | — | 4 | — | — | 9 |
| f8880.dist_2025 | — | — | — | — | — | — | — |
| f8880.prior_joint_sum | — | — | — | — | — | — | — |
| f8880.prior_joint | — | — | — | — | — | — | — |
| f8880.prior_own_a | — | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.prior_own_b | — | — | — | — | — | — | 1 (stage15.regress.f8880.prior_own_b_spouse_only) |
| f8880.line4a | — | — | — | 8 | — | — | 35 |
| f8880.line4b_joint | — | — | — | — | — | — | — |
| f8880.line4b | — | — | — | 4 | — | — | 11 |
| f8880.line5a | — | — | — | 8 | — | — | 34 |
| f8880.line5b | — | — | — | 4 | — | — | 10 |
| f8880.cap | — | — | — | — | — | — | — |
| f8880.inelig_a | — | — | — | — | — | — | — |
| f8880.inelig_b | — | — | — | — | — | — | — |
| f8880.elig_a | — | — | — | — | — | — | — |
| f8880.elig_b | — | — | — | — | — | — | — |
| f8880.line6a_figured | — | — | — | — | — | — | — |
| f8880.line6b_figured | — | — | — | — | — | — | — |
| f8880.line6a | — | — | — | 8 | — | — | 34 |
| f8880.line6b | — | — | — | 4 | — | — | 10 |
| f8880.line7 | — | — | — | 8 | — | — | 35 |
| f8880.past7 | — | — | — | — | — | — | 2 (stage21.t067.f8880_line9_stop, stage21.t067.f8880_line7_stop) |
| f8880.line8 | — | — | — | 2 (classm.f8880.2.deepseek, classm.f8880.2) | — | — | 33 |
| f8880.line9 | — | — | — | 2 (classm.f8880.2.deepseek, classm.f8880.2) | — | — | 33 |
| f8880.past9 | — | — | — | — | — | — | 2 (stage21.t067.f8880_line9_stop, stage21.t067.f8880_line7_stop) |
| f8880.line10 | — | — | — | 2 (classm.f8880.2.deepseek, classm.f8880.2) | — | PE: 1637 compared (155 nonzero), 22 excluded | 28 |
| f8880.clw1 | — | — | — | 1 (classm.f8880.2.deepseek) | — | — | 28 |
| f8880.clw2 | — | — | — | 1 (classm.f8880.2.deepseek) | — | — | 28 |
| f8880.clw3 | — | — | — | 1 (classm.f8880.2.deepseek); via f8880.line11: 1 (classm.f8880.2.deepseek) | — | — | 28 |
| f8880.line11 | — | — | — | 2 (classm.f8880.2.deepseek, classm.f8880.2) | — | — | 28 |
| f8880.agi_limit | — | — | — | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line3_total | — | — | — | — | — | — | — |
| f8880.can_take | — | — | — | — | — | — | 1 (stage15.regress.f8880.agi_limit) |
| f8880.line12_figured | — | — | — | — | — | — | — |
| f8880.line12 | — | — | — | 2 (classm.f8880.2.deepseek, classm.f8880.2); via s3.line4: 4 | — | PE below rule: 1243 compared (49 nonzero), 420 excluded | 30 |

Unasserted lines: f8880.zero, f8880.joint, f8880.dist_2025, f8880.prior_joint_sum, f8880.prior_joint, f8880.line4b_joint, f8880.cap, f8880.inelig_a, f8880.inelig_b, f8880.elig_a, f8880.elig_b, f8880.line6a_figured, f8880.line6b_figured, f8880.line3_total, f8880.line12_figured

## Form 8889 — Health Savings Accounts (Parts I and II)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8889.one | — | — | — | — | — | — | — |
| f8889.zero | — | — | — | via f8889.line4: 6; via f8889.line10: 6 | — | — | — |
| f8889.line2 | — | — | — | — | — | — | 1 (stage16.mut.hsa_contrib_and_dist) |
| f8889.line9 | — | — | — | — | — | — | — |
| f8889.any | — | — | — | — | — | — | — |
| f8889.unsupported | — | — | — | — | — | — | — |
| f8889.mfs | — | — | — | — | — | — | — |
| f8889.months_eligible | — | — | — | — | — | — | — |
| f8889.months_family | — | — | — | — | — | — | — |
| f8889.bad_months | — | — | — | — | — | — | 4 |
| f8889.age55 | — | — | — | — | — | — | — |
| f8889.twelve | — | — | — | — | — | — | — |
| f8889.married_family | — | — | — | — | — | — | 2 (audit.f8889.married_hoh_family_age55, audit.f8889.unmarried_hoh_family_age55) |
| f8889.age55_line3 | — | — | — | — | — | — | — |
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
| f8889.changed | — | — | — | — | — | — | — |
| f8889.dec_coverage | — | — | — | — | — | — | — |
| f8889.dec_amount | — | — | — | — | — | — | — |
| f8889.last_month | — | — | — | — | — | — | — |
| f8889.use_last_month | — | — | — | — | — | — | — |
| f8889.line3_changed | — | — | — | — | — | — | — |
| f8889.line3_all_year | — | — | — | — | — | — | — |
| f8889.line3_last_month | — | — | — | — | — | — | — |
| f8889.line3_part_year | — | — | — | — | — | — | — |
| f8889.line3 | — | — | — | 12 | — | UsTaxes: 188 compared (188 nonzero), 33 excluded | 15 |
| f8889.line4 | — | — | — | 12 | — | — | — |
| f8889.line5 | — | — | — | 12 | — | UsTaxes: 188 compared (188 nonzero), 33 excluded | — |
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
| f8889.allocation_bad | — | — | — | — | — | — | — |
| f8889.share | — | — | — | — | — | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.self_year | — | — | — | — | — | — | 1 (stage16.hsa.engineering.helper_arithmetic_and_boundary) |
| f8889.self_counted | — | — | — | — | — | — | — |
| f8889.self_all | — | — | — | — | — | — | — |
| f8889.self_family_months | — | — | — | — | — | — | — |
| f8889.self_dec_year | — | — | — | — | — | — | — |
| f8889.self_in_family | — | — | — | — | — | — | — |
| f8889.step4_total | — | — | — | — | — | — | — |
| f8889.step4 | — | — | — | — | — | — | 2 (stage13.hsa_part_year_family, stage13.hsa_last_month_spouses) |
| f8889.line6_split | — | — | — | — | — | — | — |
| f8889.split | — | — | — | — | — | — | — |
| f8889.line6 | — | — | — | 12 | — | UsTaxes below rule: 106 compared (106 nonzero), 115 excluded | 11 |
| f8889.additional | — | — | — | — | — | — | — |
| f8889.line7_year | — | — | — | — | — | — | — |
| f8889.line7_counted | — | — | — | — | — | — | — |
| f8889.line7_total | — | — | — | — | — | — | — |
| f8889.line7_worksheet | — | — | — | — | — | — | — |
| f8889.line7_applies | — | — | — | — | — | — | — |
| f8889.line7 | — | — | — | 12 | — | — | 5 |
| f8889.line8 | — | — | — | 12 | — | UsTaxes: 113 compared (113 nonzero), 108 excluded | 4 |
| f8889.line10 | — | — | — | 12 | — | — | — |
| f8889.line11 | — | — | — | 12 | — | UsTaxes: 221 compared (104 nonzero), 0 excluded | — |
| f8889.line12 | — | — | — | 12 | — | OpenTaxSolver: 257 compared (257 nonzero), 0 excluded; UsTaxes: 113 compared (113 nonzero), 108 excluded | 2 (stage11.hsa.self_full_year, stage11.hsa.employer) |
| f8889.employer_in_box1 | — | — | — | — | — | — | — |
| f8889.excess | — | — | — | — | — | — | — |
| f8889.excess_own | — | — | — | — | — | — | — |
| f8889.excess_employer | — | — | — | — | — | — | — |
| f8889.excess_amt | — | — | — | — | — | — | — |
| f8889.line13_figured | — | — | — | — | — | — | — |
| f8889.line13 | — | — | — | 12 | — | OpenTaxSolver: 257 compared (257 nonzero), 0 excluded; UsTaxes: 1316 compared (137 nonzero), 384 excluded | 25 |
| f8889.line14a | — | — | — | — | — | — | 6 |
| f8889.has_dist | — | — | — | — | — | — | — |
| f8889.rollover | — | — | — | — | — | — | — |
| f8889.rollover_bad | — | — | — | — | — | — | — |
| f8889.line14b | — | — | — | 12 | — | — | 12 |
| f8889.line14c | — | — | — | 12 | — | — | 13 |
| f8889.medical | — | — | — | — | — | — | — |
| f8889.line15 | — | — | — | 12 | — | — | 12 |
| f8889.line16_figured | — | — | — | — | — | — | 1 (stage16.refuse.f8889.unsupported_part2) |
| f8889.line16 | — | — | — | 12 | — | — | 15 |
| f8889.has_taxable | — | — | — | — | — | — | — |
| f8889.line17a | — | — | — | — | — | — | 4 |
| f8889.subject_part | — | — | — | — | — | — | — |
| f8889.subject_bad | — | — | — | — | — | — | 1 (stage16.hsa.engineering.helper_arithmetic_and_boundary) |
| f8889.subject_excepted | — | — | — | — | — | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.subject | — | — | — | — | — | — | 1 (stage16.refuse.f8889.subject_over) |
| f8889.line17b_figured | — | — | — | — | — | — | — |
| f8889.line17b | — | — | — | 12 | — | — | 12 |

Unasserted lines: f8889.one, f8889.any, f8889.mfs, f8889.twelve, f8889.age55_line3, f8889.self_amount, f8889.self_under55, f8889.self_55, f8889.family_amount, f8889.family_under55, f8889.family_55, f8889.family_extra, f8889.chart_self, f8889.chart_family, f8889.chart_total, f8889.chart_limit, f8889.all_year, f8889.changed, f8889.dec_amount, f8889.use_last_month, f8889.line3_changed, f8889.line3_all_year, f8889.line3_last_month, f8889.line3_part_year, f8889.family_dec_year, f8889.family_counted, f8889.step1_total, f8889.step1_line3, f8889.step1_x2, f8889.two, f8889.share_equal, f8889.share_raw, f8889.allocation_bad, f8889.self_counted, f8889.self_all, f8889.self_family_months, f8889.self_dec_year, f8889.self_in_family, f8889.step4_total, f8889.line6_split, f8889.split, f8889.additional, f8889.line7_year, f8889.line7_counted, f8889.line7_total, f8889.line7_worksheet, f8889.line7_applies, f8889.excess, f8889.excess_own, f8889.excess_employer, f8889.excess_amt, f8889.line13_figured, f8889.has_dist, f8889.rollover_bad, f8889.has_taxable, f8889.line17b_figured

## Form 8959 — Additional Medicare Tax on wages and self-employment income

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8959.unsupported | — | — | — | — | — | — | — |
| f8959.zero | — | — | — | — | — | — | — |
| f8959.line1 | — | — | — | 1 (classm.f8959.2) | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 3 |
| f8959.line2 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line3 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line8 | — | — | — | 1 (classm.f8959.2) | — | — | 5 |
| f8959.line14 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line23 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line4 | — | — | — | 1 (classm.f8959.2) | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 1 (stage4.medicare.withholding) |
| f8959.line5 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage13.additional_medicare_joint, stage4.medicare.withholding) |
| f8959.line6 | 1 (stage4.official.medicare_example5) | — | — | 1 (classm.f8959.2) | — | UsTaxes: 1400 compared (138 nonzero), 300 excluded | 17 |
| f8959.line7 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver: 1700 compared (157 nonzero), 0 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded | 4 |
| f8959.line9 | — | — | — | 1 (classm.f8959.2) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line10 | — | — | — | 1 (classm.f8959.2) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line11 | — | — | — | 1 (classm.f8959.2) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line12 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage14.f8959.se_above_threshold, stage4.medicare.withholding) |
| f8959.line13 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver below rule: 1700 compared (24 nonzero), 0 excluded | 3 |
| f8959.line15 | — | — | — | 1 (classm.f8959.2) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line16 | — | — | — | 1 (classm.f8959.2) | — | — | 2 (stage16.cleanup.f8959_line16_se_refused, stage4.medicare.withholding) |
| f8959.line17 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver below rule: 1700 compared (0 nonzero), 0 excluded | 1 (stage4.medicare.withholding) |
| f8959.line18 | — | — | — | 2 (classm.f8959.1, classm.f8959.2); via s2.line11: 3 | — | PE: 1681 compared (168 nonzero), 19 excluded; TC: 1370 compared (130 nonzero), 330 excluded; OpenTaxSolver: 1700 compared (168 nonzero), 0 excluded; OpenTaxSolver: 1700 compared (168 nonzero), 0 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded; UsTaxes: 1400 compared (138 nonzero), 300 excluded | 21 |
| f8959.line19 | — | — | — | 1 (classm.f8959.2) | — | UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line20 | — | — | — | 1 (classm.f8959.2) | — | — | 1 (stage4.medicare.withholding) |
| f8959.line21 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 1 (stage4.medicare.withholding) |
| f8959.line22 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver: 1700 compared (231 nonzero), 0 excluded; UsTaxes: 1400 compared (202 nonzero), 300 excluded | 1 (stage4.medicare.withholding) |
| f8959.line24 | — | — | — | 1 (classm.f8959.2) | — | OpenTaxSolver: 1700 compared (231 nonzero), 0 excluded; UsTaxes: 1400 compared (202 nonzero), 300 excluded | 4 |

Unasserted lines: f8959.zero

## Form 8960 — wage, interest, dividend and securities slice

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8960.unsupported | — | — | — | — | — | — | — |
| f8960.prior_2i | — | — | — | — | — | — | — |
| f8960.carryforward_adj | — | — | — | — | — | — | 1 (stage20.niit_adjustment_below_threshold) |
| f8960.refund | — | — | — | — | — | — | — |
| f8960.allocated_taxes | — | — | — | — | — | — | — |
| f8960.zero | — | — | — | via f8960.line3: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line4a: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line4b: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line5b: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line5c: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line6: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line7: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek); via f8960.line9c: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek) | — | — | — |
| f8960.line1 | — | — | — | 4 | — | — | 5 |
| f8960.line2 | — | — | — | 4 | — | — | — |
| f8960.line3 | — | — | — | 4 | — | — | 3 |
| f8960.line4a | — | — | — | 4 | — | — | 3 |
| f8960.line4b | — | — | — | 4 | — | — | 3 |
| f8960.line5b | — | — | — | 4 | — | — | 5 |
| f8960.line5c | — | — | — | 4 | — | — | 4 |
| f8960.line6 | — | — | — | 4 | — | — | 3 |
| f8960.line7 | — | — | — | 4 | — | — | 3 |
| f8960.line9c | — | — | — | 4 | — | — | 3 |
| f8960.line10 | — | — | — | 4 | — | — | 4 |
| f8960.line4c | — | — | — | 4 | — | — | — |
| f8960.line5a | — | — | — | 4 | — | — | 2 (stage20.blind.r10, stage4.niit.loss_floor) |
| f8960.line5d | — | — | — | 4 | — | — | — |
| f8960.line8 | — | — | — | 4 | — | OpenTaxSolver: 1695 compared (1669 nonzero), 0 excluded; UsTaxes: 1395 compared (1373 nonzero), 300 excluded | 3 |
| f8960.line9a | — | — | — | 4 | — | UsTaxes below rule: 1057 compared (28 nonzero), 643 excluded | 3 |
| f8960.line9b | — | — | — | 4 | — | UsTaxes below rule: 955 compared (0 nonzero), 745 excluded | 3 |
| f8960.line9d | — | — | — | 4 | — | UsTaxes below rule: 892 compared (0 nonzero), 808 excluded | 1 (stage4.additional_taxes.combined) |
| f8960.line11 | — | — | — | 4 | — | OpenTaxSolver: 1540 compared (51 nonzero), 121 excluded; UsTaxes below rule: 892 compared (0 nonzero), 808 excluded | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| f8960.line12 | — | — | — | 4 | — | OpenTaxSolver: 1540 compared (1284 nonzero), 121 excluded; UsTaxes: 892 compared (740 nonzero), 808 excluded | 5 |
| f8960.line13 | — | — | — | 4 | — | — | 5 |
| f8960.line14 | — | — | — | 4 | — | — | — |
| f8960.line15 | — | — | — | 4 | — | OpenTaxSolver: 1589 compared (205 nonzero), 111 excluded; UsTaxes: 1153 compared (144 nonzero), 547 excluded | 1 (stage20.blind.r10) |
| f8960.line16 | — | — | — | 4 | — | OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; UsTaxes: 1031 compared (94 nonzero), 669 excluded | 1 (stage16.small.s10) |
| f8960.line17 | — | — | — | 4; via s2.line12: 3 | — | PE: 1472 compared (166 nonzero), 189 excluded; TC: 1300 compared (135 nonzero), 400 excluded; OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; OpenTaxSolver: 1478 compared (172 nonzero), 222 excluded; UsTaxes: 1031 compared (94 nonzero), 669 excluded; UsTaxes: 1031 compared (94 nonzero), 669 excluded | 23 |
| f8960.bad_allocation | — | — | — | — | — | — | — |

Unasserted lines: f8960.bad_allocation

## Form 8962, Premium Tax Credit (Parts I to III)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8962.zero | — | — | — | — | — | — | — |
| f8962.forms | — | — | — | — | — | — | — |
| f8962.any | — | — | — | — | — | — | — |
| f8962.alloc | — | — | — | — | — | — | — |
| f8962.married_in_2025 | — | — | — | — | — | — | — |
| f8962.marriage | — | — | — | — | — | — | 1 (stage18.married_in_2025_single) |
| f8962.other | — | — | — | — | — | — | — |
| f8962.two_counted | — | — | — | — | — | — | — |
| f8962.same_state_counted | — | — | — | — | — | — | — |
| f8962.deps | — | — | — | — | — | — | 1 (stage18.mut.unclaimed_relative) |
| f8962.line1 | — | — | — | 12 | — | — | 22 |
| f8962.ws1_1 | — | — | — | — | — | — | — |
| f8962.ws1_2 | — | — | — | — | — | — | — |
| f8962.ws1_3 | — | — | — | — | — | — | 1 (stage18.refuse.form_2555) |
| f8962.ws1_4 | — | — | — | — | — | — | — |
| f8962.line2a | — | — | — | 12 | — | — | 21 |
| f8962.line2b | — | — | — | 12 | — | — | 2 (stage18.blind.p15, stage18.mut.unclaimed_relative) |
| f8962.income_total | — | — | — | — | — | — | — |
| f8962.line3 | — | — | — | 12 | — | — | 21 |
| f8962.fpl_table | — | — | — | — | — | — | — |
| f8962.big_family | — | — | — | — | — | — | 1 (stage18.mut.family_of_20) |
| f8962.line4 | — | — | — | 12 | — | — | 22 |
| f8962.line5 | — | — | — | 12 | — | — | 21 |
| f8962.aptc | — | — | — | — | — | — | 1 (stage18.mut.below_100_no_advance) |
| f8962.aptc_total | — | — | — | via f8962.line11f: 1 (classm.f8962.1.deepseek) | — | — | — |
| f8962.estimate_100 | — | — | — | — | — | — | — |
| f8962.applicable | — | — | — | — | — | — | 1 (stage18.mut.below_100_no_advance) |
| f8962.show_applicable | — | — | — | — | — | — | — |
| f8962.filing | — | — | — | — | — | — | — |
| f8962.alien_below | — | — | — | — | — | — | — |
| f8962.alien_branch | — | — | — | — | — | — | — |
| f8962.line7 | — | — | — | 9 | — | — | 19 |
| f8962.line8a | — | — | — | 9; via f8962.line11c: 1 (classm.f8962.1.deepseek) | — | UsTaxes below rule: 36 compared (36 nonzero), 73 excluded | 19 |
| f8962.line8b | — | — | — | 9; via f8962.line12c: 3; via f8962.line13c: 3; via f8962.line14c: 3; via f8962.line15c: 3; via f8962.line16c: 3; via f8962.line17c: 3; via f8962.line18c: 3; via f8962.line19c: 3; via f8962.line20c: 3; via f8962.line21c: 3; via f8962.line22c: 3; via f8962.line23c: 3 | — | — | 19 |
| f8962.line9 | — | — | — | 12 | — | — | — |
| f8962.nonuniform | — | — | — | — | — | — | — |
| f8962.line10 | — | — | — | 12 | — | — | 23 |
| f8962.show_annual | — | — | — | — | — | — | — |
| f8962.show_annual_calc | — | — | — | — | — | — | — |
| f8962.line11a | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | — | 16 |
| f8962.line11b | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | — | 16 |
| f8962.line11c | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | — | 16 |
| f8962.line11d | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | — | 16 |
| f8962.line11e | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | UsTaxes below rule: 36 compared (11 nonzero), 73 excluded | 16 |
| f8962.line11f | — | — | — | 2 (classm.f8962.1.deepseek, classm.f8962.1) | — | — | 17 |
| f8962.show_jan | — | — | — | — | — | — | — |
| f8962.show_jan_calc | — | — | — | — | — | — | — |
| f8962.line12a | — | — | — | 8 | — | — | 3 |
| f8962.line12b | — | — | — | 8 | — | — | 4 |
| f8962.line12c | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line12d | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line12e | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line12f | — | — | — | 10 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.show_feb | — | — | — | — | — | — | — |
| f8962.show_feb_calc | — | — | — | — | — | — | — |
| f8962.line13a | — | — | — | 8 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line13b | — | — | — | 8 | — | — | 3 |
| f8962.line13c | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line13d | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line13e | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line13f | — | — | — | 10 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.show_mar | — | — | — | — | — | — | — |
| f8962.show_mar_calc | — | — | — | — | — | — | — |
| f8962.line14a | — | — | — | 8 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line14b | — | — | — | 8 | — | — | 3 |
| f8962.line14c | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line14d | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line14e | — | — | — | 7 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.line14f | — | — | — | 10 | — | — | 2 (stage18.blind.p10, stage18.blind.p12) |
| f8962.show_apr | — | — | — | — | — | — | — |
| f8962.show_apr_calc | — | — | — | — | — | — | — |
| f8962.line15a | — | — | — | 8 | — | — | 3 |
| f8962.line15b | — | — | — | 8 | — | — | 4 |
| f8962.line15c | — | — | — | 7 | — | — | 3 |
| f8962.line15d | — | — | — | 7 | — | — | 3 |
| f8962.line15e | — | — | — | 7 | — | — | 3 |
| f8962.line15f | — | — | — | 10 | — | — | 3 |
| f8962.show_may | — | — | — | — | — | — | — |
| f8962.show_may_calc | — | — | — | — | — | — | — |
| f8962.line16a | — | — | — | 8 | — | — | 3 |
| f8962.line16b | — | — | — | 8 | — | — | 4 |
| f8962.line16c | — | — | — | 7 | — | — | 3 |
| f8962.line16d | — | — | — | 7 | — | — | 3 |
| f8962.line16e | — | — | — | 7 | — | — | 3 |
| f8962.line16f | — | — | — | 10 | — | — | 3 |
| f8962.show_jun | — | — | — | — | — | — | — |
| f8962.show_jun_calc | — | — | — | — | — | — | — |
| f8962.line17a | — | — | — | 8 | — | — | 3 |
| f8962.line17b | — | — | — | 8 | — | — | 4 |
| f8962.line17c | — | — | — | 7 | — | — | 3 |
| f8962.line17d | — | — | — | 7 | — | — | 3 |
| f8962.line17e | — | — | — | 7 | — | — | 4 |
| f8962.line17f | — | — | — | 10 | — | — | 3 |
| f8962.show_jul | — | — | — | — | — | — | — |
| f8962.show_jul_calc | — | — | — | — | — | — | — |
| f8962.line18a | — | — | — | 8 | — | — | 4 |
| f8962.line18b | — | — | — | 8 | — | — | 6 |
| f8962.line18c | — | — | — | 7 | — | — | 3 |
| f8962.line18d | — | — | — | 7 | — | — | 3 |
| f8962.line18e | — | — | — | 8 | — | — | 4 |
| f8962.line18f | — | — | — | 10 | — | — | 3 |
| f8962.show_aug | — | — | — | — | — | — | — |
| f8962.show_aug_calc | — | — | — | — | — | — | — |
| f8962.line19a | — | — | — | 8 | — | — | 3 |
| f8962.line19b | — | — | — | 8 | — | — | 4 |
| f8962.line19c | — | — | — | 7 | — | — | 3 |
| f8962.line19d | — | — | — | 7 | — | — | 3 |
| f8962.line19e | — | — | — | 8 | — | — | 3 |
| f8962.line19f | — | — | — | 10 | — | — | 3 |
| f8962.show_sep | — | — | — | — | — | — | — |
| f8962.show_sep_calc | — | — | — | — | — | — | — |
| f8962.line20a | — | — | — | 8 | — | — | 3 |
| f8962.line20b | — | — | — | 8 | — | — | 4 |
| f8962.line20c | — | — | — | 7 | — | — | 3 |
| f8962.line20d | — | — | — | 7 | — | — | 3 |
| f8962.line20e | — | — | — | 8 | — | — | 3 |
| f8962.line20f | — | — | — | 10 | — | — | 3 |
| f8962.show_oct | — | — | — | — | — | — | — |
| f8962.show_oct_calc | — | — | — | — | — | — | — |
| f8962.line21a | — | — | — | 8 | — | — | 3 |
| f8962.line21b | — | — | — | 8 | — | — | 4 |
| f8962.line21c | — | — | — | 7 | — | — | 3 |
| f8962.line21d | — | — | — | 7 | — | — | 3 |
| f8962.line21e | — | — | — | 8 | — | — | 3 |
| f8962.line21f | — | — | — | 10 | — | — | 3 |
| f8962.show_nov | — | — | — | — | — | — | — |
| f8962.show_nov_calc | — | — | — | — | — | — | — |
| f8962.line22a | — | — | — | 8 | — | — | 3 |
| f8962.line22b | — | — | — | 8 | — | — | 4 |
| f8962.line22c | — | — | — | 7 | — | — | 3 |
| f8962.line22d | — | — | — | 8 | — | — | 3 |
| f8962.line22e | — | — | — | 8 | — | — | 3 |
| f8962.line22f | — | — | — | 10 | — | — | 3 |
| f8962.show_dec | — | — | — | — | — | — | — |
| f8962.show_dec_calc | — | — | — | — | — | — | — |
| f8962.line23a | — | — | — | 8 | — | — | 3 |
| f8962.line23b | — | — | — | 8 | — | — | 4 |
| f8962.line23c | — | — | — | 7 | — | — | 3 |
| f8962.line23d | — | — | — | 8 | — | — | 3 |
| f8962.line23e | — | — | — | 8 | — | — | 3 |
| f8962.line23f | — | — | — | 10 | — | — | 3 |
| f8962.monthly_e | — | — | — | — | — | — | — |
| f8962.monthly_f | — | — | — | — | — | — | — |
| f8962.allowed | — | — | — | — | — | — | — |
| f8962.line24 | — | — | — | 11 | — | — | 29 |
| f8962.line25 | — | — | — | 12 | — | UsTaxes below rule: 36 compared (26 nonzero), 73 excluded | 28 |
| f8962.net | — | — | — | — | — | — | — |
| f8962.line26 | — | — | — | 4 | — | UsTaxes below rule: 36 compared (6 nonzero), 73 excluded | 19 |
| f8962.excess | — | — | — | — | — | — | — |
| f8962.line27 | — | — | — | 7 | — | — | 5 |
| f8962.repay_200 | — | — | — | — | — | — | — |
| f8962.repay_300 | — | — | — | — | — | — | — |
| f8962.repay_400 | — | — | — | — | — | — | — |
| f8962.show_28 | — | — | — | — | — | — | — |
| f8962.line28 | — | — | — | 6 | — | — | 4 |
| f8962.line29 | — | — | — | 7 | — | UsTaxes below rule: 36 compared (25 nonzero), 73 excluded | 5 |

Unasserted lines: f8962.zero, f8962.forms, f8962.any, f8962.two_counted, f8962.ws1_1, f8962.ws1_2, f8962.ws1_4, f8962.income_total, f8962.show_applicable, f8962.filing, f8962.alien_branch, f8962.nonuniform, f8962.show_annual, f8962.show_annual_calc, f8962.show_jan, f8962.show_jan_calc, f8962.show_feb, f8962.show_feb_calc, f8962.show_mar, f8962.show_mar_calc, f8962.show_apr, f8962.show_apr_calc, f8962.show_may, f8962.show_may_calc, f8962.show_jun, f8962.show_jun_calc, f8962.show_jul, f8962.show_jul_calc, f8962.show_aug, f8962.show_aug_calc, f8962.show_sep, f8962.show_sep_calc, f8962.show_oct, f8962.show_oct_calc, f8962.show_nov, f8962.show_nov_calc, f8962.show_dec, f8962.show_dec_calc, f8962.monthly_e, f8962.monthly_f, f8962.allowed, f8962.net, f8962.excess, f8962.repay_200, f8962.repay_300, f8962.repay_400, f8962.show_28

## Form 8995 — Qualified Business Income Deduction Simplified Computation

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (296 nonzero), 0 excluded | 3 |
| f8995.line3 | — | — | — | 3 | — | — | 1 (stage14.qbi.carryforward) |
| f8995.line4_sum | — | — | — | — | — | — | — |
| f8995.line4 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (259 nonzero), 0 excluded | 2 (stage14.sc.loss, stage14.qbi.carryforward) |
| f8995.line5 | — | — | — | 3 | — | OpenTaxSolver: 517 compared (259 nonzero), 0 excluded | 2 (stage14.sc.basic, stage14.qbi.carryforward) |
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

## Foreign tax credit — election without Form 1116

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ftc.taxes | — | — | — | — | — | — | — |
| ftc.all_passive | — | — | — | — | — | — | — |
| ftc.statements | — | — | — | — | — | — | — |
| ftc.eligible | — | — | — | — | — | — | — |
| ftc.elect | — | — | — | — | — | — | — |
| ftc.limit | — | — | — | — | — | — | — |
| ftc.zero | — | — | — | — | — | — | — |
| ftc.has_tax | — | — | — | — | — | — | 1 (stage4.base) |
| ftc.needs1116 | — | — | — | — | — | — | — |
| ftc.regular_tax | — | — | — | — | — | — | — |
| ftc.limited | — | — | — | — | — | — | — |
| ftc.credit | — | — | — | via f2441.clw2 → s3.line1: 3; via s3.line1: 4 | — | — | 10 |

Unasserted lines: ftc.limit, ftc.zero, ftc.needs1116, ftc.regular_tax, ftc.limited

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
| gift.section_b | — | — | — | 1 (classm.gift.1) | — | — | — |
| gift.allowed | — | — | — | 1 (classm.gift.1) | — | — | — |

## Household facts for dependents and head of household

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| household.persons | — | — | — | — | — | — | — |
| household.taxpayers | — | — | — | — | — | — | — |
| household.spouses | — | — | — | — | — | — | — |
| household.roster_ok | — | — | — | — | — | — | 1 (audit.household.filer_under16) |
| household.roster_bad | — | — | — | — | — | — | — |
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
| household.under16_count | — | — | — | — | — | — | — |
| household.filer_under16 | — | — | — | — | — | — | 1 (audit.household.filer_under16) |
| household.tin_count | — | — | — | — | — | — | — |
| household.all_tin | — | — | — | — | — | — | — |
| household.id_count | — | — | — | — | — | — | — |
| household.ctc_ssn | — | — | — | — | — | — | — |
| household.taxpayer_work_ssn_count | — | — | — | — | — | — | — |
| household.taxpayer_work_ssn | — | — | — | — | — | — | — |
| household.home_cost | — | — | — | — | — | — | — |
| household.unmarried | — | — | — | — | — | — | — |
| household.married | — | — | — | — | — | — | — |
| household.community_property | — | — | — | — | — | — | — |
| household.hoh_community_property | — | — | — | — | — | — | 3 |
| household.credit_disallowed | — | — | — | — | — | — | — |
| household.test1_persons | — | — | — | — | — | — | 24 |
| household.test2_persons | — | — | — | — | — | — | 24 |
| household.test1_met | — | — | — | — | — | — | 25 |
| household.test2_met | — | — | — | — | — | — | 24 |
| household.hoh_eligible | — | — | — | — | — | — | 26 |
| household.hoh_fails | — | — | — | — | — | — | 24 |

Unasserted lines: household.persons, household.taxpayers, household.spouses, household.roster_bad, household.hsa_people, household.hsa_both, household.hsa_split_count, household.hsa_agreed_count, household.work_ssn_count, household.eic_ssn_count, household.under16_count, household.tin_count, household.all_tin, household.id_count, household.ctc_ssn, household.taxpayer_work_ssn_count, household.taxpayer_work_ssn

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
| ira.anyone_covered | — | — | — | — | — | — | — |
| ira.lines2to6 | — | — | — | — | — | — | — |
| ira.cov_gate | — | — | — | — | — | — | — |
| ira.cov_you | — | — | — | — | — | — | — |
| ira.cov_spouse | — | — | — | — | — | — | — |
| ira.line1a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 12 |
| ira.line1b | — | — | — | — | — | — | 4 |
| ira.line2a_sum | — | — | — | — | — | — | — |
| ira.line2b_sum | — | — | — | — | — | — | — |
| ira.line2a | — | — | — | — | — | — | 9 |
| ira.line2b | — | — | — | — | — | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line3 | — | — | — | 1 (classm.ira.2) | — | — | 7 |
| ira.line4 | — | — | — | 1 (classm.ira.2) | — | — | 6 |
| ira.line5 | — | — | — | 1 (classm.ira.2) | — | — | 2 (stage16.mut.ira_joint_full_edge, stage19.mut.ira_single_full_edge) |
| ira.line6a_sum | — | — | — | — | — | — | — |
| ira.line6b_sum | — | — | — | — | — | — | — |
| ira.line6a | — | — | — | 1 (classm.ira.2) | — | — | 8 |
| ira.line6b | — | — | — | 1 (classm.ira.2) | — | — | 2 (stage16.ira.i1, stage16.ira.i8) |
| ira.line7a_sum | — | — | — | — | — | — | — |
| ira.line7b_sum | — | — | — | — | — | — | — |
| ira.line7a | — | — | — | 1 (classm.ira.2) | — | — | 19 |
| ira.line7b | — | — | — | 1 (classm.ira.2) | — | — | 7 |
| ira.wages | — | — | — | — | — | — | — |
| ira.line8 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 10 |
| ira.line9 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 10 |
| ira.line10 | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 16 |
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
| ira.se_capital | — | — | — | — | — | — | — |
| ira.se_capital_gate | — | — | — | — | — | — | — |
| ira.special_gate | — | — | — | — | — | — | — |
| ira.combat_gate | — | — | — | — | — | — | — |
| ira.excl_gate | — | — | — | — | — | — | — |
| ira.line11a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 15 |
| ira.line11b | — | — | — | 1 (classm.ira.2) | — | — | 6 |
| ira.line12a | — | — | — | 2 (classm.ira.1, classm.ira.2) | — | — | 20 |
| ira.line12b | — | — | — | 1 (classm.ira.2) | — | — | 7 |
| ira.total | — | — | — | — | — | E via s1.line20 → ira.line20 (PE) | 1 (stage16.refuse.ira.deduct_less) |
| ira.deduct_less | — | — | — | — | — | — | — |
| ira.less_gate | — | — | — | — | — | — | — |
| ira.line20 | — | — | — | — | — | — | 10 |
| ira.basis_total | — | — | — | — | — | — | — |

Unasserted lines: ira.zero, ira.joint, ira.joint_type, ira.contrib_total, ira.roth_total, ira.any_trad, ira.cov_count, ira.anyone_covered, ira.lines2to6, ira.cov_gate, ira.cov_you, ira.cov_spouse, ira.line2a_sum, ira.line2b_sum, ira.line6a_sum, ira.line6b_sum, ira.line7a_sum, ira.line7b_sum, ira.wages, ira.age50_count, ira.kbh_none, ira.kbh_one, ira.kbh_both, ira.kbh_amount, ira.kbh_short, ira.both_kinds, ira.all_total, ira.over_comp, ira.se_capital_gate, ira.special_gate, ira.combat_gate, ira.excl_gate, ira.less_gate, ira.basis_total

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

## Schedule 1, line 8z — other income, one entry per item listed

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| oi8z.kind | — | — | — | — | — | — | — |
| oi8z.amount | — | — | — | — | — | — | — |
| oi8z.recovery | — | — | — | 1 (classm.oi8z.1) | — | — | — |
| oi8z.additional_tax | — | — | — | 1 (classm.oi8z.1) | — | — | — |
| oi8z.figured | — | — | — | 1 (classm.oi8z.1) | — | — | — |
| oi8z.taxable | — | — | — | 1 (classm.oi8z.1) | — | — | 3 |

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
| person.age65 | — | — | — | — | — | — | — |
| person.blind | — | — | — | — | — | — | — |
| person.tin | — | — | — | — | — | — | — |
| person.itin_applied | — | — | — | — | — | — | — |
| person.work_ssn | — | — | — | — | — | — | — |
| person.eic_ssn | — | — | — | — | — | — | — |
| person.under16 | — | — | — | — | — | — | — |
| person.educator_expenses | — | — | — | — | — | — | — |
| person.eligible_educator | — | — | — | — | — | — | — |
| person.born_before_2001 | — | — | — | — | — | — | — |
| person.born_after_1960 | — | — | — | — | — | — | — |
| person.died_before_65 | — | — | — | — | — | — | — |
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
| person.employers | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.overcount | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.over | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.wages | — | — | — | — | — | — | — |
| person.withheld | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.box1 | — | — | — | — | — | — | — |
| person.box2 | — | — | — | — | — | — | — |
| person.ira_amount_a | — | — | — | — | — | — | — |
| person.ira_taxable | — | — | — | — | — | — | — |
| person.ira_rollovers | — | — | — | — | — | — | — |
| person.plan_amount_a | — | — | — | — | — | — | — |
| person.plan_taxable | — | — | — | — | — | — | — |
| person.plan_rollovers | — | — | — | — | — | — | — |
| person.sav_dist | — | — | — | — | — | — | — |
| person.eligible | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.excess | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.zero | — | — | — | — | — | — | — |
| person.credit | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.medicare5 | — | — | — | — | — | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.medicare6 | — | — | — | — | — | — | 1 (stage16.cleanup.refuse.rrta_medicare) |
| person.sc_count | — | — | — | — | — | — | — |
| person.ho_count | — | — | — | — | — | — | — |
| person.mq_q4 | — | — | — | — | — | — | — |
| person.mq_total | — | — | — | — | — | — | — |
| person.cost179 | — | — | — | — | — | — | — |
| person.s179_nonlisted | — | — | — | — | — | — | — |
| person.s179_listed | — | — | — | — | — | — | — |
| person.income179 | — | — | — | — | — | — | — |
| person.has_sc | — | — | — | — | — | — | — |
| person.sc_total | — | — | — | via person.sep_s1: 1 (classm.person.1.deepseek) | — | — | — |
| person.se_screen | — | — | — | — | — | — | — |
| person.se_screened | — | — | — | — | — | — | — |
| person.se_line2 | — | — | — | — | — | — | 2 (stage14.asset.s179, stage14.refuse.se_screen) |
| person.se_line6 | — | — | — | — | — | OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 4 |
| person.se_line12 | — | — | — | — | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded; OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 11 |
| person.se_line13 | — | — | — | via person.sep_s2: 1 (classm.person.1.deepseek) | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded; OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 1 (stage14.refuse.se_railroad) |
| person.se_line4c | — | — | — | — | — | OpenTaxSolver: 296 compared (238 nonzero), 0 excluded | 2 (stage14.refuse.se_railroad, stage19.mut.se_not_filed_loss) |
| person.plan | — | — | — | — | — | — | — |
| person.plan_screen | — | — | — | — | — | — | — |
| person.plan_screened | — | — | — | — | — | — | — |
| person.cent | — | — | — | — | — | — | — |
| person.hundred | — | — | — | — | — | — | — |
| person.sep_rate | — | — | — | — | — | — | — |
| person.sep_contrib | — | — | — | — | — | — | 1 (stage14.plan.refuse_screen) |
| person.sep_rate_c | — | — | — | — | — | — | — |
| person.sep_rate_plus | — | — | — | — | — | — | — |
| person.sep_s1 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 2 (stage14.sep.step1_other_se_income, stage14.sep.loss_floor) |
| person.sep_s2 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | — |
| person.sep_s3 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 1 (stage14.sep.loss_floor) |
| person.sep_s5 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 3 |
| person.comp_limit | — | — | — | — | — | — | — |
| person.sep_s6 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 1 (stage14.sep.dollar_limit) |
| person.sep_s7 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 2 (stage14.sep.rate_5, stage14.sep.loss_floor) |
| person.sep_s8 | — | — | — | — | — | — | — |
| person.sep_s21 | — | — | — | 2 (classm.person.1.deepseek, classm.person.1) | — | — | 4 |
| person.sep_excess | — | — | — | — | — | — | 1 (stage14.sep.loss_floor) |
| person.sep_deduction | — | — | — | — | — | — | 2 (stage14.sep.refuse_excess, stage14.plan.refuse_two_businesses) |
| person.simple_deferral | — | — | — | — | — | — | 1 (stage14.plan.refuse_screen_simple) |
| person.simple_age | — | — | — | — | — | — | — |
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
| person.simple_excess | — | — | — | — | — | — | — |
| person.simple_deduction | — | — | — | — | — | — | 4 |
| person.plan_deduction | — | — | — | — | — | — | — |
| person.s16 | — | — | — | — | — | — | — |
| person.positive_profits | — | — | — | — | — | — | — |
| person.sehi | — | — | — | — | — | — | — |
| person.qbi | — | — | — | — | — | — | — |
| person.eic_part1 | — | — | — | — | — | — | — |
| person.files_se | — | — | — | — | — | — | 1 (stage19.mut.se_not_filed_loss) |
| person.eic_se_has | — | — | — | — | — | — | — |
| person.eic_se | — | — | — | — | — | — | — |
| person.sc_1a | — | — | — | — | — | — | — |
| person.dc_benefits | — | — | — | — | — | — | — |
| person.dc_box10 | — | — | — | — | — | — | — |
| person.dc_has_box10 | — | — | — | — | — | — | — |
| person.dc_1e_mine | — | — | — | — | — | — | — |
| person.dc_1e_counted | — | — | — | — | — | — | — |
| person.dc_zero | — | — | — | — | — | — | — |
| person.dc_1e | — | — | — | — | — | — | — |
| person.dc_earned | — | — | — | — | — | — | — |
| person.dc_earned_b | — | — | — | — | — | — | — |
| person.sav_born | — | — | — | — | — | — | — |
| person.sav_student | — | — | — | — | — | — | — |
| person.sav_claimed | — | — | — | — | — | — | — |
| person.sav_ineligible | — | — | — | — | — | — | — |
| person.sav_trad | — | — | — | — | — | — | — |
| person.sav_able | — | — | — | — | — | — | — |
| person.sav_roth | — | — | — | — | — | — | — |
| person.sav_line1 | — | — | — | — | — | — | 2 (stage15.refuse.person.sav_able, stage16.refuse.person.ira_excess) |
| person.sav_w2 | — | — | — | — | — | — | — |
| person.sav_excess | — | — | — | — | — | — | — |
| person.sav_excess_gate | — | — | — | — | — | — | — |
| person.sav_voluntary | — | — | — | — | — | — | — |
| person.sav_simple_plan | — | — | — | — | — | — | — |
| person.sav_simple | — | — | — | — | — | — | — |
| person.sav_line2 | — | — | — | — | — | — | 1 (stage15.refuse.person.sav_excess) |
| person.sav_prior_joint | — | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.sav_prior_other | — | — | — | — | — | — | 1 (stage15.refuse.person.sav_able) |
| person.ira_trad | — | — | — | — | — | — | — |
| person.ira_contrib | — | — | — | — | — | — | — |
| person.ira_has | — | — | — | — | — | — | — |
| person.ira_any_contrib | — | — | — | — | — | — | — |
| person.ira_excess | — | — | — | — | — | — | — |
| person.ira_excess_gate | — | — | — | — | — | — | — |
| person.ira_age50 | — | — | — | — | — | — | — |
| person.ira_work_plan | — | — | — | — | — | — | — |
| person.ira_se_plan | — | — | — | — | — | — | — |
| person.ira_cov | — | — | — | — | — | — | — |
| person.ira_limit_under50 | — | — | — | — | — | — | — |
| person.ira_limit_over50 | — | — | — | — | — | — | — |
| person.ira_limit | — | — | — | — | — | — | — |
| person.ira_not_covered_joint | — | — | — | — | — | — | — |
| person.ira_line2_status | — | — | — | — | — | — | — |
| person.ira_line2_nc | — | — | — | — | — | — | — |
| person.ira_line2 | — | — | — | — | — | — | — |
| person.ira_line6 | — | — | — | — | — | — | 2 (audit.ira.covered_age50_single_phaseout, audit.ira.covered_age50_joint_phaseout) |
| person.ira_line6_yes | — | — | — | — | — | — | — |
| person.ira_wide | — | — | — | — | — | — | — |
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
| person.ira_line11 | — | — | — | — | — | — | 8 |
| person.ira_7or10 | — | — | — | — | — | — | — |
| person.ira_line12 | — | — | — | — | — | — | 1 (stage16.refuse.ira.dist) |
| person.ira_deduction | — | — | — | — | — | — | 1 (stage16.refuse.ira.dist) |
| person.ira_10or11 | — | — | — | — | — | — | — |
| person.ira_nd_figured | — | — | — | — | — | — | — |
| person.ira_nondeductible | — | — | — | — | — | — | — |
| person.ira_files_8606 | — | — | — | — | — | — | — |
| person.ira_basis | — | — | — | — | — | — | — |
| person.ira_basis_adjusted | — | — | — | — | — | — | — |
| person.ira_basis_gate | — | — | — | — | — | — | — |
| person.ira_8606_line2 | — | — | — | — | — | — | 1 (stage16.refuse.person.ira_basis_adjusted) |
| person.ira_dist | — | — | — | — | — | — | — |
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
| person.edu_student | — | — | — | — | — | — | — |
| person.edu_inst | — | — | — | — | — | — | — |
| person.edu_mat | — | — | — | — | — | — | — |
| person.edu_a2025 | — | — | — | — | — | — | — |
| person.edu_a2026 | — | — | — | — | — | — | — |
| person.edu_refunds | — | — | — | — | — | — | — |
| person.edu_adj_sum | — | — | — | — | — | — | — |
| person.edu_adj | — | — | — | — | — | — | — |
| person.edu_over | — | — | — | — | — | — | — |
| person.edu_over_refused | — | — | — | — | — | — | — |
| person.edu_line23 | — | — | — | — | — | — | 9 |
| person.edu_show24 | — | — | — | — | — | — | — |
| person.edu_line24 | — | — | — | — | — | — | 9 |
| person.edu_show25 | — | — | — | — | — | — | — |
| person.edu_line25 | — | — | — | — | — | — | 7 |
| person.edu_show26 | — | — | — | — | — | — | — |
| person.edu_line26 | — | — | — | — | — | — | 6 |
| person.edu_ein | — | — | — | — | — | — | — |
| person.edu_aoc | — | — | — | — | — | — | — |
| person.edu_llc | — | — | — | — | — | — | — |
| person.edu_line27 | 7 | — | — | — | — | — | 7 |
| person.edu_line28 | — | — | — | — | — | — | 7 |
| person.edu_line29 | — | — | — | — | — | — | 7 |
| person.edu_line30 | 1 (stage19.example.aoc_phaseout) | — | — | — | — | — | 7 |
| person.edu_line31 | 2 (stage19.example.bruce_toni, stage19.example.llc_phaseout) | — | — | — | — | — | 5 |
| person.edu_born_2007 | — | — | — | — | — | — | — |
| person.edu_born_2002 | — | — | — | — | — | — | — |
| person.edu_fulltime | — | — | — | — | — | — | — |
| person.edu_half_support | — | — | — | — | — | — | — |
| person.edu_parent | — | — | — | — | — | — | — |
| person.edu_kid | — | — | — | — | — | — | — |
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
| person.x_c05 | — | — | — | — | — | — | — |
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
| person.x_hsa_value | — | — | — | — | — | — | — |
| person.x_hsa_excess | — | — | — | via f5329.l47: 3; via f5329.l48 → f5329.l47: 3 | — | — | — |

Unasserted lines: person.one, person.educator_max, person.has_educator_expenses, person.educator_limited, person.educator_eligible_amount, person.educator_deduction, person.hsa_forms, person.hsa_repeated, person.hsa_split, person.hsa_agreed, person.hsa_deduction, person.hsa_taxable, person.hsa_addtax, person.tip_employers, person.tip_total, person.tip_reported, person.ot_employers, person.ot_total, person.sc_rrta_count, person.se_rrta, person.wages, person.box1, person.box2, person.ira_amount_a, person.ira_taxable, person.ira_rollovers, person.plan_amount_a, person.plan_taxable, person.plan_rollovers, person.sav_dist, person.zero, person.sc_count, person.ho_count, person.mq_q4, person.mq_total, person.cost179, person.s179_nonlisted, person.s179_listed, person.income179, person.has_sc, person.se_screened, person.plan_screened, person.cent, person.hundred, person.sep_rate_c, person.sep_rate_plus, person.comp_limit, person.sep_s8, person.simple_cap, person.simple_regular, person.simple_catchup, person.catchup_limit, person.comp_after_regular, person.rate3, person.rate2, person.match_3pct, person.deferrals_total, person.ne_comp, person.employer_max, person.simple_excess, person.plan_deduction, person.s16, person.positive_profits, person.sehi, person.qbi, person.eic_part1, person.eic_se_has, person.eic_se, person.sc_1a, person.dc_benefits, person.dc_box10, person.dc_has_box10, person.dc_1e_mine, person.dc_1e_counted, person.dc_zero, person.dc_1e, person.dc_earned, person.dc_earned_b, person.sav_ineligible, person.sav_w2, person.sav_excess_gate, person.sav_simple_plan, person.sav_simple, person.ira_contrib, person.ira_has, person.ira_any_contrib, person.ira_excess_gate, person.ira_se_plan, person.ira_cov, person.ira_limit_under50, person.ira_limit_over50, person.ira_limit, person.ira_not_covered_joint, person.ira_line2_status, person.ira_line2_nc, person.ira_line2, person.ira_line6_yes, person.ira_wide, person.ira_full_narrow, person.ira_full_joint, person.ira_full, person.ira_at_full, person.ira_p70, person.ira_p80, person.ira_p35, person.ira_p40, person.ira_prod_wide, person.ira_prod_joint, person.ira_min, person.ira_floor, person.ira_below, person.ira_line7_figured, person.ira_line7, person.ira_over_limit, person.ira_own_total, person.ira_7or10, person.ira_10or11, person.ira_nd_figured, person.ira_nondeductible, person.ira_files_8606, person.ira_basis_gate, person.ira_dist_gate, person.ira_8606_line14, person.ira_se_take, person.ira_se_figured, person.ira_se, person.edu_student, person.edu_adj_sum, person.edu_adj, person.edu_over_refused, person.edu_show24, person.edu_show25, person.edu_show26, person.edu_aoc, person.edu_llc, person.edu_kid, person.x_l2_all, person.x_l1_s, person.x_l2_s, person.x_e05, person.x_e09, person.x_e19, person.x_e22, person.x_e23, person.x_tax, person.x_must, person.x_cap09_base, person.x_cap09, person.x_cap19_one, person.x_cap19, person.x_cap22, person.x_cap23, person.x_c05, person.x_has05, person.x_c05_min, person.x_has09, person.x_c09_min, person.x_c09, person.x_has19, person.x_c19_min, person.x_c19, person.x_c22, person.x_c23, person.x_n23, person.x_two23, person.x_capped_sum, person.x_limited_sum, person.x_other_exc, person.x_limit_binds

## Qualified business income and section 199A dividends — amounts and the choice of Form 8995

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| qbi.dividends | — | — | — | — | — | E via f8995.line8 → f8995.line6 → qbi.eligible (OpenTaxSolver) | — |
| qbi.unsupported | — | — | — | — | — | — | — |
| qbi.zero | — | — | — | — | — | — | — |
| qbi.eligible | — | — | — | — | — | — | — |
| qbi.carryforward | — | — | — | — | — | — | — |
| qbi.business_any | — | — | — | — | — | — | — |
| qbi.via_8995a | — | — | — | — | — | — | 1 (stage14.refuse.qbi_8995a) |
| qbi.deductions_before | — | — | — | — | — | — | — |
| qbi.taxable_before | — | — | — | — | — | E via f8995.line11 (OpenTaxSolver) | 2 (stage4.qbi.income_limit, stage4.qbi.zero_income) |
| qbi.net_capital_gain | — | — | — | — | — | — | — |
| qbi.threshold | — | — | — | — | — | — | — |
| qbi.use_8995a | — | — | — | — | — | — | 3 |
| qbi.deduction | — | — | — | via f1040.line13a: 6 | — | OpenTaxSolver: 387 compared (329 nonzero), 130 excluded; E via f1040.line13a (PE, OpenTaxSolver) | 11 |

Unasserted lines: qbi.zero, qbi.eligible, qbi.business_any, qbi.deductions_before, qbi.net_capital_gain, qbi.threshold

## Qualified Dividends and Capital Gain Tax Worksheet—Line 16

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| qdcg.schedule_d_filed | — | — | — | — | — | — | 12 |
| qdcg.schedule_d_net_gain | — | — | — | — | — | — | 1 (qdcg.sd.side) |
| qdcg.line1 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 58 |
| qdcg.line2 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (607 nonzero), 313 excluded; UsTaxes below rule: 515 compared (371 nonzero), 555 excluded | 58 |
| qdcg.line3 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (386 nonzero), 313 excluded; UsTaxes below rule: 515 compared (290 nonzero), 555 excluded | 15 |
| qdcg.line4 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes below rule: 515 compared (515 nonzero), 555 excluded | 12 |
| qdcg.line5 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 515 compared (453 nonzero), 555 excluded | 12 |
| qdcg.line6 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes below rule: 515 compared (515 nonzero), 555 excluded | 58 |
| qdcg.line7 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 58 |
| qdcg.line8 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 515 compared (453 nonzero), 555 excluded | 12 |
| qdcg.line9 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (378 nonzero), 313 excluded; UsTaxes below rule: 515 compared (205 nonzero), 555 excluded; E via qdcg.line11 (OpenTaxSolver) | 12 |
| qdcg.line10 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 12 |
| qdcg.line11 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (378 nonzero), 313 excluded; UsTaxes below rule: 515 compared (205 nonzero), 555 excluded | 12 |
| qdcg.line12 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 515 compared (279 nonzero), 555 excluded | 12 |
| qdcg.line13 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes below rule: 515 compared (515 nonzero), 555 excluded | 58 |
| qdcg.line14 | 1 (example.official) | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 58 |
| qdcg.line15 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 12 |
| qdcg.line16 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 515 compared (279 nonzero), 555 excluded | 12 |
| qdcg.line17 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 515 compared (279 nonzero), 555 excluded | 12 |
| qdcg.line18 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (410 nonzero), 313 excluded; UsTaxes: 515 compared (279 nonzero), 555 excluded | 12 |
| qdcg.line19 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (756 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 12 |
| qdcg.line20 | — | — | — | 3 | — | OpenTaxSolver below rule: 793 compared (0 nonzero), 313 excluded; UsTaxes below rule: 515 compared (0 nonzero), 555 excluded | 12 |
| qdcg.line21 | — | — | — | 3 | — | OpenTaxSolver below rule: 793 compared (0 nonzero), 313 excluded; UsTaxes below rule: 515 compared (0 nonzero), 555 excluded | 12 |
| qdcg.line22 | — | — | — | — | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 515 compared (453 nonzero), 555 excluded | 13 |
| qdcg.line23 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 515 compared (453 nonzero), 555 excluded | 13 |
| qdcg.line24 | 1 (example.official) | — | — | — | — | OpenTaxSolver: 793 compared (793 nonzero), 313 excluded; UsTaxes: 515 compared (468 nonzero), 555 excluded | 59 |
| qdcg.line25 | — | — | — | 3 | — | OpenTaxSolver: 793 compared (770 nonzero), 313 excluded; UsTaxes: 515 compared (453 nonzero), 555 excluded | 13 |

## State and Local Income Tax Refund Worksheet—Schedule 1, Line 1

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refund.zero | — | — | — | — | — | — | — |
| refund.received | — | — | — | — | — | — | — |
| refund.has | — | — | — | — | — | — | — |
| refund.box8 | — | — | — | — | — | — | — |
| refund.not_2024 | — | — | — | — | — | — | — |
| refund.itemized | — | — | — | — | — | — | — |
| refund.sales | — | — | — | — | — | — | — |
| refund.worksheet | — | — | — | — | — | — | — |
| refund.exc_tax | — | — | — | — | — | — | — |
| refund.exc_who | — | — | — | — | — | — | — |
| refund.line5d_2024 | — | — | — | — | — | — | — |
| refund.line5e_2024 | — | — | — | — | — | — | — |
| refund.line5e_bad | — | — | — | — | — | — | — |
| refund.line1 | — | — | — | 1 (classm.refund.1) | — | — | 12 |
| refund.line2_more | — | — | — | — | — | — | 2 (stage16.mut.refund_single_unasked, stage16.mut.refund_line3_stop) |
| refund.line2 | — | — | — | — | — | — | 5 |
| refund.line3_more | — | — | — | — | — | — | 1 (stage16.mut.refund_line3_stop) |
| refund.line3 | — | — | — | 1 (classm.refund.1) | — | — | 9 |
| refund.line17_2024 | — | — | — | — | — | — | — |
| refund.line4 | — | — | — | 1 (classm.refund.1) | — | — | 8 |
| refund.status | — | — | — | — | — | — | — |
| refund.mfs_spouse_itemized | — | — | — | — | — | — | — |
| refund.std_single | — | — | — | — | — | — | — |
| refund.std_joint | — | — | — | — | — | — | — |
| refund.std_hoh | — | — | — | — | — | — | — |
| refund.line5 | — | — | — | 1 (classm.refund.1) | — | — | 8 |
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
| refund.line6 | — | — | — | 1 (classm.refund.1) | — | — | 8 |
| refund.line7 | — | — | — | 1 (classm.refund.1) | — | — | 8 |
| refund.line8_figured | — | — | — | — | — | — | — |
| refund.line8 | — | — | — | — | — | — | 7 |
| refund.line8_mfs | — | — | — | — | — | — | — |
| refund.line9_figured | — | — | — | — | — | — | — |
| refund.line9 | — | — | — | — | — | — | 8 |
| refund.taxable | — | — | — | — | — | — | 4 |

Unasserted lines: refund.zero, refund.has, refund.worksheet, refund.line5e_bad, refund.std_single, refund.std_joint, refund.std_hoh, refund.box_married, refund.box_unmarried, refund.per_box, refund.spouse_boxes, refund.amt_you_born, refund.amt_you_blind, refund.amt_spouse_born, refund.amt_spouse_born_checked, refund.amt_spouse_blind, refund.amt_spouse_blind_checked, refund.line8_figured, refund.line8_mfs, refund.line9_figured

## Form 1099-R distributions (IRAs, pensions and annuities)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| retirement.account | — | — | — | — | — | — | — |
| retirement.code | — | — | — | — | — | — | — |
| retirement.box1 | — | — | — | via retirement.smw1: 5 | — | — | — |
| retirement.box5 | — | — | — | — | — | — | — |
| retirement.rollover | — | — | — | — | — | — | — |
| retirement.special | — | — | — | — | — | — | — |
| retirement.annuity | — | — | — | — | — | — | — |
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
| retirement.smw_shown | — | — | — | — | — | — | 2 (stage21.t067.smw_hidden_ira, stage21.t067.smw_hidden_cost_recovered) |
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
| retirement.smw4 | — | — | — | 10 | — | — | 4 |
| retirement.smw5 | — | — | — | 10 | — | — | 3 |
| retirement.smw6 | — | — | — | 10 | — | — | — |
| retirement.smw7 | — | — | — | 10 | — | — | — |
| retirement.smw8 | — | — | — | 10 | — | — | 1 (stage10.smw.cost_nearly_recovered) |
| retirement.smw9 | — | — | — | 10 | — | — | — |
| retirement.smw10 | — | — | — | 10 | — | — | 4 |
| retirement.smw11 | — | — | — | 10 | — | — | 4 |
| retirement.cost_left | — | — | — | — | — | — | — |
| retirement.annuity_with_cost | — | — | — | — | — | — | — |
| retirement.annuity_rollover | — | — | — | — | — | — | — |
| retirement.annuity_taxable | — | — | — | — | — | — | — |
| retirement.ira_taxable | — | — | — | — | — | — | — |
| retirement.ira_not_rolled | — | — | — | — | — | — | — |
| retirement.plan_excluded | — | — | — | — | — | — | — |
| retirement.plan_simple | — | — | — | — | — | — | — |
| retirement.plan_taxable | — | — | — | — | — | — | — |
| retirement.taxable | — | — | — | — | — | — | — |
| retirement.show_a | — | — | — | — | — | — | — |
| retirement.amount_a | — | — | — | — | — | — | 1 (stage16.cleanup.refuse.retirement.special_first) |
| retirement.sav_military | — | — | — | — | — | — | — |
| retirement.sav_404k | — | — | — | — | — | — | — |
| retirement.sav_inherited | — | — | — | — | — | — | — |
| retirement.sav_excluded | — | — | — | — | — | — | — |
| retirement.sav_gross | — | — | — | — | — | — | — |
| retirement.sav_amount | — | — | — | — | — | — | — |
| retirement.early | — | — | — | — | — | — | — |
| retirement.early_screen | — | — | — | — | — | — | — |
| retirement.code_screen | — | — | — | — | — | — | — |
| retirement.screen_refused | — | — | — | — | — | — | — |
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

Unasserted lines: retirement.zero, retirement.one, retirement.is_ira, retirement.roth, retirement.direct, retirement.bad_code, retirement.rolled, retirement.has_rollover, retirement.smw4_t1_360, retirement.smw4_t1_310, retirement.smw4_t1_260, retirement.smw4_t1_210, retirement.smw4_t1_160, retirement.smw4_t2_410, retirement.smw4_t2_360, retirement.smw4_t2_310, retirement.smw4_t2_260, retirement.smw4_t2_210, retirement.smw4_table1, retirement.smw4_table2, retirement.smw4_new, retirement.cost_left, retirement.annuity_with_cost, retirement.annuity_rollover, retirement.annuity_taxable, retirement.ira_taxable, retirement.ira_not_rolled, retirement.plan_excluded, retirement.plan_simple, retirement.plan_taxable, retirement.taxable, retirement.show_a, retirement.sav_excluded, retirement.sav_gross, retirement.sav_amount, retirement.early, retirement.screen_refused, retirement.has_exception, retirement.wrong_kind, retirement.l1, retirement.exc_capped, retirement.l2, retirement.is_e05, retirement.l2_e05, retirement.is_e09, retirement.l2_e09, retirement.is_e19, retirement.l2_e19, retirement.is_e22, retirement.l2_e22, retirement.is_e23, retirement.l2_e23, retirement.is_s, retirement.l1_s, retirement.l2_s

## Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s1.zero | — | — | — | — | — | — | — |
| s1.line1 | — | — | — | 3 | — | — | 17 |
| s1.uc_paid | — | — | — | — | — | — | — |
| s1.has_uc | — | — | — | — | — | — | — |
| s1.uc_repaid | — | — | — | — | — | — | — |
| s1.uc_unsupported | — | — | — | — | — | — | — |
| s1.line7_figured | — | — | — | — | — | — | — |
| s1.line7 | — | — | — | 3 | — | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_box | — | — | — | 3 | — | — | 2 (stage11.uc.basic, stage11.uc.repaid) |
| s1.line7_repaid | — | — | — | 1 (classm.s1.2) | — | — | 1 (stage11.uc.repaid) |
| s1.ebl_loss | — | — | — | — | — | — | — |
| s1.ebl_total | — | — | — | — | — | — | — |
| s1.zero_ebl | — | — | — | — | — | — | — |
| s1.ebl_threshold | — | — | — | — | — | — | — |
| s1.ebl | — | — | — | — | — | — | — |
| s1.sc_count | — | — | — | — | — | — | — |
| s1.has_sc | — | — | — | — | — | — | — |
| s1.sc_1a_count | — | — | — | — | — | — | — |
| s1.sc_1a | — | — | — | — | — | — | — |
| s1.line3 | — | — | — | 3 | — | — | 12 |
| s1.line8_other | — | — | — | — | — | — | — |
| s1.gambling_winnings | — | — | — | — | — | — | — |
| s1.has_gambling | — | — | — | — | — | — | — |
| s1.gambling_pro | — | — | — | — | — | — | — |
| s1.gambling_business | — | — | — | — | — | — | — |
| s1.line8b | — | — | — | 3 | — | — | 6 |
| s1.line8g | — | — | — | — | — | — | 1 (stage16.other.o4) |
| s1.line8h | — | — | — | — | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line8i | — | — | — | — | — | — | 1 (stage16.other.o6) |
| s1.line8j | — | — | — | — | — | — | 1 (stage16.other.o7) |
| s1.line8r | 1 (stage19.example.bill.ex3) | — | — | — | — | — | 1 (stage16.other.o8) |
| s1.line8z | — | — | — | 3 | — | — | 4 |
| s1.alimony | — | — | — | — | — | — | — |
| s1.alimony_received | — | — | — | — | — | — | — |
| s1.alimony_paid | — | — | — | — | — | — | — |
| s1.alimony_unsupported | — | — | — | — | — | — | — |
| s1.alimony_refused | — | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_received) |
| s1.line2a | — | — | — | 3 | — | — | 4 |
| s1.line2b_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.cod_any | — | — | — | — | — | — | — |
| s1.cod_amount | — | — | — | — | — | — | — |
| s1.has_cod | — | — | — | — | — | — | — |
| s1.cod_unsupported | — | — | — | — | — | — | — |
| s1.cod_refused | — | — | — | — | — | — | 2 (stage16.refuse.s1.cod_unsupported, stage20.refuse.excluded_canceled_debt) |
| s1.cod_figured | — | — | — | — | — | — | — |
| s1.line8c | — | — | — | 3 | — | — | 5 |
| s1.line8f | — | — | — | 3 | — | — | 8 |
| s1.line9 | — | — | — | 3 | — | OpenTaxSolver below rule: 1700 compared (0 nonzero), 0 excluded | 24 |
| s1.line10 | — | — | — | 3; via f1040.line8: 6 | — | OpenTaxSolver: 1700 compared (576 nonzero), 0 excluded; UsTaxes below rule: 1400 compared (280 nonzero), 300 excluded; E via f1040.line8 (OpenTaxSolver) | 44 |
| s1.line11 | — | — | — | 3 | — | UsTaxes: 1400 compared (146 nonzero), 300 excluded | 5 |
| s1.line13 | — | — | — | 3 | — | UsTaxes: 1316 compared (137 nonzero), 384 excluded | 21 |
| s1.line15 | — | — | — | 3; via s8812.line22: 2 (classm.s8812.2.deepseek, classm.s8812.4.deepseek); via s8812.clwb_8 → s8812.line22: 1 (classm.s8812.4.deepseek) | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 9 |
| s1.line16 | — | — | — | 3 | — | — | 10 |
| s1.line17 | — | — | — | 3 | — | — | 3 |
| s1.line18 | — | — | — | 3; via f8960.line10: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek) | — | — | 2 (stage16.small.s1, stage16.small.s10) |
| s1.paid_refused | — | — | — | — | — | — | 1 (stage16.refuse.s1.alimony_paid) |
| s1.line19a | — | — | — | 3 | — | — | 4 |
| s1.line19b_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line19c_notice | — | — | — | — | — | — | 2 (stage16.mut.ira_alimony_comp, stage16.mut.alimony_paid) |
| s1.line20 | — | — | — | 3 | — | PE: 1640 compared (504 nonzero), 19 excluded | 31 |
| s1.line21 | — | — | — | 3 | — | OpenTaxSolver: 1589 compared (127 nonzero), 111 excluded; UsTaxes: 1153 compared (94 nonzero), 547 excluded | 2 (stage11.sli.basic, stage11.refuse.sli_pub970) |
| s1.jury_to_employer | — | — | — | — | — | — | — |
| s1.jury_over | — | — | — | — | — | — | — |
| s1.line24a | — | — | — | 3 | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line25 | — | — | — | 3 | — | — | 2 (stage16.other.o5, stage16.refuse.s1.jury_over) |
| s1.line26 | — | — | — | 3; via f1040.line10: 6 | — | OpenTaxSolver: 1589 compared (955 nonzero), 111 excluded; UsTaxes: 1153 compared (587 nonzero), 547 excluded; E via f1040.line10 (PE, TC, OpenTaxSolver, UsTaxes) | 19 |

Unasserted lines: s1.zero, s1.has_uc, s1.line7_figured, s1.ebl_loss, s1.ebl_total, s1.zero_ebl, s1.ebl_threshold, s1.ebl, s1.sc_count, s1.has_sc, s1.sc_1a_count, s1.sc_1a, s1.has_gambling, s1.gambling_business, s1.has_cod, s1.cod_figured, s1.jury_over

## Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s179.line2 | — | — | — | 4 | — | — | 2 (stage14.asset.partial_use, stage14.asset.low_use_nonlisted) |
| s179.max | — | — | — | — | — | — | — |
| s179.line1 | — | — | — | 1 (classm.s179.2) | — | — | 2 (stage14.s179.carryover_no_property, stage14.s179.dollar_limit) |
| s179.line3 | — | — | — | 4 | — | — | — |
| s179.line4 | — | — | — | 4 | — | — | 3 |
| s179.line5_full | — | — | — | — | — | — | — |
| s179.separate | — | — | — | — | — | — | — |
| s179.line5_mfs | — | — | — | — | — | — | — |
| s179.line5 | — | — | — | 1 (classm.s179.2) | — | — | 9 |
| s179.mfs | — | — | — | — | — | — | 1 (stage14.s179.mfs_no_election) |
| s179.line6 | — | — | — | 1 (classm.s179.4) | — | — | — |
| s179.line7 | — | — | — | 1 (classm.s179.4) | — | — | — |
| s179.line8 | — | — | — | 1 (classm.s179.4) | — | — | — |
| s179.over_limit | — | — | — | — | — | — | — |
| s179.line9 | — | — | — | 1 (classm.s179.4) | — | — | 3 |
| s179.show10 | — | — | — | — | — | — | 1 (stage14.s179.zero_limit_carryover) |
| s179.line10 | — | — | — | — | — | — | — |
| s179.income_sc | — | — | — | — | — | — | — |
| s179.income | — | — | — | — | — | — | — |
| s179.income0 | — | — | — | — | — | — | — |
| s179.line11 | — | — | — | 1 (classm.s179.4) | — | — | 5 |
| s179.line9_10 | — | — | — | — | — | — | — |
| s179.line12 | — | — | — | 4 | — | — | 12 |
| s179.sc_count | — | — | — | — | — | — | — |
| s179.orphan | — | — | — | — | — | — | — |
| s179.line13 | — | — | — | 4 | — | — | 9 |
| s179.differs | — | — | — | — | — | — | — |
| s179.multi | — | — | — | — | — | — | — |

Unasserted lines: s179.max, s179.line5_full, s179.separate, s179.line5_mfs, s179.over_limit, s179.income_sc, s179.income, s179.income0, s179.line9_10, s179.sc_count, s179.orphan, s179.differs, s179.multi

## Schedule 1-A (Form 1040) — Additional Deductions

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s1a.zero | — | — | — | — | — | — | — |
| s1a.line1 | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line2a | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line2b | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line2c | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line2d | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line2e | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line3 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1153 compared (1153 nonzero), 547 excluded | 1 (stage12.tips.one_employer) |
| s1a.tips | — | — | — | — | — | — | — |
| s1a.tip_employers | — | — | — | — | — | — | — |
| s1a.tip_total | — | — | — | — | — | — | — |
| s1a.tip_reported | — | — | — | — | — | — | — |
| s1a.tip_multi | — | — | — | — | — | — | — |
| s1a.tip_ssn_count | — | — | — | — | — | — | — |
| s1a.tip_ssn | — | — | — | — | — | — | — |
| s1a.part2 | — | — | — | — | — | — | — |
| s1a.line4a_calc | — | — | — | — | — | — | — |
| s1a.line4a | — | — | — | 1 (classm.s1a.1) | — | — | 5 |
| s1a.line4b_calc | — | — | — | — | — | — | — |
| s1a.line4b | — | — | — | 1 (classm.s1a.1) | — | — | 1 (stage12.tips.one_employer) |
| s1a.line4c_one | — | — | — | — | — | — | — |
| s1a.line4c_calc | — | — | — | — | — | — | — |
| s1a.line4c | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 7 |
| s1a.line5_calc | — | — | — | — | — | — | 2 (stage14.refuse.sch1a_tips, stage14.sch1a.tips_with_sc) |
| s1a.line5 | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line6_calc | — | — | — | — | — | — | — |
| s1a.line6 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 2 (stage12.tips.cap, stage12.refuse.tips_trade_or_business) |
| s1a.line7_calc | — | — | — | — | — | — | — |
| s1a.line7 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1400 compared (159 nonzero), 300 excluded | 4 |
| s1a.tips_max | — | — | — | — | — | — | — |
| s1a.base_other | — | — | — | — | — | — | — |
| s1a.base_joint | — | — | — | — | — | — | — |
| s1a.line8_calc | — | — | — | — | — | — | — |
| s1a.line8 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 135 compared (135 nonzero), 24 excluded | 1 (stage13.tips_only_spouse_no_ssn) |
| s1a.line9_calc | — | — | — | — | — | — | — |
| s1a.line9 | — | — | — | 1 (classm.s1a.1) | — | — | 1 (stage12.mfj.tips_overtime) |
| s1a.line10_calc | — | — | — | — | — | — | — |
| s1a.line10 | — | — | — | 1 (classm.s1a.1) | — | — | 3 |
| s1a.line10_over | — | — | — | — | — | — | — |
| s1a.line10_pos | — | — | — | — | — | — | — |
| s1a.line11_thousands | — | — | — | — | — | — | — |
| s1a.line12_calc | — | — | — | — | — | — | — |
| s1a.line12 | — | — | — | — | — | UsTaxes below rule: 135 compared (20 nonzero), 24 excluded | 5 |
| s1a.line13_figured | — | — | — | — | — | — | — |
| s1a.line13_amount | — | — | — | — | — | — | — |
| s1a.line13_ssn | — | — | — | — | — | — | — |
| s1a.line13_claim | — | — | — | — | — | — | — |
| s1a.line13 | — | — | — | 1 (classm.s1a.1) | — | PE: 1554 compared (163 nonzero), 143 excluded; TC: 1370 compared (168 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (190 nonzero), 111 excluded; UsTaxes: 1153 compared (132 nonzero), 547 excluded | 20 |
| s1a.overtime | — | — | — | — | — | — | — |
| s1a.ot_ssn_count | — | — | — | — | — | — | — |
| s1a.ot_ssn | — | — | — | — | — | — | — |
| s1a.part3 | — | — | — | — | — | — | — |
| s1a.line14a_calc | — | — | — | — | — | — | — |
| s1a.line14a | — | — | — | 1 (classm.s1a.1) | — | — | 11 |
| s1a.line14b_calc | — | — | — | — | — | — | 1 (stage14.sch1a.refuse_overtime_1099) |
| s1a.line14b | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line14c_calc | — | — | — | — | — | — | — |
| s1a.line14c | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1400 compared (160 nonzero), 300 excluded | 2 (stage12.ot.premium, stage12.refuse.overtime_nonemployee) |
| s1a.ot_max_other | — | — | — | — | — | — | — |
| s1a.ot_max_joint | — | — | — | — | — | — | — |
| s1a.ot_max | — | — | — | — | — | — | — |
| s1a.line15_calc | — | — | — | — | — | — | — |
| s1a.line15 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 1400 compared (160 nonzero), 300 excluded | 4 |
| s1a.line16_calc | — | — | — | — | — | — | — |
| s1a.line16 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 126 compared (126 nonzero), 34 excluded | 1 (stage13.overtime_only_spouse_no_ssn) |
| s1a.line17_calc | — | — | — | — | — | — | — |
| s1a.line17 | — | — | — | 1 (classm.s1a.1) | — | — | — |
| s1a.line18_calc | — | — | — | — | — | — | — |
| s1a.line18 | — | — | — | 1 (classm.s1a.1) | — | — | 1 (stage12.ot.phaseout) |
| s1a.line18_over | — | — | — | — | — | — | — |
| s1a.line18_pos | — | — | — | — | — | — | — |
| s1a.line19_thousands | — | — | — | — | — | — | — |
| s1a.line20_calc | — | — | — | — | — | — | — |
| s1a.line20 | — | — | — | — | — | UsTaxes below rule: 126 compared (26 nonzero), 34 excluded | 2 (stage12.ot.phaseout, stage12.mfj.tips_overtime) |
| s1a.line21_figured | — | — | — | — | — | — | — |
| s1a.line21_amount | — | — | — | — | — | — | — |
| s1a.line21_ssn | — | — | — | — | — | — | — |
| s1a.line21_claim | — | — | — | — | — | — | — |
| s1a.line21 | — | — | — | 1 (classm.s1a.1) | — | PE: 1553 compared (146 nonzero), 143 excluded; TC: 1370 compared (139 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (164 nonzero), 111 excluded; UsTaxes: 1153 compared (116 nonzero), 547 excluded | 18 |
| s1a.carloan | — | — | — | — | — | — | — |
| s1a.line23_total | — | — | — | — | — | — | — |
| s1a.line23 | — | — | — | — | — | UsTaxes below rule: 1266 compared (0 nonzero), 434 excluded | 6 |
| s1a.car_max | — | — | — | — | — | — | — |
| s1a.part4 | — | — | — | — | — | — | — |
| s1a.line24_calc | — | — | — | — | — | — | — |
| s1a.line24 | — | — | — | — | — | UsTaxes below rule: 1266 compared (0 nonzero), 434 excluded | 3 |
| s1a.car_base_other | — | — | — | — | — | — | — |
| s1a.car_base_joint | — | — | — | — | — | — | — |
| s1a.line25_calc | — | — | — | — | — | — | — |
| s1a.line25 | — | — | — | — | — | UsTaxes: 114 compared (114 nonzero), 20 excluded | — |
| s1a.line26_calc | — | — | — | — | — | — | — |
| s1a.line26 | — | — | — | — | — | — | 1 (stage12.mfj.car) |
| s1a.line27_calc | — | — | — | — | — | — | — |
| s1a.line27 | — | — | — | — | — | — | 2 (stage12.car.phaseout, stage12.car.phaseout_round_up) |
| s1a.line27_over | — | — | — | — | — | — | — |
| s1a.line27_pos | — | — | — | — | — | — | — |
| s1a.line28_thousands | — | — | — | — | — | — | — |
| s1a.line29_calc | — | — | — | — | — | — | — |
| s1a.line29 | — | — | — | — | — | UsTaxes below rule: 114 compared (37 nonzero), 20 excluded | 4 |
| s1a.line30_figured | — | — | — | — | — | — | — |
| s1a.line30_amount | — | — | — | — | — | — | — |
| s1a.line30 | — | — | — | — | — | PE: 1552 compared (99 nonzero), 143 excluded; TC: 1370 compared (98 nonzero), 330 excluded; OpenTaxSolver below rule: 1437 compared (0 nonzero), 263 excluded; UsTaxes below rule: 1039 compared (0 nonzero), 661 excluded | 15 |
| s1a.senior_count | — | — | — | — | — | — | — |
| s1a.senior_any | — | — | — | — | — | — | — |
| s1a.part5 | — | — | — | — | — | — | — |
| s1a.line31_calc | — | — | — | — | — | — | — |
| s1a.line31 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 174 compared (174 nonzero), 62 excluded | 1 (stage13.seniors_none) |
| s1a.senior_base_other | — | — | — | — | — | — | — |
| s1a.senior_base_joint | — | — | — | — | — | — | — |
| s1a.line32_calc | — | — | — | — | — | — | — |
| s1a.line32 | — | — | — | 1 (classm.s1a.1) | — | — | 1 (stage12.mfj.senior) |
| s1a.line33_calc | — | — | — | — | — | — | — |
| s1a.line33 | — | — | — | 1 (classm.s1a.1) | — | — | 3 |
| s1a.line33_over | — | — | — | — | — | — | — |
| s1a.line33_pos | — | — | — | — | — | — | — |
| s1a.line34_calc | — | — | — | — | — | — | — |
| s1a.line34 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 174 compared (86 nonzero), 62 excluded | 4 |
| s1a.senior_amount | — | — | — | — | — | — | — |
| s1a.line35_figured | — | — | — | — | — | — | — |
| s1a.line35_calc | — | — | — | — | — | — | — |
| s1a.line35 | — | — | — | 1 (classm.s1a.1) | — | UsTaxes: 174 compared (145 nonzero), 62 excluded | 8 |
| s1a.died_before_65_count | — | — | — | — | — | — | — |
| s1a.died_before_65 | — | — | — | — | — | — | — |
| s1a.senior_decedent | — | — | — | — | — | — | — |
| s1a.line36a_senior | — | — | — | — | — | — | — |
| s1a.line36a_claim | — | — | — | — | — | — | — |
| s1a.line36a | — | — | — | — | — | UsTaxes: 1153 compared (129 nonzero), 547 excluded | 11 |
| s1a.spouse_senior_count | — | — | — | — | — | — | — |
| s1a.spouse_senior | — | — | — | — | — | — | — |
| s1a.spouse_died_before_65_count | — | — | — | — | — | — | — |
| s1a.spouse_died_before_65 | — | — | — | — | — | — | — |
| s1a.spouse_senior_decedent | — | — | — | — | — | — | — |
| s1a.line36b_senior | — | — | — | — | — | — | — |
| s1a.line36b | — | — | — | 1 (classm.s1a.1) | — | UsTaxes below rule: 1153 compared (19 nonzero), 547 excluded | 8 |
| s1a.line37 | — | — | — | 1 (classm.s1a.1) | — | PE: 1668 compared (218 nonzero), 19 excluded; TC: 1370 compared (187 nonzero), 330 excluded; OpenTaxSolver: 1589 compared (212 nonzero), 111 excluded; UsTaxes: 1153 compared (145 nonzero), 547 excluded | 16 |
| s1a.line38 | — | — | — | 1 (classm.s1a.1); via f1040.line13b: 6 | — | OpenTaxSolver: 1437 compared (447 nonzero), 263 excluded; UsTaxes: 1064 compared (314 nonzero), 636 excluded; E via f1040.line13b (PE, TC, OpenTaxSolver) | 7 |

Unasserted lines: s1a.zero, s1a.tip_employers, s1a.tip_total, s1a.tip_reported, s1a.tip_multi, s1a.tip_ssn_count, s1a.tip_ssn, s1a.part2, s1a.line4a_calc, s1a.line4b_calc, s1a.line4c_one, s1a.line4c_calc, s1a.line6_calc, s1a.line7_calc, s1a.tips_max, s1a.base_other, s1a.base_joint, s1a.line8_calc, s1a.line9_calc, s1a.line10_calc, s1a.line10_over, s1a.line10_pos, s1a.line11_thousands, s1a.line12_calc, s1a.line13_figured, s1a.line13_amount, s1a.line13_ssn, s1a.line13_claim, s1a.ot_ssn_count, s1a.ot_ssn, s1a.part3, s1a.line14a_calc, s1a.line14c_calc, s1a.ot_max_other, s1a.ot_max_joint, s1a.ot_max, s1a.line15_calc, s1a.line16_calc, s1a.line17_calc, s1a.line18_calc, s1a.line18_over, s1a.line18_pos, s1a.line19_thousands, s1a.line20_calc, s1a.line21_figured, s1a.line21_amount, s1a.line21_ssn, s1a.line21_claim, s1a.line23_total, s1a.car_max, s1a.part4, s1a.line24_calc, s1a.car_base_other, s1a.car_base_joint, s1a.line25_calc, s1a.line26_calc, s1a.line27_calc, s1a.line27_over, s1a.line27_pos, s1a.line28_thousands, s1a.line29_calc, s1a.line30_figured, s1a.line30_amount, s1a.senior_count, s1a.senior_any, s1a.part5, s1a.line31_calc, s1a.senior_base_other, s1a.senior_base_joint, s1a.line32_calc, s1a.line33_calc, s1a.line33_over, s1a.line33_pos, s1a.line34_calc, s1a.senior_amount, s1a.line35_figured, s1a.line35_calc, s1a.died_before_65_count, s1a.died_before_65, s1a.senior_decedent, s1a.line36a_senior, s1a.line36a_claim, s1a.spouse_senior_count, s1a.spouse_senior, s1a.spouse_died_before_65_count, s1a.spouse_died_before_65, s1a.spouse_senior_decedent, s1a.line36b_senior

## Schedule 2 — Additional Taxes (the lines this tool computes)

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s2.amt | — | — | — | — | — | — | — |
| s2.other | — | — | — | — | — | — | — |
| s2.zero | — | — | — | via s2.line2: 3 | — | — | — |
| s2.line1a | — | — | — | 6; via s2.line1z: 3 | — | — | 6 |
| s2.line1z | — | — | — | 6 | — | — | — |
| s2.line2 | — | — | — | 6 | — | — | 3 |
| s2.line3 | — | — | — | 6; via f1040.line17: 6 | — | — | 4 |
| s2.line4 | — | — | — | 6 | — | PE: 1700 compared (238 nonzero), 0 excluded; TC: 1700 compared (238 nonzero), 0 excluded | 3 |
| s2.line8_must | — | — | — | — | — | — | — |
| s2.line8_file | — | — | — | — | — | — | — |
| s2.e05_total | — | — | — | — | — | — | — |
| s2.e05_over | — | — | — | — | — | — | — |
| s2.line8 | 2 (stage21.example.tom_jones, stage21.example.teacher_education) | — | — | 6 | — | UsTaxes below rule: 1083 compared (28 nonzero), 617 excluded | 20 |
| s2.line8_box | — | — | — | 6 | — | — | 10 |
| s2.line11 | — | — | — | 6 | — | — | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| s2.line12 | — | — | — | 6 | — | — | 2 (stage16.small.s10, stage4.additional_taxes.combined) |
| s2.line17c | — | — | — | 6; via s2.line18: 3 | — | — | 6 |
| s2.line18 | — | — | — | 6 | — | — | 5 |
| s2.line21 | — | — | — | 6; via f1040.line23: 6 | — | OpenTaxSolver: 1264 compared (319 nonzero), 436 excluded; UsTaxes below rule: 924 compared (122 nonzero), 776 excluded; E via f1040.line23 (OpenTaxSolver) | 11 |

Unasserted lines: s2.line8_must, s2.line8_file, s2.e05_total, s2.e05_over

## Schedule 3 — selected lines

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | 8 | — | — | 1 (stage18.ftc_limit_with_repayment) |
| s3.line2 | — | — | — | 8 | — | PE: 1287 compared (170 nonzero), 404 excluded; TC: 859 compared (123 nonzero), 840 excluded; OpenTaxSolver: 993 compared (130 nonzero), 707 excluded | 33 |
| s3.zero | — | — | — | — | — | — | — |
| s3.line3 | — | — | — | 8 | — | PE: 1273 compared (83 nonzero), 418 excluded; TC: 855 compared (65 nonzero), 840 excluded; UsTaxes below rule: 92 compared (44 nonzero), 120 excluded | 10 |
| s3.line4 | — | — | — | 8 | — | — | 34 |
| s3.line5a | — | — | — | 8; via s8812.clwb_15: 1 (classm.s8812.4.deepseek) | — | PE: 1278 compared (96 nonzero), 418 excluded | 28 |
| s3.line5b | — | — | — | 8 | — | PE: 1252 compared (91 nonzero), 445 excluded | 28 |
| s3.line8 | — | — | — | 8; via f1040.line20: 6 | — | OpenTaxSolver below rule: 632 compared (210 nonzero), 1068 excluded; UsTaxes below rule: 376 compared (91 nonzero), 1324 excluded; E via f1040.line20 (TC) | 4 |
| s3.mfs | — | — | — | — | — | — | — |
| s3.line9 | — | — | — | 8 | — | UsTaxes below rule: 36 compared (6 nonzero), 73 excluded | 19 |
| s3.line10 | — | — | — | — | — | — | — |
| s3.line11 | — | — | — | 8 | — | UsTaxes: 1400 compared (141 nonzero), 300 excluded | 24 |
| s3.line12 | — | — | — | — | — | — | — |
| s3.line14 | — | — | — | — | — | — | — |
| s3.line15 | — | — | — | 8; via f1040.line31: 6 | — | UsTaxes: 1288 compared (134 nonzero), 412 excluded | 21 |

Unasserted lines: s3.zero, s3.mfs

## Schedule 8812 — Credits for Qualifying Children and Other Dependents

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s8812.line1 | — | — | — | 8 | — | — | 28 |
| s8812.zero | — | — | — | via s8812.line2a: 4; via s8812.line2b: 4; via s8812.line2c: 4; via s8812.line18b → s8812.eiw_1b: 3 | — | — | — |
| s8812.line2a | — | — | — | 8 | — | — | 24 |
| s8812.line2b | — | — | — | 8 | — | — | 24 |
| s8812.line2c | — | — | — | 8 | — | — | 24 |
| s8812.line2d | — | — | — | 8 | — | — | 24 |
| s8812.line3 | — | — | — | 8 | — | UsTaxes: 611 compared (611 nonzero), 176 excluded | 28 |
| s8812.line4 | — | — | — | 8 | — | — | 29 |
| s8812.line5 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (775 nonzero), 81 excluded; UsTaxes: 737 compared (639 nonzero), 50 excluded | 31 |
| s8812.line6 | — | — | — | 8 | — | — | 25 |
| s8812.line7 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (317 nonzero), 81 excluded; UsTaxes: 737 compared (255 nonzero), 50 excluded | 27 |
| s8812.line8 | — | — | — | 8 | — | OpenTaxSolver: 889 compared (889 nonzero), 81 excluded; UsTaxes: 737 compared (737 nonzero), 50 excluded | 31 |
| s8812.line9 | — | — | — | 8 | — | — | 2 (stage15.f5695-3.g2, stage16.other.o10) |
| s8812.excess | — | — | — | — | — | — | 24 |
| s8812.line10 | — | — | — | 8 | — | OpenTaxSolver: 829 compared (82 nonzero), 141 excluded; UsTaxes: 611 compared (56 nonzero), 176 excluded | 28 |
| s8812.line11 | — | — | — | 8 | — | OpenTaxSolver: 829 compared (82 nonzero), 141 excluded; UsTaxes: 611 compared (56 nonzero), 176 excluded | 28 |
| s8812.line12 | — | — | — | 6; via s8812.clwb_1: 1 (classm.s8812.4.deepseek) | — | PE: 1511 compared (814 nonzero), 150 excluded; OpenTaxSolver: 829 compared (792 nonzero), 141 excluded; UsTaxes: 611 compared (589 nonzero), 176 excluded | 31 |
| s8812.clw_a1 | — | — | — | 6 | — | — | 30 |
| s8812.clw_a2 | — | — | — | 6 | — | — | 30 |
| s8812.clw_a3 | — | — | — | 6 | — | — | 30 |
| s8812.clw_a4 | — | — | — | 6 | — | — | 30 |
| s8812.clw_a5 | — | — | — | 6; via s8812.line13: 3 | — | — | 30 |
| s8812.show13 | — | — | — | — | — | — | 1 (stage8.single.taxpayer_without_tin) |
| s8812.line13 | — | — | — | 6 | — | — | 31 |
| s8812.line14 | — | — | — | 6; via f1040.line19: 6 | — | OpenTaxSolver below rule: 359 compared (297 nonzero), 611 excluded; UsTaxes below rule: 183 compared (152 nonzero), 604 excluded; E via f1040.line19 (PE) | 53 |
| s8812.line16a | — | — | — | 6 | — | OpenTaxSolver below rule: 359 compared (130 nonzero), 611 excluded; UsTaxes below rule: 183 compared (44 nonzero), 604 excluded | 28 |
| s8812.show16b | — | — | — | — | — | — | 1 (stage8.hoh.child.ctc) |
| s8812.line16b | — | — | — | 6; via s8812.clwb_2: 1 (classm.s8812.4.deepseek) | — | OpenTaxSolver: 275 compared (275 nonzero), 32 excluded; UsTaxes: 737 compared (639 nonzero), 50 excluded | 28 |
| s8812.show_iia | — | — | — | — | — | — | 2 (stage8.hoh.child.ctc, stage8.hoh.actc.one_child.low_wages) |
| s8812.line17 | — | — | — | 6 | — | OpenTaxSolver below rule: 359 compared (113 nonzero), 611 excluded; UsTaxes below rule: 183 compared (37 nonzero), 604 excluded | 28 |
| s8812.combat_pay | — | — | — | — | — | — | — |
| s8812.puerto_rico | — | — | — | — | — | — | — |
| s8812.eiw_1a | — | — | — | — | — | — | 24 |
| s8812.eiw_1b | — | — | — | — | — | — | 24 |
| s8812.eiw_2b | — | — | — | — | — | — | — |
| s8812.eiw_3sum | — | — | — | — | — | — | 2 (stage14.s8812.eiw_stop_with_se_tax, stage14.s8812.eiw_zero_with_se_tax) |
| s8812.eiw_3 | — | — | — | — | — | — | 24 |
| s8812.eiw_4 | — | — | — | — | — | — | 24 |
| s8812.eiw_5 | — | — | — | — | — | — | 24 |
| s8812.eiw_6 | — | — | — | — | — | — | 24 |
| s8812.eiw_7_figured | — | — | — | — | — | — | — |
| s8812.eiw_3_positive | — | — | — | — | — | — | — |
| s8812.eiw_7 | — | — | — | via s8812.clwb_3: 1 (classm.s8812.4.deepseek) | — | — | 26 |
| s8812.taking_eic | — | — | — | — | — | — | 4 |
| s8812.chart_eic | — | — | — | — | — | — | — |
| s8812.line18a | — | — | — | 6 | — | UsTaxes: 712 compared (712 nonzero), 50 excluded | 32 |
| s8812.line18b | — | — | — | 6 | — | — | 24 |
| s8812.line19 | — | — | — | 4 | — | OpenTaxSolver: 266 compared (266 nonzero), 39 excluded; UsTaxes: 712 compared (712 nonzero), 50 excluded | 31 |
| s8812.line20 | — | — | — | 6 | — | OpenTaxSolver: 268 compared (266 nonzero), 39 excluded; UsTaxes: 712 compared (712 nonzero), 50 excluded | 29 |
| s8812.ss_withheld | — | — | — | — | — | — | 24 |
| s8812.amt_ws4 | — | — | — | — | — | — | 24 |
| s8812.amt_ws6 | — | — | — | — | — | — | — |
| s8812.amt_ws7 | — | — | — | — | — | — | 1 (stage14.f8959.se_above_threshold) |
| s8812.show_iib | — | — | — | — | — | — | 2 (stage8.hoh.child.ctc, stage8.hoh.actc.one_child.low_wages) |
| s8812.line21 | — | — | — | 4; via s8812.clwb_7: 1 (classm.s8812.4.deepseek) | — | UsTaxes: 610 compared (610 nonzero), 177 excluded | 26 |
| s8812.line22 | — | — | — | 4 | — | — | 26 |
| s8812.line23 | — | — | — | 4 | — | UsTaxes: 610 compared (610 nonzero), 177 excluded | 26 |
| s8812.line24 | — | — | — | 4 | — | UsTaxes below rule: 430 compared (64 nonzero), 357 excluded | 25 |
| s8812.line25 | — | — | — | 4 | — | UsTaxes: 332 compared (332 nonzero), 455 excluded | 26 |
| s8812.line26 | — | — | — | 4 | — | UsTaxes below rule: 332 compared (332 nonzero), 455 excluded | 25 |
| s8812.few_children | — | — | — | — | — | — | 24 |
| s8812.earned_covers | — | — | — | — | — | — | 24 |
| s8812.from_part_iia | — | — | — | — | — | — | 24 |
| s8812.from_part_iib | — | — | — | — | — | — | 25 |
| s8812.part_iib_result | — | — | — | — | — | — | 24 |
| s8812.line27 | — | — | — | 6; via f1040.line28: 6 | — | OpenTaxSolver below rule: 233 compared (38 nonzero), 737 excluded; UsTaxes below rule: 102 compared (8 nonzero), 685 excluded; E via f1040.line28 (PE) | 53 |
| s8812.clwb_complete | — | — | — | — | — | — | — |
| s8812.show_clwb | — | — | — | — | — | — | 1 (stage21.t067.s8812_clwb_line6_blank) |
| s8812.clwb_1 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_2 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_3 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_4 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_5 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_three | — | — | — | — | — | — | — |
| s8812.clwb_5_covers | — | — | — | — | — | — | — |
| s8812.clwb_to7 | — | — | — | — | — | — | 1 (stage21.t067.s8812_clwb_line6_blank) |
| s8812.clwb_7 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_8 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_9 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_10 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 1 (stage16.cleanup.mut.clwb_three_figured) |
| s8812.clwb_11_figured | — | — | — | — | — | — | — |
| s8812.clwb_11_three | — | — | — | — | — | — | — |
| s8812.clwb_11 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 8 |
| s8812.clwb_12 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_13 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_14 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |
| s8812.clwb_15 | — | — | — | 2 (classm.s8812.4.deepseek, classm.s8812.4) | — | — | 6 |

Unasserted lines: s8812.eiw_2b, s8812.eiw_7_figured, s8812.eiw_3_positive, s8812.chart_eic, s8812.amt_ws6, s8812.clwb_complete, s8812.clwb_three, s8812.clwb_5_covers, s8812.clwb_11_figured, s8812.clwb_11_three

## Schedule A — supported itemized deductions and standard comparison

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sa.unsupported | — | — | — | — | — | — | — |
| sa.charity_limited | — | — | — | — | — | — | — |
| sa.excluded_income | — | — | — | — | — | — | — |
| sa.dependent | — | — | — | — | — | — | — |
| sa.spouse_extra | — | — | — | — | — | — | — |
| sa.mfs_spouse_extra | — | — | — | — | — | — | — |
| sa.age65_count | — | — | — | — | — | — | — |
| sa.age65 | — | — | — | — | — | — | — |
| sa.spouse_itemizes | — | — | — | — | — | — | — |
| sa.elect_itemize | — | — | — | — | — | — | — |
| sa.agi | — | — | — | — | — | — | — |
| sa.line1 | — | — | — | — | — | — | — |
| sa.line5a | — | — | — | — | — | — | 1 (stage16.other.o1) |
| sa.line5b | — | — | — | — | — | — | — |
| sa.line5c | — | — | — | — | — | — | — |
| sa.line8a | — | — | — | — | — | — | 1 (stage16.other.o1) |
| sa.line11 | — | — | — | — | — | — | — |
| sa.zero | — | — | — | — | — | — | — |
| sa.agi_floor | — | — | — | — | — | — | — |
| sa.line2 | — | — | — | 6 | — | — | 2 (audit.sa.negative_agi_medical, audit.sa.negative_agi_medical_paid) |
| sa.line3 | — | — | — | 6 | — | OpenTaxSolver: 1586 compared (1586 nonzero), 111 excluded; UsTaxes: 1153 compared (1153 nonzero), 547 excluded | 3 |
| sa.line4 | — | — | — | 6 | — | OpenTaxSolver: 1586 compared (100 nonzero), 114 excluded; UsTaxes: 1153 compared (73 nonzero), 547 excluded | 5 |
| sa.line5d | — | — | — | 6 | — | OpenTaxSolver: 1700 compared (826 nonzero), 0 excluded; UsTaxes: 1400 compared (682 nonzero), 300 excluded | 3 |
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
| sa.line5e | — | — | — | 6 | — | OpenTaxSolver: 1659 compared (800 nonzero), 0 excluded; UsTaxes: 1153 compared (564 nonzero), 547 excluded | 12 |
| sa.line6 | — | — | — | 6 | — | — | 5 |
| sa.line8b | — | — | — | 6 | — | — | 4 |
| sa.line8c | — | — | — | 6 | — | — | 4 |
| sa.line13 | — | — | — | 6 | — | — | 4 |
| sa.line15 | — | — | — | 6 | — | — | 4 |
| sa.gambling_losses | — | — | — | — | — | — | — |
| sa.line16_gambling | — | — | — | — | — | — | — |
| sa.line16 | — | — | — | 6 | — | — | 5 |
| sa.line7 | — | — | — | 6 | — | OpenTaxSolver: 1659 compared (800 nonzero), 0 excluded; UsTaxes: 1153 compared (564 nonzero), 547 excluded | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line8e | — | — | — | 6 | — | OpenTaxSolver: 1700 compared (505 nonzero), 0 excluded; UsTaxes: 1400 compared (404 nonzero), 300 excluded | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line9 | — | — | — | 6 | — | — | 2 (stage20.blind.r9, stage4.deductions.combined) |
| sa.line10 | — | — | — | 6 | — | OpenTaxSolver: 1579 compared (479 nonzero), 121 excluded; UsTaxes: 1057 compared (302 nonzero), 643 excluded | 2 (stage16.other.o1, stage4.deductions.combined) |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 6 | — | — | 9 |
| sa.form8283 | — | — | — | — | — | — | 3 |
| sa.line14 | — | — | — | 6 | — | OpenTaxSolver: 1697 compared (602 nonzero), 3 excluded; UsTaxes: 1400 compared (496 nonzero), 300 excluded | 1 (stage4.deductions.combined) |
| sa.line17 | — | — | — | 6 | — | PE: 1513 compared (661 nonzero), 172 excluded; TC: 1190 compared (515 nonzero), 510 excluded; OpenTaxSolver: 1476 compared (646 nonzero), 224 excluded; UsTaxes: 1057 compared (468 nonzero), 643 excluded | 11 |
| sa.standardbase | — | — | — | — | — | — | — |
| sa.extra | — | — | — | — | — | — | — |
| sa.boxes_age65 | — | — | — | — | — | — | 1 (stage16.sa.decedent_spouse) |
| sa.extra_age65 | — | — | — | — | — | — | — |
| sa.boxes_blind | — | — | — | — | — | — | — |
| sa.extra_blind | — | — | — | — | — | — | — |
| sa.standardraw | — | — | — | — | — | — | — |
| sa.standard | — | — | — | — | — | PE: 1681 compared (1681 nonzero), 19 excluded; OpenTaxSolver: 1700 compared (1700 nonzero), 0 excluded; UsTaxes: 1400 compared (1400 nonzero), 300 excluded | 12 |
| sa.itemizes | — | — | — | — | — | — | 6 |
| sa.deduction | — | — | — | via f1040.line12e: 6 | — | PE: 1513 compared (1513 nonzero), 172 excluded; TC: 902 compared (902 nonzero), 798 excluded; OpenTaxSolver: 1476 compared (1476 nonzero), 224 excluded; UsTaxes: 1057 compared (1057 nonzero), 643 excluded; E via f1040.line12e (OpenTaxSolver, UsTaxes) | 7 |
| sa.mfs_spouse_itemizes | — | — | — | — | — | — | — |

Unasserted lines: sa.mfs_spouse_extra, sa.age65_count, sa.age65, sa.agi, sa.zero, sa.agi_floor, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.line16_gambling, sa.standardbase, sa.extra, sa.extra_age65, sa.boxes_blind, sa.extra_blind, sa.standardraw, sa.mfs_spouse_itemizes

## Form 8949 and Schedule D — manually classified securities transactions

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sales.box | — | — | — | — | — | — | — |
| sales.route | — | — | — | — | — | — | — |
| sales.code | — | — | — | — | — | — | — |
| sales.special | — | — | — | — | — | — | — |
| sales.aggregate_eligible | — | — | — | — | — | — | — |
| sales.proceeds | — | — | — | — | — | — | — |
| sales.reported_basis | — | — | — | — | — | — | — |
| sales.correct_basis | — | — | — | — | — | — | — |
| sales.wash_loss | — | — | — | — | — | — | — |
| sales.covered | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.digital | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.has_b | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.has_w | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.bad_code | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.bad_aggregate | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.one | — | — | — | — | — | — | — |
| sales.zero | — | — | — | — | — | — | — |
| sales.e | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.b_difference | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.adjust_b | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.b | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.w | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.g | 4 | — | — | 1 (classm.sales.1) | — | — | 12 |
| sales.before_adjustment | — | — | — | 1 (classm.sales.1) | — | — | — |
| sales.h | 4 | — | — | 1 (classm.sales.1) | — | — | 12 |

Unasserted lines: sales.one, sales.zero

## Schedule B — supported interest and ordinary dividends

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sb.unsupported | — | — | — | — | — | — | — |
| sb.ordinary_dividends | — | — | — | via f1040.line3b → sb.line6: 6; via f8960.line2 → sb.line6: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek) | — | — | — |
| sb.line7a | — | — | — | — | — | — | — |
| sb.fbar_required | — | — | — | — | — | — | — |
| sb.form8938 | — | — | — | — | — | — | — |
| sb.line8 | — | — | — | — | — | — | — |
| sb.zero | — | — | — | — | — | — | — |
| sb.line2 | — | — | — | 2 (classm.sb.1, classm.sb.2); via f8960.line1: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek) | — | UsTaxes: 1400 compared (1059 nonzero), 300 excluded | 6 |
| sb.line3 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | — | 6 |
| sb.line4 | — | — | — | 2 (classm.sb.1, classm.sb.2); via f1040.line2b: 6 | — | UsTaxes: 1400 compared (1059 nonzero), 300 excluded | 6 |
| sb.line6 | — | — | — | 2 (classm.sb.1, classm.sb.2) | — | — | 5 |
| sb.partIII | — | — | — | — | — | — | 1 (stage4.sb.foreign_no_filing) |

Unasserted lines: sb.zero

## Schedule C (Form 1040) — Profit or Loss From Business, one per business

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sc.one | — | — | — | — | — | — | — |
| sc.rrta | — | — | — | 4 | — | — | — |
| sc.zero | — | — | — | — | — | — | — |
| sc.statutory | — | — | — | — | — | — | — |
| sc.passive | — | — | — | — | — | — | — |
| sc.spouse_owned | — | — | — | — | — | — | — |
| sc.method_other | — | — | — | — | — | — | — |
| sc.special | — | — | — | — | — | — | — |
| sc.screened | — | — | — | 4 | — | — | — |
| sc.line1 | — | — | — | — | — | — | 5 |
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
| sc.line13 | — | — | — | 4 | — | — | 17 |
| sc.line14 | — | — | — | — | — | — | — |
| sc.line15 | — | — | — | — | — | — | — |
| sc.line16a | — | — | — | — | — | — | — |
| sc.line16b | — | — | — | — | — | — | — |
| sc.line17 | — | — | — | — | — | — | — |
| sc.line18 | — | — | — | — | — | — | — |
| sc.line19 | — | — | — | — | — | — | — |
| sc.line20a | — | — | — | 4 | — | — | 2 (stage14.veh.leased_actual, stage14.sehi.with_lease) |
| sc.line20b | — | — | — | — | — | — | — |
| sc.line21 | — | — | — | — | — | — | — |
| sc.line22 | — | — | — | — | — | — | — |
| sc.line23 | — | — | — | — | — | — | — |
| sc.line24a | — | — | — | — | — | — | — |
| sc.meals_50 | — | — | — | — | — | — | — |
| sc.meals_80 | — | — | — | — | — | — | — |
| sc.meals_100 | — | — | — | — | — | — | — |
| sc.meals_50_ded | — | — | — | 4 | — | — | — |
| sc.meals_80_ded | — | — | — | 4 | — | — | — |
| sc.line24b | — | — | — | 4 | — | — | 2 (stage14.sc.basic, stage14.sc.meals_full) |
| sc.line25 | — | — | — | — | — | — | — |
| sc.line26 | — | — | — | — | — | — | — |
| sc.line27a | — | — | — | 4 | — | — | — |
| sc.line48 | — | — | — | — | — | — | — |
| sc.line27b | — | — | — | 4 | — | — | — |
| sc.line28 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | 3 |
| sc.line29 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | — |
| sc.line28_pre179 | — | — | — | 4 | — | — | — |
| sc.line29_pre179 | — | — | — | 4 | — | — | — |
| sc.ho_uses | — | — | — | — | — | — | — |
| sc.ho_other | — | — | — | — | — | — | — |
| sc.ho_screened | — | — | — | 4 | — | — | — |
| sc.ho_multi | — | — | — | 4 | — | — | — |
| sc.ho_sqft | — | — | — | — | — | — | — |
| sc.ho_home_sqft | — | — | — | — | — | — | — |
| sc.ho_rate | — | — | — | — | — | — | — |
| sc.ho_cap_sqft | — | — | — | — | — | — | — |
| sc.ho_over | — | — | — | 4 | — | — | — |
| sc.ho_line4_actual | — | — | — | 4 | — | — | — |
| sc.ho_line4_cap | — | — | — | 3 | — | — | — |
| sc.ho_line4 | — | — | — | 4 | — | — | 3 |
| sc.ho_line1 | — | — | — | 4 | — | — | 1 (stage14.ho.with_179) |
| sc.ho_room | — | — | — | 4 | — | — | — |
| sc.ho_unlimited | — | — | — | 4 | — | — | — |
| sc.ho_s179_max | — | — | — | 4 | — | — | — |
| sc.ho_no179 | — | — | — | 4 | — | — | — |
| sc.ho_limited | — | — | — | 4 | — | — | — |
| sc.ho_pre179_floor | — | — | — | 4 | — | — | — |
| sc.ho_both_limits | — | — | — | 4 | — | — | — |
| sc.ho_both | — | — | — | 3 | — | — | — |
| sc.ho_line5_lim | — | — | — | 3 | — | — | — |
| sc.ho_line5 | — | — | — | 4 | — | — | — |
| sc.line30 | — | — | — | 4 | — | — | 9 |
| sc.line31 | — | — | — | 4 | — | OpenTaxSolver: 296 compared (296 nonzero), 0 excluded | 14 |
| sc.line31_pre179 | — | — | — | 4 | — | — | — |
| sc.loss | — | — | — | 4 | — | — | — |
| sc.at_risk | — | — | — | — | — | — | — |
| sc.not_at_risk | — | — | — | 4 | — | — | — |
| sc.loss_allowed | — | — | — | 3 | — | — | 1 (stage14.refuse.at_risk) |
| sc.result | — | — | — | 4 | — | — | — |
| sc.inventory_other | — | — | — | — | — | — | — |
| sc.line35 | — | — | — | — | — | — | 1 (stage14.refuse.inventory) |
| sc.line36 | — | — | — | — | — | — | — |
| sc.line37 | — | — | — | — | — | — | — |
| sc.line38 | — | — | — | — | — | — | — |
| sc.line39 | — | — | — | — | — | — | — |
| sc.line40 | — | — | — | 4 | — | — | — |
| sc.line41 | — | — | — | — | — | — | — |
| sc.line42 | — | — | — | 4 | — | — | — |
| sc.f6 | — | — | — | 4 | — | — | 1 (stage14.asset.listed_and_not) |
| sc.f14 | — | — | — | 4 | — | — | 2 (stage14.asset.bonus_100, stage14.asset.listed_and_not) |
| sc.f17 | — | — | — | 4 | — | — | 3 |
| sc.f19_y3 | — | — | — | 4 | — | — | — |
| sc.f19_y5 | — | — | — | 4 | — | — | 1 (stage14.asset.hy_5yr) |
| sc.f19_y7 | — | — | — | 4 | — | — | — |
| sc.f19_y10 | — | — | — | 4 | — | — | — |
| sc.f19_y15 | — | — | — | 4 | — | — | — |
| sc.f19_y20 | — | — | — | 4 | — | — | — |
| sc.f19_y15sl | — | — | — | 4 | — | — | 1 (stage14.asset.qip) |
| sc.f25_assets | — | — | — | 4 | — | — | — |
| sc.f25_veh | — | — | — | 4 | — | — | — |
| sc.f25 | — | — | — | 4 | — | — | 2 (stage14.asset.listed_and_not, stage14.asset.listed_forty) |
| sc.f26_assets | — | — | — | 4 | — | — | — |
| sc.f26_veh | — | — | — | 4 | — | — | — |
| sc.f26h | — | — | — | 4 | — | — | 3 |
| sc.f28 | — | — | — | 4 | — | — | 1 (stage14.asset.listed_forty) |
| sc.f29_assets | — | — | — | 4 | — | — | — |
| sc.f29_veh | — | — | — | 4 | — | — | — |
| sc.f29 | — | — | — | 4 | — | — | 1 (stage14.asset.listed_and_not) |
| sc.s179_elected | — | — | — | 4 | — | — | — |
| sc.dep_other | — | — | — | 4 | — | — | — |
| sc.s179_return | — | — | — | 3 | — | — | — |
| sc.s179_allowed | — | — | — | 4 | — | — | 1 (stage14.s179.refuse_multi) |
| sc.mq_q4_a | — | — | — | 4 | — | — | — |
| sc.mq_q4_v | — | — | — | 4 | — | — | — |
| sc.mq_q4 | — | — | — | 4 | — | — | — |
| sc.mq_total_a | — | — | — | 4 | — | — | — |
| sc.mq_total_v | — | — | — | 4 | — | — | — |
| sc.mq_total | — | — | — | 4 | — | — | — |
| sc.cost179_a | — | — | — | 4 | — | — | — |
| sc.cost179_v | — | — | — | 4 | — | — | — |
| sc.cost179 | — | — | — | 4 | — | — | — |
| sc.rent_equipment | — | — | — | — | — | — | — |
| sc.veh_lease | — | — | — | 4 | — | — | — |
| sc.profit_pos | — | — | — | 4 | — | — | — |
| sc.hi_uses | — | — | — | — | — | — | — |
| sc.hi_screen | — | — | — | — | — | — | — |
| sc.hi_screened | — | — | — | 4 | — | — | — |
| sc.f7206_line1 | — | — | — | — | — | — | 1 (stage14.sehi.refuse_ptc) |
| sc.f7206_line2 | — | — | — | 4 | — | — | 1 (stage14.sehi.ltc) |
| sc.f7206_line3 | — | — | — | 4 | — | — | — |
| sc.f7206_line4 | — | — | — | 3 | — | — | — |
| sc.f7206_line5 | — | — | — | 4 | — | — | — |
| sc.f7206_has | — | — | — | 3 | — | — | — |
| sc.f7206_line7_pos | — | — | — | 3 | — | — | — |
| sc.f7206_line7 | — | — | — | 3 | — | — | 1 (stage14.sehi.two_businesses) |
| sc.f7206_line8 | — | — | — | 3 | — | — | — |
| sc.f7206_line9_pos | — | — | — | 4 | — | — | — |
| sc.f7206_line9 | — | — | — | 4 | — | — | 1 (stage14.sehi.with_sep) |
| sc.f7206_line10 | — | — | — | 3 | — | — | 1 (stage14.sehi.with_sep) |
| sc.f7206_line13 | — | — | — | 3 | — | — | — |
| sc.f7206_min | — | — | — | 4 | — | — | — |
| sc.f7206_line14 | — | — | — | 4 | — | — | 6 |
| sc.qbi_has | — | — | — | 4 | — | — | — |
| sc.qbi_se_pos | — | — | — | 4 | — | — | — |
| sc.qbi_se | — | — | — | 4 | — | — | — |
| sc.qbi_plan_pos | — | — | — | 4 | — | — | — |
| sc.qbi_plan | — | — | — | 4 | — | — | — |
| sc.qbi_ded | — | — | — | 4 | — | — | — |
| sc.qbi | — | — | — | 4 | — | — | 3 |
| sc.tips_ot | — | — | — | — | — | — | — |

Unasserted lines: sc.one, sc.zero, sc.ho_rate, sc.ho_cap_sqft

## Proof-of-concept scope screening

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scope.schedule1 | — | — | — | — | — | — | — |
| scope.credits | — | — | — | — | — | — | — |
| scope.other_income | — | — | — | — | — | — | — |
| scope.other_line16 | — | — | — | — | — | — | — |
| scope.ready | — | — | — | — | — | — | 5 |

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
| scveh.cm_c | — | — | — | 6 | — | — | — |
| scveh.om_c | — | — | — | — | — | — | — |
| scveh.nonbusiness_c | — | — | — | — | — | — | — |
| scveh.total_c | — | — | — | — | — | — | 1 (stage14.refuse.veh_no_miles) |
| scveh.no_miles | — | — | — | 6 | — | — | — |
| scveh.over_half | — | — | — | 6 | — | — | — |
| scveh.parking | — | — | — | — | — | — | — |
| scveh.smr_ok | — | — | — | — | — | — | — |
| scveh.smr_bad | — | — | — | 6 | — | — | — |
| scveh.rate | — | — | — | — | — | — | — |
| scveh.smr_amount | — | — | — | 6 | — | — | 1 (stage14.veh.refuse_smr) |
| scveh.line9_standard | — | — | — | 6 | — | — | — |
| scveh.operating | — | — | — | — | — | — | — |
| scveh.operating_business | — | — | — | 6 | — | — | — |
| scveh.line9_actual | — | — | — | 6 | — | — | — |
| scveh.line9 | — | — | — | 6 | — | — | 5 |
| scveh.is_actual_owned | — | — | — | 6 | — | — | — |
| scveh.is_actual_leased | — | — | — | 6 | — | — | — |
| scveh.lease | — | — | — | — | — | — | — |
| scveh.lease_business | — | — | — | 5 | — | — | — |
| scveh.line20a | — | — | — | 6 | — | — | — |
| scveh.low_use | — | — | — | 6 | — | — | — |
| scveh.placed | — | — | — | — | — | — | 2 (stage14.veh.refuse_low_use, stage14.veh.refuse_half_use) |
| scveh.screen | — | — | — | — | — | — | — |
| scveh.screened | — | — | — | 6 | — | — | — |
| scveh.cost | — | — | — | — | — | — | 2 (stage14.veh.refuse_screen, stage14.veh.refuse_too_old) |
| scveh.passenger | — | — | — | — | — | — | — |
| scveh.suv | — | — | — | — | — | — | — |
| scveh.year | — | — | — | 6 | — | — | — |
| scveh.is2025 | — | — | — | 6 | — | — | — |
| scveh.is2019 | — | — | — | 6 | — | — | — |
| scveh.y5 | — | — | — | — | — | — | — |
| scveh.bus_cost | — | — | — | 4 | — | — | — |
| scveh.s179_elect | — | — | — | — | — | — | — |
| scveh.suv_cap | — | — | — | — | — | — | — |
| scveh.s179_bad | — | — | — | 6 | — | — | — |
| scveh.after_jan19 | — | — | — | — | — | — | — |
| scveh.bonus_choice | — | — | — | — | — | — | — |
| scveh.bonus_same | — | — | — | — | — | — | — |
| scveh.bonus_mixed | — | — | — | 6 | — | — | — |
| scveh.claims_bonus | — | — | — | 6 | — | — | — |
| scveh.rate40 | — | — | — | — | — | — | — |
| scveh.lim_first_bonus | — | — | — | 3 | — | — | — |
| scveh.lim_first_none | — | — | — | 3 | — | — | — |
| scveh.lim_2025 | — | — | — | 3 | — | — | — |
| scveh.lim_prior | — | — | — | 6 | — | — | — |
| scveh.line7 | — | — | — | 6 | — | — | 3 |
| scveh.line9w | — | — | — | 6 | — | — | 3 |
| scveh.s179_2025_ok | — | — | — | 6 | — | — | 2 (stage14.veh.refuse_suv_cap, stage14.veh.refuse_suv_cap_by_1) |
| scveh.line10 | — | — | — | 6 | — | — | 1 (stage14.veh.2025_179_limit) |
| scveh.line10_2025 | — | — | — | 6 | — | — | — |
| scveh.s179_line10 | — | — | — | 6 | — | — | — |
| scveh.line11 | — | — | — | 6 | — | — | 1 (stage14.veh.2025_179_limit) |
| scveh.prior_179 | — | — | — | — | — | — | — |
| scveh.line14 | — | — | — | 6 | — | — | — |
| scveh.line15 | — | — | — | 4 | — | — | 1 (stage14.veh.2024_prior179) |
| scveh.bonus_full | — | — | — | 4 | — | — | 1 (stage14.veh.refuse_bonus_mixed) |
| scveh.bonus_forty | — | — | — | 5 | — | — | 1 (stage14.veh.refuse_bonus_mixed_forty) |
| scveh.bonus_fullcase | — | — | — | 4 | — | — | — |
| scveh.bonus_2025 | — | — | — | 6 | — | — | — |
| scveh.line16 | — | — | — | 6 | — | — | 2 (stage14.veh.suv_179, stage14.veh.2025_forty) |
| scveh.bonus_allowed | — | — | — | 6 | — | — | 2 (stage14.veh.2025_bonus, stage14.veh.2025_forty) |
| scveh.line17 | — | — | — | 6 | — | — | 1 (stage14.veh.2025_forty) |
| scveh.line18 | — | — | — | 4 | — | — | — |
| scveh.quarter | — | — | — | — | — | — | — |
| scveh.qconv | — | — | — | 6 | — | — | — |
| scveh.hy | — | — | — | — | — | — | — |
| scveh.prior_conv | — | — | — | — | — | — | — |
| scveh.rate_hy | — | — | — | 3 | — | — | — |
| scveh.rate_mq | — | — | — | 3 | — | — | — |
| scveh.rate_prior | — | — | — | 5 | — | — | — |
| scveh.line19_hy | — | — | — | 4 | — | — | — |
| scveh.line19_mq | — | — | — | 4 | — | — | — |
| scveh.line19_prior | — | — | — | 5 | — | — | — |
| scveh.line19 | — | — | — | 6 | — | — | 5 |
| scveh.line19_earlier | — | — | — | 6 | — | — | — |
| scveh.line19_2025 | — | — | — | 4 | — | — | — |
| scveh.line20 | — | — | — | 6 | — | — | 8 |
| scveh.b100 | — | — | — | 6 | — | — | — |
| scveh.k1 | — | — | — | — | — | — | — |
| scveh.r1 | — | — | — | 6 | — | — | — |
| scveh.t1 | — | — | — | 6 | — | — | — |
| scveh.l1 | — | — | — | 5 | — | — | — |
| scveh.t1s | — | — | — | 6 | — | — | — |
| scveh.d1 | — | — | — | 4 | — | — | 1 (stage14.veh.2019_cheap_mq3) |
| scveh.k2 | — | — | — | — | — | — | — |
| scveh.r2 | — | — | — | 6 | — | — | — |
| scveh.t2 | — | — | — | 6 | — | — | — |
| scveh.l2 | — | — | — | 6 | — | — | — |
| scveh.d2 | — | — | — | 6 | — | — | — |
| scveh.k3 | — | — | — | — | — | — | — |
| scveh.r3 | — | — | — | 6 | — | — | — |
| scveh.t3 | — | — | — | 6 | — | — | — |
| scveh.l3 | — | — | — | 5 | — | — | — |
| scveh.d3 | — | — | — | 5 | — | — | — |
| scveh.k4 | — | — | — | — | — | — | — |
| scveh.r4 | — | — | — | 6 | — | — | — |
| scveh.t4 | — | — | — | 6 | — | — | — |
| scveh.l4 | — | — | — | 5 | — | — | — |
| scveh.d4 | — | — | — | 5 | — | — | — |
| scveh.k5 | — | — | — | — | — | — | — |
| scveh.r5 | — | — | — | 6 | — | — | — |
| scveh.t5 | — | — | — | 6 | — | — | — |
| scveh.l5 | — | — | — | 5 | — | — | — |
| scveh.d5 | — | — | — | 5 | — | — | — |
| scveh.k6 | — | — | — | — | — | — | — |
| scveh.r6 | — | — | — | 6 | — | — | — |
| scveh.t6 | — | — | — | 6 | — | — | — |
| scveh.l6 | — | — | — | 5 | — | — | — |
| scveh.d6 | — | — | — | 5 | — | — | — |
| scveh.d_total | — | — | — | 4 | — | — | 3 |
| scveh.unrecovered | — | — | — | 4 | — | — | 3 |
| scveh.post_amount | — | — | — | 4 | — | — | — |
| scveh.post | — | — | — | 4 | — | — | 3 |
| scveh.too_old | — | — | — | 6 | — | — | — |
| scveh.bonus_v | — | — | — | 6 | — | — | — |
| scveh.macrs_pass | — | — | — | 6 | — | — | — |
| scveh.macrs_heavy | — | — | — | 6 | — | — | — |
| scveh.macrs_v | — | — | — | 6 | — | — | 2 (stage14.veh.heavy_prior, stage14.veh.heavy_2019) |
| scveh.bonus | — | — | — | 6 | — | — | — |
| scveh.macrs | — | — | — | 6 | — | — | — |
| scveh.s179_2025 | — | — | — | 6 | — | — | — |
| scveh.mq_q4 | — | — | — | 6 | — | — | — |
| scveh.mq_total | — | — | — | 6 | — | — | — |
| scveh.cost179 | — | — | — | 6 | — | — | — |
| scveh.bonus_o | — | — | — | 6 | — | — | — |
| scveh.macrs_o | — | — | — | 5 | — | — | — |
| scveh.s179_2025_o | — | — | — | 6 | — | — | — |
| scveh.q4_basis | — | — | — | 5 | — | — | — |
| scveh.mq_q4_o | — | — | — | 6 | — | — | — |
| scveh.mq_q4_a2 | — | — | — | 6 | — | — | — |
| scveh.mq_total_o | — | — | — | 6 | — | — | — |
| scveh.mq_total_a2 | — | — | — | 3 | — | — | — |
| scveh.cost179_o | — | — | — | 6 | — | — | — |
| scveh.cost179_a2 | — | — | — | 2 (classm.scveh.2, classm.scveh.5) | — | — | — |

Unasserted lines: scveh.zero, scveh.cent, scveh.bm_c, scveh.om_c, scveh.nonbusiness_c, scveh.rate, scveh.y5, scveh.suv_cap, scveh.rate40, scveh.hy, scveh.k1, scveh.k2, scveh.k3, scveh.k4, scveh.k5, scveh.k6

## Schedule D — securities sales and supplied distribution subtotals

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sd.other_forms | — | — | — | — | — | — | — |
| sd.carryover | — | — | — | — | — | — | — |
| sd.distributions | — | — | — | — | — | — | — |
| sd.line18 | — | — | — | — | — | OpenTaxSolver: 736 compared (54 nonzero), 0 excluded | 3 |
| sd.line19 | — | — | — | — | — | OpenTaxSolver: 721 compared (72 nonzero), 15 excluded | 1 (stage16.sd.line17_no_skips_19) |
| sd.filing4952 | — | — | — | — | — | — | — |
| sd.investment_election | — | — | — | — | — | — | — |
| sd.count | — | — | — | — | — | — | 13 |
| sd.screen | — | — | — | — | — | — | — |
| sd.filed | — | — | — | — | — | — | 23 |
| sd.zero | — | — | — | via sd.line4: 3; via sd.line5: 3; via sd.line11: 3; via sd.line12: 3 | — | — | — |
| sd.line1a.d | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line1a.e | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line1a.g | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line1a.h | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line1b.d | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 14 |
| sd.line1b.e | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 14 |
| sd.line1b.g | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (61 nonzero), 0 excluded | 14 |
| sd.line1b.h | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (418 nonzero), 0 excluded | 16 |
| sd.line2.d | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 14 |
| sd.line2.e | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 14 |
| sd.line2.g | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (68 nonzero), 0 excluded | 14 |
| sd.line2.h | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (426 nonzero), 0 excluded | 15 |
| sd.line3.d | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line3.e | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line3.g | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line3.h | — | — | — | 1 (classm.sd.1) | — | — | 15 |
| sd.line8a.d | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line8a.e | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line8a.g | — | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line8a.h | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 1 (classm.sd.1) | — | — | 14 |
| sd.line8b.d | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 14 |
| sd.line8b.e | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 14 |
| sd.line8b.g | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (60 nonzero), 0 excluded | 14 |
| sd.line8b.h | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (438 nonzero), 0 excluded | 15 |
| sd.line9.d | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 14 |
| sd.line9.e | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 14 |
| sd.line9.g | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (79 nonzero), 0 excluded | 14 |
| sd.line9.h | — | — | — | 1 (classm.sd.1) | — | OpenTaxSolver: 1404 compared (442 nonzero), 0 excluded | 15 |
| sd.line10.d | — | — | — | 3 | — | — | 14 |
| sd.line10.e | — | — | — | 3 | — | — | 14 |
| sd.line10.g | — | — | — | 3 | — | — | 14 |
| sd.line10.h | — | — | — | 3 | — | — | 15 |
| sd.line4 | — | — | — | 6 | — | — | 1 (sales.refuse.forms) |
| sd.line5 | — | — | — | 6 | — | — | 1 (sales.refuse.forms) |
| sd.line6_ws | — | — | — | — | — | — | 1 (stage20.refuse.other_forms_with_carryover) |
| sd.line6 | — | — | — | 6 | — | OpenTaxSolver: 260 compared (187 nonzero), 0 excluded | 22 |
| sd.line11 | — | — | — | 6 | — | — | 1 (sales.refuse.forms) |
| sd.line12 | — | — | — | 6 | — | — | 1 (sales.refuse.forms) |
| sd.line14_ws | — | — | — | — | — | — | 1 (stage20.refuse.other_forms_with_carryover) |
| sd.line14 | — | — | — | 6; via u1250.line16: 2 (classm.u1250.1.deepseek, classm.u1250.2.deepseek) | — | OpenTaxSolver: 260 compared (153 nonzero), 0 excluded | 9 |
| sd.line13 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (847 nonzero), 0 excluded | 6 |
| sd.line7 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (811 nonzero), 0 excluded; UsTaxes: 1400 compared (652 nonzero), 300 excluded | 14 |
| sd.line15 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (1269 nonzero), 0 excluded; UsTaxes: 1400 compared (1041 nonzero), 300 excluded | 10 |
| sd.line16 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (1404 nonzero), 0 excluded; UsTaxes: 1400 compared (1152 nonzero), 300 excluded | 31 |
| sd.line17 | — | — | — | 2 (classm.sd.2.deepseek, classm.sd.2) | — | — | 2 (stage16.sd.line17_no_skips_18, stage16.sd.line17_no_skips_19) |
| sd.line20 | — | — | — | 2 (classm.sd.2.deepseek, classm.sd.2) | — | — | — |
| sd.loss_limit | — | — | — | — | — | — | — |
| sd.limited_loss | — | — | — | — | — | — | — |
| sd.has_loss | — | — | — | — | — | — | — |
| sd.line21 | — | — | — | 6 | — | OpenTaxSolver: 1404 compared (572 nonzero), 0 excluded; UsTaxes: 1400 compared (468 nonzero), 300 excluded | 27 |
| sd.line22 | — | — | — | 4 | — | — | 49 |
| sd.to1040 | — | — | — | via f1040.line7a: 6; via f8960.line5a → f1040.line7a: 2 (classm.f8960.1.deepseek, classm.f8960.2.deepseek) | — | E via f1040.line7a (OpenTaxSolver, UsTaxes) | — |
| sd.net_gain_raw | — | — | — | — | — | — | 1 (sales.loss.single.700000) |
| sd.net_gain | — | — | — | — | — | — | — |

Unasserted lines: sd.filing4952, sd.investment_election, sd.screen, sd.loss_limit, sd.limited_loss, sd.has_loss, sd.net_gain

## Schedule D Tax Worksheet

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sdtw.zero | — | — | — | — | — | — | — |
| sdtw.ordinary_ceiling | — | — | — | — | — | — | — |
| sdtw.after22 | — | — | — | — | — | — | 1 (stage4.sdtw.skip22) |
| sdtw.after32 | — | — | — | — | — | — | 1 (stage4.sdtw.skip32) |
| sdtw.use1250 | — | — | — | — | — | — | — |
| sdtw.use28 | — | — | — | — | — | — | — |
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
| sdtw.line23 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw24 | — | — | — | — | — | — | — |
| sdtw.line24 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw25 | — | — | — | — | — | — | — |
| sdtw.line25 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw26 | — | — | — | — | — | — | — |
| sdtw.line26 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw27 | — | — | — | — | — | — | — |
| sdtw.line27 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw28 | — | — | — | — | — | — | — |
| sdtw.line28 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw29 | — | — | — | — | — | — | — |
| sdtw.line29 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw30 | — | — | — | — | — | — | — |
| sdtw.line30 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw31 | — | — | — | — | — | — | — |
| sdtw.line31 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 4 |
| sdtw.raw32 | — | — | — | — | — | — | — |
| sdtw.line32 | — | — | — | 4 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw33 | — | — | — | — | — | — | — |
| sdtw.line33 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 3 |
| sdtw.raw34 | — | — | — | — | — | — | — |
| sdtw.line34 | — | — | — | 3 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw35 | — | — | — | — | — | — | — |
| sdtw.line35 | — | — | — | 2 (classm.sdtw.3, classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
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
| sdtw.line41 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw42 | — | — | — | — | — | — | — |
| sdtw.line42 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 1 (stage4.sdtw.special_rates) |
| sdtw.raw43 | — | — | — | — | — | — | — |
| sdtw.line43 | — | — | — | 1 (classm.sdtw.5) | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 5 |
| sdtw.line44 | — | — | — | — | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 3 |
| sdtw.line45 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line46 | — | — | — | — | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line47 | — | — | — | 5 | — | OpenTaxSolver below rule: 0 compared (0 nonzero), 124 excluded | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |

Unasserted lines: sdtw.zero, sdtw.ordinary_ceiling, sdtw.use1250, sdtw.use28, sdtw.raw23, sdtw.raw24, sdtw.raw25, sdtw.raw26, sdtw.raw27, sdtw.raw28, sdtw.raw29, sdtw.raw30, sdtw.raw31, sdtw.raw32, sdtw.raw33, sdtw.raw34, sdtw.raw35, sdtw.raw36, sdtw.raw37, sdtw.raw38, sdtw.raw39, sdtw.raw40, sdtw.raw41, sdtw.raw42, sdtw.raw43

## Student Loan Interest Deduction Worksheet—Schedule 1, Line 21

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sli.zero | — | — | — | — | — | — | — |
| sli.interest | — | — | — | — | — | — | — |
| sli.has | — | — | — | — | — | — | — |
| sli.claimed | — | — | — | — | — | — | — |
| sli.max | — | — | — | — | — | — | — |
| sli.line1 | — | — | — | 4 | — | UsTaxes: 206 compared (206 nonzero), 0 excluded | 1 (stage11.sli.cap) |
| sli.line2 | — | — | — | 4 | — | UsTaxes: 159 compared (159 nonzero), 47 excluded | — |
| sli.line3 | — | — | — | 4 | — | UsTaxes: 159 compared (72 nonzero), 47 excluded | 1 (stage11.sli.with_adjustments) |
| sli.line4 | — | — | — | 4 | — | UsTaxes: 159 compared (159 nonzero), 47 excluded | — |
| sli.base_other | — | — | — | — | — | — | — |
| sli.base_joint | — | — | — | — | — | — | — |
| sli.line5 | — | — | — | 3 | — | — | 1 (stage11.sli.boundary_joint) |
| sli.over | — | — | — | — | — | — | — |
| sli.line6 | — | — | — | — | — | — | 3 |
| sli.divisor_other | — | — | — | — | — | — | — |
| sli.divisor_joint | — | — | — | — | — | — | — |
| sli.divisor | — | — | — | — | — | — | — |
| sli.line8_figured | — | — | — | — | — | — | — |
| sli.line8 | — | — | — | 4 | — | UsTaxes: 159 compared (65 nonzero), 47 excluded | 7 |
| sli.line9 | — | — | — | 4 | — | UsTaxes: 159 compared (94 nonzero), 47 excluded | — |
| sli.eligible | — | — | — | — | — | — | — |
| sli.allowed | — | — | — | — | — | — | — |
| sli.deduction | — | — | — | — | — | E via s1.line21 (OpenTaxSolver, UsTaxes) | 11 |

Unasserted lines: sli.zero, sli.has, sli.max, sli.base_other, sli.base_joint, sli.over, sli.divisor_other, sli.divisor_joint, sli.divisor, sli.line8_figured, sli.eligible, sli.allowed

## Social Security Benefits Worksheet—Lines 6a and 6b

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ssb.benefits | — | — | — | via f1040.line6a → ssb.line1: 6 | — | E via ssb.line1 (OpenTaxSolver, UsTaxes) | — |
| ssb.pub915 | — | — | — | — | — | — | — |
| ssb.lump_sum | — | — | — | — | — | — | — |
| ssb.terror_disability | — | — | — | — | — | — | — |
| ssb.lived_apart | — | — | — | — | — | — | — |
| ssb.line1 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.has_benefits | — | — | — | — | — | — | — |
| ssb.line2 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.line3 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 2 (stage11.ss.unemployment, stage16.ira.i10) |
| ssb.line4 | — | — | — | 5 | — | OpenTaxSolver below rule: 530 compared (0 nonzero), 20 excluded; UsTaxes below rule: 463 compared (0 nonzero), 0 excluded | 1 (stage16.ira.i10) |
| ssb.line5 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 463 compared (463 nonzero), 0 excluded | 2 (stage10.ss.refuse.schedule1, stage16.ira.i10) |
| ssb.ira_line20 | — | — | — | — | — | — | — |
| ssb.line6 | — | — | — | 5 | — | OpenTaxSolver: 530 compared (300 nonzero), 20 excluded; UsTaxes: 338 compared (155 nonzero), 125 excluded | 3 |
| ssb.line7 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 338 compared (338 nonzero), 125 excluded | 3 |
| ssb.base_single | — | — | — | — | — | — | — |
| ssb.base_joint | — | — | — | — | — | — | — |
| ssb.zero | — | — | — | — | — | — | — |
| ssb.mfs_base | — | — | — | — | — | — | — |
| ssb.line8 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (530 nonzero), 20 excluded; UsTaxes: 338 compared (338 nonzero), 125 excluded | 2 (stage13.ssb_joint_base, stage16.ira.i10) |
| ssb.line9 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded | 2 (stage10.ss.none, stage13.ssb_joint_base) |
| ssb.adjust_single | — | — | — | — | — | — | — |
| ssb.adjust_joint | — | — | — | — | — | — | — |
| ssb.mfs_adjust | — | — | — | — | — | — | — |
| ssb.line10 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 477 compared (477 nonzero), 17 excluded; UsTaxes: 338 compared (338 nonzero), 125 excluded | — |
| ssb.line11 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (451 nonzero), 20 excluded; UsTaxes: 338 compared (280 nonzero), 125 excluded | — |
| ssb.line12 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded | — |
| ssb.line13 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded | 1 (stage10.ss.middle) |
| ssb.line14 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded | 1 (stage10.ss.small_benefits) |
| ssb.line15 | — | — | — | 2 (classm.ssb.1, classm.ssb.5) | — | OpenTaxSolver: 530 compared (451 nonzero), 20 excluded; UsTaxes: 338 compared (280 nonzero), 125 excluded | 1 (stage10.ss.middle) |
| ssb.mfs_together | — | — | — | — | — | — | — |
| ssb.line16_sum | — | — | — | — | — | — | — |
| ssb.line16_together | — | — | — | — | — | — | — |
| ssb.line16 | — | — | — | 3 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded | 2 (stage10.ss.top, stage10.ss.small_benefits) |
| ssb.line17 | — | — | — | 3 | — | OpenTaxSolver: 477 compared (477 nonzero), 17 excluded; UsTaxes: 338 compared (338 nonzero), 125 excluded | — |
| ssb.line18_figured | — | — | — | — | — | — | — |
| ssb.line18 | — | — | — | 3; via f1040.line6b: 6 | — | OpenTaxSolver: 530 compared (477 nonzero), 20 excluded; UsTaxes: 338 compared (300 nonzero), 125 excluded; E via f1040.line6b (PE, TC, OpenTaxSolver, UsTaxes) | 1 (stage16.ira.i10) |

Unasserted lines: ssb.has_benefits, ssb.ira_line20, ssb.base_single, ssb.base_joint, ssb.zero, ssb.mfs_base, ssb.adjust_single, ssb.adjust_joint, ssb.mfs_adjust, ssb.mfs_together, ssb.line16_sum, ssb.line16_together, ssb.line18_figured

## Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tipjob.one | — | — | — | — | — | — | — |
| tipjob.qualified | — | — | — | — | — | — | — |
| tipjob.amount | — | — | — | — | — | — | — |
| tipjob.mixed | — | — | — | 1 (classm.tipjob.1) | — | — | — |
| tipjob.col_c | — | — | — | — | — | — | — |
| tipjob.col_d | — | — | — | 1 (classm.tipjob.1) | — | — | — |

Unasserted lines: tipjob.one, tipjob.col_c

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
| w2.g_bad | — | — | — | 2 (classm.w2.1.deepseek, classm.w2.1) | — | — | — |
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

## Schedule SE (Form 1040) — Self-Employment Tax, one per person

| line | A | B | C | M | H | E | R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| line2 | — | — | — | — | — | — | — |
| line8a | — | — | — | — | — | — | — |
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

Unasserted computed lines across all documents: 1006. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)
Asserted keys not matching a line id: dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line27, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line29, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28_zero, dependent[dep_a]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line30, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line27, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line29, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line28_zero, dependent[k0]|inst:aqee#{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"}.line30, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line3, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.positive, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4a, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.owes, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line4c, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line5b, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line6, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line7, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line8d, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line9, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line10, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line11, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line12, person[taxpayer]|inst:se#{"line2":"person.se_line2","line8a":"person.wages"}.line13, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.below_boundary, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax, qdcg.f1040.line15, qdcg.f1040.line3a, qdcg.f1040.status, f1040.qdcg.line25, qdcg.sd.distributions