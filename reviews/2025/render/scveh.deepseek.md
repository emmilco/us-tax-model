# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 3483f22958b14c2fa4a26cb76dca6e8dbff801aa714a2fddad535267460d49c6 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 5ebcdc560620146fe1bed41557e291ad2f27a3355cc0428438f9e4ee195b3ab5 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 22 / 3 / 0 / 0 |
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

Model: IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement asks only for the year, omitting month and day.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### 44a — Business miles
Status: **MATCH**

Model: IRS line 44a asks for business miles, and the restatement correctly describes business miles excluding commuting.

### 44b — Commuting miles
Status: **MATCH**

Model: IRS line 44b asks for commuting miles, and the restatement describes commuting travel between home and a work location as defined in the line 44b instructions.

### 44c — Other miles
Status: **MATCH**

Model: IRS line 44c asks for other miles, and the restatement’s 'other (personal)' miles is consistent with the remaining nonbusiness miles.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The restatement tracks the line 9 standard-mileage eligibility conditions and adds the required 'No' answer for five or more vehicles used at the same time.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: The restatement correctly chooses between the standard mileage amount plus parking/tolls and the business portion of actual operating expenses plus parking/tolls.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: IRS says to enter the business portion of rental cost, but 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.' The restatement omits that reduction.

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ("an inclusion amount for leased property"), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Form 4562 Part V column (b) says 'Date placed in service. Enter the date the property was placed in service' and treats conversion date as placed-in-service; the restatement asks only for a year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The screen narrows the tool to cases it supports and names the excluded circumstances, which is permitted.

### (d) — Cost or other basis
Status: **MATCH**

Model: The restatement matches the cost or other basis rule, including the conversion rule, within the cases not excluded by the screen.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: This matches the worksheet line computing business/investment cost by multiplying cost or other basis by the business-use percentage from business miles over total miles.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: This is the elected section 179 cost, with excess elections handled by the section 179 refusal in the related computation.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The special allowance election must be consistent for the class of 5-year property placed in service in 2025, as the restatement asks.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: The restatement selects the applicable maximum passenger automobile depreciation limit for a 2025 vehicle or for the vehicle’s 2025 recovery year.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: This matches the worksheet line multiplying the maximum deduction by the business-use percentage computed from business miles over total miles.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: For a 2025 passenger automobile, the section 179 deduction is limited to line 9, and the restatement enters zero for vehicles not placed in service in 2025.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: This correctly subtracts line 10 from line 9, with a zero floor.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: This matches the worksheet line for the section 179 deduction claimed in the year the vehicle was placed in service.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: This correctly subtracts line 14 from line 13, with a zero floor.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: This matches the special depreciation allowance worksheet line, entering zero when the vehicle was not placed in service in 2025.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: The special depreciation allowance is included in the overall passenger automobile limit, so using the smaller of line 16 or line 11 applies that limit.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: This correctly subtracts line 16 from line 11, with a zero floor.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: This correctly subtracts line 16 from line 15, with a zero floor.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: This matches the worksheet line applying the applicable MACRS rate, including half-year or mid-quarter for a 2025 vehicle and the prior convention for earlier vehicles.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: This matches the worksheet line entering the lesser of line 17 or line 19.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement asks only for the year, omitting month and day."
  - key: "44a"
    status: MATCH
    reason: "IRS line 44a asks for business miles, and the restatement correctly describes business miles excluding commuting."
  - key: "44b"
    status: MATCH
    reason: "IRS line 44b asks for commuting miles, and the restatement describes commuting travel between home and a work location as defined in the line 44b instructions."
  - key: "44c"
    status: MATCH
    reason: "IRS line 44c asks for other miles, and the restatement’s 'other (personal)' miles is consistent with the remaining nonbusiness miles."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The restatement tracks the line 9 standard-mileage eligibility conditions and adds the required 'No' answer for five or more vehicles used at the same time."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The restatement correctly chooses between the standard mileage amount plus parking/tolls and the business portion of actual operating expenses plus parking/tolls."
  - key: "20a"
    status: MISMATCH
    reason: "IRS says to enter the business portion of rental cost, but 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.' The restatement omits that reduction."
  - key: "(b)"
    status: MISMATCH
    reason: "Form 4562 Part V column (b) says 'Date placed in service. Enter the date the property was placed in service' and treats conversion date as placed-in-service; the restatement asks only for a year."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The screen narrows the tool to cases it supports and names the excluded circumstances, which is permitted."
  - key: "(d)"
    status: MATCH
    reason: "The restatement matches the cost or other basis rule, including the conversion rule, within the cases not excluded by the screen."
  - key: "13"
    status: MATCH
    reason: "This matches the worksheet line computing business/investment cost by multiplying cost or other basis by the business-use percentage from business miles over total miles."
  - key: "(i)"
    status: MATCH
    reason: "This is the elected section 179 cost, with excess elections handled by the section 179 refusal in the related computation."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The special allowance election must be consistent for the class of 5-year property placed in service in 2025, as the restatement asks."
  - key: "7"
    status: MATCH
    reason: "The restatement selects the applicable maximum passenger automobile depreciation limit for a 2025 vehicle or for the vehicle’s 2025 recovery year."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "This matches the worksheet line multiplying the maximum deduction by the business-use percentage computed from business miles over total miles."
  - key: "10"
    status: MATCH
    reason: "For a 2025 passenger automobile, the section 179 deduction is limited to line 9, and the restatement enters zero for vehicles not placed in service in 2025."
  - key: "11"
    status: MATCH
    reason: "This correctly subtracts line 10 from line 9, with a zero floor."
  - key: "14"
    status: MATCH
    reason: "This matches the worksheet line for the section 179 deduction claimed in the year the vehicle was placed in service."
  - key: "15"
    status: MATCH
    reason: "This correctly subtracts line 14 from line 13, with a zero floor."
  - key: "16"
    status: MATCH
    reason: "This matches the special depreciation allowance worksheet line, entering zero when the vehicle was not placed in service in 2025."
  - key: "25"
    status: MATCH
    reason: "The special depreciation allowance is included in the overall passenger automobile limit, so using the smaller of line 16 or line 11 applies that limit."
  - key: "17"
    status: MATCH
    reason: "This correctly subtracts line 16 from line 11, with a zero floor."
  - key: "18"
    status: MATCH
    reason: "This correctly subtracts line 16 from line 15, with a zero floor."
  - key: "19"
    status: MATCH
    reason: "This matches the worksheet line applying the applicable MACRS rate, including half-year or mid-quarter for a 2025 vehicle and the prior convention for earlier vehicles."
  - key: "20"
    status: MATCH
    reason: "This matches the worksheet line entering the lesser of line 17 or line 19."
```
