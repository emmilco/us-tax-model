# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6e37426479c5001decaf24b5fed6218f10bfd53d22f8f3fe0fada43d99c66083 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 0345c863b99b551e4ed2f166b4102d5c9670c8b7f6f5ce57e88706e875999e10 |
| lines judged | 24 |
| match / mismatch / unclear / missing | 22 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35, 91 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34, 91 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MISMATCH**

Restated: Input — Unreimbursed eligible medical and dental expenses paid in 2025 (Pub. 502 lists what counts) for yourself, your spouse, your dependents, your child whom you do not claim only because of the rules for children of divorced or separated parents, and anyone you could have claimed as a dependent except that the person had gross income of $5,200 or more or filed a joint return. Reduce them by payments from insurance or other sources, but do not reduce them by a 2025 reimbursement of expenses paid in an earlier year. Leave out: amounts equal to tax-free distributions from a health savings account (HSA) or an Archer MSA; insurance premiums paid by a pretax reduction of your pay, and premiums and other medical and dental expenses paid by an employer-sponsored health plan (cafeteria plan) unless they are included in box 1 of your Form W-2; premiums for someone on your policy who is not one of the people listed above (for example a nondependent child under age 27), unless you had family coverage when you added that person and your premiums did not increase; if you are a retired public safety officer, premiums to the extent paid with a tax-free distribution from your retirement plan; the housework part of pay to someone who did both nursing and housework (only the nursing help counts); and meals while away from home for medical care, other than hospital care, which includes its meals and lodging (other lodging for medical care counts at no more than $50 a night for each person who meets the Pub. 502 lodging requirements). Reduce health insurance premiums by any self-employed health insurance deduction on Schedule 1 (Form 1040), line 17. For Marketplace coverage on a Form 1095-A, include the total premiums (including the part paid by advance payments of the premium tax credit), minus the premium tax credit allowed on Form 8962, line 24, and minus any excess advance payments you do not have to repay because of the repayment limit (Form 8962, line 27 minus line 29); advance payments you do repay count as premiums you paid. Include qualified long-term care insurance premiums only up to the limit for the age at the end of 2025 of the person for whom they were paid: $480 if 40 or under, $900 if 41 to 50, $1,800 if 51 to 60, $4,810 if 61 to 70, $6,020 if 71 or older. On the final return of a person who died in 2025, include the medical expenses paid out of that person's estate that Pub. 502 allows on the final return.

Model: The restatement leaves out one person whose expenses count. The IRS text also includes "Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return." A filer following the restatement would leave those expenses out.

Ruling: scope; i1040sca p. 2, Line 1: "Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return." The restatement leaves that person out because the case cannot reach line 1: a filer who, or whose joint spouse, can be claimed as a dependent is refused by sa.dependent ("Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien?"), on the deduction line Form 1040 line 12e reads, so no completed return has that person's expenses to enter. PENDING-4 of the ptc-sa package records the omission as deliberate for this reason. The rest of the PENDING-2 and PENDING-4 wording (Marketplace premiums less the credit allowed and the unrepaid excess advance payments; whose expenses count; the cafeteria-plan and nondependent-premium exclusions) is not objected to.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: It follows the line 5a income-tax instructions: withholding, prior-year taxes, estimated payments, the listed mandatory fund contributions, no reduction for refunds, the safe harbor and U.S. territory taxes. The sales-tax election is excluded through the sa.unsupported refusal.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: It tracks the line 5b instructions: uniform assessment, the listed exclusions, mortgage-company payments, refund and buyer-charge reductions, the assessed-before-2026 rule and territory taxes.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: It matches "based on value alone and were imposed on a yearly basis," the car registration example and the prepayment rule.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is "Home mortgage interest and points reported to you on Form 1098." Interest subject to the debt or use limits is excluded through the sa.unsupported refusal.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is "Gifts by cash or check." Gifts reduced by income limits or carried over are excluded through the charity_limited refusal.

### 2 — Amount from sa.agi_floor
Status: **MATCH**

Model: Line 2 is "Enter amount from Form 1040 or 1040-SR, line 11b." Flooring at zero only changes the result when AGI is negative, and then line 3 cannot usefully be negative anyway.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Matches "Multiply line 2 by 7.5% (0.075)."

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Matches "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-."

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Matches "Add lines 5a through 5c."

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper chain reproduces the SALT Worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if MFS), but not less than $10,000, halved if MFS, then the smaller of that or line 5d. This also gives $40,000 or $20,000 at lower AGI, and excluded-income cases are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Line 6 covers foreign income taxes and GST. Both are excluded by the sa.unsupported refusal, so zero is correct for the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Mortgage interest not reported on Form 1098 is excluded by the sa.unsupported refusal, so zero is correct for the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Points not reported on Form 1098 are excluded by the sa.unsupported refusal, so zero is correct for the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Carryovers from a prior year are excluded by the charity_limited refusal, so zero is correct for the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Casualty and theft losses (Form 4684) are excluded by the sa.unsupported refusal, so zero is correct for the supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: Gambling losses are allowed "only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." Other line 16 items and the net qualified disaster loss are refused.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Matches "Add lines 5e and 6."

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Matches "Add lines 8a through 8c" (line 8d is reserved).

### 9 — Amount from f4952.line8
Status: **UNCLEAR**

Restated: Enter the amount from f4952 line 8.

Model: The form says "Investment interest. Attach Form 4952 if required," which implies some filers deduct investment interest without Form 4952. The restated f4952 line 8 is zero when Form 4952 is not used. The line 9 instructions are not in the pages given, so I cannot tell whether those filers would get zero wrongly.

Ruling: representation; the model asks whether a filer may deduct investment interest without Form 4952 and get zero. f4952 (2025) p. 3, Who Must File: "you must file Form 4952 to claim a deduction for your investment interest expense. Exception. You don’t have to file Form 4952 if all of the following apply" (investment income from interest and ordinary dividends less qualified dividends above the expense, no other deductible investment expenses, no 2024 carryover). Such a filer still has investment interest on Form 4952 line 1 above zero, so f4952.used is true and f4952.line8 is the smaller of lines 3 and 6, which under the exception's first condition is the whole interest: the form is used as the computation, whether or not it is filed (f4952.required). Line 8 is zero only with no investment interest, no carryforward and no election, when there is nothing to deduct. Inspected in forms/2025/f4952.yaml (f4952.used, f4952.line8) after PENDING-6 of the credits-misc package.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Matches "Add lines 8e and 9."

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: It sums noncash gift deductions before income limits. It applies the good-used-condition rule and the $250 acknowledgment rule, and Section B and special-property cases are refused, consistent with the line 12, Form 8283 and instruction text.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Matches "Add lines 11 through 13."

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Matches "Add the amounts in the far right column for lines 4 through 16" (lines 4, 7, 10, 14, 15 and 16).

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement leaves out one person whose expenses count. The IRS text also includes \"Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return.\" A filer following the restatement would leave those expenses out."
  - key: "5a"
    status: MATCH
    reason: "It follows the line 5a income-tax instructions: withholding, prior-year taxes, estimated payments, the listed mandatory fund contributions, no reduction for refunds, the safe harbor and U.S. territory taxes. The sales-tax election is excluded through the sa.unsupported refusal."
  - key: "5b"
    status: MATCH
    reason: "It tracks the line 5b instructions: uniform assessment, the listed exclusions, mortgage-company payments, refund and buyer-charge reductions, the assessed-before-2026 rule and territory taxes."
  - key: "5c"
    status: MATCH
    reason: "It matches \"based on value alone and were imposed on a yearly basis,\" the car registration example and the prepayment rule."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is \"Home mortgage interest and points reported to you on Form 1098.\" Interest subject to the debt or use limits is excluded through the sa.unsupported refusal."
  - key: "11"
    status: MATCH
    reason: "Line 11 is \"Gifts by cash or check.\" Gifts reduced by income limits or carried over are excluded through the charity_limited refusal."
  - key: "2"
    status: MATCH
    reason: "Line 2 is \"Enter amount from Form 1040 or 1040-SR, line 11b.\" Flooring at zero only changes the result when AGI is negative, and then line 3 cannot usefully be negative anyway."
  - key: "3"
    status: MATCH
    reason: "Matches \"Multiply line 2 by 7.5% (0.075).\""
  - key: "4"
    status: MATCH
    reason: "Matches \"Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.\""
  - key: "5d"
    status: MATCH
    reason: "Matches \"Add lines 5a through 5c.\""
  - key: "5e"
    status: MATCH
    reason: "The helper chain reproduces the SALT Worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if MFS), but not less than $10,000, halved if MFS, then the smaller of that or line 5d. This also gives $40,000 or $20,000 at lower AGI, and excluded-income cases are refused."
  - key: "6"
    status: MATCH
    reason: "Line 6 covers foreign income taxes and GST. Both are excluded by the sa.unsupported refusal, so zero is correct for the supported cases."
  - key: "8b"
    status: MATCH
    reason: "Mortgage interest not reported on Form 1098 is excluded by the sa.unsupported refusal, so zero is correct for the supported cases."
  - key: "8c"
    status: MATCH
    reason: "Points not reported on Form 1098 are excluded by the sa.unsupported refusal, so zero is correct for the supported cases."
  - key: "13"
    status: MATCH
    reason: "Carryovers from a prior year are excluded by the charity_limited refusal, so zero is correct for the supported cases."
  - key: "15"
    status: MATCH
    reason: "Casualty and theft losses (Form 4684) are excluded by the sa.unsupported refusal, so zero is correct for the supported cases."
  - key: "16"
    status: MATCH
    reason: "Gambling losses are allowed \"only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b.\" Other line 16 items and the net qualified disaster loss are refused."
  - key: "7"
    status: MATCH
    reason: "Matches \"Add lines 5e and 6.\""
  - key: "8e"
    status: MATCH
    reason: "Matches \"Add lines 8a through 8c\" (line 8d is reserved)."
  - key: "9"
    status: UNCLEAR
    reason: "The form says \"Investment interest. Attach Form 4952 if required,\" which implies some filers deduct investment interest without Form 4952. The restated f4952 line 8 is zero when Form 4952 is not used. The line 9 instructions are not in the pages given, so I cannot tell whether those filers would get zero wrongly."
  - key: "10"
    status: MATCH
    reason: "Matches \"Add lines 8e and 9.\""
  - key: "12"
    status: MATCH
    reason: "It sums noncash gift deductions before income limits. It applies the good-used-condition rule and the $250 acknowledgment rule, and Section B and special-property cases are refused, consistent with the line 12, Form 8283 and instruction text."
  - key: "14"
    status: MATCH
    reason: "Matches \"Add lines 11 through 13.\""
  - key: "17"
    status: MATCH
    reason: "Matches \"Add the amounts in the far right column for lines 4 through 16\" (lines 4, 7, 10, 14, 15 and 16)."
```
```
