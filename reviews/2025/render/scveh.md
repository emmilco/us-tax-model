# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c310f8dc89328aeda8eb7f8a72246e18d1cc12386eb9d2d9d274315bb0504f5f |
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

Model: The form asks for the full date the vehicle was placed in service: "When did you place your vehicle in service for business purposes? (month/day/year)". The restatement asks only for the year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 and Form 4562 from their own records. No value depends on the month or day except through the quarter, which is asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for the miles you used the vehicle for business out of the total miles driven in 2025. The restatement asks for 2025 business miles, not counting commuting.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles. The instructions say "commuting is travel between your home and a work location", and the restatement points to that definition.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for other miles. The restatement asks for the other (personal) miles driven in 2025.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: This tracks the rule that you can use the standard mileage rate only if you "Owned the vehicle and used the standard mileage rate for the first year" or "Leased the vehicle and are using the standard mileage rate for the entire lease period". It also tracks the rule that you must use actual expenses "if you used five or more vehicles simultaneously".

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: The standard branch multiplies business miles by 0.70 and adds parking fees and tolls, as the instructions say. The actual branch takes the business portion of operating expenses (gasoline, oil, repairs, insurance, license plates, etc.) and leaves depreciation and lease payments for other lines. Adding business parking and tolls under actual expenses fits within "etc."

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement takes the business portion of the lease payments but leaves out the reduction the instructions require: "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount." No refusal covers this case.

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ('an inclusion amount for leased property'), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Column (b) instructions say "Enter the date the property was placed in service", but the restatement asks only for a year. The refusal for 50%-or-less use correctly sends that case to line 27, but the printed entry is still a year, not a date.

Ruling: representation; restatement accepted. As line 43: the year chooses the recovery year and the limits, the quarter (asked separately) the mid-quarter table; the filer enters the full date on Form 4562 column (b).

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope screen. Its items match cases the text treats specially: trade-ins ("special rules apply"), EV and alternative motor vehicle credits (which reduce basis), dispositions, earlier 50%-or-less use, and vehicles for hire or ambulances and hearses ("not considered passenger automobiles").

### (d) — Cost or other basis
Status: **MISMATCH**

Restated: Input — The vehicle's cost (including sales tax) or other basis, not reduced by any section 179 deduction or depreciation

Model: The restatement matches "actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)", but it leaves out the rule for converted vehicles: "If you converted the property from personal use to business/investment use, your basis for depreciation is the smaller of the property's adjusted basis or its fair market value on the date of conversion." The screen does not exclude conversions.

Ruling: fixed; restatement now matches. The cost question now says that for a vehicle converted from personal use the basis is the smaller of its adjusted basis or its fair market value on the date of conversion (i4562, Column (d)), as the property question already did.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13 says "Multiply line 12 by line 8": cost times the business-use percentage. Column (c) defines that percentage as business miles (not commuting) divided by total miles, which is what the restatement computes.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is "the amount you elect to expense for section 179 property used more than 50% in a qualified business use". The 50%-or-less case is refused, and the separate section 179 refusal covers amounts over the business cost or the $31,300 SUV limit.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies "for any class of property ... for all such property in such class placed in service during the tax year". The screen limits the tool to a single choice across the 5-year class and refuses mixed choices.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The 2025 amounts ($20,200 with the special allowance, $12,200 without) and the earlier-year amounts match the tables. But line 7 always applies the passenger-automobile limit, even when the filer says the vehicle is not a passenger automobile. The text says the limits apply "For any passenger automobile", and those vehicles have no refusal.

Ruling: representation; restatement accepted. Line 7 is a line of the Pub. 946 worksheet for passenger automobiles and is shown for every vehicle, but it limits only a passenger automobile: for a vehicle that is not one, the special allowance, the section 179 deduction and MACRS take the scveh.passenger = false branches, which do not read it (checked: a $60,000 truck placed in service in 2025 with the 100% allowance gets $60,000, a passenger automobile $20,200).

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says "Multiply line 7 by line 8". Line 8 is the business-use percentage, figured from miles.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10 is "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service". The restatement does the same: column (i), capped at line 9, and zero for earlier years.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 says "Subtract line 10 from line 9."

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the "Section 179 deduction claimed in the year you placed the car in service". For a 2025 vehicle that is line 10; for an earlier vehicle it is the amount claimed in the year placed in service.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 says "Subtract line 14 from line 13."

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16 multiplies line 15 by the applicable percentage and enters zero if the vehicle was not placed in service this year or you elected out. The percentages match the instructions: 100% if acquired after January 19, 2025, the elective 40%, or 40% if acquired earlier.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Line 25 is "included in the overall limit", and the worksheet note says "If line 16 is equal to line 11, stop here ... limited to the amount on line 11". For one vehicle, the smaller of line 16 and line 11 follows from this.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 says "Subtract line 16 from line 11."

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 says "Subtract line 16 from line 15."

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: The 2025 half-year and mid-quarter branches match "Multiply line 18 by line 6". But a 2019 vehicle (not refused) gets zero, and the instructions say "If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)", subject to the yearly limit (Pub. 946, Deductions After the Recovery Period). No refusal names this case.

Ruling: representation; restatement accepted. Line 19 is a line of the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); Pub. 946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20 says "Enter the lesser of line 17 or line 19."

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The form asks for the full date the vehicle was placed in service: \"When did you place your vehicle in service for business purposes? (month/day/year)\". The restatement asks only for the year."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for the miles you used the vehicle for business out of the total miles driven in 2025. The restatement asks for 2025 business miles, not counting commuting."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles. The instructions say \"commuting is travel between your home and a work location\", and the restatement points to that definition."
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for other miles. The restatement asks for the other (personal) miles driven in 2025."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "This tracks the rule that you can use the standard mileage rate only if you \"Owned the vehicle and used the standard mileage rate for the first year\" or \"Leased the vehicle and are using the standard mileage rate for the entire lease period\". It also tracks the rule that you must use actual expenses \"if you used five or more vehicles simultaneously\"."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The standard branch multiplies business miles by 0.70 and adds parking fees and tolls, as the instructions say. The actual branch takes the business portion of operating expenses (gasoline, oil, repairs, insurance, license plates, etc.) and leaves depreciation and lease payments for other lines. Adding business parking and tolls under actual expenses fits within \"etc.\""
  - key: "20a"
    status: MISMATCH
    reason: "The restatement takes the business portion of the lease payments but leaves out the reduction the instructions require: \"if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.\" No refusal covers this case."
  - key: "(b)"
    status: MISMATCH
    reason: "Column (b) instructions say \"Enter the date the property was placed in service\", but the restatement asks only for a year. The refusal for 50%-or-less use correctly sends that case to line 27, but the printed entry is still a year, not a date."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a scope screen. Its items match cases the text treats specially: trade-ins (\"special rules apply\"), EV and alternative motor vehicle credits (which reduce basis), dispositions, earlier 50%-or-less use, and vehicles for hire or ambulances and hearses (\"not considered passenger automobiles\")."
  - key: "(d)"
    status: MISMATCH
    reason: "The restatement matches \"actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)\", but it leaves out the rule for converted vehicles: \"If you converted the property from personal use to business/investment use, your basis for depreciation is the smaller of the property's adjusted basis or its fair market value on the date of conversion.\" The screen does not exclude conversions."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13 says \"Multiply line 12 by line 8\": cost times the business-use percentage. Column (c) defines that percentage as business miles (not commuting) divided by total miles, which is what the restatement computes."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is \"the amount you elect to expense for section 179 property used more than 50% in a qualified business use\". The 50%-or-less case is refused, and the separate section 179 refusal covers amounts over the business cost or the $31,300 SUV limit."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies \"for any class of property ... for all such property in such class placed in service during the tax year\". The screen limits the tool to a single choice across the 5-year class and refuses mixed choices."
  - key: "7"
    status: MISMATCH
    reason: "The 2025 amounts ($20,200 with the special allowance, $12,200 without) and the earlier-year amounts match the tables. But line 7 always applies the passenger-automobile limit, even when the filer says the vehicle is not a passenger automobile. The text says the limits apply \"For any passenger automobile\", and those vehicles have no refusal."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says \"Multiply line 7 by line 8\". Line 8 is the business-use percentage, figured from miles."
  - key: "10"
    status: MATCH
    reason: "Worksheet line 10 is \"Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service\". The restatement does the same: column (i), capped at line 9, and zero for earlier years."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 says \"Subtract line 10 from line 9.\""
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the \"Section 179 deduction claimed in the year you placed the car in service\". For a 2025 vehicle that is line 10; for an earlier vehicle it is the amount claimed in the year placed in service."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 says \"Subtract line 14 from line 13.\""
  - key: "16"
    status: MATCH
    reason: "Worksheet line 16 multiplies line 15 by the applicable percentage and enters zero if the vehicle was not placed in service this year or you elected out. The percentages match the instructions: 100% if acquired after January 19, 2025, the elective 40%, or 40% if acquired earlier."
  - key: "25"
    status: MATCH
    reason: "Line 25 is \"included in the overall limit\", and the worksheet note says \"If line 16 is equal to line 11, stop here ... limited to the amount on line 11\". For one vehicle, the smaller of line 16 and line 11 follows from this."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 says \"Subtract line 16 from line 11.\""
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 says \"Subtract line 16 from line 15.\""
  - key: "19"
    status: MISMATCH
    reason: "The 2025 half-year and mid-quarter branches match \"Multiply line 18 by line 6\". But a 2019 vehicle (not refused) gets zero, and the instructions say \"If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)\", subject to the yearly limit (Pub. 946, Deductions After the Recovery Period). No refusal names this case."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20 says \"Enter the lesser of line 17 or line 19.\""
```
