# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5c0d417a5a58db0e2b9ff7dc19e55e4354f168bf31163527aaf3ad087472cd47 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | e4a476216010971db277688a7525749a0ff50e66d84fa94b8e75f6de593ef333 |
| lines judged | 27 |
| match / mismatch / unclear / missing | 24 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 39, 41, 59, 60, 61, 62, 63, 71, 72, 73, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement asks only for the year, omitting month and day.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### 44a — Business miles
Status: **MATCH**

Model: IRS line 44a is 'Business' miles; the restatement correctly limits them to business use and excludes commuting, which line 44b covers separately.

### 44b — Commuting miles
Status: **MATCH**

Model: IRS line 44b is 'Commuting (see instructions)'; the restatement correctly refers to the line 44b instructions and the home-to-work definition.

### 44c — Other miles
Status: **MATCH**

Model: IRS line 44c is 'Other' miles; the restatement correctly describes these as other/personal miles.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: Matches the IRS line 9 conditions for using the standard mileage rate, including the five-or-more-vehicle restriction.

### (screen) (scveh.employee_use) — Your employees use this vehicle for personal purposes
Status: **MATCH**

Model: Matches the Form 4562 Part V column (c) employee-use rule, including 100% business treatment when personal use is included in income or reimbursed.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Matches IRS line 9: standard mileage amount plus parking and tolls, or business operating expenses plus parking and tolls for actual expenses.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: Matches the IRS line 9 rule that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used previously.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: IRS says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement uses only the business portion of lease payments and omits the inclusion amount.

Ruling: scope; refusal located elsewhere, restatement accepted. i1040sc line 20a, "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount": sc.special refuses "an inclusion amount for leased property" for the business, read for every Schedule C (the wording is unchanged by this package; checked in forms/2025/sc.yaml).

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: IRS column (b) says 'Date placed in service. Enter the date the property was placed in service'; the restatement asks only for the year, omitting the date and the conversion-date rule.

Ruling: representation; restatement accepted. i4562 p. 14, Column (b), "Enter the date the property was placed in service": the tool needs the year (and the quarter, asked separately, for 2025 property); the filer writes the date from their records.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The screen is a scope gate listing cases the tool excludes; it does not purport to compute the IRS line differently.

### (d) — Cost or other basis
Status: **MATCH**

Model: Matches Form 4562 Part V column (d): cost including sales tax or other basis, unadjusted for section 179 or depreciation, with the converted personal-use basis rule.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Matches the Pub. 946 worksheet line 13: multiply cost by the business-use percentage (business miles divided by total miles).

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Matches Form 4562 Part V column (i) elected section 179 cost, subject to the later limitations and refusals.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: Matches the Form 4562 line 14 election-out rule that the special allowance choice must be the same for the class.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Matches the Pub. 946 worksheet line 7: maximum depreciation deduction for the year from the appropriate passenger automobile table.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Matches the worksheet line 9: line 7 times the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Matches the worksheet line 10: section 179 claimed this year, not more than line 9 for a passenger automobile; zero if not placed in service this year.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Matches the worksheet line 11: subtract line 10 from line 9, with a zero floor.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Matches the worksheet line 14: section 179 claimed in the placed-in-service year; for a 2025 vehicle this is line 10.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Matches the worksheet line 15: subtract line 14 from line 13, the tentative basis for depreciation.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Matches the worksheet line 16: special depreciation allowance, zero if not placed in service this year or no allowance is claimed.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Matches Form 4562 line 25 together with the overall passenger automobile limit: the special allowance is limited by line 11.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Matches the worksheet line 17: subtract line 16 from line 11, the limit for MACRS depreciation, with a zero floor.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Matches the worksheet line 18: subtract line 16 from line 15, the basis for depreciation.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Matches the worksheet line 19: line 18 times the MACRS rate, using the half-year or mid-quarter convention for a 2025 vehicle and the prior-year convention for earlier placements.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Matches the worksheet line 20: the lesser of line 17 or line 19.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement asks only for the year, omitting month and day."
  - key: "44a"
    status: MATCH
    reason: "IRS line 44a is 'Business' miles; the restatement correctly limits them to business use and excludes commuting, which line 44b covers separately."
  - key: "44b"
    status: MATCH
    reason: "IRS line 44b is 'Commuting (see instructions)'; the restatement correctly refers to the line 44b instructions and the home-to-work definition."
  - key: "44c"
    status: MATCH
    reason: "IRS line 44c is 'Other' miles; the restatement correctly describes these as other/personal miles."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "Matches the IRS line 9 conditions for using the standard mileage rate, including the five-or-more-vehicle restriction."
  - key: "(screen) (scveh.employee_use)"
    status: MATCH
    reason: "Matches the Form 4562 Part V column (c) employee-use rule, including 100% business treatment when personal use is included in income or reimbursed."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Matches IRS line 9: standard mileage amount plus parking and tolls, or business operating expenses plus parking and tolls for actual expenses."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "Matches the IRS line 9 rule that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used previously."
  - key: "20a"
    status: MISMATCH
    reason: "IRS says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement uses only the business portion of lease payments and omits the inclusion amount."
  - key: "(b)"
    status: MISMATCH
    reason: "IRS column (b) says 'Date placed in service. Enter the date the property was placed in service'; the restatement asks only for the year, omitting the date and the conversion-date rule."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The screen is a scope gate listing cases the tool excludes; it does not purport to compute the IRS line differently."
  - key: "(d)"
    status: MATCH
    reason: "Matches Form 4562 Part V column (d): cost including sales tax or other basis, unadjusted for section 179 or depreciation, with the converted personal-use basis rule."
  - key: "13"
    status: MATCH
    reason: "Matches the Pub. 946 worksheet line 13: multiply cost by the business-use percentage (business miles divided by total miles)."
  - key: "(i)"
    status: MATCH
    reason: "Matches Form 4562 Part V column (i) elected section 179 cost, subject to the later limitations and refusals."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "Matches the Form 4562 line 14 election-out rule that the special allowance choice must be the same for the class."
  - key: "7"
    status: MATCH
    reason: "Matches the Pub. 946 worksheet line 7: maximum depreciation deduction for the year from the appropriate passenger automobile table."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Matches the worksheet line 9: line 7 times the business-use percentage."
  - key: "10"
    status: MATCH
    reason: "Matches the worksheet line 10: section 179 claimed this year, not more than line 9 for a passenger automobile; zero if not placed in service this year."
  - key: "11"
    status: MATCH
    reason: "Matches the worksheet line 11: subtract line 10 from line 9, with a zero floor."
  - key: "14"
    status: MATCH
    reason: "Matches the worksheet line 14: section 179 claimed in the placed-in-service year; for a 2025 vehicle this is line 10."
  - key: "15"
    status: MATCH
    reason: "Matches the worksheet line 15: subtract line 14 from line 13, the tentative basis for depreciation."
  - key: "16"
    status: MATCH
    reason: "Matches the worksheet line 16: special depreciation allowance, zero if not placed in service this year or no allowance is claimed."
  - key: "25"
    status: MATCH
    reason: "Matches Form 4562 line 25 together with the overall passenger automobile limit: the special allowance is limited by line 11."
  - key: "17"
    status: MATCH
    reason: "Matches the worksheet line 17: subtract line 16 from line 11, the limit for MACRS depreciation, with a zero floor."
  - key: "18"
    status: MATCH
    reason: "Matches the worksheet line 18: subtract line 16 from line 15, the basis for depreciation."
  - key: "19"
    status: MATCH
    reason: "Matches the worksheet line 19: line 18 times the MACRS rate, using the half-year or mid-quarter convention for a 2025 vehicle and the prior-year convention for earlier placements."
  - key: "20"
    status: MATCH
    reason: "Matches the worksheet line 20: the lesser of line 17 or line 19."
```
