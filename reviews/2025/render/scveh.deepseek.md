# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7311dd255992e1262a76689bdf1de0e72a6059e8660ec52195cc208ad58d61ae |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 75872f6f2e339c3b7481cda1c990456eb7b7d9d4e15ab5bc130fc2681f2a39f7 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 19 / 6 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement captures only the year, not the required date.

Ruling: open

### 44a — Business miles
Status: **MATCH**

Model: IRS line 44a is business miles, and excluding commuting is consistent with the business-use percentage rule.

### 44b — Commuting miles
Status: **MATCH**

Model: IRS line 44b is commuting miles, and the line 44b instructions define commuting as travel between home and a work location.

### 44c — Other miles
Status: **MATCH**

Model: IRS line 44c is 'Other' miles; treating this as the personal/nonbusiness remainder is consistent with the total-miles computation.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The standard mileage eligibility questions match the line 9 instruction: owned and used in first year, or leased and used for the entire lease; five or more simultaneous vehicles require actual expenses.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MISMATCH**

Restated: Choose — [helper "Standard mileage rate or actual expenses" = 'standard' → helper "Standard mileage amount plus parking fees and tolls"] [helper "Standard mileage rate or actual expenses" = 'actual' → helper "Business portion of the operating expenses plus parking fees and tolls"]

Model: IRS says 'You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle'; the restatement allows actual whenever method is actual and only refuses standard under smr_bad.

Ruling: open

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: IRS line 20a says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement uses the gross business lease payments without the inclusion amount.

Ruling: open

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: IRS column (b) says 'Date placed in service. Enter the date the property was placed in service' (including conversion date); the restatement asks only for the year.

Ruling: open

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The screen collects the special-history and vehicle-type cases, and the line (d) refusal names the screened cases as outside the tool.

### (d) — Cost or other basis
Status: **MATCH**

Model: This matches column (d): actual cost including sales tax or other basis unadjusted for prior depreciation, with converted property using the smaller of adjusted basis or FMV on conversion.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Pub. 946 worksheet line 13 multiplies the cost/basis by the business/investment-use percentage, and the mileage ratio is the IRS method for vehicles.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is the elected section 179 cost; the related limits are handled by the low-use and section 179 refusal gates.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The special allowance election is by class, and a differing election within the 5-year class is refused as outside the tool.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: IRS states 'The depreciation deduction, including the section 179 expense deduction and special depreciation allowance, for passenger automobiles is limited'; the restatement applies a published passenger-automobile limit unconditionally and has no refusal when scveh.passenger is false.

Ruling: open

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Pub. 946 worksheet line 9 multiplies the maximum deduction by the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: For a 2025 passenger automobile, worksheet line 10 is the section 179 deduction not more than line 9; otherwise it is zero.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Pub. 946 worksheet line 11 subtracts line 10 from line 9.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Pub. 946 worksheet line 14 is the section 179 deduction claimed in the year the car was placed in service; current line 10 applies for 2025, prior_179 otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Pub. 946 worksheet line 15 subtracts line 14 from line 13.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Pub. 946 worksheet line 16 is the special depreciation allowance only in the placed-in-service year; it is zero for earlier-placed vehicles.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Form 4562 line 25 reports the special allowance included in the passenger automobile overall limit; capping it at line 11 is consistent with that limit.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Pub. 946 worksheet line 17 subtracts line 16 from line 11 to get the limit on MACRS depreciation.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Pub. 946 worksheet line 18 subtracts line 16 from line 15 to get the basis for depreciation.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: For a vehicle whose recovery period ended before 2025, IRS says 'enter your unrecovered basis, if any, in column (h)' and Pub. 946 allows unrecovered basis after the recovery period; the restatement forces zero for a 2019-placed vehicle.

Ruling: open

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Pub. 946 worksheet line 20 is the lesser of line 17 or line 19.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement captures only the year, not the required date."
  - key: "44a"
    status: MATCH
    reason: "IRS line 44a is business miles, and excluding commuting is consistent with the business-use percentage rule."
  - key: "44b"
    status: MATCH
    reason: "IRS line 44b is commuting miles, and the line 44b instructions define commuting as travel between home and a work location."
  - key: "44c"
    status: MATCH
    reason: "IRS line 44c is 'Other' miles; treating this as the personal/nonbusiness remainder is consistent with the total-miles computation."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The standard mileage eligibility questions match the line 9 instruction: owned and used in first year, or leased and used for the entire lease; five or more simultaneous vehicles require actual expenses."
  - key: "9 (scveh.line9)"
    status: MISMATCH
    reason: "IRS says 'You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle'; the restatement allows actual whenever method is actual and only refuses standard under smr_bad."
  - key: "20a"
    status: MISMATCH
    reason: "IRS line 20a says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement uses the gross business lease payments without the inclusion amount."
  - key: "(b)"
    status: MISMATCH
    reason: "IRS column (b) says 'Date placed in service. Enter the date the property was placed in service' (including conversion date); the restatement asks only for the year."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The screen collects the special-history and vehicle-type cases, and the line (d) refusal names the screened cases as outside the tool."
  - key: "(d)"
    status: MATCH
    reason: "This matches column (d): actual cost including sales tax or other basis unadjusted for prior depreciation, with converted property using the smaller of adjusted basis or FMV on conversion."
  - key: "13"
    status: MATCH
    reason: "Pub. 946 worksheet line 13 multiplies the cost/basis by the business/investment-use percentage, and the mileage ratio is the IRS method for vehicles."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is the elected section 179 cost; the related limits are handled by the low-use and section 179 refusal gates."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The special allowance election is by class, and a differing election within the 5-year class is refused as outside the tool."
  - key: "7"
    status: MISMATCH
    reason: "IRS states 'The depreciation deduction, including the section 179 expense deduction and special depreciation allowance, for passenger automobiles is limited'; the restatement applies a published passenger-automobile limit unconditionally and has no refusal when scveh.passenger is false."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Pub. 946 worksheet line 9 multiplies the maximum deduction by the business-use percentage."
  - key: "10"
    status: MATCH
    reason: "For a 2025 passenger automobile, worksheet line 10 is the section 179 deduction not more than line 9; otherwise it is zero."
  - key: "11"
    status: MATCH
    reason: "Pub. 946 worksheet line 11 subtracts line 10 from line 9."
  - key: "14"
    status: MATCH
    reason: "Pub. 946 worksheet line 14 is the section 179 deduction claimed in the year the car was placed in service; current line 10 applies for 2025, prior_179 otherwise."
  - key: "15"
    status: MATCH
    reason: "Pub. 946 worksheet line 15 subtracts line 14 from line 13."
  - key: "16"
    status: MATCH
    reason: "Pub. 946 worksheet line 16 is the special depreciation allowance only in the placed-in-service year; it is zero for earlier-placed vehicles."
  - key: "25"
    status: MATCH
    reason: "Form 4562 line 25 reports the special allowance included in the passenger automobile overall limit; capping it at line 11 is consistent with that limit."
  - key: "17"
    status: MATCH
    reason: "Pub. 946 worksheet line 17 subtracts line 16 from line 11 to get the limit on MACRS depreciation."
  - key: "18"
    status: MATCH
    reason: "Pub. 946 worksheet line 18 subtracts line 16 from line 15 to get the basis for depreciation."
  - key: "19"
    status: MISMATCH
    reason: "For a vehicle whose recovery period ended before 2025, IRS says 'enter your unrecovered basis, if any, in column (h)' and Pub. 946 allows unrecovered basis after the recovery period; the restatement forces zero for a 2019-placed vehicle."
  - key: "20"
    status: MATCH
    reason: "Pub. 946 worksheet line 20 is the lesser of line 17 or line 19."
```
