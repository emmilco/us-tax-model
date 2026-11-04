# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f9521b552cfa6ef40a43a98402e15129a4e7f8f41405e13401cf46c0d82e90f4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | af9f92a9efe22e1381eae6c0167cde7f1e2b8c4ec456685010780ad53d4b6763 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 12 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: The restatement follows Pub. 946 Appendix B Table B-1/B-2 ordering and the special classes A, B, C, and qualified improvement property used on Form 4562 line 19 column (a).

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Matches line 19 column (d): the GDS recovery period is found by asset class from Pub. 946 Appendix B Tables B-1 and B-2.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The restatement lists the screen conditions that narrow the tool, such as ADS, real property, vehicles, basis adjustments, and listed property used 50% or less; these are consistent with the IRS exclusions.

### (b) — Year placed in service
Status: **MATCH**

Model: Matches the placed-in-service year needed for the MACRS recovery year; the quarter is captured by column (e).

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS line 19 column (c) says to multiply cost by business/investment use and then 'From that result, subtract any credits and deductions allocable to the property,' including the section 179 expense deduction and any special depreciation allowance; the restatement stops after the multiplication.

Ruling: scope; this marker is the business basis before section 179 and the special allowance (its label); the reduced basis is 19(c). asset.screen refuses property whose basis "is reduced by a credit or deduction other than the section 179 deduction and the special depreciation allowance" (BUG-0373 wording), so on a computed return the only reductions are the two the project subtracts at 19(c).

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Matches line 6 column (c) elected section 179 cost and Pub. 946's section 179 property/zero rules, including the cash-plus-trade-in limit.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: Matches the requirement that a special allowance election apply consistently within a class; differing choices are refused.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Matches line 14's special allowance percentages and election-out zero.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it does not say to enter the line 14 amount, and line 14 is for non-listed property in this restatement.

Ruling: representation; restatement accepted. The per-asset allowance appears on line 25 for listed property and line 14 otherwise, figured by the same instructions (i4562 p. 14, "Enter on line 25 your total special depreciation allowance for all qualified listed property").

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the line 6(c) amount.

Ruling: representation; i4562 p. 5, Line 6, and p. 16, Column (i). asset.f26i copies asset.s179, the per-asset elected section 179 cost; the printed line 6(c) is the non-listed column, so "from line 6(c)" is loose wording. A listed property's elected cost is the amount the 26(i) column asks for.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Matches line 19 column (c) within the screen: the helper subtracts section 179 and the special allowance, and the screen excludes other basis reductions.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: Matches line 19 column (g): the depreciation deduction is the basis times the MACRS rate, using HY unless the mid-quarter 40% test is met.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: Matches line 19 column (e): HY or MQ, with the quarter needed for MQ.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Matches line 17: current-year MACRS for prior-year non-listed property, with zero once the recovery period ended before 2025.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: Matches line 26 column (h) for listed property used more than 50%; it adds current-year and prior-year MACRS, and the listed_low refusal excludes 50%-or-less property.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The restatement follows Pub. 946 Appendix B Table B-1/B-2 ordering and the special classes A, B, C, and qualified improvement property used on Form 4562 line 19 column (a)."
  - key: "(d)"
    status: MATCH
    reason: "Matches line 19 column (d): the GDS recovery period is found by asset class from Pub. 946 Appendix B Tables B-1 and B-2."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The restatement lists the screen conditions that narrow the tool, such as ADS, real property, vehicles, basis adjustments, and listed property used 50% or less; these are consistent with the IRS exclusions."
  - key: "(b)"
    status: MATCH
    reason: "Matches the placed-in-service year needed for the MACRS recovery year; the quarter is captured by column (e)."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS line 19 column (c) says to multiply cost by business/investment use and then 'From that result, subtract any credits and deductions allocable to the property,' including the section 179 expense deduction and any special depreciation allowance; the restatement stops after the multiplication."
  - key: "6(c)"
    status: MATCH
    reason: "Matches line 6 column (c) elected section 179 cost and Pub. 946's section 179 property/zero rules, including the cash-plus-trade-in limit."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "Matches the requirement that a special allowance election apply consistently within a class; differing choices are refused."
  - key: "14"
    status: MATCH
    reason: "Matches line 14's special allowance percentages and election-out zero."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it does not say to enter the line 14 amount, and line 14 is for non-listed property in this restatement."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the line 6(c) amount."
  - key: "19(c)"
    status: MATCH
    reason: "Matches line 19 column (c) within the screen: the helper subtracts section 179 and the special allowance, and the screen excludes other basis reductions."
  - key: "19(g)"
    status: MATCH
    reason: "Matches line 19 column (g): the depreciation deduction is the basis times the MACRS rate, using HY unless the mid-quarter 40% test is met."
  - key: "(e)"
    status: MATCH
    reason: "Matches line 19 column (e): HY or MQ, with the quarter needed for MQ."
  - key: "17"
    status: MATCH
    reason: "Matches line 17: current-year MACRS for prior-year non-listed property, with zero once the recovery period ended before 2025."
  - key: "26(h)"
    status: MATCH
    reason: "Matches line 26 column (h) for listed property used more than 50%; it adds current-year and prior-year MACRS, and the listed_low refusal excludes 50%-or-less property."
```
