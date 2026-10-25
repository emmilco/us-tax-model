# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 60328b0ad7993a970eb62ffa905b9b8a21b129ae5b8a7ac02632f9ae781f7266 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 581f806af1d6173b647f7819209ca510ff017e010e2aedeeda7f875a37e3fa56 |
| printed lines compared | 74 |
| agree / disagree / missing | 32 / 42 / 0 |
| extra printed lines in second | none |

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
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

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

Ruling: open

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

### person.hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

### person.hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}, {"args": [{"const": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"ref": "agreed"}, {"ref": "f8889.allocation"}], "test": "eq"}}
```

Ruling: open

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.step1", "op": "sum_over", "where": null}
```

Ruling: open

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.share", "op": "sum_over", "where": null}
```

Ruling: open

### person.hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

### person.hsa_taxable — Form 8889 line 16 for this person
Status: **AGREE**

### person.hsa_addtax — Form 8889 line 17b for this person
Status: **AGREE**

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
Status: **DISAGREE**

Project:

```json
{"collection": "tipjob", "field": "tipjob.amount", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "tipjob", "field": "tipjob.col_c", "op": "sum_over", "where": null}
```

Ruling: open

### person.ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

### person.ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

### person.box1 — Total W-2 box 1 for this person
Status: **AGREE**

### person.box2 — Total W-2 box 2 for this person
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
{"collection": "sc", "field": "sc.cost179_a", "op": "sum_over", "where": null}
```

Second transcription's note: The available Schedule C summary field cost179_a is read as the nonlisted-property total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface.

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

Second transcription's note: The available Schedule C summary field cost179_v is read as the listed-property (vehicle) total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface.

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
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}
```

Ruling: open

### person.se_line12 — Schedule SE line 12 (self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}
```

Ruling: open

### person.se_line13 — Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: open

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"input": "person.plan"}, {"ref": "sep"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"input": "person.plan"}, {"ref": "simple"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"input": "person.simple_age"}, {"ref": "under50"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"input": "person.simple_age"}, {"ref": "under50"}], "test": "ne"}, "then": {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}}], "op": "choose"}, {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"of": [{"input": "person.simple_employer"}, {"alternatives": [{"guard": {"args": [{"input": "person.simple_kind"}, {"ref": "match"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ret.match_rate"}}}, {"guard": {"args": [{"input": "person.simple_kind"}, {"ref": "nonelective"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "ret.nonelective_rate"}}}], "op": "choose"}], "op": "smaller_of"}], "op": "sum"}}], "op": "choose"}
```

Ruling: open

### person.positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **AGREE**

### person.sehi — Self-employed health insurance deduction, this person
Status: **AGREE**

### person.qbi — Qualified business income or loss of this person's businesses
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.qbi", "op": "sum_over", "where": null}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Ruling: open

### person.eic_se — Worksheet B, Parts 1 and 2, for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}
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
{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "sc.statutory"}], "test": "eq"}}
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
{"args": [{"const": 0}, {"collection": "w2", "field": "w2.dc_benefits", "op": "sum_over", "where": null}], "test": "lt"}
```

Ruling: open

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"param": "sales.zero"}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"param": "sales.zero"}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"param": "sales.zero"}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"param": "sales.zero"}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"param": "sales.zero"}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"param": "sales.zero"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: open

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without t
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second transcription's note: The supplied interface has one earned-income figure per person; this helper repeats it for the form's second earned-income column.

Ruling: open

### person.sav_ineligible — Born after January 1, 2008, claimed as a dependent on someone else's 2025 return, or a stu
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "person.sav_claimed"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.sav_student"}], "test": "eq"}, {"args": [{"param": "savers.agi_limit"}, {"ref": "f1040.line11a"}], "test": "lt"}, {"args": [{"const": true}, {"input": "person.sav_born"}], "test": "ne"}], "test": "any"}
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
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
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
{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}
```

Ruling: open

### person.ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Ruling: open

### person.ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract li
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}
```

Ruling: open

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}
```

Ruling: open

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Ruling: open

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}
```

Ruling: open

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "person.ira_basis"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_basis_adjusted"}], "test": "eq"}, {"args": [{"const": 0}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}], "test": "lt"}], "test": "any"}
```

Ruling: open

### person.ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}, "then": {"input": "person.ira_basis"}}], "op": "choose"}
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
{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}], "test": "all"}
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
{"of": [{"input": "person.ira_basis"}, {"from": {"input": "person.ira_trad"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "sum"}
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
{"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Second transcription's note: The archived text sends this figure to Pub. 590-A worksheets not included here; the line repeats the computed IRA deduction as the available reading.

Ruling: open

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "person.ira_trad"}, {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"of": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}, {"args": [{"input": "person.plan"}, {"ref": "none"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "f1040.line11a"}}, "op": "multiply_rate", "rate": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_70"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "hoh"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "mfs"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "single"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_80"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_35"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "f1040.status"}, {"ref": "mfj"}], "test": "eq"}, {"args": [{"ref": "f1040.status"}, {"ref": "qss"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.rate_40"}}], "op": "choose"}}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}, {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Second transcription's note: The archived text does not give a separate self-employment IRA figure beyond the deduction worksheet; the line repeats the computed IRA deduction.

Ruling: open

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
{"args": [{"args": [{"const": 1}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 1}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}, {"args": [{"const": true}, {"line": "over"}], "test": "ne"}], "test": "all"}
```

Ruling: open

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

Ruling: open

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"of": [{"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}, {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}}, {"guard": {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"param": "sales.zero"}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"param": "sales.zero"}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"param": "sales.zero"}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"param": "sales.zero"}}], "op": "choose"}, {"param": "sales.zero"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: open

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **DISAGREE**

Project:

```json
{"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}
```

Second:

```json
{"from": {"line": "Step 1"}, "op": "subtract", "take": {"line": "Step 2"}}
```

Ruling: open

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

Second transcription's note: Assumes no elective deferrals or catch-up contributions to the self-employed plan, because the closed input interface supplies none; only the skip-steps-9-through-20 branch is encoded.

Ruling: open

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **DISAGREE**

Project:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 3, "whole": {"param": "sc.hundred_cents"}}
```

Ruling: open

### Step 7 — Enter the smaller of step 5 or step 6
Status: **AGREE**

### Step 8 — Contribution dollar limit
Status: **AGREE**

### Step 21 — Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
Status: **AGREE**

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
| person.sav_ineligible | person.sav_able | person.sav_able |
| person.sav_line1 | person.sav_able | - |
| person.sav_line2 | person.sav_able | person.sav_able |
| person.ira_deduction | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.ira_nondeductible | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.ira_files_8606 | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.ira_8606_line2 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.ira_8606_line14 | person.ira_basis_adjusted, person.ira_dist, person.rrta, person.se_screen | person.ira_basis_adjusted, person.ira_dist, person.rrta, person.se_screen |
| person.ira_ssb | person.rrta, person.se_screen | person.rrta, person.se_screen |
| person.ira_se | person.rrta, person.se_screen | person.rrta, person.se_screen |
| credit | person.rrta | - |
| Step 1 | person.plan_screen | person.plan_screen |
| Step 2 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| Step 3 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| Step 5 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| Step 6 | person.plan_screen | person.plan_screen |
| Step 7 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |
| Step 8 | person.plan_screen | person.plan_screen |
| Step 21 | person.plan_screen, person.rrta, person.se_screen | person.plan_screen, person.rrta, person.se_screen |

## Raw second transcription

```yaml
lines:
  - id: person.employers
    printed: "employers"
    label: "Number of employers"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
  - id: person.overcount
    printed: "overcount"
    label: "Number of employers whose social security tax withheld exceeds the limit"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, eq: [w2.over, true]}}
  - id: person.over
    printed: "over"
    label: "Any one employer withheld more than the social security tax limit"
    type: Bool
    expr: {op: test, gt: [person.overcount, {const: 0}]}
  - id: person.wages
    printed: "wages"
    label: "Total social security wages and tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.wages}
  - id: person.withheld
    printed: "withheld"
    label: "Total social security tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box4}
  - id: person.eligible
    printed: "eligible"
    label: "Eligible for excess social security credit"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [person.employers, {const: 1}]}, {op: test, gt: [person.wages, {param: ss.base}]}, {op: test, not: {op: test, eq: [person.over, true]}}]}
  - id: person.excess
    printed: "excess"
    label: "Social security tax withheld in excess of the limit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.withheld, take: {param: ss.limit}}
  - id: person.zero
    printed: "zero"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.credit
    printed: "credit"
    label: "Excess social security credit"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.eligible, true]}, then: person.excess}, {guard: {op: test, eq: [person.eligible, false]}, then: person.zero}]}
    refuses: [person.rrta]
  - id: person.sep_s1
    printed: "Step 1"
    label: "Deduction worksheet for self-employed, step 1, net profit"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}
    refuses: [person.plan_screen]
  - id: person.sep_s2
    printed: "Step 2"
    label: "Deduction worksheet for self-employed, step 2, self-employment tax deduction"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line13}
    refuses: [person.plan_screen]
  - id: person.sep_s3
    printed: "Step 3"
    label: "Deduction worksheet for self-employed, step 3, net earnings from self-employment"
    type: NonNegDollars
    expr: {op: subtract, from: person.sep_s1, take: person.sep_s2}
    refuses: [person.plan_screen]
  - id: person.sep_s5
    printed: "Step 5"
    label: "Deduction worksheet for self-employed, step 5"
    type: NonNegDollars
    expr: {op: prorate, amount: person.sep_s3, part: person.sep_rate_c, whole: person.sep_rate_plus, places: 3}
    refuses: [person.plan_screen]
    note: "Assumes no elective deferrals or catch-up contributions to the self-employed plan, because the closed input interface supplies none; only the skip-steps-9-through-20 branch is encoded."
  - id: person.sep_s6
    printed: "Step 6"
    label: "Deduction worksheet for self-employed, step 6"
    type: NonNegDollars
    expr: {op: prorate, amount: {param: ret.comp_limit}, part: person.sep_rate_c, whole: person.hundred, places: 3}
    refuses: [person.plan_screen]
  - id: person.sep_s7
    printed: "Step 7"
    label: "Deduction worksheet for self-employed, step 7"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s5, person.sep_s6]}
    refuses: [person.plan_screen]
  - id: person.sep_s8
    printed: "Step 8"
    label: "Deduction worksheet for self-employed, step 8, contribution dollar limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.sep_dollar_limit}
    refuses: [person.plan_screen]
  - id: person.sep_s21
    printed: "Step 21"
    label: "Deduction worksheet for self-employed, step 21, maximum deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s7, person.sep_s8]}
    refuses: [person.plan_screen]
    note: "Assumes no designated Roth contributions or elective deferrals to the self-employed plan, because the closed input interface supplies none."
  - id: person.one
    printed: "(helper)"
    label: "Count of one"
    type: Count
    expr: {op: param, ref: ss.one}
  - id: person.educator_deduction
    printed: "(helper)"
    label: "Educator expense deduction"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.eligible_educator, true]}, then: person.educator_limited}, {guard: {op: test, eq: [person.eligible_educator, false]}, then: person.zero}]}
  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of HSA forms"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one}
  - id: person.hsa_split
    printed: "(helper)"
    label: "Number of HSA forms with a spousal split"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.split, true]}}
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "Number of HSA forms with an agreed allocation"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.allocation, "agreed"]}}
  - id: person.hsa_step1
    printed: "(helper)"
    label: "Total HSA Step 1 family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.step1}
  - id: person.hsa_share
    printed: "(helper)"
    label: "Total HSA allocated share"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.share}
  - id: person.hsa_deduction
    printed: "(helper)"
    label: "Total HSA deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line13}
  - id: person.hsa_taxable
    printed: "(helper)"
    label: "Total taxable HSA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line16}
  - id: person.hsa_addtax
    printed: "(helper)"
    label: "Total additional 20% HSA tax"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line17b}
  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers with qualified tips"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one, where: {op: test, eq: [tipjob.qualified, true]}}
  - id: person.tip_total
    printed: "(helper)"
    label: "Total qualified tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}
  - id: person.tip_reported
    printed: "(helper)"
    label: "Qualified tips reported on Form 4137"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_c}
  - id: person.ot_employers
    printed: "(helper)"
    label: "Number of employers with qualified overtime"
    type: Count
    expr: {op: sum_over, collection: otjob, field: otjob.one}
  - id: person.ot_total
    printed: "(helper)"
    label: "Total qualified overtime compensation"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}
  - id: person.box1
    printed: "(helper)"
    label: "Total Form W-2 box 1 wages"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box1}
  - id: person.box2
    printed: "(helper)"
    label: "Total Form W-2 box 2 withholding"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}
  - id: person.medicare5
    printed: "(helper)"
    label: "Total Form W-2 box 5 Medicare wages"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}
  - id: person.medicare6
    printed: "(helper)"
    label: "Total Form W-2 box 6 Medicare tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}
  - id: person.sc_count
    printed: "(helper)"
    label: "Number of Schedule C businesses"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one}
  - id: person.ho_count
    printed: "(helper)"
    label: "Number of Schedule C businesses with home office use"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, eq: [sc.ho_uses, true]}}
  - id: person.mq_q4
    printed: "(helper)"
    label: "Total mid-quarter fourth-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_q4}
  - id: person.mq_total
    printed: "(helper)"
    label: "Total mid-quarter depreciable basis"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_total}
  - id: person.cost179
    printed: "(helper)"
    label: "Total section 179 cost"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179}
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "Section 179 cost of nonlisted property"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179_a}
    note: "The available Schedule C summary field cost179_a is read as the nonlisted-property total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface."
  - id: person.s179_listed
    printed: "(helper)"
    label: "Section 179 cost of listed property"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179_v}
    note: "The available Schedule C summary field cost179_v is read as the listed-property (vehicle) total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface."
  - id: person.income179
    printed: "(helper)"
    label: "Income limitation for section 179"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}
  - id: person.sc_total
    printed: "(helper)"
    label: "Total Schedule C net profit or loss"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}
  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE line 6"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, ge: [person.se_line4c, {param: se.floor}]}, then: person.se_line6_ok}, {guard: {op: test, lt: [person.se_line4c, {param: se.floor}]}, then: person.se_line6_zero}]}
    refuses: [person.se_screen, person.rrta]
  - id: person.se_line12
    printed: "(helper)"
    label: "Schedule SE line 12, self-employment tax"
    type: NonNegDollars
    expr: {op: sum, of: [person.se_line10, person.se_line11]}
    refuses: [person.se_screen, person.rrta]
  - id: person.se_line13
    printed: "(helper)"
    label: "Schedule SE line 13, deduction for one-half of self-employment tax"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line12, rate: {param: se.rate_50}}
    refuses: [person.se_screen, person.rrta]
  - id: person.s16
    printed: "(helper)"
    label: "Schedule 1 line 16, self-employed SEP, SIMPLE, and qualified plans deduction"
    type: NonNegDollars
    expr: {op: copy, from: person.plan_deduction}
  - id: person.positive_profits
    printed: "(helper)"
    label: "Total positive Schedule C profits"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.profit_pos}
  - id: person.sehi
    printed: "(helper)"
    label: "Self-employed health insurance deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.f7206_line14}
  - id: person.qbi
    printed: "(helper)"
    label: "Qualified business income deduction"
    type: Dollars
    expr: {op: copy, from: qbi.deduction}
  - id: person.eic_se
    printed: "(helper)"
    label: "Self-employment earned income for the EIC"
    type: Dollars
    expr: {op: subtract, from: person.se_line3, take: person.se_line13}
  - id: person.sc_1a
    printed: "(helper)"
    label: "Number of statutory employee Schedule C businesses"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one, where: {op: test, eq: [sc.statutory, true]}}
  - id: person.dc_benefits
    printed: "(helper)"
    label: "Dependent care benefits"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.dc_benefits}
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "Any dependent care benefits in Form W-2 box 10"
    type: Bool
    expr: {op: test, gt: [person.dc_benefits, {const: 0}]}
  - id: person.dc_earned
    printed: "(helper)"
    label: "Earned income for dependent care"
    type: Dollars
    expr: {op: sum, of: [person.box1, person.eic_se]}
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "Earned income for dependent care, second column"
    type: Dollars
    expr: {op: copy, from: person.dc_earned}
    note: "The supplied interface has one earned-income figure per person; this helper repeats it for the form's second earned-income column."
  - id: person.sav_ineligible
    printed: "(helper)"
    label: "Ineligible for the saver's credit"
    type: Bool
    expr: {op: test, any: [{op: test, not: {op: test, eq: [person.sav_born, true]}}, {op: test, eq: [person.sav_claimed, true]}, {op: test, eq: [person.sav_student, true]}, {op: test, gt: [f1040.line11a, {param: savers.agi_limit}]}]}
    refuses: [person.sav_able]
  - id: person.sav_line1
    printed: "(helper)"
    label: "Form 8880 line 1"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_trad, person.sav_roth]}
    refuses: [person.sav_able]
  - id: person.sav_line2
    printed: "(helper)"
    label: "Form 8880 line 2"
    type: NonNegDollars
    expr: {op: sum, of: [person.sav_deferral_sum, person.sav_voluntary]}
    refuses: [person.sav_able]
  - id: person.ira_contrib
    printed: "(helper)"
    label: "Traditional IRA contributions for 2025"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_trad}
  - id: person.ira_cov
    printed: "(helper)"
    label: "Covered by a retirement plan"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [person.ira_work_plan, true]}, {op: test, eq: [person.ira_se_plan, true]}]}
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA deduction worksheet line 2"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.ira_cov, true]}, then: person.ira_line2_status}, {guard: {op: test, eq: [person.ira_cov, false]}, then: person.ira_line2_nc}]}
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA deduction worksheet line 6"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_line2, take: person.ira_line5}
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA deduction worksheet line 7"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.ira_cov, false]}, then: person.ira_limit}, {guard: {op: test, eq: [person.ira_cov, true]}, then: person.ira_line7_figured}]}
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA deduction"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_line12}
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "Nondeductible traditional IRA contributions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.ira_trad, take: person.ira_deduction}
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Must file Form 8606"
    type: Bool
    expr: {op: test, any: [{op: test, gt: [person.ira_nondeductible, {const: 0}]}, {op: test, all: [{op: test, eq: [person.ira_dist, true]}, {op: test, gt: [person.ira_basis, {const: 0}]}]}, {op: test, eq: [person.ira_basis_adjusted, true]}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2, total basis in traditional IRAs"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_basis}
    refuses: [person.ira_basis_adjusted]
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "Form 8606 Part I distribution gate"
    type: Bool
    expr: {op: copy, from: person.ira_dist}
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14, total basis in traditional IRAs for 2025 and earlier years"
    type: NonNegDollars
    expr: {op: sum, of: [person.ira_nondeductible, person.ira_8606_line2]}
    refuses: [person.ira_dist]
  - id: person.ira_ssb
    printed: "(helper)"
    label: "IRA deduction for the Social Security Benefits Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_deduction}
    note: "The archived text sends this figure to Pub. 590-A worksheets not included here; the line repeats the computed IRA deduction as the available reading."
  - id: person.ira_se
    printed: "(helper)"
    label: "IRA deduction for self-employment"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_deduction}
    note: "The archived text does not give a separate self-employment IRA figure beyond the deduction worksheet; the line repeats the computed IRA deduction."
  - id: person.cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: person.hundred
    printed: "(helper)"
    label: "One hundred cents"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: person.sep_rate_c
    printed: "(helper)"
    label: "SEP rate in cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: person.cent, count: person.sep_rate}
  - id: person.sep_rate_plus
    printed: "(helper)"
    label: "SEP rate plus one hundred cents"
    type: NonNegDollars
    expr: {op: sum, of: [person.sep_rate_c, person.hundred]}
  - id: person.educator_limited
    printed: "(helper)"
    label: "Educator expenses limited by the maximum"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, {param: s1.educator_max}]}
  - id: person.se_line3
    printed: "(helper)"
    label: "Schedule SE line 3"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
  - id: person.se_line4a_pos
    printed: "(helper)"
    label: "Schedule SE line 4a when line 3 is positive"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line3, rate: {param: se.rate_9235}}
  - id: person.se_line4a_neg
    printed: "(helper)"
    label: "Schedule SE line 4a when line 3 is zero or less"
    type: Dollars
    expr: {op: copy, from: person.se_line3}
  - id: person.se_line4a
    printed: "(helper)"
    label: "Schedule SE line 4a"
    type: Dollars
    expr: {op: choose, alternatives: [{guard: {op: test, gt: [person.se_line3, {const: 0}]}, then: person.se_line4a_pos}, {guard: {op: test, le: [person.se_line3, {const: 0}]}, then: person.se_line4a_neg}]}
  - id: person.se_line4c
    printed: "(helper)"
    label: "Schedule SE line 4c"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line4a}
  - id: person.se_line6_ok
    printed: "(helper)"
    label: "Schedule SE line 6 when the floor is met"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line4c}
  - id: person.se_line6_zero
    printed: "(helper)"
    label: "Schedule SE line 6 when the floor is not met"
    type: NonNegDollars
    expr: {op: copy, from: person.zero}
  - id: person.se_line7
    printed: "(helper)"
    label: "Schedule SE line 7"
    type: NonNegDollars
    expr: {op: param, ref: se.wage_base}
  - id: person.se_line8a
    printed: "(helper)"
    label: "Schedule SE line 8a"
    type: NonNegDollars
    expr: {op: copy, from: person.wages}
  - id: person.se_line8d
    printed: "(helper)"
    label: "Schedule SE line 8d"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line8a}
  - id: person.se_line9
    printed: "(helper)"
    label: "Schedule SE line 9"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.se_line7, take: person.se_line8d}
  - id: person.se_line10_base
    printed: "(helper)"
    label: "Smaller of Schedule SE line 6 or line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.se_line6, person.se_line9]}
  - id: person.se_line10
    printed: "(helper)"
    label: "Schedule SE line 10"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line10_base, rate: {param: se.rate_124}}
  - id: person.se_line11
    printed: "(helper)"
    label: "Schedule SE line 11"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line6, rate: {param: se.rate_029}}
  - id: person.ira_se_plan
    printed: "(helper)"
    label: "Covered by a self-employed retirement plan"
    type: Bool
    expr: {op: test, ne: [person.plan, "none"]}
  - id: person.ira_line2_status
    printed: "(helper)"
    label: "IRA worksheet line 2 for a covered person"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2}
  - id: person.ira_line2_nc
    printed: "(helper)"
    label: "IRA worksheet line 2 for a person not covered"
    type: NonNegDollars
    expr: {op: param, ref: ira.line2_not_covered}
  - id: person.ira_line5
    printed: "(helper)"
    label: "IRA worksheet line 5"
    type: Dollars
    expr: {op: copy, from: f1040.line11a}
  - id: person.ira_p70
    printed: "(helper)"
    label: "IRA percentage 70%"
    type: Rate
    expr: {op: param, ref: ira.rate_70}
  - id: person.ira_p80
    printed: "(helper)"
    label: "IRA percentage 80%"
    type: Rate
    expr: {op: param, ref: ira.rate_80}
  - id: person.ira_p35
    printed: "(helper)"
    label: "IRA percentage 35%"
    type: Rate
    expr: {op: param, ref: ira.rate_35}
  - id: person.ira_p40
    printed: "(helper)"
    label: "IRA percentage 40%"
    type: Rate
    expr: {op: param, ref: ira.rate_40}
  - id: person.status_single
    printed: "(helper)"
    label: "Filing status in the single, head of household, or married filing separately group"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [f1040.status, "single"]}, {op: test, eq: [f1040.status, "hoh"]}, {op: test, eq: [f1040.status, "mfs"]}]}
  - id: person.status_joint
    printed: "(helper)"
    label: "Filing status in the married filing jointly or qualifying surviving spouse group"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [f1040.status, "mfj"]}, {op: test, eq: [f1040.status, "qss"]}]}
  - id: person.ira_rate
    printed: "(helper)"
    label: "IRA worksheet line 7 percentage"
    type: Rate
    expr: {op: choose, alternatives: [{guard: {op: test, all: [{op: test, eq: [person.status_single, true]}, {op: test, eq: [person.ira_age50, false]}]}, then: person.ira_p70}, {guard: {op: test, all: [{op: test, eq: [person.status_single, true]}, {op: test, eq: [person.ira_age50, true]}]}, then: person.ira_p80}, {guard: {op: test, all: [{op: test, eq: [person.status_joint, true]}, {op: test, eq: [person.ira_age50, false]}]}, then: person.ira_p35}, {guard: {op: test, all: [{op: test, eq: [person.status_joint, true]}, {op: test, eq: [person.ira_age50, true]}]}, then: person.ira_p40}]}
  - id: person.ira_prod
    printed: "(helper)"
    label: "IRA worksheet line 7 product"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.ira_line6, rate: person.ira_rate}
  - id: person.ira_rounded
    printed: "(helper)"
    label: "IRA worksheet line 7 product rounded up to the next $10"
    type: NonNegDollars
    expr: {op: round, of: person.ira_prod, unit: 1000, rule: up}
  - id: person.ira_floor
    printed: "(helper)"
    label: "IRA worksheet line 7 with the $200 minimum"
    type: NonNegDollars
    expr: {op: larger_of, of: [person.ira_rounded, {param: ira.min}]}
  - id: person.ira_line7_figured
    printed: "(helper)"
    label: "IRA worksheet line 7 figured amount"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_floor}
  - id: person.ira_limit_under50
    printed: "(helper)"
    label: "IRA contribution limit under age 50"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}
  - id: person.ira_limit_over50
    printed: "(helper)"
    label: "IRA contribution limit age 50 or older"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}
  - id: person.ira_limit
    printed: "(helper)"
    label: "IRA contribution limit"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.ira_age50, true]}, then: person.ira_limit_over50}, {guard: {op: test, eq: [person.ira_age50, false]}, then: person.ira_limit_under50}]}
  - id: person.ira_line10
    printed: "(helper)"
    label: "IRA worksheet line 10, earned income"
    type: Dollars
    expr: {op: copy, from: person.dc_earned}
  - id: person.ira_own_total
    printed: "(helper)"
    label: "Smaller of IRA worksheet line 7 and line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.ira_line7, person.ira_line10]}
  - id: person.ira_line11
    printed: "(helper)"
    label: "IRA worksheet line 11, traditional IRA contributions"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_contrib}
  - id: person.ira_line12
    printed: "(helper)"
    label: "IRA worksheet line 12, most that can be deducted"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.ira_own_total, person.ira_line11]}
  - id: person.sep_deduction
    printed: "(helper)"
    label: "SEP deduction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_contrib, person.sep_s21]}
  - id: person.simple_comp
    printed: "(helper)"
    label: "SIMPLE plan compensation"
    type: NonNegDollars
    expr: {op: copy, from: person.se_line4c}
  - id: person.simple_cap
    printed: "(helper)"
    label: "SIMPLE salary reduction contribution limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.simple_limit}
  - id: person.simple_regular
    printed: "(helper)"
    label: "SIMPLE regular salary reduction contributions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.simple_deferral, person.simple_cap]}
  - id: person.catchup_raw
    printed: "(helper)"
    label: "SIMPLE salary reduction contributions above the regular limit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.simple_deferral, take: person.simple_regular}
  - id: person.simple_catchup
    printed: "(helper)"
    label: "SIMPLE catch-up contributions"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.simple_age, "under50"]}, then: person.zero}, {guard: {op: test, ne: [person.simple_age, "under50"]}, then: person.catchup_raw}]}
    note: "The 2025 SIMPLE catch-up dollar caps for age 50 and for ages 60 through 63 are stated in Pub. 560 but are not supplied as year parameters in this closed interface; the excess over the regular limit is not separately capped here."
  - id: person.rate3
    printed: "(helper)"
    label: "SIMPLE matching rate"
    type: Rate
    expr: {op: param, ref: ret.match_rate}
  - id: person.rate2
    printed: "(helper)"
    label: "SIMPLE nonelective rate"
    type: Rate
    expr: {op: param, ref: ret.nonelective_rate}
  - id: person.match_3pct
    printed: "(helper)"
    label: "SIMPLE matching contribution limit"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.simple_comp, rate: person.rate3}
  - id: person.ne_max
    printed: "(helper)"
    label: "SIMPLE nonelective contribution limit"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.simple_comp, rate: person.rate2}
  - id: person.employer_max
    printed: "(helper)"
    label: "SIMPLE employer contribution limit"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.simple_kind, "match"]}, then: person.match_3pct}, {guard: {op: test, eq: [person.simple_kind, "nonelective"]}, then: person.ne_max}]}
  - id: person.employer_actual_limited
    printed: "(helper)"
    label: "SIMPLE employer contributions allowed"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.simple_employer, person.employer_max]}
  - id: person.simple_deduction
    printed: "(helper)"
    label: "SIMPLE deduction"
    type: NonNegDollars
    expr: {op: sum, of: [person.simple_regular, person.simple_catchup, person.employer_actual_limited]}
  - id: person.plan_deduction
    printed: "(helper)"
    label: "Self-employed retirement plan deduction"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [person.plan, "sep"]}, then: person.sep_deduction}, {guard: {op: test, eq: [person.plan, "simple"]}, then: person.simple_deduction}, {guard: {op: test, eq: [person.plan, "none"]}, then: person.zero}]}
  - id: person.sav_deferral_sum
    printed: "(helper)"
    label: "Total elective deferrals from Forms W-2"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.sav_deferral}
```
