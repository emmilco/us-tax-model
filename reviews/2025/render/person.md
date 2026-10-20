# Render comparison — person

The rendered English of every printed line of `Excess Social Security credit — separately per person` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e4a38ac328e1809c657e8c8c6b456bb13325376ff1357664adde7a17a209c9ae |
| lines judged | 20 |
| match / mismatch / unclear / missing | 18 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 41, 47, 93, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 41, 93, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| p560 | For use in preparing 2025 returns | 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: Line 11 covers "social security or tier 1 railroad retirement (RRTA) tax", and the program refuses the RRTA path instead of computing it. This input correctly identifies RRTA compensation (W-2 box 14, Form CT-2) to trigger that refusal, and the refusal notes that tier 2 goes on Form 843.

### employers — Total w2.one for this person
Status: **MISMATCH**

Restated: Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS condition is "had more than one employer for 2025", but the restatement counts confirmed W-2 entries. One employer can issue several Forms W-2, which would wrongly count as more than one employer.

Ruling: representation; project retained. The W-2 collection is keyed by employer, and repeated forms from one employer are consolidated into one entry ("Keyed by employer within person; consolidate repeated forms for the same employer explicitly", forms/2025/w2.yaml collection note), so the count of entries is the count of employers that "had more than one employer for 2025" (i1040gi p. 117) asks for. No change to the data.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts entries where the employer withheld more than $10,918.20, which implements "if any one employer withheld more than $10,918.20".

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: True when at least one employer over-withheld, which is the IRS condition under which "you can't claim the excess on your return".

### wages — Total w2.wages for this person
Status: **MATCH**

Model: This sums this person's W-2 wages, matching "total wages" figured "separately for you and your spouse".

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: W-2 box 4 is social security tax withheld, so the sum is the per-person total withheld to compare with $10,918.20. Tier 1 RRTA is excluded by the rrta refusal.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This restates "had more than one employer for 2025 and total wages of more than $176,100" (subject to the employer-count issue noted on line employers).

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This computes "the amount withheld in excess of $10,918.20", floored at zero.

### zero — No excess credit
Status: **MATCH**

Model: This is the constant $0 used when the person is not eligible.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: Gives the excess when eligible and zero otherwise, figured per person. The refusals correctly exclude RRTA and the case where an employer over-withheld (adjust with the employer or file Form 843).

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: This input screens for Schedule SE situations the SE instructions handle specially (church employee income, clergy and Forms 4361/4029, partnership income, farm and CRP income, optional methods, chapter 11, community income, exempt income, Forms 4137/8919). Its gate drives a refusal naming them.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: This input screens out cases Pub. 560 chapter 5 doesn't cover by the simple path: "don't use this worksheet for SARSEPs", only one defined contribution plan, rates that are not whole percentages (rate table), and elective deferrals or Roth amounts (steps 9–20).

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: Step 1 says "Enter your net profit from Schedule C (Form 1040), line 31". Schedule F and K-1 amounts are excluded through the SE screen.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MISMATCH**

Restated: Enter the amount from helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person".

Model: The Schedule SE that feeds this line takes line 2 from all of the person's Schedule C results with no exclusion. The SE instructions say "If you were a statutory employee, don't include the net profit or (loss) from Schedule C, line 31, on Schedule SE, line 2", and notary profit is likewise excluded. Neither case is screened or refused.

Ruling: refusal located elsewhere; restatement accepted. Statutory employee income and notary fees are refused on each Schedule C (the sc screens: 'statutory employee (box 13 of Form W-2 was checked), or fees you received as a notary public'; i1040sse p. 4), so every Schedule C result that reaches Schedule SE line 2 belongs there; church employee income and the other exclusions are refused through person.se_screen.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: This restates "Subtract step 2 from step 1".

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: Rate / (1 + rate) rounded to 6 decimals reproduces the Rate Table (e.g., 10% → 0.090909) and the Rate Worksheet ("line 1 ÷ line 2"). The result is then multiplied by step 3, as in "Multiply step 3 by step 4".

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: This restates "Multiply $350,000 by your plan contribution rate (not the reduced rate)".

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: This restates "Enter the smaller of step 5 or step 6".

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: This restates "Contribution dollar limit . . . $70,000".

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: With no elective deferrals (screened out), the worksheet says "skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21".

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "Line 11 covers \"social security or tier 1 railroad retirement (RRTA) tax\", and the program refuses the RRTA path instead of computing it. This input correctly identifies RRTA compensation (W-2 box 14, Form CT-2) to trigger that refusal, and the refusal notes that tier 2 goes on Form 843."
  - key: "employers"
    status: MISMATCH
    reason: "The IRS condition is \"had more than one employer for 2025\", but the restatement counts confirmed W-2 entries. One employer can issue several Forms W-2, which would wrongly count as more than one employer."
  - key: "overcount"
    status: MATCH
    reason: "This counts entries where the employer withheld more than $10,918.20, which implements \"if any one employer withheld more than $10,918.20\"."
  - key: "over"
    status: MATCH
    reason: "True when at least one employer over-withheld, which is the IRS condition under which \"you can't claim the excess on your return\"."
  - key: "wages"
    status: MATCH
    reason: "This sums this person's W-2 wages, matching \"total wages\" figured \"separately for you and your spouse\"."
  - key: "withheld"
    status: MATCH
    reason: "W-2 box 4 is social security tax withheld, so the sum is the per-person total withheld to compare with $10,918.20. Tier 1 RRTA is excluded by the rrta refusal."
  - key: "eligible"
    status: MATCH
    reason: "This restates \"had more than one employer for 2025 and total wages of more than $176,100\" (subject to the employer-count issue noted on line employers)."
  - key: "excess"
    status: MATCH
    reason: "This computes \"the amount withheld in excess of $10,918.20\", floored at zero."
  - key: "zero"
    status: MATCH
    reason: "This is the constant $0 used when the person is not eligible."
  - key: "credit"
    status: MATCH
    reason: "Gives the excess when eligible and zero otherwise, figured per person. The refusals correctly exclude RRTA and the case where an employer over-withheld (adjust with the employer or file Form 843)."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "This input screens for Schedule SE situations the SE instructions handle specially (church employee income, clergy and Forms 4361/4029, partnership income, farm and CRP income, optional methods, chapter 11, community income, exempt income, Forms 4137/8919). Its gate drives a refusal naming them."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "This input screens out cases Pub. 560 chapter 5 doesn't cover by the simple path: \"don't use this worksheet for SARSEPs\", only one defined contribution plan, rates that are not whole percentages (rate table), and elective deferrals or Roth amounts (steps 9–20)."
  - key: "Step 1"
    status: MATCH
    reason: "Step 1 says \"Enter your net profit from Schedule C (Form 1040), line 31\". Schedule F and K-1 amounts are excluded through the SE screen."
  - key: "Step 2"
    status: MISMATCH
    reason: "The Schedule SE that feeds this line takes line 2 from all of the person's Schedule C results with no exclusion. The SE instructions say \"If you were a statutory employee, don't include the net profit or (loss) from Schedule C, line 31, on Schedule SE, line 2\", and notary profit is likewise excluded. Neither case is screened or refused."
  - key: "Step 3"
    status: MATCH
    reason: "This restates \"Subtract step 2 from step 1\"."
  - key: "Step 5"
    status: MATCH
    reason: "Rate / (1 + rate) rounded to 6 decimals reproduces the Rate Table (e.g., 10% → 0.090909) and the Rate Worksheet (\"line 1 ÷ line 2\"). The result is then multiplied by step 3, as in \"Multiply step 3 by step 4\"."
  - key: "Step 6"
    status: MATCH
    reason: "This restates \"Multiply $350,000 by your plan contribution rate (not the reduced rate)\"."
  - key: "Step 7"
    status: MATCH
    reason: "This restates \"Enter the smaller of step 5 or step 6\"."
  - key: "Step 8"
    status: MATCH
    reason: "This restates \"Contribution dollar limit . . . $70,000\"."
  - key: "Step 21"
    status: MATCH
    reason: "With no elective deferrals (screened out), the worksheet says \"skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21\"."
```
```
