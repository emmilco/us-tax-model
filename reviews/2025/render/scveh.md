# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fca791ca88a08e3788c1c72c0e83aea2e256f2ecb27cede0cb2db8a45809a55a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7abd522bb45beed38ca4fc7a89f8396f00d00202ca111a9ed0ef64d93db512cb |
| lines judged | 27 |
| match / mismatch / unclear / missing | 21 / 6 / 0 / 0 |
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

Model: The Schedule C line 44b instructions define commuting as "travel between your home and a work location." For a vehicle converted during the year they say to "enter your commuting miles only for the period you drove your vehicle for business," which the restatement reproduces.
Reviewed in: pass f7924f6e6504

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

Model: For the standard mileage rate, the instructions say "Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls". For actual expenses, line 9 takes "the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc." The five-vehicle and earlier-use limits are handled by the helper refusals.
Reviewed in: pass f7924f6e6504

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before, or it was converted bet
Status: **MATCH**

Model: The screen reflects "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle." The added question about a 2025 conversion only narrows the tool, and the lease_business refusal names that exclusion.
Reviewed in: pass f7924f6e6504

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The restatement enters the full business portion of the lease payments and never applies the inclusion amount, and no refusal covers it. The IRS text says "if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount."

Ruling: scope; An inclusion amount for leased property is refused for the business through sc.special ("an inclusion amount for leased property"), so the business portion of the lease payments is the line 20a amount for every vehicle that reaches it. The model's "no refusal covers it" is wrong. Same point as the deepseek refresh-round ruling.
Reviewed in: pass f7924f6e6504

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: The restatement records only a year from 2019 to 2025, but Form 4562 Part V asks for the full date: "Column (b)—Date placed in service. Enter the date the property was placed in service. If property held for personal use is converted to business/investment use, treat the property as placed in service on the date of conversion."

Ruling: representation; same restatement and objection as the refresh-round ruling. The tool needs the year (and, for 2025 property, the quarter, asked separately) to choose the tables and limits; no value depends on the month or day otherwise. A vehicle converted from personal use in 2025 is refused by scveh.screen.
Reviewed in: pass f7924f6e6504

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MATCH**

Model: The screen only narrows scope. Its items follow the given text: the Form 4562 line 14 exceptions (section 168(k)(9)(A)/(B), ADS, conversions), qualified business use exclusions ('Leasing the property to a 5% owner or related person if the value related to such usage is not reported as income'), the noncorporate lessor tests, the tax-exempt, governmental and foreign-use exceptions, the records requirement, casualty basis reductions, short tax years, trade-ins and original use. The refusal on column (d) names these exclusions.
Reviewed in: pass 7790431cc057

### (d) — Cost or other basis
Status: **MATCH**

Model: This matches i4562 column (d), 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation),' with the smaller of adjusted basis or FMV for conversions. It also matches Pub. 463: cost 'includes sales taxes..., destination charges, and dealer preparation' and is decreased by 'gas guzzler tax'. Section 179 is correctly left for column (e), and credit reductions are screened out.
Reviewed in: pass 7790431cc057

### 13 — Business/investment cost (cost times business use)
Status: **MISMATCH**

Restated: Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply column (d) by the result.

Model: The restatement multiplies column (d) by the business-use percentage. That is the first step of Form 4562 column (e) ('Multiply column (d) by the percentage in column (c)'), not 'Depreciation and section 179 expense deduction' as Schedule C line 13 requires. It omits the section 179 and special-allowance subtraction, the column (h) depreciation rate ('follow the instructions for line 19, column (g)'), and the passenger automobile limits ('cannot exceed the applicable limit shown in Table 1, 2, 3, or 4').

Ruling: model error; p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13, "Multiply line 12 by line 8. This is your business/investment cost" (the line's cite). The printed handle 13 is that worksheet line, not Schedule C line 13; the depreciation rate, section 179 and special-allowance subtraction and the automobile limits are on the project's later worksheet lines (column (h), scveh.macrs). The restatement states the line. Project stands.
Reviewed in: pass 7790431cc057

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: The i4562 election out applies "for any class of property ... for all such property in such class". A choice that differs within the 5-year class is refused.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Worksheet line 7 is the maximum deduction from the Pub. 946 table. For a 2025 vehicle that is $20,200 with the special allowance and $12,200 without it (footnote 1). Earlier vehicles use their year-of-recovery entry.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MISMATCH**

Restated: Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 7 by the result.

Model: Worksheet line 9 is "Multiply line 7 by line 8," and line 8 is the business/investment-use percentage. For an owned vehicle converted in 2025, that percentage must use the months fraction ("Multiply that percentage by the number of months you use the property in your business ... and divide the result by 12"). The restatement uses whole-year business miles over total miles, which gives a different value.

Ruling: scope; as worksheet line 13: the months proration applies only to a vehicle converted in 2025, refused by scveh.screen; otherwise line 9 is line 7 times the business-use percentage. Project stands.
Reviewed in: pass f7924f6e6504

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: This follows worksheet line 10: "Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service." The cap at line 9 applies to passenger automobiles, which is when the worksheet limits apply.
Reviewed in: pass f7924f6e6504

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

### (i) — Column (i): elected section 179 cost of this vehicle
Status: **MATCH**

Model: Column (i) says "Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use (subject to the limits for passenger automobiles)." The restatement takes line 10, which is the election capped by the passenger-automobile limit. Low business use is refused, and the $31,300 SUV cap and the business-cost cap are enforced through refusals.
Reviewed in: pass f7924f6e6504

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 43 | 653bdae1d00d54a8d0e502e8af68db95ad1303fb72a32c6351af88bf712d8ad9 |
| 44a | 146e16db3d74cebceb6b516ed6bb866cf35b480210cddeb836faf76b938c1111 |
| 44b | 912a0646daf46af54d73f00939094e22a3a6afcc364df5e2217b9d0c63ecdc85 |
| 44c | 1b5eb777d9f95e6354b469528f86cf17ecd87a5ca3790f73cb02264e7986557c |
| (screen) (scveh.smr_ok) | 46b635c544800b328e90dea9151300dcc66a54a49a073c67ac61a45be02b9236 |
| (screen) (scveh.employee_use) | 643c015b12e980ff10a568580ea8efa7789a30b1a2cf4fd3e81007f0b717da5c |
| 9 (scveh.line9) | 5d6585aa42f1558d281bc21fd242d8d136b0432b35c7e6268b8eca450f0c3d03 |
| (screen) (scveh.lease_smr_before) | 3b7b3aabbc6c5d31b1c98695ea76b5ebda1e48236a80be3d7d009a3c51d93807 |
| 20a | bdae3ad9304c24d80874654c5098bdea7b7b46c534edf85e944e4f3a456df4ad |
| (b) | 3d1072852e40be84db47283401be422fb858a0c61b8ba666b2b967fbc82bb104 |
| (screen) (scveh.screen) | 2e4c203329b67946eaadee7b40d5e5a5efe193ef6fa98aa7f2b0b14fcb000144 |
| (d) | 08427331c7ae9558829419cdbb0913d4bebf8f41d9028fcc1383858dbb1a1fd9 |
| 13 | 392f341557b6cc28e59c9ebf8308e0364afc87e1a3c66a6f5df892433fd21133 |
| (screen) (scveh.bonus_same) | bcc0a3d54012fab053eedd53cdfdd1d7d0a471c32654babe2b00b4cf3cc2d878 |
| 7 | 7abf8db58a329d5016a0adcdd95e4c171494f2cfa2c13c57c7e54b1b2b5b52c5 |
| 9 (scveh.line9w) | d456efa786a3ce1221cc59286357f5c111d0c4c34d469456b480450792d994f4 |
| 10 | 589d91da44efb134d4b5927ff415b6ed942501fcb1cbb14ae23dbb986448e02c |
| 11 | c251a67e80a7ae5b87a09491a97732e13a0ad6f5b6546240351ec3b1aa545148 |
| 14 | 2f3e0ff547054de12f2e2311a07f5424fdcdd40990b41183a2a7839d31afda9e |
| 15 | a460f2a57dfea4f6813be6b9396fe1447868deb1ef32883ea94cc76d9516938c |
| 16 | d681606b31a260ca767d93260165221287ebb8b675271d1a6a0ac85e8f27b547 |
| 25 | 09b526c3e2bfdef7107fade957b43cd30706c2b3b335d8fe2c5109edc2ca9d51 |
| 17 | fc975993c0b947311ad7309e5133ef9bf5d4c91a95ce22d614c92c48402c61af |
| 18 | 1433c848ce00876f117ce1f917f38006e3920a8385ffd823f98ec13b0287db87 |
| 19 | e0b0040e611610107f13e8fbfc3724388721d42414f77a656df7e24694bf77f8 |
| 20 | 0f5f8fb24b71f5f7b6554a14f6c9dff7910f7ff7b48be987895cec7827fb7609 |
| (i) | 966d5d0067ae17da45b260faab5b188cf09c9006b88dc957a68ffc92a2ace594 |
| (rest of the document) | 0d3a516739bb4c8544a0dd5b10f1356f4404d87199552357356aeea4cca5155d |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 7790431cc057

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (screen) (scveh.screen), (d), 13 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 7790431cc0571127e26cf3f38c496526895ba92630753e855f808edfc01811f8 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 12d53698e1663e72a7bc327c42b631f778d2e2bcaabbd1d9bd454da956bc193d |
| receipt | .transcription/scveh.render.lines-ce6853f5a230 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 2 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 37, 60, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 37, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |

##### Raw response

```yaml
```yaml
lines:
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The screen only narrows scope. Its items follow the given text: the Form 4562 line 14 exceptions (section 168(k)(9)(A)/(B), ADS, conversions), qualified business use exclusions ('Leasing the property to a 5% owner or related person if the value related to such usage is not reported as income'), the noncorporate lessor tests, the tax-exempt, governmental and foreign-use exceptions, the records requirement, casualty basis reductions, short tax years, trade-ins and original use. The refusal on column (d) names these exclusions."
  - key: "(d)"
    status: MATCH
    reason: "This matches i4562 column (d), 'actual cost (including sales tax) or other basis (unadjusted for prior years' depreciation),' with the smaller of adjusted basis or FMV for conversions. It also matches Pub. 463: cost 'includes sales taxes..., destination charges, and dealer preparation' and is decreased by 'gas guzzler tax'. Section 179 is correctly left for column (e), and credit reductions are screened out."
  - key: "13"
    status: MISMATCH
    reason: "The restatement multiplies column (d) by the business-use percentage. That is the first step of Form 4562 column (e) ('Multiply column (d) by the percentage in column (c)'), not 'Depreciation and section 179 expense deduction' as Schedule C line 13 requires. It omits the section 179 and special-allowance subtraction, the column (h) depreciation rate ('follow the instructions for line 19, column (g)'), and the passenger automobile limits ('cannot exceed the applicable limit shown in Table 1, 2, 3, or 4')."
```
```

#### Pass f7924f6e6504

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 44b, 9 (scveh.line9), (screen) (scveh.lease_smr_before), 20a, (b), 13, 9 (scveh.line9w), 10, (i) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f7924f6e65046f1ad23aa995ab386cce5fc7878c2814beadbf6c2fb15f733338 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c8ff25bcc798b2df3655d4705aa860b451507cf40b1315021f6d9d406fd1feee |
| receipt | .transcription/scveh.render.lines-8dde75720f89 |
| lines judged | 9 |
| match / mismatch / unclear / missing | 5 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 31, 37, 60, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 37, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |

##### Raw response

```yaml
```yaml
lines:
  - key: "44b"
    status: MATCH
    reason: "The Schedule C line 44b instructions define commuting as \"travel between your home and a work location.\" For a vehicle converted during the year they say to \"enter your commuting miles only for the period you drove your vehicle for business,\" which the restatement reproduces."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "For the standard mileage rate, the instructions say \"Multiply the number of business miles driven by 0.70 ... Add to this amount your parking fees and tolls\". For actual expenses, line 9 takes \"the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.\" The five-vehicle and earlier-use limits are handled by the helper refusals."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "The screen reflects \"You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle.\" The added question about a 2025 conversion only narrows the tool, and the lease_business refusal names that exclusion."
  - key: "20a"
    status: MISMATCH
    reason: "The restatement enters the full business portion of the lease payments and never applies the inclusion amount, and no refusal covers it. The IRS text says \"if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount.\""
  - key: "(b)"
    status: MISMATCH
    reason: "The restatement records only a year from 2019 to 2025, but Form 4562 Part V asks for the full date: \"Column (b)—Date placed in service. Enter the date the property was placed in service. If property held for personal use is converted to business/investment use, treat the property as placed in service on the date of conversion.\""
  - key: "13"
    status: MISMATCH
    reason: "Worksheet line 13 multiplies line 12 by line 8, the business/investment-use percentage. For a vehicle converted from personal use during the year, Form 4562 column (c) and Pub. 463 say to \"figure the percentage of business/investment use only for the number of months you use the property in your business ... Multiply that percentage by the number of months ... and divide the result by 12.\" The restatement instead uses whole-year business miles over total miles, and conversions of owned vehicles are not refused. (This assumes \"13\" is worksheet line 13, the business/investment cost; it is not Schedule C line 13.)"
  - key: "9 (scveh.line9w)"
    status: MISMATCH
    reason: "Worksheet line 9 is \"Multiply line 7 by line 8,\" and line 8 is the business/investment-use percentage. For an owned vehicle converted in 2025, that percentage must use the months fraction (\"Multiply that percentage by the number of months you use the property in your business ... and divide the result by 12\"). The restatement uses whole-year business miles over total miles, which gives a different value."
  - key: "10"
    status: MATCH
    reason: "This follows worksheet line 10: \"Section 179 deduction claimed this year (not more than line 9). Enter -0- if this is not the year you placed the car in service.\" The cap at line 9 applies to passenger automobiles, which is when the worksheet limits apply."
  - key: "(i)"
    status: MATCH
    reason: "Column (i) says \"Enter the amount you elect to expense for section 179 property used more than 50% in a qualified business use (subject to the limits for passenger automobiles).\" The restatement takes line 10, which is the election capped by the passenger-automobile limit. Low business use is refused, and the $31,300 SUV cap and the business-cost cap are enforced through refusals."
```
```

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
