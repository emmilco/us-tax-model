# Class M hand-work — person

`Excess Social Security credit — separately per person` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 41, 93, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 41, 93, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### case classm.person.1 — prompt sha256 90f96867990fb15b2342a51c352dd8bf68e53bd19a18c9b290cf601bb349eb29; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.eligible_educator:true, person.born_before_2001:true, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#0, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.over:false, person.eligible:false, person.eligible:true, person.excess:floor, person.excess:positive, person.credit#0, person.credit#1

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

Value: 0

### classm.person.1 — person[spouse].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

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

Value: $352,200.00

### classm.person.1 — person[spouse].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $21,836.00

### classm.person.1 — person[spouse].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $510,365.00

### classm.person.1 — person[spouse].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $81,866.00

### classm.person.1 — person[spouse].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: yes

### classm.person.1 — person[spouse].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $10,917.80

### classm.person.1 — person[spouse].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $10,917.80

### classm.person.1 — person[spouse].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $510,365.00

### classm.person.1 — person[spouse].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $8,393.00

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

Value: $17,821.00

### classm.person.1 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $17,821.00

### classm.person.1 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

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

### case classm.person.2 — prompt sha256 40bd83ec9253baa1ca300c1d4acf5228c60cde282ab8a23fbbb21295f457621c; branches: person.age65:true, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:true, person.born_after_1960:false, person.died_before_65:false, person.has_educator_expenses:true, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#0, person.hsa_repeated:false, person.rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1

### classm.person.2 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: yes

### classm.person.2 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $32.00

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

Value: 1

### classm.person.2 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 2

### classm.person.2 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $13,333.33

### classm.person.2 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 2

### classm.person.2 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $47,075.00

### classm.person.2 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $2,919.00

### classm.person.2 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $47,075.00

### classm.person.2 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $7,733.00

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

Value: $47,075.00

### classm.person.2 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $683.00

### case classm.person.3 — prompt sha256 1310bc8a038f4d366a7d3ce174e2b6b47a924f105892bb575eb7b315c086671c; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:true, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:true, person.educator_limited:right, person.educator_eligible_amount#1, person.educator_deduction#0, person.hsa_repeated:false, person.rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1

### classm.person.3 — person[taxpayer].has_educator_expenses — Any qualified educator expenses for this person
Status: **AGREE**

Value: yes

### classm.person.3 — person[taxpayer].educator_limited — This person's qualified educator expenses, up to $300
Status: **AGREE**

Value: $300.00

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
Status: **DISAGREE**

Project: 3
Model: 2
Work: tip_2 ($29,213) and tip_3 ($1,395) paid qualified tips; tip_1 paid $0

Ruling: representation; project retained; model value dropped from the fixture. The project counts each employer entered on the tip roster ('List stable keys for each employer from which you received tips'), the model only those with an amount above zero. An entry of $0 changes no amount: line 4c totals the worksheet's column (d), and with two or more employers line 4a is $0 either way (i1040gi p. 104). [dropped]

### classm.person.3 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $30,608.00

### classm.person.3 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $30,608.00

### classm.person.3 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 0

### classm.person.3 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $0.00

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

Value: $17,031.00

### classm.person.3 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $1,056.00

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

Value: $17,031.00

### classm.person.3 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $247.00

### case classm.person.4 — prompt sha256 d6bf1537d154e7a4e642f017a798b57ceb9e02bfa24002fd5913493b3816bad9; branches: person.age65:false, person.blind:false, person.tin:true, person.itin_applied:false, person.work_ssn:false, person.eligible_educator:false, person.born_before_2001:false, person.born_after_1960:true, person.died_before_65:false, person.has_educator_expenses:false, person.educator_limited:left, person.educator_eligible_amount#1, person.educator_deduction#1, person.hsa_repeated:false, person.rrta:false, person.over:false, person.eligible:false, person.excess:floor, person.credit#1

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
Status: **DISAGREE**

Project: 3
Model: 2
Work: tip_1 and tip_3 paid qualified tips; tip_2 paid $0

Ruling: representation; project retained; model value dropped from the fixture. The project counts each employer entered on the tip roster ('List stable keys for each employer from which you received tips'), the model only those with an amount above zero. An entry of $0 changes no amount: line 4c totals the worksheet's column (d), and with two or more employers line 4a is $0 either way (i1040gi p. 104). [dropped]

### classm.person.4 — person[taxpayer].tip_total — This person's worksheet column (d) total
Status: **AGREE**

Value: $31,731.00

### classm.person.4 — person[taxpayer].tip_reported — This person's worksheet column (b) total
Status: **AGREE**

Value: $31,731.00

### classm.person.4 — person[taxpayer].ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

Value: 2

### classm.person.4 — person[taxpayer].ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

Value: $73,571.00

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

Value: $137,935.00

### classm.person.4 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $8,552.00

### classm.person.4 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $119,941.00

### classm.person.4 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $21,589.00

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

Value: $137,935.00

### classm.person.4 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $2,000.00

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
    work: "Smaller of $0.00 or $300 = $0.00"
  - printed: "person[spouse].educator_eligible_amount"
    value: "0.00"
    work: "Eligible educator = yes; limited amount = $0.00"
  - printed: "person[spouse].educator_deduction"
    value: "0.00"
    work: "Line 11 educator deduction = $0.00"
  - printed: "person[spouse].hsa_forms"
    value: "0"
    work: "No Form 8889 entries for the spouse"
  - printed: "person[spouse].hsa_repeated"
    value: "no"
    work: "0 forms is not more than 1"
  - printed: "person[spouse].hsa_split"
    value: "0"
    work: "No Form 8889 for the spouse"
  - printed: "person[spouse].hsa_agreed"
    value: "0"
    work: "No Form 8889 for the spouse"
  - printed: "person[spouse].hsa_step1"
    value: "0.00"
    work: "No Form 8889 for the spouse"
  - printed: "person[spouse].hsa_share"
    value: "0.00"
    work: "No Form 8889 for the spouse"
  - printed: "person[spouse].hsa_deduction"
    value: "0.00"
    work: "No Form 8889 for the spouse; line 13 = $0.00"
  - printed: "person[spouse].tip_employers"
    value: "0"
    work: "No tip job entries for the spouse"
  - printed: "person[spouse].tip_total"
    value: "0.00"
    work: "No column (d) amounts"
  - printed: "person[spouse].tip_reported"
    value: "0.00"
    work: "No column (b) amounts"
  - printed: "person[spouse].ot_employers"
    value: "0"
    work: "No overtime entries"
  - printed: "person[spouse].ot_total"
    value: "0.00"
    work: "No overtime entries"
  - printed: "person[spouse].employers"
    value: "2"
    work: "emp_a 1 + emp_b 1 = 2"
  - printed: "person[spouse].overcount"
    value: "0"
    work: "Neither employer withheld more than $10,918.20"
  - printed: "person[spouse].over"
    value: "no"
    work: "Overcount = 0"
  - printed: "person[spouse].wages"
    value: "352200.00"
    work: "176,100 + 176,100 = 352,200"
  - printed: "person[spouse].withheld"
    value: "21836.00"
    work: "10,918 + 10,918 = 21,836"
  - printed: "person[spouse].box1"
    value: "510365.00"
    work: "245,667 + 264,698 = 510,365"
  - printed: "person[spouse].box2"
    value: "81866.00"
    work: "2,457 + 79,409 = 81,866"
  - printed: "person[spouse].eligible"
    value: "yes"
    work: "2 employers and 352,200 > 176,100"
  - printed: "person[spouse].excess"
    value: "10917.80"
    work: "21,836.00 - 10,918.20 = 10,917.80"
  - printed: "person[spouse].credit"
    value: "10917.80"
    work: "Eligible, and no single employer over the limit; credit = excess"
  - printed: "person[spouse].medicare5"
    value: "510365.00"
    work: "245,667 + 264,698 = 510,365"
  - printed: "person[spouse].medicare6"
    value: "8393.00"
    work: "3,973 + 4,420 = 8,393"
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses paid = $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300 = $0.00"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so $0"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Line 11 educator deduction = $0.00"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 (hsa) = 1"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 form is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Spouses with separate HSAs and family coverage = no; line 6 spouse rule not used"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used; allocation is equal"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Step 1 refigured line 5 = $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Steps 2-3 share = $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 = $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "1"
    work: "One tip employer (tip_1)"
  - printed: "person[taxpayer].tip_total"
    value: "17821.00"
    work: "Column (d) total = 17,821"
  - printed: "person[taxpayer].tip_reported"
    value: "17821.00"
    work: "Column (b) total = 17,821"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No overtime entries"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "No overtime entries"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "emp_a 1"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "Employer did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount = 0"
  - printed: "person[taxpayer].wages"
    value: "0.00"
    work: "Social security wages and tips = 0"
  - printed: "person[taxpayer].withheld"
    value: "0.00"
    work: "Box 4 = 0"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "Box 1 = 0"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "Box 2 = 0"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only 1 employer, and wages of 0 are not over 176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "0 - 10,918.20 is less than zero, so 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible"
  - printed: "person[taxpayer].medicare5"
    value: "0.00"
    work: "Box 5 = 0"
  - printed: "person[taxpayer].medicare6"
    value: "0.00"
    work: "Box 6 = 0"
```
```

### classm.person.2

```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "yes"
    work: "Qualified educator expenses are $32.00, which is more than zero"
  - printed: "person[taxpayer].educator_limited"
    value: "32.00"
    work: "Smaller of $32.00 or the $300 cap = 32.00"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator (K-12, 900 hours), so 0"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Line 11 deduction is allowed only for an eligible educator, so 0"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entry (hsa)"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Separate HSAs with family coverage = no, so the line 6 spouse rule does not apply"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "The spouse rule does not apply, and the allocation is equal anyway"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Refigured line 5 given as 0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Steps 2-3 share given as 0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 given as 0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "1"
    work: "One tip employer entry (tip_1)"
  - printed: "person[taxpayer].tip_total"
    value: "0.00"
    work: "Column (d) total = 0.00"
  - printed: "person[taxpayer].tip_reported"
    value: "0.00"
    work: "Column (b) total = 0.00"
  - printed: "person[taxpayer].ot_employers"
    value: "2"
    work: "Two overtime employer entries (ot_1, ot_2)"
  - printed: "person[taxpayer].ot_total"
    value: "13333.33"
    work: "0.00 + 13,333.33 = 13,333.33"
  - printed: "person[taxpayer].employers"
    value: "2"
    work: "W-2 entries emp_a + emp_b = 2"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "Neither employer withheld more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "Overcount is 0"
  - printed: "person[taxpayer].wages"
    value: "47075.00"
    work: "19,034.00 + 28,041.00 = 47,075.00"
  - printed: "person[taxpayer].withheld"
    value: "2919.00"
    work: "1,180.00 + 1,739.00 = 2,919.00"
  - printed: "person[taxpayer].box1"
    value: "47075.00"
    work: "19,034.00 + 28,041.00 = 47,075.00"
  - printed: "person[taxpayer].box2"
    value: "7733.00"
    work: "3,807.00 + 3,926.00 = 7,733.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "There are 2 employers, but 47,075.00 is not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "2,919.00 is not above 10,918.20, so 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no excess social security credit"
  - printed: "person[taxpayer].medicare5"
    value: "47075.00"
    work: "19,034.00 + 28,041.00 = 47,075.00"
  - printed: "person[taxpayer].medicare6"
    value: "683.00"
    work: "276.00 + 407.00 = 683.00"
```

### classm.person.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "yes"
    work: "Qualified educator expenses of $511.00 are more than zero"
  - printed: "person[taxpayer].educator_limited"
    value: "300.00"
    work: "Smaller of $511.00 or the $300 limit"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator in 2025, so zero"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Line 11 allows the deduction only to an eligible educator; the filer answered no"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entry (hsa)"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "Only 1 Form 8889, which is not more than one"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Line 6 spouse rule does not apply: no spouses with separate HSAs and family coverage"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Line 6 spouse rule does not apply, so there is no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Refigured line 5 given as $0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Your part of the Step 1 limit given as $0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "HSA deduction (line 13) given as $0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "tip_2 ($29,213) and tip_3 ($1,395) paid qualified tips; tip_1 paid $0"
  - printed: "person[taxpayer].tip_total"
    value: "30608.00"
    work: "Column (d): 0 + 29,213 + 1,395 = 30,608"
  - printed: "person[taxpayer].tip_reported"
    value: "30608.00"
    work: "Column (b): 0 + 29,213 + 1,395 = 30,608"
  - printed: "person[taxpayer].ot_employers"
    value: "0"
    work: "No overtime employer entries"
  - printed: "person[taxpayer].ot_total"
    value: "0.00"
    work: "No overtime entries, so column (b) total is 0"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "No employer withheld more than $10,918.20"
  - printed: "person[taxpayer].wages"
    value: "17031.00"
    work: "Social security wages and tips, emp_a: 17,031"
  - printed: "person[taxpayer].withheld"
    value: "1056.00"
    work: "Box 4, emp_a: 1,056"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "Box 1, emp_a: 0"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "Box 2, emp_a: 0"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only 1 employer and wages of 17,031 are not over $176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "1,056 - 10,918.20 is less than zero, so 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible (needs more than one employer and wages over $176,100), so no credit"
  - printed: "person[taxpayer].medicare5"
    value: "17031.00"
    work: "Box 5, emp_a: 17,031"
  - printed: "person[taxpayer].medicare6"
    value: "247.00"
    work: "Box 6, emp_a: 247"
```
```

### classm.person.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].has_educator_expenses"
    value: "no"
    work: "Qualified educator expenses paid = $0.00"
  - printed: "person[taxpayer].educator_limited"
    value: "0.00"
    work: "Smaller of $0.00 or $300 = 0.00"
  - printed: "person[taxpayer].educator_eligible_amount"
    value: "0.00"
    work: "Not an eligible educator, so 0.00"
  - printed: "person[taxpayer].educator_deduction"
    value: "0.00"
    work: "Line 11 educator deduction = 0.00"
  - printed: "person[taxpayer].hsa_forms"
    value: "1"
    work: "One Form 8889 entered (hsa)"
  - printed: "person[taxpayer].hsa_repeated"
    value: "no"
    work: "1 form is not more than 1"
  - printed: "person[taxpayer].hsa_split"
    value: "0"
    work: "Not spouses with separate HSAs treated as having family coverage; line 6 spouse rule not used"
  - printed: "person[taxpayer].hsa_agreed"
    value: "0"
    work: "Spouse rule not used, so there is no agreed allocation"
  - printed: "person[taxpayer].hsa_step1"
    value: "0.00"
    work: "Step 1 refigured line 5 = 0.00"
  - printed: "person[taxpayer].hsa_share"
    value: "0.00"
    work: "Steps 2-3 share = 0.00"
  - printed: "person[taxpayer].hsa_deduction"
    value: "0.00"
    work: "Form 8889 line 13 = 0.00"
  - printed: "person[taxpayer].tip_employers"
    value: "2"
    work: "tip_1 and tip_3 paid qualified tips; tip_2 paid $0"
  - printed: "person[taxpayer].tip_total"
    value: "31731.00"
    work: "Column (d): 16,804 + 0 + 14,927 = 31,731"
  - printed: "person[taxpayer].tip_reported"
    value: "31731.00"
    work: "Column (b): 16,804 + 0 + 14,927 = 31,731"
  - printed: "person[taxpayer].ot_employers"
    value: "2"
    work: "ot_1 and ot_2"
  - printed: "person[taxpayer].ot_total"
    value: "73571.00"
    work: "38,129 + 35,442 = 73,571"
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a)"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount 0"
  - printed: "person[taxpayer].wages"
    value: "137935.00"
    work: "SS wages + SS tips, emp_a = 137,935"
  - printed: "person[taxpayer].withheld"
    value: "8552.00"
    work: "Box 4 total = 8,552"
  - printed: "person[taxpayer].box1"
    value: "119941.00"
    work: "Box 1 total = 119,941"
  - printed: "person[taxpayer].box2"
    value: "21589.00"
    work: "Box 2 total = 21,589"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "Only one employer, and wages of 137,935 are not over 176,100"
  - printed: "person[taxpayer].excess"
    value: "0.00"
    work: "8,552 is not above 10,918.20, so 0"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible (single employer); no excess"
  - printed: "person[taxpayer].medicare5"
    value: "137935.00"
    work: "Box 5 total = 137,935"
  - printed: "person[taxpayer].medicare6"
    value: "2000.00"
    work: "Box 6 total = 2,000"
```
```
