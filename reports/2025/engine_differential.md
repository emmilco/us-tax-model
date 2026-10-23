# Engine differential — generated returns vs independent engines

Cases: 1700 generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

Not-computed floor: the run fails when the project left more than 5% of an engine's cases without a value on a mapped line (a refusal, an unknown input, a non-money value), measured outside the allow-listed returns that do not file the form: f2441.line11 unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f2441.line9c unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f5695.line13 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line15 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line30 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return); f5695.line32 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return).

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1214 | 0 | 186 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1401 | 0 | 299 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1561 | 0 | 81 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line11b | 1100 | 0 | 542 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line13a | 1492 | 0 | 19 | 118 | 0 | 0 | 71 | 71 (4.2%) |
| f1040.line13b | 1538 | 0 | 1 | 140 | 0 | 0 | 21 | 21 (1.2%) |
| f1040.line15 | 948 | 0 | 453 | 235 | 4 | 0 | 60 | 60 (3.5%) |
| f1040.line16 | 458 | 803 | 118 | 260 | 1 | 0 | 60 | 60 (3.5%) |
| f1040.line19 | 850 | 123 | 0 | 684 | 0 | 0 | 43 | 43 (2.5%) |
| f1040.line27a | 1395 | 247 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line28 | 893 | 79 | 1 | 684 | 0 | 0 | 43 | 43 (2.5%) |
| f1040.line6b | 1639 | 0 | 29 | 17 | 0 | 0 | 15 | 15 (0.9%) |
| f1040.tax_before_credits | 422 | 776 | 136 | 306 | 0 | 0 | 60 | 60 (3.5%) |
| f2441.line11 | 215 | 14 | 0 | 260 | 0 | 0 | 1211 | 9 (0.5%) |
| f2441.line9c | 277 | 0 | 0 | 17 | 0 | 0 | 1406 | 5 (0.3%) |
| f5695.line13 | 169 | 0 | 3 | 17 | 0 | 0 | 1511 | 0 (0.0%) |
| f5695.line15 | 94 | 44 | 1 | 260 | 0 | 0 | 1301 | 4 (0.2%) |
| f5695.line30 | 139 | 0 | 7 | 57 | 0 | 0 | 1497 | 0 (0.0%) |
| f5695.line32 | 111 | 7 | 5 | 297 | 0 | 0 | 1280 | 3 (0.2%) |
| f8880.line10 | 1636 | 0 | 3 | 20 | 0 | 0 | 41 | 41 (2.4%) |
| f8880.line12 | 1385 | 12 | 1 | 263 | 0 | 0 | 39 | 39 (2.3%) |
| f8959.tax | 1678 | 0 | 5 | 17 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1489 | 0 | 3 | 169 | 0 | 0 | 39 | 39 (2.3%) |
| person[taxpayer].se_line12 | 1655 | 0 | 45 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1621 | 0 | 79 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1621 | 0 | 79 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line20 | 1642 | 0 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| s1a.line13 | 1557 | 0 | 0 | 140 | 0 | 0 | 3 | 3 (0.2%) |
| s1a.line21 | 1556 | 0 | 0 | 140 | 0 | 0 | 4 | 4 (0.2%) |
| s1a.line30 | 1555 | 0 | 0 | 140 | 0 | 0 | 5 | 5 (0.3%) |
| s1a.line37 | 1669 | 0 | 1 | 17 | 0 | 0 | 13 | 13 (0.8%) |
| s2.line4 | 1655 | 0 | 45 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 1417 | 14 | 0 | 260 | 0 | 0 | 9 | 9 (0.5%) |
| s3.line5a | 1391 | 44 | 1 | 260 | 0 | 0 | 4 | 4 (0.2%) |
| s3.line5b | 1388 | 7 | 5 | 297 | 0 | 0 | 3 | 3 (0.2%) |
| s8812.line12 | 1642 | 0 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| sa.deduction | 1528 | 0 | 4 | 153 | 0 | 0 | 15 | 15 (0.9%) |
| sa.line17 | 1529 | 0 | 3 | 153 | 0 | 0 | 15 | 15 (0.9%) |
| sa.standard | 1683 | 0 | 0 | 17 | 0 | 0 | 0 | 0 (0.0%) |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US lists capped_qualified_furnace_or_hot_water_boiler_credit twice in gov.irs.credits.energy_efficient_home_improvement.qualified_expenditures.credits, so it counts the furnace credit twice in Form 5695 line 27
- PolicyEngine-US phases the student loan interest deduction out with the exact ratio; the worksheet's line 7 ratio is rounded to three places in the project (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars
- PolicyEngine-US reduces the tips, overtime and car loan interest deductions by the rate times the exact excess of modified AGI over the threshold; Schedule 1-A lines 11, 19 and 28 count whole $1,000 steps (rounded down, down and up) first
- PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does
- PolicyEngine-US's eitc_earned_income includes net earnings from self-employment less half the self-employment tax; Step 5 earned income (Form 1040 instructions, line 27) holds wages only and Worksheet B adds the self-employment amounts, so Worksheet B line 6 (eic.line1) is compared instead on self-employed returns
- PolicyEngine-US's energy_efficient_home_improvement_credit_potential takes the larger of the $1,200-capped total and the heat pump credit; Form 5695 line 30 adds line 28 and line 29h
- PolicyEngine-US's saver's credit rate (gov.irs.credits.retirement_saving.rate.joint, a bracket scale whose first threshold is $0) is zero for an adjusted gross income below zero; the Form 8880 line 9 table's first row has no lower bound ("---" to $23,750, $35,625 or $47,500: 0.5)

Project result lines not mapped:

- person[taxpayer].f8889[hsa].line13: health_savings_account_ald is an input with no formula; the engine does not compute Form 8889
- ssb.line18: reached through Form 1040 line 6b, a copy of it
- s1a.line38: reached through Form 1040 line 13b, a copy of it
- s8812.line14: reached through Form 1040 line 19, a copy of it
- s8812.line27: reached through Form 1040 line 28, a copy of it
- eic.credit: reached through Form 1040 line 27a, a copy of it

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1400 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1302 | 0 | 68 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1273 | 0 | 97 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 1043 | 0 | 6 | 633 | 0 | 0 | 18 | 18 (1.1%) |
| f1040.line13b | 1368 | 0 | 2 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 835 | 0 | 66 | 798 | 1 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 352 | 507 | 59 | 765 | 0 | 0 | 17 | 17 (1.0%) |
| f1040.line19 | 624 | 82 | 0 | 994 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 635 | 293 | 0 | 765 | 0 | 0 | 7 | 7 (0.4%) |
| f1040.line24 | 438 | 323 | 88 | 834 | 0 | 0 | 17 | 17 (1.0%) |
| f1040.line27a | 1162 | 208 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 652 | 54 | 0 | 994 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1344 | 0 | 26 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 322 | 489 | 79 | 793 | 0 | 0 | 17 | 17 (1.0%) |
| f2441.line11 | 158 | 7 | 0 | 765 | 0 | 0 | 770 | 1 (0.1%) |
| f8959.tax | 1366 | 0 | 4 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1306 | 0 | 0 | 394 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line12 | 1656 | 0 | 44 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1370 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1370 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1370 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1368 | 0 | 2 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line4 | 1656 | 0 | 44 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 927 | 7 | 0 | 765 | 0 | 0 | 1 | 1 (0.1%) |
| sa.deduction | 900 | 0 | 2 | 798 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1192 | 0 | 2 | 505 | 1 | 0 | 0 | 0 (0.0%) |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator has no saver's credit to subtract in Schedule 8812 Credit Limit Worksheet A line 2, which moves line 14 where the child tax credit does not fit under the worksheet's limit
- Tax-Calculator subtracts the whole Form 5695 amount (e07260) in Credit Limit Worksheet A line 2, which lists Schedule 3 line 5b (Part II) but not line 5a; the residential clean energy credit (Part I) follows the child tax credit, through Credit Limit Worksheet B when there is a qualifying child, which moves line 14 where the child tax credit does not fit under the engine's limit
- Tax-Calculator takes the Form 8880 credit as a supplied amount (e07240) and has no input for retirement contributions, so the total tax of a return with a saver's credit is not compared
- Tax-Calculator takes the deductible IRA contributions as a supplied amount (e03150) rather than computing the IRA Deduction Worksheet's phase-out by modified AGI, so returns whose deduction is less than the contributions are not compared
- Tax-Calculator takes the standard deduction whenever the tax is the same either way; when the Schedule 1-A deductions leave no tax even with the standard deduction zeroed, its forced pass also takes the standard deduction, so the itemized total is not compared
- Tax-Calculator takes the student loan interest deduction as a supplied amount (e03210) rather than computing the worksheet's phase-out, so returns with student loan interest are not compared
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass
- Tax-Calculator's earned includes self-employment earnings less half the self-employment tax; Step 5 earned income (Form 1040 instructions, line 27) holds wages only and Worksheet B adds the self-employment amounts, so Worksheet B line 6 (eic.line1) is compared instead on self-employed returns

Project result lines not mapped:

- person[taxpayer].f8889[hsa].line13: e03290 is an input; the engine does not compute Form 8889
- s1.line20: e03150 (deductible IRA contributions) is an input; the engine does not compute the IRA Deduction Worksheet
- f8880.line10: e07240 (the Form 8880 credit) is an input; the engine computes only its tax limit (c07240)
- f8880.line12: e07240 (the Form 8880 credit) is an input; the engine computes only its tax limit (c07240)
- f5695.line13: e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts
- f5695.line15: e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts
- f5695.line30: e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts
- f5695.line32: e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts
- f2441.line9c: F2441 computes line 9a but does not expose it; only c07180 (line 11) is an output
- s8812.line12: ChildDepTaxCredit computes line 12 but does not expose it; c07220 and odc are line 14 split
- ssb.line18: reached through Form 1040 line 6b, a copy of it
- s1a.line38: reached through Form 1040 line 13b, a copy of it
- s8812.line14: reached through Form 1040 line 19, a copy of it
- s8812.line27: reached through Form 1040 line 28, a copy of it
- eic.credit: reached through Form 1040 line 27a, a copy of it

## Explained differences

- PolicyEngine-US gen-00314 f1040.line15: project 5087668 engine 5087670 — Carried float32 error: PolicyEngine-US's AGI is 1 cent above the project's (within float32 precision at $79,136.84), line 10, the standard deduction and the QBI deduction agree exactly, and the float32 subtractions to line 15 add one more cent, for 2 cents. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.
- PolicyEngine-US gen-00372 f1040.line15: project 23286983 engine 23286988 — Carried float32 error: PolicyEngine-US's AGI ($261,861.22) is 4 cents above the project's ($261,861.18), within two units in the last place at that size (about 3.1 cents, rounded up to 4); line 10 (the IRA deduction, $1,823.63) and the itemized deduction ($28,991.35) agree exactly, and the float32 subtraction to line 15 adds one more cent, for 5 cents where the bound at line 15's size is 4 cents. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US gen-00372 f1040.line16: project 5156768 engine 5156770 — Carried float32 error: PolicyEngine-US's taxable income is 5 cents above the project's (its line 15 difference, explained separately), and the rate schedule both use above $100,000 taxes the 5 cents at 32% (taxable income $232,869.83, single), 1.6 cents, which the engine's float32 arithmetic rounds to 2 cents; the bound at line 16's size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US se-00203 f1040.line15: project 3803775 engine 3803777 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $106.47 in both, and line 13, half of it, is $53.235; the project rounds half-up to $53.24 (amb.2025.multiplication_subcent), the engine takes $53.23, so line 10 and AGI are 1 cent apart ($61,802.82 against $61,802.81); the standard deduction and the QBI deduction ($140.06) agree exactly, and the engine's float32 subtraction to line 15 adds one more cent, for 2 cents where the bound at line 15's size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US se-00293 f1040.line15: project 3977437 engine 3977439 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $3,487.87 in both, and line 13, half of it, is $1,743.935; the project rounds half-up to $1,743.94 (amb.2025.multiplication_subcent), the engine takes $1,743.93, so line 10 is 1 cent apart; the engine's gross income is 1 cent above the project's (within float32 precision at $74,283.60), so AGI is 2 cents apart ($68,112.59 against $68,112.57); the standard deduction, the QBI deduction and line 13b agree exactly, and line 15 carries the 2 cents where the bound at its size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- Tax-Calculator se-00075 f1040.line15: project 1971096 engine 1971098 — Rounding of the half of self-employment tax: Schedule SE line 12 is $822.51 in all three, and line 13, half of it, is $411.255; the project rounds half-up to $411.26 (amb.2025.multiplication_subcent), both engines take $411.25, so AGI is 1 cent apart; Schedule A, the QBI deduction and line 13b agree exactly, and Tax-Calculator's own float64 subtractions to taxable income give one more cent. Investigated 2026-10-19 when self-employment entered the generated cases.
- Tax-Calculator se-00255 sa.line17: project 32485 engine 0 — Negative adjusted gross income (-$4,331.38) with no medical expenses: the project's Schedule A line 3 (7.5% of line 2) is -$324.85 and its line 4, line 1 ($0) less line 3, is $324.85, read literally from the form ("Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"); Tax-Calculator floors AGI at zero for line 3 (calcfunctions.ItemDed: posagi = max(c00100, 0.); c17750 = medical_frt * posagi; c17000 = max(0., e17500 - c17750)) and deducts nothing. The instructions allow "only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income" (i1040sca, line 1), and no part of $0 of expenses is $324.85, so the engine's reading follows the instruction and the project's is a candidate defect referred to the owner. Investigated 2026-10-22 when IRA contributions entered the generated cases.

## Unexplained differences

None.
