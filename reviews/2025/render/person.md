# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d7d7cf6a8dc0ebc18b94cd21b3891e6cca71e0e07c1c8d49d77c266b76b52ae2 |
| subject sha256 | d282cf2c65d753a935cfca92e2549c6fb8a9ac7d32c84ae71678a379dfc742c0 |
| lines judged | 20 |
| match / mismatch / unclear / missing | 17 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 41, 47, 93, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 41, 93, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 10, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 10, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: Line 11 covers 'social security or tier 1 railroad retirement (RRTA) tax'. RRTA amounts are reported in 'Form W-2, box 14', and the Form 8959 instructions name Form CT-2 employee representatives. Asking this question so the program can refuse the RRTA path is consistent with the text.

### employers — Total w2.one for this person
Status: **MATCH**

Model: The text says 'had more than one employer for 2025' and 'Figure this amount separately for you and your spouse'. Counting each person's W-2s matches this if each employer issues one W-2. Two W-2s from the same employer would be counted as two employers.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts the employers covered by 'if any one employer withheld more than $10,918.20'.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: It is true when at least one employer withheld more than $10,918.20, which is the condition that blocks claiming the excess on the return.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: This sums each person's 'total wages' for the 'more than $176,100' test. The glossary ties w2.wages to boxes 3 and 7, which fits the social security wage base.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Box 4 is 'Social security tax withheld', so the sum is the total withheld that is compared with $10,918.20. Tier 1 RRTA is refused separately.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: It follows 'had more than one employer for 2025 and total wages of more than $176,100'.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: It follows 'credit ... for the amount withheld in excess of $10,918.20', with a floor of zero.

### zero — No excess credit
Status: **MATCH**

Model: This is a zero constant used when the person is not eligible.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The credit is the excess when eligible and zero otherwise. The refusals cover 'if any one employer withheld more than $10,918.20 ... file a claim for refund using Form 843' and excess tier 2 RRTA tax ('use Form 843').

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MISMATCH**

Restated: Input — Does any of these apply to this person: church employee income (wages from a church that elected exemption from social security and Medicare taxes); being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029; net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee); farm income (Schedule F) or Conservation Reserve Program payments; electing an optional method (Schedule SE Part II); a chapter 11 bankruptcy case; community income on a separate return; self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government; or tips reported on Form 4137 or wages on Form 8919?

Model: The screen leaves out statutory employees and notaries public. The instructions say for statutory employees 'do not report this amount on Schedule SE (Form 1040), line 2', and for notaries 'Do not enter your net profit from line 31 on Schedule SE (Form 1040), line 2', yet se_line2 adds every Schedule C.

Ruling: model error; project retained. Statutory employee income and notary fees are refused on each Schedule C (sc.statutory), so every Schedule C that reaches this line is one whose net profit Schedule SE line 2 takes; the second's filter excludes nothing the tool admits. Railroad retirement compensation with a Schedule C is refused (person.se_rrta), so line 8a is the W-2 boxes 3 and 7 for every person who reaches it.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: It screens out SARSEPs ('don't use this worksheet for SARSEPs'), non-whole or over-25% rates (the Rate Table covers whole percentages 1–25), more than one plan or a qualified plan, elective deferrals, and Roth contributions. These are the cases where Steps 9–20 or another worksheet would apply.

### Step 1 — Net profit from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".

Model: This adds Schedule C results from all of the person's businesses. Pub 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan', and nothing in the program refuses or limits that case.

Ruling: defect, fixed (BUG-0078). Pub. 560 p. 7: 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan.' Owner ruling: a SEP or SIMPLE plan with more than one Schedule C is refused (person.plan_screened), so step 1, the profit of all the person's businesses, is the profit of the one business that has the plan for every return the tool completes. This review saw the rendering before that refusal.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MISMATCH**

Restated: Enter the amount from helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person".

Model: This uses Schedule SE line 13 computed from se_line2, which includes every Schedule C, even a statutory employee's or a notary's. The instructions say for statutory employees 'do not report this amount on Schedule SE (Form 1040), line 2'. Otherwise it matches 'Enter your deduction for self-employment tax from Schedule 1 (Form 1040), line 15' for this person.

Ruling: model error; project retained. Statutory employee income and notary fees are refused on each Schedule C (sc.statutory), so every Schedule C that reaches this line is one whose net profit Schedule SE line 2 takes; the second's filter excludes nothing the tool admits. Railroad retirement compensation with a Schedule C is refused (person.se_rrta), so line 8a is the W-2 boxes 3 and 7 for every person who reaches it.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: It follows 'Net earnings from self-employment. Subtract step 2 from step 1'. The zero floor only matters for losses, where no deduction results either way.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: It folds Step 4 in by computing rate ÷ (1 + rate) to 6 decimals, which reproduces the Rate Table (for example, 10 → 0.090909 and 25 → 0.200000). It then follows 'Multiply step 3 by step 4'.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: It follows 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: It follows 'Enter the smaller of step 5 or step 6'.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: It follows 'Contribution dollar limit ... $70,000'.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: It follows 'Otherwise, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'. This applies because the plan screen excludes elective deferrals and Roth contributions.

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "Line 11 covers 'social security or tier 1 railroad retirement (RRTA) tax'. RRTA amounts are reported in 'Form W-2, box 14', and the Form 8959 instructions name Form CT-2 employee representatives. Asking this question so the program can refuse the RRTA path is consistent with the text."
  - key: "employers"
    status: MATCH
    reason: "The text says 'had more than one employer for 2025' and 'Figure this amount separately for you and your spouse'. Counting each person's W-2s matches this if each employer issues one W-2. Two W-2s from the same employer would be counted as two employers."
  - key: "overcount"
    status: MATCH
    reason: "This counts the employers covered by 'if any one employer withheld more than $10,918.20'."
  - key: "over"
    status: MATCH
    reason: "It is true when at least one employer withheld more than $10,918.20, which is the condition that blocks claiming the excess on the return."
  - key: "wages"
    status: MATCH
    reason: "This sums each person's 'total wages' for the 'more than $176,100' test. The glossary ties w2.wages to boxes 3 and 7, which fits the social security wage base."
  - key: "withheld"
    status: MATCH
    reason: "Box 4 is 'Social security tax withheld', so the sum is the total withheld that is compared with $10,918.20. Tier 1 RRTA is refused separately."
  - key: "eligible"
    status: MATCH
    reason: "It follows 'had more than one employer for 2025 and total wages of more than $176,100'."
  - key: "excess"
    status: MATCH
    reason: "It follows 'credit ... for the amount withheld in excess of $10,918.20', with a floor of zero."
  - key: "zero"
    status: MATCH
    reason: "This is a zero constant used when the person is not eligible."
  - key: "credit"
    status: MATCH
    reason: "The credit is the excess when eligible and zero otherwise. The refusals cover 'if any one employer withheld more than $10,918.20 ... file a claim for refund using Form 843' and excess tier 2 RRTA tax ('use Form 843')."
  - key: "(screen) (person.se_screen)"
    status: MISMATCH
    reason: "The screen leaves out statutory employees and notaries public. The instructions say for statutory employees 'do not report this amount on Schedule SE (Form 1040), line 2', and for notaries 'Do not enter your net profit from line 31 on Schedule SE (Form 1040), line 2', yet se_line2 adds every Schedule C."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "It screens out SARSEPs ('don't use this worksheet for SARSEPs'), non-whole or over-25% rates (the Rate Table covers whole percentages 1–25), more than one plan or a qualified plan, elective deferrals, and Roth contributions. These are the cases where Steps 9–20 or another worksheet would apply."
  - key: "Step 1"
    status: MISMATCH
    reason: "This adds Schedule C results from all of the person's businesses. Pub 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan', and nothing in the program refuses or limits that case."
  - key: "Step 2"
    status: MISMATCH
    reason: "This uses Schedule SE line 13 computed from se_line2, which includes every Schedule C, even a statutory employee's or a notary's. The instructions say for statutory employees 'do not report this amount on Schedule SE (Form 1040), line 2'. Otherwise it matches 'Enter your deduction for self-employment tax from Schedule 1 (Form 1040), line 15' for this person."
  - key: "Step 3"
    status: MATCH
    reason: "It follows 'Net earnings from self-employment. Subtract step 2 from step 1'. The zero floor only matters for losses, where no deduction results either way."
  - key: "Step 5"
    status: MATCH
    reason: "It folds Step 4 in by computing rate ÷ (1 + rate) to 6 decimals, which reproduces the Rate Table (for example, 10 → 0.090909 and 25 → 0.200000). It then follows 'Multiply step 3 by step 4'."
  - key: "Step 6"
    status: MATCH
    reason: "It follows 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'."
  - key: "Step 7"
    status: MATCH
    reason: "It follows 'Enter the smaller of step 5 or step 6'."
  - key: "Step 8"
    status: MATCH
    reason: "It follows 'Contribution dollar limit ... $70,000'."
  - key: "Step 21"
    status: MATCH
    reason: "It follows 'Otherwise, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'. This applies because the plan screen excludes elective deferrals and Roth contributions."
```
```
