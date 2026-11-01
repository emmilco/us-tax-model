# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9e8eff4434738020549ccc1510862ddb9843dfd49a96e037dff1a967d7682d55 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 148c998ab802660f4fb929e2693c43b95fb1812ea7c0b888218db2853534091f |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | bb9e07b4b43b889120c7d25885480f951bef306e8046a8c02e5ac43b619111b8 |
| printed lines compared | 99 |
| agree / disagree / missing | 29 / 70 / 0 |
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
- malformed expression (project schema): data/of/1 must be string, data/of/1 must be string, data/of/1 must be string
- person.h_educator_calc: malformed expression
- person.person.__type_gate_10: collection reference requires sum_over
- person.person.__type_gate_10: comparison operands have incompatible types
- person.person.__type_gate_11: collection reference requires sum_over
- person.person.__type_gate_11: comparison operands have incompatible types
- person.person.__type_gate_12: collection reference requires sum_over
- person.person.__type_gate_12: comparison operands have incompatible types
- person.person.__type_gate_13: collection reference requires sum_over
- person.person.__type_gate_13: comparison operands have incompatible types
- person.person.__type_gate_14: collection reference requires sum_over
- person.person.__type_gate_14: comparison operands have incompatible types

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
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}, "invalid_model_types": [{"line": "h_educator_calc", "message": "malformed expression (project schema): data/of/1 must be string, data/of/1 must be string, data/of/1 must be string"}, {"line": "h_educator_calc", "message": "person.h_educator_calc: malformed expression"}]}
```

Ruling: open

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

Ruling: open

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_step1", "message": "person.person.__type_gate_10: collection reference requires sum_over"}, {"line": "person.hsa_step1", "message": "person.person.__type_gate_10: comparison operands have incompatible types"}]}
```

Ruling: open

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "f8889.share", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_share", "message": "person.person.__type_gate_11: collection reference requires sum_over"}, {"line": "person.hsa_share", "message": "person.person.__type_gate_11: comparison operands have incompatible types"}]}
```

Ruling: open

### person.hsa_deduction — Form 8889 line 13 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line13", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "f8889.line13", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_deduction", "message": "person.person.__type_gate_12: collection reference requires sum_over"}, {"line": "person.hsa_deduction", "message": "person.person.__type_gate_12: comparison operands have incompatible types"}]}
```

Ruling: open

### person.hsa_taxable — Form 8889 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line16", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "f8889.line16", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_taxable", "message": "person.person.__type_gate_13: collection reference requires sum_over"}, {"line": "person.hsa_taxable", "message": "person.person.__type_gate_13: comparison operands have incompatible types"}]}
```

Ruling: open

### person.hsa_addtax — Form 8889 line 17b for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.line17b", "op": "sum_over", "where": null}
```

Second:

```json
{"expression": {"collection": "f8889", "field": "f8889.line17b", "op": "sum_over", "where": null}, "invalid_model_types": [{"line": "person.hsa_addtax", "message": "person.person.__type_gate_14: collection reference requires sum_over"}, {"line": "person.hsa_addtax", "message": "person.person.__type_gate_14: comparison operands have incompatible types"}]}
```

Ruling: open

### person.tip_employers — Number of employers that paid this person qualified tips
Status: **DISAGREE**

Project:

```json
{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "tipjob.qualified"}], "test": "eq"}}
```

Ruling: open

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
{"collection": "retirement", "field": "retirement.amount_a", "op": "sum_over", "where": {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}}
```

Ruling: open

### person.ira_taxable — Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.ira_taxable", "op": "sum_over", "where": {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}}
```

Ruling: open

### person.ira_rollovers — Number of this person's IRA distributions with a rollover
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}], "test": "all"}}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

### person.sav_dist — Distributions received in 2025 that Form 8880 line 4 counts, on this person's Forms 1099-R
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.sav_amount", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"input": "person.sav_prior_joint"}, {"input": "person.sav_prior_other"}], "op": "sum"}
```

Ruling: open

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
{"collection": "sc", "field": "sc.cost179_a", "op": "sum_over", "where": null}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "Step 21"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"line": "Step 3"}, {"of": [{"input": "person.simple_deferral"}, {"input": "person.simple_employer"}], "op": "sum"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: open

### person.positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: open

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

Ruling: open

### person.sc_1a — This person's Schedules C with Schedule 1-A tips or overtime
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.tips_ot"}], "test": "eq"}}
```

Second:

```json
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"ref": "sc.line1"}], "test": "lt"}}
```

Ruling: open

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

Ruling: open

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: open

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without t
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second transcription's note: The archived text does not provide a separate per-person figure for the exclusion computation; the same earned income is used.

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Second transcription's note: The archived text does not supply all line 5 modifications; Form 1040 line 11a is used as modified AGI.

Ruling: open

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}
```

Ruling: open

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Ruling: open

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}
```

Ruling: open

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "person.ira_basis"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}], "test": "lt"}], "test": "any"}
```

Ruling: open

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

Ruling: open

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

Ruling: open

### person.ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier ye
Status: **DISAGREE**

Project:

```json
{"collection": "f8606", "field": "f8606.line14", "op": "sum_over", "where": null}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_dist"}], "test": "eq"}, "then": {"of": [{"input": "person.ira_basis"}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, "then": {"from": {"of": [{"input": "person.ira_basis"}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}], "op": "smaller_of"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "sum"}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.ira_not_rolled", "op": "sum_over", "where": {"args": [{"const": "traditional_ira"}, {"ref": "retirement.account"}], "test": "eq"}}}}], "op": "choose"}
```

Ruling: open

### person.ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"ref": "ssb.line18"}
```

Ruling: open

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}
```

Ruling: open

### person.edu_kid — Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of yo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0}, {"ref": "f8863.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8863.line7"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": false}, {"input": "person.edu_over"}], "test": "eq"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}
```

Ruling: open

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

Ruling: open

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

Ruling: open

### person.x_l1_s — Line 1 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l3_s", "op": "sum_over", "where": null}
```

Ruling: open

### person.x_l2_s — Line 2 amounts from code S distributions
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f5329", "field": "f5329.l3_other", "op": "sum_over", "where": null}
```

Second transcription's note: The archived Form 5329 does not separately break out SIMPLE exception amounts; line 3 other is used as the closest supplied field.

Ruling: open

### person.x_tax — This person's Form 5329 taxes
Status: **AGREE**

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

Ruling: open

### person.x_two23 — Exception 23 claimed on more than one distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "f5329", "field": "f5329.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f5329.l48"}], "test": "lt"}], "test": "any"}}], "test": "lt"}
```

Ruling: open

### person.x_limited_sum — Exceptions 05, 09, 19, 22 and 23 within their limits
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Second:

```json
{"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}
```

Ruling: open

### person.x_other_exc — Exceptions without a fixed limit
Status: **DISAGREE**

Project:

```json
{"from": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}}
```

Second:

```json
{"from": {"collection": "f5329", "field": "f5329.l2", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}}
```

Ruling: open

### person.x_limit_binds — A limited exception over its limit on a person with a code S distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"collection": "f5329", "field": "f5329.l1", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}
```

Ruling: open

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

Ruling: open

### employers — Total w2.one for this person
Status: **AGREE**

### overcount — Number of employers that withheld more than the limit
Status: **AGREE**

### over — Any employer withheld more than the limit
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"line": "overcount"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"line": "overcount"}], "test": "eq"}, {"args": [{"const": false}, {"line": "rrta"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}
```

Ruling: open

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

Ruling: open

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
{"line": "over"}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

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
{"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 3, "whole": {"const": 10000}}
```

Ruling: open

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **DISAGREE**

Project:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"const": 10000}}
```

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "person.edu_over"}], "test": "eq"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "person.edu_over"}], "test": "ne"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: open

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

Ruling: open

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

Ruling: open

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

Ruling: open

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "person.edu_inst"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "person.edu_over"}], "test": "eq"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}], "test": "all"}, "then": {"line": "zero"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "person.edu_over"}], "test": "ne"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "llc.expense_cap"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| person.hsa_step1 | f8889.unsupported | f8889.unsupported |
| person.hsa_share | f8889.unsupported | f8889.unsupported |
| person.hsa_deduction | f8889.unsupported | - |
| person.hsa_taxable | f8889.unsupported | - |
| person.hsa_addtax | f8889.unsupported | - |
| person.s16 | person.plan_screen | person.plan_screen |
| person.sav_line1 | person.sav_able | - |
| person.ira_8606_line2 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.ira_8606_line14 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.x_l1 | person.x_other | person.x_other |
| person.x_l2_all | person.x_other | person.x_other |
| person.x_l1_s | person.x_other | person.x_other |
| person.x_l2_s | person.x_other | person.x_other |
| person.x_tax | person.x_other | - |
| person.x_must | person.x_other | person.x_other |
| person.x_c05 | person.x_other | person.x_other |
| person.x_two23 | person.x_other | person.x_other |
| person.x_limited_sum | person.x_other | person.x_other |
| person.x_other_exc | person.x_other | person.x_other |
| person.x_limit_binds | person.x_other | person.x_other |
| person.x_hsa_excess | person.x_other | person.x_other |
| over | person.rrta | person.rrta |
| eligible | person.rrta | person.rrta |
| excess | person.rrta | person.rrta |
| credit | person.rrta | - |
| Step 5 | person.plan_screen | person.plan_screen |
| Step 6 | person.plan_screen | person.plan_screen |
| Step 7 | person.plan_screen | person.plan_screen |
| Step 21 | person.plan_screen | person.plan_screen |
| 27 | person.edu_over | person.edu_over |
| 28 | person.edu_over | person.edu_over |
| 29 | person.edu_over | person.edu_over |
| 30 | person.edu_over | person.edu_over |
| 31 | person.edu_over | person.edu_over |

## Raw second transcription

```yaml
lines:
  - id: person.employers
    printed: "employers"
    label: "Number of employers reporting social security wages or tips for this person"
    type: Count
    expr: {op: copy, from: h_w2_count}
  - id: person.overcount
    printed: "overcount"
    label: "Number of Forms W-2 on which social security tax withheld is more than the social security tax limit"
    type: Count
    expr: {op: copy, from: h_w2_over_limit_count}
  - id: person.over
    printed: "over"
    label: "More than one employer, total social security wages and tips over the social security wage base, and no single employer over the limit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [person.employers, {const: 1, type: Count}]}
        - {op: test, gt: [person.wages, {param: ss.base}]}
        - {op: test, eq: [person.overcount, {const: 0, type: Count}]}
        - {op: test, eq: [person.rrta, {const: false}]}
    refuses: [person.rrta]
  - id: person.wages
    printed: "wages"
    label: "Total social security wages and social security tips from Forms W-2"
    type: NonNegDollars
    expr: {op: sum, of: [h_w2_box3, h_w2_box7]}
  - id: person.withheld
    printed: "withheld"
    label: "Total social security tax withheld from Forms W-2"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box4}
  - id: person.eligible
    printed: "eligible"
    label: "Eligible for the excess social security and tier 1 RRTA tax credit"
    type: Bool
    expr: {op: copy, from: person.over}
    refuses: [person.rrta]
  - id: person.excess
    printed: "excess"
    label: "Excess social security tax withheld over the social security tax limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.eligible, {const: true}]}
          then: h_excess_calc
        - guard: {op: test, eq: [person.eligible, {const: false}]}
          then: person.zero
    refuses: [person.rrta]
  - id: person.zero
    printed: "zero"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.credit
    printed: "credit"
    label: "Credit for excess social security and tier 1 RRTA tax withheld"
    type: NonNegDollars
    expr: {op: copy, from: person.excess}
    refuses: [person.rrta]
  - id: person.sep_s1
    printed: "Step 1"
    label: "Enter your net profit from Schedule C, line 31; Schedule F, line 34; or Schedule K-1, box 14, code A"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
  - id: person.sep_s2
    printed: "Step 2"
    label: "Enter your deduction for self-employment tax from Schedule 1, line 15"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line13}
  - id: person.sep_s3
    printed: "Step 3"
    label: "Net earnings from self-employment. Subtract step 2 from step 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.sep_s1, take: person.sep_s2}
  - id: person.sep_s5
    printed: "Step 5"
    label: "Multiply step 3 by step 4"
    type: NonNegDollars
    expr: {op: prorate, amount: person.sep_s3, part: h_sep_rate_cents, whole: {const: 10000}, places: 3}
    refuses: [person.plan_screen]
  - id: person.sep_s6
    printed: "Step 6"
    label: "Multiply $350,000 by your plan contribution rate (not the reduced rate)"
    type: NonNegDollars
    expr: {op: prorate, amount: h_comp_limit, part: h_sep_rate_cents, whole: {const: 10000}, places: 6}
    refuses: [person.plan_screen]
  - id: person.sep_s7
    printed: "Step 7"
    label: "Enter the smaller of step 5 or step 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s5, person.sep_s6]}
    refuses: [person.plan_screen]
  - id: person.sep_s8
    printed: "Step 8"
    label: "Contribution dollar limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.sep_dollar_limit}
  - id: person.sep_s21
    printed: "Step 21"
    label: "Subtract step 20 from step 19. This is your maximum deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s7, person.sep_s8]}
    refuses: [person.plan_screen]
    note: "Computed as the SEP worksheet maximum with no elective deferrals; SIMPLE contributions are represented in person.s16."
  - id: person.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses. Do not enter more than $4,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.edu_kid, {const: true}]}
          then: h_edu_adj_cap
        - guard: {op: test, eq: [person.edu_kid, {const: false}]}
          then: person.zero
    refuses: [person.edu_over]
  - id: person.edu_line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.edu_line27, take: {const: 200000}}
  - id: person.edu_line29
    printed: "29"
    label: "Multiply line 28 by 25%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.edu_line28, rate: {param: aoc.second_rate}}
  - id: person.edu_line30
    printed: "30"
    label: "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.edu_line28, {const: 0}]}
          then: person.edu_line27
        - guard: {op: test, ne: [person.edu_line28, {const: 0}]}
          then: h_edu_30_add
  - id: person.edu_line31
    printed: "31"
    label: "Adjusted qualified education expenses for the lifetime learning credit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.edu_kid, {const: true}]}
          then: person.zero
        - guard: {op: test, eq: [person.edu_kid, {const: false}]}
          then: h_edu_llc_adj
    refuses: [person.edu_over]
  - id: person.one
    printed: "(helper)"
    label: "One"
    type: Count
    expr: {op: param, ref: person.one}
  - id: person.educator_deduction
    printed: "(helper)"
    label: "Educator expense deduction for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.eligible_educator, {const: true}]}
          then: h_educator_calc
        - guard: {op: test, eq: [person.eligible_educator, {const: false}]}
          then: person.zero
  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of Forms 8889 for this person"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one}
  - id: person.hsa_split
    printed: "(helper)"
    label: "Number of Forms 8889 for this person requiring a spouse allocation"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.split, {const: true}]}}
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "Number of Forms 8889 for this person using an agreed allocation"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.allocation, {const: "agreed"}]}}
  - id: person.hsa_step1
    printed: "(helper)"
    label: "Family contribution limit allocation Step 1 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.step1}
    refuses: [f8889.unsupported]
  - id: person.hsa_share
    printed: "(helper)"
    label: "Share of the family contribution limit allocated to this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.share}
    refuses: [f8889.unsupported]
  - id: person.hsa_deduction
    printed: "(helper)"
    label: "HSA deduction for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line13}
    refuses: [f8889.unsupported]
  - id: person.hsa_taxable
    printed: "(helper)"
    label: "Taxable HSA distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line16}
    refuses: [f8889.unsupported]
  - id: person.hsa_addtax
    printed: "(helper)"
    label: "Additional 20% tax on taxable HSA distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line17b}
    refuses: [f8889.unsupported]
  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers with qualified tips for this person"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one, where: {op: test, eq: [tipjob.qualified, {const: true}]}}
  - id: person.tip_total
    printed: "(helper)"
    label: "Total qualified tips from more than one employer for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}
  - id: person.tip_reported
    printed: "(helper)"
    label: "Qualified tips reported for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.amount}
  - id: person.ot_employers
    printed: "(helper)"
    label: "Number of employers with qualified overtime compensation for this person"
    type: Count
    expr: {op: sum_over, collection: otjob, field: otjob.one}
  - id: person.ot_total
    printed: "(helper)"
    label: "Total qualified overtime compensation from more than one employer for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}
  - id: person.box1
    printed: "(helper)"
    label: "Total Form W-2 box 1 wages for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box1}
  - id: person.box2
    printed: "(helper)"
    label: "Total Form W-2 box 2 federal income tax withheld for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}
  - id: person.ira_amount_a
    printed: "(helper)"
    label: "Total traditional IRA distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.amount_a, where: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}}
  - id: person.ira_taxable
    printed: "(helper)"
    label: "Taxable traditional IRA distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.ira_taxable, where: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}}
  - id: person.ira_rollovers
    printed: "(helper)"
    label: "Number of traditional IRA distributions rolled over for this person"
    type: Count
    expr: {op: sum_over, collection: retirement, field: retirement.one, where: {op: test, all: [{op: test, eq: [retirement.account, {const: "traditional_ira"}]}, {op: test, eq: [retirement.has_rollover, {const: true}]}]}}
  - id: person.plan_amount_a
    printed: "(helper)"
    label: "Total plan distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.amount_a, where: {op: test, eq: [retirement.account, {const: "plan"}]}}
  - id: person.plan_taxable
    printed: "(helper)"
    label: "Taxable plan distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.plan_taxable, where: {op: test, eq: [retirement.account, {const: "plan"}]}}
  - id: person.plan_rollovers
    printed: "(helper)"
    label: "Number of plan distributions rolled over for this person"
    type: Count
    expr: {op: sum_over, collection: retirement, field: retirement.one, where: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.has_rollover, {const: true}]}]}}
  - id: person.sav_dist
    printed: "(helper)"
    label: "Distributions after 2022 and before the due date of the 2025 return used in the saver's credit for this person"
    type: NonNegDollars
    expr: {op: sum, of: [person.sav_prior_joint, person.sav_prior_other]}
  - id: person.medicare5
    printed: "(helper)"
    label: "Total Form W-2 box 5 Medicare wages and tips for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}
  - id: person.medicare6
    printed: "(helper)"
    label: "Total Form W-2 box 6 Medicare tax withheld for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}
  - id: person.sc_count
    printed: "(helper)"
    label: "Number of Schedule C businesses for this person"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one}
  - id: person.ho_count
    printed: "(helper)"
    label: "Number of Schedule C businesses with a home office deduction for this person"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, eq: [sc.ho_uses, {const: true}]}}
  - id: person.mq_q4
    printed: "(helper)"
    label: "Total mid-quarter fourth-quarter depreciation for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_q4}
  - id: person.mq_total
    printed: "(helper)"
    label: "Total mid-quarter depreciation for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_total}
  - id: person.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179}
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "Section 179 cost of property other than vehicles for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179_a}
  - id: person.s179_listed
    printed: "(helper)"
    label: "Section 179 cost of listed property for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179_v}
  - id: person.income179
    printed: "(helper)"
    label: "Business income for the section 179 limitation for this person"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
  - id: person.sc_total
    printed: "(helper)"
    label: "Total Schedule C net profit or loss for this person"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}
  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE line 6 for this person"
    type: NonNegDollars
    expr: {op: copy, from: h_se6}
  - id: person.se_line12
    printed: "(helper)"
    label: "Schedule SE line 12 self-employment tax for this person"
    type: NonNegDollars
    expr: {op: copy, from: h_se12}
  - id: person.se_line13
    printed: "(helper)"
    label: "Schedule SE line 13 deduction for one-half of self-employment tax for this person"
    type: NonNegDollars
    expr: {op: copy, from: h_se13}
  - id: person.s16
    printed: "(helper)"
    label: "Self-employed SEP, SIMPLE, and qualified plan deduction for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.plan, {const: "sep"}]}
          then: person.sep_s21
        - guard: {op: test, eq: [person.plan, {const: "simple"}]}
          then: h_simple_cap
        - guard: {op: test, eq: [person.plan, {const: "none"}]}
          then: person.zero
    refuses: [person.plan_screen]
  - id: person.positive_profits
    printed: "(helper)"
    label: "Positive net profit for this person for the optional methods"
    type: NonNegDollars
    expr: {op: copy, from: h_se3pos}
  - id: person.sehi
    printed: "(helper)"
    label: "Self-employed health insurance deduction for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.f7206_line14}
  - id: person.qbi
    printed: "(helper)"
    label: "Qualified business income from Schedule C businesses for this person"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.qbi}
  - id: person.eic_se
    printed: "(helper)"
    label: "Self-employment earned income for the earned income credit for this person"
    type: Dollars
    expr: {op: subtract, from: h_se3, take: person.se_line13}
  - id: person.sc_1a
    printed: "(helper)"
    label: "Number of Schedule C businesses with gross receipts for this person"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, gt: [sc.line1, {const: 0}]}}
  - id: person.dc_benefits
    printed: "(helper)"
    label: "Dependent care benefits from Forms W-2 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.dc_benefits}
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "Whether any Form W-2 for this person reports dependent care benefits in box 10"
    type: Bool
    expr: {op: test, gt: [h_dc_box10_count, {const: 0, type: Count}]}
  - id: person.dc_earned
    printed: "(helper)"
    label: "Earned income for the child and dependent care credit for this person"
    type: Dollars
    expr: {op: sum, of: [person.box1, person.ira_se]}
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "Earned income for the dependent care benefits exclusion for this person"
    type: Dollars
    expr: {op: copy, from: person.dc_earned}
    note: "The archived text does not provide a separate per-person figure for the exclusion computation; the same earned income is used."
  - id: person.sav_ineligible
    printed: "(helper)"
    label: "Whether this person is ineligible for the retirement savings contributions credit"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [person.sav_born, {const: false}]}
        - {op: test, eq: [person.sav_student, {const: true}]}
        - {op: test, eq: [person.sav_claimed, {const: true}]}
  - id: person.sav_line1
    printed: "(helper)"
    label: "Traditional and Roth IRA contributions for the saver's credit for this person"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_trad, person.sav_roth]}
    refuses: [person.sav_able]
  - id: person.sav_line2
    printed: "(helper)"
    label: "Elective deferrals and voluntary employee contributions for the saver's credit for this person"
    type: NonNegDollars
    expr: {op: sum, of: [h_sav_deferral, person.sav_voluntary]}
  - id: person.ira_contrib
    printed: "(helper)"
    label: "Traditional IRA contributions for this person"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_trad}
  - id: person.ira_cov
    printed: "(helper)"
    label: "Whether this person was covered by a retirement plan at work"
    type: Bool
    expr: {op: copy, from: person.ira_work_plan}
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA deduction worksheet line 2 for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_cov, {const: true}]}
          then: h_ira2_cov
        - guard: {op: test, eq: [person.ira_cov, {const: false}]}
          then: h_ira2_not
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA deduction worksheet line 6 for this person"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_line2, take: f1040.line11a}
    note: "The archived text does not supply all line 5 modifications; Form 1040 line 11a is used as modified AGI."
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA deduction worksheet line 7 for this person"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_ira7_min, h_ira_limit]}
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA deduction for this person"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_ira_ded1, person.ira_trad]}
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "Nondeductible traditional IRA contributions for this person"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_contrib, take: person.ira_deduction}
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Whether this person must file Form 8606"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [person.ira_nondeductible, {const: 0}]}
        - {op: test, all: [{op: test, gt: [person.ira_basis, {const: 0}]}, {op: test, eq: [person.ira_dist, {const: true}]}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2 total basis in traditional IRAs for this person"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_basis}
    refuses: [person.ira_basis_adjusted]
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "Whether this person took a traditional IRA distribution or made a Roth conversion"
    type: Bool
    expr: {op: copy, from: person.ira_dist}
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14 total basis in traditional IRAs for 2025 and earlier years"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_dist_gate, {const: true}]}
          then: h_ira_line14_calc
        - guard: {op: test, eq: [person.ira_dist_gate, {const: false}]}
          then: h_ira_line3
    refuses: [person.ira_basis_adjusted]
  - id: person.ira_ssb
    printed: "(helper)"
    label: "Taxable social security benefits used in the IRA modified AGI"
    type: NonNegDollars
    expr: {op: copy, from: ssb.line18}
  - id: person.ira_se
    printed: "(helper)"
    label: "Self-employment earned income for the IRA deduction worksheet for this person"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: h_se3, take: person.se_line13}
  - id: person.edu_kid
    printed: "(helper)"
    label: "Whether this student is eligible for the American opportunity credit"
    type: Bool
    expr: {op: copy, from: h_edu_aoc_ok}
  - id: person.x_l1
    printed: "(helper)"
    label: "Early distributions includible in income for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.l1}
    refuses: [person.x_other]
  - id: person.x_l2_all
    printed: "(helper)"
    label: "Early distributions not subject to the additional tax for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.l2}
    refuses: [person.x_other]
  - id: person.x_l1_s
    printed: "(helper)"
    label: "SIMPLE IRA early distributions includible in income for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.l3_s}
    refuses: [person.x_other]
  - id: person.x_l2_s
    printed: "(helper)"
    label: "SIMPLE IRA distributions not subject to the additional tax for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.l3_other}
    refuses: [person.x_other]
    note: "The archived Form 5329 does not separately break out SIMPLE exception amounts; line 3 other is used as the closest supplied field."
  - id: person.x_tax
    printed: "(helper)"
    label: "Additional tax on early distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.tax}
    refuses: [person.x_other]
  - id: person.x_must
    printed: "(helper)"
    label: "Number of Forms 5329 requiring this person's additional tax computation"
    type: Count
    expr: {op: sum_over, collection: f5329, field: f5329.one, where: {op: test, eq: [f5329.must, {const: true}]}}
    refuses: [person.x_other]
  - id: person.x_c05
    printed: "(helper)"
    label: "Amount of the medical expenses exception to the early distribution additional tax for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e05}
    refuses: [person.x_other]
  - id: person.x_two23
    printed: "(helper)"
    label: "Whether more than one Form 5329 applies to this person"
    type: Bool
    expr: {op: test, gt: [person.x_must, {const: 1, type: Count}]}
    refuses: [person.x_other]
  - id: person.x_limited_sum
    printed: "(helper)"
    label: "Total exception amounts from retirement distributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2}
    refuses: [person.x_other]
  - id: person.x_other_exc
    printed: "(helper)"
    label: "Exception amounts not reflected in the limited exception total for this person"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l2_all, take: person.x_limited_sum}
    refuses: [person.x_other]
  - id: person.x_limit_binds
    printed: "(helper)"
    label: "Whether the per-person exception limit binds for this person"
    type: Bool
    expr: {op: test, gt: [person.x_limited_sum, person.x_l1]}
    refuses: [person.x_other]
  - id: person.x_hsa_excess
    printed: "(helper)"
    label: "Excess HSA contributions for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f5329, field: f5329.l48}
    refuses: [person.x_other]
  - id: h_w2_count
    printed: "(helper)"
    label: "Count of Forms W-2"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
  - id: h_w2_over_limit_count
    printed: "(helper)"
    label: "Count of Forms W-2 with box 4 over the social security tax limit"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, gt: [w2.box4, {param: ss.limit}]}}
  - id: h_w2_box3
    printed: "(helper)"
    label: "Total Form W-2 box 3 social security wages"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box3}
  - id: h_w2_box7
    printed: "(helper)"
    label: "Total Form W-2 box 7 social security tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box7}
  - id: h_excess_calc
    printed: "(helper)"
    label: "Social security tax withheld over the limit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.withheld, take: {param: ss.limit}}
  - id: h_se3
    printed: "(helper)"
    label: "Schedule SE line 3 for this person"
    type: Dollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line3}}
  - id: h_se6
    printed: "(helper)"
    label: "Schedule SE line 6 for this person"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line6}}
  - id: h_se12
    printed: "(helper)"
    label: "Schedule SE line 12 for this person"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line12}}
  - id: h_se13
    printed: "(helper)"
    label: "Schedule SE line 13 for this person"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line13}}
  - id: h_se3pos
    printed: "(helper)"
    label: "Schedule SE positive net profit amount for this person"
    type: NonNegDollars
    expr: {op: copy, from: {def: se, bind: {line2: person.sc_total, line8a: person.wages}, line: line3pos}}
  - id: h_one_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: h_sep_rate_cents
    printed: "(helper)"
    label: "SEP plan contribution rate expressed in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: h_one_cent, count: person.sep_rate}
  - id: h_comp_limit
    printed: "(helper)"
    label: "Compensation limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.comp_limit}
  - id: h_simple_total
    printed: "(helper)"
    label: "Actual SIMPLE IRA contributions for this person"
    type: NonNegDollars
    expr: {op: sum, of: [person.simple_deferral, person.simple_employer]}
  - id: h_simple_cap
    printed: "(helper)"
    label: "SIMPLE IRA deduction limited by net earnings for this person"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_simple_total, person.sep_s3]}
  - id: h_dc_box10_count
    printed: "(helper)"
    label: "Count of Forms W-2 with box 10 dependent care benefits"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, eq: [w2.has_box10, {const: true}]}}
  - id: h_sav_deferral
    printed: "(helper)"
    label: "Total elective deferrals from Forms W-2 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.sav_deferral}
  - id: h_educator_calc
    printed: "(helper)"
    label: "Educator expenses limited to the maximum"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, {param: s1.educator_max}]}
  - id: h_ira2_cov
    printed: "(helper)"
    label: "IRA deduction worksheet line 2 amount when covered by a plan"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}
  - id: h_ira2_not
    printed: "(helper)"
    label: "IRA deduction worksheet line 2 amount when not covered by a plan"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}
  - id: h_ira7_70
    printed: "(helper)"
    label: "IRA phase-out at 70%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_70}}
  - id: h_ira7_80
    printed: "(helper)"
    label: "IRA phase-out at 80%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_80}}
  - id: h_ira7_35
    printed: "(helper)"
    label: "IRA phase-out at 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_35}}
  - id: h_ira7_40
    printed: "(helper)"
    label: "IRA phase-out at 40%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: {param: ira.rate_40}}
  - id: h_ira7_raw0
    printed: "(helper)"
    label: "IRA deduction worksheet line 7 before rounding and floor"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "mfs"}]}]}
              - {op: test, eq: [person.ira_age50, {const: false}]}
          then: h_ira7_70
        - guard:
            op: test
            all:
              - {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "mfs"}]}]}
              - {op: test, eq: [person.ira_age50, {const: true}]}
          then: h_ira7_80
        - guard:
            op: test
            all:
              - {op: test, any: [{op: test, eq: [f1040.status, {const: "mfj"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
              - {op: test, eq: [person.ira_age50, {const: false}]}
          then: h_ira7_35
        - guard:
            op: test
            all:
              - {op: test, any: [{op: test, eq: [f1040.status, {const: "mfj"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
              - {op: test, eq: [person.ira_age50, {const: true}]}
          then: h_ira7_40
  - id: h_ira7_round
    printed: "(helper)"
    label: "IRA deduction worksheet line 7 rounded up to the next $10"
    type: NonNegDollars
    expr: {op: round, of: h_ira7_raw0, unit: 1000, rule: up}
  - id: h_ira_min
    printed: "(helper)"
    label: "IRA deduction worksheet minimum $200"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}
  - id: h_ira7_min
    printed: "(helper)"
    label: "IRA deduction worksheet line 7 not less than $200"
    type: NonNegDollars
    expr: {op: larger_of, of: [h_ira7_round, h_ira_min]}
  - id: h_ira_limit_50
    printed: "(helper)"
    label: "IRA contribution limit when age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}
  - id: h_ira_limit_not
    printed: "(helper)"
    label: "IRA contribution limit when under age 50"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}
  - id: h_ira_limit
    printed: "(helper)"
    label: "IRA contribution limit for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.ira_age50, {const: true}]}
          then: h_ira_limit_50
        - guard: {op: test, eq: [person.ira_age50, {const: false}]}
          then: h_ira_limit_not
  - id: h_ira_line10
    printed: "(helper)"
    label: "IRA deduction worksheet line 10 earned income"
    type: NonNegDollars
    expr: {op: sum, of: [person.box1, person.ira_se]}
  - id: h_ira_ded1
    printed: "(helper)"
    label: "Smaller of IRA deduction worksheet line 7 and line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.ira_line7, h_ira_line10]}
  - id: h_ira_line3
    printed: "(helper)"
    label: "Form 8606 line 3 total basis before distributions"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_nondeductible, person.ira_8606_line2]}
  - id: h_ira_dist_amt
    printed: "(helper)"
    label: "Traditional IRA distributions not rolled over for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.ira_not_rolled, where: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}}
  - id: h_ira_line14_calc
    printed: "(helper)"
    label: "Form 8606 line 14 after distributions for this person"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: h_ira_line3, take: h_ira_dist_amt}
    note: "The archived text does not supply all Form 8606 ratio inputs; distributions are subtracted from basis as a simplified reading."
  - id: h_edu_adj_base
    printed: "(helper)"
    label: "Total qualified education expenses before reductions"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_inst, person.edu_mat]}
  - id: h_edu_adj_sum
    printed: "(helper)"
    label: "Total reductions to qualified education expenses"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_a2025, person.edu_a2026, person.edu_refunds]}
  - id: h_edu_adj
    printed: "(helper)"
    label: "Adjusted qualified education expenses"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: h_edu_adj_base, take: h_edu_adj_sum}
  - id: h_edu_aoc_ok
    printed: "(helper)"
    label: "American opportunity credit eligibility tests for this student"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.edu_line23, {const: false}]}
        - {op: test, eq: [person.edu_line24, {const: true}]}
        - {op: test, eq: [person.edu_line25, {const: false}]}
        - {op: test, eq: [person.edu_line26, {const: false}]}
        - {op: test, eq: [person.edu_ein, {const: true}]}
        - {op: test, eq: [person.edu_1098t, {const: true}]}
        - {op: test, eq: [person.edu_over, {const: false}]}
  - id: h_edu_cap27
    printed: "(helper)"
    label: "American opportunity credit expense cap"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}
  - id: h_edu_adj_cap
    printed: "(helper)"
    label: "Adjusted qualified education expenses capped at $4,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_edu_adj, h_edu_cap27]}
  - id: h_edu_28
    printed: "(helper)"
    label: "Line 28 amount before entering on Form 8863"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.edu_line27, take: {const: 200000}}
  - id: h_edu_29
    printed: "(helper)"
    label: "Line 29 amount before entering on Form 8863"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.edu_line28, rate: {param: aoc.second_rate}}
  - id: h_2000
    printed: "(helper)"
    label: "$2,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}
  - id: h_edu_30_add
    printed: "(helper)"
    label: "$2,000 plus line 29"
    type: NonNegDollars
    expr: {op: sum, of: [h_2000, person.edu_line29]}
  - id: h_edu_llc_cap
    printed: "(helper)"
    label: "Lifetime learning credit expense cap"
    type: NonNegDollars
    expr: {op: param, ref: llc.expense_cap}
  - id: h_edu_llc_adj
    printed: "(helper)"
    label: "Adjusted qualified education expenses capped for the lifetime learning credit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [h_edu_adj, h_edu_llc_cap]}
```
