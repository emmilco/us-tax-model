# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 6e37426479c5001decaf24b5fed6218f10bfd53d22f8f3fe0fada43d99c66083 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 0345c863b99b551e4ed2f166b4102d5c9670c8b7f6f5ce57e88706e875999e10 |
| lines judged | 24 |
| match / mismatch / unclear / missing | 22 / 2 / 0 / 0 |
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

Model: The restatement omits the eligible category in the IRS instructions: 'Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return.'

Ruling: scope; i1040sca p. 2, Line 1: "Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return." The restatement leaves that person out because the case cannot reach line 1: a filer who, or whose joint spouse, can be claimed as a dependent is refused by sa.dependent ("Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien?"), on the deduction line Form 1040 line 12e reads, so no completed return has that person's expenses to enter. PENDING-4 of the ptc-sa package records the omission as deliberate for this reason. The rest of the PENDING-2 and PENDING-4 wording (Marketplace premiums less the credit allowed and the unrepaid excess advance payments; whose expenses count; the cafeteria-plan and nondependent-premium exclusions) is not objected to.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Restates the IRS line 5a income-tax items, exclusions, refund treatment, safe-harbor credit, and U.S. territory rules.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Restates the IRS real estate tax rules, including uniform assessment, exclusions, mortgage-company payments, refunds, assessment timing, and U.S. territory taxes.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Restates the IRS personal property tax rules: value-based and yearly, car registration allocation, timing, and U.S. territory taxes.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Limits line 8a to eligible Form 1098 mortgage interest and points when the debt/use limits do not apply, matching the supported part of the IRS line.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Restates cash/check charitable gifts with benefit and substantiation reductions; the refusal covers income-limited and carryover charitable cases.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: The IRS line says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement uses an AGI helper that is not less than zero, adding a floor not in the line.

Ruling: ambiguity; amb.2025.sa_medical_negative_agi. The model says the restatement floors Form 1040 line 11b at zero. Schedule A (2025) line 2: "Enter amount from Form 1040 or 1040-SR, line 11b"; the project floors adjusted gross income at zero for the 7.5% medical-expense limitation and displays that floored amount, the recorded reading for a negative AGI, not a new defect. Unchanged by the backlog packages.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Multiplies line 2 by 7.5% (0.075), equivalent to 75/1000.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Subtracts line 3 from line 1 and enters zero when the result is zero or less, matching the IRS line's zero floor.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Adds lines 5a, 5b, and 5c as the IRS line directs.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: Uses the smaller of line 5d and the worksheet ceiling helper, whose formula follows the Schedule A line 5e/worksheet cap including the married-filing-separately half.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Enters zero; the refusal covers foreign tax/GST and other unsupported items, so zero is correct within supported cases for the other-taxes line.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Enters zero; the refusal covers mortgage interest not on Form 1098, so zero is correct when no unsupported 8b amount exists.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Enters zero; the refusal covers points not reported on Form 1098, so zero is correct when no unsupported 8c amount exists.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Enters zero; the refusal covers charitable carryovers and income limits, so zero is correct when no carryover exists.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Enters zero; the refusal covers casualty/theft losses and Form 4684, so zero is correct when no such loss exists.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: Computes gambling losses limited to Schedule 1 line 8b when there are gambling winnings, and zero otherwise, with refusal for other line 16 items.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Adds lines 5e and 6 as the IRS line directs.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Adds lines 8a, 8b, and 8c as the IRS line directs.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Takes the amount from Form 4952 line 8, which the provided IRS text identifies as the investment interest deduction.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Adds lines 8e and 9 as the IRS line directs.

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Adds allowed noncash gift deductions after valuation/basis and substantiation reductions, with refusals for special property and Form 8283 Section B cases; matches line 12 for supported gifts.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Adds lines 11, 12, and 13 as the IRS line directs.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Adds lines 4, 7, 10, 14, 15, and 16, which are the Schedule A far-right amounts for lines 4 through 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement omits the eligible category in the IRS instructions: 'Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return.'"
  - key: "5a"
    status: MATCH
    reason: "Restates the IRS line 5a income-tax items, exclusions, refund treatment, safe-harbor credit, and U.S. territory rules."
  - key: "5b"
    status: MATCH
    reason: "Restates the IRS real estate tax rules, including uniform assessment, exclusions, mortgage-company payments, refunds, assessment timing, and U.S. territory taxes."
  - key: "5c"
    status: MATCH
    reason: "Restates the IRS personal property tax rules: value-based and yearly, car registration allocation, timing, and U.S. territory taxes."
  - key: "8a"
    status: MATCH
    reason: "Limits line 8a to eligible Form 1098 mortgage interest and points when the debt/use limits do not apply, matching the supported part of the IRS line."
  - key: "11"
    status: MATCH
    reason: "Restates cash/check charitable gifts with benefit and substantiation reductions; the refusal covers income-limited and carryover charitable cases."
  - key: "2"
    status: MISMATCH
    reason: "The IRS line says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement uses an AGI helper that is not less than zero, adding a floor not in the line."
  - key: "3"
    status: MATCH
    reason: "Multiplies line 2 by 7.5% (0.075), equivalent to 75/1000."
  - key: "4"
    status: MATCH
    reason: "Subtracts line 3 from line 1 and enters zero when the result is zero or less, matching the IRS line's zero floor."
  - key: "5d"
    status: MATCH
    reason: "Adds lines 5a, 5b, and 5c as the IRS line directs."
  - key: "5e"
    status: MATCH
    reason: "Uses the smaller of line 5d and the worksheet ceiling helper, whose formula follows the Schedule A line 5e/worksheet cap including the married-filing-separately half."
  - key: "6"
    status: MATCH
    reason: "Enters zero; the refusal covers foreign tax/GST and other unsupported items, so zero is correct within supported cases for the other-taxes line."
  - key: "8b"
    status: MATCH
    reason: "Enters zero; the refusal covers mortgage interest not on Form 1098, so zero is correct when no unsupported 8b amount exists."
  - key: "8c"
    status: MATCH
    reason: "Enters zero; the refusal covers points not reported on Form 1098, so zero is correct when no unsupported 8c amount exists."
  - key: "13"
    status: MATCH
    reason: "Enters zero; the refusal covers charitable carryovers and income limits, so zero is correct when no carryover exists."
  - key: "15"
    status: MATCH
    reason: "Enters zero; the refusal covers casualty/theft losses and Form 4684, so zero is correct when no such loss exists."
  - key: "16"
    status: MATCH
    reason: "Computes gambling losses limited to Schedule 1 line 8b when there are gambling winnings, and zero otherwise, with refusal for other line 16 items."
  - key: "7"
    status: MATCH
    reason: "Adds lines 5e and 6 as the IRS line directs."
  - key: "8e"
    status: MATCH
    reason: "Adds lines 8a, 8b, and 8c as the IRS line directs."
  - key: "9"
    status: MATCH
    reason: "Takes the amount from Form 4952 line 8, which the provided IRS text identifies as the investment interest deduction."
  - key: "10"
    status: MATCH
    reason: "Adds lines 8e and 9 as the IRS line directs."
  - key: "12"
    status: MATCH
    reason: "Adds allowed noncash gift deductions after valuation/basis and substantiation reductions, with refusals for special property and Form 8283 Section B cases; matches line 12 for supported gifts."
  - key: "14"
    status: MATCH
    reason: "Adds lines 11, 12, and 13 as the IRS line directs."
  - key: "17"
    status: MATCH
    reason: "Adds lines 4, 7, 10, 14, 15, and 16, which are the Schedule A far-right amounts for lines 4 through 16."
```
