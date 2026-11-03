# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 192db1ebd73980dcf0fdeda6b4821c4f704dbab08285328076be55ce8519bef5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | b86b5b69178ae0e506567c11a9a4be7ba4af4c47b4efa8b19542ad937b483117 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 12 / 3 / 0 / 0 |
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

Model: The classification is determined from Pub. 946 Appendix B and the line 19(a) classifications, including the A/B/C categories and qualified improvement property, consistent with the IRS instructions.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Column (d) recovery period is determined by the asset's classification/class life from Pub. 946 Appendix B, as the IRS instructions direct.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screen collects cases outside this tool's GDS non-vehicle MACRS computation, and the refusal names those exclusions; within the supported cases the line is consistent.

### (b) — Year placed in service
Status: **MATCH**

Model: The year placed in service is the relevant column (b) input; the program narrows to 2005–2025 and separately captures the quarter for the mid-quarter convention.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS column (c) says to multiply cost by business-use percentage and then 'subtract any credits and deductions allocable to the property', including 'Section 179 expense deduction' and 'any special depreciation allowance'; the restatement stops after multiplying by the business-use percentage.

Ruling: scope; asset.screen refuses property whose basis was adjusted for anything other than depreciation, so on a computed return the only reductions are section 179 and the special allowance, which the project subtracts at 19(c).

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The restatement tracks the section 179 property definition, elected cost limits, and exclusions for land, investment property, and certain leased property in the IRS text.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The IRS special allowance election is made for a class of property placed in service during the tax year; requiring the same choice across the recovery-period class is consistent.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The allowed percentages (100% for post-January 19, 2025 acquisitions and 40% for post-September 27, 2017/pre-January 20, 2025 acquisitions) match the IRS text for the supported cases; long-production/aircraft 60% cases are screened out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it is not the amount from line 14, which is the non-listed-property special allowance line.

Ruling: representation; restatement accepted. The per-asset allowance appears on line 25 for listed property and line 14 otherwise, figured by the same instructions.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; copying line 6(c) is therefore wrong.

Ruling: representation; restatement accepted. The per-asset section 179 election appears in column (i) for listed property and on line 6 otherwise.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: This uses the basis after section 179 and the special depreciation allowance, consistent with line 19 column (c) instructions.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The deduction is column (c) basis times the MACRS rate, with the mid-quarter test based on fourth-quarter bases exceeding 40% of total 2025 bases, as the IRS instructions provide.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The supported conventions are half-year and mid-quarter for non-real property; mid-month is correctly outside this tool's scope.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: For prior-year MACRS property not listed, the current-year deduction is computed unless the recovery period ended before 2025, in which case it is zero.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: Line 26(h) is the MACRS depreciation for listed property used more than 50%; the IRS directs figuring it by following line 19(g), so summing the current-year and prior-year MACRS amounts is consistent.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The classification is determined from Pub. 946 Appendix B and the line 19(a) classifications, including the A/B/C categories and qualified improvement property, consistent with the IRS instructions."
  - key: "(d)"
    status: MATCH
    reason: "Column (d) recovery period is determined by the asset's classification/class life from Pub. 946 Appendix B, as the IRS instructions direct."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen collects cases outside this tool's GDS non-vehicle MACRS computation, and the refusal names those exclusions; within the supported cases the line is consistent."
  - key: "(b)"
    status: MATCH
    reason: "The year placed in service is the relevant column (b) input; the program narrows to 2005–2025 and separately captures the quarter for the mid-quarter convention."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS column (c) says to multiply cost by business-use percentage and then 'subtract any credits and deductions allocable to the property', including 'Section 179 expense deduction' and 'any special depreciation allowance'; the restatement stops after multiplying by the business-use percentage."
  - key: "6(c)"
    status: MATCH
    reason: "The restatement tracks the section 179 property definition, elected cost limits, and exclusions for land, investment property, and certain leased property in the IRS text."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The IRS special allowance election is made for a class of property placed in service during the tax year; requiring the same choice across the recovery-period class is consistent."
  - key: "14"
    status: MATCH
    reason: "The allowed percentages (100% for post-January 19, 2025 acquisitions and 40% for post-September 27, 2017/pre-January 20, 2025 acquisitions) match the IRS text for the supported cases; long-production/aircraft 60% cases are screened out."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it is not the amount from line 14, which is the non-listed-property special allowance line."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS line 6 says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; copying line 6(c) is therefore wrong."
  - key: "19(c)"
    status: MATCH
    reason: "This uses the basis after section 179 and the special depreciation allowance, consistent with line 19 column (c) instructions."
  - key: "19(g)"
    status: MATCH
    reason: "The deduction is column (c) basis times the MACRS rate, with the mid-quarter test based on fourth-quarter bases exceeding 40% of total 2025 bases, as the IRS instructions provide."
  - key: "(e)"
    status: MATCH
    reason: "The supported conventions are half-year and mid-quarter for non-real property; mid-month is correctly outside this tool's scope."
  - key: "17"
    status: MATCH
    reason: "For prior-year MACRS property not listed, the current-year deduction is computed unless the recovery period ended before 2025, in which case it is zero."
  - key: "26(h)"
    status: MATCH
    reason: "Line 26(h) is the MACRS depreciation for listed property used more than 50%; the IRS directs figuring it by following line 19(g), so summing the current-year and prior-year MACRS amounts is consistent."
```
