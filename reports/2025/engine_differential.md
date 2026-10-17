# Engine differential — generated returns vs independent engines

Cases: 1000 generated single-filer returns (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 806 | 0 | 194 | 0 | 0 | 0 | 0 |
| f1040.line13a | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f1040.line15 | 724 | 0 | 215 | 61 | 0 | 0 | 0 |
| f1040.line16 | 277 | 571 | 79 | 73 | 0 | 0 | 0 |
| f1040.line19 | 475 | 54 | 0 | 471 | 0 | 0 | 0 |
| f1040.line28 | 496 | 33 | 0 | 471 | 0 | 0 | 0 |
| f1040.tax_before_credits | 256 | 559 | 84 | 101 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 910 | 0 | 1 | 89 | 0 | 0 | 0 |
| sa.deduction | 928 | 0 | 4 | 68 | 0 | 0 | 0 |
| sa.line17 | 926 | 0 | 6 | 68 | 0 | 0 | 0 |
| sa.standard | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US does not treat the generated 17-23-year-old full-time students as dependents of the unit (its dependency test needs inputs the project does not model) and pays no credit for other dependents for them
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f1040.line13a | 837 | 0 | 0 | 163 | 0 | 0 | 0 |
| f1040.line15 | 675 | 0 | 0 | 325 | 0 | 0 | 0 |
| f1040.line16 | 243 | 406 | 34 | 317 | 0 | 0 | 0 |
| f1040.line19 | 425 | 79 | 0 | 496 | 0 | 0 | 0 |
| f1040.line20 | 680 | 3 | 0 | 317 | 0 | 0 | 0 |
| f1040.line24 | 262 | 319 | 19 | 400 | 0 | 0 | 0 |
| f1040.line28 | 462 | 41 | 1 | 496 | 0 | 0 | 0 |
| f1040.tax_before_credits | 222 | 401 | 46 | 331 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 947 | 0 | 1 | 52 | 0 | 0 | 0 |
| sa.deduction | 675 | 0 | 0 | 325 | 0 | 0 | 0 |
| sa.line17 | 938 | 0 | 1 | 61 | 0 | 0 | 0 |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator phases the child tax credit out by 5% of the exact excess of income over the threshold; Schedule 8812 line 10 rounds the excess up to the next multiple of $1,000 first
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass

## Unexplained differences

None.
