# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 228beb7d02996aad27975fec7478712d83a54ccf0697498143c056a8566d8f9b |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 25a027e7aa88c70d64dda6eb43ac51e5a2717be1571ef98eb893397e37eb52cb |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 2b3224752ef85bc094959c9f6706438fd33497470ba985e73879f419226182f1 |
| printed lines compared | 99 |
| agree / disagree / missing | 3 / 96 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 40, 41, 44, 45, 47, 66, 93, 95, 96, 97, 98, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 17, 18, 19, 26, 27, 28, 30, 31, 40, 41, 44, 45, 66, 93, 95, 96, 98, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
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
| p503 | For use in preparing 2025 returns | 3, 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- person.person.employers: reference 'one' does not resolve
- person.person.overcount: reference 'one' does not resolve
- person.person.wages: reference 'wages' does not resolve
- person.person.withheld: reference 'box4' does not resolve
- person.person.hsa_forms: reference 'one' does not resolve
- person.person.hsa_split: reference 'one' does not resolve
- person.person.hsa_agreed: reference 'one' does not resolve
- person.person.hsa_step1: reference 'step1' does not resolve
- person.person.hsa_share: reference 'share' does not resolve
- person.person.hsa_deduction: reference 'line13' does not resolve
- person.person.hsa_taxable: reference 'line16' does not resolve
- person.person.hsa_addtax: reference 'line17b' does not resolve
- person.person.tip_employers: reference 'one' does not resolve
- person.person.tip_total: reference 'col_d' does not resolve
- person.person.tip_reported: reference 'amount' does not resolve
- person.person.ot_employers: reference 'one' does not resolve
- person.person.ot_total: reference 'col_b' does not resolve
- person.person.box1: reference 'box1' does not resolve
- person.person.box2: reference 'box2' does not resolve
- person.person.ira_amount_a: reference 'amount_a' does not resolve
- person.person.ira_taxable: reference 'ira_taxable' does not resolve
- person.person.ira_rollovers: reference 'one' does not resolve
- person.person.plan_amount_a: reference 'amount_a' does not resolve
- person.person.plan_taxable: reference 'plan_taxable' does not resolve
- person.person.plan_rollovers: reference 'one' does not resolve
- person.person.sav_dist: reference 'sav_amount' does not resolve
- person.person.medicare5: reference 'box5' does not resolve
- person.person.medicare6: reference 'box6' does not resolve
- person.person.sc_count: reference 'one' does not resolve
- person.person.ho_count: reference 'one' does not resolve
- person.person.mq_q4: reference 'mq_q4' does not resolve
- person.person.mq_total: reference 'mq_total' does not resolve
- person.person.cost179: reference 'cost179' does not resolve
- person.person.s179_nonlisted: reference 's179_allowed' does not resolve
- person.person.income179: reference 'line31' does not resolve
- person.person.sc_total: reference 'line31' does not resolve
- person.person.positive_profits: reference 'line31' does not resolve
- person.person.sehi: reference 'f7206_line14' does not resolve
- person.person.qbi: reference 'qbi' does not resolve
- person.person.dc_benefits: reference 'dc_benefits' does not resolve
- person.person.ira_8606_line14: reference 'line14' does not resolve
- person.person.x_l1: reference 'l1' does not resolve
- person.person.x_l2_all: reference 'l2' does not resolve
- person.person.x_l1_s: reference 'l1_s' does not resolve
- person.person.x_l2_s: reference 'l2_s' does not resolve
- person.person.x_tax: reference 'tax' does not resolve
- person.person.x_must: reference 'one' does not resolve
- person.person.x_c05: reference 'l2_e05' does not resolve
- person.person.x_limited_sum: reference 'l2' does not resolve
- person.person.x_hsa_excess: reference 'l49' does not resolve
- person.h_sav_deferral: reference 'sav_deferral' does not resolve
- person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity
- person.h_ss_wages: reference 'wages' does not resolve
- person.h_ss_room: reference 'ss.base' does not resolve
- person.h_e23_count: reference 'one' does not resolve

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: representation; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 93, Line 11: "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025." Same expression as fix round 3: the smaller of the expenses and $300 (s1.educator_max) for an eligible educator and zero otherwise, the Claude reply's formula, ruled representation in that log (only the order of the two dispositive questions differs; eligibility is asked where the expenses are zero). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_forms", "message": "person.person.hsa_forms: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_forms) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}, "invalid_model_types": [{"line": "person.hsa_split", "message": "person.person.hsa_split: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_split) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}, {"args": [{"const": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "one", "op": "sum_over", "where": {"args": [{"const": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}}, "invalid_model_types": [{"line": "person.hsa_agreed", "message": "person.person.hsa_agreed: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_agreed) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, as in fix round 3: forms with f8889.allocation agreed, without the spouse-rule filter; the allocation is asked only within the spouse rule and household.hsa_agreed_count is read only on split forms. A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 253 refused-return records (project 0 against 1 on forms outside the rule) and on 11 completed ones that ask the allocation outside the rule (stage13.hsa_one_spouse_family, stage16.small.s4). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "step1", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_step1", "message": "person.person.hsa_step1: reference 'step1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_step1) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, as in fix round 3: the sum of f8889.step1 over all of the person's forms; it feeds only household.hsa_step1_sum, read only in f8889.allocation_bad on a split form, where the two sums are equal. A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on non-split forms where the project's line is $0.00 (129 completed, for example classm.s3.3.deepseek $0.00 against $712.50), which reach no printed amount. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "share", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_share", "message": "person.person.hsa_share: reference 'share' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_share) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, as in fix round 3: it sums f8889.share, the published field carrying the f8889.allocation_bad refusal whose test reads household.hsa_share_sum, which sums this line: a cycle ("cycle at household.hsa_share_sum" in the scratch evaluation), and without the spouse-rule filter it also differs on non-split forms (127 completed, for example classm.s3.3.deepseek $0.00 against $356.25). The interface gave f8889.share_raw and f8889.share by id and type only (fix round 3's interface gap). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_deduction — Form 8889 line 13 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line13", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "line13", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_deduction", "message": "person.person.hsa_deduction: reference 'line13' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_deduction) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, the sum of f8889.line13, the project's expression; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only on stage13.hsa_agreed_all_to_you (completed), where the reply's person.hsa_share cycle reaches it, and on refused returns. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_taxable — Form 8889 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line16", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "line16", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_taxable", "message": "person.person.hsa_taxable: reference 'line16' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_taxable) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.hsa_addtax — Form 8889 line 17b for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line17b", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "line17b", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_addtax", "message": "person.person.hsa_addtax: reference 'line17b' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.hsa_addtax) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.tip_employers — Number of employers that paid this person qualified tips
Status: **DISAGREE**

Project:

```json
{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "tipjob", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.tip_employers", "message": "person.person.tip_employers: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.tip_employers) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.tip_total — This person's worksheet column (d) total
Status: **DISAGREE**

Project:

```json
{"collection": "tipjob", "field": "tipjob.col_d", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "tipjob", "field": "col_d", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.tip_total", "message": "person.person.tip_total: reference 'col_d' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.tip_total) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.tip_reported — This person's worksheet column (b) total
Status: **DISAGREE**

Project:

```json
{"collection": "tipjob", "field": "tipjob.amount", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "tipjob", "field": "amount", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.tip_reported", "message": "person.person.tip_reported: reference 'amount' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.tip_reported) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **DISAGREE**

Project:

```json
{"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "otjob", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.ot_employers", "message": "person.person.ot_employers: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ot_employers) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ot_total — This person's overtime worksheet column (b) total
Status: **DISAGREE**

Project:

```json
{"collection": "otjob", "field": "otjob.col_b", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "otjob", "field": "col_b", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.ot_total", "message": "person.person.ot_total: reference 'col_b' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ot_total) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.box1 — Total W-2 box 1 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.box1) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.box2 — Total W-2 box 2 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.box2", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "box2", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.box2", "message": "person.person.box2: reference 'box2' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.box2) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_amount_a — IRA distributions on this person's Forms 1099-R (line 4a amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "amount_a", "op": "sum_over", "where": {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}}, "invalid_model_types": [{"line": "person.ira_amount_a", "message": "person.person.ira_amount_a: reference 'amount_a' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ira_amount_a) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, it sums line 4a amounts over entries whose account is traditional_ira, where the project sums every IRA entry (retirement.is_ira); A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 10 completed generated returns (generated 90, 181, 224: for example $24,237.07 against $0.00), IRA entries whose account is not traditional_ira. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_taxable — Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "ira_taxable", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.ira_taxable", "message": "person.person.ira_taxable: reference 'ira_taxable' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ira_taxable) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, it sums retirement.ira_taxable over every entry, where the project sums retirement.taxable over IRA entries (retirement.is_ira). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 20 completed records (classm.f8962.2 $0.00 against $44,119.00; classm.ira.2 $7,514.00 against $28,257.00; stage21.blind.e1 $5,123.45 against $7,580.23). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_rollovers — Number of this person's IRA distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}}, "invalid_model_types": [{"line": "person.ira_rollovers", "message": "person.person.ira_rollovers: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ira_rollovers) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.plan_amount_a — Pension and annuity distributions on this person's Forms 1099-R (line 5a amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "amount_a", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}}, "invalid_model_types": [{"line": "person.plan_amount_a", "message": "person.person.plan_amount_a: reference 'amount_a' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.plan_amount_a) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.plan_taxable — Taxable pension and annuity distributions on this person's Forms 1099-R (line 5b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "plan_taxable", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.plan_taxable", "message": "person.person.plan_taxable: reference 'plan_taxable' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.plan_taxable) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, it sums retirement.plan_taxable, bypassing the refusals the project's operand retirement.taxable carries (as fix round 2's reply did). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 48 completed records (classm.f5329.2 $0.00 against $25,190.00; classm.ira.2 $20,082.00 against $27,596.00) and the candidate computes where the project refuses at retirement special and bad_code (cited). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.plan_rollovers — Number of this person's pension distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "all"}}, "invalid_model_types": [{"line": "person.plan_rollovers", "message": "person.person.plan_rollovers: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.plan_rollovers) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sav_dist — Distributions received in 2025 that Form 8880 line 4 counts, on this person's Forms 1099-R
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.sav_amount", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "sav_amount", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sav_dist", "message": "person.person.sav_dist: reference 'sav_amount' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.sav_dist) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.medicare5 — Total W-2 box 5 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.box5", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "box5", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.medicare5", "message": "person.person.medicare5: reference 'box5' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.medicare5) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, the sum of W-2 Medicare wages, the project's amount, without the project's railroad refusal (person.rrta, cited Form 8959 lines 1 to 7: RRTA compensation outside the supported path); A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only by that cited refusal on refused returns and by records where the project needs the railroad answer (incomplete or refused returns). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.medicare6 — Total W-2 box 6 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.box6", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "box6", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.medicare6", "message": "person.person.medicare6: reference 'box6' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.medicare6) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, the sum of W-2 Medicare wages, the project's amount, without the project's railroad refusal (person.rrta, cited Form 8959 lines 1 to 7: RRTA compensation outside the supported path); A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only by that cited refusal on refused returns and by records where the project needs the railroad answer (incomplete or refused returns). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sc_count — Number of Schedules C for this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sc_count", "message": "person.person.sc_count: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.sc_count) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ho_count — Number of this person's Schedules C that claim the business use of the home
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.ho_uses"}], "test": "eq"}}
```

Second:

```json
{"expression": {"collection": "sc", "field": "one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.ho_uses"}], "test": "eq"}}, "invalid_model_types": [{"line": "person.ho_count", "message": "person.person.ho_count: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ho_count) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.mq_q4 — Mid-quarter test basis, fourth quarter, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.mq_q4", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "mq_q4", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.mq_q4", "message": "person.person.mq_q4: reference 'mq_q4' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.mq_q4) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.mq_total — Mid-quarter test basis, 2025, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.mq_total", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "mq_total", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.mq_total", "message": "person.person.mq_total: reference 'mq_total' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.mq_total) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.cost179 — Cost of section 179 property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.cost179", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "cost179", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.cost179", "message": "person.person.cost179: reference 'cost179' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.cost179) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.s179_nonlisted — Section 179 elected, other than listed property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f6", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "s179_allowed", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.s179_nonlisted", "message": "person.person.s179_nonlisted: reference 's179_allowed' does not resolve"}]}
```

Second transcription's note: The child Schedule C fields do not split listed from nonlisted section 179; this reading puts the allowed section 179 amount in nonlisted property.

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.s179_nonlisted) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, the cost of the businesses' section 179 property less its listed figure, the cost rather than the elected amount (published as sc.f6; i4562 p. 5, Line 6, "Column (c)—Elected cost. Enter the amount you elect to expense"). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Second transcription's note: The child Schedule C fields do not split listed from nonlisted section 179; this reading puts listed property at zero.

Ruling: interface gap; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i4562 p. 5, Line 7: "Enter the amount that you elected to expense for listed property (defined earlier) on line 29 here." The reply changed: it now enters zero (its note: "The child Schedule C fields do not split listed from nonlisted section 179"), so listed property elected under section 179 is lost (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): classm.eic.3 $10,918.00 against $0.00, stage14.veh.suv_179 $31,300.00 against $0.00, stage14.asset.listed_and_not $400.00 against $0.00; completed). The pages given omit the p. 5 line 7 instruction and sc.f29 was published by id and type only (as ruled since round 2). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.income179 — Business net profit or loss without section 179, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.line31_pre179", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.income179", "message": "person.person.income179: reference 'line31' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.income179) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sc_total — This person's Schedule C net profit or loss (all businesses)
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.sc_total) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.se_line6 — Schedule SE line 6 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, person.sc_total, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the se definition bound to its person.sc_total and person.wages, without the project's se_screen and railroad refusals (person.se_screened, person.se_rrta, cited i1040sse pp. 1-5 and Schedule SE line 8a). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.se_line12 — Schedule SE line 12 (self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"ref": "ss.base"}, "op": "subtract_floor0", "take": {"collection": "w2", "field": "wages", "op": "sum_over", "where": null}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the se definition bound to its person.sc_total and person.wages, without the project's se_screen and railroad refusals (person.se_screened, person.se_rrta, cited i1040sse pp. 1-5 and Schedule SE line 8a). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.se_line13 — Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"ref": "ss.base"}, "op": "subtract_floor0", "take": {"collection": "w2", "field": "wages", "op": "sum_over", "where": null}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the se definition bound to its person.sc_total and person.wages, without the project's se_screen and railroad refusals (person.se_screened, person.se_rrta, cited i1040sse pp. 1-5 and Schedule SE line 8a). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it chooses on person.plan with no Schedule C gate, so it asks plan of a person with no Schedule C (placement; 729 completed records) and computes a SEP or SIMPLE amount for such a person where the project enters zero (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 73 completed records, classm.f1040.5 $0.00 against $2,053.00, classm.s3.4 $0.00 against $8,925.00, each supplying a plan for a person with no Schedule C); it also inherits the section 179 cycle on returns with a Schedule C. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "line31", "op": "sum_over", "where": {"args": [{"const": 0}, {"ref": "sc.line31"}], "test": "lt"}}, "invalid_model_types": [{"line": "person.positive_profits", "message": "person.person.positive_profits: reference 'line31' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.positive_profits) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sehi — Self-employed health insurance deduction, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f7206_line14", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "f7206_line14", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sehi", "message": "person.person.sehi: reference 'f7206_line14' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.sehi) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.qbi — Qualified business income or loss of this person's businesses
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.qbi", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "qbi", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.qbi", "message": "person.person.qbi: reference 'qbi' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.qbi) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"ref": "ss.base"}, "op": "subtract_floor0", "take": {"collection": "w2", "field": "wages", "op": "sum_over", "where": null}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the se definition bound to its person.sc_total and person.wages, without the project's se_screen and railroad refusals (person.se_screened, person.se_rrta, cited i1040sse pp. 1-5 and Schedule SE line 8a). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.tips_ot"}], "test": "eq"}}
```

Second:

```json
{"expression": {"collection": "sc", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sc_count", "message": "person.person.sc_count: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.sc_count, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it copies person.sc_count (every Schedule C) where the project counts only Schedules C with Schedule 1-A tips or overtime (sc.tips_ot; i1040gi p. 104, Schedule 1-A Line 5, "Include the qualified tips you and/or your spouse received in the course of a trade or business"). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 343 completed records (classm.f4952.1.deepseek 0 against 1). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.dc_benefits — This person's dependent care benefits from Forms W-2 box 10, less the part reported in box
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.dc_benefits", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "dc_benefits", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.dc_benefits", "message": "person.person.dc_benefits: reference 'dc_benefits' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.dc_benefits) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.dc_has_box10 — This person's Forms W-2 show dependent care benefits in box 10
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}
```

Second:

```json
{"expression": {"args": [{"const": 0}, {"collection": "w2", "field": "dc_benefits", "op": "sum_over", "where": null}], "test": "lt"}, "invalid_model_types": [{"line": "person.dc_benefits", "message": "person.person.dc_benefits: reference 'dc_benefits' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.dc_benefits, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the count of Forms W-2 with dependent care benefits above zero, the project's test in another form; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only on one refused return (a candidate refusal reached through its other lines). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"expression": {"from": {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}, "op": "subtract", "take": {"const": 0}}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, W-2 box 1 only: it omits the line 1e part of line 1z (amb.2025.dc_line1e_attribution) and the self-employment part (i2441 p. 4: "2. The amount shown on Schedule SE (Form 1040), line 3, minus any deduction you claim on Schedule 1 (Form 1040), line 15"). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 364 completed records (classm.f2441.4 $5,000.00 against $3,000.00; classm.f4952.1.deepseek $168,227.38 against $32,936.00). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without t
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"expression": {"from": {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}, "op": "subtract", "take": {"const": 0}}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, W-2 box 1 only, omitting the self-employment part (i2441 p. 4, item 2). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 343 completed records (classm.f4952.1.deepseek $168,227.38 against $32,936.00; classm.f8863.2 -$146,616.56 against $0.00). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: ambiguity; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. amb.2025.savers_ineligible_column (owner decision). f8880 p. 2, Who Can Take This Credit: "(a) was born after January 1, 2008; (b) is claimed as a dependent on someone else's 2025 tax return; or (c) was a student." The reply changed in form only (born after January 1, 2008, a dependent claimed by someone else, or a student, each as its own test), the Claude reply's reading, ruled ambiguity in that log (every value record supplies sav_claimed yes with sa.dependent no, a record the interview does not produce; the scratch evaluation shows the same 197 records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: scope; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f8880 line 1: "Traditional and Roth IRA contributions, and ABLE account contributions by the designated beneficiary for 2025". Same expression as fix rounds 2 and 3: person.ira_trad plus person.sav_roth, without the project's sav_trad gate (the amount is the same wherever ira_trad is asked; the reply asks the amount where the project infers zero from a No: placement); the project refuses excess contributions at person.ira_excess_gate (p590a p. 35). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"input": "person.sav_voluntary"}, {"collection": "w2", "field": "sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}, "invalid_model_types": [{"line": "h_sav_deferral", "message": "person.h_sav_deferral: reference 'sav_deferral' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_sav_deferral, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, box 12 deferrals and voluntary contributions only, as in fix round 3, omitting a self-employed person's own SIMPLE salary reduction contributions (person.sav_simple) and the excess-deferral refusal (person.sav_excess_gate, cited). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 5 completed records (stage14.simple.at_limit $16,500.00 against $0.00; classm.se.2 spouse $7,815.00 against $0.00). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: scope; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 98, line 11. Same expression as fix rounds 2 and 3: person.ira_trad for everyone; the project asks the amount after a Yes to person.sav_trad (placement) and refuses excess contributions at person.ira_excess_gate (p590a p. 35). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 96, Were You Covered by a Retirement Plan?: "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan." Same expression as fix rounds 2 and 3: person.ira_work_plan alone, dropping the person's own SEP or SIMPLE plan (the project reads person.ira_se_plan; amb.2025.ira_covered). Scratch evaluation: classm.ira.2 spouse and generated 163 (completed, a Schedule C with a plan): project True, candidate False. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: representation; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 97, line 2 ("Married filing jointly, enter $146,000 in both columns. But if you checked "No" on either line 1a or 1b, enter $246,000 for the person who wasn't covered by a plan"), after line 1: "If you checked "No" on line 1a (and "No" on line 1b if married filing jointly), skip lines 2 through 6". Same structure as fix round 2: the status amount for a covered person and $246,000 otherwise, which equals the source on every worksheet that reaches line 2 (a person not covered reaches it only on a joint return whose spouse is covered); the scratch evaluation's values are single or qualifying-surviving-spouse persons not covered (classm.f4952.1.deepseek $89,000.00 against $246,000.00), inside skipped lines. It reads its own person.ira_cov, ruled there. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract li
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 97, line 6: "Subtract line 5 from line 2 in each column". The reply changed: its line 2 less its worksheet line 5. Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), on 363 of its 1,426 completed candidate-unknown records; the others ask ira_work_plan where the interview does not (514) or inherit the section 179 cycle. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}
```

Second transcription's note: Uses the 70% rate and the $200 floor as a default; age and filing-status rate variants are not encoded.

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 98, line 7: "Multiply lines 6a and 6b by the percentage below that applies to you. If the result isn't a multiple of $10, increase it to the next multiple of $10 ... But if it is less than $200, enter $200", with 70% or 80% (age 50 or older) and the joint-return rates; lines 2 to 6 are skipped for a person not covered (line 1). The reply changed: the larger of its rounded 70% figure and $200 for everyone (its note: "age and filing-status rate variants are not encoded"), with no branch for a person not covered or for line 6 zero ("None of your IRA contributions are deductible"); and through its line 6 it inherits the worksheet cycle: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation) (900 completed candidate-unknown records in the scratch evaluation; the 361 candidate refusals are other forms' refusals reached through it on refused returns). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}, {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}], "op": "smaller_of"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Second transcription's note: Earned income for the line 10 limit is read from Form W-2 box 1; self-employment earned income is not added.

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}, {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}], "op": "smaller_of"}], "op": "smaller_of"}}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"expression": {"args": [{"const": 0}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}, {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}], "op": "smaller_of"}], "op": "smaller_of"}}], "test": "lt"}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: scope; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8606 p. 9, Line 2: "Generally, if this is the first year you are required to file Form 8606, enter -0-" and otherwise the Total Basis Chart amount. Same expression as fix rounds 2 and 3: it copies person.ira_basis for everyone; the project asks the basis only of a Form 8606 filer and refuses an adjusted basis at person.ira_basis_gate (cited): placement and that cited refusal. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f8606 (2025) Part I: "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?"; p590a p. 15, Both contributions for 2025 and distributions in 2025. The reply changed: it copies person.ira_dist for everyone, where the project's gate is a distribution together with nondeductible contributions for 2025 (the case it refuses). It asks ira_dist of every person (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 817 completed candidate-unknown records, classm.f2441.1.deepseek; the interview asks it only of a Form 8606 filer), an answer the source does not need, and its person.ira_8606_line14 then refuses any person with a distribution. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier ye
Status: **DISAGREE**

Project:

```json
{"collection": "f8606", "field": "f8606.line14", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8606", "field": "line14", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.ira_8606_line14", "message": "person.person.ira_8606_line14: reference 'line14' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.ira_8606_line14) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}, {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}], "op": "smaller_of"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}, {"collection": "w2", "field": "box1", "op": "sum_over", "where": null}], "op": "smaller_of"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.box1", "message": "person.person.box1: reference 'box1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.box1, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading: Its worksheet line 5 (h_ira_line5) copies f1040.line11a, adjusted gross income, which includes the IRA deduction itself, where the source starts from line 9 less the Schedule 1 adjustments other than the IRA deduction (i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" and "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"): a cycle ("cycle at person.ira_line6" in the scratch evaluation), which reaches this line in the scratch evaluation on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.edu_kid — Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of yo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0}, {"ref": "f8863.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8863.line7"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 7, Line 7: "You don't qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." The published person.edu_kid is that test (read by f8863.no_refund). As in fix round 3 the reply redefines the line as "Student qualifies for the American opportunity credit" (lines 23 to 26, Form 1098-T and EIN answers), a different quantity, so in its graph the refundable part is withheld from eligible students and allowed to filers the test bars (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): stage19.example.bill.ex1 False against True, 13 completed records); it also needs person.edu_line23 on every return (951 completed records), an answer the interview asks only of a student. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_l1 — Form 5329 line 1 for this person: early distributions includible in income
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l1", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l1", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l1", "message": "person.person.x_l1: reference 'l1' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_l1) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_l2_all — Exception amounts before the per-person limits
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l2", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l2_all", "message": "person.person.x_l2_all: reference 'l2' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_l2_all) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_l1_s — Line 1 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l1_s", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l1_s", "message": "person.person.x_l1_s: reference 'l1_s' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_l1_s) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_l2_s — Line 2 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l2_s", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_l2_s", "message": "person.person.x_l2_s: reference 'l2_s' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_l2_s) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_tax — This person's Form 5329 taxes
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.tax", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f5329", "field": "tax", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_tax", "message": "person.person.x_tax: reference 'tax' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_tax) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, the sum of f5329.tax; through its person.x_hsa_excess (which sums f5329.l49, a line that reads this person's lines) the scratch evaluation reports "cycle at f5329.l49" on 1,719 completed records, and it refuses at its x_limit_binds on 11 completed ones (stage21.blind.e3). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_must — One if this person must file Form 5329
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f5329.l48"}], "test": "lt"}], "test": "any"}}
```

Second:

```json
{"expression": {"collection": "f5329", "field": "one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f5329.l48"}], "test": "lt"}], "test": "any"}}, "invalid_model_types": [{"line": "person.x_must", "message": "person.person.x_must: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_must) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression (f5329 forms with f5329.must); but through the reply's person.x_hsa_excess, read by the Form 5329 lines that f5329.must reads, the scratch evaluation reports "cycle at f5329.l49" on 1,716 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_c05 — Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l2_e05", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_c05", "message": "person.person.x_c05: reference 'l2_e05' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_c05) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, as in fix round 3: the exception 05 amounts with no limit, where the project limits them to Schedule A line 4 (i5329 p. 5, exception 05: "up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income"; decision D4). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): stage21.blind.e6 (completed) $7,475.00 against $9,000.00. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_two23 — Exception 23 claimed on more than one distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"expression": {"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "invalid_model_types": [{"line": "h_e23_count", "message": "person.h_e23_count: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_e23_count, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_limited_sum — Exceptions 05, 09, 19, 22 and 23 within their limits
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Second:

```json
{"expression": {"collection": "retirement", "field": "l2", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_limited_sum", "message": "person.person.x_limited_sum: reference 'l2' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_limited_sum) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, it sums every exception amount (retirement.l2) with none of the 05, 09, 19, 22 or 23 limits (p590b p. 27: "up to $10,000" for exception 09). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs on 8 completed records (stage21.blind.e4 $13,800.00 against $19,000.00; stage21.mut.e23_over_cap $1,000.00 against $1,500.00; stage21.blind.e3 $0.00 against $11,200.00). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_other_exc — Exceptions without a fixed limit
Status: **DISAGREE**

Project:

```json
{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}
```

Second:

```json
{"const": 0}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude." The reply enters zero for the exceptions without a fixed limit, so the exceptions without a fixed limit (for example the higher education expenses exception) are never excluded (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): stage21.example.teacher_education $500.00 against $0.00, stage21.blind.e3 $11,200.00 against $0.00, stage21.blind.e8 $15,000.00 against $0.00; completed). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_limit_binds — A limited exception over its limit on a person with a code S distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"expression": {"args": [{"const": 0}, {"collection": "retirement", "field": "l2", "op": "sum_over", "where": null}], "test": "lt"}, "invalid_model_types": [{"line": "person.x_limited_sum", "message": "person.person.x_limited_sum: reference 'l2' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.x_limited_sum, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it is true where its unlimited sum exceeds the limited one, without the project's code S condition (amb.2025.f5329_simple_limits), and through person.x_limited_sum it is true wherever any exception is claimed: A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) gives True against False on 11 completed records (stage21.example.teacher_education, stage21.blind.e3, e4), where the reply's person.x_tax then refuses returns the project computes. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### person.x_hsa_excess — This person's 2025 HSA excess contributions (Form 8889)
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.excess_amt", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f5329", "field": "l49", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.x_hsa_excess", "message": "person.person.x_hsa_excess: reference 'l49' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.x_hsa_excess) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, it sums f5329.l49 (the 6% tax on HSA excess contributions), a line of the per-person Form 5329 that reads this person's lines, so the scratch evaluation reports "cycle at f5329.l49" on 1,730 completed records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### employers — Total w2.one for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.one", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "one", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.employers", "message": "person.person.employers: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.employers) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### overcount — Number of employers that withheld more than the limit
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.one", "op": "sum_over", "where": {"args": [{"param": "ss.limit"}, {"ref": "w2.box4"}], "test": "lt"}}
```

Second:

```json
{"expression": {"collection": "w2", "field": "one", "op": "sum_over", "where": {"args": [{"param": "ss.limit"}, {"ref": "w2.box4"}], "test": "lt"}}, "invalid_model_types": [{"line": "person.overcount", "message": "person.person.overcount: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.overcount) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### over — Any employer withheld more than the limit
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"line": "overcount"}], "test": "lt"}
```

Second:

```json
{"expression": {"args": [{"const": 0, "type": "Count"}, {"line": "overcount"}], "test": "lt"}, "invalid_model_types": [{"line": "person.overcount", "message": "person.person.overcount: reference 'one' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.overcount, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### wages — Total w2.wages for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.wages", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "wages", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.wages", "message": "person.person.wages: reference 'wages' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.wages) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### withheld — Total w2.box4 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "w2", "field": "w2.box4", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "w2", "field": "box4", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.withheld", "message": "person.person.withheld: reference 'box4' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line (person.withheld) is one of them, so this ruling adjudicates the declaration, not the tax reading. By reading, with the prefix restored it is the project's expression or the same quantity; scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows no difference on any record. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### eligible — More than one employer and total social security wages over $176,100
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"expression": {"args": [{"args": [{"const": false}, {"line": "over"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}, "invalid_model_types": [{"line": "person.employers", "message": "person.person.employers: reference 'one' does not resolve"}, {"line": "person.overcount", "message": "person.person.overcount: reference 'one' does not resolve"}, {"line": "person.wages", "message": "person.person.wages: reference 'wages' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.employers, person.overcount, person.wages, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it adds "no employer withheld more than the limit" (i1040gi p. 117, Line 11: "But if any one employer withheld more than $10,918.20, you can't claim the excess on your return"); the project refuses person.credit when person.over; A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only on refused returns (classm.w2.1, ss.multi.over: project True, candidate False), as ruled representation in the Claude log. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### excess — Withholding above $10,918.20, if any
Status: **DISAGREE**

Project:

```json
{"from": {"line": "withheld"}, "op": "subtract_floor0", "take": {"param": "ss.limit"}}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}, "then": {"from": {"line": "withheld"}, "op": "subtract_floor0", "take": {"param": "ss.limit"}}}], "op": "choose"}, "invalid_model_types": [{"line": "person.employers", "message": "person.person.employers: reference 'one' does not resolve"}, {"line": "person.overcount", "message": "person.person.overcount: reference 'one' does not resolve"}, {"line": "person.wages", "message": "person.person.wages: reference 'wages' does not resolve"}, {"line": "person.withheld", "message": "person.person.withheld: reference 'box4' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.employers, person.overcount, person.wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the withholding above the limit, the project's amount; A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only on refused returns and partials. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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
{"expression": {"line": "excess"}, "invalid_model_types": [{"line": "person.employers", "message": "person.person.employers: reference 'one' does not resolve"}, {"line": "person.overcount", "message": "person.person.overcount: reference 'one' does not resolve"}, {"line": "person.wages", "message": "person.person.wages: reference 'wages' does not resolve"}, {"line": "person.withheld", "message": "person.person.withheld: reference 'box4' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.employers, person.overcount, person.wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it copies person.excess without the project's eligibility choice and railroad and over-withholding refusals (person.rrta, person.over, cited); A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) differs only by those cited refusals on refused returns and by incomplete records. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 1 — Net profit from Schedule C, line 31
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads person.sc_total, which is among them, so this ruling adjudicates the declaration, not the tax reading. By reading, it copies person.sc_total, the project's operand, without the project's refusal at person.se_screened (cited above), and inherits the reply's section 179 cycle: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"ref": "ss.base"}, "op": "subtract_floor0", "take": {"collection": "w2", "field": "wages", "op": "sum_over", "where": null}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, the se definition bound to its person.sc_total and person.wages, without the project's se_screen and railroad refusals (person.se_screened, person.se_rrta, cited i1040sse pp. 1-5 and Schedule SE line 8a). On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **DISAGREE**

Project:

```json
{"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}
```

Second:

```json
{"expression": {"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, Step 3 (Step 1 less Step 2, floored at zero); it inherits the section 179 cycle through Step 1: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}
```

Second:

```json
{"expression": {"line": "Step 3"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Second transcription's note: The reduced SEP rate table is not expressible with the available atoms; this reading uses net earnings as step 5.

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, Step 5 (it copies Step 3, without the reduced-rate figure p560 p. 39 asks for: "Multiply step 3 by step 4", the rate from the Rate Table for Self-Employed); it inherits the section 179 cycle through Step 1: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **DISAGREE**

Project:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"param": "ret.comp_limit"}
```

Second transcription's note: Multiplying the $350,000 compensation limit by the plan rate is not expressible; this reading uses the compensation limit itself as step 6.

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. p560 p. 39, Step 6: "Multiply $350,000 by your plan contribution rate (not the reduced rate)". The reply changed: it enters the $350,000 limit itself (its note: "Multiplying the $350,000 compensation limit by the plan rate is not expressible"); the interface expresses it (prorate with a count, the project's form, and fix round 3's reply's). A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) gives $350,000.00 against the rate's amount on 919 completed records (classm.f4952.1.deepseek $10,500.00 against $350,000.00). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, Step 7; it inherits the section 179 cycle through Step 1: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### Step 8 — Contribution dollar limit
Status: **AGREE**

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "Step 7"}, {"line": "Step 8"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "Step 7"}, {"line": "Step 8"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.sc_total", "message": "person.person.sc_total: reference 'line31' does not resolve"}, {"line": "h_se_4a_pos", "message": "person.h_se_4a_pos: declared NonNegDollars but the expression does not prove non-negativity"}, {"line": "h_ss_wages", "message": "person.h_ss_wages: reference 'wages' does not resolve"}, {"line": "h_ss_room", "message": "person.h_ss_room: reference 'ss.base' does not resolve"}]}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (triage/person.deepseek.json, state invalid), so triage executed none of its lines: 53 collection sums name the field without its collection's prefix (for example person.hsa_forms sums field "one" of f8889: "person.person.hsa_forms: reference 'one' does not resolve"; the published field is f8889.one), h_ss_room names the parameter ss.base as a line ("reference 'ss.base' does not resolve"), and h_se_4a_pos is "declared NonNegDollars but the expression does not prove non-negativity". This line reads h_se_4a_pos, h_ss_room, h_ss_wages and others, which are among them, so this ruling adjudicates the declaration, not the tax reading. By reading, Step 21; it inherits the section 179 cycle through Step 1: On returns with a Schedule C the reply's graph is circular: its person.income179 (the section 179 business income limit) sums sc.line31, which is after the section 179 deduction that the limit governs (i4562 p. 5, Line 11: "computed without regard to any section 179 expense deduction"), so the scratch evaluation reports "cycle at sc.s179_allowed" on every such return (343 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: the aqee arithmetic for a person whose redefined person.edu_kid is true (lines 23 to 26, Form 1098-T and EIN answers). That gate has no TIN test at all (i8863 p. 3: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; neither person.tin nor person.itin_applied, so BUG-0259's rewording does not reach it), omits the filers' TIN test (household.all_tin, amb.2025.edu_filer_tin) and the f8863.paid screen, so it needs person.edu_line23 of every person (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 951 completed candidate-unknown records, classm.f2441.1.deepseek), an answer the source does not need where no qualified expenses were paid. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: the aqee arithmetic for a person whose redefined person.edu_kid is true (lines 23 to 26, Form 1098-T and EIN answers). That gate has no TIN test at all (i8863 p. 3: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; neither person.tin nor person.itin_applied, so BUG-0259's rewording does not reach it), omits the filers' TIN test (household.all_tin, amb.2025.edu_filer_tin) and the f8863.paid screen, so it needs person.edu_line23 of every person (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 951 completed candidate-unknown records, classm.f2441.1.deepseek), an answer the source does not need where no qualified expenses were paid. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: the aqee arithmetic for a person whose redefined person.edu_kid is true (lines 23 to 26, Form 1098-T and EIN answers). That gate has no TIN test at all (i8863 p. 3: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; neither person.tin nor person.itin_applied, so BUG-0259's rewording does not reach it), omits the filers' TIN test (household.all_tin, amb.2025.edu_filer_tin) and the f8863.paid screen, so it needs person.edu_line23 of every person (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 951 completed candidate-unknown records, classm.f2441.1.deepseek), an answer the source does not need where no qualified expenses were paid. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

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

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: the aqee arithmetic for a person whose redefined person.edu_kid is true (lines 23 to 26, Form 1098-T and EIN answers). That gate has no TIN test at all (i8863 p. 3: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; neither person.tin nor person.itin_applied, so BUG-0259's rewording does not reach it), omits the filers' TIN test (household.all_tin, amb.2025.edu_filer_tin) and the f8863.paid screen, so it needs person.edu_line23 of every person (A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record): 951 completed candidate-unknown records, classm.f2441.1.deepseek), an answer the source does not need where no qualified expenses were paid. Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}
```

Ruling: model error; Not executable: the reply fails validation on 55 declarations (53 collection sums naming the field without its collection's prefix, for example person.hsa_forms: "reference 'one' does not resolve"; h_ss_room: "reference 'ss.base' does not resolve"; h_se_4a_pos: "declared NonNegDollars but the expression does not prove non-negativity"), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 2, as at line 27; line 31 is the lifetime learning credit amount, for a student for whom the American opportunity credit is not claimed. The reply changed: it copies its own net-expense helper (h_edu_net) for every person, with no lifetime learning eligibility gate (edu, Form 1098-T, TIN, f8863.paid) and no exclusion of American opportunity students. A scratch evaluation of the reply with the prefixes restored (also ss.base as a parameter and floors on h_se_4a_pos and person.positive_profits; tools/transcription/triage.mjs on the same bank with the witness cap lifted, a reading aid and not a triage record) shows it on lines the project hides for an American opportunity student (18 completed records: classm.f8863.4 $4,000.00, stage19.example.bill.ex1 $5,600.00), different amounts where both show it (8 completed: classm.f5695.2 $2,429.00 against $2,990.00, stage19.blind.e10 $5,600.00 against $5,900.00), and needs edu_inst of every person (992 completed records). Fix round 4 re-check: the only project change since fix round 3 is BUG-0259 (person.itin_applied now counts an application to renew an expired ITIN), which this line does not read.

## Raw second transcription

```yaml
lines:
  - id: person.employers
    printed: "employers"
    label: "Number of employers"
    type: Count
    expr: {op: sum_over, collection: w2, field: one}
  - id: person.overcount
    printed: "overcount"
    label: "Number of employers that withheld more than the Social Security limit"
    type: Count
    expr: {op: sum_over, collection: w2, field: one, where: {op: test, eq: [w2.over, {const: true}]}}
  - id: person.over
    printed: "over"
    label: "Any employer withheld more than the Social Security limit"
    type: Bool
    expr: {op: test, gt: [person.overcount, {const: 0, type: Count}]}
  - id: person.wages
    printed: "wages"
    label: "Social Security wages and tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: wages}
  - id: person.withheld
    printed: "withheld"
    label: "Social Security tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: box4}
  - id: person.eligible
    printed: "eligible"
    label: "Eligible for the excess Social Security credit"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [person.employers, {const: 1, type: Count}]}, {op: test, gt: [person.wages, {param: ss.base}]}, {op: test, eq: [person.over, {const: false}]}]}
  - id: person.excess
    printed: "excess"
    label: "Excess Social Security tax"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.eligible, {const: true}]}, then: h_excess_raw}, {guard: {op: test, eq: [person.eligible, {const: false}]}, then: h_zero_money}]}
  - id: person.zero
    printed: "zero"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.credit
    printed: "credit"
    label: "Excess Social Security credit"
    type: NonNegDollars
    expr: {op: copy, from: person.excess}
  - id: person.sep_s1
    printed: "Step 1"
    label: "Net profit from Schedule C, Schedule F or Schedule K-1"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
  - id: person.sep_s2
    printed: "Step 2"
    label: "Deduction for self-employment tax"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line13}
  - id: person.sep_s3
    printed: "Step 3"
    label: "Net earnings from self-employment"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.sep_s1, take: person.sep_s2}
  - id: person.sep_s5
    printed: "Step 5"
    label: "Step 3 multiplied by the self-employed rate"
    type: NonNegDollars
    expr: {op: copy, from: person.sep_s3}
    note: "The reduced SEP rate table is not expressible with the available atoms; this reading uses net earnings as step 5."
  - id: person.sep_s6
    printed: "Step 6"
    label: "$350,000 multiplied by the plan contribution rate"
    type: NonNegDollars
    expr: {op: param, ref: ret.comp_limit}
    note: "Multiplying the $350,000 compensation limit by the plan rate is not expressible; this reading uses the compensation limit itself as step 6."
  - id: person.sep_s7
    printed: "Step 7"
    label: "Smaller of step 5 or step 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s5, person.sep_s6]}
  - id: person.sep_s8
    printed: "Step 8"
    label: "Contribution dollar limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.sep_dollar_limit}
  - id: person.sep_s21
    printed: "Step 21"
    label: "Maximum deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s7, person.sep_s8]}
  - id: person.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses for the American opportunity credit"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.edu_kid, {const: true}]}, then: h_edu_27_min}, {guard: {op: test, eq: [person.edu_kid, {const: false}]}, then: h_zero_money}]}
  - id: person.edu_line28
    printed: "28"
    label: "Line 27 less $2,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.edu_line27, take: {const: 200000}}
  - id: person.edu_line29
    printed: "29"
    label: "Line 28 multiplied by 25%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.edu_line28, rate: {param: aoc.second_rate}}
  - id: person.edu_line30
    printed: "30"
    label: "American opportunity credit before allocation"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.edu_line28, {const: 0}]}, then: person.edu_line27}, {guard: {op: test, ne: [person.edu_line28, {const: 0}]}, then: h_edu_line30_calc}]}
  - id: person.edu_line31
    printed: "31"
    label: "Adjusted qualified education expenses for the lifetime learning credit"
    type: NonNegDollars
    expr: {op: copy, from: h_edu_net}
  - id: person.one
    printed: "(helper)"
    label: "One person"
    type: Count
    expr: {op: param, ref: person.one}
  - id: person.educator_deduction
    printed: "(helper)"
    label: "Educator expenses deduction"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.eligible_educator, {const: true}]}, then: h_educator_min}, {guard: {op: test, eq: [person.eligible_educator, {const: false}]}, then: h_zero_money}]}
  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of HSA forms"
    type: Count
    expr: {op: sum_over, collection: f8889, field: one}
  - id: person.hsa_split
    printed: "(helper)"
    label: "Number of HSA forms with a split family limit"
    type: Count
    expr: {op: sum_over, collection: f8889, field: one, where: {op: test, eq: [f8889.split, {const: true}]}}
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "Number of HSA forms with an agreed allocation"
    type: Count
    expr: {op: sum_over, collection: f8889, field: one, where: {op: test, eq: [f8889.allocation, {const: "agreed"}]}}
  - id: person.hsa_step1
    printed: "(helper)"
    label: "Total HSA Step 1 family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: step1}
  - id: person.hsa_share
    printed: "(helper)"
    label: "Total HSA allocated share"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: share}
  - id: person.hsa_deduction
    printed: "(helper)"
    label: "Total HSA deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: line13}
  - id: person.hsa_taxable
    printed: "(helper)"
    label: "Total taxable HSA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: line16}
  - id: person.hsa_addtax
    printed: "(helper)"
    label: "Total additional 20% tax on HSA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: line17b}
  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers with qualified tips"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: one}
  - id: person.tip_total
    printed: "(helper)"
    label: "Total qualified tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: col_d}
  - id: person.tip_reported
    printed: "(helper)"
    label: "Qualified tips reported by employers"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: amount}
  - id: person.ot_employers
    printed: "(helper)"
    label: "Number of employers with qualified overtime"
    type: Count
    expr: {op: sum_over, collection: otjob, field: one}
  - id: person.ot_total
    printed: "(helper)"
    label: "Total qualified overtime"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: col_b}
  - id: person.box1
    printed: "(helper)"
    label: "Total Form W-2 box 1 wages"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: box1}
  - id: person.box2
    printed: "(helper)"
    label: "Total Form W-2 box 2 withholding"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: box2}
  - id: person.ira_amount_a
    printed: "(helper)"
    label: "Traditional IRA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: amount_a, where: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}}
  - id: person.ira_taxable
    printed: "(helper)"
    label: "Taxable traditional IRA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: ira_taxable}
  - id: person.ira_rollovers
    printed: "(helper)"
    label: "Number of IRA distributions with rollovers"
    type: Count
    expr: {op: sum_over, collection: retirement, field: one, where: {op: test, all: [{op: test, eq: [retirement.is_ira, {const: true}]}, {op: test, eq: [retirement.has_rollover, {const: true}]}]}}
  - id: person.plan_amount_a
    printed: "(helper)"
    label: "Plan distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: amount_a, where: {op: test, eq: [retirement.account, {const: "plan"}]}}
  - id: person.plan_taxable
    printed: "(helper)"
    label: "Taxable plan distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: plan_taxable}
  - id: person.plan_rollovers
    printed: "(helper)"
    label: "Number of plan distributions with rollovers"
    type: Count
    expr: {op: sum_over, collection: retirement, field: one, where: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.has_rollover, {const: true}]}]}}
  - id: person.sav_dist
    printed: "(helper)"
    label: "Retirement distributions for the saver's credit"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: sav_amount}
  - id: person.medicare5
    printed: "(helper)"
    label: "Total Medicare wages"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: box5}
  - id: person.medicare6
    printed: "(helper)"
    label: "Total Medicare tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: box6}
  - id: person.sc_count
    printed: "(helper)"
    label: "Number of Schedule C businesses"
    type: Count
    expr: {op: sum_over, collection: sc, field: one}
  - id: person.ho_count
    printed: "(helper)"
    label: "Number of Schedule C businesses with home office deductions"
    type: Count
    expr: {op: sum_over, collection: sc, field: one, where: {op: test, eq: [sc.ho_uses, {const: true}]}}
  - id: person.mq_q4
    printed: "(helper)"
    label: "Total mid-quarter fourth-quarter depreciation"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: mq_q4}
  - id: person.mq_total
    printed: "(helper)"
    label: "Total mid-quarter depreciation"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: mq_total}
  - id: person.cost179
    printed: "(helper)"
    label: "Total section 179 cost"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: cost179}
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "Section 179 deduction on nonlisted property"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: s179_allowed}
    note: "The child Schedule C fields do not split listed from nonlisted section 179; this reading puts the allowed section 179 amount in nonlisted property."
  - id: person.s179_listed
    printed: "(helper)"
    label: "Section 179 deduction on listed property"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "The child Schedule C fields do not split listed from nonlisted section 179; this reading puts listed property at zero."
  - id: person.income179
    printed: "(helper)"
    label: "Business income for the section 179 limitation"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: line31}
  - id: person.sc_total
    printed: "(helper)"
    label: "Total Schedule C net profit or loss"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: line31}
  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE line 6"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, ge: [h_se_4a, h_400]}, then: h_se_4a}, {guard: {op: test, lt: [h_se_4a, h_400]}, then: h_zero_money}]}
  - id: person.se_line12
    printed: "(helper)"
    label: "Schedule SE line 12 self-employment tax"
    type: NonNegDollars
    expr: {op: sum, of: [h_tax_ss, h_tax_med]}
  - id: person.se_line13
    printed: "(helper)"
    label: "Schedule SE line 13 deduction for one-half of self-employment tax"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line12, rate: {param: se.rate_50}}
  - id: person.s16
    printed: "(helper)"
    label: "SEP, SIMPLE and qualified plan deduction"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.plan, {const: "none"}]}, then: h_zero_money}, {guard: {op: test, eq: [person.plan, {const: "sep"}]}, then: h_sep_actual}, {guard: {op: test, eq: [person.plan, {const: "simple"}]}, then: h_simple_actual}]}
  - id: person.positive_profits
    printed: "(helper)"
    label: "Total positive net profits from businesses"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: line31, where: {op: test, gt: [sc.line31, {const: 0}]}}
  - id: person.sehi
    printed: "(helper)"
    label: "Self-employed health insurance deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: f7206_line14}
  - id: person.qbi
    printed: "(helper)"
    label: "Qualified business income deduction"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: qbi}
  - id: person.eic_se
    printed: "(helper)"
    label: "Self-employment earned income for the earned income credit"
    type: Dollars
    expr: {op: subtract, from: person.sc_total, take: person.se_line13}
  - id: person.sc_1a
    printed: "(helper)"
    label: "Number of Schedule C businesses for the earned income credit worksheet"
    type: Count
    expr: {op: copy, from: person.sc_count}
  - id: person.dc_benefits
    printed: "(helper)"
    label: "Dependent care benefits"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: dc_benefits}
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "Any dependent care benefits in Form W-2 box 10"
    type: Bool
    expr: {op: test, gt: [person.dc_benefits, {const: 0}]}
  - id: person.dc_earned
    printed: "(helper)"
    label: "Earned income for the child and dependent care credit"
    type: Dollars
    expr: {op: subtract, from: person.box1, take: {const: 0}}
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "Spouse's earned income for the child and dependent care credit"
    type: Dollars
    expr: {op: subtract, from: person.box1, take: {const: 0}}
  - id: person.sav_ineligible
    printed: "(helper)"
    label: "Ineligible for the saver's credit"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [person.sav_born, {const: false}]}, {op: test, eq: [person.sav_claimed, {const: true}]}, {op: test, eq: [person.sav_student, {const: true}]}]}
  - id: person.sav_line1
    printed: "(helper)"
    label: "Retirement savings contributions credit line 1"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_trad, person.sav_roth]}
  - id: person.sav_line2
    printed: "(helper)"
    label: "Retirement savings contributions credit line 2"
    type: NonNegDollars
    expr: {op: sum, of: [h_sav_deferral, person.sav_voluntary]}
  - id: person.ira_contrib
    printed: "(helper)"
    label: "Traditional IRA contributions"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_trad}
  - id: person.ira_cov
    printed: "(helper)"
    label: "Covered by a retirement plan at work"
    type: Bool
    expr: {op: copy, from: person.ira_work_plan}
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA deduction worksheet line 2"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.ira_cov, {const: true}]}, then: h_ira_line2_cov}, {guard: {op: test, eq: [person.ira_cov, {const: false}]}, then: h_ira_line2_nocov}]}
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA deduction worksheet line 6"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_line2, take: h_ira_line5}
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA deduction worksheet line 7"
    type: NonNegDollars
    expr: {op: larger_of, of: [h_ira_line7_round, h_ira_200]}
    note: "Uses the 70% rate and the $200 floor as a default; age and filing-status rate variants are not encoded."
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_ira_min1, person.ira_trad]}
    note: "Earned income for the line 10 limit is read from Form W-2 box 1; self-employment earned income is not added."
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "Nondeductible traditional IRA contributions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_trad, take: person.ira_deduction}
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Must file Form 8606"
    type: Bool
    expr: {op: test, gt: [person.ira_nondeductible, {const: 0}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2 total basis"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_basis}
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "Traditional IRA distribution or Roth conversion in 2025"
    type: Bool
    expr: {op: copy, from: person.ira_dist}
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14 total basis for 2025 and earlier years"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8606, field: line14}
  - id: person.ira_ssb
    printed: "(helper)"
    label: "IRA deduction used in the Social Security Benefits Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_deduction}
  - id: person.ira_se
    printed: "(helper)"
    label: "IRA deduction used in the self-employment calculation"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_deduction}
  - id: person.edu_kid
    printed: "(helper)"
    label: "Student qualifies for the American opportunity credit"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [person.edu_line23, {const: false}]}, {op: test, eq: [person.edu_line24, {const: true}]}, {op: test, eq: [person.edu_line25, {const: false}]}, {op: test, eq: [person.edu_line26, {const: false}]}, {op: test, eq: [person.edu_1098t, {const: true}]}, {op: test, eq: [person.edu_ein, {const: true}]}]}
  - id: person.x_l1
    printed: "(helper)"
    label: "Early distributions includible in income"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l1}
  - id: person.x_l2_all
    printed: "(helper)"
    label: "Total early distribution exceptions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l2}
  - id: person.x_l1_s
    printed: "(helper)"
    label: "SIMPLE IRA early distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l1_s}
  - id: person.x_l2_s
    printed: "(helper)"
    label: "SIMPLE IRA exceptions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l2_s}
  - id: person.x_tax
    printed: "(helper)"
    label: "Form 5329 additional tax on early distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: tax}
  - id: person.x_must
    printed: "(helper)"
    label: "Number of Forms 5329 that must be filed"
    type: Count
    expr: {op: sum_over, collection: f5329, field: one, where: {op: test, eq: [f5329.must, {const: true}]}}
  - id: person.x_c05
    printed: "(helper)"
    label: "Medical expense exception amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l2_e05}
  - id: person.x_two23
    printed: "(helper)"
    label: "More than one emergency personal expense exception"
    type: Bool
    expr: {op: test, gt: [h_e23_count, {const: 1, type: Count}]}
  - id: person.x_limited_sum
    printed: "(helper)"
    label: "Limited exception amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: l2}
  - id: person.x_other_exc
    printed: "(helper)"
    label: "Other exception amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.x_limit_binds
    printed: "(helper)"
    label: "An exception limit reduces the distribution"
    type: Bool
    expr: {op: test, gt: [person.x_limited_sum, {const: 0}]}
  - id: person.x_hsa_excess
    printed: "(helper)"
    label: "Additional tax on excess HSA contributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: l49}
  - id: h_zero_money
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: h_excess_raw
    printed: "(helper)"
    label: "Excess Social Security withholding before eligibility"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.withheld, take: {param: ss.limit}}
  - id: h_educator_max
    printed: "(helper)"
    label: "Educator expense limit"
    type: NonNegDollars
    expr: {op: param, ref: s1.educator_max}
  - id: h_educator_min
    printed: "(helper)"
    label: "Educator expenses limited by the maximum"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, h_educator_max]}
  - id: h_sav_deferral
    printed: "(helper)"
    label: "Elective deferrals for the saver's credit"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: sav_deferral}
  - id: h_ira_line2_cov
    printed: "(helper)"
    label: "IRA worksheet line 2 when covered"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}
  - id: h_ira_line2_nocov
    printed: "(helper)"
    label: "IRA worksheet line 2 when not covered"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}
  - id: h_ira_line5
    printed: "(helper)"
    label: "IRA worksheet line 5 modified AGI"
    type: Dollars
    expr: {op: copy, from: f1040.line11a}
  - id: h_ira_line7_raw
    printed: "(helper)"
    label: "IRA worksheet line 7 before rounding"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_70}}
  - id: h_ira_line7_round
    printed: "(helper)"
    label: "IRA worksheet line 7 rounded up to the next $10"
    type: NonNegDollars
    expr: {op: round, of: h_ira_line7_raw, unit: 1000, rule: up}
  - id: h_ira_200
    printed: "(helper)"
    label: "IRA worksheet $200 floor"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}
  - id: h_ira_line10_nn
    printed: "(helper)"
    label: "IRA worksheet line 10 earned income"
    type: NonNegDollars
    expr: {op: copy, from: person.box1}
  - id: h_ira_min1
    printed: "(helper)"
    label: "Smaller of IRA line 7 and line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.ira_line7, h_ira_line10_nn]}
  - id: h_edu_total
    printed: "(helper)"
    label: "Total qualified education expenses"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_inst, person.edu_mat]}
  - id: h_edu_adjust_sum
    printed: "(helper)"
    label: "Total reductions to qualified education expenses"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_a2025, person.edu_a2026, person.edu_refunds]}
  - id: h_edu_net
    printed: "(helper)"
    label: "Adjusted qualified education expenses"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: h_edu_total, take: h_edu_adjust_sum}
  - id: h_edu_cap
    printed: "(helper)"
    label: "American opportunity credit expense cap"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}
  - id: h_edu_27_min
    printed: "(helper)"
    label: "American opportunity credit expenses limited to the cap"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_edu_net, h_edu_cap]}
  - id: h_2000
    printed: "(helper)"
    label: "$2,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}
  - id: h_edu_line30_calc
    printed: "(helper)"
    label: "American opportunity credit when line 28 is positive"
    type: NonNegDollars
    expr: {op: sum, of: [h_2000, person.edu_line29]}
  - id: h_se_4a_pos
    printed: "(helper)"
    label: "Schedule SE line 4a when line 3 is positive"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.sc_total, rate: {param: se.rate_9235}}
  - id: h_se_4a
    printed: "(helper)"
    label: "Schedule SE line 4a"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, gt: [person.sc_total, {const: 0}]}, then: h_se_4a_pos}, {guard: {op: test, le: [person.sc_total, {const: 0}]}, then: h_zero_money}]}
  - id: h_400
    printed: "(helper)"
    label: "$400 self-employment floor"
    type: NonNegDollars
    expr: {op: param, ref: se.floor}
  - id: h_ss_wages
    printed: "(helper)"
    label: "Social Security wages and tips for Schedule SE line 8a"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: wages}
  - id: h_ss_room
    printed: "(helper)"
    label: "Social Security wage base remaining"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ss.base, take: h_ss_wages}
  - id: h_se_base
    printed: "(helper)"
    label: "Schedule SE line 10 base"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.se_line6, h_ss_room]}
  - id: h_tax_ss
    printed: "(helper)"
    label: "Social Security part of self-employment tax"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: h_se_base, rate: {param: se.rate_124}}
  - id: h_tax_med
    printed: "(helper)"
    label: "Medicare part of self-employment tax"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line6, rate: {param: se.rate_029}}
  - id: h_simple_actual
    printed: "(helper)"
    label: "Actual SIMPLE IRA contributions"
    type: NonNegDollars
    expr: {op: sum, of: [person.simple_deferral, person.simple_employer]}
  - id: h_sep_actual
    printed: "(helper)"
    label: "Actual SEP contribution limited to the maximum deductible amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_contrib, person.sep_s21]}
  - id: h_e23_count
    printed: "(helper)"
    label: "Number of emergency personal expense exception 23 distributions"
    type: Count
    expr: {op: sum_over, collection: retirement, field: one, where: {op: test, eq: [retirement.is_e23, {const: true}]}}
```
