# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9af2d6bde8017cb980ed253034b09e10123fc19a1fe59e1b387f033dcd91dc6a |
| lines judged | 12 |
| match / mismatch / unclear / missing | 7 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: Pub. 946 Appendix B says to check Table B-1, then use the Table B-2 recovery period if the property is specifically included under the activity, and otherwise use Table B-1. The extra choices (no class life, qualified technological equipment, research and experimentation property, qualified improvement property) are classifications the instructions name for line 19 column (a).

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Column (d) is the GDS recovery period for the property's classification or class life, as in the instructions' 'Recovery Period for Most Property' table and Pub. 946 Appendix B. Looking it up by asset class does this.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is a refusal screen that narrows the tool to supported cases. Each excluded situation (dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments, general asset accounts, amortization, long production period or aircraft, qualified production property) is one the text treats under separate rules, and the screen names them.

### (b) — Year placed in service
Status: **MATCH**

Model: The year placed in service is an input, as column (b) and Pub. 946 require. The 2005 to 2025 range is a narrowing the screen discloses.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special 
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: The restatement stops at cost times the business-use percentage. Line 19 column (c) says 'multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property', including the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'.

Ruling: deferred to T-030 (owner); values unaffected. The line is the business-use basis before the section 179 deduction and the special allowance; the form's column (c) subtracts them, which the project does on asset.ub, the basis every MACRS amount uses. Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Line 6 column (c) says 'Enter the amount you elect to expense.' The input matches, and the s179_bad refusal enforces the more-than-50% business use rule from Part I.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out is made 'for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year'. Refusing when the choice differs within a class is a disclosed narrowing.

### 14 — Special depreciation allowance for this property
Status: **MISMATCH**

Restated: Choose — [helper "Special depreciation allowance for this class of property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%"] [helper "Special depreciation allowance for this class of property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for this class of property" = 'none' → helper "Zero"]

Model: The text says the allowance is 'For qualified property ... placed in service during the tax year' and 'applies only for the first year the property is placed in service'. The restatement does not depend on placement in 2025, so property placed in service in an earlier year would still produce a line 14 amount.

Ruling: deferred to T-030 (owner); values unaffected. The allowance is figured for every asset; Form 4562 line 14 adds it only for 2025 property that is not listed (asset.bonus_2025 with the listed filter) and line 25 for listed property, so an earlier asset's figure reaches no line. Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

### 19(g) — MACRS depreciation for 2025 property
Status: **MISMATCH**

Restated: Choose — [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = false → helper "MACRS depreciation, half-year convention"] [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = true → helper "MACRS depreciation, mid-quarter convention"]

Model: The basis after section 179 and the special allowance, times the table rate, under the convention set by a test that is true when fourth-quarter bases 'exceed 40%' of all 2025 bases, is correct for non-listed property. However, the text says 'Use lines 19a through 19j only for assets placed in service during the tax year ... except for automobiles and other listed property (which are reported in Part V)', and the restatement does not exclude listed property used more than 50%.

Ruling: deferred to T-030 (owner); values unaffected. MACRS on 2025 property is figured for every asset; lines 19a to 19j add it only for 2025 property that is not listed (asset.dep_2025 by period, with the listed filter). Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The instructions name half-year and mid-quarter as the conventions for this kind of property, and the mid-quarter convention depends on the quarter placed in service. The input records this.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MISMATCH**

Restated: Choose — [helper "The recovery period ended before 2025" = false → helper "MACRS depreciation for 2025"] [helper "The recovery period ended before 2025" = true → helper "Zero"]

Model: Line 17 is 'For tangible property placed in service in tax years beginning before 2025', and Part V covers depreciation on listed property 'regardless of the tax year the property was placed in service'. The restatement does not depend on placement before 2025 or on listed status, so 2025 property or listed property would also produce a line 17 amount.

Ruling: deferred to T-030 (owner); values unaffected. MACRS on earlier property is figured for every asset; line 17 adds it only for property placed in service before 2025 that is not listed (asset.dep_prior with the listed filter). Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

### 26(h) — Depreciation of this listed property (column (h))
Status: **MISMATCH**

Restated: Add helper "MACRS on 2025 property" and helper "MACRS on property placed in service before 2025".

Model: Line 26 is for listed property: 'Use line 26 to figure depreciation for property used more than 50% in a qualified business use', within Part V, Listed Property. The restatement adds line 19(g) and line 17 MACRS for every item, including non-listed property that belongs only on lines 17 and 19.

Ruling: deferred to T-030 (owner); values unaffected. The sum is figured for every asset; line 26 column (h) adds it only for listed property (sc.f26_assets, where listed). Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Pub. 946 Appendix B says to check Table B-1, then use the Table B-2 recovery period if the property is specifically included under the activity, and otherwise use Table B-1. The extra choices (no class life, qualified technological equipment, research and experimentation property, qualified improvement property) are classifications the instructions name for line 19 column (a)."
  - key: "(d)"
    status: MATCH
    reason: "Column (d) is the GDS recovery period for the property's classification or class life, as in the instructions' 'Recovery Period for Most Property' table and Pub. 946 Appendix B. Looking it up by asset class does this."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is a refusal screen that narrows the tool to supported cases. Each excluded situation (dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments, general asset accounts, amortization, long production period or aircraft, qualified production property) is one the text treats under separate rules, and the screen names them."
  - key: "(b)"
    status: MATCH
    reason: "The year placed in service is an input, as column (b) and Pub. 946 require. The 2005 to 2025 range is a narrowing the screen discloses."
  - key: "(c)"
    status: MISMATCH
    reason: "The restatement stops at cost times the business-use percentage. Line 19 column (c) says 'multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property', including the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'."
  - key: "6(c)"
    status: MATCH
    reason: "Line 6 column (c) says 'Enter the amount you elect to expense.' The input matches, and the s179_bad refusal enforces the more-than-50% business use rule from Part I."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The election out is made 'for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year'. Refusing when the choice differs within a class is a disclosed narrowing."
  - key: "14"
    status: MISMATCH
    reason: "The text says the allowance is 'For qualified property ... placed in service during the tax year' and 'applies only for the first year the property is placed in service'. The restatement does not depend on placement in 2025, so property placed in service in an earlier year would still produce a line 14 amount."
  - key: "19(g)"
    status: MISMATCH
    reason: "The basis after section 179 and the special allowance, times the table rate, under the convention set by a test that is true when fourth-quarter bases 'exceed 40%' of all 2025 bases, is correct for non-listed property. However, the text says 'Use lines 19a through 19j only for assets placed in service during the tax year ... except for automobiles and other listed property (which are reported in Part V)', and the restatement does not exclude listed property used more than 50%."
  - key: "(e)"
    status: MATCH
    reason: "The instructions name half-year and mid-quarter as the conventions for this kind of property, and the mid-quarter convention depends on the quarter placed in service. The input records this."
  - key: "17"
    status: MISMATCH
    reason: "Line 17 is 'For tangible property placed in service in tax years beginning before 2025', and Part V covers depreciation on listed property 'regardless of the tax year the property was placed in service'. The restatement does not depend on placement before 2025 or on listed status, so 2025 property or listed property would also produce a line 17 amount."
  - key: "26(h)"
    status: MISMATCH
    reason: "Line 26 is for listed property: 'Use line 26 to figure depreciation for property used more than 50% in a qualified business use', within Part V, Listed Property. The restatement adds line 19(g) and line 17 MACRS for every item, including non-listed property that belongs only on lines 17 and 19."
```
```
