# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b3ca3da9b87b5ea518884eac7a311833d04c9b6d396e0fe78e80d022c7650541 |
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

Model: Schedule C line 43 asks for a full date: "When did you place your vehicle in service for business purposes? (month/day/year)". The restatement collects only the year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 and Form 4562 from their own records. No value depends on the month or day except through the quarter, which is asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for the miles you used the vehicle for "Business" during 2025, which is what the restatement collects.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles, and the instructions define commuting as "travel between your home and a work location."

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for the "Other" miles driven in 2025.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: This tracks the instructions: you can use the standard mileage rate only if you "Owned the vehicle and used the standard mileage rate for the first year" or "Leased the vehicle and are using the standard mileage rate for the entire lease period," and you "must use actual expenses if you used five or more vehicles simultaneously."

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Standard rate: business miles × 0.70 plus parking fees and tolls. Actual: the business portion of gasoline, oil, repairs, insurance, license plates and similar costs, with depreciation and lease payments kept off line 9, as the instructions direct.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the business portion of the lease payments but never applies the inclusion amount. The instructions say "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount." No refusal covers this case.

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ('an inclusion amount for leased property'), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Form 4562 column (b) says "Enter the date the property was placed in service." The restatement records only the year. The refusal for 50%-or-less use (line 27, ADS) is otherwise appropriate.

Ruling: representation; restatement accepted. As line 43: the year chooses the recovery year and the limits, the quarter (asked separately) the mid-quarter table; the filer enters the full date on Form 4562 column (b).

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This screen keeps out cases the text treats specially: trade-ins, conversions, credit reductions to basis, special allowances or the standard mileage rate in earlier years, dispositions, vehicles that are not passenger automobiles (for hire, ambulance or hearse), and pre-2019 vehicles. That is a valid narrowing of the tool.

### (d) — Cost or other basis
Status: **MATCH**

Model: Column (d) is the "actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)," or for a converted vehicle "the smaller of the property's adjusted basis or its fair market value." Pub. 946 says not to reduce it by section 179. The refusals cover the excluded cases.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: This is worksheet line 13: "Multiply line 12 by line 8," where the business-use percentage is business miles divided by total miles.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is "the amount you elect to expense for section 179 property," with the SUV limit of $31,300 handled by a refusal.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies "for any class of property ... for all such property in such class." Requiring the same choice across the 5-year class is a valid narrowing.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The passenger automobile table limit ($20,200 or $12,200 for 2025, and later-year amounts) is applied to every vehicle. The text says the limits apply only to passenger automobiles "rated at 6,000 pounds unloaded gross vehicle weight or less," yet the program applies them even when its own passenger question is No. Those vehicles then get limited special allowance and MACRS amounts.

Ruling: representation; project retained. The automobile worksheet, line 7 included, is figured for every vehicle but read only for a passenger automobile: the vehicle's special allowance (scveh.bonus_v) takes the worksheet's limited figure only when scveh.passenger is true and line 16 otherwise, and column (h) takes the worksheet's line 20 only through scveh.macrs_pass, the passenger-automobile route. A vehicle that is not a passenger automobile is not limited.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9: "Multiply line 7 by line 8."

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile"] [helper "Placed in service in 2025" = false → helper "Zero"]

Model: The worksheet asks for the "Section 179 deduction claimed this year (not more than line 9)." The program uses the elected cost from column (i). The deduction claimed can be smaller because "The total cost you can deduct is limited to your taxable income from the active conduct of a trade or business" (Form 4562 line 11), and no refusal covers that limit.

Ruling: agent reading recorded for the owner (amb.2025.vehicle_s179_claimed, TASKS.md T-046); project retained. Line 10 takes the section 179 cost elected for the vehicle. The two readings differ only when the business income limit (Form 4562 line 11) cuts the year's deduction; the basis is reduced by the whole election, the carryover included (Pub. 946 p. 20: on a disposition before the carryover is used 'you must add it back to the property's basis'), and the worksheet limits the year's depreciation by the same amount.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11: "Subtract line 10 from line 9."

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14: "Section 179 deduction claimed in the year you placed the car in service." That is line 10 for a 2025 vehicle and the prior-year amount otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15: "Subtract line 14 from line 13."

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Line 15 times the applicable percentage: 100% if acquired after January 19, 2025, 40% if elected or acquired earlier, and "-0- if this is not the year you placed the car in service ... or you elected not to claim."

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: The worksheet note limits the special allowance to line 11 ("If line 16 is equal to line 11, stop here"), so the smaller of 16 or 11 is correct for passenger automobiles. The non-passenger problem comes from line 7.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17: "Subtract line 16 from line 11."

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18: "Subtract line 16 from line 15."

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: A vehicle placed in service in 2019 gets zero. The text says "If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)," and Pub. 946 says "you can deduct that unrecovered basis after the recovery period ends," up to the year's limit. No refusal covers this case.

Ruling: representation; restatement accepted. Line 19 is a line of the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); Pub. 946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20: "Enter the lesser of line 17 or line 19."

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "Schedule C line 43 asks for a full date: \"When did you place your vehicle in service for business purposes? (month/day/year)\". The restatement collects only the year."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for the miles you used the vehicle for \"Business\" during 2025, which is what the restatement collects."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles, and the instructions define commuting as \"travel between your home and a work location.\""
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for the \"Other\" miles driven in 2025."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "This tracks the instructions: you can use the standard mileage rate only if you \"Owned the vehicle and used the standard mileage rate for the first year\" or \"Leased the vehicle and are using the standard mileage rate for the entire lease period,\" and you \"must use actual expenses if you used five or more vehicles simultaneously.\""
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Standard rate: business miles × 0.70 plus parking fees and tolls. Actual: the business portion of gasoline, oil, repairs, insurance, license plates and similar costs, with depreciation and lease payments kept off line 9, as the instructions direct."
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the business portion of the lease payments but never applies the inclusion amount. The instructions say \"if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.\" No refusal covers this case."
  - key: "(b)"
    status: MISMATCH
    reason: "Form 4562 column (b) says \"Enter the date the property was placed in service.\" The restatement records only the year. The refusal for 50%-or-less use (line 27, ADS) is otherwise appropriate."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This screen keeps out cases the text treats specially: trade-ins, conversions, credit reductions to basis, special allowances or the standard mileage rate in earlier years, dispositions, vehicles that are not passenger automobiles (for hire, ambulance or hearse), and pre-2019 vehicles. That is a valid narrowing of the tool."
  - key: "(d)"
    status: MATCH
    reason: "Column (d) is the \"actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation),\" or for a converted vehicle \"the smaller of the property's adjusted basis or its fair market value.\" Pub. 946 says not to reduce it by section 179. The refusals cover the excluded cases."
  - key: "13"
    status: MATCH
    reason: "This is worksheet line 13: \"Multiply line 12 by line 8,\" where the business-use percentage is business miles divided by total miles."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is \"the amount you elect to expense for section 179 property,\" with the SUV limit of $31,300 handled by a refusal."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies \"for any class of property ... for all such property in such class.\" Requiring the same choice across the 5-year class is a valid narrowing."
  - key: "7"
    status: MISMATCH
    reason: "The passenger automobile table limit ($20,200 or $12,200 for 2025, and later-year amounts) is applied to every vehicle. The text says the limits apply only to passenger automobiles \"rated at 6,000 pounds unloaded gross vehicle weight or less,\" yet the program applies them even when its own passenger question is No. Those vehicles then get limited special allowance and MACRS amounts."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9: \"Multiply line 7 by line 8.\""
  - key: "10"
    status: MISMATCH
    reason: "The worksheet asks for the \"Section 179 deduction claimed this year (not more than line 9).\" The program uses the elected cost from column (i). The deduction claimed can be smaller because \"The total cost you can deduct is limited to your taxable income from the active conduct of a trade or business\" (Form 4562 line 11), and no refusal covers that limit."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11: \"Subtract line 10 from line 9.\""
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14: \"Section 179 deduction claimed in the year you placed the car in service.\" That is line 10 for a 2025 vehicle and the prior-year amount otherwise."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15: \"Subtract line 14 from line 13.\""
  - key: "16"
    status: MATCH
    reason: "Line 15 times the applicable percentage: 100% if acquired after January 19, 2025, 40% if elected or acquired earlier, and \"-0- if this is not the year you placed the car in service ... or you elected not to claim.\""
  - key: "25"
    status: MATCH
    reason: "The worksheet note limits the special allowance to line 11 (\"If line 16 is equal to line 11, stop here\"), so the smaller of 16 or 11 is correct for passenger automobiles. The non-passenger problem comes from line 7."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17: \"Subtract line 16 from line 11.\""
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18: \"Subtract line 16 from line 15.\""
  - key: "19"
    status: MISMATCH
    reason: "A vehicle placed in service in 2019 gets zero. The text says \"If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h),\" and Pub. 946 says \"you can deduct that unrecovered basis after the recovery period ends,\" up to the year's limit. No refusal covers this case."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20: \"Enter the lesser of line 17 or line 19.\""
```
```
