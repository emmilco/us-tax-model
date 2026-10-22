# Class M hand-work — person

`Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | a303ac74b34ee33ee91a2c41ff234587cf56f497bd42fcd5f9f5ad7b3273ffe2 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 31, 32, 41, 47, 93, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 31, 41, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
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

### case classm.person.1 — prompt sha256 a96df56a90b8e4f291f6f1d60224291e660567c953ad0bfc8785674a5f336c1f; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:false, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.simple_excess:false, person.plan_deduction#0, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:true, person.sav_ineligible:true, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#1, person.ira_contrib#1, person.ira_has:false, person.ira_any_contrib:false, person.ira_excess:false, person.ira_excess_gate:false, person.ira_age50:false, person.ira_work_plan:false, person.ira_se_plan:false, person.ira_cov:false, person.ira_limit#1, person.ira_not_covered_joint:false, person.ira_line2#1, person.ira_line6:positive, person.ira_line6_yes:true, person.ira_wide:true, person.ira_full#0, person.ira_at_full:true, person.ira_prod_wide#1, person.ira_prod_joint#1, person.ira_prod#0, person.ira_floor:left, person.ira_below#0, person.ira_line7_figured#0, person.ira_line7#1, person.ira_over_limit:false, person.ira_7or10:right, person.ira_line12:right, person.ira_deduction#1, person.ira_10or11:right, person.ira_nd_figured:floor, person.ira_nondeductible#1, person.ira_files_8606:false, person.ira_8606_line2#1, person.ira_dist:false, person.ira_dist_gate:false, person.ira_ssb_lim:right, person.ira_ssb_figured:right, person.ira_ssb#1, person.ira_se_figured:floor, person.ira_se#1

### classm.person.1 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 2

### classm.person.1 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $5,363.00

### classm.person.1 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $5,363.00

### classm.person.1 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $192.00

### classm.person.1 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $835.00

### classm.person.1 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $45.00

### classm.person.1 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **DISAGREE**

Project: $0.01
Model: $1.00
Work: Plan rate is 1%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (1% as $0.01, plus 100% as $1.01) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($3,500.00, $350,000 x 1%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.1 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **DISAGREE**

Project: $1.01
Model: $101.00
Work: 1% + 100%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (1% as $0.01, plus 100% as $1.01) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($3,500.00, $350,000 x 1%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.1 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $3,500.00

### classm.person.1 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deduct
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_contrib — This person's traditional IRA contributions for 2025 (zero if the traditional IR
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_has — This person made traditional IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_any_contrib — This person made traditional or Roth IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_excess_gate — This person's IRA contributions for 2025 are excess or recharacterized, or an ea
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_se_plan — This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_limit — The applicable amount for this person ($7,000 if under age 50 at the end of 2025
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_not_covered_joint — Married filing jointly and this person was not covered by a retirement plan
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_line2 — Worksheet line 2 for this person's column
Status: **AGREE**

Value: $89,000.00

### classm.person.1 — person[taxpayer].ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, s
Status: **AGREE**

Value: $47,713.00

### classm.person.1 — person[taxpayer].ira_line6_yes — Line 5 is less than line 2 in this person's column (line 6, Yes)
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_wide — This column takes the single rule (70% or 80%, the $10,000 threshold) — not marr
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_full — The line 6 result at or above which this column takes the applicable amount ($10
Status: **AGREE**

Value: $10,000.00

### classm.person.1 — person[taxpayer].ira_at_full — The line 6 result is at or above the threshold (enter the applicable amount on l
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_p70 — Line 6 multiplied by 70% (0.70)
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_p80 — Line 6 multiplied by 80% (0.80)
Status: **AGREE**

Value: $38,170.40

### classm.person.1 — person[taxpayer].ira_p35 — Line 6 multiplied by 35% (0.35)
Status: **AGREE**

Value: $16,699.55

### classm.person.1 — person[taxpayer].ira_p40 — Line 6 multiplied by 40% (0.40)
Status: **AGREE**

Value: $19,085.20

### classm.person.1 — person[taxpayer].ira_prod_wide — Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older a
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_prod_joint — Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older a
Status: **AGREE**

Value: $16,699.55

### classm.person.1 — person[taxpayer].ira_prod — Line 6 multiplied by the percentage that applies to this column
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_rounded — If the result isn't a multiple of $10, increase it to the next multiple of $10
Status: **AGREE**

Value: $33,400.00

### classm.person.1 — person[taxpayer].ira_floor — If the result is $200 or more, enter the result; but if it is less than $200, en
Status: **AGREE**

Value: $33,400.00

### classm.person.1 — person[taxpayer].ira_below — Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
Status: **DISAGREE**

Project: $33,400.00
Model: $0.00
Work: Line 6 result is not under the threshold

Ruling: representation; project retained; model value dropped from the fixture. person.ira_below is the amount line 7 takes when the line 6 result is under the threshold (i1040gi p. 97, IRA Deduction Worksheet, line 6, "If the result is less than $10,000, go to line 7"); the project figures it whenever line 6 is Yes (line 6 x 70%, $33,399.10, raised to $33,400.00) and reads it only when the result is under the threshold (person.ira_line7_figured). Here line 6 is $47,713.00, "$10,000 or more", so line 7 is the applicable amount, "$7,000 if under age 50 at the end of 2025", $7,000.00, on which the model agrees, as on line 12 and the deduction ($0.00, no contributions). The model gave the unread helper zero because the threshold was not crossed. No change to the data. [dropped]

### classm.person.1 — person[taxpayer].ira_line7_figured — Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_line7 — Worksheet line 7 for this person's column
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_over_limit — This person's traditional and Roth IRA contributions for 2025 together are more 
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_own_total — This person's traditional and Roth IRA contributions for 2025
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_line11 — Worksheet line 11 for this person's column (traditional IRA contributions for 20
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_7or10 — The smaller of line 7 for this column and line 10
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].ira_line12 — Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). T
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA con
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_10or11 — The smaller of line 10 or line 11 of the worksheet for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_nd_figured — Nondeductible contributions figured from the worksheet (the smaller of line 10 o
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 li
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and 
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_ssb_lim — Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].ira_ssb_figured — Social Security Benefits Worksheet copy of the IRA deduction when no one is cove
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se_take — This person's deductions on Schedule 1, lines 15 and 16
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se_figured — This person's earned income as a self-employed individual, less Schedule 1 lines
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### case classm.person.2 — prompt sha256 e5c109ee180fc81145fd9f54f6836e824a5078673d7ca194e4926bb9739ccc9e; branches: person.age65:true, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:false, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:true, person.se_screen:false, person.se_screened:false, person.se_line6#0, person.se_line12#0, person.se_line13#0, person.se_line4c#0, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#0, person.s16#0, person.files_se:false, person.eic_se_has#1, person.eic_se#0, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:true, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#0, person.ira_contrib#1, person.ira_has:false, person.ira_any_contrib:false, person.ira_excess:false, person.ira_excess_gate:false, person.ira_age50:false, person.ira_work_plan:false, person.ira_se_plan:false, person.ira_cov:false, person.ira_limit#1, person.ira_not_covered_joint:false, person.ira_line2#1, person.ira_line6:floor, person.ira_line6_yes:false, person.ira_wide:true, person.ira_full#0, person.ira_at_full:false, person.ira_prod_wide#1, person.ira_prod_joint#1, person.ira_prod#0, person.ira_floor:right, person.ira_below#1, person.ira_line7_figured#1, person.ira_line7#1, person.ira_over_limit:false, person.ira_7or10:left, person.ira_line12:right, person.ira_deduction#1, person.ira_10or11:right, person.ira_nd_figured:floor, person.ira_nondeductible#1, person.ira_files_8606:false, person.ira_8606_line2#1, person.ira_dist:false, person.ira_dist_gate:false, person.ira_ssb_lim:left, person.ira_ssb_figured:right, person.ira_ssb#1, person.ira_se_figured:floor, person.ira_se#0

### classm.person.2 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **DISAGREE**

Project: 2
Model: 1
Work: Only tip_2 paid qualified tips ($4,677); tip_1 paid $0

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line, the project counts each employer entered on the tip roster ('List stable keys for each employer from which you received tips you are deducting'), the model only those with an amount above zero (tip_1 $0, tip_2 $4,677). The count decides only whether line 4a is -0- and line 4c is the worksheet total (i1040gi p. 104, Line 4a, "If you received qualified tips as an employee with respect to employment with more than one employer, enter -0- on line 4a"). This return is married filing separately, and Part II is not filled in for it (f1040s1a p. 1, Part II caution, "If married, you must file jointly to claim this deduction"; s1a.part2), so every Part II line is $0.00 whichever count is used. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $4,677.00

### classm.person.2 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $4,677.00

### classm.person.2 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **DISAGREE**

Project: 2
Model: 0
Work: Both overtime entries report $0, so no employer paid qualified overtime

Ruling: representation; project retained; model value dropped from the fixture. As with the tip roster, the project counts each employer entered on the overtime roster ('List stable keys for each employer that paid you overtime you are deducting'), the model only those with an amount above zero; both entries here are $0 because the filer answered that they were not an FLSA-eligible employee of either employer (otjob.flsa No, so otjob.col_b is zero). The count is read only to decide whether a person with a valid SSN received overtime (s1a.ot_ssn_count), and this return is married filing separately, for which Part III is not filled in (f1040s1a p. 1, Part III caution, "If married, you must file jointly to claim this deduction"; s1a.part3), so every Part III line is $0.00 either way. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $10,165.00

### classm.person.2 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $24,593.00

### classm.person.2 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $2,377.00

### classm.person.2 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **DISAGREE**

Project: $0.09
Model: $9.00
Work: Plan rate 9%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (9% as $0.09, plus 100% as $1.09) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($31,500.00, $350,000 x 9%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.2 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **DISAGREE**

Project: $1.09
Model: $109.00
Work: 9 + 100

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (9% as $0.09, plus 100% as $1.09) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($31,500.00, $350,000 x 9%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.2 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $31,500.00

### classm.person.2 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $5,250.00

### classm.person.2 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $17,227.78

### classm.person.2 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $17,227.78

### classm.person.2 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deduct
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **DISAGREE**

Project: no
Model: yes
Work: Answer given: yes

Ruling: model reading error; project retained; model value dropped from the fixture. The gate is the screen answer joined to an amount: it refuses only when this person has elective deferrals in Form W-2 box 12 above zero and answered that they are over the limit (person.sav_excess_gate; iw2w3 p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D"). Here person.sav_w2 is $0.00, on which the model agrees, so no deferral can be over the limit and the gate is No; the model copied the screen answer (Yes) as the gate's value. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_contrib — This person's traditional IRA contributions for 2025 (zero if the traditional IR
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_has — This person made traditional IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_any_contrib — This person made traditional or Roth IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_excess_gate — This person's IRA contributions for 2025 are excess or recharacterized, or an ea
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_se_plan — This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_limit — The applicable amount for this person ($7,000 if under age 50 at the end of 2025
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_not_covered_joint — Married filing jointly and this person was not covered by a retirement plan
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project: $10,000.00
Model: $0.00
Work: Line 1a No, so lines 2-6 are skipped

Ruling: representation; project retained; model value dropped from the fixture. The project figures each person's line 2 amount from the filing status in every case (here married filing separately, $10,000: i1040gi p. 97, IRA Deduction Worksheet, line 2, "Married filing separately and you lived with your spouse at any time in 2025, enter $10,000"), and the printed worksheet lines 2a and 2b read it only when lines 2 through 6 are completed (ira.lines2to6); the model followed the skip (p. 97, "If you checked 'No' on line 1a (and 'No' on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a"). With no one covered, line 7 is the applicable amount, $7,000.00, and line 6 and the deduction ($0.00) agree. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, s
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line6_yes — Line 5 is less than line 2 in this person's column (line 6, Yes)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_wide — This column takes the single rule (70% or 80%, the $10,000 threshold) — not marr
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].ira_full — The line 6 result at or above which this column takes the applicable amount ($10
Status: **AGREE**

Value: $10,000.00

### classm.person.2 — person[taxpayer].ira_at_full — The line 6 result is at or above the threshold (enter the applicable amount on l
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_p70 — Line 6 multiplied by 70% (0.70)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p80 — Line 6 multiplied by 80% (0.80)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p35 — Line 6 multiplied by 35% (0.35)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p40 — Line 6 multiplied by 40% (0.40)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod_wide — Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older a
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod_joint — Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older a
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod — Line 6 multiplied by the percentage that applies to this column
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_rounded — If the result isn't a multiple of $10, increase it to the next multiple of $10
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_floor — If the result is $200 or more, enter the result; but if it is less than $200, en
Status: **AGREE**

Value: $200.00

### classm.person.2 — person[taxpayer].ira_below — Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line7_figured — Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line7 — Worksheet line 7 for this person's column
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_over_limit — This person's traditional and Roth IRA contributions for 2025 together are more 
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_own_total — This person's traditional and Roth IRA contributions for 2025
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line11 — Worksheet line 11 for this person's column (traditional IRA contributions for 20
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_7or10 — The smaller of line 7 for this column and line 10
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_line12 — Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). T
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA con
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_10or11 — The smaller of line 10 or line 11 of the worksheet for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_nd_figured — Nondeductible contributions figured from the worksheet (the smaller of line 10 o
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 li
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and 
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_ssb_lim — Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_ssb_figured — Social Security Benefits Worksheet copy of the IRA deduction when no one is cove
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se_take — This person's deductions on Schedule 1, lines 15 and 16
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se_figured — This person's earned income as a self-employed individual, less Schedule 1 lines
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### case classm.person.1 — prompt sha256 a96df56a90b8e4f291f6f1d60224291e660567c953ad0bfc8785674a5f336c1f; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:false, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.simple_excess:false, person.plan_deduction#0, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:true, person.sav_ineligible:true, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#1, person.ira_contrib#1, person.ira_has:false, person.ira_any_contrib:false, person.ira_excess:false, person.ira_excess_gate:false, person.ira_age50:false, person.ira_work_plan:false, person.ira_se_plan:false, person.ira_cov:false, person.ira_limit#1, person.ira_not_covered_joint:false, person.ira_line2#1, person.ira_line6:positive, person.ira_line6_yes:true, person.ira_wide:true, person.ira_full#0, person.ira_at_full:true, person.ira_prod_wide#1, person.ira_prod_joint#1, person.ira_prod#0, person.ira_floor:left, person.ira_below#0, person.ira_line7_figured#0, person.ira_line7#1, person.ira_over_limit:false, person.ira_7or10:right, person.ira_line12:right, person.ira_deduction#1, person.ira_10or11:right, person.ira_nd_figured:floor, person.ira_nondeductible#1, person.ira_files_8606:false, person.ira_8606_line2#1, person.ira_dist:false, person.ira_dist_gate:false, person.ira_ssb_lim:right, person.ira_ssb_figured:right, person.ira_ssb#1, person.ira_se_figured:floor, person.ira_se#1

### classm.person.1 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 2

### classm.person.1 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $5,363.00

### classm.person.1 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $5,363.00

### classm.person.1 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $192.00

### classm.person.1 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $835.00

### classm.person.1 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $45.00

### classm.person.1 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **DISAGREE**

Project: $0.01
Model: $1.00
Work: Plan rate is 1%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (1% as $0.01, plus 100% as $1.01) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($3,500.00, $350,000 x 1%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.1 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **DISAGREE**

Project: $1.01
Model: $101.00
Work: 1% + 100%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (1% as $0.01, plus 100% as $1.01) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($3,500.00, $350,000 x 1%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.1 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $3,500.00

### classm.person.1 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deduct
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_contrib — This person's traditional IRA contributions for 2025 (zero if the traditional IR
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_has — This person made traditional IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_any_contrib — This person made traditional or Roth IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_excess_gate — This person's IRA contributions for 2025 are excess or recharacterized, or an ea
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_se_plan — This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_limit — The applicable amount for this person ($7,000 if under age 50 at the end of 2025
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_not_covered_joint — Married filing jointly and this person was not covered by a retirement plan
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_line2 — Worksheet line 2 for this person's column
Status: **AGREE**

Value: $89,000.00

### classm.person.1 — person[taxpayer].ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, s
Status: **AGREE**

Value: $47,713.00

### classm.person.1 — person[taxpayer].ira_line6_yes — Line 5 is less than line 2 in this person's column (line 6, Yes)
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_wide — This column takes the single rule (70% or 80%, the $10,000 threshold) — not marr
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_full — The line 6 result at or above which this column takes the applicable amount ($10
Status: **AGREE**

Value: $10,000.00

### classm.person.1 — person[taxpayer].ira_at_full — The line 6 result is at or above the threshold (enter the applicable amount on l
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].ira_p70 — Line 6 multiplied by 70% (0.70)
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_p80 — Line 6 multiplied by 80% (0.80)
Status: **AGREE**

Value: $38,170.40

### classm.person.1 — person[taxpayer].ira_p35 — Line 6 multiplied by 35% (0.35)
Status: **AGREE**

Value: $16,699.55

### classm.person.1 — person[taxpayer].ira_p40 — Line 6 multiplied by 40% (0.40)
Status: **AGREE**

Value: $19,085.20

### classm.person.1 — person[taxpayer].ira_prod_wide — Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older a
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_prod_joint — Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older a
Status: **AGREE**

Value: $16,699.55

### classm.person.1 — person[taxpayer].ira_prod — Line 6 multiplied by the percentage that applies to this column
Status: **AGREE**

Value: $33,399.10

### classm.person.1 — person[taxpayer].ira_rounded — If the result isn't a multiple of $10, increase it to the next multiple of $10
Status: **AGREE**

Value: $33,400.00

### classm.person.1 — person[taxpayer].ira_floor — If the result is $200 or more, enter the result; but if it is less than $200, en
Status: **AGREE**

Value: $33,400.00

### classm.person.1 — person[taxpayer].ira_below — Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
Status: **DISAGREE**

Project: $33,400.00
Model: $0.00
Work: Line 6 result is not under the threshold

Ruling: representation; project retained; model value dropped from the fixture. person.ira_below is the amount line 7 takes when the line 6 result is under the threshold (i1040gi p. 97, IRA Deduction Worksheet, line 6, "If the result is less than $10,000, go to line 7"); the project figures it whenever line 6 is Yes (line 6 x 70%, $33,399.10, raised to $33,400.00) and reads it only when the result is under the threshold (person.ira_line7_figured). Here line 6 is $47,713.00, "$10,000 or more", so line 7 is the applicable amount, "$7,000 if under age 50 at the end of 2025", $7,000.00, on which the model agrees, as on line 12 and the deduction ($0.00, no contributions). The model gave the unread helper zero because the threshold was not crossed. No change to the data. [dropped]

### classm.person.1 — person[taxpayer].ira_line7_figured — Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_line7 — Worksheet line 7 for this person's column
Status: **AGREE**

Value: $7,000.00

### classm.person.1 — person[taxpayer].ira_over_limit — This person's traditional and Roth IRA contributions for 2025 together are more 
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_own_total — This person's traditional and Roth IRA contributions for 2025
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_line11 — Worksheet line 11 for this person's column (traditional IRA contributions for 20
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_7or10 — The smaller of line 7 for this column and line 10
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].ira_line12 — Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). T
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA con
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_10or11 — The smaller of line 10 or line 11 of the worksheet for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_nd_figured — Nondeductible contributions figured from the worksheet (the smaller of line 10 o
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 li
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and 
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_ssb_lim — Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the
Status: **AGREE**

Value: $3,094.00

### classm.person.1 — person[taxpayer].ira_ssb_figured — Social Security Benefits Worksheet copy of the IRA deduction when no one is cove
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se_take — This person's deductions on Schedule 1, lines 15 and 16
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se_figured — This person's earned income as a self-employed individual, less Schedule 1 lines
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### case classm.person.2 — prompt sha256 e5c109ee180fc81145fd9f54f6836e824a5078673d7ca194e4926bb9739ccc9e; branches: person.age65:true, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:false, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:true, person.se_screen:false, person.se_screened:false, person.se_line6#0, person.se_line12#0, person.se_line13#0, person.se_line4c#0, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#0, person.s16#0, person.files_se:false, person.eic_se_has#1, person.eic_se#0, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:true, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#0, person.ira_contrib#1, person.ira_has:false, person.ira_any_contrib:false, person.ira_excess:false, person.ira_excess_gate:false, person.ira_age50:false, person.ira_work_plan:false, person.ira_se_plan:false, person.ira_cov:false, person.ira_limit#1, person.ira_not_covered_joint:false, person.ira_line2#1, person.ira_line6:floor, person.ira_line6_yes:false, person.ira_wide:true, person.ira_full#0, person.ira_at_full:false, person.ira_prod_wide#1, person.ira_prod_joint#1, person.ira_prod#0, person.ira_floor:right, person.ira_below#1, person.ira_line7_figured#1, person.ira_line7#1, person.ira_over_limit:false, person.ira_7or10:left, person.ira_line12:right, person.ira_deduction#1, person.ira_10or11:right, person.ira_nd_figured:floor, person.ira_nondeductible#1, person.ira_files_8606:false, person.ira_8606_line2#1, person.ira_dist:false, person.ira_dist_gate:false, person.ira_ssb_lim:left, person.ira_ssb_figured:right, person.ira_ssb#1, person.ira_se_figured:floor, person.ira_se#0

### classm.person.2 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **DISAGREE**

Project: 2
Model: 1
Work: Only tip_2 paid qualified tips ($4,677); tip_1 paid $0

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line, the project counts each employer entered on the tip roster ('List stable keys for each employer from which you received tips you are deducting'), the model only those with an amount above zero (tip_1 $0, tip_2 $4,677). The count decides only whether line 4a is -0- and line 4c is the worksheet total (i1040gi p. 104, Line 4a, "If you received qualified tips as an employee with respect to employment with more than one employer, enter -0- on line 4a"). This return is married filing separately, and Part II is not filled in for it (f1040s1a p. 1, Part II caution, "If married, you must file jointly to claim this deduction"; s1a.part2), so every Part II line is $0.00 whichever count is used. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $4,677.00

### classm.person.2 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $4,677.00

### classm.person.2 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **DISAGREE**

Project: 2
Model: 0
Work: Both overtime entries report $0, so no employer paid qualified overtime

Ruling: representation; project retained; model value dropped from the fixture. As with the tip roster, the project counts each employer entered on the overtime roster ('List stable keys for each employer that paid you overtime you are deducting'), the model only those with an amount above zero; both entries here are $0 because the filer answered that they were not an FLSA-eligible employee of either employer (otjob.flsa No, so otjob.col_b is zero). The count is read only to decide whether a person with a valid SSN received overtime (s1a.ot_ssn_count), and this return is married filing separately, for which Part III is not filled in (f1040s1a p. 1, Part III caution, "If married, you must file jointly to claim this deduction"; s1a.part3), so every Part III line is $0.00 either way. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $10,165.00

### classm.person.2 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $24,593.00

### classm.person.2 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $163,954.00

### classm.person.2 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $2,377.00

### classm.person.2 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $49,122.49

### classm.person.2 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **DISAGREE**

Project: $0.09
Model: $9.00
Work: Plan rate 9%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (9% as $0.09, plus 100% as $1.09) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($31,500.00, $350,000 x 9%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.2 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **DISAGREE**

Project: $1.09
Model: $109.00
Work: 9 + 100

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (9% as $0.09, plus 100% as $1.09) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (p560 chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it agree: Deduction Worksheet for Self-Employed step 6 ($31,500.00, $350,000 x 9%) and steps 5, 7 and 21, the SEP deduction and Schedule 1 line 16 (all $0.00). [dropped]

### classm.person.2 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $31,500.00

### classm.person.2 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $5,250.00

### classm.person.2 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $-146,726.22

### classm.person.2 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $17,227.78

### classm.person.2 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $17,227.78

### classm.person.2 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deduct
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **DISAGREE**

Project: no
Model: yes
Work: Answer given: yes

Ruling: model reading error; project retained; model value dropped from the fixture. The gate is the screen answer joined to an amount: it refuses only when this person has elective deferrals in Form W-2 box 12 above zero and answered that they are over the limit (person.sav_excess_gate; iw2w3 p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D"). Here person.sav_w2 is $0.00, on which the model agrees, so no deferral can be over the limit and the gate is No; the model copied the screen answer (Yes) as the gate's value. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_contrib — This person's traditional IRA contributions for 2025 (zero if the traditional IR
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_has — This person made traditional IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_any_contrib — This person made traditional or Roth IRA contributions for 2025
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_excess_gate — This person's IRA contributions for 2025 are excess or recharacterized, or an ea
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_se_plan — This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_limit — The applicable amount for this person ($7,000 if under age 50 at the end of 2025
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_not_covered_joint — Married filing jointly and this person was not covered by a retirement plan
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project: $10,000.00
Model: $0.00
Work: Line 1a No, so lines 2-6 are skipped

Ruling: representation; project retained; model value dropped from the fixture. The project figures each person's line 2 amount from the filing status in every case (here married filing separately, $10,000: i1040gi p. 97, IRA Deduction Worksheet, line 2, "Married filing separately and you lived with your spouse at any time in 2025, enter $10,000"), and the printed worksheet lines 2a and 2b read it only when lines 2 through 6 are completed (ira.lines2to6); the model followed the skip (p. 97, "If you checked 'No' on line 1a (and 'No' on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a"). With no one covered, line 7 is the applicable amount, $7,000.00, and line 6 and the deduction ($0.00) agree. No change to the data. [dropped]

### classm.person.2 — person[taxpayer].ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, s
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line6_yes — Line 5 is less than line 2 in this person's column (line 6, Yes)
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_wide — This column takes the single rule (70% or 80%, the $10,000 threshold) — not marr
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].ira_full — The line 6 result at or above which this column takes the applicable amount ($10
Status: **AGREE**

Value: $10,000.00

### classm.person.2 — person[taxpayer].ira_at_full — The line 6 result is at or above the threshold (enter the applicable amount on l
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_p70 — Line 6 multiplied by 70% (0.70)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p80 — Line 6 multiplied by 80% (0.80)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p35 — Line 6 multiplied by 35% (0.35)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_p40 — Line 6 multiplied by 40% (0.40)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod_wide — Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older a
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod_joint — Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older a
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_prod — Line 6 multiplied by the percentage that applies to this column
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_rounded — If the result isn't a multiple of $10, increase it to the next multiple of $10
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_floor — If the result is $200 or more, enter the result; but if it is less than $200, en
Status: **AGREE**

Value: $200.00

### classm.person.2 — person[taxpayer].ira_below — Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line7_figured — Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line7 — Worksheet line 7 for this person's column
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_over_limit — This person's traditional and Roth IRA contributions for 2025 together are more 
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_own_total — This person's traditional and Roth IRA contributions for 2025
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_line11 — Worksheet line 11 for this person's column (traditional IRA contributions for 20
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_7or10 — The smaller of line 7 for this column and line 10
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_line12 — Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). T
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA con
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_10or11 — The smaller of line 10 or line 11 of the worksheet for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_nd_figured — Nondeductible contributions figured from the worksheet (the smaller of line 10 o
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 li
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and 
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_ssb_lim — Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the
Status: **AGREE**

Value: $7,000.00

### classm.person.2 — person[taxpayer].ira_ssb_figured — Social Security Benefits Worksheet copy of the IRA deduction when no one is cove
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se_take — This person's deductions on Schedule 1, lines 15 and 16
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se_figured — This person's earned income as a self-employed individual, less Schedule 1 lines
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.person.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses are $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "No eligible amount, so no deduction"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "Only one form, not more than one"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "No spouses with separate HSAs and family coverage, so the line 6 rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule of line 6 does not apply"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given Step 1 amount is $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share is $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0.00"
  - printed: "person[taxpayer].hsa_taxable"
    value: "0.00"
    work: "Form 8889 line 16 given as $0.00"
  - printed: "person[taxpayer].hsa_addtax"
    value: "0.00"
    work: "Form 8889 line 17b given as $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "Two tip employers: tip_1 and tip_2"
  - printed: "person[taxpayer].tip_total"
    value: "5363.00"
    work: "Column (d): 3,768 + 1,595"
  - printed: "person[taxpayer].tip_reported"
    value: "5363.00"
    work: "Column (b): 3,768 + 1,595"
  - printed: "person[taxpayer].ot_employers"
    value: "1"
    work: "One overtime employer entry (ot_1)"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "Column (b) total is $0.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "Neither self-employment nor railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "No employer withheld more than the limit"
  - printed: "person[taxpayer].wages"
    value: "3094.00"
    work: "Social security wages and tips from emp_a"
  - printed: "person[taxpayer].withheld"
    value: "192.00"
    work: "Box 4 from emp_a"
  - printed: "person[taxpayer].box1"
    value: "3094.00"
    work: "Box 1 from emp_a"
  - printed: "person[taxpayer].box2"
    value: "835.00"
    work: "Box 2 from emp_a"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$192 does not exceed $10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible for the excess social security credit"
  - printed: "person[taxpayer].medicare5"
    value: "3094.00"
    work: "Box 5 from emp_a"
  - printed: "person[taxpayer].medicare6"
    value: "45.00"
    work: "Box 6 from emp_a"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No depreciable property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No depreciable property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "No Schedules C"
  - printed: "person[taxpayer].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Self-employment screen answered no"
  - printed: "person[taxpayer].se_line2"
    value: "0.00"
    work: "No Schedule C profit"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Retirement screen answered no; no Schedules C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "1.00"
    work: "Plan rate is 1%"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "101.00"
    work: "1% + 100%"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "No Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 is $0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.009901"
  - printed: "person[taxpayer].sep_s6"
    value: "3500.00"
    work: "350,000 x 1%"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 or 3,500"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0) or step 8 (70,000)"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "Contributions of $0 do not exceed $0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP plan and no contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 is $0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "No catch-up contributions"
  - printed: "person[taxpayer].catchup_limit"
    value: "0.00"
    work: "Under age 50, so no catch-up"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 0 and 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% of 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "No deferrals"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals and 3% of compensation, both 0"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Compensation of $0"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% of 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Match formula maximum is 0"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "No contributions"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No plan and no contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Retirement plan is none"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "No SEP or SIMPLE deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No self-employment net profit"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "Schedule SE line 3 (0) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of $0 is under $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "No self-employment income"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "Parts 1 and 2 are both 0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so line 1e goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is $0"
  - printed: "person[taxpayer].dc_earned"
    value: "3094.00"
    work: "Box 1 3,094 + 0 + 0"
  - printed: "person[taxpayer].dc_earned_b"
    value: "3094.00"
    work: "Box 1 3,094 without line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "yes"
    work: "Claimed as a dependent on someone else's 2025 return"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "Traditional 0 + Roth 0"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "Box 12 deferrals are $0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "No SIMPLE plan"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].ira_contrib"
    value: "0.00"
    work: "Traditional IRA question answered no"
  - printed: "person[taxpayer].ira_has"
    value: "no"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_any_contrib"
    value: "no"
    work: "Traditional 0 and Roth 0"
  - printed: "person[taxpayer].ira_excess_gate"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].ira_se_plan"
    value: "no"
    work: "Retirement plan is none"
  - printed: "person[taxpayer].ira_cov"
    value: "no"
    work: "Not covered by a retirement plan at work"
  - printed: "person[taxpayer].ira_limit"
    value: "7000.00"
    work: "Under age 50 at the end of 2025"
  - printed: "person[taxpayer].ira_not_covered_joint"
    value: "no"
    work: "Filing status is not married filing jointly"
  - printed: "person[taxpayer].ira_line2"
    value: "89000.00"
    work: "Single filer amount for line 2"
  - printed: "person[taxpayer].ira_line6"
    value: "47713.00"
    work: "89,000 - 41,287"
  - printed: "person[taxpayer].ira_line6_yes"
    value: "yes"
    work: "41,287 is less than 89,000"
  - printed: "person[taxpayer].ira_wide"
    value: "yes"
    work: "Single filer, so the single rule applies"
  - printed: "person[taxpayer].ira_full"
    value: "10000.00"
    work: "Single threshold is $10,000"
  - printed: "person[taxpayer].ira_at_full"
    value: "yes"
    work: "47,713 is at least 10,000"
  - printed: "person[taxpayer].ira_p70"
    value: "33399.10"
    work: "47,713 x 0.70"
  - printed: "person[taxpayer].ira_p80"
    value: "38170.40"
    work: "47,713 x 0.80"
  - printed: "person[taxpayer].ira_p35"
    value: "16699.55"
    work: "47,713 x 0.35"
  - printed: "person[taxpayer].ira_p40"
    value: "19085.20"
    work: "47,713 x 0.40"
  - printed: "person[taxpayer].ira_prod_wide"
    value: "33399.10"
    work: "Under 50, so 70%"
  - printed: "person[taxpayer].ira_prod_joint"
    value: "16699.55"
    work: "Under 50, so 35%"
  - printed: "person[taxpayer].ira_prod"
    value: "33399.10"
    work: "Single rule uses 70%"
  - printed: "person[taxpayer].ira_rounded"
    value: "33400.00"
    work: "Rounded up to the next multiple of $10"
  - printed: "person[taxpayer].ira_floor"
    value: "33400.00"
    work: "Result is $200 or more"
  - printed: "person[taxpayer].ira_below"
    value: "0.00"
    work: "Line 6 result is not under the threshold"
  - printed: "person[taxpayer].ira_line7_figured"
    value: "7000.00"
    work: "At or above threshold, so the applicable amount"
  - printed: "person[taxpayer].ira_line7"
    value: "7000.00"
    work: "Not covered, so line 7 is the applicable amount ($7,000)"
  - printed: "person[taxpayer].ira_over_limit"
    value: "no"
    work: "$0 is not more than $7,000"
  - printed: "person[taxpayer].ira_own_total"
    value: "0.00"
    work: "Traditional 0 + Roth 0"
  - printed: "person[taxpayer].ira_line11"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_7or10"
    value: "3094.00"
    work: "Smaller of 7,000 and 3,094"
  - printed: "person[taxpayer].ira_line12"
    value: "0.00"
    work: "Smallest of 7,000, 3,094 and 0"
  - printed: "person[taxpayer].ira_deduction"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_10or11"
    value: "0.00"
    work: "Smaller of 3,094 and 0"
  - printed: "person[taxpayer].ira_nd_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_nondeductible"
    value: "0.00"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_files_8606"
    value: "no"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_8606_line2"
    value: "0.00"
    work: "Not filing Form 8606; basis is $0"
  - printed: "person[taxpayer].ira_dist_gate"
    value: "no"
    work: "No nondeductible contributions and no distribution"
  - printed: "person[taxpayer].ira_8606_line14"
    value: "0.00"
    work: "Given line 14 is $0"
  - printed: "person[taxpayer].ira_ssb_lim"
    value: "3094.00"
    work: "Smaller of 7,000 and 3,094"
  - printed: "person[taxpayer].ira_ssb_figured"
    value: "0.00"
    work: "Smallest of 7,000, 3,094 and 0"
  - printed: "person[taxpayer].ira_ssb"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_se_take"
    value: "0.00"
    work: "Schedule 1 lines 15 (0) + 16 (0)"
  - printed: "person[taxpayer].ira_se_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_se"
    value: "0.00"
    work: "No Schedule C"
```
```

### classm.person.2

```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses are $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300 = $0.00"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "No eligible amount, so no deduction"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "No family coverage with separate HSAs, so the line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given refigured line 5 = $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share = $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given = $0.00"
  - printed: "person[taxpayer].hsa_taxable"
    value: "0.00"
    work: "Form 8889 line 16 given = $0.00"
  - printed: "person[taxpayer].hsa_addtax"
    value: "0.00"
    work: "Form 8889 line 17b given = $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "1"
    work: "Only tip_2 paid qualified tips ($4,677); tip_1 paid $0"
  - printed: "person[taxpayer].tip_total"
    value: "4677.00"
    work: "Column (d): 0 + 4,677 = 4,677.00"
  - printed: "person[taxpayer].tip_reported"
    value: "4677.00"
    work: "Column (b): 0 + 4,677 = 4,677.00"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "Both overtime entries report $0, so no employer paid qualified overtime"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "0 + 0 = 0.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "Owner has no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One Form W-2 entry"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "163954.00"
    work: "Social security wages plus tips = 163,954"
  - printed: "person[taxpayer].withheld"
    value: "10165.00"
    work: "Box 4 = 10,165"
  - printed: "person[taxpayer].box1"
    value: "163954.00"
    work: "W-2 box 1"
  - printed: "person[taxpayer].box2"
    value: "24593.00"
    work: "W-2 box 2"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages of 163,954 are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "10,165 is not more than 10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no credit"
  - printed: "person[taxpayer].medicare5"
    value: "163954.00"
    work: "W-2 box 5"
  - printed: "person[taxpayer].medicare6"
    value: "2377.00"
    work: "W-2 box 6"
  - printed: "person[taxpayer].sc_count"
    value: "1"
    work: "One business (biz_a)"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No business use of home"
  - printed: "person[taxpayer].mq_q4"
    value: "49122.49"
    work: "biz_a mq_q4"
  - printed: "person[taxpayer].mq_total"
    value: "49122.49"
    work: "biz_a mq_total"
  - printed: "person[taxpayer].cost179"
    value: "49122.49"
    work: "biz_a cost179"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "biz_a section 179 elected on non-listed property = 0"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 elected on listed property"
  - printed: "person[taxpayer].income179"
    value: "-146726.22"
    work: "biz_a line 31 without section 179 = -146,726.22"
  - printed: "person[taxpayer].has_sc"
    value: "yes"
    work: "sc_count is 1"
  - printed: "person[taxpayer].sc_total"
    value: "-146726.22"
    work: "biz_a Schedule 1 line 3 amount"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "None of the screens applies to this person's self-employment"
  - printed: "person[taxpayer].se_line2"
    value: "-146726.22"
    work: "Schedule C line 31 total"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Screen answer is no, and plan is none"
  - printed: "person[taxpayer].sep_rate_c"
    value: "9.00"
    work: "Plan rate 9%"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "109.00"
    work: "9 + 100"
  - printed: "person[taxpayer].sep_s1"
    value: "-146726.22"
    work: "Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 = 0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "-146,726.22 - 0 is negative, so 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.082569 = 0"
  - printed: "person[taxpayer].sep_s6"
    value: "31500.00"
    work: "350,000 x 0.09"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 and 31,500"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0) and step 8 (70,000)"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "Contributions of 0 are not more than 0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 is a loss, so 0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "No contributions over $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "5250.00"
    work: "Age 60-63 limit for 2025"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 5,250 or 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals (0) or 3% of compensation (0)"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Smaller of 0 or 350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Nonelective formula, so ne_max"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "Contributions of 0 are within limits"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Plan is none"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "Plan deduction is 0"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "Only business has a loss"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "biz_a SEHI = 0"
  - printed: "person[taxpayer].qbi"
    value: "-146726.22"
    work: "biz_a QBI"
  - printed: "person[taxpayer].eic_part1"
    value: "-146726.22"
    work: "SE line 3 (-146,726.22) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of 0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "-146726.22"
    work: "No Schedule SE, so Part 2: Schedule C line 31"
  - printed: "person[taxpayer].eic_se"
    value: "-146726.22"
    work: "Part 2 amount (no Part 1)"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No tips or overtime in the business"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 = 0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total = 0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so it goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is 0"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is 0"
  - printed: "person[taxpayer].dc_earned"
    value: "17227.78"
    work: "163,954 + 0 - 146,726.22 (self-employment loss reduces earned income)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "17227.78"
    work: "Same; no line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 2008, not a dependent, not a student"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "Traditional 0 + Roth 0 + ABLE 0"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "W-2 box 12 deferrals = 0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "yes"
    work: "Answer given: yes"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "No own SIMPLE salary reduction contributions"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "Total = 0"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].ira_contrib"
    value: "0.00"
    work: "Traditional IRA question answered no"
  - printed: "person[taxpayer].ira_has"
    value: "no"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_any_contrib"
    value: "no"
    work: "Traditional 0 and Roth 0"
  - printed: "person[taxpayer].ira_excess_gate"
    value: "no"
    work: "Answer given: no"
  - printed: "person[taxpayer].ira_se_plan"
    value: "no"
    work: "Plan is none"
  - printed: "person[taxpayer].ira_cov"
    value: "no"
    work: "Not covered by a plan (line 1a No)"
  - printed: "person[taxpayer].ira_limit"
    value: "7000.00"
    work: "Answer to age 50 or older at end of 2025 is no"
  - printed: "person[taxpayer].ira_not_covered_joint"
    value: "no"
    work: "Filing status is not MFJ"
  - printed: "person[taxpayer].ira_line2"
    value: "0.00"
    work: "Line 1a No, so lines 2-6 are skipped"
  - printed: "person[taxpayer].ira_line6"
    value: "0.00"
    work: "Lines skipped"
  - printed: "person[taxpayer].ira_line6_yes"
    value: "no"
    work: "Line 5 (118,111.78) is not less than line 2 (0)"
  - printed: "person[taxpayer].ira_wide"
    value: "yes"
    work: "Not MFJ or QSS"
  - printed: "person[taxpayer].ira_full"
    value: "10000.00"
    work: "Single rule threshold"
  - printed: "person[taxpayer].ira_at_full"
    value: "no"
    work: "0 is less than 10,000"
  - printed: "person[taxpayer].ira_p70"
    value: "0.00"
    work: "0 x 0.70"
  - printed: "person[taxpayer].ira_p80"
    value: "0.00"
    work: "0 x 0.80"
  - printed: "person[taxpayer].ira_p35"
    value: "0.00"
    work: "0 x 0.35"
  - printed: "person[taxpayer].ira_p40"
    value: "0.00"
    work: "0 x 0.40"
  - printed: "person[taxpayer].ira_prod_wide"
    value: "0.00"
    work: "Under 50, so 70% of 0"
  - printed: "person[taxpayer].ira_prod_joint"
    value: "0.00"
    work: "35% of 0"
  - printed: "person[taxpayer].ira_prod"
    value: "0.00"
    work: "Wide rule: 0"
  - printed: "person[taxpayer].ira_rounded"
    value: "0.00"
    work: "0 is already a multiple of $10"
  - printed: "person[taxpayer].ira_floor"
    value: "200.00"
    work: "Less than 200, so enter 200"
  - printed: "person[taxpayer].ira_below"
    value: "0.00"
    work: "Line 6 is No, so zero"
  - printed: "person[taxpayer].ira_line7_figured"
    value: "0.00"
    work: "Line 6 is No, so none deductible"
  - printed: "person[taxpayer].ira_line7"
    value: "7000.00"
    work: "Line 1a No, so the applicable amount"
  - printed: "person[taxpayer].ira_over_limit"
    value: "no"
    work: "0 is not more than 7,000"
  - printed: "person[taxpayer].ira_own_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].ira_line11"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_7or10"
    value: "7000.00"
    work: "Smaller of 7,000 or 163,954"
  - printed: "person[taxpayer].ira_line12"
    value: "0.00"
    work: "Smallest of 7,000, 163,954 and 0"
  - printed: "person[taxpayer].ira_deduction"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_10or11"
    value: "0.00"
    work: "Smaller of 163,954 or 0"
  - printed: "person[taxpayer].ira_nd_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_nondeductible"
    value: "0.00"
    work: "No contributions"
  - printed: "person[taxpayer].ira_files_8606"
    value: "no"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_8606_line2"
    value: "0.00"
    work: "Not filing Form 8606"
  - printed: "person[taxpayer].ira_dist_gate"
    value: "no"
    work: "No nondeductible contributions and no distribution"
  - printed: "person[taxpayer].ira_8606_line14"
    value: "0.00"
    work: "Given line 14 = 0"
  - printed: "person[taxpayer].ira_ssb_lim"
    value: "7000.00"
    work: "Smaller of 7,000 or 163,954"
  - printed: "person[taxpayer].ira_ssb_figured"
    value: "0.00"
    work: "Smallest of 7,000, 163,954 and 0"
  - printed: "person[taxpayer].ira_ssb"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_se_take"
    value: "0.00"
    work: "Schedule 1 line 15 (0) + line 16 (0)"
  - printed: "person[taxpayer].ira_se_figured"
    value: "0.00"
    work: "-146,726.22 - 0 is zero or less, so 0"
  - printed: "person[taxpayer].ira_se"
    value: "0.00"
    work: "Self-employment earned income is 0"
```

### classm.person.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses are $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "No eligible amount, so no deduction"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "Only one form, not more than one"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "No spouses with separate HSAs and family coverage, so the line 6 rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule of line 6 does not apply"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given Step 1 amount is $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share is $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0.00"
  - printed: "person[taxpayer].hsa_taxable"
    value: "0.00"
    work: "Form 8889 line 16 given as $0.00"
  - printed: "person[taxpayer].hsa_addtax"
    value: "0.00"
    work: "Form 8889 line 17b given as $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "Two tip employers: tip_1 and tip_2"
  - printed: "person[taxpayer].tip_total"
    value: "5363.00"
    work: "Column (d): 3,768 + 1,595"
  - printed: "person[taxpayer].tip_reported"
    value: "5363.00"
    work: "Column (b): 3,768 + 1,595"
  - printed: "person[taxpayer].ot_employers"
    value: "1"
    work: "One overtime employer entry (ot_1)"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "Column (b) total is $0.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "Neither self-employment nor railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "No employer withheld more than the limit"
  - printed: "person[taxpayer].wages"
    value: "3094.00"
    work: "Social security wages and tips from emp_a"
  - printed: "person[taxpayer].withheld"
    value: "192.00"
    work: "Box 4 from emp_a"
  - printed: "person[taxpayer].box1"
    value: "3094.00"
    work: "Box 1 from emp_a"
  - printed: "person[taxpayer].box2"
    value: "835.00"
    work: "Box 2 from emp_a"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$192 does not exceed $10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible for the excess social security credit"
  - printed: "person[taxpayer].medicare5"
    value: "3094.00"
    work: "Box 5 from emp_a"
  - printed: "person[taxpayer].medicare6"
    value: "45.00"
    work: "Box 6 from emp_a"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No depreciable property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No depreciable property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "No Schedules C"
  - printed: "person[taxpayer].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Self-employment screen answered no"
  - printed: "person[taxpayer].se_line2"
    value: "0.00"
    work: "No Schedule C profit"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Retirement screen answered no; no Schedules C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "1.00"
    work: "Plan rate is 1%"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "101.00"
    work: "1% + 100%"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "No Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 is $0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.009901"
  - printed: "person[taxpayer].sep_s6"
    value: "3500.00"
    work: "350,000 x 1%"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 or 3,500"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0) or step 8 (70,000)"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "Contributions of $0 do not exceed $0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP plan and no contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 is $0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "No catch-up contributions"
  - printed: "person[taxpayer].catchup_limit"
    value: "0.00"
    work: "Under age 50, so no catch-up"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 0 and 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% of 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "No deferrals"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals and 3% of compensation, both 0"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Compensation of $0"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% of 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Match formula maximum is 0"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "No contributions"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No plan and no contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Retirement plan is none"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "No SEP or SIMPLE deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No self-employment net profit"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "Schedule SE line 3 (0) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of $0 is under $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "No self-employment income"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "Parts 1 and 2 are both 0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so line 1e goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is $0"
  - printed: "person[taxpayer].dc_earned"
    value: "3094.00"
    work: "Box 1 3,094 + 0 + 0"
  - printed: "person[taxpayer].dc_earned_b"
    value: "3094.00"
    work: "Box 1 3,094 without line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "yes"
    work: "Claimed as a dependent on someone else's 2025 return"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "Traditional 0 + Roth 0"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "Box 12 deferrals are $0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "No SIMPLE plan"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].ira_contrib"
    value: "0.00"
    work: "Traditional IRA question answered no"
  - printed: "person[taxpayer].ira_has"
    value: "no"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_any_contrib"
    value: "no"
    work: "Traditional 0 and Roth 0"
  - printed: "person[taxpayer].ira_excess_gate"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].ira_se_plan"
    value: "no"
    work: "Retirement plan is none"
  - printed: "person[taxpayer].ira_cov"
    value: "no"
    work: "Not covered by a retirement plan at work"
  - printed: "person[taxpayer].ira_limit"
    value: "7000.00"
    work: "Under age 50 at the end of 2025"
  - printed: "person[taxpayer].ira_not_covered_joint"
    value: "no"
    work: "Filing status is not married filing jointly"
  - printed: "person[taxpayer].ira_line2"
    value: "89000.00"
    work: "Single filer amount for line 2"
  - printed: "person[taxpayer].ira_line6"
    value: "47713.00"
    work: "89,000 - 41,287"
  - printed: "person[taxpayer].ira_line6_yes"
    value: "yes"
    work: "41,287 is less than 89,000"
  - printed: "person[taxpayer].ira_wide"
    value: "yes"
    work: "Single filer, so the single rule applies"
  - printed: "person[taxpayer].ira_full"
    value: "10000.00"
    work: "Single threshold is $10,000"
  - printed: "person[taxpayer].ira_at_full"
    value: "yes"
    work: "47,713 is at least 10,000"
  - printed: "person[taxpayer].ira_p70"
    value: "33399.10"
    work: "47,713 x 0.70"
  - printed: "person[taxpayer].ira_p80"
    value: "38170.40"
    work: "47,713 x 0.80"
  - printed: "person[taxpayer].ira_p35"
    value: "16699.55"
    work: "47,713 x 0.35"
  - printed: "person[taxpayer].ira_p40"
    value: "19085.20"
    work: "47,713 x 0.40"
  - printed: "person[taxpayer].ira_prod_wide"
    value: "33399.10"
    work: "Under 50, so 70%"
  - printed: "person[taxpayer].ira_prod_joint"
    value: "16699.55"
    work: "Under 50, so 35%"
  - printed: "person[taxpayer].ira_prod"
    value: "33399.10"
    work: "Single rule uses 70%"
  - printed: "person[taxpayer].ira_rounded"
    value: "33400.00"
    work: "Rounded up to the next multiple of $10"
  - printed: "person[taxpayer].ira_floor"
    value: "33400.00"
    work: "Result is $200 or more"
  - printed: "person[taxpayer].ira_below"
    value: "0.00"
    work: "Line 6 result is not under the threshold"
  - printed: "person[taxpayer].ira_line7_figured"
    value: "7000.00"
    work: "At or above threshold, so the applicable amount"
  - printed: "person[taxpayer].ira_line7"
    value: "7000.00"
    work: "Not covered, so line 7 is the applicable amount ($7,000)"
  - printed: "person[taxpayer].ira_over_limit"
    value: "no"
    work: "$0 is not more than $7,000"
  - printed: "person[taxpayer].ira_own_total"
    value: "0.00"
    work: "Traditional 0 + Roth 0"
  - printed: "person[taxpayer].ira_line11"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_7or10"
    value: "3094.00"
    work: "Smaller of 7,000 and 3,094"
  - printed: "person[taxpayer].ira_line12"
    value: "0.00"
    work: "Smallest of 7,000, 3,094 and 0"
  - printed: "person[taxpayer].ira_deduction"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_10or11"
    value: "0.00"
    work: "Smaller of 3,094 and 0"
  - printed: "person[taxpayer].ira_nd_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_nondeductible"
    value: "0.00"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_files_8606"
    value: "no"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_8606_line2"
    value: "0.00"
    work: "Not filing Form 8606; basis is $0"
  - printed: "person[taxpayer].ira_dist_gate"
    value: "no"
    work: "No nondeductible contributions and no distribution"
  - printed: "person[taxpayer].ira_8606_line14"
    value: "0.00"
    work: "Given line 14 is $0"
  - printed: "person[taxpayer].ira_ssb_lim"
    value: "3094.00"
    work: "Smaller of 7,000 and 3,094"
  - printed: "person[taxpayer].ira_ssb_figured"
    value: "0.00"
    work: "Smallest of 7,000, 3,094 and 0"
  - printed: "person[taxpayer].ira_ssb"
    value: "0.00"
    work: "No traditional IRA contributions"
  - printed: "person[taxpayer].ira_se_take"
    value: "0.00"
    work: "Schedule 1 lines 15 (0) + 16 (0)"
  - printed: "person[taxpayer].ira_se_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_se"
    value: "0.00"
    work: "No Schedule C"
```
```

### classm.person.2

```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses are $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300 = $0.00"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "No eligible amount, so no deduction"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "No family coverage with separate HSAs, so the line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given refigured line 5 = $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share = $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given = $0.00"
  - printed: "person[taxpayer].hsa_taxable"
    value: "0.00"
    work: "Form 8889 line 16 given = $0.00"
  - printed: "person[taxpayer].hsa_addtax"
    value: "0.00"
    work: "Form 8889 line 17b given = $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "1"
    work: "Only tip_2 paid qualified tips ($4,677); tip_1 paid $0"
  - printed: "person[taxpayer].tip_total"
    value: "4677.00"
    work: "Column (d): 0 + 4,677 = 4,677.00"
  - printed: "person[taxpayer].tip_reported"
    value: "4677.00"
    work: "Column (b): 0 + 4,677 = 4,677.00"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "Both overtime entries report $0, so no employer paid qualified overtime"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "0 + 0 = 0.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "Owner has no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One Form W-2 entry"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "163954.00"
    work: "Social security wages plus tips = 163,954"
  - printed: "person[taxpayer].withheld"
    value: "10165.00"
    work: "Box 4 = 10,165"
  - printed: "person[taxpayer].box1"
    value: "163954.00"
    work: "W-2 box 1"
  - printed: "person[taxpayer].box2"
    value: "24593.00"
    work: "W-2 box 2"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages of 163,954 are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "10,165 is not more than 10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no credit"
  - printed: "person[taxpayer].medicare5"
    value: "163954.00"
    work: "W-2 box 5"
  - printed: "person[taxpayer].medicare6"
    value: "2377.00"
    work: "W-2 box 6"
  - printed: "person[taxpayer].sc_count"
    value: "1"
    work: "One business (biz_a)"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No business use of home"
  - printed: "person[taxpayer].mq_q4"
    value: "49122.49"
    work: "biz_a mq_q4"
  - printed: "person[taxpayer].mq_total"
    value: "49122.49"
    work: "biz_a mq_total"
  - printed: "person[taxpayer].cost179"
    value: "49122.49"
    work: "biz_a cost179"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "biz_a section 179 elected on non-listed property = 0"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 elected on listed property"
  - printed: "person[taxpayer].income179"
    value: "-146726.22"
    work: "biz_a line 31 without section 179 = -146,726.22"
  - printed: "person[taxpayer].has_sc"
    value: "yes"
    work: "sc_count is 1"
  - printed: "person[taxpayer].sc_total"
    value: "-146726.22"
    work: "biz_a Schedule 1 line 3 amount"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "None of the screens applies to this person's self-employment"
  - printed: "person[taxpayer].se_line2"
    value: "-146726.22"
    work: "Schedule C line 31 total"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Screen answer is no, and plan is none"
  - printed: "person[taxpayer].sep_rate_c"
    value: "9.00"
    work: "Plan rate 9%"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "109.00"
    work: "9 + 100"
  - printed: "person[taxpayer].sep_s1"
    value: "-146726.22"
    work: "Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 = 0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "-146,726.22 - 0 is negative, so 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.082569 = 0"
  - printed: "person[taxpayer].sep_s6"
    value: "31500.00"
    work: "350,000 x 0.09"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 and 31,500"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0) and step 8 (70,000)"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "Contributions of 0 are not more than 0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 is a loss, so 0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "No contributions over $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "5250.00"
    work: "Age 60-63 limit for 2025"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 5,250 or 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals (0) or 3% of compensation (0)"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Smaller of 0 or 350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Nonelective formula, so ne_max"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "Contributions of 0 are within limits"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Plan is none"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "Plan deduction is 0"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "Only business has a loss"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "biz_a SEHI = 0"
  - printed: "person[taxpayer].qbi"
    value: "-146726.22"
    work: "biz_a QBI"
  - printed: "person[taxpayer].eic_part1"
    value: "-146726.22"
    work: "SE line 3 (-146,726.22) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of 0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "-146726.22"
    work: "No Schedule SE, so Part 2: Schedule C line 31"
  - printed: "person[taxpayer].eic_se"
    value: "-146726.22"
    work: "Part 2 amount (no Part 1)"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No tips or overtime in the business"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 = 0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total = 0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so it goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is 0"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is 0"
  - printed: "person[taxpayer].dc_earned"
    value: "17227.78"
    work: "163,954 + 0 - 146,726.22 (self-employment loss reduces earned income)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "17227.78"
    work: "Same; no line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 2008, not a dependent, not a student"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "Traditional 0 + Roth 0 + ABLE 0"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "W-2 box 12 deferrals = 0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "yes"
    work: "Answer given: yes"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "No own SIMPLE salary reduction contributions"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "Total = 0"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].ira_contrib"
    value: "0.00"
    work: "Traditional IRA question answered no"
  - printed: "person[taxpayer].ira_has"
    value: "no"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_any_contrib"
    value: "no"
    work: "Traditional 0 and Roth 0"
  - printed: "person[taxpayer].ira_excess_gate"
    value: "no"
    work: "Answer given: no"
  - printed: "person[taxpayer].ira_se_plan"
    value: "no"
    work: "Plan is none"
  - printed: "person[taxpayer].ira_cov"
    value: "no"
    work: "Not covered by a plan (line 1a No)"
  - printed: "person[taxpayer].ira_limit"
    value: "7000.00"
    work: "Answer to age 50 or older at end of 2025 is no"
  - printed: "person[taxpayer].ira_not_covered_joint"
    value: "no"
    work: "Filing status is not MFJ"
  - printed: "person[taxpayer].ira_line2"
    value: "0.00"
    work: "Line 1a No, so lines 2-6 are skipped"
  - printed: "person[taxpayer].ira_line6"
    value: "0.00"
    work: "Lines skipped"
  - printed: "person[taxpayer].ira_line6_yes"
    value: "no"
    work: "Line 5 (118,111.78) is not less than line 2 (0)"
  - printed: "person[taxpayer].ira_wide"
    value: "yes"
    work: "Not MFJ or QSS"
  - printed: "person[taxpayer].ira_full"
    value: "10000.00"
    work: "Single rule threshold"
  - printed: "person[taxpayer].ira_at_full"
    value: "no"
    work: "0 is less than 10,000"
  - printed: "person[taxpayer].ira_p70"
    value: "0.00"
    work: "0 x 0.70"
  - printed: "person[taxpayer].ira_p80"
    value: "0.00"
    work: "0 x 0.80"
  - printed: "person[taxpayer].ira_p35"
    value: "0.00"
    work: "0 x 0.35"
  - printed: "person[taxpayer].ira_p40"
    value: "0.00"
    work: "0 x 0.40"
  - printed: "person[taxpayer].ira_prod_wide"
    value: "0.00"
    work: "Under 50, so 70% of 0"
  - printed: "person[taxpayer].ira_prod_joint"
    value: "0.00"
    work: "35% of 0"
  - printed: "person[taxpayer].ira_prod"
    value: "0.00"
    work: "Wide rule: 0"
  - printed: "person[taxpayer].ira_rounded"
    value: "0.00"
    work: "0 is already a multiple of $10"
  - printed: "person[taxpayer].ira_floor"
    value: "200.00"
    work: "Less than 200, so enter 200"
  - printed: "person[taxpayer].ira_below"
    value: "0.00"
    work: "Line 6 is No, so zero"
  - printed: "person[taxpayer].ira_line7_figured"
    value: "0.00"
    work: "Line 6 is No, so none deductible"
  - printed: "person[taxpayer].ira_line7"
    value: "7000.00"
    work: "Line 1a No, so the applicable amount"
  - printed: "person[taxpayer].ira_over_limit"
    value: "no"
    work: "0 is not more than 7,000"
  - printed: "person[taxpayer].ira_own_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].ira_line11"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_7or10"
    value: "7000.00"
    work: "Smaller of 7,000 or 163,954"
  - printed: "person[taxpayer].ira_line12"
    value: "0.00"
    work: "Smallest of 7,000, 163,954 and 0"
  - printed: "person[taxpayer].ira_deduction"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_10or11"
    value: "0.00"
    work: "Smaller of 163,954 or 0"
  - printed: "person[taxpayer].ira_nd_figured"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].ira_nondeductible"
    value: "0.00"
    work: "No contributions"
  - printed: "person[taxpayer].ira_files_8606"
    value: "no"
    work: "No nondeductible contributions"
  - printed: "person[taxpayer].ira_8606_line2"
    value: "0.00"
    work: "Not filing Form 8606"
  - printed: "person[taxpayer].ira_dist_gate"
    value: "no"
    work: "No nondeductible contributions and no distribution"
  - printed: "person[taxpayer].ira_8606_line14"
    value: "0.00"
    work: "Given line 14 = 0"
  - printed: "person[taxpayer].ira_ssb_lim"
    value: "7000.00"
    work: "Smaller of 7,000 or 163,954"
  - printed: "person[taxpayer].ira_ssb_figured"
    value: "0.00"
    work: "Smallest of 7,000, 163,954 and 0"
  - printed: "person[taxpayer].ira_ssb"
    value: "0.00"
    work: "No traditional contributions"
  - printed: "person[taxpayer].ira_se_take"
    value: "0.00"
    work: "Schedule 1 line 15 (0) + line 16 (0)"
  - printed: "person[taxpayer].ira_se_figured"
    value: "0.00"
    work: "-146,726.22 - 0 is zero or less, so 0"
  - printed: "person[taxpayer].ira_se"
    value: "0.00"
    work: "Self-employment earned income is 0"
```
