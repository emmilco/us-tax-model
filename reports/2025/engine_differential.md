# Engine differential — generated returns vs independent engines

Cases: 1000 generated single-filer returns (tools/engines/generate_cases.py). Engines run locally under .engines/venv (tools/engines/setup.sh); versions: PolicyEngine-US 2.49.4, Tax-Calculator 6.8.5.

`table-adjusted` means the engine equals the project's tax lines recomputed with every Tax Table lookup replaced by the rate schedule (engines compute from the schedule where the form prescribes the table), keeping the worksheet path and re-taking its smaller-of; an identified cause, not a tolerance. `float` means the difference is within two units in the last place of the engine's floating-point representation (PolicyEngine-US computes in float32, Tax-Calculator in float64), a bound derived from the engine's precision. `excluded` lines carry the engine limitation stated below. Every other difference must be explained in fixtures/2025/differential/engine_investigations.json or the run fails.

## PolicyEngine-US

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 795 | 0 | 205 | 0 | 0 | 0 | 0 |
| f1040.line13a | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f1040.line15 | 720 | 0 | 222 | 58 | 0 | 0 | 0 |
| f1040.line16 | 293 | 546 | 82 | 79 | 0 | 0 | 0 |
| f1040.tax_before_credits | 272 | 524 | 87 | 117 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 903 | 0 | 1 | 96 | 0 | 0 | 0 |
| sa.deduction | 932 | 0 | 8 | 60 | 0 | 0 | 0 |
| sa.line17 | 931 | 0 | 9 | 60 | 0 | 0 | 0 |
| sa.standard | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |

Exclusions:

- PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit
- PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap
- PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does

## Tax-Calculator

| line | exact | table-adjusted | float | excluded | explained | UNEXPLAINED | not computed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f1040.line11b | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f1040.line13a | 833 | 0 | 0 | 167 | 0 | 0 | 0 |
| f1040.line15 | 679 | 0 | 2 | 319 | 0 | 0 | 0 |
| f1040.line16 | 257 | 399 | 28 | 316 | 0 | 0 | 0 |
| f1040.line20 | 682 | 2 | 0 | 316 | 0 | 0 | 0 |
| f1040.line24 | 237 | 381 | 35 | 347 | 0 | 0 | 0 |
| f1040.tax_before_credits | 235 | 383 | 35 | 347 | 0 | 0 | 0 |
| f8959.tax | 1000 | 0 | 0 | 0 | 0 | 0 | 0 |
| f8960.tax | 941 | 0 | 0 | 59 | 0 | 0 | 0 |
| sa.deduction | 680 | 0 | 1 | 319 | 0 | 0 | 0 |
| sa.line17 | 939 | 0 | 3 | 58 | 0 | 0 | 0 |

Exclusions:

- Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit
- Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a
- Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero
- Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)
- Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass

## Unexplained differences

None.
