# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5c0d417a5a58db0e2b9ff7dc19e55e4354f168bf31163527aaf3ad087472cd47 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e4a476216010971db277688a7525749a0ff50e66d84fa94b8e75f6de593ef333 |
| lines judged | 27 |
| match / mismatch / unclear / missing | 23 / 4 / 0 / 0 |
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

Model: Schedule C line 43 asks for a full date: "When did you place your vehicle in service for business purposes? (month/day/year)". The restatement collects only the year (a Count), so the printed entry would lack the month and day.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks, of the total miles driven during 2025, for the miles used for "Business". The restatement's business (non-commuting) miles for 2025 matches.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles. The instructions define commuting as "travel between your home and a work location", which the restatement follows.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for "Other" miles. The restatement's other (personal) 2025 miles matches.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The line 9 instructions allow the standard mileage rate only if you "Owned the vehicle and used the standard mileage rate for the first year" or "Leased the vehicle and are using the standard mileage rate for the entire lease period". They require actual expenses "if you used five or more vehicles simultaneously". The question covers all three conditions.

### (screen) (scveh.employee_use) — Your employees use this vehicle for personal purposes
Status: **MATCH**

Model: The column (c) instructions treat employee-used vehicles "as being used 100% for business/investment purposes if the value of personal use is included in the employees' gross income, or the employees reimburse the employer". The question states this rule correctly.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Standard method: business miles × 0.70 plus parking fees and tolls, as in "Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls". Actual method: the business portion of gasoline, oil, repairs, insurance, license plates, etc.; parking and tolls are wholly business expenses. The mileage-ratio business share matches Form 4562 column (c).

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: This supports the rule "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle". The rule is enforced by the lease_smr_bad refusal.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the full business portion of the lease payments and has no refusal for long leases. The instructions add: "But if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount."

Ruling: scope; refusal located elsewhere, restatement accepted. i1040sc line 20a, "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount": sc.special refuses "an inclusion amount for leased property" for the business, read for every Schedule C (the wording is unchanged by this package; checked in forms/2025/sc.yaml).

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Form 4562 column (b) says "Enter the date the property was placed in service". The restatement collects only the year (2019–2025), so the printed entry is not the date. The low-use refusal for line 27 property is otherwise correct.

Ruling: representation; restatement accepted. i4562 p. 14, Column (b), "Enter the date the property was placed in service": the tool needs the year (and the quarter, asked separately, for 2025 property); the filer writes the date from their records.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The listed items track exclusions and special rules in the text: trade-ins, ADS, listed property used 50% or less, 168(k)(9) property, casualty basis reductions that end use of the tables, short tax years, the lessor exception, and the records requirement. Routing these vehicles out of the tool is a valid narrowing.

### (d) — Cost or other basis
Status: **MATCH**

Model: This matches "actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)" and, for converted property, "the smaller of the property's adjusted basis or its fair market value on the date of conversion". Credit reductions and the other excluded cases are refused.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13 says "Multiply line 12 by line 8": cost or other basis times the business-use percentage. Column (c) defines that percentage as business miles divided by total miles.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is "the amount you elect to expense for section 179 property". The over-business-cost and $31,300 SUV limits are enforced by the s179_bad refusal, and the passenger-automobile cap is applied on line 10.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The text says the election out applies "for any class of property ... for all such property in such class placed in service during the tax year". Asking whether the choice is uniform across the 5-year class, and refusing mixed choices, is a valid narrowing.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The restatement always uses the passenger-automobile table, including for vehicles the program treats as not subject to the limits (passenger = false). The text says "For any passenger automobile ... cannot exceed the applicable limit", and heavier vehicles are not passenger automobiles. Because of this, lines 11, 17, 20 and 25 also cap non-passenger vehicles. For passenger automobiles, the values are correct: $20,200 with the special allowance or $12,200 without for a 2025 vehicle, and the year-of-recovery entry for earlier vehicles.

Ruling: representation; restatement accepted. The worksheet line is figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass); a vehicle that is not a passenger automobile takes lines 16 and 19 directly (scveh.bonus_o, scveh.macrs_heavy), checked earlier by evaluation on stage14.veh.suv_179 with passenger answered both ways.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says "Multiply line 7 by line 8". The restatement multiplies line 7 by the business-use percentage (business miles over total miles).

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10 is "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service." The restatement applies the line 9 cap to passenger automobiles.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 says "Subtract line 10 from line 9".

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the "Section 179 deduction claimed in the year you placed the car in service". For a 2025 vehicle that is this year's deduction (line 10); for earlier vehicles it is the input amount.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 says "Subtract line 14 from line 13".

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16 is line 15 times the applicable percentage, or -0- if not the year placed in service or the allowance is elected out. The percentages match: 100% if acquired after January 19, 2025 (40% if elected), and 40% if acquired after September 27, 2017 and before January 20, 2025.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Per the worksheet note, the special allowance is "limited to the amount on line 11", so the lesser of line 16 and line 11 is the per-vehicle Form 4562 line 25 amount for a passenger automobile.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 says "Subtract line 16 from line 11".

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 says "Subtract line 16 from line 15".

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Worksheet line 19 says "Multiply line 18 by line 6", using the table rate. The rate convention is half-year, or mid-quarter when fourth-quarter bases exceed 40% of the year's bases; 5×Q4 > 2×total is the same test. Bases are after section 179 and before the special allowance. A 2019 vehicle has no 2025 rate, so the result is zero.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20 says "Enter the lesser of line 17 or line 19".

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "Schedule C line 43 asks for a full date: \"When did you place your vehicle in service for business purposes? (month/day/year)\". The restatement collects only the year (a Count), so the printed entry would lack the month and day."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks, of the total miles driven during 2025, for the miles used for \"Business\". The restatement's business (non-commuting) miles for 2025 matches."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles. The instructions define commuting as \"travel between your home and a work location\", which the restatement follows."
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for \"Other\" miles. The restatement's other (personal) 2025 miles matches."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The line 9 instructions allow the standard mileage rate only if you \"Owned the vehicle and used the standard mileage rate for the first year\" or \"Leased the vehicle and are using the standard mileage rate for the entire lease period\". They require actual expenses \"if you used five or more vehicles simultaneously\". The question covers all three conditions."
  - key: "(screen) (scveh.employee_use)"
    status: MATCH
    reason: "The column (c) instructions treat employee-used vehicles \"as being used 100% for business/investment purposes if the value of personal use is included in the employees' gross income, or the employees reimburse the employer\". The question states this rule correctly."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Standard method: business miles × 0.70 plus parking fees and tolls, as in \"Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls\". Actual method: the business portion of gasoline, oil, repairs, insurance, license plates, etc.; parking and tolls are wholly business expenses. The mileage-ratio business share matches Form 4562 column (c)."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "This supports the rule \"You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle\". The rule is enforced by the lease_smr_bad refusal."
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the full business portion of the lease payments and has no refusal for long leases. The instructions add: \"But if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.\""
  - key: "(b)"
    status: MISMATCH
    reason: "Form 4562 column (b) says \"Enter the date the property was placed in service\". The restatement collects only the year (2019–2025), so the printed entry is not the date. The low-use refusal for line 27 property is otherwise correct."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The listed items track exclusions and special rules in the text: trade-ins, ADS, listed property used 50% or less, 168(k)(9) property, casualty basis reductions that end use of the tables, short tax years, the lessor exception, and the records requirement. Routing these vehicles out of the tool is a valid narrowing."
  - key: "(d)"
    status: MATCH
    reason: "This matches \"actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)\" and, for converted property, \"the smaller of the property's adjusted basis or its fair market value on the date of conversion\". Credit reductions and the other excluded cases are refused."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13 says \"Multiply line 12 by line 8\": cost or other basis times the business-use percentage. Column (c) defines that percentage as business miles divided by total miles."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is \"the amount you elect to expense for section 179 property\". The over-business-cost and $31,300 SUV limits are enforced by the s179_bad refusal, and the passenger-automobile cap is applied on line 10."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The text says the election out applies \"for any class of property ... for all such property in such class placed in service during the tax year\". Asking whether the choice is uniform across the 5-year class, and refusing mixed choices, is a valid narrowing."
  - key: "7"
    status: MISMATCH
    reason: "The restatement always uses the passenger-automobile table, including for vehicles the program treats as not subject to the limits (passenger = false). The text says \"For any passenger automobile ... cannot exceed the applicable limit\", and heavier vehicles are not passenger automobiles. Because of this, lines 11, 17, 20 and 25 also cap non-passenger vehicles. For passenger automobiles, the values are correct: $20,200 with the special allowance or $12,200 without for a 2025 vehicle, and the year-of-recovery entry for earlier vehicles."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says \"Multiply line 7 by line 8\". The restatement multiplies line 7 by the business-use percentage (business miles over total miles)."
  - key: "10"
    status: MATCH
    reason: "Worksheet line 10 is \"Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service.\" The restatement applies the line 9 cap to passenger automobiles."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 says \"Subtract line 10 from line 9\"."
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the \"Section 179 deduction claimed in the year you placed the car in service\". For a 2025 vehicle that is this year's deduction (line 10); for earlier vehicles it is the input amount."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 says \"Subtract line 14 from line 13\"."
  - key: "16"
    status: MATCH
    reason: "Worksheet line 16 is line 15 times the applicable percentage, or -0- if not the year placed in service or the allowance is elected out. The percentages match: 100% if acquired after January 19, 2025 (40% if elected), and 40% if acquired after September 27, 2017 and before January 20, 2025."
  - key: "25"
    status: MATCH
    reason: "Per the worksheet note, the special allowance is \"limited to the amount on line 11\", so the lesser of line 16 and line 11 is the per-vehicle Form 4562 line 25 amount for a passenger automobile."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 says \"Subtract line 16 from line 11\"."
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 says \"Subtract line 16 from line 15\"."
  - key: "19"
    status: MATCH
    reason: "Worksheet line 19 says \"Multiply line 18 by line 6\", using the table rate. The rate convention is half-year, or mid-quarter when fourth-quarter bases exceed 40% of the year's bases; 5×Q4 > 2×total is the same test. Bases are after section 179 and before the special allowance. A 2019 vehicle has no 2025 rate, so the result is zero."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20 says \"Enter the lesser of line 17 or line 19\"."
```
```
