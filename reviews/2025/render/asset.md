# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 163c18eef4ba8d8e8b74e6775dec40b3cf0a2d940d0c308f57de9d40819d77ee |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | fa356e4e0e1f6e98b2766a0aeab30290d5d4508f4c1850ce1017e47bd4473ab9 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 13 / 2 / 0 / 0 |
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

Model: This follows Pub. 946 Appendix B 'How To Use the Tables': use Table B-1, but use the Table B-2 period when the property is specifically listed under the activity. Classes A–C match 'Certain Property for Which Recovery Periods Assigned'. The QIP definition and the rule for additions and improvements match Pub. 946 pages 31 and 33.
Reviewed in: pass cfd34aadb023

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Pub. 946 says 'The GDS recovery periods for property not listed above can be found in Appendix B, Table of Class Lives and Recovery Periods.' The instructions' column (d) table also gives these periods. Looking up the GDS column by asset class matches.
Reviewed in: pass cfd34aadb023

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is an exclusion screen, and its items track the instructions' cases. These include ADS-required property ('Imported property covered by an executive order...'), basis-reducing credits and deductions, the table-use rules (short tax years, basis adjustments), section 168(k)(9) property and qualified business use exclusions. Each excluded case sends the filer outside the tool.
Reviewed in: pass cfd34aadb023

### (b) — Year placed in service
Status: **MATCH**

Model: This matches Pub. 946: 'the date the property is ready and available for a specific use' and 'treat the property as being placed in service on the conversion date'. For additions it matches 'The recovery period begins on the later of' the two dates.
Reviewed in: pass cfd34aadb023

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: The restatement stops at cost times business-use percentage. The IRS column (c) basis is reduced further: 'multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property ... Section 179 expense deduction ... Any special depreciation allowance included on line 14.' The printed (c) does not subtract the section 179 deduction or the special allowance.

Ruling: scope; same point as the backlog-round deepseek ruling of this marker. i4562 p. 11, Column (c): "multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property." This marker is the business basis before section 179 and the special allowance (its label); the reduced basis is printed at 19(c) (asset.col19c copies asset.ub, cited "From that result, subtract ... Section 179 expense deduction ... Any special depreciation allowance included on line 14"). asset.screen refuses property whose basis is reduced by any other credit or deduction, so on a computed return the only reductions are the two the project subtracts at 19(c). Project stands.
Reviewed in: pass cfd34aadb023

### 6(c) — Section 179 elected cost
Status: **MISMATCH**

Restated: Input — The amount of this property's cost you elect to expense under section 179 (zero if none; not more than its business cost). Only section 179 property qualifies: property you acquired by purchase for use in the active conduct of your business that is tangible personal property or off-the-shelf computer software, or other tangible property (not a building or its structural components) used as an integral part of manufacturing, production or extraction or of furnishing transportation, communications, electricity, gas, water or sewage disposal services (or as a research or bulk storage facility used with those activities), a storage facility (other than a building or its structural components) used in connection with distributing petroleum or any primary product of petroleum, or qualified improvement property you elect to treat as section 179 property. Enter zero for land and land improvements (such as swimming pools, paved parking areas, wharves, docks, bridges and fences), property held for investment, and property you purchased and lease to others, unless you manufactured or produced it, or the lease term is less than 50% of its class life and for the first 12 months after the transfer to the lessee your deductions for it as trade or business expenses (other than rents and reimbursed amounts) are more than 15% of its rental income. Also enter zero for property used by a tax-exempt organization (unless used in connection with the production of income subject to the tax on unrelated trade or business income) and property used by a governmental unit or a foreign person or entity (unless used under a lease with a term of less than 6 months).

Model: The restatement says 'Only section 179 property qualifies' and lists the categories, but leaves out a category the IRS includes. The instructions list '• Single purpose agricultural (livestock) or horticultural structures' as section 179 property, so the restatement would have the filer enter zero for such a structure.

Ruling: scope; the model says the restatement omits single purpose agricultural or horticultural structures, which i4562 p. 2 lists as section 179 property. Such a structure is Table B-1 class 01.4 (p946 Appendix B, Agriculture), which tables/2025/class_lives.yaml maps to outside, so asset.outside refuses it before any election is figured; the omission changes no amount the tool computes. (The backlog-round ruling recorded this under BUG-0326; that entry's asset part is closed by BUG-0373 and the agriculture classes are refused.)

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year'. Asking whether the choice is uniform supports a refusal that names the excluded mixed case.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Uses 100% for property acquired after January 19, 2025, 40% when that election is made or for property acquired after September 27, 2017 and before January 20, 2025, and zero on election out. The rate is applied to the depreciable basis after section 179. Long-production property, aircraft, used property and other exceptions are screened out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 is the special depreciation allowance for qualified listed property, figured under the line 14 instructions. Taking the line 14 computation for a non-vehicle listed item placed in service in 2025 matches.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: Line 6 instructions say: 'Enter the elected section 179 cost of listed property in column (i) of line 26.' Listed property at 50% or less is refused.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Column (c) is cost times the business/investment use percentage, less deductions including the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'. Other credits and adjustments are screened out.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The basis times the table rate follows 'Multiply column (c) by the applicable rate from the appropriate table.' The basis is the business basis after section 179 and line 14. The test 5×Q4 > 2×total is the 'exceed 40%' test, applied to bases after section 179 and before the special allowance, as Pub. 946's caution requires. The quarter-specific mid-quarter tables are used.
Reviewed in: pass cfd34aadb023

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: This is the convention used in the year placed in service, half-year or mid-quarter with the quarter, as described in the column (e) instructions. Mid-month real property is screened out.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 refers to the line 19(g) method. Pub. 946 says 'You must apply the rates in the percentage tables to your property's unadjusted basis', meaning basis reduced by the section 179 deduction and the special allowance. The original convention and the 2025 year of recovery are used, and zero is entered after the recovery period ends.
Reviewed in: pass cfd34aadb023

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g)'. The restatement does this, taking the 2025-property or prior-year amount as applicable. Listed property used 50% or less is refused.
Reviewed in: pass cfd34aadb023

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (a) | aa675ab644b2f8a35e6bf7acf7c32159b2f99b836865096d8a20b2175cd95050 |
| (d) | 3182f942b566ee9e3a315b09b89e5388c0785adaa7aa2dce113e7406d27b32c0 |
| (screen) (asset.screen) | 3df7a8a6d93402199693e764fa71178b18b4ae38d40d45df1b009561d0dd6572 |
| (b) | 11c2b67acc1cf618b82feacbaddb645adda0fb28a8d1efc758cf7952f6f6cfd8 |
| (c) | dbccd7a20e636911bf07ef24dc5576d34b12e3ff67ad8e277378ba33ef38a187 |
| 6(c) | d5f79bcbeecfded424e48963a0b007790751499ee490e055b79b4c3e1627f753 |
| (screen) (asset.bonus_same) | 2f34e9e3885fb3fa0b0ec17dc96999e5445e98b80c54ddbaaa89064cca8fe4ea |
| 14 | efe1faa232d84d1fa50d0042c6170b1fba6e791d51a4f8d77c78b3fd4a540fc7 |
| 25 | 4b426ebe7b78071c2a8116ed219a8177a4e50a5d5cd1964666a8cbc004017fea |
| 26(i) | bd8b39d7968abb5158cc9063980a008ae12af3d23b7f787952a7d32d5daff3c9 |
| 19(c) | a348543ed2f8ce1a5f3364af3b70ff6f70f79f708aea09279eb39440e6fee12b |
| 19(g) | 4d9b19d140844f675a9f5e137f8603835e1249df6862c8eabeb18f127cf97f2d |
| (e) | 58c601084fe91483f688a5198d983bff68af4e5e06906923295c9f5e6a2925d6 |
| 17 | 5a93b095d7fcd5d079c06e8ad3bfda8011c94dd0d7454fd8a020b8f4a5f3d5c4 |
| 26(h) | c177f61a98dd2618c32a9fb4836533b01729248ee90a47cec70859fcd50cecd9 |
| (rest of the document) | f636cbc4d4d8b77135b4fed9b7130553c8aeaa64b4580beda19da8d4f7a1c38a |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass cfd34aadb023

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (a), (d), (screen) (asset.screen), (b), (c), 19(g), 17, 26(h) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cfd34aadb02382a10be55fcb2c9142f55e074fb3d99b5f6207f9b0a2ae5a324a |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f7620e05c2eb26328d17cb2ccbc5e5704e6e3dc3b7c1b97d30683afcf8b8f632 |
| receipt | .transcription/asset.render.lines-337cfa08e5db |
| lines judged | 8 |
| match / mismatch / unclear / missing | 7 / 1 / 0 / 0 |
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
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "This follows Pub. 946 Appendix B 'How To Use the Tables': use Table B-1, but use the Table B-2 period when the property is specifically listed under the activity. Classes A–C match 'Certain Property for Which Recovery Periods Assigned'. The QIP definition and the rule for additions and improvements match Pub. 946 pages 31 and 33."
  - key: "(d)"
    status: MATCH
    reason: "Pub. 946 says 'The GDS recovery periods for property not listed above can be found in Appendix B, Table of Class Lives and Recovery Periods.' The instructions' column (d) table also gives these periods. Looking up the GDS column by asset class matches."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is an exclusion screen, and its items track the instructions' cases. These include ADS-required property ('Imported property covered by an executive order...'), basis-reducing credits and deductions, the table-use rules (short tax years, basis adjustments), section 168(k)(9) property and qualified business use exclusions. Each excluded case sends the filer outside the tool."
  - key: "(b)"
    status: MATCH
    reason: "This matches Pub. 946: 'the date the property is ready and available for a specific use' and 'treat the property as being placed in service on the conversion date'. For additions it matches 'The recovery period begins on the later of' the two dates."
  - key: "(c)"
    status: MISMATCH
    reason: "The restatement stops at cost times business-use percentage. The IRS column (c) basis is reduced further: 'multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property ... Section 179 expense deduction ... Any special depreciation allowance included on line 14.' The printed (c) does not subtract the section 179 deduction or the special allowance."
  - key: "19(g)"
    status: MATCH
    reason: "The basis times the table rate follows 'Multiply column (c) by the applicable rate from the appropriate table.' The basis is the business basis after section 179 and line 14. The test 5×Q4 > 2×total is the 'exceed 40%' test, applied to bases after section 179 and before the special allowance, as Pub. 946's caution requires. The quarter-specific mid-quarter tables are used."
  - key: "17"
    status: MATCH
    reason: "Line 17 refers to the line 19(g) method. Pub. 946 says 'You must apply the rates in the percentage tables to your property's unadjusted basis', meaning basis reduced by the section 179 deduction and the special allowance. The original convention and the 2025 year of recovery are used, and zero is entered after the recovery period ends."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g)'. The restatement does this, taking the 2025-property or prior-year amount as applicable. Listed property used 50% or less is refused."
```
```

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Follows Pub. 946 Appendix B: use Table B-2 when the property is specifically listed under the activity, otherwise Table B-1. Classes A, B and C are from 'Certain Property for Which Recovery Periods Assigned', and the qualified improvement property definition matches Pub. 946 page 31."
  - key: "(d)"
    status: MATCH
    reason: "Takes the GDS (MACRS) recovery period column of Tables B-1 and B-2 for the asset class. This matches the column (d) instruction to determine the recovery period, with Pub. 946 for details."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The screen only narrows the tool to supported cases, and the asset.screened refusal names what is excluded. Its items track the IRS text: the ADS-required list, basis-reducing credits, the 168(k)(9) exception, short tax years, listed property at 50% or less, and percentage-table restrictions."
  - key: "(b)"
    status: MATCH
    reason: "Matches Pub. 946's placed-in-service rule: 'the date the property is ready and available for a specific use', and converted property is 'placed in service on the conversion date'."
  - key: "(c)"
    status: MATCH
    reason: "Computes the first step of the column (c) instruction, 'multiply the cost or other basis of the property by the percentage of business/investment use'. The later subtractions are made in separate helpers. Listed property at 50% or less is refused."
  - key: "6(c)"
    status: MISMATCH
    reason: "The restatement says 'Only section 179 property qualifies' and lists the categories, but leaves out a category the IRS includes. The instructions list '• Single purpose agricultural (livestock) or horticultural structures' as section 179 property, so the restatement would have the filer enter zero for such a structure."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year'. Asking whether the choice is uniform supports a refusal that names the excluded mixed case."
  - key: "14"
    status: MATCH
    reason: "Uses 100% for property acquired after January 19, 2025, 40% when that election is made or for property acquired after September 27, 2017 and before January 20, 2025, and zero on election out. The rate is applied to the depreciable basis after section 179. Long-production property, aircraft, used property and other exceptions are screened out."
  - key: "25"
    status: MATCH
    reason: "Line 25 is the special depreciation allowance for qualified listed property, figured under the line 14 instructions. Taking the line 14 computation for a non-vehicle listed item placed in service in 2025 matches."
  - key: "26(i)"
    status: MATCH
    reason: "Line 6 instructions say: 'Enter the elected section 179 cost of listed property in column (i) of line 26.' Listed property at 50% or less is refused."
  - key: "19(c)"
    status: MATCH
    reason: "Column (c) is cost times the business/investment use percentage, less deductions including the 'Section 179 expense deduction' and 'Any special depreciation allowance included on line 14'. Other credits and adjustments are screened out."
  - key: "19(g)"
    status: MATCH
    reason: "Multiplies column (c) by the MACRS table rate for the applicable convention. The mid-quarter test compares fourth-quarter bases (after section 179, before the special allowance) to 40% of the year's bases, as the column (e) instructions and the Pub. 946 caution say."
  - key: "(e)"
    status: MATCH
    reason: "This is the convention used in the year placed in service, half-year or mid-quarter with the quarter, as described in the column (e) instructions. Mid-month real property is screened out."
  - key: "17"
    status: MATCH
    reason: "Line 17 deductions are figured per the line 19(g) instructions by applying table rates to the unadjusted basis. Per Pub. 946, the unadjusted basis is reduced by 'Any section 179 deduction claimed' and 'Any special depreciation allowance'. Zero is entered after the recovery period ends; basis adjustments and business-use changes are screened out."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50% and placed in service after 1986, 'figure column (h) by following the instructions for line 19, column (g)'. The restatement adds the 2025-property amount or the prior-year amount, whichever applies."
```
```
