# Render comparison — person

The rendered English of every printed line of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-31 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c1b75915f8a4ecbae2dc19e04ac57fe02e10c2fc90380b5d533a1b7b723fe3cf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 409c7e8c2c1530dcd5df1e9aa5cd76b9d543901c2a6405e9469a110ad5cec4cc |
| lines judged | 32 |
| match / mismatch / unclear / missing | 27 / 5 / 0 / 0 |
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
| i5329 | 2025 | 1, 3, 5, 8, 9 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5, 8, 9 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| p590b | 2025 | 27, 28 | cited pages | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 27, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f5329 | 2025 | 1, 2, 3 | whole document | 53ac10ecce39dbd1cc0a3b88c04e351c2a61f3ad35d145d5d847f30f47a1b945 | - | c65e0cd9d9ad8e8a04899ec87a11393ad5a3e281543eb6720b72357811f8f51d |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p503 | For use in preparing 2025 returns | 3, 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: The screen matches the W-2 instructions, which report RRTA compensation and Tier 1 and Tier 2 taxes in box 14, and the Form 8959 instructions on employee representatives filing Form CT-2. It gates the refusal of the RRTA path that Schedule 3, line 11 would otherwise cover.

### employers — Total w2.one for this person
Status: **MATCH**

Model: Counting one per W-2 employer entry implements the Schedule 3, line 11 test of whether the person 'had more than one employer for 2025', figured separately for each spouse.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts the employers that withheld more than $10,918.20, as in 'if any one employer withheld more than $10,918.20'. The W-2 box 4 instructions give the same amount ($176,100 x 6.2%).

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: True when any one employer overwithheld, which is the condition under which 'you can't claim the excess on your return'.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: Boxes 3 and 7 are social security wages and tips, summed per person, which fits 'total wages' under the line 11 test. Schedule SE line 8a uses the same total.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Summing W-2 box 4 per person gives the social security tax withheld that the line 11 instruction compares with $10,918.20, figured 'separately for you and your spouse'.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This matches 'had more than one employer for 2025 and total wages of more than $176,100'.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This matches 'the amount withheld in excess of $10,918.20'. The zero floor changes nothing because no excess means no credit.

### zero — No excess credit
Status: **MATCH**

Model: This program constant supplies the no-credit branch when the line 11 conditions are not met. It does not conflict with the IRS text.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The credit equals the excess when the line 11 conditions are met and zero otherwise. The refusals correctly exclude the RRTA path and Form 843 cases, including 'If the employer doesn't adjust the overcollection, you can file a claim for refund using Form 843'.

### (screen) (person.se_screen) — Does any of these apply to this person's self-employment?
Status: **MATCH**

Model: The screen covers the Schedule SE items outside a Schedule C-only computation: church income, clergy and Forms 4361 and 4029, K-1 and other income, farm and CRP amounts, optional methods, chapter 11, community income, exempt income, and lines 8b and 8c. Each item is supported by Schedule SE and its instructions.

### (screen) (person.plan_screen) — Does any of these apply to this person's retirement contributions?
Status: **MATCH**

Model: The screen narrows the plan cases consistently with Pub. 560: no SARSEPs on the worksheet, the Rate Table for whole percentages up to 25%, the section 117 higher SIMPLE limits, and one plan only. It names what is excluded.

### Step 1 — Net profit from Schedule C, line 31
Status: **MATCH**

Model: This enters net profit from Schedule C, line 31. Schedule F and K-1 amounts, and the footnote reductions tied to them, are excluded by the named self-employment refusal.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **MATCH**

Model: Worksheet step 2 uses Schedule 1, line 15, which the Form 1040 instructions and Schedule SE line 13 identify as the deductible part of self-employment tax.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **MATCH**

Model: This matches 'Subtract step 2 from step 1'. The added zero floor only prevents a negative base when there are no net earnings, and no deduction would result in that case.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **MATCH**

Model: The rate divided by (rate + 100%), rounded to six places, reproduces the Rate Table (for example 10% gives 0.090909, 25% gives 0.200000), and 'Multiply step 3 by step 4' is then applied. The Rate Worksheet uses the same formula.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **MATCH**

Model: This matches 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **MATCH**

Model: This matches 'Enter the smaller of step 5 or step 6'.

### Step 8 — Contribution dollar limit
Status: **MATCH**

Model: This matches the printed 'Contribution dollar limit' of $70,000.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **MATCH**

Model: The worksheet says that without elective deferrals you 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'. The plan screen excludes SARSEP and Roth cases that would involve deferrals.

### (screen) (person.sav_able) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or di
Status: **MATCH**

Model: This tracks Form 8880 line 1 ('ABLE account contributions by the designated beneficiary') and line 4 (distributions 'received after 2022 and before the due date (including extensions)', including ABLE accounts).

### (screen) (person.sav_excess) — Were your elective deferrals and designated Roth contributions for 2025 more than the limi
Status: **MATCH**

Model: This agrees with the W-2 instructions' 2025 limit: 'the 2025 limit for elective deferrals and designated Roth contributions is $23,500', reported in box 12. Catch-up contributions are allowed for for employees age 50 or older.

### (screen) (person.ira_excess) — Were your 2025 IRA contributions more than allowed, recharacterized, or is an earlier exce
Status: **MATCH**

Model: This reflects the combined limit (the smaller of $7,000 or $8,000, or taxable compensation) and the Roth income limit in the Form 8606 instructions. It also reflects withdrawal with earnings by the due date, recharacterizations, and prior-year excess carried on Form 5329.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: The question matches Form 8863 line 23 and the instruction that the credit 'has not been claimed (by you or anyone else) for this student for any 4 tax years before 2025'. The problems in the eligible-student gate affect the credit amounts and are recorded at lines 27 to 31.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: This matches line 24 and the instruction to treat an academic period beginning in the first 3 months of 2026 as beginning in 2025 if its expenses were paid in 2025. The reporting gate follows the form's 'Go to line 25' flow.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: This matches line 25 and the instructions: 4 years not completed as of the beginning of 2025 'as determined by the eligible educational institution', excluding credit awarded solely for proficiency examinations.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: This matches line 26 and the instruction on a 'federal or state felony for possessing or distributing a controlled substance' as of the end of 2025.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]

Model: The worksheet arithmetic and $4,000 cap are right, but the gate accepts an applied-for ITIN, while the instructions say 'Filers and students must have been issued a TIN by the due date of their 2025 return'. The gate also requires a Form 1098-T request 'after February 2, 2026', while the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. The TIN objection is an interface gap: p970 p. 11 (not among its pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return", so the gate's "applied for" (person.itin_applied, household.all_tin) says what the source allows (amb.2025.edu_filer_tin for the filers on a joint return). The worksheet arithmetic and the $4,000 cap match, as the model says. Why the line is new to the open list: lines 27 to 31 were judged MATCH in Stage 21; the render prompt changed only in the reworded questions of person.tin (BUG-0225), person.edu_1098t (BUG-0226), person.edu_inst (BUG-0227) and person.x_other (BUG-0242). The reviewer objects to text the fixes did not touch (the date and the applied-for ITIN, as in the dependent render log), and raises no objection to the new cooperation condition of the Form 1098-T exception, which matches i8863 p. 1 ("You must fully cooperate with the educational institution's efforts to gather the information needed to furnish the Form 1098-T."), or to the new expense exclusions. Fix round 4 re-check: the render prompt changed only in the person.itin_applied wording of BUG-0259 (an application to renew an expired ITIN by the due date now counts as the application); the reviewer raises no objection to the renewal wording, and its applied-for objection is the one ruled above: the p970 deeming, under which an ITIN applied for (a renewal is filed as an application on Form W-7) and issued counts as issued by the due date. Hardening round re-check: the only project change since fix round 4 is BUG-0263 (person.sep_s3 now links amb.2025.sep_loss_floor; no value change), which these lines do not read; the fresh reply repeats the same two objections in new words (the applied-for ITIN and the Form 1098-T request date), both ruled above, and raises no new one. Project stands.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]

Model: Subtracting $2,000 with a zero floor is right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. The TIN objection is an interface gap: p970 p. 11 (not among its pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return", so the gate's "applied for" (person.itin_applied, household.all_tin) says what the source allows (amb.2025.edu_filer_tin for the filers on a joint return). The subtraction matches, as the model says. Why the line is new to the open list: lines 27 to 31 were judged MATCH in Stage 21; the render prompt changed only in the reworded questions of person.tin (BUG-0225), person.edu_1098t (BUG-0226), person.edu_inst (BUG-0227) and person.x_other (BUG-0242). The reviewer objects to text the fixes did not touch (the date and the applied-for ITIN, as in the dependent render log), and raises no objection to the new cooperation condition of the Form 1098-T exception, which matches i8863 p. 1 ("You must fully cooperate with the educational institution's efforts to gather the information needed to furnish the Form 1098-T."), or to the new expense exclusions. Fix round 4 re-check: the render prompt changed only in the person.itin_applied wording of BUG-0259 (an application to renew an expired ITIN by the due date now counts as the application); the reviewer raises no objection to the renewal wording, and its applied-for objection is the one ruled above: the p970 deeming, under which an ITIN applied for (a renewal is filed as an application on Form W-7) and issued counts as issued by the due date. Hardening round re-check: the only project change since fix round 4 is BUG-0263 (person.sep_s3 now links amb.2025.sep_loss_floor; no value change), which these lines do not read; the fresh reply repeats the same two objections in new words (the applied-for ITIN and the Form 1098-T request date), both ruled above, and raises no new one. Project stands.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]

Model: Multiplying line 28 by 25% is right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. The TIN objection is an interface gap: p970 p. 11 (not among its pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return", so the gate's "applied for" (person.itin_applied, household.all_tin) says what the source allows (amb.2025.edu_filer_tin for the filers on a joint return). The 25% matches, as the model says. Why the line is new to the open list: lines 27 to 31 were judged MATCH in Stage 21; the render prompt changed only in the reworded questions of person.tin (BUG-0225), person.edu_1098t (BUG-0226), person.edu_inst (BUG-0227) and person.x_other (BUG-0242). The reviewer objects to text the fixes did not touch (the date and the applied-for ITIN, as in the dependent render log), and raises no objection to the new cooperation condition of the Form 1098-T exception, which matches i8863 p. 1 ("You must fully cooperate with the educational institution's efforts to gather the information needed to furnish the Form 1098-T."), or to the new expense exclusions. Fix round 4 re-check: the render prompt changed only in the person.itin_applied wording of BUG-0259 (an application to renew an expired ITIN by the due date now counts as the application); the reviewer raises no objection to the renewal wording, and its applied-for objection is the one ruled above: the p970 deeming, under which an ITIN applied for (a renewal is filed as an application on Form W-7) and issued counts as issued by the due date. Hardening round re-check: the only project change since fix round 4 is BUG-0263 (person.sep_s3 now links amb.2025.sep_loss_floor; no value change), which these lines do not read; the fresh reply repeats the same two objections in new words (the applied-for ITIN and the Form 1098-T request date), both ruled above, and raises no new one. Project stands.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]

Model: The line 28 zero test and the $2,000 addition are right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. The TIN objection is an interface gap: p970 p. 11 (not among its pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return", so the gate's "applied for" (person.itin_applied, household.all_tin) says what the source allows (amb.2025.edu_filer_tin for the filers on a joint return). The line 30 rule matches, as the model says. Why the line is new to the open list: lines 27 to 31 were judged MATCH in Stage 21; the render prompt changed only in the reworded questions of person.tin (BUG-0225), person.edu_1098t (BUG-0226), person.edu_inst (BUG-0227) and person.x_other (BUG-0242). The reviewer objects to text the fixes did not touch (the date and the applied-for ITIN, as in the dependent render log), and raises no objection to the new cooperation condition of the Form 1098-T exception, which matches i8863 p. 1 ("You must fully cooperate with the educational institution's efforts to gather the information needed to furnish the Form 1098-T."), or to the new expense exclusions. Fix round 4 re-check: the render prompt changed only in the person.itin_applied wording of BUG-0259 (an application to renew an expired ITIN by the due date now counts as the application); the reviewer raises no objection to the renewal wording, and its applied-for objection is the one ruled above: the p970 deeming, under which an ITIN applied for (a renewal is filed as an application on Form W-7) and issued counts as issued by the due date. Hardening round re-check: the only project change since fix round 4 is BUG-0263 (person.sep_s3 now links amb.2025.sep_loss_floor; no value change), which these lines do not read; the fresh reply repeats the same two objections in new words (the applied-for ITIN and the Form 1098-T request date), both ruled above, and raises no new one. Project stands.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MISMATCH**

Restated: Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → line zero]

Model: Institution-required expenses less adjustments is right, but the gate accepts a student's applied-for ITIN, while the IRS text says 'Students must have been issued a TIN by the due date of their 2025 return'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. The TIN objection is an interface gap: p970 p. 11 (not among its pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return", so the gate's "applied for" (person.itin_applied, household.all_tin) says what the source allows (amb.2025.edu_filer_tin for the filers on a joint return). The lifetime learning amount (expenses required to be paid to the institution) matches, as the model says. Why the line is new to the open list: lines 27 to 31 were judged MATCH in Stage 21; the render prompt changed only in the reworded questions of person.tin (BUG-0225), person.edu_1098t (BUG-0226), person.edu_inst (BUG-0227) and person.x_other (BUG-0242). The reviewer objects to text the fixes did not touch (the date and the applied-for ITIN, as in the dependent render log), and raises no objection to the new cooperation condition of the Form 1098-T exception, which matches i8863 p. 1 ("You must fully cooperate with the educational institution's efforts to gather the information needed to furnish the Form 1098-T."), or to the new expense exclusions. Fix round 4 re-check: the render prompt changed only in the person.itin_applied wording of BUG-0259 (an application to renew an expired ITIN by the due date now counts as the application); the reviewer raises no objection to the renewal wording, and its applied-for objection is the one ruled above: the p970 deeming, under which an ITIN applied for (a renewal is filed as an application on Form W-7) and issued counts as issued by the due date. Hardening round re-check: the only project change since fix round 4 is BUG-0263 (person.sep_s3 now links amb.2025.sep_loss_floor; no value change), which these lines do not read; the fresh reply repeats the same two objections in new words (the applied-for ITIN and the Form 1098-T request date), both ruled above, and raises no new one. Project stands.

## Raw response

```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The screen matches the W-2 instructions, which report RRTA compensation and Tier 1 and Tier 2 taxes in box 14, and the Form 8959 instructions on employee representatives filing Form CT-2. It gates the refusal of the RRTA path that Schedule 3, line 11 would otherwise cover."
  - key: "employers"
    status: MATCH
    reason: "Counting one per W-2 employer entry implements the Schedule 3, line 11 test of whether the person 'had more than one employer for 2025', figured separately for each spouse."
  - key: "overcount"
    status: MATCH
    reason: "This counts the employers that withheld more than $10,918.20, as in 'if any one employer withheld more than $10,918.20'. The W-2 box 4 instructions give the same amount ($176,100 x 6.2%)."
  - key: "over"
    status: MATCH
    reason: "True when any one employer overwithheld, which is the condition under which 'you can't claim the excess on your return'."
  - key: "wages"
    status: MATCH
    reason: "Boxes 3 and 7 are social security wages and tips, summed per person, which fits 'total wages' under the line 11 test. Schedule SE line 8a uses the same total."
  - key: "withheld"
    status: MATCH
    reason: "Summing W-2 box 4 per person gives the social security tax withheld that the line 11 instruction compares with $10,918.20, figured 'separately for you and your spouse'."
  - key: "eligible"
    status: MATCH
    reason: "This matches 'had more than one employer for 2025 and total wages of more than $176,100'."
  - key: "excess"
    status: MATCH
    reason: "This matches 'the amount withheld in excess of $10,918.20'. The zero floor changes nothing because no excess means no credit."
  - key: "zero"
    status: MATCH
    reason: "This program constant supplies the no-credit branch when the line 11 conditions are not met. It does not conflict with the IRS text."
  - key: "credit"
    status: MATCH
    reason: "The credit equals the excess when the line 11 conditions are met and zero otherwise. The refusals correctly exclude the RRTA path and Form 843 cases, including 'If the employer doesn't adjust the overcollection, you can file a claim for refund using Form 843'."
  - key: "(screen) (person.se_screen)"
    status: MATCH
    reason: "The screen covers the Schedule SE items outside a Schedule C-only computation: church income, clergy and Forms 4361 and 4029, K-1 and other income, farm and CRP amounts, optional methods, chapter 11, community income, exempt income, and lines 8b and 8c. Each item is supported by Schedule SE and its instructions."
  - key: "(screen) (person.plan_screen)"
    status: MATCH
    reason: "The screen narrows the plan cases consistently with Pub. 560: no SARSEPs on the worksheet, the Rate Table for whole percentages up to 25%, the section 117 higher SIMPLE limits, and one plan only. It names what is excluded."
  - key: "Step 1"
    status: MATCH
    reason: "This enters net profit from Schedule C, line 31. Schedule F and K-1 amounts, and the footnote reductions tied to them, are excluded by the named self-employment refusal."
  - key: "Step 2"
    status: MATCH
    reason: "Worksheet step 2 uses Schedule 1, line 15, which the Form 1040 instructions and Schedule SE line 13 identify as the deductible part of self-employment tax."
  - key: "Step 3"
    status: MATCH
    reason: "This matches 'Subtract step 2 from step 1'. The added zero floor only prevents a negative base when there are no net earnings, and no deduction would result in that case."
  - key: "Step 5"
    status: MATCH
    reason: "The rate divided by (rate + 100%), rounded to six places, reproduces the Rate Table (for example 10% gives 0.090909, 25% gives 0.200000), and 'Multiply step 3 by step 4' is then applied. The Rate Worksheet uses the same formula."
  - key: "Step 6"
    status: MATCH
    reason: "This matches 'Multiply $350,000 by your plan contribution rate (not the reduced rate)'."
  - key: "Step 7"
    status: MATCH
    reason: "This matches 'Enter the smaller of step 5 or step 6'."
  - key: "Step 8"
    status: MATCH
    reason: "This matches the printed 'Contribution dollar limit' of $70,000."
  - key: "Step 21"
    status: MATCH
    reason: "The worksheet says that without elective deferrals you 'skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21'. The plan screen excludes SARSEP and Roth cases that would involve deferrals."
  - key: "(screen) (person.sav_able)"
    status: MATCH
    reason: "This tracks Form 8880 line 1 ('ABLE account contributions by the designated beneficiary') and line 4 (distributions 'received after 2022 and before the due date (including extensions)', including ABLE accounts)."
  - key: "(screen) (person.sav_excess)"
    status: MATCH
    reason: "This agrees with the W-2 instructions' 2025 limit: 'the 2025 limit for elective deferrals and designated Roth contributions is $23,500', reported in box 12. Catch-up contributions are allowed for for employees age 50 or older."
  - key: "(screen) (person.ira_excess)"
    status: MATCH
    reason: "This reflects the combined limit (the smaller of $7,000 or $8,000, or taxable compensation) and the Roth income limit in the Form 8606 instructions. It also reflects withdrawal with earnings by the due date, recharacterizations, and prior-year excess carried on Form 5329."
  - key: "23"
    status: MATCH
    reason: "The question matches Form 8863 line 23 and the instruction that the credit 'has not been claimed (by you or anyone else) for this student for any 4 tax years before 2025'. The problems in the eligible-student gate affect the credit amounts and are recorded at lines 27 to 31."
  - key: "24"
    status: MATCH
    reason: "This matches line 24 and the instruction to treat an academic period beginning in the first 3 months of 2026 as beginning in 2025 if its expenses were paid in 2025. The reporting gate follows the form's 'Go to line 25' flow."
  - key: "25"
    status: MATCH
    reason: "This matches line 25 and the instructions: 4 years not completed as of the beginning of 2025 'as determined by the eligible educational institution', excluding credit awarded solely for proficiency examinations."
  - key: "26"
    status: MATCH
    reason: "This matches line 26 and the instruction on a 'federal or state felony for possessing or distributing a controlled substance' as of the end of 2025."
  - key: "27"
    status: MISMATCH
    reason: "The worksheet arithmetic and $4,000 cap are right, but the gate accepts an applied-for ITIN, while the instructions say 'Filers and students must have been issued a TIN by the due date of their 2025 return'. The gate also requires a Form 1098-T request 'after February 2, 2026', while the IRS text says 'After January 31, 2026'."
  - key: "28"
    status: MISMATCH
    reason: "Subtracting $2,000 with a zero floor is right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'."
  - key: "29"
    status: MISMATCH
    reason: "Multiplying line 28 by 25% is right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'."
  - key: "30"
    status: MISMATCH
    reason: "The line 28 zero test and the $2,000 addition are right, but the line inherits a gate that accepts an applied-for ITIN, contrary to 'must have been issued a TIN by the due date'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'."
  - key: "31"
    status: MISMATCH
    reason: "Institution-required expenses less adjustments is right, but the gate accepts a student's applied-for ITIN, while the IRS text says 'Students must have been issued a TIN by the due date of their 2025 return'. The gate also uses 'after February 2, 2026' where the IRS text says 'After January 31, 2026'."
```
