# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0d6acd42866d2ff044415426c352ba5f890cb99b812e2787a925380570b40a0a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 4d1235b5b9ff5f6cfc82c7026f6b53a277116a95b32c3330be03b0b244e9de48 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 14 / 1 / 0 / 0 |
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

Model: Follows Pub. 946 Appendix B: check Table B-1 and the activity in Table B-2, and use the Table B-2 class when the property is specifically listed under the activity. Classes A, B and C appear under 'Certain Property for Which Recovery Periods Assigned', and i4562 places qualified improvement property in 15-year property.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Looking up the GDS recovery period by asset class is what Pub. 946 Appendix B directs ('use the recovery period shown in the appropriate column'). The program's lookup table itself is not shown, so only the rule, not each entry, could be checked.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This gate narrows the tool to property under the MACRS percentage tables and sends excluded cases to a named refusal. Its exclusions track the text, including the Pub. 946 rule to stop using the tables after a basis adjustment such as a casualty loss, and the required ADS categories.

### (b) — Year placed in service
Status: **MATCH**

Model: The filer enters the year placed in service, which matches the i4562 placed-in-service entries and is what the recovery-year lookup needs. Years before 2005 are excluded by the screen.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: Cost or other basis times the business-use percentage is the first step of i4562 line 19 column (c): 'multiply the cost or other basis of the property by the percentage of business/investment use.' Later subtractions are handled in helpers and line 19(c), and listed property used 50% or less is refused as outside the tool.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: i4562 line 6 column (c) says 'Enter the amount you elect to expense', and line 6 excludes listed property, as the reporting rule does. Elections above business cost or on property used 50% or less for business are refused, consistent with 'used predominantly (more than 50%)'.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: i4562 describes the election out as applying 'for all such property in such class placed in service during the tax year.' A choice that differs within a class is refused by name, which is a permitted narrowing.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The allowance is 100% of basis after section 179 if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero on election out, as i4562 line 14 provides. It is figured on depreciable basis after section 179, and long-production property, aircraft and qualified production property are screened out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: i4562 line 25 refers to the line 14 instructions for how to figure the allowance and says to enter the special depreciation allowance for qualified listed property. This entry's line 14 amount is that figure, and listed property used 50% or less is refused.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: i4562 line 6 says 'Enter the elected section 179 cost of listed property in column (i) of line 26', and the restatement carries the elected amount there. Use of 50% or less is refused, consistent with the column (i) requirement of more than 50% use.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Business-use cost less section 179 less the line 14 allowance matches i4562 line 19 column (c), which lists 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14' as reductions. Other credit and basis adjustments are excluded by the screen.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: Column (c) times the applicable table rate matches 'Multiply column (c) by the applicable rate from the appropriate table.' The test 5 x fourth-quarter bases > 2 x total bases equals 'exceed 40%', and the bases are after section 179 and business-use reduction but before the special allowance, as Pub. 946 states.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: i4562 column (e) and Pub. 946 provide half-year and mid-quarter conventions for this property, with the mid-quarter rate depending on the quarter placed in service. Mid-month applies only to real property and railroad gradings and tunnel bores, which the screen and class lookup exclude.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 follows the line 19 column (g) method, and Pub. 946 applies table rates to unadjusted basis reduced by section 179 and any special allowance, as the restatement does. The result is zero once the recovery period has ended, since the table has no further rate; the listed-property routing gap noted at 26(h) is the only exception.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MISMATCH**

Restated: Add helper "MACRS on 2025 property" and helper "MACRS on property placed in service before 2025".

Model: The computation matches column (h), but the gate that reports this line asks only about 'a computer placed in service before 2018', while i4562 column (a) lists 'computers and peripheral equipment placed in service before 2018'. A pre-2018 peripheral not used exclusively at a regular business establishment would be treated as non-listed, so it would miss line 26(h) and go to line 17.

Ruling: deferred to T-030 (owner); values unaffected. The sum is figured for every asset; line 26 column (h) adds it only for listed property (sc.f26_assets, where listed). Entry lines are not printed on the values sheet (TASKS.md T-030), and the Form 4562 totals take the asset's amounts only where they belong (the sc sums select 2025 property, earlier property and listed property: sc.f14, sc.f17, sc.f19_*, sc.f25, sc.f26h). The owner chose that, when entry lines are printed, each per-asset printed line will carry the form's value for that asset (T-030).

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Follows Pub. 946 Appendix B: check Table B-1 and the activity in Table B-2, and use the Table B-2 class when the property is specifically listed under the activity. Classes A, B and C appear under 'Certain Property for Which Recovery Periods Assigned', and i4562 places qualified improvement property in 15-year property."
  - key: "(d)"
    status: MATCH
    reason: "Looking up the GDS recovery period by asset class is what Pub. 946 Appendix B directs ('use the recovery period shown in the appropriate column'). The program's lookup table itself is not shown, so only the rule, not each entry, could be checked."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This gate narrows the tool to property under the MACRS percentage tables and sends excluded cases to a named refusal. Its exclusions track the text, including the Pub. 946 rule to stop using the tables after a basis adjustment such as a casualty loss, and the required ADS categories."
  - key: "(b)"
    status: MATCH
    reason: "The filer enters the year placed in service, which matches the i4562 placed-in-service entries and is what the recovery-year lookup needs. Years before 2005 are excluded by the screen."
  - key: "(c)"
    status: MATCH
    reason: "Cost or other basis times the business-use percentage is the first step of i4562 line 19 column (c): 'multiply the cost or other basis of the property by the percentage of business/investment use.' Later subtractions are handled in helpers and line 19(c), and listed property used 50% or less is refused as outside the tool."
  - key: "6(c)"
    status: MATCH
    reason: "i4562 line 6 column (c) says 'Enter the amount you elect to expense', and line 6 excludes listed property, as the reporting rule does. Elections above business cost or on property used 50% or less for business are refused, consistent with 'used predominantly (more than 50%)'."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "i4562 describes the election out as applying 'for all such property in such class placed in service during the tax year.' A choice that differs within a class is refused by name, which is a permitted narrowing."
  - key: "14"
    status: MATCH
    reason: "The allowance is 100% of basis after section 179 if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero on election out, as i4562 line 14 provides. It is figured on depreciable basis after section 179, and long-production property, aircraft and qualified production property are screened out."
  - key: "25"
    status: MATCH
    reason: "i4562 line 25 refers to the line 14 instructions for how to figure the allowance and says to enter the special depreciation allowance for qualified listed property. This entry's line 14 amount is that figure, and listed property used 50% or less is refused."
  - key: "26(i)"
    status: MATCH
    reason: "i4562 line 6 says 'Enter the elected section 179 cost of listed property in column (i) of line 26', and the restatement carries the elected amount there. Use of 50% or less is refused, consistent with the column (i) requirement of more than 50% use."
  - key: "19(c)"
    status: MATCH
    reason: "Business-use cost less section 179 less the line 14 allowance matches i4562 line 19 column (c), which lists 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14' as reductions. Other credit and basis adjustments are excluded by the screen."
  - key: "19(g)"
    status: MATCH
    reason: "Column (c) times the applicable table rate matches 'Multiply column (c) by the applicable rate from the appropriate table.' The test 5 x fourth-quarter bases > 2 x total bases equals 'exceed 40%', and the bases are after section 179 and business-use reduction but before the special allowance, as Pub. 946 states."
  - key: "(e)"
    status: MATCH
    reason: "i4562 column (e) and Pub. 946 provide half-year and mid-quarter conventions for this property, with the mid-quarter rate depending on the quarter placed in service. Mid-month applies only to real property and railroad gradings and tunnel bores, which the screen and class lookup exclude."
  - key: "17"
    status: MATCH
    reason: "Line 17 follows the line 19 column (g) method, and Pub. 946 applies table rates to unadjusted basis reduced by section 179 and any special allowance, as the restatement does. The result is zero once the recovery period has ended, since the table has no further rate; the listed-property routing gap noted at 26(h) is the only exception."
  - key: "26(h)"
    status: MISMATCH
    reason: "The computation matches column (h), but the gate that reports this line asks only about 'a computer placed in service before 2018', while i4562 column (a) lists 'computers and peripheral equipment placed in service before 2018'. A pre-2018 peripheral not used exclusively at a regular business establishment would be treated as non-listed, so it would miss line 26(h) and go to line 17."
```
```
