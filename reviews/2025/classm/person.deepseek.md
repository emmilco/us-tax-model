# Class M hand-work — person

`Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f6c77cc67cd485a68ed4f671bca12db77593e7147f482a6120542683405cf654 |
| cases | 1 |
| worked target scope | printed IRS lines |

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
| i8863 | 2025 | 1, 2, 3, 4, 7, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 7, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### case classm.person.1 — prompt sha256 e6f0e2997bc356343c83413d58766d7cf219461e3e93e04c4a5df922d0dd46a1; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eic_ssn:true, person.under16:false, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.se_rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1, person.has_sc:false, person.se_screen:false, person.se_screened:false, person.se_line6#1, person.se_line12#1, person.se_line13#1, person.se_line4c#1, person.plan_screen:false, person.plan_screened:false, person.sep_s3:floor, person.sep_s7:left, person.sep_s21:left, person.sep_excess:false, person.simple_regular:left, person.simple_catchup:floor, person.comp_after_regular:floor, person.catchup_max:left, person.match_max:left, person.ne_comp:left, person.employer_max#1, person.simple_excess:false, person.plan_deduction#1, person.s16#1, person.files_se:false, person.eic_se_has#1, person.eic_se#1, person.dc_has_box10:false, person.dc_1e_mine:true, person.dc_1e_counted:false, person.dc_1e#1, person.sav_born:true, person.sav_student:true, person.sav_claimed:false, person.sav_ineligible:true, person.sav_trad:false, person.sav_able:false, person.sav_excess:false, person.sav_excess_gate:false, person.sav_simple_plan#1, person.sav_simple#1, person.ira_contrib#1, person.ira_has:false, person.ira_any_contrib:false, person.ira_excess:false, person.ira_excess_gate:false, person.ira_age50:false, person.ira_work_plan:false, person.ira_se_plan:false, person.ira_cov:false, person.ira_limit#1, person.ira_not_covered_joint:false, person.ira_line2#1, person.ira_line6:positive, person.ira_line6_yes:true, person.ira_wide:true, person.ira_full#0, person.ira_at_full:true, person.ira_prod_wide#1, person.ira_prod_joint#1, person.ira_prod#0, person.ira_floor:left, person.ira_below#0, person.ira_line7_figured#0, person.ira_line7#1, person.ira_over_limit:false, person.ira_7or10:left, person.ira_line12:right, person.ira_deduction#1, person.ira_10or11:right, person.ira_nd_figured:floor, person.ira_nondeductible#1, person.ira_files_8606:false, person.ira_basis_adjusted:false, person.ira_basis_gate:false, person.ira_8606_line2#1, person.ira_dist:false, person.ira_dist_gate:false, person.ira_ssb_lim:left, person.ira_ssb_figured:right, person.ira_ssb#1, person.ira_se_figured:floor, person.ira_se#1, person.edu:false, person.edu_1098t:false, person.edu_student:false, person.edu_adj#1, person.edu_over:false, person.edu_over_refused:false, person.edu_line23:false, person.edu_show24:false, person.edu_line24:false, person.edu_show25:false, person.edu_line25:false, person.edu_show26:false, person.edu_line26:false, person.edu_ein:false, person.edu_aoc:false, person.edu_llc:false, person.edu_line27#1, person.edu_line28#1, person.edu_line29#1, person.edu_line30#1, person.edu_line31#1, person.edu_born_2007:true, person.edu_born_2002:true, person.edu_fulltime:true, person.edu_half_support:true, person.edu_parent:true, person.edu_kid:false

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
Status: **DISAGREE**

Project: $44,754.00
Model: $29,524.00
Work: 29,524.00 + 0.00 = 29,524.00

Ruling: model error; iw2w3 p. 18, boxes 3 and 7 (social security wages and social security tips; amb.2025.ss_wages): person.wages is the sum of w2.wages, boxes 3 plus 7, the amount the excess social security tax test compares with the wage base (i1040gi p. 117, Line 11). Case inputs (fixtures/2025/classm.deepseek.json, classm.person.1.deepseek): emp_a box 1 $29,524.00, box 3 $29,524.00, box 7 $0.00; emp_b box 1 $0.00, box 3 $0.00, box 7 $15,230.00; so boxes 3 plus 7 total $44,754.00, the project's value. The model's work ("29,524.00 + 0.00 = 29,524.00") adds emp_a's amount and emp_b's box 3 (or box 1) and misses emp_b's box 7 tips of $15,230.00. Same case and ruling as round 2. A wrong worked value is not evidence; dropped. [dropped]

### classm.person.1 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $2,775.00

### classm.person.1 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

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

Value: $52,500.00

### classm.person.1 — person[taxpayer].sep_s7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

Value: $0.00

### classm.person.1 — person[taxpayer].sep_s21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective de
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.person.1

```yaml
lines:
  - printed: "person[taxpayer].employers"
    value: "2"
    work: "w2.one: emp_a = 1 plus emp_b = 1 gives 2 employers"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "Both employers answered no to withholding more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "No employer withheld more than $10,918.20"
  - printed: "person[taxpayer].wages"
    value: "29524.00"
    work: "29,524.00 + 0.00 = 29,524.00"
  - printed: "person[taxpayer].withheld"
    value: "2775.00"
    work: "1,831.00 + 944.00 = 2,775.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "2 employers, but total SS wages 29,524 + 15,230 = 44,754 <= 176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "Total withheld 2,775.00 is not above 10,918.20; excess = 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "No excess SS tax because wages <= 176,100 and no employer over-withheld; credit = 0"
  - printed: "person[taxpayer].sep_s1"
    value: "0.00"
    work: "No Schedule C net profit supplied; Schedule SE line 4c is 0"
  - printed: "person[taxpayer].sep_s2"
    value: "0.00"
    work: "Schedule SE line 13 deduction for one-half SE tax = 0.00"
  - printed: "person[taxpayer].sep_s3"
    value: "0.00"
    work: "Step 1 0.00 - step 2 0.00 = 0.00"
  - printed: "person[taxpayer].sep_s5"
    value: "0.00"
    work: "0.00 x 0.130435 (15% / 115%) = 0.00"
  - printed: "person[taxpayer].sep_s6"
    value: "52500.00"
    work: "350,000 x 15% = 52,500.00"
  - printed: "person[taxpayer].sep_s7"
    value: "0.00"
    work: "Smaller of step 5 0.00 or step 6 52,500.00 = 0.00"
  - printed: "person[taxpayer].sep_s21"
    value: "0.00"
    work: "No elective deferrals; smaller of step 7 0.00 or step 8 70,000 = 0.00"
```
