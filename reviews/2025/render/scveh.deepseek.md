# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d429bc33fb4aca749b275d2eb6dc58116ae60ef44ff7c3308532f91e3c1179c8 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 7e2c86a963dca5741dfde9e9633733a25c00704f6fd7dd34c66d6724182eb0e2 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 21 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: The IRS line asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement records only the year, omitting the month and day.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 and Form 4562 from their own records. No value depends on the month or day except through the quarter, which is asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for business miles, and the restatement says business miles not commuting, which matches the column (c) instruction to exclude commuting mileage.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles, and the restatement gives commuting as travel between home and a work location, consistent with the line 44b instructions.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c is the 'Other' miles category; treating those as personal/other nonbusiness miles is consistent with the form's three-way split.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The Schedule C line 9 instructions allow the standard mileage rate only if the vehicle was owned and the rate was used in the first year, or leased and the rate is used for the entire lease period, and require actual expenses for five or more vehicles used together.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: The restatement follows Schedule C line 9: standard mileage times business miles plus parking and tolls, or the business portion of actual operating expenses plus parking and tolls.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The IRS says 'enter on line 20a the business portion of your rental cost. But if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement omits the inclusion amount.

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ('an inclusion amount for leased property'), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Form 4562 Part V column (b) says 'Enter the date the property was placed in service'; the restatement asks only for the year.

Ruling: representation; restatement accepted. As line 43: the year chooses the recovery year and the limits, the quarter (asked separately) the mid-quarter table; the filer enters the full date on Form 4562 column (b).

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope gate: the IRS text treats trade-ins, prior credits/clean-fuel basis adjustments, conversions, 50%-or-less use, and for-hire/ambulance/hearse vehicles as special cases, and the refusal names those exclusions.

### (d) — Cost or other basis
Status: **MATCH**

Model: Column (d) asks for actual cost or other basis including sales tax, unadjusted for prior depreciation and not reduced by section 179, with the converted-property rule using the smaller of adjusted basis or fair market value.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: The Pub. 946 worksheet line 13 multiplies cost by the business/investment-use percentage; using business miles divided by total miles matches the Part V column (c) rule.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is the elected section 179 cost; the restatement asks for the amount elected, with zero if none, and the later section 179 refusal handles the limits.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The special depreciation allowance election is made by class of property for all such property placed in service during the tax year, so asking whether the choice is the same for all 5-year property is consistent.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Worksheet line 7 is the maximum depreciation deduction from the appropriate table; for a 2025 vehicle that is the first-year limit, and for an earlier vehicle it is the limit for its 2025 recovery year.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says to multiply line 7 by the business/investment-use percentage, which the restatement does using business miles divided by total miles.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10 is the section 179 deduction claimed this year, not more than line 9, and zero if this is not the year the vehicle was placed in service.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 subtracts line 10 from line 9 to get the depreciation limit; adding a zero floor does not change a valid worksheet result.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the section 179 deduction claimed in the year the vehicle was placed in service, which is line 10 for a 2025 vehicle and the prior-year input otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 subtracts line 14 from line 13 to get tentative basis for depreciation; the zero floor is harmless for valid inputs.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16 is the special depreciation allowance, and the restatement uses the 2025 allowance calculation or zero if not placed in service in 2025.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Form 4562 line 25 reports the special depreciation allowance, and the passenger automobile limit caps the special allowance plus section 179 by line 11, so using the smaller of line 16 or line 11 is consistent.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 subtracts line 16 from line 11 to get the limit on MACRS depreciation; the zero floor is consistent with the worksheet's stopping rule.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 subtracts line 16 from line 15 to get basis for depreciation; the zero floor is harmless because the special allowance cannot exceed line 15.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: For a 2019 vehicle, the IRS says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)' and permits deductions after the recovery period; the restatement returns zero for a 2019 vehicle.

Ruling: representation; restatement accepted. Line 19 is a line of the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); Pub. 946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20 says to enter the lesser of line 17 or line 19 as the MACRS depreciation deduction, which the restatement does.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The IRS line asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement records only the year, omitting the month and day."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for business miles, and the restatement says business miles not commuting, which matches the column (c) instruction to exclude commuting mileage."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles, and the restatement gives commuting as travel between home and a work location, consistent with the line 44b instructions."
  - key: "44c"
    status: MATCH
    reason: "Line 44c is the 'Other' miles category; treating those as personal/other nonbusiness miles is consistent with the form's three-way split."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The Schedule C line 9 instructions allow the standard mileage rate only if the vehicle was owned and the rate was used in the first year, or leased and the rate is used for the entire lease period, and require actual expenses for five or more vehicles used together."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The restatement follows Schedule C line 9: standard mileage times business miles plus parking and tolls, or the business portion of actual operating expenses plus parking and tolls."
  - key: "20a"
    status: MISMATCH
    reason: "The IRS says 'enter on line 20a the business portion of your rental cost. But if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement omits the inclusion amount."
  - key: "(b)"
    status: MISMATCH
    reason: "Form 4562 Part V column (b) says 'Enter the date the property was placed in service'; the restatement asks only for the year."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a scope gate: the IRS text treats trade-ins, prior credits/clean-fuel basis adjustments, conversions, 50%-or-less use, and for-hire/ambulance/hearse vehicles as special cases, and the refusal names those exclusions."
  - key: "(d)"
    status: MATCH
    reason: "Column (d) asks for actual cost or other basis including sales tax, unadjusted for prior depreciation and not reduced by section 179, with the converted-property rule using the smaller of adjusted basis or fair market value."
  - key: "13"
    status: MATCH
    reason: "The Pub. 946 worksheet line 13 multiplies cost by the business/investment-use percentage; using business miles divided by total miles matches the Part V column (c) rule."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is the elected section 179 cost; the restatement asks for the amount elected, with zero if none, and the later section 179 refusal handles the limits."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The special depreciation allowance election is made by class of property for all such property placed in service during the tax year, so asking whether the choice is the same for all 5-year property is consistent."
  - key: "7"
    status: MATCH
    reason: "Worksheet line 7 is the maximum depreciation deduction from the appropriate table; for a 2025 vehicle that is the first-year limit, and for an earlier vehicle it is the limit for its 2025 recovery year."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says to multiply line 7 by the business/investment-use percentage, which the restatement does using business miles divided by total miles."
  - key: "10"
    status: MATCH
    reason: "Worksheet line 10 is the section 179 deduction claimed this year, not more than line 9, and zero if this is not the year the vehicle was placed in service."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 subtracts line 10 from line 9 to get the depreciation limit; adding a zero floor does not change a valid worksheet result."
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the section 179 deduction claimed in the year the vehicle was placed in service, which is line 10 for a 2025 vehicle and the prior-year input otherwise."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 subtracts line 14 from line 13 to get tentative basis for depreciation; the zero floor is harmless for valid inputs."
  - key: "16"
    status: MATCH
    reason: "Worksheet line 16 is the special depreciation allowance, and the restatement uses the 2025 allowance calculation or zero if not placed in service in 2025."
  - key: "25"
    status: MATCH
    reason: "Form 4562 line 25 reports the special depreciation allowance, and the passenger automobile limit caps the special allowance plus section 179 by line 11, so using the smaller of line 16 or line 11 is consistent."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 subtracts line 16 from line 11 to get the limit on MACRS depreciation; the zero floor is consistent with the worksheet's stopping rule."
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 subtracts line 16 from line 15 to get basis for depreciation; the zero floor is harmless because the special allowance cannot exceed line 15."
  - key: "19"
    status: MISMATCH
    reason: "For a 2019 vehicle, the IRS says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)' and permits deductions after the recovery period; the restatement returns zero for a 2019 vehicle."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20 says to enter the lesser of line 17 or line 19 as the MACRS depreciation deduction, which the restatement does."
```
