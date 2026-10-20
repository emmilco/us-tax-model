# Engine differential — generated returns vs independent engines

Cases: 1700 generated returns, single, head of household and married filing jointly (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 1600 | 0 | 80 | 20 | 0 | 0 | 0 |
| f1040.line11b | 1123 | 0 | 557 | 20 | 0 | 0 | 0 |
| f1040.line13a | 1527 | 0 | 20 | 121 | 0 | 0 | 32 |
| f1040.line13b | 1555 | 0 | 1 | 144 | 0 | 0 | 0 |
| f1040.line15 | 959 | 0 | 478 | 239 | 3 | 0 | 21 |
| f1040.line16 | 453 | 824 | 138 | 264 | 0 | 0 | 21 |
| f1040.line19 | 884 | 140 | 0 | 661 | 0 | 0 | 15 |
| f1040.line27a | 1435 | 245 | 0 | 20 | 0 | 0 | 0 |
| f1040.line28 | 937 | 86 | 1 | 661 | 0 | 0 | 15 |
| f1040.line6b | 1650 | 0 | 30 | 20 | 0 | 0 | 0 |
| f1040.tax_before_credits | 416 | 797 | 156 | 310 | 0 | 0 | 21 |
| f8959.tax | 1675 | 0 | 5 | 20 | 0 | 0 | 0 |
| f8960.tax | 1526 | 0 | 2 | 172 | 0 | 0 | 0 |
| s1.line15 | 1621 | 0 | 79 | 0 | 0 | 0 | 0 |
| s2.line4 | 1655 | 0 | 45 | 0 | 0 | 0 | 0 |
| sa.deduction | 1567 | 0 | 4 | 129 | 0 | 0 | 0 |
| sa.line17 | 1566 | 0 | 5 | 129 | 0 | 0 | 0 |
| sa.standard | 1680 | 0 | 0 | 20 | 0 | 0 | 0 |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US phases the student loan interest deduction out with the exact ratio; the worksheet's line 7 ratio is rounded to three places in the project (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars
- PolicyEngine-US reduces the tips, overtime and car loan interest deductions by the rate times the exact excess of modified AGI over the threshold; Schedule 1-A lines 11, 19 and 28 count whole $1,000 steps (rounded down, down and up) first
- PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 1382 | 0 | 69 | 249 | 0 | 0 | 0 |
| f1040.line11b | 1351 | 0 | 100 | 249 | 0 | 0 | 0 |
| f1040.line13a | 1105 | 0 | 6 | 571 | 0 | 0 | 18 |
| f1040.line13b | 1449 | 0 | 2 | 249 | 0 | 0 | 0 |
| f1040.line15 | 903 | 0 | 69 | 727 | 1 | 0 | 0 |
| f1040.line16 | 376 | 536 | 61 | 710 | 0 | 0 | 17 |
| f1040.line19 | 715 | 109 | 0 | 876 | 0 | 0 | 0 |
| f1040.line20 | 983 | 3 | 0 | 710 | 0 | 0 | 4 |
| f1040.line24 | 450 | 407 | 86 | 740 | 0 | 0 | 17 |
| f1040.line27a | 1246 | 205 | 0 | 249 | 0 | 0 | 0 |
| f1040.line28 | 759 | 65 | 0 | 876 | 0 | 0 | 0 |
| f1040.line6b | 1425 | 0 | 26 | 249 | 0 | 0 | 0 |
| f1040.tax_before_credits | 344 | 518 | 81 | 740 | 0 | 0 | 17 |
| f8959.tax | 1447 | 0 | 4 | 249 | 0 | 0 | 0 |
| f8960.tax | 1384 | 0 | 0 | 316 | 0 | 0 | 0 |
| s1.line15 | 1624 | 0 | 76 | 0 | 0 | 0 | 0 |
| s2.line4 | 1656 | 0 | 44 | 0 | 0 | 0 | 0 |
| sa.deduction | 972 | 0 | 1 | 727 | 0 | 0 | 0 |
| sa.line17 | 1267 | 0 | 2 | 431 | 0 | 0 | 0 |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator takes the standard deduction whenever the tax is the same either way; when the Schedule 1-A deductions leave no tax even with the standard deduction zeroed, its forced pass also takes the standard deduction, so the itemized total is not compared
- Tax-Calculator takes the student loan interest deduction as a supplied amount (e03210) rather than computing the worksheet's phase-out, so returns with student loan interest are not compared
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass

## Explained differences

- PolicyEngine-US gen-00053 f1040.line15: project 12596165 engine 12596162 — Carried float32 error: PolicyEngine-US computes in float32. Its AGI (line 11b, $141,711.62) is 3 cents below the project's $141,711.65, within two units in the last place at that size (about 3.1 cents); line 10 and the standard deduction agree exactly, so line 15 (AGI less the deduction) carries the same 3 cents, which is more than two units in the last place at line 15's smaller size. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.
- PolicyEngine-US gen-00314 f1040.line15: project 5087668 engine 5087670 — Carried float32 error: PolicyEngine-US's AGI is 1 cent above the project's (within float32 precision at $79,136.84), line 10, the standard deduction and the QBI deduction agree exactly, and the float32 subtractions to line 15 add one more cent, for 2 cents. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.
- PolicyEngine-US gen-00919 f1040.line15: project 6140836 engine 6140838 — Carried float32 error: PolicyEngine-US's AGI is 1 cent above the project's ($87,942.70 against $87,942.69, within float32 precision at that size); the deduction (sa.deduction) and the Schedule 1-A deduction on line 13b (the enhanced deduction for seniors, $5,223.44) agree exactly, and the float32 subtractions to line 15 add one more cent, for 2 cents. Investigated 2026-10-18 when Schedule 1-A entered the generated cases.
- Tax-Calculator se-00075 f1040.line15: project 1971096 engine 1971098 — Rounding of the half of self-employment tax: Schedule SE line 12 is $822.51 in all three, and line 13, half of it, is $411.255; the project rounds half-up to $411.26 (amb.2025.multiplication_subcent), both engines take $411.25, so AGI is 1 cent apart; Schedule A, the QBI deduction and line 13b agree exactly, and Tax-Calculator's own float64 subtractions to taxable income give one more cent. Investigated 2026-10-19 when self-employment entered the generated cases.

## Unexplained differences

None.
