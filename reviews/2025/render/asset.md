# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a68093ca3c6f6b3e431c81d51bf8877e253d972a5c369d9caa135de96b11bf7d |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 8bde0b7ebdf9b1be027a1d6024ba04d896ec78485f583d4db0c5680a6fc7bcbf |
| lines judged | 15 |
| match / mismatch / unclear / missing | 15 / 0 / 0 / 0 |
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

Model: This follows Pub. 946 Appendix B: check Table B-1, then Table B-2, and use the Table B-2 class when the property is specifically listed under the activity. Property in neither table goes to 'Certain Property for Which Recovery Periods Assigned' (A, B, C), and the i4562 lists qualified improvement property as 15-year property.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The GDS recovery period is read from the GDS (MACRS) column of Tables B-1/B-2 for the asset class, as Appendix B directs. i4562 line 19(d) gives the same periods by classification.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is an input screen that narrows the tool to cases the text supports. Excluded property (dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments per Pub. 946 table rule 4, general asset accounts, reuse and recycling property, and so on) is refused, not miscomputed.

### (b) — Year placed in service
Status: **MATCH**

Model: The year placed in service is an input, consistent with i4562 column (b) and Pub. 946's rules for determining the year of recovery.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: i4562 line 19(c) says 'multiply the cost or other basis of the property by the percentage of business/investment use'; this computes that product before the later subtractions. Listed property used 50% or less is refused, which matches the line 26/27 split.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Line 6 column (c): 'Enter the amount you elect to expense.' It is limited to non-listed 2025 property ('Do not include any listed property on line 6'), and the refusal enforces the 'used predominantly (more than 50%)' condition and the business-cost limit.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year'. Mixed elections within a class are refused.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The allowance is basis after the section 179 deduction times 100% (acquired after Jan 19, 2025), 40% (acquired Sept 28, 2017–Jan 19, 2025, or the elected 40%), or zero if elected out. This matches 'multiplying the depreciable basis of the property by the applicable percentage', with depreciable basis reduced by the section 179 deduction.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 is the special allowance for qualified listed property figured as under line 14 ('See the instructions for line 14 for ... how to figure the deduction'). The line 14 computation is reused for listed property placed in service in 2025.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: Line 6 instructions: 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The same election input is reported here for listed property; the passenger automobile limits do not arise because vehicles are entered separately.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Line 19(c) is business cost less the section 179 deduction and 'Any special depreciation allowance included on line 14', which is exactly the helper used.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: Mid-quarter applies when fourth-quarter bases exceed 40% of the year's bases (5×Q4 > 2×total). The test uses bases after section 179 and before the special allowance, per Pub. 946's caution, and includes vehicle bases. The deduction is column (c) times the year-1 rate from the GDS percentage tables for the convention and quarter.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention used in the year placed in service (half-year or mid-quarter with quarter) is an input, consistent with i4562 column (e) and Pub. 946's rule to keep using the same tables for the whole recovery period.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: For MACRS property placed in service before 2025, the deduction is unadjusted basis (business cost less prior section 179 and prior special allowance, per Pub. 946 'Figuring the Unadjusted Basis') times the table rate for the 2025 year of recovery and the original convention. It is zero after the recovery period ends.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g)'. That is the line 19(g) computation for 2025 property or the line 17 computation for earlier property. Pub. 946 allows no deduction after the recovery period for listed property other than passenger automobiles.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "This follows Pub. 946 Appendix B: check Table B-1, then Table B-2, and use the Table B-2 class when the property is specifically listed under the activity. Property in neither table goes to 'Certain Property for Which Recovery Periods Assigned' (A, B, C), and the i4562 lists qualified improvement property as 15-year property."
  - key: "(d)"
    status: MATCH
    reason: "The GDS recovery period is read from the GDS (MACRS) column of Tables B-1/B-2 for the asset class, as Appendix B directs. i4562 line 19(d) gives the same periods by classification."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is an input screen that narrows the tool to cases the text supports. Excluded property (dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments per Pub. 946 table rule 4, general asset accounts, reuse and recycling property, and so on) is refused, not miscomputed."
  - key: "(b)"
    status: MATCH
    reason: "The year placed in service is an input, consistent with i4562 column (b) and Pub. 946's rules for determining the year of recovery."
  - key: "(c)"
    status: MATCH
    reason: "i4562 line 19(c) says 'multiply the cost or other basis of the property by the percentage of business/investment use'; this computes that product before the later subtractions. Listed property used 50% or less is refused, which matches the line 26/27 split."
  - key: "6(c)"
    status: MATCH
    reason: "Line 6 column (c): 'Enter the amount you elect to expense.' It is limited to non-listed 2025 property ('Do not include any listed property on line 6'), and the refusal enforces the 'used predominantly (more than 50%)' condition and the business-cost limit."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year'. Mixed elections within a class are refused."
  - key: "14"
    status: MATCH
    reason: "The allowance is basis after the section 179 deduction times 100% (acquired after Jan 19, 2025), 40% (acquired Sept 28, 2017–Jan 19, 2025, or the elected 40%), or zero if elected out. This matches 'multiplying the depreciable basis of the property by the applicable percentage', with depreciable basis reduced by the section 179 deduction."
  - key: "25"
    status: MATCH
    reason: "Line 25 is the special allowance for qualified listed property figured as under line 14 ('See the instructions for line 14 for ... how to figure the deduction'). The line 14 computation is reused for listed property placed in service in 2025."
  - key: "26(i)"
    status: MATCH
    reason: "Line 6 instructions: 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The same election input is reported here for listed property; the passenger automobile limits do not arise because vehicles are entered separately."
  - key: "19(c)"
    status: MATCH
    reason: "Line 19(c) is business cost less the section 179 deduction and 'Any special depreciation allowance included on line 14', which is exactly the helper used."
  - key: "19(g)"
    status: MATCH
    reason: "Mid-quarter applies when fourth-quarter bases exceed 40% of the year's bases (5×Q4 > 2×total). The test uses bases after section 179 and before the special allowance, per Pub. 946's caution, and includes vehicle bases. The deduction is column (c) times the year-1 rate from the GDS percentage tables for the convention and quarter."
  - key: "(e)"
    status: MATCH
    reason: "The convention used in the year placed in service (half-year or mid-quarter with quarter) is an input, consistent with i4562 column (e) and Pub. 946's rule to keep using the same tables for the whole recovery period."
  - key: "17"
    status: MATCH
    reason: "For MACRS property placed in service before 2025, the deduction is unadjusted basis (business cost less prior section 179 and prior special allowance, per Pub. 946 'Figuring the Unadjusted Basis') times the table rate for the 2025 year of recovery and the original convention. It is zero after the recovery period ends."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g)'. That is the line 19(g) computation for 2025 property or the line 17 computation for earlier property. Pub. 946 allows no deduction after the recovery period for listed property other than passenger automobiles."
```
```
