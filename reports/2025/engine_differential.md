# Engine differential — generated returns vs independent engines

Cases: 1700 generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). Engines run locally under .engines/ (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5, OpenTaxSolver 23.06 (package 0_README.txt; the Form 1040 program reports v23.05), UsTaxes 0.1.23 (git d276c7241dc8, src/forms/Y2025).

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `unrounded` (OpenTaxSolver, which computes in doubles, rounds nothing and prints each program's lines to the cent) means the engine equals the project's own derivation of the line re-evaluated in exact arithmetic without the project's half-up cent rounding of products and ratios (amb.2025.multiplication_subcent), with each amount that passes between the engine's programs taken at the cent it prints and the result printed to the cent; where the exact value is within 1/1000 cent of a half cent either neighbouring cent is the print (an engine double stays within 1/10,000 cent of the exact value at these amounts). No difference is allowed beyond what that recomputation gives; a line the adapter supplies as an amount is recomputed only where the project's value is that amount, and a case whose exact values take another branch, test or table band than the project's is not recomputed. An identified cause, not a tolerance. OpenTaxSolver builds its tax from the Tax Table below $100,000 as the form does, so it has no `table-adjusted` reading. `table-midpoint` (UsTaxes, which emulates the Tax Table by applying the rate schedule at the midpoint of the band holding the whole-dollar amount, without the table's rounding to whole dollars, and rounds Form 8960 line 17 to whole dollars) means the engine equals the project's lines recomputed by those two methods along the project's own worksheet path: each Tax Table lookup replaced by the schedule at the band midpoint, Form 8960 line 17 by 3.8% of line 16 rounded half up to whole dollars, and the lines that follow (the worksheet's tax lines, Form 1040 lines 16 to 37, Schedule 8812 lines 14 to 27) re-taken; within the engine's `float` bound, it is an identified cause, not a tolerance. `excluded` lines carry the engine limitation stated below; the features that trigger them are the generator's, those read off the project's values, and those the engine's adapter reports about its own run. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

Not-computed floor: the run fails when the project left more than 5% of an engine's cases without a value on a mapped line (a refusal, an unknown input, a non-money value), measured outside the allow-listed returns that do not file the form: f2441.line11 unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f2441.line9c unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f5695.line13 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line15 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line30 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return); f5695.line32 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return).

## PolicyEngine-US

| line | exact | table-adjusted | table-midpoint | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1214 | 0 | 0 | 186 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1401 | 0 | 0 | 299 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1559 | 0 | 0 | 81 | 0 | 19 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line11b | 1106 | 0 | 0 | 534 | 0 | 19 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line13a | 1471 | 0 | 0 | 19 | 0 | 139 | 0 | 0 | 71 | 71 (4.2%) |
| f1040.line13b | 1537 | 0 | 0 | 2 | 0 | 140 | 0 | 0 | 21 | 21 (1.2%) |
| f1040.line15 | 942 | 0 | 0 | 443 | 0 | 253 | 2 | 0 | 60 | 60 (3.5%) |
| f1040.line16 | 464 | 779 | 0 | 102 | 0 | 295 | 0 | 0 | 60 | 60 (3.5%) |
| f1040.line19 | 777 | 110 | 0 | 0 | 0 | 773 | 0 | 0 | 40 | 40 (2.4%) |
| f1040.line27a | 1281 | 230 | 0 | 0 | 0 | 150 | 0 | 0 | 39 | 39 (2.3%) |
| f1040.line28 | 816 | 70 | 0 | 1 | 0 | 773 | 0 | 0 | 40 | 40 (2.4%) |
| f1040.line6b | 1637 | 0 | 0 | 29 | 0 | 19 | 0 | 0 | 15 | 15 (0.9%) |
| f1040.tax_before_credits | 402 | 688 | 0 | 112 | 0 | 441 | 0 | 0 | 57 | 57 (3.4%) |
| f2441.line11 | 197 | 12 | 0 | 0 | 0 | 401 | 0 | 0 | 1090 | 9 (0.5%) |
| f2441.line9c | 259 | 0 | 0 | 0 | 0 | 150 | 0 | 0 | 1291 | 5 (0.3%) |
| f5695.line13 | 169 | 0 | 0 | 3 | 0 | 19 | 0 | 0 | 1509 | 0 (0.0%) |
| f5695.line15 | 81 | 41 | 0 | 1 | 0 | 401 | 0 | 0 | 1176 | 4 (0.2%) |
| f5695.line30 | 139 | 0 | 0 | 7 | 0 | 59 | 0 | 0 | 1495 | 0 (0.0%) |
| f5695.line32 | 103 | 5 | 0 | 5 | 0 | 428 | 0 | 0 | 1159 | 3 (0.2%) |
| f8880.line10 | 1634 | 0 | 0 | 3 | 0 | 22 | 0 | 0 | 41 | 41 (2.4%) |
| f8880.line12 | 1248 | 11 | 0 | 1 | 0 | 403 | 0 | 0 | 37 | 37 (2.2%) |
| f8959.tax | 1676 | 0 | 0 | 5 | 0 | 19 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1469 | 0 | 0 | 3 | 0 | 189 | 0 | 0 | 39 | 39 (2.3%) |
| person[taxpayer].se_line12 | 1655 | 0 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1621 | 0 | 0 | 79 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1621 | 0 | 0 | 79 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line20 | 1640 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 41 | 41 (2.4%) |
| s1a.line13 | 1557 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 3 | 3 (0.2%) |
| s1a.line21 | 1556 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 4 | 4 (0.2%) |
| s1a.line30 | 1555 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 5 | 5 (0.3%) |
| s1a.line37 | 1666 | 0 | 0 | 2 | 0 | 19 | 0 | 0 | 13 | 13 (0.8%) |
| s2.line4 | 1655 | 0 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 1278 | 12 | 0 | 0 | 0 | 401 | 0 | 0 | 9 | 9 (0.5%) |
| s3.line5a | 1253 | 41 | 0 | 1 | 0 | 401 | 0 | 0 | 4 | 4 (0.2%) |
| s3.line5b | 1259 | 5 | 0 | 5 | 0 | 428 | 0 | 0 | 3 | 3 (0.2%) |
| s8812.line12 | 1511 | 0 | 0 | 0 | 0 | 150 | 0 | 0 | 39 | 39 (2.3%) |
| sa.deduction | 1508 | 0 | 0 | 4 | 0 | 173 | 0 | 0 | 15 | 15 (0.9%) |
| sa.line17 | 1508 | 0 | 0 | 4 | 0 | 173 | 0 | 0 | 15 | 15 (0.9%) |
| sa.standard | 1681 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 0 | 0 (0.0%) |

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
- the engine is given no Form 1095-A, so its tax, credits and payments omit the premium tax credit reconciliation (Form 8962) the project figures on these returns

Project result lines not mapped:

- person[taxpayer].f8889[hsa].line13: health_savings_account_ald is an input with no formula; the engine does not compute Form 8889
- ssb.line18: reached through Form 1040 line 6b, a copy of it
- s1a.line38: reached through Form 1040 line 13b, a copy of it
- s8812.line14: reached through Form 1040 line 19, a copy of it
- s8812.line27: reached through Form 1040 line 28, a copy of it
- eic.credit: reached through Form 1040 line 27a, a copy of it

## Tax-Calculator

| line | exact | table-adjusted | table-midpoint | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1624 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1302 | 0 | 0 | 68 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1273 | 0 | 0 | 97 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 1033 | 0 | 0 | 6 | 0 | 643 | 0 | 0 | 18 | 18 (1.1%) |
| f1040.line13b | 1368 | 0 | 0 | 2 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 821 | 0 | 0 | 69 | 0 | 809 | 1 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 354 | 502 | 0 | 55 | 0 | 772 | 0 | 0 | 17 | 17 (1.0%) |
| f1040.line19 | 566 | 78 | 0 | 0 | 0 | 1056 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 580 | 273 | 0 | 0 | 0 | 840 | 0 | 0 | 7 | 7 (0.4%) |
| f1040.line24 | 413 | 292 | 0 | 77 | 0 | 902 | 0 | 0 | 16 | 16 (0.9%) |
| f1040.line27a | 1065 | 195 | 0 | 0 | 0 | 440 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 594 | 50 | 0 | 0 | 0 | 1056 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1344 | 0 | 0 | 26 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 302 | 446 | 0 | 69 | 0 | 867 | 0 | 0 | 16 | 16 (0.9%) |
| f2441.line11 | 146 | 6 | 0 | 0 | 0 | 840 | 0 | 0 | 708 | 1 (0.1%) |
| f8959.tax | 1366 | 0 | 0 | 4 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1300 | 0 | 0 | 0 | 0 | 400 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line12 | 1656 | 0 | 0 | 44 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1624 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1624 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1370 | 0 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1370 | 0 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1370 | 0 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1368 | 0 | 0 | 2 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line4 | 1656 | 0 | 0 | 44 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 853 | 6 | 0 | 0 | 0 | 840 | 0 | 0 | 1 | 1 (0.1%) |
| sa.deduction | 889 | 0 | 0 | 2 | 0 | 809 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1180 | 0 | 0 | 2 | 0 | 518 | 0 | 0 | 0 | 0 (0.0%) |

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
- the engine is given no Form 1095-A, so its tax, credits and payments omit the premium tax credit reconciliation (Form 8962) the project figures on these returns

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

## OpenTaxSolver

| line | exact | table-adjusted | table-midpoint | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clcw.line1 | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line10 | 153 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line11 | 153 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line12 | 153 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line13 | 153 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line2 | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line3 | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line4 | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line5 | 196 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line6 | 196 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line7 | 196 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line8 | 196 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| clcw.line9 | 153 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1514 | 0 | 0 | 0 | 75 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1485 | 0 | 0 | 0 | 104 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line12e | 1474 | 0 | 0 | 0 | 2 | 224 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 370 | 0 | 0 | 0 | 17 | 130 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13b | 1434 | 0 | 0 | 0 | 3 | 263 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line14 | 1215 | 0 | 0 | 0 | 21 | 464 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 1150 | 0 | 0 | 0 | 86 | 464 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 1023 | 0 | 0 | 0 | 53 | 624 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line17 | 1462 | 0 | 0 | 0 | 0 | 238 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line18 | 946 | 0 | 0 | 0 | 48 | 706 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line19 | 422 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line1z | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 749 | 0 | 0 | 0 | 0 | 951 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line21 | 749 | 0 | 0 | 0 | 0 | 951 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line22 | 709 | 0 | 0 | 0 | 40 | 951 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line23 | 1320 | 0 | 0 | 0 | 42 | 338 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line24 | 691 | 0 | 0 | 0 | 58 | 951 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line25d | 1567 | 0 | 0 | 0 | 0 | 133 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 265 | 0 | 0 | 0 | 1 | 704 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line32 | 552 | 0 | 0 | 0 | 1 | 1147 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line33 | 552 | 0 | 0 | 0 | 1 | 1147 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line34 | 532 | 0 | 0 | 0 | 21 | 1147 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line37 | 524 | 0 | 0 | 0 | 29 | 1147 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1557 | 0 | 0 | 0 | 32 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line7a | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line8 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line9 | 1558 | 0 | 0 | 0 | 31 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 920 | 0 | 0 | 0 | 74 | 706 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line10 | 158 | 0 | 0 | 0 | 4 | 123 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line11 | 162 | 0 | 0 | 0 | 0 | 123 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line3 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line4 | 273 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line6 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line7 | 251 | 0 | 0 | 0 | 16 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line9a | 266 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line9c | 250 | 0 | 0 | 0 | 0 | 35 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line13 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line17 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line18 | 1695 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line21 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line22 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line24 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line7 | 1699 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.tax | 1695 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line11 | 1540 | 0 | 0 | 0 | 0 | 121 | 0 | 0 | 39 | 39 (2.3%) |
| f8960.line12 | 1540 | 0 | 0 | 0 | 0 | 121 | 0 | 0 | 39 | 39 (2.3%) |
| f8960.line15 | 1576 | 0 | 0 | 0 | 13 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line16 | 1474 | 0 | 0 | 0 | 4 | 222 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line17 | 1477 | 0 | 0 | 0 | 1 | 222 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line8 | 1695 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 5 (0.3%) |
| f8960.tax | 1477 | 0 | 0 | 0 | 1 | 222 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line10 | 495 | 0 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line11 | 290 | 0 | 0 | 0 | 65 | 130 | 32 | 0 | 0 | 0 (0.0%) |
| f8995.line13 | 323 | 0 | 0 | 0 | 64 | 130 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line14 | 370 | 0 | 0 | 0 | 17 | 130 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line15 | 370 | 0 | 0 | 0 | 17 | 130 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line2 | 441 | 0 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line4 | 441 | 0 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line5 | 504 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line8 | 517 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line9 | 517 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line12 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line13 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line28 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line29 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line31 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line7 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line12 | 252 | 0 | 0 | 0 | 44 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 220 | 0 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line4c | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line6 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| qbi.deduction | 370 | 0 | 0 | 0 | 17 | 130 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line1 | 726 | 0 | 0 | 0 | 61 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line10 | 784 | 0 | 0 | 0 | 3 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line11 | 780 | 0 | 0 | 0 | 7 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line12 | 783 | 0 | 0 | 0 | 4 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line13 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line14 | 726 | 0 | 0 | 0 | 61 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line15 | 730 | 0 | 0 | 0 | 57 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line16 | 783 | 0 | 0 | 0 | 4 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line17 | 783 | 0 | 0 | 0 | 4 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line18 | 770 | 0 | 0 | 0 | 17 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line19 | 784 | 0 | 0 | 0 | 3 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line2 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line20 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line21 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line22 | 776 | 0 | 0 | 0 | 11 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line23 | 735 | 0 | 0 | 0 | 52 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line24 | 777 | 0 | 0 | 0 | 10 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line25 | 735 | 0 | 0 | 0 | 52 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line3 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line4 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line5 | 729 | 0 | 0 | 0 | 58 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line6 | 787 | 0 | 0 | 0 | 0 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line7 | 760 | 0 | 0 | 0 | 27 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line8 | 759 | 0 | 0 | 0 | 28 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line9 | 780 | 0 | 0 | 0 | 7 | 311 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line10 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line21 | 1589 | 0 | 0 | 0 | 0 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line26 | 1514 | 0 | 0 | 0 | 75 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line9 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1589 | 0 | 0 | 0 | 0 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1589 | 0 | 0 | 0 | 0 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1437 | 0 | 0 | 0 | 0 | 263 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1586 | 0 | 0 | 0 | 3 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line38 | 1434 | 0 | 0 | 0 | 3 | 263 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line21 | 1320 | 0 | 0 | 0 | 42 | 338 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 994 | 0 | 0 | 0 | 0 | 706 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line8 | 749 | 0 | 0 | 0 | 0 | 951 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line10 | 830 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line11 | 830 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line12 | 830 | 0 | 0 | 0 | 0 | 140 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line14 | 422 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16a | 422 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16b | 285 | 0 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line17 | 422 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line19 | 263 | 0 | 0 | 0 | 13 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line20 | 269 | 0 | 0 | 0 | 9 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line27 | 265 | 0 | 0 | 0 | 1 | 704 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line5 | 889 | 0 | 0 | 0 | 0 | 81 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line7 | 889 | 0 | 0 | 0 | 0 | 81 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line8 | 889 | 0 | 0 | 0 | 0 | 81 | 0 | 0 | 0 | 0 (0.0%) |
| sa.deduction | 1474 | 0 | 0 | 0 | 2 | 224 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line10 | 1579 | 0 | 0 | 0 | 0 | 121 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line14 | 1697 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1473 | 0 | 0 | 0 | 3 | 224 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line3 | 1558 | 0 | 0 | 0 | 28 | 111 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line4 | 1583 | 0 | 0 | 0 | 3 | 114 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5d | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5e | 1659 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 41 | 41 (2.4%) |
| sa.line7 | 1659 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 41 | 41 (2.4%) |
| sa.line8e | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sa.standard | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line13 | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line14 | 260 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line15 | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line16 | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line18 | 736 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line19 | 721 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.d | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.e | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.g | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.h | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.d | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.e | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.g | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.h | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line21 | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line6 | 260 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line7 | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.d | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.e | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.g | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.h | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.d | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.e | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.g | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.h | 1404 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line1 | 75 | 0 | 0 | 0 | 7 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line10 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line11 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line12 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line13 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line14 | 74 | 0 | 0 | 0 | 8 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line15 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line16 | 77 | 0 | 0 | 0 | 5 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line17 | 77 | 0 | 0 | 0 | 5 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line18 | 75 | 0 | 0 | 0 | 7 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line19 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line2 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line20 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line21 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line22 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line23 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line24 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line25 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line26 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line27 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line28 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line29 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line3 | 72 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line30 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line31 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line32 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line33 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line34 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line35 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line36 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line37 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line38 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line39 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line4 | 72 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line40 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line41 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line42 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line43 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line44 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line45 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line46 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line47 | 0 | 0 | 0 | 0 | 0 | 122 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line5 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line6 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line7 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line8 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line9 | 82 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line1 | 529 | 0 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line10 | 471 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line11 | 406 | 0 | 0 | 0 | 123 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line12 | 525 | 0 | 0 | 0 | 4 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line13 | 520 | 0 | 0 | 0 | 9 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line14 | 459 | 0 | 0 | 0 | 70 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line15 | 410 | 0 | 0 | 0 | 119 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line16 | 335 | 0 | 0 | 0 | 194 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line17 | 453 | 0 | 0 | 0 | 18 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line18 | 497 | 0 | 0 | 0 | 32 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line2 | 406 | 0 | 0 | 0 | 123 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line3 | 529 | 0 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line4 | 529 | 0 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line5 | 396 | 0 | 0 | 0 | 133 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line6 | 507 | 0 | 0 | 0 | 22 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line7 | 381 | 0 | 0 | 0 | 148 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line8 | 529 | 0 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line9 | 402 | 0 | 0 | 0 | 127 | 21 | 0 | 0 | 0 | 0 (0.0%) |

Exclusions:

- OpenTaxSolver 23.06's Schedule 1-A Part IV (sched_1A) truncates line 28 (`j = sched1A_L[27] / 1000.0`) where the form rounds up to the next whole number, and multiplies line 29 by $300 per $1,000 where the form says $200; the 23.07 revision history reports both fixed
- OpenTaxSolver 23.06's Schedule D Tax Worksheet (sched_D_tax_worksheet) codes the line 19 ceiling for single and married filing separately as 197,390 (the 2025 worksheet: $197,300) and runs lines 33 to 43 only when lines 1 and 32 are equal (`absolutev(ws[1]-ws[32]) < 0.01`), where the worksheet says to skip them when they are equal; the 23.07 revision history reports both fixed
- OpenTaxSolver figures Schedule A line 3 as 7.5% of a negative adjusted gross income and line 4 as `NotLessThanZero(SchedA[1] - SchedA[3])`, adding the negative floor to the medical expenses, where the instructions allow "only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income" (i1040sca, line 1). It caps lines 11 and 12 at 60% and 30% of adjusted gross income by multiplying the AGI as it stands (`if (charityCC > 0.60 * L[11]) charityCC = 0.60 * L[11]`), so a negative AGI turns gifts, even none, into a negative charitable deduction on line 14; the project's limit is the sa.charity_limited screen, which the generator answers no. Its Form 2441 program's line 8 rate lookup (GetLimit over line_8_rate_table) returns zero for an AGI below the table's first row, where the project reads the first row ("$0—15,000": 0.35) for any amount not over $15,000
- OpenTaxSolver fixes Schedule D Tax Worksheet lines 3 and 4 at zero (sched_D_tax_worksheet: `ws[3] = 0.0; /* Form 4952, line 4g. */ ws[4] = 0.0; /* Form 4952, line 4e. */`); on a return that files Form 4952 the project carries its line 4e there. Line 3 is zero on the generated returns (no line 4g election), so lines 5 and 8 and the tax are unmoved
- OpenTaxSolver has no Form 8995-A; its Form 8995 program computes the simplified deduction above the taxable income threshold, where the form sends the filer to Form 8995-A and the project refuses the return
- OpenTaxSolver takes Schedule A line 9 as entered (A9) and fixes Schedule D Tax Worksheet lines 3 and 4 at zero; it does not apply the Form 4952 net-investment-income limit, and the adapter supplies the investment interest paid
- OpenTaxSolver takes Schedule D line 19 as an input (D19, 'amount from line 18 of the Unrecaptured Section 1250 Gain Worksheet'), supplied as Form 1099-DIV box 2b; the worksheet nets the gain against the net short-term loss and the 28% worksheet amounts, which the project does
- OpenTaxSolver takes the IRA deduction as an input (S1_20), supplied as the contributions; it does not compute the IRA Deduction Worksheet's phase-out by modified AGI, so returns whose deduction is less than the contributions are not compared on the lines that follow AGI, nor on Schedule 1 line 21, whose student loan interest phase-out reads modified AGI after the IRA deduction
- OpenTaxSolver takes the earned income credit as an input (L27) and has no EIC worksheet or table; the credit is supplied as zero, so Schedule 8812 line 24 and the payment lines are not compared on returns with an EIC
- OpenTaxSolver takes the energy efficient home improvement credit as an input (S3_5b) and does not compute Form 5695; supplied as zero
- OpenTaxSolver takes the excess social security withholding credit as an input (S3_11), supplied as zero; it does not compute it from per-employer withholding
- OpenTaxSolver takes the residential clean energy credit as an input (S3_5a) and does not compute Form 5695; supplied as zero
- OpenTaxSolver takes the saver's credit as an input (S3_4) and does not compute Form 8880; the credit is supplied as zero, so the lines after the nonrefundable credits, and Schedule 8812 Credit Limit Worksheet A, are not compared on returns with one
- OpenTaxSolver's Schedule 8812 program takes the Part II-A route (`if (L16b <= 5100.0)`, taxsolve_f8812) when line 16b is exactly $5,100, where the form's line 20 asks 'On line 16b, is the amount $5,100 or more?' and sends a Yes to Part II-B when line 20 is less than line 17; with three qualifying children the engine skips Part II-B
- OpenTaxSolver's TaxRateFunction emulates the Tax Table by quantizing the amount to its band (`k = income / x; x = x * (double)k + dx`) on a double built by summing the return's lines; when the project's amount in integer cents is exactly a band boundary, the engine's double can land a hair below it (mfj-00061: 107,096.84 + 2,341.61 + 7,689.01 - 277.46 - 31,500 = 85,349.99999999999) and the band below is read; the Tax Table reads "At least" the boundary
- OpenTaxSolver's student loan interest worksheet (Calc_StudentLoan_Sched1L21) uses the exact line 7 ratio; the project rounds it to three places (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars, so returns in the phase-out are not compared on the lines that follow AGI
- the engine is given no Form 1095-A, so its tax, credits and payments omit the premium tax credit reconciliation (Form 8962) the project figures on these returns

Project result lines not mapped:

- f1040.line27a: the earned income credit is an input (L27); OTS has no EIC worksheet or table
- eic.credit: the earned income credit is an input (L27); OTS has no EIC worksheet or table
- f8880.line10: the saver's credit is an input (S3_4); OTS does not compute Form 8880
- f8880.line12: the saver's credit is an input (S3_4); OTS does not compute Form 8880
- f5695.line13: the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695
- f5695.line15: the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695
- f5695.line30: the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695
- f5695.line32: the residential energy credits are inputs (S3_5a, S3_5b); OTS does not compute Form 5695
- s3.line5a: the residential energy credits are inputs; the engine's zero would not be a computation
- s3.line5b: the residential energy credits are inputs; the engine's zero would not be a computation
- s1.line20: the IRA deduction is an input (S1_20); OTS does not compute the IRA Deduction Worksheet
- s3.line11: the excess social security withholding credit is an input (S3_11); OTS does not compute it
- eic.earned_income: no EIC computation
- eic.line1: no EIC computation
- u1250.line18: the Unrecaptured Section 1250 Gain Worksheet is not computed; its result is the input D19
- f1040.line1z: mapped (sum of Forms W-2 box 1)

## UsTaxes

| line | exact | table-adjusted | table-midpoint | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11a | 1132 | 0 | 0 | 20 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1132 | 0 | 0 | 20 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line12e | 1054 | 0 | 0 | 2 | 0 | 644 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 819 | 0 | 0 | 0 | 0 | 881 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13b | 818 | 0 | 0 | 1 | 0 | 881 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line14 | 817 | 0 | 0 | 2 | 0 | 881 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 798 | 0 | 0 | 21 | 0 | 881 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 410 | 0 | 268 | 39 | 0 | 983 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line17 | 682 | 0 | 0 | 0 | 0 | 1018 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line18 | 390 | 0 | 255 | 37 | 0 | 1018 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line19 | 390 | 0 | 25 | 0 | 0 | 1285 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line1a | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line1z | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 415 | 0 | 0 | 0 | 0 | 1285 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line21 | 390 | 0 | 25 | 0 | 0 | 1285 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line22 | 260 | 0 | 127 | 28 | 0 | 1285 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line23 | 894 | 0 | 88 | 0 | 0 | 718 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line24 | 212 | 0 | 174 | 19 | 0 | 1295 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line25a | 1330 | 0 | 0 | 0 | 0 | 370 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line25d | 1330 | 0 | 0 | 0 | 0 | 370 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line27a | 856 | 0 | 0 | 0 | 0 | 844 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 258 | 0 | 5 | 0 | 0 | 1437 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line32 | 258 | 0 | 5 | 0 | 0 | 1437 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line33 | 256 | 0 | 5 | 0 | 0 | 1439 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line34 | 162 | 0 | 90 | 9 | 0 | 1439 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line37 | 214 | 0 | 34 | 13 | 0 | 1439 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1132 | 0 | 0 | 20 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line7a | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line8 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line9 | 1132 | 0 | 0 | 20 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 324 | 0 | 316 | 23 | 0 | 1037 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line1 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line18 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line19 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line21 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line22 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line24 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line4 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line6 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line7 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.tax | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line11 | 891 | 0 | 0 | 0 | 0 | 809 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line12 | 891 | 0 | 0 | 0 | 0 | 809 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line15 | 1150 | 0 | 0 | 2 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line16 | 1029 | 0 | 0 | 1 | 0 | 670 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line17 | 940 | 0 | 90 | 0 | 0 | 670 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line8 | 1395 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 5 | 5 (0.3%) |
| f8960.line9a | 1056 | 0 | 0 | 0 | 0 | 644 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line9b | 954 | 0 | 0 | 0 | 0 | 746 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line9d | 891 | 0 | 0 | 0 | 0 | 809 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 940 | 0 | 90 | 0 | 0 | 670 | 0 | 0 | 0 | 0 (0.0%) |
| f8962.line11e | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| f8962.line25 | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| f8962.line26 | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| f8962.line29 | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| f8962.line8a | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line11 | 221 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line12 | 113 | 0 | 0 | 0 | 0 | 108 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line13 | 1316 | 0 | 0 | 0 | 0 | 384 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line3 | 188 | 0 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line5 | 188 | 0 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line6 | 106 | 0 | 0 | 0 | 0 | 115 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line8 | 113 | 0 | 0 | 0 | 0 | 108 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line1 | 503 | 0 | 0 | 12 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line10 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line11 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line12 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line13 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line14 | 503 | 0 | 0 | 12 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line15 | 503 | 0 | 0 | 12 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line16 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line17 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line18 | 502 | 0 | 0 | 13 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line19 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line2 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line20 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line21 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line22 | 324 | 0 | 187 | 4 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line23 | 292 | 0 | 187 | 36 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line24 | 320 | 0 | 189 | 6 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line25 | 292 | 0 | 187 | 36 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line3 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line4 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line5 | 503 | 0 | 0 | 12 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line6 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line7 | 509 | 0 | 0 | 6 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line8 | 509 | 0 | 0 | 6 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line9 | 515 | 0 | 0 | 0 | 0 | 555 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line10 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line11 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line13 | 1316 | 0 | 0 | 0 | 0 | 384 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line21 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line26 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line12 | 135 | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line14c | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line15 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line16 | 124 | 0 | 0 | 1 | 0 | 35 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line20 | 125 | 0 | 0 | 0 | 0 | 35 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line23 | 1266 | 0 | 0 | 0 | 0 | 434 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line24 | 1266 | 0 | 0 | 0 | 0 | 434 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line25 | 113 | 0 | 0 | 1 | 0 | 20 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line29 | 114 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line3 | 1132 | 0 | 0 | 20 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1038 | 0 | 0 | 0 | 0 | 662 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line31 | 170 | 0 | 0 | 4 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line34 | 172 | 0 | 0 | 2 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line35 | 172 | 0 | 0 | 2 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line36a | 1151 | 0 | 0 | 1 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line36b | 1151 | 0 | 0 | 1 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1150 | 0 | 0 | 2 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line38 | 1061 | 0 | 0 | 2 | 0 | 637 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line4c | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line6 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line7 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line8 | 133 | 0 | 0 | 2 | 0 | 24 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line21 | 894 | 0 | 88 | 0 | 0 | 718 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line11 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line15 | 1328 | 0 | 0 | 0 | 0 | 372 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line8 | 415 | 0 | 0 | 0 | 0 | 1285 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line9 | 36 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line10 | 611 | 0 | 0 | 0 | 0 | 176 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line11 | 611 | 0 | 0 | 0 | 0 | 176 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line12 | 611 | 0 | 0 | 0 | 0 | 176 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line14 | 170 | 0 | 25 | 0 | 0 | 592 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16a | 170 | 0 | 25 | 0 | 0 | 592 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16b | 737 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line17 | 179 | 0 | 16 | 0 | 0 | 592 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line18a | 712 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 25 | 25 (3.2%) |
| s8812.line19 | 712 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 25 | 25 (3.2%) |
| s8812.line20 | 702 | 0 | 0 | 10 | 0 | 50 | 0 | 0 | 25 | 25 (3.2%) |
| s8812.line21 | 610 | 0 | 0 | 0 | 0 | 177 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line23 | 610 | 0 | 0 | 0 | 0 | 177 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line24 | 423 | 0 | 0 | 0 | 0 | 364 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line25 | 327 | 0 | 0 | 0 | 0 | 460 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line26 | 322 | 0 | 0 | 5 | 0 | 460 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line27 | 99 | 0 | 5 | 0 | 0 | 683 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line3 | 600 | 0 | 0 | 11 | 0 | 176 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line5 | 737 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line7 | 737 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line8 | 737 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| sa.deduction | 1054 | 0 | 0 | 2 | 0 | 644 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line10 | 1056 | 0 | 0 | 0 | 0 | 644 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line14 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1054 | 0 | 0 | 2 | 0 | 644 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line3 | 1130 | 0 | 0 | 22 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line4 | 1150 | 0 | 0 | 2 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5d | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5e | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line7 | 1152 | 0 | 0 | 0 | 0 | 548 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line8e | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sa.standard | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sb.line2 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sb.line4 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line15 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line16 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line21 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line7 | 1400 | 0 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line1 | 206 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line2 | 158 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line3 | 158 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line4 | 158 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line8 | 158 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 0 (0.0%) |
| sli.line9 | 158 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line1 | 463 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line10 | 337 | 0 | 0 | 0 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line11 | 258 | 0 | 0 | 79 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line12 | 333 | 0 | 0 | 4 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line13 | 329 | 0 | 0 | 8 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line14 | 292 | 0 | 0 | 45 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line15 | 259 | 0 | 0 | 78 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line16 | 207 | 0 | 0 | 130 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line17 | 329 | 0 | 0 | 8 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line18 | 317 | 0 | 0 | 20 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line2 | 353 | 0 | 0 | 110 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line3 | 463 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line4 | 463 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line5 | 341 | 0 | 0 | 122 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line6 | 337 | 0 | 0 | 0 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line7 | 240 | 0 | 0 | 97 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line8 | 337 | 0 | 0 | 0 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line9 | 252 | 0 | 0 | 85 | 0 | 126 | 0 | 0 | 0 | 0 (0.0%) |

Exclusions:

- UsTaxes allocates part of the Schedule A state and local tax deduction to investment income on Form 8960 line 9b by the ratio of line 8 to AGI (irsForms/F8960.ts `l9b`); the generator enters no allocation (f8960.allocated_taxes is zero), so itemizers with a state and local tax deduction are not compared from line 9b on
- UsTaxes allocates part of the Schedule A state and local tax deduction to investment income on Form 8960 line 9b by the ratio of line 8 to AGI (irsForms/F8960.ts `l9b`); the generator enters no allocation (f8960.allocated_taxes is zero), so itemizers with a state and local tax deduction are not compared from line 9b on; where modified AGI is over the threshold (Form 8960 line 15) the tax lines follow
- UsTaxes allowed an earned income credit on this return (see the `eic` limitation for its method); its eligibility tests are partly stubs (ScheduleEIC.ts: `validSSNs`, `over25Under65`, `qualifyingChildOfAnother` return fixed values), so the lines the credit moves are not compared
- UsTaxes attaches Schedule 3 only for the excess social security credit, the foreign tax credit, an extension payment or Schedule R (irsForms/Schedule3.ts lines 50-54, `isNeeded`); a net premium tax credit with none of those is dropped from Schedule 3 line 15 and Form 1040 line 31 although Schedule3.ts `l9` returns it
- UsTaxes computed an alternative minimum tax (Form 6251, irsForms/F6251.ts `l11`) on this return; Form 6251 is outside the project's scope (the s2.amt screen)
- UsTaxes emulates the Tax Table by flooring the amount to whole dollars and taking the band midpoint (irsForms/TaxTable.ts `computeTax`, `Math.floor(income)`) on a double built by summing the return's lines; when the project's amount in integer cents is exactly a band boundary, the double can land a hair below it (mfj-00061: line 15 is $85,350.00 and the engine reads the $85,300 band); the Tax Table reads "At least" the boundary
- UsTaxes enters the $1,000 additional contribution for age 55 on Form 8889 line 7 in every case (irsForms/F8889.ts `l7`) and $4,300 on line 3, where the project's Line 3 Limitation Chart includes it on line 3 for an unmarried filer; line 8 is the same either way
- UsTaxes figures the Form 8889 line 7 additional contribution from the date of birth (irsForms/F8889.ts `l7`: $1,000 when the filer is 55 by December 31), the same date that gives the senior deduction; the generator answers the age-55 question (f8889 age55) independently of the age it gives a senior, so a filer 66 or older who answered no cannot be expressed to UsTaxes
- UsTaxes figures the earned income credit from Rev. Proc. formulas at a rounded income (irsForms/ScheduleEIC.ts `roundIncome`: `Math.round(Math.round(income) / 50) * 50 + 25`, which for the upper half of each $50 band reads the next band's midpoint), not from the EIC Table, keeps the unrounded formula value, and always takes the smaller of the amounts at earned income and at AGI (`credit`), where Worksheet A uses the earned income amount alone when AGI is below the phase-out threshold
- UsTaxes floors adjusted gross income at zero (irsForms/F1040.ts line 472, `l11a = Math.max(0, l9 - l10)`), where Form 1040 line 11 is line 9 minus line 10 and may be negative
- UsTaxes never builds Schedule C: irsForms/F1040.ts declares `scheduleC?: ScheduleC` and no code assigns it, so `selfEmployedIncome` reaches no form (Schedule 1 line 3, Schedule SE, the QBI deduction and earned income are all zero); returns with self-employment income are not run
- UsTaxes takes qualified business income only from Schedule K-1 (Form 1065) box 20 code Z (irsForms/F1040.ts `totalQbi`); its Form 1099-DIV has no box 5, so section 199A dividends give no Form 8995 and no line 13a deduction
- UsTaxes takes the Form 5695 Part II credit as an entered amount (CreditType.EnergyEfficientHomeImprovement, irsForms/F5695.ts `l14PartII`), supplied as the generator's credit before the limit; Schedule 3 line 5b is `f5695.l30` (Parts I and II, unlimited), it reaches Form 1040 only when Schedule 3 is needed for another reason, and Credit Limit Worksheet A subtracts it twice when Schedule 3 is needed (Schedule8812.ts lines 97-124)
- UsTaxes takes the IRA deduction as an entered amount (`otherIncome.iraDeduction`, Schedule 1 line 19a in irsForms/Schedule1.ts), supplied as the contributions; it has no IRA Deduction Worksheet, so returns whose deduction the worksheet limits are not compared on the lines that follow it
- UsTaxes takes the foreign tax credit as an entered amount (`otherIncome.foreignTaxCredit`, irsForms/Schedule3.ts `l1`), supplied as the foreign tax paid, with no limit by the tax; returns whose credit the tax limits are not compared after the credits
- UsTaxes' 28% Rate Gain Worksheet and Unrecaptured Section 1250 Gain Worksheet are stubs returning undefined (irsForms/worksheets/SDRateGainWorksheet.ts, SDUnrecaptured1250.ts) and its Form 1099-DIV has no box 2b or 2d, so Schedule D lines 18 and 19 are empty, the Schedule D Tax Worksheet is never reached (ScheduleD.ts `computeTaxOnDTaxWorksheet`) and the gain is taxed on the Qualified Dividends and Capital Gain Tax Worksheet
- UsTaxes' Form 2441 credit (irsForms/F2441.ts `credit`) is rounded to whole dollars and not limited by the tax (no line 10 or 11), and it reaches Form 1040 only when Schedule 3 is needed for another reason: Schedule3.ts `isNeeded` tests only excess social security, the foreign tax credit, an extension payment and Schedule R, and F1040.ts line 536 takes line 20 only `if schedule3.isNeeded()`; Schedule 8812 Credit Limit Worksheet A drops the Schedule 3 lines under the same test (Schedule8812.ts lines 99-111)
- UsTaxes' Form 4952 counts only taxable interest and nonqualified dividends as investment income (irsForms/F4952.ts `l4a`; lines 4b to 4d, the qualified dividends and the net gain from investment property, are left undefined), so where the limit applies its Schedule A line 9 differs from the form's
- UsTaxes' Form 4952 limited the investment interest deduction on this return (its line 4h is positive); it counts only taxable interest and nonqualified dividends as investment income (irsForms/F4952.ts `l4a`)
- UsTaxes' Form 5695 Part I (irsForms/F5695.ts `l15`) is 30% of the costs rounded to whole dollars with no limit by the tax; it enters Schedule 3 line 5a only when Schedule 3 is needed for another reason (Schedule3.ts `isNeeded`), while Credit Limit Worksheet A subtracts Form 5695 line 30 (Parts I and II together) whether or not it does, and twice when Schedule 3 is needed (once as Schedule 3 line 5b, which is `f5695.l30`, and once directly; Schedule8812.ts lines 97-124); there is no Credit Limit Worksheet B (`creditLimitWorksheetB` returns undefined)
- UsTaxes' Form 8880 (irsForms/F8880.ts `l4`) is the contributions times the rate rounded down to whole dollars, with no line 11 limit by the tax, and reaches Form 1040 line 20 only when Schedule 3 is needed for another reason (Schedule3.ts `isNeeded`, F1040.ts line 536)
- UsTaxes' Form 8889 line 6 halves the line 5 limit for any family-coverage account (irsForms/F8889.ts `splitFamilyContributionLimit`: `Math.round(this.l5() / 2)`), where the instructions split it only between spouses with separate HSAs
- UsTaxes' Form 8889 line 6 halves the line 5 limit for any family-coverage account (irsForms/F8889.ts `splitFamilyContributionLimit`: `Math.round(this.l5() / 2)`), where the instructions split it only between spouses with separate HSAs; on this return the contributions exceed UsTaxes' halved line 12, or (a joint return) UsTaxes' spouse Form 8889, which takes in every family-coverage account (F8889.ts constructor), deducts the same contributions again on Schedule 1 line 13, so line 13 and the lines after it differ
- UsTaxes' Form 8962 (irsForms/F8962.ts) applies a flat 8.5% of AGI (`applicableContributionRate`) with no federal poverty line, Table 2 or Table 5 limitation and no monthly calculation: it is the form only at 400% of the poverty line or more, on line 11, with modified AGI equal to AGI; other returns with a Form 1095-A are not compared after line 16
- UsTaxes' Schedule 1-A Part IV (irsForms/Schedule1A.ts lines 150-207) reads line 23 from `l22aiii`/`l22biii`, which return undefined, so lines 23 and 24 are empty and the car loan interest deduction (line 30) is always zero; the entered interest (`l22iiiTotal`) is never used
- UsTaxes' Schedule 1-A Part IV (irsForms/Schedule1A.ts lines 150-207) reads line 23 from `l22aiii`/`l22biii`, which return undefined, so lines 23 and 24 are empty and the car loan interest deduction (line 30) is always zero; the entered interest (`l22iiiTotal`) is never used; returns where the project's line 30 is positive are not compared from line 38 on
- UsTaxes' Schedule 8812 line 20 test is inverted and uses $4,800 (irsForms/Schedule8812.ts lines 184-194: `l20No = l16b >= 4800`), where the form asks whether line 16b is $5,100 or more and, if not, enters the smaller of lines 17 and 20 on line 27; so with one or two qualifying children UsTaxes goes to Part II-B, and with three or more it skips Part II-B, whenever line 20 is less than line 17
- UsTaxes' Schedule 8812 line 21 is the W-2 boxes 4 and 6 total (irsForms/Schedule8812.ts `part2b`, lines 221-229) in every case, where the instructions send a filer with Additional Medicare Tax to the Additional Medicare Tax and RRTA Tax Worksheet (Form 8959 lines 7 and 24 change the amount)
- UsTaxes' Social Security Benefits Worksheet line 6 adds Schedule 1 line 10 (the additional income total) to the adjustments (irsForms/worksheets/SocialSecurityBenefits.ts `l6`, first term `schedule1.l10()`), where the worksheet's line 6 is Schedule 1 lines 11 through 20, 23 and 25; returns with benefits and unemployment compensation are not compared from line 6 on
- UsTaxes' student loan interest phase-out starts at $80,000 ($165,000 married filing jointly) over $15,000 ($30,000) (data/federal.ts lines 358-364, the 2024 amounts), where the 2025 worksheet uses $85,000 ($170,000) to $100,000 ($200,000); returns whose modified AGI (worksheet line 4) lies between UsTaxes' start and the worksheet's end are not compared on the lines that follow it
- UsTaxes' student loan interest worksheet uses the unrounded line 7 ratio (irsForms/worksheets/StudentLoanInterestWorksheet.ts `l7`), where the project rounds it to three places (amb.2025.sli_ratio_places)

Project result lines not mapped:

- s1.line20: the IRA deduction is an input (`otherIncome.iraDeduction`); UsTaxes has no IRA Deduction Worksheet
- s3.line1: the foreign tax credit is an input (`otherIncome.foreignTaxCredit`), not limited by the tax
- s3.line2: Form 2441: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- f2441.line9c: Form 2441: UsTaxes exposes only the rounded credit (`credit`), not line 9
- f2441.line11: Form 2441: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- s3.line4: Form 8880: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- f8880.line10: Form 8880: the credit before the limit is rounded down to whole dollars (`l4`)
- f8880.line12: Form 8880: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- s3.line5a: Form 5695 Part I: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- f5695.line13: Form 5695 Part I: 30% of the costs rounded to whole dollars (`l15`)
- f5695.line15: Form 5695 Part I: the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 is needed for another reason (see the limitations); the lines it moves are compared on returns without it
- s3.line5b: Form 5695 Part II is an input (the credit amount itself, CreditType.EnergyEfficientHomeImprovement)
- f5695.line30: Form 5695 Part II is an input
- f5695.line32: Form 5695 Part II is an input
- eic.credit: the EIC is figured from formulas at a misrounded income (ScheduleEIC.ts `roundIncome`); Form 1040 line 27a is mapped and excluded on returns with an EIC
- eic.earned_income: UsTaxes exposes earned income only inside its EIC computation (`earnedIncome`), whose eligibility tests are stubs
- sdtw.line1: the Schedule D Tax Worksheet is never reached (the 28% and section 1250 worksheets are stubs)
- sd.line18: the 28% Rate Gain Worksheet is a stub returning undefined (worksheets/SDRateGainWorksheet.ts)
- sd.line19: the Unrecaptured Section 1250 Gain Worksheet is a stub returning undefined (worksheets/SDUnrecaptured1250.ts)
- sd.line1b.h: the Form 8949 rows UsTaxes builds from its Asset list are all box C or F (F8949.ts `part1BoxC`, `part2BoxF`), so Schedule D lines 1b, 2, 8b and 9 are empty; lines 7, 15, 16 and 21 are mapped
- f8995.line15: Form 8995 is built only for Schedule K-1 QBI (F1040.ts `totalQbi`); no generated return reaches it
- sa.line9: Form 4952 counts only interest and nonqualified dividends (F4952.ts `l4a`); lines 10 and 17 are mapped and excluded where either side's limit applies
- f4952.line8: see sa.line9
- person.f8889.line7: UsTaxes enters the age-55 additional contribution on line 7 in every case, the project on line 3 for an unmarried filer (limitation hsa_age55); line 8 is mapped
- sli.line5: UsTaxes' phase-out start is the 2024 amount (data/federal.ts `studentLoanInterest`), a parameter, not a computation
- sli.line6: the project carries the negative difference where the worksheet says to skip line 6; UsTaxes floors it at zero
- sli.line7: a ratio, not a money line
- s1a.line10: the project carries the negative difference where the form says to skip the phase-out; UsTaxes floors it at zero (likewise lines 18, 27 and 33); the part totals (lines 13, 21, 30, 37) are mapped
- s1a.line9: the phase-out thresholds (lines 9, 17, 26, 32) are parameters
- person.se_line12: UsTaxes never builds Schedule C, so self-employed returns are not run

## Explained differences

- PolicyEngine-US se-00203 f1040.line15: project 3803775 engine 3803777 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $106.47 in both, and line 13, half of it, is $53.235; the project rounds half-up to $53.24 (amb.2025.multiplication_subcent), the engine takes $53.23, so line 10 and AGI are 1 cent apart ($61,802.82 against $61,802.81); the standard deduction and the QBI deduction ($140.06) agree exactly, and the engine's float32 subtraction to line 15 adds one more cent, for 2 cents where the bound at line 15's size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US se-00293 f1040.line15: project 3977437 engine 3977439 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $3,487.87 in both, and line 13, half of it, is $1,743.935; the project rounds half-up to $1,743.94 (amb.2025.multiplication_subcent), the engine takes $1,743.93, so line 10 is 1 cent apart; the engine's gross income is 1 cent above the project's (within float32 precision at $74,283.60), so AGI is 2 cents apart ($68,112.59 against $68,112.57); the standard deduction, the QBI deduction and line 13b agree exactly, and line 15 carries the 2 cents where the bound at its size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- Tax-Calculator se-00075 f1040.line15: project 1971096 engine 1971098 — Rounding of the half of self-employment tax: Schedule SE line 12 is $822.51 in all three, and line 13, half of it, is $411.255; the project rounds half-up to $411.26 (amb.2025.multiplication_subcent), both engines take $411.25, so AGI is 1 cent apart; Schedule A, the QBI deduction and line 13b agree exactly, and Tax-Calculator's own float64 subtractions to taxable income give one more cent. Investigated 2026-10-19 when self-employment entered the generated cases.
- OpenTaxSolver gen-00000 f8995.line11: project 0 engine -454298 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00064 f8995.line11: project 0 engine -402136 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00120 f8995.line11: project 0 engine -4849094 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00123 f8995.line11: project 0 engine -1871619 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00198 f8995.line11: project 0 engine -265018 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00203 f8995.line11: project 0 engine -3523823 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00291 f8995.line11: project 0 engine -380928 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00378 f8995.line11: project 0 engine -181064 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00622 f8995.line11: project 0 engine -150944 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00832 f8995.line11: project 0 engine -2192877 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00071 f8995.line11: project 0 engine -1332223 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00108 f8995.line11: project 0 engine -312706 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00111 f8995.line11: project 0 engine -1102488 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00389 f8995.line11: project 0 engine -67292 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00010 f8995.line11: project 0 engine -2185226 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00014 f8995.line11: project 0 engine -733386 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00018 f8995.line11: project 0 engine -14783 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00019 f8995.line11: project 0 engine -1034658 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00079 f8995.line11: project 0 engine -2191191 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00101 f8995.line11: project 0 engine -118068 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00110 f8995.line11: project 0 engine -1888351 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00128 f8995.line11: project 0 engine -729203 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00142 f8995.line11: project 0 engine -337670 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00168 f8995.line11: project 0 engine -555644 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00175 f8995.line11: project 0 engine -178752 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00212 f8995.line11: project 0 engine -1807724 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00235 f8995.line11: project 0 engine -2288603 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00238 f8995.line11: project 0 engine -1058360 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00258 f8995.line11: project 0 engine -43077 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00266 f8995.line11: project 0 engine -1697919 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00289 f8995.line11: project 0 engine -2630572 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00290 f8995.line11: project 0 engine -1440946 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.

## Unexplained differences

None.
