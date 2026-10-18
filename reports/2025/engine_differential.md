# Engine differential — generated returns vs independent engines

Cases: 1000 generated single-filer returns (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f1040.line11b | 727 | 0 | 257 | 16 | 0 | 0 | 0 |
| f1040.line13a | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f1040.line15 | 662 | 0 | 255 | 81 | 2 | 0 | 0 |
| f1040.line16 | 279 | 541 | 87 | 93 | 0 | 0 | 0 |
| f1040.line19 | 581 | 79 | 0 | 340 | 0 | 0 | 0 |
| f1040.line27a | 808 | 176 | 0 | 16 | 0 | 0 | 0 |
| f1040.line28 | 608 | 52 | 0 | 340 | 0 | 0 | 0 |
| f1040.line6b | 962 | 0 | 22 | 16 | 0 | 0 | 0 |
| f1040.tax_before_credits | 260 | 524 | 92 | 124 | 0 | 0 | 0 |
| f8959.tax | 984 | 0 | 0 | 16 | 0 | 0 | 0 |
| f8960.tax | 886 | 0 | 2 | 112 | 0 | 0 | 0 |
| sa.deduction | 912 | 0 | 0 | 88 | 0 | 0 | 0 |
| sa.line17 | 910 | 0 | 2 | 88 | 0 | 0 | 0 |
| sa.standard | 984 | 0 | 0 | 16 | 0 | 0 | 0 |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US phases the student loan interest deduction out with the exact ratio; the worksheet's line 7 ratio is rounded to three places in the project (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars
- PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line10 | 854 | 0 | 0 | 146 | 0 | 0 | 0 |
| f1040.line11b | 835 | 0 | 19 | 146 | 0 | 0 | 0 |
| f1040.line13a | 730 | 0 | 0 | 270 | 0 | 0 | 0 |
| f1040.line15 | 586 | 0 | 14 | 400 | 0 | 0 | 0 |
| f1040.line16 | 208 | 356 | 38 | 398 | 0 | 0 | 0 |
| f1040.line19 | 386 | 69 | 0 | 545 | 0 | 0 | 0 |
| f1040.line20 | 601 | 1 | 0 | 398 | 0 | 0 | 0 |
| f1040.line24 | 225 | 274 | 22 | 479 | 0 | 0 | 0 |
| f1040.line27a | 702 | 152 | 0 | 146 | 0 | 0 | 0 |
| f1040.line28 | 411 | 44 | 0 | 545 | 0 | 0 | 0 |
| f1040.line6b | 838 | 0 | 16 | 146 | 0 | 0 | 0 |
| f1040.tax_before_credits | 191 | 344 | 47 | 418 | 0 | 0 | 0 |
| f8959.tax | 853 | 0 | 1 | 146 | 0 | 0 | 0 |
| f8960.tax | 808 | 0 | 0 | 192 | 0 | 0 | 0 |
| sa.deduction | 600 | 0 | 0 | 400 | 0 | 0 | 0 |
| sa.line17 | 797 | 0 | 1 | 202 | 0 | 0 | 0 |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator phases the child tax credit out by 5% of the exact excess of income over the threshold; Schedule 8812 line 10 rounds the excess up to the next multiple of $1,000 first
- Tax-Calculator takes the student loan interest deduction as a supplied amount (e03210) rather than computing the worksheet's phase-out, so returns with student loan interest are not compared
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass

## Explained differences

- PolicyEngine-US gen-00053 f1040.line15: project 12596165 engine 12596162 — Carried float32 error: PolicyEngine-US computes in float32. Its AGI (line 11b, $141,711.62) is 3 cents below the project's $141,711.65, within two units in the last place at that size (about 3.1 cents); line 10 and the standard deduction agree exactly, so line 15 (AGI less the deduction) carries the same 3 cents, which is more than two units in the last place at line 15's smaller size. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.
- PolicyEngine-US gen-00314 f1040.line15: project 6337668 engine 6337670 — Carried float32 error: PolicyEngine-US's AGI is 1 cent above the project's (within float32 precision at $79,136.84), line 10, the standard deduction and the QBI deduction agree exactly, and the float32 subtractions to line 15 add one more cent, for 2 cents. Investigated 2026-10-18 when Schedule 1 items entered the generated cases.

## Unexplained differences

None.
