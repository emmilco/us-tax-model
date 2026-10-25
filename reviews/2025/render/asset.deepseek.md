# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | eed7a7ec179ec1dddb769dad604527e7a3d70e68ab153181cc336e17f2cef0fa |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 3f317e7cda60bc1ed6b72c1ac9c73ed519d44429278e796df75d70b610f58e63 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 11 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MISMATCH**

Restated: Input — The asset class of this property: find the property in Pub. 946 Appendix B, Table B-1, and the activity it is used in in Table B-2 (use the Table B-2 class when the property is specifically listed there under your activity); or choose A (personal property with no class life), B (qualified technological equipment), C (property used in research and experimentation), or qualified improvement property

Model: Column (a) asks for the classification, such as 3-year property, 5-year property, etc.; the restatement instead directs use of Pub. 946 Appendix B asset classes/class-life tables.

Ruling: open

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: For property not listed on the form, the Pub. 946 Appendix B asset class and activity tables supply the GDS recovery period required for column (d).

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screen lists property types and situations outside this one-item, non-vehicle, MACRS-table tool, and the cost refusal names those exclusions.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this property in service in the business (2005 to 2025)

Model: Column (b) is month and year placed in service; the restatement captures only the year and limits it to 2005-2025.

Ruling: open

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special 
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: Column (c) requires subtracting allocable credits and deductions, including section 179 and the special allowance, after multiplying; the restatement stops at the multiplication.

Ruling: open

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Line 6(c) is the elected section 179 cost for current-year property, with listed property excluded from line 6; the input and reporting rule match.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The IRS permits the special-allowance election out by class for all property in the class; the same-class gate and mixed-election refusal name the narrowing.

### 14 — Special depreciation allowance for this property
Status: **MISMATCH**

Restated: Choose — [helper "Special depreciation allowance for this class of property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%"] [helper "Special depreciation allowance for this class of property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for this class of property" = 'none' → helper "Zero"]

Model: The IRS line also provides a 50% special allowance for qualified reuse and recycling property; the full/forty/none choices do not cover it and no refusal names it.

Ruling: open

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: For qualified listed property, line 25 is the special allowance figured under the line 14 rules; taking the line 14 computed allowance gives that amount within the supported listed-property cases.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: Line 26(i) is the elected section 179 cost for listed property; the same elected-cost input is used, and line 6 reporting is suppressed for listed property.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The helper reduces the business-use basis by section 179 and the special allowance as column (c) instructs; other credits and basis adjustments are screened out.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The line uses the MACRS half-year or mid-quarter rate on the column (c) basis, with mid-quarter triggered by the Q4-over-40% test.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: For non-real property, the convention is half-year or mid-quarter with the placed quarter; the screen excludes mid-month real property and other methods.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 is current-year MACRS for property placed before 2025, and becomes zero when the recovery period ended before 2025; vehicles are excluded.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, column (h) follows the line 19(g) or line 17 MACRS computation; low-use and vehicle cases are refused or excluded.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MISMATCH
    reason: "Column (a) asks for the classification, such as 3-year property, 5-year property, etc.; the restatement instead directs use of Pub. 946 Appendix B asset classes/class-life tables."
  - key: "(d)"
    status: MATCH
    reason: "For property not listed on the form, the Pub. 946 Appendix B asset class and activity tables supply the GDS recovery period required for column (d)."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen lists property types and situations outside this one-item, non-vehicle, MACRS-table tool, and the cost refusal names those exclusions."
  - key: "(b)"
    status: MISMATCH
    reason: "Column (b) is month and year placed in service; the restatement captures only the year and limits it to 2005-2025."
  - key: "(c)"
    status: MISMATCH
    reason: "Column (c) requires subtracting allocable credits and deductions, including section 179 and the special allowance, after multiplying; the restatement stops at the multiplication."
  - key: "6(c)"
    status: MATCH
    reason: "Line 6(c) is the elected section 179 cost for current-year property, with listed property excluded from line 6; the input and reporting rule match."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The IRS permits the special-allowance election out by class for all property in the class; the same-class gate and mixed-election refusal name the narrowing."
  - key: "14"
    status: MISMATCH
    reason: "The IRS line also provides a 50% special allowance for qualified reuse and recycling property; the full/forty/none choices do not cover it and no refusal names it."
  - key: "25"
    status: MATCH
    reason: "For qualified listed property, line 25 is the special allowance figured under the line 14 rules; taking the line 14 computed allowance gives that amount within the supported listed-property cases."
  - key: "26(i)"
    status: MATCH
    reason: "Line 26(i) is the elected section 179 cost for listed property; the same elected-cost input is used, and line 6 reporting is suppressed for listed property."
  - key: "19(c)"
    status: MATCH
    reason: "The helper reduces the business-use basis by section 179 and the special allowance as column (c) instructs; other credits and basis adjustments are screened out."
  - key: "19(g)"
    status: MATCH
    reason: "The line uses the MACRS half-year or mid-quarter rate on the column (c) basis, with mid-quarter triggered by the Q4-over-40% test."
  - key: "(e)"
    status: MATCH
    reason: "For non-real property, the convention is half-year or mid-quarter with the placed quarter; the screen excludes mid-month real property and other methods."
  - key: "17"
    status: MATCH
    reason: "Line 17 is current-year MACRS for property placed before 2025, and becomes zero when the recovery period ended before 2025; vehicles are excluded."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, column (h) follows the line 19(g) or line 17 MACRS computation; low-use and vehicle cases are refused or excluded."
```
