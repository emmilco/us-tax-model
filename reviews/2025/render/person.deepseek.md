# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4a463469695f692171c99d1fd3b66d05d02ba647f45a2516554a2df009b4d850 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a13414b8df766c51657a30dcdf2b8cf3025ca895a0c16c5d5818b1a26c3ad8b3 |
| lines judged | 32 |
| match / mismatch / unclear / missing | 31 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 33, 40, 41, 44, 45, 47, 66, 93, 94, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 26, 27, 28, 30, 31, 33, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
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
| i5329 | 2025 | 1, 3, 5, 8, 9 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5, 8, 9 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| p590b | 2025 | 27, 28 | cited pages | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 27, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f5329 | 2025 | 1, 2, 3 | whole document | 53ac10ecce39dbd1cc0a3b88c04e351c2a61f3ad35d145d5d847f30f47a1b945 | - | c65e0cd9d9ad8e8a04899ec87a11393ad5a3e281543eb6720b72357811f8f51d |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p501 | 2025 returns; PDF created 2026-02-04 | 23 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 23 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: The restatement matches the RRTA indicators in the provided W-2 and Form CT-2 instructions.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Counts employer entries; IRS line 11 applies when the filer had more than one employer.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: Counts employers whose own withholding exceeds $10,918.20, matching the IRS any-one-employer condition.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: True when at least one employer exceeded the per-employer limit, matching the IRS bar on claiming the excess.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: Sums W-2 box 3 plus box 7, the social security wages and tips used for the $176,100 wage test.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Sums W-2 box 4 social security tax withheld, as used for the excess withholding credit.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: Uses more than one employer and social security wages over $176,100, matching the line 11 eligibility conditions.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: Subtracts $10,918.20 from total withholding and floors at zero, matching the excess Social Security credit computation.

### zero — No excess credit
Status: **MATCH**

Model: The ineligible case is $0, as the credit is not available.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: Chooses excess when eligible and zero otherwise; refusals correctly exclude RRTA and any one employer's over-withholding.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: The screen enumerates the self-employment items outside the supported Schedule C computation and is used as a refusal gate.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: The screen enumerates SARSEP, non-whole or over-25% SEP rates, higher SIMPLE limits, multiple or qualified plans, other deferrals, Roth SEP/SIMPLE, and excess contributions, all outside the supported worksheet cases.

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: IRS Step 1 asks for net profit from Schedule C line 31 (and other self-employment sources the program refuses), and the restatement uses the Schedule C net profit/loss helper only for SEP filers while naming the excluded non-Schedule C sources.
Reviewed in: pass a220b07af79f

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: IRS Step 2 asks for the self-employment tax deduction from Schedule 1 line 15, which is Schedule SE line 13; the restatement uses that helper, with a refusal for railroad retirement cases.
Reviewed in: pass a220b07af79f

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MISMATCH**

Restated: Subtract line Step 2 from line Step 1. If zero or less, enter -0-.

Model: IRS Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; the restatement adds 'If zero or less, enter -0-,' which changes a negative subtraction result.

Ruling: ambiguity; amb.2025.sep_loss_floor (BUG-0181). p560 p. 39, "Step 3 Net earnings from self-employment. Subtract step 2 from step 1" prints no floor; person.sep_s3 floors Step 3 at zero and its English says so, the register's chosen reading. Same restatement and objection as the refresh-round ruling. Project stands.
Reviewed in: pass 431c866fff3d

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: The restatement computes the Rate Worksheet rate (plan rate divided by plan rate plus 1) and multiplies Step 3 by it; rounding to 6 decimals satisfies the IRS 'at least 3 decimal places' rule.
Reviewed in: pass 431c866fff3d

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: IRS Step 6 multiplies $350,000 by the plan contribution rate (not the reduced rate), which is what the restatement computes.
Reviewed in: pass 431c866fff3d

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: IRS Step 7 is the smaller of step 5 or step 6, matching the restatement.
Reviewed in: pass 431c866fff3d

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: IRS Step 8 is the $70,000 contribution dollar limit, matching the restatement.
Reviewed in: pass 431c866fff3d

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: For the supported SEP case without elective deferrals, IRS Step 8 directs the filer to enter the smaller of step 7 or step 8 on step 21, matching the restatement.
Reviewed in: pass 431c866fff3d

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: The restatement matches the Form 8880 ABLE contribution and distribution facts.

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: The restatement matches the elective deferral and designated Roth contribution limit, including plan-allowed catch-up contributions.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or did an earlier exc
Status: **MATCH**

Model: The restatement describes the Pub. 590-A and Form 8606 IRA excess, timely-withdrawal, recharacterization, and prior-year excess cases.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: Matches Form 8863 line 23 and the instruction that the American opportunity credit must not have been claimed for the student for any 4 tax years before 2025.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: Matches the half-time enrollment and program-credential requirement, including the first-3-months-of-2026 prepayment rule.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: Matches the first-4-years requirement and the instruction not to count credit awarded solely for proficiency examinations.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: Matches Form 8863 line 26 and the felony controlled-substance conviction disqualifier.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: Uses the Adjusted Qualified Education Expenses Worksheet and the $4,000 cap through the referenced Form 8863 line 27 helper; the multi-period refusal names the excluded over-adjustment case.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: Uses Form 8863 line 28, subtracting $2,000 from line 27 and flooring at zero.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: Multiplies line 28 by 25%, matching Form 8863 line 29.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: Matches Form 8863 line 30: line 27 if line 28 is zero, otherwise $2,000 plus line 29.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: Uses the lifetime learning credit worksheet amount, excludes other course materials, and names the TIN and multi-period exclusions.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| rrta | c288d66fc0f67a39aebb651525bd843ea9349d3ed442ec217c0f6b87e8491641 |
| employers | 08db99585cb04c792038309076c08f4a25e53de478703fbeda72de2fb371c53b |
| overcount | 09ea1d2d60f982805105b3a93befc7303a0de55c8d3de283a6ddb62694dd6741 |
| over | da0cb84ba3b2f215c551b8517f33892c0e8df9c6dce69f97c5cf79d684ad9815 |
| wages | ef55de63eecf9940ed7ddc4524060e242c1ac3627a6a21df545d29ed78e168be |
| withheld | 5dab9ef0579d279bb77cbc94ca90c5869f94016d96bf65afe4b34aaa22af019a |
| eligible | 6b2594067f72412d9f12c77b8627857f26c0aa81b9c1419b2f55922fecb8a726 |
| excess | 2ec6c73ca182e811cf7259d5a2359870a6b4847c23b1a1213dd210cceb89c0f9 |
| zero | 56a11e09deb0116e1f3c128f1752c8b174532238c961ae27a9a708421219f121 |
| credit | 04f651e17bd41d95113216306e28f5303f80898e3ef2041e1a151adc423b3e75 |
| (screen) (person.se_screen) | b0d1e9b80b73ff047c2ba94e65ff5b6abcef473d6027d9c9e88b75e9ecc90d16 |
| (screen) (person.plan_screen) | ed86e8484bea910c1df4dd0d64973e941cda2456c239f982c52205101ac3bd51 |
| Step 1 | 2f1ee32f848fae246d96f744b1f94b9cb1b1e64460d6a4c0b48c0c935a1fd51d |
| Step 2 | 11602d9af4406ebfba4bb3cb46649bd7be586b4194b42ab25e064553db835639 |
| Step 3 | 6dc9e181cefa05af31b1d01d394d867ff43f957d419f78037ca796695fe1f2fa |
| Step 5 | e00f89f146804b9f4194bc873efd88c70e6260f55aa15c548921892b6bdd3c0d |
| Step 6 | 5c109917e19c8a33451ba0d9c242848d4f96a7a3812418f2d5d77536f94746a0 |
| Step 7 | 4785acf98f3e9e7f81ba9b4142b456ed5dcc40b05432d2aac35039d71f2e8b1f |
| Step 8 | 4d37fed6cb8938331b58ff550c7a9144c7e9a75890f7b63ad4c24ac1dd9007f6 |
| Step 21 | c09eb630c2d318f1edb9dbc207e75c4ce84b690f82647c535d3a905095456a44 |
| (screen) (person.sav_able) | 4dac837ece8f3062a726a3909e8e873a3c1a610a0dc74c0fe2bb112fbf2fb6e6 |
| (screen) (person.sav_excess) | 8268c2fc44d105f215387ac095fc2d13542bd84d97ae1432802d40bdd791497e |
| (screen) (person.ira_excess) | fad6ca1db48468bf005a8a6f78cbd76556fe1fbb6c8911d71fa27e5690355329 |
| 23 | 9223c23e3c46b26b83ccb5d841633f2f1b39bbf9863863f6d107c062cbebd231 |
| 24 | 9f1d38d7e493b18f7b91c64374bad4f7eaa16e7049076217bf16d8d3c87ed5a7 |
| 25 | 92bbf9d23da231a378008f560b77f4ecc9287bdf9de6a32bb55f97d1df37d95c |
| 26 | 5e230914a1d319de23b13cb4bc87ab8ec9fae1f62dbbda87ffa25dcff0585388 |
| 27 | 5ef37e070b23e6a98285fa4b0e0cd9726a40cd65c86dfb962b21c02c23edc8c9 |
| 28 | 6c1f2a168e9868523fed8f2c32fc66e42a716d026f5a9f020316b2887ecab81f |
| 29 | ee7befdce4550952ab00442bb5d9727836d56b5abbbcf4b0a5b85f9fc6294ec2 |
| 30 | ed27bcd7d876d97eb839b2ab5dfc58f0a4d3a0f76be0b814b8c73ce0ac7e5a0a |
| 31 | 2e2cf650db9042c47f251df02c2bf685a8204fe8ced1bc6904642a2634133c65 |
| (rest of the document) | 774637a29894532eb1f17ff28873aee0739a6158bd21538f87516cd8da60346c |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 431c866fff3d

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines Step 1, Step 2, Step 3, Step 5, Step 6, Step 7, Step 8, Step 21 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 431c866fff3d39a71db7e878f8aeca4070123dacbee3c91383fd3a05fd3d1cc3 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 042c599231fdffe2732c9f69946822d5f258a6ae8e0bdb1ed6016b3aa4a30e89 |
| receipt | .transcription/person.deepseek.render.lines-5c98605ef622 |
| lines judged | 8 |
| match / mismatch / unclear / missing | 7 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i1040gi | 2025; printed date 2026-02-25 | 93, 94, 95 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 93, 95 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

##### Raw response

```yaml
lines:
  - key: "Step 1"
    status: MATCH
    reason: "IRS Step 1 is net profit from Schedule C line 31 (and Schedule F or K-1 when applicable); the program narrows to Schedule C income and names the excluded self-employment items in its refusal, so it matches within the supported cases."
  - key: "Step 2"
    status: MATCH
    reason: "IRS Step 2 is the deduction for self-employment tax from Schedule 1, line 15; the program uses Schedule SE line 13, which is the same deduction."
  - key: "Step 3"
    status: MISMATCH
    reason: "IRS Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; the restatement adds 'If zero or less, enter -0-,' which changes a negative subtraction result."
  - key: "Step 5"
    status: MATCH
    reason: "The restatement computes the Rate Worksheet rate (plan rate divided by plan rate plus 1) and multiplies Step 3 by it; rounding to 6 decimals satisfies the IRS 'at least 3 decimal places' rule."
  - key: "Step 6"
    status: MATCH
    reason: "IRS Step 6 multiplies $350,000 by the plan contribution rate (not the reduced rate), which is what the restatement computes."
  - key: "Step 7"
    status: MATCH
    reason: "IRS Step 7 is the smaller of step 5 or step 6, matching the restatement."
  - key: "Step 8"
    status: MATCH
    reason: "IRS Step 8 is the $70,000 contribution dollar limit, matching the restatement."
  - key: "Step 21"
    status: MATCH
    reason: "For the supported SEP case without elective deferrals, IRS Step 8 directs the filer to enter the smaller of step 7 or step 8 on step 21, matching the restatement."
```

#### Pass a220b07af79f

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines Step 1, Step 2 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a220b07af79f7ae82fca85535d6bb45233036328f66e3187fbf7e6f3df6c6cf1 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 0573d016b0e35ccad4617f4b18cbf6315ddc93d9cd1b7673d763ba13f4e0d4ce |
| receipt | .transcription/person.deepseek.render.lines-4e81c261b2ac |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| i1040gi | 2025; printed date 2026-02-25 | 93, 94, 95 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 93, 95 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

##### Raw response

```yaml
lines:
  - key: "Step 1"
    status: MATCH
    reason: "IRS Step 1 asks for net profit from Schedule C line 31 (and other self-employment sources the program refuses), and the restatement uses the Schedule C net profit/loss helper only for SEP filers while naming the excluded non-Schedule C sources."
  - key: "Step 2"
    status: MATCH
    reason: "IRS Step 2 asks for the self-employment tax deduction from Schedule 1 line 15, which is Schedule SE line 13; the restatement uses that helper, with a refusal for railroad retirement cases."
```

## Raw response

```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The restatement matches the RRTA indicators in the provided W-2 and Form CT-2 instructions."
  - key: "employers"
    status: MATCH
    reason: "Counts employer entries; IRS line 11 applies when the filer had more than one employer."
  - key: "overcount"
    status: MATCH
    reason: "Counts employers whose own withholding exceeds $10,918.20, matching the IRS any-one-employer condition."
  - key: "over"
    status: MATCH
    reason: "True when at least one employer exceeded the per-employer limit, matching the IRS bar on claiming the excess."
  - key: "wages"
    status: MATCH
    reason: "Sums W-2 box 3 plus box 7, the social security wages and tips used for the $176,100 wage test."
  - key: "withheld"
    status: MATCH
    reason: "Sums W-2 box 4 social security tax withheld, as used for the excess withholding credit."
  - key: "eligible"
    status: MATCH
    reason: "Uses more than one employer and social security wages over $176,100, matching the line 11 eligibility conditions."
  - key: "excess"
    status: MATCH
    reason: "Subtracts $10,918.20 from total withholding and floors at zero, matching the excess Social Security credit computation."
  - key: "zero"
    status: MATCH
    reason: "The ineligible case is $0, as the credit is not available."
  - key: "credit"
    status: MATCH
    reason: "Chooses excess when eligible and zero otherwise; refusals correctly exclude RRTA and any one employer's over-withholding."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "The screen enumerates the self-employment items outside the supported Schedule C computation and is used as a refusal gate."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "The screen enumerates SARSEP, non-whole or over-25% SEP rates, higher SIMPLE limits, multiple or qualified plans, other deferrals, Roth SEP/SIMPLE, and excess contributions, all outside the supported worksheet cases."
  - key: "Step 1"
    status: MATCH
    reason: "Uses the Schedule C net profit helper and refuses non-Schedule C self-employment income, matching Pub. 560 Step 1 within the supported cases."
  - key: "Step 2"
    status: MATCH
    reason: "Uses Schedule SE line 13, which is the Schedule 1 line 15 self-employment tax deduction required by Pub. 560 Step 2."
  - key: "Step 3"
    status: MISMATCH
    reason: "The IRS text says 'Net earnings from self-employment. Subtract step 2 from step 1'; it has no zero-or-less floor, while the restatement adds one."
  - key: "Step 5"
    status: MATCH
    reason: "Computes plan rate divided by plan rate plus 100%, the reduced self-employed rate, then multiplies Step 3; the rounding and cap do not differ in supported whole-percent cases."
  - key: "Step 6"
    status: MATCH
    reason: "Computes $350,000 times the plan contribution rate, not the reduced rate, matching Pub. 560 Step 6."
  - key: "Step 7"
    status: MATCH
    reason: "Takes the smaller of Step 5 and Step 6, as the IRS worksheet says."
  - key: "Step 8"
    status: MATCH
    reason: "Enters the $70,000 contribution dollar limit, as Pub. 560 Step 8 says."
  - key: "Step 21"
    status: MATCH
    reason: "With elective deferrals screened out, IRS Step 21 reduces to the smaller of Step 7 or Step 8; the restatement does that."
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "The restatement matches the Form 8880 ABLE contribution and distribution facts."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "The restatement matches the elective deferral and designated Roth contribution limit, including plan-allowed catch-up contributions."
  - key: "(screen) (person.ira_excess)"
    status: MATCH
    reason: "The restatement describes the Pub. 590-A and Form 8606 IRA excess, timely-withdrawal, recharacterization, and prior-year excess cases."
  - key: "23"
    status: MATCH
    reason: "Matches Form 8863 line 23 and the instruction that the American opportunity credit must not have been claimed for the student for any 4 tax years before 2025."
  - key: "24"
    status: MATCH
    reason: "Matches the half-time enrollment and program-credential requirement, including the first-3-months-of-2026 prepayment rule."
  - key: "25"
    status: MATCH
    reason: "Matches the first-4-years requirement and the instruction not to count credit awarded solely for proficiency examinations."
  - key: "26"
    status: MATCH
    reason: "Matches Form 8863 line 26 and the felony controlled-substance conviction disqualifier."
  - key: "27"
    status: MATCH
    reason: "Uses the Adjusted Qualified Education Expenses Worksheet and the $4,000 cap through the referenced Form 8863 line 27 helper; the multi-period refusal names the excluded over-adjustment case."
  - key: "28"
    status: MATCH
    reason: "Uses Form 8863 line 28, subtracting $2,000 from line 27 and flooring at zero."
  - key: "29"
    status: MATCH
    reason: "Multiplies line 28 by 25%, matching Form 8863 line 29."
  - key: "30"
    status: MATCH
    reason: "Matches Form 8863 line 30: line 27 if line 28 is zero, otherwise $2,000 plus line 29."
  - key: "31"
    status: MATCH
    reason: "Uses the lifetime learning credit worksheet amount, excludes other course materials, and names the TIN and multi-period exclusions."
```
