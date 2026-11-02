# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 77833620d219cb4f9c568dea77631cb2db9c9ad543369a2bb01774ec062a0b2b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 2ac0576d88cb323f64f71c418327b6fe3b235d5641e72f5107aacd18c16aeea1 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 15 / 0 / 0 / 0 |
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

Model: Pub. 946 Appendix B says to check Table B-1 and the activity in Table B-2, using the Table B-2 period when the property is 'specifically listed in Table B-2 under the type of activity in which it is used'. Choices A, B and C are in the 'Certain Property for Which Recovery Periods Assigned' list, and the Form 4562 instructions classify qualified improvement property separately.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The restatement takes the GDS recovery period from Appendix B by asset class, as the Pub. 946 tables and the column (d) instructions direct. The program's table entries are not shown, so this judges the reference rather than each row.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is a refusal gate that narrows the tool to property the IRS text treats under the MACRS percentage tables, and it excludes basis adjustments, ADS, other methods, general asset accounts and dispositions. One gap is that it does not name short tax years, although Pub. 946 says 'You cannot use the percentage tables for a short tax year'.

### (b) — Year placed in service
Status: **MATCH**

Model: This is the year placed in service, which the instructions and Pub. 946 use to determine the depreciation year. The 2005 to 2025 range is a narrowing enforced by the screen.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: This computes the first step of the line 19 column (c) instruction, 'multiply the cost or other basis of the property by the percentage of business/investment use', with later reductions handled by other lines. The listed-property refusal tests business use, while the instructions note that qualified business use 'may be smaller', so a filer must answer the percentage on that basis for the line 27 exclusion to work as named.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: Column (c) says 'Enter the amount you elect to expense', and the restatement takes that as an input. The non-listed gate follows 'Do not include any listed property on line 6', and the refusal enforces the business-cost cap and the more-than-50% use requirement.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The instructions make the election out apply 'for any class of property' to 'all such property in such class placed in service during the tax year'. This question only sends mixed choices to a refusal, which is a permitted narrowing, including its conservative treatment of a spouse's property.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The result is 100% of depreciable basis if acquired after January 19, 2025, 40% if acquired after September 27, 2017 and before January 20, 2025, 40% if elected, and zero on election out. Depreciable basis is taken after section 179, as the line 14 instructions state, and the 60%, 50% and QPP cases are screened out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 reports the special depreciation allowance for qualified listed property, figured as in 'the instructions for line 14'. Using the line 14 computation for each listed entry matches this, and listed property used 50% or less is refused.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: The line 6 instructions say to 'Enter the elected section 179 cost of listed property in column (i) of line 26'. The restatement carries the elected amount there for listed property placed in service in 2025.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The instructions take the business portion of cost and subtract the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'. The helper computes exactly that, and other basis adjustments are screened out.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The instructions say to 'Multiply column (c) by the applicable rate from the appropriate table', using Table A-1 or the mid-quarter table for the quarter. The 5 times versus 2 times test equals 'exceed 40%', on bases after section 179 and before the special allowance as Pub. 946 states; the test sums only Schedule C property and vehicles, so it assumes no other MACRS property in the tool's scope.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The filer supplies the half-year or mid-quarter convention, with the quarter, for the year the property was placed in service. These are the conventions the column (e) instructions and Pub. 946 give for non-real property, and mid-month property is screened out.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 follows the line 19(g) method for earlier-year MACRS property, and Pub. 946 says to apply table rates to unadjusted basis reduced by the section 179 deduction and special allowance. The restatement does this using the 2025 recovery year, and gives zero after the recovery period, consistent with no rate remaining in the tables.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, the instructions say to 'figure column (h) by following the instructions for line 19, column (g)'. The restatement uses the 19(g) computation for 2025 property and the line 17 computation for earlier property, and vehicles are handled separately.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Pub. 946 Appendix B says to check Table B-1 and the activity in Table B-2, using the Table B-2 period when the property is 'specifically listed in Table B-2 under the type of activity in which it is used'. Choices A, B and C are in the 'Certain Property for Which Recovery Periods Assigned' list, and the Form 4562 instructions classify qualified improvement property separately."
  - key: "(d)"
    status: MATCH
    reason: "The restatement takes the GDS recovery period from Appendix B by asset class, as the Pub. 946 tables and the column (d) instructions direct. The program's table entries are not shown, so this judges the reference rather than each row."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is a refusal gate that narrows the tool to property the IRS text treats under the MACRS percentage tables, and it excludes basis adjustments, ADS, other methods, general asset accounts and dispositions. One gap is that it does not name short tax years, although Pub. 946 says 'You cannot use the percentage tables for a short tax year'."
  - key: "(b)"
    status: MATCH
    reason: "This is the year placed in service, which the instructions and Pub. 946 use to determine the depreciation year. The 2005 to 2025 range is a narrowing enforced by the screen."
  - key: "(c)"
    status: MATCH
    reason: "This computes the first step of the line 19 column (c) instruction, 'multiply the cost or other basis of the property by the percentage of business/investment use', with later reductions handled by other lines. The listed-property refusal tests business use, while the instructions note that qualified business use 'may be smaller', so a filer must answer the percentage on that basis for the line 27 exclusion to work as named."
  - key: "6(c)"
    status: MATCH
    reason: "Column (c) says 'Enter the amount you elect to expense', and the restatement takes that as an input. The non-listed gate follows 'Do not include any listed property on line 6', and the refusal enforces the business-cost cap and the more-than-50% use requirement."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The instructions make the election out apply 'for any class of property' to 'all such property in such class placed in service during the tax year'. This question only sends mixed choices to a refusal, which is a permitted narrowing, including its conservative treatment of a spouse's property."
  - key: "14"
    status: MATCH
    reason: "The result is 100% of depreciable basis if acquired after January 19, 2025, 40% if acquired after September 27, 2017 and before January 20, 2025, 40% if elected, and zero on election out. Depreciable basis is taken after section 179, as the line 14 instructions state, and the 60%, 50% and QPP cases are screened out."
  - key: "25"
    status: MATCH
    reason: "Line 25 reports the special depreciation allowance for qualified listed property, figured as in 'the instructions for line 14'. Using the line 14 computation for each listed entry matches this, and listed property used 50% or less is refused."
  - key: "26(i)"
    status: MATCH
    reason: "The line 6 instructions say to 'Enter the elected section 179 cost of listed property in column (i) of line 26'. The restatement carries the elected amount there for listed property placed in service in 2025."
  - key: "19(c)"
    status: MATCH
    reason: "The instructions take the business portion of cost and subtract the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'. The helper computes exactly that, and other basis adjustments are screened out."
  - key: "19(g)"
    status: MATCH
    reason: "The instructions say to 'Multiply column (c) by the applicable rate from the appropriate table', using Table A-1 or the mid-quarter table for the quarter. The 5 times versus 2 times test equals 'exceed 40%', on bases after section 179 and before the special allowance as Pub. 946 states; the test sums only Schedule C property and vehicles, so it assumes no other MACRS property in the tool's scope."
  - key: "(e)"
    status: MATCH
    reason: "The filer supplies the half-year or mid-quarter convention, with the quarter, for the year the property was placed in service. These are the conventions the column (e) instructions and Pub. 946 give for non-real property, and mid-month property is screened out."
  - key: "17"
    status: MATCH
    reason: "Line 17 follows the line 19(g) method for earlier-year MACRS property, and Pub. 946 says to apply table rates to unadjusted basis reduced by the section 179 deduction and special allowance. The restatement does this using the 2025 recovery year, and gives zero after the recovery period, consistent with no rate remaining in the tables."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, the instructions say to 'figure column (h) by following the instructions for line 19, column (g)'. The restatement uses the 19(g) computation for 2025 property and the line 17 computation for earlier property, and vehicles are handled separately."
```
```
