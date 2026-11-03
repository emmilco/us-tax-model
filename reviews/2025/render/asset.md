# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d4a7aa92ad1f56d3b522f5f5478e21c59c30c4601628c2f19f764493b9e34db0 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | aca9afbf03c111e08e13f231c7b354cd49b268c2363d4a81476f384026f7ff99 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 15 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: Pub. 946 Appendix B says to check Table B-1, then use the Table B-2 recovery period if the property is specifically listed under its activity. It lists classes A (personal property with no class life), B (qualified technological equipment) and C (research and experimentation property), and the instructions classify qualified improvement property as 15-year property.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The GDS (MACRS) recovery period column of Tables B-1 and B-2, keyed by asset class, is the recovery period that column (d) asks for. It agrees with the classification table in the line 19(d) instructions.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screened cases are excluded from the tool rather than computed wrongly, and the refusal on cost or other basis names them. The listed-property test follows the qualified business use exclusions in the line 26/27 instructions: investment use, leasing to or compensation of a 5% owner or related person, compensation of others not included in income, and use nondeductible under section 274.

### (b) — Year placed in service
Status: **MATCH**

Model: This input records the year the property was placed in service. Property placed in service before 2005 is screened out, so the range of 2005 to 2025 is consistent.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: It multiplies cost or other basis by the business use percentage, capped at 100%. This is the business/investment portion of cost that the line 19(c) instructions start from: 'multiply the cost or other basis of the property by the percentage of business/investment use.' Section 179 and the special allowance are subtracted later. Listed property at 50% or less is refused, consistent with line 27 using ADS.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The section 179 property definition, the land and land-improvement exclusions, the noncorporate lessor tests and the cash-only rule for trade-ins all follow i4562 and Pub. 946. Listed property is kept off line 6 as instructed ('Do not include any listed property on line 6').

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The instructions treat the election out as made 'for any class of property ... for all such property in such class placed in service during the tax year.' Asking whether the choice is uniform within the class, and refusing when it is not, is consistent with that.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The allowance is 100% for property acquired after January 19, 2025 unless the 40% election is made, 40% for property acquired after September 27, 2017 and before January 20, 2025, and zero on election out. It is applied to the depreciable basis after the section 179 deduction, per 'subtract from the business/investment portion of the cost ... Section 179 expense deduction.'

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: The line 25 instructions say to figure the special allowance for qualified listed property using the line 14 rules ('See the instructions for line 14 for the definition of qualified property and how to figure the deduction'). Only listed property used more than 50% reaches this line.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: The instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' Column (i) is for property used more than 50% in a qualified business use, which the refusal enforces.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: This is the business portion of cost less the section 179 deduction and less 'Any special depreciation allowance included on line 14', as the line 19 column (c) instructions direct.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The mid-quarter test (fourth-quarter bases more than 40% of the year's bases) uses bases after section 179 and before the special allowance, per the Pub. 946 caution. Column (c) is multiplied by the matching table rate (Table A-1 for half-year, Tables A-2 to A-5 for mid-quarter by quarter), as the column (g) instructions direct.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: This input records the convention (half-year, or mid-quarter with its quarter) fixed in the year the property was placed in service. That is the column (e) convention used with the percentage tables in later years.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 tells the filer to figure the deduction under the line 19(g) instructions. Pub. 946 says to apply the table rate to unadjusted basis, reduced by 'Any section 179 deduction claimed' and 'Any special depreciation allowance taken.' Zero after the recovery period agrees with 'You cannot claim a depreciation deduction for listed property other than passenger automobiles after the recovery period ends' and with the table rows ending.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50% and placed in service after 1986, column (h) is figured 'by following the instructions for line 19, column (g).' The helpers use the 19(g) computation for 2025 property and the line 17 computation for earlier property, and vehicles (with their passenger automobile limits) are handled separately.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Pub. 946 Appendix B says to check Table B-1, then use the Table B-2 recovery period if the property is specifically listed under its activity. It lists classes A (personal property with no class life), B (qualified technological equipment) and C (research and experimentation property), and the instructions classify qualified improvement property as 15-year property."
  - key: "(d)"
    status: MATCH
    reason: "The GDS (MACRS) recovery period column of Tables B-1 and B-2, keyed by asset class, is the recovery period that column (d) asks for. It agrees with the classification table in the line 19(d) instructions."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screened cases are excluded from the tool rather than computed wrongly, and the refusal on cost or other basis names them. The listed-property test follows the qualified business use exclusions in the line 26/27 instructions: investment use, leasing to or compensation of a 5% owner or related person, compensation of others not included in income, and use nondeductible under section 274."
  - key: "(b)"
    status: MATCH
    reason: "This input records the year the property was placed in service. Property placed in service before 2005 is screened out, so the range of 2005 to 2025 is consistent."
  - key: "(c)"
    status: MATCH
    reason: "It multiplies cost or other basis by the business use percentage, capped at 100%. This is the business/investment portion of cost that the line 19(c) instructions start from: 'multiply the cost or other basis of the property by the percentage of business/investment use.' Section 179 and the special allowance are subtracted later. Listed property at 50% or less is refused, consistent with line 27 using ADS."
  - key: "6(c)"
    status: MATCH
    reason: "The section 179 property definition, the land and land-improvement exclusions, the noncorporate lessor tests and the cash-only rule for trade-ins all follow i4562 and Pub. 946. Listed property is kept off line 6 as instructed ('Do not include any listed property on line 6')."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The instructions treat the election out as made 'for any class of property ... for all such property in such class placed in service during the tax year.' Asking whether the choice is uniform within the class, and refusing when it is not, is consistent with that."
  - key: "14"
    status: MATCH
    reason: "The allowance is 100% for property acquired after January 19, 2025 unless the 40% election is made, 40% for property acquired after September 27, 2017 and before January 20, 2025, and zero on election out. It is applied to the depreciable basis after the section 179 deduction, per 'subtract from the business/investment portion of the cost ... Section 179 expense deduction.'"
  - key: "25"
    status: MATCH
    reason: "The line 25 instructions say to figure the special allowance for qualified listed property using the line 14 rules ('See the instructions for line 14 for the definition of qualified property and how to figure the deduction'). Only listed property used more than 50% reaches this line."
  - key: "26(i)"
    status: MATCH
    reason: "The instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' Column (i) is for property used more than 50% in a qualified business use, which the refusal enforces."
  - key: "19(c)"
    status: MATCH
    reason: "This is the business portion of cost less the section 179 deduction and less 'Any special depreciation allowance included on line 14', as the line 19 column (c) instructions direct."
  - key: "19(g)"
    status: MATCH
    reason: "The mid-quarter test (fourth-quarter bases more than 40% of the year's bases) uses bases after section 179 and before the special allowance, per the Pub. 946 caution. Column (c) is multiplied by the matching table rate (Table A-1 for half-year, Tables A-2 to A-5 for mid-quarter by quarter), as the column (g) instructions direct."
  - key: "(e)"
    status: MATCH
    reason: "This input records the convention (half-year, or mid-quarter with its quarter) fixed in the year the property was placed in service. That is the column (e) convention used with the percentage tables in later years."
  - key: "17"
    status: MATCH
    reason: "Line 17 tells the filer to figure the deduction under the line 19(g) instructions. Pub. 946 says to apply the table rate to unadjusted basis, reduced by 'Any section 179 deduction claimed' and 'Any special depreciation allowance taken.' Zero after the recovery period agrees with 'You cannot claim a depreciation deduction for listed property other than passenger automobiles after the recovery period ends' and with the table rows ending."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50% and placed in service after 1986, column (h) is figured 'by following the instructions for line 19, column (g).' The helpers use the 19(g) computation for 2025 property and the line 17 computation for earlier property, and vehicles (with their passenger automobile limits) are handled separately."
```
```
