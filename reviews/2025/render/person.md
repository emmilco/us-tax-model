# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 696bdaa4820f4a2da38a1844c8d7be579e7d734c19fa7cfe6d43668d032b8fd5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e8261ae8a5a4aaab504e935401e7e2a322539ad8ee4596e1a066434a577e0e5c |
| lines judged | 32 |
| match / mismatch / unclear / missing | 32 / 0 / 0 / 0 |
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
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p501 | 2025 returns; PDF created 2026-02-04 | 23 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 23 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: Schedule 3 line 11 covers excess social security and tier 1 RRTA tax, and the IRS sends excess tier 2 to Form 843. This input screens out the RRTA case, and the refusal on the credit line names that case.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Counting the person's confirmed W-2 entries tests the line 11 condition 'had more than one employer for 2025', figured 'separately for you and your spouse'.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts the employers that withheld more than $10,918.20, which is the condition in 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.'

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: This is true when any one employer over-withheld. That triggers the Form 843 or employer-adjustment route, which the credit's refusal names.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: Social security wages plus tips (W-2 boxes 3 and 7) across all W-2s is the 'total wages' tested against $176,100 for line 11.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: The sum of box 4 (social security tax withheld) across W-2s is the amount compared with $10,918.20.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This restates 'had more than one employer for 2025 and total wages of more than $176,100'.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This restates 'a credit on this line for the amount withheld in excess of $10,918.20', floored at zero.

### zero — No excess credit
Status: **MATCH**

Model: This is a zero constant used when the eligibility conditions are not met.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The credit is the excess when eligible and zero otherwise. The refusals cover the RRTA and Form 843 cases the instructions exclude from Form 1040.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: This input screens out the self-employment items the Schedule SE instructions handle specially: church employee income, clergy, Forms 4361/4029, K-1 income, farm income, optional methods, chapter 11, community income, exempt income, and Forms 4137/8919.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: This input screens out the cases Pub. 560 chapter 5 excludes: SARSEPs, rates that are not whole percentages (the Rate Table applies only to whole percentages up to 25%), SECURE 2.0 higher limits, more than one plan, elective deferrals, Roth contributions, and excess contributions.

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: Step 1 is 'net profit from Schedule C (Form 1040), line 31'. Other self-employment sources are refused, and a plan covering more than one Schedule C is screened out.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Step 2 is 'deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which is Schedule SE line 13.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: This restates 'Subtract step 2 from step 1'. The zero floor does not change the maximum deductible contribution.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: The reduced rate (plan rate divided by plan rate plus 1, to 6 decimals) reproduces the Rate Table values, for example 10% gives 0.090909. This restates 'Multiply step 3 by step 4'.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: This restates 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: This restates 'Enter the smaller of step 5 or step 6'.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: This restates 'Contribution dollar limit . . . $70,000'.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: With no elective deferrals (deferrals are screened out for SEP), the worksheet says 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'.

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: This tracks Form 8880 line 1 (ABLE account contributions by the designated beneficiary) and line 4 (distributions received after 2022 and before the due date, including extensions).

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: This uses the elective deferral limit stated in the IRS text, '$23,500 for 2025', plus allowed catch-up contributions.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or did an earlier exc
Status: **MATCH**

Model: This matches Pub. 590-A's excess contribution definition (the smaller of $7,000, or $8,000 at age 50 or older, and taxable compensation, not withdrawn by the due date) and the Form 5329 triggers for recharacterizations and prior-year excess contributions.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: This restates Form 8863 line 23, 'Has the American opportunity credit been claimed for this student for any 4 prior tax years?', and the instructions' 'by you or anyone else'.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: This restates line 24 and the instruction to treat an academic period beginning in the first 3 months of 2026 as beginning in 2025 if paid in 2025.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: This restates line 25 and requirement 1: completion is 'as determined by the eligible educational institution', excluding credit 'awarded solely because of the student's performance on proficiency examinations'.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: This restates line 26 and requirement 4, 'had not been convicted of a federal or state felony for possessing or distributing a controlled substance'.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: This is the smaller of $4,000 and worksheet line 4 (expenses including course materials, less lines 2a+2b+2c). The single-period refusal names the per-academic-period requirement.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: This restates 'Subtract $2,000 from line 27. If zero or less, enter -0-'.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: This restates 'Multiply line 28 by 25% (0.25)'.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: This restates 'If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29'.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: For the lifetime learning credit, qualified expenses are tuition, fees, and materials 'required to be paid to the institution', less the worksheet adjustments, floored at zero. The refusals cover the TIN requirement and multiple academic periods.

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
| (screen) (person.se_screen) | b117049b2d5c553634ae6c5ee8d0619cf62c008db8ea56a0cfd25844c808caa2 |
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
| (screen) (person.ira_excess) | 0725f9a698f6683481a436d50d331a4b1194adc6c9248c3aea874d016a1a961b |
| 23 | 9223c23e3c46b26b83ccb5d841633f2f1b39bbf9863863f6d107c062cbebd231 |
| 24 | 9f1d38d7e493b18f7b91c64374bad4f7eaa16e7049076217bf16d8d3c87ed5a7 |
| 25 | 92bbf9d23da231a378008f560b77f4ecc9287bdf9de6a32bb55f97d1df37d95c |
| 26 | 5e230914a1d319de23b13cb4bc87ab8ec9fae1f62dbbda87ffa25dcff0585388 |
| 27 | d04de78e920912b791ba394ae04e95f4fef3f10775f71a81750b78e02d2017aa |
| 28 | 64f318a8c10578a3c2d0a7174d1edb8fc670185c9e2823f4757760363b220961 |
| 29 | d415e839d3b21c9a897530d90f0ab5460521b98b50772217912525df774c966d |
| 30 | 501858bae5de6663c688087286e82619f981040f1fee5d0e69e3c8d43fa99a1c |
| 31 | a4982520f1dc72c4c683082f99b9af4e316c5c97a1fca88b4f2818b6fafd2763 |
| (rest of the document) | 774637a29894532eb1f17ff28873aee0739a6158bd21538f87516cd8da60346c |

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "Schedule 3 line 11 covers excess social security and tier 1 RRTA tax, and the IRS sends excess tier 2 to Form 843. This input screens out the RRTA case, and the refusal on the credit line names that case."
  - key: "employers"
    status: MATCH
    reason: "Counting the person's confirmed W-2 entries tests the line 11 condition 'had more than one employer for 2025', figured 'separately for you and your spouse'."
  - key: "overcount"
    status: MATCH
    reason: "This counts the employers that withheld more than $10,918.20, which is the condition in 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.'"
  - key: "over"
    status: MATCH
    reason: "This is true when any one employer over-withheld. That triggers the Form 843 or employer-adjustment route, which the credit's refusal names."
  - key: "wages"
    status: MATCH
    reason: "Social security wages plus tips (W-2 boxes 3 and 7) across all W-2s is the 'total wages' tested against $176,100 for line 11."
  - key: "withheld"
    status: MATCH
    reason: "The sum of box 4 (social security tax withheld) across W-2s is the amount compared with $10,918.20."
  - key: "eligible"
    status: MATCH
    reason: "This restates 'had more than one employer for 2025 and total wages of more than $176,100'."
  - key: "excess"
    status: MATCH
    reason: "This restates 'a credit on this line for the amount withheld in excess of $10,918.20', floored at zero."
  - key: "zero"
    status: MATCH
    reason: "This is a zero constant used when the eligibility conditions are not met."
  - key: "credit"
    status: MATCH
    reason: "The credit is the excess when eligible and zero otherwise. The refusals cover the RRTA and Form 843 cases the instructions exclude from Form 1040."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "This input screens out the self-employment items the Schedule SE instructions handle specially: church employee income, clergy, Forms 4361/4029, K-1 income, farm income, optional methods, chapter 11, community income, exempt income, and Forms 4137/8919."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "This input screens out the cases Pub. 560 chapter 5 excludes: SARSEPs, rates that are not whole percentages (the Rate Table applies only to whole percentages up to 25%), SECURE 2.0 higher limits, more than one plan, elective deferrals, Roth contributions, and excess contributions."
  - key: "Step 1"
    status: MATCH
    reason: "Step 1 is 'net profit from Schedule C (Form 1040), line 31'. Other self-employment sources are refused, and a plan covering more than one Schedule C is screened out."
  - key: "Step 2"
    status: MATCH
    reason: "Step 2 is 'deduction for self-employment tax from Schedule 1 (Form 1040), line 15', which is Schedule SE line 13."
  - key: "Step 3"
    status: MATCH
    reason: "This restates 'Subtract step 2 from step 1'. The zero floor does not change the maximum deductible contribution."
  - key: "Step 5"
    status: MATCH
    reason: "The reduced rate (plan rate divided by plan rate plus 1, to 6 decimals) reproduces the Rate Table values, for example 10% gives 0.090909. This restates 'Multiply step 3 by step 4'."
  - key: "Step 6"
    status: MATCH
    reason: "This restates 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'."
  - key: "Step 7"
    status: MATCH
    reason: "This restates 'Enter the smaller of step 5 or step 6'."
  - key: "Step 8"
    status: MATCH
    reason: "This restates 'Contribution dollar limit . . . $70,000'."
  - key: "Step 21"
    status: MATCH
    reason: "With no elective deferrals (deferrals are screened out for SEP), the worksheet says 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'."
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "This tracks Form 8880 line 1 (ABLE account contributions by the designated beneficiary) and line 4 (distributions received after 2022 and before the due date, including extensions)."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "This uses the elective deferral limit stated in the IRS text, '$23,500 for 2025', plus allowed catch-up contributions."
  - key: "(screen) (person.ira_excess)"
    status: MATCH
    reason: "This matches Pub. 590-A's excess contribution definition (the smaller of $7,000, or $8,000 at age 50 or older, and taxable compensation, not withdrawn by the due date) and the Form 5329 triggers for recharacterizations and prior-year excess contributions."
  - key: "23"
    status: MATCH
    reason: "This restates Form 8863 line 23, 'Has the American opportunity credit been claimed for this student for any 4 prior tax years?', and the instructions' 'by you or anyone else'."
  - key: "24"
    status: MATCH
    reason: "This restates line 24 and the instruction to treat an academic period beginning in the first 3 months of 2026 as beginning in 2025 if paid in 2025."
  - key: "25"
    status: MATCH
    reason: "This restates line 25 and requirement 1: completion is 'as determined by the eligible educational institution', excluding credit 'awarded solely because of the student's performance on proficiency examinations'."
  - key: "26"
    status: MATCH
    reason: "This restates line 26 and requirement 4, 'had not been convicted of a federal or state felony for possessing or distributing a controlled substance'."
  - key: "27"
    status: MATCH
    reason: "This is the smaller of $4,000 and worksheet line 4 (expenses including course materials, less lines 2a+2b+2c). The single-period refusal names the per-academic-period requirement."
  - key: "28"
    status: MATCH
    reason: "This restates 'Subtract $2,000 from line 27. If zero or less, enter -0-'."
  - key: "29"
    status: MATCH
    reason: "This restates 'Multiply line 28 by 25% (0.25)'."
  - key: "30"
    status: MATCH
    reason: "This restates 'If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29'."
  - key: "31"
    status: MATCH
    reason: "For the lifetime learning credit, qualified expenses are tuition, fees, and materials 'required to be paid to the institution', less the worksheet adjustments, floored at zero. The refusals cover the TIN requirement and multiple academic periods."
```
```
