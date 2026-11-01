# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 0d6acd42866d2ff044415426c352ba5f890cb99b812e2787a925380570b40a0a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 4d1235b5b9ff5f6cfc82c7026f6b53a277116a95b32c3330be03b0b244e9de48 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 11 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: The asset-class lookup follows Pub. 946 Appendix B Tables B-1 and B-2, with the stated special classes, within the form's scope.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The GDS recovery period is taken from Pub. 946 Appendix B by asset class, as required for line 19 column (d).

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screen excludes the listed out-of-scope cases, and the refusal names the excluded property.

### (b) — Year placed in service
Status: **MATCH**

Model: The placed-in-service year is used for the convention and recovery-year determinations, consistent with line 19 column (b).

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: The business/investment-use cost is cost times the business-use percentage, with the percentage capped and the listed-property low-use case refused.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The elected section 179 cost is limited to the business cost and not allowed for listed property on line 6, as the IRS requires.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The IRS requires the special allowance election to be consistent for the class of property placed in service during the year.

### 14 — Special depreciation allowance for this property
Status: **MISMATCH**

Restated: Choose — [helper "Special depreciation allowance for this class of property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%"] [helper "Special depreciation allowance for this class of property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for this class of property" = 'none' → helper "Zero"]

Model: The IRS also provides a 50% allowance for qualified reuse and recycling property and limits the 40% rate to property acquired after September 27, 2017; the restatement applies 40% to any property not acquired after January 19, 2025.

Ruling: finding — i4562 pp. 5–7, Line 14. The 40% rate applies to property acquired after September 27, 2017 and before January 20, 2025; qualified reuse and recycling property placed in service after August 31, 2008 is eligible for 50%. The restatement's "otherwise 40%" applies 40% to any property not acquired after January 19, 2025, and the bonus-choice question has no 50% branch. A pre-September-27-2017 asset can be given 40% and a reuse/recycling asset cannot be given 50%. BUG-0291; fix the screen and add the branches with the asset pass (T-158).

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it is not the line 14 amount, which the restatement reports only for property other than listed property.

Ruling: representation — i4562 p. 13, Line 25. asset.f25 copies asset.bonus, the per-asset special allowance; the printed line 14 is the non-listed-property line, so "from line 14" is loose wording, not the value. The line is shown only for listed property placed in service in 2025, and the Schedule C totals read the per-asset amount filtered by asset.listed.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the line 6(c) amount.

Ruling: representation — i4562 p. 5, Line 6, and p. 16, Column (i). asset.f26i copies asset.s179, the per-asset elected section 179 cost; the printed line 6(c) is the non-listed-property column, so "from line 6(c)" is loose wording. A listed property's elected cost is the amount the 26(i) column asks for.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MISMATCH**

Restated: Enter the amount from helper "Basis for MACRS depreciation (after section 179 and the special allowance)".

Model: IRS line 19(c) says to subtract 'any credits and deductions allocable to the property'; the restatement subtracts only section 179 and the special allowance.

Ruling: scope — asset.screen refuses an asset whose basis was adjusted for anything other than depreciation (i4562 pp. 11–12), which covers the credits and deductions allocable to the property that column (c) subtracts. The MACRS basis subtracts section 179 and the special allowance, the two adjustments in this slice.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The MACRS deduction uses the applicable half-year or mid-quarter rate on the MACRS basis, consistent with line 19 column (g).

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention is half-year or mid-quarter with the quarter placed in service, consistent with line 19 column (e) for non-real property.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Prior-year MACRS property gets the 2025 MACRS deduction unless the recovery period ended before 2025, in which case it is zero for non-vehicle property.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: The listed-property depreciation is the MACRS amount for the 2025 property plus any prior-year MACRS, following line 19 column (g).

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The asset-class lookup follows Pub. 946 Appendix B Tables B-1 and B-2, with the stated special classes, within the form's scope."
  - key: "(d)"
    status: MATCH
    reason: "The GDS recovery period is taken from Pub. 946 Appendix B by asset class, as required for line 19 column (d)."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen excludes the listed out-of-scope cases, and the refusal names the excluded property."
  - key: "(b)"
    status: MATCH
    reason: "The placed-in-service year is used for the convention and recovery-year determinations, consistent with line 19 column (b)."
  - key: "(c)"
    status: MATCH
    reason: "The business/investment-use cost is cost times the business-use percentage, with the percentage capped and the listed-property low-use case refused."
  - key: "6(c)"
    status: MATCH
    reason: "The elected section 179 cost is limited to the business cost and not allowed for listed property on line 6, as the IRS requires."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The IRS requires the special allowance election to be consistent for the class of property placed in service during the year."
  - key: "14"
    status: MISMATCH
    reason: "The IRS also provides a 50% allowance for qualified reuse and recycling property and limits the 40% rate to property acquired after September 27, 2017; the restatement applies 40% to any property not acquired after January 19, 2025."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it is not the line 14 amount, which the restatement reports only for property other than listed property."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the line 6(c) amount."
  - key: "19(c)"
    status: MISMATCH
    reason: "IRS line 19(c) says to subtract 'any credits and deductions allocable to the property'; the restatement subtracts only section 179 and the special allowance."
  - key: "19(g)"
    status: MATCH
    reason: "The MACRS deduction uses the applicable half-year or mid-quarter rate on the MACRS basis, consistent with line 19 column (g)."
  - key: "(e)"
    status: MATCH
    reason: "The convention is half-year or mid-quarter with the quarter placed in service, consistent with line 19 column (e) for non-real property."
  - key: "17"
    status: MATCH
    reason: "Prior-year MACRS property gets the 2025 MACRS deduction unless the recovery period ended before 2025, in which case it is zero for non-vehicle property."
  - key: "26(h)"
    status: MATCH
    reason: "The listed-property depreciation is the MACRS amount for the 2025 property plus any prior-year MACRS, following line 19 column (g)."
```
