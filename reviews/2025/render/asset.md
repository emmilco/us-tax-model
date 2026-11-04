# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f9521b552cfa6ef40a43a98402e15129a4e7f8f41405e13401cf46c0d82e90f4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | af9f92a9efe22e1381eae6c0167cde7f1e2b8c4ec456685010780ad53d4b6763 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 12 / 2 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 39, 41, 59, 61, 62, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 6, 7, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (a) — Asset class of the property (Pub. 946, Appendix B)
Status: **MATCH**

Model: Follows Pub. 946 Appendix B: check Table B-1, and use the Table B-2 activity class when the property is 'specifically included in that asset class.' It also offers the 'Certain Property for Which Recovery Periods Assigned' categories A, B and C, plus qualified improvement property.

### (d) — Recovery period under GDS for the asset class
Status: **MATCH**

Model: Takes the GDS (MACRS) recovery period shown for the asset class in Tables B-1/B-2, as Appendix B and the column (d) instructions direct.

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: This input screen refuses cases the program does not support. Examples are dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments, short tax years, 168(k)(9) property and listed property at 50% or less qualified business use. Each item tracks IRS text, and the refusal names what is excluded.

### (b) — Year placed in service
Status: **MATCH**

Model: Input of the year placed in service. Earlier years are excluded by the screen.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MATCH**

Model: Computes the business/investment portion of cost: 'multiply the cost or other basis of the property by the percentage of business/investment use.' This is the first step of column (c); the section 179 and special allowance reductions are applied in later helpers. Percentages over 100 and listed property used 50% or less are refused.

### 6(c) — Section 179 elected cost
Status: **MISMATCH**

Restated: Input — The amount of this property's cost you elect to expense under section 179 (zero if none; not more than its business cost). Only section 179 property qualifies: property you acquired by purchase for use in the active conduct of your business that is tangible personal property or off-the-shelf computer software, or other tangible property (not a building or its structural components) used as an integral part of manufacturing, production or extraction or of furnishing transportation, communications, electricity, gas, water or sewage disposal services (or as a research or bulk storage facility used with those activities), or qualified improvement property you elect to treat as section 179 property. Enter zero for land and land improvements (such as swimming pools, paved parking areas, wharves, docks, bridges and fences), property held for investment, and property you purchased and lease to others, unless you manufactured or produced it, or the lease term is less than 50% of its class life and for the first 12 months after the transfer to the lessee your deductions for it as trade or business expenses (other than rents and reimbursed amounts) are more than 15% of its rental income. Also enter zero for property used by a tax-exempt organization (unless used in connection with the production of income subject to the tax on unrelated trade or business income) and property used by a governmental unit or a foreign person or entity (unless used under a lease with a term of less than 6 months). If you paid for it with cash and a trade-in, the elected cost cannot be more than the cash you paid.

Model: The restatement says 'Only section 179 property qualifies' and gives a list that leaves out IRS-qualifying property that is not screened out. The IRS list includes 'Single purpose agricultural (livestock) or horticultural structures' and 'Storage facilities (except buildings and their structural components) used in connection with distributing petroleum or any primary product of petroleum.' A filer with such property would be told to enter zero.

Ruling: finding (low; pre-existing, not introduced by the package); i4562 p. 2 lists as section 179 property "Storage facilities (except buildings and their structural components) used in connection with distributing petroleum or any primary product of petroleum" and "Single purpose agricultural (livestock) or horticultural structures". The question's list omits both. Single purpose structures are class 01.4, which class_lives maps to outside (refused at asset.outside), so only the petroleum storage facilities are reachable: such a filer is told only listed property qualifies and may enter zero. The earlier ruling recorded this under BUG-0326/T-183, which BUG-0373 now closes without this item; see bklg/asset.findings.md. The wording the package added (tax-exempt, governmental and foreign users) matches p946 p. 17.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' A choice that differs within a class is refused.

### 14 — Special depreciation allowance for this property
Status: **MATCH**

Model: Gives 100% for qualified property acquired after January 19, 2025, and 40% for property acquired after September 27, 2017 and before January 20, 2025 or under the 40% election. It gives zero on election out. The base is the depreciable basis (business portion less section 179), per 'multiplying the depreciable basis of the property by the applicable percentage.' The 60% cases, used property and excepted property are screened out.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MATCH**

Model: Line 25 uses the line 14 definition and computation for qualified listed property ('See the instructions for line 14 for the definition of qualified property and how to figure the deduction'). Vehicles are outside this form and listed property at 50% or less is refused.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MATCH**

Model: Per the line 6 instructions, 'Enter the elected section 179 cost of listed property in column (i) of line 26.'

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MATCH**

Model: Business cost less the section 179 deduction less 'Any special depreciation allowance included on line 14,' per the column (c) instructions. Other credit and deduction adjustments are screened out.

### 19(g) — MACRS depreciation for 2025 property
Status: **UNCLEAR**

Restated: Choose — [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = false → helper "MACRS depreciation, half-year convention"] [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = true → helper "MACRS depreciation, mid-quarter convention"]

Model: The mid-quarter test (fourth-quarter bases over 40% of all bases, after section 179 and before the special allowance) and 'Multiply column (c) by the applicable rate' match the text. However, the rate lookup is keyed only on period, convention and year, across both the declining-balance tables (A-1 to A-5) and the straight-line tables (A-8 to A-12). The text says 'The straight line method is the only applicable method for trees and vines bearing fruits or nuts,' which the screen does not exclude, and the restatement does not show how that method is chosen.

Ruling: scope; restatement accepted. i4562 p. 11, "The straight line method is the only applicable method for trees and vines bearing fruits or nuts": trees and vines are agriculture classes (p946 Table B-1, 01.x), which class_lives maps to outside and asset.outside refuses; the 150% method for farm property applies to property used in a farming business, reported on Schedule F (i1040sc p. 2, "Schedule F (Form 1040) to report profit or (loss) from farming"), and smart electric meters are refused by asset.screen. For the property the tool admits the rate is the 200% or 150% table the class determines.

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: Input of the half-year or mid-quarter convention (with quarter) used in the year placed in service, consistent with the column (e) instructions. Mid-month property is screened out.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MISMATCH**

Restated: Choose — [helper "The recovery period ended before 2025" = false → helper "MACRS depreciation for 2025"] [helper "The recovery period ended before 2025" = true → helper "Zero"]

Model: The rate is looked up only by period, convention and year, and no method is selected. The IRS text requires 150% declining balance for farm property placed before 2018: 'property used in a farming business. The applicable method is the 150% declining balance method' and 'For 3-, 5-, 7-, or 10-year property used in a farming business and placed in service after 2017 ... the 150% declining balance method is no longer required.' Such property placed 2005–2017 is not screened out, so it would get 200% DB rates. The unadjusted-basis computation (less section 179 and special allowance) and zero after the recovery period otherwise match.

Ruling: scope; restatement accepted. i4562 p. 12, "15- and 20-year property and property used in a farming business. The applicable method is the 150% declining balance method": the 15- and 20-year rates are in the table the project uses, agriculture classes are refused (class_lives maps 01.x to outside), and a farming business reports on Schedule F (i1040sc p. 2), not on this Schedule C asset entry.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g),' which uses line 19(g) for 2025 property and the line 17 method for earlier property. No deduction is allowed after the recovery period for listed property other than passenger automobiles.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Follows Pub. 946 Appendix B: check Table B-1, and use the Table B-2 activity class when the property is 'specifically included in that asset class.' It also offers the 'Certain Property for Which Recovery Periods Assigned' categories A, B and C, plus qualified improvement property."
  - key: "(d)"
    status: MATCH
    reason: "Takes the GDS (MACRS) recovery period shown for the asset class in Tables B-1/B-2, as Appendix B and the column (d) instructions direct."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "This input screen refuses cases the program does not support. Examples are dispositions, like-kind exchanges, real property, ADS, other methods, basis adjustments, short tax years, 168(k)(9) property and listed property at 50% or less qualified business use. Each item tracks IRS text, and the refusal names what is excluded."
  - key: "(b)"
    status: MATCH
    reason: "Input of the year placed in service. Earlier years are excluded by the screen."
  - key: "(c)"
    status: MATCH
    reason: "Computes the business/investment portion of cost: 'multiply the cost or other basis of the property by the percentage of business/investment use.' This is the first step of column (c); the section 179 and special allowance reductions are applied in later helpers. Percentages over 100 and listed property used 50% or less are refused."
  - key: "6(c)"
    status: MISMATCH
    reason: "The restatement says 'Only section 179 property qualifies' and gives a list that leaves out IRS-qualifying property that is not screened out. The IRS list includes 'Single purpose agricultural (livestock) or horticultural structures' and 'Storage facilities (except buildings and their structural components) used in connection with distributing petroleum or any primary product of petroleum.' A filer with such property would be told to enter zero."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The election out applies 'for any class of property ... for all such property in such class placed in service during the tax year.' A choice that differs within a class is refused."
  - key: "14"
    status: MATCH
    reason: "Gives 100% for qualified property acquired after January 19, 2025, and 40% for property acquired after September 27, 2017 and before January 20, 2025 or under the 40% election. It gives zero on election out. The base is the depreciable basis (business portion less section 179), per 'multiplying the depreciable basis of the property by the applicable percentage.' The 60% cases, used property and excepted property are screened out."
  - key: "25"
    status: MATCH
    reason: "Line 25 uses the line 14 definition and computation for qualified listed property ('See the instructions for line 14 for the definition of qualified property and how to figure the deduction'). Vehicles are outside this form and listed property at 50% or less is refused."
  - key: "26(i)"
    status: MATCH
    reason: "Per the line 6 instructions, 'Enter the elected section 179 cost of listed property in column (i) of line 26.'"
  - key: "19(c)"
    status: MATCH
    reason: "Business cost less the section 179 deduction less 'Any special depreciation allowance included on line 14,' per the column (c) instructions. Other credit and deduction adjustments are screened out."
  - key: "19(g)"
    status: UNCLEAR
    reason: "The mid-quarter test (fourth-quarter bases over 40% of all bases, after section 179 and before the special allowance) and 'Multiply column (c) by the applicable rate' match the text. However, the rate lookup is keyed only on period, convention and year, across both the declining-balance tables (A-1 to A-5) and the straight-line tables (A-8 to A-12). The text says 'The straight line method is the only applicable method for trees and vines bearing fruits or nuts,' which the screen does not exclude, and the restatement does not show how that method is chosen."
  - key: "(e)"
    status: MATCH
    reason: "Input of the half-year or mid-quarter convention (with quarter) used in the year placed in service, consistent with the column (e) instructions. Mid-month property is screened out."
  - key: "17"
    status: MISMATCH
    reason: "The rate is looked up only by period, convention and year, and no method is selected. The IRS text requires 150% declining balance for farm property placed before 2018: 'property used in a farming business. The applicable method is the 150% declining balance method' and 'For 3-, 5-, 7-, or 10-year property used in a farming business and placed in service after 2017 ... the 150% declining balance method is no longer required.' Such property placed 2005–2017 is not screened out, so it would get 200% DB rates. The unadjusted-basis computation (less section 179 and special allowance) and zero after the recovery period otherwise match."
  - key: "26(h)"
    status: MATCH
    reason: "For listed property used more than 50%, 'figure column (h) by following the instructions for line 19, column (g),' which uses line 19(g) for 2025 property and the line 17 method for earlier property. No deduction is allowed after the recovery period for listed property other than passenger automobiles."
```
```
