# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 77e3df642b0b7aea3c41d4754954b616f89d9f74212f3be821aedced128908dc |
| subject sha256 | f589cc0a4b9dd952ace13caac5deda87537bfebd80a05493a2ce2f5f0b334fcb |
| lines judged | 23 |
| match / mismatch / unclear / missing | 21 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 31, 32, 40, 41, 44, 45, 47, 66, 93, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 31, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
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
| p590a | 2025 | 6, 15, 30, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 15, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| i8606 | 2025 | 2, 5, 9 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 2, 5, 9 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: The W-2/W-3 instructions say railroad employers report RRTA compensation and Tier 1/Tier 2 tax in W-2 box 14, and the Form 8959 instructions cover employee representatives filing Form CT-2. The question captures both cases.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Schedule 3 line 11 applies if you 'had more than one employer for 2025'. Counting the person's W-2 entries is a reasonable proxy, and the count is kept per person as the text requires ('Figure this amount separately for you and your spouse').

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts W-2s whose withholding exceeds $10,918.20, which tests the IRS condition 'if any one employer withheld more than $10,918.20'.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: This is true when any employer over-withheld, which is the condition that bars claiming the excess on the return.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: The IRS test is 'total wages of more than $176,100'. Summing W-2 boxes 3 and 7 gives social security wages and tips, the amounts measured against the $176,100 wage base.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Summing W-2 box 4 gives the social security tax withheld that the excess is figured from. RRTA tier 1 tax is excluded by the rrta refusal.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This restates the IRS condition: 'more than one employer for 2025 and total wages of more than $176,100'.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: The IRS allows 'a credit on this line for the amount withheld in excess of $10,918.20'. Subtracting with a floor of zero matches.

### zero — No excess credit
Status: **MATCH**

Model: This supplies the zero credit used when the filer is not eligible.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The line equals the excess when eligible and zero otherwise, figured per person. The refusals correctly cover the RRTA/Tier 2 case ('use Form 843') and the single-employer over-withholding case ('The employer should adjust the tax... file a claim for refund using Form 843').

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MISMATCH**

Restated: Input — Does any of these apply to this person: church employee income (wages from a church that elected exemption from social security and Medicare taxes); being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029; net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee); farm income (Schedule F) or Conservation Reserve Program payments; electing an optional method (Schedule SE Part II); a chapter 11 bankruptcy case; community income on a separate return; self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government; or tips reported on Form 4137 or wages on Form 8919?

Model: The screen omits statutory employees and notaries public. Yet Schedule C line 31 flows to Schedule SE line 2 here, and the Schedule C instructions say 'Statutory employees... do not report this amount on Schedule SE (Form 1040), line 2' and 'Notary public. Do not enter your net profit from line 31 on Schedule SE (Form 1040), line 2'.

Ruling: refusal located elsewhere; restatement accepted (as the prior rulings). Statutory employee income and notary fees are refused on each Schedule C (sc.statutory, 'income you received as a statutory employee ... or fees you received as a notary public'; i1040sc, line 31, 'Statutory employees' and 'Notary public'), so every Schedule C whose net profit reaches Schedule SE line 2 is one the instructions send there.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: The screen excludes the cases Pub. 560 chapter 5 says the worksheet does not cover: SARSEPs, more than one plan, rates that are not whole percentages or exceed 25% (the rate table only runs to 25), elective deferrals, and SIMPLE plans with higher limits. Within those exclusions the SEP worksheet applies.

### Step 1 — Net profit from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".

Model: This line sums Schedule C results across all of the person's businesses. Pub. 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan', and no screen excludes that case.

Ruling: refusal located elsewhere; project retained (BUG-0078, as the prior rulings). Pub. 560 p. 7, Earned income, 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan': a SEP or SIMPLE plan with more than one Schedule C is refused (person.plan_screen), so the sum over businesses reaches this line only for a person with one business.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Pub. 560 Step 2 is 'your deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which for one person is Schedule SE line 13. That line is computed with line 8a set to W-2 boxes 3 and 7, and the zeroed lines are covered by the screens.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: Step 3 is 'Subtract step 2 from step 1'. The zero floor cannot change the maximum deduction, because Steps 5, 7 and 21 would otherwise go negative.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: The reduced rate is the plan rate divided by (plan rate + 1), which reproduces the Rate Table (for example 10% gives 0.090909). Multiplying by Step 3 matches 'Multiply step 3 by step 4'.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: This restates 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: This restates 'Enter the smaller of step 5 or step 6'.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: This restates the 'Contribution dollar limit... $70,000'.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: With elective deferrals excluded by the screen, the worksheet says to 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'.

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: Form 8880 line 1 includes 'ABLE account contributions by the designated beneficiary for 2025', and line 4 counts distributions 'received after 2022 and before the due date of your 2025 return (including extensions)' from ABLE accounts.

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: The W-2/W-3 instructions give 'the 2025 limit for elective deferrals and designated Roth contributions is $23,500', reported in box 12, with catch-up contributions reported separately. The question tests for excess deferrals on that basis.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or is an earlier exce
Status: **MATCH**

Model: Pub. 590-A defines an excess contribution as more than the smaller of '$7,000 ($8,000 if you are age 50 or older)' or taxable compensation, subject to tax if not withdrawn 'by the date your return for the year is due (including extensions)'. Recharacterization is also discussed, so the screen matches the text.

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The W-2/W-3 instructions say railroad employers report RRTA compensation and Tier 1/Tier 2 tax in W-2 box 14, and the Form 8959 instructions cover employee representatives filing Form CT-2. The question captures both cases."
  - key: "employers"
    status: MATCH
    reason: "Schedule 3 line 11 applies if you 'had more than one employer for 2025'. Counting the person's W-2 entries is a reasonable proxy, and the count is kept per person as the text requires ('Figure this amount separately for you and your spouse')."
  - key: "overcount"
    status: MATCH
    reason: "This counts W-2s whose withholding exceeds $10,918.20, which tests the IRS condition 'if any one employer withheld more than $10,918.20'."
  - key: "over"
    status: MATCH
    reason: "This is true when any employer over-withheld, which is the condition that bars claiming the excess on the return."
  - key: "wages"
    status: MATCH
    reason: "The IRS test is 'total wages of more than $176,100'. Summing W-2 boxes 3 and 7 gives social security wages and tips, the amounts measured against the $176,100 wage base."
  - key: "withheld"
    status: MATCH
    reason: "Summing W-2 box 4 gives the social security tax withheld that the excess is figured from. RRTA tier 1 tax is excluded by the rrta refusal."
  - key: "eligible"
    status: MATCH
    reason: "This restates the IRS condition: 'more than one employer for 2025 and total wages of more than $176,100'."
  - key: "excess"
    status: MATCH
    reason: "The IRS allows 'a credit on this line for the amount withheld in excess of $10,918.20'. Subtracting with a floor of zero matches."
  - key: "zero"
    status: MATCH
    reason: "This supplies the zero credit used when the filer is not eligible."
  - key: "credit"
    status: MATCH
    reason: "The line equals the excess when eligible and zero otherwise, figured per person. The refusals correctly cover the RRTA/Tier 2 case ('use Form 843') and the single-employer over-withholding case ('The employer should adjust the tax... file a claim for refund using Form 843')."
  - key: "(screen) (person.se_screen)"
    status: MISMATCH
    reason: "The screen omits statutory employees and notaries public. Yet Schedule C line 31 flows to Schedule SE line 2 here, and the Schedule C instructions say 'Statutory employees... do not report this amount on Schedule SE (Form 1040), line 2' and 'Notary public. Do not enter your net profit from line 31 on Schedule SE (Form 1040), line 2'."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "The screen excludes the cases Pub. 560 chapter 5 says the worksheet does not cover: SARSEPs, more than one plan, rates that are not whole percentages or exceed 25% (the rate table only runs to 25), elective deferrals, and SIMPLE plans with higher limits. Within those exclusions the SEP worksheet applies."
  - key: "Step 1"
    status: MISMATCH
    reason: "This line sums Schedule C results across all of the person's businesses. Pub. 560 says 'If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan', and no screen excludes that case."
  - key: "Step 2"
    status: MATCH
    reason: "Pub. 560 Step 2 is 'your deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which for one person is Schedule SE line 13. That line is computed with line 8a set to W-2 boxes 3 and 7, and the zeroed lines are covered by the screens."
  - key: "Step 3"
    status: MATCH
    reason: "Step 3 is 'Subtract step 2 from step 1'. The zero floor cannot change the maximum deduction, because Steps 5, 7 and 21 would otherwise go negative."
  - key: "Step 5"
    status: MATCH
    reason: "The reduced rate is the plan rate divided by (plan rate + 1), which reproduces the Rate Table (for example 10% gives 0.090909). Multiplying by Step 3 matches 'Multiply step 3 by step 4'."
  - key: "Step 6"
    status: MATCH
    reason: "This restates 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'."
  - key: "Step 7"
    status: MATCH
    reason: "This restates 'Enter the smaller of step 5 or step 6'."
  - key: "Step 8"
    status: MATCH
    reason: "This restates the 'Contribution dollar limit... $70,000'."
  - key: "Step 21"
    status: MATCH
    reason: "With elective deferrals excluded by the screen, the worksheet says to 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'."
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "Form 8880 line 1 includes 'ABLE account contributions by the designated beneficiary for 2025', and line 4 counts distributions 'received after 2022 and before the due date of your 2025 return (including extensions)' from ABLE accounts."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "The W-2/W-3 instructions give 'the 2025 limit for elective deferrals and designated Roth contributions is $23,500', reported in box 12, with catch-up contributions reported separately. The question tests for excess deferrals on that basis."
  - key: "(screen) (person.ira_excess)"
    status: MATCH
    reason: "Pub. 590-A defines an excess contribution as more than the smaller of '$7,000 ($8,000 if you are age 50 or older)' or taxable compensation, subject to tax if not withdrawn 'by the date your return for the year is due (including extensions)'. Recharacterization is also discussed, so the screen matches the text."
```
```
