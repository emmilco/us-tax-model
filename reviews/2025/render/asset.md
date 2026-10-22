# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5485b050048e723c6c66fd40fb055c6103d3bbd4a447c994e23a5c2d6204260f |
| subject sha256 | 3f317e7cda60bc1ed6b72c1ac9c73ed519d44429278e796df75d70b610f58e63 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 15 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: Follows Pub. 946 Appendix B: check Table B-1, then use the Table B-2 activity class 'if the property is specifically listed in Table B-2 under the type of activity in which it is used.' The extra choices (no class life, qualified technological equipment, research and experimentation, qualified improvement property) match classifications in the line 19 column (a) instructions.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Takes the GDS recovery period for the asset class from Appendix B, as the instructions direct: 'use the recovery period shown in the appropriate column.' The table entries themselves are not in the text given, so only the method can be checked.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is a refusal screen. It excludes cases the text handles differently: disposals, like-kind exchanges, real property (mid-month convention), ADS and elected methods, basis adjustments that bar the percentage tables, general asset accounts, amortization, long-production property and aircraft, and qualified production property. It does not change any computed value.

### (b) — Year placed in service
Status: **MATCH**

Model: The placed-in-service year is a plain input, used to choose line 17 or line 19 and to find the year of recovery. The 2005 to 2025 range matches the screen's exclusion of earlier property.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special 
Status: **MATCH**

Model: Matches the first step of line 19 column (c): 'multiply the cost or other basis of the property by the percentage of business/investment use.' The section 179 and special allowance reductions are taken later, in the helpers that feed line 19(c). The refusal excludes listed property used 50% or less. The text notes the qualified business use percentage 'may be smaller' than business/investment use, but the program's percentage is business use only.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Matches line 6 column (c), 'Enter the amount you elect to expense.' It is shown only for non-listed property placed in 2025, consistent with 'Do not include any listed property on line 6.'

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' This input checks for that consistency, and a refusal covers mixed elections.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Applies 100% for property acquired after January 19, 2025 ('can elect to take a 40% special depreciation allowance ... instead'), 40% for property acquired before January 20, 2025, and zero on election out. The rate is applied to depreciable basis after the section 179 deduction, as 'multiplying the depreciable basis of the property by the applicable percentage' requires. Excepted property (ADS, listed property used 50% or less, same-year disposal) is screened or refused.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 for qualified listed property directs 'See the instructions for line 14 for the definition of qualified property and how to figure the deduction,' so using the line 14 computation matches.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: The instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The section 179 refusal requires more than 50% use, and vehicles (subject to the $31,300 limit) are excluded.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Business-use basis minus the section 179 deduction minus 'Any special depreciation allowance included on line 14', as the line 19 column (c) instructions say.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: Uses mid-quarter if Q4 bases 'exceed 40% of the total depreciable bases' (5×Q4 > 2×total is the same test), otherwise half-year. It then multiplies column (c) 'by the applicable rate from the appropriate table.' The roster inputs for the bases are assumed to follow the text's rules: before the special allowance and after section 179.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention input is half-year or mid-quarter with the quarter, consistent with the column (e) instructions. Mid-month property is excluded by the real-property screen.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: For property placed in service before 2025, the program applies the table rate to unadjusted basis (business basis less section 179 and less the special allowance), per Pub. 946: 'You must apply the table rates to your property's unadjusted basis.' It enters zero once the year of recovery passes the last year of recovery.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g).' The program uses the 19(g) computation for 2025 property and the line 17 computation for earlier property. Column (e) basis (cost × use %, less section 179 and the special allowance) matches the basis the program uses.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Follows Pub. 946 Appendix B: check Table B-1, then use the Table B-2 activity class 'if the property is specifically listed in Table B-2 under the type of activity in which it is used.' The extra choices (no class life, qualified technological equipment, research and experimentation, qualified improvement property) match classifications in the line 19 column (a) instructions."
  - key: "(d)"
    status: MATCH
    reason: "Takes the GDS recovery period for the asset class from Appendix B, as the instructions direct: 'use the recovery period shown in the appropriate column.' The table entries themselves are not in the text given, so only the method can be checked."
  - key: "asset.screen"
    status: MATCH
    reason: "This is a refusal screen. It excludes cases the text handles differently: disposals, like-kind exchanges, real property (mid-month convention), ADS and elected methods, basis adjustments that bar the percentage tables, general asset accounts, amortization, long-production property and aircraft, and qualified production property. It does not change any computed value."
  - key: "(b)"
    status: MATCH
    reason: "The placed-in-service year is a plain input, used to choose line 17 or line 19 and to find the year of recovery. The 2005 to 2025 range matches the screen's exclusion of earlier property."
  - key: "(c)"
    status: MATCH
    reason: "Matches the first step of line 19 column (c): 'multiply the cost or other basis of the property by the percentage of business/investment use.' The section 179 and special allowance reductions are taken later, in the helpers that feed line 19(c). The refusal excludes listed property used 50% or less. The text notes the qualified business use percentage 'may be smaller' than business/investment use, but the program's percentage is business use only."
  - key: "6(c)"
    status: MATCH
    reason: "Matches line 6 column (c), 'Enter the amount you elect to expense.' It is shown only for non-listed property placed in 2025, consistent with 'Do not include any listed property on line 6.'"
  - key: "asset.bonus_same"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' This input checks for that consistency, and a refusal covers mixed elections."
  - key: "14"
    status: MATCH
    reason: "Applies 100% for property acquired after January 19, 2025 ('can elect to take a 40% special depreciation allowance ... instead'), 40% for property acquired before January 20, 2025, and zero on election out. The rate is applied to depreciable basis after the section 179 deduction, as 'multiplying the depreciable basis of the property by the applicable percentage' requires. Excepted property (ADS, listed property used 50% or less, same-year disposal) is screened or refused."
  - key: "25"
    status: MATCH
    reason: "Line 25 for qualified listed property directs 'See the instructions for line 14 for the definition of qualified property and how to figure the deduction,' so using the line 14 computation matches."
  - key: "26(i)"
    status: MATCH
    reason: "The instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The section 179 refusal requires more than 50% use, and vehicles (subject to the $31,300 limit) are excluded."
  - key: "19(c)"
    status: MATCH
    reason: "Business-use basis minus the section 179 deduction minus 'Any special depreciation allowance included on line 14', as the line 19 column (c) instructions say."
  - key: "19(g)"
    status: MATCH
    reason: "Uses mid-quarter if Q4 bases 'exceed 40% of the total depreciable bases' (5×Q4 > 2×total is the same test), otherwise half-year. It then multiplies column (c) 'by the applicable rate from the appropriate table.' The roster inputs for the bases are assumed to follow the text's rules: before the special allowance and after section 179."
  - key: "(e)"
    status: MATCH
    reason: "The convention input is half-year or mid-quarter with the quarter, consistent with the column (e) instructions. Mid-month property is excluded by the real-property screen."
  - key: "17"
    status: MATCH
    reason: "For property placed in service before 2025, the program applies the table rate to unadjusted basis (business basis less section 179 and less the special allowance), per Pub. 946: 'You must apply the table rates to your property's unadjusted basis.' It enters zero once the year of recovery passes the last year of recovery."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g).' The program uses the 19(g) computation for 2025 property and the line 17 computation for earlier property. Column (e) basis (cost × use %, less section 179 and the special allowance) matches the basis the program uses."
```
```
