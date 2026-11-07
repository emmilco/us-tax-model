# Render comparison — scveh

The rendered English of every printed line of `Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` (`rendered/2025/scveh.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 3 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | fca791ca88a08e3788c1c72c0e83aea2e256f2ecb27cede0cb2db8a45809a55a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: IRS line 43 asks "When did you place your vehicle in service for business purposes? (month/day/year)"; the restatement asks only for the year.

Ruling: representation; same as the earlier ruling. The tool needs the year (and, for 2025 property, the quarter); the filer writes the full date on Schedule C line 43 from their own records.

### 44a — Business miles
Status: **MATCH**

Model: Matches the business miles requested on line 44a, excluding commuting.

### 44b — Commuting miles
Status: **MATCH**

Model: The restatement matches the line 44b instruction, including limiting commuting miles to the business-use period for a vehicle converted during the year.
Reviewed in: pass f7924f6e6504

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

Model: The standard branch uses business miles times the 0.70 rate plus parking and tolls; the actual branch uses the business portion of operating expenses plus parking and tolls and leaves depreciation and lease payments to lines 13 and 20a.
Reviewed in: pass f7924f6e6504

### (screen) (scveh.lease_smr_before) — The standard mileage rate was used for this leased vehicle before, or it was converted bet
Status: **MATCH**

Model: The prior standard-mileage-use condition matches the rule that actual expenses cannot be used for a leased vehicle after using the standard mileage rate; the converted-vehicle case is expressly excluded as outside the tool.
Reviewed in: pass f7924f6e6504

### 20a — Rent or lease of this vehicle (business portion)
Status: **MISMATCH**

Restated: Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]

Model: The IRS says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement computes only the business portion of lease payments and omits that reduction.

Ruling: scope; same as the refresh-round ruling: an inclusion amount for leased property is refused for the business through sc.special, so line 20a is the business portion of the lease payments on every vehicle that reaches it.
Reviewed in: pass f7924f6e6504

### (b) — Year placed in service
Status: **MISMATCH**

Restated: Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)

Model: The IRS column (b) instruction says 'Enter the date the property was placed in service' and treats converted property as placed in service on the conversion date; the restatement asks only for the year.

Ruling: representation; same as the refresh-round ruling: no value depends on the month or day except through the quarter, asked separately.
Reviewed in: pass f7924f6e6504

### (screen) (scveh.screen) — Does any of these apply to this vehicle?
Status: **MISMATCH**

Restated: Input — Does any of these apply to this vehicle?

- you placed it in service before 2019
- you claimed a special depreciation allowance for it in an earlier year
- you used the standard mileage rate for it in an earlier year
- you disposed of it in 2025
- you made a substantial improvement to it in 2025 or an earlier year (such as adding air conditioning or a new engine)
- you used it in 2025 for investment, that is, for the production of income outside your trade or business
- you acquired it in a trade-in or from a related person
- you placed it in service in 2025 but acquired it before September 28, 2017
- its business use was 50% or less in any earlier year
- it is an electric vehicle placed in service before 2007
- you reduced its basis by a clean-fuel deduction or a vehicle credit
- you converted it from personal use to business use during 2025
- you use it in your business of transporting persons or property for hire, or it is an ambulance or hearse
- you converted it from business use to personal use during 2025
- you acquired it in an involuntary conversion or a like-kind exchange
- you must depreciate it under ADS (for example, it is used predominantly outside the United States), or you elected ADS, the straight line method or the 150% declining balance method for it
- you reduced its basis because of a casualty
- your 2025 tax year, or any tax year since you placed it in service, is shorter than 12 months
- you are regularly engaged in the business of leasing passenger automobiles
- you are not a corporation and you purchased it and lease it to others, unless you manufactured or produced it, or the lease term (including options to renew) is less than 50% of its class life and for the first 12 months after the transfer to the lessee your business deductions for it (other than rents and reimbursed amounts) are more than 15% of its rental income
- it is used by a tax-exempt organization, unless used in connection with the production of income subject to the tax on unrelated trade or business income
- it is used by a governmental unit or a foreign person or entity, unless used under a lease with a term of less than 6 months
- you cannot prove its business use with adequate records or with sufficient evidence to support your own statements
- you claim a special depreciation allowance for it in 2025 and its original use did not begin with you (original use is the first use to which the vehicle is put, whether or not by you, so a vehicle someone else used before you acquired it is used property, and so is a reconditioned or rebuilt vehicle you acquired unless the cost of its used parts is not more than 20% of its total cost)
- you claim a special depreciation allowance for it in 2025 and it is property described in section 168(k)(9)(A) or 168(k)(9)(B), that is:
  - property primarily used in a trade or business of furnishing or selling electrical energy, water or sewage disposal services, gas or steam through a local distribution system, or transportation of gas or steam by pipeline, whose rates are established or approved by a State or political subdivision, an agency or instrumentality of the United States, a public service or public utility commission or similar body of a State or political subdivision, or the governing or ratemaking body of an electric cooperative
  - property used in a trade or business that has had floor plan financing indebtedness (a loan used to buy motor vehicles, boats, farm machinery or equipment, or trailers or campers held for sale or lease, and secured by them) whose interest was taken into account under section 163(j)(1)(C) in figuring the business interest expense limit
- its qualified business use is 50% or less once you leave out uses that are not qualified business use:
  - investment use
  - leasing it to a 5% owner or related person, or using it as compensation for services of a 5% owner or related person, unless for the lease the value is reported as income to that person
  - using it as compensation for services of anyone else unless an amount is included in that person's income for the use and any required income tax was withheld
  - use that is nondeductible under section 274

Model: The screen treats 'an electric vehicle placed in service before 2007' as a special case, but the IRS text defines the special electric-vehicle category as 'vehicles produced by an original equipment manufacturer and designed to run primarily on electricity, placed in service after August 5, 1997, and before January 1, 2007'; the lower date and design/OEM limits are omitted.

Ruling: representation (a screen wider than the source); i4562 p. 15 and p946 p. 60 define the electric-vehicle category as vehicles produced by an original equipment manufacturer, designed to run primarily on electricity and placed in service after August 5, 1997, and before 2007. The screen item "it is an electric vehicle placed in service before 2007" refuses every such vehicle and more; any vehicle placed in service before 2007 is also refused by the first item ("you placed it in service before 2019"). A wider refusal changes no computed amount. The item's wording is unchanged by the R3 restructuring. Project stands.
Reviewed in: pass 5e6c27f2bfbb

### (d) — Cost or other basis
Status: **MATCH**

Model: Matches Form 4562 Part V column (d): actual cost (including sales tax; Pub. 463 adds destination charges and dealer preparation) or other basis unadjusted for prior depreciation, with converted property using the lesser of adjusted basis or FMV, and Pub. 463's gas guzzler tax reduction.
Reviewed in: pass 7790431cc057

### 13 — Business/investment cost (cost times business use)
Status: **MISMATCH**

Restated: Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply column (d) by the result.

Model: The IRS line is 'Depreciation and section 179 expense deduction'; the restatement instead computes Form 4562 Part V column (e), 'Basis for depreciation (business/investment use only),' by multiplying column (d) by business-use percentage, omitting the depreciation rate and passenger automobile limits.

Ruling: model error; p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13, "Multiply line 12 by line 8. This is your business/investment cost". The handle 13 is that worksheet line, not Schedule C line 13; depreciation and the automobile limits are on later worksheet lines (scveh.macrs). Same point as the Claude ruling of this line. Project stands.
Reviewed in: pass 7790431cc057

### (screen) (scveh.bonus_same) — Is the choice the same for all 5-year property placed in service in 2025?
Status: **MATCH**

Model: Matches the requirement that the special allowance election be consistent for the class of 5-year property placed in service in 2025.

### 7 — Maximum depreciation deduction for this year from the appropriate table
Status: **MATCH**

Model: Matches the maximum depreciation limit for the vehicle's applicable year from the passenger automobile table.

### 9 (scveh.line9w) — Adjusted maximum depreciation deduction (line 7 times the business/investment-use percenta
Status: **MISMATCH**

Restated: Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 7 by the result.

Model: Worksheet line 9 multiplies line 7 by the business/investment-use percentage; for a converted vehicle that percentage must be prorated by the months used in business, which the restatement's business-miles/total-miles calculation omits.

Ruling: scope; as line 13: a vehicle converted in 2025 is refused by scveh.screen, so line 7 times the business-use percentage is the whole supported case. Project stands.
Reviewed in: pass f7924f6e6504

### 10 — Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
Status: **MATCH**

Model: The restatement says to enter zero if the vehicle was not placed in service in 2025 and otherwise not more than line 9 for a passenger automobile, matching the worksheet line 10 instruction.
Reviewed in: pass f7924f6e6504

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

### (i) — Column (i): elected section 179 cost of this vehicle
Status: **MATCH**

Model: The restatement takes column (i) from line 10 for owned actual-expense vehicles and zero otherwise, matching the elected section 179 cost for listed property subject to the passenger-automobile limits.
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
| (screen) (scveh.screen) | 8e05c51fb73208ef560cbdf7d2afcaf4eec521001c018878bc47a2a6a66e189c |
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
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7790431cc0571127e26cf3f38c496526895ba92630753e855f808edfc01811f8 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 12d53698e1663e72a7bc327c42b631f778d2e2bcaabbd1d9bd454da956bc193d |
| receipt | .transcription/scveh.deepseek.render.lines-ce6853f5a230 |
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
lines:
  - key: "(screen) (scveh.screen)"
    status: MATCH
    reason: "The listed conditions correspond to IRS exclusions and complications (prior standard mileage, ADS/straight line/150% DB, listed property 50% or less, insufficient records, special-allowance exceptions), so the program's screen is a permissible narrowing and names the excluded cases."
  - key: "(d)"
    status: MATCH
    reason: "Matches Form 4562 Part V column (d): actual cost (including sales tax; Pub. 463 adds destination charges and dealer preparation) or other basis unadjusted for prior depreciation, with converted property using the lesser of adjusted basis or FMV, and Pub. 463's gas guzzler tax reduction."
  - key: "13"
    status: MISMATCH
    reason: "The IRS line is 'Depreciation and section 179 expense deduction'; the restatement instead computes Form 4562 Part V column (e), 'Basis for depreciation (business/investment use only),' by multiplying column (d) by business-use percentage, omitting the depreciation rate and passenger automobile limits."
```

#### Pass f7924f6e6504

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 44b, 9 (scveh.line9), (screen) (scveh.lease_smr_before), 20a, (b), 13, 9 (scveh.line9w), 10, (i) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f7924f6e65046f1ad23aa995ab386cce5fc7878c2814beadbf6c2fb15f733338 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c8ff25bcc798b2df3655d4705aa860b451507cf40b1315021f6d9d406fd1feee |
| receipt | .transcription/scveh.deepseek.render.lines-8dde75720f89 |
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
lines:
  - key: "44b"
    status: MATCH
    reason: "The restatement matches the line 44b instruction, including limiting commuting miles to the business-use period for a vehicle converted during the year."
  - key: "9 (scveh.line9)"
    status: MATCH
    reason: "The standard branch uses business miles times the 0.70 rate plus parking and tolls; the actual branch uses the business portion of operating expenses plus parking and tolls and leaves depreciation and lease payments to lines 13 and 20a."
  - key: "(screen) (scveh.lease_smr_before)"
    status: MATCH
    reason: "The prior standard-mileage-use condition matches the rule that actual expenses cannot be used for a leased vehicle after using the standard mileage rate; the converted-vehicle case is expressly excluded as outside the tool."
  - key: "20a"
    status: MISMATCH
    reason: "The IRS says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement computes only the business portion of lease payments and omits that reduction."
  - key: "(b)"
    status: MISMATCH
    reason: "The IRS column (b) instruction says 'Enter the date the property was placed in service' and treats converted property as placed in service on the conversion date; the restatement asks only for the year."
  - key: "13"
    status: MISMATCH
    reason: "The IRS business/investment-use percentage for converted property must be figured only for the months used in business and multiplied by months/12; the restatement simply divides annual business miles by total miles without that conversion proration."
  - key: "9 (scveh.line9w)"
    status: MISMATCH
    reason: "Worksheet line 9 multiplies line 7 by the business/investment-use percentage; for a converted vehicle that percentage must be prorated by the months used in business, which the restatement's business-miles/total-miles calculation omits."
  - key: "10"
    status: MATCH
    reason: "The restatement says to enter zero if the vehicle was not placed in service in 2025 and otherwise not more than line 9 for a passenger automobile, matching the worksheet line 10 instruction."
  - key: "(i)"
    status: MATCH
    reason: "The restatement takes column (i) from line 10 for owned actual-expense vehicles and zero otherwise, matching the elected section 179 cost for listed property subject to the passenger-automobile limits."
```

#### Pass 5e6c27f2bfbb

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines (screen) (scveh.screen) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5e6c27f2bfbb686e3f1b2ce9da4ee2d8fb4938b2e8e35bf6ddeaa453f78480b6 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a3bf05f389eeb8e2c721d02820ff275ae575845995ab29c15ae1f31290e56a2c |
| receipt | .transcription/scveh.deepseek.render.lines-28e8aef8e1b0 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 0 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 37, 60, 63 | pages named by another document's citation | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 37, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |

##### Raw response

```yaml
lines:
  - key: "(screen) (scveh.screen)"
    status: MISMATCH
    reason: "The screen treats 'an electric vehicle placed in service before 2007' as a special case, but the IRS text defines the special electric-vehicle category as 'vehicles produced by an original equipment manufacturer and designed to run primarily on electricity, placed in service after August 5, 1997, and before January 1, 2007'; the lower date and design/OEM limits are omitted."
```

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
