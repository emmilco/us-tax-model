# Review record 6d6dd4b3edb5 — render f2441

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f2441",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2"
 },
 "prompt_sha256": "6e0579bcdc95c0e45c9afa3119ee6a455b0e17b68bff038b6e7e6402ae7cb6db",
 "response_sha256": "027494f7eb56509519935b7d5acfd5c39948e4b8af48ca7fa714f74e73bcd6e4",
 "scope": "whole",
 "subjects": {
  "(document)": "7e56035cffc0ea921aefb924abbdad65e29ed2267f648d6e5f5514c915cf260b"
 }
}
```

<!-- part head -->
# Render comparison — f2441

The rendered English of every printed line of `Form 2441 — Child and Dependent Care Expenses (Parts I to III)` (`rendered/2025/f2441.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6e0579bcdc95c0e45c9afa3119ee6a455b0e17b68bff038b6e7e6402ae7cb6db |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7e56035cffc0ea921aefb924abbdad65e29ed2267f648d6e5f5514c915cf260b |
| lines judged | 36 |
| match / mismatch / unclear / missing | 31 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i2441 | 2025 | 1, 2, 3, 4, 5, 6 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 2, 3, 4, 5, 6 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p503 | For use in preparing 2025 returns | 3, 6, 7, 8, 10, 11, 12 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 6, 7, 8, 10, 11, 12 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i1040s8812 | 2025; printed date 2026-01-23 | 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | - | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 14, 47, 93, 94, 95, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 93, 95, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| iw2w3 | 2025; printed date 2025-02-19 | 17, 18, 19 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 17, 18, 19 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

<!-- part section 1 (box) -->
1 (box) — If you have more than three care providers, see the instructions and check this box
Status: **MATCH**

Model: The box is checked when you file the form and have more than three care providers, matching "If you have more than three care providers, see the instructions and check this box."

<!-- part section 2 (box) -->
2 (box) — If you have more than three qualifying persons, see the instructions and check this box
Status: **MATCH**

Model: The box is checked when the count of qualifying persons is more than three, matching "If you have more than three qualifying persons, see the instructions and check this box."

<!-- part section 3 -->
3 — Add the amounts in column (d) of line 2. Don't enter more than $3,000 if you had one quali
Status: **MATCH**

Model: With dependent care benefits (Part III completed) it takes line 31. Otherwise it takes the column (d) total capped at $3,000 or $6,000, as the line says.

<!-- part section 4 -->
4 — Enter your earned income
Status: **MISMATCH**

Restated: Add person.dc_earned over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.

Model: Earned income is figured from W-2 box 1 plus line 1e plus self-employment. The instructions start from "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z", which also includes lines 1b, 1c, 1d, 1f, 1g and 1h. No refusal names those lines.

Ruling: open

<!-- part section 5 -->
5 — If married filing jointly, enter your spouse's earned income (if you or your spouse was a
Status: **MISMATCH**

Restated: Choose — [helper "Married filing jointly" = true → helper "Your spouse's earned income for line 5"] [helper "Married filing jointly" = false → line 4]

Model: The choose structure (spouse's earned income if joint, else line 4) matches. However, the spouse's earned income uses the same per-person sum, which omits the rest of "Form 1040 ... line 1z" (lines 1b-1d, 1f-1h) without a refusal.

Ruling: open

<!-- part section 6 -->
6 — Enter the smallest of line 3, 4, or 5. If zero or less, enter -0-
Status: **MATCH**

Model: Smallest of lines 3, 4 and 5, with -0- if zero or less, as the line says.

<!-- part section 7 -->
7 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11a
Status: **MATCH**

Model: Takes Form 1040 line 11a, as the line says.

<!-- part section 8 -->
8 — Enter on line 8 the decimal amount shown below that applies to the amount on line 7
Status: **MATCH**

Model: Looks up the decimal amount by the AGI band for line 7, as the line says.

<!-- part section 9a -->
9a — Multiply line 6 by the decimal amount on line 8
Status: **MATCH**

Model: Line 6 times line 8.

<!-- part section 9b -->
9b — If you paid 2024 expenses in 2025, complete Worksheet A in the instructions. Enter the amo
Status: **MATCH**

Model: Enters -0- when no 2024 expenses were paid in 2025. The Worksheet A case is refused and named.

<!-- part section 9c -->
9c — Add lines 9a and 9b and enter the result
Status: **MATCH**

Model: Adds lines 9a and 9b.

<!-- part section CLW 1 -->
CLW 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 18
Status: **MATCH**

Model: Takes Form 1040 line 18, as worksheet line 1 says.

<!-- part section CLW 2 -->
CLW 2 — Enter the amount from Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (For
Status: **MISMATCH**

Restated: Enter the amount from s3 line 1.

Model: Only Schedule 3 line 1 is entered. The worksheet says "Enter the amount from Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14)", and line 6l is omitted with no refusal.

Ruling: open

<!-- part section CLW 3 -->
CLW 3 — Subtract line 2 from line 1. Also enter this amount on Form 2441, line 10. But if zero or
Status: **MATCH**

Model: Line 1 less line 2, floored at zero. A zero result yields no credit, which is equivalent to "stop; you can't take the credit".

<!-- part section 10 -->
10 — Tax liability limit. Enter the amount from the Credit Limit Worksheet in the instructions
Status: **MATCH**

Model: Takes the Credit Limit Worksheet line 3 amount.

<!-- part section 11 -->
11 — Credit for child and dependent care expenses. Enter the smaller of line 9c or line 10 here
Status: **MATCH**

Model: Smaller of line 9c or line 10. Married filing separately is refused and named.

<!-- part section 12 -->
12 — Enter the total amount of dependent care benefits you received in 2025. Amounts you receiv
Status: **MATCH**

Model: Totals W-2 box 10 less the part reported as wages in box 1, per "don't include amounts reported in box 10 that exceed your plan's exclusion and are therefore reported as wages in box 1". Sole-proprietor and partnership benefits are screened out by named refusals.

<!-- part section 13 -->
13 — Enter the amount, if any, you carried over from 2024 and used in 2025 during the grace per
Status: **MATCH**

Model: Input of the grace-period carryover from 2024 used in 2025, per the line 13 instructions.

<!-- part section 14 -->
14 — Enter the amount, if any, you forfeited or carried forward to 2026
Status: **MATCH**

Model: Input of amounts forfeited or carried forward that are included on line 12, per the line 14 instructions.

<!-- part section 15 -->
15 — Combine lines 12 through 14
Status: **MATCH**

Model: "Add the amounts on lines 12 and 13 and subtract from that total the amount on line 14."

<!-- part section 16 -->
16 — Enter the total amount of qualified expenses incurred in 2025 for the care of the qualifyi
Status: **MATCH**

Model: Expenses incurred and paid in 2025 plus 2025-incurred expenses paid later give "all qualified expenses incurred in 2025 ... It doesn't matter when the expenses were paid." Nondependent and employer-furnished cases are refused.

<!-- part section 17 -->
17 — Enter the smaller of line 15 or 16
Status: **MATCH**

Model: Smaller of line 15 or line 16. The employer-furnished care case is refused and named.

<!-- part section 18 -->
18 — Enter your earned income
Status: **MISMATCH**

Restated: Add person.dc_earned_b over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.

Model: Leaving out line 1e follows "earned income doesn't include any dependent care benefits shown on line 12". However, the base still omits the rest of "Form 1040 ... line 1z" (lines 1b-1d, 1f-1h) without a refusal.

Ruling: open

<!-- part section 19 -->
19 — If married filing jointly, enter your spouse's earned income (if you or your spouse was a
Status: **MISMATCH**

Restated: Choose — [helper "Married filing jointly" = true → helper "Your spouse's earned income for line 19"] [helper "Married filing jointly" = false → line 18]

Model: The choose structure matches and married filing separately is refused elsewhere. However, the spouse's earned income omits the rest of "line 1z" (lines 1b-1d, 1f-1h) without a refusal, as on line 18.

Ruling: open

<!-- part section 20 -->
20 — Enter the smallest of line 17, 18, or 19. If zero or less, enter -0-
Status: **MATCH**

Model: Smallest of lines 17, 18 and 19, with -0- if zero or less.

<!-- part section 21 -->
21 — Enter $5,000 ($2,500 if married filing separately and you were required to enter your spou
Status: **MATCH**

Model: Smaller of $5,000 and the plan maximum, per "Don't enter more than the maximum amount allowed under your dependent care plan". Married filing separately ($2,500) and differing plans are refused and named.

<!-- part section 22 -->
22 — Is any amount on line 12 or 13 from your sole proprietorship or partnership? No. Enter -0-
Status: **MATCH**

Model: Enters -0- (the "No" answer). Sole-proprietor and partnership dependent care assistance programs are screened out by named refusals.

<!-- part section 23 -->
23 — Subtract line 22 from line 15
Status: **MATCH**

Model: Line 15 less line 22.

<!-- part section 24 -->
24 — Deductible benefits. Enter the smallest of line 20, 21, or 22. Also, include this amount o
Status: **MATCH**

Model: Smaller of (smaller of line 20 or 21) and line 22, which equals the smallest of lines 20, 21 and 22.

<!-- part section 25 -->
25 — Excluded benefits. If you checked "No" on line 22, enter the smaller of line 20 or line 21
Status: **MATCH**

Model: With line 22 at -0-, line 24 is zero. Subtracting it from the smaller of lines 20 or 21 equals the "No" instruction. The line 13 grace-period case is refused and named.

<!-- part section 26 -->
26 — Taxable benefits. Subtract line 25 from line 23. If zero or less, enter -0-. Also, enter t
Status: **MATCH**

Model: Line 23 less line 25, with -0- if zero or less.

<!-- part section 27 -->
27 — Enter $3,000 ($6,000 if two or more qualifying persons)
Status: **MATCH**

Model: "Enter $3,000 ($6,000 if two or more qualifying persons)."

<!-- part section 28 -->
28 — Add lines 24 and 25
Status: **MATCH**

Model: Adds lines 24 and 25.

<!-- part section 29 -->
29 — Subtract line 28 from line 27. If zero or less, stop. You can't take the credit. Exception
Status: **MATCH**

Model: Line 27 less line 28, floored at zero, which gives no credit as with "stop". The 2024-expense exception is refused under line 9b.

<!-- part section 30 -->
30 — Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on
Status: **MATCH**

Model: Column (d) total less line 28 benefits, floored at zero, per "Don't include in column (d) any benefits shown on line 28". Employer-furnished care is refused and named.

<!-- part section 31 -->
31 — Enter the smaller of line 29 or 30. Also, enter this amount on line 3 on page 1 of this fo
Status: **MATCH**

Model: Smaller of line 29 or line 30.

<!-- part raw -->

## Raw response

```yaml
```yaml
lines:
  - key: "1 (box)"
    status: MATCH
    reason: "The box is checked when you file the form and have more than three care providers, matching \"If you have more than three care providers, see the instructions and check this box.\""
  - key: "2 (box)"
    status: MATCH
    reason: "The box is checked when the count of qualifying persons is more than three, matching \"If you have more than three qualifying persons, see the instructions and check this box.\""
  - key: "3"
    status: MATCH
    reason: "With dependent care benefits (Part III completed) it takes line 31. Otherwise it takes the column (d) total capped at $3,000 or $6,000, as the line says."
  - key: "4"
    status: MISMATCH
    reason: "Earned income is figured from W-2 box 1 plus line 1e plus self-employment. The instructions start from \"The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z\", which also includes lines 1b, 1c, 1d, 1f, 1g and 1h. No refusal names those lines."
  - key: "5"
    status: MISMATCH
    reason: "The choose structure (spouse's earned income if joint, else line 4) matches. However, the spouse's earned income uses the same per-person sum, which omits the rest of \"Form 1040 ... line 1z\" (lines 1b-1d, 1f-1h) without a refusal."
  - key: "6"
    status: MATCH
    reason: "Smallest of lines 3, 4 and 5, with -0- if zero or less, as the line says."
  - key: "7"
    status: MATCH
    reason: "Takes Form 1040 line 11a, as the line says."
  - key: "8"
    status: MATCH
    reason: "Looks up the decimal amount by the AGI band for line 7, as the line says."
  - key: "9a"
    status: MATCH
    reason: "Line 6 times line 8."
  - key: "9b"
    status: MATCH
    reason: "Enters -0- when no 2024 expenses were paid in 2025. The Worksheet A case is refused and named."
  - key: "9c"
    status: MATCH
    reason: "Adds lines 9a and 9b."
  - key: "CLW 1"
    status: MATCH
    reason: "Takes Form 1040 line 18, as worksheet line 1 says."
  - key: "CLW 2"
    status: MISMATCH
    reason: "Only Schedule 3 line 1 is entered. The worksheet says \"Enter the amount from Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14)\", and line 6l is omitted with no refusal."
  - key: "CLW 3"
    status: MATCH
    reason: "Line 1 less line 2, floored at zero. A zero result yields no credit, which is equivalent to \"stop; you can't take the credit\"."
  - key: "10"
    status: MATCH
    reason: "Takes the Credit Limit Worksheet line 3 amount."
  - key: "11"
    status: MATCH
    reason: "Smaller of line 9c or line 10. Married filing separately is refused and named."
  - key: "12"
    status: MATCH
    reason: "Totals W-2 box 10 less the part reported as wages in box 1, per \"don't include amounts reported in box 10 that exceed your plan's exclusion and are therefore reported as wages in box 1\". Sole-proprietor and partnership benefits are screened out by named refusals."
  - key: "13"
    status: MATCH
    reason: "Input of the grace-period carryover from 2024 used in 2025, per the line 13 instructions."
  - key: "14"
    status: MATCH
    reason: "Input of amounts forfeited or carried forward that are included on line 12, per the line 14 instructions."
  - key: "15"
    status: MATCH
    reason: "\"Add the amounts on lines 12 and 13 and subtract from that total the amount on line 14.\""
  - key: "16"
    status: MATCH
    reason: "Expenses incurred and paid in 2025 plus 2025-incurred expenses paid later give \"all qualified expenses incurred in 2025 ... It doesn't matter when the expenses were paid.\" Nondependent and employer-furnished cases are refused."
  - key: "17"
    status: MATCH
    reason: "Smaller of line 15 or line 16. The employer-furnished care case is refused and named."
  - key: "18"
    status: MISMATCH
    reason: "Leaving out line 1e follows \"earned income doesn't include any dependent care benefits shown on line 12\". However, the base still omits the rest of \"Form 1040 ... line 1z\" (lines 1b-1d, 1f-1h) without a refusal."
  - key: "19"
    status: MISMATCH
    reason: "The choose structure matches and married filing separately is refused elsewhere. However, the spouse's earned income omits the rest of \"line 1z\" (lines 1b-1d, 1f-1h) without a refusal, as on line 18."
  - key: "20"
    status: MATCH
    reason: "Smallest of lines 17, 18 and 19, with -0- if zero or less."
  - key: "21"
    status: MATCH
    reason: "Smaller of $5,000 and the plan maximum, per \"Don't enter more than the maximum amount allowed under your dependent care plan\". Married filing separately ($2,500) and differing plans are refused and named."
  - key: "22"
    status: MATCH
    reason: "Enters -0- (the \"No\" answer). Sole-proprietor and partnership dependent care assistance programs are screened out by named refusals."
  - key: "23"
    status: MATCH
    reason: "Line 15 less line 22."
  - key: "24"
    status: MATCH
    reason: "Smaller of (smaller of line 20 or 21) and line 22, which equals the smallest of lines 20, 21 and 22."
  - key: "25"
    status: MATCH
    reason: "With line 22 at -0-, line 24 is zero. Subtracting it from the smaller of lines 20 or 21 equals the \"No\" instruction. The line 13 grace-period case is refused and named."
  - key: "26"
    status: MATCH
    reason: "Line 23 less line 25, with -0- if zero or less."
  - key: "27"
    status: MATCH
    reason: "\"Enter $3,000 ($6,000 if two or more qualifying persons).\""
  - key: "28"
    status: MATCH
    reason: "Adds lines 24 and 25."
  - key: "29"
    status: MATCH
    reason: "Line 27 less line 28, floored at zero, which gives no credit as with \"stop\". The 2024-expense exception is refused under line 9b."
  - key: "30"
    status: MATCH
    reason: "Column (d) total less line 28 benefits, floored at zero, per \"Don't include in column (d) any benefits shown on line 28\". Employer-furnished care is refused and named."
  - key: "31"
    status: MATCH
    reason: "Smaller of line 29 or line 30."
```
```

<!-- end -->
