# Engine differential — generated returns vs independent engines

Cases: 1000 generated single-filer returns (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. For Form 1040 line 27a, `table-adjusted` means the engine is within $1 of the project's Worksheet A path recomputed with each EIC Table lookup replaced by the credit at the exact amount (the engines compute from the formula where the instructions prescribe the table built at each $50 band's midpoint); the $1 allows for the engines' statutory percentages, which the archive does not hold, against the rates the Rev. Proc. 2024-40 amounts imply (at most about $0.20 apart over the table's range). `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 743 | 0 | 257 | 0 | 0 | 0 | 0 |
| f1040.line13a | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f1040.line15 | 685 | 0 | 255 | 60 | 0 | 0 | 0 |
| f1040.line16 | 323 | 507 | 92 | 77 | 1 | 0 | 0 |
| f1040.line19 | 464 | 60 | 0 | 476 | 0 | 0 | 0 |
| f1040.line27a | 637 | 143 | 0 | 220 | 0 | 0 | 0 |
| f1040.line28 | 483 | 41 | 0 | 476 | 0 | 0 | 0 |
| f1040.line6b | 974 | 0 | 26 | 0 | 0 | 0 | 0 |
| f1040.tax_before_credits | 310 | 483 | 88 | 119 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 898 | 0 | 0 | 102 | 0 | 0 | 0 |
| sa.deduction | 929 | 0 | 2 | 69 | 0 | 0 | 0 |
| sa.line17 | 928 | 0 | 3 | 69 | 0 | 0 | 0 |
| sa.standard | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US does not treat the generated 17-23-year-old full-time students as dependents of the unit (its dependency test needs inputs the project does not model) and pays no credit for other dependents for them; it does not count them as qualifying children for the earned income credit either (Tax-Calculator, given the count, agrees with the project on these returns)
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 983 | 0 | 17 | 0 | 0 | 0 | 0 |
| f1040.line13a | 823 | 0 | 0 | 177 | 0 | 0 | 0 |
| f1040.line15 | 646 | 0 | 11 | 343 | 0 | 0 | 0 |
| f1040.line16 | 269 | 366 | 38 | 327 | 0 | 0 | 0 |
| f1040.line19 | 395 | 71 | 0 | 534 | 0 | 0 | 0 |
| f1040.line20 | 670 | 3 | 0 | 327 | 0 | 0 | 0 |
| f1040.line24 | 273 | 273 | 20 | 434 | 0 | 0 | 0 |
| f1040.line27a | 810 | 190 | 0 | 0 | 0 | 0 | 0 |
| f1040.line28 | 418 | 48 | 0 | 534 | 0 | 0 | 0 |
| f1040.line6b | 985 | 0 | 15 | 0 | 0 | 0 | 0 |
| f1040.tax_before_credits | 246 | 347 | 50 | 357 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 937 | 0 | 0 | 63 | 0 | 0 | 0 |
| sa.deduction | 657 | 0 | 0 | 343 | 0 | 0 | 0 |
| sa.line17 | 939 | 0 | 1 | 60 | 0 | 0 | 0 |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator phases the child tax credit out by 5% of the exact excess of income over the threshold; Schedule 8812 line 10 rounds the excess up to the next multiple of $1,000 first
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass

## Explained differences

- PolicyEngine-US gen-00816 f1040.line16: project 5322947 engine 5322945 — Carried float32 error: PolicyEngine-US computes in float32, where one unit in the last place at this AGI ($255,108.89) is about 1.6 cents; its AGI (line 11b) and taxable income (line 15) are each 1 cent lower than the project's, within their own float bounds, and that cent moves its rate-schedule tax by 2 cents. Investigated 2026-10-18 when social security benefits entered the generated cases.

## Unexplained differences

None.
