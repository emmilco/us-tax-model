# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b0be20f963e73a89730bcead8d86b75478c233b92f88f57734c07473b0656ba1 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 117cd5b4f43aabdf2c0e1e93b20d6607de49a897ca6f516ad58555e53e57612a |
| lines judged | 26 |
| match / mismatch / unclear / missing | 19 / 7 / 0 / 0 |
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

Model: The form asks for a full date, 'When did you place your vehicle in service for business purposes? (month/day/year)', but the restatement collects only the year. No computation is affected, but the printed entry would be incomplete.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Line 44a asks for the miles the vehicle was used for business out of the total driven during 2025, and the restatement collects that.

### 44b — Commuting miles
Status: **MATCH**

Model: The restatement collects 2025 commuting miles and uses the instructions' definition by reference ('travel between your home and a work location').

### 44c — Other miles
Status: **MATCH**

Model: Line 44c is 'Other' miles, and the restatement collects the other (personal) miles driven in 2025.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The screen follows the Line 9 conditions: an owned vehicle on the standard rate in its first year, a leased vehicle on the standard rate for the entire lease, and actual expenses required for 'five or more vehicles simultaneously'.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MATCH**

Model: The standard branch is business miles x 0.70 plus parking fees and tolls, as instructed and as Notice 2025-5 confirms. The actual branch is the business portion of operating expenses; the text does not separately mention parking and tolls on this branch, but its open-ended 'etc.' accommodates adding their business amount.

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before
Status: **MATCH**

Model: This collects the fact behind the rule 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.'

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the business portion of lease payments with no adjustment or refusal, but the text adds 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.' The omission can change the amount. Pub. 946 instead reports the inclusion as other income, but neither treatment is computed or refused here.

Ruling: refusal located elsewhere; restatement accepted. sc.special refuses "an inclusion amount for leased property" for the business, read for every Schedule C, so the business portion of the lease payments is the line 20a amount on a computed return.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Column (b) says 'Enter the date the property was placed in service', but the restatement collects only a year. The year is enough for the table lookups, and the low-use refusal correctly follows the line 26/27 split, but the printed entry would be incomplete.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope screen that excludes cases the text treats specially, including trade-ins, vehicle credits, conversions, and vehicles for hire, ambulances or hearses. The refusal on column (d) names the exclusions.

### (d) — Cost or other basis
Status: **MATCH**

Model: This follows 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)' and the smaller-of rule for conversions. Worksheet footnote 1 confirms no section 179 reduction, and credit reductions are screened out.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13 multiplies cost (line 12) by the business-use percentage (line 8). Column (c) defines that percentage as business miles, excluding commuting, divided by total miles, which is what the restatement computes.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) is 'the amount you elect to expense', and the restatement collects that election. The limits are applied elsewhere.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies to 'all such property in such class placed in service during the tax year', and mixed choices are refused. Including a spouse on a joint return is not in the text, but it only narrows what the program accepts.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The restatement applies the limit to every vehicle with no passenger-automobile condition, although the limits apply to 'passenger automobiles' and the text lists vehicles 'not considered passenger automobiles' (also over 6,000 pounds). The amounts themselves follow the tables for passenger automobiles ($20,200 with the allowance, $12,200 without), but a non-passenger vehicle is wrongly carried through this limit.

Ruling: representation; restatement accepted. The worksheet lines are figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass). Checked by evaluation on stage14.veh.suv_179 with passenger answered both ways: the allowance is $20,200 and $70,000.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: The worksheet says 'Multiply line 7 by line 8', and the restatement multiplies line 7 by business miles over total miles, the column (c) percentage.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: This follows 'Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service.' It uses the elected amount as the claimed amount; the given lines do not show the Part I business income limit being applied.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: The worksheet says 'Subtract line 10 from line 9'. The floor at zero does not conflict with it.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. That is line 10 for a 2025 vehicle and the prior-year claimed amount otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: The worksheet says 'Subtract line 14 from line 13'.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: This multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero on election out or when not the year placed in service. That agrees with the line 14 instructions and worksheet line 16.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MISMATCH**

Restated: Enter the smaller of line 16 or line 11.

Model: Capping at line 11 is right for passenger automobiles, since the allowance 'is included in the overall limit' for them. The program applies the cap to all vehicles, so a vehicle answered as not subject to the limits has its allowance reduced by a limit that applies only to 'passenger automobiles'.

Ruling: representation; restatement accepted. The worksheet lines are figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass). Checked by evaluation on stage14.veh.suv_179 with passenger answered both ways: the allowance is $20,200 and $70,000.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: The worksheet says 'Subtract line 16 from line 11'.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: The worksheet says 'Subtract line 16 from line 15'.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: Line 18 x the table rate matches 'Multiply line 18 by line 6' within the recovery period, with the half-year and mid-quarter choice following the 40% test. A 2019 vehicle gets zero and is not refused, whereas the text says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)', subject to the annual limit.

Ruling: representation; restatement accepted. The worksheet is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis (scveh.post, read by scveh.macrs_pass for column (h); p946 p. 61), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MISMATCH**

Restated: Enter the smaller of line 17 or line 19.

Model: 'Enter the lesser of line 17 or line 19' is followed arithmetically, but line 17 carries the passenger limit to vehicles not subject to it, whose deduction is wrongly capped. A 2019 vehicle also ends at zero despite the text's 'enter your unrecovered basis, if any, in column (h)'.

Ruling: representation; restatement accepted. The worksheet is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis (scveh.post, read by scveh.macrs_pass for column (h); p946 p. 61), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059). representation; restatement accepted. The worksheet lines are figured for every vehicle but read only for a passenger automobile (scveh.bonus_v, scveh.macrs_pass). Checked by evaluation on stage14.veh.suv_179 with passenger answered both ways: the allowance is $20,200 and $70,000.

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The form asks for a full date, 'When did you place your vehicle in service for business purposes? (month/day/year)', but the restatement collects only the year. No computation is affected, but the printed entry would be incomplete."
  - key: "44a"
    status: MATCH
    reason: "Line 44a asks for the miles the vehicle was used for business out of the total driven during 2025, and the restatement collects that."
  - key: "44b"
    status: MATCH
    reason: "The restatement collects 2025 commuting miles and uses the instructions' definition by reference ('travel between your home and a work location')."
  - key: "44c"
    status: MATCH
    reason: "Line 44c is 'Other' miles, and the restatement collects the other (personal) miles driven in 2025."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The screen follows the Line 9 conditions: an owned vehicle on the standard rate in its first year, a leased vehicle on the standard rate for the entire lease, and actual expenses required for 'five or more vehicles simultaneously'."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The standard branch is business miles x 0.70 plus parking fees and tolls, as instructed and as Notice 2025-5 confirms. The actual branch is the business portion of operating expenses; the text does not separately mention parking and tolls on this branch, but its open-ended 'etc.' accommodates adding their business amount."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "This collects the fact behind the rule 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.'"
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the business portion of lease payments with no adjustment or refusal, but the text adds 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.' The omission can change the amount. Pub. 946 instead reports the inclusion as other income, but neither treatment is computed or refused here."
  - key: "(b)"
    status: MISMATCH
    reason: "Column (b) says 'Enter the date the property was placed in service', but the restatement collects only a year. The year is enough for the table lookups, and the low-use refusal correctly follows the line 26/27 split, but the printed entry would be incomplete."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a scope screen that excludes cases the text treats specially, including trade-ins, vehicle credits, conversions, and vehicles for hire, ambulances or hearses. The refusal on column (d) names the exclusions."
  - key: "(d)"
    status: MATCH
    reason: "This follows 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)' and the smaller-of rule for conversions. Worksheet footnote 1 confirms no section 179 reduction, and credit reductions are screened out."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13 multiplies cost (line 12) by the business-use percentage (line 8). Column (c) defines that percentage as business miles, excluding commuting, divided by total miles, which is what the restatement computes."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) is 'the amount you elect to expense', and the restatement collects that election. The limits are applied elsewhere."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies to 'all such property in such class placed in service during the tax year', and mixed choices are refused. Including a spouse on a joint return is not in the text, but it only narrows what the program accepts."
  - key: "7"
    status: MISMATCH
    reason: "The restatement applies the limit to every vehicle with no passenger-automobile condition, although the limits apply to 'passenger automobiles' and the text lists vehicles 'not considered passenger automobiles' (also over 6,000 pounds). The amounts themselves follow the tables for passenger automobiles ($20,200 with the allowance, $12,200 without), but a non-passenger vehicle is wrongly carried through this limit."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "The worksheet says 'Multiply line 7 by line 8', and the restatement multiplies line 7 by business miles over total miles, the column (c) percentage."
  - key: "10"
    status: MATCH
    reason: "This follows 'Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service.' It uses the elected amount as the claimed amount; the given lines do not show the Part I business income limit being applied."
  - key: "11"
    status: MATCH
    reason: "The worksheet says 'Subtract line 10 from line 9'. The floor at zero does not conflict with it."
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. That is line 10 for a 2025 vehicle and the prior-year claimed amount otherwise."
  - key: "15"
    status: MATCH
    reason: "The worksheet says 'Subtract line 14 from line 13'."
  - key: "16"
    status: MATCH
    reason: "This multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero on election out or when not the year placed in service. That agrees with the line 14 instructions and worksheet line 16."
  - key: "25"
    status: MISMATCH
    reason: "Capping at line 11 is right for passenger automobiles, since the allowance 'is included in the overall limit' for them. The program applies the cap to all vehicles, so a vehicle answered as not subject to the limits has its allowance reduced by a limit that applies only to 'passenger automobiles'."
  - key: "17"
    status: MATCH
    reason: "The worksheet says 'Subtract line 16 from line 11'."
  - key: "18"
    status: MATCH
    reason: "The worksheet says 'Subtract line 16 from line 15'."
  - key: "19"
    status: MISMATCH
    reason: "Line 18 x the table rate matches 'Multiply line 18 by line 6' within the recovery period, with the half-year and mid-quarter choice following the 40% test. A 2019 vehicle gets zero and is not refused, whereas the text says 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)', subject to the annual limit."
  - key: "20"
    status: MISMATCH
    reason: "'Enter the lesser of line 17 or line 19' is followed arithmetically, but line 17 carries the passenger limit to vehicles not subject to it, whose deduction is wrongly capped. A 2019 vehicle also ends at zero despite the text's 'enter your unrecovered basis, if any, in column (h)'."
```
```
