# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 163c18eef4ba8d8e8b74e6775dec40b3cf0a2d940d0c308f57de9d40819d77ee |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | fa356e4e0e1f6e98b2766a0aeab30290d5d4508f4c1850ce1017e47bd4473ab9 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 10 / 3 / 0 / 2 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: The restatement follows the Form 4562 line 19 column (a) classification rules and Pub. 946 Appendix B lookup, including the special Table B-2 categories and qualified improvement property description.
Reviewed in: pass 420a0bbe07a6

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The recovery period is determined from the asset classification using the GDS recovery-period tables, which corresponds to Form 4562 line 19 column (d) and Pub. 946 Appendix B.
Reviewed in: pass 420a0bbe07a6

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MISSING**

Restated: Input — Does any of these apply to this property?

- you disposed of it, or of a portion of it, or converted it to personal use in 2025
- you acquired it in a like-kind exchange or an involuntary conversion, with a trade-in (you traded in other property as part of its price), from a related person, or by gift or inheritance
- it is real property (a building or a structural component, other than qualified improvement property) or land
- it is a car, truck or other vehicle (enter vehicles separately)
- you must depreciate it under ADS, for example:
  - it is imported property covered by an executive order of the President of the United States
  - it is used predominantly in a farming business and placed in service in a tax year in which you made an election under section 263A(d)(3) not to have the uniform capitalization rules apply
  - it is qualified improvement property held by an electing real property trade or business
  - it has a recovery period of 10 years or more and is held by an electing farming business
- you elected ADS, the straight line method or the 150% declining balance method for it
- you depreciate it by a method other than the MACRS percentage tables
- it is a film, videotape or sound recording
- it is computer software, unless you placed it in service in 2025 and deduct all of its business cost in 2025 through section 179 and the special depreciation allowance
- it is an initial clearing and grading land improvement for gas utility property or for electric utility transmission and distribution plants
- its basis was adjusted for anything other than depreciation (for example a casualty loss)
- its basis is reduced by a credit or deduction other than the section 179 deduction and the special depreciation allowance, for example:
  - the section 179D deduction for energy efficient commercial building property
  - the deduction for removal of barriers to the disabled and the elderly
  - the disabled access credit
  - the enhanced oil recovery credit
  - the credit for alternative fuel vehicle refueling property
  - the credit for employer-provided childcare facilities and services
  - a basis adjustment for investment credit property or advanced manufacturing investment credit property
- it is in a general asset account
- you amortize it
- it is used predominantly outside the United States, or is tax-exempt use or tax-exempt bond financed property
- it was placed in service before 2005
- its business use percentage has changed since you placed it in service
- it is qualified reuse and recycling property (machinery or equipment used exclusively to collect, distribute or recycle reuse and recyclable materials, section 168(m))
- you acquired it before September 28, 2017
- it is property with a long production period, an aircraft, or qualified production property
- you claim a special depreciation allowance for it in 2025 and its original use did not begin with you (original use is the first use to which the property is put, whether or not by you, so property someone else used before you acquired it is used property, and so is reconditioned or rebuilt property you acquired unless the cost of its used parts is not more than 20% of its total cost)
- you claim a special depreciation allowance for it in 2025 and it is property described in section 168(k)(9)(A) or 168(k)(9)(B), that is:
  - property primarily used in a trade or business of furnishing or selling electrical energy, water or sewage disposal services, gas or steam through a local distribution system, or transportation of gas or steam by pipeline, whose rates are established or approved by a State or political subdivision, an agency or instrumentality of the United States, a public service or public utility commission or similar body of a State or political subdivision, or the governing or ratemaking body of an electric cooperative
  - property used in a trade or business that has had floor plan financing indebtedness (a loan used to buy motor vehicles, boats, farm machinery or equipment, or trailers or campers held for sale or lease, and secured by them) whose interest was taken into account under section 163(j)(1)(C) in figuring the business interest expense limit
- it is any of these:
  - qualified rent-to-own property (section 168(i)(14))
  - energy property specified in section 168(e)(3)(B)(vi)
  - a motorsports entertainment complex (section 168(i)(15))
  - a natural gas gathering line (section 168(i)(17))
  - qualified smart electric meter or qualified smart electric grid system property
  - electric transmission property specified in section 168(e)(3)(E)(v)
- your 2025 tax year, or any tax year since you placed it in service, is shorter than 12 months
- it is listed property whose qualified business use is 50% or less once you leave out uses that are not qualified business use:
  - investment use
  - leasing it to a 5% owner or related person, or using it as compensation for services of a 5% owner or related person, unless for the lease the value is reported as income to that person
  - using it as compensation for services of anyone else unless an amount is included in that person's income for the use and any required income tax was withheld
  - use that is nondeductible under section 274

Model: the model returned no verdict for this line

Ruling: model error; the reply returned no verdict for this line. The restructured asset.screen question was judged MATCH in the Claude render pass of the same restatement (reviews/2025/render/asset.md), and its words are the earlier question's (R3 word check: none lost).
Reviewed in: pass 420a0bbe07a6

### (b) — Year placed in service
Status: **MISSING**

Restated: Input — The year you placed this property in service in the business (2005 to 2025). Property is placed in service when it is ready and available for a specific use, even if you have not yet used it; property you converted from personal use to use in the business is placed in service on the date of the conversion; for an addition or improvement, the later of the year you placed it in service and the year you placed in service the property it was made to

Model: the model returned no verdict for this line

Ruling: model error; the model returned no verdict for this line.
Reviewed in: pass cfd34aadb023

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS column (c) says: "From that result, subtract any credits and deductions allocable to the property," including the section 179 expense deduction and special depreciation allowance; the restatement only multiplies cost by the business-use percentage and omits those subtractions.

Ruling: representation; same objection as the earlier rulings. This marker is the business basis before section 179 and the special allowance (its label); the form's column (c) after those deductions is 19(c) (asset.col19c), which subtracts them (i4562 p. 9, Lines 19a Through 19j, column (c)). asset.screen refuses property whose basis "is reduced by a credit or deduction other than the section 179 deduction and the special depreciation allowance", so on a computed return the only reductions are the two 19(c) subtracts. No printed amount differs. Project stands.
Reviewed in: pass 420a0bbe07a6

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The input is the elected section 179 cost limited to section 179 property and business cost, and the instructions plus Pub. 946 support the stated section 179 property rules and zero entries within the program’s screened cases.
Reviewed in: pass 420a0bbe07a6

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The special allowance election must be consistent for the entire class of property placed in service in 2025.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The restatement matches the line 14 allowance rates: 100% for qualified property acquired after January 19, 2025, 40% for property acquired after September 27, 2017 and before January 20, 2025, the 40% election, and zero if no allowance is claimed.
Reviewed in: pass 420a0bbe07a6

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; line 14 is not the listed-property special allowance total, so copying line 14 uses a different operand.

Ruling: representation; same as the earlier rulings. asset.f25 copies asset.bonus, the per-asset special allowance, and is shown only for listed property placed in service in 2025 (asset.on_26_2025); "from line 14" names the shared per-asset amount, not the non-listed total (i4562 p. 14, Line 25).

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS line 6 says: "Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26." The restatement instead says to enter the amount from line 6(c), which is the non-listed-property line.

Ruling: representation; same as the earlier rulings. asset.f26i copies asset.s179, the per-asset elected section 179 cost (the input whose marker is 6(c)), shown only for listed property; Form 4562 line 6 itself is s179.line6, "Elected cost of section 179 property (other than listed property)", which sums the non-listed elections (i4562 p. 5, Line 6, "Enter the elected section 179 cost of listed property in column (i) of line 26"). Project stands.
Reviewed in: pass 420a0bbe07a6

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Within the screened cases, the helper computes the basis for MACRS depreciation after subtracting the section 179 election and the special depreciation allowance, matching what line 19 column (c) requires.
Reviewed in: pass 420a0bbe07a6

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The restatement uses the half-year convention unless the mid-quarter test is met, and multiplies the MACRS basis by the applicable GDS table rate, matching line 19 column (g).
Reviewed in: pass 420a0bbe07a6

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention options are half-year and mid-quarter, and the quarter is needed to apply the mid-quarter convention correctly.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: For MACRS property placed in service before 2025, the restatement computes the current-year MACRS deduction using the unadjusted basis and applicable rate, and enters zero if the recovery period ended before 2025, matching line 17.
Reviewed in: pass 420a0bbe07a6

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property, line 26 column (h) follows the line 19 column (g) MACRS computation; using the current-year MACRS amount and zero for the other placed-in-service period matches that within the program's exclusions.
Reviewed in: pass cfd34aadb023

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (a) | e7ddc5c08fd4fdfb949997e3fd3aaa39b70c52428a85a8e87272ea5c37bda358 |
| (d) | b92ddb258734975b9f3862acfd79b1bee56e7844fd13894f7e35d6be7c8d8e54 |
| (screen) (asset.screen) | 403bea3751c53fd013b85f53589e47ad6da348c6eee96cc150f54b347c4d6009 |
| (b) | 11c2b67acc1cf618b82feacbaddb645adda0fb28a8d1efc758cf7952f6f6cfd8 |
| (c) | d73586c607b01c97ecdfab67f565e7b67aaf3ed18e11df61d97bab267ebb8f74 |
| 6(c) | 084dddb1873a0f47ceb66432c36955190ec9664cc738b5f474619c191e8ecce7 |
| (screen) (asset.bonus_same) | 2f34e9e3885fb3fa0b0ec17dc96999e5445e98b80c54ddbaaa89064cca8fe4ea |
| 14 | 27d44495cfd6497c4dfdcdc5e24b593b76bb784200fd9031e9e335cfeb45e781 |
| 25 | 4b426ebe7b78071c2a8116ed219a8177a4e50a5d5cd1964666a8cbc004017fea |
| 26(i) | 972bf999bb72cb2de985955f855b6d9c9bae4e980b417a580fd7fd6d51ef6d5a |
| 19(c) | 5b66752b589f0971467311e10fed998f21c63678fcf35bcdfbd9884586abec92 |
| 19(g) | 03bbe7b036774ffb313bb79f78b8a4f71d9012e5e129191f610ef58659e0be41 |
| (e) | 58c601084fe91483f688a5198d983bff68af4e5e06906923295c9f5e6a2925d6 |
| 17 | 6a34fb433b328c67729c214a1ec1207019105c47a5d049f10f94ffc4706a75c5 |
| 26(h) | c177f61a98dd2618c32a9fb4836533b01729248ee90a47cec70859fcd50cecd9 |
| (rest of the document) | f636cbc4d4d8b77135b4fed9b7130553c8aeaa64b4580beda19da8d4f7a1c38a |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass cfd34aadb023

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (a), (d), (screen) (asset.screen), (b), (c), 19(g), 17, 26(h) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | cfd34aadb02382a10be55fcb2c9142f55e074fb3d99b5f6207f9b0a2ae5a324a |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f7620e05c2eb26328d17cb2ccbc5e5704e6e3dc3b7c1b97d30683afcf8b8f632 |
| receipt | .transcription/asset.deepseek.render.lines-337cfa08e5db |
| lines judged | 8 |
| match / mismatch / unclear / missing | 6 / 1 / 0 / 1 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 33, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

##### Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The restatement follows line 19 column (a): classify using Pub. 946 Appendix B Tables B-1 and B-2, with the QIP definition and the separate-property rule for additions and improvements matching the IRS text."
  - key: "(d)"
    status: MATCH
    reason: "Column (d) is a recovery-period lookup by asset classification; using the GDS recovery period for the asset class matches the line 19 column (d) instruction within the property this tool supports."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen collects the categories the program treats as outside this tool, and the cost refusal identifies those screened-out cases; this is a permissible narrowing of the form within the supported cases."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS column (c) says: 'To find the basis for depreciation, multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property.' The restatement only multiplies cost by the business-use percentage and omits the required subtraction."
  - key: "19(g)"
    status: MATCH
    reason: "The restatement computes MACRS depreciation for 2025 property using the GDS rate for the applicable convention; choosing half-year unless the 40%-fourth-quarter mid-quarter test applies matches line 19 column (g) within the screened cases."
  - key: "17"
    status: MATCH
    reason: "Line 17 covers prior-year MACRS property; using the 2025 recovery-year rate and entering zero after the recovery period has ended matches the instruction to follow line 19 column (g)."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property, line 26 column (h) follows the line 19 column (g) MACRS computation; using the current-year MACRS amount and zero for the other placed-in-service period matches that within the program's exclusions."
```

#### Pass 420a0bbe07a6

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines (a), (d), (screen) (asset.screen), (c), 6(c), 14, 26(i), 19(c), 19(g), 17 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 420a0bbe07a6c9933ea3fa233cec4ccef3ede17fe0253bc4c7b54022d05501f1 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 9da84f6710dde8fa01520bc38e4565739a737fa2eb5de13af9560462bfe13f3d |
| receipt | .transcription/asset.deepseek.render.lines-f9eada4139a6 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 7 / 2 / 0 / 1 |
| verdicts for lines not in the form | (screen) |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 33, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p463 | For use in preparing 2025 returns | 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |

##### Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The restatement follows the Form 4562 line 19 column (a) classification rules and Pub. 946 Appendix B lookup, including the special Table B-2 categories and qualified improvement property description."
  - key: "(d)"
    status: MATCH
    reason: "The recovery period is determined from the asset classification using the GDS recovery-period tables, which corresponds to Form 4562 line 19 column (d) and Pub. 946 Appendix B."
  - key: "(screen)"
    status: MATCH
    reason: "The screen lists the conditions the program excludes and the refusals name those excluded cases; within the cases it supports, the exclusions are consistent with the IRS instructions and Pub. 946."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS column (c) says: \"From that result, subtract any credits and deductions allocable to the property,\" including the section 179 expense deduction and special depreciation allowance; the restatement only multiplies cost by the business-use percentage and omits those subtractions."
  - key: "6(c)"
    status: MATCH
    reason: "The input is the elected section 179 cost limited to section 179 property and business cost, and the instructions plus Pub. 946 support the stated section 179 property rules and zero entries within the program’s screened cases."
  - key: "14"
    status: MATCH
    reason: "The restatement matches the line 14 allowance rates: 100% for qualified property acquired after January 19, 2025, 40% for property acquired after September 27, 2017 and before January 20, 2025, the 40% election, and zero if no allowance is claimed."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS line 6 says: \"Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.\" The restatement instead says to enter the amount from line 6(c), which is the non-listed-property line."
  - key: "19(c)"
    status: MATCH
    reason: "Within the screened cases, the helper computes the basis for MACRS depreciation after subtracting the section 179 election and the special depreciation allowance, matching what line 19 column (c) requires."
  - key: "19(g)"
    status: MATCH
    reason: "The restatement uses the half-year convention unless the mid-quarter test is met, and multiplies the MACRS basis by the applicable GDS table rate, matching line 19 column (g)."
  - key: "17"
    status: MATCH
    reason: "For MACRS property placed in service before 2025, the restatement computes the current-year MACRS deduction using the unadjusted basis and applicable rate, and enters zero if the recovery period ended before 2025, matching line 17."
```

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The restatement follows the Appendix B Table B-1/Table B-2 lookup order and the special Table B-2 categories, including the QIP definition."
  - key: "(d)"
    status: MATCH
    reason: "The IRS recovery period is determined from the property's classification/asset class using the Appendix B tables and the Form 4562 recovery-period table."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is a scope screen that names the types of property excluded from this tool; the exclusions are consistent with the Form 4562/Pub. 946 text provided, and narrowing the supported cases is permitted."
  - key: "(b)"
    status: MATCH
    reason: "The placed-in-service definition matches Pub. 946, including readiness and availability and the conversion-date rule; capturing year and separately the quarter is sufficient for this computation."
  - key: "(c)"
    status: MATCH
    reason: "This computes the business/investment-use portion of cost; within the supported cases line 19(c) then reduces that amount by section 179 and the special allowance as column (c) requires."
  - key: "6(c)"
    status: MATCH
    reason: "The restatement describes the elected section 179 cost and the section 179 property/exclusion rules reflected in the provided Form 4562 and Pub. 946 text."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The special allowance election must be consistent for the entire class of property placed in service in 2025."
  - key: "14"
    status: MATCH
    reason: "The 100%/40%/none choices and the acquisition-date split match the line 14 special depreciation allowance rules for the supported property."
  - key: "25"
    status: MISMATCH
    reason: "IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; line 14 is not the listed-property special allowance total, so copying line 14 uses a different operand."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.'; line 6(c) is not the listed-property elected section 179 cost."
  - key: "19(c)"
    status: MATCH
    reason: "The restatement enters the basis after section 179 and the special allowance, which is what Form 4562 line 19 column (c) requires within the screened cases."
  - key: "19(g)"
    status: MATCH
    reason: "The restatement selects MACRS half-year or mid-quarter depreciation based on whether the mid-quarter test is met, matching the line 19(g) and convention instructions."
  - key: "(e)"
    status: MATCH
    reason: "The convention options are half-year and mid-quarter, and the quarter is needed to apply the mid-quarter convention correctly."
  - key: "17"
    status: MATCH
    reason: "Line 17 is current-year MACRS depreciation for property placed in service before 2025, and zero once the recovery period has ended."
  - key: "26(h)"
    status: MATCH
    reason: "For one listed property, adding current-year MACRS for 2025-placed property and current-year MACRS for prior-placed property reduces to the proper line 26(h) current-year depreciation."
```
