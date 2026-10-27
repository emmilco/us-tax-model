# Engine differential — generated returns vs independent engines

Cases: 1700 generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). Engines run locally under .engines/ (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5, OpenTaxSolver 23.06 (package 0_README.txt; the Form 1040 program reports v23.05).

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `unrounded` (OpenTaxSolver, which computes in doubles, rounds nothing and prints each program's lines to the cent) means the engine equals the project's own derivation of the line re-evaluated in exact arithmetic without the project's half-up cent rounding of products and ratios (amb.2025.multiplication_subcent), with each amount that passes between the engine's programs taken at the cent it prints and the result printed to the cent; where the exact value is within 1/1000 cent of a half cent either neighbouring cent is the print (an engine double stays within 1/10,000 cent of the exact value at these amounts). No difference is allowed beyond what that recomputation gives; a line the adapter supplies as an amount is recomputed only where the project's value is that amount, and a case whose exact values take another branch, test or table band than the project's is not recomputed. An identified cause, not a tolerance. OpenTaxSolver builds its tax from the Tax Table below $100,000 as the form does, so it has no `table-adjusted` reading. `excluded` lines carry the engine limitation stated below; the features that trigger them are the generator's, those read off the project's values, and those the engine's adapter reports about its own run. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

Not-computed floor: the run fails when the project left more than 5% of an engine's cases without a value on a mapped line (a refusal, an unknown input, a non-money value), measured outside the allow-listed returns that do not file the form: f2441.line11 unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f2441.line9c unknown where `f2441.care` is false (Form 2441 is not filed without care expenses; Schedule 3 line 2 carries the zero and is compared on every return); f5695.line13 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line15 unknown where `f5695.part1_any` is false (Form 5695 Part I is not filed without Part I costs; Schedule 3 line 5a carries the zero and is compared on every return); f5695.line30 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return); f5695.line32 unknown where `f5695.part2_any` is false (Form 5695 Part II is not filed without Part II costs; Schedule 3 line 5b carries the zero and is compared on every return).

## PolicyEngine-US

| line | exact | table-adjusted | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1214 | 0 | 186 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1401 | 0 | 299 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1561 | 0 | 81 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line11b | 1100 | 0 | 542 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line13a | 1492 | 0 | 19 | 0 | 118 | 0 | 0 | 71 | 71 (4.2%) |
| f1040.line13b | 1538 | 0 | 1 | 0 | 140 | 0 | 0 | 21 | 21 (1.2%) |
| f1040.line15 | 948 | 0 | 453 | 0 | 235 | 4 | 0 | 60 | 60 (3.5%) |
| f1040.line16 | 456 | 799 | 116 | 0 | 268 | 1 | 0 | 60 | 60 (3.5%) |
| f1040.line19 | 843 | 123 | 0 | 0 | 691 | 0 | 0 | 43 | 43 (2.5%) |
| f1040.line27a | 1395 | 247 | 0 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| f1040.line28 | 886 | 79 | 1 | 0 | 691 | 0 | 0 | 43 | 43 (2.5%) |
| f1040.line6b | 1639 | 0 | 29 | 0 | 17 | 0 | 0 | 15 | 15 (0.9%) |
| f1040.tax_before_credits | 420 | 772 | 134 | 0 | 314 | 0 | 0 | 60 | 60 (3.5%) |
| f2441.line11 | 213 | 14 | 0 | 0 | 268 | 0 | 0 | 1205 | 9 (0.5%) |
| f2441.line9c | 277 | 0 | 0 | 0 | 17 | 0 | 0 | 1406 | 5 (0.3%) |
| f5695.line13 | 169 | 0 | 3 | 0 | 17 | 0 | 0 | 1511 | 0 (0.0%) |
| f5695.line15 | 93 | 43 | 1 | 0 | 268 | 0 | 0 | 1295 | 4 (0.2%) |
| f5695.line30 | 139 | 0 | 7 | 0 | 57 | 0 | 0 | 1497 | 0 (0.0%) |
| f5695.line32 | 111 | 7 | 5 | 0 | 305 | 0 | 0 | 1272 | 3 (0.2%) |
| f8880.line10 | 1636 | 0 | 3 | 0 | 20 | 0 | 0 | 41 | 41 (2.4%) |
| f8880.line12 | 1377 | 12 | 1 | 0 | 271 | 0 | 0 | 39 | 39 (2.3%) |
| f8959.tax | 1678 | 0 | 5 | 0 | 17 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1489 | 0 | 3 | 0 | 169 | 0 | 0 | 39 | 39 (2.3%) |
| person[taxpayer].se_line12 | 1655 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1621 | 0 | 79 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1621 | 0 | 79 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line20 | 1642 | 0 | 0 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| s1a.line13 | 1557 | 0 | 0 | 0 | 140 | 0 | 0 | 3 | 3 (0.2%) |
| s1a.line21 | 1556 | 0 | 0 | 0 | 140 | 0 | 0 | 4 | 4 (0.2%) |
| s1a.line30 | 1555 | 0 | 0 | 0 | 140 | 0 | 0 | 5 | 5 (0.3%) |
| s1a.line37 | 1669 | 0 | 1 | 0 | 17 | 0 | 0 | 13 | 13 (0.8%) |
| s2.line4 | 1655 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 1409 | 14 | 0 | 0 | 268 | 0 | 0 | 9 | 9 (0.5%) |
| s3.line5a | 1384 | 43 | 1 | 0 | 268 | 0 | 0 | 4 | 4 (0.2%) |
| s3.line5b | 1380 | 7 | 5 | 0 | 305 | 0 | 0 | 3 | 3 (0.2%) |
| s8812.line12 | 1642 | 0 | 0 | 0 | 17 | 0 | 0 | 41 | 41 (2.4%) |
| sa.deduction | 1529 | 0 | 4 | 0 | 152 | 0 | 0 | 15 | 15 (0.9%) |
| sa.line17 | 1530 | 0 | 3 | 0 | 152 | 0 | 0 | 15 | 15 (0.9%) |
| sa.standard | 1683 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 (0.0%) |

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

| line | exact | table-adjusted | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| eic.earned_income | 1400 | 0 | 0 | 0 | 300 | 0 | 0 | 0 | 0 (0.0%) |
| eic.line1 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line10 | 1302 | 0 | 68 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1273 | 0 | 97 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 1043 | 0 | 6 | 0 | 633 | 0 | 0 | 18 | 18 (1.1%) |
| f1040.line13b | 1368 | 0 | 2 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 835 | 0 | 66 | 0 | 798 | 1 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 352 | 507 | 59 | 0 | 765 | 0 | 0 | 17 | 17 (1.0%) |
| f1040.line19 | 624 | 82 | 0 | 0 | 994 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 635 | 293 | 0 | 0 | 765 | 0 | 0 | 7 | 7 (0.4%) |
| f1040.line24 | 438 | 323 | 88 | 0 | 834 | 0 | 0 | 17 | 17 (1.0%) |
| f1040.line27a | 1162 | 208 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 652 | 54 | 0 | 0 | 994 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1344 | 0 | 26 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 322 | 489 | 79 | 0 | 793 | 0 | 0 | 17 | 17 (1.0%) |
| f2441.line11 | 158 | 7 | 0 | 0 | 765 | 0 | 0 | 770 | 1 (0.1%) |
| f8959.tax | 1366 | 0 | 4 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1306 | 0 | 0 | 0 | 394 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line12 | 1656 | 0 | 44 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line15 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1370 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1370 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1370 | 0 | 0 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1368 | 0 | 2 | 0 | 330 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line4 | 1656 | 0 | 44 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 927 | 7 | 0 | 0 | 765 | 0 | 0 | 1 | 1 (0.1%) |
| sa.deduction | 900 | 0 | 2 | 0 | 798 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1193 | 0 | 2 | 0 | 505 | 0 | 0 | 0 | 0 (0.0%) |

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

## OpenTaxSolver

| line | exact | table-adjusted | float | unrounded | excluded | explained | UNEXPLAINED | not computed | not computed outside the allow-list (share) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 1516 | 0 | 0 | 75 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line11b | 1486 | 0 | 0 | 105 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line12e | 1494 | 0 | 0 | 2 | 204 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13a | 376 | 0 | 0 | 17 | 124 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line13b | 1436 | 0 | 0 | 3 | 261 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line14 | 1231 | 0 | 0 | 21 | 448 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line15 | 1167 | 0 | 0 | 85 | 448 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line16 | 1034 | 0 | 0 | 57 | 609 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line17 | 1590 | 0 | 0 | 0 | 110 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line18 | 1034 | 0 | 0 | 57 | 609 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line19 | 463 | 0 | 0 | 0 | 507 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line1z | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line20 | 826 | 0 | 0 | 0 | 874 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line21 | 826 | 0 | 0 | 0 | 874 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line22 | 780 | 0 | 0 | 46 | 874 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line23 | 1454 | 0 | 0 | 45 | 201 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line24 | 761 | 0 | 0 | 65 | 874 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line25d | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line28 | 291 | 0 | 0 | 1 | 678 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line32 | 611 | 0 | 0 | 1 | 1088 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line33 | 611 | 0 | 0 | 1 | 1088 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line34 | 587 | 0 | 0 | 25 | 1088 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line37 | 581 | 0 | 0 | 31 | 1088 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line6b | 1559 | 0 | 0 | 32 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line7a | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line8 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.line9 | 1559 | 0 | 0 | 32 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| f1040.tax_before_credits | 1006 | 0 | 0 | 85 | 609 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line10 | 168 | 0 | 0 | 7 | 110 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line11 | 175 | 0 | 0 | 0 | 110 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line3 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line4 | 273 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line6 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line7 | 251 | 0 | 0 | 17 | 17 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line9a | 267 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| f2441.line9c | 267 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line13 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line17 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line18 | 1695 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line21 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line22 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line24 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.line7 | 1699 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8959.tax | 1695 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line11 | 1559 | 0 | 0 | 0 | 102 | 0 | 0 | 39 | 39 (2.3%) |
| f8960.line12 | 1559 | 0 | 0 | 0 | 102 | 0 | 0 | 39 | 39 (2.3%) |
| f8960.line15 | 1578 | 0 | 0 | 13 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line16 | 1495 | 0 | 0 | 4 | 201 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line17 | 1498 | 0 | 0 | 1 | 201 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.line8 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8960.tax | 1498 | 0 | 0 | 1 | 201 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line10 | 495 | 0 | 0 | 22 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line11 | 294 | 0 | 0 | 66 | 124 | 33 | 0 | 0 | 0 (0.0%) |
| f8995.line13 | 328 | 0 | 0 | 65 | 124 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line14 | 375 | 0 | 0 | 18 | 124 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line15 | 376 | 0 | 0 | 17 | 124 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line2 | 441 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line4 | 441 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line5 | 504 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line8 | 517 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| f8995.line9 | 517 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line12 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].f8889[hsa].line13 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line28 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line29 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line31 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].sc[biz].line7 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line12 | 252 | 0 | 0 | 44 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line13 | 220 | 0 | 0 | 76 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line4c | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| person[taxpayer].se_line6 | 296 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| qbi.deduction | 376 | 0 | 0 | 17 | 124 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line1 | 744 | 0 | 0 | 61 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line10 | 803 | 0 | 0 | 2 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line11 | 799 | 0 | 0 | 6 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line12 | 801 | 0 | 0 | 4 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line13 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line14 | 744 | 0 | 0 | 61 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line15 | 749 | 0 | 0 | 56 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line16 | 801 | 0 | 0 | 4 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line17 | 801 | 0 | 0 | 4 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line18 | 788 | 0 | 0 | 17 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line19 | 803 | 0 | 0 | 2 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line2 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line20 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line21 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line22 | 794 | 0 | 0 | 11 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line23 | 748 | 0 | 0 | 57 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line24 | 793 | 0 | 0 | 12 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line25 | 748 | 0 | 0 | 57 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line3 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line4 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line5 | 747 | 0 | 0 | 58 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line6 | 805 | 0 | 0 | 0 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line7 | 778 | 0 | 0 | 27 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line8 | 776 | 0 | 0 | 29 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| qdcg.line9 | 799 | 0 | 0 | 6 | 305 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line10 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line21 | 1677 | 0 | 0 | 0 | 17 | 0 | 0 | 6 | 6 (0.4%) |
| s1.line26 | 1516 | 0 | 0 | 75 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| s1.line9 | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line13 | 1591 | 0 | 0 | 0 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line21 | 1591 | 0 | 0 | 0 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line30 | 1439 | 0 | 0 | 0 | 261 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line37 | 1588 | 0 | 0 | 3 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| s1a.line38 | 1436 | 0 | 0 | 3 | 261 | 0 | 0 | 0 | 0 (0.0%) |
| s2.line21 | 1454 | 0 | 0 | 45 | 201 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line2 | 1091 | 0 | 0 | 0 | 609 | 0 | 0 | 0 | 0 (0.0%) |
| s3.line8 | 826 | 0 | 0 | 0 | 874 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line10 | 908 | 0 | 0 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line11 | 908 | 0 | 0 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line12 | 908 | 0 | 0 | 0 | 62 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line14 | 463 | 0 | 0 | 0 | 507 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16a | 463 | 0 | 0 | 0 | 507 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line16b | 317 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line17 | 463 | 0 | 0 | 0 | 507 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line19 | 293 | 0 | 0 | 15 | 7 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line20 | 299 | 0 | 0 | 11 | 7 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line27 | 291 | 0 | 0 | 1 | 678 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line5 | 970 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line7 | 970 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| s8812.line8 | 970 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sa.deduction | 1494 | 0 | 0 | 2 | 204 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line10 | 1598 | 0 | 0 | 0 | 102 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line14 | 1697 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line17 | 1493 | 0 | 0 | 3 | 204 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line3 | 1559 | 0 | 0 | 29 | 109 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line4 | 1585 | 0 | 0 | 3 | 112 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5d | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sa.line5e | 1659 | 0 | 0 | 0 | 0 | 0 | 0 | 41 | 41 (2.4%) |
| sa.line7 | 1659 | 0 | 0 | 0 | 0 | 0 | 0 | 41 | 41 (2.4%) |
| sa.line8e | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sa.standard | 1700 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line13 | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line15 | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line16 | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line18 | 810 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line19 | 798 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.d | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.e | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.g | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line1b.h | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.d | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.e | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.g | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line2.h | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line21 | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line7 | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.d | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.e | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.g | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line8b.h | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.d | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.e | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.g | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sd.line9.h | 1354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line1 | 90 | 0 | 0 | 8 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line10 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line11 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line12 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line13 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line14 | 89 | 0 | 0 | 9 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line15 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line16 | 93 | 0 | 0 | 5 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line17 | 93 | 0 | 0 | 5 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line18 | 90 | 0 | 0 | 8 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line19 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line2 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line20 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line21 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line22 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line23 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line24 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line25 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line26 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line27 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line28 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line29 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line3 | 85 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line30 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line31 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line32 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line33 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line34 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line35 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line36 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line37 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line38 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line39 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line4 | 85 | 0 | 0 | 0 | 50 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line40 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line41 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line42 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line43 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line44 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line45 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line46 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line47 | 0 | 0 | 0 | 0 | 135 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line5 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line6 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line7 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line8 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| sdtw.line9 | 98 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line1 | 529 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line10 | 472 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line11 | 403 | 0 | 0 | 126 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line12 | 525 | 0 | 0 | 4 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line13 | 519 | 0 | 0 | 10 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line14 | 458 | 0 | 0 | 71 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line15 | 412 | 0 | 0 | 117 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line16 | 336 | 0 | 0 | 193 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line17 | 454 | 0 | 0 | 18 | 18 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line18 | 497 | 0 | 0 | 32 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line2 | 406 | 0 | 0 | 123 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line3 | 529 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line4 | 529 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line5 | 394 | 0 | 0 | 135 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line6 | 507 | 0 | 0 | 22 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line7 | 378 | 0 | 0 | 151 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line8 | 529 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 (0.0%) |
| ssb.line9 | 399 | 0 | 0 | 130 | 21 | 0 | 0 | 0 | 0 (0.0%) |

Exclusions:

- OpenTaxSolver 23.06's Schedule 1-A Part IV (sched_1A) truncates line 28 (`j = sched1A_L[27] / 1000.0`) where the form rounds up to the next whole number, and multiplies line 29 by $300 per $1,000 where the form says $200; the 23.07 revision history reports both fixed
- OpenTaxSolver 23.06's Schedule D Tax Worksheet (sched_D_tax_worksheet) codes the line 19 ceiling for single and married filing separately as 197,390 (the 2025 worksheet: $197,300) and runs lines 33 to 43 only when lines 1 and 32 are equal (`absolutev(ws[1]-ws[32]) < 0.01`), where the worksheet says to skip them when they are equal; the 23.07 revision history reports both fixed
- OpenTaxSolver computed an alternative minimum tax (Form 6251, Schedule 2 line 2) on this return; Form 6251 is outside the project's scope (the s2.amt screen), so the lines from Schedule 2 line 3 onward are not compared
- OpenTaxSolver figures Schedule A line 3 as 7.5% of a negative adjusted gross income and line 4 as `NotLessThanZero(SchedA[1] - SchedA[3])`, adding the negative floor to the medical expenses, where the instructions allow "only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income" (i1040sca, line 1). It caps lines 11 and 12 at 60% and 30% of adjusted gross income by multiplying the AGI as it stands (`if (charityCC > 0.60 * L[11]) charityCC = 0.60 * L[11]`), so a negative AGI turns gifts, even none, into a negative charitable deduction on line 14; the project's limit is the sa.charity_limited screen, which the generator answers no. Its Form 2441 program's line 8 rate lookup (GetLimit over line_8_rate_table) returns zero for an AGI below the table's first row, where the project reads the first row ("$0—15,000": 0.35) for any amount not over $15,000
- OpenTaxSolver fixes Schedule D Tax Worksheet lines 3 and 4 at zero (sched_D_tax_worksheet: `ws[3] = 0.0; /* Form 4952, line 4g. */ ws[4] = 0.0; /* Form 4952, line 4e. */`); on a return that files Form 4952 the project carries its line 4e there. Line 3 is zero on the generated returns (no line 4g election), so lines 5 and 8 and the tax are unmoved
- OpenTaxSolver has no Form 8995-A; its Form 8995 program computes the simplified deduction above the taxable income threshold, where the form sends the filer to Form 8995-A and the project refuses the return
- OpenTaxSolver takes Schedule A line 9 as entered (A9) and fixes Schedule D Tax Worksheet lines 3 and 4 at zero; it does not apply the Form 4952 net-investment-income limit, and the adapter supplies the investment interest paid
- OpenTaxSolver takes Schedule D line 19 as an input (D19, 'amount from line 18 of the Unrecaptured Section 1250 Gain Worksheet'), supplied as Form 1099-DIV box 2b; the worksheet nets the gain against the net short-term loss and the 28% worksheet amounts, which the project does
- OpenTaxSolver takes the IRA deduction as an input (S1_20), supplied as the contributions; it does not compute the IRA Deduction Worksheet's phase-out by modified AGI, so returns whose deduction is less than the contributions are not compared on the lines that follow AGI
- OpenTaxSolver takes the earned income credit as an input (L27) and has no EIC worksheet or table; the credit is supplied as zero, so Schedule 8812 line 24 and the payment lines are not compared on returns with an EIC
- OpenTaxSolver takes the energy efficient home improvement credit as an input (S3_5b) and does not compute Form 5695; supplied as zero
- OpenTaxSolver takes the excess social security withholding credit as an input (S3_11), supplied as zero; it does not compute it from per-employer withholding
- OpenTaxSolver takes the residential clean energy credit as an input (S3_5a) and does not compute Form 5695; supplied as zero
- OpenTaxSolver takes the saver's credit as an input (S3_4) and does not compute Form 8880; the credit is supplied as zero, so the lines after the nonrefundable credits, and Schedule 8812 Credit Limit Worksheet A, are not compared on returns with one
- OpenTaxSolver's Schedule 8812 program takes the Part II-A route (`if (L16b <= 5100.0)`, taxsolve_f8812) when line 16b is exactly $5,100, where the form's line 20 asks 'On line 16b, is the amount $5,100 or more?' and sends a Yes to Part II-B when line 20 is less than line 17; with three qualifying children the engine skips Part II-B
- OpenTaxSolver's TaxRateFunction emulates the Tax Table by quantizing the amount to its band (`k = income / x; x = x * (double)k + dx`) on a double built by summing the return's lines; when the project's amount in integer cents is exactly a band boundary, the engine's double can land a hair below it (mfj-00061: 107,096.84 + 2,341.61 + 7,689.01 - 277.46 - 31,500 = 85,349.99999999999) and the band below is read; the Tax Table reads "At least" the boundary
- OpenTaxSolver's student loan interest worksheet (Calc_StudentLoan_Sched1L21) uses the exact line 7 ratio; the project rounds it to three places (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars, so returns in the phase-out are not compared on the lines that follow AGI

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

## Explained differences

- PolicyEngine-US gen-00314 f1040.line15: project 5087668 engine 5087670 — Carried float32 error: PolicyEngine-US's AGI is 1 cent above the project's (within float32 precision at $79,136.84), line 10, the standard deduction and the QBI deduction agree exactly, and the float32 subtractions to line 15 add one more cent, for 2 cents. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.
- PolicyEngine-US gen-00372 f1040.line15: project 23286983 engine 23286988 — Carried float32 error: PolicyEngine-US's AGI ($261,861.22) is 4 cents above the project's ($261,861.18), within two units in the last place at that size (about 3.1 cents, rounded up to 4); line 10 (the IRA deduction, $1,823.63) and the itemized deduction ($28,991.35) agree exactly, and the float32 subtraction to line 15 adds one more cent, for 5 cents where the bound at line 15's size is 4 cents. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US gen-00372 f1040.line16: project 5156768 engine 5156770 — Carried float32 error: PolicyEngine-US's taxable income is 5 cents above the project's (its line 15 difference, explained separately), and the rate schedule both use above $100,000 taxes the 5 cents at 32% (taxable income $232,869.83, single), 1.6 cents, which the engine's float32 arithmetic rounds to 2 cents; the bound at line 16's size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US se-00203 f1040.line15: project 3803775 engine 3803777 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $106.47 in both, and line 13, half of it, is $53.235; the project rounds half-up to $53.24 (amb.2025.multiplication_subcent), the engine takes $53.23, so line 10 and AGI are 1 cent apart ($61,802.82 against $61,802.81); the standard deduction and the QBI deduction ($140.06) agree exactly, and the engine's float32 subtraction to line 15 adds one more cent, for 2 cents where the bound at line 15's size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- PolicyEngine-US se-00293 f1040.line15: project 3977437 engine 3977439 — Rounding of the half of self-employment tax plus float32: Schedule SE line 12 is $3,487.87 in both, and line 13, half of it, is $1,743.935; the project rounds half-up to $1,743.94 (amb.2025.multiplication_subcent), the engine takes $1,743.93, so line 10 is 1 cent apart; the engine's gross income is 1 cent above the project's (within float32 precision at $74,283.60), so AGI is 2 cents apart ($68,112.59 against $68,112.57); the standard deduction, the QBI deduction and line 13b agree exactly, and line 15 carries the 2 cents where the bound at its size is 1 cent. Investigated 2026-10-22 when IRA contributions entered the generated cases.
- Tax-Calculator se-00075 f1040.line15: project 1971096 engine 1971098 — Rounding of the half of self-employment tax: Schedule SE line 12 is $822.51 in all three, and line 13, half of it, is $411.255; the project rounds half-up to $411.26 (amb.2025.multiplication_subcent), both engines take $411.25, so AGI is 1 cent apart; Schedule A, the QBI deduction and line 13b agree exactly, and Tax-Calculator's own float64 subtractions to taxable income give one more cent. Investigated 2026-10-19 when self-employment entered the generated cases.
- OpenTaxSolver gen-00000 f8995.line11: project 0 engine -454298 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00064 f8995.line11: project 0 engine -402136 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00120 f8995.line11: project 0 engine -4849094 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00123 f8995.line11: project 0 engine -1871619 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00198 f8995.line11: project 0 engine -265018 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00203 f8995.line11: project 0 engine -3423615 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00291 f8995.line11: project 0 engine -309497 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00378 f8995.line11: project 0 engine -181064 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00622 f8995.line11: project 0 engine -150944 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00832 f8995.line11: project 0 engine -2192877 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver gen-00948 f8995.line11: project 0 engine -2359717 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00071 f8995.line11: project 0 engine -1332223 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00108 f8995.line11: project 0 engine -312706 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00111 f8995.line11: project 0 engine -1102488 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver mfj-00389 f8995.line11: project 0 engine -67292 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00010 f8995.line11: project 0 engine -1594725 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00014 f8995.line11: project 0 engine -733386 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00018 f8995.line11: project 0 engine -14783 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00019 f8995.line11: project 0 engine -1034658 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00079 f8995.line11: project 0 engine -2191191 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00101 f8995.line11: project 0 engine -118068 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00110 f8995.line11: project 0 engine -1888351 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00128 f8995.line11: project 0 engine -419301 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00142 f8995.line11: project 0 engine -337670 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00168 f8995.line11: project 0 engine -555644 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00175 f8995.line11: project 0 engine -178752 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00212 f8995.line11: project 0 engine -1807724 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00226 f8995.line11: project 0 engine -1300344 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00235 f8995.line11: project 0 engine -2243123 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00258 f8995.line11: project 0 engine -43077 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00266 f8995.line11: project 0 engine -1697919 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00289 f8995.line11: project 0 engine -2630572 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.
- OpenTaxSolver se-00290 f8995.line11: project 0 engine -1440946 — Form 8995 line 11 on a return whose deductions exceed adjusted gross income: the project floors qbi.taxable_before at zero (subtract_floor0), OpenTaxSolver prints the signed difference (taxsolve_f8995: `L[11] = f1040i.L11a - f1040i.L12 - f1040i.L13b`). The instructions define the line as an arithmetic difference with no floor, so the engine's reading follows the text and the project's sign is a candidate defect; line 13 (line 11 less line 12, not below zero) is zero on both sides, so the deduction is unmoved.

## Unexplained differences

None.
