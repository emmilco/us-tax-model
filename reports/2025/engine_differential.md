# Engine differential — generated returns vs independent engines

Cases: 1000 generated single-filer returns (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f1040.line11b | 727 | 0 | 257 | 16 | 0 | 0 | 0 |
| f1040.line13a | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f1040.line13b | 922 | 0 | 1 | 77 | 0 | 0 | 0 |
| f1040.line15 | 619 | 0 | 240 | 138 | 3 | 0 | 0 |
| f1040.line16 | 259 | 521 | 71 | 149 | 0 | 0 | 0 |
| f1040.line19 | 534 | 86 | 0 | 380 | 0 | 0 | 0 |
| f1040.line27a | 813 | 171 | 0 | 16 | 0 | 0 | 0 |
| f1040.line28 | 569 | 51 | 0 | 380 | 0 | 0 | 0 |
| f1040.line6b | 962 | 0 | 22 | 16 | 0 | 0 | 0 |
| f1040.tax_before_credits | 239 | 505 | 78 | 178 | 0 | 0 | 0 |
| f8959.tax | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f8960.tax | 886 | 0 | 2 | 112 | 0 | 0 | 0 |
| sa.deduction | 911 | 0 | 1 | 88 | 0 | 0 | 0 |
| sa.line17 | 910 | 0 | 2 | 88 | 0 | 0 | 0 |
| sa.standard | 984 | 0 | 0 | 16 | 0 | 0 | 0 |

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
| f1040.line10 | 854 | 0 | 0 | 146 | 0 | 0 | 0 |
| f1040.line11b | 835 | 0 | 19 | 146 | 0 | 0 | 0 |
| f1040.line13a | 730 | 0 | 0 | 270 | 0 | 0 | 0 |
| f1040.line13b | 853 | 0 | 1 | 146 | 0 | 0 | 0 |
| f1040.line15 | 568 | 0 | 16 | 416 | 0 | 0 | 0 |
| f1040.line16 | 220 | 346 | 36 | 398 | 0 | 0 | 0 |
| f1040.line19 | 429 | 74 | 0 | 497 | 0 | 0 | 0 |
| f1040.line20 | 599 | 3 | 0 | 398 | 0 | 0 | 0 |
| f1040.line24 | 280 | 258 | 44 | 418 | 0 | 0 | 0 |
| f1040.line27a | 707 | 147 | 0 | 146 | 0 | 0 | 0 |
| f1040.line28 | 458 | 45 | 0 | 497 | 0 | 0 | 0 |
| f1040.line6b | 838 | 0 | 16 | 146 | 0 | 0 | 0 |
| f1040.tax_before_credits | 204 | 334 | 44 | 418 | 0 | 0 | 0 |
| f8959.tax | 853 | 0 | 1 | 146 | 0 | 0 | 0 |
| f8960.tax | 808 | 0 | 0 | 192 | 0 | 0 | 0 |
| sa.deduction | 584 | 0 | 0 | 416 | 0 | 0 | 0 |
| sa.line17 | 741 | 0 | 1 | 258 | 0 | 0 | 0 |

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

## Unexplained differences

None.
