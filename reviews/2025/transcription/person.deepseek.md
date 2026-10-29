# Transcription agreement — person

Second transcription of `Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f2021d873ccea832bc1cd6813ffc7118e005061ec2ba74e1aea107cc516f31dd |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 669a0788eac2f9447979f13f411945b1db52d2e402fce2f8a0bf2abb30ad894d |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ebe28dcf736bff381f44e46fc56978601981c79e9abaeb44fbcd80d025cd38c6 |
| printed lines compared | 99 |
| agree / disagree / missing | 41 / 58 / 0 |
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
| i5329 | 2025 | 1, 3, 5, 8 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5, 8 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| p590b | 2025 | 27, 28 | cited pages | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 27, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| f1040s2 | 2025; created 2025-05-08 | 1, 2 | whole document | 29e3a05ca4dca4b5316833984170cff8815045c2e3957d048cb713ad90cb728f | - | 129b2541cce9743c9bde3a48fdfcc2512767d88b7cbbbe562d7989b117232d62 |
| f5329 | 2025 | 1, 2, 3 | whole document | 53ac10ecce39dbd1cc0a3b88c04e351c2a61f3ad35d145d5d847f30f47a1b945 | - | c65e0cd9d9ad8e8a04899ec87a11393ad5a3e281543eb6720b72357811f8f51d |
| i4562 | 2025 | 4, 11 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 11 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |
| p503 | For use in preparing 2025 returns | 11 | pages named by another document's citation | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 11 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant
- malformed expression (project schema): data/of/1 must be string, data/of/1 must be string, data/of/1 must be string
- malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object
- person.person.se_line6: malformed expression
- person.person.se_line12: malformed expression
- person.person.h_sep_10000: malformed expression
- person.person.h_educator_cap: malformed expression
- person.person.h_se_line4a: malformed expression

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
{"expression": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.h_educator_cap", "message": "malformed expression (project schema): data/of/1 must be string, data/of/1 must be string, data/of/1 must be string"}, {"line": "person.h_educator_cap", "message": "person.person.h_educator_cap: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_educator_cap (malformed: its smaller_of operand is an inline param object where an id is required), so no value of it was computed. By reading: i1040gi p. 93, Line 11: "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025." The reply's intent is the project's formula (the smaller of the expenses and $300 for an eligible educator, zero otherwise), as rounds 1 to 3.

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"ref": "f8889.line2"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8889.line9"}], "test": "lt"}], "test": "any"}}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8889 p. 4, Name and social security number (SSN): "complete a separate Form 8889 for each of you"; i8889 p. 1, Who Must File: "You must file Form 8889 if any of the following applies. • You, your employer, or someone else made contributions to your HSA. • Your HSA made a distribution." The line counts the Forms 8889 entered for the person (its label, read by person.hsa_repeated and household.hsa_people); the reply counts only forms with contributions (f8889.any), so a Form 8889 entered for distributions only is not counted: a second form for the same person escapes the person.hsa_repeated refusal, and a spouse with only a distribution form is not counted as a person with a Form 8889 for the line 6 spouse rule.

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

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8889 p. 7, Line 6, Step 2: "Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation". Same expression as round 2 and as the Claude reply: forms with f8889.allocation agreed without the spouse-rule filter; the allocation is asked only within the spouse rule and household.hsa_agreed_count is read only on split forms (ruled representation in the Claude log on classm.f8889.1, completed). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

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

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8889 p. 7, Line 6, Step 2. The reply dropped round 2's invalid refusal declaration (refuses f8889.unsupported at the person level); the expression is now the Claude reply's sum of f8889.step1 over all of the person's forms, ruled representation in that log (the filtered and unfiltered sums are equal on every split form, the only place household.hsa_step1_sum is read; non-split values such as classm.s3.3.deepseek $0.00 against $712.50 reach no amount). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

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

Ruling: interface gap; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8889 p. 7, Line 6, Step 3: "Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1." The reply dropped round 2's invalid refusal declaration; it sums f8889.share, the published field carrying the f8889.allocation_bad refusal whose test reads household.hsa_share_sum, which sums this line: a cycle. The interface gave f8889.share_raw and f8889.share by id and type only, so the candidate could not tell the pre-check amount from the checked one; the Claude reply's identical line is ruled interface gap in that log (classm.f8889.1 and .1.deepseek). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

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
Status: **AGREE**

### person.ira_taxable — Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
Status: **DISAGREE**

Project:

```json
{"collection": "retirement", "field": "retirement.taxable", "op": "sum_over", "where": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.ira_taxable", "op": "sum_over", "where": null}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 26, Lines 4a and 4b, IRA Distributions: "You should receive a Form 1099-R showing the total amount of any distribution from your IRA". The line is the taxable amount of the person's IRA distributions (Form 1040 line 4b, decision D1). The reply sums retirement.ira_taxable over every Form 1099-R with no IRA filter; that helper is box 1 less the amount rolled over for any entry whose account is not a Roth IRA, so a pension entry adds its amount to line 4b as well as to line 5b. By reading on stage21.blind.e4 (three IRA entries $7,000.00, $4,500.00 and $4,000.00 and a plan entry $3,500.00): project $15,500.00, candidate $19,000.00; on stage21.blind.e1: project $5,123.45, candidate $7,580.23.

### person.ira_rollovers — Number of this person's IRA distributions with a rollover
Status: **AGREE**

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

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities: "You should receive a Form 1099-R showing the total amount of your pension and annuity payments". The same sum of retirement.amount_a over the person's plan entries as the project (decision D1); only the operand order of the account test differs (the Claude reply's equivalent line agrees on all 4,917 comparisons).

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

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities. The reply sums retirement.plan_taxable over the person's plan entries; for a plan entry retirement.taxable is retirement.plan_taxable (its is_ira branch is false), so the sum is the project's (decision D1).

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

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi pp. 28-29, Lines 5a and 5b, rollovers. The reply counts plan entries with retirement.has_rollover, the published helper whose definition (code G, or a rollover amount above zero) the project's expression spells out; the same count (the Claude reply's equivalent line agrees on all 4,917 comparisons).

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

Ruling: interface gap; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i4562 p. 5, Line 6, column (c), Elected cost, and Line 7 (listed property, from line 29). The reply changed: it now sums sc.s179_elected (lines 6 and 29 together) where round 3 read the line 12 deduction (circular), the expression of the Claude reply ruled interface gap in that log (classm.eic.3, completed: project $0.00, candidate $10,918.00). The pages given (i4562 pp. 4 and 11) omit the p. 5 instructions that split the listed election onto line 7, and sc.f6 and sc.f29 were published by id and type only.

### person.s179_listed — Section 179 elected on listed property, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.f29", "op": "sum_over", "where": null}
```

Second:

```json
{"line": "zero"}
```

Second transcription's note: The supplied Schedule C interface does not expose a person-level split of elected section 179 cost between listed and nonlisted property; this line reports zero and the total elected cost is carried on person.s179_nonlisted.

Ruling: interface gap; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i4562 p. 5, Line 7: "Enter the amount that you elected to expense for listed property (defined earlier) on line 29 here." The reply enters zero (its note: listed property is outside the supplied interface). The pages given (i4562 pp. 4 and 11) omit the p. 5 line 7 instruction and sc.f29 was published by id and type only, so the candidate could not place the listed election; the Claude reply made the same choice and is ruled interface gap in that log (classm.eic.3, completed: project $10,918.00, candidate $0.00). In this reply line 6 also lacks the listed amount (it reads line 12; ruled at person.s179_nonlisted). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

### person.income179 — Business net profit or loss without section 179, this person
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.line31_pre179", "op": "sum_over", "where": null}
```

Second:

```json
{"collection": "sc", "field": "sc.line29", "op": "sum_over", "where": {"args": [{"const": 0}, {"ref": "sc.line29"}], "test": "lt"}}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i4562 p. 5, Line 11: the business income limit is "the total taxable income from any trade or business you actively conducted, computed without regard to any section 179 expense deduction, the deduction for one-half of self-employment taxes under section 164(f), or any net operating loss deduction." The reply changed: it sums Schedule C line 29 (tentative profit) over the businesses with a profit. That drops the losses of other businesses, which the aggregate taxable income nets, and the home-office deduction (line 30) that line 31 subtracts; the project's sc.line31_pre179 is line 31 before section 179. The p. 5 text was not among the pages given, but the published sc.line31_pre179 label states the amount.

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

Ruling: scope; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040sc p. 15, Line 32, Some investment is not at risk: "Be sure to attach Form 6198". The candidate sums sc.line31, the project sc.result, which differs only for a loss with amounts not at risk, refused at sc.loss_allowed; the Claude reply's identical expression differs only by that cited refusal (stage14.refuse.at_risk). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

### person.se_line6 — Schedule SE line 6 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches its own malformed expression and person.h_se_line4a (a choose whose guard is not an object), so no value of it was computed. By reading: i1040sse p. 1, line 4c: "Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax." The intended line 6 is line 4c (line 4a, 92.35% of line 3) for a Schedule C person; it still declares the se_screen refusal for every person (an answer the interview asks only with a Schedule C; scope on that kind, as in the Claude log).

### person.se_line12 — Schedule SE line 12 (self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches its own malformed expression and person.h_se_line4a, so no value of it was computed. By reading: i1040sse p. 1, line 12: "Self-employment tax. Add lines 10 and 11." The intended lines 8 to 12 (the wage base less person.wages, 12.4% and 2.9%) follow the source as in round 3; the se_screen placement is scope, as in the Claude log.

### person.se_line13 — Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.se_line12 and person.h_se_line4a, both malformed, so no value of it was computed. By reading: i1040sse line 13: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)." Half of its line 12, the source's formula.

### person.s16 — Schedule 1 line 16 for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "Step 21"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_sep_10000 (malformed: a count operand that is not an id) and the Schedule SE lines through Step 21 and its SIMPLE helpers, so no value of it was computed. By reading: p560 p. 39, after Step 21: "Enter your actual contribution, not to exceed your maximum deductible contribution, on Schedule 1 (Form 1040), line 16". The intended SEP part is the smaller of the contribution and Step 21 (the project deducts the contribution and refuses an excess at person.sep_excess, scope); the SIMPLE part is as round 3 (an over-limit SIMPLE the project refuses at person.simple_excess, p560 p. 17: scope on that kind).

### person.positive_profits — Total of all net profits of this person's businesses (losses not included)
Status: **DISAGREE**

Project:

```json
{"collection": "sc", "field": "sc.profit_pos", "op": "sum_over", "where": null}
```

Second:

```json
{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": {"args": [{"const": 0}, {"ref": "sc.line31"}], "test": "lt"}}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. Form 7206 (2025), line 5: "Enter the total of all net profits* from Schedule C (Form 1040), line 31" (the project's cite). The reply sums Schedule C line 31 over the businesses with a profit and floors the total at zero; the project sums sc.profit_pos (each business's result floored at zero). The same amount, except that sc.result and line 31 differ for a loss not at risk, which is excluded by both filters (a loss) and refused at sc.loss_allowed.

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
{"expression": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches the malformed person.h_se_line4a (Schedule SE line 4a) through its Schedule SE lines, so no value of it was computed. By reading: i1040gi EIC Worksheet B, Part 1 (Schedule SE line 3 less line 13) and Part 2 (Schedule C line 31 when you do not file Schedule SE). The intended reading is the project's (line 3 less line 13, which equals Schedule C line 31 where no Schedule SE is required).

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 104, Schedule 1-A Line 5: "Include the qualified tips you and/or your spouse received in the course of a trade or business". The line counts this person's Schedules C with Schedule 1-A tips or overtime (sc.tips_ot, published); the reply counts Schedules C with sc.statutory true (the statutory-employee screen), the wrong field, as in round 1 (round 2 counted gross receipts). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i2441 p. 5, Line 12: "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2." The reply changed: it tests person.dc_benefits (box 10 less the part reported as wages in box 1, w2.dc_net) above zero where the line tests the box 10 total above zero (person.dc_box10); a person whose box 10 amount is all reported in box 1 has box 10 benefits but is not counted, which changes f2441.box10_persons, the count the line 1e attribution reads (amb.2025.dc_line1e_attribution).

### person.dc_earned — This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's shar
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f1040.line1e"}], "test": "lt"}], "test": "all"}, "then": {"ref": "f1040.line1e"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}, {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "w2", "field": "w2.box10", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"ref": "f1040.line1e"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches the malformed person.h_se_line4a (Schedule SE line 4a) through its Schedule SE lines (person.eic_se), so no value of it was computed. By reading: i2441 p. 4: "Earned income for figuring the credit generally includes the following amounts. 1. The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z", and line 1z includes line 1e, taxable dependent care benefits. As rounds 1 to 3, the reply adds W-2 box 1 and the self-employment amount without the line 1e term (the Claude reply's same omission executes as classm.carloan.1, $238,056.00 against $234,528.00).

### person.dc_earned_b — This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without t
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"expression": {"from": {"of": [{"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract", "take": {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}, {"collection": "w2", "field": "w2.box1", "op": "sum_over", "where": null}], "op": "sum"}, "op": "subtract", "take": {"collection": "w2", "field": "w2.dc_benefits", "op": "sum_over", "where": null}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches the malformed person.h_se_line4a (Schedule SE line 4a) through its Schedule SE lines (person.dc_earned), so no value of it was computed. By reading: i2441 p. 5, Line 18: earned income for Part III is figured as for lines 4 and 5. The intended reading is the project's (a copy of its lines 4 and 5 amount), as round 3.

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

Ruling: ambiguity; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. amb.2025.savers_ineligible_column (owner decision). f8880 p. 2, Who Can Take This Credit: "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else's 2025 tax return; or (c) was a student." Same expression as round 2 and as the Claude reply (ruled ambiguity there: sav_claimed supplied with sa.dependent false, classm.f5695.2 and .2.deepseek). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged.

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

Ruling: scope; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f8880 line 1: "Traditional and Roth IRA contributions, and ABLE account contributions by the designated beneficiary, for 2025". The reply changed: person.ira_trad plus person.sav_roth, without the project's sav_trad gate (person.ira_contrib is zero after a No); the amount is the same wherever ira_trad is asked, and the ABLE refusal (person.sav_able) is the project's cited screen. The project refuses excess contributions at person.ira_excess_gate (p590a p. 35; stage16.refuse.person.ira_excess in the Claude log).

### person.sav_line2 — Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "person.sav_voluntary"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.simple_deferral"}}], "op": "choose"}}], "op": "choose"}, {"collection": "w2", "field": "w2.sav_deferral", "op": "sum_over", "where": null}], "op": "sum"}
```

Second:

```json
{"of": [{"input": "person.sav_voluntary"}, {"collection": "w2", "field": "w2.sav_listed", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f8880 p. 2, Line 2: "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP". The reply changed its W-2 field (w2.sav_listed for w2.sav_deferral) but still omits the person's own SIMPLE salary reduction contributions as a self-employed person (person.sav_simple), which line 2 names; the Claude reply's round-3 omission executed as stage14.simple.match_age50, $18,000.00 against $0.00 (completed). It dropped the sav_able refusal; its sav_excess refusal without box 12 deferrals is scope, as in the Claude log.

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

Ruling: scope; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 98, line 11: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return ... for 2025". As round 3: person.ira_trad for everyone, now with the person.ira_excess refusal declared; the project asks the amount after a Yes to person.sav_trad and refuses excess contributions at person.ira_excess_gate (p590a p. 35), as ruled on the Claude reply's same line.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 96, Were You Covered by a Retirement Plan?: "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan." As rounds 1 to 3: person.ira_work_plan alone, dropping the person's own SEP or SIMPLE plan (amb.2025.ira_covered); it now also declares an ira_excess refusal for every person, an answer the interview asks only with contributions.

### person.ira_line2 — Worksheet line 2 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "spouse"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line2b"}}, {"guard": {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line2a"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 97, line 2: "Married filing jointly, enter $146,000 in both columns. But if you checked "No" on either line 1a or 1b, enter $246,000 for the person who wasn't covered by a plan." The reply changed: it copies the return-level column the project builds from this line (ira.line2a and ira.line2b sum person.ira_line2 by role), so the line is defined by itself: a cycle with no worksheet figure.

### person.ira_line6 — Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract li
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "spouse"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line6b"}}, {"guard": {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line6a"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 97, line 6: "Is the amount on line 5 less than the amount on line 2? ... Yes. Subtract line 5 from line 2 in each column." As round 1, the reply copies the return-level column the project builds from this line (ira.line6a and ira.line6b sum person.ira_line6 by role), so the line is defined by itself: a cycle with no worksheet figure.

### person.ira_line7 — Worksheet line 7 for this person's column
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "spouse"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line7b"}}, {"guard": {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line7a"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi pp. 97-98, line 7: multiply line 6 by the percentage that applies, increase to the next multiple of $10 and enter at least $200, or the applicable amount when no one is covered. The reply copies the return-level column the project builds from this line (ira.line7a and ira.line7b sum person.ira_line7 by role), so the line is defined by itself: a cycle with no worksheet figure.

### person.ira_deduction — This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "spouse"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line12b"}}, {"guard": {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line12a"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 98: "On line 12a, enter the smallest of line 7a, 10, or 11a ... This is the most you can deduct." The reply copies ira.line12a or ira.line12b, which sum person.ira_deduction by role: a cycle with no deduction figured, as round 1.

### person.ira_nondeductible — This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}
```

Second:

```json
{"collection": "f8606", "field": "f8606.line1", "op": "sum_over", "where": null}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8606 p. 9, Line 1: subtract worksheet line 12 "from the smaller of line 10 or line 11 of the worksheet". The reply changed: it sums f8606.line1 over the person's Forms 8606, and f8606.line1 copies person.ira_nondeductible, so the line is defined by itself (a cycle with no amount).

### person.ira_files_8606 — This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "person.ira_dist"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "f8606", "field": "f8606.line1", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "f8606", "field": "f8606.line2", "op": "sum_over", "where": null}], "test": "lt"}], "test": "any"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8606 p. 2, Who Must File: "You made nondeductible contributions to a traditional IRA for 2025". The reply tests its nondeductible amount, its Form 8606 line 2 and its distribution gate; the first two are circular (ruled at person.ira_nondeductible and person.ira_8606_line2), and a basis or distribution alone makes it true for a person with no nondeductible contribution, a Form 8606 Part I the project's line does not serve (a distribution with basis is screened by retirement.special).

### person.ira_8606_line2 — Form 8606 line 2 for this person (asked only when the person files Form 8606)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}], "test": "lt"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"amount": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, "then": {"param": "ira.line2_not_covered"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"param": "ira.line2"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"ref": "ira.line5"}}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}}], "op": "choose"}], "test": "lt"}, "then": {"input": "person.ira_basis"}}], "op": "choose"}
```

Second:

```json
{"collection": "f8606", "field": "f8606.line2", "op": "sum_over", "where": null}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8606 p. 9, Line 2: "Generally, if this is the first year you are required to file Form 8606, enter -0-" and otherwise the Total Basis Chart amount. As round 3: it sums f8606.line2, which copies person.ira_8606_line2, a cycle with no base amount (now with the ira_basis_adjusted refusal the project also makes at person.ira_basis_gate); the published person.ira_basis was not used.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f8606 (2025) Part I: "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?", asked of a person filing Form 8606 for nondeductible contributions. The reply changed: it copies person.ira_dist alone, so any person with a 2025 traditional IRA distribution trips the gate, which the project's Form 8606 lines read as a refusal (f8606.dist); the project's line also requires a Form 8606 filer with contributions (person.ira_has and person.ira_files_8606).

### person.ira_8606_line14 — Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier ye
Status: **AGREE**

### person.ira_ssb — This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.sav_trad"}], "test": "eq"}, "then": {"input": "person.ira_trad"}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": true}, {"input": "person.ira_age50"}], "test": "eq"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}, {"ref": "ira.line10"}], "op": "smaller_of"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "spouse"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line12b"}}, {"guard": {"args": [{"const": "taxpayer"}, {"input": "person.role"}], "test": "eq"}, "then": {"ref": "ira.line12a"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. amb.2025.ira_ssb_copy; i1040gi p. 98, line 12. As round 3: the reply copies its person.ira_deduction, which is circular (ruled there) and which reads Form 1040 line 9 through the worksheet's modified AGI, so the Social Security Benefits Worksheet would read itself: the cycle the register's chosen reading breaks.

### person.ira_se — This person's part of worksheet line 9 (zero without a Schedule C)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"input": "person.sep_contrib"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.simple_employer"}, {"of": [{"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}, {"from": {"input": "person.simple_deferral"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.simple_deferral"}, {"param": "ret.simple_limit"}], "op": "smaller_of"}}], "op": "sum"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}], "op": "sum"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"input": "person.sep_contrib"}, {"line": "Step 21"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "Step 21"}}], "op": "choose"}, {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}], "op": "sum"}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.s16 (person.h_sep_10000, malformed) and person.se_line13, so no value of it was computed. By reading: i1040gi p. 97, line 9: "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner ... minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-." The intended amount is Schedule C line 31 less lines 15 and 16 floored at zero, the project's (amb.2025.ira_se_floor); it reads sc.line31 for sc.result (the cited at-risk refusal, scope) and declares se_screen for every person (scope, as in the Claude log).

### person.edu_kid — Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of yo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": 0}, {"ref": "f8863.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f8863.line7"}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.sav_born"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.edu_fulltime"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_half_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "person.edu_born_2007"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "person.edu_born_2002"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_parent"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 7, Line 7: "1. You were: a. Under age 18 at the end of 2025, or b. Age 18 at the end of 2025 and your earned income (defined later) was less than one-half of your support (defined later), or c. Over age 18 and under age 24 at the end of 2025 and a full-time student". The reply restructured its test (under 24, born on or after January 2, 2002; a parent alive; not filing jointly; and either born on or after January 2, 2007, or a full-time student with earned income below half of support). Its branch for anyone born on or after January 2, 2007 still covers age 18 without the support test of (b) (person.sav_born, born before January 2, 2008, separates under 18 from 18; amb.2025.edu_age_rule), so an 18-year-old whose earned income was at least half of support loses the refundable credit, as round 3; ages 19 to 23 are the project's (c). It still omits the f8863.kid_needed gate, so it needs these answers where the interview does not ask them.

### person.x_l1 — Form 5329 line 1 for this person: early distributions includible in income
Status: **AGREE**

### person.x_l2_all — Exception amounts before the per-person limits
Status: **AGREE**

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
{"of": [{"amount": {"from": {"collection": "retirement", "field": "retirement.l1", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}}, "op": "multiply_rate", "rate": {"param": "f5329.early_rate"}}, {"from": {"amount": {"from": {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}}, "op": "multiply_rate", "rate": {"param": "f5329.simple_rate"}}, "op": "subtract_floor0", "take": {"amount": {"from": {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"collection": "retirement", "field": "retirement.l2_s", "op": "sum_over", "where": null}}, "op": "multiply_rate", "rate": {"param": "f5329.early_rate"}}}], "op": "sum"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. f5329 p. 1, Part I, line 4: "Additional tax. Enter 10% (0.10) of line 3. Include this amount on Schedule 2 (Form 1040), line 8"; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude"; f5329 p. 2, Part VII, line 49: "Enter 6% (0.06) of the smaller of line 48 or the value of your HSAs on December 31, 2025". The line is the person's Form 5329 tax for Schedule 2 line 8 (lines 4 and 49). The reply figures 10% of line 1 less the exception amounts before the per-person limits, plus 15% more on the code S part; it applies none of the limits of exceptions 05, 09, 19, 22 and 23 and leaves out Part VII. By reading: stage21.blind.e4 (exceptions 09 and 19 over their limits, blind-predicted line 4 $520.00): project $520.00, candidate $0.00; stage21.blind.e10 (Part VII, line 49 $54.60): project $254.60, candidate $200.00. Its 10%/25% split and the person.x_other refusal are the project's.

### person.x_must — One if this person must file Form 5329
Status: **DISAGREE**

Project:

```json
{"collection": "f5329", "field": "f5329.one", "op": "sum_over", "where": {"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f5329.l48"}], "test": "lt"}], "test": "any"}}
```

Second:

```json
{"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i5329 p. 1, Who Must File: "However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don't have to file Form 5329." The project counts the person's form when it must be filed (an exception claimed, a code S distribution, or a 2025 HSA excess; decision D5). The reply counts the person's code 1 and code S distributions, so every code 1 distribution with no exception makes the form required and the no-form path with the Schedule 2 line 8 box never applies. By reading: stage21.example.tom_jones (p590b p. 29, one code 1 distribution, no exception; s2.line8_box checked): project 0, candidate 1.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i5329 p. 5, Line 2, exception 05: "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." The reply sums the exception 05 amounts with no limit, as the Claude reply (ruled model error there on stage21.blind.e6: project $7,475.00, candidate $9,000.00).

### person.x_two23 — Exception 23 claimed on more than one distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "retirement", "field": "retirement.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "test": "lt"}], "test": "any"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. p590b p. 28, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year". The line is the refusal gate for exception 23 claimed on more than one Form 1099-R (person.x_n23 above 1). The reply tests whether any exception 22 or 23 amount is above zero, so as the gate it is it would refuse every return claiming exception 22 or 23 once. By reading: stage21.mut.e23_over_cap (one exception 23 distribution, line 4 $200.00): project False, candidate True.

### person.x_limited_sum — Exceptions 05, 09, 19, 22 and 23 within their limits
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}
```

Second:

```json
{"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. p590b p. 27, First home: "When added to all your prior qualified first-time homebuyer distributions, if any, total qualifying distributions can't be more than $10,000"; p590b p. 28: "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer"; "must not exceed the lesser of $10,300 for 2025"; "must not exceed the lesser of $1,000". The line is exceptions 05, 09, 19, 22 and 23 within their limits. The reply adds the five amounts with no limit. By reading: stage21.blind.e4 (09 $11,500.00 against $8,800.00 left; 19 $7,500.00 against $5,000.00; blind-predicted line 2 $13,800.00): project $13,800.00, candidate $19,000.00. Separately, the project's own limits of exceptions 22 and 23 omit the account-value limbs (p590b p. 28: "the lesser of $10,300 for 2025 or 50% of the present value of the IRA"; "the lesser of $1,000 or your total interest in the IRA minus $1,000"), which no question attests: finding F1 VALUE-LIMBS (.transcription/proposed/stage21/person.findings.md); both replies share the omission, so it is no difference here.

### person.x_other_exc — Exceptions without a fixed limit
Status: **AGREE**

### person.x_limit_binds — A limited exception over its limit on a person with a code S distribution
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l1_s", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"of": [{"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"ref": "sa.line4"}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"from": {"param": "f5329.cap_first_home"}, "op": "subtract_floor0", "take": {"input": "person.x_prior09"}}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"of": [{"amount": {"param": "f5329.cap_birth"}, "count": {"input": "person.x_births"}, "op": "multiply_count"}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}], "op": "smaller_of"}}], "op": "choose"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"param": "f5329.cap_abuse"}], "op": "smaller_of"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}, {"param": "f5329.cap_emergency"}], "op": "smaller_of"}], "op": "sum"}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0}, {"of": [{"collection": "retirement", "field": "retirement.l2_e05", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e09", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e19", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e22", "op": "sum_over", "where": null}, {"collection": "retirement", "field": "retirement.l2_e23", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}
```

Second transcription's note: The supplied retirement interface does not expose per-exception limit usage; treated as true when any limited-exception amount is present.

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%"; amb.2025.f5329_simple_limits. The line is the refusal gate for a limited exception over its limit on a person with a code S distribution. The reply tests only that a limited exception amount is present, with neither the over-limit nor the code S condition, so as the gate it would refuse every return with exception 05, 09, 19, 22 or 23. By reading: stage21.blind.e6 (exception 05, no SIMPLE distribution, completed): project False, candidate True.

### person.x_hsa_excess — This person's 2025 HSA excess contributions (Form 8889)
Status: **AGREE**

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
{"args": [{"args": [{"const": false}, {"line": "over"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"line": "employers"}], "test": "lt"}, {"args": [{"param": "ss.base"}, {"line": "wages"}], "test": "lt"}], "test": "all"}
```

Ruling: representation; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i1040gi p. 117, Line 11: "But if any one employer withheld more than $10,918.20, you can't claim the excess on your return." The candidate adds "no employer over the limit" (overcount zero) to the test; the project refuses person.credit when person.over, and eligible feeds only the credit and excess lines (the Claude reply's same test is ruled representation there; every difference has person.over true, refused returns). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged. The reply's wages and overcount helpers are now the project's (w2.wages, w2.over); the added test of person.over false is as ruled.

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

Ruling: scope; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. p560 p. 39, Step 1: "Enter your net profit from Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34; or Schedule K-1 (Form 1065), box 14, code A." The candidate sums Schedule C line 31; the project copies sc.result and refuses at person.se_screened when there is self-employment income not on a Schedule C. The differences are the at-risk refusal and that cited screen, as on the Claude reply's identical line (ruled scope there). Stage 21 re-check: same expression as Stage 19 round 3 (dependency closure unchanged); project line unchanged. It now also declares the plan_screen refusal on this step; the project refuses at person.plan_screened (cited p560 p. 7): scope on that kind too.

### Step 2 — Deduction for self-employment tax from Schedule 1, line 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"from": {"collection": "sc", "field": "sc.result", "op": "sum_over", "where": null}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}}], "op": "choose"}
```

Second:

```json
{"expression": {"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"from": {"param": "ss.base"}, "op": "subtract_floor0", "take": {"line": "wages"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.se_line12 and person.h_se_line4a (malformed) through its Schedule SE line 13, so no value of it was computed. By reading: p560 p. 39, Step 2: "Enter your deduction for self-employment tax from Schedule 1 (Form 1040), line 15." A copy of its Schedule SE line 13, the project's.

### Step 3 — Net earnings from self-employment. Subtract step 2 from step 1
Status: **DISAGREE**

Project:

```json
{"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}
```

Second:

```json
{"expression": {"from": {"line": "Step 1"}, "op": "subtract_floor0", "take": {"line": "Step 2"}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_se_line4a (malformed) through Steps 1 to 3, so no value of it was computed. By reading: p560 p. 39, Step 3: "Net earnings from self-employment. Subtract step 2 from step 1"; amb.2025.sep_loss_floor (the project floors at zero). The intended subtraction is the source's, floored at zero as the register's chosen reading (subtract_floor0, the project's person.sep_s3).

### Step 5 — Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal p
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"of": [{"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, {"param": "sc.hundred_cents"}], "op": "sum"}}
```

Second:

```json
{"expression": {"amount": {"line": "Step 3"}, "op": "prorate", "part": {"amount": {"param": "sc.hundred_cents"}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 9, "whole": {"of": [{"amount": {"param": "sc.hundred_cents"}, "count": {"const": 100, "type": "Count"}, "op": "multiply_count"}, {"amount": {"param": "sc.hundred_cents"}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}], "op": "sum"}}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_se_line4a (malformed) through Steps 1 to 3, so no value of it was computed. By reading: p560 pp. 38-39, Rate Worksheet and Step 5: "Multiply step 3 by step 4". The intended product is Step 3 times the plan rate divided by 1 plus the rate, as the project, though it carries nine decimal places where the line rounds the reduced rate to six (a rounding difference).

### Step 6 — Multiply $350,000 by your plan contribution rate (not the reduced rate)
Status: **DISAGREE**

Project:

```json
{"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"expression": {"amount": {"param": "ret.comp_limit"}, "op": "prorate", "part": {"amount": {"param": "sc.hundred_cents"}, "count": {"input": "person.sep_rate"}, "op": "multiply_count"}, "places": 9, "whole": {"amount": {"param": "sc.hundred_cents"}, "count": {"const": 100, "type": "Count"}, "op": "multiply_count"}}, "invalid_model_types": [{"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_sep_10000 (malformed), so no value of it was computed. By reading: p560 p. 39, Step 6: "Multiply $350,000 by your plan contribution rate (not the reduced rate)". The intended product is the project's.

### Step 7 — Enter the smaller of step 5 or step 6
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "Step 5"}, {"line": "Step 6"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_sep_10000 and person.h_se_line4a (malformed) through Steps 5 and 6, so no value of it was computed. By reading: p560 p. 39, Step 7: "Enter the smaller of step 5 or step 6". The intended choice is the project's.

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
{"expression": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": "sep"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"line": "Step 7"}, {"line": "Step 8"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "simple"}, {"input": "person.plan"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}], "test": "le"}, "then": {"from": {"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"of": [{"line": "zero"}, {"alternatives": [{"guard": {"args": [{"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 0}, {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"amount": {"collection": "sc", "field": "sc.line31", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}, {"param": "se.floor"}], "test": "lt"}, "then": {"line": "zero"}}], "op": "choose"}, {"of": [{"input": "person.simple_employer"}, {"of": [{"input": "person.simple_deferral"}, {"of": [{"keys": [{"input": "person.simple_age"}], "op": "keyed_lookup", "table": "simple_catchup"}, {"param": "ret.simple_limit"}], "op": "sum"}], "op": "smaller_of"}], "op": "sum"}], "op": "smaller_of"}}], "op": "choose"}, "invalid_model_types": [{"line": "person.se_line6", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line12", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.h_sep_10000", "message": "malformed expression (project schema): data/count must be string, data/op must be equal to constant, data/op must be equal to constant"}, {"line": "person.h_se_line4a", "message": "malformed expression (project schema): data/alternatives/0/guard must be object, data/alternatives/0/guard must be object, data/alternatives/0/guard must be object"}, {"line": "person.se_line6", "message": "person.person.se_line6: malformed expression"}, {"line": "person.se_line12", "message": "person.person.se_line12: malformed expression"}, {"line": "person.h_sep_10000", "message": "person.person.h_sep_10000: malformed expression"}, {"line": "person.h_se_line4a", "message": "person.person.h_se_line4a: malformed expression"}]}
```

Ruling: model error; adjudicates the declaration, not the tax reading. Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line's candidate reaches person.h_sep_10000 and person.h_se_line4a (malformed) through Steps 5 and 6, so no value of it was computed. By reading: p560 p. 39, Step 21: the smaller of step 7 or step 8 when there are no elective deferrals. The intended choice is the project's.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 3, Who cannot claim a credit: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: it now copies the aqee definition's line27 for every person with the edu_over refusal declared, and drops every eligibility gate of round 3 (person.edu, person.edu_1098t, the lines 23 to 26 answers, the institution EIN) and the student-TIN test, so a person who is not a student, or whose student fails the American opportunity credit tests, gets the amounts (lines 27 to 30 also omit the filers' TIN test, household.all_tin, amb.2025.edu_filer_tin); the arithmetic is the project's aqee definition.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 3, Who cannot claim a credit: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: it now copies the aqee definition's line28 for every person with the edu_over refusal declared, and drops every eligibility gate of round 3 (person.edu, person.edu_1098t, the lines 23 to 26 answers, the institution EIN) and the student-TIN test, so a person who is not a student, or whose student fails the American opportunity credit tests, gets the amounts (lines 27 to 30 also omit the filers' TIN test, household.all_tin, amb.2025.edu_filer_tin); the arithmetic is the project's aqee definition.

### 29 — Multiply line 28 by 25% (0.25)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 3, Who cannot claim a credit: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: it now copies the aqee definition's line29 for every person with the edu_over refusal declared, and drops every eligibility gate of round 3 (person.edu, person.edu_1098t, the lines 23 to 26 answers, the institution EIN) and the student-TIN test, so a person who is not a student, or whose student fails the American opportunity credit tests, gets the amounts (lines 27 to 30 also omit the filers' TIN test, household.all_tin, amb.2025.edu_filer_tin); the arithmetic is the project's aqee definition.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "eq"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "ne"}, "then": {"of": [{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.tin"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_1098t"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "person.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "eq"}, "then": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": 0}, {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}], "test": "ne"}, "then": {"of": [{"amount": {"from": {"of": [{"from": {"of": [{"input": "person.edu_inst"}, {"input": "person.edu_mat"}], "op": "sum"}, "op": "subtract_floor0", "take": {"of": [{"input": "person.edu_a2025"}, {"input": "person.edu_a2026"}, {"input": "person.edu_refunds"}], "op": "sum"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}
```

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 3, Who cannot claim a credit: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: it now copies the aqee definition's line30 for every person with the edu_over refusal declared, and drops every eligibility gate of round 3 (person.edu, person.edu_1098t, the lines 23 to 26 answers, the institution EIN) and the student-TIN test, so a person who is not a student, or whose student fails the American opportunity credit tests, gets the amounts (lines 27 to 30 also omit the filers' TIN test, household.all_tin, amb.2025.edu_filer_tin); the arithmetic is the project's aqee definition.

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

Ruling: model error; Not executable: the reply fails validation on five expressions (person.se_line6, person.se_line12 and person.h_se_line4a: "data/alternatives/0/guard must be object"; person.h_sep_10000: "data/count must be string"; person.h_educator_cap: "data/of/1 must be string", project schema), so triage cannot run any of its lines (triage/person.deepseek.json, state invalid); this line is outside those errors' dependency closure and is ruled by reading the expressions against the source. i8863 p. 3, Who cannot claim a credit: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)"; i8863 p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." The reply changed: it now copies the aqee definition's ws4_llc for every person with the edu_over refusal declared, and drops every eligibility gate of round 3 (person.edu, person.edu_1098t, the lines 23 to 26 answers, the institution EIN) and the student-TIN test, so a person who is not a student, or whose student fails the American opportunity credit tests, gets the amounts, and the lifetime learning credit amount is not limited to students who do not take the American opportunity credit; the arithmetic is the project's aqee definition.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| person.se_line6 | person.se_screen | person.se_screen |
| person.se_line12 | person.se_screen | person.se_screen |
| person.se_line13 | person.se_screen | person.se_screen |
| person.s16 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| person.eic_se | person.se_screen | person.se_screen |
| person.dc_earned | person.se_screen | person.se_screen |
| person.dc_earned_b | person.se_screen | person.se_screen |
| person.sav_line1 | person.sav_able | - |
| person.sav_line2 | person.sav_excess | person.sav_excess |
| person.ira_contrib | person.ira_excess | person.ira_excess |
| person.ira_cov | person.ira_excess | person.ira_excess |
| person.ira_line2 | person.ira_excess | person.ira_excess |
| person.ira_line6 | person.ira_excess | person.ira_excess |
| person.ira_line7 | person.ira_excess | person.ira_excess |
| person.ira_deduction | person.ira_excess | person.ira_excess |
| person.ira_nondeductible | person.ira_excess | person.ira_excess |
| person.ira_files_8606 | person.ira_basis_adjusted, person.ira_excess | person.ira_basis_adjusted, person.ira_excess |
| person.ira_8606_line2 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.ira_8606_line14 | person.ira_basis_adjusted | person.ira_basis_adjusted |
| person.ira_ssb | person.ira_excess | person.ira_excess |
| person.ira_se | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| person.x_l1 | person.x_other | person.x_other |
| person.x_l2_all | person.x_other | person.x_other |
| person.x_l1_s | person.x_other | person.x_other |
| person.x_l2_s | person.x_other | person.x_other |
| person.x_tax | person.x_other | - |
| person.x_must | person.x_other | person.x_other |
| person.x_other_exc | person.x_other | person.x_other |
| credit | person.rrta | - |
| Step 1 | person.plan_screen | person.plan_screen |
| Step 2 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| Step 3 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| Step 5 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| Step 6 | person.plan_screen | person.plan_screen |
| Step 7 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
| Step 8 | person.plan_screen | person.plan_screen |
| Step 21 | person.plan_screen, person.se_screen | person.plan_screen, person.se_screen |
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
    label: "Number of employers on this person’s wage statements"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
  - id: person.overcount
    printed: "overcount"
    label: "Number of employers that withheld more than the Social Security tax limit"
    type: Count
    expr:
      op: sum_over
      collection: w2
      field: w2.one
      where: {op: test, eq: [w2.over, {const: true}]}
  - id: person.over
    printed: "over"
    label: "Any one employer withheld more than the Social Security tax limit"
    type: Bool
    expr: {op: test, gt: [person.overcount, {const: 0, type: Count}]}
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
    label: "Eligible for the excess Social Security credit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [person.employers, {const: 1, type: Count}]}
        - {op: test, gt: [person.wages, {param: ss.base}]}
        - {op: test, eq: [person.over, {const: false}]}
  - id: person.excess
    printed: "excess"
    label: "Social Security tax withheld above the limit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.withheld, take: {param: ss.limit}}
  - id: person.zero
    printed: "zero"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: person.credit
    printed: "credit"
    label: "Excess Social Security credit for this person"
    type: NonNegDollars
    refuses: [person.rrta]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.eligible, {const: true}]}, then: person.excess}
        - {guard: {op: test, eq: [person.eligible, {const: false}]}, then: person.zero}
  - id: person.sep_s1
    printed: "Step 1"
    label: "Net profit from Schedule C"
    type: Dollars
    refuses: [person.plan_screen]
    expr: {op: sum_over, collection: sc, field: sc.line31}
  - id: person.sep_s2
    printed: "Step 2"
    label: "Deduction for self-employment tax"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: copy, from: person.se_line13}
  - id: person.sep_s3
    printed: "Step 3"
    label: "Net earnings from self-employment"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: subtract_floor0, from: person.sep_s1, take: person.sep_s2}
  - id: person.sep_s5
    printed: "Step 5"
    label: "Step 3 multiplied by the reduced contribution rate"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: prorate, amount: person.sep_s3, part: person.h_sep_part, whole: person.h_sep_whole, places: 9}
  - id: person.sep_s6
    printed: "Step 6"
    label: "Compensation limit multiplied by the plan contribution rate"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: prorate, amount: person.h_comp_limit, part: person.h_sep_part, whole: person.h_sep_10000, places: 9}
  - id: person.sep_s7
    printed: "Step 7"
    label: "Smaller of Step 5 or Step 6"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: smaller_of, of: [person.sep_s5, person.sep_s6]}
  - id: person.sep_s8
    printed: "Step 8"
    label: "Contribution dollar limit"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr: {op: param, ref: ret.sep_dollar_limit}
  - id: person.sep_s21
    printed: "Step 21"
    label: "Maximum deductible contribution for this person"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.plan, {const: "sep"}]}, then: person.h_sep_s21_sep}
        - {guard: {op: test, eq: [person.plan, {const: "simple"}]}, then: person.h_simple_deduction}
        - {guard: {op: test, eq: [person.plan, {const: "none"}]}, then: person.zero}
  - id: person.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses for the American opportunity credit"
    type: NonNegDollars
    refuses: [person.edu_over]
    expr: {op: copy, from: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_edu_adj}, line: line27}}
  - id: person.edu_line28
    printed: "28"
    label: "Line 27 reduced by $2,000"
    type: NonNegDollars
    refuses: [person.edu_over]
    expr: {op: copy, from: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_edu_adj}, line: line28}}
  - id: person.edu_line29
    printed: "29"
    label: "25% of line 28"
    type: NonNegDollars
    refuses: [person.edu_over]
    expr: {op: copy, from: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_edu_adj}, line: line29}}
  - id: person.edu_line30
    printed: "30"
    label: "American opportunity credit for this student"
    type: NonNegDollars
    refuses: [person.edu_over]
    expr: {op: copy, from: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_edu_adj}, line: line30}}
  - id: person.edu_line31
    printed: "31"
    label: "Adjusted qualified education expenses for the lifetime learning credit"
    type: NonNegDollars
    refuses: [person.edu_over]
    expr: {op: copy, from: {def: aqee, bind: {inst: person.edu_inst, mat: person.edu_mat, adj: person.h_edu_adj}, line: ws4_llc}}
  - id: person.one
    printed: "(helper)"
    label: "One"
    type: Count
    expr: {op: param, ref: person.one}
  - id: person.educator_deduction
    printed: "(helper)"
    label: "Educator expense deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.eligible_educator, {const: true}]}, then: person.h_educator_cap}
        - {guard: {op: test, eq: [person.eligible_educator, {const: false}]}, then: person.zero}
  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of Forms 8889 for this person"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where: {op: test, eq: [f8889.any, {const: true}]}
  - id: person.hsa_split
    printed: "(helper)"
    label: "Number of Forms 8889 with a family-coverage split"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where: {op: test, eq: [f8889.split, {const: true}]}
  - id: person.hsa_agreed
    printed: "(helper)"
    label: "Number of Forms 8889 using an agreed allocation"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where: {op: test, eq: [f8889.allocation, {const: "agreed"}]}
  - id: person.hsa_step1
    printed: "(helper)"
    label: "Total HSA Step 1 family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.step1}
  - id: person.hsa_share
    printed: "(helper)"
    label: "Total allocated HSA share"
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
    label: "Additional 20% tax on HSA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line17b}
  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers with qualified tips"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one}
  - id: person.tip_total
    printed: "(helper)"
    label: "Total qualified tips from all employers"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}
  - id: person.tip_reported
    printed: "(helper)"
    label: "Qualified tips reported by employers"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.amount}
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
    label: "Total Form W-2 box 2 federal income tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}
  - id: person.ira_amount_a
    printed: "(helper)"
    label: "Total IRA distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.amount_a
      where: {op: test, eq: [retirement.is_ira, {const: true}]}
  - id: person.ira_taxable
    printed: "(helper)"
    label: "Taxable IRA distributions"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.ira_taxable}
  - id: person.ira_rollovers
    printed: "(helper)"
    label: "Number of IRA distributions with rollovers"
    type: Count
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where:
        op: test
        all:
          - {op: test, eq: [retirement.is_ira, {const: true}]}
          - {op: test, eq: [retirement.has_rollover, {const: true}]}
  - id: person.plan_amount_a
    printed: "(helper)"
    label: "Total pension and annuity distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.amount_a
      where: {op: test, eq: [retirement.account, {const: "plan"}]}
  - id: person.plan_taxable
    printed: "(helper)"
    label: "Taxable pension and annuity distributions"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: retirement
      field: retirement.plan_taxable
      where: {op: test, eq: [retirement.account, {const: "plan"}]}
  - id: person.plan_rollovers
    printed: "(helper)"
    label: "Number of pension and annuity distributions with rollovers"
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
    label: "Distributions counted for the saver’s credit"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.sav_amount}
  - id: person.medicare5
    printed: "(helper)"
    label: "Total Medicare wages and tips"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}
  - id: person.medicare6
    printed: "(helper)"
    label: "Total Medicare tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}
  - id: person.sc_count
    printed: "(helper)"
    label: "Number of Schedule C businesses"
    type: Count
    expr: {op: sum_over, collection: sc, field: sc.one}
  - id: person.ho_count
    printed: "(helper)"
    label: "Number of Schedule C businesses with a home office deduction"
    type: Count
    expr:
      op: sum_over
      collection: sc
      field: sc.one
      where: {op: test, eq: [sc.ho_uses, {const: true}]}
  - id: person.mq_q4
    printed: "(helper)"
    label: "Total mid-quarter fourth-quarter depreciation"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_q4}
  - id: person.mq_total
    printed: "(helper)"
    label: "Total mid-quarter depreciation"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.mq_total}
  - id: person.cost179
    printed: "(helper)"
    label: "Total cost of section 179 property"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.cost179}
  - id: person.s179_nonlisted
    printed: "(helper)"
    label: "Section 179 elected cost for nonlisted property"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.s179_elected}
  - id: person.s179_listed
    printed: "(helper)"
    label: "Section 179 elected cost for listed property"
    type: NonNegDollars
    note: "The supplied Schedule C interface does not expose a person-level split of elected section 179 cost between listed and nonlisted property; this line reports zero and the total elected cost is carried on person.s179_nonlisted."
    expr: {op: copy, from: person.zero}
  - id: person.income179
    printed: "(helper)"
    label: "Business income available for the section 179 limitation"
    type: Dollars
    expr:
      op: sum_over
      collection: sc
      field: sc.line29
      where: {op: test, gt: [sc.line29, {const: 0}]}
  - id: person.sc_total
    printed: "(helper)"
    label: "Total Schedule C net profit or loss"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.line31}
  - id: person.se_line6
    printed: "(helper)"
    label: "Schedule SE line 6 net earnings"
    type: NonNegDollars
    refuses: [person.se_screen]
    expr:
      op: choose
      alternatives:
        - {guard: person.h_se_owes, then: person.h_se_line6_raw}
        - {guard: {op: test, eq: [person.h_se_owes, {const: false}]}, then: person.zero}
  - id: person.se_line12
    printed: "(helper)"
    label: "Schedule SE line 12 self-employment tax"
    type: NonNegDollars
    refuses: [person.se_screen]
    expr:
      op: choose
      alternatives:
        - {guard: person.h_se_owes, then: person.h_se_line12_raw}
        - {guard: {op: test, eq: [person.h_se_owes, {const: false}]}, then: person.zero}
  - id: person.se_line13
    printed: "(helper)"
    label: "Deduction for one-half of self-employment tax"
    type: NonNegDollars
    refuses: [person.se_screen]
    expr: {op: multiply_rate, amount: person.se_line12, rate: {param: se.rate_50}}
  - id: person.s16
    printed: "(helper)"
    label: "Deductible self-employed SEP, SIMPLE, and qualified plan contributions"
    type: NonNegDollars
    refuses: [person.plan_screen]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.plan, {const: "sep"}]}, then: person.h_s16_sep}
        - {guard: {op: test, eq: [person.plan, {const: "simple"}]}, then: person.sep_s21}
        - {guard: {op: test, eq: [person.plan, {const: "none"}]}, then: person.zero}
  - id: person.positive_profits
    printed: "(helper)"
    label: "Total net profits from profitable Schedule C businesses"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_positive_profits_sum, take: {const: 0}}
  - id: person.sehi
    printed: "(helper)"
    label: "Self-employed health insurance deduction"
    type: NonNegDollars
    expr: {op: sum_over, collection: sc, field: sc.f7206_line14}
  - id: person.qbi
    printed: "(helper)"
    label: "Qualified business income from Schedule C businesses"
    type: Dollars
    expr: {op: sum_over, collection: sc, field: sc.qbi}
  - id: person.eic_se
    printed: "(helper)"
    label: "Self-employment earned income for the earned income credit"
    type: Dollars
    refuses: [person.se_screen]
    expr: {op: subtract, from: person.sc_total, take: person.se_line13}
  - id: person.sc_1a
    printed: "(helper)"
    label: "Number of statutory-employee Schedule C businesses"
    type: Count
    expr:
      op: sum_over
      collection: sc
      field: sc.one
      where: {op: test, eq: [sc.statutory, {const: true}]}
  - id: person.dc_benefits
    printed: "(helper)"
    label: "Dependent care benefits from Form W-2 box 10"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.dc_benefits}
  - id: person.dc_has_box10
    printed: "(helper)"
    label: "Any dependent care benefits in Form W-2 box 10"
    type: Bool
    expr: {op: test, gt: [person.dc_benefits, {const: 0}]}
  - id: person.dc_earned
    printed: "(helper)"
    label: "Earned income for the child and dependent care credit"
    type: Dollars
    expr: {op: sum, of: [person.box1, person.eic_se]}
  - id: person.dc_earned_b
    printed: "(helper)"
    label: "Earned income excluding dependent care benefits for the exclusion computation"
    type: Dollars
    expr: {op: subtract, from: person.dc_earned, take: person.dc_benefits}
  - id: person.sav_ineligible
    printed: "(helper)"
    label: "Ineligible for the saver’s credit"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [person.sav_born, {const: false}]}
        - {op: test, eq: [person.sav_claimed, {const: true}]}
        - {op: test, eq: [person.sav_student, {const: true}]}
  - id: person.sav_line1
    printed: "(helper)"
    label: "Saver’s credit line 1 traditional, Roth IRA and ABLE contributions"
    type: NonNegDollars
    refuses: [person.sav_able]
    expr: {op: sum, of: [person.ira_trad, person.sav_roth]}
  - id: person.sav_line2
    printed: "(helper)"
    label: "Saver’s credit line 2 elective deferrals and voluntary contributions"
    type: NonNegDollars
    refuses: [person.sav_excess]
    expr: {op: sum, of: [person.sav_voluntary, person.h_sav_w2_listed]}
  - id: person.ira_contrib
    printed: "(helper)"
    label: "Traditional IRA contributions for 2025"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr: {op: copy, from: person.ira_trad}
  - id: person.ira_cov
    printed: "(helper)"
    label: "Covered by a retirement plan at work"
    type: Bool
    refuses: [person.ira_excess]
    expr: {op: copy, from: person.ira_work_plan}
  - id: person.ira_line2
    printed: "(helper)"
    label: "IRA deduction worksheet line 2"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.role, {const: "taxpayer"}]}, then: ira.line2a}
        - {guard: {op: test, eq: [person.role, {const: "spouse"}]}, then: ira.line2b}
  - id: person.ira_line6
    printed: "(helper)"
    label: "IRA deduction worksheet line 6"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.role, {const: "taxpayer"}]}, then: ira.line6a}
        - {guard: {op: test, eq: [person.role, {const: "spouse"}]}, then: ira.line6b}
  - id: person.ira_line7
    printed: "(helper)"
    label: "IRA deduction worksheet line 7"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.role, {const: "taxpayer"}]}, then: ira.line7a}
        - {guard: {op: test, eq: [person.role, {const: "spouse"}]}, then: ira.line7b}
  - id: person.ira_deduction
    printed: "(helper)"
    label: "IRA deduction"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [person.role, {const: "taxpayer"}]}, then: ira.line12a}
        - {guard: {op: test, eq: [person.role, {const: "spouse"}]}, then: ira.line12b}
  - id: person.ira_nondeductible
    printed: "(helper)"
    label: "Nondeductible traditional IRA contributions"
    type: NonNegDollars
    refuses: [person.ira_excess]
    expr: {op: sum_over, collection: f8606, field: f8606.line1}
  - id: person.ira_files_8606
    printed: "(helper)"
    label: "Form 8606 required for this person"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [person.ira_nondeductible, {const: 0}]}
        - {op: test, gt: [person.ira_8606_line2, {const: 0}]}
        - {op: test, eq: [person.ira_dist_gate, {const: true}]}
  - id: person.ira_8606_line2
    printed: "(helper)"
    label: "Form 8606 line 2 total basis"
    type: NonNegDollars
    refuses: [person.ira_basis_adjusted]
    expr: {op: sum_over, collection: f8606, field: f8606.line2}
  - id: person.ira_dist_gate
    printed: "(helper)"
    label: "Traditional IRA distribution or Roth conversion in 2025"
    type: Bool
    expr: {op: copy, from: person.ira_dist}
  - id: person.ira_8606_line14
    printed: "(helper)"
    label: "Form 8606 line 14 total basis for 2025 and earlier years"
    type: NonNegDollars
    refuses: [person.ira_basis_adjusted]
    expr: {op: sum_over, collection: f8606, field: f8606.line14}
  - id: person.ira_ssb
    printed: "(helper)"
    label: "IRA deduction used in the Social Security Benefits Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: person.ira_deduction}
  - id: person.ira_se
    printed: "(helper)"
    label: "Self-employment earned income for the IRA deduction worksheet"
    type: NonNegDollars
    refuses: [person.se_screen]
    expr: {op: subtract_floor0, from: person.sc_total, take: person.h_ira_se_ded}
  - id: person.edu_kid
    printed: "(helper)"
    label: "Student is treated as a dependent student for the refundable American opportunity credit"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [person.edu_born_2002, {const: false}]}
        - {op: test, eq: [person.edu_parent, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfj"}]}
        - op: test
          any:
            - {op: test, eq: [person.edu_born_2007, {const: false}]}
            - op: test
              all:
                - {op: test, eq: [person.edu_fulltime, {const: true}]}
                - {op: test, eq: [person.edu_half_support, {const: true}]}
  - id: person.x_l1
    printed: "(helper)"
    label: "Form 5329 line 1 early distributions includible in income"
    type: NonNegDollars
    refuses: [person.x_other]
    expr: {op: sum_over, collection: retirement, field: retirement.l1}
  - id: person.x_l2_all
    printed: "(helper)"
    label: "Form 5329 line 2 early distributions not subject to the additional tax"
    type: NonNegDollars
    refuses: [person.x_other]
    expr: {op: sum_over, collection: retirement, field: retirement.l2}
  - id: person.x_l1_s
    printed: "(helper)"
    label: "SIMPLE IRA early distributions includible in income"
    type: NonNegDollars
    refuses: [person.x_other]
    expr: {op: sum_over, collection: retirement, field: retirement.l1_s}
  - id: person.x_l2_s
    printed: "(helper)"
    label: "SIMPLE IRA early distributions not subject to the additional tax"
    type: NonNegDollars
    refuses: [person.x_other]
    expr: {op: sum_over, collection: retirement, field: retirement.l2_s}
  - id: person.x_tax
    printed: "(helper)"
    label: "Additional tax on early distributions"
    type: NonNegDollars
    refuses: [person.x_other]
    expr: {op: sum, of: [person.h_x_base_tax, person.h_x_extra]}
  - id: person.x_must
    printed: "(helper)"
    label: "Number of distributions subject to the early distribution additional tax"
    type: Count
    refuses: [person.x_other]
    expr:
      op: sum_over
      collection: retirement
      field: retirement.one
      where: {op: test, eq: [retirement.early, {const: true}]}
  - id: person.x_c05
    printed: "(helper)"
    label: "Exception 05 medical expenses"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e05}
  - id: person.x_two23
    printed: "(helper)"
    label: "Exception 22 or 23 applies"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [person.h_x_e22, {const: 0}]}
        - {op: test, gt: [person.h_x_e23, {const: 0}]}
  - id: person.x_limited_sum
    printed: "(helper)"
    label: "Sum of exceptions subject to per-person limits"
    type: NonNegDollars
    expr: {op: sum, of: [person.x_c05, person.h_x_e09, person.h_x_e19, person.h_x_e22, person.h_x_e23]}
  - id: person.x_other_exc
    printed: "(helper)"
    label: "Exceptions other than the limited exceptions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l2_all, take: person.x_limited_sum}
  - id: person.x_limit_binds
    printed: "(helper)"
    label: "A limited exception is present"
    type: Bool
    note: "The supplied retirement interface does not expose per-exception limit usage; treated as true when any limited-exception amount is present."
    expr: {op: test, gt: [person.x_limited_sum, {const: 0}]}
  - id: person.x_hsa_excess
    printed: "(helper)"
    label: "Excess HSA contributions for 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.excess_amt}
  - id: person.h_ss_base
    printed: "(helper)"
    label: "Social security wage base"
    type: NonNegDollars
    expr: {op: param, ref: ss.base}
  - id: person.h_comp_limit
    printed: "(helper)"
    label: "Compensation limit for retirement plan contributions"
    type: NonNegDollars
    expr: {op: param, ref: ret.comp_limit}
  - id: person.h_sep_100
    printed: "(helper)"
    label: "One hundred cents used as a rate-building unit"
    type: NonNegDollars
    expr: {op: param, ref: sc.hundred_cents}
  - id: person.h_sep_10000
    printed: "(helper)"
    label: "Ten thousand cents used as a rate-building unit"
    type: NonNegDollars
    expr: {op: multiply_count, amount: person.h_sep_100, count: {const: 100, type: Count}}
  - id: person.h_sep_part
    printed: "(helper)"
    label: "Plan percentage as cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: person.h_sep_100, count: person.sep_rate}
  - id: person.h_sep_whole
    printed: "(helper)"
    label: "One hundred plus the plan percentage, as cents"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_sep_10000, person.h_sep_part]}
  - id: person.h_sep_s21_sep
    printed: "(helper)"
    label: "SEP maximum deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_s7, person.sep_s8]}
  - id: person.h_simple_base_limit
    printed: "(helper)"
    label: "SIMPLE IRA salary reduction limit"
    type: NonNegDollars
    expr: {op: param, ref: ret.simple_limit}
  - id: person.h_simple_catchup
    printed: "(helper)"
    label: "SIMPLE IRA catch-up limit"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: simple_catchup, keys: [person.simple_age]}
  - id: person.h_simple_deferral_limit
    printed: "(helper)"
    label: "SIMPLE IRA salary reduction limit plus catch-up"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_simple_base_limit, person.h_simple_catchup]}
  - id: person.h_simple_deferral_capped
    printed: "(helper)"
    label: "SIMPLE IRA salary reduction contributions capped"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.simple_deferral, person.h_simple_deferral_limit]}
  - id: person.h_simple_total
    printed: "(helper)"
    label: "SIMPLE IRA total contributions"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_simple_deferral_capped, person.simple_employer]}
  - id: person.h_simple_deduction
    printed: "(helper)"
    label: "SIMPLE IRA deductible contribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.h_simple_total, person.se_line6]}
  - id: person.h_s16_sep
    printed: "(helper)"
    label: "SEP contribution actually deductible"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.sep_contrib, person.sep_s21]}
  - id: person.h_educator_cap
    printed: "(helper)"
    label: "Educator expenses capped at $300"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, {param: s1.educator_max}]}
  - id: person.h_edu_adj
    printed: "(helper)"
    label: "Total adjustments to qualified education expenses"
    type: NonNegDollars
    expr: {op: sum, of: [person.edu_a2025, person.edu_a2026, person.edu_refunds]}
  - id: person.h_sav_w2_listed
    printed: "(helper)"
    label: "Saver’s credit elective deferrals from Forms W-2"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.sav_listed}
  - id: person.h_ira_se_ded
    printed: "(helper)"
    label: "Self-employment tax and retirement plan deductions"
    type: NonNegDollars
    expr: {op: sum, of: [person.se_line13, person.s16]}
  - id: person.h_se_line3
    printed: "(helper)"
    label: "Schedule SE line 3"
    type: Dollars
    expr: {op: copy, from: person.sc_total}
  - id: person.h_se_line3_pos
    printed: "(helper)"
    label: "Schedule SE line 3 is positive"
    type: Bool
    expr: {op: test, gt: [person.h_se_line3, {const: 0}]}
  - id: person.h_se_line4a_calc
    printed: "(helper)"
    label: "92.35% of positive Schedule SE line 3"
    type: Dollars
    expr: {op: multiply_rate, amount: person.h_se_line3, rate: {param: se.rate_9235}}
  - id: person.h_se_line4a
    printed: "(helper)"
    label: "Schedule SE line 4a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: person.h_se_line3_pos, then: person.h_se_line4a_calc}
        - {guard: {op: test, eq: [person.h_se_line3_pos, {const: false}]}, then: person.h_se_line3}
  - id: person.h_se_line4c_raw
    printed: "(helper)"
    label: "Schedule SE line 4c before the $400 floor"
    type: Dollars
    expr: {op: sum, of: [person.h_se_line4a, person.zero]}
  - id: person.h_se_line6_raw
    printed: "(helper)"
    label: "Schedule SE line 6 before the $400 test"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_se_line4c_raw, take: {const: 0}}
  - id: person.h_se_owes
    printed: "(helper)"
    label: "Self-employment tax applies"
    type: Bool
    expr: {op: test, ge: [person.h_se_line4c_raw, {param: se.floor}]}
  - id: person.h_se_line9
    printed: "(helper)"
    label: "Schedule SE line 9"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_ss_base, take: person.wages}
  - id: person.h_se_small
    printed: "(helper)"
    label: "Smaller of Schedule SE line 6 or line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.se_line6, person.h_se_line9]}
  - id: person.h_se_line10
    printed: "(helper)"
    label: "Schedule SE line 10"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_se_small, rate: {param: se.rate_124}}
  - id: person.h_se_line11
    printed: "(helper)"
    label: "Schedule SE line 11"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.se_line6, rate: {param: se.rate_029}}
  - id: person.h_se_line12_raw
    printed: "(helper)"
    label: "Schedule SE line 12"
    type: NonNegDollars
    expr: {op: sum, of: [person.h_se_line10, person.h_se_line11]}
  - id: person.h_positive_profits_sum
    printed: "(helper)"
    label: "Sum of positive Schedule C net profits"
    type: Dollars
    expr:
      op: sum_over
      collection: sc
      field: sc.line31
      where: {op: test, gt: [sc.line31, {const: 0}]}
  - id: person.h_x_subject
    printed: "(helper)"
    label: "Early distributions subject to additional tax"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l1, take: person.x_l2_all}
  - id: person.h_x_s_subject
    printed: "(helper)"
    label: "SIMPLE IRA early distributions subject to additional tax"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.x_l1_s, take: person.x_l2_s}
  - id: person.h_x_base_tax
    printed: "(helper)"
    label: "10% additional tax on early distributions"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_x_subject, rate: {param: f5329.early_rate}}
  - id: person.h_x_simple25
    printed: "(helper)"
    label: "25% tax on SIMPLE IRA early distributions"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_x_s_subject, rate: {param: f5329.simple_rate}}
  - id: person.h_x_simple10
    printed: "(helper)"
    label: "10% tax on SIMPLE IRA early distributions"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: person.h_x_s_subject, rate: {param: f5329.early_rate}}
  - id: person.h_x_extra
    printed: "(helper)"
    label: "Extra 15% SIMPLE IRA early distribution tax"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.h_x_simple25, take: person.h_x_simple10}
  - id: person.h_x_e09
    printed: "(helper)"
    label: "Exception 09 first-home amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e09}
  - id: person.h_x_e19
    printed: "(helper)"
    label: "Exception 19 birth or adoption amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e19}
  - id: person.h_x_e22
    printed: "(helper)"
    label: "Exception 22 domestic abuse amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e22}
  - id: person.h_x_e23
    printed: "(helper)"
    label: "Exception 23 emergency personal expense amount"
    type: NonNegDollars
    expr: {op: sum_over, collection: retirement, field: retirement.l2_e23}
```
