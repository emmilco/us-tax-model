# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d429bc33fb4aca749b275d2eb6dc58116ae60ef44ff7c3308532f91e3c1179c8 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7e2c86a963dca5741dfde9e9633733a25c00704f6fd7dd34c66d6724182eb0e2 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 17 / 8 / 0 / 0 |
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

Model: The form asks for a full date: 'When did you place your vehicle in service for business purposes? (month/day/year)'. The restatement collects only the year, so it cannot supply the entry the line asks for.

Ruling: representation; restatement accepted. The tool needs the year (and, for 2025 property, the quarter) to choose the tables and limits; the filer writes the full date on Schedule C line 43 and Form 4562 from their own records. No value depends on the month or day except through the quarter, which is asked separately.

### 44a — Business miles
Status: **MATCH**

Model: Schedule C line 44a asks for the 2025 miles the vehicle was used for 'Business', and the restatement asks for the same miles, excluding commuting.

### 44b — Commuting miles
Status: **MATCH**

Model: This is the commuting miles entry and it defers to the line 44b instructions. The restatement does not itself state the rule for a vehicle converted during the year ('enter your commuting miles only for the period you drove your vehicle for business'), but it points to the instructions containing that rule.

### 44c — Other miles
Status: **MATCH**

Model: Line 44c asks for 'Other' miles driven during 2025, and the restatement asks for the other (personal) miles.

### (screen) (scveh.smr_ok) — May you use the standard mileage rate for this vehicle?
Status: **MATCH**

Model: The screen tracks the instructions: owned and 'used the standard mileage rate for the first year', leased and using it 'for the entire lease period', and actual expenses required for 'five or more vehicles simultaneously'.

### 9 (scveh.line9) — Car and truck expenses for this vehicle
Status: **MISMATCH**

Restated: Choose — [helper "Standard mileage rate or actual expenses" = 'standard' → helper "Standard mileage amount plus parking fees and tolls"] [helper "Standard mileage rate or actual expenses" = 'actual' → helper "Business portion of the operating expenses plus parking fees and tolls"]

Model: The standard branch (miles × $0.70 plus parking and tolls) and the actual branch match the instructions, but nothing blocks the actual branch for a leased vehicle with earlier standard mileage use. The IRS text says 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.'

Ruling: refusal located elsewhere; restatement accepted. A vehicle for which the standard mileage rate was used in an earlier year, leased or owned, is refused through scveh.screen ('you used the standard mileage rate for it in an earlier year'), so a leased vehicle that reaches actual expenses has never used the standard rate.

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the business portion of the lease payments with no adjustment or refusal for the inclusion amount. The instructions say 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.'

Ruling: refusal located elsewhere; restatement accepted. An inclusion amount for leased property is refused for the business through sc.special ('an inclusion amount for leased property'), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it.

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: Column (b) says 'Enter the date the property was placed in service', but the restatement collects only the year. The 2019 to 2025 limit and the refusal for 50% or less business use (line 27) are acceptable narrowings.

Ruling: representation; restatement accepted. As line 43: the year chooses the recovery year and the limits, the quarter (asked separately) the mid-quarter table; the filer enters the full date on Form 4562 column (b).

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: This is a scope screen that routes the listed cases out of the tool, including trade-ins, vehicle credits, conversions, for-hire vehicles, ambulances and hearses. It does not conflict with the text, and the refusal on column (d) names what is excluded.

### (d) — Cost or other basis
Status: **MATCH**

Model: It matches 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)' and the smaller-of rule for converted property. Not reducing basis by section 179 follows the worksheet line 12 footnote, and the credit reductions are excluded by the screen refusal.

### 13 — Business/investment cost (cost times business use)
Status: **MATCH**

Model: Worksheet line 13 says 'Multiply line 12 by line 8', and column (c) defines the percentage as business miles divided by total miles for all purposes. The restatement multiplies column (d) by that ratio.

### (i) — Elected section 179 cost
Status: **MATCH**

Model: Column (i) says 'Enter the amount you elect to expense', and the restatement asks for that elected amount. The limits on it are applied through line 10 and its refusal.

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property' to 'all such property in such class placed in service during the tax year'. The screen sends differing choices to a named refusal, which is an acceptable narrowing.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]

Model: The table lookups match for passenger automobiles ($20,200 with the allowance, $12,200 without, and the later-year amounts), but line 7 has no branch for a vehicle outside those limits, although line 10 does. The limits apply to 'any passenger automobile', and the worksheet is the 'Depreciation Worksheet for Passenger Automobiles', so a heavier vehicle is given a limit that does not apply to it.

Ruling: representation; restatement accepted. Line 7 is a line of the Pub. 946 worksheet for passenger automobiles and is shown for every vehicle, but it limits only a passenger automobile: for a vehicle that is not one, the special allowance, the section 179 deduction and MACRS take the scveh.passenger = false branches, which do not read it (checked: a $60,000 truck placed in service in 2025 with the 100% allowance gets $60,000, a passenger automobile $20,200).

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MATCH**

Model: Worksheet line 9 says 'Multiply line 7 by line 8', and the restatement multiplies line 7 by the business-mile ratio that column (c) prescribes.

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MISMATCH**

Restated: Choose — [helper "Placed in service in 2025" = true → helper "Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile"] [helper "Placed in service in 2025" = false → helper "Zero"]

Model: The line 9 cap and the zero for later years match, but the SUV test behind the $31,300 refusal drops a required element of the third exception, so a vehicle lacking that element can avoid the cap. The IRS exception requires a vehicle that 'has an integral enclosure fully enclosing the driver compartment and load carrying device' as well as the seating and 30-inch conditions.

Ruling: ambiguity — owner accepted (T-046, 2026-11-01): line 10 takes the section 179 amount elected for the vehicle, not the part deducted after the business income limit (amb.2025.vehicle_s179_claimed). The reviewer's other reading is the recorded competing one.

### 11 — Subtract line 10 from line 9
Status: **MATCH**

Model: Worksheet line 11 says 'Subtract line 10 from line 9', and the restatement does the same with a floor of zero.

### 14 — Section 179 deduction claimed in the year you placed the car in service
Status: **MATCH**

Model: Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. The restatement uses line 10 for a 2025 vehicle and the amount claimed in the earlier year otherwise.

### 15 — Tentative basis for depreciation (line 13 less line 14)
Status: **MATCH**

Model: Worksheet line 15 says 'Subtract line 14 from line 13', and the restatement does the same.

### 16 — Special depreciation allowance
Status: **MATCH**

Model: Line 16 multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero if elected out or not placed in service in 2025. The not-qualified case has no separate branch and depends on the filer's answer to the allowance question.

### 25 — Special depreciation allowance allowed (not more than line 11)
Status: **MISMATCH**

Restated: Enter the smaller of line 16 or line 11.

Model: Capping at line 11 is right for a passenger automobile, but the restatement also caps vehicles outside the limits, because line 11 derives from the ungated line 7. The text says 'This special depreciation allowance is included in the overall limit on depreciation and section 179 expense deduction for passenger automobiles', and the limits apply to vehicles 'rated at 6,000 pounds unloaded gross vehicle weight or less'.

Ruling: representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: the vehicle's special allowance (scveh.bonus_v) takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass, the passenger-automobile route. A vehicle that is not a passenger automobile is not limited.

### 17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **MATCH**

Model: Worksheet line 17 says 'Subtract line 16 from line 11', and the restatement does the same with a floor of zero.

### 18 — Basis for depreciation (line 15 less line 16)
Status: **MATCH**

Model: Worksheet line 18 says 'Subtract line 16 from line 15', and the restatement does the same with a floor of zero.

### 19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **MATCH**

Model: Worksheet line 19 says 'Multiply line 18 by line 6', using the 5-year table rate for the convention and recovery year, and the mid-quarter test (more than 40%) matches the instructions. Zero for a 2019 vehicle is consistent because the recovery period ended in 2024 and the 5-year tables have no year 7.

### 20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **MISMATCH**

Restated: Enter the smaller of line 17 or line 19.

Model: The worksheet's 'lesser of line 17 or line 19' is followed, but line 17 carries the passenger automobile limit into vehicles outside those limits. A 2019 vehicle also gets zero here, while column (h) says 'enter your unrecovered basis, if any', and no listed line or refusal shows that amount being handled.

Ruling: representation; project retained. The automobile worksheet lines are figured for every vehicle but read only for a passenger automobile: the vehicle's special allowance (scveh.bonus_v) takes line 25 only when scveh.passenger is true and line 16 otherwise, and column (h) takes line 20 only through scveh.macrs_pass, the passenger-automobile route. A vehicle that is not a passenger automobile is not limited.

## Raw response

```yaml
```yaml
lines:
  - key: "43"
    status: MISMATCH
    reason: "The form asks for a full date: 'When did you place your vehicle in service for business purposes? (month/day/year)'. The restatement collects only the year, so it cannot supply the entry the line asks for."
  - key: "44a"
    status: MATCH
    reason: "Schedule C line 44a asks for the 2025 miles the vehicle was used for 'Business', and the restatement asks for the same miles, excluding commuting."
  - key: "44b"
    status: MATCH
    reason: "This is the commuting miles entry and it defers to the line 44b instructions. The restatement does not itself state the rule for a vehicle converted during the year ('enter your commuting miles only for the period you drove your vehicle for business'), but it points to the instructions containing that rule."
  - key: "44c"
    status: MATCH
    reason: "Line 44c asks for 'Other' miles driven during 2025, and the restatement asks for the other (personal) miles."
  - key: "(screen) (scveh.smr_ok)"
    status: MATCH
    reason: "The screen tracks the instructions: owned and 'used the standard mileage rate for the first year', leased and using it 'for the entire lease period', and actual expenses required for 'five or more vehicles simultaneously'."
  - key: "9 (scveh.line9)"
    status: MISMATCH
    reason: "The standard branch (miles × $0.70 plus parking and tolls) and the actual branch match the instructions, but nothing blocks the actual branch for a leased vehicle with earlier standard mileage use. The IRS text says 'You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.'"
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the business portion of the lease payments with no adjustment or refusal for the inclusion amount. The instructions say 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.'"
  - key: "(b)"
    status: MISMATCH
    reason: "Column (b) says 'Enter the date the property was placed in service', but the restatement collects only the year. The 2019 to 2025 limit and the refusal for 50% or less business use (line 27) are acceptable narrowings."
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "This is a scope screen that routes the listed cases out of the tool, including trade-ins, vehicle credits, conversions, for-hire vehicles, ambulances and hearses. It does not conflict with the text, and the refusal on column (d) names what is excluded."
  - key: "(d)"
    status: MATCH
    reason: "It matches 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation)' and the smaller-of rule for converted property. Not reducing basis by section 179 follows the worksheet line 12 footnote, and the credit reductions are excluded by the screen refusal."
  - key: "13"
    status: MATCH
    reason: "Worksheet line 13 says 'Multiply line 12 by line 8', and column (c) defines the percentage as business miles divided by total miles for all purposes. The restatement multiplies column (d) by that ratio."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) says 'Enter the amount you elect to expense', and the restatement asks for that elected amount. The limits on it are applied through line 10 and its refusal."
  - key: "(screen) (scveh.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property' to 'all such property in such class placed in service during the tax year'. The screen sends differing choices to a named refusal, which is an acceptable narrowing."
  - key: "7"
    status: MISMATCH
    reason: "The table lookups match for passenger automobiles ($20,200 with the allowance, $12,200 without, and the later-year amounts), but line 7 has no branch for a vehicle outside those limits, although line 10 does. The limits apply to 'any passenger automobile', and the worksheet is the 'Depreciation Worksheet for Passenger Automobiles', so a heavier vehicle is given a limit that does not apply to it."
  - key: "9 (scveh.line9w)"
    status: MATCH
    reason: "Worksheet line 9 says 'Multiply line 7 by line 8', and the restatement multiplies line 7 by the business-mile ratio that column (c) prescribes."
  - key: "10"
    status: MISMATCH
    reason: "The line 9 cap and the zero for later years match, but the SUV test behind the $31,300 refusal drops a required element of the third exception, so a vehicle lacking that element can avoid the cap. The IRS exception requires a vehicle that 'has an integral enclosure fully enclosing the driver compartment and load carrying device' as well as the seating and 30-inch conditions."
  - key: "11"
    status: MATCH
    reason: "Worksheet line 11 says 'Subtract line 10 from line 9', and the restatement does the same with a floor of zero."
  - key: "14"
    status: MATCH
    reason: "Worksheet line 14 is the 'Section 179 deduction claimed in the year you placed the car in service'. The restatement uses line 10 for a 2025 vehicle and the amount claimed in the earlier year otherwise."
  - key: "15"
    status: MATCH
    reason: "Worksheet line 15 says 'Subtract line 14 from line 13', and the restatement does the same."
  - key: "16"
    status: MATCH
    reason: "Line 16 multiplies line 15 by the applicable percentage: 100% if acquired after January 19, 2025, 40% if acquired earlier or if the 40% election is made, and zero if elected out or not placed in service in 2025. The not-qualified case has no separate branch and depends on the filer's answer to the allowance question."
  - key: "25"
    status: MISMATCH
    reason: "Capping at line 11 is right for a passenger automobile, but the restatement also caps vehicles outside the limits, because line 11 derives from the ungated line 7. The text says 'This special depreciation allowance is included in the overall limit on depreciation and section 179 expense deduction for passenger automobiles', and the limits apply to vehicles 'rated at 6,000 pounds unloaded gross vehicle weight or less'."
  - key: "17"
    status: MATCH
    reason: "Worksheet line 17 says 'Subtract line 16 from line 11', and the restatement does the same with a floor of zero."
  - key: "18"
    status: MATCH
    reason: "Worksheet line 18 says 'Subtract line 16 from line 15', and the restatement does the same with a floor of zero."
  - key: "19"
    status: MATCH
    reason: "Worksheet line 19 says 'Multiply line 18 by line 6', using the 5-year table rate for the convention and recovery year, and the mid-quarter test (more than 40%) matches the instructions. Zero for a 2019 vehicle is consistent because the recovery period ended in 2024 and the 5-year tables have no year 7."
  - key: "20"
    status: MISMATCH
    reason: "The worksheet's 'lesser of line 17 or line 19' is followed, but line 17 carries the passenger automobile limit into vehicles outside those limits. A 2019 vehicle also gets zero here, while column (h) says 'enter your unrecovered basis, if any', and no listed line or refusal shows that amount being handled."
```
```
