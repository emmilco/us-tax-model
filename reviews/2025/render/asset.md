# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 192db1ebd73980dcf0fdeda6b4821c4f704dbab08285328076be55ce8519bef5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | b86b5b69178ae0e506567c11a9a4be7ba4af4c47b4efa8b19542ad937b483117 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 14 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: Follows Pub. 946 Appendix B: check Table B-1, then use the Table B-2 activity class when the property is specifically listed there. It also offers the 'Certain Property for Which Recovery Periods Assigned' classes A, B and C, and qualified improvement property, which i4562 classifies as 15-year property.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: The GDS recovery period is read from the GDS (MACRS) column of Tables B-1 and B-2 for the chosen asset class, as Pub. 946 Appendix B and the i4562 column (d) instructions direct.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This is a scope screen, and the cases it excludes are named in the asset.screened refusal. The listed-property qualified business use definition matches the i4562 lines 26 and 27 text, including the exclusions from the numerator.

### (b) — Year placed in service
Status: **MATCH**

Model: Year placed in service is entered as input. Limiting it to 2005 to 2025 narrows the cases the program supports and is consistent with the screen.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: Matches the first step of the column (c) instruction, 'multiply the cost or other basis of the property by the percentage of business/investment use.' The percentage is applied as a whole number divided by 100, and the refusal excludes listed property used 50% or less and percentages over 100.

### 6(c) — Section 179 elected cost
Status: **MISMATCH**

Restated: Input — The amount of this property's cost you elect to expense under section 179 (zero if none; not more than its business cost). Only section 179 property qualifies: property you acquired by purchase for use in the active conduct of your business that is tangible personal property or off-the-shelf computer software, or other tangible property (not a building or its structural components) used as an integral part of manufacturing, production or extraction or of furnishing transportation, communications, electricity, gas, water or sewage disposal services (or as a research or bulk storage facility used with those activities), or qualified improvement property you elect to treat as section 179 property. Enter zero for land and land improvements (such as swimming pools, paved parking areas, wharves, docks, bridges and fences), property held for investment, and property you purchased and lease to others, unless you manufactured or produced it, or the lease term is less than 50% of its class life and for the first 12 months after the transfer to the lessee your deductions for it as trade or business expenses (other than rents and reimbursed amounts) are more than 15% of its rental income. If you paid for it with cash and a trade-in, the elected cost cannot be more than the cash you paid.

Model: The restatement's list of qualifying section 179 property leaves out two categories the i4562 text includes: '• Single purpose agricultural (livestock) or horticultural structures. • Storage facilities (except buildings and their structural components) used in connection with distributing petroleum or any primary product of petroleum.' A filer with such property would enter zero instead of the amount elected, and no refusal names these cases.

Ruling: finding, recorded (BUG-0326, T-183, open); i4562 p. 2 lists single purpose agricultural or horticultural structures and certain storage facilities as section 179 property, and the question's list omits them. A filer with such property may not elect; it changes no amount the tool computes for property it does list.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' The question checks that the choice is uniform across the class, and the bonus_mixed refusal excludes the case where it is not.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Gives 100% for property acquired after January 19, 2025, 40% for property acquired after September 27, 2017 and before January 20, 2025, or 40% under the election. Each rate is applied to the depreciable basis, which is the business portion less the section 179 deduction, as the line 14 'How to figure the allowance' text says. Zero applies when the filer elected out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 takes the special allowance for qualified listed property placed in service in 2025, figured 'See the instructions for line 14 ... how to figure the deduction.' Reusing the line 14 computation matches.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: Line 6 instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The restatement does this.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: The column (c) basis is the business portion of cost minus the section 179 deduction and 'Any special depreciation allowance included on line 14.' The restatement computes exactly this.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: Column (c) is multiplied by the applicable table rate for the year of recovery. The convention is mid-quarter when fourth-quarter bases exceed 40% of all 2025 bases, using bases after section 179 and before any special allowance, as the Pub. 946 caution says. The test is applied across the taxpayer's businesses.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The convention is entered as input, either half-year or mid-quarter with its quarter, matching the i4562 column (e) conventions for property within the program's scope.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: The prior-year MACRS deduction is the unadjusted basis times the table rate for the 2025 year of recovery. Unadjusted basis is reduced by the section 179 deduction and the special allowance, as Pub. 946 'Figuring the Unadjusted Basis' requires. The deduction is zero after the recovery period ends.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, column (h) is figured 'by following the instructions for line 19, column (g).' Using the line 19(g) amount for 2025 property and the line 17 amount for earlier property matches.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Follows Pub. 946 Appendix B: check Table B-1, then use the Table B-2 activity class when the property is specifically listed there. It also offers the 'Certain Property for Which Recovery Periods Assigned' classes A, B and C, and qualified improvement property, which i4562 classifies as 15-year property."
  - key: "(d)"
    status: MATCH
    reason: "The GDS recovery period is read from the GDS (MACRS) column of Tables B-1 and B-2 for the chosen asset class, as Pub. 946 Appendix B and the i4562 column (d) instructions direct."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This is a scope screen, and the cases it excludes are named in the asset.screened refusal. The listed-property qualified business use definition matches the i4562 lines 26 and 27 text, including the exclusions from the numerator."
  - key: "(b)"
    status: MATCH
    reason: "Year placed in service is entered as input. Limiting it to 2005 to 2025 narrows the cases the program supports and is consistent with the screen."
  - key: "(c)"
    status: MATCH
    reason: "Matches the first step of the column (c) instruction, 'multiply the cost or other basis of the property by the percentage of business/investment use.' The percentage is applied as a whole number divided by 100, and the refusal excludes listed property used 50% or less and percentages over 100."
  - key: "6(c)"
    status: MISMATCH
    reason: "The restatement's list of qualifying section 179 property leaves out two categories the i4562 text includes: '• Single purpose agricultural (livestock) or horticultural structures. • Storage facilities (except buildings and their structural components) used in connection with distributing petroleum or any primary product of petroleum.' A filer with such property would enter zero instead of the amount elected, and no refusal names these cases."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' The question checks that the choice is uniform across the class, and the bonus_mixed refusal excludes the case where it is not."
  - key: "14"
    status: MATCH
    reason: "Gives 100% for property acquired after January 19, 2025, 40% for property acquired after September 27, 2017 and before January 20, 2025, or 40% under the election. Each rate is applied to the depreciable basis, which is the business portion less the section 179 deduction, as the line 14 'How to figure the allowance' text says. Zero applies when the filer elected out."
  - key: "25"
    status: MATCH
    reason: "Line 25 takes the special allowance for qualified listed property placed in service in 2025, figured 'See the instructions for line 14 ... how to figure the deduction.' Reusing the line 14 computation matches."
  - key: "26(i)"
    status: MATCH
    reason: "Line 6 instructions say 'Enter the elected section 179 cost of listed property in column (i) of line 26.' The restatement does this."
  - key: "19(c)"
    status: MATCH
    reason: "The column (c) basis is the business portion of cost minus the section 179 deduction and 'Any special depreciation allowance included on line 14.' The restatement computes exactly this."
  - key: "19(g)"
    status: MATCH
    reason: "Column (c) is multiplied by the applicable table rate for the year of recovery. The convention is mid-quarter when fourth-quarter bases exceed 40% of all 2025 bases, using bases after section 179 and before any special allowance, as the Pub. 946 caution says. The test is applied across the taxpayer's businesses."
  - key: "(e)"
    status: MATCH
    reason: "The convention is entered as input, either half-year or mid-quarter with its quarter, matching the i4562 column (e) conventions for property within the program's scope."
  - key: "17"
    status: MATCH
    reason: "The prior-year MACRS deduction is the unadjusted basis times the table rate for the 2025 year of recovery. Unadjusted basis is reduced by the section 179 deduction and the special allowance, as Pub. 946 'Figuring the Unadjusted Basis' requires. The deduction is zero after the recovery period ends."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, column (h) is figured 'by following the instructions for line 19, column (g).' Using the line 19(g) amount for 2025 property and the line 17 amount for earlier property matches."
```
```
