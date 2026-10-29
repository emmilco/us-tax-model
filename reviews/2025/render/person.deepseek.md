# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4e7fb03a9d422496e64b86663fe1c6b20f1057773864aab15d5265e76f14f3bf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 7c169d40fdc7d4fbbb259b663a974cf8e3a39cf3ab9549cab6d5275e4f4b47f0 |
| lines judged | 32 |
| match / mismatch / unclear / missing | 31 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 40, 41, 44, 45, 47, 66, 93, 94, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 26, 27, 28, 30, 31, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i2441 | 2025 | 4, 5 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 4, 5 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p590a | 2025 | 6, 15, 30, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 15, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| i8606 | 2025 | 2, 5, 9 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 2, 5, 9 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |
| i8863 | 2025 | 1, 2, 3, 4, 7, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 7, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| i5329 | 2025 | 1, 3, 5, 8 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5, 8 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| p590b | 2025 | 27, 28 | cited pages | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 27, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f5329 | 2025 | 1, 2, 3 | whole document | 53ac10ecce39dbd1cc0a3b88c04e351c2a61f3ad35d145d5d847f30f47a1b945 | - | c65e0cd9d9ad8e8a04899ec87a11393ad5a3e281543eb6720b72357811f8f51d |
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

Model: Input tracks RRTA compensation in W-2 box 14 and employee-representative Form CT-2, matching the RRTA references in the IRS text.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Counts employer/W-2 entries; the excess social security rule requires more than one employer.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: Counts employers whose W-2 box 4 exceeds $10,918.20, matching the IRS rule for any one employer over the limit.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: True exactly when an employer withheld more than the per-employer limit, matching the bar on claiming the excess.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: Sums W-2 boxes 3 and 7, the social security wages and tips tested against the $176,100 base.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Sums W-2 box 4 social security tax withheld, the amount used for the excess social security credit.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: Requires more than one employer and total social security wages over $176,100, as the IRS line states.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: Subtracts the $10,918.20 maximum from total withheld and enters zero if not positive.

### zero — No excess credit
Status: **MATCH**

Model: Zero is the correct fallback when the excess social security credit conditions are not met.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: Uses excess only when eligible, otherwise zero; the refusals correctly carve out RRTA and single-employer overwithholding.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: The screen lists the Schedule SE items excluded by the simple Schedule C-only computation.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: The screen lists SEP/SIMPLE/qualified-plan and excess-contribution situations outside the one-plan worksheet.

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: Within supported Schedule C-only cases, the IRS Step 1 amount is the Schedule C net profit or loss; non-Schedule C SE items are refused.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Schedule SE line 13 is the deduction for one-half of self-employment tax also entered on Schedule 1 line 15.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MISMATCH**

Restated: Subtract line Step 2 from line Step 1. If zero or less, enter -0-.

Model: IRS Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; it does not provide a zero-or-less floor.

Ruling: ambiguity; amb.2025.sep_loss_floor (BUG-0181, the disposition of the round-4 finding BUG-0180). p560 p. 39, Deduction Worksheet for Self-Employed: "Step 3 Net earnings from self-employment. Subtract step 2 from step 1" prints no floor. The model read the page and the English correctly: person.sep_s3 floors Step 3 at zero and the English says so ("If zero or less, enter -0-"). The register records both readings and chooses the floor ("A maximum deductible contribution below zero has no meaning"; where both readings complete the return no Form 1040 or Schedule 1 amount differs, only the printed worksheet steps), naming person.sep_s3 in its chosen reading; the line itself still carries no ambiguity field pointing back to the entry (a traceability gap only, noted in round 1). Unchanged since round 1; the Stage 21 reply repeats the same reading, person.sep_s3 is unchanged in the Stage 21 subject and still carries no ambiguity field; project stands.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: Matches Rate Worksheet line 1 divided by line 2, then multiplying Step 3 by that reduced rate.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: Multiplies $350,000 by the unreduced plan contribution rate, as IRS Step 6 says.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: Takes the smaller of Steps 5 and 6, exactly as IRS Step 7.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: $70,000 is the IRS Step 8 contribution dollar limit for 2025.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: With no elective deferrals in the supported case, the IRS instruction is to enter the smaller of Step 7 or Step 8 on Step 21.

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: Matches Form 8880 line 1 ABLE contributions and line 4 ABLE distributions after 2022 before the due date.

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: Tracks the $23,500 elective-deferral and designated Roth limit plus catch-up, consistent with the 2025 401(k) limit.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or is an earlier exce
Status: **MATCH**

Model: Tracks Pub. 590-A and Form 5329 excess IRA contribution conditions, including $7,000/$8,000, compensation, Roth income limits, and timely withdrawal.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: Matches Form 8863 line 23 and the American opportunity credit four-prior-tax-year bar.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: Matches Form 8863 line 24 half-time enrollment requirement, including first-three-months-of-2026 treatment for expenses paid in 2025.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: Matches Form 8863 line 25 and the instruction excluding credit awarded solely for proficiency examinations.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: Matches Form 8863 line 26 felony conviction question.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: Uses Form 8863 line 27 with the Adjusted Qualified Education Expenses Worksheet and permits per-period refusal when adjustments exceed a period's expenses.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: Uses Form 8863 line 28, the $2,000 subtraction from line 27 with a zero floor.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: Uses Form 8863 line 29, which is 25% of line 28.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: Uses Form 8863 line 30, the line 28-zero rule or $2,000 plus line 29.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: Uses the lifetime learning worksheet amount, institution expenses less adjustments with a zero floor, for Form 8863 line 31.

## Raw response

```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "Input tracks RRTA compensation in W-2 box 14 and employee-representative Form CT-2, matching the RRTA references in the IRS text."
  - key: "employers"
    status: MATCH
    reason: "Counts employer/W-2 entries; the excess social security rule requires more than one employer."
  - key: "overcount"
    status: MATCH
    reason: "Counts employers whose W-2 box 4 exceeds $10,918.20, matching the IRS rule for any one employer over the limit."
  - key: "over"
    status: MATCH
    reason: "True exactly when an employer withheld more than the per-employer limit, matching the bar on claiming the excess."
  - key: "wages"
    status: MATCH
    reason: "Sums W-2 boxes 3 and 7, the social security wages and tips tested against the $176,100 base."
  - key: "withheld"
    status: MATCH
    reason: "Sums W-2 box 4 social security tax withheld, the amount used for the excess social security credit."
  - key: "eligible"
    status: MATCH
    reason: "Requires more than one employer and total social security wages over $176,100, as the IRS line states."
  - key: "excess"
    status: MATCH
    reason: "Subtracts the $10,918.20 maximum from total withheld and enters zero if not positive."
  - key: "zero"
    status: MATCH
    reason: "Zero is the correct fallback when the excess social security credit conditions are not met."
  - key: "credit"
    status: MATCH
    reason: "Uses excess only when eligible, otherwise zero; the refusals correctly carve out RRTA and single-employer overwithholding."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "The screen lists the Schedule SE items excluded by the simple Schedule C-only computation."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "The screen lists SEP/SIMPLE/qualified-plan and excess-contribution situations outside the one-plan worksheet."
  - key: "Step 1"
    status: MATCH
    reason: "Within supported Schedule C-only cases, the IRS Step 1 amount is the Schedule C net profit or loss; non-Schedule C SE items are refused."
  - key: "Step 2"
    status: MATCH
    reason: "Schedule SE line 13 is the deduction for one-half of self-employment tax also entered on Schedule 1 line 15."
  - key: "Step 3"
    status: MISMATCH
    reason: "IRS Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; it does not provide a zero-or-less floor."
  - key: "Step 5"
    status: MATCH
    reason: "Matches Rate Worksheet line 1 divided by line 2, then multiplying Step 3 by that reduced rate."
  - key: "Step 6"
    status: MATCH
    reason: "Multiplies $350,000 by the unreduced plan contribution rate, as IRS Step 6 says."
  - key: "Step 7"
    status: MATCH
    reason: "Takes the smaller of Steps 5 and 6, exactly as IRS Step 7."
  - key: "Step 8"
    status: MATCH
    reason: "$70,000 is the IRS Step 8 contribution dollar limit for 2025."
  - key: "Step 21"
    status: MATCH
    reason: "With no elective deferrals in the supported case, the IRS instruction is to enter the smaller of Step 7 or Step 8 on Step 21."
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "Matches Form 8880 line 1 ABLE contributions and line 4 ABLE distributions after 2022 before the due date."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "Tracks the $23,500 elective-deferral and designated Roth limit plus catch-up, consistent with the 2025 401(k) limit."
  - key: "(screen) (person.ira_excess)"
    status: MATCH
    reason: "Tracks Pub. 590-A and Form 5329 excess IRA contribution conditions, including $7,000/$8,000, compensation, Roth income limits, and timely withdrawal."
  - key: "23"
    status: MATCH
    reason: "Matches Form 8863 line 23 and the American opportunity credit four-prior-tax-year bar."
  - key: "24"
    status: MATCH
    reason: "Matches Form 8863 line 24 half-time enrollment requirement, including first-three-months-of-2026 treatment for expenses paid in 2025."
  - key: "25"
    status: MATCH
    reason: "Matches Form 8863 line 25 and the instruction excluding credit awarded solely for proficiency examinations."
  - key: "26"
    status: MATCH
    reason: "Matches Form 8863 line 26 felony conviction question."
  - key: "27"
    status: MATCH
    reason: "Uses Form 8863 line 27 with the Adjusted Qualified Education Expenses Worksheet and permits per-period refusal when adjustments exceed a period's expenses."
  - key: "28"
    status: MATCH
    reason: "Uses Form 8863 line 28, the $2,000 subtraction from line 27 with a zero floor."
  - key: "29"
    status: MATCH
    reason: "Uses Form 8863 line 29, which is 25% of line 28."
  - key: "30"
    status: MATCH
    reason: "Uses Form 8863 line 30, the line 28-zero rule or $2,000 plus line 29."
  - key: "31"
    status: MATCH
    reason: "Uses the lifetime learning worksheet amount, institution expenses less adjustments with a zero floor, for Form 8863 line 31."
```
