# Class M hand-work — person

`Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | a015b7b83d691293077dc92ec2b0059536faa9837d73fbc3efb69019d8dbc1fb |
| cases | 7 |

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

### case classm.person.1 — prompt sha256 ec7603b7bf39fe5fd7bd74e66760f31dd993852babc6ca44fba75fd832613b3e; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.eligible_educator:true, person.born_before_2001:false, person.born_before_2001:true, person.born_after_1960:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#0, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.employer_max#1, person.simple_excess:false, person.plan_deduction#0, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#1

### classm.person.1 — person[spouse].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 1

### classm.person.1 — person[spouse].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $6,220.00

### classm.person.1 — person[spouse].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].employers — Total w2.one for this person
Status: **AGREE**

Value: 2

### classm.person.1 — person[spouse].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].wages — Total w2.wages for this person
Status: **AGREE**

Value: $49,960.00

### classm.person.1 — person[spouse].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $3,098.00

### classm.person.1 — person[spouse].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $49,960.00

### classm.person.1 — person[spouse].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $12,990.00

### classm.person.1 — person[spouse].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $49,960.00

### classm.person.1 — person[spouse].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $724.00

### classm.person.1 — person[spouse].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.11

### classm.person.1 — person[spouse].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.11

### classm.person.1 — person[spouse].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $38,500.00

### classm.person.1 — person[spouse].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $3,500.00

### classm.person.1 — person[spouse].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.1 — person[spouse].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $49,960.00

### classm.person.1 — person[spouse].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $49,960.00

### classm.person.1 — person[spouse].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $12,940.00

### classm.person.1 — person[spouse].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.1 — person[spouse].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[spouse].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $12,940.00

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

### classm.person.1 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 1

### classm.person.1 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

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

Value: 2

### classm.person.1 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.person.1 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.20

### classm.person.1 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.20

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

Value: $70,000.00

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

Value: $3,500.00

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

Value: $0.00

### classm.person.1 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
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

### case classm.person.2 — prompt sha256 392039780df9c30f77a775ad71bb5225c889013bcbf23b51d901939dab92dd18; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:true, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#0, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:true, person.se_screen:false, person.se_screened:false, person.se_line6#0, person.se_line12#0, person.se_line13#0, person.se_line4c#0, person.plan_screen:false, person.plan_screened:false, person.sep_s3:positive, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:positive, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#2, person.s16#0, person.files_se:true, person.eic_se_has#0, person.eic_se#0, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:false, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:true, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#2, person.sav_simple#0

### classm.person.2 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $212.00

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

### classm.person.2 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

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

Value: $32,540.00

### classm.person.2 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $2,017.00

### classm.person.2 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $32,540.00

### classm.person.2 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $8,786.00

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

Value: $32,540.00

### classm.person.2 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $472.00

### classm.person.2 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $41,890.00

### classm.person.2 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $41,890.00

### classm.person.2 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $41,890.00

### classm.person.2 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.05

### classm.person.2 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.05

### classm.person.2 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $41,890.00

### classm.person.2 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $2,959.44

### classm.person.2 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $38,930.56

### classm.person.2 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $1,853.83

### classm.person.2 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $17,500.00

### classm.person.2 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $1,853.83

### classm.person.2 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $1,853.83

### classm.person.2 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $38,685.42

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

Value: $38,685.42

### classm.person.2 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $5,250.00

### classm.person.2 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $1,160.56

### classm.person.2 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $38,685.42

### classm.person.2 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $773.71

### classm.person.2 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $773.71

### classm.person.2 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $96.00

### classm.person.2 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $96.00

### classm.person.2 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $96.00

### classm.person.2 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $41,890.00

### classm.person.2 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $38,834.56

### classm.person.2 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $38,930.56

### classm.person.2 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $38,930.56

### classm.person.2 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $38,930.56

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

Value: $71,470.56

### classm.person.2 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $71,470.56

### classm.person.2 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $6,186.00

### classm.person.2 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### case classm.person.3 — prompt sha256 84d90499ba8e9c4eb682722aa9c5e280964936e7a1a6d2799b06946973488ef1; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.simple_excess:false, person.plan_deduction#1, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#1, person.sav_simple#1

### classm.person.3 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.3 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 2

### classm.person.3 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $28,523.00

### classm.person.3 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $28,523.00

### classm.person.3 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 1

### classm.person.3 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.3 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.16

### classm.person.3 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.16

### classm.person.3 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $56,000.00

### classm.person.3 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.3 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $3,366.00

### classm.person.3 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.3 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.3 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### case classm.person.4 — prompt sha256 2d255b05e7a36bb2ed130b7e7ec12c79e6b237fb900d317fcc3ca2cec812f8c9; branches: person.age65:true, person.blind:true, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:false, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:true, person.se_screen:false, person.se_screened:false, person.se_line6#0, person.se_line12#0, person.se_line13#0, person.se_line4c#0, person.plan_screen:false, person.plan_screened:false, person.sep_s3:positive, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:positive, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#0, person.s16#0, person.files_se:true, person.eic_se_has#0, person.eic_se#0, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#0

### classm.person.4 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.4 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 3

### classm.person.4 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $69,863.00

### classm.person.4 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $69,863.00

### classm.person.4 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.4 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 1

### classm.person.4 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $43,540.89

### classm.person.4 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: yes

### classm.person.4 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $43,540.89

### classm.person.4 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $43,540.89

### classm.person.4 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **DISAGREE**

Project: $0.03
Model: $3.00
Work: Plan rate is 3%

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (3% as $0.03) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it, the Deduction Worksheet for Self-Employed steps 5 to 7 and 21, the SEP deduction and Schedule 1 line 16, agree. [dropped]

### classm.person.4 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **DISAGREE**

Project: $1.03
Model: $103.00
Work: 3 + 100

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier rulings on this line: the plan rate is carried as an amount (3% as $0.03, plus 100% as $1.03) so that Pub. 560's rate for the self-employed, rate / (1 + rate) (chapter 5, Rate Table for Self-Employed), is figured exactly; the model wrote the percentage as a number. The lines that use it, the Deduction Worksheet for Self-Employed steps 5 to 7 and 21, the SEP deduction and Schedule 1 line 16, agree. [dropped]

### classm.person.4 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $43,540.89

### classm.person.4 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $3,076.07

### classm.person.4 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $1,178.58

### classm.person.4 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $10,500.00

### classm.person.4 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $1,178.58

### classm.person.4 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $1,178.58

### classm.person.4 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $40,210.01

### classm.person.4 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $40,210.01

### classm.person.4 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $1,206.30

### classm.person.4 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $40,210.01

### classm.person.4 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $804.20

### classm.person.4 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $804.20

### classm.person.4 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $43,540.89

### classm.person.4 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: yes

### classm.person.4 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.4 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.4 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $40,464.82

### classm.person.4 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $4,059.00

### classm.person.4 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.4 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.4 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### case classm.person.5 — prompt sha256 6aa11785c03d44837e6ec5ad46330604057cd4e267c6c96dd6b200f7c95187b1; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#0, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:true, person.sav_claimed:false, person.sav_ineligible:true, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#1

### classm.person.5 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.5 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 2

### classm.person.5 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $14,821.00

### classm.person.5 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $14,821.00

### classm.person.5 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 2

### classm.person.5 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $44,754.00

### classm.person.5 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $2,775.00

### classm.person.5 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $29,524.00

### classm.person.5 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $7,676.00

### classm.person.5 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $44,754.00

### classm.person.5 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $649.00

### classm.person.5 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.16

### classm.person.5 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.16

### classm.person.5 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $56,000.00

### classm.person.5 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $3,500.00

### classm.person.5 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.5 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.5 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $29,524.00

### classm.person.5 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $29,524.00

### classm.person.5 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: yes

### classm.person.5 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.5 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.5 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $0.00

### case classm.person.6 — prompt sha256 e0c94280fcc55a763fd4a5a292fa6b9857f34d8f6f9c143571a7ccb49f2a993d; branches: person.age65:false, person.blind:false, person.tin:false, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:true, person.born_before_2001:true, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#0, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.simple_excess:false, person.plan_deduction#0, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#1

### classm.person.6 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.6 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 2

### classm.person.6 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $68,151.00

### classm.person.6 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.6 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $155,611.00

### classm.person.6 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $9,648.00

### classm.person.6 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $155,611.00

### classm.person.6 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $45,127.00

### classm.person.6 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $155,611.00

### classm.person.6 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $2,256.00

### classm.person.6 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.04

### classm.person.6 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.04

### classm.person.6 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $14,000.00

### classm.person.6 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $3,500.00

### classm.person.6 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.6 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.6 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $155,611.00

### classm.person.6 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $155,611.00

### classm.person.6 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $8,174.00

### classm.person.6 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.6 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.6 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $8,174.00

### case classm.person.7 — prompt sha256 2d5a3781cba14470b2414b5e9f2850586e07968af06e21b9322198a768ef35d6; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:false, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:true, person.se_screen:false, person.se_screened:false, person.se_line6#0, person.se_line12#0, person.se_line13#0, person.se_line4c#0, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:right, person.match_max:left, person.ne_comp:left, person.employer_max#0, person.simple_excess:false, person.plan_deduction#0, person.s16#0, person.files_se:false, person.eic_se_has#1, person.eic_se#0, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:false, person.sav_claimed:false, person.sav_ineligible:false, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#0, person.sav_simple#0

### classm.person.7 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].educator_eligible_amount — This person's qualified educator expenses up to $300 if an eligible educator, el
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].educator_deduction — This person's educator expense deduction
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

Value: 1

### classm.person.7 — person[taxpayer].hsa_repeated — More than one Form 8889 entered for this person
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

Value: 2

### classm.person.7 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $637.00

### classm.person.7 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $637.00

### classm.person.7 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 1

### classm.person.7 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sc_rrta_count — Number of this person's Schedules C while this person has railroad retirement co
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].se_rrta — Self-employment and railroad retirement compensation together
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.7 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $121,779.00

### classm.person.7 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $7,550.00

### classm.person.7 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $121,779.00

### classm.person.7 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $26,791.00

### classm.person.7 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $121,779.00

### classm.person.7 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $1,766.00

### classm.person.7 — person[taxpayer].sc_count — Number of Schedules C for this person
Status: **AGREE**

Value: 2

### classm.person.7 — person[taxpayer].ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].cost179 — Cost of section 179 property, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].s179_listed — Section 179 elected on listed property, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].has_sc — This person has at least one Schedule C
Status: **AGREE**

Value: yes

### classm.person.7 — person[taxpayer].sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].se_screened — This person's self-employment tax is outside this tool
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].se_line2 — Schedule SE line 2 for this person
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].plan_screened — This person's retirement contributions are outside this tool (screened, or a pla
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].sep_rate_c — The plan rate, as cents
Status: **AGREE**

Value: $0.21

### classm.person.7 — person[taxpayer].sep_rate_plus — The plan rate plus 100%, as cents
Status: **AGREE**

Value: $1.21

### classm.person.7 — person[taxpayer].sep_s1 — Net profit from Schedule C, line 31
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].sep_s2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sep_s3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sep_s5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sep_s6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

Value: $73,500.00

### classm.person.7 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sep_excess — The SEP contributions are more than the maximum deductible contribution
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].sep_deduction — SEP deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].simple_comp — Compensation: net earnings from self-employment (Schedule SE, line 4)
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].simple_regular — Salary reduction contributions that are not catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].simple_catchup — Catch-up contributions
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].catchup_limit — Catch-up contribution limit
Status: **AGREE**

Value: $3,500.00

### classm.person.7 — person[taxpayer].comp_after_regular — Compensation less the salary reduction contributions that are not catch-up contr
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].catchup_max — Maximum catch-up contribution
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].match_3pct — 3% of compensation
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].deferrals_total — Salary reduction contributions (allowed)
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].match_max — Maximum matching contribution
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].ne_comp — Compensation taken into account (not more than $350,000)
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].ne_max — Maximum nonelective contribution
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].employer_max — Maximum employer contribution for the plan's formula
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].simple_excess — Contributions above the SIMPLE limits
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].simple_deduction — SIMPLE deduction for yourself
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].plan_deduction — Self-employed SEP or SIMPLE deduction for this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].s16 — Schedule 1 line 16 for this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].eic_part1 — Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].files_se — This person files Schedule SE (line 4c is $400 or more)
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].eic_se_has — This person's self-employment earned income for Worksheet B
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **AGREE**

Value: $-99,721.09

### classm.person.7 — person[taxpayer].sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

Value: 0

### classm.person.7 — person[taxpayer].dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part repor
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].dc_box10 — Total of box 10 of this person's Forms W-2
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].dc_1e_mine — Form 1040 line 1e is counted in this person's earned income: the only person who
Status: **AGREE**

Value: yes

### classm.person.7 — person[taxpayer].dc_1e_counted — Form 1040 line 1e is more than zero and is counted in this person's earned incom
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].dc_1e — This person's share of Form 1040 line 1e (taxable dependent care benefits) in Fo
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the per
Status: **AGREE**

Value: $22,057.91

### classm.person.7 — person[taxpayer].dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5,
Status: **AGREE**

Value: $22,057.91

### classm.person.7 — person[taxpayer].sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].sav_line1 — Form 8880 line 1 for this person (Roth IRA contributions for 2025)
Status: **AGREE**

Value: $6,564.00

### classm.person.7 — person[taxpayer].sav_w2 — Elective deferrals and designated Roth contributions for 2025 from this person's
Status: **AGREE**

Value: $1,208.00

### classm.person.7 — person[taxpayer].sav_excess_gate — Elective deferrals in box 12 over the limit for 2025
Status: **AGREE**

Value: no

### classm.person.7 — person[taxpayer].sav_simple_plan — This self-employed person's own SIMPLE IRA salary reduction contributions, by pl
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sav_simple — This person's own SIMPLE IRA salary reduction contributions as a self-employed p
Status: **AGREE**

Value: $0.00

### classm.person.7 — person[taxpayer].sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and 
Status: **AGREE**

Value: $1,208.00

## Raw responses

### classm.person.1

```yaml
```yaml
lines:
  - printed: "person[spouse].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses paid = $0.00"
  - printed: "person[spouse].educator_limited"
    value: "0.00"
    work: "smaller of $0.00 or $300"
  - printed: "person[spouse].educator_eligible_amount"
    value: "0.00"
    work: "Eligible educator, so the limited amount applies: $0.00"
  - printed: "person[spouse].educator_deduction"
    value: "0.00"
    work: "Educator expense deduction = $0.00"
  - printed: "person[spouse].hsa_forms"
    value: "0"
    work: "No Form 8889 entered for the spouse"
  - printed: "person[spouse].hsa_repeated"
    value: "no"
    work: "0 forms, which is not more than 1"
  - printed: "person[spouse].hsa_split"
    value: "0"
    work: "No Form 8889"
  - printed: "person[spouse].hsa_agreed"
    value: "0"
    work: "No Form 8889"
  - printed: "person[spouse].hsa_step1"
    value: "0.00"
    work: "No Form 8889"
  - printed: "person[spouse].hsa_share"
    value: "0.00"
    work: "No Form 8889"
  - printed: "person[spouse].hsa_deduction"
    value: "0.00"
    work: "No Form 8889, so line 13 = 0"
  - printed: "person[spouse].tip_employers"
    value: "0"
    work: "No tip employer entries"
  - printed: "person[spouse].tip_total"
    value: "0.00"
    work: "No entries"
  - printed: "person[spouse].tip_reported"
    value: "0.00"
    work: "No entries"
  - printed: "person[spouse].ot_employers"
    value: "1"
    work: "One overtime employer entry (ot_1)"
  - printed: "person[spouse].ot_total"
    value: "6220.00"
    work: "Column (b): $6,220.00"
  - printed: "person[spouse].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[spouse].se_rrta"
    value: "no"
    work: "No self-employment and no railroad retirement compensation"
  - printed: "person[spouse].employers"
    value: "2"
    work: "1 (emp_a) + 1 (emp_b)"
  - printed: "person[spouse].overcount"
    value: "0"
    work: "Neither employer withheld more than $10,918.20"
  - printed: "person[spouse].over"
    value: "no"
    work: "overcount = 0"
  - printed: "person[spouse].wages"
    value: "49960.00"
    work: "0 + 49,960"
  - printed: "person[spouse].withheld"
    value: "3098.00"
    work: "0 + 3,098"
  - printed: "person[spouse].box1"
    value: "49960.00"
    work: "0 + 49,960"
  - printed: "person[spouse].box2"
    value: "12990.00"
    work: "0 + 12,990"
  - printed: "person[spouse].eligible"
    value: "no"
    work: "Wages of $49,960 are not over $176,100"
  - printed: "person[spouse].excess"
    value: "0.00"
    work: "3,098 is not more than 10,918.20"
  - printed: "person[spouse].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[spouse].medicare5"
    value: "49960.00"
    work: "0 + 49,960"
  - printed: "person[spouse].medicare6"
    value: "724.00"
    work: "0 + 724"
  - printed: "person[spouse].sc_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[spouse].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[spouse].mq_q4"
    value: "0.00"
    work: "No property"
  - printed: "person[spouse].mq_total"
    value: "0.00"
    work: "No property"
  - printed: "person[spouse].cost179"
    value: "0.00"
    work: "No property"
  - printed: "person[spouse].s179_nonlisted"
    value: "0.00"
    work: "None"
  - printed: "person[spouse].s179_listed"
    value: "0.00"
    work: "None"
  - printed: "person[spouse].income179"
    value: "0.00"
    work: "No business"
  - printed: "person[spouse].has_sc"
    value: "no"
    work: "sc_count = 0"
  - printed: "person[spouse].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[spouse].se_screened"
    value: "no"
    work: "Screening answer = no"
  - printed: "person[spouse].se_line2"
    value: "0.00"
    work: "No Schedule C profit"
  - printed: "person[spouse].plan_screened"
    value: "no"
    work: "Screening answer = no; plan = none"
  - printed: "person[spouse].sep_rate_c"
    value: "0.11"
    work: "11% = 0.11"
  - printed: "person[spouse].sep_rate_plus"
    value: "1.11"
    work: "0.11 + 1"
  - printed: "person[spouse].sep_s1"
    value: "0.00"
    work: "Schedule C line 31 = 0"
  - printed: "person[spouse].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 = 0"
  - printed: "person[spouse].sep_s3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[spouse].sep_s5"
    value: "0.00"
    work: "0 x 0.099099"
  - printed: "person[spouse].sep_s6"
    value: "38500.00"
    work: "350,000 x 0.11"
  - printed: "person[spouse].sep_s7"
    value: "0.00"
    work: "smaller of 0 or 38,500"
  - printed: "person[spouse].sep_s21"
    value: "0.00"
    work: "smaller of 0 or 70,000"
  - printed: "person[spouse].sep_excess"
    value: "no"
    work: "SEP contributions of $0 are not more than $0"
  - printed: "person[spouse].sep_deduction"
    value: "0.00"
    work: "No contributions"
  - printed: "person[spouse].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 = 0"
  - printed: "person[spouse].simple_regular"
    value: "0.00"
    work: "Salary reduction contributions = 0"
  - printed: "person[spouse].simple_catchup"
    value: "0.00"
    work: "None above $16,500"
  - printed: "person[spouse].catchup_limit"
    value: "3500.00"
    work: "Age 50 catch-up limit for 2025"
  - printed: "person[spouse].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[spouse].catchup_max"
    value: "0.00"
    work: "lesser of 3,500 or 0"
  - printed: "person[spouse].match_3pct"
    value: "0.00"
    work: "3% x 0"
  - printed: "person[spouse].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[spouse].match_max"
    value: "0.00"
    work: "smaller of deferrals 0 or 3% 0"
  - printed: "person[spouse].ne_comp"
    value: "0.00"
    work: "smaller of 0 or 350,000"
  - printed: "person[spouse].ne_max"
    value: "0.00"
    work: "2% x 0"
  - printed: "person[spouse].employer_max"
    value: "0.00"
    work: "Nonelective formula: ne_max = 0"
  - printed: "person[spouse].simple_excess"
    value: "no"
    work: "All contributions are 0"
  - printed: "person[spouse].simple_deduction"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[spouse].plan_deduction"
    value: "0.00"
    work: "SEP 0 + SIMPLE 0"
  - printed: "person[spouse].s16"
    value: "0.00"
    work: "plan_deduction"
  - printed: "person[spouse].positive_profits"
    value: "0.00"
    work: "No businesses"
  - printed: "person[spouse].sehi"
    value: "0.00"
    work: "No self-employment"
  - printed: "person[spouse].qbi"
    value: "0.00"
    work: "No businesses"
  - printed: "person[spouse].eic_part1"
    value: "0.00"
    work: "SE line 3 of 0 - line 13 of 0"
  - printed: "person[spouse].files_se"
    value: "no"
    work: "Line 4c of $0 is less than $400"
  - printed: "person[spouse].eic_se_has"
    value: "0.00"
    work: "No self-employment"
  - printed: "person[spouse].eic_se"
    value: "0.00"
    work: "Part 1 0 + Part 2 0"
  - printed: "person[spouse].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[spouse].dc_benefits"
    value: "0.00"
    work: "Box 10 = 0"
  - printed: "person[spouse].dc_box10"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[spouse].dc_has_box10"
    value: "no"
    work: "Box 10 total = 0"
  - printed: "person[spouse].dc_1e_mine"
    value: "no"
    work: "No single person has box 10, so it goes to the taxpayer, not the spouse"
  - printed: "person[spouse].dc_1e_counted"
    value: "no"
    work: "Line 1e = 0, and it is not this person's"
  - printed: "person[spouse].dc_1e"
    value: "0.00"
    work: "Not counted"
  - printed: "person[spouse].dc_earned"
    value: "49960.00"
    work: "Box 1 49,960 + 1e 0 + SE 0"
  - printed: "person[spouse].dc_earned_b"
    value: "49960.00"
    work: "49,960 without line 1e"
  - printed: "person[spouse].sav_ineligible"
    value: "no"
    work: "Born before 1/2/2008, not a student, not a dependent"
  - printed: "person[spouse].sav_line1"
    value: "0.00"
    work: "No IRA, Roth or ABLE contributions"
  - printed: "person[spouse].sav_w2"
    value: "12940.00"
    work: "0 + 12,940"
  - printed: "person[spouse].sav_excess_gate"
    value: "no"
    work: "Answer = no"
  - printed: "person[spouse].sav_simple_plan"
    value: "0.00"
    work: "No self-employed SIMPLE plan"
  - printed: "person[spouse].sav_simple"
    value: "0.00"
    work: "None"
  - printed: "person[spouse].sav_line2"
    value: "12940.00"
    work: "12,940 + 0 voluntary + 0 SIMPLE"
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Expenses = $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "smaller of 0 or 300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 (hsa)"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 form, which is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Family coverage with separate HSAs = no"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Spouse rule not used"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Spouse rule not used"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 = $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "1"
    work: "One tip employer entry (tip_1)"
  - printed: "person[taxpayer].tip_total"
    value: "0.00"
    work: "Column (d) = 0"
  - printed: "person[taxpayer].tip_reported"
    value: "0.00"
    work: "Column (b) = 0"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No overtime entries"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "Neither applies"
  - printed: "person[taxpayer].employers"
    value: "2"
    work: "1 + 1"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "No employer withheld over the limit"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount = 0"
  - printed: "person[taxpayer].wages"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].withheld"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Wages of $0 are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "0 is not more than 10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[taxpayer].medicare5"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].medicare6"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "sc_count = 0"
  - printed: "person[taxpayer].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Screening answer = no"
  - printed: "person[taxpayer].se_line2"
    value: "0.00"
    work: "No Schedule C"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Screening answer = no; plan = none"
  - printed: "person[taxpayer].sep_rate_c"
    value: "0.20"
    work: "20% = 0.20"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.20"
    work: "0.20 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "Schedule C line 31 = 0"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "SE line 13 = 0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.166667"
  - printed: "person[taxpayer].sep_s6"
    value: "70000.00"
    work: "350,000 x 0.20"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "smaller of 0 or 70,000"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "smaller of 0 or 70,000"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "$0 contributions are not more than $0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "SE line 4 = 0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].catchup_limit"
    value: "3500.00"
    work: "Age 50 catch-up limit for 2025"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "lesser of 3,500 or 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "smaller of 0 or 0"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "smaller of 0 or 350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Match formula: match_max = 0"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "All contributions are 0"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "plan_deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No self-employment"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of $0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "No self-employment"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 = 0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 total = 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so it goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e = 0, which is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e = 0"
  - printed: "person[taxpayer].dc_earned"
    value: "0.00"
    work: "Box 1 0 + 1e 0 + SE 0"
  - printed: "person[taxpayer].dc_earned_b"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 1/2/2008, not a student, not a dependent"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "No IRA, Roth or ABLE contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Answer = no"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 + 0"
```
```

### classm.person.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "yes"
    work: "Qualified educator expenses $212.00 > 0"
  - printed: "person[taxpayer].educator_limited"
    value: "212.00"
    work: "Smaller of $212.00 or $300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Eligible amount is $0"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Not spouses with separate HSAs and family coverage; line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given Step 1 refigured line 5 = $0"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share = $0"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0"
  - printed: "person[taxpayer].tip_employers"
    value: "0"
    work: "No qualified tips reported"
  - printed: "person[taxpayer].tip_total"
    value: "0.00"
    work: "No tip entries"
  - printed: "person[taxpayer].tip_reported"
    value: "0.00"
    work: "No tip entries"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No qualified overtime reported"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "No overtime entries"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "Owner has no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "32540.00"
    work: "Social security wages plus tips, emp_a"
  - printed: "person[taxpayer].withheld"
    value: "2017.00"
    work: "Box 4, emp_a"
  - printed: "person[taxpayer].box1"
    value: "32540.00"
    work: "Box 1, emp_a"
  - printed: "person[taxpayer].box2"
    value: "8786.00"
    work: "Box 2, emp_a"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and $32,540 is not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$2,017 is not above $10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[taxpayer].medicare5"
    value: "32540.00"
    work: "Box 5, emp_a"
  - printed: "person[taxpayer].medicare6"
    value: "472.00"
    work: "Box 6, emp_a"
  - printed: "person[taxpayer].sc_count"
    value: "1"
    work: "One business (biz_a)"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No home-office deduction claimed"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "biz_a mq_q4 = $0"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "biz_a mq_total = $0"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "biz_a cost179 = $0"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "biz_a = $0"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "None entered"
  - printed: "person[taxpayer].income179"
    value: "41890.00"
    work: "biz_a line 31 without section 179"
  - printed: "person[taxpayer].has_sc"
    value: "yes"
    work: "sc_count = 1"
  - printed: "person[taxpayer].sc_total"
    value: "41890.00"
    work: "biz_a amount for Schedule 1 line 3"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Screening answer is no"
  - printed: "person[taxpayer].se_line2"
    value: "41890.00"
    work: "Schedule C line 31 total"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Not screened; one Schedule C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "0.05"
    work: "5% = 0.05"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.05"
    work: "0.05 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "41890.00"
    work: "Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "2959.44"
    work: "Schedule SE line 13 / Schedule 1 line 15"
  - printed: "person[taxpayer].sep_s3"
    value: "38930.56"
    work: "41,890.00 - 2,959.44"
  - printed: "person[taxpayer].sep_s5"
    value: "1853.83"
    work: "38,930.56 x 0.047619"
  - printed: "person[taxpayer].sep_s6"
    value: "17500.00"
    work: "350,000 x 5%"
  - printed: "person[taxpayer].sep_s7"
    value: "1853.83"
    work: "Smaller of 1,853.83 or 17,500"
  - printed: "person[taxpayer].sep_s21"
    value: "1853.83"
    work: "Smaller of step 7 or $70,000"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "SEP contributions of $0 do not exceed the maximum"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP contributions (plan is SIMPLE)"
  - printed: "person[taxpayer].simple_comp"
    value: "38685.42"
    work: "Schedule SE line 4c"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "None above $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "5250.00"
    work: "Age 60-63 limit"
  - printed: "person[taxpayer].comp_after_regular"
    value: "38685.42"
    work: "38,685.42 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "5250.00"
    work: "Lesser of 5,250 or 38,685.42"
  - printed: "person[taxpayer].match_3pct"
    value: "1160.56"
    work: "38,685.42 x 3%"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals 0 or 1,160.56"
  - printed: "person[taxpayer].ne_comp"
    value: "38685.42"
    work: "Not more than $350,000"
  - printed: "person[taxpayer].ne_max"
    value: "773.71"
    work: "38,685.42 x 2%"
  - printed: "person[taxpayer].employer_max"
    value: "773.71"
    work: "Nonelective formula"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "Employer $96 <= 773.71; deferrals 0"
  - printed: "person[taxpayer].simple_deduction"
    value: "96.00"
    work: "0 deferrals + 96 employer contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "96.00"
    work: "SEP 0 + SIMPLE 96"
  - printed: "person[taxpayer].s16"
    value: "96.00"
    work: "Plan deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "41890.00"
    work: "biz_a net profit"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "biz_a SEHI = $0"
  - printed: "person[taxpayer].qbi"
    value: "38834.56"
    work: "biz_a QBI"
  - printed: "person[taxpayer].eic_part1"
    value: "38930.56"
    work: "SE line 3 41,890.00 - line 13 2,959.44"
  - printed: "person[taxpayer].files_se"
    value: "yes"
    work: "Line 4c 38,685.42 >= 400"
  - printed: "person[taxpayer].eic_se_has"
    value: "38930.56"
    work: "Part 1 amount (files SE)"
  - printed: "person[taxpayer].eic_se"
    value: "38930.56"
    work: "Part 1 + Part 2 (0)"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedule 1-A tips or overtime"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 $0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total $0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person with box 10; taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e $0"
  - printed: "person[taxpayer].dc_earned"
    value: "71470.56"
    work: "32,540.00 + 0 + (41,890.00 - 2,959.44)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "71470.56"
    work: "Same, without line 1e (0)"
  - printed: "person[taxpayer].sav_ineligible"
    value: "yes"
    work: "Answered not born before Jan 2, 2008"
  - printed: "person[taxpayer].sav_line1"
    value: "6186.00"
    work: "Roth IRA contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "emp_a box 12 deferrals $0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Not over the limit"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "Own SIMPLE salary reduction $0"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "Own SIMPLE salary reduction $0"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 voluntary + 0 SIMPLE"
```
```

### classm.person.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses = $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Zero eligible amount, so no deduction"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 (hsa) entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "Only 1 form, not more than one"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Spouses with separate HSAs and family coverage = no, so the line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Spouse rule not used; given $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Spouse rule not used; given $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "tip_1 + tip_2 = 2 employers"
  - printed: "person[taxpayer].tip_total"
    value: "28523.00"
    work: "Column (d): 12,005.00 + 16,518.00"
  - printed: "person[taxpayer].tip_reported"
    value: "28523.00"
    work: "Column (b): 12,005.00 + 16,518.00"
  - printed: "person[taxpayer].ot_employers"
    value: "1"
    work: "One overtime employer entry (ot_1)"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "Column (b) total: $0.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No railroad retirement compensation and no Schedule C"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "0.00"
    work: "Social security wages and tips total $0.00"
  - printed: "person[taxpayer].withheld"
    value: "0.00"
    work: "Box 4 total $0.00"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "Box 1 total $0.00"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "Box 2 total $0.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages of $0 are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$0.00 withheld minus $10,918.20; zero or less, so 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no excess social security credit"
  - printed: "person[taxpayer].medicare5"
    value: "0.00"
    work: "Box 5 total $0.00"
  - printed: "person[taxpayer].medicare6"
    value: "0.00"
    work: "Box 6 total $0.00"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C entered"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No Schedule C property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No Schedule C property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "Schedule C count is 0"
  - printed: "person[taxpayer].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Self-employment screening answer = no"
  - printed: "person[taxpayer].se_line2"
    value: "0.00"
    work: "No Schedule C line 31 amounts"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Retirement screening answer = no, and not more than one Schedule C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "0.16"
    work: "Plan rate 16% = 0.16"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.16"
    work: "0.16 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "No Schedule C line 31 net profit"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 given as $0.00"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "Step 1 minus step 2: 0 - 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.137931"
  - printed: "person[taxpayer].sep_s6"
    value: "56000.00"
    work: "$350,000 x 16%"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0.00 or 56,000.00"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0.00) or $70,000"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "SEP contributions of $0 are not more than the $0 maximum"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "Smaller of $0 contributed or $0 maximum"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4c given as $0.00"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "Salary reduction contributions are $0"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "No contributions above the regular limit"
  - printed: "person[taxpayer].catchup_limit"
    value: "0.00"
    work: "Under age 50, so no catch-up limit"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of the $0 catch-up limit or $0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x $0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 regular + 0 catch-up"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals ($0) or 3% of compensation ($0)"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Smaller of $0 or $350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x $0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Match formula, so match_max of $0"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "SIMPLE contributions of $0 are within the limits"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "SEP plan; SEP deduction is $0"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "Plan deduction is $0"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No business profits"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No net profit from self-employment, so no deduction"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "Schedule SE line 3 (0) minus line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of $0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "No self-employment earned income"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "Parts 1 and 2 total $0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 of $0, less the part in box 1"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total $0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 total is $0"
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
    value: "0.00"
    work: "Box 1 (0) + line 1e (0) + SE (0)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "0.00"
    work: "Box 1 (0) + SE (0), without line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 1/2/2008, no one can claim as a dependent, and not a student"
  - printed: "person[taxpayer].sav_line1"
    value: "3366.00"
    work: "Roth IRA contributions $3,366.00; no traditional IRA or ABLE contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "W-2 box 12 deferrals total $0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Deferrals were not over the limit (answer = no)"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "SEP plan; SIMPLE salary reductions are $0"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "No own SIMPLE salary reduction contributions"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 voluntary + 0 SIMPLE"
```
```

### classm.person.4

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
    work: "No eligible amount"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "Only 1 form, not more than one"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Spouses with separate HSAs and family coverage = no, so the line 6 spouse rule is not used"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given Step 1 refigured line 5 = $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given Steps 2 and 3 share = $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Given HSA deduction (line 13) = $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "3"
    work: "tip_1, tip_2 and tip_3"
  - printed: "person[taxpayer].tip_total"
    value: "69863.00"
    work: "28,218 + 21,862 + 19,783 (column d)"
  - printed: "person[taxpayer].tip_reported"
    value: "69863.00"
    work: "28,218 + 21,862 + 19,783 (column b)"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No overtime entries"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "No overtime entries"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "Owner has no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "Count is 0"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "0.00"
    work: "Social security wages and tips = $0.00"
  - printed: "person[taxpayer].withheld"
    value: "0.00"
    work: "Box 4 = $0.00"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "Box 1 = $0.00"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "Box 2 = $0.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$0 withheld is not above $10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[taxpayer].medicare5"
    value: "0.00"
    work: "Box 5 = $0.00"
  - printed: "person[taxpayer].medicare6"
    value: "0.00"
    work: "Box 6 = $0.00"
  - printed: "person[taxpayer].sc_count"
    value: "1"
    work: "One business (biz_a)"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No home-office deduction claimed"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "biz_a mq_q4 = $0.00"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "biz_a mq_total = $0.00"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "biz_a cost179 = $0.00"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "biz_a section 179 on non-listed property = $0.00"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 property, so no listed-property amount"
  - printed: "person[taxpayer].income179"
    value: "43540.89"
    work: "biz_a line 31 without section 179"
  - printed: "person[taxpayer].has_sc"
    value: "yes"
    work: "sc_count is 1"
  - printed: "person[taxpayer].sc_total"
    value: "43540.89"
    work: "biz_a net profit"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "No screening condition applies to self-employment"
  - printed: "person[taxpayer].se_line2"
    value: "43540.89"
    work: "Schedule C line 31 goes to Schedule SE line 2"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Not screened, and only one Schedule C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "3.00"
    work: "Plan rate is 3%"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "103.00"
    work: "3 + 100"
  - printed: "person[taxpayer].sep_s1"
    value: "43540.89"
    work: "Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "3076.07"
    work: "Schedule SE line 13 (Schedule 1 line 15)"
  - printed: "person[taxpayer].sep_s3"
    value: "40464.82"
    work: "43,540.89 - 3,076.07"
  - printed: "person[taxpayer].sep_s5"
    value: "1178.58"
    work: "40,464.82 x 0.029126 (rate table for 3%)"
  - printed: "person[taxpayer].sep_s6"
    value: "10500.00"
    work: "350,000 x 3%"
  - printed: "person[taxpayer].sep_s7"
    value: "1178.58"
    work: "Smaller of step 5 or step 6"
  - printed: "person[taxpayer].sep_s21"
    value: "1178.58"
    work: "Smaller of step 7 or $70,000; no elective deferrals"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "$0 contributed is not more than the maximum"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No SEP contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "40210.01"
    work: "Schedule SE line 4c"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].catchup_limit"
    value: "0.00"
    work: "Under 50, so no catch-up allowed"
  - printed: "person[taxpayer].comp_after_regular"
    value: "40210.01"
    work: "40,210.01 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Smaller of $0 limit or 40,210.01"
  - printed: "person[taxpayer].match_3pct"
    value: "1206.30"
    work: "40,210.01 x 3%"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals $0 or the 3% amount"
  - printed: "person[taxpayer].ne_comp"
    value: "40210.01"
    work: "Not more than $350,000"
  - printed: "person[taxpayer].ne_max"
    value: "804.20"
    work: "40,210.01 x 2%"
  - printed: "person[taxpayer].employer_max"
    value: "804.20"
    work: "Plan uses the nonelective formula"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "$0 contributed"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No SIMPLE contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Retirement plan is none, and no contributions"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "Equals the plan deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "43540.89"
    work: "biz_a net profit"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "biz_a SEHI = $0.00"
  - printed: "person[taxpayer].qbi"
    value: "40464.82"
    work: "biz_a QBI"
  - printed: "person[taxpayer].eic_part1"
    value: "40464.82"
    work: "SE line 3 43,540.89 - line 13 3,076.07"
  - printed: "person[taxpayer].files_se"
    value: "yes"
    work: "Line 4c 40,210.01 is $400 or more"
  - printed: "person[taxpayer].eic_se_has"
    value: "40464.82"
    work: "Files Schedule SE, so Part 1 applies"
  - printed: "person[taxpayer].eic_se"
    value: "40464.82"
    work: "Part 1; Part 2 is not used"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedule 1-A tips or overtime on the Schedule C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 is $0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total is $0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is zero"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so line 1e is the taxpayer's"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is $0"
  - printed: "person[taxpayer].dc_earned"
    value: "40464.82"
    work: "Box 1 0 + 1e 0 + (43,540.89 - 3,076.07)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "40464.82"
    work: "Same as dc_earned without line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 1/2/2008; not claimed as a dependent; not a student"
  - printed: "person[taxpayer].sav_line1"
    value: "4059.00"
    work: "Roth IRA contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "W-2 box 12 deferrals = $0"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Filer answered no (not over the limit)"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "Plan is none, and no SIMPLE salary reductions"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 + 0 voluntary + 0 SIMPLE"
```

### classm.person.5

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
    work: "No eligible amount"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entry (hsa)"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Not spouses with separate HSAs treated as having family coverage; line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule does not apply, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Line 6 spouse rule does not apply, so the given Step 1 amount is not used"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "Two employer entries (tip_1, tip_2), one each"
  - printed: "person[taxpayer].tip_total"
    value: "14821.00"
    work: "Column (d): 14,821.00 + 0.00"
  - printed: "person[taxpayer].tip_reported"
    value: "14821.00"
    work: "Column (b): 14,821.00 + 0.00"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No overtime employer entries"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "No overtime entries"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No self-employment and no railroad retirement compensation"
  - printed: "person[taxpayer].employers"
    value: "2"
    work: "emp_a 1 + emp_b 1"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "Neither employer withheld more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "44754.00"
    work: "29,524.00 + 15,230.00"
  - printed: "person[taxpayer].withheld"
    value: "2775.00"
    work: "1,831.00 + 944.00"
  - printed: "person[taxpayer].box1"
    value: "29524.00"
    work: "29,524.00 + 0.00"
  - printed: "person[taxpayer].box2"
    value: "7676.00"
    work: "7,676.00 + 0.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Two employers, but $44,754 is not more than $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "$2,775 is not more than $10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no excess social security credit"
  - printed: "person[taxpayer].medicare5"
    value: "44754.00"
    work: "29,524.00 + 15,230.00"
  - printed: "person[taxpayer].medicare6"
    value: "649.00"
    work: "428.00 + 221.00"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No business property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No business property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "Schedule C count is 0"
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
    value: "0.16"
    work: "16% = 0.16"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.16"
    work: "0.16 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "No Schedule C line 31"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 is $0.00"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0.00 x 0.137931"
  - printed: "person[taxpayer].sep_s6"
    value: "56000.00"
    work: "350,000 x 0.16"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0.00 or 56,000.00"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0.00) or step 8 (70,000)"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "SEP contributions of $0 are not more than $0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No plan and no contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 is $0.00"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "None above $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "3500.00"
    work: "Catch-up eligibility given as age50: $3,500"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 3,500 or 0.00"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x 0.00"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals or 3% of compensation"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Smaller of 0.00 or 350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x 0.00"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Nonelective formula: ne_max"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "No contributions"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No plan and no contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Plan is none"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "No SEP or SIMPLE deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No self-employment"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No businesses"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "Schedule SE line 3 (0) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of $0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "No self-employment earned income"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "Parts 1 and 2 are both 0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 is 0 on both Forms W-2"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 total is 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so line 1e goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e is $0.00"
  - printed: "person[taxpayer].dc_earned"
    value: "29524.00"
    work: "Box 1 29,524 + line 1e 0 + SE 0"
  - printed: "person[taxpayer].dc_earned_b"
    value: "29524.00"
    work: "29,524 without dependent care benefits"
  - printed: "person[taxpayer].sav_ineligible"
    value: "yes"
    work: "Was a student in 2025"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "No traditional IRA, Roth IRA or ABLE contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Elective deferrals were not over the limit"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "Plan is none"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "No own SIMPLE salary reduction contributions"
  - printed: "person[taxpayer].sav_line2"
    value: "0.00"
    work: "0 (box 12) + 0 (voluntary) + 0 (SIMPLE)"
```
```

### classm.person.6

```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses = $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300 = 0"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Eligible educator = yes; amount up to $300 = 0"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Schedule 1 line 11: up to $300 of qualified expenses = 0"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Not spouses with separate HSAs and family coverage, so the line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Spouse rule not used; given refigured line 5 = 0"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Spouse rule not used; given share = 0"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 as given = 0"
  - printed: "person[taxpayer].tip_employers"
    value: "0"
    work: "No employers with qualified tips were entered"
  - printed: "person[taxpayer].tip_total"
    value: "0.00"
    work: "No tip worksheet rows; column (d) total = 0"
  - printed: "person[taxpayer].tip_reported"
    value: "0.00"
    work: "No tip worksheet rows; column (b) total = 0"
  - printed: "person[taxpayer].ot_employers"
    value: "2"
    work: "Overtime entries ot_1 and ot_2"
  - printed: "person[taxpayer].ot_total"
    value: "68151.00"
    work: "39,445.00 + 28,706.00"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "No Schedules C and no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No railroad retirement compensation and no self-employment"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount = 0"
  - printed: "person[taxpayer].wages"
    value: "155611.00"
    work: "Social security wages plus tips, emp_a"
  - printed: "person[taxpayer].withheld"
    value: "9648.00"
    work: "W-2 box 4, emp_a"
  - printed: "person[taxpayer].box1"
    value: "155611.00"
    work: "W-2 box 1, emp_a"
  - printed: "person[taxpayer].box2"
    value: "45127.00"
    work: "W-2 box 2, emp_a"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and 155,611 is not over 176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "9,648.00 is not more than 10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible (Schedule 3 line 11 test fails)"
  - printed: "person[taxpayer].medicare5"
    value: "155611.00"
    work: "W-2 box 5, emp_a"
  - printed: "person[taxpayer].medicare6"
    value: "2256.00"
    work: "W-2 box 6, emp_a"
  - printed: "person[taxpayer].sc_count"
    value: "0"
    work: "No Schedules C entered"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "No Schedule C property"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "No Schedule C property"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "No section 179 property"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].income179"
    value: "0.00"
    work: "No business income"
  - printed: "person[taxpayer].has_sc"
    value: "no"
    work: "sc_count = 0"
  - printed: "person[taxpayer].sc_total"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "Answered no to the self-employment screens"
  - printed: "person[taxpayer].se_line2"
    value: "0.00"
    work: "Schedule SE line 2 = Schedule C line 31 total = 0"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Answered no to the retirement screens; no Schedules C"
  - printed: "person[taxpayer].sep_rate_c"
    value: "0.04"
    work: "4% = 0.04"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.04"
    work: "0.04 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "Schedule C line 31 = 0"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule 1 line 15 = Schedule SE line 13 = 0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.038462"
  - printed: "person[taxpayer].sep_s6"
    value: "14000.00"
    work: "350,000 x 4%"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 or 14,000"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of step 7 (0) or $70,000"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "SEP contributions of 0 are not more than 0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "Smaller of contributions (0) or maximum (0)"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "Schedule SE line 4 (4c) = 0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "Salary reduction contributions of 0, up to $16,500"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "0 above $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "3500.00"
    work: "Age 50 catch-up limit for 2025"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 3,500 or 0"
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
    work: "Matching formula, so match_max = 0"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "Contributions of 0 do not exceed the limits"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Plan = none; SEP 0 + SIMPLE 0"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "Equals plan_deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "No Schedules C"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "No net profit, so Form 7206 line 13 = 0"
  - printed: "person[taxpayer].qbi"
    value: "0.00"
    work: "No business income; wages are not QBI"
  - printed: "person[taxpayer].eic_part1"
    value: "0.00"
    work: "Schedule SE line 3 (0) - line 13 (0)"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c of 0 is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "0.00"
    work: "Not filing Schedule SE; Part 2 Schedule C = 0"
  - printed: "person[taxpayer].eic_se"
    value: "0.00"
    work: "Part 1 0 + Part 2 0"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "No Schedules C"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 = 0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "emp_a box 10 = 0"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 total = 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single person has box 10, so line 1e goes to the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than zero"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e = 0"
  - printed: "person[taxpayer].dc_earned"
    value: "155611.00"
    work: "Box 1 155,611 + line 1e 0 + SE 0"
  - printed: "person[taxpayer].dc_earned_b"
    value: "155611.00"
    work: "155,611 without line 1e"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 1/2/2008, not a dependent, not a student"
  - printed: "person[taxpayer].sav_line1"
    value: "0.00"
    work: "Roth 0; no traditional IRA or ABLE contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "8174.00"
    work: "emp_a box 12 deferrals"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Answered no to over the limit"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "Plan = none; own SIMPLE salary reduction = 0"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "Total of 0"
  - printed: "person[taxpayer].sav_line2"
    value: "8174.00"
    work: "8,174 + voluntary 0 + SIMPLE 0"
```

### classm.person.7

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses are $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0 or $300"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so 0"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "No eligible amount"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Not spouses with separate HSAs and family coverage"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Given refigured line 5 = 0; rule does not apply"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Given share = 0"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as $0"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "Two tip employer entries (tip_1, tip_2), each = 1"
  - printed: "person[taxpayer].tip_total"
    value: "637.00"
    work: "Column (d): 0 + 637"
  - printed: "person[taxpayer].tip_reported"
    value: "637.00"
    work: "Column (b): 0 + 637"
  - printed: "person[taxpayer].ot_employers"
    value: "1"
    work: "One overtime employer entry"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "Column (b) = 0"
  - printed: "person[taxpayer].sc_rrta_count"
    value: "0"
    work: "Owner has no railroad retirement compensation"
  - printed: "person[taxpayer].se_rrta"
    value: "no"
    work: "No RRTA compensation"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount = 0"
  - printed: "person[taxpayer].wages"
    value: "121779.00"
    work: "Social security wages plus tips, one W-2"
  - printed: "person[taxpayer].withheld"
    value: "7550.00"
    work: "Box 4 total"
  - printed: "person[taxpayer].box1"
    value: "121779.00"
    work: "Box 1 total"
  - printed: "person[taxpayer].box2"
    value: "26791.00"
    work: "Box 2 total"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer; wages not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "7,550 is not above 10,918.20"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[taxpayer].medicare5"
    value: "121779.00"
    work: "Box 5 total"
  - printed: "person[taxpayer].medicare6"
    value: "1766.00"
    work: "Box 6 total"
  - printed: "person[taxpayer].sc_count"
    value: "2"
    work: "biz_a and biz_b"
  - printed: "person[taxpayer].ho_count"
    value: "0"
    work: "Neither business claims home use"
  - printed: "person[taxpayer].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].s179_nonlisted"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].s179_listed"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].income179"
    value: "-99721.09"
    work: "-24,794.00 + -74,927.09"
  - printed: "person[taxpayer].has_sc"
    value: "yes"
    work: "sc_count = 2"
  - printed: "person[taxpayer].sc_total"
    value: "-99721.09"
    work: "-24,794.00 + -74,927.09"
  - printed: "person[taxpayer].se_screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].se_line2"
    value: "-99721.09"
    work: "Schedule C line 31 total"
  - printed: "person[taxpayer].plan_screened"
    value: "no"
    work: "Not screened; plan is none"
  - printed: "person[taxpayer].sep_rate_c"
    value: "0.21"
    work: "21% = 0.21"
  - printed: "person[taxpayer].sep_rate_plus"
    value: "1.21"
    work: "0.21 + 1"
  - printed: "person[taxpayer].sep_s1"
    value: "-99721.09"
    work: "Schedule C line 31 total"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule 1 line 15 = SE line 13 = 0"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "-99,721.09 - 0, not below 0"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0 x 0.173554"
  - printed: "person[taxpayer].sep_s6"
    value: "73500.00"
    work: "350,000 x 0.21"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of 0 or 73,500"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "Smaller of 0 or 70,000"
  - printed: "person[taxpayer].sep_excess"
    value: "no"
    work: "Contributions of 0 are not more than 0"
  - printed: "person[taxpayer].sep_deduction"
    value: "0.00"
    work: "No contributions"
  - printed: "person[taxpayer].simple_comp"
    value: "0.00"
    work: "SE line 4 is negative, so 0"
  - printed: "person[taxpayer].simple_regular"
    value: "0.00"
    work: "No salary reduction contributions"
  - printed: "person[taxpayer].simple_catchup"
    value: "0.00"
    work: "None over $16,500"
  - printed: "person[taxpayer].catchup_limit"
    value: "3500.00"
    work: "age50 catch-up limit"
  - printed: "person[taxpayer].comp_after_regular"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].catchup_max"
    value: "0.00"
    work: "Lesser of 3,500 or 0"
  - printed: "person[taxpayer].match_3pct"
    value: "0.00"
    work: "3% x 0"
  - printed: "person[taxpayer].deferrals_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].match_max"
    value: "0.00"
    work: "Smaller of deferrals 0 or 3% 0"
  - printed: "person[taxpayer].ne_comp"
    value: "0.00"
    work: "Smaller of 0 or 350,000"
  - printed: "person[taxpayer].ne_max"
    value: "0.00"
    work: "2% x 0"
  - printed: "person[taxpayer].employer_max"
    value: "0.00"
    work: "Match formula: match_max"
  - printed: "person[taxpayer].simple_excess"
    value: "no"
    work: "All contributions are 0"
  - printed: "person[taxpayer].simple_deduction"
    value: "0.00"
    work: "No contributions"
  - printed: "person[taxpayer].plan_deduction"
    value: "0.00"
    work: "Plan none; 0"
  - printed: "person[taxpayer].s16"
    value: "0.00"
    work: "plan_deduction"
  - printed: "person[taxpayer].positive_profits"
    value: "0.00"
    work: "Both businesses had losses"
  - printed: "person[taxpayer].sehi"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].qbi"
    value: "-99721.09"
    work: "-24,794.00 + -74,927.09"
  - printed: "person[taxpayer].eic_part1"
    value: "-99721.09"
    work: "SE line 3 -99,721.09 - line 13 0"
  - printed: "person[taxpayer].files_se"
    value: "no"
    work: "Line 4c = 0, which is less than $400"
  - printed: "person[taxpayer].eic_se_has"
    value: "-99721.09"
    work: "Part 2: Schedule C line 31 total"
  - printed: "person[taxpayer].eic_se"
    value: "-99721.09"
    work: "No Schedule SE, so use Part 2"
  - printed: "person[taxpayer].sc_1a"
    value: "0"
    work: "Neither business has Schedule 1-A tips or overtime"
  - printed: "person[taxpayer].dc_benefits"
    value: "0.00"
    work: "Box 10 is 0"
  - printed: "person[taxpayer].dc_box10"
    value: "0.00"
    work: "Box 10 total"
  - printed: "person[taxpayer].dc_has_box10"
    value: "no"
    work: "Box 10 is 0"
  - printed: "person[taxpayer].dc_1e_mine"
    value: "yes"
    work: "No single box-10 person, so the taxpayer"
  - printed: "person[taxpayer].dc_1e_counted"
    value: "no"
    work: "Line 1e is not more than 0"
  - printed: "person[taxpayer].dc_1e"
    value: "0.00"
    work: "Line 1e = 0"
  - printed: "person[taxpayer].dc_earned"
    value: "22057.91"
    work: "121,779 + 0 + (-99,721.09 - 0)"
  - printed: "person[taxpayer].dc_earned_b"
    value: "22057.91"
    work: "121,779 + (-99,721.09)"
  - printed: "person[taxpayer].sav_ineligible"
    value: "no"
    work: "Born before 2008, not a student, not a dependent"
  - printed: "person[taxpayer].sav_line1"
    value: "6564.00"
    work: "Roth IRA contributions"
  - printed: "person[taxpayer].sav_w2"
    value: "1208.00"
    work: "W-2 box 12 deferrals"
  - printed: "person[taxpayer].sav_excess_gate"
    value: "no"
    work: "Not over the limit"
  - printed: "person[taxpayer].sav_simple_plan"
    value: "0.00"
    work: "Plan none; 0"
  - printed: "person[taxpayer].sav_simple"
    value: "0.00"
    work: "No own SIMPLE salary reduction contributions"
  - printed: "person[taxpayer].sav_line2"
    value: "1208.00"
    work: "1,208 + 0 voluntary + 0 SIMPLE"
```
```
