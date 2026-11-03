# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fe34c4b233013cc042789fb8528ac1c2bd327970af236c69a005818cb52d6747 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 955488a7d83ff65edf3ea34b04b9179e1d61c3f9f351dc6d2a4a729697caca93 |
| lines judged | 26 |
| match / mismatch / unclear / missing | 23 / 3 / 0 / 0 |
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

Model: The restatement collects only the year (a Count). The form asks for a full date: "When did you place your vehicle in service for business purposes? (month/day/year)".

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records.

### 44a — Business miles
Status: **MATCH**

Model: Business miles for 2025, excluding commuting, as line 44a asks.

### 44b — Commuting miles
Status: **MATCH**

Model: Commuting miles, defined by reference to the line 44b instructions ("travel between your home and a work location"), which include the conversion-period rule.

### 44c — Other miles
Status: **MATCH**

Model: Other (personal) miles, matching "c Other".

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: Matches the line 9 conditions. An owned vehicle must have used the standard rate "for the first year you placed the vehicle in service". A leased vehicle must use it "for the entire lease period". Actual expenses are required if "you used five or more vehicles simultaneously".

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: Standard: "Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls". Actual: "the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.", with business parking and tolls added. Depreciation and lease payments go elsewhere.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: Implements "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle". The related refusal enforces this.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the business portion of the lease payments and nothing else. No inclusion-amount reduction is made, and no refusal excludes leases where one applies. The line 20a instructions say "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount".

Ruling: refusal located elsewhere; restatement accepted. sc.special refuses "an inclusion amount for leased property" for the business, read for every Schedule C (checked by evaluation in the A-backlog session: sc.special answered Yes refuses at sc.line1).

### (b) — Year placed in service
Status: **MATCH**

Model: Collects the year placed in service, limited to 2019–2025. A refusal excludes vehicles used 50% or less, which per the instructions go on "line 27 ... for property used 50% or less in a qualified business use" under ADS.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is an exclusion screen. Each item is a case the program declines, and each is consistent with the texts given (trade-ins, short years, casualty basis adjustments, credits, ADS, qualified business use, record requirements, employee use, conversions).

### (d) — Cost or other basis
Status: **MATCH**

Model: Matches column (d): "actual cost (including sales tax) or other basis", and for a converted vehicle the "smaller of the property's adjusted basis or its fair market value on the date of conversion". Basis reduction for vehicle credits is excluded by the screen refusal; pre-2019 vehicles are refused.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13: "Multiply line 12 by line 8". The business percentage is business miles divided by total miles, per column (c): "dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles".

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i): "Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use". Low use and amounts over cost or the SUV limit are refused.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies "for any class of property ... for all such property in such class placed in service during the tax year". Mixed elections within the class are refused.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The passenger-automobile limit table is applied to every vehicle, including those flagged as not subject to the limits (scveh.passenger = false, e.g. SUVs over 6,000 lbs). The text says "For any passenger automobile ... cannot exceed the applicable limit" and lists vehicles that "are not considered passenger automobiles". Table values used otherwise match (2025: $20,200 with allowance, $12,200 without).

Ruling: representation; restatement accepted. The worksheet line is figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass); checked by evaluation on stage14.veh.suv_179 with passenger answered both ways: the allowance is $20,200 and $70,000.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9: "Multiply line 7 by line 8", using the mileage-based business percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: Worksheet line 10: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service." For a passenger automobile the cap at line 9 is applied.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11: "Subtract line 10 from line 9."

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14: "Section 179 deduction claimed in the year you placed the car in service". For a 2025 vehicle that is line 10; for earlier years it is the prior claim.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15: "Subtract line 14 from line 13."

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Worksheet line 16: "Multiply line 15 by the applicable percentage ... Enter -0- if this is not the year you placed the car in service ... or you elected not to claim". Percentages: 100% if acquired after January 19, 2025, 40% if elected; 40% if acquired before January 20, 2025.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MATCH**

Model: The special allowance on Form 4562 line 25 is limited to line 11 ("Your depreciation deduction (including your special depreciation allowance) is limited to the amount on line 11"). The smaller of line 16 or line 11 gives that result.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17: "Subtract line 16 from line 11."

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18: "Subtract line 16 from line 15."

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Worksheet line 19: "Multiply line 18 by line 6", using 5-year rates from Tables A-1 to A-5. The convention follows the 40% fourth-quarter test on bases after section 179 and before the special allowance. A 2019 vehicle in year 7 has no table rate, so zero follows from the tables.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MATCH**

Model: Worksheet line 20: "Enter the lesser of line 17 or line 19."

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The restatement collects only the year (a Count). The form asks for a full date: \"When did you place your vehicle in service for business purposes? (month/day/year)\"."
  - key: "44a"
    status: MATCH
    reason: "Business miles for 2025, excluding commuting, as line 44a asks."
  - key: "44b"
    status: MATCH
    reason: "Commuting miles, defined by reference to the line 44b instructions (\"travel between your home and a work location\"), which include the conversion-period rule."
  - key: "44c"
    status: MATCH
    reason: "Other (personal) miles, matching \"c Other\"."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "Matches the line 9 conditions. An owned vehicle must have used the standard rate \"for the first year you placed the vehicle in service\". A leased vehicle must use it \"for the entire lease period\". Actual expenses are required if \"you used five or more vehicles simultaneously\"."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "Standard: \"Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls\". Actual: \"the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.\", with business parking and tolls added. Depreciation and lease payments go elsewhere."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "Implements \"You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle\". The related refusal enforces this."
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the business portion of the lease payments and nothing else. No inclusion-amount reduction is made, and no refusal excludes leases where one applies. The line 20a instructions say \"if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount\"."
  - key: "(b)"
    status: MATCH
    reason: "Collects the year placed in service, limited to 2019–2025. A refusal excludes vehicles used 50% or less, which per the instructions go on \"line 27 ... for property used 50% or less in a qualified business use\" under ADS."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is an exclusion screen. Each item is a case the program declines, and each is consistent with the texts given (trade-ins, short years, casualty basis adjustments, credits, ADS, qualified business use, record requirements, employee use, conversions)."
  - key: "(d)"
    status: MATCH
    reason: "Matches column (d): \"actual cost (including sales tax) or other basis\", and for a converted vehicle the \"smaller of the property's adjusted basis or its fair market value on the date of conversion\". Basis reduction for vehicle credits is excluded by the screen refusal; pre-2019 vehicles are refused."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13: \"Multiply line 12 by line 8\". The business percentage is business miles divided by total miles, per column (c): \"dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles\"."
  - key: "(i)"
    status: MATCH
    reason: "Column (i): \"Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use\". Low use and amounts over cost or the SUV limit are refused."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies \"for any class of property ... for all such property in such class placed in service during the tax year\". Mixed elections within the class are refused."
  - key: "7"
    status: MISMATCH
    reason: "The passenger-automobile limit table is applied to every vehicle, including those flagged as not subject to the limits (scveh.passenger = false, e.g. SUVs over 6,000 lbs). The text says \"For any passenger automobile ... cannot exceed the applicable limit\" and lists vehicles that \"are not considered passenger automobiles\". Table values used otherwise match (2025: $20,200 with allowance, $12,200 without)."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9: \"Multiply line 7 by line 8\", using the mileage-based business percentage."
  - key: "10"
    status: MATCH
    reason: "Worksheet line 10: \"Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service.\" For a passenger automobile the cap at line 9 is applied."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11: \"Subtract line 10 from line 9.\""
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14: \"Section 179 deduction claimed in the year you placed the car in service\". For a 2025 vehicle that is line 10; for earlier years it is the prior claim."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15: \"Subtract line 14 from line 13.\""
  - key: "16"
    status: MATCH
    reason: "Worksheet line 16: \"Multiply line 15 by the applicable percentage ... Enter -0- if this is not the year you placed the car in service ... or you elected not to claim\". Percentages: 100% if acquired after January 19, 2025, 40% if elected; 40% if acquired before January 20, 2025."
  - key: "25"
    status: MATCH
    reason: "The special allowance on Form 4562 line 25 is limited to line 11 (\"Your depreciation deduction (including your special depreciation allowance) is limited to the amount on line 11\"). The smaller of line 16 or line 11 gives that result."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17: \"Subtract line 16 from line 11.\""
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18: \"Subtract line 16 from line 15.\""
  - key: "19"
    status: MATCH
    reason: "Worksheet line 19: \"Multiply line 18 by line 6\", using 5-year rates from Tables A-1 to A-5. The convention follows the 40% fourth-quarter test on bases after section 179 and before the special allowance. A 2019 vehicle in year 7 has no table rate, so zero follows from the tables."
  - key: "20"
    status: MATCH
    reason: "Worksheet line 20: \"Enter the lesser of line 17 or line 19.\""
```
```
