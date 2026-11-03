# Render comparison — asset

The rendered English of every printed line of `Form 4562 — one item of depreciable property (other than a vehicle) of a business` (`rendered/2025/asset.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d4a7aa92ad1f56d3b522f5f5478e21c59c30c4601628c2f19f764493b9e34db0 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | aca9afbf03c111e08e13f231c7b354cd49b268c2363d4a81476f384026f7ff99 |
| lines judged | 15 |
| match / mismatch / unclear / missing | 9 / 6 / 0 / 0 |
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

Model: The asset class lookup follows Table B-1/B-2 and the special Appendix B classes A, B, C, and QIP, consistent with the line 19 classification instructions.

### (d) — Recovery period under GDS for the asset class
Status: **MISMATCH**

Restated: Find the entry in GDS recovery period by asset class (Pub. 946, Appendix B, Tables B-1 and B-2) for asset_class column (a).

Model: The IRS assigns qualified improvement property to 15-year property in the line 19 classification instructions ("Qualified improvement property ... placed in service by you after December 31, 2017"), but the restatement only points to Appendix B Tables B-1/B-2, which do not list QIP.

Ruling: representation; cqip, qualified improvement property placed in service after 2017, is one of the asset class answers and maps to 15-year straight line (Pub. 946 Table 4-1).

### (screen) (asset.screen) — Does any of these apply to this property?
Status: **MATCH**

Model: The listed screen conditions are the cases the program refuses as outside the supported Form 4562 computation, and the refusal names the excluded categories.

### (b) — Year placed in service
Status: **MATCH**

Model: The year placed in service determines the recovery year; the program separately captures the quarter needed for the mid-quarter convention.

### (c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **MISMATCH**

Restated: Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.

Model: IRS line 26/27 uses qualified business use: "Use line 26 to figure depreciation for property used more than 50% in a qualified business use. Use line 27 ... 50% or less in a qualified business use." The refusal gate asset.listed_low instead tests the business/investment-use percentage.

Ruling: representation; the listed-property questions now state the qualified business use limits (BUG-0315), so the percentage asked is the one the 50% test uses; any remaining exclusions are the BUG-0307 gap.

### 6(c) — Section 179 elected cost
Status: **MATCH**

Model: The restatement describes the elected section 179 cost, eligibility, limits, and cash/trade-in rule, and excludes listed property from line 6 as the IRS text requires.

### (screen) (asset.bonus_same) — Is the choice the same for all property of this class placed in service in 2025?
Status: **MATCH**

Model: The IRS allows the special allowance election out for any class of property for all such property in the class placed in service during the tax year.

### 14 — Special depreciation allowance for this property
Status: **MISMATCH**

Restated: Choose — [helper "Special depreciation allowance for this class of property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025; 40% if acquired after September 27, 2017 and before January 20, 2025"] [helper "Special depreciation allowance for this class of property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for this class of property" = 'none' → helper "Zero"]

Model: IRS says to figure the allowance by subtracting from the business/investment cost "any credits and deductions allocable to the property"; the special-allowance helpers use only cost less the section 179 election.

Ruling: scope; asset.screen refuses property whose basis was adjusted for anything other than depreciation, so on a computed return there are no other credits or deductions allocable to it.

### 25 — Special depreciation allowance for this listed property (line 25)
Status: **MISMATCH**

Restated: Enter the amount from line 14.

Model: IRS says "Enter on line 25 your total special depreciation allowance for all qualified listed property." The restatement copies line 14, which the program itself limits to non-listed property.

Ruling: representation; restatement accepted. The per-asset allowance appears on line 25 for listed property and line 14 otherwise, figured by the same instructions.

### 26(i) — Elected section 179 cost of this listed property (column (i))
Status: **MISMATCH**

Restated: Enter the amount from line 6(c).

Model: IRS says "Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26." Line 26(i) is the listed property election, not the line 6(c) amount.

Ruling: representation; restatement accepted. The per-asset section 179 election appears in column (i) for listed property and on line 6 otherwise.

### 19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **MISMATCH**

Restated: Enter the amount from helper "Basis for MACRS depreciation (after section 179 and the special allowance)".

Model: IRS says after multiplying cost by business/investment use, "subtract any credits and deductions allocable to the property." The helper only subtracts section 179 and the special allowance, omitting other required credits and deductions.

Ruling: scope; asset.screen refuses property whose basis was adjusted for anything other than depreciation, so on a computed return there are no other credits or deductions allocable to it.

### 19(g) — MACRS depreciation for 2025 property
Status: **MATCH**

Model: It chooses MACRS half-year or mid-quarter depreciation based on the 40% mid-quarter test, matching line 19 column (g).

### (e) — Convention used in the year placed in service
Status: **MATCH**

Model: The supported conventions are half-year and mid-quarter with the quarter placed in service; mid-month is unnecessary because real property is screened out.

### 17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **MATCH**

Model: It computes current-year MACRS for property placed in service before 2025 and zero when the recovery period ended before 2025, consistent with line 17.

### 26(h) — Depreciation of this listed property (column (h))
Status: **MATCH**

Model: For the single listed property this reduces to the MACRS deduction (line 19(g) for 2025 property or the equivalent prior-year computation), as line 26(h) directs.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The asset class lookup follows Table B-1/B-2 and the special Appendix B classes A, B, C, and QIP, consistent with the line 19 classification instructions."
  - key: "(d)"
    status: MISMATCH
    reason: "The IRS assigns qualified improvement property to 15-year property in the line 19 classification instructions (\"Qualified improvement property ... placed in service by you after December 31, 2017\"), but the restatement only points to Appendix B Tables B-1/B-2, which do not list QIP."
  - key: "(screen) (asset.screen)"
    status: MATCH
    reason: "The listed screen conditions are the cases the program refuses as outside the supported Form 4562 computation, and the refusal names the excluded categories."
  - key: "(b)"
    status: MATCH
    reason: "The year placed in service determines the recovery year; the program separately captures the quarter needed for the mid-quarter convention."
  - key: "(c)"
    status: MISMATCH
    reason: "IRS line 26/27 uses qualified business use: \"Use line 26 to figure depreciation for property used more than 50% in a qualified business use. Use line 27 ... 50% or less in a qualified business use.\" The refusal gate asset.listed_low instead tests the business/investment-use percentage."
  - key: "6(c)"
    status: MATCH
    reason: "The restatement describes the elected section 179 cost, eligibility, limits, and cash/trade-in rule, and excludes listed property from line 6 as the IRS text requires."
  - key: "(screen) (asset.bonus_same)"
    status: MATCH
    reason: "The IRS allows the special allowance election out for any class of property for all such property in the class placed in service during the tax year."
  - key: "14"
    status: MISMATCH
    reason: "IRS says to figure the allowance by subtracting from the business/investment cost \"any credits and deductions allocable to the property\"; the special-allowance helpers use only cost less the section 179 election."
  - key: "25"
    status: MISMATCH
    reason: "IRS says \"Enter on line 25 your total special depreciation allowance for all qualified listed property.\" The restatement copies line 14, which the program itself limits to non-listed property."
  - key: "26(i)"
    status: MISMATCH
    reason: "IRS says \"Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.\" Line 26(i) is the listed property election, not the line 6(c) amount."
  - key: "19(c)"
    status: MISMATCH
    reason: "IRS says after multiplying cost by business/investment use, \"subtract any credits and deductions allocable to the property.\" The helper only subtracts section 179 and the special allowance, omitting other required credits and deductions."
  - key: "19(g)"
    status: MATCH
    reason: "It chooses MACRS half-year or mid-quarter depreciation based on the 40% mid-quarter test, matching line 19 column (g)."
  - key: "(e)"
    status: MATCH
    reason: "The supported conventions are half-year and mid-quarter with the quarter placed in service; mid-month is unnecessary because real property is screened out."
  - key: "17"
    status: MATCH
    reason: "It computes current-year MACRS for property placed in service before 2025 and zero when the recovery period ended before 2025, consistent with line 17."
  - key: "26(h)"
    status: MATCH
    reason: "For the single listed property this reduces to the MACRS deduction (line 19(g) for 2025 property or the equivalent prior-year computation), as line 26(h) directs."
```
