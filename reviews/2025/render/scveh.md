# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3483f22958b14c2fa4a26cb76dca6e8dbff801aa714a2fddad535267460d49c6 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 5ebcdc560620146fe1bed41557e291ad2f27a3355cc0428438f9e4ee195b3ab5 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 18 / 7 / 0 / 0 |
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

Model: The form asks for a full date: 'When did you place your vehicle in service for business purposes? (month/day/year)'. The restatement collects only the year.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### 44a — Business miles
Status: **MATCH**

Model: This restates Part IV line 44a, 'Business' miles out of the total miles driven during 2025. Excluding commuting agrees with the Column (c) instruction, 'not to include any commuting mileage'.

### 44b — Commuting miles
Status: **MATCH**

Model: This restates line 44b, commuting miles, using the instruction's definition: 'travel between your home and a work location'.

### 44c — Other miles
Status: **MATCH**

Model: This restates line 44c, 'Other' miles driven during 2025.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The question tracks the Line 9 conditions: owned and 'used the standard mileage rate for the first year', or leased and using it 'for the entire lease period'. It also applies the rule that 'five or more vehicles simultaneously' must use actual expenses.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MISMATCH**

Restated: Choose — [helper "Standard mileage rate or actual expenses" = 'standard' → helper "Standard mileage amount plus parking fees and tolls"] [helper "Standard mileage rate or actual expenses" = 'actual' → helper "Business portion of the operating expenses plus parking fees and tolls"]

Model: The standard branch (miles x 0.70 plus parking and tolls) and the business portion of operating expenses agree with the text, but no refusal is shown for this rule: 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.' The screen that asks about earlier standard mileage use only refuses at column (d), which the leased path does not use.

Ruling: finding (BUG-0310, open, T-173); i1040sc p. 6: "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle." The screen's refusal is on scveh.cost, which a leased vehicle does not read; stage14.veh.leased_actual with the screen answered Yes still completes. The rest of the restatement matches.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The business portion of the lease cost agrees with the text, but the restatement omits this adjustment and has no refusal for it: 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.'

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ("an inclusion amount for leased property"), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: The instruction says 'Enter the date the property was placed in service', but the restatement collects only the year. The narrowing to 2019-2025 and the refusal for 50% or less business use are acceptable.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on the form from their own records. No value depends on the month or day except through the quarter, asked separately.

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope screen that excludes cases the instructions treat specially, such as trade-ins, conversions, vehicle credits, earlier low business use, and vehicles for hire, ambulances and hearses. It narrows the supported cases without changing a computation.

### (d) — Cost or other basis
Status: **MATCH**

Model: This agrees with Column (d): 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)', and the smaller of adjusted basis or fair market value on conversion. Credit reductions and pre-2019 vehicles are excluded by named refusals.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: This agrees with worksheet line 13, 'Multiply line 12 by line 8', where line 8 is the business/investment-use percentage that Column (c) defines as business miles divided by total miles. Column (d) serves as line 12 because credit reductions are screened out.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: This agrees with Column (i), 'Enter the amount you elect to expense'. The more-than-50% use requirement, the $31,300 SUV limit and the passenger automobile limit are handled by the refusals and worksheet line 10.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The text says an election out applies 'for any class of property' and to 'all such property in such class placed in service during the tax year'. A No answer leads to a named refusal, so the screen only narrows the supported cases.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: This agrees with worksheet line 7, 'Maximum depreciation deduction for this year from the appropriate table', including the first-year $20,200 and $12,200 amounts for 2025. The missing branch for vehicles not subject to these limits is reported at lines 25 and 20.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: This agrees with worksheet line 9, 'Multiply line 7 by line 8', with line 8 computed as business miles divided by total miles.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: This agrees with worksheet line 10, 'Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service'. Removing the line 9 cap for vehicles outside the passenger automobile limits is consistent with those limits applying only to passenger automobiles.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: This agrees with worksheet line 11, 'Subtract line 10 from line 9'. The zero floor changes nothing for a passenger automobile because line 10 is capped at line 9.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: This agrees with worksheet line 14, 'Section 179 deduction claimed in the year you placed the car in service': line 10 for a 2025 vehicle and the amount claimed earlier for an older one.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: This agrees with worksheet line 15, 'Subtract line 14 from line 13'.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: This agrees with worksheet line 16 and the Line 14 instructions: 100% if acquired after January 19, 2025, a 40% election, 40% if acquired earlier, and -0- if not placed in service in 2025 or the taxpayer elected out. Acquisitions before September 28, 2017 and low-use vehicles are excluded by refusals.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MISMATCH**

Restated: Enter the smaller of line 16 or line 11.

Model: The line 11 cap applies to every vehicle, including those the program treats as not subject to the limits at line 10. The instructions limit only passenger automobiles ('For any passenger automobile... cannot exceed the applicable limit'), so a heavier vehicle's allowance would be wrongly capped.

Ruling: representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: scveh.bonus_v takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass. A vehicle that is not a passenger automobile is not limited.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: This agrees with worksheet line 17, 'Subtract line 16 from line 11', with -0- when line 16 is larger, consistent with the worksheet's stop note.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: This agrees with worksheet line 18, 'Subtract line 16 from line 15'.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]

Model: The in-recovery branches agree with 'Multiply line 18 by line 6' and the half-year and mid-quarter tables, but a 2019 vehicle gets zero with no other computation shown. The instructions say, 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)', subject to the annual limit.

Ruling: representation; restatement accepted. Lines 19 and 20 belong to the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); p946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059).

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MISMATCH**

Restated: Enter the smaller of line 17 or line 19.

Model: The formula matches 'Enter the lesser of line 17 or line 19', but it yields zero for a 2019 vehicle even though Pub. 946 says 'you can deduct that unrecovered basis after the recovery period ends'. It also applies the line 17 limit to vehicles outside the 'Limits for passenger automobiles'.

Ruling: representation; restatement accepted. Lines 19 and 20 belong to the automobile worksheet, which is not used after the recovery period; a 2019 vehicle's deduction is its unrecovered basis, limited and prorated (scveh.post, read by scveh.macrs_pass for column (h); p946 p. 61, Deductions After the Recovery Period), as stage14.veh.2019_cheap_mq3 asserts (BUG-0059). representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: scveh.bonus_v takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass. A vehicle that is not a passenger automobile is not limited.

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The form asks for a full date: 'When did you place your vehicle in service for business purposes? (month/day/year)'. The restatement collects only the year."
  - key: "44a"
    status: MATCH
    reason: "This restates Part IV line 44a, 'Business' miles out of the total miles driven during 2025. Excluding commuting agrees with the Column (c) instruction, 'not to include any commuting mileage'."
  - key: "44b"
    status: MATCH
    reason: "This restates line 44b, commuting miles, using the instruction's definition: 'travel between your home and a work location'."
  - key: "44c"
    status: MATCH
    reason: "This restates line 44c, 'Other' miles driven during 2025."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The question tracks the Line 9 conditions: owned and 'used the standard mileage rate for the first year', or leased and using it 'for the entire lease period'. It also applies the rule that 'five or more vehicles simultaneously' must use actual expenses."
  - key: "9 (scveh.line9)"
    status: MISMATCH
    reason: "The standard branch (miles x 0.70 plus parking and tolls) and the business portion of operating expenses agree with the text, but no refusal is shown for this rule: 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.' The screen that asks about earlier standard mileage use only refuses at column (d), which the leased path does not use."
  - key: "20a"
    status: MISMATCH
    reason: "The business portion of the lease cost agrees with the text, but the restatement omits this adjustment and has no refusal for it: 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.'"
  - key: "(b)"
    status: MISMATCH
    reason: "The instruction says 'Enter the date the property was placed in service', but the restatement collects only the year. The narrowing to 2019-2025 and the refusal for 50% or less business use are acceptable."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a scope screen that excludes cases the instructions treat specially, such as trade-ins, conversions, vehicle credits, earlier low business use, and vehicles for hire, ambulances and hearses. It narrows the supported cases without changing a computation."
  - key: "(d)"
    status: MATCH
    reason: "This agrees with Column (d): 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)', and the smaller of adjusted basis or fair market value on conversion. Credit reductions and pre-2019 vehicles are excluded by named refusals."
  - key: "13"
    status: MATCH
    reason: "This agrees with worksheet line 13, 'Multiply line 12 by line 8', where line 8 is the business/investment-use percentage that Column (c) defines as business miles divided by total miles. Column (d) serves as line 12 because credit reductions are screened out."
  - key: "(i)"
    status: MATCH
    reason: "This agrees with Column (i), 'Enter the amount you elect to expense'. The more-than-50% use requirement, the $31,300 SUV limit and the passenger automobile limit are handled by the refusals and worksheet line 10."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The text says an election out applies 'for any class of property' and to 'all such property in such class placed in service during the tax year'. A No answer leads to a named refusal, so the screen only narrows the supported cases."
  - key: "7"
    status: MATCH
    reason: "This agrees with worksheet line 7, 'Maximum depreciation deduction for this year from the appropriate table', including the first-year $20,200 and $12,200 amounts for 2025. The missing branch for vehicles not subject to these limits is reported at lines 25 and 20."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "This agrees with worksheet line 9, 'Multiply line 7 by line 8', with line 8 computed as business miles divided by total miles."
  - key: "10"
    status: MATCH
    reason: "This agrees with worksheet line 10, 'Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service'. Removing the line 9 cap for vehicles outside the passenger automobile limits is consistent with those limits applying only to passenger automobiles."
  - key: "11"
    status: MATCH
    reason: "This agrees with worksheet line 11, 'Subtract line 10 from line 9'. The zero floor changes nothing for a passenger automobile because line 10 is capped at line 9."
  - key: "14"
    status: MATCH
    reason: "This agrees with worksheet line 14, 'Section 179 deduction claimed in the year you placed the car in service': line 10 for a 2025 vehicle and the amount claimed earlier for an older one."
  - key: "15"
    status: MATCH
    reason: "This agrees with worksheet line 15, 'Subtract line 14 from line 13'."
  - key: "16"
    status: MATCH
    reason: "This agrees with worksheet line 16 and the Line 14 instructions: 100% if acquired after January 19, 2025, a 40% election, 40% if acquired earlier, and -0- if not placed in service in 2025 or the taxpayer elected out. Acquisitions before September 28, 2017 and low-use vehicles are excluded by refusals."
  - key: "25"
    status: MISMATCH
    reason: "The line 11 cap applies to every vehicle, including those the program treats as not subject to the limits at line 10. The instructions limit only passenger automobiles ('For any passenger automobile... cannot exceed the applicable limit'), so a heavier vehicle's allowance would be wrongly capped."
  - key: "17"
    status: MATCH
    reason: "This agrees with worksheet line 17, 'Subtract line 16 from line 11', with -0- when line 16 is larger, consistent with the worksheet's stop note."
  - key: "18"
    status: MATCH
    reason: "This agrees with worksheet line 18, 'Subtract line 16 from line 15'."
  - key: "19"
    status: MISMATCH
    reason: "The in-recovery branches agree with 'Multiply line 18 by line 6' and the half-year and mid-quarter tables, but a 2019 vehicle gets zero with no other computation shown. The instructions say, 'If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any, in column (h)', subject to the annual limit."
  - key: "20"
    status: MISMATCH
    reason: "The formula matches 'Enter the lesser of line 17 or line 19', but it yields zero for a 2019 vehicle even though Pub. 946 says 'you can deduct that unrecovered basis after the recovery period ends'. It also applies the line 17 limit to vehicles outside the 'Limits for passenger automobiles'."
```
```
