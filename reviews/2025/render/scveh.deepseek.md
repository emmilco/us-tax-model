# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | fe34c4b233013cc042789fb8528ac1c2bd327970af236c69a005818cb52d6747 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 955488a7d83ff65edf3ea34b04b9179e1d61c3f9f351dc6d2a4a729697caca93 |
| lines judged | 26 |
| match / mismatch / unclear / missing | 22 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 59, 60, 61, 62, 63, 71, 72, 73, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: IRS line 43 asks "When did you place your vehicle in service for business purposes? (month/day/year)"; the restatement asks only for the year, omitting month/day.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for business miles, with commuting miles reported separately on 44b; the restatement matches that.

### 44b — Commuting miles
Status: **MATCH**

Model: The restatement matches line 44b and the instruction that commuting is generally travel between home and a work location.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for other miles; the restatement treats these as other/personal miles, consistent with the form.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The restatement matches the line 9 standard-mileage conditions: first-year use for an owned vehicle, entire lease period for a leased vehicle, and no five-or-more-vehicle use.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Standard mileage is business miles times 0.70 plus parking/tolls; actual expenses use the business portion of operating expenses plus parking/tolls, with lease payments on line 20a.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: The restatement matches the instruction that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used for it earlier.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: IRS says if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount; the restatement only takes the business portion of lease payments and has no inclusion-amount adjustment or refusal.

Ruling: refusal located elsewhere; restatement accepted. sc.special refuses "an inclusion amount for leased property" for the business, read for every Schedule C (checked by evaluation in the A-backlog session: sc.special answered Yes refuses at sc.line1).

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: IRS column (b) says "Date placed in service. Enter the date the property was placed in service"; the restatement asks only for the year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope gate; the refusal names the excluded cases, and within the supported cases the listed conditions are consistent with the IRS depreciation and listed-property text.

### (d) — Cost or other basis
Status: **MATCH**

Model: The restatement matches column (d): cost or other basis including sales tax, unadjusted for prior depreciation, and the smaller of adjusted basis or FMV for a conversion.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: The restatement matches worksheet line 13 and Form 4562 column (e) first step: cost or basis multiplied by the business-use percentage.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is the elected section 179 cost; the restatement treats it as that input, with the s179_bad refusal covering the vehicle-cost and SUV limits.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The input gates the special-allowance choice by 5-year class, consistent with the election-out rule being made for an entire class; mixed choices are refused.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The IRS text limits the deduction for passenger automobiles; the restatement uses the passenger-automobile limit table helper for every 2025 vehicle, even when the vehicle is not a passenger automobile.

Ruling: representation; restatement accepted. The worksheet line is figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass); checked by evaluation on stage14.veh.suv_179 with passenger answered both ways: the allowance is $20,200 and $70,000.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: The restatement matches worksheet line 9: multiply the maximum deduction on line 7 by the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10 is the section 179 deduction claimed this year, not more than line 9, and zero if not the year placed in service; the restatement matches.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 is line 9 minus line 10, not below zero; the restatement matches.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the section 179 deduction claimed in the year the vehicle was placed in service; using line 10 for a 2025 vehicle and prior_179 otherwise matches.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 is line 13 minus line 14, not below zero; the restatement matches.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16 is the special allowance only in the year placed in service, and zero otherwise; the restatement matches.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: For one vehicle, the special allowance allowed is capped by the remaining overall limit on line 11, so the smaller-of-lines computation is consistent with Form 4562 line 25 and the passenger-automobile limit.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 is line 11 minus line 16, not below zero; the restatement matches.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 is line 15 minus line 16, not below zero; the restatement matches.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Worksheet line 19 multiplies line 18 by the applicable MACRS rate; the 2025 half-year/mid-quarter choice and prior-year recovery rate are consistent with the tables.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20 is the lesser of line 17 or line 19; the restatement matches.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: 'IRS line 43 asks "When did you place your vehicle in service for business purposes? (month/day/year)"; the restatement asks only for the year, omitting month/day.'
  - key: "44a"
    status: MATCH
    reason: 'Line 44a asks for business miles, with commuting miles reported separately on 44b; the restatement matches that.'
  - key: "44b"
    status: MATCH
    reason: 'The restatement matches line 44b and the instruction that commuting is generally travel between home and a work location.'
  - key: "44c"
    status: MATCH
    reason: 'Line 44c asks for other miles; the restatement treats these as other/personal miles, consistent with the form.'
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: 'The restatement matches the line 9 standard-mileage conditions: first-year use for an owned vehicle, entire lease period for a leased vehicle, and no five-or-more-vehicle use.'
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: 'Standard mileage is business miles times 0.70 plus parking/tolls; actual expenses use the business portion of operating expenses plus parking/tolls, with lease payments on line 20a.'
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: 'The restatement matches the instruction that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used for it earlier.'
  - key: "20a"
    status: MISMATCH
    reason: 'IRS says if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount; the restatement only takes the business portion of lease payments and has no inclusion-amount adjustment or refusal.'
  - key: "(b)"
    status: MISMATCH
    reason: 'IRS column (b) says "Date placed in service. Enter the date the property was placed in service"; the restatement asks only for the year.'
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: 'This is a scope gate; the refusal names the excluded cases, and within the supported cases the listed conditions are consistent with the IRS depreciation and listed-property text.'
  - key: "(d)"
    status: MATCH
    reason: 'The restatement matches column (d): cost or other basis including sales tax, unadjusted for prior depreciation, and the smaller of adjusted basis or FMV for a conversion.'
  - key: "13"
    status: MATCH
    reason: 'The restatement matches worksheet line 13 and Form 4562 column (e) first step: cost or basis multiplied by the business-use percentage.'
  - key: "(i)"
    status: MATCH
    reason: 'Column (i) is the elected section 179 cost; the restatement treats it as that input, with the s179_bad refusal covering the vehicle-cost and SUV limits.'
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: 'The input gates the special-allowance choice by 5-year class, consistent with the election-out rule being made for an entire class; mixed choices are refused.'
  - key: "7"
    status: MISMATCH
    reason: 'The IRS text limits the deduction for passenger automobiles; the restatement uses the passenger-automobile limit table helper for every 2025 vehicle, even when the vehicle is not a passenger automobile.'
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: 'The restatement matches worksheet line 9: multiply the maximum deduction on line 7 by the business-use percentage.'
  - key: "10"
    status: MATCH
    reason: 'Worksheet line 10 is the section 179 deduction claimed this year, not more than line 9, and zero if not the year placed in service; the restatement matches.'
  - key: "11"
    status: MATCH
    reason: 'Worksheet line 11 is line 9 minus line 10, not below zero; the restatement matches.'
  - key: "14"
    status: MATCH
    reason: 'Worksheet line 14 is the section 179 deduction claimed in the year the vehicle was placed in service; using line 10 for a 2025 vehicle and prior_179 otherwise matches.'
  - key: "15"
    status: MATCH
    reason: 'Worksheet line 15 is line 13 minus line 14, not below zero; the restatement matches.'
  - key: "16"
    status: MATCH
    reason: 'Worksheet line 16 is the special allowance only in the year placed in service, and zero otherwise; the restatement matches.'
  - key: "25"
    status: MATCH
    reason: 'For one vehicle, the special allowance allowed is capped by the remaining overall limit on line 11, so the smaller-of-lines computation is consistent with Form 4562 line 25 and the passenger-automobile limit.'
  - key: "17"
    status: MATCH
    reason: 'Worksheet line 17 is line 11 minus line 16, not below zero; the restatement matches.'
  - key: "18"
    status: MATCH
    reason: 'Worksheet line 18 is line 15 minus line 16, not below zero; the restatement matches.'
  - key: "19"
    status: MATCH
    reason: 'Worksheet line 19 multiplies line 18 by the applicable MACRS rate; the 2025 half-year/mid-quarter choice and prior-year recovery rate are consistent with the tables.'
  - key: "20"
    status: MATCH
    reason: 'Worksheet line 20 is the lesser of line 17 or line 19; the restatement matches.'
```
