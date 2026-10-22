# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 556abe612f443001e62be3f6bfff49f1ab380b90d6d378ff8b3f5b3a4bd889a9 |
| subject sha256 | 75872f6f2e339c3b7481cda1c990456eb7b7d9d4e15ab5bc130fc2681f2a39f7 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 18 / 7 / 0 / 0 |
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

Model: Schedule C line 43 asks for a full date: "When did you place your vehicle in service for business purposes? (month/day/year)". The restatement takes only the year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 and Form 4562 from their own records. No value depends on the month or day except through the quarter, which is asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for the miles 'of the total number of miles you drove your vehicle during 2025' used for 'Business'. The restatement asks for the same.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles. The instructions describe commuting as 'travel between your home and a work location', which the restatement follows.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for 'Other' miles. The restatement asks for the other (personal) miles.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The screen follows the line 9 instructions. You may use the standard rate only if you 'Owned the vehicle and used the standard mileage rate for the first year' or 'Leased the vehicle and are using the standard mileage rate for the entire lease period'. You 'must use actual expenses if you used five or more vehicles simultaneously'.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Standard rate: business miles × 0.70 plus parking fees and tolls, as the instructions say. Actual expenses: 'the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.' Parking and tolls are added at 100% business use, which the 'etc.' allows. Depreciation and lease payments are kept off this line.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The program enters the business portion of the lease payments with no adjustment and no refusal. The instructions say 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'.

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ('an inclusion amount for leased property'), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Form 4562 column (b) says 'Enter the date the property was placed in service'; the restatement records only a year. The refusal for 50%-or-less use (line 27) is a proper narrowing.

Ruling: representation; restatement accepted. As line 43: the year chooses the recovery year and the limits, the quarter (asked separately) the mid-quarter table; the filer enters the full date on Form 4562 column (b).

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a gating question that narrows the tool to cases it supports. Each excluded case is named in the refusal on column (d).

### (d) — Cost or other basis
Status: **MATCH**

Model: The instructions say: 'Enter the property's actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)'. For a converted vehicle they say 'the smaller of the property's adjusted basis or its fair market value on the date of conversion'. The credit reductions are excluded by the screen.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13 says 'Multiply line 12 by line 8'. Line 12 equals column (d) because credits are screened out. Line 8, business-use percentage, is business miles divided by total miles, as column (c) directs.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) says 'Enter the amount you elect to expense for section 179 property'. The restatement asks for that amount.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class'. Refusing the case where the choice differs within the 5-year class is a valid narrowing.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Worksheet line 7 is the 'Maximum depreciation deduction for this year from the appropriate table'. The program uses Pub. 946 limits by year placed in service and year of recovery: $20,200 for 2025 with the special allowance, and footnote $12,200 without it.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says 'Multiply line 7 by line 8', where line 8 is the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile"] [helper "Placed in service in 2025" = false → helper "Zero"]

Model: Worksheet line 10 is the 'Section 179 deduction claimed this year (not more than line 9)'. The program uses the elected cost from column (i) and never applies the Form 4562 line 11 limit: 'The total cost you can deduct is limited to your taxable income from the active conduct of a trade or business'.

Ruling: owner's reading open (amb.2025.vehicle_s179_claimed, TASKS.md T-046); project retained pending the owner. Line 10 takes the section 179 cost elected for the vehicle. The two readings differ only when the business income limit (Form 4562 line 11) cuts the year's deduction; the basis is reduced by the whole election, the carryover included (Pub. 946 p. 20: on a disposition before the carryover is used 'you must add it back to the property's basis'), and the worksheet limits the year's depreciation by the same amount.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 says 'Subtract line 10 from line 9'.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. That is line 10 for a 2025 vehicle and the filer's input otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 says 'Subtract line 14 from line 13'.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16 is line 15 times the applicable percentage: 100% if acquired after January 19, 2025 unless 40% is elected, otherwise 40%. It is 'Enter -0- if this is not the year you placed the car in service ... or you elected not to claim'. The program assumes the vehicle is qualified property.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MISMATCH**

Restated: Enter the smaller of line 16 or line 11.

Model: The program applies the line 11 cap even when the vehicle is not subject to the passenger-automobile limits, and it does model such vehicles (helper 'Subject to the limits for passenger automobiles'). The instructions say the limit applies 'For any passenger automobile' and list 'Exception. The following vehicles are not considered passenger automobiles'. For those vehicles line 25 should not be capped by line 11.

Ruling: representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: the vehicle's special allowance (scveh.bonus_v) takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass, the passenger-automobile route. A vehicle that is not a passenger automobile is not limited.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 says 'Subtract line 16 from line 11'.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 says 'Subtract line 16 from line 15'.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: For a vehicle placed in service in 2019, the program enters zero with no refusal. The text says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)'. Pub. 946 says 'you can deduct that unrecovered basis after the recovery period ends'.

Ruling: representation; restatement accepted. Line 19 is a line of the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); Pub. 946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MISMATCH**

Restated: Enter the smaller of line 17 or line 19.

Model: The program caps line 20 at line 17 even when the vehicle is not a passenger automobile. The instructions limit only 'passenger automobiles' and exclude the listed vehicles ('are not considered passenger automobiles'). For those vehicles, line 19 depreciation should not be capped.

Ruling: representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: the vehicle's special allowance (scveh.bonus_v) takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass, the passenger-automobile route. A vehicle that is not a passenger automobile is not limited.

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "Schedule C line 43 asks for a full date: \"When did you place your vehicle in service for business purposes? (month/day/year)\". The restatement takes only the year."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for the miles 'of the total number of miles you drove your vehicle during 2025' used for 'Business'. The restatement asks for the same."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles. The instructions describe commuting as 'travel between your home and a work location', which the restatement follows."
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for 'Other' miles. The restatement asks for the other (personal) miles."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The screen follows the line 9 instructions. You may use the standard rate only if you 'Owned the vehicle and used the standard mileage rate for the first year' or 'Leased the vehicle and are using the standard mileage rate for the entire lease period'. You 'must use actual expenses if you used five or more vehicles simultaneously'."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Standard rate: business miles × 0.70 plus parking fees and tolls, as the instructions say. Actual expenses: 'the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.' Parking and tolls are added at 100% business use, which the 'etc.' allows. Depreciation and lease payments are kept off this line."
  - key: "20a"
    status: MISMATCH
    reason: "The program enters the business portion of the lease payments with no adjustment and no refusal. The instructions say 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'."
  - key: "(b)"
    status: MISMATCH
    reason: "Form 4562 column (b) says 'Enter the date the property was placed in service'; the restatement records only a year. The refusal for 50%-or-less use (line 27) is a proper narrowing."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a gating question that narrows the tool to cases it supports. Each excluded case is named in the refusal on column (d)."
  - key: "(d)"
    status: MATCH
    reason: "The instructions say: 'Enter the property's actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)'. For a converted vehicle they say 'the smaller of the property's adjusted basis or its fair market value on the date of conversion'. The credit reductions are excluded by the screen."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13 says 'Multiply line 12 by line 8'. Line 12 equals column (d) because credits are screened out. Line 8, business-use percentage, is business miles divided by total miles, as column (c) directs."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) says 'Enter the amount you elect to expense for section 179 property'. The restatement asks for that amount."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class'. Refusing the case where the choice differs within the 5-year class is a valid narrowing."
  - key: "7"
    status: MATCH
    reason: "Worksheet line 7 is the 'Maximum depreciation deduction for this year from the appropriate table'. The program uses Pub. 946 limits by year placed in service and year of recovery: $20,200 for 2025 with the special allowance, and footnote $12,200 without it."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says 'Multiply line 7 by line 8', where line 8 is the business-use percentage."
  - key: "10"
    status: MISMATCH
    reason: "Worksheet line 10 is the 'Section 179 deduction claimed this year (not more than line 9)'. The program uses the elected cost from column (i) and never applies the Form 4562 line 11 limit: 'The total cost you can deduct is limited to your taxable income from the active conduct of a trade or business'."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 says 'Subtract line 10 from line 9'."
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. That is line 10 for a 2025 vehicle and the filer's input otherwise."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 says 'Subtract line 14 from line 13'."
  - key: "16"
    status: MATCH
    reason: "Worksheet line 16 is line 15 times the applicable percentage: 100% if acquired after January 19, 2025 unless 40% is elected, otherwise 40%. It is 'Enter -0- if this is not the year you placed the car in service ... or you elected not to claim'. The program assumes the vehicle is qualified property."
  - key: "25"
    status: MISMATCH
    reason: "The program applies the line 11 cap even when the vehicle is not subject to the passenger-automobile limits, and it does model such vehicles (helper 'Subject to the limits for passenger automobiles'). The instructions say the limit applies 'For any passenger automobile' and list 'Exception. The following vehicles are not considered passenger automobiles'. For those vehicles line 25 should not be capped by line 11."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 says 'Subtract line 16 from line 11'."
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 says 'Subtract line 16 from line 15'."
  - key: "19"
    status: MISMATCH
    reason: "For a vehicle placed in service in 2019, the program enters zero with no refusal. The text says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)'. Pub. 946 says 'you can deduct that unrecovered basis after the recovery period ends'."
  - key: "20"
    status: MISMATCH
    reason: "The program caps line 20 at line 17 even when the vehicle is not a passenger automobile. The instructions limit only 'passenger automobiles' and exclude the listed vehicles ('are not considered passenger automobiles'). For those vehicles, line 19 depreciation should not be capped."
```
```
