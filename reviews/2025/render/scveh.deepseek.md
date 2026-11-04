# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | fca791ca88a08e3788c1c72c0e83aea2e256f2ecb27cede0cb2db8a45809a55a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 7abd522bb45beed38ca4fc7a89f8396f00d00202ca111a9ed0ef64d93db512cb |
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
| p946 | For use in preparing 2025 returns | 17, 31, 32, 34, 37, 39, 41, 59, 60, 61, 62, 63, 71, 72, 73, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### 43 — When did you place your vehicle in service for business purposes? (month/day/year)
Status: **MISMATCH**

Restated: Input — The year you first placed this vehicle in service for business purposes (for example 2023)

Model: IRS line 43 asks "When did you place your vehicle in service for business purposes? (month/day/year)"; the restatement asks only for the year.

Ruling: representation; same as the earlier ruling. The tool needs the year (and, for 2025 property, the quarter); the filer writes the full date on Schedule C line 43 from their own records.

### 44a — Business miles
Status: **MATCH**

Model: Matches the business miles requested on line 44a, excluding commuting.

### 44b — Commuting miles
Status: **MATCH**

Model: Matches commuting miles as travel between home and a work location, with reference to the line 44b instructions.

### 44c — Other miles
Status: **MATCH**

Model: Matches the other miles requested on line 44c.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: Matches the line 9 conditions for using the standard mileage rate, including the five-or-more-vehicles rule.

### (screen) (scveh.employee_use) — Your employees use this vehicle for personal purposes
Status: **MATCH**

Model: Matches the employee-use rule, including 100% business treatment when personal use is included in income or reimbursed.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Matches line 9: standard mileage amount plus parking and tolls, or business operating expenses plus parking and tolls, depending on the method.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: Matches line 9's rule that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used previously.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: IRS line 20a says to enter the business portion of rental cost but also that "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount"; the restatement omits that reduction.

Ruling: scope; same as the earlier ruling (restatement and objection unchanged). An inclusion amount for leased property is refused for the business through sc.special ("an inclusion amount for leased property"), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: IRS column (b) says "Date placed in service" and instructs entering the date, not just the year.

Ruling: representation; same as the earlier ruling. No value depends on the month or day except through the quarter, asked separately.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The screen narrows the tool by naming the excluded vehicle situations; within the supported cases the line is not misstated.

### (d) — Cost or other basis
Status: **MATCH**

Model: Matches the vehicle cost or other basis within the supported cases, with excluded credit/trade-in/conversion situations covered by the screen and refusal.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Matches the worksheet line 13 computation of business/investment cost by multiplying the vehicle basis by the business-use percentage.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Matches the elected section 179 cost column within the supported cases.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: Matches the requirement that the special allowance election be consistent for the class of 5-year property placed in service in 2025.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Matches the maximum depreciation limit for the vehicle's applicable year from the passenger automobile table.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Matches worksheet line 9: line 7 multiplied by the business/investment-use percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Matches worksheet line 10: section 179 claimed this year, limited to line 9 for passenger automobiles, and zero if not placed in service this year.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Matches worksheet line 11: line 9 minus line 10, not below zero.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Matches worksheet line 14: section 179 claimed in the year the vehicle was placed in service.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Matches worksheet line 15: line 13 minus line 14.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Matches worksheet line 16: special allowance for a 2025 vehicle and zero if not placed in service that year.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: Matches the passenger automobile overall limit by limiting the special allowance to the remaining limit on line 11.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Matches worksheet line 17: line 11 minus line 16, not below zero.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Matches worksheet line 18: line 15 minus line 16.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Matches worksheet line 19: line 18 multiplied by the applicable MACRS rate, using the half-year or mid-quarter convention for 2025 vehicles and the prior convention for earlier vehicles.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Matches worksheet line 20: the lesser of line 17 or line 19.

## Raw response

```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "IRS line 43 asks \"When did you place your vehicle in service for business purposes? (month/day/year)\"; the restatement asks only for the year."
  - key: "44a"
    status: MATCH
    reason: "Matches the business miles requested on line 44a, excluding commuting."
  - key: "44b"
    status: MATCH
    reason: "Matches commuting miles as travel between home and a work location, with reference to the line 44b instructions."
  - key: "44c"
    status: MATCH
    reason: "Matches the other miles requested on line 44c."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "Matches the line 9 conditions for using the standard mileage rate, including the five-or-more-vehicles rule."
  - key: "(screen) (scveh.employee_use)"
    status: MATCH
    reason: "Matches the employee-use rule, including 100% business treatment when personal use is included in income or reimbursed."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Matches line 9: standard mileage amount plus parking and tolls, or business operating expenses plus parking and tolls, depending on the method."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "Matches line 9's rule that actual expenses cannot be used for a leased vehicle if the standard mileage rate was used previously."
  - key: "20a"
    status: MISMATCH
    reason: "IRS line 20a says to enter the business portion of rental cost but also that \"if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount\"; the restatement omits that reduction."
  - key: "(b)"
    status: MISMATCH
    reason: "IRS column (b) says \"Date placed in service\" and instructs entering the date, not just the year."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The screen narrows the tool by naming the excluded vehicle situations; within the supported cases the line is not misstated."
  - key: "(d)"
    status: MATCH
    reason: "Matches the vehicle cost or other basis within the supported cases, with excluded credit/trade-in/conversion situations covered by the screen and refusal."
  - key: "13"
    status: MATCH
    reason: "Matches the worksheet line 13 computation of business/investment cost by multiplying the vehicle basis by the business-use percentage."
  - key: "(i)"
    status: MATCH
    reason: "Matches the elected section 179 cost column within the supported cases."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "Matches the requirement that the special allowance election be consistent for the class of 5-year property placed in service in 2025."
  - key: "7"
    status: MATCH
    reason: "Matches the maximum depreciation limit for the vehicle's applicable year from the passenger automobile table."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Matches worksheet line 9: line 7 multiplied by the business/investment-use percentage."
  - key: "10"
    status: MATCH
    reason: "Matches worksheet line 10: section 179 claimed this year, limited to line 9 for passenger automobiles, and zero if not placed in service this year."
  - key: "11"
    status: MATCH
    reason: "Matches worksheet line 11: line 9 minus line 10, not below zero."
  - key: "14"
    status: MATCH
    reason: "Matches worksheet line 14: section 179 claimed in the year the vehicle was placed in service."
  - key: "15"
    status: MATCH
    reason: "Matches worksheet line 15: line 13 minus line 14."
  - key: "16"
    status: MATCH
    reason: "Matches worksheet line 16: special allowance for a 2025 vehicle and zero if not placed in service that year."
  - key: "25"
    status: MATCH
    reason: "Matches the passenger automobile overall limit by limiting the special allowance to the remaining limit on line 11."
  - key: "17"
    status: MATCH
    reason: "Matches worksheet line 17: line 11 minus line 16, not below zero."
  - key: "18"
    status: MATCH
    reason: "Matches worksheet line 18: line 15 minus line 16."
  - key: "19"
    status: MATCH
    reason: "Matches worksheet line 19: line 18 multiplied by the applicable MACRS rate, using the half-year or mid-quarter convention for 2025 vehicles and the prior convention for earlier vehicles."
  - key: "20"
    status: MATCH
    reason: "Matches worksheet line 20: the lesser of line 17 or line 19."
```
