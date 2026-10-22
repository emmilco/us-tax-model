# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9f42344093842e96433faca6561c07b53ed333f2bf9b2ad4038f35fda49857e6 |
| subject sha256 | 5991a0cf87017b52b8669cb97cc68fe67abc025f0479465dafeb85c9c6d264e4 |
| lines judged | 23 |
| match / mismatch / unclear / missing | 22 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 41, 47, 93, 95, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 41, 93, 95, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 10, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 10, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i2441 | 2025 | 4, 5 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 4, 5 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: Schedule 3 line 11 covers 'social security or tier 1 railroad retirement (RRTA) tax' and says to use Form 843 for excess tier 2 RRTA tax. The W-2 instructions put RRTA compensation and taxes in box 14. This input sends the railroad case to the refusal on line credit, which names what is excluded.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Counts the person's Forms W-2 to test 'more than one employer for 2025'. The instructions say to 'Figure this amount separately for you and your spouse', and the count is per person.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: Counts W-2s on which one employer withheld more than $10,918.20. That is the case where the instructions say 'you can't claim the excess on your return.'

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: True when any single employer withheld more than $10,918.20. This triggers the Form 843 refusal on line credit, as the instructions describe.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: Totals the person's wages from all W-2s to test 'total wages of more than $176,100'.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Totals W-2 box 4 ('Social security tax withheld'). This is the amount compared with $10,918.20. Tier 1 RRTA tax is excluded by the rrta refusal.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: Matches the condition in the instructions: 'had more than one employer for 2025 and total wages of more than $176,100.'

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: The credit is 'the amount withheld in excess of $10,918.20'. The restatement subtracts $10,918.20 from total withholding, with a floor of zero.

### zero — No excess credit
Status: **MATCH**

Model: Zero is the credit when the eligibility condition is not met.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: Gives the excess when eligible and zero otherwise, figured per person. The refusals cover the RRTA/tier 2 case and the case where one employer overcollected, which goes to Form 843.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: Lists the Schedule SE situations the tool does not handle: church employee income, clergy and Forms 4361/4029, K-1 box 14 code A and other self-employment income, farm income and CRP, optional methods, chapter 11, community income, exempt income, and Forms 4137 and 8919. All of these come from the Schedule SE form and instructions, and the se_screened gate refuses them.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: Pub 560 says the worksheets 'apply only to self-employed individuals who have only one defined contribution plan' and 'don't use this worksheet for SARSEPs'. The rate table covers only whole-percentage rates up to 25%. Elective deferrals go through steps 9–20. The screen excludes each of these cases.

### Step 1 — Net profit from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".

Model: The restatement adds net profit from all of the person's Schedules C. Pub 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan,' and nothing in the screens excludes that case.

Ruling: refusal located elsewhere; project retained (BUG-0078, as the prior ruling). Pub. 560 p. 7, Earned income: "If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan." The owner's remedy for BUG-0078 refuses a SEP or SIMPLE plan with more than one Schedule C: person.plan_screened is true when person.plan_screen is answered yes or the person has a plan and person.sc_count is more than 1, and it refuses the plan contributions (person.sep_contrib and the SIMPLE inputs, 'a plan with more than one Schedule C', shown in the glossary). So for every return the tool completes the person has one Schedule C, and step 1, the profit of all the person's businesses, is the profit of the business that has the plan. No change.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Step 2 is 'your deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which is Schedule SE line 13. The restatement figures it from the person's own Schedule SE, using the Schedule C total on line 2 and box 3 plus box 7 wages on line 8a. The items the tool cannot handle are refused.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: The worksheet says 'Subtract step 2 from step 1'. The added zero floor only changes negative results, and a negative result would give no deduction anyway, so the outcome is the same.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: Multiplies step 3 by rate ÷ (1 + rate), rounded to 6 decimal places. This reproduces the Rate Table values, for example 10% → 0.090909 and 25% → 0.200000.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: The worksheet says 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'. The restatement multiplies $350,000 by the whole-percent plan rate.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: The worksheet says 'Enter the smaller of step 5 or step 6.'

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: The contribution dollar limit printed on the worksheet is $70,000.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: With no elective deferrals, the worksheet says to 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21.' Elective deferrals, Roth contributions and SARSEPs are excluded by plan_screen.

### (screen) (person.sav_trad) — Did you make contributions (other than rollover contributions) to a traditional IRA for 20
Status: **MATCH**

Model: Form 8880 line 1 includes traditional IRA contributions for 2025 and says 'Do not include rollover contributions.'

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: Form 8880 line 1 includes 'ABLE account contributions by the designated beneficiary for 2025'. Line 4 includes distributions from ABLE accounts 'received after 2022 and before the due date (including extensions) of your 2025 tax return.'

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: The W-2 instructions give a 2025 limit of $23,500 for elective deferrals and designated Roth contributions. Form 8880 line 4 instructions treat 'Distributions of excess contributions or deferrals' specially, so asking about excess deferrals is consistent with the text.

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "Schedule 3 line 11 covers 'social security or tier 1 railroad retirement (RRTA) tax' and says to use Form 843 for excess tier 2 RRTA tax. The W-2 instructions put RRTA compensation and taxes in box 14. This input sends the railroad case to the refusal on line credit, which names what is excluded."
  - key: "employers"
    status: MATCH
    reason: "Counts the person's Forms W-2 to test 'more than one employer for 2025'. The instructions say to 'Figure this amount separately for you and your spouse', and the count is per person."
  - key: "overcount"
    status: MATCH
    reason: "Counts W-2s on which one employer withheld more than $10,918.20. That is the case where the instructions say 'you can't claim the excess on your return.'"
  - key: "over"
    status: MATCH
    reason: "True when any single employer withheld more than $10,918.20. This triggers the Form 843 refusal on line credit, as the instructions describe."
  - key: "wages"
    status: MATCH
    reason: "Totals the person's wages from all W-2s to test 'total wages of more than $176,100'."
  - key: "withheld"
    status: MATCH
    reason: "Totals W-2 box 4 ('Social security tax withheld'). This is the amount compared with $10,918.20. Tier 1 RRTA tax is excluded by the rrta refusal."
  - key: "eligible"
    status: MATCH
    reason: "Matches the condition in the instructions: 'had more than one employer for 2025 and total wages of more than $176,100.'"
  - key: "excess"
    status: MATCH
    reason: "The credit is 'the amount withheld in excess of $10,918.20'. The restatement subtracts $10,918.20 from total withholding, with a floor of zero."
  - key: "zero"
    status: MATCH
    reason: "Zero is the credit when the eligibility condition is not met."
  - key: "credit"
    status: MATCH
    reason: "Gives the excess when eligible and zero otherwise, figured per person. The refusals cover the RRTA/tier 2 case and the case where one employer overcollected, which goes to Form 843."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "Lists the Schedule SE situations the tool does not handle: church employee income, clergy and Forms 4361/4029, K-1 box 14 code A and other self-employment income, farm income and CRP, optional methods, chapter 11, community income, exempt income, and Forms 4137 and 8919. All of these come from the Schedule SE form and instructions, and the se_screened gate refuses them."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "Pub 560 says the worksheets 'apply only to self-employed individuals who have only one defined contribution plan' and 'don't use this worksheet for SARSEPs'. The rate table covers only whole-percentage rates up to 25%. Elective deferrals go through steps 9–20. The screen excludes each of these cases."
  - key: "Step 1"
    status: MISMATCH
    reason: "The restatement adds net profit from all of the person's Schedules C. Pub 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan,' and nothing in the screens excludes that case."
  - key: "Step 2"
    status: MATCH
    reason: "Step 2 is 'your deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which is Schedule SE line 13. The restatement figures it from the person's own Schedule SE, using the Schedule C total on line 2 and box 3 plus box 7 wages on line 8a. The items the tool cannot handle are refused."
  - key: "Step 3"
    status: MATCH
    reason: "The worksheet says 'Subtract step 2 from step 1'. The added zero floor only changes negative results, and a negative result would give no deduction anyway, so the outcome is the same."
  - key: "Step 5"
    status: MATCH
    reason: "Multiplies step 3 by rate ÷ (1 + rate), rounded to 6 decimal places. This reproduces the Rate Table values, for example 10% → 0.090909 and 25% → 0.200000."
  - key: "Step 6"
    status: MATCH
    reason: "The worksheet says 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'. The restatement multiplies $350,000 by the whole-percent plan rate."
  - key: "Step 7"
    status: MATCH
    reason: "The worksheet says 'Enter the smaller of step 5 or step 6.'"
  - key: "Step 8"
    status: MATCH
    reason: "The contribution dollar limit printed on the worksheet is $70,000."
  - key: "Step 21"
    status: MATCH
    reason: "With no elective deferrals, the worksheet says to 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21.' Elective deferrals, Roth contributions and SARSEPs are excluded by plan_screen."
  - key: "(screen) (person.sav_trad)"
    status: MATCH
    reason: "Form 8880 line 1 includes traditional IRA contributions for 2025 and says 'Do not include rollover contributions.'"
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "Form 8880 line 1 includes 'ABLE account contributions by the designated beneficiary for 2025'. Line 4 includes distributions from ABLE accounts 'received after 2022 and before the due date (including extensions) of your 2025 tax return.'"
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "The W-2 instructions give a 2025 limit of $23,500 for elective deferrals and designated Roth contributions. Form 8880 line 4 instructions treat 'Distributions of excess contributions or deferrals' specially, so asking about excess deferrals is consistent with the text."
```
```
