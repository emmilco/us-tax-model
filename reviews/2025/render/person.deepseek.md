# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 48ef7562afe5cce34480e39076280e93b02e5651a4f33e8bf16ae6921b59d121 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 42cc96c706aa33a05c311726a91f1fe8c95fa33bb3cb78c6857d12212f265c89 |
| lines judged | 23 |
| match / mismatch / unclear / missing | 20 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 31, 32, 40, 41, 44, 45, 47, 66, 93, 94, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 31, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
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
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: IRS line 11 and Form 8959 recognize RRTA compensation and tax from W-2 box 14 and Form CT-2; the program uses this only as a gate and refuses the RRTA path.

### employers — Total w2.one for this person
Status: **MATCH**

Model: IRS line 11 requires more than one employer; the program counts one per confirmed W-2 employer entry.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: IRS line 11 says if any one employer withheld more than $10,918.20 the excess cannot be claimed on the return; the program counts those employers.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: The IRS one-employer overwithholding bar applies if any employer withheld more than $10,918.20, which is what an overcount greater than zero means.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: For the excess Social Security credit, the relevant wages are social security wages and tips (W-2 boxes 3 and 7), which w2.wages adds.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: IRS line 11 compares social security tax withheld; W-2 box 4 is the social security tax withheld amount.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: IRS line 11 requires more than one employer and total wages of more than $176,100; the restatement uses those two conditions.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: IRS line 11 allows a credit for the amount withheld in excess of $10,918.20, with zero if there is no excess.

### zero — No excess credit
Status: **MATCH**

Model: The IRS line uses zero when no excess credit is allowable; entering $0 matches that result.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: Within the Social Security-only path, the credit is the excess over $10,918.20 when eligible; the refusals mirror IRS line 11 for an employer overwithholding and for the RRTA path.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: The listed items match the Schedule SE matters outside a Schedule C-only computation, including church income, clergy, farm, partnership and other self-employment income, optional methods, bankruptcy, community income, exempt income, and Forms 4137 and 8919.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: The listed SEP and SIMPLE complications match Pub. 560 limits and exclusions such as SARSEPs, non-whole or over-25% SEP rates, higher SIMPLE limits, multiple plans, other elective deferrals, Roth SEP/SIMPLE contributions, and excess contributions.

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: Within the supported Schedule C-only cases, Pub. 560 Step 1 starts from Schedule C line 31 net profit or loss; the refusal excludes Schedule F, K-1 and other self-employment income.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Pub. 560 Step 2 uses the Schedule 1 line 15 deduction for self-employment tax, which is Schedule SE line 13.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MISMATCH**

Restated: Subtract line Step 2 from line Step 1. If zero or less, enter -0-.

Model: Pub. 560 Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; it does not provide the added 'If zero or less, enter -0-' floor.

Ruling: finding; the project's line, not its English, departs from the page. p560 p. 39, Deduction Worksheet for Self-Employed: "Step 3 Net earnings from self-employment. Subtract step 2 from step 1" (no floor; the page prints no "-0-" instruction for Steps 3 to 21). person.sep_s3 is NonNegDollars by subtract_floor0, and the English states that faithfully ("If zero or less, enter -0-"), so the model read the English correctly. On a reachable return the printed step differs: a SEP participant (person.plan sep, contribution $0) whose Schedule C shows a $5,000 loss has Step 1 -$5,000.00 and Step 2 $0.00; the page's arithmetic gives Step 3 -$5,000.00 (and negative Steps 5, 7 and 21), the project prints $0.00 (constructed, not executed). No Form 1040 amount changes: any contribution above zero is refused at person.sep_excess on both readings, and a zero contribution deducts zero. The floor is a reasonable reading (a maximum deductible contribution below zero has no meaning), but it is an unprinted rule with no ambiguity-register entry, as amb.2025.sa_medical_negative_agi records for the like case on Schedule A. Severity: low (printed worksheet steps only). Proposed: record the reading in ambiguities/2025.yaml and cite it on person.sep_s3; see .transcription/proposed/round4/person.findings.md.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: Pub. 560 Step 5 multiplies step 3 by the self-employed rate from the Rate Worksheet, which is plan rate divided by plan rate plus 1; the rounding and cap do not change supported whole-percent rates.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: Pub. 560 Step 6 multiplies $350,000 by the plan contribution rate, not the reduced rate; the restatement converts the whole-percent rate to that decimal.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: Pub. 560 Step 7 is the smaller of step 5 or step 6.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: Pub. 560 Step 8 shows the $70,000 contribution dollar limit.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: Pub. 560 Step 8 instructions say that if there are no elective deferrals, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21; the program supports that no-deferral path.

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MISMATCH**

Restated: Input — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?

Model: IRS Form 8880 line 4 includes only 'Certain distributions received after 2022 and before the due date' rather than any ABLE distribution; the restatement also combines that with the separate line 1 ABLE contribution question.

Ruling: scope; f8880 p. 2, Line 4: "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions) from any of the following types of plans. • Traditional or Roth IRAs, or ABLE accounts." followed by "Don't include any of the following" (rollovers and other excluded distributions); Who Can Take This Credit, "(e) contributions, as a designated beneficiary of an ABLE account, to the ABLE account". The English says what the project asks: one screen that refuses the credit for ABLE contributions and for any ABLE distribution in the line 4 period (person.sav_able refuses person.sav_line1 and the line 4 distributions). The model is right that line 4 counts only some ABLE distributions; the screen is wider, so a return with only an excluded ABLE distribution is refused rather than figured. A broader refusal never misfigures a credit; refusal scope, not a misstatement.

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: The W-2 instructions state the 2025 elective deferral and designated Roth contribution limit is $23,500, and catch-up contributions are separately recognized; the screen asks whether total deferrals exceed the applicable limit.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or is an earlier exce
Status: **MISMATCH**

Restated: Input — Does any of these apply to you: your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return; you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse); or an excess contribution from an earlier year is still in your traditional or Roth IRA?

Model: Pub. 590-A defines an excess contribution by the $7,000/$8,000 or compensation limits and by failure to withdraw it; it does not make recharacterizing a 2025 contribution an excess contribution by itself.

Ruling: model error; project retained. The model reads the screen as a definition of an excess contribution. The English lists three separate cases joined by "; ... ; or": contributions above the limit "and the excess was not withdrawn with its earnings by the due date of your return" (p590a p. 35, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of" the limit or compensation), "you recharacterized a 2025 contribution", and an earlier excess still in the IRA. It does not say a recharacterization is an excess contribution; it screens recharacterized contributions as their own case, as amb.2025.savers_traditional records ("Excess or recharacterized contributions, traditional or Roth, are refused by one screen per person (person.ira_excess)").

## Raw response

```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "IRS line 11 and Form 8959 recognize RRTA compensation and tax from W-2 box 14 and Form CT-2; the program uses this only as a gate and refuses the RRTA path."
  - key: "employers"
    status: MATCH
    reason: "IRS line 11 requires more than one employer; the program counts one per confirmed W-2 employer entry."
  - key: "overcount"
    status: MATCH
    reason: "IRS line 11 says if any one employer withheld more than $10,918.20 the excess cannot be claimed on the return; the program counts those employers."
  - key: "over"
    status: MATCH
    reason: "The IRS one-employer overwithholding bar applies if any employer withheld more than $10,918.20, which is what an overcount greater than zero means."
  - key: "wages"
    status: MATCH
    reason: "For the excess Social Security credit, the relevant wages are social security wages and tips (W-2 boxes 3 and 7), which w2.wages adds."
  - key: "withheld"
    status: MATCH
    reason: "IRS line 11 compares social security tax withheld; W-2 box 4 is the social security tax withheld amount."
  - key: "eligible"
    status: MATCH
    reason: "IRS line 11 requires more than one employer and total wages of more than $176,100; the restatement uses those two conditions."
  - key: "excess"
    status: MATCH
    reason: "IRS line 11 allows a credit for the amount withheld in excess of $10,918.20, with zero if there is no excess."
  - key: "zero"
    status: MATCH
    reason: "The IRS line uses zero when no excess credit is allowable; entering $0 matches that result."
  - key: "credit"
    status: MATCH
    reason: "Within the Social Security-only path, the credit is the excess over $10,918.20 when eligible; the refusals mirror IRS line 11 for an employer overwithholding and for the RRTA path."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "The listed items match the Schedule SE matters outside a Schedule C-only computation, including church income, clergy, farm, partnership and other self-employment income, optional methods, bankruptcy, community income, exempt income, and Forms 4137 and 8919."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "The listed SEP and SIMPLE complications match Pub. 560 limits and exclusions such as SARSEPs, non-whole or over-25% SEP rates, higher SIMPLE limits, multiple plans, other elective deferrals, Roth SEP/SIMPLE contributions, and excess contributions."
  - key: "Step 1"
    status: MATCH
    reason: "Within the supported Schedule C-only cases, Pub. 560 Step 1 starts from Schedule C line 31 net profit or loss; the refusal excludes Schedule F, K-1 and other self-employment income."
  - key: "Step 2"
    status: MATCH
    reason: "Pub. 560 Step 2 uses the Schedule 1 line 15 deduction for self-employment tax, which is Schedule SE line 13."
  - key: "Step 3"
    status: MISMATCH
    reason: "Pub. 560 Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; it does not provide the added 'If zero or less, enter -0-' floor."
  - key: "Step 5"
    status: MATCH
    reason: "Pub. 560 Step 5 multiplies step 3 by the self-employed rate from the Rate Worksheet, which is plan rate divided by plan rate plus 1; the rounding and cap do not change supported whole-percent rates."
  - key: "Step 6"
    status: MATCH
    reason: "Pub. 560 Step 6 multiplies $350,000 by the plan contribution rate, not the reduced rate; the restatement converts the whole-percent rate to that decimal."
  - key: "Step 7"
    status: MATCH
    reason: "Pub. 560 Step 7 is the smaller of step 5 or step 6."
  - key: "Step 8"
    status: MATCH
    reason: "Pub. 560 Step 8 shows the $70,000 contribution dollar limit."
  - key: "Step 21"
    status: MATCH
    reason: "Pub. 560 Step 8 instructions say that if there are no elective deferrals, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21; the program supports that no-deferral path."
  - key: "(screen) (person.sav_able)"
    status: MISMATCH
    reason: "IRS Form 8880 line 4 includes only 'Certain distributions received after 2022 and before the due date' rather than any ABLE distribution; the restatement also combines that with the separate line 1 ABLE contribution question."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "The W-2 instructions state the 2025 elective deferral and designated Roth contribution limit is $23,500, and catch-up contributions are separately recognized; the screen asks whether total deferrals exceed the applicable limit."
  - key: "(screen) (person.ira_excess)"
    status: MISMATCH
    reason: "Pub. 590-A defines an excess contribution by the $7,000/$8,000 or compensation limits and by failure to withdraw it; it does not make recharacterizing a 2025 contribution an excess contribution by itself."
```
