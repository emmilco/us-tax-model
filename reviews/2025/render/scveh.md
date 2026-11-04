# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fca791ca88a08e3788c1c72c0e83aea2e256f2ecb27cede0cb2db8a45809a55a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7abd522bb45beed38ca4fc7a89f8396f00d00202ca111a9ed0ef64d93db512cb |
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
| p946 | For use in preparing 2025 returns | 17, 31, 32, 34, 37, 39, 41, 59, 60, 61, 62, 63, 71, 72, 73, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: The program asks only for the year (for example 2023). Schedule C line 43 asks for a full date: "When did you place your vehicle in service for business purposes? (month/day/year)".

Ruling: representation; same as the earlier ruling (restatement and objection unchanged). The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 from their own records.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for the miles of 2025 business use. Form 4562 column (c) instructions exclude commuting from business miles.

### 44b — Commuting miles
Status: **MATCH**

Model: Line 44b asks for commuting miles. The instructions define commuting as travel between home and a work location, and the restatement refers to them.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for the other miles driven in 2025, and the restatement asks the same.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The question follows the line 9 instructions. The standard rate requires owning the vehicle and using the rate in its first year, or leasing it and using the rate for the entire lease. Actual expenses are required with five or more vehicles used simultaneously.

### (screen) (scveh.employee_use) — Your employees use this vehicle for personal purposes
Status: **MATCH**

Model: This follows the Form 4562 column (c) text. Vehicles used by employees are treated as 100% business use if the value of personal use is included in the employees' gross income or the employees reimburse the employer.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: The standard case is business miles × 0.70 plus parking fees and tolls, as the instructions and Notice 2025-5 say. The actual case is the business portion (business miles ÷ total miles) of operating expenses, the instructions' "business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.", plus business parking and tolls. Excluded cases are refused.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: This tracks "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle." The program refuses that case.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MATCH**

Model: Line 20a takes "the business portion of your rental cost" when actual expenses are used. Under the standard rate, lease payments are not deducted. Pub. 946 says to report the lease inclusion amount as other income on the same schedule, not on this line.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: The program records only a year. Form 4562 column (b) instructions say "Enter the date the property was placed in service." The low-use refusal properly excludes vehicles reported on line 27.

Ruling: representation; same as the earlier ruling. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; no value depends on the month or day except through the quarter, asked separately.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The excluded cases match the IRS text. They include trade-ins, ADS, the listed-property exclusions, the qualified-business-use exclusions, the special-allowance exceptions, the casualty basis adjustment, short tax years, leasing and recordkeeping. Each falls outside what the program computes and is refused.

### (d) — Cost or other basis
Status: **MATCH**

Model: This matches column (d): "actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)". A converted vehicle uses the smaller of adjusted basis or FMV. Vehicle-credit reductions and trade-ins are refused through the screen.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Pub. 946 worksheet line 13 says "Multiply line 12 by line 8": cost times the business-use percentage. For vehicles that percentage is business miles divided by total miles.

### (i) — Elected section 179 cost
Status: **MISMATCH**

Restated: Input — The amount of this vehicle's cost you elect to expense under section 179 (zero if none)

Model: The program prints the raw election. It is not limited to the passenger automobile cap and is not set to zero for a vehicle placed in service before 2025. Column (i) is the amount elected "(subject to the limits for passenger automobiles)". Section 179 applies only to property "placed in service during the tax year".

Ruling: finding (low); the model says the printed column (i) is the raw election, not limited for a passenger automobile and not zero for an earlier vehicle. i4562 p. 16, Column (i): "Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use (subject to the limits for passenger automobiles)"; p946 worksheet line 10, "(not more than line 9)". The deduction is capped (scveh.line10 is the smaller of the election and line 9, and scveh.s179_2025 reads line 10), but the column (i) input is displayed as answered, so a passenger automobile whose election exceeds line 9 shows more in column (i) than it deducts; scveh.s179_bad refuses only an election above the business cost or the SUV limit. No tax amount differs. The earlier-vehicle part is not reachable: the election is read only for a 2025 vehicle (fixture stage14.veh.heavy_2019 completes without it). See `.transcription/proposed/rf/scveh.findings.md`, Low.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The i4562 election out applies "for any class of property ... for all such property in such class". A choice that differs within the 5-year class is refused.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Worksheet line 7 is the maximum deduction from the Pub. 946 table. For a 2025 vehicle that is $20,200 with the special allowance and $12,200 without it (footnote 1). Earlier vehicles use their year-of-recovery entry.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says "Multiply line 7 by line 8", and line 8 is the business-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10 is the "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service". The program follows this.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 says "Subtract line 10 from line 9."

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the section 179 deduction claimed in the year placed in service. For a 2025 vehicle that is line 10; otherwise the earlier year's amount is entered.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 says "Subtract line 14 from line 13."

### 16 — Special depreciation allowance
Status: **MATCH**

Model: The program multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025 (or 40% if elected), and 40% if acquired earlier. It enters -0- if the vehicle was not placed in service this year or the allowance is elected out, as i4562 line 14 and the worksheet say.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MISMATCH**

Restated: Enter the smaller of line 16 or line 11.

Model: The program prints line 25 only for passenger automobiles under the limits. A listed-property vehicle outside the limits, such as a heavier SUV, with a special allowance gets no line 25. Line 25 says "Enter on line 25 your total special depreciation allowance for all qualified listed property", and listed property includes "SUVs".

Ruling: representation; same as the earlier ruling (restatement and objection unchanged). The vehicle's special allowance (scveh.bonus_v) takes line 25 only for a passenger automobile under the limits and line 16 otherwise; a vehicle that is not a passenger automobile is not limited.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 says "Subtract line 16 from line 11."

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 says "Subtract line 16 from line 15."

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Worksheet line 19 says "Multiply line 18 by line 6", the table rate for 5-year property under the applicable convention. The program's mid-quarter test uses bases after section 179 and before the special allowance, as Pub. 946 says. Line 19 is zero after the recovery period, where the table gives no rate.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20 says "Enter the lesser of line 17 or line 19."

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The program asks only for the year (for example 2023). Schedule C line 43 asks for a full date: \"When did you place your vehicle in service for business purposes? (month/day/year)\"."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for the miles of 2025 business use. Form 4562 column (c) instructions exclude commuting from business miles."
  - key: "44b"
    status: MATCH
    reason: "Line 44b asks for commuting miles. The instructions define commuting as travel between home and a work location, and the restatement refers to them."
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for the other miles driven in 2025, and the restatement asks the same."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The question follows the line 9 instructions. The standard rate requires owning the vehicle and using the rate in its first year, or leasing it and using the rate for the entire lease. Actual expenses are required with five or more vehicles used simultaneously."
  - key: "(screen) (scveh.employee_use)"
    status: MATCH
    reason: "This follows the Form 4562 column (c) text. Vehicles used by employees are treated as 100% business use if the value of personal use is included in the employees' gross income or the employees reimburse the employer."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The standard case is business miles × 0.70 plus parking fees and tolls, as the instructions and Notice 2025-5 say. The actual case is the business portion (business miles ÷ total miles) of operating expenses, the instructions' \"business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.\", plus business parking and tolls. Excluded cases are refused."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "This tracks \"You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.\" The program refuses that case."
  - key: "20a"
    status: MATCH
    reason: "Line 20a takes \"the business portion of your rental cost\" when actual expenses are used. Under the standard rate, lease payments are not deducted. Pub. 946 says to report the lease inclusion amount as other income on the same schedule, not on this line."
  - key: "(b)"
    status: MISMATCH
    reason: "The program records only a year. Form 4562 column (b) instructions say \"Enter the date the property was placed in service.\" The low-use refusal properly excludes vehicles reported on line 27."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The excluded cases match the IRS text. They include trade-ins, ADS, the listed-property exclusions, the qualified-business-use exclusions, the special-allowance exceptions, the casualty basis adjustment, short tax years, leasing and recordkeeping. Each falls outside what the program computes and is refused."
  - key: "(d)"
    status: MATCH
    reason: "This matches column (d): \"actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)\". A converted vehicle uses the smaller of adjusted basis or FMV. Vehicle-credit reductions and trade-ins are refused through the screen."
  - key: "13"
    status: MATCH
    reason: "Pub. 946 worksheet line 13 says \"Multiply line 12 by line 8\": cost times the business-use percentage. For vehicles that percentage is business miles divided by total miles."
  - key: "(i)"
    status: MISMATCH
    reason: "The program prints the raw election. It is not limited to the passenger automobile cap and is not set to zero for a vehicle placed in service before 2025. Column (i) is the amount elected \"(subject to the limits for passenger automobiles)\". Section 179 applies only to property \"placed in service during the tax year\"."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The i4562 election out applies \"for any class of property ... for all such property in such class\". A choice that differs within the 5-year class is refused."
  - key: "7"
    status: MATCH
    reason: "Worksheet line 7 is the maximum deduction from the Pub. 946 table. For a 2025 vehicle that is $20,200 with the special allowance and $12,200 without it (footnote 1). Earlier vehicles use their year-of-recovery entry."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says \"Multiply line 7 by line 8\", and line 8 is the business-use percentage."
  - key: "10"
    status: MATCH
    reason: "Worksheet line 10 is the \"Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service\". The program follows this."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 says \"Subtract line 10 from line 9.\""
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the section 179 deduction claimed in the year placed in service. For a 2025 vehicle that is line 10; otherwise the earlier year's amount is entered."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 says \"Subtract line 14 from line 13.\""
  - key: "16"
    status: MATCH
    reason: "The program multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025 (or 40% if elected), and 40% if acquired earlier. It enters -0- if the vehicle was not placed in service this year or the allowance is elected out, as i4562 line 14 and the worksheet say."
  - key: "25"
    status: MISMATCH
    reason: "The program prints line 25 only for passenger automobiles under the limits. A listed-property vehicle outside the limits, such as a heavier SUV, with a special allowance gets no line 25. Line 25 says \"Enter on line 25 your total special depreciation allowance for all qualified listed property\", and listed property includes \"SUVs\"."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 says \"Subtract line 16 from line 11.\""
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 says \"Subtract line 16 from line 15.\""
  - key: "19"
    status: MATCH
    reason: "Worksheet line 19 says \"Multiply line 18 by line 6\", the table rate for 5-year property under the applicable convention. The program's mid-quarter test uses bases after section 179 and before the special allowance, as Pub. 946 says. Line 19 is zero after the recovery period, where the table gives no rate."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20 says \"Enter the lesser of line 17 or line 19.\""
```
```
