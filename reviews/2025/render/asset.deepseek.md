# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 163c18eef4ba8d8e8b74e6775dec40b3cf0a2d940d0c308f57de9d40819d77ee |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | fa356e4e0e1f6e98b2766a0aeab30290d5d4508f4c1850ce1017e47bd4473ab9 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 11 / 3 / 0 / 1 |
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

Model: The restatement follows line 19 column (a): classify using Pub. 946 Appendix B Tables B-1 and B-2, with the QIP definition and the separate-property rule for additions and improvements matching the IRS text.
Reviewed in: pass cfd34aadb023

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Column (d) is a recovery-period lookup by asset classification; using the GDS recovery period for the asset class matches the line 19 column (d) instruction within the property this tool supports.
Reviewed in: pass cfd34aadb023

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The screen collects the categories the program treats as outside this tool, and the cost refusal identifies those screened-out cases; this is a permissible narrowing of the form within the supported cases.
Reviewed in: pass cfd34aadb023

### (b) — Year placed in service
Status: **MISSING**

Restated: Input — The year you placed this property in service in the business (2005 to 2025). Property is placed in service when it is ready and available for a specific use, even if you have not yet used it; property you converted from personal use to use in the business is placed in service on the date of the conversion; for an addition or improvement, the later of the year you placed it in service and the year you placed in service the property it was made to

Model: the model returned no verdict for this line

Ruling: model error; the model returned no verdict for this line.
Reviewed in: pass cfd34aadb023

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS column (c) says: 'To find the basis for depreciation, multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property.' The restatement only multiplies cost by the business-use percentage and omits the required subtraction.

Ruling: scope; as the Claude ruling of this marker: the subtraction of section 179 and the special allowance is printed at 19(c), and asset.screen refuses any other basis-reducing credit or deduction (i4562 p. 11, Column (c)).
Reviewed in: pass cfd34aadb023

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The restatement describes the elected section 179 cost and the section 179 property/exclusion rules reflected in the provided Form 4562 and Pub. 946 text.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The special allowance election must be consistent for the entire class of property placed in service in 2025.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: The 100%/40%/none choices and the acquisition-date split match the line 14 special depreciation allowance rules for the supported property.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; line 14 is not the listed-property special allowance total, so copying line 14 uses a different operand.

Ruling: representation; same as the earlier rulings. asset.f25 copies asset.bonus, the per-asset special allowance, and is shown only for listed property placed in service in 2025 (asset.on_26_2025); "from line 14" names the shared per-asset amount, not the non-listed total (i4562 p. 14, Line 25).

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.'; line 6(c) is not the listed-property elected section 179 cost.

Ruling: representation; same as the earlier rulings. asset.f26i copies asset.s179, the per-asset elected section 179 cost, shown only for listed property (i4562 p. 5, Line 6, "Enter the elected section 179 cost of listed property in column (i) of line 26").

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The restatement enters the basis after section 179 and the special allowance, which is what Form 4562 line 19 column (c) requires within the screened cases.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: The restatement computes MACRS depreciation for 2025 property using the GDS rate for the applicable convention; choosing half-year unless the 40%-fourth-quarter mid-quarter test applies matches line 19 column (g) within the screened cases.
Reviewed in: pass cfd34aadb023

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention options are half-year and mid-quarter, and the quarter is needed to apply the mid-quarter convention correctly.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: Line 17 covers prior-year MACRS property; using the 2025 recovery-year rate and entering zero after the recovery period has ended matches the instruction to follow line 19 column (g).
Reviewed in: pass cfd34aadb023

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property, line 26 column (h) follows the line 19 column (g) MACRS computation; using the current-year MACRS amount and zero for the other placed-in-service period matches that within the program's exclusions.
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
