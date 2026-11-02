# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 77833620d219cb4f9c568dea77631cb2db9c9ad543369a2bb01774ec062a0b2b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 2ac0576d88cb323f64f71c418327b6fe3b235d5641e72f5107aacd18c16aeea1 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 12 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: IRS line 19(a) classification is determined from Pub. 946 Appendix B Tables B-1/B-2 and the listed special categories; the restatement follows that approach.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: IRS line 19(d) directs determining the recovery period from the property classification; using the GDS recovery period for the selected asset class in Pub. 946 Appendix B is consistent.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screen lists conditions that place the property outside the supported MACRS-table computation, and the refusals for screened property name those exclusions.

### (b) — Year placed in service
Status: **MATCH**

Model: The year placed in service is the input needed to select line 17 versus line 19 and the recovery year; the mid-quarter quarter is captured separately.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: The computation multiplies cost by the business/investment-use percentage, matching the first step for basis; section 179 and the special allowance are applied in the later line 19(c) helper.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Line 6(c) is the elected section 179 cost, not more than the business cost, for property placed in service in 2025 that is not listed property.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The special allowance election must be consistent for the class of property placed in service in 2025; the screen tests that consistency.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Line 14 applies the applicable special allowance percentage, 100% or 40%, to the basis less the section 179 election, as described for qualified property.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; the restatement instead takes the line 14 amount, which is for non-listed property.

Ruling: representation; restatement accepted. Line 14 and line 19 amounts are figured per asset and shown by listed status (asset.on_19, asset.on_26_2025); for listed property the same per-asset allowance, election and depreciation appear on lines 25, 26(i) and 26(h), figured by the line 19 instructions as i4562 p. 15, Column (h) directs. The objection reads the shared helper names as the other lines' columns.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS line 6 says 'Do not include any listed property on line 6,' and line 26 column (i) is the elected section 179 cost for listed property; the restatement takes line 6(c).

Ruling: representation; restatement accepted. Line 14 and line 19 amounts are figured per asset and shown by listed status (asset.on_19, asset.on_26_2025); for listed property the same per-asset allowance, election and depreciation appear on lines 25, 26(i) and 26(h), figured by the line 19 instructions as i4562 p. 15, Column (h) directs. The objection reads the shared helper names as the other lines' columns.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The helper subtracts section 179 and the special allowance from the business basis, matching line 19(c).

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The restatement selects half-year or mid-quarter MACRS depreciation according to the mid-quarter test and applies the applicable rate to the line 19(c) basis.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention is half-year or mid-quarter; mid-month is not needed because real property is screened out.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 is the current-year MACRS deduction for property placed in service before 2025, with zero after the recovery period ends.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MISMATCH**

Restated: Add helper "MACRS on 2025 property" and helper "MACRS on property placed in service before 2025".

Model: IRS line 26(h) says for property used more than 50% in a qualified business use and placed in service after 1986, 'figure column (h) by following the instructions for line 19, column (g)'; the restatement adds line 19(g)/line 17 amounts, which are for non-listed property, instead of computing from the listed property's own basis after line 26(i) and line 25.

Ruling: representation; restatement accepted. Line 14 and line 19 amounts are figured per asset and shown by listed status (asset.on_19, asset.on_26_2025); for listed property the same per-asset allowance, election and depreciation appear on lines 25, 26(i) and 26(h), figured by the line 19 instructions as i4562 p. 15, Column (h) directs. The objection reads the shared helper names as the other lines' columns.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "IRS line 19(a) classification is determined from Pub. 946 Appendix B Tables B-1/B-2 and the listed special categories; the restatement follows that approach."
  - key: "(d)"
    status: MATCH
    reason: "IRS line 19(d) directs determining the recovery period from the property classification; using the GDS recovery period for the selected asset class in Pub. 946 Appendix B is consistent."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen lists conditions that place the property outside the supported MACRS-table computation, and the refusals for screened property name those exclusions."
  - key: "(b)"
    status: MATCH
    reason: "The year placed in service is the input needed to select line 17 versus line 19 and the recovery year; the mid-quarter quarter is captured separately."
  - key: "(c)"
    status: MATCH
    reason: "The computation multiplies cost by the business/investment-use percentage, matching the first step for basis; section 179 and the special allowance are applied in the later line 19(c) helper."
  - key: "6(c)"
    status: MATCH
    reason: "Line 6(c) is the elected section 179 cost, not more than the business cost, for property placed in service in 2025 that is not listed property."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The special allowance election must be consistent for the class of property placed in service in 2025; the screen tests that consistency."
  - key: "14"
    status: MATCH
    reason: "Line 14 applies the applicable special allowance percentage, 100% or 40%, to the basis less the section 179 election, as described for qualified property."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; the restatement instead takes the line 14 amount, which is for non-listed property."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS line 6 says 'Do not include any listed property on line 6,' and line 26 column (i) is the elected section 179 cost for listed property; the restatement takes line 6(c)."
  - key: "19(c)"
    status: MATCH
    reason: "The helper subtracts section 179 and the special allowance from the business basis, matching line 19(c)."
  - key: "19(g)"
    status: MATCH
    reason: "The restatement selects half-year or mid-quarter MACRS depreciation according to the mid-quarter test and applies the applicable rate to the line 19(c) basis."
  - key: "(e)"
    status: MATCH
    reason: "The convention is half-year or mid-quarter; mid-month is not needed because real property is screened out."
  - key: "17"
    status: MATCH
    reason: "Line 17 is the current-year MACRS deduction for property placed in service before 2025, with zero after the recovery period ends."
  - key: "26(h)"
    status: MISMATCH
    reason: "IRS line 26(h) says for property used more than 50% in a qualified business use and placed in service after 1986, 'figure column (h) by following the instructions for line 19, column (g)'; the restatement adds line 19(g)/line 17 amounts, which are for non-listed property, instead of computing from the listed property's own basis after line 26(i) and line 25."
```
