# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5acd7748711e48a20b6b569cd453aba96958feda7e44fb1d7eb742f56cf15cdd |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 32f211285c7e50d0bed2b756fae9b033a4350676800d8634d69fe0738fc18510 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0b36a8a0f52fc76d4f7330c090070e80439bb12436d36e0b1788c257489b6c1b |
| printed lines compared | 99 |
| agree / disagree / missing | 42 / 57 / 0 |
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

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dcprov, div, f1095a, f4562, f4952, f8960, f8962, ftc, g28, gift, sales, sb, sdtw, u1250 |
| shared page | asset, carloan, dependent, eic, f1040, f2441, f5329, f8606, f8863, f8880, f8889, f8959, f8995, f8995a, household, interest, ira, ltc, oi8z, otjob, qbi, refund, retirement, s1, s179, s1a, s2, s3, s8812, sa, sc, scope, scveh, sd, sli, ssb, tipjob, w2 |
| worksheet | qdcg |

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

Ruling: model error; i1040gi p. 93, Line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025.". The reply asks person.eligible_educator of filers with no educator expenses entered; the project skips it when the expense is zero. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,124 of 5,033 agree; 1,888 candidate-unknown, 21 project-unknown; on returns the full interview completes: 204 candidate-unknown. Project stands.

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

### person.hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

### person.hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.share", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; i8889 p. 7, Line 6. The project's helper is read only under the married-family split of line 6 and is zero otherwise; the reply omits that gate (spot-checked: classm.s3.3.deepseek taxpayer, project split false and $0, candidate $712.50), so the amount differs on a helper no return reads outside the split. No printed Form 8889 line was compared here. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,009 of 5,033 agree; 18 candidate-refuses, 6 candidate-unknown; on returns the full interview completes: none. Project stands.

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
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "ne"}}
```

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### person.ira_taxable — Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "ne"}}
```

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### person.ira_rollovers — Number of this person's IRA distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "ne"}], "test": "all"}}
```

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

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

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### person.plan_taxable — Taxable pension and annuity distributions on this person's Forms 1099-R (line 5b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}}
```

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

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

Ruling: representation; i1040gi pp. 26-28, Lines 4a to 5b. The same answer is read through a ref where the project uses an input reference. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

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
{"collection": "sc", "field": "sc.s179_elected", "op": "sum_over", "where": null}
```

Second transcription's note: The catalog offers no Schedule C-level split between line 6 (property other than listed) and line 7 (listed property from Part V). A person-level line may read only its own child collection, so asset and vehicle entries cannot be summed here. The only Schedule C aggregate, sc.s179_elected, is used. This is a limitation.

Ruling: model error; i4562 p. 5, Line 7, "Enter the amount that you elected to expense for listed property (defined earlier) on line 29 here". As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply puts every section 179 amount in the non-listed total (classm.eic.3.deepseek, a listed asset with $10,918 elected: project listed $10,918 and non-listed $0, candidate $0 and $10,918; stage14.veh.suv_179 $31,300). The totals agree; listed property belongs on Form 4562 line 29. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,857 of 5,033 agree; 100 candidate-refuses, 76 value; on returns the full interview completes: 54 value. Project stands.

### person.s179_listed — Section 179 elected on listed property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f29", "op": "sum_over", "where": null}
```

Second:

```json
{"const": 0}
```

Second transcription's note: LIMITATION: no Schedule C-level aggregate of the section 179 election on listed property (Part V) is in the catalog, and nested vehicle entries cannot be read from a person entry. The listed amount is counted within person.s179_nonlisted (sc.s179_elected). This line holds zero to avoid counting it twice. A published Schedule C aggregate is needed to separate it.

Ruling: model error; i4562 p. 5, Line 7. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply's listed total is the constant zero (the 54 completed values mirror person.s179_nonlisted). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,834 of 5,033 agree; 100 project-refuses, 76 value, 23 project-unknown; on returns the full interview completes: 54 value. Project stands.

### person.income179 — Business net profit or loss without section 179, this person
Status: **AGREE**

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

Ruling: scope; i1040sc p. 15, Line 32, Some investment is not at risk: "Be sure to attach Form 6198". New to the open list (the line agreed in fix round 2): the reply sums sc.line31, the project sc.result, which differ only for a loss with amounts not at risk, refused at sc.not_at_risk (stage14.refuse.at_risk, refused). No value differs. Fix round 3 re-check: the only project change since fix round 2 is BUG-0256 (person.tin: an expired ITIN counts only if renewed by the due date), which this line does not read. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,031 of 5,033 agree; 1 project-refuses, 1 project-unknown; on returns the full interview completes: none. Project stands.

### person.se_line6 — Schedule SE line 6 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, "You must file Schedule SE if:". The reply reads its own self-employment screen (person.se_screen) for every person, including persons with no Schedule C, and refuses on it where the project computes zero or the amount. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,183 of 5,033 agree; 1,701 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.se_line12 — Schedule SE line 12 (self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, "You must file Schedule SE if:". The reply reads its own self-employment screen (person.se_screen) for every person, including persons with no Schedule C, and refuses on it where the project computes zero or the amount. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,183 of 5,033 agree; 1,701 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.se_line13 — Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, "You must file Schedule SE if:". The reply reads its own self-employment screen (person.se_screen) for every person, including persons with no Schedule C, and refuses on it where the project computes zero or the amount. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,183 of 5,033 agree; 1,701 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"of": [{"input": "person.simple_employer"}, {"alternatives": [{"guard": {"args": [{"const": "match"}, {"input": "person.simple_kind"}], "test": "eq"}, "then": {"of": [{"amount": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ret.match_rate"}}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"of": [{"keys": [{"input": "person.simple_age"}], "op": "keyed_lookup", "table": "simple_catchup"}, {"param": "ret.simple_limit"}], "op": "sum"}], "op": "smaller_of"}, {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "nonelective"}, {"input": "person.simple_kind"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"param": "ret.comp_limit"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "ret.nonelective_rate"}}}], "op": "choose"}], "op": "smaller_of"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"of": [{"keys": [{"input": "person.simple_age"}], "op": "keyed_lookup", "table": "simple_catchup"}, {"param": "ret.simple_limit"}], "op": "sum"}], "op": "smaller_of"}, {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error; p560 p. 39, "Enter your actual contribution, not to exceed your maximum deductible contribution, on Schedule 1 (Form 1040), line 16". The reply asks the plan screen and the plan answers of persons who have no Schedule C (and so no self-employed plan the project computes). The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. New this round: 117 completed-return value differences, all on class M fixtures of the deepseek family that answer person.plan for a person with no Schedule C (spot-checked: classm.clcw26.2.deepseek and classm.s3.4.deepseek, plan simple, no Schedule C entry: project $0, candidate $5,199 and $8,925). The project reads person.plan only with a Schedule C, so the interview never asks these answers; the reply computes a self-employed deduction without self-employment income, against p560 p. 39 ("net profit from line 31, Schedule C"). Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,007 of 5,033 agree; 1,963 candidate-unknown, 38 project-refuses, 25 candidate-refuses; on returns the full interview completes: 222 candidate-unknown. Project stands.

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
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}
```

Second transcription's note: Lines 4b (optional methods) and 5a (church employee income) are screened by person.se_screen, so 1c equals Schedule SE line 3.

Ruling: model error; i1040sse p. 1, Who Must File Schedule SE, "You must file Schedule SE if:". The reply reads its own self-employment screen (person.se_screen) for every person, including persons with no Schedule C, and refuses on it where the project computes zero or the amount. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,183 of 5,033 agree; 1,701 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **AGREE**

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

Ruling: representation; i2441 p. 4, Part III, Form W-2 box 10. Triage found no difference: Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second transcription's note: Line 1z items other than 1a (Form W-2 box 1) are screened (scope.other_income), apart from 1e. Line 1e is a return-level amount from Form 2441 line 26 and cannot be attributed to one person, so it is not included. A self-employment loss reduces earned income, as the instructions require.

Ruling: model error; i2441 p. 4, Lines 4 and 5, "Earned income for figuring the credit generally includes the following amounts.". The reply reads person.se_screen for every person to figure earned income. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. The two value differences (classm.carloan.1, generated 198) are on refused returns, where the reply's line 31 reading meets a refused Schedule C. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,162 of 5,033 agree; 1,670 candidate-unknown, 144 candidate-refuses, 40 value, 16 project-refuses, 1 project-unknown; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without l
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second transcription's note: Line 12 excludes box 10 amounts already reported as wages in box 1, and the excluded benefits are not in box 1. So the line 18/19 earned income equals the credit earned income here.

Ruling: model error; i2441 p. 5, Line 18, "for purposes of lines 18 and 19, earned income doesn’t include any dependent care benefits shown on line 12". As person.dc_earned. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. The person-dep change to this line (PENDING-1, T-121) is its label only; the sum (W-2 box 1 plus net self-employment earnings, without line 1e) is unchanged and equals the reply's, and the new f2441.line13_earned refusal sits on Form 2441 line 25, not here. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,201 of 5,033 agree; 1,683 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### person.sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return, or a stu
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}], "test": "any"}
```

Ruling: ambiguity; amb.2025.savers_ineligible_column (owner decision). As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply reads person.sav_claimed where the project reads sa.dependent for the filer; the 1 completed value (generated 360) follows from that recorded reading, the 13 completed unknowns are partial records withholding sav_claimed. BUG-0392 (sav_claimed now asked whenever education expenses are paid) does not change this line. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,743 of 5,033 agree; 258 value, 28 candidate-unknown, 4 project-unknown; on returns the full interview completes: 13 candidate-unknown, 1 value. Project stands.

### person.sav_line1 — Form 8880 line 1 for this person (traditional IRA contributions for 2025, deductible or no
Status: **AGREE**

### person.sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "ne"}, "then": {"line": "zero"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: ambiguity; amb.2025.ira_covered (owner decision); f8880 p. 1, line 2. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply counts a SIMPLE deferral answered under person.plan without a Schedule C (classm.f1040.5.deepseek taxpayer: plan simple, simple_deferral $1,572, no Schedule C: project $10,797, candidate $12,369), which the recorded reading reads only with one; it also asks sav_excess where the project's gate does not (86 completed). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,295 of 5,033 agree; 1,526 candidate-unknown, 143 value, 52 candidate-refuses, 16 project-refuses, 1 project-unknown; on returns the full interview completes: 121 candidate-unknown, 68 value. Project stands.

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

Ruling: model error; i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction.". The reply asks person.ira_excess and person.ira_trad of persons the project does not ask them of. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,120 of 5,033 agree; 1,884 candidate-unknown, 28 project-unknown, 1 value; on returns the full interview completes: 209 candidate-unknown. Project stands.

### person.ira_cov — Covered by a retirement plan (worksheet line 1a or 1b for this person)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}
```

Ruling: ambiguity; amb.2025.ira_covered (owner decision). As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply treats person.plan as coverage without a Schedule C (classm.f8889.1.deepseek spouse: ira_work_plan No, plan sep: project not covered, candidate covered). The 5 completed project-unknowns (ira_work_plan, stage21.f1.lower_bound_still_decides spouse and partial records) are as before. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,373 of 5,033 agree; 596 value, 55 candidate-unknown, 9 project-unknown; on returns the full interview completes: 359 value, 11 candidate-unknown, 5 project-unknown. Project stands.

### person.ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second transcription's note: $246,000 applies to a person not covered only on a joint return where the other spouse is covered. Return-level gates (ira.lines2to6, ira.cov_gate) decide where lines 2-6 are used. The $89,000 amount for married filing separately and lived apart is not available from the keyed parameter, whose MFS value is $10,000. That case must be screened at return level.

Ruling: ambiguity; amb.2025.ira_covered; i1040gi p. 97, line 1, "skip lines 2 through 6". The reply changed: where nobody is covered (lines 2 to 6 skipped) it fills the not-covered amount and the project the status amount (classm.f8960.1.deepseek, head of household, not covered: project $89,000, candidate $246,000; 449 completed); both are values of a skipped helper read by no later line there. The other values are the coverage reading of person.ira_cov ($246,000 against $146,000 and the reverse). No IRA deduction differs (person.ira_deduction has no completed value difference). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,271 of 5,033 agree; 1,383 candidate-unknown, 1,374 value, 5 project-unknown; on returns the full interview completes: 753 value, 153 candidate-unknown, 3 project-unknown. Project stands.

### person.ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract li
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Ruling: ambiguity; amb.2025.ira_covered; i1040gi p. 97, lines 1 to 6. Inherits person.ira_line2: the values are the skipped-path line 2 amounts and the coverage reading carried through line 5 (for example classm.s2.1.deepseek $56,064 against $213,064). No IRA deduction differs. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,673 of 5,033 agree; 1,294 candidate-unknown, 981 value, 44 project-refuses, 32 project-unknown, 9 candidate-refuses; on returns the full interview completes: 685 value, 242 candidate-unknown, 3 project-unknown, 1 candidate-refuses. Project stands.

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Line 6 'No' (line 5 not less than line 2) means 'None of your IRA contributions are deductible' (STOP). That case gives zero, not the $200 minimum.

Ruling: ambiguity; amb.2025.ira_covered; i1040gi p. 97, line 7. The reply changed: the 161 completed values are now project $7,000 and candidate $0 on persons the reply counts as covered by person.plan without a Schedule C (classm.f8889.1.deepseek spouse: plan sep, no Schedule C, its line 6 $0 against the project's limit). No IRA deduction differs on the sample (no contribution on those records). The class changes from representation because the difference now follows the recorded coverage reading. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,487 of 5,033 agree; 261 value, 193 candidate-unknown, 44 candidate-refuses, 36 project-refuses, 12 project-unknown; on returns the full interview completes: 162 value, 67 candidate-unknown, 9 project-unknown. Project stands.

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 98, line 12, "enter the smallest of line 7a, 10, or 11a". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,252 of 5,033 agree; 2,220 candidate-unknown, 521 candidate-refuses, 24 project-unknown, 16 project-refuses; on returns the full interview completes: 328 candidate-unknown, 1 candidate-refuses. Project stands.

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"from": {"of": [{"input": "person.ira_trad"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}}
```

Ruling: model error; i8606 p. 2, Who Must File, "You made nondeductible contributions to a traditional IRA for 2025". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,252 of 5,033 agree; 2,221 candidate-unknown, 521 candidate-refuses, 24 project-unknown, 15 project-refuses; on returns the full interview completes: 328 candidate-unknown, 1 candidate-refuses. Project stands.

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "person.ira_basis"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"from": {"of": [{"input": "person.ira_trad"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}}], "test": "lt"}], "test": "any"}
```

Ruling: model error; i8606 p. 2, Who Must File, "You made nondeductible contributions to a traditional IRA for 2025". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,252 of 5,033 agree; 2,221 candidate-unknown, 521 candidate-refuses, 24 project-unknown, 15 project-refuses; on returns the full interview completes: 328 candidate-unknown, 1 candidate-refuses. Project stands.

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

Ruling: model error; i8606 p. 9, Line 2, "Generally, if this is the first year you are required to file Form 8606, enter -0-". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,077 of 5,033 agree; 1,911 candidate-unknown, 28 project-unknown, 17 project-refuses; on returns the full interview completes: 224 candidate-unknown. Project stands.

### person.ira_dist_gate — Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or Roth conv
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "person.ira_basis"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"from": {"of": [{"input": "person.ira_trad"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}}], "test": "lt"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}], "test": "all"}
```

Ruling: model error; i8606 p. 2, Who Must File. The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,642 of 5,033 agree; 1,855 candidate-unknown, 521 candidate-refuses, 15 project-refuses; on returns the full interview completes: 194 candidate-unknown, 1 candidate-refuses. Project stands.

### person.ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier ye
Status: **DISAGREE**

Project:

```json
{"collection": "f8606", "field": "f8606.line14", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"input": "person.ira_basis"}, {"from": {"of": [{"input": "person.ira_trad"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}}], "op": "sum"}
```

Ruling: model error; i8606 p. 2, Who Must File. The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,205 of 5,033 agree; 2,267 candidate-unknown, 521 candidate-refuses, 24 project-unknown, 16 project-refuses; on returns the full interview completes: 358 candidate-unknown, 1 candidate-refuses. Project stands.

### person.ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"of": [{"input": "person.ira_trad"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}], "op": "smaller_of"}, {"ref": "ira.line10"}], "op": "smaller_of"}
```

Second transcription's note: Not named by the IRS text. When IRA contributions are made and anyone is covered by a plan, the line 6a/6b instructions require Pub. 590-A (ssb.pub915 screen). Otherwise the deduction is the smallest of the limit, earned income (line 10) and contributions, independent of AGI. That is the reading used.

Ruling: model error; i1040gi p. 98, line 12, "enter the smallest of line 7a, 10, or 11a". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,376 of 5,033 agree; 2,123 candidate-unknown, 494 candidate-refuses, 24 project-unknown, 16 project-refuses; on returns the full interview completes: 288 candidate-unknown, 1 candidate-refuses. Project stands.

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"from": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"of": [{"input": "person.simple_employer"}, {"alternatives": [{"guard": {"args": [{"const": "match"}, {"input": "person.simple_kind"}], "test": "eq"}, "then": {"of": [{"amount": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ret.match_rate"}}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"of": [{"keys": [{"input": "person.simple_age"}], "op": "keyed_lookup", "table": "simple_catchup"}, {"param": "ret.simple_limit"}], "op": "sum"}], "op": "smaller_of"}, {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "nonelective"}, {"input": "person.simple_kind"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"param": "ret.comp_limit"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "ret.nonelective_rate"}}}], "op": "choose"}], "op": "smaller_of"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"of": [{"keys": [{"input": "person.simple_age"}], "op": "keyed_lookup", "table": "simple_catchup"}, {"param": "ret.simple_limit"}], "op": "sum"}], "op": "smaller_of"}, {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}], "op": "sum"}}], "op": "choose"}}
```

Ruling: model error; i1040gi p. 98, line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner". The reply asks IRA, basis, distribution, plan and self-employment answers of persons the project does not ask them of (no contribution, distribution or Schedule C), and refuses on its self-employment screen. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. The reply now sums sc.line31 where the project (and the previous reply) read sc.result; the two are equal except on a Schedule C loss limited by the cited at-risk screen (see person.sc_total), so this changes no computed amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,899 of 5,033 agree; 1,928 candidate-unknown, 165 candidate-refuses, 41 project-refuses; on returns the full interview completes: 229 candidate-unknown, 1 candidate-refuses. Project stands.

### person.edu_kid — Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of yo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0}, {"ref": "f8863.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8863.line7"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_born"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Second transcription's note: Ages at the end of 2025 are read from the birth-date questions. Born after Jan 1, 2008 means under 18. Born before Jan 2, 2008 but not before Jan 2, 2007 means age 18. Born before Jan 2, 2007 but not before Jan 2, 2002 means over 18 and under 24. This uses the rule that a person reaches an age on the day before the birthday.

Ruling: representation; i8863 p. 6, Line 7, "If you were under age 24 at the end of 2025 and the conditions listed below apply to you, you cannot claim any part of the American opportunity credit as a refundable credit". The project tests the Form 8863 conditions on this line; the reply leaves them to the form and asks the birth-date answers of every person, so it is unknown where the project gives no on a person with no education credit; no credit is read on the witnesses. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,421 of 5,033 agree; 1,569 candidate-unknown, 33 project-refuses, 10 value; on returns the full interview completes: 240 candidate-unknown. Project stands.

### person.x_l1 — Form 5329 line 1 for this person: early distributions includible in income
Status: **AGREE**

### person.x_l2_all — Exception amounts before the per-person limits
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}, {"of": [{"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}], "op": "sum"}
```

Ruling: model error; i5329 p. 5, Line 2, "Enter on line 2 the amount that you can exclude". The project sums each 1099-R entry's line 2 amount; the reply rebuilds line 2 from the exception caps and asks person.x_births and person.x_prior09 of every person, including persons with no early distribution (300 completed-return unknowns), and it leaves the exception 05 limit out (stage21.blind.e4, incomplete). Answers the source does not need. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,473 of 5,033 agree; 2,558 candidate-unknown, 2 value; on returns the full interview completes: 415 candidate-unknown. Project stands.

### person.x_l1_s — Line 1 amounts from code S distributions
Status: **AGREE**

### person.x_l2_s — Line 2 amounts from code S distributions
Status: **AGREE**

### person.x_tax — This person's Form 5329 taxes
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.tax", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"amount": {"of": [{"input": "person.x_hsa_value"}, {"collection": "f8889", "field": "f8889.excess_amt", "op": "sum_over", "where": null}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "f5329.excess_rate"}}, {"amount": {"from": {"from": {"collection": "retirement", "field": "retirement.l1", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}, {"of": [{"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}], "op": "sum"}}, "op": "subtract_floor0", "take": {"from": {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}}}, "op": "multiply_rate", "rate": {"param": "f5329.early_rate"}}, {"amount": {"from": {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}}, "op": "multiply_rate", "rate": {"param": "f5329.simple_rate"}}], "op": "sum"}
```

Ruling: model error; i5329 p. 5, Line 2, "Enter on line 2 the amount that you can exclude". The reply asks person.x_prior09 and the other exception answers of every person, including persons with no early distribution, which the project does not ask. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,568 of 5,033 agree; 2,459 candidate-unknown, 6 project-refuses; on returns the full interview completes: 425 candidate-unknown. Project stands.

### person.x_must — One if this person must file Form 5329
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f5329.l48"}], "test": "lt"}], "test": "any"}}
```

Second:

```json
{"of": [{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"input": "f8889.employer_in_box1"}], "test": "eq"}, {"args": [{"ref": "f8889.line8"}, {"ref": "f8889.line11"}], "test": "lt"}], "test": "all"}}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "early_1"}, {"ref": "retirement.code"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}], "test": "all"}}], "op": "sum"}
```

Second transcription's note: Form 5329 need not be filed when code 1 is shown on all Forms 1099-R and the tax is owed on the full amount. It must be filed for an exception or an excess HSA contribution.

Ruling: model error; i5329 p. 1, Who Must File. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply's must-file count omits the HSA excess part (123 completed, for example classm.f8889.1.deepseek spouse, project 1, candidate 0); and it counts a code 1 entry with an exception and a $0 distribution (generated 259: project 0, candidate 1). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 4,678 of 5,033 agree; 307 value, 45 project-refuses, 2 candidate-unknown, 1 project-unknown; on returns the full interview completes: 124 value. Project stands.

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

Ruling: model error; i5329 p. 5, Line 2, exception 05, distributions "to the extent you have deductible medical expenses that exceed 7.5% of your adjusted gross income". The reply sums the exception 05 amounts without that limit: stage21.blind.e6 $9,000 against the project's $7,475 (an incomplete record). Reclassified from representation: the reply changed and now drops the limit. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,032 of 5,033 agree; 1 value; on returns the full interview completes: none. Project stands.

### person.x_two23 — Exception 23 claimed on more than one distribution
Status: **AGREE**

### person.x_limited_sum — Exceptions 05, 09, 19, 22 and 23 within their limits
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Second:

```json
{"of": [{"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Ruling: model error; i5329 p. 5, Line 2 (exceptions 09, 19, 22 and 23 and their limits); p590b p. 27. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`); the reply now also asks the exception answers of every person (415 completed unknowns). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,474 of 5,033 agree; 2,559 candidate-unknown; on returns the full interview completes: 415 candidate-unknown. Project stands.

### person.x_other_exc — Exceptions without a fixed limit
Status: **DISAGREE**

Project:

```json
{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}
```

Second:

```json
{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}
```

Ruling: model error; i5329 p. 5, Line 2, exception 05. The reply leaves exception 05 in the unlimited remainder: stage21.blind.e6 $9,000 against $0 and stage21.blind.e7 (incomplete or refused records only). Reclassified from representation: the reply changed. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,028 of 5,033 agree; 5 value; on returns the full interview completes: none. Project stands.

### person.x_limit_binds — A limited exception over its limit on a person with a code S distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"of": [{"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}
```

Ruling: model error; i5329 p. 5, Line 2, "Enter on line 2 the amount that you can exclude". The reply asks person.x_prior09 and the other exception answers of every person, including persons with no early distribution, which the project does not ask. The candidate reads answers this line does not need on the project's interview (the differences are candidate-unknown, or a candidate refusal on a screen the source does not apply here); it gives no different completed-return amount. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,472 of 5,033 agree; 2,558 candidate-unknown, 2 value, 1 project-refuses; on returns the full interview completes: 415 candidate-unknown. Project stands.

### person.x_hsa_excess — This person's 2025 HSA excess contributions (Form 8889)
Status: **AGREE**

### employers — Total w2.one for this person
Status: **AGREE**

### overcount — Number of employers that withheld more than the limit
Status: **AGREE**

### over — Any employer withheld more than the limit
Status: **AGREE**

### wages — Total w2.wages for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.wages", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"collection": "w2", "field": "w2.box3", "op": "sum_over", "where": null}, {"collection": "w2", "field": "w2.box7", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: representation; i1040gi p. 117, Line 11; iw2w3 p. 18, boxes 3 and 7. The reply sums boxes 3 and 7; the project sums w2.wages (box 3 plus box 7). No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

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
{"args": [{"args": [{"const": false}, {"line": "over"}], "test": "eq"}, {"args": [{"const": 2, "type": "Count"}, {"line": "employers"}], "test": "le"}], "test": "all"}
```

Second transcription's note: The text says excess tax 'may have been withheld' when total wages are more than $176,100. Wages over the base are not used as a separate test. Without such wages, the excess over $10,918.20 computed on the next line is zero.

Ruling: model error; i1040gi p. 117, Line 11, "If you had more than one employer and total wages of more than $176,100, too much social security tax may have been withheld". The reply drops the total-wages condition (its note argues that withholding above $10,918.20 with no employer over the limit implies wages over the base, which holds only when each employer withheld 6.2%). The 308 completed-return differences are this helper on persons with two employers and wages under the base, where the printed credit is $0 either way (a scratch pair evaluation of person.credit in both graphs: 2 differences, none completed: ss.base.exact $0 against $0.01, generated 206 $0 against $183.87, both on box 4 above 6.2% of box 3). The reply gives a credit the source denies on such W-2s. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,816 of 5,033 agree; 1,212 value, 4 candidate-unknown, 1 project-unknown; on returns the full interview completes: 392 value. Project stands.

### excess — Withholding above $10,918.20, if any
Status: **AGREE**

### zero — No excess credit
Status: **AGREE**

### credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

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

Ruling: scope; p560 p. 39, Step 1. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply sums sc.line31 with no refusal; the project copies person.sc_total and refuses at person.se_screened (cited) where there is self-employment income not on a Schedule C. The 91 completed project-unknowns (person.se_screen, for example classm.f4952.1.deepseek taxpayer) are persons with no Schedule C on returns that do not use the worksheet; the 1 completed project-refuses is classm.ssb.5. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,195 of 5,033 agree; 1,690 project-unknown, 147 project-refuses, 1 candidate-refuses; on returns the full interview completes: 91 project-unknown, 1 project-refuses. Project stands.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: model error; p560 p. 39, Step 2. As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): it reads its own person.se_screen for every person (91 completed unknowns). executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 3,183 of 5,033 agree; 1,701 candidate-unknown, 147 candidate-refuses, 2 project-refuses; on returns the full interview completes: 91 candidate-unknown, 1 candidate-refuses. Project stands.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}}
```

Second:

```json
{"shown_when": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "value": {"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}}
```

Second transcription's note: The worksheet gives no floor for a loss. A negative result is held as zero, since no SEP deduction can arise from it.

Ruling: representation; p560 pp. 39-40, Deduction Worksheet for Self-Employed, Step 3. The formula is the project's; every difference is on an incomplete or refused record (the reply's person.rrta question and refusals reached through Steps 1 and 2); no completed return differs. The reply now adds shown_when person.plan == "sep"; the project's person worksheet computes and shows the Deduction Worksheet for Self-Employed steps for every person (display only, recorded under Low in the findings file); triage compares the project's display. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,003 of 5,033 agree; 20 candidate-unknown, 8 candidate-refuses, 2 project-refuses; on returns the full interview completes: none. Project stands.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}}
```

Second:

```json
{"shown_when": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "value": {"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}}
```

Second transcription's note: No table of Column B rates is supplied. The table rate equals rate ÷ (1 + rate) rounded to six decimal places (for example 10% gives 0.090909 and 25% gives 0.200000). This line reproduces it with prorate at 6 places. Non-whole rates are screened by person.plan_screen.

Ruling: representation; p560 pp. 39-40, Step 5. The prorate is the project's; every difference is on an incomplete or refused record; no completed return differs. The reply now adds shown_when person.plan == "sep"; the project's person worksheet computes and shows the Deduction Worksheet for Self-Employed steps for every person (display only, recorded under Low in the findings file); triage compares the project's display. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,003 of 5,033 agree; 20 candidate-unknown, 8 candidate-refuses, 2 project-refuses; on returns the full interview completes: none. Project stands.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **DISAGREE**

Project:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}
```

Ruling: representation; p560 p. 40, Step 6. The reply rounds to 2 places where the project uses 6; for the whole-percent rates the interview takes the results are the same. No difference. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}}
```

Second:

```json
{"shown_when": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "value": {"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}}
```

Ruling: representation; p560 pp. 39-40, Deduction Worksheet for Self-Employed, Step 7. The formula is the project's; every difference is on an incomplete or refused record (the reply's person.rrta question and refusals reached through Steps 1 and 2); no completed return differs. The reply now adds shown_when person.plan == "sep"; the project's person worksheet computes and shows the Deduction Worksheet for Self-Employed steps for every person (display only, recorded under Low in the findings file); triage compares the project's display. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,003 of 5,033 agree; 20 candidate-unknown, 8 candidate-refuses, 2 project-refuses; on returns the full interview completes: none. Project stands.

### Step 8 — Contribution dollar limit
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"param": "ret.sep_dollar_limit"}}
```

Second:

```json
{"shown_when": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "value": {"param": "ret.sep_dollar_limit"}}
```

Ruling: representation; p560 p. 40, Step 8, the dollar limit. Same parameter; the only disagreement is the visibility. The reply now adds shown_when person.plan == "sep"; the project's person worksheet computes and shows the Deduction Worksheet for Self-Employed steps for every person (display only, recorded under Low in the findings file); triage compares the project's display. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,033 of 5,033 agree; none; on returns the full interview completes: none. Project stands.

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"of": [{"line": "Step 7"}, {"line": "Step 8"}], "op": "smaller_of"}}
```

Second:

```json
{"shown_when": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "value": {"of": [{"line": "Step 7"}, {"line": "Step 8"}], "op": "smaller_of"}}
```

Second transcription's note: Steps 9-20 apply only to elective deferrals to the self-employed plan. Those are screened by person.plan_screen (SARSEP and other deferrals), so step 21 is the smaller of step 7 or step 8.

Ruling: representation; p560 pp. 39-40, Deduction Worksheet for Self-Employed, Step 21. The formula is the project's; every difference is on an incomplete or refused record (the reply's person.rrta question and refusals reached through Steps 1 and 2); no completed return differs. The reply now adds shown_when person.plan == "sep"; the project's person worksheet computes and shows the Deduction Worksheet for Self-Employed steps for every person (display only, recorded under Low in the findings file); triage compares the project's display. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 5,003 of 5,033 agree; 20 candidate-unknown, 8 candidate-refuses, 2 project-refuses; on returns the full interview completes: none. Project stands.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: model error; f8863 p. 2, line 27; p970 p. 11. The reply has the education lines read person.edu_over for every person (no f8863.paid gate), so it is unknown on returns with no education credit where the project hides the line (180 completed records, for example classm.f4952.1.deepseek); and it requires an issued TIN for the American opportunity credit, against p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (owner decision T-113 keeps that deeming): f1.t113.person_aoc_itin_applied (stage19.example.aoc_phaseout with the ITIN applied for) gives line 27 $0.00 where the project gives $4,000.00. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,677 of 5,033 agree; 2,355 candidate-unknown, 1 value; on returns the full interview completes: 306 candidate-unknown. Project stands.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: model error; f8863 p. 2, line 28; p970 p. 11. The reply has the education lines read person.edu_over for every person (no f8863.paid gate), so it is unknown on returns with no education credit where the project hides the line (180 completed records, for example classm.f4952.1.deepseek); and it requires an issued TIN for the American opportunity credit, against p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (owner decision T-113 keeps that deeming): f1.t113.person_aoc_itin_applied (stage19.example.aoc_phaseout with the ITIN applied for) gives line 27 $0.00 where the project gives $4,000.00. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,677 of 5,033 agree; 2,355 candidate-unknown, 1 value; on returns the full interview completes: 306 candidate-unknown. Project stands.

### 29 — Multiply line 28 by 25% (0.25)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: model error; f8863 p. 2, line 29; p970 p. 11. The reply has the education lines read person.edu_over for every person (no f8863.paid gate), so it is unknown on returns with no education credit where the project hides the line (180 completed records, for example classm.f4952.1.deepseek); and it requires an issued TIN for the American opportunity credit, against p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (owner decision T-113 keeps that deeming): f1.t113.person_aoc_itin_applied (stage19.example.aoc_phaseout with the ITIN applied for) gives line 27 $0.00 where the project gives $4,000.00. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,677 of 5,033 agree; 2,355 candidate-unknown, 1 value; on returns the full interview completes: 306 candidate-unknown. Project stands.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "eq"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "ne"}, "then": {"of": [{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "eq"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "ne"}, "then": {"of": [{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: model error; f8863 p. 2, line 30; p970 p. 11. The reply has the education lines read person.edu_over for every person (no f8863.paid gate), so it is unknown on returns with no education credit where the project hides the line (180 completed records, for example classm.f4952.1.deepseek); and it requires an issued TIN for the American opportunity credit, against p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (owner decision T-113 keeps that deeming): f1.t113.person_aoc_itin_applied (stage19.example.aoc_phaseout with the ITIN applied for) gives line 27 $0.00 where the project gives $4,000.00. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,677 of 5,033 agree; 2,355 candidate-unknown, 1 value; on returns the full interview completes: 306 candidate-unknown. Project stands.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "all"}, "then": {"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second transcription's note: Course materials not required to be paid to the institution count for the AOC only. The LLC amount is taken from the shared worksheet's LLC result (ws4_llc).

Ruling: model error; f8863 p. 2, line 31; i8863 p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions).". The reply has the education lines read person.edu_over for every person (no f8863.paid gate), so it is unknown on returns with no education credit where the project hides the line (180 completed records, for example classm.f4952.1.deepseek); and it requires an issued TIN for the American opportunity credit, against p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (owner decision T-113 keeps that deeming): f1.t113.person_aoc_itin_applied (stage19.example.aoc_phaseout with the ITIN applied for) gives line 27 $0.00 where the project gives $4,000.00. Off completed returns: f1.t113.person_llc_itin_applied (a lifetime learning credit student whose ITIN was only applied for) is refused by the project at person.edu_llc_tin_refused, as the owner decided (T-113), and the reply computes $0.00 by excluding the student (scope: a cited refusal); stage19.refuse.period_over_person is refused by the reply on its own edu_over declaration where the project hides the line. Reused from the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`), re-checked: project line unchanged; counts below supersede any in the reused text. executable-triage-v2 (`reviews/2025/transcription/triage/person.json`; 1,565 fixtures, 500 generated returns seed 20261026, 1,859 partial records; 5,033 comparisons): 2,675 of 5,033 agree; 2,356 candidate-unknown, 1 candidate-refuses, 1 project-refuses; on returns the full interview completes: 306 candidate-unknown. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| person.se_line6 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.se_line12 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.se_line13 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.s16 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.eic_se | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.dc_earned | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.dc_earned_b | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.sav_line1 | person.sav_able | - |
| person.sav_line2 | person.sav_excess | person.sav_excess |
| person.ira_deduction | person.ira_excess | person.ira_excess |
| person.ira_nondeductible | person.ira_excess | person.ira_excess |
| person.ira_files_8606 | person.ira_excess | person.ira_excess |
| person.ira_8606_line2 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.ira_dist_gate | person.ira_excess | person.ira_excess |
| person.ira_8606_line14 | person.ira_basis_adjusted, person.ira_dist_gate, person.ira_excess | person.ira_basis_adjusted, person.ira_dist_gate, person.ira_excess |
| person.ira_se | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| person.x_tax | person.h_s_split, person.x_other | person.h_s_split |
| credit | person.rrta | - |
| Step 2 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 3 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 5 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 7 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| Step 21 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| 27 | person.edu_over | person.edu_over |
| 28 | person.edu_over | person.edu_over |
| 29 | person.edu_over | person.edu_over |
| 30 | person.edu_over | person.edu_over |
| 31 | person.edu_over | person.edu_over |

## Raw second transcription

```yaml
```yaml
lines:
  - id: person.employers
    printed: "employers"
    label: "Number of employers (Forms W-2) for 2025"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
    note: "Schedule 3 line 11 applies if you 'had more than one employer for 2025'. Each Form W-2 entry is counted as one employer."
  - id: person.overcount
    printed: "overcount"
    label: "Number of employers that withheld more than $10,918.20 of social security tax"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, gt: [w2.box4, {param: ss.limit}]}}
  - id: person.over
    printed: "over"
    label: "Any one employer withheld more than $10,918.20 (you can't claim the excess on your return)"
    type: Bool
    expr: {op: test, gt: [person.overcount, {const: 0, type: Count}]}
  - id: person.h_box3
    printed: "(helper)"
    label: "Total of Forms W-2, box 3"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box3}
  - id: person.h_box7
    printed: "(helper)"
    label: "Total of Forms W-2, box 7"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box7}
  - id: person.wages
    printed: "wages"
    label: "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2)"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_box3, person.h_box7]}
  - id: person.withheld
    printed: "withheld"
    label: "Total social security tax withheld (Forms W-2, box 4)"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box4}
  - id: person.eligible
    printed: "eligible"
    label: "More than one employer, and no one employer withheld more than $10,918.20"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [person.employers, {const: 2, type: Count}]}
        - {op: test, eq: [person.over, {const: false}]}
    note: "The text says excess tax 'may have been withheld' when total wages are more than $176,100. Wages over the base are not used as a separate test. Without such wages, the excess over $10,918.20 computed on the next line is zero."
  - id: person.excess
    printed: "excess"
    label: "Social security tax withheld in excess of $10,918.20"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.withheld, take: {param: ss.limit}}
  - id: person.zero
    printed: "zero"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.credit
    printed: "credit"
    label: "Excess social security tax withheld (figured separately for you and your spouse)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.eligible, {const: true}]}, then: person.excess}
        - {guard: {op: test, eq: [person.eligible, {const: false}]}, then: person.zero}
    refuses: [person.rrta]

  - id: person.h_is_sep
    printed: "(helper)"
    label: "Contributed for yourself to a SEP IRA"
    type: Bool
    expr: {op: test, eq: [person.plan, {const: "sep"}]}
  - id: person.sep_s1
    printed: "Step 1"
    label: "Enter your net profit from Schedule C (Form 1040), line 31"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
    shown_when: person.h_is_sep
  - id: person.sep_s2
    printed: "Step 2"
    label: "Enter your deduction for self-employment tax from Schedule 1 (Form 1040), line 15"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line13}
    shown_when: person.h_is_sep
  - id: person.sep_s3
    printed: "Step 3"
    label: "Net earnings from self-employment. Subtract step 2 from step 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.sep_s1, take: person.sep_s2}
    shown_when: person.h_is_sep
    note: "The worksheet gives no floor for a loss. A negative result is held as zero, since no SEP deduction can arise from it."
  - id: person.h_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: person.h_hundred
    printed: "(helper)"
    label: "One hundred cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: person.h_rate_c
    printed: "(helper)"
    label: "Plan contribution rate expressed as cents (rate × 1 cent)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: person.h_cent, count: person.sep_rate}
  - id: person.h_rate_plus
    printed: "(helper)"
    label: "Plan contribution rate plus 100% (in cents)"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_rate_c, person.h_hundred]}
  - id: person.sep_s5
    printed: "Step 5"
    label: "Multiply step 3 by step 4 (rate from the Rate Table for Self-Employed)"
    type: NonNegDollars
    expr: {op: prorate, amount: person.sep_s3, part: person.h_rate_c, whole: person.h_rate_plus, places: 6}
    shown_when: person.h_is_sep
    note: "No table of Column B rates is supplied. The table rate equals rate ÷ (1 + rate) rounded to six decimal places (for example 10% gives 0.090909 and 25% gives 0.200000). This line reproduces it with prorate at 6 places. Non-whole rates are screened by person.plan_screen."
  - id: person.h_comp_limit
    printed: "(helper)"
    label: "$350,000 compensation limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.comp_limit}
  - id: person.sep_s6
    printed: "Step 6"
    label: "Multiply $350,000 by your plan contribution rate (not the reduced rate)"
    type: NonNegDollars
    expr: {op: prorate, amount: person.h_comp_limit, part: person.h_rate_c, whole: person.h_hundred, places: 2}
    shown_when: person.h_is_sep
  - id: person.sep_s7
    printed: "Step 7"
    label: "Enter the smaller of step 5 or step 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s5, person.sep_s6]}
    shown_when: person.h_is_sep
  - id: person.sep_s8
    printed: "Step 8"
    label: "Contribution dollar limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.sep_dollar_limit}
    shown_when: person.h_is_sep
  - id: person.sep_s21
    printed: "Step 21"
    label: "Maximum deductible contribution (no elective deferrals: enter the smaller of step 7 or step 8)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s7, person.sep_s8]}
    shown_when: person.h_is_sep
    note: "Steps 9-20 apply only to elective deferrals to the self-employed plan. Those are screened by person.plan_screen (SARSEP and other deferrals), so step 21 is the smaller of step 7 or step 8."
  - id: person.h_sep_ded
    printed: "(helper)"
    label: "Actual SEP contribution, not to exceed the maximum deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_contrib, person.sep_s21]}

  - id: person.h_aqee_adj
    printed: "(helper)"
    label: "Total adjustments (tax-free educational assistance 2025 and 2026, and refunds)"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_a2025, person.edu_a2026, person.edu_refunds]}
  - id: person.h_edu_aoc
    printed: "(helper)"
    label: "Lines 27-30 apply (American opportunity credit for this student)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.edu, {const: true}]}
        - {op: test, eq: [person.edu_1098t, {const: true}]}
        - {op: test, eq: [person.edu_line23, {const: false}]}
        - {op: test, eq: [person.edu_line24, {const: true}]}
        - {op: test, eq: [person.edu_line25, {const: false}]}
        - {op: test, eq: [person.edu_line26, {const: false}]}
        - {op: test, eq: [person.edu_ein, {const: true}]}
        - {op: test, eq: [person.tin, {const: true}]}
  - id: person.h_edu_llc
    printed: "(helper)"
    label: "Line 31 applies (lifetime learning credit for this student)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.edu, {const: true}]}
        - {op: test, eq: [person.edu_1098t, {const: true}]}
        - {op: test, eq: [person.tin, {const: true}]}
        - {op: test, not: {op: test, eq: [person.h_edu_aoc, {const: true}]}}
  - id: person.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses. Don't enter more than $4,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: true}]}, then: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_aqee_adj}, line: line27}}
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: false}]}, then: person.zero}
    refuses: [person.edu_over]
    shown_when: person.h_edu_aoc
  - id: person.edu_line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: true}]}, then: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_aqee_adj}, line: line28}}
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: false}]}, then: person.zero}
    refuses: [person.edu_over]
    shown_when: person.h_edu_aoc
  - id: person.edu_line29
    printed: "29"
    label: "Multiply line 28 by 25% (0.25)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: true}]}, then: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_aqee_adj}, line: line29}}
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: false}]}, then: person.zero}
    refuses: [person.edu_over]
    shown_when: person.h_edu_aoc
  - id: person.edu_line30
    printed: "30"
    label: "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: true}]}, then: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_aqee_adj}, line: line30}}
        - {guard: {op: test, eq: [person.h_edu_aoc, {const: false}]}, then: person.zero}
    refuses: [person.edu_over]
    shown_when: person.h_edu_aoc
  - id: person.edu_line31
    printed: "31"
    label: "Lifetime learning credit: adjusted qualified education expenses"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_edu_llc, {const: true}]}, then: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_aqee_adj}, line: ws4_llc}}
        - {guard: {op: test, eq: [person.h_edu_llc, {const: false}]}, then: person.zero}
    refuses: [person.edu_over]
    shown_when: person.h_edu_llc
    note: "Course materials not required to be paid to the institution count for the AOC only. The LLC amount is taken from the shared worksheet's LLC result (ws4_llc)."

  - id: person.one
    printed: "(helper)"
    label: "One"
    type: Count
    expr: {op: param, ref: person.one}
  - id: person.h_educator_max
    printed: "(helper)"
    label: "$300 educator expense limit"
    type: NonNegDollars
    expr: {op: param, ref: s1.educator_max}
  - id: person.h_educator_capped
    printed: "(helper)"
    label: "Qualified educator expenses, up to $300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, person.h_educator_max]}
  - id: person.educator_deduction
    printed: "(helper)"
    label: "Educator expenses (Schedule 1, line 11), this person's share"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.eligible_educator, {const: true}]}, then: person.h_educator_capped}
        - {guard: {op: test, eq: [person.eligible_educator, {const: false}]}, then: person.zero}

  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of Forms 8889 for this person"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one}
  - id: person.hsa_split
    printed: "(helper)"
    label: "Forms 8889 on which the family limit is divided between spouses with separate HSAs (line 6 rules)"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.split, {const: true}]}}
    note: "The interface name is not defined by the IRS text. It is read as a count of this person's Forms 8889 where the line 6 spousal division applies."
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "Forms 8889 dividing the family limit by an agreed (not equal) allocation"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where:
        op: test
        all:
          - {op: test, eq: [f8889.split, {const: true}]}
          - {op: test, eq: [f8889.allocation, {const: "agreed"}]}
    note: "Read as a count of divided Forms 8889 using an agreed allocation, so the household can check both spouses agree. This reading is not stated in the IRS text."
  - id: person.hsa_step1
    printed: "(helper)"
    label: "Refigured family contribution limit (line 6 Step 1) on divided Forms 8889"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.step1, where: {op: test, eq: [f8889.split, {const: true}]}}
  - id: person.hsa_share
    printed: "(helper)"
    label: "Part of the family limit allocated to this person (line 6 Step 2) on divided Forms 8889"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.share, where: {op: test, eq: [f8889.split, {const: true}]}}
  - id: person.hsa_deduction
    printed: "(helper)"
    label: "HSA deduction (Form 8889, line 13)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line13}
  - id: person.hsa_taxable
    printed: "(helper)"
    label: "Taxable HSA distributions (Form 8889, line 16)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line16}
  - id: person.hsa_addtax
    printed: "(helper)"
    label: "Additional 20% tax (Form 8889, line 17b)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line17b}

  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers from which qualified tips were received"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one}
  - id: person.tip_total
    printed: "(helper)"
    label: "Qualified Tips From More Than One Employer Worksheet, line 2 (total of column (d))"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}
  - id: person.tip_reported
    printed: "(helper)"
    label: "Qualified tips reported by employers on Form W-2 or reported to employers on Forms 4070 (column (b))"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.amount}
    note: "Read as the total of column (b), used on line 4a when there is one employer. The IRS text does not name this interface."
  - id: person.ot_employers
    printed: "(helper)"
    label: "Number of employers paying qualified overtime compensation"
    type: Count
    expr: {op: sum_over, collection: otjob, field: otjob.one}
  - id: person.ot_total
    printed: "(helper)"
    label: "Qualified Overtime Compensation From More Than One Employer Worksheet, line 2"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}

  - id: person.box1
    printed: "(helper)"
    label: "Total amount from Form(s) W-2, box 1"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box1}
  - id: person.box2
    printed: "(helper)"
    label: "Federal income tax withheld from Form(s) W-2, box 2"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}

  - id: person.ira_amount_a
    printed: "(helper)"
    label: "IRA distributions (Form 1040, line 4a), this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.amount_a, where: {op: test, ne: [retirement.account, {const: "plan"}]}}
  - id: person.ira_taxable
    printed: "(helper)"
    label: "IRA distributions taxable amount (Form 1040, line 4b), this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.taxable, where: {op: test, ne: [retirement.account, {const: "plan"}]}}
  - id: person.ira_rollovers
    printed: "(helper)"
    label: "IRA distributions with a rollover (line 4c, box 1)"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where:
        op: test
        all:
          - {op: test, ne: [retirement.account, {const: "plan"}]}
          - {op: test, eq: [retirement.has_rollover, {const: true}]}
  - id: person.plan_amount_a
    printed: "(helper)"
    label: "Pensions and annuities (Form 1040, line 5a), this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.amount_a, where: {op: test, eq: [retirement.account, {const: "plan"}]}}
  - id: person.plan_taxable
    printed: "(helper)"
    label: "Pensions and annuities taxable amount (Form 1040, line 5b), this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.taxable, where: {op: test, eq: [retirement.account, {const: "plan"}]}}
  - id: person.plan_rollovers
    printed: "(helper)"
    label: "Pension and annuity distributions with a rollover (line 5c, box 1)"
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
    label: "Form 8880 line 4 distributions received in 2025 (this person)"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.sav_amount}

  - id: person.medicare5
    printed: "(helper)"
    label: "Medicare wages and tips from Form W-2, box 5 (total)"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}
  - id: person.medicare6
    printed: "(helper)"
    label: "Medicare tax withheld from Form W-2, box 6 (total)"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}

  - id: person.sc_count
    printed: "(helper)"
    label: "Number of Schedules C for this person"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one}
  - id: person.ho_count
    printed: "(helper)"
    label: "Number of businesses claiming business use of the home"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, eq: [sc.ho_uses, {const: true}]}}
  - id: person.mq_q4
    printed: "(helper)"
    label: "Depreciable bases of MACRS property placed in service in the last 3 months"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_q4}
  - id: person.mq_total
    printed: "(helper)"
    label: "Depreciable bases of MACRS property placed in service during the year"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_total}
  - id: person.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property placed in service (Form 4562, line 2)"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179}
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "Elected cost of section 179 property (Form 4562, line 6)"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.s179_elected}
    note: "The catalog offers no Schedule C-level split between line 6 (property other than listed) and line 7 (listed property from Part V). A person-level line may read only its own child collection, so asset and vehicle entries cannot be summed here. The only Schedule C aggregate, sc.s179_elected, is used. This is a limitation."
  - id: person.s179_listed
    printed: "(helper)"
    label: "Listed property elected cost (Form 4562, line 7)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "LIMITATION: no Schedule C-level aggregate of the section 179 election on listed property (Part V) is in the catalog, and nested vehicle entries cannot be read from a person entry. The listed amount is counted within person.s179_nonlisted (sc.s179_elected). This line holds zero to avoid counting it twice. A published Schedule C aggregate is needed to separate it."
  - id: person.income179
    printed: "(helper)"
    label: "Business income from the active conduct of trade or business, figured without the section 179 deduction (Form 4562, line 11)"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31_pre179}
    note: "Read as this person's Schedule C net profit or loss before the section 179 deduction. Wages, which line 11 also counts, are left to the return-level line."
  - id: person.sc_total
    printed: "(helper)"
    label: "Net profit or (loss) from Schedule C, line 31 (all this person's businesses)"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}

  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE, line 6"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line6}}
    refuses: [person.se_screen, person.rrta]
  - id: person.se_line12
    printed: "(helper)"
    label: "Self-employment tax (Schedule SE, line 12)"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line12}}
    refuses: [person.se_screen, person.rrta]
  - id: person.se_line13
    printed: "(helper)"
    label: "Deduction for one-half of self-employment tax (Schedule SE, line 13)"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line13}}
    refuses: [person.se_screen, person.rrta]
  - id: person.h_se3
    printed: "(helper)"
    label: "Schedule SE, line 3"
    type: Dollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line3}}
    refuses: [person.se_screen, person.rrta]
  - id: person.h_se4a
    printed: "(helper)"
    label: "Schedule SE, line 4a"
    type: Dollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line4a}}
    refuses: [person.se_screen, person.rrta]

  - id: person.h_simple_comp
    printed: "(helper)"
    label: "SIMPLE compensation: net earnings from self-employment (Schedule SE line 4), before SIMPLE contributions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_se4a, take: {const: 0}}
    note: "Pub. 560 says 'line 4 of Schedule SE'. Optional methods (line 4b) are screened, so line 4a is used, held as zero if negative."
  - id: person.h_simple_base
    printed: "(helper)"
    label: "SIMPLE salary reduction limit ($16,500)"
    type: NonNegDollars
    expr: {op: param, ref: ret.simple_limit}
  - id: person.h_catchup
    printed: "(helper)"
    label: "SIMPLE catch-up contribution limit for this age"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: simple_catchup, keys: [person.simple_age]}
  - id: person.h_simple_deflimit
    printed: "(helper)"
    label: "Salary reduction limit plus catch-up limit"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_simple_base, person.h_catchup]}
  - id: person.h_def1
    printed: "(helper)"
    label: "Salary reduction contributions up to the limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.simple_deferral, person.h_simple_deflimit]}
  - id: person.h_def_allowed
    printed: "(helper)"
    label: "Salary reduction contributions, not more than compensation"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_def1, person.h_simple_comp]}
  - id: person.h_match_cap
    printed: "(helper)"
    label: "3% of compensation"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_simple_comp, rate: {param: ret.match_rate}}
  - id: person.h_match_max
    printed: "(helper)"
    label: "Matching contribution: dollar-for-dollar up to 3% of compensation"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_def_allowed, person.h_match_cap]}
  - id: person.h_ne_comp
    printed: "(helper)"
    label: "Compensation taken into account (up to $350,000)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_simple_comp, person.h_comp_limit]}
  - id: person.h_ne_max
    printed: "(helper)"
    label: "2% nonelective contribution"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_ne_comp, rate: {param: ret.nonelective_rate}}
  - id: person.h_er_max
    printed: "(helper)"
    label: "Maximum employer contribution under the plan formula"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.simple_kind, {const: "match"}]}, then: person.h_match_max}
        - {guard: {op: test, eq: [person.simple_kind, {const: "nonelective"}]}, then: person.h_ne_max}
  - id: person.h_er_allowed
    printed: "(helper)"
    label: "Employer contributions for yourself, up to the maximum"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.simple_employer, person.h_er_max]}
  - id: person.h_simple_ded
    printed: "(helper)"
    label: "SIMPLE contributions for yourself"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_def_allowed, person.h_er_allowed]}
    note: "Pub. 560 ch. 3 limits are applied as follows. Salary reduction is capped at $16,500 plus the catch-up for the person's age, and not above compensation. The match is dollar-for-dollar up to 3% of compensation. The nonelective contribution is 2% of compensation up to $350,000. Contributions above the deductible maximum are screened by person.plan_screen."
  - id: person.s16
    printed: "(helper)"
    label: "Self-employed SEP and SIMPLE contributions for yourself (Schedule 1, line 16), this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.plan, {const: "none"}]}, then: person.zero}
        - {guard: {op: test, eq: [person.plan, {const: "sep"}]}, then: person.h_sep_ded}
        - {guard: {op: test, eq: [person.plan, {const: "simple"}]}, then: person.h_simple_ded}
    refuses: [person.plan_screen]

  - id: person.positive_profits
    printed: "(helper)"
    label: "Total of all net profits from Schedule C, line 31 (no net losses) (Form 7206, line 5)"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.profit_pos}
  - id: person.sehi
    printed: "(helper)"
    label: "Self-employed health insurance deduction (Form 7206, line 14)"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.f7206_line14}
  - id: person.qbi
    printed: "(helper)"
    label: "Qualified business income or (loss) (Form 8995, line 1(c)), this person's businesses"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.qbi}
  - id: person.eic_se
    printed: "(helper)"
    label: "EIC Worksheet B line 1e: Schedule SE line 3 (plus line 4b and 5a) minus line 13"
    type: Dollars
    expr: {op: subtract, from: person.h_se3, take: person.se_line13}
    note: "Lines 4b (optional methods) and 5a (church employee income) are screened by person.se_screen, so 1c equals Schedule SE line 3."
  - id: person.sc_1a
    printed: "(helper)"
    label: "Businesses whose income includes qualified tips or overtime for Schedule 1-A"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, eq: [sc.tips_ot, {const: true}]}}

  - id: person.dc_benefits
    printed: "(helper)"
    label: "Dependent care benefits received (Form 2441, line 12), this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.dc_benefits}
  - id: person.h_box10_n
    printed: "(helper)"
    label: "Number of Forms W-2 with an amount in box 10"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, gt: [w2.box10, {const: 0}]}}
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "Any Form W-2 shows dependent care benefits in box 10"
    type: Bool
    expr: {op: test, gt: [person.h_box10_n, {const: 0, type: Count}]}
  - id: person.dc_earned
    printed: "(helper)"
    label: "Earned income for Form 2441 lines 4/5: Form W-2 wages plus Schedule SE line 3 minus Schedule 1 line 15"
    type: Dollars
    expr: {op: sum, of: [person.box1, person.eic_se]}
    note: "Line 1z items other than 1a (Form W-2 box 1) are screened (scope.other_income), apart from 1e. Line 1e is a return-level amount from Form 2441 line 26 and cannot be attributed to one person, so it is not included. A self-employment loss reduces earned income, as the instructions require."
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "Earned income for Form 2441 lines 18/19 (not including dependent care benefits shown on line 12)"
    type: Dollars
    expr: {op: copy, from: person.dc_earned}
    note: "Line 12 excludes box 10 amounts already reported as wages in box 1, and the excluded benefits are not in box 1. So the line 18/19 earned income equals the credit earned income here."

  - id: person.sav_ineligible
    printed: "(helper)"
    label: "Born after January 1, 2008, claimed as a dependent, or a student"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [person.sav_born, {const: false}]}
        - {op: test, eq: [person.sav_claimed, {const: true}]}
        - {op: test, eq: [person.sav_student, {const: true}]}
  - id: person.h_sav_trad
    printed: "(helper)"
    label: "Traditional IRA contributions for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.sav_trad, {const: true}]}, then: person.ira_trad}
        - {guard: {op: test, eq: [person.sav_trad, {const: false}]}, then: person.zero}
  - id: person.sav_line1
    printed: "(helper)"
    label: "Form 8880 line 1: traditional and Roth IRA contributions for 2025 (no rollovers)"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_sav_trad, person.sav_roth]}
    refuses: [person.sav_able]
  - id: person.h_sav_w2
    printed: "(helper)"
    label: "Elective deferrals shown on Forms W-2, box 12"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.sav_deferral}
  - id: person.h_sav_simple
    printed: "(helper)"
    label: "SIMPLE salary reduction contributions as a self-employed person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.plan, {const: "simple"}]}, then: person.simple_deferral}
        - {guard: {op: test, ne: [person.plan, {const: "simple"}]}, then: person.zero}
  - id: person.sav_line2
    printed: "(helper)"
    label: "Form 8880 line 2: elective deferrals, voluntary employee contributions and 501(c)(18)(D) contributions"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_sav_w2, person.sav_voluntary, person.h_sav_simple]}
    refuses: [person.sav_excess]

  - id: person.ira_contrib
    printed: "(helper)"
    label: "Traditional IRA contributions for 2025 (IRA Deduction Worksheet line 11)"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_trad}
  - id: person.ira_cov
    printed: "(helper)"
    label: "Covered by a retirement plan at work or through self-employment (SEP or SIMPLE)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [person.ira_work_plan, {const: true}]}
        - {op: test, ne: [person.plan, {const: "none"}]}
  - id: person.h_line2_cov
    printed: "(helper)"
    label: "IRA worksheet line 2 amount for a covered person by filing status"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}
  - id: person.h_line2_nc
    printed: "(helper)"
    label: "$246,000 for the person who wasn't covered by a plan"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA Deduction Worksheet line 2 (this person's column)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.ira_cov, {const: true}]}, then: person.h_line2_cov}
        - {guard: {op: test, eq: [person.ira_cov, {const: false}]}, then: person.h_line2_nc}
    note: "$246,000 applies to a person not covered only on a joint return where the other spouse is covered. Return-level gates (ira.lines2to6, ira.cov_gate) decide where lines 2-6 are used. The $89,000 amount for married filing separately and lived apart is not available from the keyed parameter, whose MFS value is $10,000. That case must be screened at return level."
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA Deduction Worksheet line 6: subtract line 5 from line 2 (zero if line 5 is not less)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_line2, take: ira.line5}
  - id: person.h_lim
    printed: "(helper)"
    label: "$7,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}
  - id: person.h_lim50
    printed: "(helper)"
    label: "$8,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}
  - id: person.h_ira_limit
    printed: "(helper)"
    label: "$7,000 if under age 50; $8,000 if age 50 or older at the end of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.ira_age50, {const: true}]}, then: person.h_lim50}
        - {guard: {op: test, eq: [person.ira_age50, {const: false}]}, then: person.h_lim}
  - id: person.h_joint_cov
    printed: "(helper)"
    label: "Married filing jointly or QSS, in the column of a covered person"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [person.ira_cov, {const: true}]}
  - id: person.h_full_joint
    printed: "(helper)"
    label: "$20,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_joint}
  - id: person.h_full_narrow
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_narrow}
  - id: person.h_full
    printed: "(helper)"
    label: "Line 6 amount at or above which the full limit applies"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.h_joint_cov, {const: true}]}, then: person.h_full_joint}
        - {guard: {op: test, eq: [person.h_joint_cov, {const: false}]}, then: person.h_full_narrow}
  - id: person.h_p70
    printed: "(helper)"
    label: "Line 6 × 70%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_70}}
  - id: person.h_p80
    printed: "(helper)"
    label: "Line 6 × 80%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_80}}
  - id: person.h_p35
    printed: "(helper)"
    label: "Line 6 × 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_35}}
  - id: person.h_p40
    printed: "(helper)"
    label: "Line 6 × 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_40}}
  - id: person.h_prod
    printed: "(helper)"
    label: "Line 6 multiplied by the applicable percentage"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [person.h_joint_cov, {const: true}]}, {op: test, eq: [person.ira_age50, {const: false}]}]}
          then: person.h_p35
        - guard: {op: test, all: [{op: test, eq: [person.h_joint_cov, {const: true}]}, {op: test, eq: [person.ira_age50, {const: true}]}]}
          then: person.h_p40
        - guard: {op: test, all: [{op: test, eq: [person.h_joint_cov, {const: false}]}, {op: test, eq: [person.ira_age50, {const: false}]}]}
          then: person.h_p70
        - guard: {op: test, all: [{op: test, eq: [person.h_joint_cov, {const: false}]}, {op: test, eq: [person.ira_age50, {const: true}]}]}
          then: person.h_p80
  - id: person.h_prod_r
    printed: "(helper)"
    label: "If the result isn't a multiple of $10, increase it to the next multiple of $10"
    type: NonNegDollars
    expr: {op: round, of: person.h_prod, unit: 1000, rule: up}
  - id: person.h_ira_min
    printed: "(helper)"
    label: "$200"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}
  - id: person.h_prod_min
    printed: "(helper)"
    label: "If the result is less than $200, enter $200"
    type: NonNegDollars
    expr: {op: larger_of, of: [person.h_prod_r, person.h_ira_min]}
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA Deduction Worksheet line 7 (this person's column)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.anyone_covered, {const: false}]}
          then: person.h_ira_limit
        - guard: {op: test, all: [{op: test, eq: [ira.anyone_covered, {const: true}]}, {op: test, eq: [person.ira_line6, {const: 0}]}]}
          then: person.zero
        - guard: {op: test, all: [{op: test, eq: [ira.anyone_covered, {const: true}]}, {op: test, gt: [person.ira_line6, {const: 0}]}, {op: test, ge: [person.ira_line6, person.h_full]}]}
          then: person.h_ira_limit
        - guard: {op: test, all: [{op: test, eq: [ira.anyone_covered, {const: true}]}, {op: test, gt: [person.ira_line6, {const: 0}]}, {op: test, lt: [person.ira_line6, person.h_full]}]}
          then: person.h_prod_min
    note: "Line 6 'No' (line 5 not less than line 2) means 'None of your IRA contributions are deductible' (STOP). That case gives zero, not the $200 minimum."
  - id: person.h_lim_contrib
    printed: "(helper)"
    label: "Smaller of the contribution limit or traditional IRA contributions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_ira_limit, person.ira_trad]}
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA Deduction Worksheet line 12: smallest of line 7, 10, or 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_line7_11, ira.line10]}
    refuses: [person.ira_excess]
  - id: person.h_line7_11
    printed: "(helper)"
    label: "Smaller of line 7 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.ira_line7, person.ira_trad]}
  - id: person.h_10_11
    printed: "(helper)"
    label: "Smaller of IRA worksheet line 10 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line10, person.ira_trad]}
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "Form 8606 line 1: smaller of worksheet line 10 or 11, minus line 12"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_10_11, take: person.ira_deduction}
    refuses: [person.ira_excess]
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Form 8606 required (nondeductible contributions, or traditional IRA distributions with basis)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [person.ira_nondeductible, {const: 0}]}
        - op: test
          all:
            - {op: test, eq: [person.ira_dist, {const: true}]}
            - {op: test, gt: [person.ira_basis, {const: 0}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2: total basis in traditional IRAs"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_basis}
    refuses: [person.ira_basis_adjusted]
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "Form 8606 filed and a traditional IRA distribution or Roth conversion in 2025 (lines 4-13 needed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.ira_files_8606, {const: true}]}
        - {op: test, eq: [person.ira_dist, {const: true}]}
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14 (no distribution: enter the amount from line 3, lines 1 + 2)"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_nondeductible, person.ira_8606_line2]}
    refuses: [person.ira_dist_gate]
  - id: person.ira_ssb
    printed: "(helper)"
    label: "IRA deduction for the Social Security Benefits Worksheet (no one covered by a plan)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_lim_contrib, ira.line10]}
    note: "Not named by the IRS text. When IRA contributions are made and anyone is covered by a plan, the line 6a/6b instructions require Pub. 590-A (ssb.pub915 screen). Otherwise the deduction is the smallest of the limit, earned income (line 10) and contributions, independent of AGI. That is the reading used."
  - id: person.ira_se
    printed: "(helper)"
    label: "IRA worksheet line 9 component: net earnings from self-employment minus Schedule 1 lines 15 and 16 (if zero or less, -0-)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.eic_se, take: person.s16}

  - id: person.edu_kid
    printed: "(helper)"
    label: "Form 8863 line 7 conditions: under 24 conditions met, a parent alive, and not filing jointly"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, eq: [person.sav_born, {const: false}]}
            - op: test
              all:
                - {op: test, eq: [person.sav_born, {const: true}]}
                - {op: test, eq: [person.edu_born_2007, {const: false}]}
                - {op: test, eq: [person.edu_half_support, {const: true}]}
            - op: test
              all:
                - {op: test, eq: [person.edu_born_2007, {const: true}]}
                - {op: test, eq: [person.edu_born_2002, {const: false}]}
                - {op: test, eq: [person.edu_fulltime, {const: true}]}
                - {op: test, eq: [person.edu_half_support, {const: true}]}
        - {op: test, eq: [person.edu_parent, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfj"}]}
    note: "Ages at the end of 2025 are read from the birth-date questions. Born after Jan 1, 2008 means under 18. Born before Jan 2, 2008 but not before Jan 2, 2007 means age 18. Born before Jan 2, 2007 but not before Jan 2, 2002 means over 18 and under 24. This uses the rule that a person reaches an age on the day before the birthday."

  - id: person.x_l1
    printed: "(helper)"
    label: "Form 5329 line 1: early distributions includible in income"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l1}
  - id: person.h_l2_raw
    printed: "(helper)"
    label: "Early distributions covered by an exception, before per-person limits"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2}
  - id: person.h_e09
    printed: "(helper)"
    label: "First home (09) amounts"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e09}
  - id: person.h_e19
    printed: "(helper)"
    label: "Birth or adoption (19) amounts"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e19}
  - id: person.h_e22
    printed: "(helper)"
    label: "Domestic abuse (22) amounts"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e22}
  - id: person.h_e23
    printed: "(helper)"
    label: "Emergency personal expense (23) amounts"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e23}
  - id: person.h_cap_first
    printed: "(helper)"
    label: "$10,000 first-home limit"
    type: NonNegDollars
    expr: {op: param, ref: f5329.cap_first_home}
  - id: person.h_cap09
    printed: "(helper)"
    label: "$10,000 reduced by prior first-home distributions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_cap_first, take: person.x_prior09}
  - id: person.h_e09c
    printed: "(helper)"
    label: "First home exception, limited"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_e09, person.h_cap09]}
  - id: person.h_cap_birth
    printed: "(helper)"
    label: "$5,000 per birth or adoption"
    type: NonNegDollars
    expr: {op: param, ref: f5329.cap_birth}
  - id: person.h_cap19
    printed: "(helper)"
    label: "$5,000 times the number of births or adoptions"
    type: NonNegDollars
    expr: {op: multiply_count, amount: person.h_cap_birth, count: person.x_births}
  - id: person.h_e19c
    printed: "(helper)"
    label: "Birth or adoption exception, limited"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_e19, person.h_cap19]}
  - id: person.h_cap_abuse
    printed: "(helper)"
    label: "$10,300 domestic abuse limit"
    type: NonNegDollars
    expr: {op: param, ref: f5329.cap_abuse}
  - id: person.h_e22c
    printed: "(helper)"
    label: "Domestic abuse exception, limited"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_e22, person.h_cap_abuse]}
  - id: person.h_cap_emerg
    printed: "(helper)"
    label: "$1,000 emergency expense limit"
    type: NonNegDollars
    expr: {op: param, ref: f5329.cap_emergency}
  - id: person.h_e23c
    printed: "(helper)"
    label: "Emergency expense exception, limited"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_e23, person.h_cap_emerg]}
  - id: person.h_limited_raw
    printed: "(helper)"
    label: "Limited-exception amounts before limits"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_e09, person.h_e19, person.h_e22, person.h_e23]}
  - id: person.x_limited_sum
    printed: "(helper)"
    label: "Limited-exception amounts after per-person limits"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_e09c, person.h_e19c, person.h_e22c, person.h_e23c]}
  - id: person.x_other_exc
    printed: "(helper)"
    label: "Exception amounts not subject to a per-person dollar limit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_l2_raw, take: person.h_limited_raw}
  - id: person.x_l2_all
    printed: "(helper)"
    label: "Form 5329 line 2: early distributions not subject to the additional tax"
    type: NonNegDollars
    expr: {op: sum, of: [person.x_other_exc, person.x_limited_sum]}
  - id: person.x_limit_binds
    printed: "(helper)"
    label: "A per-person dollar limit reduces an exception amount"
    type: Bool
    expr: {op: test, gt: [person.h_limited_raw, person.x_limited_sum]}
  - id: person.x_l1_s
    printed: "(helper)"
    label: "Line 1 amounts from a SIMPLE IRA within the first 2 years (code S)"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l1_s}
  - id: person.x_l2_s
    printed: "(helper)"
    label: "Line 2 exception amounts on code S distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_s}
  - id: person.h_s_split
    printed: "(helper)"
    label: "A dollar limit reduces exceptions while code S distributions have exceptions (allocation between 10% and 25% undetermined)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.x_limit_binds, {const: true}]}
        - {op: test, gt: [person.x_l2_s, {const: 0}]}
  - id: person.h_l3
    printed: "(helper)"
    label: "Form 5329 line 3: subtract line 2 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l1, take: person.x_l2_all}
  - id: person.h_l3_s
    printed: "(helper)"
    label: "Part of line 3 from a SIMPLE IRA within 2 years"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l1_s, take: person.x_l2_s}
  - id: person.h_l3_other
    printed: "(helper)"
    label: "Rest of line 3"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_l3, take: person.h_l3_s}
  - id: person.h_tax10
    printed: "(helper)"
    label: "10% of line 3 (other than SIMPLE within 2 years)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_l3_other, rate: {param: f5329.early_rate}}
  - id: person.h_tax25
    printed: "(helper)"
    label: "25% of the SIMPLE IRA amount"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_l3_s, rate: {param: f5329.simple_rate}}
  - id: person.x_hsa_excess
    printed: "(helper)"
    label: "Form 5329 line 47/48: excess contributions to HSAs for 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.excess_amt}
    note: "Prior-year excess (lines 42-46) is screened by person.x_other, so line 48 equals line 47."
  - id: person.h_l48
    printed: "(helper)"
    label: "Smaller of line 48 or the value of your HSAs on December 31, 2025"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.x_hsa_excess, person.x_hsa_value]}
  - id: person.h_l49
    printed: "(helper)"
    label: "Form 5329 line 49: 6% additional tax"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_l48, rate: {param: f5329.excess_rate}}
  - id: person.x_tax
    printed: "(helper)"
    label: "Form 5329 additional taxes (lines 4 and 49) included on Schedule 2, line 8"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_tax10, person.h_tax25, person.h_l49]}
    refuses: [person.x_other, person.h_s_split]
  - id: person.h_must_ret
    printed: "(helper)"
    label: "Early distributions needing Form 5329 (exception claimed, or not code 1)"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where:
        op: test
        all:
          - {op: test, eq: [retirement.early, {const: true}]}
          - op: test
            any:
              - {op: test, eq: [retirement.has_exception, {const: true}]}
              - {op: test, ne: [retirement.code, {const: "early_1"}]}
  - id: person.h_must_hsa
    printed: "(helper)"
    label: "Forms 8889 with excess HSA contributions"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.excess, {const: true}]}}
  - id: person.x_must
    printed: "(helper)"
    label: "Reasons Form 5329 must be filed (zero if the 10% tax can be reported directly on Schedule 2, line 8)"
    type: Count
    expr: {op: sum, of: [person.h_must_ret, person.h_must_hsa]}
    note: "Form 5329 need not be filed when code 1 is shown on all Forms 1099-R and the tax is owed on the full amount. It must be filed for an exception or an excess HSA contribution."
  - id: person.x_c05
    printed: "(helper)"
    label: "Medical expense (05) exception amounts claimed"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e05}
  - id: person.h_e23_n
    printed: "(helper)"
    label: "Number of emergency personal expense distributions"
    type: Count
    expr: {op: sum_over, collection: retirement, field: retirement.one, where: {op: test, eq: [retirement.is_e23, {const: true}]}}
  - id: person.x_two23
    printed: "(helper)"
    label: "More than one emergency personal expense distribution in 2025 (limited to one per calendar year)"
    type: Bool
    expr: {op: test, gt: [person.h_e23_n, {const: 1, type: Count}]}
```
```
