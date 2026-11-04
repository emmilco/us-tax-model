# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b32afc24066f15532e659f8df4890a279d7e9920d00daafdc8d2af9eb4f49e6c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ab54dc51f5578f6e92147301ec717bdbb6f6ab0be18d86c03ca30c49305b6971 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7c1982142570d77b86602ee931236dfad956df58ff01c7515117175c08e52cfa |
| printed lines compared | 99 |
| agree / disagree / missing | 37 / 62 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 33, 40, 41, 44, 45, 47, 66, 93, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 26, 27, 28, 30, 31, 33, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i1040sc | 2025 | 10, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 10, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
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
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p501 | 2025 returns; PDF created 2026-02-04 | 23 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 23 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- person.person.x_l1_s: reference 'f5329.l1_s' does not resolve
- person.person.x_l2_s: reference 'f5329.l2_s' does not resolve
- person.person.h_s1_ira_total: reference 's1.line23' does not resolve

## Lines

### person.one — One entry for this person
Status: **AGREE**

### person.educator_deduction — This person's educator expense deduction
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "person.educator_expenses"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"input": "person.educator_expenses"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 93, Line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025". The reply asks person.eligible_educator of persons with no educator expense entered; the project skips it when the expense is zero. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,266 of 5,127 agree; 1,835 candidate-unknown, 26 project-unknown; on returns the full interview completes: 101 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 102 against the record's 101, the class M fixtures having been rewritten by a concurrent run): 102 candidate-unknown person.eligible_educator (for example classm.asset.1, person[spouse]). Project stands.

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

### person.hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

### person.hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}, {"args": [{"const": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"const": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}}
```

Ruling: model error; i8889 p. 7, Line 6. Same reply as the Claude family: no married-family split gate, so it asks the Form 8889 allocation of persons the spouse rule does not reach (2 completed-return unknowns). Reclassified from scope for that reason. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,830 of 5,127 agree; 253 value, 44 candidate-unknown; on returns the full interview completes: 1 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 2 against the record's 1, the class M fixtures having been rewritten by a concurrent run): 2 candidate-unknown person.allocation (for example classm.asset.1, person[taxpayer]). Project stands.

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": null}
```

Ruling: model error; i8889 p. 7, Line 6, Step 1, "Refigure the contribution limit that would have been entered on line 5". The reply sums f8889.step1_total, not this person's Step 1 limit, and has no split filter: classm.s2.2.deepseek $85,500 against $7,125 on a completed return. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,560 of 5,127 agree; 562 value, 5 candidate-unknown; on returns the full interview completes: 27 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 27 value (for example classm.s2.2.deepseek, person[spouse]). Project stands.

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.share", "op": "sum_over", "where": null}
```

Ruling: model error; i8889 p. 7, Line 6, Steps 2 and 3. The reply sums f8889.share without the married-family split gate (classm.s3.3.deepseek $356.25 against $0, completed). The Claude family's identical difference is ruled representation on a helper read only under the split; here the reply also refuses and asks answers outside the rule (36 candidate-refuses, 293 candidate-unknown). Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,547 of 5,127 agree; 293 candidate-unknown, 251 value, 36 candidate-refuses; on returns the full interview completes: 23 value, 1 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 25 against the record's 24, the class M fixtures having been rewritten by a concurrent run): 23 value (for example classm.s3.3.deepseek, person[taxpayer]); 2 candidate-unknown person.allocation (for example classm.asset.1, person[taxpayer]). Project stands.

### person.hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

### person.hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

### person.hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

### person.tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

### person.tip_total — This person's worksheet column (d) total
Status: **AGREE**

### person.tip_reported — This person's worksheet column (b) total
Status: **AGREE**

### person.ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

### person.ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

### person.box1 — Total W-2 box 1 for this person
Status: **AGREE**

### person.box2 — Total W-2 box 2 for this person
Status: **AGREE**

### person.ira_amount_a — IRA distributions on this person's Forms 1099-R (line 4a amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"args": [{"const": "roth_ira"}, {"ref": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "any"}}
```

Ruling: model error; i1040gi p. 26, Lines 4a and 4b, IRA distributions (traditional, Roth, SEP and SIMPLE IRAs). The reply keeps only account traditional_ira and drops Roth IRA distributions from line 4a: classm.f8962.3.deepseek $0 against $29,242 on a completed return. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,897 of 5,127 agree; 139 project-refuses, 90 value, 1 project-unknown; on returns the full interview completes: 66 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 66 value (for example classm.f8962.3.deepseek, person[taxpayer]). Project stands.

### person.ira_taxable — Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.ira_taxable", "op": "sum_over", "where": {"args": [{"args": [{"const": "roth_ira"}, {"ref": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; i1040gi pp. 26-27, Line 4b. The reply keeps only traditional_ira accounts (its line 4a error); on the sample every Roth IRA taxable amount is either zero or refused by the cited retirement.taxable screens (Form 8606 Part III), so the only differences are those project refusals. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,987 of 5,127 agree; 139 project-refuses, 1 project-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.ira_rollovers — Number of this person's IRA distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"args": [{"const": "roth_ira"}, {"ref": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "any"}], "test": "all"}}
```

Ruling: model error; i1040gi p. 27, Exception 1 (rollovers). As person.ira_amount_a: a Roth IRA rollover is not counted (generated 90: 0 against 1, completed). executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,981 of 5,127 agree; 139 project-refuses, 6 value, 1 project-unknown; on returns the full interview completes: 4 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 4 value (for example generated 90, person[taxpayer]). Project stands.

### person.plan_amount_a — Pension and annuity distributions on this person's Forms 1099-R (line 5a amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}}
```

Ruling: representation; i1040gi p. 28, Lines 5a and 5b. Reply unchanged; no difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,127 of 5,127 agree; none; on returns the full interview completes: none. No difference. Project stands.

### person.plan_taxable — Taxable pension and annuity distributions on this person's Forms 1099-R (line 5b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.plan_taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}}
```

Ruling: representation; i1040gi p. 28, Lines 5a and 5b. Same filter (account plan) and field as the project; no difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,127 of 5,127 agree; none; on returns the full interview completes: none. No difference. Project stands.

### person.plan_rollovers — Number of this person's pension distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; i1040gi p. 30, Rollovers. Reply unchanged; no difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,127 of 5,127 agree; none; on returns the full interview completes: none. No difference. Project stands.

### person.sav_dist — Distributions received in 2025 that Form 8880 line 4 counts, on this person's Forms 1099-R
Status: **AGREE**

### person.medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

### person.medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

### person.sc_count — Number of Schedules C for this person
Status: **AGREE**

### person.ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **AGREE**

### person.mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **AGREE**

### person.mq_total — Mid-quarter test basis, 2025, this person
Status: **AGREE**

### person.cost179 — Cost of section 179 property, this person
Status: **AGREE**

### person.s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f6", "op": "sum_over", "where": null}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.cost179", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "sc", "field": "sc.cost179_v", "op": "sum_over", "where": null}}
```

Ruling: model error; i4562 p. 5, Line 6 (the amount elected to expense) and Line 7 (listed property). The reply sums sc.cost179 (the cost of section 179 property, not the amount elected) and puts listed property here: classm.f4952.1.deepseek $46,128 against $0, completed. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,640 of 5,127 agree; 386 value, 101 candidate-refuses; on returns the full interview completes: 128 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 127 against the record's 128, the class M fixtures having been rewritten by a concurrent run): 127 value (for example classm.f4952.1.deepseek, person[taxpayer]). Project stands.

### person.s179_listed — Section 179 elected on listed property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f29", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "sc", "field": "sc.cost179_v", "op": "sum_over", "where": null}
```

Ruling: model error; i4562 p. 5, Line 7, "Enter the amount that you elected to expense for listed property (defined earlier) on line 29 here". The reply is the constant zero: stage14.veh.suv_179 $0 against $31,300, completed. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,993 of 5,127 agree; 99 project-refuses, 23 project-unknown, 12 value; on returns the full interview completes: 6 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 5 against the record's 6, the class M fixtures having been rewritten by a concurrent run): 5 value (for example classm.eic.3.deepseek, person[taxpayer]). Project stands.

### person.income179 — Business net profit or loss without section 179, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.line31_pre179", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}
```

Ruling: model error; i4562 p. 5, Line 11 (business income limitation). The reply reads sc.profit_pos, which through the reply's own section 179 lines makes a cycle at sc.result: unknown on every completed return with a Schedule C. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,358 of 5,127 agree; 736 candidate-unknown, 29 candidate-refuses, 4 project-refuses; on returns the full interview completes: 267 candidate-unknown, 2 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 268 against the record's 269, the class M fixtures having been rewritten by a concurrent run): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 2 candidate-refuses (for example classm.s179.2, person[taxpayer]). Project stands.

### person.sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}
```

Ruling: model error; i4562 p. 5, Line 11, "computed without regard to any section 179 expense deduction". The reply sums sc.line31 and its own person.income179 copies person.sc_total, so the section 179 business income limit reads the Schedule C profit after the section 179 deduction: a cycle at person.sc_total, unknown on every completed return with a Schedule C, and on classm.s179.2 and stage14.s179.zero_limit_carryover a section 179 over-limit refusal the project does not make. The project-refuses differences are the cited at-risk screen of sc.result (as the Claude family's ruling). executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 4,170 of 4,906 agree; 705 candidate-unknown, 21 candidate-refuses, 10 project-refuses; on returns the full interview completes: 266 candidate-unknown, 2 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run `/tmp/adj-fx/`, recorded triage file untouched; it counts 272 against the record's 268, the class M fixtures having been rewritten by a concurrent run): 270 candidate-unknown (cycle at sc_total or s179.differs) (for example classm.f4952.1.deepseek, person[taxpayer]); 2 candidate-refuses s179.over_limit (classm.s179.2, person[taxpayer]). Project stands.

### person.se_line6 — Schedule SE line 6 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,486 of 5,127 agree; 2,389 candidate-unknown, 245 candidate-refuses, 7 project-refuses; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.se_line12 — Schedule SE line 12 (self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,486 of 5,127 agree; 2,389 candidate-unknown, 245 candidate-refuses, 7 project-refuses; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.se_line13 — Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,486 of 5,127 agree; 2,389 candidate-unknown, 245 candidate-refuses, 7 project-refuses; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error; p560 p. 39, "Enter your actual contribution, not to exceed your maximum deductible contribution, on Schedule 1 (Form 1040), line 16". No Schedule C gate: it computes a deduction from plan answers of persons with no self-employment income (class M deepseek fixtures, for example classm.clcw26.2.deepseek $5,199 against $0) and asks the plan answers of everyone; with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,868 of 5,127 agree; 1,897 candidate-unknown, 218 value, 117 project-refuses, 25 candidate-refuses, 2 project-unknown; on returns the full interview completes: 119 value, 116 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 236 against the record's 235, the class M fixtures having been rewritten by a concurrent run): 119 value (for example classm.clcw26.2.deepseek, person[taxpayer]); 95 candidate-unknown person.plan_screen (for example classm.asset.1, person[spouse]); 9 candidate-unknown person.plan (for example classm.s2.3.deepseek without plan, person[taxpayer]); 5 candidate-unknown (cycle) (for example classm.ira.2, person[spouse]); 2 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[spouse]); 2 candidate-unknown person.sep_contrib (for example classm.s2.3.deepseek without sep_contrib, person[spouse]); 2 candidate-unknown person.simple_deferral (for example classm.s3.4.deepseek without simple_deferral, person[taxpayer]); 2 candidate-unknown person.simple_employer (for example classm.s3.4.deepseek without simple_employer, person[taxpayer]). Project stands.

### person.positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

### person.sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

### person.qbi — Qualified business income or loss of this person's businesses
Status: **AGREE**

### person.eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,485 of 5,127 agree; 2,389 candidate-unknown, 246 candidate-refuses, 7 project-refuses; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.tips_ot"}], "test": "eq"}}
```

Second:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.statutory"}], "test": "eq"}}
```

Ruling: model error; i1040gi p. 104, Schedule 1-A, line 5 (qualified tips and overtime of a self-employed person). The reply counts the Schedules C answered as statutory-employee income (sc.statutory) instead of those with Schedule 1-A tips or overtime (sc.tips_ot). Every difference is on a refused record (stage14.refuse.statutory, stage14.refuse.sch1a_tips; project-unknown where sc.tips_ot was not asked on a refused return). executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 4,895 of 4,906 agree; 7 project-unknown, 4 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part reported in box
Status: **AGREE**

### person.dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "w2", "field": "w2.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"ref": "w2.box10"}], "test": "lt"}}], "test": "lt"}
```

Ruling: representation; i2441 p. 5, Line 12. Count of W-2s with box 10 above zero against the box 10 total above zero; no difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,127 of 5,127 agree; none; on returns the full interview completes: none. No difference. Project stands.

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,506 of 5,127 agree; 2,355 candidate-unknown, 243 candidate-refuses, 21 project-refuses, 2 value; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without l
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,465 of 5,127 agree; 2,405 candidate-unknown, 247 candidate-refuses, 7 project-refuses, 3 value; on returns the full interview completes: 283 candidate-unknown, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 266 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 17 candidate-unknown person.se_screen (for example classm.asset.1, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return, or a stu
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_born"}], "test": "ne"}], "test": "any"}
```

Ruling: ambiguity; amb.2025.savers_ineligible_column (owner decision). The reply reads person.sav_claimed where the project reads sa.dependent for the filer. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,817 of 5,127 agree; 258 value, 48 candidate-unknown, 4 project-unknown; on returns the full interview completes: 14 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 14 candidate-unknown person.sav_claimed (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deductible or no
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "person.sav_roth"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"input": "person.ira_trad"}, {"input": "person.sav_roth"}], "op": "sum"}
```

Ruling: model error; f8880 line 1. The reply asks person.ira_trad of persons who entered no IRA contribution. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,405 of 5,127 agree; 1,686 candidate-unknown, 35 project-unknown, 1 project-refuses; on returns the full interview completes: 108 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 109 against the record's 108, the class M fixtures having been rewritten by a concurrent run): 109 candidate-unknown person.ira_trad (for example classm.asset.1, person[spouse]). Project stands.

### person.sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"input": "person.sav_voluntary"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error; f8880 p. 2, Line 2, "Elective deferrals to a 401(k) or other qualified employer plan ... SIMPLE". The reply omits a self-employed person's own SIMPLE deferrals: classm.se.2 spouse $0 against $7,815, stage14.simple.match_age50 $0 against $18,000. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,952 of 5,127 agree; 144 project-refuses, 17 value, 14 project-unknown; on returns the full interview completes: 5 value, 1 project-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 5 value (for example classm.se.2, person[spouse]); 1 project-unknown person.sav_excess (for example classm.f1040.5.deepseek without sav_excess, person[taxpayer]). Project stands.

### person.ira_contrib — This person's traditional IRA contributions for 2025 (zero if the traditional IRA question
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}
```

Second:

```json
{"input": "person.ira_trad"}
```

Ruling: model error; i1040gi pp. 97-98, IRA Deduction Worksheet. The reply asks person.ira_trad of persons who entered no contribution. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,199 of 5,127 agree; 1,897 candidate-unknown, 31 project-unknown; on returns the full interview completes: 108 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 109 against the record's 108, the class M fixtures having been rewritten by a concurrent run): 109 candidate-unknown person.ira_trad (for example classm.asset.1, person[spouse]). Project stands.

### person.ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"input": "person.ira_work_plan"}
```

Ruling: model error; i1040gi p. 96, Were You Covered by a Retirement Plan? The reply drops the person's own SEP or SIMPLE plan as coverage: classm.ira.2 spouse not covered against covered. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,978 of 5,127 agree; 121 value, 22 candidate-unknown, 6 project-unknown; on returns the full interview completes: 8 candidate-unknown, 2 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 8 candidate-unknown person.ira_work_plan (for example classm.se.2, person[spouse]); 2 value (for example classm.ira.2, person[spouse]). Project stands.

### person.ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 97, line 2. The reply carries its coverage error (person.ira_cov, own plan dropped): classm.ira.2 spouse $246,000 against $146,000, and asks ira_work_plan of persons the project does not ask. The previous declaration error is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,033 of 5,127 agree; 89 value, 3 project-unknown, 2 candidate-unknown; on returns the full interview completes: 1 candidate-unknown, 1 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 1 value (for example classm.ira.2, person[spouse]); 1 candidate-unknown person.ira_work_plan (for example classm.se.2, person[spouse]). Project stands.

### person.ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract li
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi pp. 97-98, IRA Deduction Worksheet lines 3 to 6. The reply's lines 3 to 5 give a different result (classm.f8889.1.deepseek $71,375.33 against $71,339 on a completed return) and, with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,086 of 5,127 agree; 1,765 candidate-unknown, 173 value, 46 project-refuses, 33 candidate-refuses, 24 project-unknown; on returns the full interview completes: 376 candidate-unknown, 111 value, 5 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 276 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 111 value (for example classm.f8889.1.deepseek, person[spouse]); 17 candidate-unknown person.eligible_educator (for example classm.eic.1, person[taxpayer]); 11 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[spouse]); 11 candidate-unknown person.plan (for example classm.s2.3.deepseek without plan, person[spouse]); 11 candidate-unknown person.plan_screen (for example classm.s2.3.deepseek without plan_screen, person[spouse]); 11 candidate-unknown person.ira_trad (for example classm.s2.3.deepseek without ira_trad, person[spouse]); 11 candidate-unknown person.ira_excess (for example classm.s2.3.deepseek without ira_excess, person[spouse]); 11 candidate-unknown person.ira_age50 (for example classm.s2.3.deepseek without ira_age50, person[spouse]); 10 candidate-unknown person.ira_work_plan (for example classm.se.2, person[spouse]); 5 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]); 3 candidate-unknown person.sep_contrib (for example classm.s2.3.deepseek without sep_contrib, person[spouse]); 2 candidate-unknown person.simple_deferral (for example classm.s3.4.deepseek without simple_deferral, person[taxpayer]); 2 candidate-unknown person.simple_employer (for example classm.s3.4.deepseek without simple_employer, person[taxpayer]). Project stands.

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi p. 97, line 7. The reply fills the limit for persons with no traditional contribution (classm.ira.2 $7,000 against $0) and asks ira_work_plan of them; with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,866 of 5,127 agree; 216 project-refuses, 22 candidate-unknown, 17 project-unknown, 6 value; on returns the full interview completes: 3 candidate-unknown, 3 value, 2 project-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 3 value (for example classm.ira.2, person[spouse]); 2 candidate-unknown person.ira_work_plan (for example classm.se.2, person[spouse]); 2 project-unknown person.ira_work_plan (for example classm.s2.3.deepseek without ira_work_plan, person[spouse]); 1 candidate-unknown (cycle) (for example stage21.f1.lower_bound_still_decides, person[taxpayer]). Project stands.

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, {"from": {"of": [{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi p. 98, line 12; i8606 p. 2, Who Must File. The reply asks the IRA answers (ira_excess, ira_trad, ira_work_plan, ira_age50) of persons with no contribution and, with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. The previous copy of the IRA worksheet line is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,169 of 5,127 agree; 2,617 candidate-unknown, 306 candidate-refuses, 23 project-unknown, 12 project-refuses; on returns the full interview completes: 324 candidate-unknown, 3 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 172 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 109 candidate-unknown person.ira_excess (for example classm.asset.1, person[spouse]); 13 candidate-unknown person.ira_work_plan (for example stage21.f1.lower_bound_still_decides, person[spouse]); 12 candidate-unknown person.ira_age50 (for example classm.u1250.1.deepseek without ira_age50, person[taxpayer]); 9 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[taxpayer]); 9 candidate-unknown person.ira_trad (for example classm.s2.3.deepseek without ira_trad, person[taxpayer]); 3 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, {"from": {"of": [{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi p. 98, line 12; i8606 p. 2, Who Must File. The reply asks the IRA answers (ira_excess, ira_trad, ira_work_plan, ira_age50) of persons with no contribution and, with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. The previous copy of the IRA worksheet line is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,169 of 5,127 agree; 2,618 candidate-unknown, 306 candidate-refuses, 23 project-unknown, 11 project-refuses; on returns the full interview completes: 324 candidate-unknown, 3 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 169 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 109 candidate-unknown person.ira_trad (for example classm.asset.1, person[spouse]); 13 candidate-unknown person.ira_work_plan (for example stage21.f1.lower_bound_still_decides, person[spouse]); 12 candidate-unknown person.ira_excess (for example classm.u1250.1.deepseek without ira_excess, person[taxpayer]); 12 candidate-unknown person.ira_age50 (for example classm.u1250.1.deepseek without ira_age50, person[taxpayer]); 9 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[taxpayer]); 3 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"expression": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.ira_basis_adjusted"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "person.ira_basis"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, {"from": {"of": [{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}}], "test": "lt"}], "test": "any"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi p. 98, line 12; i8606 p. 2, Who Must File. The reply asks the IRA answers (ira_excess, ira_trad, ira_work_plan, ira_age50) of persons with no contribution and, with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. The previous copy of the IRA worksheet line is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,169 of 5,127 agree; 2,618 candidate-unknown, 306 candidate-refuses, 23 project-unknown, 11 project-refuses; on returns the full interview completes: 324 candidate-unknown, 3 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 169 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 109 candidate-unknown person.ira_trad (for example classm.asset.1, person[spouse]); 13 candidate-unknown person.ira_work_plan (for example stage21.f1.lower_bound_still_decides, person[spouse]); 12 candidate-unknown person.ira_excess (for example classm.u1250.1.deepseek without ira_excess, person[taxpayer]); 12 candidate-unknown person.ira_age50 (for example classm.u1250.1.deepseek without ira_age50, person[taxpayer]); 9 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[taxpayer]); 3 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}, "then": {"input": "person.ira_basis"}}], "op": "choose"}
```

Second:

```json
{"input": "person.ira_basis"}
```

Ruling: model error; i8606 p. 9, Line 2. The reply asks the basis answers of persons with no contribution or distribution. Reply unchanged. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,158 of 5,127 agree; 1,926 candidate-unknown, 31 project-unknown, 12 project-refuses; on returns the full interview completes: 120 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 121 against the record's 120, the class M fixtures having been rewritten by a concurrent run): 109 candidate-unknown person.ira_basis_adjusted (for example classm.asset.1, person[spouse]); 12 candidate-unknown person.ira_basis (for example classm.u1250.1.deepseek without ira_basis, person[taxpayer]). Project stands.

### person.ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or Roth conv
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"input": "person.ira_dist"}
```

Ruling: model error; i8606 p. 2, Who Must File. The reply asks person.ira_dist of every person, including persons with no contribution or basis (100 completed-return unknowns). executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 3,242 of 5,127 agree; 1,869 candidate-unknown, 12 project-refuses, 4 candidate-refuses; on returns the full interview completes: 99 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 100 against the record's 99, the class M fixtures having been rewritten by a concurrent run): 100 candidate-unknown person.ira_dist (for example classm.asset.1, person[spouse]). Project stands.

### person.ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier ye
Status: **DISAGREE**

Project:

```json
{"collection": "f8606", "field": "f8606.line14", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_basis"}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, {"from": {"of": [{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "sum"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Second transcription's note: The excerpts do not give all Form 8606 Part I lines needed to reduce basis for distributions or conversions; this reading carries basis plus 2025 nondeductible contributions.

Ruling: model error on the declaration; the line names an instance of f8606, a definition that does not exist ("instance def 'f8606' does not exist"), so it was not executed. This adjudicates the declaration, not the tax reading; by reading it rebuilds Form 8606 line 14 from the answers instead of the project's Form 8606 entries. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records): the candidate is invalid and was not executed (person.person.edu_line31: 'aqee' has no line 'line31'; person.person.ira_8606_line14: instance def 'f8606' does not exist). Project stands.

### person.ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"from": {"ref": "f1040.line9"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line23"}, {"ref": "s1.line25"}], "op": "sum"}}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}, {"from": {"of": [{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.h_s1_ira_total", "message": "person.person.h_s1_ira_total: reference 's1.line23' does not resolve"}]}
```

Ruling: model error; i1040gi p. 98, line 12; i8606 p. 2, Who Must File. The reply asks the IRA answers (ira_excess, ira_trad, ira_work_plan, ira_age50) of persons with no contribution and, with a Schedule C, the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. The previous copy of the IRA worksheet line is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,169 of 5,127 agree; 2,618 candidate-unknown, 306 candidate-refuses, 23 project-unknown, 11 project-refuses; on returns the full interview completes: 324 candidate-unknown, 3 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 172 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 109 candidate-unknown person.ira_excess (for example classm.asset.1, person[spouse]); 13 candidate-unknown person.ira_work_plan (for example stage21.f1.lower_bound_still_decides, person[spouse]); 12 candidate-unknown person.ira_age50 (for example classm.u1250.1.deepseek without ira_age50, person[taxpayer]); 9 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[taxpayer]); 9 candidate-unknown person.ira_trad (for example classm.s2.3.deepseek without ira_trad, person[taxpayer]); 3 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"from": {"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i1040gi p. 98, line 9, "Enter the earned income you (and your spouse if filing jointly) received". The reply is the constant zero, dropping net self-employment earnings: 136 completed-return value differences. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,544 of 5,127 agree; 327 value, 198 project-refuses, 58 project-unknown; on returns the full interview completes: 136 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 136 value (for example classm.f4952.1.deepseek, person[taxpayer]). Project stands.

### person.edu_kid — Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of yo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0}, {"ref": "f8863.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8863.line7"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_born_2002"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu_born_2007"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: The excerpts give age conditions by birth-date input rather than exact ages; this reading treats not being born before January 2, 2007 as the under-19 branch and uses the under-24 full-time/half-support branch.

Ruling: model error; i8863 pp. 6-7, Line 7 (the conditions under which the credit is not refundable). The reply redefines the line as the student test (edu and edu_1098t), so it differs on completed returns and asks those answers of everyone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,518 of 5,127 agree; 2,410 candidate-unknown, 104 value, 92 project-refuses, 3 project-unknown; on returns the full interview completes: 180 candidate-unknown, 47 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 228 against the record's 227, the class M fixtures having been rewritten by a concurrent run): 181 candidate-unknown person.edu (for example classm.f4952.1.deepseek, person[taxpayer]); 47 value (for example classm.f1040.2.deepseek, person[spouse]). Project stands.

### person.x_l1 — Form 5329 line 1 for this person: early distributions includible in income
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l1", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l1", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 p. 3, Line 1, "Enter the amount of early distributions includible in income". The reply defines the per-person line 1 total as Form 5329 line 1, but the project's f5329.l1 copies person.x_l1, so the reply's line is a cycle at person.x_l1, unknown on every completed return. The project-refuses differences are refused records. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 20 of 4,906 agree; 4,883 candidate-unknown, 3 project-refuses; on returns the full interview completes: 1,011 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run `/tmp/adj-fx/`, recorded triage file untouched; it counts 1,018 against the record's 1,011, the class M fixtures having been rewritten by a concurrent run): 1,018 candidate-unknown (cycle at x_l1) (for example classm.f8889.1.deepseek, person[taxpayer]). Project stands.

### person.x_l2_all — Exception amounts before the per-person limits
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l2", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 p. 5, Line 2, "Enter on line 2 the amount that you can exclude". The reply takes f5329.l2, which is the reply's own person.x_other_exc (every retirement.l2, limited exceptions included) plus person.x_limited_sum, so it counts each limited exception twice (classm.f5329.3.deepseek $18,780 against $9,390, refused), and the reply's x_limited_sum reads retirement.exc_amount of distributions with no exception, which the interview does not ask. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 4,493 of 4,906 agree; 213 candidate-refuses, 123 candidate-unknown, 77 value; on returns the full interview completes: 13 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run `/tmp/adj-fx/`, recorded triage file untouched): 13 candidate-unknown retirement.exc_amount (for example classm.aqee.1.deepseek, person[taxpayer]). Project stands.

### person.x_l1_s — Line 1 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f5329", "field": "f5329.l1_s", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l1_s", "message": "person.person.x_l1_s: reference 'f5329.l1_s' does not resolve"}]}
```

Ruling: model error on the declaration; the reply reads f5329.l1_s, which does not resolve ("reference 'f5329.l1_s' does not resolve"), so the line was not executed (4,906 candidate-invalid in `reviews/2025/transcription/triage/person.deepseek.json`). This ruling adjudicates the declaration, not the tax reading; by reading, a per-person code S total taken from a Form 5329 line would also run the wrong way (Form 5329 lines read the person helpers). Project stands.

### person.x_l2_s — Line 2 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f5329", "field": "f5329.l2_s", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l2_s", "message": "person.person.x_l2_s: reference 'f5329.l2_s' does not resolve"}]}
```

Ruling: model error on the declaration; the reply reads f5329.l2_s, which does not resolve ("reference 'f5329.l2_s' does not resolve"), so the line was not executed (4,906 candidate-invalid in `reviews/2025/transcription/triage/person.deepseek.json`). This ruling adjudicates the declaration, not the tax reading. Project stands.

### person.x_tax — This person's Form 5329 taxes
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.tax", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l4", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 pp. 3-5 and Form 5329 Part VII. The reply adds the early-distribution taxes and leaves out the HSA excess contribution tax: classm.f8889.1.deepseek spouse $0 against $97.92, completed. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,755 of 5,127 agree; 167 value, 111 project-unknown, 94 project-refuses; on returns the full interview completes: 19 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 19 value (for example classm.f8889.1.deepseek, person[spouse]). Project stands.

### person.x_must — One if this person must file Form 5329
Status: **AGREE**

### person.x_c05 — Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 p. 5, Line 2, exception 05 (only medical expenses above 7.5% of adjusted gross income). The reply sums the exception 05 amounts without the limit: stage21.blind.e6 $9,000 against $7,475 (incomplete). Reclassified from scope. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,126 of 5,127 agree; 1 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.x_two23 — Exception 23 claimed on more than one distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}}], "test": "lt"}
```

Ruling: model error; p590b p. 28, exception 23, one emergency distribution a year. The reply counts every code 1 or code S entry, not only those claiming exception 23, so it is true for two early distributions of any kind (classm.f5329.3, refused; stage21.blind.e1, incomplete). No completed return differs. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,055 of 5,127 agree; 72 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.x_limited_sum — Exceptions 05, 09, 19, 22 and 23 within their limits
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Second:

```json
{"collection": "retirement", "field": "retirement.exc_capped", "op": "sum_over", "where": null}
```

Ruling: scope; i5329 p. 5, Line 2. Reply unchanged; the differences are on refused or incomplete records (stage21 limit cases) where the project refuses on the cited amb.2025.f5329_simple_limits screen. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,122 of 5,127 agree; 5 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.x_other_exc — Exceptions without a fixed limit
Status: **DISAGREE**

Project:

```json
{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 p. 5, Line 2, and the exception limits of exceptions 05, 09, 19, 22 and 23 (p590b p. 28). The reply puts every exception amount in the unlimited remainder, so the limited exceptions are also counted there: stage21.blind.e4 to e7 and stage21.mut.e23_over_cap (incomplete or refused records only). As the Claude family's ruling on this line. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 4,893 of 4,906 agree; 13 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.x_limit_binds — A limited exception over its limit on a person with a code S distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"collection": "retirement", "field": "retirement.exc_capped", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.exc_amount", "op": "sum_over", "where": null}], "test": "lt"}
```

Ruling: model error; i5329 p. 5, Line 4; amb.2025.f5329_simple_limits. The reply is the constant false, so it never flags the case the project refuses (stage21.refuse.limit_binds). No completed return differs. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,105 of 5,127 agree; 20 project-unknown, 1 project-refuses, 1 value; on returns the full interview completes: none. No completed-return difference. Project stands.

### person.x_hsa_excess — This person's 2025 HSA excess contributions (Form 8889)
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.excess_amt", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l48", "op": "sum_over", "where": null}
```

Ruling: model error; i5329 p. 8, Line 47, "Enter the excess of your contributions ... to your HSAs for 2025 from Form 8889, line 2 ... over your contribution limit (Form 8889, line 12)". The excess comes from Form 8889; the reply reads Form 5329 line 48, which the project derives from line 47 and so from person.x_hsa_excess: a cycle, unknown on every completed return. The project-refuses differences are refused records. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 39 of 4,906 agree; 4,807 candidate-unknown, 60 project-refuses; on returns the full interview completes: 1,011 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run `/tmp/adj-fx/`, recorded triage file untouched; it counts 1,018 against the record's 1,011, the class M fixtures having been rewritten by a concurrent run): 1,018 candidate-unknown (cycle at f5329.l48) (for example classm.f8889.1.deepseek, person[taxpayer]). Project stands.

### employers — Total w2.one for this person
Status: **AGREE**

### overcount — Number of employers that withheld more than the limit
Status: **AGREE**

### over — Any employer withheld more than the limit
Status: **AGREE**

### wages — Total w2.wages for this person
Status: **AGREE**

### withheld — Total w2.box4 for this person
Status: **AGREE**

### eligible — More than one employer and total social security wages over $176,100
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}, {"args": [{"param": "ss.limit"}, {"line": "withheld"}], "test": "lt"}, {"args": [{"const": true}, {"line": "over"}], "test": "ne"}], "test": "all"}
```

Ruling: scope; i1040gi p. 117, Line 11. The reply adds "no employer withheld over the limit" to the project's test; that case is refused at person.credit (Form 843, the cited person.over screen), so the differences are on refused records only. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,117 of 5,127 agree; 9 value, 1 project-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

### excess — Withholding above $10,918.20, if any
Status: **DISAGREE**

Project:

```json
{"from": {"line": "withheld"}, "op": "subtract_floor0", "take": {"param": "ss.limit"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}, "then": {"from": {"line": "withheld"}, "op": "subtract_floor0", "take": {"param": "ss.limit"}}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 117, Line 11 worksheet. The reply gates the excess helper on eligible, which the project applies one line later at person.credit; the helper is read only there, and no completed return differs. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,893 of 5,127 agree; 191 candidate-unknown, 21 value, 20 candidate-refuses, 2 project-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

### zero — No excess credit
Status: **AGREE**

### credit — Excess social security tax withheld, figured separately for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "excess"}}], "op": "choose"}
```

Second:

```json
{"line": "excess"}
```

Ruling: scope; i1040gi p. 117, Line 11, "If any one employer withheld more than $10,918.20, you can't claim the excess on your return". The reply copies its gated excess and omits the project's cited refusals (person.over, Form 843; person.rrta); every difference is one of those refusals. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 5,106 of 5,127 agree; 19 project-refuses, 2 project-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

### Step 1 — Net profit from Schedule C, line 31
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}
```

Ruling: model error; p560 p. 39, Deduction Worksheet for Self-Employed, Step 1, "Enter your net profit from line 31, Schedule C", with i4562 p. 5, Line 11 (business income "computed without regard to any section 179 expense deduction"). The reply sums sc.line31, which through its own person.income179 (a copy of person.sc_total) is the cycle of person.sc_total: unknown on every return with a Schedule C, and a section 179 over-limit refusal on classm.s179.2. The project-unknown and project-refuses differences are the cited person.se_screened screen and its unasked answer for persons with no plan, as the Claude family's scope ruling on this line. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,939 partial records; 4,906 comparisons): 2,338 of 4,906 agree; 1,655 project-unknown, 696 candidate-unknown, 195 project-refuses, 22 candidate-refuses; on returns the full interview completes: 266 candidate-unknown, 55 project-unknown, 2 candidate-refuses, 2 project-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run `/tmp/adj-fx/`, recorded triage file untouched; it counts 329 against the record's 325, the class M fixtures having been rewritten by a concurrent run): 270 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 55 project-unknown person.se_screen (for example classm.s3.1.deepseek, person[taxpayer]); 2 candidate-refuses s179.over_limit (classm.s179.2); 2 project-refuses person.se_screened (classm.f5695.2.deepseek). Project stands.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, and the Schedule SE lines. The formula follows Schedule SE, but the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C, and the reply also reads person.se_screen of persons with no Schedule C and refuses on it. The previous reply's declaration error (an unresolved line reference) is gone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,402 of 5,127 agree; 2,420 candidate-unknown, 255 candidate-refuses, 50 project-refuses; on returns the full interview completes: 294 candidate-unknown, 3 candidate-refuses. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 190 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 95 candidate-unknown person.plan_screen (for example classm.asset.1, person[spouse]); 9 candidate-unknown person.se_screen (for example classm.s2.3.deepseek without se_screen, person[taxpayer]); 3 candidate-refuses (for example classm.f5695.2.deepseek, person[taxpayer]). Project stands.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **AGREE**

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}
```

Second:

```json
{"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 3, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}
```

Ruling: model error; p560 pp. 39-40, Step 5, "Multiply step 3 by step 4". The reply copies Step 3 and drops the self-employed rate, and with a Schedule C the reply's own section 179 income line (person.income179 as sc.profit_pos) makes a cycle at sc.result, so the line is unknown on every return with a Schedule C. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 4,395 of 5,127 agree; 611 candidate-unknown, 53 project-refuses, 44 candidate-refuses, 24 project-unknown; on returns the full interview completes: 196 candidate-unknown, 9 project-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 204 against the record's 205, the class M fixtures having been rewritten by a concurrent run): 183 candidate-unknown (cycle) (for example classm.f4952.1.deepseek, person[taxpayer]); 12 candidate-unknown person.plan_screen (for example classm.u1250.1.deepseek without plan_screen, person[taxpayer]); 9 project-unknown person.sep_rate (for example classm.s2.3.deepseek without sep_rate, person[taxpayer]). Project stands.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **AGREE**

### Step 7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

### Step 8 — Contribution dollar limit
Status: **AGREE**

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **AGREE**

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}
```

Ruling: model error; f8863 p. 2, lines 26-31; i8863 pp. 2-3. The reply has no eligibility gate: it shows amounts on lines the project hides for a person with no American opportunity credit (42 completed candidate-shows-skipped) and asks the education answers of everyone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,481 of 5,127 agree; 2,556 candidate-unknown, 79 candidate-shows-skipped, 10 project-unknown, 1 project-refuses; on returns the full interview completes: 231 candidate-unknown, 42 candidate-shows-skipped. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 274 against the record's 273, the class M fixtures having been rewritten by a concurrent run): 191 candidate-unknown person.edu_inst (for example classm.f4952.1.deepseek, person[taxpayer]); 42 candidate-shows-skipped (for example classm.f1040.2.deepseek, person[spouse]); 11 candidate-unknown person.edu_mat (for example classm.s2.3.deepseek without edu_mat, person[taxpayer]); 10 candidate-unknown person.edu_a2025 (for example classm.s2.3.deepseek without edu_a2025, person[taxpayer]); 10 candidate-unknown person.edu_a2026 (for example classm.s2.3.deepseek without edu_a2026, person[taxpayer]); 10 candidate-unknown person.edu_refunds (for example classm.s2.3.deepseek without edu_refunds, person[taxpayer]). Project stands.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "27"}, "op": "subtract_floor0", "take": {"const": 200000}}
```

Ruling: model error; f8863 p. 2, lines 26-31; i8863 pp. 2-3. The reply has no eligibility gate: it shows amounts on lines the project hides for a person with no American opportunity credit (42 completed candidate-shows-skipped) and asks the education answers of everyone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,483 of 5,127 agree; 2,556 candidate-unknown, 77 candidate-shows-skipped, 10 project-unknown, 1 project-refuses; on returns the full interview completes: 231 candidate-unknown, 42 candidate-shows-skipped. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 274 against the record's 273, the class M fixtures having been rewritten by a concurrent run): 191 candidate-unknown person.edu_inst (for example classm.f4952.1.deepseek, person[taxpayer]); 42 candidate-shows-skipped (for example classm.f1040.2.deepseek, person[spouse]); 11 candidate-unknown person.edu_mat (for example classm.s2.3.deepseek without edu_mat, person[taxpayer]); 10 candidate-unknown person.edu_a2025 (for example classm.s2.3.deepseek without edu_a2025, person[taxpayer]); 10 candidate-unknown person.edu_a2026 (for example classm.s2.3.deepseek without edu_a2026, person[taxpayer]); 10 candidate-unknown person.edu_refunds (for example classm.s2.3.deepseek without edu_refunds, person[taxpayer]). Project stands.

### 29 — Multiply line 28 by 25% (0.25)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "28"}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}
```

Ruling: model error; f8863 p. 2, lines 26-31; i8863 pp. 2-3. The reply has no eligibility gate: it shows amounts on lines the project hides for a person with no American opportunity credit (42 completed candidate-shows-skipped) and asks the education answers of everyone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,483 of 5,127 agree; 2,556 candidate-unknown, 77 candidate-shows-skipped, 10 project-unknown, 1 project-refuses; on returns the full interview completes: 231 candidate-unknown, 42 candidate-shows-skipped. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 274 against the record's 273, the class M fixtures having been rewritten by a concurrent run): 191 candidate-unknown person.edu_inst (for example classm.f4952.1.deepseek, person[taxpayer]); 42 candidate-shows-skipped (for example classm.f1040.2.deepseek, person[spouse]); 11 candidate-unknown person.edu_mat (for example classm.s2.3.deepseek without edu_mat, person[taxpayer]); 10 candidate-unknown person.edu_a2025 (for example classm.s2.3.deepseek without edu_a2025, person[taxpayer]); 10 candidate-unknown person.edu_a2026 (for example classm.s2.3.deepseek without edu_a2026, person[taxpayer]); 10 candidate-unknown person.edu_refunds (for example classm.s2.3.deepseek without edu_refunds, person[taxpayer]). Project stands.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "eq"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "ne"}, "then": {"of": [{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "28"}, {"const": 0}], "test": "le"}, "then": {"line": "27"}}, {"guard": {"args": [{"const": 0}, {"line": "28"}], "test": "lt"}, "then": {"of": [{"line": "29"}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error; f8863 p. 2, lines 26-31; i8863 pp. 2-3. The reply has no eligibility gate: it shows amounts on lines the project hides for a person with no American opportunity credit (42 completed candidate-shows-skipped) and asks the education answers of everyone. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records; 5,127 comparisons): 2,481 of 5,127 agree; 2,556 candidate-unknown, 79 candidate-shows-skipped, 10 project-unknown, 1 project-refuses; on returns the full interview completes: 231 candidate-unknown, 42 candidate-shows-skipped. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 274 against the record's 273, the class M fixtures having been rewritten by a concurrent run): 191 candidate-unknown person.edu_inst (for example classm.f4952.1.deepseek, person[taxpayer]); 42 candidate-shows-skipped (for example classm.f1040.2.deepseek, person[spouse]); 11 candidate-unknown person.edu_mat (for example classm.s2.3.deepseek without edu_mat, person[taxpayer]); 10 candidate-unknown person.edu_a2025 (for example classm.s2.3.deepseek without edu_a2025, person[taxpayer]); 10 candidate-unknown person.edu_a2026 (for example classm.s2.3.deepseek without edu_a2026, person[taxpayer]); 10 candidate-unknown person.edu_refunds (for example classm.s2.3.deepseek without edu_refunds, person[taxpayer]). Project stands.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}
```

Ruling: model error on the declaration; the reply names aqee line31, which does not exist ("'aqee' has no line 'line31'"), so the line was not executed. By reading it also lacks the eligibility gate of lines 27 to 30. executable-triage-v2 (`reviews/2025/transcription/triage/person.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 2,118 partial records): the candidate is invalid and was not executed (person.person.edu_line31: 'aqee' has no line 'line31'; person.person.ira_8606_line14: instance def 'f8606' does not exist). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| person.se_line6 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.se_line12 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.se_line13 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.s16 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.qbi | qbi.unsupported | qbi.unsupported |
| person.eic_se | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.dc_earned | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.dc_earned_b | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.sav_line1 | person.sav_able | - |
| person.ira_deduction | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.ira_nondeductible | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.ira_files_8606 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.ira_8606_line14 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.ira_ssb | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.ira_se | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| excess | person.rrta | person.rrta |
| credit | person.rrta | - |
| Step 2 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 3 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 5 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 7 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 21 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |

## Raw second transcription

```yaml
lines:
  - id: person.employers
    printed: "employers"
    label: "employers"
    type: Count
    expr:
      op: sum_over
      collection: w2
      field: w2.one
  - id: person.overcount
    printed: "overcount"
    label: "overcount"
    type: Count
    expr:
      op: sum_over
      collection: w2
      field: w2.one
      where: {op: test, eq: [w2.over, {const: true}]}
  - id: person.over
    printed: "over"
    label: "over"
    type: Bool
    expr:
      op: test
      gt: [person.overcount, {const: 0, type: Count}]
  - id: person.wages
    printed: "wages"
    label: "wages"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.wages
  - id: person.withheld
    printed: "withheld"
    label: "withheld"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box4
  - id: person.eligible
    printed: "eligible"
    label: "eligible"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [person.employers, {const: 1, type: Count}]}
        - {op: test, gt: [person.wages, {param: ss.base}]}
        - {op: test, gt: [person.withheld, {param: ss.limit}]}
        - {op: test, not: {op: test, eq: [person.over, {const: true}]}}
  - id: person.excess
    printed: "excess"
    label: "excess"
    type: NonNegDollars
    refuses: [person.rrta]
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.eligible, {const: true}]}
          then: person.h_ss_excess
        - guard: {op: test, eq: [person.eligible, {const: false}]}
          then: person.zero
  - id: person.zero
    printed: "zero"
    label: "zero"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
  - id: person.credit
    printed: "credit"
    label: "credit"
    type: NonNegDollars
    refuses: [person.rrta]
    expr:
      op: copy
      from: person.excess
  - id: person.sep_s1
    printed: "Step 1"
    label: "Step 1"
    type: Dollars
    expr:
      op: copy
      from: person.sc_total
  - id: person.sep_s2
    printed: "Step 2"
    label: "Step 2"
    type: NonNegDollars
    expr:
      op: copy
      from: person.se_line13
  - id: person.sep_s3
    printed: "Step 3"
    label: "Step 3"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.sep_s1
      take: person.sep_s2
  - id: person.sep_s5
    printed: "Step 5"
    label: "Step 5"
    type: NonNegDollars
    expr:
      op: prorate
      amount: person.sep_s3
      part: person.h_sep_rate_cents
      whole: person.h_sep_whole
      places: 3
  - id: person.sep_s6
    printed: "Step 6"
    label: "Step 6"
    type: NonNegDollars
    expr:
      op: prorate
      amount: person.h_ret_comp
      part: person.h_sep_rate_cents
      whole: person.h_100_cents
      places: 6
  - id: person.sep_s7
    printed: "Step 7"
    label: "Step 7"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.sep_s5, person.sep_s6]
  - id: person.sep_s8
    printed: "Step 8"
    label: "Step 8"
    type: NonNegDollars
    expr:
      op: param
      ref: ret.sep_dollar_limit
  - id: person.sep_s21
    printed: "Step 21"
    label: "Step 21"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr:
      op: smaller_of
      of: [person.sep_s7, person.sep_s8]
    note: "The supplied excerpts give steps 1 through 8 and 21 but not the elective-deferral and catch-up steps 9 through 20; this reading assumes no such deferrals and returns the smaller of step 7 and the step 8 dollar limit."
  - id: person.edu_line27
    printed: "27"
    label: "27"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.h_edu_net, person.h_aoc_cap]
  - id: person.edu_line28
    printed: "28"
    label: "28"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.edu_line27
      take: {const: 200000}
  - id: person.edu_line29
    printed: "29"
    label: "29"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.edu_line28
      rate: {param: aoc.second_rate}
  - id: person.edu_line30
    printed: "30"
    label: "30"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.edu_line28, {const: 0}]}
          then: person.edu_line27
        - guard: {op: test, ne: [person.edu_line28, {const: 0}]}
          then: person.h_edu_line30_add
  - id: person.edu_line31
    printed: "31"
    label: "31"
    type: NonNegDollars
    expr:
      op: copy
      from: person.h_edu_llc_net
  - id: person.one
    printed: "(helper)"
    label: "one"
    type: Count
    expr:
      op: param
      ref: person.one
  - id: person.educator_deduction
    printed: "(helper)"
    label: "educator deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.eligible_educator, {const: true}]}
          then: person.h_educator_min
        - guard: {op: test, eq: [person.eligible_educator, {const: false}]}
          then: person.zero
  - id: person.hsa_forms
    printed: "(helper)"
    label: "HSA forms"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
  - id: person.hsa_split
    printed: "(helper)"
    label: "HSA split forms"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where: {op: test, eq: [f8889.split, {const: true}]}
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "HSA agreed allocations"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where: {op: test, eq: [f8889.allocation, {const: "agreed"}]}
  - id: person.hsa_step1
    printed: "(helper)"
    label: "HSA step 1"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f8889
      field: f8889.step1
  - id: person.hsa_share
    printed: "(helper)"
    label: "HSA share"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f8889
      field: f8889.share
  - id: person.hsa_deduction
    printed: "(helper)"
    label: "HSA deduction"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f8889
      field: f8889.line13
  - id: person.hsa_taxable
    printed: "(helper)"
    label: "HSA taxable distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f8889
      field: f8889.line16
  - id: person.hsa_addtax
    printed: "(helper)"
    label: "HSA additional tax"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f8889
      field: f8889.line17b
  - id: person.tip_employers
    printed: "(helper)"
    label: "tip employers"
    type: Count
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.one
  - id: person.tip_total
    printed: "(helper)"
    label: "tip total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.col_d
  - id: person.tip_reported
    printed: "(helper)"
    label: "tip reported"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.amount
  - id: person.ot_employers
    printed: "(helper)"
    label: "overtime employers"
    type: Count
    expr:
      op: sum_over
      collection: otjob
      field: otjob.one
  - id: person.ot_total
    printed: "(helper)"
    label: "overtime total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: otjob
      field: otjob.col_b
  - id: person.box1
    printed: "(helper)"
    label: "W-2 box 1 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box1
  - id: person.box2
    printed: "(helper)"
    label: "W-2 box 2 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box2
  - id: person.ira_amount_a
    printed: "(helper)"
    label: "IRA distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.amount_a
      where:
        op: test
        any:
          - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: person.ira_taxable
    printed: "(helper)"
    label: "IRA taxable amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.ira_taxable
      where:
        op: test
        any:
          - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: person.ira_rollovers
    printed: "(helper)"
    label: "IRA rollovers"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where:
        op: test
        all:
          - op: test
            any:
              - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
              - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          - {op: test, eq: [retirement.has_rollover, {const: true}]}
  - id: person.plan_amount_a
    printed: "(helper)"
    label: "plan distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.amount_a
      where: {op: test, eq: [retirement.account, {const: "plan"}]}
  - id: person.plan_taxable
    printed: "(helper)"
    label: "plan taxable amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.plan_taxable
      where: {op: test, eq: [retirement.account, {const: "plan"}]}
  - id: person.plan_rollovers
    printed: "(helper)"
    label: "plan rollovers"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where:
        op: test
        all:
          - {op: test, eq: [retirement.account, {const: "plan"}]}
          - {op: test, eq: [retirement.has_rollover, {const: true}]}
  - id: person.sav_dist
    printed: "(helper)"
    label: "savers distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.sav_amount
  - id: person.medicare5
    printed: "(helper)"
    label: "W-2 box 5 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box5
  - id: person.medicare6
    printed: "(helper)"
    label: "W-2 box 6 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box6
  - id: person.sc_count
    printed: "(helper)"
    label: "Schedule C count"
    type: Count
    expr:
      op: sum_over
      collection: sc
      field: sc.one
  - id: person.ho_count
    printed: "(helper)"
    label: "home-office business count"
    type: Count
    expr:
      op: sum_over
      collection: sc
      field: sc.one
      where: {op: test, eq: [sc.ho_uses, {const: true}]}
  - id: person.mq_q4
    printed: "(helper)"
    label: "mid-quarter fourth-quarter basis"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.mq_q4
  - id: person.mq_total
    printed: "(helper)"
    label: "mid-quarter total basis"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.mq_total
  - id: person.cost179
    printed: "(helper)"
    label: "section 179 cost"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.cost179
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "section 179 nonlisted property"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.cost179
      take: person.s179_listed
  - id: person.s179_listed
    printed: "(helper)"
    label: "section 179 listed property"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.cost179_v
  - id: person.income179
    printed: "(helper)"
    label: "section 179 business income"
    type: Dollars
    expr:
      op: copy
      from: person.sc_total
  - id: person.sc_total
    printed: "(helper)"
    label: "Schedule C total"
    type: Dollars
    expr:
      op: sum_over
      collection: sc
      field: sc.line31
  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE line 6"
    type: NonNegDollars
    refuses: [person.se_screen, person.rrta]
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ge: [person.h_se_base, {param: se.floor}]}
          then: person.h_se_base
        - guard: {op: test, not: {op: test, ge: [person.h_se_base, {param: se.floor}]}}
          then: person.zero
  - id: person.se_line12
    printed: "(helper)"
    label: "Schedule SE line 12"
    type: NonNegDollars
    refuses: [person.se_screen, person.rrta]
    expr:
      op: sum
      of: [person.h_se_line10, person.h_se_line11]
  - id: person.se_line13
    printed: "(helper)"
    label: "Schedule SE line 13"
    type: NonNegDollars
    refuses: [person.se_screen, person.rrta]
    expr:
      op: multiply_rate
      amount: person.se_line12
      rate: {param: se.rate_50}
  - id: person.s16
    printed: "(helper)"
    label: "self-employed SEP and SIMPLE deduction"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.plan, {const: "none"}]}
          then: person.zero
        - guard: {op: test, eq: [person.plan, {const: "sep"}]}
          then: person.h_sep_allowed
        - guard: {op: test, eq: [person.plan, {const: "simple"}]}
          then: person.h_simple_allowed
  - id: person.positive_profits
    printed: "(helper)"
    label: "positive business profits"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.profit_pos
  - id: person.sehi
    printed: "(helper)"
    label: "self-employed health insurance deduction"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sc
      field: sc.f7206_line14
  - id: person.qbi
    printed: "(helper)"
    label: "qualified business income"
    type: Dollars
    refuses: [qbi.unsupported]
    expr:
      op: sum_over
      collection: sc
      field: sc.qbi
  - id: person.eic_se
    printed: "(helper)"
    label: "self-employment earned income for EIC"
    type: Dollars
    expr:
      op: copy
      from: person.h_se_after_tax
  - id: person.sc_1a
    printed: "(helper)"
    label: "statutory employee businesses"
    type: Count
    expr:
      op: sum_over
      collection: sc
      field: sc.one
      where: {op: test, eq: [sc.statutory, {const: true}]}
  - id: person.dc_benefits
    printed: "(helper)"
    label: "dependent care benefits"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.dc_benefits
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "has dependent care benefits"
    type: Bool
    expr:
      op: test
      gt: [person.h_dc_box10_count, {const: 0, type: Count}]
  - id: person.dc_earned
    printed: "(helper)"
    label: "earned income for dependent care"
    type: Dollars
    expr:
      op: sum
      of: [person.box1, person.eic_se]
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "earned income for dependent care spouse column"
    type: Dollars
    expr:
      op: copy
      from: person.dc_earned
  - id: person.sav_ineligible
    printed: "(helper)"
    label: "savers credit ineligible"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, not: {op: test, eq: [person.sav_born, {const: true}]}}
        - {op: test, eq: [person.sav_claimed, {const: true}]}
        - {op: test, eq: [person.sav_student, {const: true}]}
  - id: person.sav_line1
    printed: "(helper)"
    label: "savers credit line 1"
    type: NonNegDollars
    refuses: [person.sav_able]
    expr:
      op: sum
      of: [person.ira_trad, person.sav_roth]
  - id: person.sav_line2
    printed: "(helper)"
    label: "savers credit line 2"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.h_w2_sav_deferral, person.sav_voluntary]
  - id: person.ira_contrib
    printed: "(helper)"
    label: "traditional IRA contributions"
    type: NonNegDollars
    expr:
      op: copy
      from: person.ira_trad
  - id: person.ira_cov
    printed: "(helper)"
    label: "covered by retirement plan"
    type: Bool
    expr:
      op: copy
      from: person.ira_work_plan
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA deduction worksheet line 2"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_cov, {const: true}]}
          then: person.h_ira_line2_cov
        - guard: {op: test, eq: [person.ira_cov, {const: false}]}
          then: person.h_ira_line2_nocov
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA deduction worksheet line 6"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_cov, {const: false}]}
          then: person.zero
        - guard: {op: test, eq: [person.ira_cov, {const: true}]}
          then: person.h_ira_line6_calc
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA deduction worksheet line 7"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_cov, {const: false}]}
          then: person.h_ira_limit
        - guard:
            op: test
            all:
              - {op: test, eq: [person.ira_cov, {const: true}]}
              - {op: test, gt: [person.ira_line6, {const: 0}]}
          then: person.h_ira_line7_min
        - guard:
            op: test
            all:
              - {op: test, eq: [person.ira_cov, {const: true}]}
              - {op: test, eq: [person.ira_line6, {const: 0}]}
          then: person.zero
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA deduction"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.h_ira_min1, person.ira_contrib]
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "nondeductible IRA contribution"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.ira_contrib
      take: person.ira_deduction
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Form 8606 required"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [person.ira_nondeductible, {const: 0}]}
        - op: test
          all:
            - {op: test, eq: [person.ira_dist, {const: true}]}
            - {op: test, gt: [person.ira_basis, {const: 0}]}
        - op: test
          all:
            - {op: test, eq: [person.ira_dist, {const: true}]}
            - {op: test, eq: [person.ira_basis_adjusted, {const: true}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2"
    type: NonNegDollars
    expr:
      op: copy
      from: person.ira_basis
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "IRA distribution gate"
    type: Bool
    expr:
      op: copy
      from: person.ira_dist
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14"
    type: NonNegDollars
    expr:
      op: copy
      from: person.h_ira_basis_plus
    note: "The excerpts do not give all Form 8606 Part I lines needed to reduce basis for distributions or conversions; this reading carries basis plus 2025 nondeductible contributions."
  - id: person.ira_ssb
    printed: "(helper)"
    label: "IRA deduction for social security worksheet"
    type: NonNegDollars
    expr:
      op: copy
      from: person.ira_deduction
  - id: person.ira_se
    printed: "(helper)"
    label: "self-employment earned income for IRA"
    type: NonNegDollars
    expr:
      op: copy
      from: person.h_ira_se_pos
  - id: person.edu_kid
    printed: "(helper)"
    label: "student child condition for refundable education credit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.edu_parent, {const: true}]}
        - op: test
          any:
            - {op: test, not: {op: test, eq: [person.edu_born_2007, {const: true}]}}
            - op: test
              all:
                - {op: test, not: {op: test, eq: [person.edu_born_2002, {const: true}]}}
                - {op: test, eq: [person.edu_fulltime, {const: true}]}
                - {op: test, eq: [person.edu_half_support, {const: true}]}
    note: "The excerpts give age conditions by birth-date input rather than exact ages; this reading treats not being born before January 2, 2007 as the under-19 branch and uses the under-24 full-time/half-support branch."
  - id: person.x_l1
    printed: "(helper)"
    label: "Form 5329 line 1"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l1
  - id: person.x_l2_all
    printed: "(helper)"
    label: "Form 5329 line 2 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l2
  - id: person.x_l1_s
    printed: "(helper)"
    label: "Form 5329 SIMPLE line 1"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l1_s
  - id: person.x_l2_s
    printed: "(helper)"
    label: "Form 5329 SIMPLE line 2"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l2_s
  - id: person.x_tax
    printed: "(helper)"
    label: "Form 5329 early distribution tax"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l4
  - id: person.x_must
    printed: "(helper)"
    label: "Form 5329 required count"
    type: Count
    expr:
      op: sum_over
      collection: f5329
      field: f5329.one
      where: {op: test, eq: [f5329.must, {const: true}]}
  - id: person.x_c05
    printed: "(helper)"
    label: "exception 05 amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.l2_e05
  - id: person.x_two23
    printed: "(helper)"
    label: "more than one exception"
    type: Bool
    expr:
      op: test
      gt: [person.h_ret_exc_count, {const: 1, type: Count}]
  - id: person.x_limited_sum
    printed: "(helper)"
    label: "limited exception amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.exc_capped
  - id: person.x_other_exc
    printed: "(helper)"
    label: "other exception amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.l2
  - id: person.x_limit_binds
    printed: "(helper)"
    label: "exception dollar limit binds"
    type: Bool
    expr:
      op: test
      gt: [person.h_ret_exc_raw, person.h_ret_exc_capped]
  - id: person.x_hsa_excess
    printed: "(helper)"
    label: "excess HSA contributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: f5329
      field: f5329.l48
  - id: person.h_ss_excess
    printed: "(helper)"
    label: "excess social security withholding"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.withheld
      take: {param: ss.limit}
  - id: person.h_one_cent
    printed: "(helper)"
    label: "one cent"
    type: NonNegDollars
    expr:
      op: param
      ref: sc.one_cent
  - id: person.h_100_cents
    printed: "(helper)"
    label: "one hundred cents"
    type: NonNegDollars
    expr:
      op: param
      ref: sc.hundred_cents
  - id: person.h_sep_rate_cents
    printed: "(helper)"
    label: "SEP rate in cents"
    type: NonNegDollars
    expr:
      op: multiply_count
      amount: person.h_one_cent
      count: person.sep_rate
  - id: person.h_sep_whole
    printed: "(helper)"
    label: "SEP rate plus one hundred"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.h_sep_rate_cents, person.h_100_cents]
  - id: person.h_ret_comp
    printed: "(helper)"
    label: "annual compensation limit"
    type: NonNegDollars
    expr:
      op: param
      ref: ret.comp_limit
  - id: person.h_educator_max
    printed: "(helper)"
    label: "educator expense maximum"
    type: NonNegDollars
    expr:
      op: param
      ref: s1.educator_max
  - id: person.h_educator_min
    printed: "(helper)"
    label: "educator expense allowed"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.educator_expenses, person.h_educator_max]
  - id: person.h_edu_total
    printed: "(helper)"
    label: "education expenses"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.edu_inst, person.edu_mat]
  - id: person.h_edu_adj
    printed: "(helper)"
    label: "education expense adjustments"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.edu_a2025, person.edu_a2026, person.edu_refunds]
  - id: person.h_edu_net
    printed: "(helper)"
    label: "adjusted education expenses"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.h_edu_total
      take: person.h_edu_adj
  - id: person.h_edu_llc_net
    printed: "(helper)"
    label: "adjusted institution education expenses"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.edu_inst
      take: person.h_edu_adj
  - id: person.h_aoc_cap
    printed: "(helper)"
    label: "American opportunity expense cap"
    type: NonNegDollars
    expr:
      op: param
      ref: aoc.expense_cap
  - id: person.h_2000
    printed: "(helper)"
    label: "two thousand dollars"
    type: NonNegDollars
    expr:
      op: param
      ref: aoc.full_band
  - id: person.h_edu_line30_add
    printed: "(helper)"
    label: "line 29 plus two thousand dollars"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.h_2000, person.edu_line29]
  - id: person.h_dc_box10_count
    printed: "(helper)"
    label: "W-2s with dependent care benefits"
    type: Count
    expr:
      op: sum_over
      collection: w2
      field: w2.one
      where: {op: test, eq: [w2.has_box10, {const: true}]}
  - id: person.h_w2_sav_deferral
    printed: "(helper)"
    label: "W-2 retirement deferrals total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.sav_deferral
  - id: person.h_ss_box3
    printed: "(helper)"
    label: "W-2 box 3 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box3
  - id: person.h_ss_box7
    printed: "(helper)"
    label: "W-2 box 7 total"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: w2
      field: w2.box7
  - id: person.h_ss_wages
    printed: "(helper)"
    label: "social security wages and tips"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.h_ss_box3, person.h_ss_box7]
  - id: person.h_ss_base
    printed: "(helper)"
    label: "social security wage base"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.base
  - id: person.h_sc_total_pos
    printed: "(helper)"
    label: "nonnegative Schedule C total"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.sc_total
      take: {const: 0}
  - id: person.h_se_base
    printed: "(helper)"
    label: "self-employment earnings base"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.h_sc_total_pos
      rate: {param: se.rate_9235}
  - id: person.h_se_line9
    printed: "(helper)"
    label: "Schedule SE line 9"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.h_ss_base
      take: person.h_ss_wages
  - id: person.h_se_min
    printed: "(helper)"
    label: "smaller of line 6 and line 9"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.se_line6, person.h_se_line9]
  - id: person.h_se_line10
    printed: "(helper)"
    label: "Schedule SE line 10"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.h_se_min
      rate: {param: se.rate_124}
  - id: person.h_se_line11
    printed: "(helper)"
    label: "Schedule SE line 11"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.se_line6
      rate: {param: se.rate_029}
  - id: person.h_se_after_tax
    printed: "(helper)"
    label: "self-employment earnings after deduction"
    type: Dollars
    expr:
      op: subtract
      from: person.sc_total
      take: person.se_line13
  - id: person.h_se_after_tax2
    printed: "(helper)"
    label: "self-employment earnings after retirement deduction"
    type: Dollars
    expr:
      op: subtract
      from: person.h_se_after_tax
      take: person.s16
  - id: person.h_ira_se_pos
    printed: "(helper)"
    label: "nonnegative self-employment earnings"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.h_se_after_tax2
      take: {const: 0}
  - id: person.h_sep_allowed
    printed: "(helper)"
    label: "SEP contribution allowed"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.sep_contrib, person.sep_s21]
  - id: person.h_simple_allowed
    printed: "(helper)"
    label: "SIMPLE contribution allowed"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.simple_deferral, person.simple_employer]
  - id: person.h_s1_ira_total
    printed: "(helper)"
    label: "Schedule 1 deductions for IRA worksheet"
    type: NonNegDollars
    expr:
      op: sum
      of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line23, s1.line25]
  - id: person.h_ira_line5
    printed: "(helper)"
    label: "IRA worksheet line 5"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: f1040.line9
      take: person.h_s1_ira_total
  - id: person.h_ira_line2_cov
    printed: "(helper)"
    label: "IRA worksheet line 2 covered"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.line2
  - id: person.h_ira_line2_nocov
    printed: "(helper)"
    label: "IRA worksheet line 2 not covered"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.line2_not_covered
  - id: person.h_ira_line6_calc
    printed: "(helper)"
    label: "IRA worksheet line 6 computed"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.ira_line2
      take: person.h_ira_line5
  - id: person.h_ira_limit_50
    printed: "(helper)"
    label: "IRA limit age 50"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.limit_50
  - id: person.h_ira_limit_under
    printed: "(helper)"
    label: "IRA limit under age 50"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.limit
  - id: person.h_ira_limit
    printed: "(helper)"
    label: "IRA contribution limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_age50, {const: true}]}
          then: person.h_ira_limit_50
        - guard: {op: test, eq: [person.ira_age50, {const: false}]}
          then: person.h_ira_limit_under
  - id: person.h_ira_product_70
    printed: "(helper)"
    label: "IRA phaseout product 70 percent"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.ira_line6
      rate: {param: ira.rate_70}
  - id: person.h_ira_product_80
    printed: "(helper)"
    label: "IRA phaseout product 80 percent"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.ira_line6
      rate: {param: ira.rate_80}
  - id: person.h_ira_product_35
    printed: "(helper)"
    label: "IRA phaseout product 35 percent"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.ira_line6
      rate: {param: ira.rate_35}
  - id: person.h_ira_product_40
    printed: "(helper)"
    label: "IRA phaseout product 40 percent"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: person.ira_line6
      rate: {param: ira.rate_40}
  - id: person.h_ira_line7_product
    printed: "(helper)"
    label: "IRA worksheet line 7 product"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                any:
                  - {op: test, eq: [f1040.status, {const: "mfj"}]}
                  - {op: test, eq: [f1040.status, {const: "qss"}]}
              - {op: test, eq: [person.ira_age50, {const: true}]}
          then: person.h_ira_product_40
        - guard:
            op: test
            all:
              - op: test
                any:
                  - {op: test, eq: [f1040.status, {const: "mfj"}]}
                  - {op: test, eq: [f1040.status, {const: "qss"}]}
              - {op: test, eq: [person.ira_age50, {const: false}]}
          then: person.h_ira_product_35
        - guard:
            op: test
            all:
              - op: test
                not:
                  op: test
                  any:
                    - {op: test, eq: [f1040.status, {const: "mfj"}]}
                    - {op: test, eq: [f1040.status, {const: "qss"}]}
              - {op: test, eq: [person.ira_age50, {const: true}]}
          then: person.h_ira_product_80
        - guard:
            op: test
            all:
              - op: test
                not:
                  op: test
                  any:
                    - {op: test, eq: [f1040.status, {const: "mfj"}]}
                    - {op: test, eq: [f1040.status, {const: "qss"}]}
              - {op: test, eq: [person.ira_age50, {const: false}]}
          then: person.h_ira_product_70
  - id: person.h_ira_line7_rounded
    printed: "(helper)"
    label: "IRA worksheet line 7 rounded up"
    type: NonNegDollars
    expr:
      op: round
      of: person.h_ira_line7_product
      unit: 1000
      rule: up
  - id: person.h_ira_min
    printed: "(helper)"
    label: "IRA worksheet minimum"
    type: NonNegDollars
    expr:
      op: param
      ref: ira.min
  - id: person.h_ira_line7_min
    printed: "(helper)"
    label: "IRA worksheet line 7 floored at minimum"
    type: NonNegDollars
    expr:
      op: larger_of
      of: [person.h_ira_line7_rounded, person.h_ira_min]
  - id: person.h_ira_earned
    printed: "(helper)"
    label: "IRA earned income"
    type: Dollars
    expr:
      op: sum
      of: [person.box1, person.h_se_after_tax2]
  - id: person.h_ira_earned_pos
    printed: "(helper)"
    label: "nonnegative IRA earned income"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: person.h_ira_earned
      take: {const: 0}
  - id: person.h_ira_min1
    printed: "(helper)"
    label: "smaller of IRA line 7 and earned income"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [person.ira_line7, person.h_ira_earned_pos]
  - id: person.h_ira_basis_plus
    printed: "(helper)"
    label: "IRA basis plus nondeductible contributions"
    type: NonNegDollars
    expr:
      op: sum
      of: [person.ira_basis, person.ira_nondeductible]
  - id: person.h_ret_exc_count
    printed: "(helper)"
    label: "retirement distributions with exceptions"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where: {op: test, eq: [retirement.has_exception, {const: true}]}
  - id: person.h_ret_exc_raw
    printed: "(helper)"
    label: "raw exception amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.exc_amount
  - id: person.h_ret_exc_capped
    printed: "(helper)"
    label: "capped exception amount"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.exc_capped
```
