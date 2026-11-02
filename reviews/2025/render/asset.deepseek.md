# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a68093ca3c6f6b3e431c81d51bf8877e253d972a5c369d9caa135de96b11bf7d |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 131072 |
| subject sha256 | 8bde0b7ebdf9b1be027a1d6024ba04d896ec78485f583d4db0c5680a6fc7bcbf |
| lines judged | 15 |
| match / mismatch / unclear / missing | 10 / 5 / 0 / 0 |
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
Status: **MISMATCH**

Restated: Input — The asset class of this property: find the property in Pub. 946 Appendix B, Table B-1, and the activity it is used in in Table B-2 (use the Table B-2 class when the property is specifically listed there under your activity); or choose A (personal property with no class life), B (qualified technological equipment), C (property used in research and experimentation), or qualified improvement property

Model: The IRS column (a) is 'Classification of property' and says to sort the property 'according to its classification (3-year property, 5-year property, etc.)'; the restatement instead asks for the Appendix B asset class or A/B/C/QIP.

Ruling: representation — the line is an intermediate in the project's basis computation. (a) the class input derives the form's 3/5/7-year classification through the Appendix B class; (b) the year plus the 2025 quarter gives the MACRS convention the form's month would give; (c) the pre-section-179 basis is shown under the column marker (c), and the form's column (c) after section 179 and the special allowance is item 19(c) (asset.col19c), which subtracts them. No printed tax amount differs. Lines 25 and 26(i) copy the per-asset allowance and elected cost, not the other lines' columns.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: This matches the column (d) instruction to determine the GDS recovery period from Pub. 946; using the asset class from column (a) is the prescribed way to find it.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: These are support gates that exclude cases the IRS text treats specially, such as ADS, real property, vehicles, basis adjustments, general asset accounts, amortization, and pre-2005 property; the refusal names the excluded cases.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this property in service in the business (2005 to 2025)

Model: The IRS column (b) calls for the 'Month and year placed in service' and line 19 is only for assets placed in service during 2025, while the restatement asks only for the year and permits 2005 through 2025.

Ruling: representation — the line is an intermediate in the project's basis computation. (a) the class input derives the form's 3/5/7-year classification through the Appendix B class; (b) the year plus the 2025 quarter gives the MACRS convention the form's month would give; (c) the pre-section-179 basis is shown under the column marker (c), and the form's column (c) after section 179 and the special allowance is item 19(c) (asset.col19c), which subtracts them. No printed tax amount differs. Lines 25 and 26(i) copy the per-asset allowance and elected cost, not the other lines' columns.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS line 19 column (c) says after multiplying cost by business use, 'subtract any credits and deductions allocable to the property' (including section 179 and the special allowance); the restatement stops after the multiplication.

Ruling: representation — the line is an intermediate in the project's basis computation. (a) the class input derives the form's 3/5/7-year classification through the Appendix B class; (b) the year plus the 2025 quarter gives the MACRS convention the form's month would give; (c) the pre-section-179 basis is shown under the column marker (c), and the form's column (c) after section 179 and the special allowance is item 19(c) (asset.col19c), which subtracts them. No printed tax amount differs. Lines 25 and 26(i) copy the per-asset allowance and elected cost, not the other lines' columns.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: This matches line 6 column (c), the elected section 179 cost, limited by the business-use cost and excluded from listed property by the reporting rule.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The IRS text requires a special-allowance election for a class to apply to all such property in that class placed in service during the tax year; the screen checks the same class-wide consistency.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The IRS text provides 100% for certain qualified property acquired after Jan. 19, 2025, 40% for certain property acquired after Sept. 27, 2017 and before Jan. 20, 2025 (with 60% exceptions screened out), and allows electing no allowance.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it does not say to enter the amount from line 14, and line 14 is not the listed-property allowance.

Ruling: representation — the line is an intermediate in the project's basis computation. (a) the class input derives the form's 3/5/7-year classification through the Appendix B class; (b) the year plus the 2025 quarter gives the MACRS convention the form's month would give; (c) the pre-section-179 basis is shown under the column marker (c), and the form's column (c) after section 179 and the special allowance is item 19(c) (asset.col19c), which subtracts them. No printed tax amount differs. Lines 25 and 26(i) copy the per-asset allowance and elected cost, not the other lines' columns.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: The IRS text says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the amount from line 6(c).

Ruling: representation — the line is an intermediate in the project's basis computation. (a) the class input derives the form's 3/5/7-year classification through the Appendix B class; (b) the year plus the 2025 quarter gives the MACRS convention the form's month would give; (c) the pre-section-179 basis is shown under the column marker (c), and the form's column (c) after section 179 and the special allowance is item 19(c) (asset.col19c), which subtracts them. No printed tax amount differs. Lines 25 and 26(i) copy the per-asset allowance and elected cost, not the other lines' columns.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The helper subtracts the section 179 election and the special allowance from the business-use basis, which is the computation described for line 19 column (c) within the screened cases.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The restatement uses the MACRS table rate under the half-year or mid-quarter convention selected by the 40%-of-bases test, matching line 19 column (g).

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The IRS column (e) requires HY or MQ (mid-month is outside this property screen), and the restatement asks for the convention including the mid-quarter quarter.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 is the current-year MACRS deduction for property placed in service before 2025; once the recovery period has ended, no current deduction remains for this nonvehicle property.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50% in qualified business use, line 26 column (h) is the MACRS depreciation for the current year, computed by the line 19(g) method; the helper combines the 2025 and prior-year cases with one zero.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MISMATCH
    reason: "The IRS column (a) is 'Classification of property' and says to sort the property 'according to its classification (3-year property, 5-year property, etc.)'; the restatement instead asks for the Appendix B asset class or A/B/C/QIP."
  - key: "(d)"
    status: MATCH
    reason: "This matches the column (d) instruction to determine the GDS recovery period from Pub. 946; using the asset class from column (a) is the prescribed way to find it."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "These are support gates that exclude cases the IRS text treats specially, such as ADS, real property, vehicles, basis adjustments, general asset accounts, amortization, and pre-2005 property; the refusal names the excluded cases."
  - key: "(b)"
    status: MISMATCH
    reason: "The IRS column (b) calls for the 'Month and year placed in service' and line 19 is only for assets placed in service during 2025, while the restatement asks only for the year and permits 2005 through 2025."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS line 19 column (c) says after multiplying cost by business use, 'subtract any credits and deductions allocable to the property' (including section 179 and the special allowance); the restatement stops after the multiplication."
  - key: "6(c)"
    status: MATCH
    reason: "This matches line 6 column (c), the elected section 179 cost, limited by the business-use cost and excluded from listed property by the reporting rule."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The IRS text requires a special-allowance election for a class to apply to all such property in that class placed in service during the tax year; the screen checks the same class-wide consistency."
  - key: "14"
    status: MATCH
    reason: "The IRS text provides 100% for certain qualified property acquired after Jan. 19, 2025, 40% for certain property acquired after Sept. 27, 2017 and before Jan. 20, 2025 (with 60% exceptions screened out), and allows electing no allowance."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; it does not say to enter the amount from line 14, and line 14 is not the listed-property allowance."
  - key: "26(i)"
    status: MISMATCH
    reason: "The IRS text says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26'; line 26(i) is not the amount from line 6(c)."
  - key: "19(c)"
    status: MATCH
    reason: "The helper subtracts the section 179 election and the special allowance from the business-use basis, which is the computation described for line 19 column (c) within the screened cases."
  - key: "19(g)"
    status: MATCH
    reason: "The restatement uses the MACRS table rate under the half-year or mid-quarter convention selected by the 40%-of-bases test, matching line 19 column (g)."
  - key: "(e)"
    status: MATCH
    reason: "The IRS column (e) requires HY or MQ (mid-month is outside this property screen), and the restatement asks for the convention including the mid-quarter quarter."
  - key: "17"
    status: MATCH
    reason: "Line 17 is the current-year MACRS deduction for property placed in service before 2025; once the recovery period has ended, no current deduction remains for this nonvehicle property."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50% in qualified business use, line 26 column (h) is the MACRS depreciation for the current year, computed by the line 19(g) method; the helper combines the 2025 and prior-year cases with one zero."
```
